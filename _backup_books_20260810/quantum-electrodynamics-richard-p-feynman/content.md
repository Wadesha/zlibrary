# Quantum Electrodynamics Richard P Feynman Z Library

> 来源文件：pre_Quantum_Electrodynamics_Richard_P_Feynman_Z_Library.txt
> 字符数（约）：259223
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

ADVANCEBODO K CLASSICS David Pines, Series Editor Anderson, P. W., Baric Notions of Condensed Matter Physics Bethe H. and Jackiw, R., Intermediate Quantum Mechanics, Third Edition Feynman, R., Photon-Hadron Interactions Feynman, R., Quantum Electrodynamics Feynman, R., Statistical Mechanics Feynman, R., The Theory of Fundamental Processes Norieres, P., Theory of Interacting Fermi System Pines, D., The Many-Body Problem Quigg, C., Gauge Theories of the Strong, Weak, and Electromagnetic Interactions RICHARD FEYNMAN late, California Institute of Technology Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book and Perseus Publishing was aware of a trademark claim, the designations have been printed in initial capital letters.

retrieval system, or transmitted, in any form or by any means, electronic, mechan- ical, photocopying, recording, or otherwise, without the prior written permission of the publisher. Printed in the United States of America.

Westview Press is a member of the Perseus Books Group Cover design by Suzanne Heiser Editor's Foreword Addison-Wesley's Frontiers in Physics series has, since 1961, made it possible for leading physicists to communicate in coherent fashion their views of recent developments in the most exciting and active fields of physics-without having to devote the time and energy required to prepare a formal review or monograph. Indeed, throughout its nearly forty-year existence, the series has emphasized informality in both style and content, as well as pedagogical clar- ity. Over time, it was expected that these informal accounts would be replaced by more formal counterparts-textbooks or monographs-as the cutting-edge topics they treated gradually became integrated into the body of physics knowl- edge and reader interest dwindled. However, this has not proven to be the case for a number of the volumes in the series: Many works have remained in print on an on-demand basis, while others have such intrinsic value that the physics community has urged us to extend their life span.

The Advanced Book Classics series has been designed to meet this demand. It will keep in print those volumes in Frontiers in Physics or its sister series, Lecture Notes and Supplements in Physics, that continue to provide a unique account of a topic of lasting interest. And through a sizable printing, these classics will be made available at a comparatively modest cost to the reader.

These lecture notes on Richard Feynman's Caltech course on Quantum Electrodynamics were first published in 1961, as part of the first group of lec- ture note reprint volumes to be included in the Frontiers in Physics series. As is the case with all of the Feynman lecture note volumes, the presentation in this work reflects his deep physical insight, the freshness and originality of his approach to quantum electrodynamics, and the overall pedagogical wizardry of Richard Feynman. Taken together with the reprints included here of vi EDITOR'S FOREWORD Feynman's seminal papers on the space-time approach to quantum electro- dynamics and the theory of positrons, the lecture notes provide beginning students and experienced researchers alike with an invaluable introduction to quantum electrodynamics and to Feynman's highly original approach to the topic.

David Pines Urbana, Illinois December 1997 Preface The text material herein constitutes notes on the third of a three-semester course in quantum mechanics given at the California Institute of Technology in 1953. Actually, some questions involving the interaction of light and mat- ter were discussed during the preceding semester. These are also included, as the first six lectures. The relativistic theory begins in the seventh lecture.

The aim was to present the main results and calculational procedures of quantum electrodynamics in as simple and straightforward a way as possible.

Many of the students working for degrees in experimental physics did not intend to take more advanced graduate courses in theoretical physics. The course was designed with their needs in mind. It was hoped that they would learn how one obtains the various cross sections for photon processes which are so important in the design of high-energy experiments, such as with the synchrotron at Cal Tech. For this reason little attention is given to many aspects of quantum electrodynamics which would be of use for theoretical physicists tackling the more complicated problems of the interaction of pions and nucleons. That is, the relations among the many different formulations of quantum electrodynamics, including operator representations of fields, explic- it discussion of properties of the S matrix, etc., are not included. These were available in a more advanced course in quantum field theory. Nevertheless, this course is complete in itself, in much the way that a course dealing with Newton's laws can be a complete discussion of mechanics in a physical sense although topics such as least action or Hamilton's equations are omitted.

The attempt to teach elementary quantum mechanics and quantum elec- trodynamics together in just one year was an experiment. It was based on the idea that, as new fields of physics are opened up, students must work their way further back, to earlier stages of the educational program. The first two terms were the usual quantum mechanical course using Schiff (McGraw-Hill) as a main reference (omitting Chapters X, XII, XIII, and XIV, relating to quantum electrodynamics). However, in order to ease the transition to the latter part of the course, the theory of propagation and potential scattering was developed in detail in the way outlined in Eqs. 15-3 to 15-5. One other unusual point was made, namely, that the nonrelativistic Pauli equation could be written as on page 6 of the notes.

The experiment was unsuccessful. The total material was too much for one year, and much of the material in these notes is now given after a full year grad- uate course in quantum mechanics.

The notes were originally taken by A. R. Hibbs. They have been edited and corrected by H. T. Yura and E. R. Huggins.

R. R. FEYNMAN Pasadena, California November 1961 The publisher wishes to acknowledge the assistance of the American Physical Society in the preparation of this volume, specifically their permission to reprint the three articles from the Physical Review.

Contents Editor's Foreword Preface Interaction of Light with Matter-Quantum Electrodynamics Discussion of Fermi's method Laws of Quantum electrodynamics Resume of the Principles and Results of Special Relativity Solution of the Maxwell equation in empty space Relativistic particle mechanics Relativistic Wave Equation Units Klein-Gordon, Pauli, and Dirac equations Algebra of the γ matrices Equivalence transformation Relativistic invariance Hamiltonian form of the Dirac equation Nonrelativistic approximation to the Dirac equation Solution of the Dirac equation for a Free Particle Definition of the spin of a moving electron Normalization of the wave functions Methods of obtaining matrix elements Interpretation of negative energy states Potential Problems in Quantum Electrodynamics Pair creation and annihilation Conservation of energy The propagation kernel Use of the kernel K, (2,1)

Transition probability Scattering of an electron from a coulomb potential Calculation of the propagation kernel for a free particle Momentum representation CONTENTS Relativistic Treatment of the Interaction of Particles with Light Radiation from atoms Scattering of gamma rays by atomic electrons Digression on the density of final states Compton radiation Two-photon pair annihilation Positron annihilation from rest Bremsstrahlung Pair production A method of summing matrix elements over spin states Effects of screening of the coulomb field in atoms Interaction of Several Electrons Derivation of the "rules" of quantum electrodynamics Electron-electron scattering Discussion and Interpretation of Various "Correction" Terms Electron-electron interaction Electron-positron interaction Positronium Two-photon exchange between electrons and/or positrons Self-energy of the electron Method of integration of integrals appearing in quantum electrodynamics Self-energy integral with an external potential Scattering in an external potential Resolution of the fictitious "infrared catastrophe"

Another approach to the infrared difficulty Effect on an atomic electron Closed-loop processes, vacuum polarization Scattering of light by a potential Pauli Principle and the Dirac Equation Reprints Summary of Numerical Factors for Transition Probabilities, Phys. Rev., 84, 123 (1951)

The Theory of Positrons. Phys. Rev., 76, 749-759 (1949)

Space-Time Approach to Quantum Electrodynamics.

Phys. Rev., 76, 169-189 (1949)

This page intentionally left blank Interaction of Light with Matter-Quantum Electrodynamics The theory of interaction of light with matter is called quantum electro- dynamics. The subject is made to appear more difficult than it actually is by the very many equivalent methods by which it may be formulated. One of the simplest is that of Fermi. We shall take another starting point by just postulating for the emission or absorption of photons. In this form it is most immediately applicable.

Suppose all the atoms of the universe are in a box. Classically the box may be treated as having natural modes describable in terms of a distribu- tion of harmonic oscillators with coupling between the oscillators and matter.

The transition to quantum electrodynamics involves merely the assump- tion that the oscillators are quantum mechanical instead of classical. They then have energies (a + 1/2)ħω, a = 0, 1, ..., with zero-point energy 1/2ħω.

The box is considered to be full of photons with a distribution of energies ħω. The interaction of photons with matter causes the number of photons photons of n to increase by Δl (emission or absorption).

Waves in a box can be represented as plane radiating waves, spherical waves, or plane running waves exp(iK·X). One can say there is an instan- taneous Coulomb interaction e2/rij between all charges plus transverse waves only. Then the Coulomb forces may be put into the Schrödinger equa- tion directly. Other formal means of expression are in Hamiltonian form, field operators, etc.

Fermi's technique leads to an infinite self-energy term e2/rii. It is poa- sible to eliminate this term in suitable coordinate systems but then the trans- verse waves contribute an infinity (interpretation more obscure). This mom- entarily was one of the central problems of modern quantum electrodynamics, Second Lecture LAWS OF QUANTUM ELECTRODYNAMICS Without justification at this time the "laws of quantum electrodynamics"

will be stated as follows:

## 1. The amplitude that an atomic system will absorb a photon during the

process of transition from one state to another is exactly the same as the amplitude that the same transition will be made under the influence of a po- tential equal to that of a classical electromagnetic wave representing that photon, provided: (a) the classical wave is normalized to represent an en- ergy density equal to h times the probability per cubic centimeter of find- ing the photon; (b) the real classical wave is split into two complex waves e^{-iwt} and e^{+iwt}, and only the e^{-iwt} part is kept; and (c) the potential acts only once in the perturbation; that is, only terms to first order in the electro- magnetic field strength should be retained.

Replacing the word "absorbed" by "emitted" in rule 1 requires only that the wave represented by exp(+iwt) be kept instead of exp(-iwt).

## 2. The number of states available per cubic centimeter of a given polar-

ization is Note this is exactly the same as the number of normal modes per cubic cen- timeter in classical theory.

## 3. Photons obey Bose-Einstein statistics. That is, the states of a col-

lection of identical photons must be symmetric (exchange photons, add ampli- tudes). Also the statistical weight of a state of n identical photons is 1 in- stead of the classical 1/n!

Thus, in general, a photon may be represented by a solution of the classi- cal Maxwell equations if properly normalized.

Although many forms of expression are possible it is most convenient to describe the electromagnetic field in terms of plane waves. A plane wave can always be represented by a vector potential only (scalar potential made zero by suitable gauge transformation). The vector potential representing a real classical wave is taken as

## INTERACTION OF LIGHT WITH MATTER

A = a0 cos (ωt – K·x)

We want the normalization of A to correspond to unit probability per cu- bic centimeter of finding the photon. Therefore the average energy density should be hω.

Now H = (1/c) (∂A/∂t) = (ωa0/c) sin (ωt – K·x)

for a plane wave. Therefore the average energy density is equal to (1/8π)⟨H^2 + E^2⟩ = (1/4π)(ω²a0²/c²) sin²(ωt – K·x)

Setting this equal to hω/2: we find that Thus - - a0 = sqrt[(4πhc/ω) (1/V)] exp[-i(ωt – K·x)] or exp[+i(ωt – K·x)]

Hence we take the amplitude that an atomic system will absorb a photon to be For emission the vector potential is the same except for a positive exponen- tial.

Example: Suppose an atom is in an excited state |i> with energy Ei and makes a transition to a final state |f> with energy Ef. The probability of transition per second is the same as the probability of transition under the influence of a vector potential as exp[-i(ωt – K·x)] representing the emit- ted photon. According to the laws of quantum mechanics (Fermi's golden rule)

Trans. prob./sec = 2π/ℏ |<f(potential)i>|^2 * (density of states)

Density of states = ...

6 QUANTUM ELECTRODYNAMICS The matrix element Ufi = <f(potential)i> is to be computed from pertur- bation theory. This is explained in more detail in the next lecture. First, however, we shall note that more than one choice for the potential may give the same physical results. (This is to justify the possibility of always chos- ing Φ = 0 for our photon.)

Third Lecture The representation of the plane-wave photon by the potentials is essentially a choice of "gauge." The fact that a freedom of choice exists results from the invariance of the Pauli equation to the quantum-mechanical gauge transform.

The quantum-mechanical transformation is a simple extension of the classical, where, if and if χ is any scalar, then the substitutions leave E and B invariant.

In quantum mechanics the additional transformation of the wave function is introduced. The invariance of the Pauli equation is shown as follows. The Pauli equation is

## INTERACTION OF LIGHT WITH MATTER

The partial derivative with respect to time introduces a term (∂χ/∂t)Ψ and this may be included with 4e-χΦ. Therefore the sub- stitutions leave the Pauli equation unchanged.

The vector potential A as defined for a photon enters the Pauli Hamil- tonian as a perturbation potential for a transition from state i to a state f.

Any time-dependent perturbation which can be written results in the matrix element Ufi given by This expression indicates that the perturbation has the same effects as a time- independent perturbation U(x,y,z) between initial and final states whose en- ergies are, respectively, Ei and Ef. As is well known, the most impor- tant contribution will come from the states such that Ef ≈ Ei + ℏω.

Using the previous results, the probability of a transition per second is f See, for example, L. D. Landau and E. M. Lifshitz, "Quantum Meehan- ics: Non-Relativistic Theory," Addison-Wesley, Reading, Massachu- setts, 1958, Sec. 40.

## QUANTUM ELECTRODYNAMICS

To determine Ufi, write Because of the rule that the potential acts only once, which is the same as requiring only first-order terms to enter, the term in A^2 does not en- ter this problem. Making use of A = a0 exp[-i(ωt – K·x)] and the two operator relations where K·a = 0 (which follows from the choice of gauge and the Maxwell equations), we may write This result is exact. It can be simplified by using the so-called "dipole"

approximation. To derive this approximation consider the term (e/2mc) (p·a e^{-i K·x}), which is of the order of the velocity of an electron in the atom, or the current. The exponent can be expanded.

K·x is of the order a0/λc, where a0 = dimension of the atom and λ = wave- length. If a0/λ << 1, all terms of higher orders than the first in a0/λ may be neglected. To complete the dipole approximation, it is also necessary to neglect the last term. This is easily done since the last term may be taken as the order of ℏ(K/mc) = (2πℏc/mc²) * (mv²/2mc²). Although such a term is negligible even this is an overestimate. More correctly,

## INTERACTION OF LIGHT WITH MATTER

(eℏ/2mc)σ·(K × a) e^{+i K·x} may be omitted. Thus the matrix element is A good approximation allows the separation Then to the accuracy of this approximation the integral is ∫ Ψ_f* (a·(K·p)) Ψ_i d vol = 0 since the states are orthogonal.

For the present, the dipole approximation is to be used. Then Ufi = -a0 (e/m) (π·p)fi Using operator algebra, p/m = (i/ℏ)[H, x], so that (π·p)fi = a0[(e^2)/(2π) (e·x)fi dΩ where xfi = ∫ Ψ_f* x Ψ_i d vol. The total probability is obtained by inte- grating Pfi over dΩ, thus Total prob./sec = (a0^2 ω^4)/(2πℏ) (e·xfi)^2 dΩ 10 QUANTUM ELECTRODYNAMICS the term e·xfi is resolved by noting (Fig. 3-1)

|e·xfi| = |xfi| sin θ FIG. 3-1 Substituting for |xfi|: Total prob./sec = (8π^2 e^2 ω^3)/(3ℏc^3) |xfi|^2 Absorption of Light. The amplitude to go from state k to state l in time T (Fig. 4-1) is given from perturbation theory by

## INTERACTION OF LIGHT WITH MATTER

where the time dependence of |k(t)| is indicated by writing Uk(t) = uk e^{-iωt} (In accord with the rules of lecture 2, the argument of the exponential is minus and only terms which are linear in the potential are included.) Using this time dependence and performing the integration, the transition probability is given by This is the probability that a photon of frequency ω traveling in direction (θ, φ) will be absorbed. The dependence on the photon direction is contained in the matrix element ukl. For example, see Eq. (4-1) for the directional dependence in the dipole approximation.

If the incident radiation contains a range of frequencies and directions, that is, suppose n(ω, θ, φ) dω dΩ = probability that a photon is present with fre- quency ω to ω + dω and in solid angle dΩ about the direction (θ, φ)

and the probability of absorption of any photon traveling in the (θ, φ) direc- tion is desired, it is necessary to integrate over all frequencies. This ab- sorption probability is When T is large, the factor sin[(ωlk – ω)T/2]/(ωlk – ω) has an appreciable value only for ω near ωlk, and n(ω, θ, φ) will be substantially constant over the small range in which contributes to the integral so that it may be taken out of the integral. Similarly for ulk, so that Trans. prob. = 2π(ℏ)^{-1} |ulk|^2 n(ωlk, θ, φ) dΩ where 12 QUANTUM ELECTRODYNAMICS This can also be written in terms of the incident intensity (energy crossing a unit area in unit time) by noting that Using the dipole approximation, in which the total probability of absorption (per second) is It is evident that there is a relation between the probability of spontane- ous emission, with accompanying atomic transition from state l to state k, Probability of spontaneous = 2π(ℏ)^{-1} (2πc)^{-3} |ulk|^2 ω^2 dΩ emission/sec and the absorption of a photon with accompanying atomic transition from state k to state l, Eq. (4-1), although the initial and final states are re- versed since |ulk|^2 = |kl|u|^2. This relation may be stated most simply in terms of the concept of the probability n(ω, θ, φ) that a particular photon state is occupied. Since there are (2πc)^{-3} ω^2 dω dΩ photon states in frequency range dω and solid angle dΩ, the probability that there is some photon within this range is Expressing the probability of absorption in terms of n(ω, θ, φ), Trans The prob./sec = 2n(~)*lu lk nfw,~,(13)(2ncw)-k~1 2 do

(4-4)

This equation may be interpreted as follows. Since a(n,@,cp) is the probability that a photon state is occupied, the remainder of the terms on the right-hand side must be the probability per second that a photon in that state will be absorbed. Comparing Eq, (4-4) with the rate of spontaneous emission shows that

Prob. /sec of absorption prob. /see of spontaneous emission of a photon into of a photon from a state (per photon in that state) that state

In what follows, it will be shown that Eq. (4-4) is correct even when there is a possibility of more than one photon per state provided n(n,@,$) is taken as the mean number of photons per state.

If the initial state consists of two photons in the same photon state, it will not be possible to distinguish them and the statistical weight of the initial state will be 1/2 ! However, the amplitude for absorption will be twice that for one photon. Taking the statistical weight times the square of the amplitude for this process, the transition probability per second is found to be twice that for only one photon per photon state. When there are three photons per initial photon state and one is absorbed, the following processes (shown on Fig. 4-22) can occur.

Any of the three incident photons may be absorbed and, in addition, there is the possibility that the photons which are not absorbed may be interchanged. The statistical weight of the initial state is 1/3 !, the statistical weight of the final state is 2/2! , and the amplitude for the process is 6. Thus the transition probability is (1/3 !)(1/2 !) (6)^2 = 3 times that if there were one photon in that state. In general, the transition probability for n photons per initial photon state is n times that for a single photon per photon state, so Eq. (4-4) is correct if n(n,@,$) is taken as the mean number of photons per state.

A transition that results in the emission of a photon may be induced by incident radiation. Such a process (involving one incident photon) could be indicated diagrammatically, as in Fig. 4-3.

One photon is incident on the atom and two indistinguishable photons come off. The statistical weight of the final state is 1/2! and the amplitude for the process is 2, so the probability of emission for this process is twice that of spontaneous emission. For n incident photons the statistical weight of the initial state is 1/n!, the statistical weight of the final state is 1/(n + 1)!, and the amplitude for the process is (n + 1) times the amplitude for spontaneous emission. The probability (per second) of emission is then n+1 times the probability of spontaneous emission. The n can be said to account for the induced part of the transition rate, while the 1 is the spontaneous part of the transition rate.

Since the potentials used in computing the transition probability have been normalized to one photon per cubic centimeter and the transition probability depends on the square of the amplitude of the potential, it is clear that when there are n photons per photon state the correct transition probability for absorption would be obtained by normalizing the potential to n photons per cubic centimeter (amplitude times as large). This is the basis for the validity of the so-called semiclassical theory of radiation. In that theory absorption is calculated as resulting from the perturbation by a potential normalized to the actual energy in the field, that is, to energy nEw if there are n photons. The correct transition probability for emission is not obtained this way, however, because it is proportional to n + 1. The error corresponds to omitting the spontaneous part of the transition probability. In the semiclassical theory of radiation, the spontaneous part of the emission probability is arrived at by general arguments, including the fact that its inclusion leads to the observed Planck distribution formula. Einstein first deduced these relationships by semiclassical reasoning.

Selection Rules in the Dipole Approximation. In the dipole approximation the appropriate matrix element is

The matrix elements components of Xif are xif, yif, zif and selection rules are determined by the conditions that cause this matrix element to vanish. For example, if in hydrogen the initial and final states are S states (spherically symmetrical), Xif = 0 and transitions between these states are "forbidden." For transitions from P to S states, however, Xif ≠ 0 and they are allowed.

In general, for single electron transitions, the selection rule is Δl = ±1.

This may be seen from the fact that the coordinates x, y, and z are essentially the Legendre polynomial P1. If the orbital angular momentum of the initial state is l, the wave function contains Pl. But

Hence for the matrix element not to vanish, the angular momentum of the final state must be l ± 1, so that its wave function will contain either Pl+1 or Pl-1.

For a complex atom (more than one electron), the Hamiltonian is

H = Σ(1/2m) P_i^2 - (e/c)A(x_i p_i) + Coulomb terms

The transition probability is proportional to |p_fi|^2 = |Σ(p_i)_fi|^2 where the sum is over all the electrons of the atom. As has been shown, (p_i)_fi is the same, up to a constant, as (x_i)_fi, and the transition probability is proportional to

In particular, for two electrons, the matrix element is

x1 + x2 behaves under rotation of coordinates similarly to the wave function of some "object" with unit angular momentum. If the "object" and the atom in the initial state do not interact, then the product (x1 + x2) Ψ_i (x1,x2) can be formally regarded as the wave function of a system (atom + object) having possible values of Ji + 1, Ji, and Ji - 1 for total angular momentum. Therefore the matrix element is nonzero only Transition and their Selection Rules Electric dipole Magnetic quadrupole octupole Actually all the implicit selection rules for ΔJ, which become numerous for the higher multipole orders, can be expressed explicitly by writing the selection rule as where ℓ is the multipole order or ℓ is the vector change in angular momentum, INTERACTION OF LIGHT WITH MATTER (1)

It turns out that in so-called parity-favored transitions, wherein the product of the initial and final parities is (-1)^ℓ and the lowest possible multipole order is |J_i - J_f|, the transition probabilities for multipole types contained within the dashed vertical lines in Table 5-1 are roughly equal. In parity-unfavored transitions, where the parity product is (-1)^ℓ and the lowest multipole order is |J_i - J_f| + 1, this may not be true.

Equilibrium of radiation. If a system is in equilibrium, the relative number of atoms per cubic centimeter in two states, say i and k, is given by according to statistical mechanics, when the energies differ by E_m. Since the system is in equilibrium, the number of atoms going from state k to i per unit time by absorption of photons must equal the number going from i to k by emission. If n_ν photons of frequency ν are present per cubic centimeter, then probabilities of absorption are proportional to n_ν, and the probability of emission is proportional to n_ν + 1. Thus This is thus Planck black-body distribution law.

The scattering of light. We discuss here the phenomena of an incident photon being scattered by an atom into a new direction (and possibly energy) (see Fig. 6-1). This may be considered as the absorption of the incoming photon and the emission of a new photon by the atom. The two photons taking part in the phenomenon are represented by the vector potentials.

The number to be determined is the probability that an atom initially in state k will be left in state i by the action of this perturbation A_μ A^μ. The time T. This probability can be computed just as any transition probability with the use of A_ik, where the dipole approximation is to be employed and where spin parts are neglected.

In each integral defining A_ik, each of the two vector potentials must appear once and only once. Thus, in the first integral the term p · A_2 of A will not appear in U_ik. The product A · A = (A_1 + A_2)(A_1 + A_2) will contribute only its cross-product term 2A_1 · A_2. The second integral will have no contribution from A · A, but will be the sum of two terms. The first term contains a U_ik based on p · A_2 and a U_ik based on p · A_1. The second has U_ik based on p · A_1 and U_ik on p · A_2. The line sequences resulting in these two terms can be represented schematically as shown in Fig. 6-2.

The integral resulting from the first term we shall now be developed in detail.

Then the resulting integral is

## INTERACTION OF LIGHT WITH MATTER

first / atom FIG. 6-2 exp[-i(E_i/ℏ)t'] dt' - iω exp[-i(E_k/ℏ)t'] dt, The integral is similar to the integrals considered previously with regard to transition probabilities, and the sum becomes where δ = (E_i + ℏω - E_k), and the phase angle α is independent of ω.

A term with the denominator given by (E_k - E_i)(E_i + ℏω - E_k) has been neglected, since previous results show that only energies such that E_i + ℏω ≈ E_k are important. The final result can be written where |M|^2 is determined from A_ik by integrating over ω_2 and averaging over ε_2. Then the complete expression for the cross section σ is 22 QUANTUM ELECTRODYNAMICS The first term under the summation comes from the "first term" previously referred to and the second from the "second term." The last term in the absolute brackets comes from A · A.

If i ≠ k, the scattering is incoherent, and the result is called the "Raman effect." If i = k, the scattering is coherent.

Further, note that if all the atoms are in the ground state and i ≠ k, then the energy of the atom can only increase and the frequency of the light can only decrease. This gives rise to "Stokes lines". The opposite effect gives "anti-Stokes lines".

Suppose ω_0 = (coherent scattering) but further E_w1 is very nearly equal to E_k - E_i, where E_i is some possible energy level of the atom. Then one term in the sum over n becomes extremely large and dominates the remainder. The result is called "resonance scattering." If it is plotted against ω, then at such values of ω the cross section has a sharp maximum (see Fig. 6-3).

FIG. 6-3 The index of refraction of a gas can be obtained by our scattering formula. It can be obtained, as for other types of scattering, by considering the light scattered in the forward direction.

Self-energy. Another phenomenon that must be considered in quantum electrodynamics is the possibility of an atom emitting a photon and reabsorbing the same photon. This affects the diagonal element A_kk. Its effect is equivalent to a shift of energy of the level, the effect being where ε is the direction of polarization. This integral diverges. A more exact relativistic calculation also gives a divergent integral. This means that our formulation of electromagnetic effects is not really a completely satisfactory theory. The modifications required to avoid this difficulty of the infinite self-energy will be discussed later. The net result is a very small shift ΔE in position of energy levels. This shift has been observed by Lamb and Retherford.

the Principles and Results of Special Relativity The principle of relativity is the principle that all physical phenomena would appear to be exactly the same if all the objects concerned were moving uniformly together at velocity V; that is, no experiments made entirely inside of a closed spaceship moving uniformly with velocity v (relative to the center of gravity of the matter in the universe, for example) can determine absolute velocity. The principle has been verified experimentally. Newton's laws satisfy this principle; for they are unchanged when subject to a Galilean transformation, because they involve only second derivatives. The Maxwell equations are changed, however, when subjected to this transformation, and early workers in this field attempted to make an absolute determination of velocity of the earth using this feature (Michelson-Morley experiment). Failure to detect any effects of this type ultimately led to Einstein's postulate that the Maxwell equations are of the same form in any coordinate system; and, in particular, that the velocity of light is the same in all coordinate systems. The transformation between coordinate systems which leaves the Maxwell equations invariant is the Lorentz transformation: where now u = v/c. Henceforth we shall use time units so that the speed of light c is unity. The latter form is written to demonstrate the analogy with rotation of axes, X' = x cos θ - y sin θ y' = -x sin θ + y cos θ Successive transformations v_1 and v_2, or u_1 and u_2, add in the sense that a single transformation v_3 or u_3 will give the same final system if Einstein postulated [theory of special relativity] that the Newton laws must be modified in such a way that they, too, are unchanged in form under a Lorentz transformation.

An interesting consequence of the Lorentz transformation is that clocks appear to run slower in moving systems; that is called time dilation. In transforming from one coordinate system to another it is convenient to use tensor analysis. To this end, a four-vector will be defined as a set of four quantities that transforms in the same way as x, y, z and ct. The subscript μ will be used to designate which of the four components is being considered; for example, The following quantities are four-vectors: V_μ = (∂/∂x, ∂/∂y, ∂/∂z, ∂/∂(ct)) - four-dimensional gradient j_μ = (j_x, j_y, j_z, cρ) - current (and charge) density A_μ = (A, V) - vector (and scalar) potential p_μ = (p_x, p_y, p_z, E) - momentum and total energy $ The energy E, here, is the total energy including the rest energy mc^2.

## SPECIAL RELATIVITY

An invariant is a quantity that does not change under a Lorentz transformation. If a_μ and b_μ are two four-vectors, the "product"

a_μ b_μ = a_0 b_0 - a_1 b_1 - a_2 b_2 - a_3 b_3 is an invariant. To avoid writing the summation symbol, the following summation convention will be used. When the same index occurs twice, sum over it, placing minus in front of first, second, and third components. The Lorentz invariance of the continuity equation is easily demonstrated by writing it as a "4-product" of four-vectors V_μ and j_μ: V_μ j_μ = 0.

Conservation of charge in all systems if it is conserved in one system is a consequence of the invariance of this "product," the four-dimensional divergence V · j. Another invariant is p_μ p_μ = p·p = E^2 - p_x^2 - p_y^2 - p_z^2 = E^2 - p^2 = m^2.

(E = total energy, m = rest mass, mc^2 = rest energy, p = momentum.) Thus, It is also interesting to note that the phase of a free particle wave function exp[-(i/ℏ)(Et - p·x)] is invariant since The invariance of p_μ p_μ can be used to facilitate converting laboratory energies to center-of-mass energies (Fig. 6-4) in the following way (consider identical particles, for simplicity): x-no-trixy~ sttltiona xy particle padicle bboratarjr system Center-of-mass system

## QUANTUM ELECTRODYNAMICS

but and The equations of electromagnetism B = ∇ × A and E = (i/c)(∂A/∂t) - ∇Φ, are easily written in tensor notation, where use is made of the fact that Φ is the fourth component of the four-vector potential A_μ. From the foregoing it can be seen that B_x, B_y, B_z, E_x, E_y, and E_z are the components of a second-rank tensor: This tensor is antisymmetric (F_μν = -F_νμ) and the diagonal terms (μ = ν)

are zero; thus there are only six independent components (three components of E and three components of B) instead of sixteen.

The Maxwell equations ∇ × B = 4πJ + (1/c)(∂E/∂t) and ∇·E = 4πρ are written lel Q

## QUANTUM ELECTRODYNAMICS

SOLUTION OF THE MAXWELL EQUATIONS IN EMPTY SPACE In empty space the plane wave solution of the wave equation where E, and k, are constant vectors, and k, is subject to the condition that This may be seen from the fact that V, operating on e-ik·x has the effect of multiplying by ik, (V, does not operate on E since the coordinates are rectangular). Thus, Note that in these operations ∂_μ A_ν actually forms a second-rank tensor, ∂_μ (∂_ν A_λ) forms a third-rank tensor, and then contraction on the index ν yields a first-rank tensor or vector.

The k_μ is the propagation vector with components and the condition k_μk^μ = 0 means Problem: Show that the Lorentz condition implies that k_μ E^μ = 0.

When working in three dimensions it is customary to take the polarization vector ε such that k · ε = 0 and to let the scalar potential φ = 0. But this is not a unique condition; that is, it is not relativistically invariant and will be true only in a one-coordinate system. This would seem to be a para- dox attaching some uniqueness to the system in which k · ε = 0, a situation incompatible with relativity theory. The "paradox" however is resolved by the fact that one can always make a so-called gauge transformation, which leaves the field F_{μν} unaltered but which does change ε. Therefore, choosing k · ε = 0 in a particular system amounts to selecting a certain gauge.

The gauge transformation, Eq. (1-31), is where χ is a scalar. But ∂_μ A^μ = 0, the Lorentz condition, Eq. (7-4), will still hold if This equation has a solution χ = C exp(ik · x). So where C is an arbitrary constant. Therefore, ε_μ' = ε_μ - ik_μ (C)

is the new polarization vector obtained by gauge transformation. In ordinary notation k · ε' = k · ε - ik · iC = k · ε + k^2 C = k · ε since, no matter what coordinate system is used, k · ε can be made to vanish by choice of the constant C.

Clearly the field is left unchanged by a gauge transformation for 30 QUANTUM ELECTRODYNAMICS the ∂_μ A_ν - ∂_ν A_μ because the order of differentiations is immaterial.

The components of ordinary velocity do not transform in such a manner that they form the components of a four-vector. But another quantity u_μ = dx_μ / dτ where dx_μ = dt, dx, dy, dz is an element of path of the particle and dτ is the proper time defined by (dτ)^2 = dt^2 - (dx^2 + dy^2 + dz^2)

is a four-vector and is called the four-velocity. By dividing by dt^2 one obtains the relation between proper time and local time to be dτ = dt √(1 - v^2)

The components of ordinary velocity are related as follows: u_1 = v_x / √(1 - v^2), etc.

It is evident that u_μ u^μ = 1, for u_μ u^μ = 1/(1 - v^2) - v^2/(1 - v^2) = 1.

The four-momentum is defined as p_μ = m u_μ = m/(√(1 - v^2), m v_x/√(1 - v^2), m v_y/√(1 - v^2), m v_z/√(1 - v^2))

Note that p_0 = m/√(1 - v^2) is the total energy E, so that in ordinary nota- tion the momentum P is given by

## SPECIAL RELATIVITY

P = m v / √(1 - v^2)

where v is the ordinary velocity.

Like the velocity, the components of ordinary force defined by d/dt (mo- mentum) cannot form the components of a four-vector. But the quantity f_μ = dp_μ / dτ does form a four-vector with the components f = dp/dt f_4 = dE/dt where F is the ordinary force. The fourth component is f_4 = power = rate of change of energy.

This is seen from the fact that m/√(1 - v^2) is the total energy and also from the ordinary identity F · v = d/dt (½ m v^2)

Thus the relativistic analogue of the Newton equation is d/dτ (p_μ) = f_μ = m d^2 x_μ / dτ^2 The ordinary Lorentz force is F = e(E + v × B)

and the rate of change of energy is dE/dt = e E · v Then from the preceding definition of four-force, f_μ = e u^ν F_{μν} and f_4 = e u^ν F_{4ν} = e (u_1 F_{41} + u_2 F_{42} + u_3 F_{43}) = e (v_x E_x + v_y E_y + v_z E_z) = e v · E.

## QUANTUM ELECTRODYNAMICS

Problem: Show that the expressions just given for f and f_4 are equivalent to f_μ = e u^ν F_{μν} so that the relativistic analogue of the Newton equation becomes m d^2 x_μ / dτ^2 = e (dx_ν / dτ) F_{μν} (8-23)

Also show that this implies d/dτ [(dx_μ / dτ)^2] = 0 In ordinary terms the equation of motion is d/dt (m v) = e (E + v × B)

It can be shown by direct application of the Lagrange equations d/dt (∂L/∂v) - (∂L/∂x) = 0 that the Lagrangian L = -m c^2 √(1 - v^2/c^2) - e φ + e v · A leads to these equations of motion. Also the momenta conjugate to x is given by ∂L/∂v or P = m v / √(1 - v^2/c^2) + e A The corresponding Hamiltonian is H = e φ + [(P - e A)^2 + m^2]^{1/2} (8-6)

which satisfies (H - e φ)^2 - (P - e A)^2 = m^2. It is difficult to convert the Hamiltonian idea to a covariant or four-dimensional formulation. But the principle of least action, which states that the action S = ∫ L dα shall be a minimum, will lead to the relativistic form of the equations of motion directly when expressed as

## SPECIAL RELATIVITY

S = -m c ∫ ds = -m c ∫ √(dx_μ dx^μ)

Note that by definition (ds/dα)^2 = (dx_μ / dα)(dx^μ / dα)

It is interesting that one may also define S = ∫ p_μ dx^μ = ∫ m u_μ dx^μ = m ∫ u_μ u^μ ds = m ∫ ds which leads to the same result as for S in the foregoing.

Problems: (1) Show that the Lagrangian, Eq. (8-5), leads to the equations of motion, Eq. (8-4), and that the corresponding Hamiltonian is Eq. (8-6). Also find the expression for H. (2) Show that δS = 0 (va- riation of S), where S is the action just given, leads to the same equa- tions.

Relativistic Wave Equation The following convention will be used hereafter. We define the units of mass and time and length such that Table 9-1 (top of page 39) is given as a useful reference for conversion to cgs units.

The following numerical values are useful: m_p = mass of proton = 1836.1 m_e = 938.2 Mev Mass unit of atomic weights = 931.2 Mev m_H = mass of hydrogen atom = 1.00815 mass units m_n = mass of neutron = 784 kev + m_H kT = 1 ev when T = 11,605 K.

N_A = Avogadro's number = 6.025 x 10^23 N_F e = 96,520 coulombs According to relativistic classical mechanics, the Hamiltonian is given by

## RELATIVISTIC WAVE EQUATION

TABLE 9-1. Notations and Units Present notation | Meaning | Customary notation | Value m | Mass of electron | m_e | — mc^2 | Energy | — | 510.99 kev mc | Momentum | — | 1.855 x 10^{-17} gm cm/sec mc^2/h | Frequency | — | 1.235 x 10^{20} cps mc/h | Wave number | — | 4.121 x 10^{10} cm^{-1} ħ/mc | Compton wavelength/2π | λ_c/2π | 3.8625 x 10^{-11} cm ħ | Time | ℏ | 6.582 x 10^{-22} sec e^2 | Fine-structure constant | α (dimensionless) | 1/137.04 e^2/mc^2 | Classical radius of the electron | r_e | 2.8179 x 10^{-13} cm ħ^2/(m e^2) | Bohr radius | a_0 | 5.2917 x 10^{-8} cm If the quantum-mechanical operator -iħ∇ is used for p, the operation determined by the square root is undefined. Thus the relativistic quantum- mechanical Hamiltonian has not been obtained directly from the classical equation, Eq. (9-1). However, it is possible to define the square of the operator and to write (E - e φ)^2 = c^2 (p - e A)^2 + m^2 c^4 where the square of an operator is evaluated by ordinary operator algebra.

This equation was first discovered by Schrödinger as a possible relativistic equation. It is usually referred to as the Klein-Gordon equation. In relativistic notation it is (∂_μ ∂^μ + m^2) ψ = 0 This equation does not allow for "spin" and therefore fails to describe the fine structure of the hydrogen spectrum. It is proposed now for applica- tion to the π meson, a particle with no spin. To demonstrate its application to the hydrogen atom, let A = 0 and φ = -Ze/r, then let ψ = ψ(r) exp(-iEt/ħ).

Then the equation is [∇^2 + (E + Ze^2/r)^2 / ħ^2 - m^2 c^4 / ħ^2] ψ = 0 Let E = m c^2 + W, where m is the electron mass and substituting V = Ze^2/r, [∇^2 + (2m/ħ^2)(W - V) + (1/ħ^2)(2m c^2 (W - V) + (W - V)^2)] ψ = 0 Neglecting the term on the right in comparison with the first term on the left gives the ordinary Schrödinger equation. By using (W - V)^2/2m c^2 as a perturbation potential, the student should obtain the fine-structure split-ting for hydrogen and compare with the correct values.

Exercise: For the Klein-Gordon equation, let ρ = i (ψ* ∂ψ/∂t - ψ ∂ψ*/∂t) = charge density j = -i ħ (ψ* ∇ψ - ψ ∇ψ*) = current density Then show (∂ρ/∂t + ∇·j) = 0 and show ∂_μ j^μ = 0.

The Klein-Gordon equation leads to a result that seemed so unreasonable at the time it was first brought to light that it was considered a valid basis for rejecting the equation. This result is the possibility of negative energy states. To see that the Klein-Gordon equation predicts such energy states, consider the equation for a free particle, which can be written (□^2 + m^2) ψ = 0 where □^2 is the d'Alembertian operator. In four-vector notation, this e- quation has the solution ψ = A exp (-i p_μ x^μ) , where p_μ p^μ = m^2. Then, since p_0 = E/c, there results E^2 = p^2 c^2 + m^2 c^4 The apparent impossibility of negative values of E led Dirac to the de- velopment of a new relativistic wave equation. The Dirac equation proves to be correct in predicting the energy levels of the hydrogen atom and is the accepted description of the electron. However, contrary to Dirac's original

## RELATIVISTIC WAVE EQUATION

intent, his equation also leads to the existence of negative energy levels, which by now have been satisfactorily interpreted. Modes of the Klein- Gordon equation can also be interpreted.

Exercise: Show if ψ_1 = exp(-iEt)φ(x ,y,z) is a solution of the Klein- Gordon equation with constant A and V, then ψ_2 = exp(+i Et)φ is a so- lution with -A and -V, replacing A and V. This indicates one manner in which "negative" energy solutions can be interpreted. It is the solution for a particle of opposite charge to the electron, but the same mass.

Instead of following the original method in the development of the Dirac equation, a different approach will be used here. The Klein-Gordon equation is actually the four-vector form of the Schrödinger equation. With a similar point of view, the Dirac equation can be developed as the four-vector form of the Pauli equation.

In following such a procedure, the terms involving "spin" will be included in the relativistic equation. The idea of spin was first introduced by Pauli, but it was not at first clear why the magnetic moment of the electron had to be taken as e ħ/2m c. This value did seem to follow naturally from the Dirac equation, and it is often stated that only the Dirac equation produces as a consequence the correct value of the electron magnetic moment. However, this is not true, as further work on the Pauli equation showed that the same value follows just as naturally, i.e., as the value that produces the greatest simplification. Because spin is present in the Dirac equation, and absent in the Klein-Gordon, and because the Klein-Gordon equation was thought to be invalid, it is often stated that spin is a relativistic requirement. This is in- correct, since the Klein-Gordon equation is a valid relativistic equation for spinless particles.

Thus the Schrödinger equation is i ħ ∂ψ/∂t = H ψ where H = p^2/2m + V and the Klein Gordon equation is Now the Pauli equation is also H* = E*, where Thus  -iV appearing in the Schrodinger equation has been replaced by [σ · (-i∇ - eA) ]/2ℏ. Then a possible relativistic version of the Pauli equation, in analogy to the Klein-Gordon equation, might be Actually, this is incorrect, but a very similar form (with m replaced by i(ℏ/∂t)) is correct, namely, This is one form of the Dirac equation.

The wave function ψ on which the operations are being carried out is actually a matrix.

A form closer to that originally proposed by Dirac may be obtained as follows. For convenience, write Now let the function X be defined by (γ₄ + γ·σ)φ = χ.

Then Eq. (9-5) implies (γ₄ ∂/∂t + γ·r)χ = mψ. This pair of equations can be rewritten (only to arrive at a particular conventional form) by writing Then adding and subtracting the pair of equations for φ, χ, there results These two equations may be written as one by employing a particular convention. Define a four-component matrix wave function as where the matrix character of φ and χ has been shown explicitly, i.e., actually Then, if the auxiliary definitions are made, (Note: An example of the latter definition is 0 0 0 0 0 0 0 0 0 σ_x = ( 1 0 )

( 0 1 )

since σ_x, σ_y and σ_z are similar.) The two equations in φ and χ can be written as one in the form which is actually four equations in four wave functions. Then using four-vector notation, the Dirac equation is that is, show γ_1² = γ_2² = γ_3² = γ_4² = -1 A similar form for the Dirac equation can be obtained, by a different argument, by comparison to the Klein-Gordon equation, with H = i(ℏ/∂t) = i∂_μ, and with eφ = eA₄, Eq. (9-3) becomes in four-vector notation. Using a similar notation in the Pauli equation, Eq. (9-4), but also using α = γ and setting Q = γ₄ arbitrarily (to complete the definition of a four-vector form of Q), Eq. (9-4) can be written in a form similar to Eq. (9-9a), This should be compared to Eq. (9-9).

Now the Pauli equation, Eq. (9-4), differs from the Schrodinger equation in the replacement of the three-dimensional scalar product (p·e)² by the square of a single quantity (p·e)². Analogously one might guess that the four-vector product (p_μ, eA_μ) in Eq. (9-10) must be replaced by the square of a single quantity γ_μ(p_μ - eA_μ), where we must invent four matrices γ_μ in four dimensions in analogy to the three matrices α in three dimensions. The resulting equation, is essentially equivalent to Eq. (9-9) (operate on both sides of Eq. (9-9) by γ_μ(i∇_μ - eA_μ) and use Eq. (9-9) again to simplify the right-hand side).

Exercise: Show that Eq. (13-11) is equivalent to (i∇_μ - eA_μ)(i∇^μ - eA^μ)ψ = m²ψ FORM OF THE γ MATRICES In the preceding lecture the Dirac equation, γ_μ(i∇_μ - eA_μ)ψ = mψ was obtained, together with a special representation for the γ_μ's, where each element in these four-by-four matrices is another two-by-two matrix, that is, The best way to define the γ's, however, is to give their commutation relationships, since this is all that is important in their use. The commutation relationships do not determine a unique representation for the γ_μ's, and the foregoing is only one of many possible representations. The commutation relationships are or, in a unified notation, Note that with this definition of γ_μ and the rule for forming a scalar product, Other new matrices may arise by forming products of the matrices already defined. For example, the matrices of Eq. (10-5) are products of γ's taken two at a time. The matrices are all independent of γ_1, γ_2, γ_3, γ_4. (They cannot be formed by a linear combination of the latter.) Similarly, products of three matrices, These are the only new products of three. For, if two of the matrices were equal, the product could be reduced, thus γ_1γ_1γ_2 = γ_1(-γ_1γ_2) = -γ_2. The only new product of four that can be formed is given a special name, γ_5. Products of more than four must contain two equal so that they can be reduced, are, therefore, sixteen linearly independent combinations of them may involve sixteen arbitrary constants. This accords with the fact that such a combination can be expressed by a four-by-four matrix. (It is mathematically interesting then that all four-by-four matrices can be expressed in the algebra of the γ's; this is called a Clifford algebra or hypercomplex algebra. A simpler example is that of two-by-two matrices, the so-called algebra of quaternions, which is the algebra of the Pauli spin matrices.)

It is convenient to define another γ matrix, since it occurs frequently: Verify that For later use, it will be convenient to define from which it can be shown that For example, the first may be verified by writing and, moving the second factor to the front, by using the commutation relationships. Doing this with the first term, (a_pγ_p) of the second factor produces since γ_p commutes with itself and anticommutes with γ_q, γ_r, and γ_s. By performing this operation on all terms, one obtains = -iβp + 2(b_p a_p γ_t^2 + b_q a_q γ_y^2 + b_r a_r γ_z^2 + b_s a_s γ_w^2)

= -iβp + 2b·a Exercises: (1) Show that γ_p γ_q + γ_q γ_p = -2δ_{pq} I + 2ε_{pqr} γ_s γ_p γ_q γ_r + γ_r γ_q γ_p = 4ε_{pqr} I γ_p γ_q γ_r γ_s + γ_s γ_r γ_q γ_p = 2(δ_{pr}δ_{qs} - δ_{ps}δ_{qr})

γ_p γ_q γ_r γ_s γ_t + γ_t γ_s γ_r γ_q γ_p = -4(δ_{pr}γ_sγ_t - ...)

(2) Verify by expanding in power series that exp[(a/2) γ_p γ_q] = cosh(a/2) + γ_p γ_q sinh(a/2)

exp[(ia/2) γ_p γ_q] = cos(a/2) + γ_p γ_q sin(a/2)

(3) Show that Suppose another representation for the γ matrices is obtained which satisfies the same commutation relationships, Eq. (10-3); will the form of the Dirac equation, Eq. (10-1), remain the same? To answer this question, make the following transformation of the wave function ψ' = S^{-1}ψ, where S is a constant matrix which is assumed to have an inverse S^{-1} (S^{-1}S = I). The Dirac equation becomes The ∂_μ and S commute, since ∂_μ is a differential operator plus a function of position, so this equation may be written Multiplying by the inverse matrix, where γ'_μ = S^{-1} γ_μ S. The transformation γ'_μ = S^{-1} γ_μ S is called an equivalence transformation, and it is easily verified that the new γ's satisfy the commutation relationships, Eq. (10-3). Products of γ's, transform in exactly the same manner as the γ's, so that equations involving the γ's (the commutation relationships specifically) are the same in the transformed representation. This demonstrates another representation for the γ's, and the Dirac equation is in exactly the same form as the original, Eq. (10-1), and is equivalent in all its results.

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = except p * cr. But a = I, ao the eigenvalues of a! are a l. Hence the eigexlvelocities of .k are ~ts: peed of light. This re~ulits sometimes made plausibb by the ar cise determination of velocity implies precise determinations of position at t;wo times. Then, by the uncertainty principle, the momentum is completely uncertain a d a ll values me equaftly likely. Wiefi the rehtiviatle relation be- tween velseity and mamentm, &is is seen t~ imply t;ha;t velocitieo near the speed of light are more probabb, rso tbt in the limit the exwcted value of the velocity is the speed of Light.?

Similarly, (P - @A;), = i (Hp, - p,H) - is (HA, - A,$$) - eaA,/at The terms in A and A,, except the last, expand m follows:

?This argument is not completely acceptable, for k commutes with p; that ia, one should bs able to nsreaaure the two quantities simultansously.

## QUANTUM ELECTRODYNAMICS

Thihs seen to be the x component of The first and last term form the x component of E. Therefore, where F is the analowe of the Lorenlz force, Thi~eq uation is sometimes regarded as the analowe of Newton's equations. But, since there is no di- rect comection beheen this equation and 2, it does not had directly to Newton" equations in the Udt of small veloeitiee and hence i~ not com- pletely acceptable as a suitable analowe.

The followixrg relaaons may be verified as true but their memiw is not; yet completely understod, if at all: where in last relation a means the matrix; so that o, = --tar, ay,e tc.

From analogy to classical physics, one mi&t expet that the anmlar mo- mentum clpemlor is now From previous results for k and (Pp eh ), the time derivative of L may be written

## RELATIVISTIC WAVE EQUATION

The last term may be interpreted as torque. For a central force F, this term vanishes. But then it is seen that L 0 because of the first krm; that is, the angular molnanhtm L is eaneerved, even wl& central forces.

But consider the time derivative of Ule operator a defined as where c, = -a,ay, etc. The z component is seen to commute with the 8, e+, and a, terms of H but not with the a, and ay terms, so that cr, = - - + l(Ha,ay aXayH)= + ((Y,T,OI,(Y~ Q,@y(Yx~x+ QyTyaxay@-x @y@ylfy).

where

But so that This is seen to be the z component of -2or X ar IFinal3,y &en, and this is the first term of i w ith negative sign. Therefore it follows that which vanishes M* central forces. The operator L t- @/2)o may be re- garded as the total anguf ar momentum oprator, where L represents orbi- tag anwlar momentum and i-fi/2)o intrinsic a-Ear momenhm for spin 112.

Thus total, ang~ularm omenhm is conserved with central forces,

Pwblems: (1) h a stationary field $3 = 0, BA/@t = 0, show tfiat is a coastant of the motion. Nob that this is a consequence of the anomalous gyroma@etie ratio of the electron. X t also me cyclotron, frewency of the electron equals its rate of precession in iil mapetic field.

(2) fn a stationary nrr2lgnetic field 4 = 0, @A/Bt = 0, and for a sta- tionary stak, show that %fr. vIrz in are the same as JlrZ in the PauXi eqwtion, Also, if EPHulii a the Mnetle energy. in the PauXf equation and EBirsc = W + m i~ the msrt plus kineWc errsrm in the? Erac ewtiont, show ~t and explain the simplicity of &is relationship.

ltt will be assumed &at all ~bntialsar e etatiomry and statimary states will be considered. This m&es the work simpbr but is not necessary, h &is case Tbt is, f~gi= (m = a * (p- eA)@ +pm* + e@3 It wilE be recalled wiLh ?k written as Eq, (9-5) and wi& a,/3 as given in bcture 10, the previous equaaon may be writbn aa two eqiaaona (11)-4*), RELATIVISTXG WAVE EQUATI[QN 51 where, as befora, r = (p BA) a& V =- e$. Simplifying a ds olving Eq, (11-5) for ilib gives It is noted &at if W and V are 2m, aen JCrb -- (v/c)O,, For this remon +, and are sometimes referred to as the large and small components of @, respectively. S&st;itution of qb from Eq, (11-6) into Eq. (11-4)g ives and, if W and V are negiected in. eompari~enco 2m, the result Is This is the Pauli equation, Eq, (9-4).

Now fAe approdxnation will be carried out to h3ec0XTd order, that is, to order vZ/c2, to determine just what error may be expected from use of the Pauli equation.

Using the results of Leetrrre 11, given by Eqs, (11-6) md (11-7), the low- enerw approximation (W V) << 2m will be made, keeping terms to order v'. Thus Then Eq. f 11-71 bcomes while the normalizing requirement + ObZ)d v01 = 1, becornea By use of the substitution the normalizing integral can bs lsinzplified to read (to order v2/cZ)

## QUANTUM ELEGTRQDYNAMICS

This 8ubstitut;ion also allowe easier interpretation sf Eq, (12-2). Rewriting Eq. (12-21, [l + (o ~)~/(8rn~(]Wl - V) l1 + (cr.

Then applying Eq. (12-.4f and dividing by 1 + (cr*w]2/(8m2),t here results (W-V)X = (1/2m)(cr*~)\ (1/8rn~,(@.r1'~ The techniques c>E opralor akebra may be used to convert Q. (12-5) to a form more easily interpreted, In particular ane should recall that - - - A% -- 2ABA't. BA' = A(AB BA) (AB BA)A Then, since rr = (p ~fl3c),a nd since there result8 fwiGh cr. r = A and (W V) = B in the foregoiqj, fain~eV x E 8B/at = 0 here), so Eq, (12-5) can be expanded as - - WX = VX +- (f/ltm)(p -- eA).(p sA)x (c?/rztnr)(rr*B)~ (11 (21 1-31 -(1/8m')(~*p~~x (4 + (e2/8m2)~-+ -2~0 . (p -eAf x EfX (12-6)

(51 (6)

In this form the wave eqwtion may be interpreted by considering each term of Eq. (112-6) separately,

Term (1) give8 the ordinary scalar potential energ.y as it has appard before.

## RELATIVISTIC WAVE EQUATION

Term (2) can be interpreted as the kinetic enera.

Term (31, the Paull spin effect, ilr~j ust as it appears in the PmI equa- tion.

Term (4) is a relativistic correction to the kinetic energy. The correc- tion. derives from The last term in tlris expansion is e?quivalent to term (4).

Terms (5) and (6) express the spin-orbit coupling, To understmd this in- terpretation cornides the part of term (6) given by a * (p x E). In an inverse- square field this is proportional to o (p x r)/r3. The factor p x r can be u/r3, interpreted as the angular momentum L to get fa* the spin-orbit cou- pling. This term has no effect when the electron is in a s-state (L = 0). On the other hand, (5) reduces to V E = 4nZ&(r),w hich affects only the s-states (when the wave funetion is nonzero at r = Of. So (5) and (6) together result in a continuaus hnction for spin-orbit coupling. The magnetic moment of the electron e/2m, appars as the cmfficient of term (3), a d a gain of terms (5) and (G), i.e., (e/2m)(1/4m2),

A classical argment can be made to Interpret term (6). A charge mov- ing &rough m electric fiel - d vvi& velocity 'tt feels an effective magnetic field B = v x E = ff[m)(p eA) x E, and term (6) is just the energy (e/2m) x (o B) in Ws field. flVe get a factor 2 too much this way, however. Even, be- fore the development of" the Dirac equation, Thornas showed that tMs simple classical armrnent is incomplete and gave the correct term (6). The siha- tion is d;ir%eread for the anomalou~m orrxenh intraduced by PauU to describe neubons and protons (aee Problem 3 below). In PauIi's mmodified equation, the momalous moment does appeas w'rth the factor 2 vvhn multiplying terms (5) and (6).

Problems: (1) Apply Eq. (12-6) Lo the Wdrogen atom and correct the energy levels to first order. The resulb should be compared to the exact results.? Note the difference of the wave functions at the origin of coordinaks, This difference actualIy is too restricted in space to have any imporbnce. Near the origin the correct solution to the Dirac equation i~ praportioml to for the hydrogenie aloma , while the Schrbdinger equation gives 0 conatmt as r - + 0, t gchiff* "Wanturn Mechanics, McGraw-Hilt, New York, 1949, pp. 323fif.

(2) @uppose A iuld $ I depend on time. b t W = iB/a t and follow tfirawh the procedures of this lectme to the sme order af approa- mation.

(3) Pauli" edified eqwl;ion can be applied to neutrons a d p ro- tons. It ilts obtained by adang a term for anomalous moments to the Rirac equation, thus Multiplyiq by P, this may be written in the more familiar "LHrzmil- toniarr" expression i(@/at)@= PI,,,, 9 -+ p@( P E) -cl! * E)* Show thd the s m e appsaamation which led to Eq. (12-6) will naw prduce the brms far protans, and a similar expree%sianf or neutronw, but Mth e = 0.

(4) Equation (12-7) cm be used to inbrpret electran-neutron scat- tering in an atom. Mat of the scatteriq of neutrons by atoms is the ieotropie scsttbri~fr om the nucleus, However, the electrons of the atom also scatter, and give rise ta a warre which inbrferes with nuclear scattering. For slow nearam, $hi@e Eeet is experimentally oh- served. lit is interpreted by term (5) of Eq. (12-6) [as mdified in Eq, (12-7) vvith e = 01 . Since the electron charge is present outside Ule nucleus, V E has a value different from 0, Term (5) cm be used in a Born approxirnalf on to cornpub tlre mplitude for neutron-elecdron scattering, However, when the effect was first discovered, it wm @X- plained by the assmption of a neutron-electron interaction given by the potential e6(E1), where 5 is the Dirac 6 function and R is the neua Itron-electron distance.

Comwte t-he scattering mplitude vvith ct9(R) by the Born approd- mation and campare with fiat given by term (5). ~XZOWt bt In order to interpret cd(R) as a potential, the averwe p-cltential 5 is defined as that potential which. acting over a sphere of radius e2/mc2, would prduce the same effect.

Using = 1.91 35 eB/22hlM, show that the resuiting V agrees with exprimental results within the slat;ed accuracy, i.e., 4400 -1 1100 ev, t -f L, Foldy, Phys, Rev., 87, 693 (1952).

## RELATIVXSTXC WAVE EQUATION

(5) Neglecting terms of order v2/c', show that

Solution of the Dirac Equation for a Free Particle

Thirteenth L eeture

It will be co~vttnlentt o use the form of the Dirac wuaaan rrlith the Y 'ET when ao2;rriw for the free-particle wave hn~tiom Using the definition of Lecture 10, = yl,a P and the Dirac equation may be written (Recall that the quantity 4 = ypaP is invariant under a Lorentz transfo rms- tiaa,)

It is necessary to put the probability density and current into a four-dimensional form. In the standard representation, the probability density and current are given by If the relativistic adjoint of ψ is defined in the standard representation, then the probability density and current may be written To verify this, replace ψ by ψ*γ and note that γ² = 1 and that γμγν = -γνγμ.

Exercises: (1) Show that the adjoint of ψ satisfies (2) From Eqs. (13-1) and (13-3) show that ∂μjμ = 0 (conservation of probability density)

In general, the adjoint of an operator N is denoted by \(\bar{N}\), and is the same as N except that the order of all γ appearing in it is reversed, and each explicit i (not those contained in the γ's) is replaced by -i. For example, if N = γμ, then \(\bar{N}\) = γμγ0 = -γμ. If N = iγμγνγρ, then \(\bar{N}\) = -iγργνγμ. The following property takes the place of the Hermitian property so useful in nonrelativistic quantum mechanics: For a free particle, there are no potentials, so Aμ = 0 and the Dirac equation becomes To resolve this, try as a solution ψ is a four-component column vector.

The adjoint \(\bar{ψ}\) is the four-component row vector in the standard representation. Multiplication by γ0 changes the sign of the third and fourth components, in addition to going from a column vector to a row vector.

To see what is meant by the trial solution is that each of the four components is of this form, that is, Thus u1, u2, u3, and u4 are the components of a column vector, and u is called a Dirac spinor. The problem is now to determine what restrictions must be placed on the u's and p in order that the trial solution satisfy the Dirac equation. The γμ∂μ operation on each component of ψ multiplies each component by -ipμ, so that the result of this operation on ψ produces so that Eq. (13-5) becomes Thus the assumed solution will be satisfactory if \((γμpμ - m)u = 0\). To simplify writing, it will now be assumed that the particle moves in the xy plane, so that pz = 0.

Under these conditions, \(γμpμ = γ1p1 + γ2p2\) in standard representation.

By components, Eq. (13-7) becomes (E - m)u1 - (p1 - ip2)u4 = 0 (E - m)u2 - (p1 + ip2)u3 = 0 (p1 - ip2)u1 - (E + m)u4 = 0 (p1 + ip2)u2 - (E + m)u3 = 0 The ratio u3/u4 can be determined from Eq. (13-9a) and also from Eq. (13-9d). These two values must agree in order that Eq. (13-6) be a solution.

Thus This is not a surprising condition. It states that the p must be chosen so as to satisfy the relativistic equation for total energy.

Similarly, Eqs. (13-9b) and (13-9c) can be solved for u2/u3 giving which also leads to condition (13-10).

A more elegant way of obtaining exactly the same condition is to start directly with Eq. (13-7). Then, by multiplying this equation by γ0 gives The former is the same condition as obtained before, and the latter is a trivial solution (no wave function)

Evidently there are two linearly independent solutions of the free-particle Dirac equation. This is so because substitution of the assumed solution, Eq. (13-6), into the Dirac equation gives only a condition on pairs of the u's, u1, u3 and u2, u4. It is convenient to choose the independent solutions so that each has two components which are zero, u3 = u4 = 0 for these two solutions can be taken as where the following notation has been used: These solutions are not normalized.

What do the two linearly independent solutions mean? There must be some physical quantity that can still be specified, which will uniquely determine the wave function. It is known, for example, that in the coordinate system in which the particle is at rest there are two possible spin orientations. Mathematically speaking, existence of two solutions to the eigenvalue equation \(\gamma \cdot p u = mu\) implies the existence of an operator that commutes with γ·p. This operator will have to be discovered. Observe that γ0 anticommutes with γ·p; that is, γ0γ·p = -γ·pγ0. Also observe that no γμ operator will anticommute with γ·p if γμpμ ≠ 0, because The combination γ0 of these two anticommuting operators is an operator which commutes with γ·p. That is, The eigenvalues of the operator (iγ0γ1γ2) must now be found (the i has been added to make eigenvalues come out real in what follows). Denoting these eigenvalues by s, To find the possible values of s, multiply Eq. (13-23) by iγ0γ1γ2, If \((γ0γ1γ2)^2\) is seen to be -1, then the eigenvalues of the operator iγ0γ1γ2 are ±1. The significance of the choice \((γ0γ1γ2)^2 = -1\) is as follows: In the system in which the particle is at rest, p1 = p2 = 0 and p4 = iE. Then Thus, \((γ0γ1γ2)^2 = -1\) or \(γ0γ1γ2 = 1\). This states that in the coordinate system in which the particle is at rest, \(\Sigma_z\) is an ordinary vector (it has zero fourth component) with unit length.

When the particle moves in the xy plane, choose p to be γ·p, so the operator equation for iγ0γ1γ2 becomes Using relationships derived in Lecture 10, this becomes, for a stationary particle, This choice makes \(\Sigma_z\) the σz operator, and the relationship with spin is clearly demonstrated. If we define u to satisfy both \(\gamma \cdot p u = mu\) and \(iγ0γ1γ2 u = su\), this completely specifies u. It represents a particle moving with momentum p, and having its spin (in the coordinate system moving with the particle) along the z axis in the positive (s = +1) or negative (s = -1) direction.

Exercise: Show that the first of the wave functions, Eq. (13-11), is the s = +1 solution and the second is the s = -1 solution.

Another way of obtaining the wave function for a freely moving electron is to perform an equivalence transformation of the wave function as in Eq. (10-12). If the electron is initially at rest with its spin up or down in the z direction, then the spinor for an electron moving with a velocity v in the spatial direction k is [For normalization, see Eq. (13-14).]

From Eq. (10-12), S is given by cosh α = 1/(1 - v²)^{1/2} For a stationary particle, γ·u = u.

(2m)^{1/2} cosh (α/2) = [m(v² + 1)]^{1/2} = (E + m)^{1/2} Writing f = (E + m)^{1/2}, a = γ·v, and noting (v² - m²)^{1/2} = p, we get For the case that v is in the xy plane, this just gives the result, Eq. (13-11), with a normalization factor 1/n.

Noticing that for an electron at rest γ0u0 = u0, may be written It is clear that this is a solution to the free-particle Dirac equation.

In nonrelativistic quantum mechanics, a plane wave is normalized to give unity probability of finding the particle in a cubic centimeter, that is, u* u = 1. The analogous normalization for the relativistic plane wave must be something else.

However, u† u transforms similarly to the fourth component of a four-vector (it is the fourth component of four-vector current), so this normalization would not be invariant. It is possible to make a relativistically invariant normalization by letting u† u equal to the fourth component of a suitable four-vector. For example, p4 is the fourth component of the momentum four-vector pμ, so the wave function could be normalized by The constant of proportionality (2)^{1/2} is chosen for convenience in later formulas. Working out (u† u) for this state, The C is the normalizing factor multiplying the wave functions of Eq. (13-11). In order that (u† u) be equal to 2E, the normalizing factor must be chosen (E + m)^{-1/2}. In terms of (u† u), this normalizing condition becomes The same result is obtained for the s = -1 state. Thus the normalizing condition can be found.

It will be convenient to have the matrix elements of all the γμ between various initial and final states, so Table 13-1 has been worked out.

TABLE 13-1. Matrix Elements for Particle Moving in the xy Plane 1 2m p1^2 + p2^2 0 p1 + p2 - 0 γ1 ~ p1 p2 p1 + p2 - p1 - 0 γ2 2p2 - (p1^2 + p2^2) + 1 p1 - p2 - 0 γ3 0 0 -p1* p2 + p1 + p2 + 0 γ4 2E p1 + p2 - 0 Interchanging cases: To obtain the case where γ1 is a positron at rest, the table gives matrix elements p1 = p2 = 0, p1+ = 1 = p1- in the table. For both at rest as well as antiparticles, the table gives (γμ)_{ul} u_f if F1 = F2 = 0; p1+ = p1- = 1.

Fourth Lecture The matrix element of an operator M between initial state ui and final state uf will be denoted by The matrix element is independent of the representations used if they are related by unitary equivalence transformations. That is, where the property S = S† has been assumed for S.

The straightforward method to compute the matrix elements is simply to write them out in matrix form and carry out the operations. In this way the data in Table 13-1 were obtained.

Other methods may be used, however, sometimes simpler and sometimes leading to corollary information, as illustrated by the following example. By the normalization convention, u† u = 1. Similarly, (γμ u)† (γν u) = m(μ† γν u)

But also note that (γμ u)† (γν u) = m(μ† γν u)

because γμ† = γ0γμγ0 = γμ. Adding the two expressions, one obtains From the relation proved in the exercises, it is seen that p1 + p2 = 0, γμ = γν = 2 But p1 is just a number, so it follows that and since u† u = 2m, by normalization (γμ u)† (γν u) = 2pμ The second objection is mathematical.

That is, excluding the negative energy states leads to an incomplete set of wave functions. It is not possible to represent an arbitrary function as an expansion in functions of an incomplete set. This situation led Schrödinger into insurmountable difficulties.

Problem: Suppose that for t < 0 a particle is in a positive energy state moving in the x direction with spin up in the z direction (σ_z = +1). Then at t = 0, a constant potential A = A_x (A_y = A_z = 0) is turned on and at t = τ it is turned off. Find the probability that the particle is in a negative energy state at t = τ.

Answer: Probability of being in negative energy state = A^2 / (A^2 + m^2) sin^2 [(m^2 + A^2)^(1/2) τ]

at t = τ.

Note that when E = -m, 1/u = m, so that the u's apparently blow up.

But actually the components of u also vanish when E = -m, so that a limiting process is involved. It may be avoided and the correct results obtained simply by omitting 1/u and replacing E by zero and p_x by 1 in the components of u.

The positive energy levels form a continuum extending from E = m to +∞, and the negative energies if accepted as such form another continuum from E = -m to -∞. Between +m and -m there are no available energy levels (see Fig. 14-1). Dirac proposed the idea that all the negative energy levels are normally filled. Explanations for the apparent obscurity of such a set of electrons in negative energy states, if it exists, usually contain a psychological aspect and are not very satisfactory. But, nevertheless, if such a situation is assumed to exist, some of the important consequences are these:

## 1. Electrons in positive energy states will not normally be observed to

make transitions into negative energy states because these states are not available; they are already full.

## 2. With the sea of electrons in negative energy levels unobservable, a

"hole" produced by a transition of one of its electrons into a positive energy state should manifest itself. The manifestation of the hole is regarded as a positron and behaves like an electron with a positive charge.

## 3. The Pauli exclusion principle is implied in order that the negative sea

may be full. That is, if more than just one electron could occupy a given state, it would be impossible to fill all the negative energy states. It is in this way that the Dirac theory is sometimes considered as a "proof of the exclusion principle."

Another interpretation of negative energy states has been proposed by the present author. The fundamental idea is that the "negative energy"

states represent the states of electrons moving backward in time.

In the classical equation of motion reversing the direction of (proper) time amounts to the same as reversing the sign of the charge so that the electron moving backward in time would look like a positron moving forward in time.

In elementary quantum mechanics, the total amplitude for an electron to go from x₁, t₁ to x₂, t₂ was computed by summing the amplitudes over all possible trajectories between x₁, t₁ and x₂, t₂, assuming that the trajectories always moved forward in time. Three trajectories might appear in one dimension as shown in Fig. 14-2. But with the new point of view, a possible trajectory might be as shown in Fig. 14-3.

Imagining oneself an observer moving along in time in the ordinary way, being conscious only of the present and past, the sequence of events would appear as follows: t₁ only the initial electron present.

t only the initial electron still present but somewhere else, say as an electron-positron pair is formed.

t' the initial electron, and newly arrived electron-positron pair are present.

t'' the positron meets with the initial electron, both of them annihilating, leaving only the previously created electron.

t₂ only one electron present.

To handle this idea quantum mechanically two rules must be followed:

1. In calculating matrix elements for positrons, the sign of the wave function must be reversed. That is, for an electron moving forward in time from a past state to a future state the matrix element is But moving backward in time, the electron proceeds from future to past, so the matrix element for a positron is 2. If the energy E is positive, then e^(-iEt) is the wave function of an electron with energy p_0 = E. If E is negative, then e^(-iEt) is the wave function of a positron with energy -E or p_0 (and of four-momentum -p).

Potential Problems

Fifteenth Lecture

## PAIR CREATION AND ANNIHILATION

Two possible paths of an electron being scattered between the states ψ₁ and ψ₂ were discussed in the last lecture. These are: Case I. Both ψ₁, ψ₂ states of positive energy, interpreted as ψ₁ electron in "past," ψ₂ electron in "future." This is electron scattering.

Case II. Both ψ₁, ψ₂ states of negative energy, interpreted as ψ₁ positron in "future," ψ₂ positron in "past." This is positron scattering.

The existence of negative energy states makes two more types of paths possible. These are: Case III. The ψ₁ positive energy, ψ₂ negative energy, interpreted as ψ₁ electron in "past," ψ₂ positron in "past." Both states are in the past, and nothing in the future. This represents pair annihilation.

Case IV. The ψ₁ negative energy, ψ₂ positive energy, interpreted as ψ₁ positron in "future," ψ₂ electron in "future." This is pair creation.

The four cases can be diagrammed as shown in Fig. 15-1. Note that in each diagram the arrows point from ψ₁ to ψ₂, and though time is increasing upward in all cases. The arrows give the direction of motion of the electron in the present interpretation of negative energy states. In common language, the arrows point toward positive or negative time according to whether the energy is positive or negative, that is, whether the state represented is that of an electron or a positron.

## CONSERVATION OF ENERGY

Energy relations for the scattering in case I have been established in previous lectures. It can be seen that identical results hold for case II. To show this, recall that in case I, if the electron goes from the energy E₁ to E₂ and if the perturbation potential is taken proportional to exp(-iωt), then this perturbation brings in a positive energy ω. To see this, note that the amplitude for scattering is proportional to As has been shown, there is a resonance between E₂ and E₁ + ω, so that the only contributing energies are those for which E₂ = E₁ + ω. In case II the same integral holds but E₂ and E₁ are negative. A positron goes from an energy (past) of E_past = -E₂ to an energy (future) of E_future = -E₁. With the same perturbation energy, the amplitude is large again only if E₂ = E₁ + ω or -E_future = -E_past + ω, so that E_future = ω + E_past; that is, the perturbation carries in a positive energy ω just as it does for the electron case.

In the nonrelativistic case (Schrödinger equation), the wave equation, including a perturbation potential, is written where V is the perturbation potential and H₀ is the unperturbed Hamiltonian. For the free particle, the kernel giving the amplitude to go from point 1 to point 2 in space and time can be shown to be where N is a normalizing factor depending on the time interval t₂ - t₁ and the mass of the particle: Note that the kernel is defined to be 0 for t₂ < t₁. It can be shown that K₀ satisfies the equation The propagation kernel K_V(2,1) giving a similar amplitude, but in the presence of the perturbation potential V, must satisfy the equation It can be shown that K_V can be computed from the series In case the complete Hamiltonian H = H₀ + V is independent of time, and all the stationary states ψ of the system are known, then K_V(2,1) may be obtained from the sum The extension of these ideas to the relativistic case (Dirac equation) is straightforward. By choosing a particular form for the Hamiltonian, the Dirac equation can be written Defining the propagation kernel as K, then the kernel is the solution to the equation The matrix γ₄ is inserted in the last term in order that the kernel derived from the Hamiltonian be relativistically invariant. [Note the similarity to the nonrelativistic case, Eq. (15-6).] Multiplying this equation by β, a simpler form results: The equation for a free particle is obtained simply by letting V = 0, then call this free-particle kernel K₀.

The notation K₀ replaces the K of the nonrelativistic case, and Eq. (15-10)

replaces Eq. (15-4) as the defining equation.

Just as K_V can be expanded in the series of Eq. (15-6), so can K be expanded: Note that the kernel is now a four-by-four matrix, so that all components of K can be determined. Since this is true, the order of the terms in Eq.

(15-11) is important. The element of integration is actually an element of volume in four-space.

The potential, -ieA_μ(1)c, can be interpreted as the amplitude per cubic centimeter per second for the particle to be scattered once at the point A_μ(1). Thus the interpretation of Eq. (15-11) is completely analogous to that of Eq.

(15-6).

Problem: Show that K_V as defined by Eq. (15-11) is consistent with Eqs. (15-8) and (15-9).

In the nonrelativistic case, the gaps along which the particle reversed its motion in time are excluded. In the present case is no longer true.

The existence and interpretation of the negative energy eigenvalues of the Dirac equation allows the interpretation and inclusion of such paths.

Taking t₄ to t₅ implies the creation of virtual pairs. The section from t₄ to t₅ represents the motion of a positron (see Fig. 15-2).

In a time-stationary field, if the wave functions ψ are known for all the states of the system, then K₀ may be defined by Another solution of Eq. (15-9) is K_A(2,1) = C exp[-iE_a(t₂ - t₁)] ψ_a (~g)$mn (~t)

pos. energies C ' t exp [-i~,(tl- tl)~#~(x~)?~t(2x ~)

neg. energies Equation (15-13) has an interpretation consistent with the positron interpretation of negative energy states. Thus when the thing is "ordinary" (L2 > e,), an electron is present, and only positive energy states contribute, When the time is "reversed" (t2< . tlf , a positron is present, and only negative energies" contributes. On the other hand, Eq. (15-13) does not have so satisfactory an interpretation. Although the kernel has been defined by Eq. (15-13) is also a satisfactory mathematical solution of Eq. (15-9) (as shown below), the interpretation of Eq. (15-13) requires the idea of an electron in a negative energy state.

To show that both kernels are solutions of the same inhomogeneous equation, note that their difference is for all. t2, This is, term: by term, a solution of the homogeneous equation [i.e., Eq. (15-9) with zero right-hand side). The possibility that two such solutions exist results from the fact that boundary conditions have not been definitely fixed. We shall always use K , ~ .

The kernel K + defined by Eq. (15-12), allows treatment of case 111 (pair annihilation) and case N (pair creation) shown at the beginning of a structure. In each case, the potential, -V(r), acts at the interaction of positron and electron paths.

Sixteenth Lecture USE OF THE KERNEL K,(2,1)

In the nonrelativistic theory it was possible to calculate the wave function at a point xz at time tz from a knowledge of the wave function at an earlier time tl (see Fig, 16-1) by means of the nonrelativistic kernel Ko(xz,tz; tj,t1), It might be expected that a relativistic generalization of this would be FIG. 16-1 FIG. 16-2 It turns out to be incorrect, however. It is not sufficient, in the relativistic case, to know just the wave function at an earlier time only because K(2,f) is not zero for t2 < t1 when the kernel, is defined in this manner (Chapter 15), the wave function at xz,tz (see Fig. 16-2) is given by The first term is the contribution from positive energy states at earlier times and the second term is the contribution from negative energy states at later times. This expression can be generalized to state that it is necessary to have 9(x1tx) on a four-dimensional surface surrounding the point xz,tz (see Fig. 16-3): where We is the four-vector normal to the surface that encloses xz,tz The amplitude to go from a state f to a state g under the action of a potential V is given by an expression similar to that in nonrelativistic theory, Using the expansion of ~(2.1) in terms of K,(2.1), Eq. (16-12), and assuming that the amplitude for transition from state f to state g as a free particle is zero if f and g are orthogonal states), the first-order amplitude for transition (Born approximation) is It is convenient to let Thus state that the particle has the free-particle wave function f just prior to scattering and the free-particle wave function g just after scattering, and that it eliminates any computation of the motion as a free particle, The amplitude for transition, to first order, only be written omits integration over time as well as space). The second-order term would be written -(1/2) ∫g*(4)eA(4)K,(4,3)e((3)f(3) d^4x If f(3) is a negative energy state, then it represents a positron of the future instead of an electron of the past and the process described by this amplitude is that of pair production.

We shall make use of the theory just presented to calculate the scattering of an electron from an infinitely heavy nucleus of charge Ze. Suppose the incident electron has momentum in the x direction and the scattered electron has momentum in the xy plane (see Fig. 16-4): FIG. 16-4 The potential is that of a stationary charge Ze.

The initial and final wave functions are plane waves: f(1) = u1 e^{-i p x} g (2) = u2 e^{-i p x} (four-component wave function)

Thus, for Eq. (16-5), the first-order amplitude for transition from state f to state g (momentum p1 to momentum p2) is Separating space and time dependence in the wave functions, this expression for the foregoing fe /oa - ~+(t,xk= -(l/srr2) d a exp I-(i/2)[(m2/(u) + or (t2 x2)))

Both of these farms are too complicated to be of much. practical use. It will be shown shortly that a tremendous simplification results from transforma- tion to momentum representation, Note that I+(t,x) ac-fly demands only on |x| not on its direction. In the time-space diagram (Fig. 27-1) the vertical axis represents |x| and the diag- onal lines represent the surface of a light cone including the t axis, that is, the accessible region of |x| space in the ordinary sense. It can be shown that the asymptotic form of I+(t,x) for large s is proportional to e^(-ms).

When one's region of accessibility is limited to the inside of the light cone, large s implies t² >> |x|², so that the region of the asymptotic approxima- tion lies roughly within the dotted cone around the t axis and is FIG. 15-1 ?See Phys. Rev., 78, 749 (1949); included in this volume,

## PROBLEMS IN QUANTUM ELECTRODYNAMICS

The first form is seen to be essentially the same as the propagation ker- nel for a free particle used in nonrelativistic theory. If, as in the new theory, possible trajectories are not limited to regions within the light cone, an- other region included in this asymptotic approximation is that within the dotted cone along the |x| axis where large s implies |x|² >> t². Hence It is seen that the distance along |x| in which this becomes small is roughly the Compton wavelength (recall that m -- mc/h when it represents a length as here), so that in reality not much of the |x| space outside the light cone is accessible.

The transformation to momentum representation will now be made. This is facilitated by use of the integral formula The iε term in the denominator is introduced solely to ensure passage around the proper side of the singularities at: p = ±E along the path of integration.

Passage on the wrong side will reverse the sign in the exponential on the right.

Problem: Work out the integral above by contour integration; or otherwise, Using the integral relation above, d+(t,x) becomes But E² = p² + m² so this is where p is now a four-vector so that dp⁴ = dp⁴ dp¹ dp² dp³, and p · x = p⁰t - p·x. Hereafter the iε term will be omitted. Its effect can be included simply by imagining that m has an infinitesimal negative imaginary part. In this form the transformation to momentum representation is easily ac- complished as follows (we actually take Fourier transform of both space and time, so this is really a momentum-energy representation): where the dummy variable q has been substituted for p in the p integral.

But Hence the q integration gives the result Finally, applying the operator i(∂/∂t - ∇²/m) to d+(t,x) gives the propagation ker- nel (here x = x₂ - x₁)

recalling that i∂/∂t operating on exp [-i(p · x)] is the same as multiplying by -i p⁰. From the identity the kernel can also be written By the same process used for d+(t,x), the transform of K+(2,1) in momen- tum representation is seen to be This is the result which was sought.

Actually, this transformation could have been obtained in an elegant man- ner. For K+(2,1) is the Green's function of (∂/∂t - ∇²/m), that is, and it is known that if F is a solution of this equation and δ(2,1) is unity.

Therefore the transform of this equation can be written down immedi- ately: as before.

The fact that Eq. (17-1) for K(2,1) has more than one solution is re- flected in Eq. (17-2) in the fact that (d - m)⁻¹ is singular if p² = m². We shall have to say just how we are to handle poles arising from this source in integrals. The rule that selects the particular form we want is that m has considered as having an infinitesimal negative imaginary part.

Eighteenth Lecture Since the propagation kernel for a free particle is so simply expressed in momentum representation, it will be convenient to convert all our equations to this representation. It is especially useful for problems involving free, fast, moving particles. This requires four-dimensional Fourier transforms. To convert the potential, define Then the inverse transform is The function a(q) is interpreted as the amplitude that the potential con- tains the momentum (q). As an example, consider the Coulomb potential, given by A = 0, φ = Ze/r.

Substituting into Eq. (18-1) gives Here the vector Q is the spatial part of the momentum. The delta func- tion δ(q₀) arises from the time dependence of φ(x).

88 QUANTUM ELECTRODYNAMICS Ultraviolet Elements: An advantage of momentum representation is the sim- plicity of computing matrix elements. Recall that in space representation the first-order perturbation matrix element is given by the integral For the free particle, this becomes In momentum representation, this is simply where p' is defined analogously to the three-vector q.

The second-order matrix element in space representation is given by Substituting for a free particle and also expressing the Green's functions as their Fourier transforms by means of Eq. (18-g), this becomes If Eq. (18-2) is used for K+(2,1), this kernel can be written Writing the factors that depend on x₁, this part of the integral is exp (i p · x₁) exp (-i q · x₁) exp (-i p' · x₁) dx₁ = (2π)⁴δ⁴(p - q - p')

where the function δ⁴(x) is to be interpreted as δ(t₁)δ(x₂)δ(y₃)δ(z₄). Then the integral over x₁ is zero for all except q = p - p'. So the integral over p reduces Eq. (18-4) to

## PROBLEMS IN QUANTUM ELECTRODYNAMICS

Integrating over x₂ results in another δ function [similar to Eq. (18-5)], which differs from zero only when Then integrating over p and q gives finally These results can be written down immediately by inspection of a diagram of the interaction (see Fig. 18-1). The electron enters the region at 1 with FIG. 18-1 wave function u₁ and moves from 1 to 3 as a free particle of momentum p₁.

At point 3, it is scattered by a photon of momentum q₁ under the action of the potential -ieφ(q₁). Having absorbed the momentum of the photon, it then moves from 3 to 4 as a free particle of momentum p₁ + q₁. By conservation of momentum, at point 4, it is scattered by a second photon of momentum q₂ (under the action of the potential -ieφ(q₂)) absorbing the additional momen- tum q₂. Finally, it moves from 4 to 2 as a free particle with wave func- tion u₂ and momentum p₂ = p₁ + q₁ + q₂. It is also clear from the diagram that the integral need be taken over q₁ only, because when q₁ and q₂ are given, q₂ is determined by q₂ = p₂ - p₁ - q₁. The law of conservation of en- ergy requires p₁² = m², p₂² = m²; but, since the intermediate state is a vir- tual state, it is not necessary that (p₁ + q₁)² = m². Since the operator /(p₁ + q₁ - m) may be resolved as (p₁ + q₁ + m)/((p₁ + q₁)² - m²), the impor- tance of a virtual state is inversely proportional to the degree to which the conservation law is violated.

The results given in Eqs. (18-3') and (18-6) may be summarized by the following list of handy rules for computing the matrix element M = (2|S|1):

## 1. An electron in a virtual state of momentum p contributes the ampli-

tude i/(p̸ - m) to M.

## 2. A potential containing the momentum q contributes the ampli-

tude -ieφ(q) to M.

## 3. All indeterminate momenta q are summed over ∫ d⁴q/(2π)⁴

Remember, in computing the integral, the value of the integral is desired.

Use the path of integration, assuming the singularities in a definite manner.

Typically this means replace m by m - iε in the integrand; then in the solution take the limit as ε → 0.

For relativistic work, only a few terms in the perturbation series are necessary for computation. To assume that fast electrons (and positrons)

interact with photons only once (Born approximation) is often sufficiently ac- curate.

After the matrix element is determined, the probability of transition per second is given by P = 2π/(ℏN) ∫ |M|² × (density of final states)

where ℏN is the normalization factor defined in lecture 16.

*See Summary of numerical factors for transition probabilities, R. P.

Feynman, An Operator Calculus, Phys. Rev., 84, 123 (1951); included in this volume.

Relativistic Treatment of the Interaction of Particles with Light In lecture 2 the rules governing nonrelativistic interaction of particles with light were given. The rules specified what potentials were to be used in the calculation of transition probabilities by perturbation theory. Those po- tentials are also applicable to the relativistic theory if the matrix elements are computed as described in lecture 18. For absorption of a photon, the potential used in nonrelativistic theory was For emission of a photon, the complex conjugate of this expression is used.

These potentials are normalized to one photon per cubic centimeter and hence the normalization is not invariant under Lorentz transformations. In a manner similar to that for the normalization of electron wave functions, photon potentials will, in the future, be normalized to 2ω photons per cubic centimeter by dropping the (2ω)⁻¹/² factor in Eq. (19-1), giving A_λ = (4πe²/2ω)¹/² e_λ exp (ik · x) (19-1')

This makes any matrix element computed with these potentials invariant, but to obtain the correct transition probability in a given coordinate sys- tem, it is necessary to reinsert a factor (2ω)⁻¹ for each photon in the initial and final states. This becomes part of the normalization factor N, which con- tains a similar factor for each electron in the initial and final states.

92 QUANTUM ELECTRODYNAMICS In momentum representation, the amplitude to absorb (emit) a photon of polarization e_λ is -i(4πe²/2ω)¹/² e_λ. The polarization vector e_λ is a unit vector perpendicular to the propagation vector k. Hence e · k = 0, and e · e = 1.

## EQUATION FROM ATOM

The transition probability per second is Trans. prob./sec = 2π/ℏ N ∫ |M|² × (density of final states)

where M is the matrix element of the relativistic Hamiltonian, H = α · (-i∇ + A_λ) + βm between initial and final states. That is, ⟨f|H|i⟩ = (4πe²/2ω)¹/² ∫ ψ_f† [α · e exp(ik · x)] d vol (19-2)

Problem: Show that in the nonrelativistic limit, Eq. (19-2) reduces to × ψ_f* exp(ik · x) ψ_i d vol This is the same result as was obtained from the Pauli equation.

A relativistic treatment of scatter ing of photons from electrons will now be given. As an approximation, consider the electrons to be free (energies at which a relativistic treatment is necessary are, generally, much greater than atomic binding energies). This will lead to the Klein-Nishina formula for the Compton-effect cross section.

incoming recoil electron FIG. 19-1

## INTERACTION OF PARTICLES WITH LIGHT

For the incoming photon take as a potential Aμ = εμ exp (-iq₁ · X) and for the outgoing photon take Aμ = εμ exp (-iq₂ · X). The light is polarized per- pendicular to the direction of propagation (see Fig. 19-1). Thus, ε · q₁ = 0 and ε · q₂ = 0 q₁² = q₂² = 0 and q₁ · q₂ = q₁₂ = 0 As initial and final state electron wave functions, choose ψ = u exp (-ip · X)

Conservation of energy and momentum (four equations) is written The coordinate system is chosen so that electron number 1 is at rest, - - q₂ = ω₂(y₂ + x₂ cos θ + y₂ sin θ) (19-6d)

The last two equations follow from the fact that, for a photon, the energy and momentum are both equal to the frequency (in units in which c = 1). The momentum has been resolved into components. The incoming photon beam can be resolved into two types of polarization, which will be designated type A and type B: Type A has the electric vector in the z direction and type B has the elec- tric vector in the y direction. Similarly the outgoing photon beam can be resolved into two types of polarization:

## QUANTUM ELECTRODYNAMICS

(4") ε₂ = y₂ (B') ε₂ = y₂ cos θ + z₂ sin θ Conservation of energy and momentum dictates that either the angle of the recoil electron θ or the angle at which the scattered photon comes off θ completely determines the remaining quantities. If the electron direction is unimportant, its momentum can be eliminated by solving Eq. (19-5) for p₂ and squaring the resulting equation: =m² + ω² + ω'² + 2mω - 2mω' - 2ωω' (1 - cos θ)

where the last line was obtained from the preceding line by using Eqs. (19-3), (19-4), and (19-6a, c, d). This can be written - - ω' = ( ω / [1 + (ω / m)(1 - cos θ)])

This is the well-known formula for the Compton shift in wavelength (or fre- quency)

## DIRECTION ON THE DENSITY OF FINAL STATES

By the method discussed in the earlier part of the course, the following final state densities (per unit energy interval) can be obtained.

If a system of total energy E and total linear momentum p disintegrates into a two- particle final state, dG₁ Density of states = (2π)^{-3} |E₁(p₀)p₁|^{-1} dΩ₁ (B-1)

where E₁ = energy of particle 1; E₂ = energy of particle 2; p₁ = momentum of particle 1; dΩ₁ = solid angle into which particle 1 comes out; m₁ = mass of particle 1; m₂ = mass of particle 2; and E₁ + E₂ = E, p₁ + p₂ = p.

Another useful formula is in terms of the final energy of particle 1 and its azimuth φ₁ [instead of dΩ₁). It is Density of states = (2π)^{-3} (E₁E₂ / |p₁|) d E₁ dφ₁ (B-2)

## INTERACTION OF PARTICLES WITH LIGHT

Special cases: (a) when m₂ = 0, E₂ = E = m): Density of states = (2π)^{-3} E' |p₁| dΩ₁ Density of states = (2π)^{-3} E' dE₁ / [ ω' (1 + ω'/m)] (B-4)

When a system disintegrates into a three-particle final state, Density of states = (2π)^{-3} E₃E₂E₁ Special case: when m₃ = 03: Density of states = (2π)^{-3} E₂ |p₁| dΩ₁ dE₂ (B-6)

The Compton effect has a two-particle final state: taking particle 1 to be photon 2 and particle 2 to be electron 2, from Eq. (D-1), Dens3ity of states = (2π)^{-3} (1 / (2ω')) dΩ₂ Calculation of |M|². Using the Compton relation Eq. (19-7) to eliminate θ, this becomes Density of states = (2π)^{-3} dω₂ / [ω' (1 + ω'/m)]

The probability of transition per second is given by In working out the matrix element M, there are two ways in which the scat- tering can occur: (R) the incoming photon is absorbed by the electron and then the electron emits the outgoing photon; (S) the electron emits a photon and subsequently absorbs the incident photon. These two processes are shown diagrammatically in Fig. 19-2.

In momentum representation, the matrix element M for the first pro- cess R is Reading from right to left the factors in the matrix element are inter- preted as follows: (a) The initial electron enters with amplitude u₁; (b) the electron is first scattered by a potential (i.e., absorbs a photon); (c) having re- ceived momentum q₁ from the potential the electron travels as a free elec- tron with momentum p₁ + q₁; (d) the electron emits a photon of polarization ε₂; and (e) we now ask for the amplitude that the electron is in a state u₂.

Exercise: Write down the matrix element for the second process.

## 5. The total matrix element is the sum of these two. Rationalize

these matrix elements and, using the table of matrix elements (Table 13-1) work out |M|².

Twentieth Lecture For the R diagram, M was found to be -i4πe² [ū₂ / (p̸₁ + q̸₁ - m)] ε̸₁ u₁ = -i4πe² ( G_R )

and as an exercise the matrix element for the S diagram was found to be -i4πe² { ū₂ ε̸₂ [1/(p̸₁ - q̸₂ - m)] ε̸₁ u₁) = -i4πe² ( G_S )

The complete matrix element is the sum of these, so that the cross section becomes The problem now is actually to compute the matrix elements for R and S.

First R will be considered. Using the identity the matrices may be removed from the denominator of R giving The denominator is seen to be 2mω from the following relations: The matrix elements for the various spin and polarization combinations can be calculated straightforwardly from this point. But certain preliminary manipulations will reduce the labor involved. Using the identity it is seen that But p₁ has only a time component ω and ε₁ only a space component, so p₁ · ε₁ = 0. Knowing that q̸₁ u₁ = m u₁, it is seen that and this is the matrix element of the first term of R. It is also the negative of the matrix element of the last term of R, so R may be replaced by the equivalent 98 QUANTUM ELECTRODYNAMICS By an exactly similar manipulation, the S matrix is equivalent to Substituting q̸₁ = (ω - ω') and q₂ = ω' (y₂ + x₂ cos θ + y₂ sin θ) and trans- posing the 2×1 factor, the complete matrix may be written A still more useful form is obtained by noting that p₁ anticommutes with q₁ (ε₁ · q₁ = 0) and with q₂ and that = 2ε₂ · ε₁ - p₁ · q₂. Thus, Using this form of the matrix, the matrix elements may be computed easily.

For example, consider the case for polarization: ε₁ = y₁, ε₂ = y₂ cos θ + z₂ sin θ.

This corresponds to cases (A) and (B") of Table 19 and will be de- noted by (AB"). The matrix is - - 2m(R+ S) = my₂ (y₂ cos θ + z₂ sin θ)[y₁(1 - cos θ) + y₂ sin θ]

since ε₂ · ε₁ = 0. Expanded this becomes 2m(R+ S) = -y₂[ y₂y₁ cos θ(1 - cos θ) + cos θ sin θ + y₂ sin θ(1 - cos θ)

- z₂ sin θ]

where the anticommutation of the γ's has been used. In the case of spin- up for the incoming particle and spin down for the outgoing particle (s₁ = +1), s₂ = -1), the matrix elements =: may be found by reference to Table 13-I. But note that in this problem p₁ = p₁ g⁰ + iγ = 0 since particle 1 is at rest. Hence the final matrix element for this case, polarization (AB"), spin s₁ = +1, s₂ = -1, is

## QUANTUM ELECTRODYNAMICS

2m (R+ S) u₂ = -(1 - cos θ)iγ¹p₂ + sin θ γ² + iγ¹ The results for the other combinations of polarization and spin are obtained in the same manner and will only be presented in tabular form (Table 22-1).

They may be verified as an exercise.

For any one of the polarization cases listed, |M|² is the sum of the square amplitudes of the matrix elements for outgoing spin states averaged over in- coming spin states. But this is seen to be simply the square magnitude of the non-spin matrix element listed under the appropriate polarization case.

For example, in case (AA", By employing the relation and the square magnitudes of the matrix elements for the various cases reduce, after considerable amount of algebra, to the expressions given in Table 20-2.

AB" [ (ω² + ω'²) / (ω ω') ] + ...

BB' [ (ω² + ω'²) / (ω ω') + 4 ] cos θ ...

It is clear that all four of these formulae may be written simultaneously in the form Note that these formulas are not adequate for circular polarization, since, if ε₁ were, for example, 1/√2 (iy₁ + y₁), it is seen that because of the phas- INTERACTION OF PARTICLES WITH LIGHT l01 ing represented by the imaginary part, all the calculations must be carried out before squaring the matrix elements in order to get the proper interference.

Finally the cross section for scattering with prescribed plane polarization of the incoming and outgoing photons is This is the Klein-Nishina formula for polarized light. For unpolarized light this cross section must be averaged over all polarizations.

It is noted that diagram cases such as Fig. 20-1 have been included in the previous derivation as a result of the generality in the transformation of Kμ(2, X) to momentum representation. In fact, all diagram cases have been included except higher-order effects to be discussed later. (They corre- spond to emission and reabsorption of a third photon by the electron, such as in Fig. 20-2.)

Twenty-first Lecture Discussion of the Klein-Nishina Formula. In the "Thompson limit,"

ω << m. Then the electron picks up very little energy in recoil, and ω' ≈ ω.

This can be seen from the relation In this limit, the Klein-Nishina formula gives 102 QUANTUM ELECTRODYNAMICS which is the Rayleigh-Thompson scattering cross section. Note that ω is still very large compared to the eigenvalues of an atom, in accordance with our original assumptions for Compton scattering.

The same result is obtained by a classical picture. Under the action of the electric field of the photon E = E₁ exp (iωt), the electron is given the acceleration Classically, an accelerated charge radiates to give the scattered radia- tion e (reduced acceleration projected on plane 1 to E_scat = ----- R line of sight)

The scattered radiation polarized in the direction ε₂ is determined by the component of the acceleration in this direction. The intensity of the scat- tered radiation of polarization ε₂ is then (per unit solid angle and per unit incident intensity)

The customary factors of c may be inserted in Eq. (22-11) as follows (σ is an area or length squared): σ₂ = (re/ℏ)² = classical length squared Averaging over all polarizations, it is often desired to have the scattering cross section for a beam re gadless of the incoming or outgoing polarization. This can be obtained by summing the probabilities over the polarizations of the outgoing beam and averaging over the incoming beam. Thus, suppose the incoming beam has polarization of t pA. The probabilities (or cross sections) for the two possible types of outgoing polarization, A' and B' can be symbolized as U*a nd AS. The total probability for scattering a photon of either polarization is AA' + AB*. Then suppose the incoming beam is equally likely to be polarized as type A or type B. The resulting probability can be obtained as the sum 1/2 (probability if type A) + 1/2 (probability if type B). This is the situation for unpolarized incoming beam, and gives

cr (averaged over polarizations) = (1/2)(A*A' + B*B') + (1/2)(A*B' + B*A')

E, on the other hand, the polarization of the outgoing beam is measured (still with an unpolarized incoming beam), its dependence on frequency and scattering angle is given by the ratio

Probability of polarization type A' / Probability of polarization type B' = (1/2)(AA' + BA') / (1/2)(BB' + AB')

The forward radiation (θ = 0) remains unpolarized, but a certain degree of polarization will be found in light scattered through any nonzero angle. In the low-frequency limit (ω << m), the polarization is complete at θ = π/2. Thus an unpolarized beam becomes plane-polarized when scattered through 90°.

Total scattering cross section: If the cross section (averaged over polarizations) given in Eq. (21-3) is integrated over the solid angle

the total cross section for scattering through any angle is obtained. So, from Eq. (21-3),

and the variable ω2 goes between the limits mω1/(2ω1 + m) and ω1 as cos θ goes from -1 to +1. Equation (21-3) can be written

where the last five terms replace -sin² θ = cos²θ - 1 using Eq. (21-5).

Simple integrations yield

h the high-frequency limit (ω1 >> m)

Cf. Walter Heitler, "Quantum Theory of Radiation," 3rd ed., Oxford, 1954; and B. Rossi and K. Greisen, Phys. Rev., 62, 121 (1942).

## § Cf. Heitler, op. cit., p. 53

Thus Compton scattering is a negligible effect, at high frequencies, where pair production becomes the important effect.

From the quantum-electrodynamical point of view, another phenomenon completely analogous to Compton scattering is two-photon pair annihilation. Two photons are necessary (in the outgoing radiation) to maintain conservation of momentum and energy when pair annihilation takes place in the absence of an external potential. This interaction can be diagrammed as shown in Fig. 21-1. This figure should be compared to that for Compton scattering (Lecture 20). The only differences are that the direction of photon is reversed, and, since particle 2 is positron, -p2 is the (momentum of positron). So write

S1 = (E-, p-), S2 = (E+, -p+)

where the energies E- and E+ of the electron and positron are both positive numbers. The conservation law gives

p+ = p- + k1 + k2  (just as for Compton scattering, but the direction of k is reversed), so the matrix element for this interaction is

M1.

The second possibility, indistinguishable from the first by any measurement, is obtained from the first by interchanging the two photons (see Fig. 21-2); again note similarity to Compton scattering.

Immediately, the matrix element is

M2.

The sum of the two matrix elements squared and the density of final states gives the cross section

σ (velocity of positron) = 2α²/(2E- 2E+ 2ω1 2ω2) |M1 + M2|² × (density of states)

In a system where the electron is at rest and the positron is moving, the density of final states is

Since particle 2 is a positron, p2 = -p+, so the conservation law, Eq. (21-4),

gives

p+·p* = p+·(p- + k1 + k2)

Then

This reduces to

Taking the velocity of the positron as v = |p+|/E+, the cross section is

σ = (2π)² α² dΩ1/[12E- · 2E+ |p+|³/(2π)³ m(E+ + m)] × |M1 + M2|²

From a comparison of the diagrams, it is clear that the matrix elements for pair annihilation are the same as the matrix elements for the Compton effect if the sign of ω1 is changed. In the cross section, this amounts to changing the sign of ω1. Then the cross section is

in analogy with the Klein-Nishina formula.

## ANNIHILATION FROM REST

The formula for positron-electron annihilation derived in lecture 21 diverges as the positron velocity approaches zero (as 1/v; this is true for other cross sections when a process involves absorption of the incoming particle, and is the well-known 1/v law). To calculate the positron lifetime in an electron density ρ (resultant from the previously calculated cross section was for an electron density of one per cubic centimeter) as v → 0, we use

plus the fact that as v → 0, E+ → m and ω1 = ω2 = m (when the electron and positron are both approximately at rest, momentum and energy can be conserved only with two photons of momenta equal in magnitude but opposite in direction). Thus

where θ = angle between directions of polarization of the two photons (cos θ = ε1·ε2). The sin² θ dependence indicates that the two photons have their polarizations at right angles. To get the probability of transition per second for any photon direction and any polarization, it is necessary to sum over solid angle dΩ = 4π and average over polarizations (sin² θ = 2/3), giving

factors of e and E replaced where required), where r₀ = classical electron radius, and τ = mean lifetime.

Problems: (I) Obtain the preceding result directly by using matrix elements for an electron and positron at rest. Show that only the singlet state (spins antiparallel) can disintegrate into two photons. The triplet state disintegrates into three photons and has a longer lifetime (see the next problem).

(II) Find the mean time required for a positron and electron to disintegrate into three photons (spins must be parallel). The following procedure is suggested: (1) set up formula for rate of disintegration; (2) write M in the simplest possible form; (3) make a table of matrix elements (same as Table 13-1 but with ω = m/2); (4) find the matrix element M for eight polarization cases; (5) find the rate of disintegration for each case; (6) sum the disintegration rates over polarizations; (7) obtain the photon spectrum; (8) obtain the final disintegration rate by integrating over photon spectrum and angle; and (9) compare with Ore and Powell.†

(III) It is known that the matrix elements should be independent of a gauge transformation εμ' = εμ + α kμ, where α is an arbitrary constant and kμ is the momentum of a photon whose polarization is εμ or εμ'. Show that substituting εμ for εμ in the matrix elements for the Compton effect gives M = 0.

When an electron passes through the Coulomb field of a nucleus it is deflected. Associated with this deflection is an acceleration which, according to the classical theory, results in radiation. According to quantum electrodynamics, there is a certain probability that the incident electron will make a transition to a different electron state with a photon emitted, while in the field of the nucleus. Interaction with the field of the nucleus is necessary to satisfy conservation of energy and momentum. That is, the electron cannot emit a photon and make a transition to a different electron state while traveling along in a vacuum. Figure 22-1 shows the process and defines angles that arise later.

The Coulomb potential of the nucleus will be considered to act only once (Born approximation). The validity of this approximation was discussed in Lecture 16. There are two (indistinguishable) orders in which the bremsstrahlung process can occur: (a) the electron interacts with the Coulomb field and subsequently emits a photon, or (b) the electron first emits a photon and then interacts with the Coulomb field. The diagrams for these processes are shown in Fig. 22-2. The interaction with the nucleus gives momentum q to the electron. Conservation of energy and momentum requires

electron 1 → electron 2 + photon + Coulomb field of the nucleus

In Lecture 18 it was shown that the Fourier transform of the Coulomb potential was proportional to δ(q₄), since the potential is independent of time. This means that only transitions for which q₄ = 0 occur, or energy must be conserved among the incident electron, final electron, and photon. Thus E1 = E2 + ω. The transition probability is given by

Since the nucleus is to be considered infinitely heavy,

Notice that there is a spectrum of photons; that is, the photon energy is not determined (as it was in the Compton effect, for example). Letting "S12" = (G2M U$),

where the first term comes from Fig. 22-2a and the second term from Fig. 22-2b. The explanation of these factors in the first term, for example, is, reading from right to left, that an electron initially in state u1 is scattered by the Coulomb potential acquiring an additional momentum q, the electron moves as a free particle with momentum p1 + q until it emits a photon of polarization εμ. We then ask: is the electron in state u2? For the Coulomb potential

(see Momentum representation, Lecture 18) in a coordinate system in which the nucleus does not move. [For potential other than Coulomb, use appropriate v(q), the Fourier transform of the space dependence of the potential.]

Rationalizing the denominator of the matrix,

The outgoing photon can be polarized in either of two directions, and the incoming and outgoing electron each have two possible spin states. The various matrix elements can be worked out using Table 33-1, exactly as was done in deriving the Klein-Nishina cross section in Lecture 20. Nothing new is involved, so we omit the details. After (1) summing over photon polarizations, (2) summing over outgoing electron spin states, and (3) averaging over incoming electron spin states, the following differential cross section is obtained:

dσ = (sin θ₂ dΩ₂ sin θ₁ dΩ₁) / (2p₁p₂ sin θ₁ sin θ₂ cos Φ (4E1E2ω)²) × [ (2E₁E₂ + 2ω²) - 2ω² (p₁² sin²θ₂ + sin²θ₁) ] / [ (E₂ + p₂ cos θ₂)(E₁ + p₁ cos θ₁) ]

An approximate expression with a simple interpretation in terms of the Coulomb elastic scattering cross section can be obtained when the photon energy is small (small compared to rest mass of electron but large compared to electron binding energies). Writing the matrix (22-3) in terms of 4 instead of @ using the relationships gOPlz = -$z$ + 2~3 * p2 , $14 =: -661 + Ze PI, and neglecting 4 in the numerator, since it is small, this becomes where use is made of the fact that the matrix element of M between states u2 and ul is to be calculated and uz$z= dtui = mule.

The cross section for photon emission can then be written. The first bracket is the probability of transition for elastic scattering (see Lecture 161, so the last bracket may be interpreted as the probability of photon emission in frequency interval dw and solid angle da, if there is elastic scattering from momentum pi to pz.

Problem: Calculate the amplitude for emission of two low-energy photons by the forward-scattering method. Neglect q's in the numerator but not in the denominator.

Answer: Another factor, similar to that in the preceding equations, is obtained for the extra photon.

It is easily shown that a single photon of energy greater than 2m cannot create an electron positron pair without the presence of some other means of conserving momentum and energy. Two photons could get together and create a pair, but the photon density is so low that this process is extremely unlikely. A photon can, however, create a pair with the aid of a field, such as that of a nucleus, to which it can impart some momentum. As with bremsstrahlung, there are two indistinguishable ways in which this can happen: (a.) The incoming photon creates a pair and subsequently the electron interacts with the field of the nucleus; or (b) the photon creates a pair and the positron interacts with the field of the nucleus. The diagrams for these alternatives are shown in Fig. 22-3. The arrows in the diagram indicate that $l is the positron momentum and yJ2 is the electron momentum. Notice that, with respect to the directions that the arrows point (but without regard to direction of increasing time), these diagrams look exactly like those for the bremsstrahlung process. Starting with in case (a), the particle is first scattered by the Coulomb potential and then by the photon; in case the order of the events is reversed. The difference between pair production and bremsstrahlung, when the direction of time is taken into account, is (1) is a positron state (an electron traveling backward in time), and (2) the photon is absorbed rather than emitted. As a result, the bremsstrahlung matrix elements can be used for this process if 6% is replaced by --$, and 4 by -4.

The $+ is the positron momentum and is the momentum of the absorbed photon. The density of final states is different, of course, since the particles in the final state are now a positron and electron. Thus = (1/2a)(~e~/~'e)2' @,p- sin 8, dB, sin 8- d8- d+/w3) where the brackets are the same as for bremsstrahlung, Eq. (22-52, except for the following substitutions:

E+ P- for P2 -6- for O2 E- for -P+ Pi -8, for 6- -E, for E, -W for W

Figure 22-4 defines the angles (rS, = angle between electron-photon plane and positron-photon plane).

positron

## A METHOD OF SUMMATION OVER SPIN STATES

By using current methods of computing cross sections, one first arrives at a cross section for "polarized" electrons, that is, electrons with definite incoming and outgoing spin states. In practice it is common that the incident beam will be "unpolarized" and the spins of the outgoing particles will be unobserved. In this case, one needs the cross section obtained from that for "polarized" electrons by summing probabilities over final spin states and averaging this sum over initial spin states. This is the correct process since the final spin states do not interfere and there is equal probability of initial spin in either direction. Formally, if

## INTERACTION OF PARTICLES WITH LIGHT

one needs @ - 1 C C I(u2~uill~ 2 spins I spins 2 where means the sum over final spin states for only one sign of the spins 2 the energy, that is, over only two of the four possible eigenstates. Similarly, is the sum over initial spins for one sign of the energy. The purpose spins I now is to develop a simple method for obtaining these sums.

In accordance with the usual rule for matrix multiplication, the following is true: (G2~u(IU) I~u2=) 2rn(G2~~u2) all Y where A and B are any operators or matrices, the 2m factor on the right arises from the normalization uu = 21x1, and the sum is over all eigenstates represented by ul. But the states u, which we want in Eq, (23-1) are not all states, just those satisfying IzJiut = mu$. That is, they belong to the eigenvalue +m of the operator &. Since 612 = rnZF$ l also has the eigenvalue -m, that is, there are two more solutions 05: &U = -mu which, together with the two we wish in Eqi, (23-1) bring the total to four. Let us call the latter "negative eigenvalue" states.

Now, if in Eq. (23-2) the matrix elements of B were zero in negative eigenvalue states, this would be the same as , that is, just over positive eigenvalue states. So consider spins 1 (;2~u,)(;l@f+m)~uz) = (:2~(dt+m)~u2)2m all U, But r u V i(Iljf+m) = Q for negative eigenvalue states = ui(2m) for positive eigenvalue states so the preceding sum also equals (G 2~ ul)am(GBfu z) spins 1 Cancelling the 2m factors, this gives C (Gz~u!)(';l Buz) = (G~AMI + m)Buz) spins 1 (pJi -t- m) is called a projection operator for obvious reasons. Similarly it can be shown that

## QUANTUM ELECTRODYNAMICS

spins 2 all U, where X is again any matrix. Remembering the normalization &u2 = 2m. it is seen that the last sum is just the trace or spur of the matrix (;plj2+ m)X. Note that the order of X and -t- m is immaterial.

Finally, when one wants collection and specialization of the previous results is seen to give spin 1 spins 2 spins 1 spins 2 where the last notation means the spur of the matrix in the brackets. It is true whether &, &12 represent electrons or positrons.

The following list of the spurs of several frequently encountered matrices may be verified easily:

It is also true that the spur of the product of any odd number of daggered operators is zero.

## INTERACTION OF PARTICLES WITH LIGHT

As an example, the case of Coulomb scattering will be treated using this technique. The cross section for polarized electrons was previously found to be Therefore, since = y,, the cross section for unpolarized electrons is, by Eq, (23-31, The spur can be evaluated immediately from Eq. (23-5) with m2 = m4 O and - 5; -g4 = p14 = yt. Another way is: Since ytdI = 2Ei ~%ytit, it is seen that Using a few of the formulas listed previously, the spur of this matrix is seen to be But p% * p2 = E - p1 a h, p% * p2 = cos 8, and Et = .E2, so this is 4~~- + 4m2+ cos B Also rn2 = E' ,'p so that finally the cross section becomes @mpok = 1/2 (Z~@'/Q[~)8 + ~4p2 ~(cos @ 111 where v2 = pZ/~Z. This is the same cross section obtained previously by other methods.

The cross sections for the pair production and bremsstrahlung processes contain the factor [v(Q)wI'h,e re V(&) is the momentum representation of the potential; that is, which for a Coulomb potential is where Q is the momentum transferred to the nucleus or p% - p2 - q.

116 QUANTUM ELECTRODYNAMICS

Clearly V(Q) gets large as Q gets small. The minimum value of Q occurs when all three momenta are lined up (Fig, 23-1: Pr P a FIG, 23-1 For very high energies E m, so that in this case - - From this it is seen that Qmin O as Er 00 This shows clearly why the cross sections for pair production and bremsstrahlung go up with energy. From the integral expression for V(Q) it is seen that the main contribution to the integral comes when R 1/Q. So as Q becomes small the important range of R gets large. It is in this way that screening of the Coulomb field becomes effective. The value of for a continuum process can be estimated from the foregoing formula. The atomic radius is given roughly by ao~-'/', where a . is the Bohr radius. Thus if or, what is the same, then screening effect will be important, and vice versa for the opposite inequalities. If from this estimate screening would appear to be important, one should use the screened Coulomb potential. It gives the result where F(Q) is the atomic structure factor given by and nm) is the electron density as a function of R.

## INTERACTION OF PARTICLES WITH LIGHT

Problem: In discussing bremsstrahlung it was found that the cross section for emission of a low-energy photon can be approximated as where cfo is the scattering cross section (neglecting emission). Now consider an energetic Compton scattering in which a third, weak photon is emitted. The three diagrams are shown in Fig. 24-1 FIG, 24-1. Show that the cross section for this effect is given by Eq. (24-l), with the Klein-Nishina formula replacing remembering to assume q small, ) potential region Interaction of Several Electrons Even though the Dirac equation describes the motion of one particle only, we can obtain the amplitude for the interaction of two or more particles from the principles of quantum electrodynamics (so long as nuclear forces are not involved). First consider two electrons moving through a region where a potential is present and assume that they do not interact with one another (see Fig, 24-2). The amplitude for electron a moving from 1 to 3, while electron b moves from 2 to 4 is given the symbol K(3,4; U). If it is assumed that no interaction between electrons takes place, then K can be written as the product of kernels K,(')(3,1) K,(& )(4,2), where the superscript means that K,(') operates only on those variables describing particle a, and similarly for K,(~). A second type of interaction gives a result indistinguishable from the first by any measurement in accordance with the Pauli principle. This differs from the first case by the interchange of particle coordinates between positions 3 and, 4 (see Fig.

Hour the Pauli principle says that the wave function of a system composed of several electrons is such that the interchange of space variables for two particles results in a change of sign for the wave function. Thus the amplitude (including both possibilities) is K = K₁(s₁) K₂(s₂) K₁⁻¹(s₂) K₂(s₁) ~, (~"(s,2)),

A similar situation arises in the following occurrence. Initially, one electron moves into a region where a potential is present. The potential creates a pair. Finally one positron and two electrons emerge from the region. There are two possibilities for this occurrence, as shown in Fig. 24-4. Again, the total amplitude for the occurrence is the difference between the amplitudes for the two possibilities.

The probability of this occurrence, or the previous, or any other similar occurrence is given by the absolute square of the amplitude times the number Pv. The Pv is actually the probability that a vacuum remains a vacuum; because of the possibility of pair production, it is not unity. The Pv can be computed by making a table of the probabilities of starting with nothing and ending with various numbers of pairs, as is shown in Table 24-1.

## TABLE 24-1

The sum of all these probabilities must equal unity, and Pv is determined from this equation. The magnitude of Pv depends on the potential present. So the "probabilities" (taken as merely the squares of amplitudes, that is, omitting the Pv factor) are actually relative probabilities for various occurrences in a given potential.

Use of Δ_s(s₁, s₂). For the present, the existence of more than one possibility for an occurrence (the Pauli principle) will be neglected. The total amplitude can always be derived from one by interchanging proper space variables, making the corresponding changes in spin, and summing all the amplitudes so obtained.

The nonrelativistic Born approximation to the amplitude for an interaction is

where, from earlier lectures,

and

Note that t₅ = t₆ since a nonrelativistic interaction affects both particles simultaneously. The potential for the interaction is the Coulomb potential.

Separate variables may be used for t₅ and t₆, if the function δ(t₅ - t₆) is included as a factor. Then

where the differential dτ includes both space and time variables. It is conceivable that the relativistic kernel could be obtained by substituting K_s for K, and introducing the idea of a retarded potential by replacing δ(t₅ - t₆)

by δ(t₅ - t₆ - r₅₆). However, this δ function is not quite right. Its Fourier transform contains both positive and negative frequencies, whereas a photon has only positive energy. Thus

To correct this, define the function

Δ_s(X) = exp(-iωX) dω/π

which contains only positive energy. The value of the function is determined by the integral,

Δ_s(X) = lim (1/πi)(X + iε)

ε → 0 = δ_s(X) + (1/πi)(principal value 1/X)

Abbreviating t₅ - t₆ as T and r₅ - r₆ as R, and taking account of the fact that both t₅ > t₆ and t₅ < t₆ are possible, the retarded potential is

Exercises: (1) Show that

Defining t₂ - t₂ as a relativistic invariant, the potential is

(2). e²Δ_s(s). Another term which must be included is the magnetic interaction, proportional to -∇₂ - * ∇₆. In the notation used for the Dirac equation, this product is -α₂ · α₆. It will be found convenient to express this in the equivalent form -(βγμ)₂ · (βγμ)₆, and in this notation the retarded Coulomb potential is proportional to P_μ₂ P^μ₆. These P's come from the use of the relativistic kernel. Thus the complete potential for the interaction becomes

and then the first-order kernel is

Here the superscript on γ^μ indicates on which set of variables the matrix operates, just as for the superscripts on K.

The occurrence represented by this kernel can be diagrammed as in Fig. 24-5. This represents the exchange of a virtual photon between the electrons. The virtual photon can be polarized in any one of the four directions, t, x, y, z. Summation over these four possibilities is indicated by the repeated index μ. The integral expression for

the kernel, Eq. (24-2), implies that the amplitude for a photon to go from 5 to 6 (or from 6 to 5, depending on timing) is Δ_s(s₅₆, t₅₆). Equation (24-2) can be taken as another statement of the fundamental laws of quantum electrodynamics.

(2) Show that

Thus, in momentum space,

From the results of the first lecture, it is evident that the laws of electrodynamics could be stated as follows: (1) The amplitude to emit (or absorb) a photon is eγ^μ, and (2) the amplitude for a photon to go from 1 to 2 is Δ_s(s₁₂, t₁₂), where

in momentum representation. It is interesting to note that Δ_s(s₁₂, t₁₂) is the same as I_s(s₁₂, t₁₂), the quantity appearing in the derivation of the propagation kernel of a free particle, with m, the particle mass, set equal to zero. A more direct connection with the Maxwell equations can be seen by writing the wave equation. ∇²φ = 4πρ in momentum representation.

We now consider the connection with the "rules" of quantum electrodynamics given in the second lecture. The amplitude for a to emit a photon which b absorbs will now be calculated according to those rules (see Fig. 25-1). The amplitude that electron a goes from 1 to 5, emits a photon of polarization ε and direction K, then goes from 5 to 3 is given by

whereas the amplitude that b goes from 2 to 6, absorbs a photon of polarization ε' and direction K at 6, then goes from 6 to 4 is given by

The amplitude that both these processes occur, which is equivalent to b absorbing a photon if t₆ < t₅, is just the product of the individual amplitudes. If a absorbs a photon, the signs of all the exponentials in the preceding amplitudes are changed and t₆ must be greater than t₅.

To obtain the amplitude that any photon is exchanged between a and b, it is necessary to integrate over photon direction, sum over possible photon polarizations, and integrate over t₅ and t₆, subject to the aforementioned restrictions. In summing over polarizations, ε_α will be replaced by γ^μ_α and a summation over μ will be taken. This amounts to summing over four directions of polarization, something that will be explained further. Thus

Comparing this with the result of the last lecture, it must be that

This can be written in a form which makes the space-time symmetry evident by using the Fourier transform

exp(-iK |t/ ) = ∫ (ω/ K² + iε) exp(-iωt) dω/2π

so that the foregoing equation becomes

and comparing this with the result of the last problem of Lecture 24 establishes that the rules given in Lecture 2 are consistent with relativistic electrodynamics developed in the last lecture.

The theory will now be used to obtain the electron-electron scattering cross section. The diagrams for the two indistinguishable processes are shown in Fig. 25-2.

The amplitude expressed in momentum representation is obtained as follows: Write Eq. (25-3) [with the aid of Eq. (25-4)] as

Since electron state 1 is a plane wave of momentum and electron state 3 is a plane wave of momentum p, it is clear that in momentum representation the spinor part of the first bracket will become (ū₃γ^μu₁) and the spinor part of the second bracket will become (ū₄γ^μu₂). Integration over r₅ and r₆ produces the conservation laws given at the bottom of the diagrams. Dropping the integration over q puts the photon propagation in momentum representation directly. Thus the matrix element can be written

The first term comes from diagram R, the second from diagram S, and the summation over μ is implied. In the center-of-mass system, the probability of transition per second is

(see Density of Final States, Lecture 19). The method of Lecture 23 can be used to average over initial spin states and sum over final spin states. For example, the sums over spin states that result from R by R matrices and R by S plus R by S matrices are

By judicious use of the spur relations given in Lecture 23 the following differential cross section is obtained (alternatively, Table 13-1 could be used to calculate M directly):

where x = E'/m₀. This is called Møller scattering (see Fig. 25-3).

Problems: (1) Calculate positron-electron scattering by the preceding method.

(2) Find the cross section for a photon to produce a positron-electron pair. Assume that the pair satisfies the Dirac equation with s = 1/2 and no anomalous moment. Remember that the particles are distinguishable and hence there is no interchange of particles.

(3) Calculate the electromagnetic electron-proton scattering cross section assuming the proton has no structure but does have an anomalous moment. The Dirac equation for a proton is (see page 54)

Thus the perturbation potential can be written as (see page 54)

and the coupling with a photon is

The Sum over Four Polarizations. In classical electrodynamics, longitudinal waves can always be eliminated in favor of transverse waves and an instantaneous Coulomb interaction. This is the approach used by Fermi (see Lecture I), and it will now be demonstrated that the sum over four polarizations is also equivalent to transverse waves but plus an instantaneous Coulomb interaction. Instead of choosing space directions x, y, z, one direction parallel to K (photon momentum) and two directions transverse to K are taken. The matrix element can be written

For the proton μ = 1.1896.

where γ_μ is the γ matrix for the K direction and γ_⊥ represents the γ matrix in either of the transverse directions. The matrix element of γ_μ is zero in general (from the argument for gauge invariance). Thus γ_μ can be replaced by γ_⊥ with the result

Now 1/K² represents a Coulomb field in momentum space and γ^0 is the fourth component of the current density or charge, so that the first term represents a Coulomb interaction while the second term contains the interaction through transverse waves.

In our special case, it is is easy to see directly, for example, Discussion and Interpretation of Various "Correction" Terms Twenty-sixth Lecture In many processes the behavior of electrons in the quantum-electrodynamics theory turns out to be the same as predicted by simpler theories save for small "correction" terms. It is the purpose of the present lecture to point out and discuss a few such cases.

## ELECTRON-ELECTRON INTERACTION

The simplest diagrams for the interaction are shown in Fig. 28-1. The amplitude for the process has been found to be representaton is not yet in equality, since the normalizing factors are different in the two expressions.

To obtain the correct equation proceed as follows: First, it is clear that the probability of the occurrence depends only on the interval in space and time between points 3 and 4, and not at all on the absolute values of the space and time variables. So suppose a change of variable is made so that dξ represents the element of interval (in space and time) between 3 and 4.

Then write the integral in Eq. (27-1)

where it is clear that the operators K, and G, depend only on the interval 3-4.

Second, expression (27-2) contains the time-dependent part of the wave function, exp (-iE,t), because it was assumed that the wave functions used did not contain time factors. In Eq. (27-3), f (3), f (4) do already include the time-dependent part, so it should be omitted in Eq. (27-2).

Third, the normalization of wave functions is different for the two ap- proaches. For the development that led to Eq. (27-2), the normalization was used. For the present development the normalization is Thus, to establish an equality, expression (27-3) must still be divided by the normalizing integral of Eq. (27-4).

The resulting expression is The integral over d3xs gives a V which cancels with the denominator, and the integral over dt3 gives a T which cancels with the left-hand side, so finally Note that the integral is relativistically invariant. Further, since p is the same before and after the perturbation and E = m2 + p2, the change in E can be taken as a change in the mass of the electron, from Using this expression, and transforming to momentum space, The integrand may be rewritten; from using εu = mu and the relations of Lecture 10. Then Eq. (27-6) becomes This integral is divergent, and this fact presented a major obstacle to quantum electrodynamics for 20 years. Its solution requires a change in the fundamental laws. Thus suppose that the propagation kernel for a photon is (1/k²)c(k²) instead of just (1/k²), where c(k²) is so chosen that c(0) = 1 and c(k²) → 0 as k² → ∞. In space representation the modification takes the form The new function f₁ differs significantly from δ only for small inter- vals. This is clear from the fact that if the high-frequency components are removed from the Fourier equation of a function, only the short-range de- tails are modified. In the present case the size of the interval over which the function is modified can be described roughly as follows: Consider a large number, Λ², and suppose that so long as k² << Λ², c(k) ≈ 1. Then from the exponential term, differences will occur when the interval s² ≈ 1/Λ. Call this value a², and the general behavior of f₁ is shown by Fig. 27-2. Thus a² is sort of a "mean width" of f₁. If a² << 1, as assumed, then when which is the size of the interval. The significance of the form of f₁(s²) can be understood from the following. The original function, δ⁺(s²), differs from zero only when s² = t² - r² = 0. That is to say, an electromagnetic signal can reach a point at distance r only at a time t such that t² - r²= 0 or t = r (i.e., the speed of light is 1). This is no longer true for f₁(s²). The depar- ture is obtained by a measure of 1/Λ. But, by Eq. (27-8), for all values of r, as long as this measure is negligible. Thus, depending on Λ, the laws will be found unaffected over any practical distance.

Choosing Λ² >> m², a practical (and general) representation of c(k²) is and the simple form is suggested.

From this, obtain the propagation kernel as The second term is that for the propagation of a photon of mass Λ; how- ever, the minus sign in front of the term has not been explained so far from this point of view.

A convenient representation for this kernel is the integral Introducing this kernel into Eq. (27-6') in place of 1/k² gives which can be written as the sum of two integrals, which differ only by having m or g in the numerator, that is, m or k₂ (since g = k·γ).

METHOD OF INTEGRATION FOR INTEGRALS APPEARING IN

## QUANTUM ELECTRODYNAMICS

We shall need to do many integrals of a form similar to the preceding one. A method has been worked out to do these fairly efficiently. We now stop to describe this method of integration.

Everything will be based on the following two integrals: In Eq. (27-11), to write a little more compactly, we use the notation f(X,k₂)

to mean that either X or k₂ is in the numerator, in which case, on the right- hand side the (1,0) is 1 or 0, respectively. To prove the first of these, note R. P. Feynman, Phys. Rev., 76, 769 (1949); included in this volume. Note that in the article d⁴k is equivalent to d⁴k/(2π)⁴ in our notation.

that, if k₂ is in the numerator, the integrand is an odd function. Thus the integral is zero. With 1 in the numerator, contour integration is employed.

Write the integral Then for L + k², there are poles at ω = ± √[(L + k²)/2 ∓ iε], and contour integration of ω gives with the contour in the upper half-plane. Two differentiations with respect to L give Then the remaining integral is which proves Eq. (27-11). If εu - p is substituted for the variable of integra- tion in Eq. (27-11), the result is By differentiating both sides of Eq. (27-13) with respect to Λ or with respect to p, there follows directly Further differentiations give directly successive integrals including one k₂ factor in the numerator and higher powers of (k² - 2p·k -Λ²) in the de- nominator.

SELF-ENERGY INTEGRAL WITH AN EXTERNAL POTENTIAL Last time it was found that the self-energy of the electron is equivalent "CORRECTION" TERMS and that this could also be expressed in terms of integrals.

It was also found that Using the definite integral the denominator of the integrand of Eq. (28-2) may be expressed as so that Eq. (28-2) becomes The integral over k can be done by using Eq. (28-3) with the substitutions εx for p and Λ(1 - x) for Λ, giving The integral over Λ is elementary and gives I = -2(32π²i)⁻¹ ∫₀¹ dx (1-x)²p² In [(1-x)Λ² + m²x²/m²x²]

When Λ² >> m², it is legitimate to neglect m²x² in the numerator [it is true that when x → 1, (1 - x)Λ² is not much larger than m²], but the interval over which this is true is so small, for Λ² >> m², that the error is small], so that, when the x integration is performed, The change in mass is [from Eq. (28-1)]

Since εu = mu and dU/dm = 2m, this can be simplified to Now (α/π) is about 1/137, so that even if Λ is many times m, the fraction change in mass will not be large. The interpretation of this result is as fol- lows. There is a shift in mass which depends on Λ and hence cannot be de- termined theoretically. One can imagine an experimental mass and a theo- retical mass which are related by All our measurements are of mexp, that is, self-action is included, and mth, the mass without self-action, cannot be determined. More accurately stated, a theory using mexp and the exact self-action term is equivalent to a theory using mth, and the self-action term calculated for a particle.

When the electron is free, the exact self-action term exactly cancels the Δm term and a theory using mexp is exactly correct. When the electron is not free, the exact self-action term is not quite equal to the Δm term and there is a small correction to a theory using mexp. This effect leads to the Lamb shift in the hydrogen atom, and, in order to calculate such effects, we shall now consider the effect of self-action on the scattering of an electron by an external potential.

## SCATTERING IN AN EXTERNAL POTENTIAL

The diagram for scattering in an external potential is shown in Fig. 28-1, and the relationships for this process, excluding the possibility of self- action, are as follows: Potential: φ(9) = η (μ²/εQ(Q)) for Coulomb potential Matrix element: M = -ie(f̄γᵤud)

Conservation relation: q = p₁ - p₂ First-order self-action will produce the diagrams shown in Fig. 28-2. The amplitude for process is obtained in the usual manner. For example, dia- gram I gives Rationalizing the denominators and inserting the convergence factor, this becomes This expression also happens to diverge for small photon momenta (k) (a result which has been called the "infrared catastrophe," but which has a clear physical interpretation, discussed later). Temporarily the k² under d⁴k will be replaced by (k² + Λ²min), where Λ²min << m², to make the inte- gral convergent. This is equivalent to cutting off the integral somewhere near k = Λmin, and the physical interpretation is left to Lectures 29 and 30.

To facilitate the integration over k, the following identity is used: since Λ² >> m² >> Λ²min. This substitution produces integrals of the form To evaluate these integrals, we make use of the identity where Δy = yΛ² + (1 - y)m². Performing integrations in the order, k, Λ, y, and using the appropriate integrals in Eq. (28-6) gives as the matrix element to be taken between states u₂ and u₁ -e² m² [...] + [...] + [...] + 2π X² min where r = ln (Λ/m) + 9/4 - 2 ln (m/Λmin) and 4m² sin²β = q².

It is shown in Lecture 30 that diagrams II and III (Fig. 28-2) produce a contribution M₂ + M₃ = -(e²/2π)rδ, which just cancels a similar term in M₁.

When q is small, β ≈ (q²)¹/²/2m, and the sum M₁ + M₂ + M₃ can be approxi- mated by The (46 - β4) can be written out But qp is the gradient operator so this can be written, in coordinate repre- sentation, [see Eq. (7-1)]. Reference to page 54 shows that the effect of a particle's having an anomalous magnetic moment is to subtract a potential μ FP from the ordinary potential γᵤAᵤ appearing in the Dirac equation. Since this is precisely what the first term of Eq. (28-10) does, one can say that this part of the self-action correction looks like a correction to the elec- tron's magnetic moment, so that Note that this result [and (28-9) and (28-10)] does not depend on the cutoff Λ, and hence Λ can now be taken to be infinity.

It has been shown that when a particle is scattered by a potential, the pri- mary effect is that of g, and that for diagr am I (Fig. 28-2) a correction term arises which is FIG. 28-2 R. P. Feynman, Phys. Rev., 76, 769 (1949); included in this volume.

It remains to show that the combined effect of diagrams II and II (Fig. 28-2), when considered along with the effect of the mass correction, is another correction term, just cancelling the first term in the preceding expression. It is recalled that the necessity for considering the effect of the mass correction together with the self-action represented in diagrams I, II, and III is that the theory being developed must contain the experimental mass rather than the ''theoretical'' mass.

Suppose that in the Dirac equation m is the theoretical mass, is replaced by m + Δm, where m is the experimental mass; then The mass correction Δm is just a number, so that in momentum representation it is a δ function of momentum. Hence from the form of the foregoing equation, it is seen to behave like a potential with zero momentum and involves no matrices. Diagrammatically its effect may be represented as in Fig. 29-1. The minus sign is used because the effect of the mass correction Δm is to be subtracted from the results obtained from diagrams X, IX, and XI (Fig. 28-2). For diagram II, the amplitude would appear to be "CORRECTION" TERMS and for diagram II' (Fig. 29-1), But the part of the amplitude for diagram II (Fig. 28-2) combined in the parentheses is just -A_μν, so that II and II' seem to cancel. A similar result applies for diagrams III and III'. This is an error, however, arising from the fact that both of these amplitudes are infinite, owing to the factor (4 - m) in the denominator. Hence their difference is indeterminate. But by subtracting them properly it will be found that their difference does not vanish.

The method proposed to accomplish this subtraction will, in fact, give the combined effect of the self-action and mass correction of both diagrams II and III and II' and III'. It is based on the fact that an electron is never actually free. An electron's history will have always involved a series of scatterings, as will its future. These scatterings will be considered as occurring at long but finite time intervals. It will be sufficient to calculate the effect of self-action and the mass correction between any two of these scatterings, since the result will evidently be the same between each pair of them. Then, the effect will account for simply by regarding a correction, equal to that calculated for one of the intervals between scatterings, as being associated with the potential at each scattering (number of intervals equals number of scatterings). Then, considering a single scattering event as here, this correction to the potential represents all the effects of diagrams II, III, II', and III'.

For an electron which is not quite free, p = m² exactly, but instead by the uncertainty principle, and T is the interval between scatterings.

Since T is large, E is a small quantity. Let β = (1 + ε)β₀, where β₀ is the momentum of a free electron.

If U and V are the momentum representatives of the scattering potential at a and b (any two scatterings), then the matrix of the amplitude to go from the initial state at a to the final state at b without any perturbations is up to terms of order ε. With the perturbations of self-action and mass correction, this matrix is (a) Without perturbation (b) With perturbation of self-action and mass correction It is the value of this matrix compared to that of the unperturbed matrix which gives the desired correction term (see Fig. 29-2).

Problem: Show that for two noncommuting (or commuting) operators A and B, the following expansion is true.

Using the result of the preceding problem, one can write.

"CORRECTION" TERMS so that the foregoing matrix becomes The first and last terms are identical, up to terms of order ε, hence may be cancelled. The integral in the second term has already been done essentially in computing diagram I (Fig. 28-1), except here replaces β₀, β₀, and β₀, so that U = V = β₀ in this case and gives the result To this order in ε the β in the numerator may be replaced by β₀. It is also noted that since β = m, so that the foregoing result may be written This is just -(e²/2π)ln times the matrix for no perturbation. Hence the correction term due to diagrams II, III, II', and III' is obtained simply by replacing the scattering potential β by -(e²/2π)ln β, as was stated earlier.

It should be noted that the difficulty in obtaining the proper subtraction of the self-action and mass corrections just clarified does not represent a "divergence" problem of quantum electrodynamics. It is a typical problem which could as well arise in nonrelativistic quantum mechanics if, for example, one chose some norm value as a reference of potential, that is, regarded a free electron as moving in a uniform normal potential. It may be easily verified that this would give rise to an "energy correction" for the free electron analogous to the mass correction involved here. Then in computing the amplitude for a scattering process where one used a "theoretical energy" and subtracted the effect of the "energy correction," the difference of indeterminate terms would appear if one used free-electron wave functions. In this simple case the indeterminate term would, indeed, cancel upon proper subtraction but in principle the problem is the same as the present one.

Finally, the complete correction term arising from self-action and mass correction is tan 2θ e² 2θ –M ln dd)

+ 8πn sin –2θ 2 RESOLUTION OF THE INFRARED "CATASTROPHE"

From the correction term just determined, it is seen that, to order e², the cross section for scattering of an electron with the emission of no photons is where σ₀ is the cross section for the potential β only. This cross section diverges logarithmically as λ_min → 0, and it is this divergence which was formerly referred to as the "infrared catastrophe."

This result, however, arises from the physical fact that it is impossible to scatter an electron, with the emission of no photons. When the electron is scattered, the electromagnetic field must change from that of a charge moving with momentum p₁ to that for momentum p₂. This change of the field is necessarily accompanied by radiation.

In the theory of bremsstrahlung, it was shown that the cross section for emission of one low-energy photon is Problem: Show that the integral over all directions and the sum over polarizations of the foregoing cross section is where sin² θ = q²/4m². Thus the probability of emitting any photon between k = 0 and k = K is which diverges logarithmically.

Therefore, the dilemma of the diverging scattering cross section actually arises from asking an improper question: What is the chance of scattering with the emission of no photons? Instead, one should ask: What is the chance of scattering with the emission of no photon of energy greater than K?

For there will always be some very soft photons emitted.

Then, effectively, what is sought in answer to the last question is the chance of scattering and emitting no photon, the chance of emitting one photon of energy below K, and the chance of two and more photons below K (but these terms are of order e⁴ and higher and hence are neglected).

Each of these terms is infinite, actually, but is kept finite temporarily by the artifice of the δ function. Their sum, however, does not diverge, as may be seen by gathering the previous results and by writing Chance of scattering and emitting no photon of energy > K, + (terms independent of order e⁴)

terms independent This does not depend on λ_min and hence resolves the "infrared catastrophe."

It has been shown by Bloch and Nordsieck that the same idea applies to all orders.

It is interesting that the largest term in the quantum-electrodynamic corrections to the scattering cross section, namely, may be obtained from classical electrodynamics, since such long wavelengths are involved. The other terms have small effects. To date, the scattering experiments have been accurate enough to verify the existence of the large term but not accurate enough to verify the exact contributions of the smaller terms. Hence they do not provide a nontrivial test of quantum electrodynamics.

These same considerations apply in any process involving the deflection of free electrons. The best way to handle the problem is to calculate everything in terms of the λ_min and then to ask only questions which can have a sensible answer as verified by the eventual elimination of the limit.

Problem: Prepare diagrams and integrals needed for the radiative corrections (of order e²) to the Klein-Nishina formula. Do as much as possible and compare results with those of L. Brown and R. P. Feynman.

## ANOTHER APPROACH TO THE SAME DIFFICULTY

Instead of introducing an artificial mass, assume no weak photons contribute. Thus we must subtract from the previous results the contributions of all photons with momentum magnitude less than some number k₀ >> λ_min.

The previous result is {1 + (e²/2π)[2 ln(m/λ_min)(1 – 2θ/tan 2θ)] + tan θ The term to be subtracted is We assume k₀ ≈ π or p, and neglect both K and the first two k² in this integral. Then using d = 2p – β', the integral is approximately Then This is the term to be subtracted from expression (30-1).

Using sin² θ = q²/4m², for small q, Eq. (30-4) becomes Subtracting this from Eq. (30-1), also with q small, gives The last term is [ln(λ_min/2k₀) + (13/24)].

## EFFECT ON ATOMIC ELECTRON

Consider the hydrogen atom with a potential V = e²/r and a wave function (R) exp(–iE₀ t) = ψ₀(x). Take the wave function to be normalized in the conventional manner. The effect of the self-energy of the electron is to shift the energy level by an amount The first integral is written down from Fig. 30-1. The second is the free-particle effect as noted in previous lectures. The kernel is not well enough determined to make exact calculation of this integral possible, An approximate calculation can be made with the form similar sum over negative energies for t2 < t1, The photon propagation kernel can be written as - - 6, (S,,$) = 4% $exp [-ik(ts t,) + ik(xZ xl)j d'k/2k(2~)-~ = 4n J'exp[+ik(tz -tl) + ik(xz-~$1d 3k/2k(2n)"

tz t1 If we use these expressions, Eq. (30-6) becomes = C + b f p (-iK * R)lon (E, + K - ~ ~ 1(a- Ple xp (iK * R)],@ +D dSk/4nk - exp (-iK . R )]@,( JE , I + U + E,)-~ --a [a exp (iK R)lno dS k/4nk - (Am term) (30-7)

+* This form implies the use of instead of and a4 = 1, = a.

Another approach to the motion of an electron in a hydrogen atom is the following. Consider the electron as a free particle intermittently scattered by the Coulomb potential. The scattering causes phase shift in the wave function of the order of Rydberg ) , Thus the period between scatterings Is of the order T = tf/Rydberg. Take the lower limit of the momentum of the "self-action" photons as very large compared to the Rydberg. Then it Is very probable that an emitted photon will be reabsorbed before two inter- actions between the electron: a the potential have taken place; it is very improbable for two or more scatterings to take place between emission and absorption (see Fig, 30-2). Then the correction to the potential is that com- puted in Eq. (30-5) for small q plus anomalous moment correction), This is in momentum space, To transform to ordinary space, use s2 P (4a2 - Q') $ M (aZ/at2 - v2)V Thus the correction is This correction is of greatest importance for the s state, since with a Coulomb potential V ~ =V 4 nze26m), and only in the s states is different from 0 at 1R = 0.

The choice of q is determined by the inequalities m ko >> Rydberg. A h, satisfactory value is = 137 Ryd. With such a the effect of photons of k c ko must b included. This will b done by separating the effect into the sum of three contributory effects. It will be seen that two of these effects 'CORRECTION" TERMS probable improbable FIG. 30-2 are independent of the potential V and thus are canceled by similar terms in the anomalous moment correction for a free particle, Thus for only one situation must the effect be computed. In all cases, since k is small, the nonrelativistic approximation to expression (30-7) may be used, (1) The contribution of negative energy states : Neglecting k with respect to m gives The matrix element for at is very small, and only the elements for at need be considered. Then the sum over negative states is If this sum is continued for +n, a negligible term of order vZ/c2 is added.

Thus the sum is approximately - C J [(aan()a no)/2m1 k2 dk/k = (a * k2 dW2mk negative states This is k-independent of V, and thus is canceled by a similar quantity in the anomalous moment term, -- (2) Longitudinal positive energy states (ap Q k/k) : As an exercise the reader may show

## QUANTUM ELECTRODYNAMICS

X@ k/k) (ik R) lno (En - Eg)/k fewf ik . R )fno * =: and the contribution of these terms summed over positive energy states gives - (E, - ~ ~ ) ~ex/pk (ik~ R1),, exp (-ik R),o (E, + k - E,)" dS k/4sk Writing H = p2/2m (V commutes with the exponent), this becomes This term is independent of V, and thus is also canceled by the anomalous mo- ment correction.

(3) Transverse positive energy states: Since ko is large compared to the size of the atom, the dipole approximation can be used. The general term in the sum of Eq, (30-7) becomes writing (E, + k - E@)-' = l/k - (E, - Ed/(En + k - Eo)k the term in l[k can be split off from the rest of the integral as a quantity independent of V and thus canceled by the anomalous moment correction. Further, by averaging over direction, in the nonrelativistic approximation. Thus the integral of Eq. (30-8) is Using the relation I. Cf. H, Bethe, Ph.ys, Rev., 72, 339 (1947)* and the fact that >> E, E@,o one part of the sum over transverse positive energy states is This cancels with the ln of Eq, (30-77, leaving the final correction as -anomalous moment correction This sum has been carried out numerically to be compared with the observed Lamb shift, CLOSED-LOOP PROCESSES, VACUUM POLARIZATION Another process which is still of first order in eZ has not been consid - ered in the scattering by a potential. Instead of the potential scattering the particle directly, it can do so by first creating a pair which subsequently annihilates, creating a photon which does the scattering. Diagram I (Fig.

32-1) applies to this process; diagram II applies to a similar process, with the order in time changed slightly, The amplitude for these processes is sum

## C 1

i4m2 ( ~ Z Y ~ ~ I ) $ J U Y~ (l spin states where u is the spinor part of the closed-loop wave function. The first pa- renthesis is the amplitude for the electron to be scattered by the photon; 1/q2 is the photon propagation factor; and the second parenthesis is the am- plitude for the closed-loop process which produces the photon. The expres- sion is integrated over p because the amplitude for a positron of mo- mentum is desired. In the sum over four spin states of u, two states take care of the processes of diagram I and two states take care of the proc- esses of diagram II. No projection operators are required, so the method of spurs may be used directly to give a form which correlates to X and E (so as usual it is not necessary to make separate diagrams for processes whose only difference is the order in time).

158 QUANTUM ELECTRODYNAMICS This integral also diverges, but a photon convergence factor, as used in the previous lectures, Is of no value because now the integral is over p, the mo- mentum of the positron. In the intermediate step, The method which has been used to circumvent the divergence difficulty is to subtract from this integral, a similar integral with m replaced by M. M is taken to be much larger FIG. 31-1 t b m , and this results in, a cutoff in the integral over p, When this is done, the amplitude is found to be (4m2 + ~ ~ "+ 1/1/913 ~ ~ (3 f -3)

?See R. P. Feynman, Phys. Rev,, 76, 769 (1949); included in this volume, "CORRECTION" TERMS where = 4m2 sin2 8, which, for small q, becomes Notice that (GzYpu l) = (G2$u1), SO that, considering only the divergent part of the correction, the effective potential is The 1 comes from the theory without radiative corrections, while the e2 term is the correction due to processes of the type just described, Thus the correction can be interpreted as a small reduction in the effect of all potentials, and one can introduce an experimental charge e0 and a theo- retical charge e related by where B(@) = -(e2/31h) ln (~/m)', in a manner analogous to the mass cor- rection described in Lecture 28. This is referred to as "charge renormal- ization." The other term, (v2 is more interesting, since it represents a perturbation 2e2/15r V). This correction is responsible for 21 Mc in the Lamb shift and the {ln fnn/2(E,- E@)]

+ (11/24)) term in (50-7" is replaced by (ln (m/2 (E, - Eo)j + (11/24) - (1/5)) .

The 115 term is due to the ""polarization of the vacuum."* One possible process for the scattering of light, and an indistinguishable alternative, is indicated by the diagrams in Fig. 32-22. The second diagram differs from the first only in the direction of the arrows of the electron lines, Reversing such a direction is equivalent to changing an electron to a posi- tron. Thus the coupling with each potential would change Since there are three such couplings, the amplitude for the second process is the nega- tive of that for the first. Since the amplitudes add, the net amplitude is zero.

In general, any closed-loop process of this type involving an odd number of couplings to a potential (including photon), has zero net amplitude, Problems: Set up the integrals for each of the two diagrams in Fig.

31-2 and show that they are equal and opposite in sign.

However, the higher-order processes shown in Fig. 31-3 can take place.

The amplitude for the process is FIG, 31-3 plus five similar terms resulting from permuting the order of photons, This integral appears to diverge logarithmically, But when all six alternatives are taken into account, the sum leaves no divergent term, More complicated closed-loop processes are convergent,

Pauli Principle and the Dirac Equation In Lecture 24 the probability of a vacuum remaining a vacuum under the influence of a potential was calculated, The potential can create and an- nihilate pairs (a closed-loop process) between times ti and t2, The amplitude for the creation and annihilation of one pair is (to first nonvanishing or-der)

The amplitude for the creation and annihilation for two pairs is a factor L for each, but, to avoid counting each twice when integrating over all dq and d t it is ,IJ2 /2, For three pairs the amplitude is lL3/3!. The total amplitude for a vacuum to remain a vacuum is, then, where the I comes from the amplitude to remain a vacuum with nothing happening. The use of minus signs for the amplitude for an odd number of pairs can be given the following justification in terms of the Pauli principle, Suppose the diagram for t ti is as shown in Fig, 31-4. The completion of this process can occur in two ways, however (see Fig, 32-5)- The second way can be thought of as obtained by the interchange of the two electrons, hence the amplitude of the second must be subtracted from that of the first, FIG. 31-4

## PAULI PRINCIPLE AND DIRAC EQUATIONS

FIG, 31-5 according to the Pauli principle. But the second process is a one-loop proc- ess, whereas the first process is a two-loop process, so it can be concluded that amplitudes for an odd number of loops must be subtracted, The prob- ability for a vacuum to remain a vacuum is P , ,-,,, = /c,I = exp (-2 real part of L)

The real part of L (Re. P. of L) may be shown to be positive, so it is clear that terms in the series must alternate in sign in order that this probability be not greater than unity.

We have, therefore, two arguments as to why the expression must be e'L, One involves the sign of the real part, a property just of K, and the Dirac equation. The second involves the Pauli pr inciple, We see, therefore, that it could not be consistent to interpret the Dirac equation as we do unless the electrons obey Fermi-Dirac statistics. There is, therefore, some connection between the relativistic Dirac equation and the exclusion principle. Pauli has given a more elaborate proof of the necessity for the exclusion principle but this argument makes it plausible.

This question of the connection between the exclusion principle and the Dirac equation is so interesting that we shall try to give another argument that does not involve closed loops. We shall prove that it is inconsistent to assume that electrons are completely independent and wave functions for several electrons are simply products of individual wave functions (even though we neglect their interaction). For if we assume this, then Probability of vacuum = Pv remaining a vacuum Probability of vacuum to 1 pair = Pv of 1 pair Probability of vacuum to 2 pairs = Pv of 2 pairs

164 QUANTUM ELECTRODYNAMICS Now, the sum of these probabilities is the probability of a vacuum becoming anything and this must be unity. Thus 1 = Pv [1 + Prob. of 1 pair) + Prob. of 2 pairs) + ...] (31-8)

The probability that an electron goes from a to b and nothing else happens is Pv |ψ(b, a)|². The probability that the electron goes from a to b and one pair is produced is Pv |ψ(b, a)|² |ψ(pair)|², and the probability that the electron goes from a to b with two pairs produced is Pv |ψ(b, a)|² |ψ(2 pair)|². Thus the probability for an electron to go from a to b with any number of pairs produced is [see Eq. (31-8)]. Now since the electron must go somewhere, However, it is a property of the Dirac kernel that and an inconsistency results. The inconsistency can be eliminated by assuming that electrons obey Fermi-Dirac statistics and are not independent. Under these circumstances the original electron and the electron of the pair are not independent and Probability of electron from |ψ(b, a)|² [1 - ψ(pair)|²]

a to b plus 1 pair produced because we should not allow the case that the electron in the pair is in the same state as the electron at b.

For the kernel of the Klein-Gordon equation, it turns out that the sign of the inequality in Eq. (31-10) is reversed. Therefore, for a spin-zero particle neither Fermi-Dirac statistics nor independent particles are possible.

If the wave functions are taken symmetric (charges reversed and amplitudes, Einstein-Bose statistics), the inequality Eq. (31-11) is also reversed.

In symmetrical statistics the presence of a particle in a state (say b) enhances the chance that another is created in the same state. So the Klein-Gordon equation requires Bose statistics.

It is interesting to try to sharpen these arguments to show that the |ψ(b, a)|² db between 0 and 1 is quantitatively exactly compensated for by the exclusion principle. Such a fundamental relation ought to have a clear and simple exposition.

## 10. SUBSEQUENT ANALYSIS BY SORT OF NUMBERS FOR REAL PARTS OF INTEGRAL EQUATIONS

First, write down the matrix directly without smearing numerical factors. Thus, electron propagation factor in the rules of for computing transition probabilities is (p - iε)⁻¹, virtual photon factor is with couplings are not clearly stated there, so we give a brief summary here.

The probability of transition per unit volume and time from an initial state of energy E to a final state of the same total energy (which is taken to be in a continuum) is given by |I|² (density of final states per unit energy range at energy E) × (normizing constant)² where is the density of final states per unit energy range at energy E and is the square of the matrix element taken between the initial and final state of the transition matrix appropriate to the problem. N is a normizing constant. For bound states conventionally normalized it is 1. For free particles, N is a product of a factor N for each particle in the initial and for each in the final energy state. N depends on the normalization of the wave functions of the particles (photons are considered as particles) which is used in computing the matrix element of the Hamiltonian. The simplest normalization (which does not destroy the apparent covariance of QED) is N = 2E, where E is the energy of the particle. This corresponds to choosing in momentum space, plane waves for photons of unit vector potential, e² = -1.

For electrons it corresponds to using (2E) (so that, for example, if an electron is deviated from initial state a to final state b, the sum over all initial and final spin states of the result is 1). A choice of normalization (2E)⁻¹ results in N=1 for electrons. The matrix I is evaluated by making the diagrams and following the rules of QED, but with the following definition of numerical factors. (We give them here for the special case that the initial, final, and intermediate unperturbed states in question are divided by the normalization constant N, belonging to each particle comprising the unperturbed state.)

The confusing factor (2π)⁴ here serves no useful purpose so the convention will be abandoned. In this notation, δ⁴(k) has its usual meaning. The author has profited from discussions with G. Feynman, M. Pashkin and L. Brown.

*In general, 1/N is the particle density. It is N = (2π)³ for plane waves.

unity.

61.

This page intentionally left blank PHYSICAL REVIEW VOLUME 76, NUMBER 6 SEPTEMBER 15, 1949

The problem of the behavior of positrons and electrons in given external potentials, neglecting their mutual interaction, is solved by replacing the theory of holes by a reinterpretation of the solutions of the Dirac equation. It is possible to write down a complete solution of this problem in terms of boundary conditions on the wave function, and this solution contains virtually all the possibilities of virtual (and real) pair formation and annihilation together with the ordinary scattering process, including the correct relative signs of the various terms.

In this solution, the "negative energy states" appear in a form which may be pictured (as by Stueckelberg) in space-time as waves traveling away from the external potential backwards in time. Experimentally such a wave corresponds to a positron approaching the potential and annihilating the electron. A particle moving forward in time (electron) in a potential may be scattered forward in time (ordinary scattering) or backward (pair annihilation). When moving backward (positron) it may be scattered forward in time (positron scattering) or backward (pair production). For such a particle the amplitude for transition from an initial to a final state is analyzed to any order in the potential by considering it to undergo a sequence of such scatterings.

The amplitude for a process involving many such particles is the product of the transition amplitudes for each particle. The exclusion principle requires that antisymmetric combinations of amplitudes be used for these complete processes which differ only by exchange of particles. It seems that a consistent interpretation is only possible if the exclusion principle is adopted. The exclusion principle does not enter into intermediate states. Vacuum problems do not arise for charges which do not interact with one another, but these are needed nevertheless in consideration of application to quantum electrodynamics.

The results are also given in momentum-energy variables. Equivalence to the second quantization theory of Fermi is proved in an appendix.

THIS INTRODUCTION is the first of a set of papers dealing with the solution of problems in quantum electrodynamics. The main principle is to deal directly with the Hamiltonian differential equations rather than with these equations themselves. Here we treat simply the motion of electrons and positrons in given potentials, where we consider the interactions into account at the same time.

It is as though a bombardier were looking over a road of three targets and it is when two of them come together and disappear that he realizes that he has missed one over a long distance. This point of view leads to considerable simplification in many problems. One can take into account at the same time many particles.

the process which ordi- of these particles, that is, quantum electrodynamics, The of charge in a fixed potential is usually na~lyw would have to be considered separately. for example, when considering the scattering of an electron e tr l < e ? c a tr t a d n by the the of seco d nd t q h u e a n th ti m za ry ti o o n f o h f o l t e h s e , by a potential one automtiall~ ~ ~ into account the effects of virtuzb pair productions. The =me eqwtion, we show that bq. a suitable choiu: and inter- Dirac's, rvhich descrihs the deflection of the world line pretion of the solutions of Dirac,s qttatron the of an electron in a field, can atso describe the deltectian be equally well treated in a manner which Is (and in just as simple a manner1 when it is large enough fundamentally no more complicatd than SchMinger,s to rever* the time-senw of the world line, and thereby method dealing with one or more The vaii- corrwnd to pair annihilation. Quantum mechanically ous and annihilation aprators in the direction of the world lines is rqlaced by the n ti u o m na b l e r e o le f c p tr a o r n ti c f le ie s l , d is v n i o e t w c o a n r x e rv re e q d , i i r .e . e , d , p b a e i c r a s u m ne y th b c e direction of propagation of ~ bvieiw is~ dzerent from thto f the Or datroyed. On the "lter h'nd charge tonian method which considers the future as developing conwed which su@nts that if we the charge* mntinuovsly from out of &e psi, Here we imagine the not tbe prticle, the mulls can be sirnplifid, entire space-time hktory laid out, and that we just the a~pro~hatioofn c hsicai relativistic theory become aware of incrembg portions of it succemively.

the crati.an of an electron pair (eleftron A, positron B) rn =tterkg problem this over-rtll view oj the mm- saigbt be rwresentd by the start of two ~ r l d plete xattering prww is simikr to the $-matr* view- from the point of creation, 1- 'he ~ ~grimr of~ &@d pi at of Heknhrg, The temporal order of events dur- pitran %dlth en continue until it annihilat~a aother ing the sattering, analyEd such detail by eimtron, c, at a world pint 2, Betw*n the times 11 the &nziltanian difierential equation, is irrelevant. The and I2 there are then thre world lines, before and after rehtion of thae viewpoints will be d k a d more onfy one.. However, the war@ lines of c, B, and A fully In the intduction to the s~onpda per, in which wether farm one continuous line albeit the "mitron the more camplicated interactions are analyzed.

partJ' B of thL continuous line is dkecw backwar& The deveiapment stemmtxi from the idea that in non- in the. Follawinp the chwge mtker than the particlm rektivistic quantum mechanics the amplitude for a comespnds to considering this wntinuous world line given procm can be mmidered as the sum of an ampii- tude for each space-the path availab1e.l In view of the (where we write 1 fox xi, tl and 2 for X*, la) in thi case fact that in cltassical physics positrons could be viewed as electrons procding along world lines toward the 1)=x( bm(xa>@$(xezx) p(- iE,(ba-ti)), (3)

pSt(r eference 7, the was lnade removes in for le>lI.T iVe shall find it convenient for Is<&r to define the relativistic case, tbe restriction that the paths must = Q (2) ia not valid tr).

proceed always in one direction in time. It was dk- then readily shown that in general K can be defined by coved that the results could be even more easily tht solution of understoob frorn a more familiar physical viewpoint, that of sfattered waves, This viewpoint is the one used <i3/3l$-R~)K(l2)= ~ G (2, (4)

in this paper. Aflrtr the equations were worked out which is zero for l%<%w here 6(2,1)== b(12-1~)8(~2-zt)

physially the prwf of the equivalence to ttie sr?cond X~@S-YZ)&(aInZd ~th-e ~su~b~se rigt 2 on Lfz means quantization theory was founds2 that the oprator acts on the vaxiables of 2 of K(2, 1).

First we diwuss the relation of the Hamiltonian When E is not constant, (2) and (4) are wIid but K is digerenth1 equation to its solution, using for an example Iess easy to evaluate than (3),$ the Schrifidinger quation, Next we deal in an analogous Ur, can call 8(2,1) the total amplitude for arrival way with the Dirac equation and show how the solu- at X*, 12 starting frorn XL, I.E. (It results from adding an tions m y be interpreted to apply to positrons. The arnplitude,expiS,fore ach, space time path loetween these intepretatim we~nso t to be conistent unless the pints, where S is the action along the path," The electrons obey the exclusion principle. (Charge obying transition amplitude for fxnding a particlie in state the Klein-Grdon equations can be described in an ~(xst2,) at time 12, if at 11 it was in +<X,, td, is analogous manner, but here consistency apparently requires Bose statistics.)$ A represenhtion in momen- turn and energy varhbles which is uselul for the caicu- lation of matrix elements is dexribd. A proof of the equivafence of the methd to the theory of holes in A quantum mechanical system is dezribert equally well second quantization is given in the Appendix. by specifying the function K, or by specifying the &mi;ltonian E from which it results. For some purposes 2. GmBX'S WNCTION T-ATMEET OF the specificatbn in terms of K is easier to use and SCHRI)DTNGBR%E QUATEOR visualize. We desire eventurtlly to dkus quantum We begin by a brief discussian of the rehtion of the electrodpamics from this point of view.

non-rektivistic wave eqmtion to its solution. The ideas To gain a greater familiarity with the K function and will then be extended to rehtivistic particles, satisfying the point of view it suggests, we consider a simple Dirac's quation, and Plslaitfy in the succading paper to perturbation problem. Imagine we have a partick in hteracthg rehtivistic particles, that is, quantum a weak potential U(x, 11, a function of psition and ekctrodynamics. time. We wish to cafcufate K@, 1) if U ditfers from The Schriidinger equation zero only for 1 between 9 and to, We shall expand X in inc~eshgpo wers of U: dwribes the change in the wave function J, in an X(2, 1)sR o(2, l)+K(lf( 2, 1)+K(2)f2, l)+ * - . . (6)

infinitminzaf the At as due to tbe aperation of an To zero order in U, IC is that for a, free prtkfe, Ko(2, l),' oprator exp(-iHdl). One can ask also, if $(xi, 11) is To study the first order correction K""f(Z,I) , first con- tlze wave function at x, at time tl, what is the wave sider the case that U digers from zero only for the function attht z>&7 It can always be written as infinitesimal time interval between sme tbe ta and la;+dta(lg<k<Is).T hen il $(l) is the wave function at xl, it, the wave function at XQ, fa is where K is a Green's function for t z m S n 1 g 1 e . 18 to ka bause of o ti n o n t . h I e n i n (1 it 0 ia ), l U w ( a 3 v ) e c f a u n n b c e ti o g n e , n g e i r v a e fi s z t d h e t o fi r A m 4 1 3 w ) a - v a e a f A u ( n 3 c ) - We can undersund the result (B), (9) this way. We where A 6, A. are the scalar and vector potentkg (timm e, can imitgine that a prticle traveb as a free particle the elmtron charge) and a are Dkc matrices.

fram point to point, but is scattered by the patential U. To discuss this we sbll define a convenient reC Thus the total ampiitude for ar~vaal t 2 from l can tivistic notation. We represent four-vwtom like x, 1 by be considered as the sum of the amplitudes for variaus a symbol S,, where p= l, 2,3,4 and 2qJra l h real. Thus alternative routes. It may go directly from I to 2 the vector and scalar potential (thes e} A, A, isi A,.

(amplitude K&?, I), giving the zero order term in (6)). The four tnat~ce@sa ,B tan be comidered m trmform- Or (see Fig. I(&)) it may go from I to 3 (amplitude ing: as a four vcrctor r, (our y, digem from Paufi's by a &(St l)), get scattered there by the potential (scatter- factor i for P==l , 2,3). We use the summation conven- ing amplitude -z'U(3) per unit volume and time) and tion &,h,= a&&- atb~-ds-ada= a.6. In pzlrticukr if then go from 3 to 2 [amplitude K&!, 3)). This ntay a, is any four vector (but not a matrk) we write occur for any point 3 so that summing over these a=afiy, so that a is a matrk with a vector alternatives gives (9). (a wit1 often be used in place ymbol for the &&in, it may be scattered twice by the potential vector). The satisfy rp7*3-.~p~2f26i,, = where &M= -f- l, (Fig. l(b)}. It goes fr~m1 t o 5 (K@@I,) ), gets scatted there (-iU(3)) then prmeeds ta =me other pint, 4, in space time (amplitude Re(&3 )) is scattered win and S,,= 4, Note that ab+ba= 2ct-b and that &=G@@, o (- v - e il r Z a ( l 4 l ) p ) s a s n ib d l e th p e l n a c p e r s o a c n e d d s t im to e 2 s f ( o & r ( 3 ;l, , 4 4 f ) u ). l d S t u h m at m t i h n e g a = /a @ 6 . f a o i s r a p ~ p 1 ur . e 4a n n ~d u m - be a r /a . z T , he - s a y / m a 'b y o , I - a a / 8 / z & , w fo il r l m a = a l n , scond order contribution to the total aqlitltde 2,3. Gall V= y,a/d+= Ba/at-t-isa" V. We shall im@ne K""(Z, 1) is We are rintpky wlving by suamive apprdmaticns an in-1 quation (deducible dimctly from (1) WE& ljl-H~+U and (8 with R=&@>, This urn be radily verifid directfyfram (If just as (9) p w e h a a t e r t t h h e a n fi r t s h t e i 6 n , te a @ lp wr e i x n l g ea h ds t h a e v e m r c n iU d s t erm e , a a n n d d a k l > l r ti b m es expmion of the intern1 equation K+cA'(Z1, ) l])

wKch it a hs atbges.

We would now expet to choo*, for the spttciaf solu- tion of (12), II+mXe whem Ke(2,I) wnaw for 12<it and for t3>& is given by (3) where 4, and E, are the eigenfwctians and energy valum of a parGcle satis- f hBk acJse quation, and @ *, is by $n.

The formuk arising from this choice, however, s&er keta from the drawback that they apply to the one electron WDWP OIIMB, LQ, (84) theory of Dirac rather than to the hob theory of the F%@ 2. The Dim equsrtien wrmits anaiher mlutien K+(2 1) witran. For example, consider its in Fig. 1(a) an if oat kn~dertsb at wava ~~ibttembdy the ptential can electron after kkg zatterd by a potential io a small Mwmda in drne as ia Fig. 2 (a). This is intcpreted in the wand rd ty a Pcrfw - o f virtu (b ad lp i: o b ag n a th t t r e p o is s it n g - r s ( ) w sp it c e t h th lec on r d ampE tu to b. aoi&tied. ?his on be pirrvd as dmilar to or$li~~ya t another poitlt 2 will procd toward mitive thes w t e t h t rn i t J f t ) o a 24 m T Lt w th a a v t m t h s e a e k k fn t r r e o d ts m f r t t t c o l e d i b ( w 4 k r w r d m s a in t w bo i v os ti v e n e t iv q a ra tl o f e n rg is s e , P the dmtron &m X. %%is view is proved equlvdent to hk hty: wave 19 mtLerd to times previous. to the time of electram tmveLing bekwards in time are rmmizad m etrons.

mtkring. nrn are just the prowrtim of R0(2,3).

OR the other haad, according to the pitran herdter, purely for relativistic convenience, that +,* in (3) is rephced by its djokt &=, cbn*fl. neptive enew stittes are not availabk to the electron Thus the I)& equation for a partick, mms m, in sn after the mtteriw, Therefore the choice K+=Ko is unsa&facby. But there are other mlutions of (12).

exteml field A = A ,y, is We shall choose the solutrion dehhg Kc(2, 1) so that K+(Z, 1) for tt> 1% is 1h I(!%= uj (3) m podioe w g y md m, (G determining the propgation of a free stales o~lyN. ow this new solu~onm mt =My (12) for prticle bwoma ilU tima in orda that the rwrewnk&a be cornpieb.

It must *erefore dBer from the old wlution K@b y a (iVa-m>K+(2, 1) = i6(2, l), f 12) mlution of the homogenaus Dirsc eqwGon. It is c k the hdex 2 on 17% indiating dgerentiation with rmpct from &e deftnition tht the difference K@-K+ is the to the coordhtes sss which are reprewated as 2 in sum of (3) over all neetive enerp;y statm, ars long as IE+(2,1) and W,1 ). 12>11. But this gaerence mat be a wiuGoa of the The function 11=,(2,1i)s d&ed in the abnm of a homogenmus Dhae equa~onfo r all tims and mat field. If a ptentiilf A is acting a shikr function, ay &erefore h rreprwnteci by the =me sum over nega~ve K+(h"(2,1)m be dehd, It differs from K+(2,1) by a enew skta aka for Ca<ll. Since KB~iOn Skt cam, %mt order comeetion given by the analoee of (9) it fobws that our new kernel, I),f or In<lx is the namely ~SK+(Z, mrg&iw Ql the sunr (3)o uer wgolifx?m g ys tates. That is, K+")(Z, 1) = 3)d(3)Kt(3, i)drr, (13) R+(2$ l)=xpo~a. 4n(2)6n(1)

repreen~ngth e amplitude to go from 1 to 3 as a free -Crvs X o e xp( 4 -i i B )n , f ( 2 tg i( - i l ; l n l) ( l) for t2> 18 lf 7)

particle, get mttered there by the p&ntM (now the X~p(-iE~@a-h)) for It<lt.

matrix A(3) ins-4 of U(3))a nd coatlnue to 2 as free.

order mmction, italogom to is Ifih koim of K+ ~atiom (13) and - (14) wiif now give results quivdent to tfiose of the - 6tmnh alie a w ~ , X+m(Z, 1) ssKI(2,4IA(4) That (141, for ample, is the mrrHt mond order e~re&onf or h&g at 2 an or&&& at 1 M+(4,3)A(3)15+(3, l)dzdrs, (14)

according to the msitron thmq m yb e wen ar, follows and so on. In generat K+") ~ati$fies (Fig. 2). &me as a speciat wmpb h ttz 3El and ( l ) , ('5) that potential vani*la arept in ktcrml fz-h &at E4 and tr both lie betwan tt and k and the succmive tern (131, (14) are the power =rim First supp4 > ts (F&. 2(b)). Then (since is> tl)

"THEORY OF the electron assumed originauy in a positive enerw With ehi inteqretation real pair grduction is aho state propagates in that state (by f(+(3, X)) to posihn dmribed carretly (W Fig. 3). For example in (13) if 3 where it gets scatter& (A(3)).f t then prmeds to 4, tl<la<ta the equatbn gives the amplitude that if at which it must do as a positive energy ekdron. Thh is time $1 one electron is present at 1, then at time just correctly descGbed by (l+ for fC+(4, 3) contains only one ctl~tronw ilt be present (having been scattered at 3)

positive energy compnents in its expansion, as tr>t,, and it will be at 2. On the other hand if IS is less than h, After being scattered at 4 It then prwds on to 2, for examph, if t2= tI< t g, the same expression gives the aein necms~ilyin a positive energy sCate, as It> tr. amplitude that a pair, electron at 1, gositran at 2 will In positron theory there is an additional contribution annihihte at 3, and subvequently no particles wijl he due to the possibiiity d virtual pair prduction (Fig. prewnt. Likewise if 6% and I1 exceed ta we have (minus)

2fc)). A pair could be created by the potential A(4) the amplitude for Snding a single pair, electron at. 2, at 4, ihe electron of which is that fwnd later at 2. The psitxon at 1 crezrtad by A(3) from a vacuum, If positron (or rather, the hob) PEW& to 3 where it ta>ta>ls, ($3) dacribes the wattering of a psitron, annihilates the electron which has arfived there from l. A'fl these amphttldes are rehtive to the ampiitude that This alternative is alrmdy included in (14) as; con- a vwuum will remain a vacuum, which is taken as tributions far which l,< La, and its study will lead us to unity. (This will be discussed more fully later.)

an inltrvretation of K+(4,3) for Ir<la. The fmtor The analsue of (2) can be easily worked our.@X t is, K+(2, 4) de~ribesth e electron (after the pair prduc- tion at 4) proceeding from 4 to 2. Ckewiss: K+@, It)

repmnts the electron prweding from 1t o 3. K+(4,3)

must therefore represent the propagation of the positron where d8iVr is the volunte element of the clad 3- o th r a h t o i l n e h fr o o le m t 4 h e to a y 3 . t h T e h h a o t k it p d rw m ee S d O s i i s n c t l h e e a r m . T n h n e e f r a C ct A dirmensioml surf;tcseo f a re&on of space time contaking and electron of negative energy is rekted in the fact that K+(4,3) far (P<~J is fmhus) the sum of only negative energy componenb. In hale theaq the real enera of these intermdiate sbm is, of coum, positive. Thb is true here too, since in the phasa ap(-iEn(lr-ls)) desmg K+(& 3) in (17), ERi s nega- tive but so is Ir-lg. That is, the contributions vary with 11 as e:p(-i\E,/ (to-14)) as they would if the enera of the mtermediate state were t E,/.T he fact that the entire sum is taken as negrttve in computing IC+(4,3)

is reflected in the fact that in hale theq the amplitude has its sign reversed in accordance with the Pauli principle and the fact that the electron arriving at 2 has been exchanged with one in the %a.@T o this, and to higher orders, all procesw involving virtual pirs for F m to & . P 3. d S ,e e ] ve nG r d a i l a d gA i l o fe n r ~e t n h t e( p r t~i w m - e , r ela ca ti n o n b s e o d f em the ib v ed ar b ia y b t l h es e 1 = 1 m , I e t , are correctly dwritrted in this way. Thus I)/* is the probattUity that: (a) An electron at a p eq io k c r o 14 )

(3 I)

, s ca tk r- s ((1 3w l l & l e n c & t r on a a i t r t e a 1 a I m d p a 1 i i s tm r r u e a a M t t h f r a r n m n i r h si m i la t m e fo r le .

a ( v d ) n g A ac ing at 3 by A@), proceeding to 4 (K+(4,3)), scatrering at 2 io metered ta 1. (~+(41(2,1) is tbe sum of the e e k 2 agin, A(4), arriving finally at 2. The scatterin@ may, sflttteh in the potential to all orders. P, is a normalizing bowwer, be toward both future and past times* an mtanttt)

electron prapagakimg backwards in time king recag- &ed ats a positron.

This tkerefore sul~gestst hat negative energy corn- ponents created by scattering in a ptentkl be con- sider& as waves propgating from the scattering mint toward the pt, and that such waves rqmnt the propgation of a positron annihilating the eltt~tronin tfie p~tenthi.~ "t has often boen noted &at the one-electron theory s patently gives the m em atrix ehents for lhi pr- as dam hofe theory.

The pr&lern is one of iniepretadon apdIyi n a way that will alsa 've urrreet radts for other &r& -, e.g., self-enmgy.

7 &e idea that pitmm an repiewnted as elrrvoos with p th r e o p a er u t t h im or e a r n e d v o e th d m r s e , t a p ti a v r e t i t c o u i t s m rl e y e b m y S & t S B c b k e e en ik k r~E w . cd, b C!

paint 2, and N(1) h N,(l)r, where N,(I) is the i~we~dtiv istic calculations, om be removed irs follows. Instead drawn unit nomaI to the sdace at the paint X. That of dehing a skte by the wave function f(x), which it is, the wave function #(2) (m this case for a free par- h aa t a given time tt=O, we define the state by the ticle) is determind at any point inside a four-dimen- function $(l) of four varirrblm XI, t.1 Ilvhi& is a satution sbnal region if its values on the surface of that re@on of the free particle equath for all 4 and is f(xr) for are sp&ed, k=Q. The h fst ate is mewi~de fined by a functian To intewret this, cornider the case that the 3-surfam g(2) over-all sp~e-theT. Hen aur sudace integrah can comkts mntklly of all space at =me time say t=O be prformd since JK+(3, l)@j[xl)@x~f=(3 ) and previous to h, and of aU spce at the time T> tg. The JQ(s;~)B@x&+(2,3) = #(3), There results qlhder connecting these to wmpIete the chsure of the sudae may be very distant from X* so that it gives no appreciable contribution (as R+(2, l) deamws expo- nentially in spce-&L ddir~tbns)H, ence, if yr= @ , since the inward &awn norm& N will be B and -8, the intepl now biryq aver-aU swe-time, The transi- tion amplitude to wwnd order (from (14)) is for the mticXe a r ~ *a~t 1 with am~litude{ (l) is scatter4 (A(z)), prsg&m to 2, [~+\2, I)), ihd is where fr...@, 2'. positive energy (elmtron) scattered again (A(2)), and we then ask for the ampli- comwnenls in $(l) contribute to the first integral and tude that it in slate g(2), E g(2) is a negative energy only nwtive energy (wsitronf com~nen:ntoff @(X? state we are sol+@ a problem of annihilation of elec- the =con&, That is, the amplitude for finding a charge tron in 1(1), positron in g(~)e,k , at 2 is deter&& both by the amplitude for Gnfmdinh: f;Ve have hen emphasizing scattering problem, but an electron preriotls to the measurement and by the be motion in a fix& V; say in a ampli m tu i d g e b f t o b r e h i d n h te g qr a e p te o d si t a ro s n m a m fte n r i n t g h e t h m a e t a s e u v r e e n m i e n t a . h v y ie d w ro & g en a a to m % , a t c r a e n ri ng prable d m ea lt can ~ a f s k i t f i o s r f t i h rs e t problem involving but one char@ the amplitude for amplitude, dra(X), that an efwtran with original free findkg the charge at 2 is not determined when the only wave function was scattered K times in the potential. V thing known in the amplitude far finding an electron either famard or backward in time to arrive a~1t. Then (or a positron) at an earlier time. There may have been the gfter one more scattering no electron pment initially but a pair was created in the masurement (or atso by otber external &eieXds). The ampfitude for this contingency is spified by the amplitude for fxnding a po~itroni n the future.

We clan a ho bhin exprwions for transirion ampli- An equation for the teal am~htude tudes, like (S). For emmpk if at 1=0 we have an elec- tron prmnt in a state with (positive enerw] wave fmction f(x), what is the amplitude for finding it at T wia ae (pgi~ve enew) wave function for ar~Gngat 1 either dirwtly or after any numhr of The amplitude for h&mg &e electron anywhere after mtthne is ob~sainedb y summing (24) over all K from l= 0 it; given by (19) with $(l) r q h d b y f(x), the 0 to CO ; second in&@ait vanwing. Rence, the transition ele- $(2)= 4.(2l-ib(z, I)V(l)+(l)drx. (25)

ment to h di t in slate g($ is, in anatqy to (S), just Viewed as a s M y s tate problem we w y wish, for emmpie, to find &at initial condition 4s (or better just +.

the $1 which l& to a p~dimco tion of This is sine g* = #B. mast pmctidy done, of coumt by mlving the Dirac equation8 If a potenthi acts sommhere in the internal betwan (iV-m>+(1)= v(l)#(l), (26)

0 and T; K+ i6 repked by K+cA).T hus the first order egst on tbe transition ampEtude is, from (131, deducd from (25) by bpmting on both sides by iVa- m, athg the h, and using (12). This illus- iS@(xi)~x+(3z1.4 (3)K+(3*I )@j(xr)hlhr. (21) trates fhe rehtion betwm tht? pohb of view.

For mny problem the total potenhl A+ V may be Eqrwions such as this ean be simplifid and the split conveniently into a h& one, V, and another, A, ;dsurfoce htwblsw,h ich are inconvenient for rela- comiderd as a perturktioa, If K+") is de&& as in

## POSITRONS

(t6) with V for A, eqressions such as (23) are valid and u%ful with K+ replaced by and the functions f(t), g(2) reQl"ced by solutions for all space and time of the Dlrac Eq. (26) in the potential V (rather than free particle wave functions)

We wish next to consider the case that there are two (or more) distinct charges (in addition to pairs they may prduce III virtual states), In a succeding paper we dkws the interaction between such charges. Here we amurnr: that they do not interact. In this case each particle behrlves independendy of the other. lnJe can expect &at if we have tvvo particles a and b, the ampfi- tude that particle a goes from xl at Is,t o xa at while b gaes from X$ at t* to xp at tq is the product The spbols a, 6 sinpliy indiate that the matrices apgearing in the K, apply to the Dirac four component spinors corraponding to particle a or b respectiveiy [the wave function now having 16 indices). In a. ptential FE. Q. Some problems involving two distinct charges (in ail&- X+, and K+b &come K+,tA) and K.+I.(w~h)e re t - i - o K n,1 t A a jj v 4, irtu 1 a) l & f a ~ i l r @ s, t hey m i a s y t p h r e d u p c ra e b ): a c b , ~ J i K ity + ,t ( h A a A t: " ( (I a 3) ) k. ; E fA tm jf tr 4 a ,2 n ) s is defind a dc jzlculated as for a single particle. They at I and 2 are -9attered to 3,4 (and no paws are farmed). (W commute?. Rereafter the a, b can be omittd; the space Starting with an electran at 1 a single pair i eleetrans at 3 4 (c) A pair at 1, 4 is found eleetrans at 3 4 (c) A pair at 1, 4 is found time varhble appearing in the kernels suffice to dehe sian princiF1ef r&uirw that the amplitudes on what they operate. exchsnge of two eiclctrons be subtracted.

The par~clesa re idential however and satisfy the exclusion principle. The principle requires only that one term (14). We shall see, hovvever, that considering the calculate K(3,4; 1,2)- R(4,3; 1,2) to get the net exclutusion principle also requires another change which ampIitude for arrival of charges at 3,4. (It is normlisd reinstate the quantity.

suming that when an intqral is yx?rform& over mints For we are computing amplitudes relative to the 3 and 4, for example, since the electrons represented are amplitude that a vauurn at tl will still be a vacuum at identical, one divida by 2.1 This expmsion is correct E*W. e are interested in the alkration in this amplitude for pitrons also (Fig. 4). For emmple the amplitude due to the preEnce of an electron at 1. Now one process thi~ta, n efectron and a psitron found Initially at x2 and that can be visualized rls occurring in the vacuum is the X, (say Itsir) are later found at xa and (with creation of a pir at 4 follow& by a re-annihilation of t2 =i g> 13) is given by the =me expression the same pair at 3 (a proces which we shall call a closed loop path). But if a real efectron is present in a cerbin state 1, those pairs for which the electron was created The h tte rm repreen& the amplitude that the electron in state 1 in the vacuum must now be excludd, W prwee& from 1 to 3 and the psitron from 4 to 2 [Fig, must therefore subtrset frmo ur rejative amplitude the 4(c)), while the mcond term reprwnts the Intedering term correspndiag to this prxess, But this just reis- amplitude that the pair at I, 4 annihilate and what is states the quantity which it was argued shouM not found at 3, 2 is a pair newly creaee$ in the potential. have been included in (14), the necessary minus sign The generaEzation to ~verapla rticles is clmr. There k coming autamaticaIly from the definition of K+. It is an additional factor K+(A' for each particle, and anti- obviously simpler to disregard the exclusion principle symmetric combinatims are always taken, completeb in the intermediate states.

No account need be taken of the excitusion principte AII the amplitudes are relative and their quares give in Lntemdiate states. As an example consider wain the rehtive probabilities of the various phenomena, rqression (14) for Ir>l~ and suppw t4<ta SO that The Abwlute prohbiiities result if: one nnultipiim each of situation reprant& (Fig. 2(c)) is that a pair is made the prolsabilities by P*, the true probability that if one at 4 with the ei~tronpr weeding to 2, and the psitrsn has no partictes prewnt inithay there will be none to 3 where it iuxnikiktes the electron arriving from 1. finally. This quantity P, can be crzkutatd by normal- It may tT& obje-cted that ifi t happns that the eiwtron izing the relative probabilities such that the sum of the cmted at 4 is in the sam state as the one co ming from probabilities of all mutually exclusive phenomena is 1, then the process cannot occur because of the exclusion unity. (For example, if one starts with a vacuum, one can principle and we should not have included it in our calculate the relative probability that there remains a 756 R. P. FEYNMAN vacuum (unity), or one pair is created, or two pairs, etc. In addition to these single loops, we have the possibility The sum is P=1.) Put in this form, the theory is cam-that two independent pairs may be created, and plete and there are no divergence problems. Real proc- each pair may annihilate itself again. That is, there may esses are completely independent of what goes on in be formed in the vacuum two closed loops, and the the vacuum.

contribution in amplitude from this alternative is just When we come, in the succeeding paper, to deal with the product of the contribution from each of the loops interactions between charges, however, the situation is considered singly. The total contribution from all such not so simple. There is the possibility that virtual elec-pairs of loops (it is still consistent to disregard the trons in the vacuum may interact electromagnetically exclusion principle for these virtual states) is L²/2, for with the real electrons. For that reason processes oc-in L we count every pair of loops twice. The total curring in the vacuum are analyzed in the next section, in vacuum-vacuum amplitude is then an independent method of obtaining P₀ is C₀ = 1 - L + L²/2 - L³/6 + ...

= exp(-L), (30)

the successive terms representing the amplitude from An alternative way of obtaining absolute amplitudes zero, one, two, etc., loops. The fact that the contribu- is to multiply all amplitudes by C₀, the vacuum to tion to C₀ of single loops is -L is a consequence of the vacuum amplitude, that is, the absolute amplitude that Pauli principle. For example, consider a situation in there be no particles both initially and finally. We can which two pairs of particles are created. Then these assume C₀=1 if no potential is present during the hop, particles later destroy themselves so that we have two internal, and otherwise we compute it as follows. It de-electrons which, at a given time, are interchanged viates from unity because, for example, a pair could be forming a kind of figure eight which is a single loop.

created which eventually annihilates itself again. Such The fact that the interchange must change the sign a path would appear as a closed loop on a space-time dia-of the contribution requires that the terms in C₀ gram. The sum of the amplitudes resulting from all appear with alternate signs. (The exclusion principle is such single closed loops we call, L. To a first approxima-also responsible in a similar way for the fact that the tion L is given by amplitude for a pair creation is -K⁺ rather than +K⁺.)

The quantity L has an infinite imaginary part (from For a pair could be created at 1, the electron and higher orders are finite). We will discuss this in positron could both go on to 2 and there annihilate. connection with vacuum polarization in the succeeding The spur, Sₚ, is taken since one has to sum over all paper. This has no effect on the normalization constant possible spins for the pair. The factor 8 arises from the for the probability that a vacuum remains a vacuum is fact that the same loop could be considered as starting given by at either potential, and the minus sign results since the P₀ = |C₀|² = exp(-2 times real part of L), potentials are each iA. The next order term would be from (30). This value agrees with the one calculated directly by normalizing probabilities. The real part etc. The sum of all such terms gives L. It does not of L appears to be positive as a consequence of the Dirac require a closed loop as an essential element.

For example, there is a contribution to C₀ which equation and properties of K⁺ so that P₀ is less than one. Bose statistics would give C₀=exp(+L) and con- sequently a value of P₀ greater than unity which appears to be incorrect. This indicates that the exclusion principle is an essential element in the theory.

Charges obeying the Klein-Gordon equation can be equally well treated by the methods which are de- scribed in this paper. The final result after summing over n by (13) and (14) and using (15) is hard to obtain because of the factor (1/i)ⁿ in the nth term. However, the per- turbation in L, dL, due to a small change in potential dA, is easy to express. First (1/i)ⁿ is caused by the fact that dA can appear in any of the n potentials. The term K⁺, I is actually identical to are.

## POSITRONS

P(k), B(k) is the Bessel function and δ(k) is the Dirac delta function of k. It behaves asymptotically The practical evaluation of the matrix elements in as exp(-kr), decaying exponentially in space-like some problems is often simplified by working with directions.

momentum and energy variables rather than space and time. This is because the function K(x, 1) is fairly By means of such transforms, the matrix elements complicated but we shall find that its Fourier transform like (22) and (23) are easily worked out. A free particle is very simple, namely, (i(γ·p - m) - ε)⁻¹ that wave function for an electron of momentum p is e^(-ip·x) where u is a constant spinor satisfying the Dirac equation (γ·p - m)u = 0 so that p²=m². The matrix element (22) for going from a state p₁ to a state of momentum p₂, spinor u₂, is -i(u₂*γ(q)u₁)

=B(e^(ip₂·x))*, where we have imagined A expanded in a Fourier integral ∫dp₁dp₂d³q d(p₂, t) the integral over all p. True can be seen immediately from (12).

for the representation of the operator (V-m) in energy (p₄) and momentum (p₁x, p₁y, p₁z) space, (V-m) is the true and the true form of K(x, 1) is a constant. The reciprocal matrix (V-m)⁻¹ can be interpreted as (p₄-m)(p₄-m)⁻¹ for p²-m² = (p₄-m)(p₄+E(p)) is a pure number not involving matrices. Hence, if one wishes, one can write K(x, 1) is not a matrix operator but a function satisfying -∂/∂t + a = m, where (a/∂xg)(a/dx).

The integrals (31) and (32) are not yet completely defined for there are poles in the integrand when p₄² - E² = 0. We can define how these poles are to be evaluated by the rule that m is to be understood to have an imaginary part -iε. That is, m is re- placed by m - iε and the limit taken as ε → 0 from above. This can be seen by noting that we calculate K⁺ by integrating on p₄ first. If we call E=+(m²-δ+ p_x²+p_y²+p_z²) then the integrals involve p₄ essentially as ∫ exp(-x₄(tg-I t1)]dp₄(p₄² - E²)⁻¹ which has poles at p₄ = +E and p₄ = -E. The replacement of m by m - iε means that E has a small negative imaginary part; the first pole is below, the second above the real axis. Now, if (t₂-t₁)>0 the contour can be closed around the semicircle below the real axis thus giving a residue from the p₄ = +E pole, or (2πi)e^(-iE(t₂-t₁)). If (t₂-t₁)<0, the upper semicircle must be used, and p₄ = -E at the pole, so that the function varies in the manner as required by the other definition (17).

Other definitions of (12) result from other prescrip- tions. For example, if 94 in the factor (V-m²)⁻¹ is con- sidered to have a positive imaginary part R is become replaced by K⁰, the Dirac one-electron kernel, zero for t < t'. Explicitly the function is I⁺(x, t) = - (4π)⁻¹(∂/∂x)(m/xt)R₁(ms)(34)

where a=+(m²-x²)½ for P>x and S= -i(x²-P²)½ for a case for positive and negative times. We may be useful to write (x, t) = W(D) - iD R(x, t). W(D) and R(x, t) are the functions we have previously defined. We note that R(x, t) has an effect to keep with m here too the functions W(D) appear.

[ i M )) o w d. ll r P rr h s p 0 . 1 1 a 3 n ,2 d 0 3 D ( 1 m 4 e 4 1 t ) h . n: i r n e m g a m te e f r i a u l d a a c a e a s. i yses in avaidiw wmpLica&ns fmm inffniteiy negative energies are inserted, and the situation interpreted in accordance with the timing relations above. (We have wave functions normalized to (8%). instead of the conventional φ†φ = 1. On our scale φ†φ = energy/m so the probabilities must be corrected by the appropriate factors.) The author has many thanks for fruitful conventions about this subject, particularly H. A. Bethe and F. J. Dyson. In this section we shall show the equivalence of this theory with the hole theory of the positron according to the theory of second quantization of the electron field in a given potential. The state in which the field at any time is represented by a wave function ψ at T arising from ψ(x) at 0. Then i∂ψ/∂t = Nψ, where N = ∫ψ*(x){(-i∇-A)² + m + β}{ψ(x)} dx and ψ(x) is an operator annihilating an electron at position x, while ψ†(x) is the corresponding creation operator. We contemplate a situation in which at t=0 in a vacuum all negative energy states are filled, all positive energy empty. Then we describe as holes in which some positrons. The vectors representing this situation are X and X' respectively, we wish to calculate the matrix element and the method must be slightly modified. Before putting P through the operator we shall add to it another operator F' arising from a function ψ(rk) containing only negative energy components and so choose that the resulting ψ has only positive energy components. That is we want S(Fψ*+ Pneg*) F'ψ*S, where the "pos" and "neg" serve as reminders of the sign of the energy components connected in the operators. This we can now use in the form Sψ*posψ*S = Sψ*negψ*S, (47) writing S for exp(-iHTdt). Our problem is to evaluate R and show that it is a simple factor times C, and that the factor involves the K functions as discussed in the previous sections. In our one electron problem this substitution replaces r by two terms r = ∫ψ*F'ψ dx (ψGSr*ψ, ...). The first of these reduces to r = ∫ψ*(x)ψ, ... (x) dx. The second of these reduces to ... (48) ∫ψ*(x-1) J_{K+}(x,1) d f ... (42) ... where we have defined ψ(x,1) by ψ(x,1) = ... (41) ... for example, see Wentzel, Einführung in die Quantentheorie, (Springer, Leipzig, 1943), Chap. ... from t=0. The positive ones ... negative ones ... The value of C(10-d10) arises from the Hamiltonian m *( a X n ) n e p r a r e t x o m f t i l t y , g R i v is e l r y r d th u r c o d u , g h w i t t h h e t P h ' e s q u e nt c if t e it. d g f i a v c e l s t lrs (an w d h e w n i t a h c a ti t n tw g o o a n t i X n * g ' $ & g u m s analogous LO (47) when f is a function. (An alternative derivation required by the allusion principle, to simpler terms maintaining results from the consideration that the operator *(X, l) which two base operators which may in turn be further reduced by using satisfies the Dirac equation also satisfies the linear integral equa- c h a * n b in e a r e fi d m u it d ar i n m a a s n im er i , l a e r t m c. a A nn ft e e r r . T al h l e t y h e a r F e * m a o re v d us t e h d r o t u h g e h @ th * e 'S b ti y o n W s w h h ( i ( c 5 h 0 , a re quivaient to it,) That is, (58) can be written S in the opposite direction in such a manner as to produce purely negative energy operator at time 0, using relations analogous to (45) to (49). After all this is done we are left *ply with the ex- pected factor times Cr (assuming the net charge is the same in initial and final state.)

In this way we have written the solution to the general problem of the motion of electrons in given potentials. The factor CV is obtained by normalization. However for photon fields it is de- sirable to have an explicit form for C, in terms of the potentials.

This is also given by the (3, 29) modification (29) and (31) as stated that where in the first term h==T , and in the final term. The (A) in (A) refers to that part of the potential A after The b. The Theory of the Vacuum Problem What C.V.  (This is $n v e a w &h c e o s m p f o o n r e i n t t s i n of v o W lvm ,w M (fr c o h m g iv th e e z e K ro c ( o A p " e 2 r , a t l i ) n ) g o in n t l o y We * shall calculate C, from second quantization by induction x8'. In the final term only negative commutants of **(X$)

considering a series of problems each containing a potential de- appear. U, then if"fx8) is interchanged in order with %(X$)i t will tribution more nearly like the one we wish. Suppose we know C, give zero operating an X@, and only the term, for a problem like the one we want and having the same potentials for time t between same k and T, but having zero potentials for times from 0 to t. Call this C,(@, the corresponding Hamiltonian Bto and the sum of contributions for all single loops, U(T). Then for t=0 we have zero potential at all times, no pairs will be will remain, from the usual commutation relation of *a and *, produced, I;(T)=0 and CI(T)=I . For t=T we have the simple problem, so that C,(@ is what is defined as, Cp.i n (38). (reference 01, just L(t- t)-l;(t) in this difference arises here we have, from the Dirac potential A-A during the short time interval At<<T that integration from T to 0 gives (30).

Starting from the theory of the electromagnetic field in second quantization, a derivation of the equations for quantum electro- dynamics will appear in the succeeding paper may be worked out since B& is identical to the constant Hamiltonian Hr for our using very similar principles. The Paul-Weisskopf theory of ;*h and X@i is an eigenfunction of HT with an eigenvalue (energy of vacuum) which we will take as zero.

PHYSICAL REVIEW VOLUME 76, NUMBER 6 SEPTEMBER $5, 1941)

(In this paper two things are done. (1) It is shown that a con- and primarily consistent, method is therefore available for the siderable simplification can be attained in writing down matrix involving electrons and photons.

elements for complex processes in electrodynamics. Further, a The simplification in writing the expressions results from an physical point of view is available which permits these to be emphasis on the over-all space-time view resulting from a study written down directly for any specific problem. Being simply a of the solutions of the equations of electrodynamics. The relation restatement of conventional electrodynamics, however, the matrix of this to the more conventional Hamiltonian point of view is elements diverge for complex processes. (2) Electrodynamics is derived. It would be very difficult to make the modification modified by altering the interaction of electrons at short distances. which is proposed if one insisted on having the equations in All matrix elements are now finite, with the exception of those Hamiltonian form.

relating to problems of vacuum polarization. The latter are The methods apply as well to charges obeying the Klein-Gordon treated in a manner suggested by Pauli and Bethe, which gives equation, and to the various meson theories of nuclear forces.

finite results for these matrices also. The only effects *n the modi- I u U s e u d s t i r n a t e iv le e c a rr m od p y l n e a s d c a s re a gi n ve m n a . k A e l t a h lt o w m h at r a i c m es d f if in re it a e t i f o o n r a li ll k e of th th a e t fication are changes in mass and charge of the electrons, meson theories, for most of the theories it is no longer true that Such effects could not be directly observed. Phenomena directly all directly observable phenomena are insensitive to the de-tails observable, are insensitive to the details of the modification used of the modification used.

(except at extreme energies). For such phenomena, a limit can The actual evaluation of integrals appearing in the matrix be taken as the range of the modification goes to zero. The results elements may be facilitated, in the simpler cases, by methods then agree with those of Schwinger. A complete, unambiguous, described in the appendix.

THE present paper should be considered as a direct con- positive energy electrons are involved. Further, the tinuation of a preceding one,(1) in which the effects of longitudinal and transverse waves can be motion of electrons, neglecting interaction, was ana- combined together. The separations previously made lyzed, by dealing directly with the solution of the were on an unrelativistic basis (reflected in the circum- Hamiltonian differentiable equations. Here the same tech- stance that apparently momentum but not energy is nique is applied to include interactions and in that way commuted in intermediate states). When the terms are to express in simple terms the solution of problems in combined and simplified, the relativistic invariance of quantum electrodynamics. the result is evident.

For most practical calculations in quantum electro- We begin by assuming the solution in space and time dynamics the solution is ordinarily in terms of the Schrödinger equation for particles interacting of a matrix element. The matrix is worked out as an instantaneously. The results are immediately general- expansion in powers of &/ht, the successive terms cor- izable to delayed interactions of relativistic electrons responding to the inclusion of an increasing number of and we represent in that way the laws of quantum virtual quanta. It appears that a considerable simplifi- electrodynamics. We then see how the matrix ele- cation can be achieved in writing down these matrix ment for any process can be written down directly. In elements for complex processes. Furthermore, each term particular, the self-energy expression is written down.

in the expansion can be written down and understood So far, nothing has been done other than a restate- directly from a physical point of view, similar to the ment of conventional electrodynamics in other terms.

space-time view in I. It is the purpose of this paper to Therefore, the self-energy diverges. A modification in describe how this may be done. We shall also discuss interaction between charges is next made, and it is methods of handling the divergent integrals which appear shown that the self-energy is made convergent and in these matrix elements. corresponds to a correction to the electron mass. After The simplification in the formulas results mainly from this mass correction is made, other real processes are the fact that previous methods unnecessarily separated finite and insensitive to the "width" of the cut-off in into individual terms processes that were closely related the interaction.(2)

physically. For example, exchange of a quantum Unfortunately, the modification proposed is not com- between two electrons there were two terms depending pletely satisfactory theoretically (it leads to some diffi- on which electron emitted and which absorbed the culties of conservation of energy). It does, however, quantum. Yet, in the virtual states considered, timing seem consistent and satisfactory to define the matrix relations are not significant. 0by the order of operators p in r o t d h u e c e m d a c tr a k n m be u s c t o m be b i m ne a d i n i w t n a i i t n w h e b d o ic , t h b W e r v e s i r h i t n u a a v w l e h p B ic e & e h n o ( n a I) r l , y e R to . 8 " I o l b d P r , k b F r i c e e r f y d m s i u m a m n d m # o P n b o o f f . t t R h h i e e s v m . r n e 7 o 4 a d i d f 9 i # 3 a 9 t a i n o ( d n I W r in e su e ), l l t m h s e w i r a i u t1 r l f t b p e e h r y f * r o e u f n e d rr g e e in d e R P. Feynman, Phys. Rev. 74, 1430 (1948), hereafter referred 1 R. P. Feynman, Phys. Rev. 76, 749 (1949), hereafter referred 16 9 element for all real processes as the limit of that com- was still not complete because the Hamiltonian method puted here as the cut-off width goes to zero. A similar had been worked out in detail only for particles obeying technique suggested by Pauli and by Bethe can be the non-relativistic Schrödinger equation. It was then applied to problems of vacuum polarization (resulting modified in accordance with the requirements of the in a renormalization of charge) but again a strict Dirac equation and the phenomenon of pair creation.

physical basis for the rules of convergence is not known. This was made easier by the reinterpretation of the After mass and charge renormalization, the limit of theory of holes (1). Finally for practical calculations acknowledgments the zero cut-off width can be taken for all real processes, expressions were developed in a power series in @/he.

The results are then equivalent to those of Schwinger who does not make explicit use of the convergence factor. It was apparent that each term in the series had a simple physical interpretation. Since the result was easier to understand than the derivation, it was thought best to publish the results first in this paper. Considerable time has been spent to make these first two parts as complete and as physically plausible as possible without relying on the Lagrangian method, because it is not generally familiar. It is realized that such a description cannot carry the conviction of truth which would accompany the derivation. On the other hand, in the interest of keeping simple things simple the derivation will appear in a separate paper.

The method of Schwinger is to identify the terms corresponding to corrections in mass and charge and, previous to their evaluation, to remove them from the expressions for real processes. This has the advantage of showing that the results can be strictly independent of particular cut-off methods. On the other hand, many of the properties of the integrals are analyzed using formal properties of invariant propagation functions. But one of the properties is that the integrals are infinite and it is not clear to what extent this invalidates the demonstrations. A practical advantage of the present method is that ambiguities can be more easily resolved; simply by direct calculation of the otherwise divergent integrals. Nevertheless, it is not at all clear that the convergence factors do not upset the physical consistency of the theory. Although in the limit the two methods agree, neither method appears to be thoroughly satisfactory theoretically. Nevertheless, it does appear that we now have available a complete and definite method for the calculation of physical processes to any order in quantum electrodynamics.

Since we can write down the solution to any physical problem, we have a complete theory which could stand by itself. It will be theoretically incomplete, however, in two respects. First, although each term of increasing order in &/&c can be written down it would be desirable to see some way of expressing things in finite form to all orders in &/hc at once. Second, although it will be physically evident that the results obtained are equivalent to those obtained by conventional electrodynamics the mathematical proof of this is not included. Both of these limitations will be removed in a subsequent paper (see also Dyson).

The possible application of these methods to the various meson theories is discussed briefly. The formulas corresponding to a charge particle of zero spin moving in accordance with the Klein Gordon equation are also given. In an Appendix a method is given for calculating the integral appearing in the matrix elements for the simpler processes.

Briefly the genesis of this theory was this. The conventional electrodynamics was expressed in the Lagrangian form of quantum mechanics described in the Reviews of Modern Physics. The motion of the field oscillators could be integrated out (as described in Section 1.3 of that paper), the result being an expression of the delayed interaction of the particles. Next the modification of the delta-function interaction could be made directly from the analogy to the classical case. This (Rev. 75, 486 (1949). R. P. Feynman, Rev. Mod. Phys.;2 % 357 (1941). The applications; U1,3 (1949). QUANTUM ELECTRODYNAMICS 17 1) are not readily distinguishable, there is an intimate exchange of quanta. The fields are so closely determined by the motions of the particles that it is just as well not to separate the question into two problems but to consider the process as a direct interaction. Roughly, the field point of view is more practical for problems involving real quanta, while the interaction view is best for the discussion of the virtual quanta involved. We shall emphasize the interaction viewpoint in this paper, first because it is less familiar and therefore requires more discussion, and second because the important aspect of the problems with which we shall deal is the effect of virtual quanta.

The point of view which is taken here of the interaction of charges differs from the more usual point of view of field theory. Furthermore, the familiar Hamiltonian form of quantum mechanics must be compared to the over-all space-time view used here. The first section is, therefore, devoted to a discussion of the relations of these viewpoints.

Electrodynamics can be looked upon in two equivalent and complementary ways. One is as the description of the behavior of a field (Maxwell's equations). The other is as a description of a direct interaction at a distance (albeit delayed in time) between charges (the solutions of Liénard and Wiechert). From the latter point of view light is considered as an interaction of the charges in the source with those in the absorber. This is an impractical point of view because many kinds of sources produce the same kind of effects. The first point of view separates these aspects into two simpler problems, production of light, and absorption of light. On the other hand, the field point of view is less practical when dealing with close collisions of particles (or their action on themselves). For here the source and absorber are not readily distinguishable, there is an intimate exchange of quanta. The fields are so closely determined by the motions of the particles that it is just as well not to separate the question into two problems but to consider the process as a direct interaction. Roughly, the field point of view is more practical for problems involving real quanta, while the interaction view is best for the discussion of the virtual quanta involved. We shall emphasize the interaction viewpoint in this paper, first because it is less familiar and therefore requires more discussion, and second because the important aspect of the problems with which we shall deal is the effect of virtual quanta.

The Hamiltonian method is not well adapted to represent the direct action at a distance between charges because that action is delayed. The Hamiltonian method represents the future as developing out of the present. If the values of a complete set of quantities are known now, their values can be computed at the next instant in time. If particles interact through a delayed interaction, however, one cannot predict the future by simply knowing the present motion of the particles. One would also have to know what the motions of the particles were in the past in view of the interaction this may have on the future motions. This is done in the Hamiltonian electrodynamics, of course, by requiring that one specify besides the present motion of the particles, the values of a host of new variables (the coordinates of the field oscillators) to keep track of that aspect of the past motions of the particles which determines their future behavior. The use of the Hamiltonian forces one to choose the field viewpoint rather than the interaction viewpoint.

In many problems, for example, the close collisions of particles, we are not interested in the precise time sequence of events. It is not of interest to be able to say how the situation would look at each instant of time during a collision and how it progresses from instant to instant. Such ideas are only useful for events taking a long time and for which we can readily obtain information during the intervening period. For collisions it is much easier to treat the process as a whole. The Møller interaction matrix for the collision of two electrons is not essentially more complicated than the non-relativistic Rutherford formula, yet the mathematical machinery used to obtain the former from quantum electrodynamics is vastly more complicated than Schrödinger's equation with the δ/r⁴ interaction needed to obtain the latter. The difference is only that in the latter the action is instantaneous so that the Hamiltonian method requires no extra variables, while in the former relativistic case it is delayed and the Hamiltonian method is very cumbersome.

The Hamiltonian method is not well adapted to represent the direct action at a distance between charges because that action is delayed. The Hamiltonian method represents the future as developing out of the present. If the values of a complete set of quantities are known now, their values can be computed at the next instant in time. If particles interact through a delayed interaction, however, one cannot predict the future by simply knowing the present motion of the particles. One would also have to know what the motions of the particles were in the past in view of the interaction this may have on the future motions. This is done in the Hamiltonian electrodynamics, of course, by requiring that one specify besides the present motion of the particles, the values of a host of new variables (the coordinates of the field oscillators) to keep track of that aspect of the past motions of the particles which determines their future behavior. The use of the Hamiltonian forces one to choose the field viewpoint rather than the interaction viewpoint.

The point of view which is taken here of the interaction of charges differs from the more usual point of view of field theory. Furthermore, the familiar Hamiltonian form of quantum mechanics must be compared to the over-all space-time view used here. The first section is, therefore, devoted to a discussion of the relations of these viewpoints.

We illustrate these points in the next section by studying the solution of Schrödinger's equation for non-relativistic particles interacting by an instantaneous Coulomb potential (Eq. 2). When the solution is modified to include the effects of delay in the interaction and the relativistic properties of the electrons we obtain an expression of the laws of quantum electrodynamics (Eq. 4).

We study by the same methods as in I, the interaction of two particles using the same notation as in I. We start by considering the non-relativistic case described by the Schrödinger equation (I, Eq. X). The wave function at a given time is a function ψ(X₁, X₂, t) of the coordinates X₁ and X₂ of each particle. Thus call K(x₁, x₁', t; x₂', t') the amplitude that particle a at x₁' at time t' will get to x₁ at t while particle b at x₂' at t' gets to x₂ at t. If the particles are free and do not interact this is K⁰(x₁, x₁', t-t') K⁰(x₂, x₂', t-t') where K⁰ is the kernel function for particle a considered as free. In this case we can obviously define a quantity like K⁰, but for which the time t-t' need not be the same for particles a and b (likewise for t₂-t₂'); e.g., K(x₁, x₁', t₁, t₂; x₂', t₂', t₄) can be thought of as the amplitude that particle a goes from x₁' at t₁' to x₁ at t₁ and that particle b goes from x₂' at t₂' to x₂ at t₄.

When the particles do interact we can only define the quantity K(x₁, x₁', t₁, t₂; x₂', t₂', t₄) precisely if the interaction vanishes between t₁' and t₂' and also between t₁ and t₄. In a real physical system such is not the case. There is such an enormous advantage, however, to the concept that we shall continue to use it, imagining that we can neglect the effect of interactions between t₁' and t₂' and between t₁ and t₄. For practical problem this means choosing such long time intervals t₂-t₁ and t₄-t₂ that the extra interactions near the end.

pints have small of the over-all space-time view that they permit, are as relative effects. As an example, in a scattering problem easy to understand when interactions are defined as it may well be that the particles are so well separated when they are instantaneous. initially and finally that the interaction at these times As a further point, relativistic invariance will be self- is negligible. Again energy values can be defined by the evident. The Hamiltonian form of the equations de- average rate of change of phase over such long time velops the future from the instantaneous present. But intervals that errors initially and finally can be neg- the viewpoint of the theory of the S matrix of Heisen- lected.

This turns out to be not quite right: for when this interaction is represented by photons they must be of only positive energy, while the Fourier transform of S(Ebb-r5~fc contains frequencies of both signs. It should instead be replaced by S+(p~-rLw~)r e. This is to be averaged with ~a-~6+(-l~e-w~r) which arises when tS<k and corresponds to a emitting the quantum which b receives. Since

this means rIe-f4(tgp) is replaced by 6+(s&$) where ~,~~=r~ri;s "th-er s~qu~a re of the relativistically in-variant interval between points 5 and 5.

Since in classical electrodynamics there is also an interaction through the vector potential, the complete interaction (see A, Eq. (1)) should be (1- (V,.V~)&+(So~r sin), the relativistic case,

Hence we have for electrons obeying the Dirac equation, the formula of this interaction can be expressed very simply.

To see how this may be done, imagine first that the interaction is simply that given by a Coulomb potential e2/r where r is the distance between the particles. If this be turned on only for a very short time &lo at time C, where ra, and ybr are the Dirac matrices applying to the spinor corresponding to particles a and b, respec- tively, the first-order correction to K(3,4; 1,2) can be worked out in exactly two possible ways: (9) of X by an obvious general-ization. (17) of K to +r) B. D. being absorbed in the definition,

This is our fundamental equation for electrodynamics. It describes the effect of exchange of one quantum (therefore first order in 8) between two electrons. It will serve as a prototype enabling us to write down the corresponding quantities involving the exchange of two or more quanta between two electrons or the interaction of an electron with itself. It is a consequence of conventional electrodynamics. Relativistic invariance is clear. Since one sums over p it contains the effects of both longitudinal and transverse waves in a relativistically symmetrical way.

We shall now interpret Eq. (4) in the manner which will permit us to write down the higher order terms. It can be understood (see Fig. 1) as saying that the amplitude for "a" to go from 1 to 3 and "b" to go from 2 to 4 is altered to first order because they can exchange a quantum. Thus, "a" can go to 5 (amplitude K+(5, 1)), emit a quantum (longitudinal, transverse, or scalar, once (either in emission or in absorption), terms like r,,) and then proceed to 3 (&(3,5)). Meantime "b" goes to 6 (R+(6,2)), absorbs the quantum (f&,,) and proceeds to 4 (K+(4,6)). The quantum meanwhile proceeds from 5 to 6, which it does with amplitude S,(55B*). We must sum over all the possible quantum polarizations and positions and times of emission 5, and of the absorption 6. Actually if Is>& it would be better to say that "a" absorbs and "b" emits but no attention need be paid to these matters, as all such alternatives are automatically contained in (4).

The correct terms of higher order in 8 or involving larger numbers of electrons (interacting with themselves or in pairs) can be written down by the same kind of reasoning. They will be illustrated by examples as we proceed. In a succeeding paper they will all be deduced from conventional quantum electrodynamics.

Calculation from (4) of the transition element between positive energy free electron states gives the Mott scattering of two electrons, when account is taken of the Pauli principle.

The exclusion principle for interacting charges is handled in exactly the same way as for non-interacting charges (X). For example, for two charges it requires only that one calculate K(3,4; 1,2)-K(4,3; 1,2) to get the net amplitude for arrival of charges at 3 and 4. It is disregarded in intermediate states. The interference effects for scattering of electrons by positrons discussed by Bhabha will be seen to result directly in this formulation. The formulas are interpreted to apply to positrons in the manner discussed in I.

As our primary concern will be for processes in which the quanta are virtual we shall not include here the detailed analysis of processes involving real quanta in initial and final state, and shall content ourselves by only stating the rules applying to them. The result of the analysis is, as expected, that they can be included by the same line of reasoning as is used in discussing the virtual processes, provided the quantities are normalized in the usual manner to represent single quanta. For example, the amplitude that an electron in going from 1 to 2 absorbs a quantum whose vector potential, suitably normalized, is c,, exp(- ik-x)= Ce(%) is just the expression (X, Eq. (13)) for scattering in a potential with A (3) replaced by C (3). Each quantum interacts only once (either in emission or in absorption), terms like f,, Eq, (14)) occur only when there is more than one quantum involved. The Bose-Einstein statistics of the quanta can, in all cases, be disregarded in intermediate states. The only effect of the statistics is to change the weight of initial or final states. If there are among quanta, in the initial state, some of which are identical then the weight of the state is (1/8!)of what it would be if these quanta were considered as different (similarly for the final state).

## 3. SELF-ENERGY PROBLEM

Having a term representing the mutual interaction of a pair of charges, we must include similar terms to represent the interaction of a charge with itself. For under some circumstances what appears to be two distinct electrons may, according to I, be viewed also as a single electron (namely in case one electron was created in a pair with a positron destined to annihilate the other electron). Thus to the interaction between such electrons must correspond the possibility of the action of an electron on itself. This interaction is the heart of the self energy problem. Consider to first order in 8 the action of an electron on itself in an otherwise force free region. The amplitude K(2,1) for a single particle to go from 1 to 2 differs from K+(2, 1) to first order in 8 by a term

It arises because the electron instead of going from 1 directly to 2, may go (Fig. 2) first to 3, (K+(3, l)), emit a quantum (r,), proceed to 4, (K+(4,3)), absorb it (f,,), and finally arrive at 2 (K+(2,4)). The quantum must go from 3 to 4 (&+(srsZ)).

This is related to the self-energy of a free electron in the following manner. Suppose initially, time t, we have an electron in state j(1) which we imagine to be a positive energy solution of Dirac equation for a free particle. After a long time ts-!r the perturbation will alter the expression (X, Eq. (13)) for scattering in a potential with A (3) replaced by C (3). Each quantum interacts only

1 Although in the expressions stemming from (4) the quanta are virtual, this is not actually a theoretical limitation. One way to deduce the correct rules for real quanta from (4) is to note that in a closed system all quanta can be considered as virtual (i.e. they have a known source and are eventually absorbed) so that in such a system the present description is complete and equivalent to the conven tional one. In particular, the relation of the Einstein A and B coefficients can be r(edumd). A more practical direct deduction of the aprmsions for real quanta will be given in the aubmuent paper. It might be noted that (Q) can be re-written as dmribtng the d? on a, If"B(3, t)-iJK+(3, 5) A(K + 2),l) d o m po t e tia -d at io / 4-, =4 r& xJ f t r it o le m b B i " n c p u in f g ~ f e m ~ m t ' 2 ~ t ~ o ( d 6)( ~ 4= 6& k 17i~l s g 2 rt ( ;e 6 2) o ft r h o e d u f c .r ~ t db t K .1 pa I t * - ten * t T io h n e s o e f c f o . n A si d W era b ti s o i n e s r m an a d k e R . i t P a . p F w qy E n m un a l n ik e R ly ev h M& % . t b P c h o y n a - .

satid= - 17, 157 (tM),b at electmm do not aet on &ewiva, wi8 be a o/atlscj")4na(2,1). (5) sucewfut mnqti n quantam efeetr0dynatnies. the wave function, which can then be took& upon as volume. If normaliad to volume V, the result would a superposition of free particle mlutions (actually it simpfy be proportionaI to T,T his is expected, for if the only contains f). The amplitude that g(2) is contained eEst were quivalent to a change in enerw AE, the is m1cuXated as in (L, Eq, (2f)), The tlmgonaI element amplitude for arrival in f at fa is alter& by a factor (g=f) is therefore exp(-idE(t%-&)), or to first order by the BiBmence -ifaZ: Hence, we have JJ~(~)BK~o(z1,) fij(1)8rt@s. (71 AE=Z [(1271~+(4,3 1 ~e1~p(~ip.~)a )6+(IaI)dr(1 (9) The time intewal T= 12-ll (and the spatial volume V over which one integrates) must be taken very large, integrated over all space-time $74. This expression will for the expraions are only approximate (rmaXogous to be sirnp1ifit.d prexntly. In interpreting (9) we have the situation for two interacting charges).la This is Witty warned that the wave functions are nomalized ha,fox example, we are dealing inwrretfy with so that (as%) = (iiy41r)= l, The equation may therefore quanta. emitted just before which would normaHy be be made independent of the normaliation by writing rabsorbed at times aher t~. the left side as (M>(ar4%or) s,i nce (&/m)(Bu) If k'("(2, 1) from (6) is actually substituted into (7) and mhnt.=EbE, as Am(au) where Am is an equivalent the surface integrs~isc an be perfomed as was done in change in mass of the electron, Xn this form invariance obkining I, Eq. (22) rmulting in is obvious. One can likewise obtain an expression for the energy shift for sn eIectron in a hydrogen atom. Simply replace K+ in (g), ,by Il+.Cv', the exact kernel for an electron in Putting for fll) the plane wave u ex:xp(-@.1;_) where the potenttal, Ir=@8/r, of the atom, and j by a wave p w , = is n th 2 e ) , e a n nd e rp ~1 ( i p s 3 a an c d o n m st o a m nt e n & tu - m ind o ex f s th ym e j e b l o e t c , tr ( o 8 n ) p ge r n t e r i a s l n th e e g a & ti E ve w a h n ic d h i r n a u e E x t p s ( i - s d n d o E t T re ) al p . r T o h d e u i c m e a a g n in a e r x y - becomes ponenthlty decreiasing amplitude with tirne. This is because we are asking for the amplitude that an atom initsly with no photon in the field, witl diB appear after tirne T with no photon, If the atom is in a state which can radiate, this ampfltude must decay with time, The imaginary part of"^ when catcufated does the integrals exten&ng over the vofurne V and time indeed give the correct rate of mdiation from atomic intervai 2= Since K+($, 3) dqends only on the &Eerence states. It is zero for the ground state and for a free of the =ordinates of' 4 and 5, the integmi on 4 eledron. $v= a result (except nmr the sudaces of the redon) In the mn-relativistic region the exprmion for bE m i~ u de lt p e is n d af e n o to r d f e 3 r , V W T h . e n T h in e t e ef g f r ts a s t t e d is o p n r o 3 m , t r h ti e o r n ef a o l re to , t h V e , c re m hti b v e i s w ti o c r k re e g d i a o n u t ( p as i n hh t a s s 4 b e a e n n d d 3 o a n s e c b l y o s B e e to th g e e e t L h " e n r a t s h a e for the wave functions have been normalid to unit Gompton wave-length) the lil;(nw hich should appear in (8) can be rqhced to first order in V by K+ plus K+(i",(2,1) given in I, Eq. (53). The problem is then very shilar to the radiationless scattering probjem md below. The evaluation of (91, as are11 as all the other more complicated eqressions ariing in thm problems, is very much simpl%& by wor~ngin the mmentum and energy varkbles, rather than spae nd time. For this we shall need the Eourier Transfom of $(ss?) which is Fir, 3. Xntewdan af m eiatroa with itself. Mommtum space, Eq. Uli). which a n be obt;ii~edf rom (32 and (5) or from I, Tbb is disfud in rrfemam S in which it is inted out that Eq. (32) noting that 1+(2, 1) for &-0 b 6+(st;") from cclnccpt of a mve function IOW mm if &e arc de~syd pleE*Gam* B, A, Bcthe, Pbys, Rev, 72,339 (1947).

l0 1 fbf

FIG, 5. Comptan scattering, Erl, (151. FIG. 3, Ittirttarrvt correction to scattering, momentum space trated in Fig. &fa),f ind the ntktrix: I, Eq. (34). The F means (KeR)-I or more precisely the limit as M of (k-k+i&)-L Further @R means (2~)-~dkldFE2dkadkpI.f we imagine that quanta are par- ticles of zero mass, then we can make the genera1 rule that all poles are to be resolved by considering the For in this case, firstf2a quantum of momentum k is masses of the particles and quanta to have inffnitesimal emitted (r,), the electron then having momentum tregative imaginary parts, PS--k, and hence propagating with factor @I- k-?)-'. Using these results we see that the xlf-enerm (9) is Next ~ti s scattered by the potential (matrix a r teshal negative imaginary pat, (ll ) gives an infinite result when waluatd*T he infinity The function f+(s1z2) my still bve a discontinuity ariscrs, apparendy, from the coincidence of the B-function in value on the Ii@t cone, This is of no influence for the singufarities in K+($, 3) and 4(s4a2f.O nly at this point Dirm electron. For a particle satisfying the Rlein is it necasary to m&e a real dqarture from conven- Gordon equation, however, the interaction involves tional electrodynamics, a departure other thain simply gdients of the potential which reinstates the d func- rewriting ezpressions in a simpler form. tion if f has discontinuities. The condition that f is to We desire to make a modification of quantum eleetro- have no discontinuity in value on the light cone impties dmmics analogous to the modification of classical k2C(ka) appraaches aro as k2 approaches infinity, In electrodynamics described in a previous article, A, terms of G(k) the condition is There the &(slag)a ppearing in the action of interaction was rephced by where J(s)i s a function of small width and great height, The obviom comespondin@m; dif"ication in the quan- This condition will also be U& in discusing the con- tum theary is ta =$ace the &+(ss) appsring the vergence of vvacuun? polarization integmIs, quantum mechanical interaction by a new function The exprasion for the sezenergy matrix is now f+(s2). We can postulate that if the Fourier trans- form of the classical J(st22) is the integral over all R of F(k2)e xp(-ik.xtz)d4k, then the Fourier trwform of which, since e(kz)f aus off at temt as rapidly as 1/k2, f+.($\s") is the same inlegxa1 t&en over only positive fre- quenciies for &> tl and over only negative ones for which, since e(kz)f aus off at temt as rapidly as 1/k2, f I. u r n < c l t ~ i i o n n a l( n . a @) l = o = p j t ( o z - th z e c) a r n e l b a e ti o w n r i o t f t en &( * s s a ) s to S($), The h co e n r v a e f r t g e e r s . t h F a o t r C p f k ra 2 c ) t i i s c a s l i m p p u l p y - -X2/( w k e 2 - s - f k. x g a ) ll im su p p l p y o in s g e that =me average (with weight G(X)dX) over values of X may be taken afterwards. Since in all procmes the quantum momentum will be cantabed in at teat one extra factor 01 the form Cp-R-.m)-' representing X cos(]R ~)dkrEKg(KR),. propagation of an electron while that quantum is in the held, vve can expect aU such integrals with their may be apre?r~fdox pwitive RI as (A, Q. (26)) convergence hcrors to converge and that the result of all such pracessrts will now be finite and detinite {ex- cepting the p Itb clo~ldo op, discas& below, in which the inlegr%Isa rs over the moments of the electrons rather than the quanta), where &"G(X)dX= l and G involves values of X large The integral of (IQ) with C(P) - X2(kZ-- h2)-koting compared to m. This sixndy means that the ampfitude is (see Appendix A) *This reIalion is given incarrecdy in A, equiitian just pre- ceding lb. QUANTUM ELECTRODYNAMICS 177 When applied to a state of an electron of Illamenturn P Vile mwt now study the remaining terns (13) and satisfying pzl=mu, it gives for the change in mass (as (14). The integrar on k in (13) can be performed (aftw h B, Eq. (9)) mdtiplimtion by C(R3) since it involves nothing but the intepl (19) for the self-energy and the reult is: low& to operate on the initial sbte SE, (so that Ptlkr=ml). Hence the factor folloGring af#I-mf-%iii be just Am, But, if one ROW tries 10 expand l/(P1-m) We can now cornpteb the discussion of the radiative =(P~+m)/(nP-tlf~) one obtains an infinite result, corrections to sattering. In the integrails we include the convergence factor C(kZ),s o that they converge for large k. Xntqral (12 1 is also not eonverpnt because of the well-known infra-red cabstrophy. For this reason we catculate (as disrzusd in B) the vatue of the integml meuning the photons ta have a smaff mass Xm;,<<m<X, The integral (12) becomes which, since pla=mz. This is, however, just what is expected physically. For the quantum a nb e emitted and ab- sorbed at any time previous to the scattering. Such a proceps has the e8ect of a change in mass of the electron in the state 1. It therefore changes the energy by dE and the amplitude to first order in AE by -iAB.! where 1 is the time it is acting, which is infinite, Tbt is, the major effect of this term wuld be eanceted by the e@~t of ckange of mass 6%. which when integrated (see Appendix B) gives (e2/2r) times The situation can be analyzed in the following manner, We suppofe that the electron approaching the scrtttering potential a has not been free for an infinite which when integrated (see Appendix B) gives (e2/2r) times time, but at =me time far past suffered a scattering by a potential b. 11 we limit our discusion to the egects of Am and of the virtual radiation of one quantum be- tween two such scatterings each of tlre eEfects will be finite, though larp, and their Blgerence is determinate. The propagation from b to a is represented by a matrix in which one is to integrate possibly over P7depending on deails of the situation). (If the time is long between b and a, the energy is very nearly dekrmined m that 8'2 is very nearly m2.) We shall compare the effect on the matrix (25) of the where fq*)t = 2% sin@a nd we have assumed the m;ctrix to virtual quanb and af the chanp of mass Art&,T he egect operate between statetr of momentum #I and $z=#~+q of a virtual quantum is and have neglected term of order &,,,/m, dX, and q*/kz. Here the onIy dqendence on the convergence factor is in the term fa, where r=;1n(XJrn)-+9/4-2tn(~ltm,,>. (U) that of a chan~eo f mass can be written As we shall see in a moment, the other terms (131, whik (14) give contributions which just cancel the ra term. The remaining terms give for smaI1 q, and we are interested in the digerence (25)-(27). A (24. simple and direct rnethod of mrsking this comprison is just to evatuate the integral on k in (26) and subtract which shows the change in magnetic moment and the from the resuit the exprmsion (27) where Am is givm Lamb shift ils intepreted in more detail in B.'* in (21). The remainder can be expressed as a muttiple That the result given in B in Eq. (19) was in error rtdiyp ointed out u, the author, h private communiration, y V. F. ~eiwkopfa ad 5. B. Rench, as their ai~utatton,a m- d p i l f e l t e e r d e n s t i m re u s l u a l n t. e o F u re sl n y c h w h it a h s f t i h n e a l a ly u t s h h o o r w 's nm e t a h. d a y t a in l h L u O g IK h J, g th a e v e e x a - -he potentia l$ a and 6 in (25) (l - %rwt a ) n a d p rs re c s o s r io re n c t f , a r i t t h w e a r s a d rn ia c t r i r o rr n e l c e t s ty s ~ jo a i t n & e d d : r o in n g t B o , Bethe (1 's 8 ) n o o n r - ( r 2 e .6 l 1 1 a t a iv & is ? t rc Phyg. Rev. 75 1248 (19%) and N. E. Kroll and ,W, Fn hp4 result. He shows that the reiatiain Ln?k,,,-- l used by the Phys. Rev. 7~~~(3198418)) . The author feels unhepptly raponsble. author should have been in2k,n-S/5--.lnX,,,. This raufts in for the very considsnrble delay in the publiarran of French's adding a term --(l/@ to the I arithm in W Eq. (19) so thst the result otc~onedb y this error, Tllis foolnote is spprwriately result now agrees with that of7 R. Fren& ind V. F, Weidopf, numbered. (1-&r(p"l))b. In the finit, then, as fie-* the net tron the same type of term arises from the eBerts of a effect on the scattering is -3ra where r, the limit of virtual embsion and abmvtion both previous t;o the I@~a)s fi'*qS( assuming the integrals have an infra- red cut-off), turns out to be just equal to that givm in other prmesm. They, therefore, simply lead to the (25). An equak term -&a arEses from virtual tmnsitions same factor r so that the exprmion (23) may be used after the wttering (14) m that the entire 7a tern in directly and these renormalization integrah need not (22) is crmeeled. PR this problem of the radiative corrwtions to scatter- be computed afresh for each problem. The reason that r is just the value of (12) wben q2==0 ing the net result is insensitive to the cut-off. This can also be seen without a direct calculation as follows: means, of course, that by a simple rearrangement of Let us call the vector rzT length m in the dimtion of terms prwvious to the integration we could have avoided p' so that if &'z=m(l+~}2w e have P'== ((+E)# and we the use of the convergence factom completdy (see for b-k e t as very smalt, king of order Pi where 2" is the example Lfuuuisw7), The probkm was solved in the time between the scatterings b and a, Since W-m)-" manner here in order to illustrate how the use of such w+m)/(P'2-ntl) =,Cp+mf/2m2e, the quantity (25) convergence factors, wen when they are actually un- is of order 4€ or T. Re shall compute corrections to it necasary, may facilitate analysis some~vhatb y remov- only to its own order (s-9 in the limit e-4, The tern (27) can be written approximatelyBaPs ing the effort and ambiguities that may be involved in trying to rearrange the othmwl'w divergent terms. The rephcement of 8+ by f+ given in (161, (17) is The replacement of 8+ by f+ given in (161, (17) is not determined by the analam with the cksical prob- not determined by the analam with the cksical prob- lem. In the clrossical limit only the real part of 4 (i.e., lem. In the clrossical limit only the real part of 4 (i.e., using the expression (19) for Ant, The net of the two we have miLde here (in defining, m we have, the Ioctation egects b thmefore approgmatelyg6 of the ppoles of (57)) is arbitra-ary and almost certainty of the radiation resistance is calculated for an atom, as the imaginary part of (81, the result de- pends slightly an the function f+,O n the other hand the light ra&ted at very large disknces from a fource is a term nw of order l/c (since W-rn)-"@?~) indepndent of f4,T he total energy ahrkdb y distant absorkn will not chd with the en

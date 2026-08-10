# David Tong Lectures on Supersymmetric Quantum Mechanicssusyqm

> 来源文件：pre_David_Tong_Lectures_on_Supersymmetric_Quantum_Mechanicssusyqm.txt
> 字符数（约）：188332
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Supersymmetric Quantum Mechanics David Tong Department of Applied Mathematics and Theoretical Physics, Centre for Mathematical Sciences, Wilberforce Road, Cambridge, CB3 OBA, UK http://www.damtp.cam.ac.uk/user/tong/susyqm.html d.tong@damtp.cam.ac.uk

Recommended Books and Resources

There are very few decent textbooks that cover the material of these lectures. The handful of textbooks that exist with titles like “supersymmetric quantum mechanics” tend to focus on the slightly dull topics of exact solutions, rather than on the connections to geometry that we care about here. Nonetheless, there are two books that will be useful for what lies ahead: • Nakahara “Geometry, Topology and Physics” This book covers homology, cohomology, index theorems and Kähler manifolds, which is much of the mathematics you’ll need in these lectures. Later editions of the book also cover supersymmetric quantum mechanics towards the end although, in contrast to the rest of the book, the presentation of this material isn’t particularly good.

• Kentaro Hori, in the Clay Mathematics Monograph “Mirror Symmetry”.

This book is something of a mixed bag, with contributions from many authors. But the sections written by Kentaro Hori, which comprise Part 2 and Part 3 of the book (pages 143 to 480) are spectacularly good. Our lectures will largely follow the first few steps along the path laid down by Kentaro although I suspect that he would disapprove of the times I replace his rigorous statements with wild, but enthusiastic, handwaving. You can download the book directly from the Clay Mathematics Institute.

While decent books on the subject are in short supply, there is one resource that I strongly recommend. A remarkably large fraction of these lectures (not to mention subsequent developments in the field) is due to Edward Witten. His papers are not only brimming with beautiful physics, but are also models of scientific writing. If you want to learn large swathes of modern physics, you could do worse than turn to Witten’s papers. Those from the late 1970s and early 1980s are particularly accessible. Much of what we cover in these lectures can be found in the papers “Constraints on Supersymmetry Breaking” and “Supersymmetry and Morse Theory”. These, and a number of further resources, can be found on the course webpage.

Contents

0 Introduction 3 1 Introducing Supersymmetric Quantum Mechanics 5

## 1.1 Supersymmetry Algebra

1.1.1 A First Look at the Energy Spectrum 5

## 1.2 A Particle in a Potential

1.2.1 Ground States 9 1.2.2 The Witten Index 14

## 1.3 The Supersymmetric Action

1.3.1 Supersymmetry as a Fermionic Symmetry 19

## 1.4 A Particle Moving in Higher Dimensions

1.4.1 A First Look at Morse Theory 21 1.4.2 More Supersymmetry and Holomorphy 25 1.4.3 Less Supersymmetry and Spinors 29 2 Supersymmetry and the Path Integral 33

## 2.1 The Partition Function and the Index

2.1.1 An Example: The Harmonic Oscillator 35 2.1.2 Fermions: Periodic or Anti-Periodic? 38 2.1.3 The Witten Index Revisited 42

## 2.2 Instantons

2.2.1 Tunnelling 49 2.2.2 The Dilute Gas Approximation 54

## 2.3 Instantons and Supersymmetry

2.3.1 Fermi Zero Modes 57 2.3.2 Computing Determinants 59 2.3.3 Computing the Ground State Energy 61 2.3.4 One Last Example: A Particle on a Circle 63 3 Supersymmetry and Geometry 65

## 3.1 The Supersymmetric Sigma Model

3.1.1 Quantisation: Filling in Forms 71 3.1.2 Ground States and de Rham Cohomology 74 3.1.3 The Witten Index and the Chern-Gauss-Bonnet Theorem 80

## 3.2 Morse Theory

3.2.1 Instantons Again 87 3.2.2 The Morse-Witten Complex 95

## 3.3 The Atiyah-Singer Index Theorem

3.3.1 The N = 1 Sigma Model 98 3.3.2 The Path Integral Again 100 3.3.3 Adding a Gauge Field 104

## 3.4 What Comes Next?

Acknowledgements

This course is aimed at beginning graduate students. It assumes a good background in quantum mechanics and path integrals and a basic knowledge of differential geometry, say at the level of my lecture notes on General Relativity. The course is based largely on lectures by Kentaro Hori and David Skinner. I’m particularly grateful to David Skinner and Oscar Randal-Williams for patiently explaining a number of issues to me. I also thank Andy Zhao for helping me get minus signs right in the susy variation of the sigma model action.

0 Introduction

It will come as no surprise to hear that there is a close relationship between mathematics and physics. Yet, for many centuries, the relationship was more than a little one sided. There was, in the language of marriage counsellors, a lack of equitable reciprocity. Physicists took, but gave little in return. Admittedly there were exceptions, some of them rather important like Newton’s development of calculus. Nonetheless, it remains true that mathematics is a tool that us physicists cannot live without, while many mathematicians have no more use of physics than they do of chemistry or botany.

In the last few decades, this narrative has started to change. Physicists have been giving back. As our understanding of quantum field theories has grown, we have uncovered increasingly sophisticated mathematical structures lurking within. These are largely, but not exclusively, the structures that arise in geometry and topology. Using physicist’s methods and techniques to solve quantum fields theories has revealed connections to these mathematical ideas. Initially this gave new ways of deriving results well known to mathematicians. But, as the quantum field theories became more involved, so too did the mathematics until physicists were able to discover new results that came as a complete surprise to mathematicians. Prominent among these is an idea called mirror symmetry, a novel relationship between different manifolds.

You might reasonably wonder what advantage physicists have over mathematicians in this game. After all, we’re certainly not smarter. (At least, not most of us.) And yet, there are times when we are able to leapfrog mathematicians and then turn around and present them with new results that sit firmly within their area of expertise. This seems unfair, like physicists have some kind of secret weapon that mathematicians are unable to wield. And we do. In fact, we have two. The first is the path integral. The second, a wilful disregard for rigour.

These two weapons are not unrelated. The path integral approach to quantum field theory has so far evaded attempts to be placed on a rigorous footing, at least beyond quantum mechanics. This means that most often the physicist’s approach to these questions does not meet the mathematician’s bar for proof. Physics is perhaps better thought of as an idea generating machine, giving new insights into areas of mathematics that can subsequently be proven using more traditional methods. Happily, in most cases, these subsequent proofs have turned out to be much more than an exercise in dotting i’s and crossing ℏ’s. Mathematicians take their own path to a problem, developing new ideas along the way, and these then feed back into our understanding of quantum field theory. Over the past few decades this process has resulted in a harmonious and extraordinarily fruitful relationship between communities of physicists and mathematicians.

This interaction has revolutionised certain areas of mathematics. For example, it’s difficult to envisage a thriving field of symplectic geometry without mirror symmetry. But it has also changed what we mean by “mathematical physics”. Towards the end of the 20th century, this was viewed as a rather dry subject and mostly involved bringing a mathematician’s level of pedantry to bear on problems that physicists care about, but with little insight flowing back into the underlying physics. Now, this situation has been reversed, with interesting and exciting ideas flowing in both directions. To emphasise the shift of focus, this new activity is sometimes rebranded “physical mathematics”.

Much of this interplay between physics and mathematics takes place in the arena of supersymmetric field theories. (There are important exceptions, Witten’s Fields medal winning work on knot polynomials in Chern Simons theory among them.) Supersymmetric theories are a class of quantum field theories that have a symmetry relating bosons and fermions. There is, so far, no experimental evidence that supersymmetry is a symmetry of our world. But supersymmetric theories have a number of special properties that allow us to make much more progress in solving them than would otherwise be possible. It is often in these solutions to supersymmetric field theories that we find results of interest to mathematicians.

The purpose of these lectures is to take the first few steps along this journey. Sadly we will not reach the heights of the subject like mirror symmetry or knot invariants, both of which require quantum field theories in higher dimensions (d = 1 + 1 and d = 2 + 1 respectively). Instead, we will restrict ourselves to d = 0 + 1 dimensional quantum field theories, also known as quantum mechanics. We will study a number of examples of supersymmetric quantum mechanics and, in solving them, recover some of the highlights of 20th century geometry, including ideas of de Rham, Hodge, Morse, Atiyah and Singer.

I should warn you that the level of rigour when addressing the more mathematical aspect of these lectures will be mediocre at best. Anyone with a real interest in these ideas is encouraged to learn both the underlying mathematics and physics to truly appreciate how the two connect. But that is not the path we will take here. Instead, these lectures will assume only a basic knowledge in differential geometry (at the level, say, of my lectures on General Relativity.) We will then use supersymmetric quantum mechanics as a vehicle to take us deeper into the mathematician’s territory, allowing us to take a peek at some of the beautiful vistas that await.

1 Introducing Supersymmetric Quantum Mechanics

In this section, we discuss some basic facts about supersymmetry ric quantum mechanics.

Our focus will be on a simple class of quantum mechanical systems that, while they have a certain elegance, won’t exhibit any deep mathematics. Instead, we will treat them as a proving ground, allowing us to build some intuition for supersymmetry while developing a number of useful calculational techniques. We’ll then bring these to bear on problems with a deeper mathematical pedigree in Section 3.

## 1.1 Supersymmetry Algebra

Supersymmetric quantum mechanics is the name given to a class of Hamiltonians H that can be written as H = {Q,Q†} with Q² = 0 (1.1)

Here {A,B} = AB + BA is the anti-commutator. The operator Q is called the supercharge and, as you can see, is something like the square root of the Hamiltonian. Equation (1.1) is called the supersymmetry algebra. As we will see, Hamiltonians that can be written in this way enjoy many special properties.

1.1.1 A First Look at the Energy Spectrum The first property is straightforward: the energy of any state is necessarily non-negative. To see this, we just take the usual expectation value in a state |ψ⟩, ⟨ψ|H|ψ⟩ = ⟨ψ|Q†Q + QQ†|ψ⟩ = |Q|ψ⟩|² + |Q†|ψ⟩|² ≥ 0 Furthermore, we see that energy E is only zero for states |ψ⟩ that are annihilated by both the supercharge and its adjoint E = 0 ⇔ Q|ψ⟩ = Q†|ψ⟩ = 0 (1.2)

Already, the statement that we have a positive definite spectrum is slightly surprising. Usually in quantum mechanics, we don’t care about the overall energy of states since we can always add a constant to the Hamiltonian without changing the physics. But that’s not the case for supersymmetric quantum mechanics (nor, indeed, for supersymmetric quantum field theories). The requirement that E ≥ 0 also rules out some very familiar quantum mechanical potentials, like V = −1/r of the hydrogen atom. The potential in supersymmetric quantum mechanics must always be positive definite.

As an aside: there’s only one other place in physics where we care about the overall value of the ground state energy, and that’s the cosmological constant in general relativity. So far, sadly, no plausible link has been found between the value of the cosmological constant and the supersymmetry algebra.

We can learn more from the supersymmetry algebra. The energy eigenstates of supersymmetric quantum mechanics are almost always degenerate. Consider the set of states with some fixed energy E, H|ψ⟩ = E|ψ⟩ It’s simple to check from the supersymmetry algebra (1.1) that [H,Q] = [H,Q†] = 0, facts which require us to also use Q² = Q†² = 0. This means that the operators Q and Q† act within an energy eigenspace. If the energy is E ≠ 0, we have {Q,Q†} = 2E ⇒ {c,c†} = 1 with c = Q / √(2E) (1.3)

We also have c² = c†² = 0. This is the same algebra that is formed by fermionic creation and annihilation operators. The algebra has a two-dimensional irreducible representation spanned by the states |0⟩ and |1⟩ with the properties that c|0⟩ = 0 and |1⟩ = c†|0⟩ Equivalently we have c†|1⟩ = 0 and |0⟩ = c|1⟩. The algebra is telling us that all energy eigenstates with E ≠ 0 states must come in pairs. Of course, there could be a still bigger degeneracy, with several pairs all having the same energy. But, at each energy level, the number of states must be even.

The one exception is when we have states with energy E = 0. As we’ve seen, if such states exist then they are necessarily the ground states. Importantly, the argument above that enforces the degeneracy of the spectrum fails: it is quite possible to have a lone ground state |Ω⟩ because, as we can see in (1.2), any such ground state necessarily obeys Q|Ω⟩ = Q†|Ω⟩ = 0. Again, it’s quite possible to have more than one ground state. But if that’s the case, they’re not related by the action of Q or Q†.

Finally, there is a slightly more formal way of viewing the story above. Inspired by the connection to fermionic creation operators, we define the “fermion number operator” F = c†c This obeys [F,Q] = −Q and [F,Q†] = Q† and [F,H] = 0. Clearly this operator is well defined only on states with energy E ≠ 0, where it acts as F|0⟩ = 0 and F|1⟩ = |1⟩. Correspondingly, the Hilbert space decomposes into “bosonic states” with F = 0 and “fermionic states” with F = 1, H = H_B ⊕ H_F (1.4)

We say that there is a Z grading of the Hilbert space. The E ≠ 0 pairs have one state in H_B and one in H_F. As it stands, it’s not clear which of these Hilbert spaces we should assign the E = 0 states to. This will become clearer when we turn to specific examples below.

Finally, one last piece of terminology. If a ground state with energy E = 0 exists, then we say that supersymmetry is unbroken. If the ground state has energy E > 0 then we say that supersymmetry is broken. This language is really adopted from higher dimensions where symmetries that do not leave the vacuum invariant are said to be “spontaneously broken”. In the present context we say that supersymmetry is broken if the vacuum is not annihilated by the supercharges: the connection to symmetries will become clearer as we proceed.

## 1.2 A Particle in a Potential

An abstract algebra like (1.1) is all well and good, but to build intuition we really need a concrete example that realises this algebra. Happily such an example exists: we consider the quantum mechanics of a particle moving on a line. The only small novelty is that the particle has an internal degree of freedom, like spin, that can take two different values. The Hilbert space is H = L²(ℝ) ⊗ ℂ² where the L²(ℝ) means normalisable functions on the real line ℝ which, of course, is simply the Hilbert space for a particle on a line. Meanwhile the ℂ² factor is the internal degree of freedom. In keeping with the notation of the previous section, we’ll take the internal states of the ℂ² factor to be spanned by |0⟩ and |1⟩. The Hilbert space then decomposes into our “fermionic” and “bosonic” pieces, H = L²(ℝ)|0⟩ ⊕ L²(ℝ)|1⟩ = H_B ⊕ H_F In this context, it might be better to think of |0⟩ and |1⟩ as a spin degree of freedom, with H_B and H_F the “spin down” and “spin up” components of the Hilbert space. On the other hand, it might be confusing to think of “spin up” as a fermion and “spin down” as a boson so I stress that these are just names at this stage and don’t come with any other fermionic/bosonic connotations. We’ll use both pieces of terminology in what follows.

For our supercharge Q, we take Q = (p − i h′(x)) ⊗ ( 0 0 ; 1 0 ) (1.5)

Here p = −i d/dx is the usual momentum operator (in units where ℏ = 1) and h(x) is a real function. We have Q² = 0 because the 2×2 matrix squares to zero. Taking the conjugate gives Q† = (p + i h′(x)) ⊗ ( 0 1 ; 0 0 ) (1.6)

and so H = (1/2)(QQ† + Q†Q) = (1/2)(p² + h′²) 1 − (1/2) h′′ σ₃ (1.7)

The first factor is the familiar Hamiltonian for a particle with unit mass moving on a line with potential V(x) = (1/2) (dh/dx)² (1.8)

This term comes with the 2 × 2 unit matrix 1 and so doesn’t care about the spin of the particle. In contrast, the second term comes with the Pauli matrix σ₃ = ( 1 0 ; 0 −1 )

This term acts like a magnetic field, distinguishing spin up and spin down by the minus sign.

The operator F that distinguishes spin up from spin down is simply F = ( 1 0 ; 0 0 ) (1.9)

This tells us that the “bosonic” or “spin down” part of the Hilbert space H_B is composed of states of the form ψ(x)|0⟩ = ψ(x) ( 0 ; 1 ) and the “fermionic” or “spin up” part of the Hilbert space H_F is composed of states of the form ψ(x)|1⟩ = ψ(x) ( 1 ; 0 ). Note that the definition of F now happily extends to the zero energy states as well.

1.2.1 Ground States Usually, it is challenging to find the exact ground states of any quantum mechanical potential. One of the rather pretty features of supersymmetric quantum mechanics is that we can sometimes find exact expressions for the ground states.

To kick things off, let’s look at the semi-classical ground states. The potential energy (1.8) is positive definite and has a minimum whenever there is a critical point of h, V(x) = 0 ⇔ h′(x) = 0 If we Taylor expand around such a critical point x = x₀, we have h(x) ≈ h(x₀) + ω(x − x₀)² + ...

This gives a potential energy (1.8) that is, to leading order, a harmonic oscillator, V(x) = (1/2) ω² (x − x₀)² + ...

While the classical ground state energy of a harmonic oscillator vanishes, quantum mechanically we have E = (1/2)|ω| (working in units with ℏ = 1.) But the supersymmetric system also gets a contribution only from the spin-dependent term in (1.7) which, at leading order, is ΔE = ± |ω| (1.10)

If we take the minus sign, this precisely cancels the contribution from the harmonic oscillator ground state energy, giving us a total, semi-classical energy E = 0. This simple minded analysis shows that it’s quite plausible that zero energy ground states exist in this system.

Let’s now look more closely at the full quantum problem and, in particular, the question of whether E = 0 ground states exist. A general state takes the form Ψ(x) = ( ψ(x) ; ϕ(x) ) (1.11)

But to qualify as an E = 0 ground state, this must be annihilated by both the supercharges, QΨ = Q†Ψ = 0, meaning that ( −i d/dx + h′ ) ψ = 0 and ( −i d/dx − h′ ) ϕ = 0 The magic of supersymmetry means that, at least for the ground state, the Schrödinger equation has morphed from a challenging second order differential equation into a pair of decoupled, first order differential equations. Note that this same trick doesn’t work to figure out the excited states of the theory. We can’t solve for the whole spectrum. But we can solve for the ground state.

Indeed, the equations are straightforward to solve. We have ψ(x) = e^{-h} and ϕ(x) = e^{+h} (1.12)

There is, as always in quantum mechanics, one last criterion: we need to determine if these states are normalisable. This clearly depends on the form of h(x) which, in turn, determines the potential energy (1.8). There are three possibilities • If h → +∞ as |x| → +∞ then ψ(x) is normalisable and we must have ϕ(x)

=0.

In this case there is a unique ground state that sits in the "fermionic" or "spin up" part of the Hilbert space H.

• If h → −∞ as |x| → +∞ then ϕ(x) is normalisable and we must have ψ(x) = 0. In this case there is a unique ground state that sits in the "bosonic" or "spin down" part of the Hilbert space H.

• If h has neither of these properties, then there is no E = 0 ground state and supersymmetry is broken. In this case the ground state necessarily has E ≠ 0 and is degenerate.

To get a better sense of what's going on, let's look at some simple examples.

Example 1: Quadratic h To start, we take h = 1/2 ω x^2 with ω > 0. In this case, we just have a harmonic oscillator with potential energy given by V(x) = 1/2 ω^2 x^2. The additional spin-dependent term in the Hamiltonian just shifts the spectrum up or down by 1/2 ω. The upshot is that the "fermionic" or "spin up" spectrum in H takes the form E = ω n, n = 0,1,2...

Here we find the unique ground state. Meanwhile, the "bosonic" or "spin down" spectrum in H takes the form E = ω n, n = 1,2,...

As promised, all excited states with E > 0 are paired, but there is a single unpaired ground state at E = 0.

Figure 1. The potential for a cubic h has two classical E = 0 ground states.

Note that, had we chosen ω < 0, the situation would be reversed with the ground state living in H.

Example 2: Cubic h When h is a polynomial of degree higher than two, we can't solve the entire spectrum. But we can get a good understanding of the ground states. Suppose that we take h = λ x^3 +...

where ... are lower order monomials. As we have seen, in this case there can be no E = 0 ground states.

A typical form of h is shown on the left of Figure 1, with the corresponding potential V(x) on the right. If we neglected the spin degree of freedom, we would have the familiar double well potential of quantum mechanics and we have some intuition about what happens in this case. Clearly there are two classical minima with V(x) = 0 and we can construct an approximation to the ground state with a Gaussian wavefunction that is localised at one, or other, of the minima, as shown on the right, with the orange and green curves each showing different candidate ground state wavefunctions.

Since h'' < 0 near the left-hand minimum we expect that this wavefunction can lower its energy by sitting in the "spin down" part of the Hilbert space H. Similarly, h'' > 0 near the right-hand minimum so we expect that it's energetically preferable for this wavefunction to sit in H.

Figure 2. The potential for a quartic h has three classical E = 0 ground states.

Usually in a double well potential, the particle can lower its energy by tunnelling through the barrier and sitting in a superposition of both states. But that's not the case here because the two wavefunctions live in different components of spin space. This kills the possibility for tunnelling. Instead, the supersymmetric set-up is closer to our naive, classical guess of the ground states, with a Gaussian around each minima giving a good approximation to the ground state. Our arguments above tell us that the energy of this two-fold degenerate ground state is necessarily E > 0. We will say more about tunnelling in this system and how to compute the actual energy in Section 2.2.

Example 3: Quartic h Next consider h(x) of the form h = λ x^4 +... (1.13)

where ... are terms of order cubic and lower. We pick λ > 0 so that h → +∞ as |x| → ∞.

A typical h(x) and the associated potential V(x) are shown in Figure 2. There are now three classical ground states and a naive semi-classical approach would suggest that we can approximate the true ground states as Gaussians localised around any of these three minima. The two outside minima have h'' > 0 and so the lowest energy wavefunctions live in H, while the middle minimum has h'' < 0 and so the lowest energy state sits in H.

Figure 3. The exact E = 0 wavefunction is localised only on the outer minima.

However, this time we know the exact ground state: it is given by ψ(x) = e^{-h(x)} and lives in H. This is plotted in orange, superposed on the potential, in Figure 3. The wavefunction is peaked on those places where h < 0 which, in this case, means the two outer minima. This clearly demonstrates the tunnelling phenomena, in which the true ground state sits in a superposition of minima but, as you can see, there is not necessarily a symmetric distribution between the two vacua.

We started with three states that we thought had the smallest energy – one for each minima – but only one survives as the true E = 0 ground state. The other two states must have some small, but non-zero energy. These states are the Gaussian localised in the middle vacuum, and the combination of states localised on the outside minima that is orthogonal to the ground state. Although it is far from obvious from staring at the potential, supersymmetry tells us that the energies of these states must be degenerate.

As we vary the parameters in the function h(x), the energy spectrum of the theory will change. However, the energy of the ground state remains pinned to E = 0. The one exception to this statement occurs if we send λ → 0. In this case, one of the minima of the potential runs off to infinity, as x ∼ 1/λ, and carries the E = 0 ground state wavefunction with it. In this case, we go over to the situation of a cubic h(x) described above in which there are two ground states, both with E > 0.

1.2.2 The Witten Index The robustness of supersymmetric ground states can be formulated more generally using the Witten index. As we've seen, the Hilbert space decomposes into two pieces H = H_B ⊕ H_F These two pieces are characterised by the "fermion number operator" F which has eigenvalues 0 or 1. It is often more useful to consider the operator (-1)^F, sometimes called fermion parity, that takes eigenvalues +1 on states in H_B and −1 on states in H_F. For our example of a particle on a line, it's simple to check that (-1)^F = −σ3.

The Witten index is defined as I = Tr(-1)^F e^{-β H} Here the trace is taken over all states in the Hilbert space. The parameter β plays a role like inverse temperature β = 1/k T in statistical mechanics. The Witten index differs from the usual statistical mechanical partition function by the signs (-1)^F.

Importantly, as we will now argue, in supersymmetric theories the Witten index is actually independent of β, dI/dβ = 0 This follows because, as we have seen, the spectrum of supersymmetric quantum mechanics is degenerate for any state with E > 0. Formally, there is an isomorphism between H_B and H_F, H_B|_{E>0} ∼ = H_F|_{E>0} This means that the trace over any state with E > 0 simply cancels out in the Witten index: for every +e^{-βE} from H_B there is a corresponding −e^{-βE} from H_F. This means that the Witten index only receives contributions from the zero energy states which, as we've seen, need not be duplicated in both H_B and H_F. In other words, the Witten index really counts the difference in the number of ground states in each sector, I = dim H_{0,B} − dim H_{0,F} where H_{0,B} is the space of E = 0 bosonic ground states, and similar for H_{0,F}.

Before we proceed, a few comments. Since I doesn't depend on β, you might wonder why we don't just set β = 0 and consider Tr(-1)^F. Indeed, often the Witten index is written in this way as shorthand, but it's a dangerous thing to do. The quantity Tr(-1)^F is an infinite series of +1 and −1 and by pairing terms together in various ways you can get any answer that you like. Including e^{-β H} in the definition acts as a regulator for this sum, rendering it finite. Of course, it's a familiar regulator because it also appears in the partition function in statistical mechanics.

The same arguments that show dI/dβ = 0 also show that I is independent of the parameters of the Hamiltonian H. This was demonstrated in the examples above although, as we also saw, it comes with a caveat: if you change the Hamiltonian too dramatically then you can lose states in your Hilbert space and this will change I. This happens for the particle on a line whenever we change the power of the leading term in h(x).

The Witten index counts the difference between the bosonic and fermionic E = 0 states. However, in the simple examples considered above, it actually counts the number of E = 0 states, positive if they're bosonic, negative if they're fermionic. One might wonder if, in practice, it always does this. Indeed, there is some intuition that suggests this is the case. If there's no good reason for pairs of states to be stuck at E = 0 then, as you vary parameters in the potential, it's tempting to think that they will be lifted to E > 0.

However, it's not difficult to exhibit examples where, for example, I = 0 but there are a pair of bosonic and fermionic E = 0 states. A particularly simple example arises from particle moving on a circle S^1 of radius R. The supercharge and Hamiltonian take the same form as before and are characterised by a periodic function h(x) = h(x+2πR). We can follow our earlier footsteps to find a two parameter family of ground states labelled by α,β ∈ C, Ψ(x) = ( e^{-h} 0; 0 e^{+h} ) α + β This time, because the particle lives on a circle, there is no issue with the normalisability of the wavefunction. We see that the system has two linearly independent E = 0 ground states for any choice of h. Yet, because one ground state lives in H and the other in H_F, the Witten index of this system is I = 0. The potential (in blue) and wavefunctions (in orange and green) for h(x) = sin(x/R) are shown in Figure 4.

Figure 4. Two E = 0 ground states for the double well potential on a circle.

For this particle on the circle, the pair of states sticks at E = 0 as we change the parameters of h, even though these ground states are not protected by the Witten index. One might wonder if there's a deeper reason for this. There is and it's related to the deeper mathematical concept...

The request was rejected because it was considered high risk Start with a direct generalisation of our earlier supersymmetric system to a particle moving in R^n, parameterised by coordinates x_i with i = 1,...,n. The observation that supersymmetry relates bosonic to fermionic fields suggests that we should also introduce n Grassmann valued fields ψ_i, with i = 1,...,n. These obey the anti-commutation relations {ψ_i,ψ_j} = {ψ†_i,ψ†_j} = 0 and {ψ_i,ψ†_j} = δ_ij (1.23)

As in our previous discussion, these fermionic fields should be viewed as operators acting on some internal, finite dimensional Hilbert space. To construct a representation we introduce the "Fock vacuum" state |0⟩ that obeys ψ_i|0⟩ = 0 for all i = 1,...,n We can then build up the space of states by acting on |0⟩ with ψ†_i, recalling that you only get to act with a given ψ† once. This means that the spectrum of internal states takes the form |0⟩ ψ†_i|0⟩ ψ†_iψ†_j|0⟩ ψ†_1...ψ†_n|0⟩ There are \binom{n}{p} states in the sector where we act with p different ψ†'s. The total number of states is then \sum_{p=0}^{n} \binom{n}{p} = (1+1)^n = 2^n where you should expand out the (1+1)^n in the middle using the binomial theorem to get the sum on the left. This means that our supersymmetric quantum mechanics will describe a particle moving in R^n with 2^n internal states.

There's a useful geometrical way to think about these states. At the top of the pyramid depicted above we have wavefunctions that look like ϕ(x)|0⟩: these are just functions over R^n.

At the next level, the wavefunctions look like ϕ(x)ψ†_i|0⟩ and come with an internal index i = 1,...,n. We usually think of objects on R^n that carry such an index as vectors. However, as we now explain, the anti-symmetric nature of the Grassmann variable means that it's much more natural to think about these states as one-forms on R^n.

We really see why it's useful to think of these states as forms when we get to the second level. Here wavefunctions look like ϕ(x)ψ†_iψ†_j|0⟩ = -ϕ(x)ψ†_jψ†_i|0⟩, with the i,j index necessarily anti-symmetric. But this is precisely the definition of a two-form in differential geometry. This then continues until we reach the unique top form ψ†_1...ψ†_n|0⟩. All of this suggests that we should make the identification between Grassmann variables and forms ψ†_i ↔ dx_i ∧ On R^n, there's little advantage to be had in working with p-forms rather than just sticking with Grassmann variables and, for the rest of this section, we'll use the latter notation. However, this relationship to p-forms will be of crucial importance when we turn to more geometrical settings in Section 3.

The supersymmetric quantum mechanics also has a fermion parity operator (-1)^F which simply counts the number of excited fermions mod 2. By convention, we take F|0⟩ = 0 so (-1)^F|0⟩ = +1. Then if |p⟩ denotes a state in the sector with p excited fermions, we have (-1)^F|p⟩ = (-1)^p|p⟩ (1.24)

In other words, (-1)^F counts the degree of a p-form, mod 2.

The Supersymmetric Hamiltonian The supersymmetric quantum mechanics for a particle moving in R^N involves a real function h(x_i) and the Hamiltonian H = 1/2 Σ_{i=1}^n (p_i^2 + (∂_i h)^2) - 1/2 Σ_{i,j} ∂_i ∂_j h [ψ†_i, ψ_j] (1.25)

It's not difficult to check that this can be written in the defining way H = 1/2 {Q, Q†} with the standard (anti)-commutation relations and the supercharges Q = (p_i - i ∂_i h) ψ_i and Q† = (p_i + i ∂_i h) ψ†_i (1.26)

where summation convention is used, both for the supercharges and the final term of the Hamiltonian.

We can compute the Witten index by looking at the semi-classical ground states. The bosonic part of the Hamiltonian has a ground state at any critical point x = X, ∂_i h(X) = 0 for all i = 1,...,n But where does this ground state sit in the internal space? First recall what happened in the simpler case where we just had one fermion and, correspondingly, two states |0⟩ and |1⟩ with ψ|0⟩ = 0 and |1⟩ = ψ†|0⟩. In that case, the final term in the Hamiltonian was H_Fermi = - h'' [ψ†, ψ]

So acting on the two states, we had H_Fermi |0⟩ = + h'' |0⟩ H_Fermi |1⟩ = - h'' |1⟩ So in that simpler case, if h'' > 0 at the critical point, then we lower the energy by sitting in the state |1⟩, while if h'' < 0 then we should sit in |0⟩. This can be seen in the various examples that we explored in the previous section.

Now let's return to the multi-fermion case, with H_Fermi = - Σ_{i,j} ∂_i ∂_j h [ψ†_i, ψ_j]

At each critical point x = X, we should think of the Hessian ∂_i ∂_j h(X) as a matrix, with a collection of eigenvectors e_j and eigenvalues λ_a. In fact, to align with other conventions, it turns out to be best to think of the eigenvalue equation of the matrix -∂_i ∂_j h, -(∂_i ∂_j h) e_k = λ_k e_k (1.27)

where k = 1,...,n labels the different eigenvectors and shouldn't be summed over. The generalisation of the story above is now the following: for each negative eigenvalue λ_k < 0, we should excite the corresponding collection of fermions e_k^j ψ†_j. Meanwhile, for each positive eigenvalue λ_k > 0, we should just leave well alone: we're better off in the unexcited state. At a given critical point x = X, the semi-classical ground state then sits in the part of the Hilbert space given by |ground⟩ ∼ \prod_{k \text{ with } λ_k < 0} (e_k^j ψ†_j) |0⟩ We define the Morse index to be μ(X) = The number of negative eigenvalues of -∂_i ∂_j h(X) (1.28)

(We picked the eigenvalues of -∂_i ∂_j h rather than +∂_i ∂_j h so that this definition of the Morse index, in terms of negative rather than positive eigenvalues, is the standard one.) The ground state around the critical point X sits in the sector with μ(X) excited fermions. In the geometrical language, this means that the ground state wavefunction is a p-form, where p = μ(X) is the Morse index.

Now we can put everything together. We know that the Witten index only receives contributions from the ground states, and we now know that these are associated to critical points X of h, and live in the sector with μ(X) excited fermions. We will assume that h(x) is chosen to be suitably generic so that there are no degenerate critical points. Then, using our previous result (1.24), we have \sum_X Tr((-1)^F e^{-βH}) = \sum_X (-1)^{μ(X)} (1.29)

where the sum is over all critical points X of h.

Note that we're not assuming that all critical points of h correspond to true E = 0 ground states of the theory. It may well be that some get lifted to non-zero energy and, later in these lectures, we'll put in some effort to understand when this happens. But that's not relevant for computing the Witten index since any such states must get lifted in pairs and so cancel out.

The same formula (1.29) also holds for our earlier model with a single x and ψ. There a maximum of h was necessarily followed by a minimum, so the sum over critical points could never exceed +1 or drop below -1. Now, however, we could have multiple ground states. For example, we could have a situation where all the critical points X have μ(X) even. In this case, they all contribute +1 to the Witten index and each of them must correspond to a true, E = 0 ground state of the system.

1.4.2 More Supersymmetry and Holomorphy It is quite possible for a quantum system to be invariant under more than one supersymmetry transformation. The extended supersymmetry algebra replaces (1.1) with {Q_α, Q†_β} = H δ_{αβ} and {Q_α, Q_β} = {Q†_α, Q†_β} = 0 (1.30)

with α,β = 1,...,q. A Hamiltonian that can be written in this form is said to have N = 2q supersymmetries, with the 2 because each Q is complex. In this convention, the kind of quantum mechanics that we considered up until now is said to have N = 2 supersymmetry. (I should warn you that the nomenclature for counting supersymmetry generators in quantum mechanics is not completely standard: things settle down once we go to higher dimensional quantum field theories.)

In this section, we'll construct a quantum mechanical model that has N = 4 supersymmetry, meaning two complex supercharges Q_1 and Q_2 and their conjugates. Our strategy is to start with the Hamiltonian (1.25) with 2n degrees of freedom. We'll split these up into two groups of n, related by supersymmetry as x_i ↔ ψ_{x,i} y_i ↔ ψ_{y,i} with i = 1,...,n. This supersymmetry is generated by the supercharge (1.26) which takes the form Q_1 = (p_{x,i} - i ∂_{x,i} h) ψ_{x,i} + (p_{y,i} - i ∂_{y,i} h) ψ_{y,i} Q†_1 = (p_{x,i} + i ∂_{x,i} h) ψ†_{x,i} + (p_{y,i} + i ∂_{y,i} h) ψ†_{y,i} The supercharge depends on a single real function h(x,y). The idea is to introduce a second supercharge that will relate the degrees of freedom in a different way, namely x_i ↔ ψ_{y,i} y_i ↔ ψ_{x,i} It takes some messing around to get the minus signs right, but it turns out that the following supercharge does the job Q_2 = (p_{x,i} + i ∂_{y,i} h) ψ_{y,i} - (p_{y,i} + i ∂_{x,i} h) ψ_{x,i} Q†_2 = (p_{x,i} - i ∂_{y,i} h) ψ†_{y,i} - (p_{y,i} - i ∂_{x,i} h) ψ†_{x,i} The two supercharges Q_1 and Q_2 obey the algebra (1.30) but only if the function h(x,y) has some special properties. For example, we can compute the Hamiltonian in two different ways, {Q_1, Q†_1} = Σ_{i=1}^n (p_{x,i}^2 + p_{y,i}^2 + |∂_{x,i} h|^2 + |∂_{y,i} h|^2)

- Σ_{i,j=1}^n ([ψ†_{x,i}, ψ_{x,j}] ∂^2 h/∂x_i ∂x_j + [ψ†_{y,i}, ψ_{y,j}] ∂^2 h/∂y_i ∂y_j + ([ψ†_{x,i}, ψ_{y,j}] + [ψ†_{y,j}, ψ_{x,i}]) ∂^2 h/∂x_i ∂y_j)

Alternatively, we have {Q_2, Q†_2} = Σ_{i=1}^n (p_{x,i}^2 + p_{y,i}^2 + |∂_{x,i} h|^2 + |∂_{y,i} h|^2)

+ Σ_{i,j=1}^n ([ψ†_{y,i}, ψ_{y,j}] ∂^2 h/∂x_i ∂x_j + [ψ†_{x,i}, ψ_{x,j}] ∂^2 h/∂y_i ∂y_j - ([ψ†_{y,i}, ψ_{x,j}] + [ψ†_{x,j}, ψ_{y,i}]) ∂^2 h/∂x_i ∂y_j)

The difference lies in the second line, where the ψ_x and ψ_y fermions are exchanged, together with some minus signs. At first glance, it looks like these are simply different Hamiltonians. However, all is not lost: these two Hamiltonians coincide if the function h(x,y) obeys ∂^2 h/∂x_i ∂x_j = ∂^2 h/∂y_i ∂y_j and ∂^2 h/∂x_i ∂y_j = -∂^2 h/∂y_i ∂x_j h = −∂x_i∂x_j + ∂y_i∂y_j，∂x_i∂y_j + ∂y_i∂x_j (1.31)

There’s a much nicer way of writing these conditions: as we will now see, they are telling us that h(x,y) is related to a holomorphic function.

We introduce the complex coordinates z_i = x_i + i y_i and z̄_i = x_i - i y_i. Notice the extra bar on the conjugate z̄_i = 1,...,n index; it’s a fairly common notation when dealing with complex coordinates. The corresponding derivative operators are ∂_i = 1/2 (∂_{x_i} - i ∂_{y_i}) and ∂̄_i = 1/2 (∂_{x_i} + i ∂_{y_i}), which obey ∂_i z_j = δ_{ij} and ∂̄_i z̄_j = δ̄_{ij} and ∂_i z̄_j = ∂̄_i z_j = 0.

Now consider a holomorphic function W(z) which depends only on the z_i and not on z̄_i. If we decompose this in terms of a real and imaginary piece W(z) = −h(x,y) − i g(x,y) (1.32) then the Cauchy-Riemann equations read ∂W/∂z̄_i = 0 ⇒ ∂h/∂x_i = ∂g/∂y_i and ∂h/∂y_i = −∂g/∂x_i. It is simple to show that these then imply the requirements (1.31).

This motivates us to frame the theory with N = 4 supersymmetry in terms of complex variables rather than real variables. In addition to the complex coordinates z_i, we also introduce complex momenta p_{x_i} = 1/2 (p_{x_i} - i p_{y_i}) and p̄_{x_i} = 1/2 (p_{x_i} + i p_{y_i}), as well as “complex” Grassmann variables. Here the word “complex” is in inverted commas because our original Grassmann variables were already complex; we just introduce different linear combinations: Ψ_i = ψ_{x_i} + i ψ_{y_i} and Ψ̄_i = ψ̄_{x_i} - i ψ̄_{y_i}, ˜Ψ_i = ψ̄_{x_i} + i ψ̄_{y_i} and ˜Ψ̄_i = ψ_{x_i} - i ψ_{y_i}. We’ve now abandoned the † notation for complex conjugation and resorted instead to the barred notation. (If nothing else, it is easier to write bars when doing long calculations.) Finally, we have combinations of supercharges: Q_{+i} = 1/2 (Q_{1i} + i Q_{2i}) = p_{x_i} ˜Ψ̄_i - i ∂̄_{x_i} W̄ ˜Ψ̄_i, Q̄_{+i} = 1/2 (Q̄_{1i} - i Q̄_{2i}) = p̄_{x_i} Ψ̄_i + ∂_{x_i} W ˜Ψ_i, Q_{-i} = 1/2 (Q_{1i} - i Q_{2i}) = p̄_{x_i} ˜Ψ̄_i - ∂_{x_i} W Ψ_i, Q̄_{-i} = 1/2 (Q̄_{1i} + i Q̄_{2i}) = p_{x_i} ˜Ψ_i + ∂̄_{x_i} W̄ Ψ̄_i. These obey the extended supersymmetry algebra (1.30), now with α,β = +,−.

The flurry of complexified definitions conspire to make the theory look somewhat simpler. In the Lagrangian picture, it takes the form L = ∑_{i=1}^n |ż_i|² + i ˜Ψ̄_i ∂_t ˜Ψ̄_i + i Ψ̄_i ∂_t Ψ_i − 1/2 |∂W|² − 1/2 ∑_{i,j} (∂_{x_i} ∂_{x_j} W Ψ_i ˜Ψ_j + ∂̄_{x_i} ∂̄_{x_j} W̄ ˜Ψ̄_i Ψ̄_j) (1.33). Supersymmetric Lagrangians of this kind, involving complex scalar fields and fermions, are usually referred to as Landau-Ginzburg theories. This is a nod to the Landau-Ginzburg theories that we met when discussing phase transitions in Statistical Physics. But it’s not a very good nod. In particular, the theory (1.25) with just a single supersymmetry is just as much related to the kinds of models that Landau and Ginzburg considered but is never given this name in the context of supersymmetry. It’s best to think of the name “Landau-Ginzburg” for the Lagrangian (1.33) as merely a quirk of history and forget that the term is also used elsewhere in physics.

The Landau-Ginzburg Lagrangian depends on a single holomorphic function W(z). This is known as the superpotential. The fact that extended supersymmetry comes hand in hand with holomorphy and associated ideas in complex analysis is extremely important. We will not discuss quantum mechanics with N = 4 supersymmetry in these lectures, but it’s not for want of interesting content. In particular, there is a beautiful relationship to a form of complex geometry known as “Kähler geometry” that underlies many of the most interesting results in this subject.

Furthermore, when we go to higher dimensional field theories, supersymmetry generators are associated to spinors and these necessarily have more than one component. This means that in, for example, d = 3+1 dimensions, the simplest supersymmetric theories have the form (1.33) and are based on complex, rather than real variables. In that context, the holomorphy of the superpotential goes a long way towards allowing us to solve some complicated features of supersymmetric quantum field theories. This is covered in some detail in the lectures on Supersymmetric Field Theory.

The Ground States

Finally, we can turn to some physics of the theory (1.33). As previously, we can ask how many ground states the theory has. The semi-classical ground states are associated to critical points of the superpotential, ∂W/∂z_i = 0 for all i = 1,...,n. We know from our discussion in Section 1.4.1 what we should do next: we compute the Morse index for each critical point, meaning the number of positive eigenvalues of the Hessian of h. But this is trivial for a holomorphic function W(z). For example, if there is a critical point near the origin, we can expand (after a suitable diagonalisation) W(z) ≈ ∑ λ_i (z_i)² + ... In terms of our real variables, (z_i)² = (x_i)² − (y_i)² + 2i x_i y_i, while our original function h(x,y) is given, from (1.32), as h(x,y) = −Re W = −∑ [λ_i (x_i)² − (y_i)²] + ... We learn that, because of the holomorphy of W, for every positive eigenvalue of the Hessian of h, there is a corresponding negative eigenvalue. This ensures that every critical point has Morse index (1.28) given by n and each contributes exactly the same to the Witten index (1.29) which becomes Tr(−1)^F e^{−βH} = (−1)^n × (Number of critical points of W). We learn that in theories with N = 4 supersymmetry, every critical point of W is a true E = 0 ground state of the quantum theory.

1.4.3 Less Supersymmetry and Spinors

It’s also possible to consider theories with less supersymmetry than our starting point. In fact, this is easy to achieve. We return to our theory with N = 2 supersymmetry and impose a reality condition on the Grassmann variables ψ̄_{x_i} = ψ_{x_i}. Real quantum mechanical Grassmann variables like this are called Majorana modes or Majorana fermions.

For our current purposes, it will suffice to discuss just the free theory, S = ∫ dt [∑_{i=1}^n ẋ_i ẋ_i + 1/2 ∑_{i=1}^n ψ_i ψ̇_i] (1.34). This is invariant under a single real supercharge, Q = ∑ ẋ_i ψ_i, which obeys Q† = Q and generates the supersymmetry transformation δx_i = ϵ ψ_i and δψ_i = −ϵ ẋ_i. This is usually referred to as N = 1 supersymmetry. (You will sometimes see the terminology N = 1 supersymmetry in the literature, counting complex supercharges rather than real.)

Here our interest lies in a very specific property of these theories: how should we think of the internal degrees of freedom generated by the real fermions ψ_i? There is a very pretty answer to this question. To see this, first note that the momentum conjugate to the fermion is ∂L/∂ψ̇_i = i ψ_i. The canonical commutation relation for the fermion is then {ψ_i, ψ_j} = 2δ_{ij} for i,j = 1,...,n. But this is a very familiar equation: it is the Clifford algebra, usually written in terms of gamma matrices {γ_i, γ_j} = 2δ_{ij} for i,j = 1,...,n. This means that the fermions in this theory should be viewed as gamma matrices! The Clifford algebra has a unique irreducible representation of dimension 2^{n/2} if n is even and 2^{(n-1)/2} if n is odd. This strongly suggests that the internal degrees of freedom of the particle described by the action (1.34) have something to do with spinors on ℝ^n.

It is straightforward to construct these internal degrees of freedom. First, let’s assume that n is even. (We will discuss the case of n odd below.) We pair up the Majorana modes into complex fermions c_i = 1/√2 (ψ_{2i} + i ψ_{2i-1}) for i = 1,...,n/2. Then the complex c_i operators form the usual algebra of fermionic creation and annihilation operators that we’re used to: {c_i†, c_j} = δ_{ij} and {c_i†, c_j†} = {c_i, c_j} = 0, and we can use them to build the familiar fermionic Fock space starting with |0⟩ that obeys c_i|0⟩ = 0 and then acting with c_i†. Following the discussion in Section 1.4.1, we see that the fermions fill out an internal space with Dimension of Internal Space = 2^{n/2}. This is precisely the dimension of a Dirac spinor on ℝ^n.

There is more to say about these spinors. Under a rotation in ℝ^n, the Dirac spinor transforms in the representation generated by Σ_{ij} = 1/2 [γ_i, γ_j]. (See the lectures on Quantum Field Theory for more details of this.) However, in even dimension, as we have here, this is not an irreducible representation. It is composed of two smaller representations known as chiral spinors or Weyl spinors. These arise because we can always construct an operator γ̂ that is analogous to γ₅ in four dimensions. In general, this is given by multiplying all the gamma matrices together, with a suitable factor of i to ensure Hermiticity, γ̂ = i^{n/2} γ₁ ... γ_n. This obeys γ̂² = 1 and {γ̂, γ_i} = 0. The existence of the γ̂ operator means that all the internal states can be decomposed into two different camps: those with eigenvalue γ̂ = +1 and those with eigenvalue γ̂ = −1. In the language of the Dirac equation, these are spinors of different chirality.

In the context of our supersymmetric quantum mechanics, this γ̂ operator has a very natural meaning. The eigenvalues are simply states with an even or odd number of c_i† operators excited. In other words, this plays the role of our fermion number. γ̂ = (−1)^F. This means that γ̂ determines whether states live in H_B or H_F.

The punchline of this argument is that quantising real fermions, appropriate for N = 1 supersymmetry, gives Dirac spinors on ℝ^n, at least for n even. These have dimension 2^{n/2}. Meanwhile, while quantising complex fermions, appropriate for N = 2 supersymmetry, gives forms on ℝ^n. These have dimension 2^n. We’ll have use for quantum mechanics with N = 1 supersymmetry in Section 3.3 where we discuss the Atiyah-Singer index theorem.

As an aside, clearly the construction of spinors and forms on ℝ^n from Grassmann degrees of freedom is closely related. This also suggests that you can take 2^{n/2} different Dirac spinors and bundle them together to look like forms. Such a construction is called Kähler-Dirac fermions. It won’t play a role in these lectures, but arises in a number of other areas of physics including topological twisting of field theories and quantum gravity.

d lattice gauge theory where it goes by the name of staggered fermions.

The Case of n Odd: A Subtle Anomaly We still have to understand the case of n odd. Here there is a surprise. Quantum mechanical theories with an odd number of Majorana modes don’t make any sense! They are an example of what is sometimes called an anomalous quantum theory: a seemingly sensible classical theory that cannot be quantised.

The argument is straightforward. Consider two, non-interacting Majorana fermions, ψ1 and ψ2. From the discussion above, we can construct a single complex fermion c = (ψ1 + iψ2)/ 2 and this acts on a two-dimensional Hilbert space spanned by |0⟩ and c†|0⟩.

But, by the factorisation of Hilbert spaces, that means that a single Majorana fermion, say ψ1, must act on a Hilbert space of dimension 2. And that’s nonsense! You can reach the same conclusion if you use the path integral to compute Tre−βH, which just counts the dimension of the Hilbert space when H = 0, Again, after suitable regularisation, you find 2.

For us, this means that theories with N = 1 supersymmetry are restricted to describe a particle moving in an even dimensional space, like Rn with n even.

2 Supersymmetry and the Path Integral In addition to making the symmetry aspect of supersymmetry manifest, the Lagrangian description of the quantum mechanics has one additional advantage: it allows us to bring the path integral to bear on the problem.

We’ll make plenty of use of the path integral in later studies of supersymmetric systems. The purpose of this section is to understand some of the basic properties of the quantum mechanical path integral and how we can use it to compute quantities of interest in supersymmetric theories.

## 2.1 The Partition Function and the Index

Let’s start with a purely bosonic system, with the familiar action S = ∫ dt (ẋ2 − V(x)) (2.1)

In statistical mechanics, we typically want to compute the partition function Z = Tre−βH How do we compute this using path integrals?

Our starting point is Feynman’s expression for the propagator. Take a particle that sits at point xi at time ti. The quantum amplitude for it to be at point xf at a later time tf has the beautiful path integral expression ⟨xf |e−iH(tf −ti)|xi ⟩ = ∫ Dx(t) eiS[x(t)] (2.2)

where the path integral is over all paths x(t) such that x(ti) = xi and x(tf) = xf.

Our goal now is to manipulate (2.2) so that the left-hand-side looks like the partition function Z. There are a number of differences that we need to fix. First, the time evolution operator in quantum mechanics is unitary, e−iHt. Meanwhile, in statistical mechanics the relevant operator is e−βH, with a minus sign in the exponent rather than a factor of i. To deal with this, we work in imaginary time, τ = it So e−iHt = e−Hτ. On the right-hand-side, we write the action in Euclidean time so it becomes S = ∫ dτ ( (dx/dτ)2 + V(x) ) = iSE Here SE is the Euclidean action. In quantum field theory, this operation is tantamount to Wick rotation. The Feynman expression (2.2) then becomes ⟨xf |e−H(τf −τi)|xi ⟩ = ∫ Dx(τ) e−SE[x(τ)] (2.3)

where the integral is over paths with x(τi) = xi and x(τf) = xf.

That’s fixed up the minus signs and factors of i. Next up is the trace in the partition function. This means that we sum over a basis of states. If we choose that basis to be position eigenstates, then we have Z = Tre−βH = ∫ dx ⟨x|e−βH|x⟩ Comparing this to (2.3), we have Z = ∫ dx ⟨x|e−βH|x⟩ = ∫ dx ∫ Dx(τ) e−SE[x(τ)]

where the path integral is over paths with x(τi) = x and x(τf) = x, and τf − τi = β. The important point is that we now integrate over paths where the particle comes back to where it started: x(τf) = x(τi). Furthermore, we integrate over all possible starting points x. This gives our final expression for the partition function which we write as Z = Tre−βH = ∫ Dx(τ) e−SE[x(τ)]

where now the boundary conditions just tell us that we should integrate over all possible closed paths. Equivalently, we can implement this condition by insisting that we work in periodic Euclidean time, so that τ is a coordinate on a circle S1, with τ ≡ τ + β Although we’ve derived this punchline in the context of quantum mechanics, it also works in quantum field theory. If you want to compute the thermal partition function of any quantum field theory, you simply need to work in periodic, Euclidean time. This will tell you information about the equilibrium properties of the system at temperature T = 1/β.

2.1.1 An Example: The Harmonic Oscillator To get a sense for how these calculations work, let’s look at everyone’s favourite example: the harmonic oscillator. This, of course, takes the form (2.1) with the potential V(x) = ω2x2 We know that the harmonic oscillator has energy levels E = ω(n+ 1/2) with n = 0,1,... (assuming that ω > 0). This means that, in this case, we can just compute the partition function by summing over all states.

Z = Σ_{n=0}^∞ e−βω(n+1/2) = e−βω/2 / (1−e−βω) (2.4)

How does the path integral reproduce this? We have Z = ∫ Dx(τ) exp( −∫ dτ (1/2)(dx/dτ)2 + (1/2)ω2 x2 )

where we’ve left the periodic boundary conditions implicit and integrated by parts in the Euclidean action to highlight the fact that the resulting path integral takes a Gaussian form. If we extrapolate from finite-dimensional Gaussian integrals, we find ourselves with the slightly formal expression Z = [ det( −d2/dτ2 + ω2 ) ]^{-1/2} We should think of this determinant as the product of eigenvalues of the differential operator. The eigenfunctions of this operator are x(τ) = e^{ikτ} ⇒ ( −d2/dτ2 + ω2 ) x(τ) = (k2 + ω2)x(τ)

but we should remember that we’re working on a circle with periodic boundary conditions so we require x(τ +β) = x(τ). This restricts the k values to be quantised k = 2πn/β, n ∈ Z This, of course, is just the usual calculations that we do in our first course on Quantum Mechanics. The novelty here is that we now need to multiply all these eigenvalues together Z = [ Π_{n=−∞}^{+∞} ( (2πn/β)^2 + ω^2 ) ]^{-1/2} = (1/β) [ Π_{n=1}^{∞} ( (2πn/β)^2 + ω^2 ) ]^{-1} In the second equality we’ve taken out the n = 0 term, and then used the fact that ±n give the same contribution to remove the square-root factor at the expense of restricting the product to positive integers. We can rewrite the resulting expression as a product of two terms, each itself an infinite product Z = (1/(βω)) Π_{n'=1}^{∞} (1 + (βω/(2πn))^2 )^{-1} (2.5)

The second of these expressions is convergent and the result is well known: Π_{n=1}^{∞} (1 + (βω/(2πn))^2 ) = sinh(βω/2) / (βω/2) (2.6)

We won’t prove this result here, but just note that it follows immediately from Euler’s product formula for sine, sin(πz) = πz Π_{n=1}^{∞} (1 − z^2/n^2)

As an obvious sanity check, it’s clear that both sides of this equation have the same zeros. A full proof of the equivalence is not too hard, but a little involved.

That leaves us with the first infinite product in (2.5) to deal with. And that’s more tricky because it diverges. To better understand such terms, we should really go back and dissect the path integral to figure out where it came from. (For example, the partition function should be dimensionless but this term has dimension of [Energy]^{2∞} which is a hint that we didn’t define our measure very well.) However, in the spirit of this course we’re going to treat this term as blithely as possible. And, for those physicists of a blithe disposition, there are few tools more useful than zeta function regularisation.

The zeta function is defined, for Re(s) > 1, by the sum ζ(s) = Σ_{n=1}^{∞} n^{-s} However, ζ(s) is defined for all values of s. The idea is that we use this to give meaning to divergent sums. For example, we could think of the sum of all positive integers as ζ(−1) = −1/12. Although these zeta function games seem rather inane when you first meet them, the magic is that they tend to give the right answers when used to regulate divergences in quantum field theory. (For example, in the lectures on String Theory we first invoked the unconvincing ζ(−1) = −1/12 argument to compute the critical dimension of the string, and then spent a significant amount of time rederiving this using conformal field theory techniques where the divergences were absent.)

Let’s see how we can put the zeta function to work for the harmonic oscillator. We first introduce the related function ζ1(s) = Σ_{n=1}^{∞} (2πn/β)^{-2s} = (2π/β)^{-2s} ζ(2s)

Now we take the derivative with respect to s. Note that, if y = ax then dy/dx = yloga. So ζ1'(s) = 2 log(2π/β) ζ(2s) + ζ'(2s)

= 2 Σ_{n=1}^{∞} log(2πn/β) (2πn/β)^{-2s} Evaluated at s = 0, we have ζ1'(0) = 2 log(2π/β) ζ(0) + ζ'(0) = Σ_{n=1}^{∞} 2 log(2πn/β) (2πn/β)^{0} Or, taking the exponential of both sides, Π_{n=1}^{∞} (2πn/β)^{-2} = e^{2ζ1'(0)} = (2π/β)^{2ζ(0)} Now we need the values ζ(0) = −1/2 and ζ'(0) = −1/2 log(2π). Combining these gives the zeta-tamed value for the divergent product Π_{n=1}^{∞} (2πn/β)^{-2} = (2π/β)^{-1} = β/(2π) = 1/β (2.7)

We can see immediately that, despite the dubious route to get there, the end result is plausible. This is because the 1/β factor from the regularised product combines with the 1/ω factor that sits in front of (2.5) to ensure that the partition function is dimensionless, as it should be.

Putting this together with our convergent product (2.6), we get our end result for the path integral Z = 1/(2 sinh(βω/2)) (2.8)

But this is what we want: it agrees with the harmonic oscillator partition function (2.4) computed through more traditional means.

First, a trivial observation before we move on. The harmonic oscillator potential depends, of course, on ω2. In the derivation above, we assumed that ω > 0. In what follows, a better answer for the partition function is Z = 1/(2sinh(β|ω|/2))

This trivial amendment will be important to remember later when we discuss the supersymmetric oscillator.

2.1.2 Fermions: Periodic or Anti-Periodic?

When dealing with supersymmetric systems, our theory necessarily contains fermionic, or Grassmann, variables. And these bring a new subtlety to the problem. In quantum field theories in higher dimensions, fermions famously come with a minus sign issue: rotate a fermionic field by 2π and it doesn’t come back to itself, but picks up a minus sign. This same minus sign manifests itself when computing the thermal partition function. As we saw in Section 2.1, if we want to compute Z = Tre−βH then we should work in Euclidean time with period β. The bosonic fields x(t) are given periodic boundary conditions x(τ +β) = x(τ)

But for the fermionic fields, that minus sign suggests two possibilities: we could have periodic or anti-periodic boundary conditions ψ(τ +β) = ψ(τ) or ψ(τ +β) = −ψ(τ)

Relatedly, there are two natural partition functions that we could construct for fermions. In addition to the thermal partition function Tre−βH, we could also consider the quantity Tr(−1)Fe−βH. In supersymmetric quantum mechanics, Tr(−1)Fe−βH is the Witten index and is necessarily an integer. But, for a general fermionic system it is just a different way to sum the states, weighted by an extra minus sign. I’ll refer to the quantity Tr(−1)Fe−βH as an “index” in both supersymmetric and non-supersymmetric theories, although strictly this terminology should be reserved for the former case. It seems plausible that inserting a factor of (−1)F in the trace would flip the sign of the fermion as we go around the Euclidean temporal circle. But which boundary condition corresponds to the thermal partition function, and which to the index?

As always, the right answer can be found by going back to first principles and looking at how one constructs the path integral from small, but finite, time steps. Here, however, we will simply give the answer and then provide some motivation. The answer is that the thermal partition function requires anti-periodic boundary conditions for fermions, Anti-Periodic: Z = Tre−βH = Dψ†Dψ e−SE[ψ,ψ†]

ψ(β)=−ψ(0)

Meanwhile, the index is computed with periodic boundary conditions: Periodic: Tr(−1)Fe−βH = Dψ†Dψ e−SE[ψ,ψ†]

ψ(β)=ψ(0)

To motivate this result, we will calculate the path integral in a particularly simple case.

The Fermionic Oscillator The simple model that we’ll use as a testing ground is a free fermion with action S = ∫ dt iψ†ψ˙ − ωψ†ψ This is nothing complicated: it is the Lagrangian description for a two state system. As we’ve seen previously, the canonical commutation relations are {ψ,ψ} = {ψ†,ψ†} = 0 and {ψ,ψ†} = 1 and these naturally act on a two-dimensional Hilbert space spanned by |0⟩ and |1⟩ such that ψ|0⟩ = 0 and |1⟩ = ψ†|0⟩ The Hamiltonian of this system is H = ω[ψ†,ψ] ⇒ H|0⟩ = −ω/2 |0⟩ and H|1⟩ = +ω/2 |1⟩ Note that we’ve chosen the symmetric operator ordering for the Hamiltonian, so that the energies are E = ±ω/2. In the absence of supersymmetry, there is nothing that enforces this upon us and other orderings will give energies shifted by E + constant. However, we will see below that the naive implementation of the path integral also gives this symmetric choice of energies.

For the two state system, the computation of the thermal partition function using the Hamiltonian approach is a trivial calculation: we get Z = Tre−βH = e−βω/2 + e+βω/2 (2.10)

We define the fermion number F = ψ†ψ, so F|0⟩ = 0 and F|1⟩ = 1. Then the index differs from the partition function just by a minus sign Tr(−1)Fe−βH = −e−βω/2 + e+βω/2 (2.11)

Clearly the index isn’t independent of β for this simple model: that is only true for supersymmetric systems. Our challenge is to reproduce these two results from the path integral and use this to confirm which boundary condition gives which quantity. For both choices of boundary condition, the starting point is the same: the Euclidean action is S_E[ψ†,ψ] = ∫ dτ ψ† (d/dτ + ω)ψ The fermionic path integral is Gaussian. By dint of the complex Grassmann nature of the integration variables, we get det rather than det−1/2, so that ∫ Dψ†Dψ e−S_E[ψ†,ψ] = det(d/dτ + ω)

We again think of the determinant as the product of eigenvalues. The eigenfunctions have the same form as before ψ(τ) = η e^{ikτ} ⇒ (d/dτ + ω) ψ = (ik + ω)ψ for some constant Grassmann parameter η. The difference between periodic and anti-periodic boundary conditions comes in the allowed values of k. We have Periodic : ψ(τ +β) = ψ(τ) ⇒ k = 2πn / β Anti-Periodic : ψ(τ +β) = −ψ(τ) ⇒ k = 2π(n−1/2) / β with n ∈ Z. We see that the modes are, up to a normalisation, either integer or half-integer valued depending on the choice of boundary conditions.

Let’s start with the periodic case. We have Periodic: det(d/dτ + ω) = ∏_{n∈Z} (i * 2πn / β + ω)

= ∏_{n=1}^∞ (ω^2 + (2πn / β)^2)

= ∏_{n'=1}^∞ (1 + (βω / 2πn)^2) * ∏_{n=1}^∞ (βω / 2πn)^2 = 2sinh(βω / 2)

where, in the last line, we’ve used our previous expressions for the convergent product (2.6) and the divergent product, tamed by zeta function regularisation (2.7). As promised, this coincides with the index Tr(−1)Fe−βH that we computed in (2.11). (Actually it differs by a minus sign, but this is simply the convention for F.)

Meanwhile, with anti-periodic boundary conditions, we have Anti-Periodic: det(d/dτ + ω) = ∏_{n∈Z} (i * 2π(n−1/2) / β + ω)

The modes k come in ± pairs with n pairing with −n + 1. (So, for example, n = 1 pairs up with n = 0 since both have k = ±π/β). We use this to rewrite the product as det(d/dτ + ω) = ∏_{n=1}^∞ (ω^2 + (2π(n−1/2) / β)^2)

= ∏_{n'=1}^∞ (1 + (βω / 2π(n−1/2))^2) * ∏_{n=1}^∞ (βω / 2π(n−1/2))^2 Again, the determinant factorises into two inner products. Again, the second of these is convergent and has a well known form (that, once more, we won’t prove), ∏_{n=1}^∞ (1 + (βω / 2π(n−1/2))^2) = cosh(βω / 2)

We’re left, however, with the first infinite product and this is clearly divergent. As before, we turn to zeta function regularisation for refuge. The same argument that we used for the bosonic oscillator can be invoked here too, now applied to the so-called Hurwitz zeta function ζ(s,1/2) = ∑_{n=0}^∞ 1/(n+1/2)^s The upshot is that, with anti-periodic boundary conditions, the path integral gives det(d/dτ + ω) |_{anti−periodic} = 2cosh(βω / 2)

This reproduces the thermal partition function (2.10). It will not have escaped your attention that the path integral calculation was a lot of work to get the partition function for a two state system. However, as we come to consider more complicated quantum mechanical models, including higher dimensional field theories, the path integral starts to come into its own and, ultimately, is much more convenient than canonical quantisation.

2.1.3 The Witten Index Revisited It’s useful to understand why, from the path integral perspective, the Witten index is always an integer for supersymmetric theories. After all, something magical must happen where we do an infinite dimensional integral but, regardless of the parameters in the integrand, we always get an integer. How does this come about? The answer is a rather special property of supersymmetric path integrals known as localisation. To see how this works, we’ll revert to the simplest system of a particle with spin on a line. In Euclidean time, the action (1.14) becomes S[x,ψ,ψ†] = ∫ dτ [ (1/2) (dx/dτ)^2 + ψ† (dψ/dτ + h') − (h''/2) ψ†ψ ] (2.13)

where the ∮ is there to remind us that we’re working in periodic time. The Euclidean action is invariant under the Wick rotated supersymmetry transformations (1.19), which read δx = ϵ†ψ − ϵψ† , δψ = ϵ (dx/dτ + h') , δψ† = ϵ† (−dx/dτ + h') (2.14)

The bosonic field x(τ) is always periodic: x(τ) = x(τ +β). But that means that the supersymmetry transformations (2.14) only hold if ψ is also periodic: ψ(τ) = ψ(τ+β). As we’ve seen, if we wish to compute the thermal partition function Z = Tre−βH using the path integral then we must give the fermions anti-periodic boundary conditions. But, in doing so, we break supersymmetry. In contrast, if we wish to compute the Witten index Tr(−1)Fe−βH then the path integral enjoys supersymmetry. This makes intuitive sense. In general, the full partition function Z is no easier to compute for a supersymmetric theory than a non-supersymmetric theory. But the Witten index is much easier. And, from the path integral perspective, this manifests itself because of the transformations (2.14).

To proceed, let’s first show that the Witten index I = Tr(−1)Fe−βH = ∮ DxDψ†Dψ e−SE[x,ψ,ψ†]

doesn’t care about the magnitude of the potential. To this end, we rescale h → λh with λ > 0. We then differentiate with respect to λ to find dI/dλ = ∮ DxDψDψ† [− ∫ dτ (λh'^2 − h'' ψ†ψ)] e−SE The extra term in the integrand has a special form because it is itself a supersymmetry variation. To see this, it’s useful to use the supersymmetry generators that we introduced in (1.21). With a rescaled potential λh and Euclidean time, these become Q = ∫ dt ψ(t) [δ/δx(t) − (−λh')] d/dτ (δ/δψ†(t))

Q† = ∫ dt −ψ†(t) [δ/δx(t) + (λh')] d/dτ (δ/δψ(t))

h′ (2.15)

λ δx(t) dτ δψ(t)

Then look at ∫ dτ h′ψ = ∫ dτ ( −h′′ψ†ψ + h′ + λh′² )

λ = ∫ dτ ( −h′′ψ†ψ + dh/dτ + λh′² )

= ∫ dτ ( −h′′ψ†ψ + λh′² )

where, in the final term, we lost the total derivative. (Note that there’s no danger of a boundary term here because τ parameterises a circle and all fields are periodic.) This means that we can write the derivative of the Witten index as dI/dλ = ∫ DxDψDψ† ( −Q† ∫ dτ h′ψ ) e^{−S_E} But we also know that the action is invariant under supersymmetry and, as we showed in (1.22), this can be written as Q†S_E/λ = 0. This means that our final expression is a path integral of a total supersymmetry variation, dI/dλ = ∫ DxDψDψ† Q† ( − e^{−S_E} ∫ dτ h′ψ )

The integrand is said to be Q-exact. The all-important point is that the integral of any Q-exact quantity always vanishes.

To see this, note from (2.15) that there are two terms in Q† (or Q): one in which we differentiate with respect to x(t), and one in which we differentiate with respect to ψ(t). Let’s start with the second of these.

To set the scene, we’ll briefly return to normal Grassmann integration (as opposed to functional integration). Recall that the integral over any Grassmann variable θ only gives a non-zero answer if there’s a single copy of θ in the integrand, ∫ dθ 1 = 0 and ∫ dθ θ = 1 There can’t be more powers of θ in the integrand because these are Grassmann variables and θ² = 0. This means that Grassmann integration always obeys ∫ dθ (Anything) = 0 (2.16)

dθ That’s because the d/dθ kills any power of θ that may have been lurking in the expression “Anything”, ensuring that there’s nothing left to saturate the dθ integral. The formula (2.16) looks very much like an “integration by parts” formula for Grassmann variables, but with no danger of a boundary term.

The story above also holds for the functional integration over fermionic fields. We have ∫ DψDψ† (δ/δψ(t)) (Anything) = ∫ DψDψ† (δ/δψ†(t)) (Anything) = 0 That deals with the fermionic functional derivatives in Q and Q†.

We’re left with the bosonic functional derivatives δ/δx(t). Here we have a total derivative, albeit of a functional kind and we would expect such an integral to be given by the boundary term. The question is: what should we consider to be the boundary of this functional space? Large x(t)? Wildly varying x(t)? Either way, the boundary term vanishes. This is because there is an exponential suppression from the action e^{−S_E} that asymptotes quickly to zero for anything that you might reasonably consider to be the boundary. The upshot of these arguments is that ∫ DxDψDψ† Q†(Anything) = ∫ DxDψDψ† Q(Anything Else) = 0 This, in turn, ensures that dI/dλ = 0 which, of course, we know to be true from our Hamiltonian analysis.

Now we’re in business. Because the Witten index is independent of λ, we can calculate it in the limit λ → ∞. Here the potential term in the action suppresses all contribution except for the a finite number of constant maps, x(τ) = X such that h′(X) = 0 There are the critical points of h. The phenomenon of an integral – in this case an infinite dimensional functional integral – receiving contributions from just a handful of points is known as localisation. It is a property of supersymmetric path integrals that is not shared by most other quantum systems.

We still need to compute the partition function around each of these critical points. As we increase λ, the potential around each critical point gets steeper and steeper and the physics can be better and better approximated by a harmonic oscillator, with h′(x) ≈ h′′(X)(x−X)+... ⇒ V(x) ≈ (h′′(X))²(x−X)² +...

Indeed, taking the λ → ∞ limit should be viewed as suppressing the non-linear interactions in the potential. The statement that the Witten index is independent of λ is equivalently to saying that the one-loop approximation is, in fact, exact.

All of this means that the path integral expression for the Witten index is Tr(−1)^F e^{−βH} = ∫ DxDψDψ† e^{−S_E} = ∑ det(d/dτ − h′′(X)) / det^{1/2}(−d²/dτ² + h′′(X)²)

where the sum is over the critical points. Happily, we’ve already put some effort into computing the determinants of these operators. The bosonic contribution is (2.9)

det^{1/2}(−d²/dτ² + ω²) = 2 sinh(β|ω|/2)

Meanwhile, the fermionic contribution is (2.12)

det(−d/dτ − ω) = −2 sinh(βω/2)

The end result is Tr(−1)^F e^{−βH} = ∑ −h′′(X)/|h′′(X)| = ∑ sign(−h′′(X))

X This is the answer we expected. If h(x) is a polynomial of odd degree, then it has an even number of critical points X, with h′′(X) alternating in sign, giving Tr(−1)^F e^{−βH} = 0. Meanwhile, if h(x) is a polynomial of even degree then the alternating signs don’t cancel out, leaving Tr(−1)^F e^{−βH} = ±1.

## 2.2 Instantons

Much of our story so far has revolved around understanding the structure of ground states in supersymmetric systems. A common theme – one familiar from other quantum mechanical models – is that the existence of multiple classical ground states does not necessarily mean that there are multiple quantum ground states.

In this section, we develop a more hands-on understanding of how ground states are lifted. Once again, our tool of choice will be the path integral and, as we will see, this provides a particularly direct way to think about quantum tunnelling and related phenomena. We will explore how this works in some detail, first in ordinary quantum mechanical systems and then in those that exhibit supersymmetry.

The path integral in Euclidean time is (2.3), ⟨x_f | e^{−HT} | x_i ⟩ = ∫_{x(−T/2)=x_i}^{x(T/2)=x_f} Dx(τ) e^{−S_E[x(τ)]} (2.17)

To start, we’ll focus only on the bosonic degrees of freedom and then introduce fermions into the discussion later. We’ll also restrict attention to just a single degree of freedom x(τ), with Euclidean action S_E = ∫ dτ [ (1/2)(dx/dτ)² + (1/2)(dh/dx)² ] (2.18)

Although the specific form of the potential V = ½h′² arises naturally in any supersymmetric theory, it is possible to write any positive definite potential in this way. Moreover, as we now show, this turns out to be a useful thing to do even in a non-supersymmetric theory.

Tunnelling is particularly easy to understand from the path integral perspective. It arises from paths that start at one minima and end up at another. If the parameters in the potential are such that we can do a semi-classical analysis, then the amplitude for tunnelling is dominated by the classical paths that minimise S_E. There is a rather cute way of finding these paths. We write the action (2.18) by completing the square S_E = ∫ dτ [ (1/2)(dx/dτ ∓ dh/dx)² ± (d/dτ)(x dh/dx) ]

The first term is positive definite, the second a total derivative. This means that we have S_E ≥ ± ∫ dτ dh/dτ = ±(h(x_f) − h(x_i)) (2.19)

If we fix the endpoints x_i and x_f to be two distinct minima, then the action is minimised when this inequality is saturated with the most stringent ± sign. This means that if h(x_f) > h(x_i), we should solve the equation dx/dτ = dh/dx (2.20)

Solutions to this equation are known as instantons. The name is chosen (by ’t Hooft) to mimic the names give to particles but, as will see, these solutions are not localised in space but in (Euclidean) time and so occur just for an instant. If h(x_f) < h(x_i), we should solve the other equation dx/dτ = − dh/dx (2.21)

Solutions to this equations are called anti-instantons. They interpolate between the two vacua in the opposite direction to instantons.

It will be useful to look at an example. Suppose that we take h = (ω/(2a)) ( (1/3)x³ − a²x ) ⇒ V = (ω²/(8a²)) (x² − a²)² (2.22)

This is a double well potential with minima at x = ±a. The coefficient out front is chosen so that, around each minima, the potential is approximated by a harmonic oscillator with frequency ω, V(x) ≈ ½ ω²(x±a)² +... (2.23)

We have h(−a) = ωa²/3 > h(a) = −ωa²/3. The instanton therefore interpolates from x = +a at τ → −∞ to x = −a to τ → +∞. In this case, the solution to (2.20) is x_inst(τ) = −a tanh( ω(τ − τ₀)/2 ) (2.24)

The profile of the instanton is shown in Figure 5. As τ → ∞, we see that x(τ) ≈ ∓a e^{∓ωτ} → ∓a and the instanton asymptotes exponentially quickly back to the vacuum. The profile deviates significantly from the vacuum only in region of width ∼ 1/ω. The exact position τ = τ₀ where this happens is an arbitrary integration constant.

For this example, the action of the instanton is S_inst = 2ωa²/3 For more general h(x) the exact solution of the instanton may be harder to come by but its simple to get an intuitive feel for its properties. Viewed from the usual perspective of Lagrangian dynamics, the Euclidean action (2.18) describes a particle moving in a potential −V(x). This is shown on the right-hand side of Figure 6 for the double well potential. The instanton (or anti-instanton) describes a particle that starts at one maximum of −V(x) at τ → −∞ and then rolls down and up to another maximum, reaching the peak only at τ → +∞.

If V(x) has multiple minima, then we can only find solutions to the instanton equations (2.20) and (2.21) that interpolate between neighbouring minima. This is because these are first order equations of motion, and once you sit at a critical point of h you have necessarily stopped. That doesn’t mean that there is no tunnelling between multiple vacua: indeed, as we’ll see shortly, in non-supersymmetric quantum mechanics it is usually approximate solutions to the classical equations of motion that dominate proceedings.

Quantum mechanical physics of the double well potential shown in the left-hand side of Figure 6.

Let’s first remind ourselves what we qualitatively expect from the ground states. Around each minima, the potential looks like a harmonic oscillator (2.23) and we can then construct approximations to the ground states as Gaussian wavefunctions, localised around each of the minima:

ψ_left(x) = exp(−(x+a)^2 ω/2) and ψ_right(x) = exp(−(x−a)^2 ω/2)

For any even potential V(x) = V(−x), the energy eigenstates are also eigenstates of the parity operator, meaning that they are either even or odd functions. A better approximation to the low-lying energy eigenstates must therefore be:

ψ_±(x) ≈ ψ_left(x) ± ψ_right(x)

But the true ground state of any quantum system has no node, meaning that ψ(x) ≠ 0 for any finite x. (Given a wavefunction ψ(x) with a node, we can consider |ψ(x)| and then smooth out the cusp to lower the expected energy.) So it must be that ψ_+(x) is an approximation to the ground state, while ψ_−(x) is an approximation to the first excited state.

We’ll now add some quantitative meat to these statements using the path integral which provides a particularly straightforward way to compute the ground state energies of the double well potential. To see this, we pick position eigenstates |x_i⟩ and |x_f⟩. These need not themselves be ground states of the system, but should have a non-zero overlap with the ground states. As we’ve seen, the path integral (2.17) naturally computes ⟨x_f|e^(−HT)|x_i⟩. If we insert a complete set of energy eigenstates |n⟩, with energy E_n, then we have:

⟨x_f|e^(−HT)|x_i⟩ = Σ_n e^(−E_n T) ⟨x_f|n⟩⟨n|x_i⟩

If we wait long enough, this sum is dominated by the ground state E_0 < E_n for all n ≠ 0. We then have, for large T:

⟨x_f|e^(−HT)|x_i⟩ ∼ e^(−E_0 T)

So to determine the ground state energy, we just need to compute the path integral and extract the large T behaviour. We can then find the ground state energy in the exponent.

We will now use the semi-classical, or WKB, approximation to compute the amplitude for a particle to tunnel from one vacuum to the other and, in doing so, extract the ground state energy. We start by using the path integral to compute the amplitude for the particle to tunnel from one classical vacuum to another due to a single instanton. We write:

x(τ) = x_inst(τ) + δx

where x_inst(τ) is the solution to the relevant instanton equation (either (2.20) or (2.21)). We then expand the Euclidean action as:

S_E[x] = S_inst + ∫ dτ (1/2) ( (d^2/dτ^2) + V'' ) δx + O(δx^3) (2.25)

Here V'' is evaluated on x_inst. Similarly, S_inst is the action of the instanton which, from (2.19), is:

S_inst = |h(x_f) − h(x_i)| (2.26)

Alternatively, written in terms of the potential V = (1/2) h'^2, the action of the instanton is S_inst = ∫ dx √(2V). It should be thought of as a measure of the difficulty in getting up and over (or, more precisely, through) the barrier between the two minima.

The semi-classical approximation is valid whenever we can ignore the O(δx^3) contributions relative to the δx^2 contributions in the path integral. To understand the circumstances under which this holds, we should look more closely at the action and identify a dimensionless coupling constant g which multiplies all higher order terms. Perturbation theory is then valid when g ≪ 1. A simpler way to view things is to rescale the potential h(x) → λh(x). Then the semi-classical approximation is valid in the limit λ ≫ 1 where we have a steep potential, with deep minima. Under this rescaling, the action of the instanton (2.26) becomes:

S_inst → λ|h(x_f) − h(x_i)|

and so we see that λ ≫ 1 is equivalent to:

S_inst ≫ 1

This is the requirement that we will use for the semi-classical approximation to be valid. The results that we will get below will receive corrections of order 1/S_inst.

In the language of quantum field theory, neglecting the higher order δx^3 terms is tantamount to computing one-loop diagrams but not two-loop or higher. In normal circumstances, we would be doing perturbation theory around the classical vacuum x(τ) = ±a, in which case we would have V'' = ω^2, a constant. The difference here is that we’re now doing perturbation theory around the background of the instanton profile.

The kind of instanton calculations that we’re performing here are often referred to as non-perturbative. This refers to the fact that tunnelling phenomena of this kind can’t be captured by perturbation theory around any single vacuum. However, the phrase “non-perturbative” is also a little misleading: we’re still doing perturbation theory, just around a non-trivial solution.

Inserting (2.25) into the path integral (2.17), and dropping the terms that are cubic or higher, we are left with a Gaussian integral:

⟨−a|e^(−HT)|+a⟩|_(one-inst) = e^(−S_inst) ∫ Dδx exp(−∫ dτ (1/2) ( (d^2/dτ^2) + V'' ) δx + ...)

On the left-hand side, we’ve taken the tunnelling to happen over a time T; ultimately we will be interested in taking T → ∞. We have also stressed that we’re computing the contribution to the tunnelling from a single instanton and we’ll subsequently see that this is just part of the story.

Now we’re in a familiar situation. The Gaussian integral gives, as usual, a factor of:

det^(−1/2) ( −(d^2/dτ^2) + V'' ) (2.27)

As we stressed above, this differs from the usual determinant that we compute in perturbation theory only because V'' = V''(x_inst(τ)) is now evaluated on the time-dependent profile x_inst(τ). Nonetheless, the strategy to computing the determinant remains the same: we first find the eigenvalues:

( −(d^2/dτ^2) + V'' ) δx = λ δx (2.28)

The determinant is then given by the (suitably regularised) product of eigenvalues λ.

There is, however, a catch. In the background of the instanton, there is always one eigenvalue that is zero. Viewed naively, this would seem to tell us that the determinant vanishes, giving an infinite amplitude for tunnelling. This, it turns out, is not an infinity that we should try to regulate away, but instead an infinity that means we should think more carefully about what we’re calculating. Our first task, therefore, is to understand the physics behind this zero eigenvalue.

Happily, there is a simple reason for the existence of this zero eigenvalue. It follows from the fact that, as seen in the explicit instanton profile (2.24), the instantons come with an integration constant τ which specifies the “time” at which the profile jumps from one ground state to the other. Clearly the action of the instanton x_inst(τ − τ_1) is independent of τ_1. But this means that:

δx = ∂x_inst / ∂τ (2.29)

obeys (2.28) with a vanishing eigenvalue λ = 0.

Understanding zero modes is an important part of any instanton computation. They typically arise, as in the present case, because the instanton solution is not unique, but labelled by a number of parameters known as collective coordinates. For us, the instanton profile has a single collective coordinate, τ. Any fluctuation, like (2.29), that can be thought of as a variation of a collective coordinate necessarily has zero eigenvalue. These fluctuations are called zero modes.

In the present case, the existence of the zero mode can be traced to the fact that the underlying quantum mechanics enjoys time translation symmetry, while any particular instanton profile does not. In quantum field theory (or statistical field theory), we would refer to the zero mode as a “Goldstone boson” for time translational symmetry.

Now that we understand that the zero mode simply corresponds to the possible times, −T/2 < τ < T/2, at which the instanton makes its move, it’s clearer how we should proceed. We should treat the zero mode separately. First we integrate over all the non-zero modes. Then, rather than attempting to integrate over the zero mode, we instead exchange this for an explicit integration over the collective coordinate τ; this will simply multiply our final expression by an overall factor of T, the time over which the tunnelling takes place. The end result is:

⟨−a|e^(−HT)|+a⟩|_(one-inst) = e^(−S_inst) ∫_{-T/2}^{T/2} dτ √(1/(2π)) √(1/det'(−∂_τ^2 + V'')) J (2.30)

There are a few things to unpick in this formula. First, this is only the one-loop contribution and, strictly speaking, we should include a +... corresponding to higher loop contributions. Next, the determinant is written as det', with the prime denoting that we include only non-vanishing eigenvalues. The 2π is the standard normalisation for each mode in the path integral.

Finally, there is that factor of J: this is merely the Jacobian that arises when changing from integrating over the field x(τ), to the collective coordinate τ. It is easy to calculate:

J^2 = ∫ dτ (∂x_inst/∂τ)^2 = ∫ dτ ( (∂x_inst/∂τ)^2 + (dh/dx)^2 ) = S_inst (2.31)

where, in the second equality, we’ve used the fact that x_inst(τ) satisfies the instanton equation (2.20).

There is one further step that is useful. We will write our expression in a way that makes the comparison to the classical ground state energy clearer. As we’ve seen, each classical ground state is given by a harmonic oscillator of frequency ω. We already computed the path integral for Euclidean periodic time β in Section 2. The long time behaviour must be independent of the boundary conditions, so we also have:

⟨a|e^(−HT)|a⟩ = √(ω/(2π sinh(ωT))) ≈ e^(−ωT/2) (2.32)

where e^(−ωT/2) is the long time behaviour of the 1/sinh formula that we derived in (2.8). It will ultimately be clearer to write our tunnelling amplitude in a way that highlights the connection to the harmonic oscillator so, to this end, we collect everything together to get the final result for the one-instanton contribution:

⟨−a|e^(−HT)|+a⟩|_(one-inst) = T e^(−ωT/2) K e^(−S_inst) (2.33)

where all the other pre-factors have been bundled together into:

K = √(det(−∂^2 + ω^2) / det'(−∂_τ^2 + V'')) * √(S_inst/(2π))

−∂2 +ω2) K = inst τ 2π det′(−∂2 +V′′)

There are three things to take away from this. First, there are some slightly messy pre-factors that we’ve absorbed into K, which now include a ratio of the harmonic oscillator and instanton determinants. The exact expression for this ratio will not be particularly important in what follows and we won’t make any attempt to compute it. However, the advantage of writing this as a ratio of determinants is that it makes it clear that it differs from 1 only due to physics in a region of width 1/ω where the instanton profile is non-trivial, and V′′(x ) differs from ω2. We’ll see the utility of inst this shortly.

Figure 7. A dilute gas consisting of an instanton, followed by an anti-instanton and then, finally, another instanton.

Second, the amplitude is suppressed by a factor of e−Sinst. This is a characteristic feature of tunnelling in quantum mechanics. Finally, we see that the tunnelling amplitude from a single instanton has the slightly odd Te−T behaviour. It turns out that the correct interpretation of this comes by considering not a lone instanton, but a whole slew of them.

2.2.2 The Dilute Gas Approximation In the calculation above, we restricted to a single instanton solution that interpolates from one classical ground state to the other. However, we know that the interesting part of this instanton profile takes place over a region that is exponentially localised within a width ∼ 1/ω. That means that if we take an instanton, followed a long time later, by an anti-instanton, followed some time later still by another instanton, then this almost solves the classical equation of motion. It’s not an exact solution because there are no exact classical solution with these properties. But, if the instantons and anti-instantons are separated by a distance L ≫ 1/ω, then the action of a string of n such objects is roughly S = nS +O(e−ωL) n−inst inst This means that the action decreases very little as L increases. In this sense, as long as L ≫ 1/ω, the deviation from an exact solution is small.

Our interest in the classical instanton solutions is purely as a starting point for a semi-classical evaluation of the path integral. But, for these purposes, the approximate solutions, consisting of a string of instantons and anti-instantons are equally as good. This is known as the dilute gas approximation. An example of a dilute gas is shown in Figure 7.

We take the locations of these instantons and anti-instantons to lie at T T − < τ < τ < ... < τ < (2.34) 1 2 n 2 2 where τ is the position of an instanton for k odd, and an anti-instanton for k even. The dilute gas approximation holds if τ −τ ≫ 1/ω. k+1 k Incomputingtheamplitude⟨−a|e−HT|a⟩, weshouldsumoverallpossiblenumbersof instantons and anti-instantons. We just need one more instanton than anti-instanton to ensure that we end up in the opposite vacuum from where we started. In other words, n should be odd in (2.34).

Becausethe(anti)-instantonsarefarseparated,theircontributiontothepathintegral are independent. That means that we can simply import the calculation that we did above and the full tunnelling amplitude generalises the one-instanton result (2.33) (cid:90) T/2 (cid:90) T/2 (cid:90) T/2 (cid:88) ⟨−a|e−HT|+a⟩ = e−ωT/2 dτ dτ ... dτ (Ke−Sinst)n 1 2 n nodd −T/2 τ1 τn−1 Note that the harmonic oscillator contribution e−ωT/2 sits out the front of everything. Instead, each (anti)-instanton independently contributes a factor of the ratio of determinants K since, as we argued above, this ratio of determinants is non-trivial only in the vicinity of the (anti)-instanton.

The factor of T in (2.33), which came from the integral over the collective coordinate τ , is now replaced by the multi-integral above. This is straightforward to evaluate and gives (cid:88) Tn ⟨−a|e−HT|+a⟩ = e−ωT/2 (Ke−Sinst)n = e−ωT/2sinh(KTe−Sinst) n! nodd We see the effect of summing over the dilute gas is to exponentiate the one-instanton contribution KTe−Sinst.

We can also do a similar calculation to evaluate the amplitude ⟨+a|e−HT| + a⟩ = ⟨−a|e−HT|−a⟩ for returning to our original vacuum. Everything is the same, except that we should now take the number n of instantons and anti-instantons to be even. Of course, n = 0 is allowed. We then get (cid:88) Tn ⟨−a|e−HT|−a⟩ = e−ωT/2 (Ke−Sinst)n = e−ωT/2cosh(KTe−Sinst) n! neven Before we go on, we note that this same calculation appears in a seemingly different setting of Statistical Field Theory when we showed that discrete symmetries in 1d hot systems cannot be spontaneously broken. (See section 1.3.3 of those notes.)

The two formulae above contain the information about the energy splitting that we wanted to find. From our earlier discussion, we know that the ground state has non-vanishing overlap with |ground⟩ = |+a⟩+|−a⟩ while the first excited state has overlap with |excited⟩ = |+a⟩−|−a⟩ From above, we have ⟨ground|e−HT|ground⟩ = 2e−E0T with E = −Ke−Sinst and ⟨excited|e−HT|excited⟩ = 2e−E1T with E = +Ke−Sinst We see the promised energy splitting, proportional to the characteristic tunnelling amplitude e−Sinst.

Strictly speaking, neither of the formulae above can be trusted. Both E and E will 0 1 receive perturbative contributions to their energies and these will scale as some power of 1/S . The important fact is that, because of the symmetry of the potential, these inst contributions will be the same for both states. The real meaning of the calculation we’ve just done is to compute the splitting of the two states E −E = 2Ke−Sinst 1 0 Of course, if we really want to do a good job then we should roll up our sleeves and compute the ratio of determinants that sits in K. But we can see the key piece of physics without doing this: the splitting of energy levels scales as e−Sinst.

2.3 Instantons and Supersymmetry It’s now time to return to supersymmetric quantum mechanics. It turns out that there is a deep relationship between instantons and supersymmetry, both in quantum mechanics and in higher dimensional quantum field theories. The two make for perfect bedfellows. In this section, we will start to get a hint of where this relationship emerges from. We’ll also see that the existence of fermions brings some important technical differences to the tunnelling calculation that we did in the last section.

For concreteness, we’ll again work with the cubic h given in (2.22), corresponding to a double well potential V(x) with minima at x = ±a. The novelty, of course, is the presence of fermions.

The Euclidean supersymmetric action is (2.13) (cid:34) (cid:35) (cid:90) (cid:18) dx (cid:19)2 dψ 1 S [x,ψ,ψ†] = dτ +ψ† + h′2 −h′′ψ†ψ (2.35) 2 dτ dτ 2 We can largely proceed as the previous section. The bosonic instanton configuration is x (τ) and we evaluate the path integral in a semi-classical expansion around this inst background. In addition to the bosonic fluctuations δx, we must also integrate out the fermions. This give the usual determinant contribution (cid:18) (cid:19) det −h′′ (2.36) dτ where, as for the bosonic fluctuations, we evaluate h′′ = h′′(x (τ)) on the instanton profile.

inst We need to briefly pause to think about what this determinant means because, in contrast to the bosonic fluctuations (2.27), it’s not the determinant of a Hermitian operator. The operator used to be Hermitian, back when we were living in real time, where it was (+id/dt−h′′). But the Wick rotation ruined that property. We define d d D = −h′′ and D† = − −h′′ (2.37) dτ dτ The eigenvalue equation of this pair of operators should be thought of as Df(τ) = λg(τ) and D†g(τ) = λf(τ) The determinant (2.36) is then the product of all eigenvalues λ.

2.3.1 Fermi Zero Modes When we come to evaluate the fermionic determinant we run into the same subtlety that we saw in the bosonic case: the operator D has a zero eigenvalue and so the determinant is zero. In fact, the profile of the associated fermionic fluctuation takes the same form as the bosonic zero mode (2.29), dx inst ψ = η (2.38) dτ Here η is a constant Grassmann parameter. You should think of it as a Grassmann collective coordinate, analogous to the bosonic collective coordinate τ . It is straight-forward to see that ψ is an eigenfunction with vanishing eigenvalue. We have dx dh d2x dx (cid:18) d (cid:19) inst = ⇒ inst −h′′ inst = 0 ⇒ −h′′ ψ = 0 dτ dx dτ2 dτ dτ 0 We could have anticipated the existence of this fermionic zero mode on symmetry grounds. Recall that we could trace the bosonic collective coordinate τ to time translationalsymmetrysince, whiletheactionisinvariantundertimetranslations, anygiven instanton profile is not. Similarly, the fermionic collective coordinate can be traced to a fermionic symmetry which is, of course, supersymmetry. If we look again at the transformation rules (2.14) for the fermions in Euclidean time, then we see something rather nice: (cid:18) (cid:19) (cid:18) (cid:19) dx dx δψ = ϵ +h′ , δψ† = ϵ† − +h′ (2.39) dτ dτ The supersymmetry transformations have, hidden within them, the instanton and anti-instanton equations (2.20) and (2.21)! This, it turns out, is a beautiful feature of supersymmetry, and one that persists as we look both to more complicated theories and to more complicated instantons and other solitons. For now, we note that if we take an instanton obeying x˙ = h′ and hit it with a supersymmetry transformation, then ψ will turn on while ψ† will not. But, because supersymmetry is a symmetry, the action of the solution doesn’t change when ψ turns on. This is the fermi zero mode (2.38) that we identified above.

You might be nervous that we seem to have broken reality. In the background of an instanton, the fermion ψ has a zero mode, but ψ† does not. Indeed, the equation of motion for ψ† is D†ψ† = 0 and D† has no zero mode in the background of an instanton. Conversely, in the background of an anti-instanton ψ† has a zero mode, while ψ has none. This issue is commonplace for fermions in Euclidean time (or, more generally, in Euclidean space) and arises because D is not Hermitian. It’s best to think of ψ and ψ† as independent degrees of freedom in Euclidean time. Only when we Wick rotate back to real time (or Minkowski space) do the reality and Hermiticity properties of various operators manifest themselves again.

The upshot is that the instanton breaks one half of the supersymmetries: Q† is broken and generates a fermionic zero mode, while Q survives. Objects, like instantons, which have the property of preserving some fraction of the supersymmetry are known as BPS. (The initials stand for Bogomolnyi, Prasad and Sommerfeld, but what they actually did was only vaguely related to supersymmetry and the meaning of the initials BPS has evolved over the years.)

Although Q is unbroken, it is not totally redundant. It actually relates the collective coordinates τ and η of the instanton, a kind of “zero dimensional” supersymmetry. This interpretation won’t be important for now.

Let’s now return to our tunnelling computation. We know what to do: rather than integrate over all fermion modes, we isolate the zero mode and treat it separately, choosing instead to integrate over the fermionic collective coordinate η. As before, we pick up a Jacobian factor which, because the fermion zero mode (2.38) has the same functional form as the bosonic zero mode (2.29), is the same value J = S_inst that we computed in (2.31). But Jacobians for Grassmann integration come as 1/J, rather than J so this actually cancels our original bosonic contribution.

The net effect is that if we repeat the steps that took us to (2.30), we now have ⟨−a|e−HT|+a⟩|_{one−inst} = e^{−S_{inst}} ∫_{−T/2}^{T/2} dτ ∫ \frac{1}{2π} \frac{\sqrt{det'(∂_τ − h'')}}{\sqrt{det'(−∂_τ^2 + V'')}} dη We now have a ratio of determinants, both with zero eigenvalues omitted. There is no need to do our previous trick of introducing the harmonic oscillator amplitude (2.32). Indeed, part of the reason for doing that previously was to make manifest the 1/2 ℏω ground state energy but, as we’ve seen, the analogous semi-classical energy in supersymmetric quantum mechanics is exactly zero.

2.3.2 Computing Determinants In non-supersymmetric theories, it can be very challenging to compute the determinants in the background of an instanton. In contrast, in supersymmetric theories it is trivial because the ratio of determinants precisely cancels! To see this, we use the definition of the fermionic operators in (2.37) and note that D†D = (−d/dτ − h'') (d/dτ − h'')

= −d^2/dτ^2 + h''' + (h'')^2 = −d^2/dτ^2 + h''' h' + (h'')^2 where, to get to the second line, we’ve used the fact that these operators are evaluated on the solution to the instanton equation (2.20). But the potential is V = 1/2 h'^2, so V' = h' h'' and V'' = h''' h' + (h'')^2, so D†D = −d^2/dτ^2 + V'' which is precisely the bosonic fluctuation operator. This means that if we have a bosonic eigenfunction f, with D†D f = λ f with λ > 0, then we can define g = D f / √λ. We then have D f = √λ g and D† g = √λ f, which means that √λ is an eigenvalue of the fermionic operator (in the sense that we described previously).

This cancellation is entirely analogous to our previous observation that the ground state energy in a supersymmetric vacuum is zero, since the +1/2 ℏω from the harmonic oscillator is precisely cancelled by a −1/2 ℏω from the fermions. Here we see a similar cancellation persists about a BPS instanton configuration. This is a lesson that also transfers to higher dimensional quantum field theories, where it is often the case that all perturbative contributions cancel between bosons and fermions when evaluated about BPS backgrounds.

In the present context, it means that the tunnelling amplitude in a supersymmetric theory due to a single instanton is extremely simple: ⟨−a|e−HT|+a⟩|_{one−inst} = e^{−S_{inst}} ∫_{−T/2}^{T/2} dτ \frac{1}{2π} ∫ dη Not only is it very simple, it is also very zero. That’s because of the presence of the fermion zero mode. Recall the rules for Grassmann integration, ∫ dη 1 = 0 and ∫ dη η = 1 With nothing to soak up the fermion zero mode in the integrand, the amplitude for tunnelling vanishes.

In fact, this is to be expected given our earlier discussion of supersymmetric quantum mechanics. From Section 1.2, we know that the semi-classical ground states |−a⟩ and |+a⟩ lie in different spin sectors or, equivalently, in different components of the Hilbert space factorisation H = H_B ⊕ H_F. This means that there can be no tunnelling from one state to another and the path integral realises this by introducing a lone fermion zero mode.

2.3.3 Computing the Ground State Energy The Hamiltonian analysis of Section 1.2 told us more about this system. We know, for example, that the two states localised in different minima remain true ground states of the system but their energy is lifted above zero (i.e. supersymmetry is broken for a cubic h(x)). It is possible to see this from the path integral. We just need a small tweak of our previous analysis.

Rather than working with position eigenstates | ± a⟩, we’ll instead revert briefly to the exact ground states |L⟩ and |R⟩, which have support localised around the left and right minima respectively. Supersymmetry means that these must have the same energy E_0 and sit in H_B and H_F respectively. This means that Q†|R⟩ = Q|L⟩ = 0. Moreover, from our early analysis (1.3) we know that the two states are related by |R⟩ = Q†|L⟩ / √{2E_0}. The energy of either state can then be computed as follows: E_0 = ⟨L|H|L⟩ = (1/2) ⟨L|{Q,Q†}|L⟩ = (1/2) ⟨L|Q Q†|L⟩ = (E_0/2) |⟨L|Q|R⟩|^2 This means that E_0 = |⟨L|Q|R⟩|^2 (2.40)

We see that, to compute the energy of the ground state, we must compute a tunnelling amplitude ⟨L|Q|R⟩ but, crucially, with a factor of the supercharge Q sandwiched between the two states.

In fact, it turns out that there’s a little trick and things work out better if we compute the amplitude ⟨L|[Q,h]|R⟩^1. This is very closely related to the amplitude ⟨L|Q|R⟩ that we need. First, for a steep potential, we have |R⟩ ≈ | + a⟩ and |L⟩ ≈ | − a⟩, so h(x)|R⟩ ≈ h(a)|R⟩ and h(x)|L⟩ = h(−a)|L⟩ and ⟨L|[Q,h]|R⟩ ≈ (h(a)−h(−a)) ⟨L|Q|R⟩ = S_{inst} ⟨L|Q|R⟩ But the commutator [Q,h] has a particularly nice form. After Wick rotating the supercharge (1.17) reads Q = i(p−h')ψ and the commutator is [Q,h] = ψ dh/dx ^1 This sidesteps an annoying subtlety. If you compute the matrix element for ⟨L|Q|R⟩ directly then, at leading order, the result will vanish. This is because, after Wick rotation to Euclidean time, Q is proportional to the instanton equations and so vanishes when evaluated on the instanton. (This follows from the fact that the supersymmetry transformation (2.39) is proportional to the instanton equation.) You then have to work to higher order to find the non-vanishing ground state energy. Computing the matrix element of [Q,h] avoids this headache.

This means that we can get to the ground state energy (2.40) by computing the amplitude ⟨L|Q|R⟩ ≈ (1/S_{inst}) ⟨L|[Q,h]|R⟩ = (1/S_{inst}) ⟨L|h' ψ|R⟩ Now we can revert to our path integral expression again. We compute ⟨L|Q|R⟩ by the same kind of analysis that we performed above, but this time with an extra power of h'ψ in the integrand, ⟨L|Q|R⟩ = (e^{−S_{inst}} / √{S_{inst}}) ∫_{−T/2}^{T/2} dτ \frac{1}{2π} ∫ dη h' ψ We next replace the ψ that appears in this expression with the fermi zero mode (2.38) ψ = η dx/dτ. Furthermore, h' should be evaluated on the the instanton background x_{inst}(τ). Importantly, the presence of ψ soaks up the dη integral, rescuing the result from the vanishing answer we found before. We now have ⟨L|Q|R⟩ = (e^{−S_{inst}} / √{S_{inst}}) ∫ dτ (dh/dx)(dx/dτ) = (e^{−S_{inst}} / √{S_{inst}}) ∫ dτ (dh/dτ)

Rather wonderfully, the final integral is a total derivative and just gives us h(τ = +∞)−h(τ = −∞) = S_{inst}. The final answer is then very simple: ⟨L|Q|R⟩ = (e^{−S_{inst}} / √{2π}) (2.41)

We learn that the ground state energy is non-zero, but exponentially small E_0 ∼ e^{−2 S_{inst}} There’s another lesson lurking in the calculation above. To compute the energy E_0, we didn’t need to invoke the dilute gas approximation; it was sufficient to look at a single instanton. Indeed, viewed the right way it was necessary to look at just a single instanton. This is because the single instanton is BPS, meaning that it is invariant under one-half of the supersymmetries, and therefore has just a single fermion zero mode. However, a string of instanton-anti-instanton pairs does not have this property: it breaks both Q and Q† and therefore has two fermion zero modes, rather than just one. This is a special property of BPS instantons in supersymmetric theories that is closely related to the localisation of the path integral that we saw previously.

We’ll revisit instanton calculations of this kind in Section 3.2 where we discuss Morse theory. It will turn out that these kind of calculations underlie many of the key ideas in that context.

2.3.4 One Last Example: A Particle on a Circle Before we move on to more geometrical things, there is one last example that will prove useful to have under our belts. This is the supersymmetric particle moving on a circle S^1, with h(x) = ω R sin(x/R)

where R is the radius of the circle. The associated potential is V(x) = ω^2 cos^2(x/R)

and has two minima at x = ±πR/2.

We briefly discussed this model in Section 1.2.2 where we showed that, despite its similarities to the double well potential, it actually has two zero energy ground states, given by e^{h}|0⟩ and e^{−h} ψ†|0⟩. The puzzle that we’d like to address here is: why aren’t these states lifted from the perspective of the path integral?

It’s straightforward to guess the reason for this, but a little trickier to show how it works. Consider instantons (as opposed to anti-instantons) that solve dx/dτ = h' = ω cos(x/R)

These necessarily interpolate from small h(x) to large h(x) which, for us, means from the vacuum x = −πR/2 at τ → −∞ to the vacuum x = +πR/2 at τ → +∞. The novelty is that we have two different instanton solutions in this case, corresponding to the two different ways to go around the circle. The first instanton has ẋ > 0, the second ẋ < 0.

So it’s clear what the solution to our puzzle must be. These two instantons must contribute with opposite signs, so that they cancel out in the matrix element ⟨+|Q|−⟩ that we care about, leaving the energy of both states at zero. The question is: how does this minus sign arise in the computation?

This, it turns out is subtle. A rerun of the calculation above shows that there’s nowhere obvious that this sign could appear. The non-obvious place is, it turns out, in the definition of the determinants. The cancellation that we derived in Section 2.3.2 is really det D / √det D†D = ±1.

Figuring out which sign we get is not so straightforward. For now, we’ll content ourselves with the observation that, by answer analysis, the signs must be opposite for the two instantons that traverse the circle in different directions. We’ll give a prescription for computing this sign in Section 3.2 when we discuss Morse theory.

3 Supersymmetry and Geometry

In this section, we will begin our journey into the territory of mathematicians. Our strategy is to think about the physics of a particle moving on a manifold. As this section progresses, we will learn that the quantum ground states of this particle encode some precious information about the manifold.

Before we get to supersymmetry, let’s set the scene. We consider a massive, non-relativistic particle moving on the manifold M of dimension dim(M) = n. The dynamics of this particle is described by the Lagrangian L = g_{ij}(x) ẋ^i ẋ^j (3.1), where x^i are coordinates on the manifold, with i = 1,...,n, and g_{ij}(x) is a Riemannian metric on M.

Lagrangians of the form (3.1) are commonplace in physics, both in quantum mechanics and in higher dimensional quantum field theories. They often go by the unhelpful name of a sigma model. Sometimes they are called non-linear sigma models to reflect the fact that, unless g_{ij} is constant, the equations of motion will be non-linear. The name “sigma model” is utterly unilluminating; it dates from one of the first such models written down by Gell-Mann and Levy to describe the dynamics of mesons. (Somewhat comically, Gell-Mann and Levy were building on an earlier model that described both pions and an extra meson known as the “sigma”. They then wrote down an improved model that described just the mesons but chose to name it after the missing particle. And the name stuck.)

Geometrically, we should think of the sigma model as a map from the worldline of the particle W to the manifold, x(t) : W → M. The manifold M is known as the target space. For much of what we do below, the story will be simplest if M is a compact, orientable manifold and we’ll assume this to be the case in what follows.

Strictly speaking, the metric g_{ij}(x) in the Lagrangian should be viewed as the pull back of the metric from M to W. As we saw in earlier courses covering differential geometry, strictly speaking the sigma model only describes the particle in a patch of the manifold M that is covered by the coordinates x^i. One might think that to understand more subtle topological issues, we should be willing to consider overlapping patches. Perhaps surprisingly, it will turn out that this is not necessary, at least in these lectures.

We now ask: what does the particle described by (3.1) know about the manifold M, and what kind of mathematics might it encapsulate? To get a sense for this, we could first think about the Lagrangian (3.1) as describing a classical particle. In this case the equations of motion are the geodesic equations ẍ^i + Γ^i_{jk} ẋ^j ẋ^k = 0 (3.2), where Γ^i_{jk} is the Levi-Civita connection, Γ^i_{jk} = (1/2) g^{il} (∂_j g_{kl} + ∂_k g_{jl} - ∂_l g_{jk}), and we’re using the notation ∂_i = ∂/∂x^i.

There is certainly a lot of interesting physics in the geodesic equation. But it’s challenging to extract any interesting mathematical statements about the manifold M from knowledge of these geodesics. In particular, at any given time, the particle knows only about its immediate surrounding, yet any point looks much the same as any other locally. This means that the state of the particle cannot know anything about the global properties of the manifold. To extract any such information, we would need to know about the entire history of the particle.

This can be contrasted with the situation in quantum mechanics. Now the wavefunction spreads over the manifold M, which suggests that the state of the particle may well know about some of the manifold’s quirks. In particular, the state of a quantum particle may be sensitive to the topology of M. Ultimately, we will see that this is indeed the case, at least when we consider supersymmetric extension of our theory. But, for now, let’s push on and consider the quantum theory associated to the non-supersymmetric Lagrangian (3.1).

To describe the quantum theory, we first need the momentum p_i = ∂L/∂ẋ^i = g_{ij} ẋ^j. We then impose canonical commutation relations [x^i, p_j] = iδ^i_j and construct the Hamiltonian H = p_i ẋ^i − L = g^{ij} p_i p_j.

Already here, things are not so straightforward because the metric g_{ij} depends on x^i and these don’t commute with p_i. Different choices of ordering give different quantum Hamiltonians and so different theories.

There is no right or wrong choice here. But we can narrow down our options by requiring that the resulting theory has certain desirable properties. Given that we’re interested in the geometry of M, it makes sense to search for a Hamiltonian that is covariant with respect to changes of coordinates on M. In other words, to stick as closely as possible to differential geometry. The action of the momentum on the wavefunction is, as usual, p_i = −i∂_i, so the Hamiltonian should be a second order differential operator with terms that involve no more than two derivatives acting on the metric. There is a one-parameter family of such Hamiltonians, labelled by α ∈ ℝ,

H = − (1/2) √g^{-1} ∂_i (√g g^{ij} ∂_j) + αR (3.3),

where g = det g_{ij} and R is the Ricci scalar. The first term in this expression is the Laplacian, acting on functions, and can also be written more simply using the covariant derivative, H = − g^{ij} ∇_i ∇_j + αR (3.4).

We should also decide what Hilbert space we want our operators to act on. The obvious choice is to take the wavefunctions ψ(x) as functions over M, with the norm given by ||ψ||^2 = ∫ d^n x √g |ψ(x)|^2 (3.5). Note, in particular, that the inner product includes the factor of √g in the measure, as is appropriate in the geometric context.

Now we have our Hamiltonian (3.4) describing a quantum particle roaming around on a manifold M. What do we do with it? As physicists, our natural inclination is to find the spectrum of the Hamiltonian. We would typically expect that the particle has a unique ground state, with an infinite tower of excited states. This prompts two interesting questions: first, is it possible to calculate this spectrum? Second, what can we do with this information?

Both of these questions are interesting, although neither is easy. In general, it is a difficult problem to determine the spectrum of the Hamiltonian (3.4). Which properties of the manifold can be reconstructed from this spectrum is reminiscent of the famous question “can you hear the shape of a drum?”. Mathematicians have spent much time on this question. It is known, for example, that two manifolds may have the same spectrum even though they are not isometric. The first examples are 16-dimensional tori, but subsequent examples have been found in any dimension n ≥ 2. In fact, it’s known that two manifolds may share the same spectrum even if they have different topology (e.g. their fundamental group may be different). All of which is to say that the problem of a quantum particle moving on a manifold M is certainly interesting, but thinking as a physicist provides no particular advantage. We will now see that this situation changes (for the better!) when we introduce supersymmetry.

## 3.1 The Supersymmetric Sigma Model

There is a beautiful generalisation of the sigma model Lagrangian (3.1) that admits supersymmetry. In addition to the n coordinates x^i, we also introduce n complex Grassmann variables ψ_i, and then consider the action

S = ∫ dt [ (1/2) g_{ij}(x) ẋ^i ẋ^j + i g_{ij} ψ†^i ∇_t ψ^j − (1/4) R_{ijkl} ψ^i ψ^j ψ†^k ψ†^l ] (3.6).

The index i on ψ_i is telling us that the fermions live in the tangent space (strictly the tangent bundle) of M. This is highlighted by the appearance of the covariant derivative, pulled back to the worldline, in the fermion kinetic term ∇_t ψ^i = dψ^i/dt + Γ^i_{jk} ψ^k (dx^j/dt). As the particle moves on M, the fermions rotate due to this extra term. Finally, note that the four fermion term contracts with the Riemann tensor R_{ijkl}. This is the first suggestion that there might be some pretty geometry lurking in this theory. It’s sometimes useful to note that the last term can also be written as (1/4) R_{ijkl} ψ^i ψ^j ψ†^k ψ†^l = (1/2) R_{ijkl} ψ^i ψ†^j ψ^k ψ†^l. The equivalence of these two expressions follows from the Riemann tensor identity R_{i[jkl]} = 0.

The action (3.6) is invariant under N = 2 supersymmetry, given by the following supersymmetry transformations, δx^i = ε† ψ^i − ε ψ†^i, δψ^i = ε (−i ẋ^i + Γ^i_{jk} ψ†^j ψ^k), δψ†^i = ε† (+i ẋ^i + Γ^i_{jk} ψ†^j ψ^k) (3.7).

The associated supercharges are: Q = g_{ij} ẋ^i ψ†^j and Q† = g_{ij} ẋ^i ψ^j (3.8). Note that, in contrast to Section 1, we have taken the supercharge Q to depend on ψ rather than ψ†. This is a notational convenience whose advantage we will see as we go along.

How to Show that the Sigma Model is Supersymmetric

Conceptually, it’s straightforward to demonstrate the supersymmetricness of the sigma model: you just vary the action, use the transformations (3.7), and show that it vanishes. In practice, you end up with a tsunami of terms. Here’s some help to guide you along the way.

First, when implementing the supersymmetry transformation it’s useful to set ε = 0 and just keep the ε†.

在变分中，只需保留一半的项。另一半则由作用量及其变分必须为实数的要求最终确定。特别地，设ϵ = 0意味着δψ = 0而δψ† ≠ 0。其次，有一个在量子场论课程中描述过的技巧，用于计算与任何对称性相关的守恒荷：我们进行局域变分，而不是全局变分。为此，我们把ϵ†提升为ϵ†(t)。这样，我们就能从作用量的变分中找出乘在ϵ†项前的超荷。现在可以开始了。在δψ = 0但δx, δψ† ≠ 0的条件下变分作用量，得到

δS = ∫ dt [ g_ij ẋ_i δẋ_j + i δψ†_i ψ̇_j + i δψ†_i Γ^j_{kl} ẋ_k ψ_l + i ψ†_i δΓ^j_{kl} ẋ_k ψ_l + i ψ†_i Γ^j_{kl} δẋ_k ψ_l + δg_ij (ẋ_i ẋ_j + i ψ†_i ψ̇_j) + i Γ^j_{kl} ẋ_k ψ†_i ψ_l - (1/4) δR_{ijkl} ψ_i ψ_j ψ†_k ψ†_l - (1/2) R_{ijkl} ψ_i ψ_j δψ†_k ψ†_l ]

其中在最后一项中我们用到了R_{ijkl} = R_{ij[kl]}。接下来，通过计算它们所含的费米子数量来梳理这些项会很有帮助。将会有包含1个费米子、3个费米子和5个费米子的项，如果作用量要保持不变，这些项必须各自单独地相消。

例如，单费米子项来自开始时没有费米子的项中的δx_i = ϵ†ψ_i，以及开始时有两个费米子的项中费米子变分的第一部分δψ†_i = iϵ†ẋ_i。这些项是

δS|_{1-fermion} = ∫ dt [ g_ij ẋ_i δẋ_j + i g_ij δψ†_i (ψ̇_j + Γ^j_{kl} ẋ_k ψ_l) + (1/2) δg_ij ẋ_i ẋ_j ]

= ∫ dt [ g_ij ẋ_i (ϵ̇†ψ_j + ϵ†ψ̇_j) - g_ij ϵ†ẋ_i (ψ̇_j + Γ^j_{kl} ẋ_k ψ_l) + ∂_l g_ij ϵ†ψ_l ẋ_i ẋ_j ]

有两个包含ϵ†ẋ ψ̇的项立即相消。我们剩下

δS|_{1-fermion} = ∫ dt ϵ† [ (1/2) ∂_l g_ij - g_ik Γ^k_{jl} ] ẋ_i ẋ_j ψ†_l + ϵ̇† g_ij ẋ_i ψ_j

第一项因为度规是协变常数∇g = 0而消失。或者更详细地说，我们使用Levi-Civita联络的定义：g_ik Γ^k_{jl} = (1/2)(∂_j g_il + ∂_l g_ij - ∂_i g_jl)。但由于它乘以变分中的ẋ_i ẋ_j，这意味着我们需要对称化，因此g_ik Γ^k_{jl} ẋ_i ẋ_j = (1/2) ∂_l g_ij ẋ_i ẋ_j，这恰好与作用量变分中的另一项相消。我们剩下

δS|_{1-fermion} = ∫ dt ϵ̇† g_ij ẋ_i ψ_j

如上所述，我们将此识别为来自对称性的守恒荷，δS = ϵ̇†Q†，于是得到 Q† = g_ij ẋ_i ψ_j，正如(3.8)中所宣称的。

接下来最简单的是看包含5个费米子的项。它们来自δR_{ijkl}项和R_{ijkl} ψ_i δψ†_j ψ_k ψ†_l项，其中费米子变分我们只取本身包含两个费米子的部分，δψ†_j = ϵ†Γ^j_{mn} ψ†_m ψ_n。合起来，这些项给出

δS|_{5-fermion} = ∫ dt ϵ† [ -(1/4) ∂_m R_{ijkl} ψ_m ψ_i ψ_j ψ†_k ψ†_l + (1/2) R_{ijkl} Γ^j_{mn} ψ_i ψ_j ψ†_m ψ_n ψ†_l ]

在利用费米子施加反对称性后，此项由于Bianchi恒等式∇_{[m} R_{ij]kl} = 0而消失。

这就留下了作用量变分中的3费米子项。当然，它们就是我们尚未考虑的所有项。

δS|_{3-fermion} = ∫ dt [ δg_ij (i ψ†_i ψ̇_j + i Γ^j_{kl} ẋ_k ψ†_i ψ_l) + i g_ij δψ†_i (ψ̇_j + Γ^j_{kl} ẋ_k ψ_l) + i g_ij ψ†_i (δΓ^j_{kl} ẋ_k ψ_l + Γ^j_{kl} δẋ_k ψ_l) - R_{ijkl} ψ_i ψ_j δψ†_k ψ†_l ]

= ∫ dt ϵ† ∂_m g_ij ψ_m [ i ψ†_i ψ̇_j + i Γ^j_{kl} ẋ_k ψ†_i ψ_l + i g_mn ϵ† Γ^i_{mn} (ψ̇_j + Γ^j_{kl} ẋ_k ψ_l) - i g_ij ψ†_i ∂_m Γ^j_{kl} ψ_m ẋ_k ψ_l + i g_ij ψ†_i Γ^j_{kl} ψ̇_k ψ_l + (i/2) ϵ† R_{ijkl} ψ_i ψ_j ẋ_k ψ†_l ]

在这个表达式中有两种不同形式的项。第一种是ψ†ψψ̇形式。将它们汇集起来，我们发现它们乘以∇g = 0。第二种是ẋψ†ψψ形式。其中第一种涉及联络的组合，它们汇聚起来给出∂Γ + Γ²。但这正是黎曼张量的定义，并被上面的最后一项所抵消。结果是，对于全局变分ϵ̇† = 0，我们有δS = 0：作用量是超对称的。

**3.1.1 量子化：填充形式**

由于算符顺序问题，量子化σ模型需要一点技巧。正则动量为

p_i = ∂L/∂ẋ_i = g_ij ẋ_j + i Γ^i_{kl} ψ†_k ψ_l，和 ∂L/∂ψ̇_i = i g_ij ψ†_j

我们照常有

[x_i, p_j] = δ_ij，{ψ_i, ψ†_j} = g_ij

事实证明，玻色子和费米子之间的对易子是最棘手的。这最好用机械动量而非正则动量来描述：

π_i = g_ij ẋ_j = p_i - i g_il Γ^l_{jk} ψ†_j ψ_k

相关的对易关系为

[π_i, ψ_j] = i Γ^j_{ik} ψ_k，[π_i, ψ†_j] = i Γ^j_{ik} ψ†_k，[π_i, π_j] = - R_{ijkl} ψ†_k ψ_l

现在让我们更仔细地看看费米子的希尔伯特空间。我们以通常的方式量子化费米子：引入一个状态|0⟩，满足

ψ_i|0⟩ = 0

对所有 i = 1,...,n。然后我们通过连续作用ψ†_i来构建希尔伯特空间。在第一层我们有n个状态，ψ†_i|0⟩。在下一层我们有(1/2)n(n-1)个状态，ψ†_iψ†_j|0⟩ = -ψ†_jψ†_i|0⟩，依此类推。Grassmann量的自然反对称性意味着共有

\binom{n}{p} 个形如(ψ†)^p|0⟩的状态。

正如我们在1.4.1节中已经宣称的，这在几何中是一个非常熟悉的结构：它出现在完全反对称的(0, p)张量场中，也被称为p-形式。这促使我们建立如下认同：

|0⟩  ↔ 1 ψ†_i|0⟩  ↔ dx_i ψ†_iψ†_j|0⟩  ↔ dx_i ∧ dx_j ψ†_1...ψ†_n|0⟩  ↔ dx_1 ∧ ... ∧ dx_n

超对称量子力学希尔伯特空间中的状态不再仅仅是流形M上的函数，而是流形M上的所有形式。形如f(x)(ψ†)^p|0⟩的状态对应于p-形式。我们将M上的p-形式空间记为Λ^p(M)。

Grassmann变量与形式之间的这种关系，即将ψ†_i认同为dx_i∧，提供了超对称与几何更有趣方面之间的关键联系。由此，许多美妙的几何事实随之而来。例如，我们可以问：ψ_i的几何解释是什么？从对易关系{ψ_i, ψ†_j} = g_ij来看，它显然充当一个映射ψ_i: Λ^p(M) → Λ^{p-1}(M)。我们可以更明确地检查：

ψ_iψ†_jψ†_k...ψ†_l|0⟩ = {ψ_i, ψ†_jψ†_k...ψ†_l}|0⟩ = (g_ijψ†_k...ψ†_l) - (ψ†_j g_ik...ψ†_l) + ... |0⟩

但在形式的语言中，这是内乘（interior product）的作用：

ψ_i ↔ g_ij ι_{∂/∂x_j}

同时，希尔伯特空间中状态之间的内积为

⟨ω|η⟩ = ∫ ω̄ ∧ ⋆ η   (3.9)

其中ω̄是ω的复共轭，⋆是Hodge对偶。注意，只有当ω和η是相同次数p的形式时，它才非零。此外，当作用在函数ω ∈ Λ^0(M)上时，它重现了范数(3.5)。

拉格朗日量(3.6)具有一个U(1)对称性，作用在费米子上为

ψ_i → e^{iα}ψ_i，ψ†_i → e^{-iα}ψ†_i

相应的Noether荷是

F = g_ij ψ†_i ψ_j

它计数费米子激发数，或者用我们新的几何语言来说，就是形式的次数。如果我们有一个状态|ϕ⟩ ∈ Λ^p(M)，那么

F|ϕ⟩ = p|ϕ⟩

F守恒这一事实意味着哈密顿演化不会混合不同次数的形式：能量本征态位于某个特定的Λ^p(M)中。费米子数F还提供了将我们的希尔伯特空间分为玻色部分和费米部分的分级：H = H_B ⊕ H_F。它们分别由偶次和奇次形式组成。

H_B = ⨂_{p even} ℂ ⊗ Λ^p(M)，H_F = ⨂_{p odd} ℂ ⊗ Λ^p(M)

其中整体因子ℂ的出现仅仅是因为量子力学中的波函数是复值的，而不是实值的。

最后，我们来看超荷Q和Q†本身。动量算符的存在意味着它们充当导数，而费米子确保它们也将Q映射为Q: Λ^p(M) → Λ^{p+1}(M)。但在微分几何中，有一个具有这些性质的非常自然的对象：它就是外微分

Q = i ψ†_i ∂/∂x_i ↔ dx_i ∧ = d

类似地，Q†: Λ^p(M) → Λ^{p-1}(M)充当伴随算符

Q† = i ψ_i p_i ↔ g_ij ι_{∂/∂x_j} = d†

作用在p-形式上，伴随算符也可以写成

d† = (-1)^{n(p+1)+1} ⋆ d ⋆

这个伴随算符湮灭函数d†f = 0，对f ∈ Λ^0(M)成立。这是预料之中的，因为它源于ψ_i|0⟩ = 0。类似地，外微分本身湮灭最高次形式，dω = 0，对所有ω ∈ Λ^n(M)成立。在我们继续之前，注意Q ≡ d和Q† ≡ d†的对应关系是我们选择定义Q为涉及ψ†而非如第1节中那样涉及ψ的超荷的原因。

超荷的认同也赋予了哈密顿量一个几何意义。它是

H = {Q, Q†}/2 ⇒ H = Δ/2

其中

Δ = d d† + d† d

这是微分几何中的拉普拉斯算符。从它用d和d†的定义可以清楚地看出，它是超对称哈密顿量的首要候选者；在某种意义上，我们上面所做的一切只是用Grassmann变量ψ和ψ†来实现这种可能性。

拉普拉斯算符是正定的，这符合超对称哈密顿量的要求。这源于Q†(或等价的d†)中的†意味着关于内积(3.9)的伴随运算，因此对任何ω ∈ Λ^p(M)，

⟨ω|Δω⟩ = ⟨ω|d d†ω⟩ + ⟨ω|d† dω⟩ = ||d†ω||² + ||dω||² ≥ 0   (3.10)

一次简短的计算（例如，参见广义相对论讲座的3.1.4节）表明，当作用在函数f ∈ Λ^0(M)上时，拉普拉斯算符由下式给出

Δf = (1/√g) ∂_i (√g g^{ij} ∂_j f)

这与非超对称σ模型的哈密顿量(3.3)一致。然而，请注意，在没有超对称性的情况下，总是可以选择将(3.3)中的αR项添加到哈密顿量中。超对称性消除了这种模糊性。

**3.1.2 基态与de Rham上同调**

我们现在将考虑我们预期发现的谱的类型。正如我们在第1节中看到的，所有能量E ≠ 0的状态必须成对出现。特别地，如果一个能量本征态|α⟩满足E ≠ 0，并且

Q|α⟩ = 0

那么|α⟩ is Q-exact, meaning that it can be written as |α⟩ = Q|ϕ⟩ for some |ϕ⟩. To see this, we just need to use QQ† + Q†Q = 2E to see that |α⟩ = Q (Q†|α⟩)/(2E)

This tells us that Q and Q† map us back and forth between the two states related by supersymmetry. In the form language, we see that supersymmetry relates pairs of p and p+1 forms. These are shown as the yellow dots in Figure 8.

However, as we’ve seen in previous examples, the ground states with E = 0 are special since there is no need for these to be paired. In the present context, the ground states arise from forms that obey Δγ = 0 ⇔ dγ = d†γ = 0 Forms of this kind are called harmonic. These are depicted as red dots in Figure 8. The space of harmonic p-forms is denoted Harp(M). We learn that the Hilbert space of ground states is Hground = ⊕ Harp(M)

This discussion also tells us that there are three kinds of states in the Hilbert space: those for which |ϕ⟩ = Q|α⟩ or |ϕ⟩ = Q†|β⟩, which sit in supersymmetric pairs. And those for which Q|ϕ⟩ = Q†|ϕ⟩ = 0 which are the supersymmetric ground states. This means that any state |ϕ⟩ ∈ H has a unique decomposition as |ϕ⟩ = Q|α⟩ + Q†|β⟩ + |ω⟩ (3.11)

where Δ|ω⟩ = 0. In the geometric language, this is equivalent to saying that any form can be written uniquely as ω = dα + d†β + γ (3.12)

where ω is harmonic. This is known as the Hodge decomposition theorem.

There is an important comment to make here. The Hodge decomposition theorem is not a trivial statement in mathematics. It took Hodge much of the 1930s to prove and, even then, needed corrections from Weyl and Kodaira. Yet the statement about the decomposition of states in the Hilbert space (3.11) follows trivially from the structure of supersymmetric quantum mechanics! What’s going on?

Shortly we will “prove” other theorems in geometry where we will make use of the physicist’s secret weapon, the path integral. Here, however, the power of physics comes only from our blatant disregard for anything approaching rigour. In geometry, the space of differential forms is not a Hilbert space because the inner product (3.9) is not complete. In quantum mechanics, we deal with this by restricting attention to L2 forms but then one has to worry whether the exterior derivative acts solely within this space. All of these are subtleties that we sweep under the rug in physics, but present the real challenge behind the proof of the Hodge decomposition theorem.

Cohomology There is another way to view the ground states in terms of cohomology. As we’ve seen, the exterior derivative d (or equivalently the supercharge Q) maps us from d: Λp(M) → Λp+1(M). We can depict this in terms of what mathematicians call a chain complex Λ0(M) →d Λ1(M) →d Λ2(M) →d Λ3(M) →d ...

Because d² = 0, the image of one map necessarily lies in the kernel of the next. The idea of cohomology is that it’s interesting to look more closely at the difference between the kernel and image.

First some definitions. A form ϕ is said to be closed if dϕ = 0. We denote the space of all closed p-forms as Zp(M). Another way to say this is that Zp(M) is the kernel of the map d: Λp(M) → Λp+1(M).

A form ϕ is said to be exact if it can be written as ϕ = dα for some α. We denote the space of all exact p-forms as Bp(M). Another way to say this is that Bp(M) is image of the map d: Λp−1(M) → Λp(M).

As we mentioned above, we necessarily have Bp(M) ⊂ Zp(M). The de Rham cohomology group is defined to be Hp(M) = Zp(M)/Bp(M)

The quotient here is an equivalence class. Two closed forms ϕ and ϕ′ ∈ Zp(M) are said to be equivalent if ϕ = ϕ′ + dα for some α. We say that ϕ and ϕ′ sit in the same equivalence class [ϕ]. The cohomology group Hp(M) is the set of equivalence classes. In other words, it consists of closed forms mod exact forms.

Finally, we define the Betti numbers, bp = dimHp(M)

There are a number of interesting things about these Betti numbers. First, this counting of cohomology classes is just another way of counting the ground states in quantum mechanics, and the Betti numbers can equally well be viewed as counting harmonic forms. This follows from...

Claim: There is an isomorphism Hp(M) ≅ Harp(M) and so bp = dimHarp(M)

Proof: The proof follows straightforwardly from the Hodge decomposition (3.12). We’ll first show that each harmonic form is associated to an element of Hp(M). Clearly any harmonic form γ is closed, with dγ = 0. But the unique nature of the Hodge decomposition (3.12) means that γ cannot be written as γ = d(something) and so forms the basis of an equivalence class [γ] ∈ Hp(M).

Next we must go the other way and show that each equivalence class [ω] ∈ Hp(M) is associated to a harmonic form. We decompose ω = dα + d†β + γ. By the definition of [ω] ∈ Hp(M), we must have dω = 0 and so, using the inner product (3.9), we have 0 = ⟨dω|β⟩ = ⟨ω|d†β⟩ = ⟨dα + d†β + γ|d†β⟩ = ⟨d†β|d†β⟩ where, in the final step, we integrated by parts and used the facts that ddα = 0 and dγ = 0. The upshot is that d†β = 0 and any element of the equivalence class [ω] ∈ Hp(M) takes the form ω = dα + γ. Any other member of the same equivalence class ω′ ∈ [ω] can be written as ω′ = dη + γ and is associated to the same harmonic form γ. □

There’s an analogy here with gauge symmetry that is worth highlighting. In Maxwell theory, the gauge potentials A and A + dα are physically equivalent as they are related by a gauge transformation. If we want to pick a representative of this equivalence class then we need gauge fixing condition that picks out one particular choice of A. For cohomology, the equivalence class [ω] relates ω ∼ ω + dα. A representative of this class can be picked by the “gauge fixing condition” d†ω = 0. This then picks out the harmonic forms as special.

Any manifold M with dimension dim(M) = n always has b0 = 1 and bn = 1. The zero forms are just functions over the manifold, and any constant function over M is clearly harmonic, but cannot be written as d(something) as there are no p = −1 forms. Similarly, the volume form Vol = ⋆1 provides the harmonic top form.

Other Betti numbers come in pairs with bp = bn−p, a relationship that follows from Poincaré duality. It turns out that all these higher Betti numbers are non-vanishing only if the manifold M has some interesting topology. To explain this, we need to remove the co in cohomology.

Homology Here we give a brief overview of how the de Rham cohomology, and associated harmonic forms, contain information about the topology of the manifold M.

Consider a submanifold C ⊂ M. We’ll take this to be a closed submanifold, meaning that it has no boundary ∂C = 0 An interesting question is whether C itself can be thought of as the boundary of another manifold, meaning C = ∂D. This is a question of topology.

We can see this in two simple examples shown in Figure 9. There we depict two manifolds of dimension two: the sphere M = S² and the torus M = T². On each we’ve drawn a one-dimensional submanifold C as a red line. For C ⊂ S², this submanifold is the boundary of a disc C = ∂D. For C ⊂ T² there is no such bounding manifold D. This reflects the fact that there is interesting topology in the torus, but not in the sphere.

Indeed, there are actually two different topologically non-trivial submanifolds of the torus: in addition to the circle C shown in Figure 9, there is also the circle C′ that winds in the way shown on the right.

The algebraic structure of these topologically non-trivial submanifolds is identical to those of forms. In particular, a boundary of a boundary is always vanishing, which we write as ∂² = 0. This, obviously, is strikingly reminiscent of the exterior derivative relation d² = 0. We use this to define homology groups using ∂ analogous to the cohomology groups that we defined previously using d. The homology group Hp(M) is the equivalence class of closed p-dimensional submanifolds that are not themselves the boundary of a (p+1)-dimensional manifold. In particular, two submanifolds C1 and C2 lie in the same homology class if one can be smoothly deformed into the other. In terms of equations, this means that the difference is a boundary, C1 ∼ C2 if and only if C1 − C2 = ∂D

The relationship between homology and cohomology is more than just an analogy. The spaces Hp(M) and Hp(M) are dual to each other, and hence isomorphic. This statement, known as de Rham’s theorem, is not straightforward to prove but it’s easy to get some intuition for how it works. Given a closed submanifold C ⊂ M and a form ω on M we can define a map to the real numbers, given by (C, ω) = ∫C ω Strictly speaking, the integral only makes sense if dimC = p and ω is a p-form. If the form ω has a degree different than dimC then the pairing is simply said to be zero. In what follows, we will sometimes refer to such a closed submanifold C as a cycle.

This pairing has some lovely properties that follow from Stokes’ theorem. First, the answer depends only on the equivalence class [ω] ∈ Hp(M). To see this, note that ∫C (ω + dα) = ∫C ω + ∫C dα but the total derivative ∫C dα = 0 because ∂C = 0.

Conversely, if we consider two submanifolds C1 and C2 that can be smoothly deformed into each other, so C1 − C2 = ∂D, then integrating any closed form ω gives ∫C1 ω − ∫C2 ω = ∫∂D ω = ∫D dω = 0 We see that the answer only depends on the equivalence class [C] ∈ Hp(M).

The upshot of these arguments is that the ground states of the supersymmetric sigma model (3.6) are determined by the topology of the target space M. Heuristically, the quantum particle can minimise its energy by spreading its wavefunction over topologically non-trivial submanifolds of M.

Here are some simple examples. The sphere Sn is boring: its only Betti numbers are b0 = 1 corresponding to constant functions and bn = 1 corresponding to the top form.

the torus T^n is more interesting: it has Betti numbers b_p = C(n,p).

In n = 2 dimensions, closed manifolds are known as Riemann surfaces and are labelled by their genus g which counts the number of holes. Here are some examples of manifolds with genus g = 0, g = 1 and g = 2 respectively.

The Betti numbers are b_0 = b_2 = 1 and b_1 = 2g. Each extra hole introduces two new topologically non-trivial 1-manifolds that encircle the hole in different ways.

Finally, I should mention that in any logical presentation, homology precedes cohomology. Our physics approach has lead us to introduce these in an inverted order.

3.1.3 The Witten Index and the Chern-Gauss-Bonnet Theorem

In Section 1, we learned that there is something special about the Witten index in supersymmetric quantum mechanics. Recall that this is defined by Tr(-1)^F e^{-βH} and counts the number of supersymmetric ground states, up to a sign.

For our supersymmetric sigma model, the Witten index is just the alternating sum of Betti numbers Tr(-1)^F e^{-βH} = χ(M) := Σ_p (-1)^p b_p. (3.13)

This is perhaps the most famous topological invariant in mathematics: it is known as the Euler character of the manifold.

Again, some examples. The sphere S^n has Euler character χ(S^n) = 1+(-1)^n, so is either χ(S^n) = 2 for n even or χ(S^n) = 0 for n odd. The torus T^n always has χ(T^n) = 0. The 2d Riemann surface of genus g has χ(M) = 2−2g.

We can see from our discussion of quantum mechanics why this is a topological invariant. We know that the Witten index is robust against any small change of the parameters in the quantum mechanics. In the present case, that means that if we vary the metric g_ij, at least within reason so that we avoid singularities, then the Witten index should remain unchanged. But that means that the object χ(M) defined in (3.13) must be independent of the choice of metric: it can depend only on cruder aspects of M, specifically its topology.

Finally, note that the sigma models provide many other examples in which the Witten index vanishes but there are, nonetheless, ground states with E = 0. For example, the sigma model on S^3 (or, indeed, any odd dimensional sphere) has χ(S^3) = 0 but there are two ground states, one the constant function corresponding to b_0 = 1 and the other the volume form corresponding to b_3 = 1. These ground states are also protected by topology, this time by the cohomology rather than the cruder Euler character.

The Path Integral Again

As we saw in Section 2, there is a straightforward description of the Witten index in terms of the path integral. We simply need to calculate I = Tr(-1)^F e^{-βH} = ∫ Dx Dψ† Dψ e^{-S_E[x,ψ,ψ†]} where Euclidean time τ has period β and both x and ψ are assigned periodic boundary conditions. The Euclidean action is S_E = ∫ dτ [ (1/2) g_ij x˙_i x˙_j + g_ij ψ†_i ∇_τ ψ_j - (1/4) R_{ijkl} ψ_i ψ_j ψ†_k ψ†_l ]

with ∇_τ ψ_i = ψ˙_i + Γ^i_{jk} x˙_j ψ_k. We know that the Witten index is independent of β. We will use this to compute the path integral in the limit β → 0. The key idea is that, in this limit, any non-trivial excitations around the Euclidean circle costs an increasing amount of action and so we can restrict ourselves to constant configurations, where the path integral reduces to a normal integral.

Putting these words into formulae, we first rescale the time coordinate to work with τ′ = τ/β so the new time coordinate has period τ′ ∈ [0,1). We also rescale ψ → β^{-1/4} ψ, leaving us with the Euclidean action S_E = ∫ dτ′ [ (1/(2β)) g_ij x˙_i x˙_j + (1/√β) g_ij ψ†_i ∇_τ ψ_j - (1/(4β)) R_{ijkl} ψ_i ψ_j ψ†_k ψ†_l ]

where we now see explicitly that in the limit β → 0, the modes with x˙ and ψ non-zero are heavily suppressed. The path integral then reduces to the ordinary integral Tr(-1)^F e^{-βH} = ∫ d^n x ∫ d^n ψ d^n ψ† exp[ - (1/4) R_{ijkl} ψ_i ψ_j ψ†_k ψ†_l ] / ( (2π)^{n/2} √g )

As in previous examples, we have to saturate the Grassmann integration. But this time, there’s a clear way to do it. We simply expand out the exponential until we find the right number of fermions.

Since the fermions always come in groups of four, if n is odd the integral necessarily vanishes. We learn that χ(M) = 0 if dimM = odd.

This simple result also follows from the relation b_p = b_{n−p}. However, if n is even then the term with n/2 powers of the Riemann tensor will saturate the integral.

We start with n = 2. In this case, we pull down just a single copy of the Riemann tensor. After doing the Grassmann integrations, we find Tr(-1)^F e^{-βH} = ∫ d^2 x (√g / (4π)) R.

This is the well known Gauss-Bonnet expression for the Euler character of a Riemann surface.

In general, the Grassmann integrations leave us with n/2 copies of the Riemann tensor, contracted with epsilon symbols Tr(-1)^F e^{-βH} = ∫ d^n x (1/( (4π)^{n/2} (n/2)! )) √g ε^{i_1...i_n} ε^{j_1...j_n} R_{i_1 i_2 j_1 j_2} ... R_{i_{n-1} i_n j_{n-1} j_n}.

This is the generalisation of the Gauss-Bonnet theorem, first proven by Chern in 1944. The contraction of the epsilon symbols results in an expression known as the Euler density. The slightly unusual looking 1/√g should be thought of as √g × (1/√g) × (1/√g) with the (1/√g) factors combining with the epsilon symbols to give tensor densities.

As an example, for n = 4 dimensional manifolds the expansion of the Euler density gives χ(M) = ∫ d^4 x (√g / (8π^2)) (R_{ijkl} R^{ijkl} − 4R_{ij} R^{ij} + R^2).

The magic of the Chern-Gauss-Bonnet theorem is that a global topological object, χ(M), is described in terms of an integral of local data, the Euler density. The magic of supersymmetric quantum mechanics is that it gives a straightforward derivation of this result, with the only real complication the combinatoric factors that arise from Grassmann integration. This is the first example where a deep mathematical result can be derived in a different way using the path integral. It won’t be the last.

## 3.2 Morse Theory

Our goal in this section is to understand some basic ideas of Morse theory, viewed through the lens of supersymmetric quantum mechanics.

We stick with our N = 2 supersymmetric sigma model (3.6), describing a particle moving on a manifold M. The novelty is that we now also include a potential h(x) over the manifold. The resulting supersymmetric theory is a combination of the sigma model and the kind of theories we considered in Section 1.4.1, L = (1/2) g_ij x˙_i x˙_j + i g_ij ψ†_i ∇_t ψ_j − (1/4) R_{ijkl} ψ_i ψ_j ψ†_k ψ†_l − (1/2) g_{ij} ∂h/∂x^i ∂h/∂x^j − (∇_i ∂_j h) ψ†_i ψ_j. (3.14)

Note that the final, fermionic term has the opposite sign from that of Section 1.3; this is purely a choice of convention and, as we will see shortly, will bring us in line with definitions used in mathematics. This action is invariant under the supersymmetry transformations δx = ϵ†ψ − ϵψ† δψ_i = ϵ(−ix˙_i + Γ^i_{jk} ψ†_j ψ_k − ∂h/∂x^i) (3.15)

δψ†_i = ϵ†(+ix˙_i + Γ^i_{jk} ψ†_j ψ_k − ∂h/∂x^i).

These are a combination of the transformations (1.19) for our original quantum mechanics with a potential and (3.7) for the supersymmetric sigma model.

In the absence of the potential, we know that the ground states of the supersymmetric quantum mechanics spread over cycles of M. However, when we add the potential h, the wavefunctions get squeezed and, as the potential gets larger, the wavefunctions are increasingly localised at the minima of the potential. We know that the Witten index can’t change. But, more strongly, the total number of E = 0 ground states doesn’t change either and, even in the presence of the potential, is given by the Betti numbers of the manifold.

To see this statement, first note that the supercharges associated to (3.15) are given by Q = g_ij (x˙_i + i ∂h/∂x^j) ψ†_j and Q† = g_ij (x˙_i − i ∂h/∂x^j) ψ_j.

Translated into the geometric language, we have Q ←→ d + dx^i ∧ ∂h = d + dh∧ = e^{-h} d e^h. (3.16)

Similarly Q† ←→ (d + dh∧)† = e^h d† e^{-h}.

We saw in Section 3.1.2 that the ground states are determined by the cohomology of Q. But the cohomology when h ≠ 0 is isomorphic to the cohomology when h = 0. We simply take the wavefunctions in the latter case and multiply them by e^{-h}. Indeed, this is the form of the wavefunctions (1.12) that we found back in Section 1.2 when considering a particle on a line.

The fact that the number of supersymmetric ground states is independent of h means that something interesting must be going on. Because if we crank up h to be very large, the ground states are localised around the minima of the potential V = |∂h|^2. This means that there must be some relationship between these minima and the topology of the manifold. This relationship goes under the name of Morse theory.

The minima lie at critical points of h which we will label x = X. They obey ∂h/∂x^i (X) = 0 for all i = 1,...,n.

The function h is said to be a Morse function if it has the property that the critical points x = X are isolated and non-degenerate. From now on, we’ll assume that this is the case.

Consider the situation where we scale the Morse function h(x) → ζ h(x), and subsequently send ζ → ∞. In this limit, the physics is entirely dominated by the critical points of the potential and, at the semi-classical level, the ground state wavefunction is localised at the critical point x = X. That’s not to say that all critical points are necessarily true E = 0 ground states; there may well be tunnelling of the kind that we discussed in Section 2.3 that lifts putative ground states in pairs. But the true ground states must be contained within the set of critical points.

We also need to figure out what’s going on with fermions. This is the same calculation that we already met in Section 1.4.1. There, we learned that we should look at the eigenvalues of the Hessian ∂_i ∂_j h, (∂_i ∂_j h) e_j = λ_j e_j, where e_j are the eigenvectors and λ_j the eigenvalues, with j = 1,...,n. (The index j labels the eigenvectors and eigenvalues and shouldn’t be summed over. Note also that we flipped the sign of h in the action (3.14) relative to our discussion in Section 1.4.1, and that shows up as a change of minus sign in this equation relative to (1.27).)

For each negative eigenvalue λ_j < 0, the final term in (3.14) tells us that we can lower the energy by exciting the corresponding collection of fermions ejψ†j. Meanwhile, for each positive eigenvalue λ > 0, we’re better off in the unexcited state.

We define the Morse index, µ(X), to be µ(X) = The number of negative eigenvalues of ∂ ∂ h(X)

i j

We learn that the semi-classical ground state sits in the sector with µ(X) fermions excited. In other words, the semi-classical ground state at the critical point x = X is a p-form with p = µ(X).

Already we learn something striking. We can compute the Witten index by simply summing over the critical points X, just as we did in (1.24). The novelty is that we know that, for our supersymmetric sigma model, the Witten index tells us the Euler character of the manifold M. This means that we can compute the Euler character of M from the critical points of a function over M, χ(M) = (−1)µ(X)

In fact, we can say more than this. The total number of critical points may well be more than the total number of E = 0 ground states, since states can be lifted in pairs. But the number of critical points can never be smaller than the number of ground states! Suppose that there are m critical points X with Morse index p = µ(X). This can be no less than the number of ground states associated to p-forms, so m ≥ b (3.17)

p p with b the Betti number. This is known as the weak Morse inequalities.

Nice as this is, it’s possible to do better. We can, in fact, recover the original Betti numbers b from an understanding of the critical points and the relationships between them. In the rest of this section we explain how.

Figure 10. Two shapes, both topologically S2 with the Morse function given by the height. On the left there are two critical points, on the right there are four. My wife thought it important to point out that these are not drawn to scale.

A Simple Example: The Two Sphere

To illustrate these ideas, we can look at the case of S2. We know that the Betti numbers are b = b = 1 and b = 0.

0 2 1

Suppose that we embed S2 with its round metric in R3. Then we can consider the height function h = z This is shown in the left-hand side of Figure 10. Clearly there are two critical points of the height function: at the bottom of the sphere where it is a minimum and at the top of the sphere where it is a maximum. The Morse index is µ = 0 and µ = 2 respectively, so from the discussion above we know that these ground states are associated to 0-forms and 2-forms. We also know that ground states localised around these minima must be exact E = 0 states.

Now we deform the system. We could change the Morse function h but, for illustrative purposes, it is simplest if we instead change the metric on the sphere. We’ll turn it into the bean shape shown in the right-hand side of Figure 10, keeping the same height function h = z. This time there are four critical points, one with µ = 0, two at the top with µ = 2, and the saddle point in the middle with µ = 1.

Note that the Euler character hasn’t changed, χ(S2) = (−1)µ(X) = 1+(−1)+1+1 = 2 Moreover, the weak Morse inequalities hold, with m = b = 1 and 1 = m > b = 0 0 0 1 1 and 2 = m > b = 1.

2 2

For the bean shaped metric, we know that two of four semi-classical ground states must be lifted to have E > 0. Clearly, it should be the 1-form and some combination of the two 2-forms that gets lifted. Our goal now is to understand how this works, both in the case of the kidney bean and more generally. We will see that much of the technology that we will need has already been covered in the supersymmetric instanton calculation of Section 2.3.

3.2.1 Instantons Again

Suppose that our Morse function has r critical points at x = X with a = 1,...,r, such that ∂h (X ) = 0 ∂xi a

The weak Morse inequalities (3.17) tell us that r ≥ b , the total number of supersymmetric ground states (counted without sign). If r = b then the Morse inequalities are saturated, m = b , and we’re done: as we crank up the strength of the potential, the ground state wavefunctions morph smoothly from being spread over cycles of the manifold, to being localised at the critical points. This is the situation depicted by the orange in the previous example.

However if r > b , like in the example of the kidney bean, then there are more critical points than genuine ground states and we have some work to do. Some of the semi-classical ground states associated to critical points must be lifted.

The exact energy eigenstate localised around x = X will be denoted as |Ψ ⟩. Some of these states will persist as zero energy states when all quantum corrections are taken into account. Meanwhile others will be lifted but, as we saw in Section 2.3, will remain as low lying states, with energies of order e−Sinst. Our goal is to understand this spectrum.

To this end, we will compute the matrix elements ⟨Ψ |Q|Ψ ⟩ a b

Any state with E = 0 must be annihilated by Q so, in general, we expect this matrix to have rank r− b , with the zero eigenvectors the true quantum ground states and the remainder those that are lifted.

As is Section 2.3, it’s simpler to compute the related set of matrix elements ⟨Ψ |[Q,h]|Ψ ⟩ a b

⟨Ψ |Q|Ψ ⟩ ≈ a b h(X )−h(X )

b a

where, after Wick rotation, the commutator with the supercharge (3.16) gives ∂h [Q,h(x)] = ψ†i ∂xi

The fact that we have just a single fermion ψ† in the matrix element means that we’ll get non-vanishing contributions if the state |Ψ ⟩ has one additional fermion excited than |Ψ ⟩. Or, said differently, if the Morse indices differ by one: µ(X )−µ(X ) = 1 (3.18)

a b

The difference ∆µ = µ(X )−µ(X ) is called the relative Morse index.

a b

The Instanton Equations

It’s clear that we are now back in the realm of the quantum tunnelling calculations that we performed in Sections 2.2 and 2.3. To start, we can study the instantons in a sigma model with potential. Focussing just on the bosonic fields for now, the action (3.14) in Euclidean time is 1 1 ∂h ∂h S = dτ g x˙ix˙j + gij E 2 ij 2 ∂xi∂xj where now x˙ = dx/dτ. We can write this by completing the square as 1 ( dxi ∂h )( dxk ∂h ) dxi ∂h S = dτ g ∓gij ∓gkl ± E 2 ik dτ ∂xj dτ ∂xl dτ ∂xi

For the class of configurations that interpolate from x(τ) = X at time τ → −∞ to x(τ) = Xa at time τ → +∞, the action is minimised for configurations that obey the instanton equations dxi ∂h = ±gij dτ ∂xj

Solutions to the equation with the + sign are instantons; those with the − sign are anti-instantons. The action is given by S = ±(h(X )−h(X ))

inst a b

Since we want the action to be positive definite, we should pick the instanton solution when h(X ) > h(X ) and the anti-instanton when h(X ) < h(X ).

a b a b

From our previous calculation in Section 2.3, we know that the fermion zero modes play a crucial role in supersymmetric instanton calculations. So our next question: how many fermi zero modes does our instanton have? To answer this, we look at the linearised fermion equation of motion. Here “linearised” means that we drop the Riemann tensor term in (3.14), and the connection term in ∇ . In Euclidean time, the linearised equations are dψi Dψi := +gij∇ ∂ hψk = 0 (3.19)

j k dτ

and dψ†i D†ψ†i := − +gij∇ ∂ hψ†k = 0 j k dτ

We want to know how many solutions each of these equations have in the background of an instanton. In fact, we really just want to know the difference between the number of solutions to these equations. This is because if both D and D† have zero modes then they will most likely be lifted by the non-linear terms in the action. And, indeed, generically, this will happen. However if there are unpaired zero modes of, say D†, then these must be saturated in some other way in the path integral. This prompts our interest in the index I(D) = dimKerD−dimKerD†

where KerD is the kernel of D, the space of solutions to Dψi = 0. Clearly, the index counts the number of unpaired zero modes of the instanton.

Furthermore, because our matrix element ⟨Ψ |[Q,h]|Ψ ⟩ contains just a single fermion ψ†, we’re only going to get non-zero contributions from instantons which have one more zero mode for ψ† than for ψ, namely I(D) = −1 or,equivalently I(D†) = +1

We’re always guaranteed to get some fermi zero modes from acting with broken supersymmetry. If we start from an instanton configuration, and originally set all fermions to zero, then acting with the supersymmetry transformations (3.15) (and remembering to Wick rotate to Eulidean time τ = it), we have δψi = ϵ ( −gij dxi ∂h )

dτ ∂xj δψ†i = −ϵ† ( +gij dxi ∂h )

dτ ∂xj

Because we want a ψ† zero mode, rather than a ψ zero mode, we should focus on configurations that obey dxi ∂h = gij (3.20)

dτ ∂xj

That is, we should focus on instantons rather than anti-instantons. This means that we should look at configurations that start, at τ → −∞ at X and end up at τ → +∞ at X , with h(X ) > h(X ). If we think of h(x) as a height function, these are trajectories that go up, rather than down.

a a b

Instantons and the Relative Morse Index

We’ve now played the “Grassmann integration” card twice: once in (3.18) to argue that we should get contributions only between vacua that have relative Morse index 1, and again above to argue that we should only get contributions from instantons with I(D†) = 1. Clearly we need these two different arguments to coincide. Happily they do because of the following result:

Claim: The index of D† is equal to the relative Morse index I(D†) = µ(X )−µ(X )

a b

Proof(ish): Here we give a sketch of the proof of this statement. The operator D, defined in (3.19), acts on an n-dimensional space of fermions ψi and takes the form D† = −Hess[h]

dτ

where Hess[h] is the n×n Hessian matrix Hess[h]i = gik∇ ∂ h j k j

When evaluated at the critical points x = X , this coincides with the Hessian that we previously used to define the Morse index. But the equation above provides an

Figure 11. An example of the spectral flow of eigenvalue Instantons between two vacua, albeit one in which creative licence has trumped mathematical precision. The level crossings shown above can occur but they are not generic. In a more typical trajectory, the order of eigenvalues remains the same under spectral flow.

We can extend the definition of the Hessian to each point along the instanton trajectory x(τ). As we move along this trajectory, the eigenvalues and orthonormal eigenvectors will smoothly evolve, Hess[h(τ)]eₖ(τ) = λₖ(τ)eₖ(τ) (3.21)

There is no sum over k = 1,...,n in this equation which labels the eigenvectors and eigenvalues. (The eigenvectors e have an additional i = 1,...,n index which is the vector index and is suppressed in the equation above.)

We can now follow the n eigenvalues λ as we move from one critical point to another. This is known as spectral flow, and an example is shown in Figure 11. The number of negative eigenvalues at τ = −∞ is the Morse index µ(X); the number of negative eigenvalues at τ = +∞ is µ(X).

Of particular interest are those eigenvalues which start negative and end up positive, or vice versa. The difference between those that cross in one direction, and those that cross in the other, is the relative Morse index µ(Xₐ)−µ(X_b). The example shown in Figure 11 has one more negative eigenvalue at the end than at the beginning which means that the corresponding instanton interpolates between two values with relative Morse index µ(Xₐ)−µ(X_b) = +1.

To solve the Dirac equation D†ψ = 0, we simply expand the fermions in terms of the eigenvectors, writing ψᵢ(τ) = ∑ₖ cₖ(τ)eᵢₖ(τ). We insert this ansatz into the Dirac equation and, using the orthogonality of eigenvectors gᵢⱼeᵢₖeⱼₗ = δₖₗ, we have d/dτ cₖ(τ) − λₖ(τ) cₖ(τ) = −∑ₗ gᵢⱼeᵢₖ ėⱼₗ cₗ(τ) (3.22)

with no sum over k. First, let’s suppose that we can ignore the term on the right-hand side. Then the equation has a straightforward solution, cₖ(τ) = Aₖ exp( +∫ dτ′ λₖ(τ′) )

But this is a normalisable solution to the Dirac equation only if λ(τ) < 0 for τ → +∞ and λ(τ) > 0 for τ → −∞. That is, we get a solution for every eigenvalue that flips from positive to negative. Meanwhile, the same analysis shows that every eigenvalue that goes the other way, from negative to positive, gives a solution to Dψ = 0. This is precisely what we wanted to show, namely I(D†) = µ(Xₐ)−µ(X_b)

That leaves us with the question of why it’s legal to ignore the term on the right-hand side of (3.22). This is where we get to the “ish” part of proofish. The term captures how the eigenvectors twist as we move along the instanton trajectory due to the Levi-Civita connection. (In (3.22), this takes the form of a Berry connection.) This connection doesn’t introduce any further topology into the game and it is a true fact that it doesn’t change the index, albeit not a fact that I will demonstrate here. In acknowledgement of this slipshod approach, I’ll replace the traditional QED box used at the end of a proof with something more wonky.

It turns out that for background configurations with I(D†) > 0 we generically have KerD = 0, so that I(D†) = dimKerD†. (For example, the situation shown in Figure 11 is not generic.) We will assume that this is the case moving forwards.

The calculation above also tells us about the bosonic collective coordinates of an instanton. Suppose that we find a solution x(τ) to the instanton equation (3.20). To see if this solution has any collective coordinates, we can look at variations x(τ)+δx(τ) and see if δx(τ) satisfies the linearised instanton equation, δxⁱ − gⁱʲ∇ₖ ∂ⱼh δxᵏ = 0 But this coincides with the Dirac equation D†δx = 0 whose solutions we’ve just counted. The upshot is that the number of bosonic collective coordinates is equal to the number of fermi zero modes, and both are counted by the relative Morse index. A slicker way of saying this is to note that bosonic and fermionic zero modes are related by the unbroken supersymmetry Q† in the background of an instanton.

For our purposes, we want to consider instantons that interpolate between critical points with relative Morse index 1. Here the sole bosonic collective coordinate is the obvious one: the time τ at which the instanton does its business of interpolating from one critical point to the other. This is the collective coordinate that we met previously in Section 2.2.

Although not of immediate utility, we can also get a feel for where the other bosonic collective coordinates may come from when ∆µ > 1. Consider the height Morse function on the round sphere S2. We know that there are two critical points at the south and north pole with Morse index 0 and 2 respectively. Correspondingly, the instanton that interpolates from the south to the north pole has two collective coordinates: one is the time τ at which the instanton makes the jump, the other is the angle ϕ of the trajectory as shown in the figure. In this example, the second collective coordinate is obvious because it arises due to a symmetry. But the arguments above tell us that, perhaps surprisingly, this second collective coordinate persists even when we deform the sphere, or potential, so that there’s no longer a rotational symmetry.

Completing the Instanton Computation The rest of our instanton computation proceeds in exactly the same manner as that of Section 2.3. Our final answer is the obvious generalisation (2.41): for vacua |Ψₐ⟩ and |Ψ_b⟩, whose Morse index differs by 1, we have ⟨Ψₐ|Q|Ψ_b⟩ = ∑_γ (e^{-S_{inst}} / √{2π}) n_γ (3.23)

Here the sum is over all distinct instantons γ and n_γ = ±1 is a sign that comes from computing the determinants n_γ = √(detD / detD†D) = ±1

We met this sign before in Section 2.3 where we confessed that it is a little tricky to fix. Now it is time to make good on our promise of explaining where it comes from.

Let’s start in the vacuum |Ψₐ⟩ localised at the end of the instanton trajectory at Xₐ. There are µ(Xₐ) negative eigenvalues of the Hessian and their eigenvectors span a µ(Xₐ)-dimensional space that we call Vₐ. The ground state |Ψₐ⟩ is associated to a µ(Xₐ)-form and this induces an orientation on Vₐ.

The tangent to the instanton trajectory at Xₐ lies in the space Vₐ of negative eigenvectors. Let us call this tangent vector v. Generically, v will coincide with the eigenvector with largest negative eigenvalue λₖ (or smallest |λₖ|) since this is usually the unique direction for which the eigenvalue flips sign by the time we reach Xₐ at the bottom. We denote the subspace of Vₐ that is orthogonal to v as Vₐ. There is a natural orientation on Vₐ that comes from taking the interior product ι_v Ψₐ.

Now we propagate the space Vₐ along the instanton trajectory γ. We can do this, for example, by following the eigenvectors eₖ(τ) of (3.21) corresponding to those eigenvalues that remain negative along the entire journey.

By the time we reach the end of the trajectory, the orientation on Vₐ that we started with gives an orientation on V_b, the space of negative eigenvectors of the Hessian at X_b. But there is a different way to define an orientation on V_b, which is that induced by the ground state |Ψ_b⟩ or, more precisely, the corresponding µ(X_b)-form. The question is: do these two ways of defining an orientation coincide? If they do, we take n_γ = 1. If they do not, we take n_γ = −1.

For example, consider again the deformed bean-shaped sphere shown in Figure 12. There are two instanton trajectories that interpolate from the minimum X_b at the bottom to the saddle point Xₐ in the middle. At Xₐ, the tangent vectors to the two different instanton trajectories point in different directions, and that means that each instanton trajectory induces opposite orientations ι_v Ψₐ on Vₐ. Correspondingly, one instanton will have n_γ = +1 and the other n_γ = −1, and the two cancel out in (3.23).

This same argument explains why the ground states are not lifted for the double well on a circle that we discussed in Section 2.3.4.

3.2.2 The Morse-Witten Complex

Let’s recap. A Morse function gives us a collection of critical points. There are m critical points Xₐ with Morse index p = µ(Xₐ) and, associated to each, there is an energy eigenstate |Ψₐ⟩ and an associated p-form. These can be thought of as a basis for an m_p-dimensional space that we will call C_p.

Not all the energy eigenstates |Ψₐ⟩ have vanishing energy or, equivalently, not all of them are annihilated by Q. But, as we saw in Section 2.3, they all have energy that is, at most, of order e^{-S_{inst}}. The tunnelling calculation that we’ve just done shows that, ⟨Ψₐ|Q|Ψ_b⟩ = ∑_γ (e^{-S_{inst}} / √{2π}) n_γ   whenever µ(Xₐ)−µ(X_b) = 1

If we think about Q as acting within this space of states, we can insert an “almost resolution” of the identity 1 ≈ ∑ₐ |Ψₐ⟩⟨Ψₐ| to get Q|Ψ_b⟩ = ∑ₐ ⟨Ψₐ|Q|Ψ_b⟩ |Ψₐ⟩ = ∑ₐ ∑_γ (n_γ / √{2π}) e^{-(h(Xₐ)−h(X_b))} |Ψₐ⟩ Here the “almost resolution” of 1 is because we’ve neglected all higher energy states. But their overlap with the low lying states |Ψₐ⟩ is exponentially suppressed and can be ignored. This means that we’re left with an expression for the action of Q among the critical points. Neither the factor of 2π, nor the instanton action, are important for our present purposes and can be absorbed into the normalisation of the states. We then have Q|Ψ_b⟩ = ∑ₐ ∑_γ n_γ |Ψₐ⟩ (where the sum is over a with µₐ=µ_b+1 and over γ)

This is a map Q : C_p → C_{p+1}. More abstractly, it can be viewed as a map between spaces of critical points. And, importantly, it satisfies Q² = 0. This means that we can define a chain complex (strictly a cochain complex), known as the Morse-Witten complex, or sometimes the Morse-Smale-Witten complex 0 → C_0 →^Q C_1 →^Q ... →^Q C_n →^Q 0

The cohomology of Q describes the E = 0 ground states.

tates of the system or, equivalently, the Betti numbers.

As an example we can look once again at the bean shaped manifold shown in Figure 13. We’ve already seen that the two instantons taking us from X to X cancel out, leaving us with

Q|Ψ₃⟩ = 0

This means that |Ψ₃⟩ is a true ground state of the system. There are also two instanton trajectories emanating from X₃, one to each of the peaks at X₁ and X₂. These trajectories have different orientations, meaning

Q|Ψ₃⟩ = |Ψ₁⟩ − |Ψ₂⟩

Finally, we have Q|Ψ₁⟩ = Q|Ψ₂⟩ = 0 as both states are top forms. The true ground states lie in Q-cohomology and there are two of them: the 0-form |Ψ₃⟩ and the 2-form |Ψ₁⟩ + |Ψ₂⟩. This reproduces the cohomology of S².

## 3.3 The Atiyah-Singer Index Theorem

We now turn to a second application of supersymmetric quantum mechanics. We will study a version of supersymmetric quantum mechanics that yields the Atiyah-Singer index theorem. Before introducing the physics, we first explain what problem the index theorem addresses.

In n dimensions, where n is even, a Dirac spinor χ has 2^{n/2} components. In flat space, the free Dirac equation reads

∂̸χ = γ^a ∂_a χ = 0  (3.24)

Here the gamma matrices obey the usual Clifford algebra

{γ^a, γ^b} = 2δ^{ab}, a,b = 1,...,n  (3.25)

The only solutions to (3.24) are constant spinors. That’s a bit boring and, in Rⁿ, more than a bit non-normalisable. Things get more interesting when the fermion lives on a curved manifold M. To describe this situation, we first introduce vielbeins

e^i_a e^j_b g_{ij} = δ_{ab}

The i,j indices are raised and lowered using the metric g_{ij} while the tangent space indices a,b are raised and lowered using δ_{ab}. (See the lectures on General Relativity for more details.) The Dirac equation then takes the form

D̸χ = γ^a e^i_a D_i χ = 0  (3.26)

with the covariant derivative given by

D_i = ∂_i + (ω_i)^{bc} S_{bc}  (3.27)

Here S_{ab} are the generators of SO(n) (strictly Spin(n)) in the spinor representation

S_{ab} = [γ_a, γ_b]

Meanwhile (ω_i)^{ab} is the spin connection, defined by

(ω_i)^a_b = Γ^a_{cb} e^c_j + e^j_a ∇_i e^j_b

We can then ask: how many solutions are there to the Dirac equation (3.26)? This is where the Atiyah-Singer index theorem comes in. It relates the number of solutions to the Dirac equation to the topology of the underlying manifold. The purpose of this section is to give a physics derivation of the index theorem from supersymmetric quantum mechanics.

3.3.1 The N = 1 Sigma Model

Our quantum mechanics of choice has half the supersymmetry of the models that we’ve considered until now in this section. That is, we will have N = 1 supersymmetry with a single real supercharge Q. We met some simple theories of this kind already in Section 1.4.3.

With N = 1 supersymmetry, the sigma model action (3.6) is replaced by something that, at first glance, appears much simpler,

L = ∫ dt [ (1/2) g_{ij} ẋ^i ẋ^j + (i/2) g_{ij} ψ^i ∇_t ψ^j ]  (3.28)

The key difference is that the Grassmann variables are now Majorana modes

ψ^†_i = ψ_i

We no longer have the Riemann tensor interaction term, but the Levi-Civita connection still shows up, as before, in the kinetic term for the fermions,

∇_t ψ_i = dψ_i/dt + Γ_{jk}^i ψ_k dx^j/dt  (3.29)

Although the action (3.28) has fewer interaction terms, it also has less symmetry. In particular, because the fermions are real we no longer have the U(1) symmetry that rotated the phase of the fermions. For our N = 2 sigma model (3.6), this symmetry ensured that the energy eigenstates had a fixed number, p, of excited fermions. Now that we no longer have this symmetry, we expect the energy eigenstates to involve a mixture of different fermions. The only protection we have comes from the (−1)^F symmetry that categorises states into H_B with an even number of fermions and H_F with an odd number.

We’ve already seen in Section 1.4.3 what emerges when we quantise the fermions so we will be brief here. The canonical anti-commutation relations are

{ψ_i, ψ_j} = g_{ij}

which is closely related to the Clifford algebra (3.25): the relationship between the fermions and gamma matrices involves a vielbein to accommodate the presence of the metric: ψ_i = e^i_a γ_a. This is telling us that, upon quantisation, the fermions will give 2^{n/2} states which can be viewed as a Dirac spinor χ living on the manifold M. While quantisation of the N = 2 sigma model (3.6) gave us p-forms over the manifold, now we have a spinor.

The action (3.28) is invariant under the supersymmetry transformations

δx^i = ε ψ^i and δψ^i = −ε ẋ^i

with the associated supercharge

Q = g_{ij} ψ^i ẋ^j

The ground states of the quantum mechanics once again obey Q|χ⟩ = 0. We can ask how this equation translates into the geometric language. The answer is clear: the fermion ψ_i in the supercharge is replaced by a gamma matrix, while the mechanical momentum ẋ^i is replaced by the appropriate covariant derivative, so that Q = iD̸. The upshot is that ground states of the quantum mechanics are given by solutions to the Dirac equation

D̸χ = 0  (3.30)

where the covariant derivative is (3.27), as appropriate for a spinor on a curved manifold M. The Hamiltonian is then H = Q² = −D̸².

We can now see why this quantum mechanics is of interest. The ground states are specified by solutions to the Dirac equation which is exactly what we want to count. Moreover, we know how to count ground states in supersymmetric quantum mechanics, at least up to sign: we use the Witten index.

To get an expression for the index, we first need to figure out which states sit in H_B and which in H_F. As we already saw in Section 1.4.3, this has a particularly nice interpretation in terms of the spinor. Because we are in an even dimension n, the Dirac spinor decomposes into two Weyl spinors which are eigenspinors of

γ̂ = i^{n/2} γ^1...γ^n

This obeys γ̂² = 1 and {γ̂, γ^i} = 0, and is the generalisation of the “γ₅” matrix in four dimensions. This is the operator that determines whether a given state lies in H_B or H_F via the identification

γ̂ = (−1)^F

We can always pick a basis of gamma matrices that are block off-diagonal, so that we have

γ̂ = ( 1   0 ; 0  -1 )

where each entry is a 2^{n/2−1} dimensional matrix. The Dirac operator then takes the form

D̸ = ( 0   D† ; D   0 )

where D : H_B → H_F and D† : H_F → H_B. The Witten index coincides with the index of the operator D,

Tr(−1)^F e^{−βH} = I(D) := dim Ker D − dim Ker D†  (3.32)

This is also the quantity of relevance to the Atiyah-Singer index theorem. Our next task is to compute it. But, by now, our strategy for this should be clear: we turn to the path integral.

3.3.2 The Path Integral Again

The same argument that we used in Section 3.1.3 when deriving the Chern-Gauss-Bonnet theorem tells us that the path integral localises on constant configurations ẋ^i = ψ̇^i = 0. We’ll pick a constant configuration and expand

x^i(τ) = x^i_0 + δx^i(τ) and ψ_i(τ) = ψ_i^0 + δψ_i(τ)

We then compute the path integral by performing a Gaussian integration over the fluctuations δx and δψ. Our life is made easier if we work in normal coordinates in which

g_{ij}(x) = δ_{ij} − (1/3) R_{ikjl}(x_0) δx^k δx^l

and

δΓ^i_{jk}(x) = ∂_l Γ^i_{jk}(x_0) δx^l = −(1/3)(R^i_{jkl}(x_0) + R^i_{kjl}(x_0)) δx^l

To quadratic order, the Euclidean action then becomes

S_E = ∫ dτ [ (1/2) δ_{ij} δẋ^i δẋ^j + δψ_i (d/dτ) ψ_j^0 − (1/2) R_{ijkl}(x_0) ψ_i^0 ψ_j^0 δx^k (dδx^l/dτ) ]

Performing the Gaussian integral with periodic boundary conditions, we have

Z = ∫ Dδx Dδψ e^{−S_E} = [ det'(δ_{ij} ∂_τ) ]^{1/2} / [ det'(-δ_{ij} ∂²_τ + Ω_{ij} ∂_τ) det'(-δ_i^j ∂_τ + Ω_i^j) ]^{1/2} = [ det'(−δ_{ij} ∂²_τ + Ω_{ij} ∂_τ) det'(−δ_i^j ∂_τ + Ω_i^j) ]^{-1/2}

The fermionic determinant in the numerator now sits under square root, reflecting the fact that the fermions are real. (It could be better thought of as a Pfaffian.) Both determinants have had their zero modes truncated since these correspond to the integrals over x^0 and ψ^0, both of which we will do explicitly below.

After the small cancellation seen above, we’re left with the task of computing the determinant operator involving the matrix

Ω_i^j := δ^{jp} R_{pklm}(x_0) ψ^k_0 ψ^l_0  (3.33)

This should be thought of as an n×n matrix that depends both on the point x_0 and on the background fermion ψ^0. (It may seem odd to think about a matrix as depending on a background Grassmann parameter like ψ^0; the meaning of this should become clearer below when we think about what we’re going to do with this matrix.) This is an anti-symmetric matrix and we can choose a basis in which it takes block diagonal form

Ω_i^j = diag( W, ..., W ), with W = ( 0 ω_a ; -ω_a 0 )

The eigenvalues are ±iω_a and these depend on both x_0 and on ψ^0. We can also diagonalise the derivative term simply by working in a Fourier basis around the circle. Since we know that the end result for the Witten index must be independent of β, we’ll take advantage of this and work with β = 1. We then have

δx^i(τ) ∼ e^{ikτ} with k = 2πp and p ∈ Z

This means that the eigenvalues of the bosonic fluctuation operator are i(k ± ω_a). Restricting to any given 2×2 matrix W, we have

det'(−∂_τ + W) = ∏_{p≠0} (2πip + iω)^{1/2} (2πip − iω)^{1/2} = ∏_{p=1}^∞ [ (2πip)² (1 + (iω / 2πp)²) ]

We’ve met each of these products before. The second, convergent product is given by (2.6)

∏_{p=1}^∞ (1 + (iω / 2πp)²) = sinh(iω/2) / (iω/2)

The first, divergent, product can be treated using zeta function regularisation as in (2.7) and gives

∏_{p=1}^∞ (2πip)² = −i

Putting this together, we have an expression for the partition function after integrating over the fluctuations,

Z = (−i)^{n/2} ∏_{a=1}^{n/2} [ iω_a / 2 ] / sinh(iω_a / 2)

We’re now left just with the zero mode integrations: including these gives us the expression for the Witten index and hence the index of the Dirac operator

I(D) = (−i)^{n/2} ∫ ∏_{i=1}^n (dx^i_0 / √(2π)) ∏_{j=1}^n dψ_j^0 ∏_{a=1}^{n/2} [ iω_a / 2 ] / sinh(iω_a / 2)

The next step is to do the fermion zero mode integration. The idea here is that each ω_a depends quadratically on the fermion zero modes. We should expand each term in the product,

ω/2 / sinh(ω/2) = (ω/2) / (ω/2 + (ω/2)^3/6 + ...) = 1 / (1 + ω²/24 + ...) ≈ 1 − ω²/24 + ...

Because the function is even, the expansion contains only even powers of ω and hence the fermionic variables ψ come in groups of four. The fermionic integration picks out the term that saturates the Grassmann integration. We learn that the index I(D) will be non-vanishing only on manifolds whose dimension n is a multiple of four. (This also eliminates the factors of i in the expression for I(D).)

There is a more geometric way to think about this. Instead working with fermions, we turn again to forms. (The fact that our fermions don’t yield forms upon quantisation is irrelevant here: this is just a formal trick.) We introduce the curvature 2-form R_ab = R_{abcd} θ̂^c ∧ θ̂^d where θ̂ = e_a dx^i are a basis of one-forms. (see the lectures on General Relativity for more details.) Clearly R has the same formal structure as the fermionic matrix Ω that we met before. This means that we can equally well write I(D) = A(M) with A(M) = ∫ det(1/2 R / sinh(1/2 R))^{1/2} (2π)^{-n/2}. This is the Atiyah-Singer index theorem. The expression A(M) is referred to as the A-roof genus or A-hat genus of M (or, more correctly, the tangent bundle of M). The expression should be viewed as expanding out the determinant until we find a top form that can be integrated over the manifold M. The terms that appear in this expansion are Â(M) = ∫ 1 - (1/24)p_1 + (7/16)p_1^2 - (1/360)p_2 + ... where the various terms in the expansion arise for manifolds of dimension n = 0,4,8 and so on. The p are known as Pontryagin numbers and can be expressed as integrals of the curvature 2-form over the manifold M. For a manifold of dimension dim(M) = 4, we have Â(M) = -p_1/24 with p_1 = -1/(8π^2) ∫ tr R^2 (3.34). The simplest examples of 4-manifolds are the torus and sphere, which have p_1(T^4) = p_1(S^4) = 0. This tells us that the index of the Dirac operator vanishes. For the torus T^4, with periodic boundary conditions for spinors, this is because both D and D† have zero modes. For the sphere S^4, it is because there are no zero modes.

To find a compact manifold M with p_1 ≠ 0, we need to turn to something more exotic. A nice example is provided by the manifold known as M = K3, which can be viewed as a smooth quartic surface in CP^3. This is the only non-trivial Calabi-Yau 4-manifold and has p_1(K3) = -48.

The factor of 1/24 in (3.34) is telling us something interesting. Because the left-hand side is counting something, the right-hand-side must be an integer. This suggests that the integral p_1 must be a multiple of 24. In fact, things are a little more subtle. The thing that we’re counting is the number of solutions to the Dirac equation and to pose this question at all, we must be able to put Dirac spinors on the manifold M. This, it turns out, is not possible for all manifolds. Those for which is is possible are called spin manifolds. And for any orientable spin manifold, it turns out that p_1 is always divisible by 48.

The canonical example of a non-spin 4-manifold is complex projective space CP^2. It’s not possible to consistently patch spinor fields over this space, and so the question of counting solutions to the Dirac equation is irrelevant. It turns out that p_1(CP^2) = 3. Moreover, one can show that for any orientable 4-manifold, p_1 is always divisible by 3.

For manifolds with dimM = 8, we need the result p_2 = 1/(128π^4) ∫ (tr R^2)^2 - 2 tr R^4. There are generalisations to higher dimensional manifolds.

3.3.3 Adding a Gauge Field

There is an interesting generalisation of the action (3.28) that retains N = 1 supersymmetry. This is L = ∫ dt [ (1/2) g_{ij} ẋ^i ẋ^j + (i/2) ψ^i ∇_t ψ_j + i η^†_α D_t η^α + (1/2) (F)_{ij}^β α η^†_η^β ψ^i ψ^j ] (3.35) with i,j = 1,...,n as before and α,β = 1,...,r. Here the ψ^i are Majorana fermions, with covariant derivative given by the same expression (3.29) that we had before. Meanwhile, the η are complex fermions with covariant derivative D_t η^α = dη^α/dt + (A_i)^α β (dx^i/dt) η^β. We should think of A as a U(r) gauge connection over the manifold M. Just as the metric g_{ij} is something fixed, so too is this gauge field. In more mathematical language, we should think of A as a connection of a vector bundle E. In the action (3.35) F is the associated field strength (F_{ij})^α β = ∂_i (A_j)^α β - ∂_j (A_i)^α β + [A_i , A_j]^α β. Note that the four-fermion term involves F, which is the curvature of A. This entirely analogous to the situation in N = 2 supersymmetric quantum mechanics where the four-fermion term involves the Riemann tensor, which is the curvature of the spin connection.

At first glance, it is surprising that the action (3.35) admits supersymmetry. Until now, all our examples of supersymmetry involve a matching between bosonic and fermionic degrees of freedom. But here we have introduced additional fermionic degrees of freedom η^α without the corresponding bosonic partners. Nonetheless, you can check that the action is invariant under the following N = 1 supersymmetry, δx^i = εψ^i, δψ^i = -εẋ^i, δη^α = -εψ^i (A_i)^α β ψ^β. Together with the conjugate expression δη^†_β = εη^†_β (A_i)^α β ψ^i. It turns out that adding extra fermions, without bosonic counterparts, is an option only for supersymmetric theories in d = 0+1 and d = 1+1 dimensions.

How should we think about the theory (3.35). Quantising the real fermions ψ^i gives us a spinor over M as before. Quantising the complex fermions η^α gives us forms, but they’re not forms over the manifold M since they don’t carry the i = 1,...,n index. Instead, they are forms over the gauge bundle E. In more mundane language, this simply means that the states transform in different representations of the U(r) gauge connection. Ignoring the ψ^i fermions for now, we start with the state |0⟩ such that η^α|0⟩ = 0. This is a singlet (i.e. neutral) under the U(r) gauge bundle. Next, we have η^†_α|0⟩ which sit in the fundamental representation of U(r), and the η^†_αη^†_β|0⟩ which sits in the anti-fundamental representation, and so on. Furthermore, there is a U(1) symmetry that rotates η^α → e^{iθ}η^α and this ensures that energy eigenstates have fixed number of η^† excitations and so sit in a fixed representation of U(r).

The upshot is that the Hilbert space consists of a collection of spinors over M, each transforming in the pth antisymmetric representation of U(r). The E = 0 ground states obey Q|χ⟩ = 0 which, translated into the geometric language, becomes the Dirac equation D/χ = 0 with D = ∂_i + (ω_i)_{bc} S^{bc} + A_i with A in the appropriate representation. Once again, this can be put in block off-diagonal form (3.31) and we can compute the index I(D) which, as in (3.32), coincides with the Witten index. Restricting to the fundamental representation, a similar calculation to the one above now yields the Atiyah-Singer index theorem I(D) = ∫ A(M) ∧ ch(F) (3.36) where F it the Chern character, ch(F) = Tre^{F/2π} = r + c_1(F) + c_2(F) + ... The individual Chern classes are topological invariants of the gauge field when integrated over the manifold M. The first two are c_1 = TrF/(2π) and c_2 = 1/(8π^2) [TrF ∧ F - TrF ∧ TrF]. There are close connections here to the physics of solitons. In particular, the integral of the first Chern number counts the number of vortices in a gauge theory. The integral of the second Chern number counts the number of Yang-Mills instantons. Both of these have an interesting zero mode structure, even in flat spacetime, as follows from the Atiyah-Singer index theorem (3.36).

## 3.4 What Comes Next?

We have barely scratched the surface of supersymmetric theories and their connection to mathematics. In this final section we give a brief sketch of the next steps. Roughly speaking, there are two directions that are particularly rich: increase the number of supersymmetries, and increase the spacetime dimension of the quantum theory.

First the supersymmetries. The stories we told above revolved around N = 2 supersymmetry (for Morse theory) and N = 1 supersymmetry (for the index theorem). We briefly met theories with N = 4 supersymmetry in Section 1.4.2 where we saw that they naturally come with complex fields and a holomorphic superpotential. This suggests that a sigma model with N = 4 supersymmetry should have a target space M that is, in some sense, a complex manifold.

This is indeed what happens. Sigma models with N = 4 supersymmetry have target spaces that are Kähler. These target spaces necessarily have even dimension, with coordinates that can be paired together into complex numbers consistently over the entire manifold. This structure is best seen through the introduction of superfields, where the kinetic terms in the Lagrangian are written directly in terms of a function known as the Kähler potential K(ϕ,ϕ̄) that is related to the metric by g_{i¯j} = 2 ∂^2 K / ∂ϕ^i ∂ϕ̄^j (3.37). Superfields and the Kähler potential are both described in the accompanying lectures on Supersymmetric Field Theory.

More supersymmetry brings yet more structure to the geometry, at least to a point. There are theories with N = 8 supersymmetry whose target spaces are hyperKähler. Such manifolds have a dimension that is a multiple of four, with three inequivalent ways of pairing coordinates together into complex numbers. It’s a little like having a quaternionic structure on the manifold (although beware that there is a different kind of object in mathematics known as a “quaternionic manifold”). However, the interesting things don’t keep happening forever and by the time we get to N = 16 supersymmetry the restriction becomes too strong and the target space is obliged to be flat and largely boring.

The full riches of supersymmetry really come when we consider theories in higher dimensions, meaning quantum field theories rather than quantum mechanics. While there are interesting stories for field theories in any spacetime dimension d ≤ 6 (and, if you include gravitational theories, for d ≤ 11) there is, as I now explain, a reason why QFTs in d = 1+1 dimensions are special.

Consider a sigma model in d spacetime dimensions. We introduce coordinates xµ, with µ = 0,1,...,d − 1 for spacetime. The action is again based on some target space M. This means that the fields ϕi(x), with i = 1,...,n should be thought of as coordinates on M. The sigma model takes the form S = ∫ddx gij(ϕ) ∂µϕi ∂µϕj +fermions (3.38)

Note that there are two conceptually different spaces in this action. The spacetime of the quantum field theory has dimension d, while the target space M has dimension dimM = n.

With no potential V(ϕ) to preference one point on the manifold M from another, this theory has many classical ground states: each point on M or, equivalently, each constant value of ϕi should be viewed as a different classical ground state of the system.

But what happens in the quantum theory? We’ve already seen that for d = 1, which is just quantum mechanics, the ground state wavefunction spreads over M. This is important as it means that the ground state knows something about the entire manifold M and may therefore encode some information about its topology. We’ve seen examples of this throughout these lectures.

What happens in higher dimensions with d > 1? It turns out that d = 2 is just like quantum mechanics: the ground state wavefunction spreads over the whole manifold M. Meanwhile, at least in this respect, quantum theories in dimensions d ≥ 3 behave like the classical theory: each point on M defines a different ground state.

I won’t prove this statement in these lectures. It sometimes goes by the name of the (Coleman)-Mermin-Wagner theorem and is closely related to the concept of a “lower critical dimension” in Statistical Field Theory. At heart, it boils down to a property of the Poisson equation ∇2ϕ = δ(x) in d Euclidean dimensions. At long distances, the solution grows in d = 1 and d = 2. (It is ϕ ∼ x in d = 1 and ϕ ∼ logx in d = 2.)

Conversely, the solution decays at long distance as ϕ ∼ 1/xd−2 in d ≥ 3. Physically, this translates into the fact that wavefunctions spread over M for sigma models with d = 1 and d = 2, while the ground state remains localised at a point in M for d ≥ 3.

This means that if we want to find some interesting physics that captures topological properties of M, we should first look at d = 1 and d = 2. We’ve now spent over 100 pages studying supersymmetric quantum mechanics. So the next step is to look at supersymmetric sigma models of the form (3.38) in d = 1+1.

There is a rather special feature of quantum field theories in d ≥ 2 dimensions that distinguishes them from quantum mechanics in d = 1: renormalisation. This means that the coupling constants that characterise a theory are not, in fact, constant. Instead they change with scale. Sigma models in d = 1+1 dimensions are no exception. Here, the couplings of the theory are encoded in the metric gij(ϕ). Under renormalisation, this metric changes and depends on the scale µ at which you look. The manner in which the metric changes is governed by the beautifully geometric beta function equation, known as Ricci flow ∂gij/∂µ = Rij (3.39)

This equation also plays an important role in String Theory, where it is ultimately responsible for the emergence of the Einstein equations of general relativity.

Taking into account the renormalisation (3.39), there are three types of behaviour that can occur depending on the type of target space M. Those spaces with positive Ricci curvature, R > 0, will shrink under RG flow. In this case, the theory becomes increasingly strongly coupled in the infra-red and the impact on the physics is rather dramatic with the seemingly massless scalars ϕi developing a quantum-generated mass.

Examples include M = Sn and M = CPn. You can read more about this in the lectures on Statistical Field Theory and the lectures on Gauge Theory.

Target spaces M with negative Ricci curvature, R < 0, will typically expand under RG flow. In this case they become more and more weakly coupled as the flow to the infra-red. Hyperbolic spaces provide a simple example.

The sweet spot are those target spaces M for which the metric is Ricci flat, with Rij = 0. In fact, rather wonderfully, you don’t have to start in the UV with a manifold M with a Ricci flat metric. If the manifold admits a Ricci flat metric, then the quantum theory will typically find it through the RG flow. The long-wavelength physics of such a theory is then governed by an interacting conformal field theory. Or, if we’re dealing with a supersymmetric sigma model, an interacting supersymmetric conformal field theory or SCFT for short.

At this point, there is again a lovely intersection with results from mathematics.

If we have N = 4 supersymmetry so that the target space is Kähler, then there is a famous class of compact manifolds M that admit a Ricci flat metric known as Calabi- Yau manifolds. (For what it’s worth, they are defined by having vanishing first Chern class.) Our discussion above means that for each Calabi-Yau manifold M there is an associated SCFT.

That, it turns out, is interesting. While the quantum mechanical sigma models described earlier in these lecture notes capture well-known stories of geometry, the d = 1 + 1 sigma models give a new lens through which to look at the manifolds M. And this lens gives us new information about the manifolds that goes beyond what mathematicians originally knew (although they very quickly caught up!) It is appropriate to refer to this view of the target space M, as seen by a SCFT, as “quantum geometry”.

There are many novelties that come from associating a SCFT to a Calabi-Yau manifold M. But one stands out. There is not a unique association between manifolds M and SCFTs. Instead, pairs of manifolds M and N turn out to give rise to the same SCFT. These two manifolds M and N are topologically distinct and, naively, one wouldn’t have thought that they have anything to do with each other. But, perhaps surprisingly, “quantum geometry” turns out to be more myopic than classical geometry and the SCFT approach cannot distinguish objects which appear obviously different to a classical geometer. At first glance, this myopia might appear to be a weakness, but closer examination shows that it is very much a strength. The myopia only arises because there are deep connections between the two manifolds M and N, with the geometric information of one encoded in a hidden and subtle form in the other. In technical language, the complex structure of one manifold is mapped to the symplectic structure of the other. This mapping is known as mirror symmetry. It is, sadly, a topic for another course.

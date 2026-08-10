# Principles of Quantum Mechanics R Shankar Z Library

> 来源文件：pre_Principles_of_Quantum_Mechanics_R_Shankar_Z_Library.txt
> 字符数（约）：259177
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Principles of Quantum Mechanics SECOND EDITION R. Shankar Yale University New Haven, Connecticut PLENUM PRESS NEW YORK AND LONDON

Library of Congress Cataloging—in—Publication Data Shankar, Ramamurti.

Principles of quantum mechanics / R. Shankar. -- 2nd ed.

p. cm.

Includes bibliographical references and index.

ISBN 0-306-44790-8

## 1. Quantum theory. I. Title

QC174.12.S52 1994 530.1'2--dc20 94-26837 CIP

## ISBN 0-306-44790-8

©1994, 1980 Plenum Press, New York A Division of Plenum Publishing Corporation 233 Spring Street, New York, N.Y. 10013 No part of this book may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, microfilming, recording, or otherwise, without written permission from the Publisher Printed in the United States of America

To My Parents and to Uma, Umesh, Ajeet, Meera, and Maya

Preface to the Second Edition

Over the decade and a half since I wrote the first edition, nothing has altered my belief in the soundness of the overall approach taken here. This is based on the response of teachers, students, and my own occasional rereading of the book. I was generally quite happy with the book, although there were portions where I felt I could have done better and portions which bothered me by their absence. I welcome this opportunity to rectify all that.

Apart from small improvements scattered over the text, there are three major changes. First, I have rewritten a big chunk of the mathematical introduction in Chapter 1. Next, I have added a discussion of time-reversal invariance. I don't know how it got left out the first time—I wish I could go back and change it. The most important change concerns the inclusion of Chapter 21, "Path Integrals: Part II." The first edition already revealed my partiality for this subject by having a chapter devoted to it, which was quite unusual in those days. In this one, I have cast off all restraint and gone all out to discuss many kinds of path integrals and their uses. Whereas in Chapter 8 the path integral recipe was simply given, here I start by deriving it. I derive the configuration space integral (the usual Feynman integral), phase space integral, and (oscillator) coherent state integral. I discuss two applications: the derivation and application of the Berry phase and a study of the lowest Landau level with an eye on the quantum Hall effect. The relevance of these topics is unquestionable. This is followed by a section of imaginary time path integrals—its description of tunneling, instantons, and symmetry breaking, and its relation to classical and quantum statistical mechanics. An introduction is given to the transfer matrix. Then I discuss spin coherent state path integrals and path integrals for fermions. These were thought to be topics too advanced for a book like this, but I believe this is no longer true. These concepts are extensively used and it seemed a good idea to provide the students who had the wisdom to buy this book with a head start.

How are instructors to deal with this extra chapter given the time constraints? I suggest omitting some material from the earlier chapters. (No one I know, myself included, covers the whole book while teaching any fixed group of students.) A realistic option is for the instructor to teach part of Chapter 21 and assign the rest as reading material, as topics for take-home exams, term papers, etc. To ignore it, I think, would be to lose a wonderful opportunity to expose the student to ideas that are central to many current research topics and to deny them the attendant excitement. Since the aim of this chapter is to guide students toward more frontline topics, it is more concise than the rest of the book. Students are also expected to consult the references given at the end of the chapter.

Over the years, I have received some very useful feedback and I thank all those students and teachers who took the time to do so. I thank Howard Haber for a discussion of the Born approximation; Harsh Mathur and Ady Stern for discussions of the Berry phase; Alan Chodos, Steve Girvin, Ilya Gruzberg, Martin Gutzwiller, Ganpathy Murthy, Charlie Sommerfeld, and Senthil Todari for many useful comments on Chapter 21. I thank Amelia McNamara of Plenum for urging me to write this edition and Plenum for its years of friendly and warm cooperation. Finally, I thank my wife Uma for shielding me as usual from real life so I could work on this edition, and my battery of kids (revised and expanded since the previous edition) for continually charging me up.

R. Shankar New Haven, Connecticut

Preface to the First Edition

Publish and perish—Giordano Bruno

Given the number of books that already exist on the subject of quantum mechanics, one would think that the public needs one more as much as it does, say, the latest version of the Table of Integers. But this does not deter me (as it didn't my predecessors) from trying to circulate my own version of how it ought to be taught. The approach to be presented here (to be described in a moment) was first tried on a group of Harvard undergraduates in the summer of '76, once again in the summer of '77, and more recently at Yale on undergraduates ('77-'78) and graduates ('78-'79) taking a year-long course on the subject. In all cases the results were very satisfactory in the sense that the students seemed to have learned the subject well and to have enjoyed the presentation. It is, in fact, their enthusiastic response and encouragement that convinced me of the soundness of my approach and impelled me to write this book.

The basic idea is to develop the subject from its postulates, after addressing some indispensable preliminaries. Now, most people would agree that the best way to teach any subject that has reached the point of development where it can be reduced to a few postulates is to start with the latter, for it is this approach that gives students the fullest understanding of the foundations of the theory and how it is to be used. But they would also argue that whereas this is all right in the case of special relativity or mechanics, a typical student about to learn quantum mechanics seldom has any familiarity with the mathematical language in which the postulates are stated. I agree with these people that this problem is real, but I differ in my belief that it should and can be overcome. This book is an attempt at doing just this.

It begins with a rather lengthy chapter in which the relevant mathematics of vector spaces is developed from simple ideas on vectors and matrices the student is assumed to know. The level of rigor is what I think is needed to make a practicing quantum mechanic out of the student. This chapter, which typically takes six to eight lecture hours, is filled with examples from physics to keep students from getting too fidgety while they wait for the "real physics." Since the math introduced has to be taught sooner or later, I prefer sooner to later, for this way the students, when they get to it, can give quantum theory their fullest attention without having to battle with the mathematical theorems at the same time. Also, by segregating the mathematical theorems from the physical postulates, any possible confusion as to which is which is nipped in the bud.

This chapter is followed by one on classical mechanics, where the Lagrangian and Hamiltonian formalisms are developed in some depth. It is for the instructor to decide how much of this to cover; the more students know of these matters, the better they will understand the connection between classical and quantum mechanics.

Chapter 3 is devoted to a brief study of idealized experiments that betray the inadequacy of classical mechanics and give a glimpse of quantum mechanics.

Having trained and motivated the students I now give them the postulates of quantum mechanics of a single particle in one dimension. I use the word "postulate" here to mean "that which cannot be deduced from pure mathematical or logical reasoning, and given which one can formulate and solve quantum mechanical problems and interpret the results." This is not the sense in which the true axiomatist would use the word. For instance, where the true axiomatist would just postulate that the dynamical variables are given by Hilbert space operators, I would add the operator identifications, i.e., specify the operators that represent coordinate and momentum (from which others can be built). Likewise, I would not stop with the statement that there is a Hamiltonian operator that governs the time evolution through the equation ih∂|ψ⟩/∂t = H|ψ⟩; I would say the H is obtained from the classical Hamiltonian by substituting for x and p the corresponding operators. While the more general axioms have the virtue of surviving as we progress to systems of more degrees of freedom, with or without classical counterparts, students given just these will not know how to calculate anything such as the spectrum of the oscillator. Now one can, of course, try to "derive" these operator assignments, but to do so one would have to appeal to ideas of a postulatory nature themselves. (The same goes for "deriving" the Schrödinger equation.) As we go along, these postulates are generalized to more degrees of freedom and it is for pedagogical reasons that these generalizations are postponed. Perhaps when students are finished with this book, they can free themselves from the specific operator assignments and think of quantum mechanics as a general mathematical formalism obeying certain postulates (in the strict sense of the term).

The postulates in Chapter 4 are followed by a lengthy discussion of the same, with many examples from fictitious Hilbert spaces of three dimensions. Nonetheless, students will find it hard. It is only as they go along...

ng and see these postulates used over and over again in the rest of the book, in the setting up of problems and the interpretation of the results, that they will catch on to how the game is played. It is hoped they will be able to do it on their own when they graduate. I think that any attempt to soften this initial blow will be counterproductive in the long run.

Chapter 5 deals with standard problems in one dimension. It is worth mentioning that the scattering off a step potential is treated using a wave packet approach. If the subject seems too hard at this stage, the instructor may decide to return to it after Chapter 7 (oscillator), when students have gained more experience. But I think that sooner or later students must get acquainted with this treatment of scattering.

The classical limit is the subject of the next chapter. The harmonic oscillator is discussed in detail in the next. It is the first realistic problem and the instructor may be eager to get to it as soon as possible. If the instructor wants, he or she can discuss the classical limit after discussing the oscillator.

We next discuss the path integral formulation due to Feynman. Given the intuitive understanding it provides, and its elegance (not to mention its ability to give the full propagator in just a few minutes in a class of problems), its omission from so many books is hard to understand. While it is admittedly hard to actually evaluate a path integral (one example is provided here), the notion of expressing the propagator as a sum over amplitudes from various paths is rather simple. The importance of this point of view is becoming clearer day by day to workers in statistical mechanics and field theory. I think every effort should be made to include at least the first three (and possibly five) sections of this chapter in the course.

The content of the remaining chapters is standard, in the first approximation. The style is of course peculiar to this author, as are the specific topics. For instance, an entire chapter (11) is devoted to symmetries and their consequences. The chapter on the hydrogen atom also contains a section on how to make numerical estimates starting with a few mnemonics. Chapter 15, on addition of angular momenta, also contains a section on how to understand the "accidental" degeneracies in the spectra of hydrogen and the isotropic oscillator. The quantization of the radiation field is discussed in Chapter 18, on time-dependent perturbation theory. Finally the treatment of the Dirac equation in the last chapter (20) is intended to show that several things such as electron spin, its magnetic moment, the spin-orbit interaction, etc. which were introduced in an ad hoc fashion in earlier chapters, emerge as a coherent whole from the Dirac equation, and also to give students a glimpse of what lies ahead. This chapter also explains how Feynman resolves the problem of negative-energy solutions (in a way that applies to bosons and fermions).

For Whom Is this Book Intended?

In writing it, I addressed students who are trying to learn the subject by themselves; that is to say, I made it as self-contained as possible, included a lot of exercises and answers to most of them, and discussed several tricky points that trouble students when they learn the subject. But I am aware that in practice it is most likely to be used as a class text. There is enough material here for a full year graduate course. It is, however, quite easy to adapt it to a year-long undergraduate course. Several sections that may be omitted without loss of continuity are indicated. The sequence of topics may also be changed, as stated earlier in this preface. I thought it best to let the instructor skim through the book and chart the course for his or her class, given their level of preparation and objectives. Of course the book will not be particularly useful if the instructor is not sympathetic to the broad philosophy espoused here, namely, that first comes the mathematical training and then the development of the subject from the postulates. To instructors who feel that this approach is all right in principle but will not work in practice, I reiterate that it has been found to work in practice, not just by me but also by teachers elsewhere.

The book may be used by nonphysicists as well. (I have found that it goes well with chemistry majors in my classes.) Although I wrote it for students with no familiarity with the subject, any previous exposure can only be advantageous.

Finally, I invite instructors and students alike to communicate to me any suggestions for improvement, whether they be pedagogical or in reference to errors or misprints.

Acknowledgments As I look back to see who all made this book possible, my thoughts first turn to my brother R. Rajaraman and friend Rajaram Nityananda, who, around the same time, introduced me to physics in general and quantum mechanics in particular. Next come my students, particularly Doug Stone, but for whose encouragement and enthusiastic response I would not have undertaken this project. I am grateful to Professor Julius Kovacs of Michigan State, whose kind words of encouragement assured me that the book would be as well received by my peers as it was by my students. More recently, I have profited from numerous conversations with my colleagues at Yale, in particular Alan Chodos and Peter Mohr. My special thanks go to Charles Sommerfield, who managed to make time to read the manuscript and made many useful comments and recommendations. The detailed proofreading was done by Tom Moore. I thank you, the reader, in advance, for drawing to my notice any errors that may have slipped past us.

The bulk of the manuscript production cost were borne by the J. W. Gibbs fellowship from Yale, which also supported me during the time the book was being written. Ms. Laurie Liptak did a fantastic job of typing the first 18 chapters and Ms. Linda Ford did the same with Chapters 19 and 20. The figures are by Mr. J. Brosious. Mr. R. Badrinath kindly helped with the index.

On the domestic front, encouragement came from my parents, my in-laws, and most important of all from my wife, Uma, who cheerfully donated me to science for a year or so and stood by me throughout. Little Umesh did his bit by tearing up all my books on the subject, both as a show of support and to create a need for this one.

R. Shankar New Haven, Connecticut

Prelude Our description of the physical world is dynamic in nature and undergoes frequent change. At any given time, we summarize our knowledge of natural phenomena by means of certain laws. These laws adequately describe the phenomenon studied up to that time, to an accuracy then attainable. As time passes, we enlarge the domain of observation and improve the accuracy of measurement. As we do so, we constantly check to see if the laws continue to be valid. Those laws that do remain valid gain in stature, and those that do not must be abandoned in favor of new ones that do.

In this changing picture, the laws of classical mechanics formulated by Galileo, Newton, and later by Euler, Lagrange, Hamilton, Jacobi, and others, remained unaltered for almost three centuries. The expanding domain of classical physics met its first obstacles around the beginning of this century. The obstruction came on two fronts: at large velocities and small (atomic) scales. The problem of large velocities was successfully solved by Einstein, who gave us his relativistic mechanics, while the founders of quantum mechanics—Bohr, Heisenberg, Schrödinger, Dirac, Born, and others--solved the problem of small-scale physics. The union of relativity and quantum mechanics, needed for the description of phenomena involving simultaneously large velocities and small scales, turns out to be very difficult. Although much progress has been made in this subject, called quantum field theory, there remain many open questions to this date. We shall concentrate here on just the small-scale problem, that is to say, on non-relativistic quantum mechanics.

The passage from classical to quantum mechanics has several features that are common to all such transitions in which an old theory gives way to a new one: (1) There is a domain D, of phenomena described by the new theory and a subdomain D₀ wherein the old theory is reliable (to a given accuracy). (2) Within the subdomain D₀ either theory may be used to make quantitative predictions. It might often be more expedient to employ the old theory. (3) In addition to numerical accuracy, the new theory often brings about radical conceptual changes. Being of a qualitative nature, these will have a bearing on all of D.

For example, in the case of relativity, D₀ and D represent (macroscopic) phenomena involving small and arbitrary velocities, respectively, the latter, of course, being bounded by the velocity of light. In addition to giving better numerical predictions for high-velocity phenomena, relativity theory also outlaws several cherished notions of the Newtonian scheme, such as absolute time, absolute length, unlimited velocities for particles, etc.

In a similar manner, quantum mechanics brings with it not only improved numerical predictions for the microscopic world, but also conceptual changes that rock the very foundations of classical thought.

This book introduces you to this subject, starting from its postulates. Between you and the postulates there stand three chapters wherein you will find a summary of the mathematical ideas appearing in the statement of the postulates, a review of classical mechanics, and a brief description of the empirical basis for the quantum theory. In the rest of the book, the postulates are invoked to formulate and solve a variety of qu quantum mechanical problems. It is hoped that, by the time you get to the end of the book, you will be able to do the same yourself.

Note to the Student

Do as many exercises as you can, especially the ones marked * or whose results carry equation numbers. The answer to each exercise is given either with the exercise or at the end of the book.

The first chapter is very important. Do not rush through it. Even if you know the math, read it to get acquainted with the notation.

I am not saying it is an easy subject. But I hope this book makes it seem reasonable.

Good luck.

Contents

## 1. Mathematical Introduction

1.1. Linear Vector Spaces: Basics 1.2. Inner Product Spaces 1.3. Dual Spaces and the Dirac Notation 1.4. Subspaces 1.5. Linear Operators 1.6. Matrix Elements of Linear Operators 1.7. Active and Passive Transformations 1.8. The Eigenvalue Problem 1.9. Functions of Operators and Related Concepts 1.10. Generalization to Infinite Dimensions

## 2. Review of Classical Mechanics

2.1. The Principle of Least Action and Lagrangian Mechanics 2.2. The Electromagnetic Lagrangian 2.3. The Two-Body Problem 2.4. How Smart Is a Particle?

2.5. The Hamiltonian Formalism 2.6. The Electromagnetic Force in the Hamiltonian Scheme 2.7. Cyclic Coordinates, Poisson Brackets, and Canonical Transformations 2.8. Symmetries and Their Consequences

## 3. All Is Not Well with Classical Mechanics

3.1. Particles and Waves in Classical Physics 3.2. An Experiment with Waves and Particles (Classical)

3.3. The Double-Slit Experiment with Light 3.4. Matter Waves (de Broglie Waves)

3.5. Conclusions

## 4. The Postulates—a General Discussion

4.1. The Postulates 4.2. Discussion of Postulates I-III 4.3. The Schrödinger Equation (Dotting Your i's and Crossing your h's)

## 5. Simple Problems in One Dimension

5.1. The Free Particle 5.2. The Particle in a Box 5.3. The Continuity Equation for Probability 5.4. The Single-Step Potential: a Problem in Scattering 5.5. The Double-Slit Experiment 5.6. Some Theorems

## 6. The Classical Limit

## 7. The Harmonic Oscillator

7.1. Why Study the Harmonic Oscillator?

7.2. Review of the Classical Oscillator 7.3. Quantization of the Oscillator (Coordinate Basis)

7.4. The Oscillator in the Energy Basis 7.5. Passage from the Energy Basis to the X Basis

## 8. The Path Integral Formulation of Quantum Theory

8.1. The Path Integral Recipe 8.2. Analysis of the Recipe 8.3. An Approximation to U(t) for the Free Particle 8.4. Path Integral Evaluation of the Free-Particle Propagator 8.5. Equivalence to the Schrödinger Equation 8.6. Potentials of the Form V= a+ bx+ cx^2 + dx^3 + ex^4

## 9. The Heisenberg Uncertainty Relations

9.1. Introduction 9.2. Derivation of the Uncertainty Relations 9.3. The Minimum Uncertainty Packet 9.4. Applications of the Uncertainty Principle 9.5. The Energy-Time Uncertainty Relation

## 10. Systems with N Degrees of Freedom

10.1. N Particles in One Dimension 10.2. More Particles in More Dimensions 10.3. Identical Particles

## 11. Symmetries and Their Consequences

11.1. Overview 11.2. Translational Invariance in Quantum Theory 11.3. Time Translational Invariance 11.4. Parity Invariance 11.5. Time-Reversal Symmetry

## 12. Rotational Invariance and Angular Momentum

12.1. Translations in Two Dimensions 12.2. Rotations in Two Dimensions 12.3. The Eigenvalue Problem of Lz 12.4. Angular Momentum in Three Dimensions 12.5. The Eigenvalue Problem of L^2 and Lz 12.6. Solution of Rotationally Invariant Problems

## 13. The Hydrogen Atom

13.1. The Eigenvalue Problem 13.2. The Degeneracy of the Hydrogen Spectrum 13.3. Numerical Estimates and Comparison with Experiment 13.4. Multielectron Atoms and the Periodic Table

## 14. Spin

14.1. Introduction 14.2. What is the Nature of Spin?

14.3. Kinematics of Spin 14.4. Spin Dynamics 14.5. Return of Orbital Degrees of Freedom

## 15. Addition of Angular Momenta

15.1. A Simple Example 15.2. The General Problem 15.3. Irreducible Tensor Operators 15.4. Explanation of Some "Accidental" Degeneracies

## 16. Variational and WKB Methods

16.1. The Variational Method 16.2. The Wentzel-Kramers-Brillouin Method

## 17. Time-Independent Perturbation Theory

17.1. The Formalism 17.2. Some Examples 17.3. Degenerate Perturbation Theory

## 18. Time-Dependent Perturbation Theory

18.1. The Problem 18.2. First-Order Perturbation Theory 18.3. Higher Orders in Perturbation Theory 18.4. A General Discussion of Electromagnetic Interactions 18.5. Interaction of Atoms with Electromagnetic Radiation

## 19. Scattering Theory

19.1. Introduction 19.2. Recapitulation of One-Dimensional Scattering and Overview 19.3. The Born Approximation (Time-Dependent Description)

19.4. Born Again (The Time-Independent Approximation)

19.5. The Partial Wave Expansion 19.6. Two-Particle Scattering

## 20. The Dirac Equation

20.1. The Free-Particle Dirac Equation 20.2. Electromagnetic Interaction of the Dirac Particle 20.3. More on Relativistic Quantum Mechanics

## 21. Path Integrals—II

21.1. Derivation of the Path Integral 21.2. Imaginary Time Formalism 21.3. Spin and Fermion Path Integrals 21.4. Summary

## Appendix

A.1. Matrix Inversion A.2. Gaussian Integrals A.3. Complex Numbers A.4. The iε Prescription

## ANSWERS TO SELECTED EXERCISES

## TABLE OF CONSTANTS

## INDEX

Mathematical Introduction

The aim of this book is to provide you with an introduction to quantum mechanics, starting from its axioms. It is the aim of this chapter to equip you with the necessary mathematical machinery. All the math you will need is developed here, starting from some basic ideas on vectors and matrices that you are assumed to know. Numerous examples and exercises related to classical mechanics are given, both to provide some relief from the math and to demonstrate the wide applicability of the ideas developed here. The effort you put into this chapter will be well worth your while: not only will it prepare you for this course, but it will also unify many ideas you may have learned piecemeal. To really learn this chapter, you must, as with any other chapter, work out the problems.

1.1. Linear Vector Spaces: Basics

In this section you will be introduced to linear vector spaces. You are surely familiar with the arrows from elementary physics encoding the magnitude and direction of velocity, force, displacement, torque, etc. You know how to add them and multiply them by scalars and the rules obeyed by these operations. For example, you know that scalar multiplication is associative: the multiple of a sum of two vectors is the sum of the multiples. What we want to do is abstract from this simple case a set of basic features or axioms, and say that any set of objects obeying the same forms a linear vector space. The cleverness lies in deciding which of the properties to keep in the generalization. If you keep too many, there will be no other examples; if you keep too few, there will be no interesting results to develop from the axioms. The following is the list of properties the mathematicians have wisely chosen as requisite for a vector space. As you read them, please compare them to the world of arrows and make sure that these are indeed properties possessed by these familiar vectors. But note also that conspicuously missing are the requirements that every vector have a magnitude and direction, which was the first and most salient feature drilled into our heads when we first heard about them. So you might think that dropping this requirement, the baby has been thrown out with the bath water. However, you will have ample time to appreciate the wisdom behind this choice as you go along and see a great unification and synthesis of diverse ideas under the heading of vector spaces. You will see examples of vector spaces that involve entities that you cannot intuitively perceive as having either a magnitude or a direction. While you should be duly impressed with all this, remember that it does not hurt at all to think of these generalizations in terms of arrows and to use the intuition to prove theorems or at the very least anticipate them.

Definition 1. A linear vector space V is a collection of objects |V>, ..., |W>, ..., called vectors, for which there exists

## 1. A definite rule for forming the vector sum, denoted |V> + |W>

## 2. A definite rule for multiplication

ion by scalars a, b, . . . , denoted a|V>, with the following features: • The result of these operations is another element of the space, a feature called closure: |V> + |W> ∈ V.

• Scalar multiplication is distributive in the vectors: a(|V> + |W>) = a|V> + a|W>.

• Scalar multiplication is distributive in the scalars: (a + b)|V> = a|V> + b|V>.

• Scalar multiplication is associative: a(b|V>) = ab|V>.

• Addition is commutative: |V> + |W> = |W> + |V>.

• Addition is associative: |V> + (|W> + |Z>) = (|V> + |W>) + |Z>.

• There exist a null vector obeying |0> + |0> = |0>.

• For every vector |V> there exists an inverse under addition, |−V>, such that |V> + |−V> = |0>.

There is a good way to remember all of these; do what comes naturally.

Definition 2. The numbers a, b, . . . are called the field over which the vector space is defined.

If the field consists of all real numbers, we have a real vector space, if they are complex, we have a complex vector space. The vectors themselves are neither real or complex; the adjective applies only to the scalars.

Let us note that the above axioms imply • |0> is unique, i.e., if |0'> has all the properties of |0>, then |0> = |0'>.

• 0|V> = |0>.

• |−V> = −|V>.

• |−V> is the unique additive inverse of |V>.

The proofs are left as to the following exercise. You don't have to know the proofs, but you do have to know the statements.

Exercise 1.1.1. Verify these claims. For the first consider |0> + |0'> and use the advertised properties of the two null vectors in turn. For the second start with |0> = (0 + 1)|V> + |V>. For the third, begin with |V> + (−1|V>) = 0|V> = |0>. For the last, let |W> also satisfy |V> + |W> = |0>. Since |0> is unique, this means |V> + |W> = |V> + |−V>. Take it from here.

Figure 1.1. The rule for vector addition. Note that it obeys axioms (i)-(iii).

Exercise 1.1.2. Consider the set of all entities of the form (a, b, c) where the entries are real numbers. Addition and scalar multiplication are defined as follows: (a, b, c) + (d, e, f) = (a + d, b + e, c + f)

α(a, b, c) = (αa, αb, αc).

Write down the null vector and inverse of (a, b, c). Show that vectors of the form (a, b, 1) do not form a vector space.

Observe that we are using a new symbol |V> to denote a generic vector. This object is called ket V and this nomenclature is due to Dirac whose notation will be discussed at some length later. We do not purposely use the symbol V to denote the vectors as the first step in weaning you away from the limited concept of the vector as an arrow. You are however not discouraged from associating with |V> the arrow-like object till you have seen enough vectors that are not arrows and are ready to drop the crutch.

You were asked to verify that the set of arrows qualified as a vector space as you read the axioms. Here are some of the key ideas you should have gone over. The vector space consists of arrows, typical ones being |V> and |W>. The rule for addition is familiar: take the tail of the second arrow, put it on the tip of the first, and so on as in Fig. 1.1.

Scalar multiplication by α corresponds to stretching the vector by a factor α. This is a real vector space since stretching by a complex number makes no sense. (If α is negative, we interpret it as changing the direction of the arrow as well as rescaling it by |α|.) Since these operations acting on arrows give more arrows, we have closure. Addition and scalar multiplication clearly have all the desired associative and distributive features. The null vector is the arrow of zero length, while the inverse of a vector is the vector reversed in direction.

So the set of all arrows qualifies as a vector space. But we cannot tamper with it. For example, the set of all arrows with positive z-components do not form a vector space: there is no inverse.

Note that so far, no reference has been made to magnitude or direction. The point is that while the arrows have these qualities, members of a vector space need not. This statement is pointless unless I can give you examples, so here are two.

Consider the set of all 2 × 2 matrices. We know how to add them and multiply them by scalars (multiply all four matrix elements by that scalar). The corresponding rules obey closure, associativity, and distributive requirements. The null matrix has all zeros in it and the inverse under addition of a matrix is the matrix with all elements negated. You must agree that here we have a genuine vector space consisting of things which don't have an obvious length or direction associated with them. When we want to highlight the fact that the matrix M is an element of a vector space, we may want to refer to it as, say, ket number 4 or: |4>.

As a second example, consider all functions f(x) defined in an interval 0 < x < L. We define scalar multiplication by α simply as αf(x) and addition as pointwise addition: the sum of two functions f and g has the value f(x) + g(x) at the point x. The null function is zero everywhere and the additive inverse of f is −f.

Exercise 1.1.3. Do functions that vanish at the end points x=0 and x=L form a vector space? How about periodic functions obeying f(0)=f(L)? How about functions that obey f(0)=4? If the functions do not qualify, list the things that go wrong.

The next concept is that of linear independence of a set of vectors |1>, |2>, . . . , |n>. First consider a linear relation of the form ∑ αᵢ|i> = |0> We may assume without loss of generality that the left-hand side does not contain any multiple of |0>, for if it did, it could be shifted to the right, and combined with the |0> there to give |0> once more. (We are using the fact that any multiple of |0> equals |0>.)

Definition 3. The set of vectors is said to be linearly independent if the only such linear relation as Eq. (1.1.1) is the trivial one with all αᵢ = 0. If the set of vectors is not linearly independent, we say they are linearly dependent.

Equation (1.1.1) tells us that it is not possible to write any member of the linearly independent set in terms of the others. On the other hand, if the set of vectors is linearly dependent, such a relation will exist, and it must contain at least two nonzero coefficients. Let us say α₃ ≠ 0. Then we could write |3> = ∑(i=1, i≠3) (-αᵢ/α₃)|i> thereby expressing |3> in terms of the others.

As a concrete example, consider two nonparallel vectors |1> and |2> in a plane. These form a linearly independent set. There is no way to write one as a multiple of the other, or equivalently, no way to combine them to get the null vector. On the other hand, if the vectors are parallel, we can clearly write one as a multiple of the other or equivalently play them against each other to get 0.

Notice I said 0 and not |0>. This is, strictly speaking, incorrect since a set of vectors can only add up to a vector and not a number. It is, however, common to represent the null vector by 0.

Suppose we bring in a third vector |3> also in the plane. If it is parallel to either of the first two, we already have a linearly dependent set. So let us suppose it is not. But even now the three of them are linearly dependent. This is because we can write one of them, say |3>, as a linear combination of the other two. To find the combination, draw a line from the tail of |3> in the direction of |1>. Next draw a line antiparallel to |2> from the tip of |3>. These lines will intersect since |1> and |2> are not parallel by assumption. The intersection point P will determine how much of |1> and |2> we want: we go from the tail of |3> to P using the appropriate multiple of |1> and go from P to the tip of |3> using the appropriate multiple of |2>.

Exercise 1.1.4. Consider three elements from the vector space of real 2 x 2 matrices: |1> = [[1, 0], [0, 0]], |2> = [[0, 1], [0, 0]], |3> = [[0, 0], [0, −2]]

Are they linearly independent? Support your answer with details. (Notice we are calling these matrices vectors and using kets to represent them to emphasize their role as elements of a vector space.)

Exercise 1.1.5. Show that the following row vectors are linearly dependent: (1, 1, 0), (1, 0, 1), and (3, 2, 1). Show the opposite for (1, 1, 0), (1, 0, 1), and (0, 1, 1).

Definition 4. A vector space has dimension n if it can accommodate a maximum of n linearly independent vectors. It will be denoted by V(R) if the field is real and by V(C) if the field is complex.

In view of the earlier discussions, the plane is two-dimensional and the set of all arrows not limited to the plane define a three-dimensional vector space. How about 2 x 2 matrices? They form a four-dimensional vector space. Here is a proof. The following vectors are linearly independent: |1> = [[1, 0], [0, 0]], |2> = [[0, 1], [0, 0]], |3> = [[0, 0], [1, 0]], |4> = [[0, 0], [0, 1]]

since it is impossible to form linear combinations of any three of them to give the fourth any three of them will have a zero in the one place where the fourth does not. So the space is at least four-dimensional. Could it be bigger? No, since any arbitrary 2 x 2 matrix [[a, b], [c, d]] can be written in terms of them: [[a, b], [c, d]] = a|1> + b|2> + c|3> + d|4> If the scalars a, b, c, d are real, we have a real four-dimensional space, if they are complex we have a complex four-dimensional space.

Theorem 1. Any vector |V> in an n-dimensional space can be written as a linear combination of n linearly independent vectors |1>, . . . , |n>.

The proof is as follows: if there were a vector |V> for which this were not possible, it would join the given set of vectors and form a set of n+1 linearly independent vectors, which is not possible in an n-dimensional space by definition.

Definition 5. A set of n linearly independent vectors in an n-dimensional space is called a basis.

Thus we can write, on the strength of the above |V> = ∑ αᵢ|i> where the v...

Definition 6. The coefficients of expansion $\gamma_i$ of a vector $|V\rangle$ in terms of a linearly independent basis $\{|i\rangle\}$ are called the components of the vector in that basis.

Theorem 2. The expansion in Eq. (1.1.1) is unique.

Suppose the expansion is not unique. We must then have a second expansion: $$|V\rangle = \sum v'_i |i\rangle \quad (1.1.4)$$ Subtracting Eq. (1.1.4) from Eq. (1.1.3) (i.e., multiplying the second by the scalar $-1$ and adding the two equations) we get $$|0\rangle = \sum (v_i - v'_i) |i\rangle \quad (1.1.5)$$ which implies that $$v_i = v'_i \quad (1.1.6)$$ since the basis vectors are linearly independent and only a trivial linear relation between them can exist. Note that given a basis the components are unique, but if we change the basis, the components will change. We refer to $|V\rangle$ as the vector in the abstract, having an existence of its own and satisfying various relations involving other vectors. When we choose a basis the vectors assume concrete forms in terms of their components and the relation between vectors is satisfied by the components.

Imagine for example three arrows in the plane, $\vec{A}$, $\vec{B}$, $\vec{C}$, satisfying $\vec{A} + \vec{B} = \vec{C}$ according to the laws for adding arrows. So far no basis has been chosen and we do not need a basis to make the statement that the vectors form a closed triangle. Now we choose a basis and write each vector in terms of the components. The components will satisfy $C_i = A_i + B_i$, $i = 1, 2$. If we choose a different basis, the components will change in numerical value, but the relation between them expressing the equality of $\vec{C}$ to the sum of the other two will still hold between the new set of components.

In the case of nonarrow vectors, adding them in terms of components proceeds as in the elementary case thanks to the axioms. If $$|V\rangle = \sum v_i |i\rangle \quad \text{and} \quad (1.1.7)$$ $$|W\rangle = \sum w_i |i\rangle \quad \text{then} \quad (1.1.8)$$ $$|V\rangle + |W\rangle = \sum (v_i + w_i) |i\rangle \quad (1.1.9)$$ where we have used the axioms to carry out the regrouping of terms. Here is the conclusion: To add two vectors, add their components.

There is no reference to taking the tail of one and putting it on the tip of the other, etc., since in general the vectors have no head or tail. Of course, if we are dealing with arrows, we can add them either using the tail and tip routine or by simply adding their components in a basis.

In the same way, we have: $$a |V\rangle = a \sum v_i |i\rangle = \sum a v_i |i\rangle \quad (1.1.10)$$ In other words, To multiply a vector by a scalar, multiply all its components by the scalar.

1.2. Inner Product Spaces The matrix and function examples must have convinced you that we can have a vector space with no preassigned definition of length or direction for the elements. However, we can make up quantities that have the same properties that the lengths and angles do in the case of arrows. The first step is to define a sensible analog of the dot product, for in the case of arrows, from the dot product $$\vec{A} \cdot \vec{B} = |\vec{A}| |\vec{B}| \cos \theta \quad (1.2.1)$$ we can read off the length of say $\vec{A}$ as $\sqrt{\vec{A} \cdot \vec{A}} = |\vec{A}|$ and the cosine of the angle between two vectors as $\vec{A} \cdot \vec{B} / |\vec{A}| |\vec{B}|$. Now you might rightfully object: how can you use the dot product to define the length and angles, if the dot product itself requires knowledge of the lengths and angles? The answer is this. Recall that the dot product has a second equivalent expression in terms of the components: $$\vec{A} \cdot \vec{B} = A_x B_x + A_y B_y + A_z B_z \quad (1.2.2)$$ Our goal is to define a similar formula for the general case where we do have the notion of components in a basis. To this end we recall the main features of the above dot product: 1. $\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$ (symmetry)

2. $\vec{A} \cdot \vec{A} \geq 0$, and $\vec{A} \cdot \vec{A} = 0$ iff $\vec{A} = 0$ (positive semidefiniteness)

3. $\vec{A} \cdot (b\vec{B} + c\vec{C}) = b \vec{A} \cdot \vec{B} + c \vec{A} \cdot \vec{C}$ (linearity)

The linearity of the dot product is illustrated in Fig. 1.2.

We want to invent a generalization called the inner product or scalar product between any two vectors $|V\rangle$ and $|W\rangle$. We denote it by the symbol $\langle V | W\rangle$. It is once again a number (generally complex) dependent on the two vectors. We demand that it obey the following axioms: 1. $\langle V | W\rangle = \langle W | V\rangle^*$ (skew-symmetry)

2. $\langle V | V\rangle \geq 0$, and $\langle V | V\rangle = 0$ iff $|V\rangle = |0\rangle$ (positive semidefiniteness)

3. $\langle V | (a |W\rangle + b |Z\rangle) = a \langle V | W\rangle + b \langle V | Z\rangle$ (linearity in ket)

Definition 7. A vector space with an inner product is called an inner product space.

Notice that we have not yet given an explicit rule for actually evaluating the scalar product, we are merely demanding that any rule we come up with must have these properties. With a view to finding such a rule, let us familiarize ourselves with the axioms. The first differs from the corresponding one for the dot product and makes the inner product sensitive to the order of the two factors, with the two choices leading to complex conjugates. In a real vector space this axiom states the symmetry of the dot product under exchange of the two vectors. For the present, let us note that this axiom ensures that $\langle V | V\rangle$ is real.

The second axiom says that $\langle V | V\rangle$ is not just real but also positive semidefinite, vanishing only if the vector itself does. If we are going to define the length of the vector as the square root of its inner product with itself (as in the dot product) this quantity had better be real and positive for all nonzero vectors.

The last axiom expresses the linearity of the inner product when a linear superposition $a |W\rangle + b |Z\rangle$ appears as the second vector in the scalar product. We have discussed its validity for the arrows case (Fig. 1.2).

What if the first factor in the product is a linear superposition, i.e., what is $\langle aW + bZ | V\rangle$? This is determined by the first axiom: $$\langle aW + bZ | V\rangle = \langle V | aW + bZ\rangle^* \text{ by BI}$$ $$= (a \langle V | W\rangle + b \langle V | Z\rangle)^*$$ $$= a^* \langle V | W\rangle^* + b^* \langle V | Z\rangle^*$$ $$= a^* \langle W | V\rangle + b^* \langle Z | V\rangle \quad (1.2.3)$$ which expresses the antilinearity of the inner product with respect to the first factor in the inner product. In other words, the inner product of a linear superposition with another vector is the corresponding superposition of inner products if the superposition occurs in the second factor, while it is the superposition with all coefficients conjugated if the superposition occurs in the first factor. This asymmetry, unfamiliar in real vector spaces, is here to stay and you will get used to it as you go along.

Let us continue with inner products. Even though we are trying to shed the restricted notion of a vector as an arrow and seeking a corresponding generalization of the dot product, we still use some of the same terminology.

Definition 8. We say that two vectors are orthogonal or perpendicular if their inner product vanishes.

Definition 9. We will refer to $\sqrt{\langle V | V\rangle}$ as the norm or length of the vector. A normalized vector has unit norm.

Definition 10. A set of basis vectors all of unit norm, which are pairwise orthogonal will be called an orthonormal basis.

We will also frequently refer to the inner or scalar product as the dot product.

We are now ready to obtain a concrete formula for the inner product in terms of the components. Given $|V\rangle$ and $|W\rangle$, $$|V\rangle = \sum v_i |i\rangle$$ we follow the axioms obeyed by the inner product to obtain: $$\langle V | W\rangle = \sum_i \sum_j v_i^* w_j \langle i | j\rangle \quad (1.2.4)$$ To go any further we have to know $\langle i | j\rangle$, the inner product between basis vectors. That depends on the details of the basis vectors and all we know for sure is that they are linearly independent. This situation exists for arrows as well. Consider a two-dimensional problem where the basis vectors are two linearly independent but nonperpendicular vectors. If we write all vectors in terms of this basis, the dot product of any two of them will likewise be a double sum with four terms (determined by the four possible dot products between the basis vectors) as well as the vector components. However, if we use an orthonormal basis such as $\hat{i}, \hat{j}, \hat{k}$, only diagonal terms like $\langle i | i\rangle$ will survive and we will get the familiar result $\vec{A} \cdot \vec{B} = A_x B_x + A_y B_y + A_z B_z$ depending only on the components.

For the more general nonarrow case, we invoke Theorem 3.

Theorem 3 (Gram-Schmidt). Given a linearly independent basis we can form linear combinations of the basis vectors to obtain an orthonormal basis.

Postponing the proof for a moment, let us assume that the procedure has been implemented and that the current basis is orthonormal: $$\langle i | j\rangle = \delta_{ij} = \begin{cases} 1 & \text{for } i = j \\ 0 & \text{for } i \neq j \end{cases}$$ where $\delta_{ij}$ is called the Kronecker delta symbol. Feeding this into Eq. (1.2.4) we find the double sum collapses to a single one due to the Kronecker delta, to give $$\langle V | W\rangle = \sum_i v_i^* w_i \quad (1.2.5)$$ This is the form of the inner product we will use from now on.

You can now appreciate the first axiom; but for the complex conjugation of the components of the first vector, $\langle V | V\rangle$ would not even be real, not to mention positive. But now it is given by $$\langle V | V\rangle = \sum_i |v_i|^2 \quad (1.2.6)$$ and vanishes only for the null vector. This makes it sensible to refer to $\langle V | V\rangle$ as the length or norm squared of a vector.

Consider Eq. (1.2.5). Since the vector $|V\rangle$ is uniquely specified by its components in a given basis, we may, in this basis, write it as a column vector: $$|V\rangle \rightarrow \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix} \text{ in this basis} \quad (1.2.7)$$ Likewise, $$|W\rangle \rightarrow \begin{pmatrix} w_1 \\ w_2 \\ \vdots \\ w_n \end{pmatrix} \text{ in this basis} \quad (1.2.8)$$ The inner product $\langle V | W\rangle$ is given by the matrix product of the transpose conjugate of the column vector representing $|V\rangle$ with the column vector representing $|W\rangle$: $$\langle V | W\rangle = [v_1^*, v_2^*, \ldots, v_n^*] \begin{pmatrix} w_1 \\ w_2 \\ \vdots \\ w_n \end{pmatrix} \quad (1.2.9)$$

1.3. Dual Spaces and the Dirac Notation There is a technical point here. The inner product is a number we are trying to generate from two kets $|V\rangle$ and $|W\rangle$, which are both represented by column vectors in some basis. Now there is no way to make a number out of two columns by direct matrix multiplication, but there is a way to make a number by multiplying a row vector and a column vector.

矩阵乘法涉及行乘以列。我们从两列产生一个数的技巧，是将一个列向量与一个唯一的行向量（其共轭转置）关联，然后计算该行向量与代表另一列的列向量的矩阵乘积。这种方法的特点是结果取决于我们将两个向量中的哪一个转换为行向量，两种选择（<V W> 和 <W|V>）得出的结果通过复共轭相关联，如公理1(h)所述。

但也可以采用以下替代观点。列向量是抽象向量 |V> 或 ket 在特定基中的具体表示。我们也可以反向操作，从列向量回到抽象的 ket。但同样地，也可以反向操作，将每个行向量与一个抽象对象 <W|（称为 bra-W）关联起来。现在我们可以随意命名这些 bra，但让我们这样做：与每个 ket |V> 关联的是一个列向量。我们取其伴随（即共轭转置）来形成一个行向量。与之关联的抽象 bra 将带有相同的标签，即称为 <V|。这样，我们就有两个向量空间：ket 的空间和 bra 的对偶空间，每个 ket 对应一个 bra，反之亦然（它们的分量通过伴随运算相关联）。内积实际上只定义在 bra 和 ket 之间，因此涉及两个不同但相关的向量空间的元素。存在一组用于展开 ket 的基矢 |i> 和一组用于展开 bra 的类似基矢 <i|。基 ket |i> 在我们所用的基中由一个列向量表示，该列向量除了第 i 行为 1 外全为零；而基 bra <i| 是一个行向量，除了第 i 列为 1 外全为零。

所有这些可以总结如下：

## CHAPTER

|V> = (V1, V2, ..., Vn)^T (1.3.1)

其中 => 表示“在某个基下”。

然而，将标量积与一对列向量或 ket 关联（不涉及另一个对偶空间），并接受内积中第一个和第二个向量之间的这种不对称性（对哪个进行共轭转置？），这种观点也没有错。如果你觉得上面的讨论很费力，可以暂时忽略它。你唯一必须记住的是，在一般的非箭头向量空间中：

• 向量仍然可以在某个正交归一基中被赋予分量，就像箭头一样，但这些分量可以是复数。

• 任何两个向量的内积由这些分量通过公式(1.2.5)给出。该乘积满足所有公理。

1.3.1. 在正交归一基中展开向量

假设我们希望在一个正交归一基中展开一个向量 |V>。为了找到展开式中的分量，我们进行如下操作：我们用 |j>（或者如果你是纯粹主义者，用 <j|）点乘假设的展开式的两边： |V> = Σ v_i |i> (1.3.2)

<j|V> = Σ v_i <j|i> (1.3.3)

= v_j (1.3.4)

即，要找到一个向量的第 j 个分量，我们用第 j 个单位向量进行点乘，这与箭头的情况完全一样。利用这个结果，我们可以写成： |V> = Σ |i><i|V> (1.3.5)

让我们确保基矢看起来是正确的。如果在公式(1.3.5)中设 |V> = |j>，我们发现得到正确的答案：第 j 个基矢的第 i 个分量是 δ_ij。例如，代表第 4 号基矢的列向量将在第 4 行有一个 1，其他位置全为零。抽象关系 |V> = Σ v_i |i> (1.3.6)

在此基下变为：

## MATHEMATICAL INTRODUCTION

|V> = (V1, V2, ..., Vn)^T (1.3.7)

1.3.2. 伴随运算

我们已经看到，可以通过伴随运算（即共轭转置）从代表 ket 的列向量得到代表相应 bra 的行向量。现在让我们问：如果 <V| 是 ket |V> 对应的 bra，那么标量 a 乘以 |V> (即 a|V>) 对应的 bra 是什么？通过到任意基下计算，很容易发现： a|V> => (a*v1, a*v2, ..., a*vn)^T => <V|a* (1.3.8)

通常将 a|V> 写为 |aV>，相应的 bra 写为 <aV|。我们发现： <aV| = <V|a* (1.3.9)

由于 bra 和 ket 之间的关系是线性的，我们可以说，如果我们有一个关于 ket 的方程，比如： a|V> = b|W> + c|Z> + ...

(1.3.10)

这意味着相应的 bra 有另一个方程： <V|a* = <W|b* + <Z|c* + ...

(1.3.11)

上面的两个方程被称为彼此的伴随。就像任何涉及复数的方程都意味着另一个通过取两边复共轭得到的方程一样，一个（bra 或 ket 的）方程意味着另一个在（ket 或 bra 之间的）方程。如果你在基下思考，你会看到这仅仅源于这样一个事实：如果两个列向量相等，那么它们的共轭转置也相等。

以下是取伴随的规则： 要对一个涉及 ket（或 bra）的线性方程取伴随，将每个 ket（或 bra）替换为其对应的 bra（或 ket），并对所有系数取复共轭。

我们可以扩展这个规则。假设我们有一个向量的展开式： |V> = Σ v_i |i> (1.3.12)

（用基矢表示）。其伴随是： <V| = Σ v_i* <i| （其中 i=1）

回忆 v_i = <i|V> 且 v_i* = <V|i>，可得公式 (1.3.13)

|V> = Σ |i><i|V> (1.3.13)

的伴随是： <V| = Σ <V|i><i| (1.3.14)

由此得到规则： 要对一个涉及 bra、ket 和系数的方程取伴随，需反转所有因子的顺序，交换 bra 和 ket，并对所有系数取复共轭。

Gram-Schmidt 定理

现在让我们讨论将线性无关基转化为正交归一基的 Gram-Schmidt 步骤。基本思想可以通过一个简单的例子来看。想象平面上箭头的二维空间。让我们取两个不平行向量，它们构成一组基。要从这组基得到正交归一基，我们执行以下操作：

• 将第一个向量按其自身长度重新缩放，使其成为单位向量。这将是第一个基矢。

• 从第二个向量中减去其在第一个向量上的投影，只留下垂直于第一个向量的部分。（根据假设向量不平行，这样的部分会保留下来。）

• 将剩余的部分按其自身长度重新缩放。我们现在得到第二个基矢：它正交于第一个基矢且长度为单位长度。

这个简单的例子讲述了该过程的全部故事，现在我们将用狄拉克记号在一般情况下进行讨论。

令 |φ1>, |φ2>, ... 为一个线性无关基。正交归一基的第一个矢量将是： |1> = |φ1> / ||φ1|| = |φ1> / <φ1|φ1>^{1/2} 显然 <1|1> = 1。

对于基中的第二个矢量，考虑： |2'> = |φ2> - |1><1|φ2> 即 |φ2> 减去指向第一个单位矢量方向的部分。（读下去时想想箭头的例子。）不出所料，它与后者正交： <1|2'> = <1|φ2> - <1|1><1|φ2> = 0 现在我们将 |2'> 除以其范数以得到 |2>，它将与第一个矢量正交且归一化。最后，考虑： |3'> = |φ3> - |1><1|φ3> - |2><2|φ3> 它与 |1> 和 |2> 都正交。除以其范数，我们得到 |3>，即正交基的第三个成员。生成其余基矢的过程没有新内容。

我们何时使用了原始基的线性无关性？如果我们从一个线性相关的基开始会怎样？那么在某一步，像 |2'> 或 |3'> 这样的矢量会变为零，从而停止整个过程。另一方面，线性无关性将确保这种情况永远不会发生，因为它意味着线性无关矢量的非平凡线性组合等于零矢量。（回头看看 |2'> 或 |3'> 的方程，并确信它们是旧基矢的线性组合。）

练习1.3.1. 从 ψ1 = 3i + 4j 和 ψ2 = 5i - 6j 出发，在二维空间中构成一个正交基。你能从这两个向量开始生成另一个正交归一基吗？如果能，生成另一个。

练习1.3.2. 展示如何从基 |1> = [1, 0, 0]^T, |2> = [0, 1, 0]^T, |3> = [0, 0, 1]^T 转换到正交归一基 |I1> = [0, 1, 0]^T, |I2> = [1/√3, 0, 1/√3]^T, |I3> = [1/√3, 0, -1/√3]^T

当我们第一次学习维度时，将其与垂直方向的数量联系起来。在本章中，我们用空间中线性无关向量的最大数量来定义维度。以下定理连接了这两个定义。

定理4. 空间的维度等于 n，即其中相互正交向量的最大数量。

为了证明这一点，首先注意到任何相互正交的集合也是线性无关的。假设我们有一个正交向量的线性组合等于零。通过用任意一个成员点乘两边并利用正交性，我们可以证明乘以该向量的系数必须为零。显然可以对所有系数进行此操作，表明该线性组合是平凡的。

现在 n' 只能等于、大于或小于空间的维度 n。Gram-Schmidt 过程通过显式构造排除了最后一种情况，而垂直向量的线性无关性排除了倒数第二种情况。

Schwarz 和三角不等式

两个强大的定理适用于任何满足我们公理的内积空间：

定理5. Schwarz 不等式 |<V|W>| ≤ ||V|| ||W|| (1.3.15)

定理6. 三角不等式 ||V + W|| ≤ ||V|| + ||W|| (1.3.16)

第一个定理的证明将提供，以便你习惯于使用 bra 和 ket 进行运算。第二个将作为练习留给你。

在证明任何内容之前，请注意这些结果对于箭头显然是正确的：Schwarz 不等式说两个向量的点积不能超过它们长度的乘积，三角不等式说和的长度小于等于长度的和。

cannot exceed the sum of the lengths. This is an example which illustrates the merits of thinking of abstract vectors as arrows and guessing what properties they might share with arrows. The proof will of course have to rely on just the axioms.

To prove the Schwarz inequality, consider axiom 1(i) applied to |z⟩ = |v⟩ − (⟨w|v⟩/⟨w|w⟩) |w⟩. (1.3.17)

We get ⟨w|v⟩ ⟨w|v⟩ ⟨z|z⟩ = ⟨v|w⟩⟨w|v⟩ − |⟨w|v⟩|²/⟨w|w⟩ + |⟨w|v⟩|²/⟨w|w⟩² ⟨w|w⟩ = |⟨w|v⟩|²/⟨w|w⟩ > 0. (1.3.18)

where we have used the antilinearity of the inner product with respect to the bra.

Using ⟨v|w⟩* = ⟨w|v⟩ we find |⟨w|v⟩|²/⟨w|w⟩ ≤ ⟨v|v⟩. (1.3.19)

Cross-multiplying by ⟨w|w⟩ and taking square roots, the result follows.

Exercise 1.3.3. When will this inequality be satisfied? Does this agree with you experience with arrows?

Exercise 1.3.4. Prove the triangle inequality starting with |v + w|². You must use Re⟨v|w⟩ ≤ |⟨v|w⟩| and the Schwarz inequality. Show that the final inequality becomes an equality only if |v⟩ = a|w⟩ where a is a real positive scalar.

1.4. Subspaces Definition 11. Given a vector space V, a subset of its elements that form a vector space among themselves is called a subspace. We will denote a particular subspace of dimensionality n_i by V_i.

Vector addition and scalar multiplication are defined the same way in the subspace as in V.

Example 1.4.1. In the space V_3(ℝ), the following are some example of subspaces: (a) all vectors along the x axis, the space V_x; (b) all vectors along the y axis, the space V_y; (c) all vectors in the x-y plane, the space V_xy. Notice that all subspaces contain the null vector and that each vector is accompanied by its inverse to fulfill axioms for a vector space. Thus the set of all vectors along the positive x axis alone do not form a vector space.

Definition 12. Given two subspaces V_i and V_j, we define their sum V_i ⊕ V_j as the set containing (1) all elements of V_i, (2) all elements of V_j, (3) all possible linear combinations of the above. But for the elements (3), closure would be lost.

Example 1.4.2. If, for example, V_x ⊕ V_y contained multiple of |i> with a coefficient (v_i) which is the component of |V> along |i>. Since P_i projects out the component of any ket |V> along the direction |i>, it is called a projection operator.

The completeness relation, Eq. (1.6.7), says that the sum of the projections of a vector along all the n directions equals the vector itself. Projection operators can also act on bras in the same way: <ψ| P_i = <ψ|i><i| = v_i*<i| (1.6.9)

Projection operators corresponding to the basis vectors obey P_i P_j = |i><i| j><j| = δ_{ij} P_i (1.6.10)

This equation tells us that (1) once P_i projects out the part of |V> along |i>, further applications of P_i make no difference; and (2) the subsequent application of P_j (j ≠ i)

will result in zero, since a vector entirely along |i> cannot have a projection along a perpendicular direction |j>.

Figure 1.4. P_x and P_y are polarizers placed in the way of a beam traveling along the z axis. The action of the polarizers on the electric field E obeys the law of combination of projection operators: P_y P_x = The following example from optics may throw some light on the discussion.

Consider a beam of light traveling along the z axis and polarized in the x – y plane at an angle θ with respect to the y axis (see Fig. 1.4). If a polarizer P_y that only admits light polarized along the y axis is placed in the way, the projection E cos θ along the y axis is transmitted. An additional polarizer P_y placed in the way has no further effect on the beam. We may equate the action of the polarizer to that of a projection operator P_y that acts on the electric field vector E. If P_y is followed by a polarizer P_x the beam is completely blocked. Thus the polarizers obey the equation P_x P_y = δ_{xy} P_x as expected of projection operators.

Let us next turn to the matrix elements of P. There are two approaches. The first one, somewhat indirect, gives us a feeling for what kind of an object |i><i| is.

We know |i> and <i| = (0, 0, ... , 1, 0, 0, ... , 0)

so that 25

## MATHEMATICAL INTRODUCTION

|i><i| = |i> <i| = |i> (0, 0, ... , 1, 0, ... , 0) = |i> (1.6.11)

... ... 0 ... ...

by the rules of matrix multiplication. Whereas <ψ|ψ'> = (1 x n matrix) x (n x 1 matrix) = (1 x 1 matrix) is a scalar, |ψ><ψ'| = (n x 1 matrix) x (1 x n matrix) = (n x n matrix) is an operator. The inner product <ψ|ψ'> represents a bra and ket which have found each other, while |ψ><ψ'|, sometimes called the outer product, has the two factors looking the other way for a bra or a ket to dot with.

The more direct approach to the matrix elements gives (P_i)_{kl} = <k|P_i|l> = <k|i><i|l> = δ_{ki} δ_{il} (1.6.12)

which is of course identical to Eq. (1.6.11). The same result also follows from mnemonic. Each projection operator has only one nonvanishing matrix element, a 1 at the ith element on the diagonal. The completeness relation, Eq. (1.6.7), says that when all the P_i are added, the diagonal fills out to give the identity. If we form the sum over just some of the projection operators, we get the operator which projects a given vector into the subspace spanned by just the corresponding basis vectors.

Matrices Corresponding to Products of Operators Consider next the matrices representing a product of operators. These are related to the matrices representing the individual operators by the application of Eq. (1.6.7) : (Q A)_{ij} = <i|Q A|j> = <i|Q A |k><k|j> = Σ_k <i|Q|k><k|A|j> = Σ_k Q_{ik} A_{kj} (1.6.13)

Thus the matrix representing the product of operators is the product of the matrices representing the factors.

The Adjoint of an Operator Recall that given a ket a |ψ> the corresponding bra is <a ψ| = a* <ψ| (and not a <ψ|)

26 In the same way, given a ket

## CHAPTER

|ψ'> = Ω |ψ> the corresponding bra is <ψ'| = <ψ| Ω† (1.6.14)

which defines the operator Ω†. One may state this equation in words: if Ω turns a ket |ψ> to |ψ'>, then Ω† turns the bra <ψ| into <ψ'|. Just as a and a*, |ψ> and <ψ| are related but distinct objects, so are Ω and Ω†. The relation between Ω, and Ω†, called the adjoint of Ω or "omega dagger," is best seen in a basis: (Ω†)_{ij} = <i|Ω†|j> = (<j|Ω|i>)* = (Ω_{ji})* So Ω†_{ij} = Ω_{ji}^* (1.6.15)

In other words, the matrix representing Ω† is the transpose conjugate of the matrix representing Ω. (Recall that the row vector representing <ψ| is the transpose conjugate of the column vector representing |ψ>. In a given basis, the adjoint operation is the same as taking the transpose conjugate.)

The adjoint of a product is the product of the adjoints in reverse: (Ω A)† = A† Ω† (1.6.16)

To prove this we consider <Ω A ψ|. First we treat Ω A as one operator and get <Ω A ψ| = <(Ω A) ψ| = <ψ| (Ω A)† Next we treat (A |ψ>) as just another vector, and write <Ω A ψ| = <Ω (A ψ)| = <A ψ| Ω† We next pull out A, pushing Ω† further out: <Ω A ψ| = <ψ| A† Ω† Comparing this result with the one obtained a few lines above, we get the desired result.

Consider now an equation consisting of kets, scalars, and operators, such as a₁ |ψ₁> = a₂ |ψ₂> + a₃ |ψ₃><ψ₄|ψ₅> + a₄ Ω A |ψ₆> (1.6.17a)

What is its adjoint? Our old rule tells us that it is 27

## MATHEMATICAL INTRODUCTION

<ψ₁| a₁* = <ψ₂| a₂* + <ψ₅|ψ₄><ψ₃| a₃* + <ψ₆| A† Ω† a₄* In the last term we can replace <ψ₆|Ω A| by <ψ₆|(Ω A)† = <ψ₆| A† Ω† so that finally we have the adjoint of Eq. (1.6.17a): <ψ₁| a₁* = <ψ₂| a₂* + <ψ₅|ψ₄><ψ₃| a₃* + <ψ₆| A† Ω† a₄* (1.6.17b)

The final rule for taking the adjoint of the most general equation we will ever encounter is this: When a product of operators, bras, kets, and explicit numerical coefficients is encountered, reverse the order of all factors and make the substitutions Ω → Ω†, |ψ> → <ψ|, a → a*.

(Of course, there is no real need to reverse the location of the scalars a except in the interest of uniformity.)

Hermitian, Anti Hermitian, and Unitary Operators We now turn our attention to certain special classes of operators that will play a major role in quantum mechanics.

Definition 13. An operator Ω is Hermitian if Ω† = Ω.

Definition 14. An operator Ω is anti-Hermitian if Ω† = -Ω.

The adjoint is to an operator what the complex conjugate is to numbers. Hermitian and anti-Hermitian operators are like pure real and pure imaginary numbers. Just as every number may be decomposed into a sum of pure real and pure imaginary parts, a = (a + a*)/2 + (a - a*)/2, we can decompose every operator into its Hermitian and anti-Hermitian parts: Ω = (Ω + Ω†)/2 + (Ω - Ω†)/2 (1.6.18)

Exercise 1.6.2.* Given Ω and A are Hermitian what can you say about (1) Ω A; (2) Ω A + A Ω; (3) [Ω, A]; and (4) i[Ω, A]?

28 Definition 15. An operator U is unitary if

## CHAPTER 1 U U† = I (1.6.19)

This equation tells us that U and U† are inverses of each other. Consequently, from Eq. (1.5.12), U† U = I (1.6.20)

Following the analogy between operators and numbers, unitary operators are like complex numbers of unit modulus, u = e^{iφ}. Just as u* u = 1, so is U† U = I.

Exercise 1.6.3.* Show that a product of unitary operators is unitary.

Theorem 7. Unitary operators preserve the inner product between the vectors they act on.

Proof Let |ψ₁'> = U |ψ₁> and |ψ₂'> = U |ψ₂> Then <ψ₂'|ψ₁'> = <U ψ₂|U ψ₁> = <ψ₂| U† U |ψ₁> = <ψ₂|ψ₁> (1.6.21)

(Q.E.D.)

Unitary operators are the generalizations of rotation operators from V₃(R) to V₃(C), for just like rotation operators in three dimensions, they preserve the lengths of vectors and their dot products. In fact, on a real vector space, the unitarity condition becomes U⁻¹ = Uᵀ (T means transpose), which defines an orthogonal or rotation matrix. [R(φ) is an example.]

Theorem 8. If one treats the columns of an n x n unitary matrix as components of n vectors, these vectors are orthonormal. In the same way, the rows may be interpreted as components of n orthonormal vectors.

Proof 1. According to our mnemonic, the jth column of the matrix representing U is the image of the jth basis vector after U acts on it. Since U preserves inner products, the rotated set of vectors is also orthonormal. Consider next the rows. We now use the fact that U† is also a rotation. (How else can it neutralize U to give U† U = I?) Since the rows of U are the columns of U† (but for an overall complex conjugation which does not affect the question of orthonormality), the result we 29 already have for the columns of a unitary matrix tells us the rows of U are orthonormal.

Proof 2. Since U† U = I, δ_{ij} = <i|I|j> = <i| U† U |j> = Σ_k <i| U†|k><k| U |j> = Σ_k U_{ki}^* U_{kj} (1.6.22)

which proves the theorem for the columns. A similar result for the rows follows if we start with the equation U U† = I. Q.E.D.

Note that U† U = I and U U† = I are not independent conditions.

Exercise 1.6.4.* It is assumed that you know (1) what a determinant is, (2) that det Sᵀ = det S (T denotes transpose), (3) that the determinant of a product of matrices is the product of the determinants. [If you do not, verify these properties for a two-dimensional case S = (a b)

(c d)

with det S = ad - bc.] Prove that the determinant of a unitary matrix is a complex number of unit modulus.

Exercise 1.6.5.* Verify that R(φ) is unitary (orthogonal) by examining its matrix.

Exercise 1.6.6. Verify that the following matrices are unitary: (1/√2) [1 i] (1/2) [1+i 1-i]

[i 1]       [1-i 1+i]

Verify that the determinant is of the form e^{iθ} in each case. Are any of the above matrices Hermitian?

1.7. Active and Passive Transformations Suppose we subject all the vectors |ψ> in a space to a unitary transformation |ψ> → |ψ'> = U |ψ> (1.7.1)

Under this transformation, the matrix elements of any operator Ω are modified as follows: <ψ'|Ω|ψ'> = <U ψ|Ω|U ψ> = <ψ| U† Ω U |ψ> (1.7.2)

30 It is clear that the same change would be effected if we left the vectors alone and subjected all operators to the change Ω → Ω' = U† Ω U (1.7.3)

The first case is called an active transformation and the second a passive transformation. The present nomenclature is in reference to the vectors: they are affected in an active transformation and left alone in the passive case. The situation is exactly the opposite from the point of view of the operators.

Later we will see that the physics in quantum theory lies in the matrix elements of operators, and that active and passive transformations provide us with two equivalent ways of describing the same physical transformation.

Exercise 1.7.1.* The trace of a matrix is defined to be the sum of its diagonal matrix elements Tr = Σ n.

Show that (1) Tr(ΩA) = Tr(AΩ)

(2) Tr(ΩAΘ) = Tr(AΘΩ) = Tr(ΘΩA) (The permutations are cyclic).

(3) The trace of an operator is unaffected by a unitary change of basis |ψ'> = U|ψ>. [Equivalently, show Tr Ω = Tr(U†ΩU).]

Exercise 1.7.2. Show that the determinant of a matrix is unaffected by a unitary change of basis. [Equivalently show det Ω = det(U†ΩU).]

1.8. The Eigenvalue Problem Consider some linear operator Ω acting on an arbitrary nonzero ket |ψ>: Ω|ψ> = |ψ'> (1.8.1)

Unless the operator happens to be a trivial one, such as the identity or its multiple, the ket will suffer a nontrivial change, i.e., |ψ'> will not be simply related to |ψ>.

So much for an arbitrary ket. Each operator, however, has certain kets of its own, called its eigenkets, on which its action is simply that of rescaling: Ω|ω> = ω|ω> (1.8.2)

Equation (1.8.2) is an eigenvalue equation: |ω> is an eigenket of Ω with eigenvalue ω. In this chapter we will see how, given an operator Ω, one can systematically determine all its eigenvalues and eigenvectors. How such an equation enters physics will be illustrated by a few examples from mechanics at the end of this section, and once we get to quantum mechanics proper, it will be eigen, eigen, eigen all the way.

Example 1.8.1. To illustrate how easy the eigenvalue problem really is, we will begin with a case that will be completely solved: the case Ω = I. Since I|ψ> = |ψ> for all |ψ>, we conclude that (1) the only eigenvalue of I is 1; (2) all vectors are its eigenvectors with this eigenvalue.

Example 1.8.2. After this unqualified success, we are encouraged to take on a slightly more difficult case: Ω = P_ψ, the projection operator associated with a normalized ket |ψ>. Clearly (1) any ket α|ψ>, parallel to |ψ> is an eigenket with eigenvalue 1: P_ψ(α|ψ>) = |ψ><ψ|α|ψ> = α|ψ><ψ|ψ> = α|ψ> = 1*(α|ψ>)

(2) any ket |φ>, perpendicular to |ψ>, is an eigenket with eigenvalue 0: P_ψ|φ> = |ψ><ψ|φ> = 0 = 0|φ> (3) kets that are neither, i.e., kets of the form α|ψ> + β|φ>, are simply not eigenkets: P_ψ(α|ψ> + β|φ>) = α|ψ> ≠ λ(α|ψ> + β|φ>)

Since every ket in the space falls into one of the above classes, we have found all the eigenvalues and eigenvectors.

Example 1.8.3. Consider now the operator R(x̂π). We already know that it has one eigenket, the basis vector |x̂> along the x axis: R(x̂π)|x̂> = |x̂> Are there others? Of course, any vector α|x̂> along the x axis is also unaffected by the x rotation. This is a general feature of the eigenvalue equation and reflects the linearity of the operator: if Ω|ω> = ω|ω> then Ω(α|ω>) = αΩ|ω> = αω|ω> = ω(α|ω>)

for any multiple α. Since the eigenvalue equation fixes the eigenvector only up to an overall scale factor, we will not treat the multiples of an eigenvector as distinct eigenvectors. With this understanding in mind, let us ask if R(x̂π) has any eigenvectors besides |x̂>. Our intuition says no, for any vector not along the x axis necessarily gets rotated by R(x̂π) and cannot possibly transform into a multiple of itself. Since every vector is either parallel to |x̂> or isn't, we have fully solved the eigenvalue problem.

The trouble with this conclusion is that it is wrong! R(x̂π) has two other eigenvectors besides |x̂>. But our intuition is not to be blamed, for these vectors are in V3(C) and not V3(R). It is clear from this example that we need a reliable and systematic method for solving the eigenvalue problem in Vn(C). We now turn our attention to this very question.

The Characteristic Equation and the Solution to the Eigenvalue Problem We begin by rewriting Eq. (1.8.2) as (Ω − ωI)|ω> = |0> (1.8.3)

Operating both sides with (Ω − ωI)⁻¹, assuming it exists, we get |ω> = (Ω − ωI)⁻¹|0> (1.8.4)

Now, any finite operator (an operator with finite matrix elements) acting on the null vector can only give us a null vector. It therefore seems that in asking for a nonzero eigenvector |ω>, we are trying to get something for nothing out of Eq. (1.8.4). This is impossible. It follows that our assumption that the operator (Ω − ωI)⁻¹ exists (as a finite operator) is false. So we ask when this situation will obtain. Basic matrix theory tells us (see Appendix A.1) that the inverse of any matrix M is given by M⁻¹ = (cofactor M)ᵀ / det M (1.8.5)

Now the cofactor of M is finite if M is. Thus what we need is the vanishing of the determinant. The condition for nonzero eigenvectors is therefore det(Ω − ωI) = 0 (1.8.6)

This equation will determine the eigenvalues ω. To find them, we project Eq. (1.8.3) onto a basis. Dotting both sides with a basis bra <i|, we get <i|Ω − ωI|ω> = 0 and upon introducing the representation of the identity [Eq. (1.6.7)], to the left of |ω>, we get the following image of Eq. (1.8.3): Σ_j (Ω_{ij} − ω δ_{ij}) ω_j = 0 (1.8.7)

Setting the determinant to zero will give us an expression of the form Σ c_m ω^m = 0 (1.8.8)

m=0 Equation (1.8.8) is called the characteristic equation and P_n(ω) = Σ c_m ω^m (1.8.9)

m=0 is called the characteristic polynomial. Although the polynomial is being determined in a particular basis, the eigenvalues, which are its roots, are basis independent, for they are defined by the abstract Eq. (1.8.3), which makes no reference to any basis.

Now, a fundamental result in analysis is that every nth-order polynomial has n roots, not necessarily distinct and not necessarily real. Thus every operator in Vn(C) has n eigenvalues. Once the eigenvalues are known, the eigenvectors may be found, at least for Hermitian and unitary operators, using a procedure illustrated by the following example. [Operators on Vn(C) that are not of the above variety may not have n eigenvectors—see Exercise 1.8.4. Theorems 10 and 12 establish that Hermitian and unitary operators on Vn(C) will have n eigenvectors.]

Example 1.8.4. Let us use the general techniques developed above to find all the eigenvectors and eigenvalues of R(x̂π). Recall that the matrix representing it is R(x̂π) = [0 0 0; 0 0 -1; 0 1 0]

Therefore the characteristic equation is det(R − ωI) = det([ -ω 0 0; 0 -ω -1; 0 1 -ω]) = 0 (−ω)(ω² + 1) = 0 (1.8.10)

with roots ω = 0, ± i. We know that ω = 0 corresponds to |x̂>. Let us see this come out of the formalism. Feeding ω = 0 into Eq. (1.8.7) we find that the components x1, x2, and x3 of the corresponding eigenvector must obey the equations [0 0 0; 0 0 -1; 0 1 0] [x1; x2; x3] = 0 Thus any vector of the form [x1; 0; 0] is acceptable, as expected. It is conventional to use the freedom in scale to normalize the eigenvectors. Thus in this case a choice is |ω = 0> = |x̂> = [1; 0; 0]

I say a choice, and not the choice, since the vector may be multiplied by a number of modulus unity without changing the norm. There is no universally accepted convention for eliminating this freedom, except perhaps to choose the vector with real components when possible.

Note that of the three simultaneous equations above, the first is not a real equation. In general, there will be only (n−1) LI equations. This is the reason the norm of the vector is not fixed and, as shown in Appendix A.1, the reason the determinant vanishes.

Consider next the equations corresponding to ω = i. The components of the eigenvector obey the equations (1 − i)x1 = 0 (i.e., x1 = 0)

−x3 = 0 (i.e., x3 = 0)

x2 − i x3 = 0 (i.e., x2 = i x3)

Notice once again that we have only n−1 useful equations. A properly normalized solution to the above is |ω = i> = (1/√2) [0; 1; i]

A similar procedure yields the third eigenvector: |ω = −i> = (1/√2) [0; 1; -i]

In the above example we have introduced a popular convention: labeling the eigenvectors by the eigenvalue. For instance, the ket corresponding to ω = ω_i is labeled |ω = ω_i> or simply |ω_i>. This notation presumes that to each ω_i there is just one vector labeled by it. Though this is not always the case, only a slight change in this notation will be needed to cover the general case.

The phenomenon of a single eigenvalue representing more than one eigenvector is called degeneracy and corresponds to repeated roots for the characteristic polynomial. In the face of degeneracy, we need to modify not just the labeling, but also the procedure used in the example above for finding the eigenvectors. Imagine that instead of R(x̂π) we were dealing with another operator Ω on V3(R) with roots ω1 and ω2 = ω3. It appears as if we can get two eigenvectors, by the method described above, one for each distinct ω. How do we get a third? Or is there no third? These questions will be answered in all generality shortly when we examine the question of degeneracy in detail. We now turn our attention to two central theorems on Hermitian operators. These play a vital role in quantum mechanics.

Theorem 9. The eigenvalues of a Hermitian operator are real.

Proof Let Ω|ω> = ω|ω> Dot both sides with <ω| <ω|Ω|ω> = ω<ω|ω> (1.8.11)

Take the adjoint to get <ω|Ω†|ω> = ω*<ω|ω> Since Ω = Ω†, this becomes <ω|Ω|ω> = ω*<ω|ω> Subtracting from Eq. (1.8.11)

0 = (ω − ω*)<ω|ω> ω = ω* Q.E.D.

Theorem 10. To every Hermitian operator Ω, there exists (at least) a basis consisting of its orthonormal eigenvectors. It is diagonal in this eigenbasis and has its eigenvalues as its diagonal entries.

Proof Let us start with the characteristic equation. It must have at least one root, call it ω1. Corresponding to ω1 there must exist at least one nonzero eigenvector |ψ₁⟩. [If not, Theorem (A.1.1) would imply that (Ω - ω₁I) is invertible.] Consider the subspace V_{n-1} of all vectors orthogonal to |ψ₁⟩. Let us choose as our basis the vector |ψ₁⟩ (normalized to unity) and any n-1 orthonormal vectors {|ψ_1', ψ_2', ..., ψ_{n-1}'} in V_{n-1}. In this basis Ω has the following form:

Ω = | ω₁  0    0    ... 0   | |  0   *    *    ... *   | |  0   *    *    ... *   | |  .   .    .        .   | |  0   *    *    ... *   |

(1.8.12)

The first column is just the image of |ψ₁⟩ after Ω has acted on it. Given the first column, the first row follows from the Hermiticity of Ω.

The characteristic equation now takes the form

(ω - ω₁) × (determinant of boxed submatrix) = 0

or (ω₁ - ω) ∏_{m=2}^{n} (ω - ω_m) = 0

Now the polynomial P_{n-1} must also generate one root, ω₂, and a normalized eigenvector |ψ₂⟩. Define the subspace V_{n-1,2} of vectors in V_{n-1} orthogonal to |ψ₂⟩ (and automatically to |ψ₁⟩) and repeat the same procedure as before. Finally, the matrix Ω becomes, in the basis {|ψ₁⟩, |ψ₂⟩, ...}:

Ω = | ω₁  0    0    ... 0   | |  0   ω₂   0    ... 0   | |  0   0    ω₃   ... 0   | |  .   .    .        .   | |  0   0    0    ... ω_n |

Since every |ψ_i⟩ was chosen from a space that was orthogonal to the previous ones, ⟨ψ_i | ψ_j⟩ = δ_{ij} for i, j = 1, 2, ..., n; the basis of eigenvectors is orthonormal. (Notice that nowhere did we have to assume that the eigenvalues were all distinct.) Q.E.D.

[The analogy between real numbers and Hermitian operators is further strengthened by the fact that in a certain basis (of eigenvectors) the Hermitian operator can be represented by a matrix with all real elements.]

In stating Theorem 10, it was indicated that there might exist more than one basis of eigenvectors that diagonalized Ω. This happens if there is any degeneracy. Suppose ω₁ = ω₂ = ω. Then we have two orthonormal vectors obeying

Ω |ψ₁⟩ = ω |ψ₁⟩ Ω |ψ₂⟩ = ω |ψ₂⟩

It follows that

Ω [α |ψ₁⟩ + β |ψ₂⟩] = ω [α |ψ₁⟩ + β |ψ₂⟩]

for any α and β. Since the vectors |ψ₁⟩ and |ψ₂⟩ are orthogonal (and hence LI), we find that there is a whole two-dimensional subspace spanned by |ψ₁⟩ and |ψ₂⟩, the elements of which are eigenvectors of Ω with eigenvalue ω. One refers to this space as an eigenspace of Ω with eigenvalue ω. Besides the vectors |ψ₁⟩ and |ψ₂⟩, there exists an infinity of orthonormal pairs |ψ_a⟩, |ψ_b⟩, obtained by a rigid rotation of |ψ₁⟩, |ψ₂⟩, from which we may select any pair in forming the eigenbasis of Ω.

In general, if an eigenvalue occurs m_i times, that is, if the characteristic equation has m_i of its roots equal to some ω_i, there will be an eigenspace V_{n,m_i} from which we may choose any m_i orthonormal vectors to form the basis referred to in Theorem 10.

In the absence of degeneracy, we can prove Theorem 9 and 10 very easily. Let us begin with two eigenvectors:

Ω |ψ_i⟩ = ω_i |ψ_i⟩ (1.8.13a)

Ω |ψ_j⟩ = ω_j |ψ_j⟩ (1.8.13b)

Dotting the first with ⟨ψ_i| and the second with ⟨ψ_i|, we get

⟨ψ_i| Ω |ψ_i⟩ = ω_i ⟨ψ_i|ψ_i⟩ (1.8.14a)

⟨ψ_i| Ω |ψ_j⟩ = ω_j ⟨ψ_i|ψ_j⟩ (1.8.14b)

Taking the adjoint of the last equation and using the Hermitian nature of Ω, we get

⟨ψ_j| Ω |ψ_i⟩ = ω_j* ⟨ψ_j|ψ_i⟩

Subtracting this equation from Eq. (1.8.14a), we get

0 = (ω_i - ω_j) ⟨ψ_i|ψ_j⟩ (1.8.15)

If i=j, we get, since ⟨ψ_i | ω_i⟩ = 1,

1 = 1 (1.8.16)

If i ≠ j, we get

0 = ⟨ψ_i | ψ_j⟩ (1.8.17)

since ω_i - ω_j* = ω_i - ω_j ≠ 0 by assumption. That the proof of orthogonality breaks down for ω_i = ω_j is not surprising, for two vectors labeled by a degenerate eigenvalue could be any two members of the degenerate space which need not necessarily be orthogonal. The modification of this proof in this case of degeneracy calls for arguments that are essentially the ones used in proving Theorem 10. The advantage in the way Theorem 10 was proved first is that it suffers no modification in the degenerate case.

Degeneracy We now address the question of degeneracy as promised earlier. Now, our general analysis of Theorem 10 showed us that in the face of degeneracy, we have not one, but an infinity of orthonormal eigenbases. Let us see through an example how this variety manifests itself when we look for eigenvectors and how it is to be handled.

Example 1.8.5. Consider an operator Ω with matrix elements

Ω = | 1 0 1 | | 0 2 0 | | 1 0 1 |

in some basis. The characteristic equation is

(ω - 2)² ω = 0 ω = 0, 2, 2

The vector corresponding to ω = 0 is found by the usual means to be

|ω = 0⟩ = |  0 | |  1 | * (1/√2)

| -1 |

The case ω = 2 leads to the following equations for the components of the eigenvector:

x₁ + x₃ = 0 0 = 0 x₁ - x₃ = 0

Now we have just one equation, instead of the two (n-1) we have grown accustomed to! This is a reflection of the degeneracy. For every extra appearance (besides the first) a root makes, it takes away one equation. Thus degeneracy permits us extra degrees of freedom besides the usual one (of normalization). The conditions

x₁ = x₃ x₂ arbitrary

define an ensemble of vectors that are perpendicular to the first, |ω = 0⟩, i.e., lie in a plane perpendicular to |ω = 0⟩. This is in agreement with our expectation that a twofold degeneracy should lead to a two-dimensional eigenspace. The freedom in x₂ (or more precisely, the ratio x₂/x₃) corresponds to the freedom of orientation in this plane. Let us arbitrarily choose x₂ = 1, to get a normalized eigenvector corresponding to ω = 2:

|ω = 2, first⟩ = | 1 | | 1 | * (1/√2)

| 1 |

The third vector is now chosen to lie in this plane and to be orthogonal to the second (being in this plane automatically makes it perpendicular to the first |ω = 0⟩):

|ω = 2, second⟩ = |  1 | |  0 | * (1/√2)

| -1 |

Clearly each distinct choice of the ratio x₂/x₃ gives us a distinct doublet of orthonormal eigenvectors with eigenvalue 2.

Notice that in the face of degeneracy, |ω_i⟩ no longer refers to a single ket but to a generic element of the eigenspace V_i. To refer to a particular element, we must use the symbol |ω_i, a⟩, where a labels the ket within the eigenspace. A natural choice of the label a will be discussed shortly.

We now consider the analogs of Theorems 9 and 10 for unitary operators.

Theorem 11. The eigenvalues of a unitary operator are complex numbers of unit modulus.

Theorem 12. The eigenvectors of a unitary operator are mutually orthogonal.

(We assume there is no degeneracy.)

Proof of Both Theorems (assuming no degeneracy). Let

U |u_i⟩ = u_i |u_i⟩ (1.8.18a)

and

U |u_j⟩ = u_j |u_j⟩ (1.8.18b)

If we take the adjoint of the second equation and dot each side with the corresponding side of the first equation, we get

⟨u_i| U† U |u_j⟩ = u_i* u_j ⟨u_i|u_j⟩

so that

(1 - u_i* u_j) ⟨u_i|u_j⟩ = 0 (1.8.19)

If i=j, we get, since ⟨u_i | u_i⟩ = 1,

1 - |u_i|² = 0 (1.8.20a)

while if i ≠ j,

⟨u_i | u_j⟩ = 0 (1.8.20b)

since |u_i| = 1. Q.E.D.

If U is degenerate, we can carry out an analysis parallel to that for the Hermitian operator Ω, with just one difference. Whereas in Eq. (1.8.12), the zeros of the first row followed from the zeros of the first column and Ω = Ω†, here they follow from the requirement that the sum of the modulus squared of the elements in each row adds up to 1. Since |u_{1i}| = 1, all the other elements in the first row must vanish.

Diagonalization of Hermitian Matrices Consider a Hermitian operator Ω on V(C) represented as a matrix in some orthonormal basis {|1⟩, ..., |i⟩, ..., |n⟩}. If we trade this basis for the eigenbasis {|ω₁⟩, ..., |ω_i⟩, ..., |ω_n⟩}, the matrix representing Ω will become diagonal. Now the operator U inducing the change of basis

|i⟩ = U |ω_i⟩ (1.8.21)

is clearly unitary, for it "rotates" one orthonormal basis into another. (If you wish you may apply our mnemonic to U and verify its unitary nature: its columns contain the components of the eigenvectors |ω_i⟩ that are orthonormal.) This result is often summarized by the statement:

Every Hermitian matrix on V(C) may be diagonalized by a unitary change of basis.

We may restate this result in terms of passive transformations as follows:

If Ω is a Hermitian matrix, there exists a unitary matrix U (built out of the eigenvectors of Ω) such that U† Ω U is diagonal.

Thus the problem of finding a basis that diagonalizes Ω is equivalent to solving its eigenvalue problem.

Exercise 1.8.1. (1) Find the eigenvalues and normalized eigenvectors of the matrix

Ω = | 1 3 1 | | 0 2 0 | | 0 1 4 |

(2) Is the matrix Hermitian? Are the eigenvectors orthogonal?

Exercise 1.8.2.* Consider the matrix

Ω = | 0 0 1 | | 0 0 0 | | 1 0 0 |

(1) Is it Hermitian?

(2) Find its eigenvalues and eigenvectors.

(3) Verify that U† Ω U is diagonal, U being the matrix of eigenvectors of Ω.

Exercise 1.8.3.* Consider the Hermitian matrix

Ω = (1/√3) * | 2  0  0 | | 0  0 -1 | | 0 -1  0 |

(1) Show that ω₁ = ω₂ = 1; ω₃ = 2.

(2) Show that |ω = 2⟩ is any vector of the form

| a₁ | | √2 a₂ | | -a₁ |   (normalized)

(3) Show that the ω = 1 eigenspace contains all vectors of the form

| a₂ + 2a₃ | / √(12)

| a₁ | | a₂ |

either by feeding ω = 1 into the equations or by requiring that the ω = 1 eigenspace be orthogonal to |ω = 2⟩.

Exercise 1.8.4. An arbitrary n x n matrix need not have n eigenvectors. Consider as an example

A = | 1  1 | | -1 -1 |

(1) Show that ω₁ = ω₂ = 0.

(2) By feeding in this value show we get only one eigenvector of the form

| a | | -a |

We cannot find another one that is LI.

Exercise 1.8.5.* Consider the matrix

U = | cos θ  sin θ | | -sin θ  cos θ |

(1) Show that it is unitary.

(2) Show that its eigenvalues are e^{iθ} and e^{-iθ}.

(3) Find the corresponding eigenvectors; show that they are orthogonal.

(4) Verify that U† U = I (diagonal matrix), where U is the matrix of eigenvectors of U.

Exercise 1.8.6.* (1) We have seen that the determinant of a matrix is unchanged under a unitary change of basis. Argue now that

det Ω = product of eigenvalues of Ω = ∏ ω_i

for a Hermitian or unitary Ω.

(2) Using the invariance of the trace under the same transformation, show that

Tr Ω = Σ ω_i

Exercise 1.8.7. By using the results on the trace and determinant from the last exercise, show that for a 2x2 Hermitian matrix, the characteristic equation may be written as

ω² - (Tr Ω) ω + (det Ω) = 0.

ast problem, show that the eigenvalues of the matrix are 3 and —1. Verify this by explicit computation. Note that the Hermitian nature of the matrix is an essential ingredient.

Exercise 1.8.8. Consider Hermitian matrices M₁, M₂, M₃, M₄ that obey MᵢMⱼ + MⱼMᵢ = 2δᵢⱼI for i,j = 1, . . . , 4 (1) Show that the eigenvalues of Mᵢ are ±1. (Hint: go to the eigenbasis of Mᵢ, and use the equation for i=j.)

(2) By considering the relation MᵢMⱼ = −MⱼMᵢ for i ≠ j show that Mᵢ are traceless. [Hint: Tr(A CB)=Tr(CBA).]

(3) Show that they cannot be odd-dimensional matrices.

Exercise 1.8.9. A collection of masses mₐ, located at rₐ and rotating with angular velocity ω around a common axis has an angular momentum L = Σ mₐ(rₐ × vₐ)

where vₐ = ω × rₐ is the velocity of mₐ. By using the identity A × (B × C) = B(A · C) − C(A · B)

show that each Cartesian component Lᵢ of L is given by Lᵢ = Σⱼ Iᵢⱼωⱼ; where Iᵢⱼ = Σₐ mₐ[rₐ²δᵢⱼ − (rₐ)ᵢ(rₐ)ⱼ]

or in Dirac notation |L⟩ = I |ω⟩ (1) Will the angular momentum and angular velocity always be parallel?

(2) Show that the moment of inertia matrix Iᵢⱼ is Hermitian.

(3) Argue now that there exist three directions for ω such that L and ω will be parallel. How are these directions to be found?

(4) Consider the moment of inertia matrix of a sphere. Due to the complete symmetry of the sphere, it is clear that every direction is its eigendirection for rotation. What does this say about the three eigenvalues of the matrix I?

Simultaneous Diagonalization of Two Hermitian Operators Let us consider next the question of simultaneously diagonalizing two Hermitian operators.

Theorem 13. If Ω and A are two commuting Hermitian operators, there exists (at least) a basis of common eigenvectors that diagonalizes them both.

Proof. Consider first the case where at least one of the operators is nondegenerate, i.e., to a given eigenvalue, there is just one eigenvector, up to a scale. Let us assume Ω is nondegenerate. Consider any one of its eigenvectors: Ω|ωᵢ⟩ = ωᵢ|ωᵢ⟩ Since [A, Ω] = 0, Ω A|ωᵢ⟩ = A Ω|ωᵢ⟩ = ωᵢ A|ωᵢ⟩ i.e., A|ωᵢ⟩ is an eigenvector of Ω with eigenvalue ωᵢ. Since this vector is unique up to a scale, A|ωᵢ⟩ = λᵢ|ωᵢ⟩ Thus |ωᵢ⟩ is also an eigenvector of A with eigenvalue λᵢ. Since every eigenvector of Ω is an eigenvector of A, it is evident that the basis |ωᵢ⟩ will diagonalize both operators. Since Ω is nondegenerate, there is only one basis with this property.

What if both operators are degenerate? By ordering the basis vectors such that the elements of each eigenspace are adjacent, we can get one of them, say Ω, into the form (Theorem 10)

diag[ω₁, ω₁, ..., ω₂, ω₂, ...]

Now this basis is not unique: in every eigenspace Vᵢ corresponding to the eigenvalue ωᵢ, there exists an infinity of bases. Let us arbitrarily pick in Vᵢ: a set |ωᵢ, α⟩ where the additional label α runs from 1 to mᵢ.

How does A appear in the basis? Although we made no special efforts to get A into a simple form, it already has a simple form by virtue of the fact that it commutes with Ω. Let us start by mimicking the proof in the nondegenerate case: Ω A|ωᵢ, α⟩ = A Ω|ωᵢ, α⟩ = ωᵢ A|ωᵢ, α⟩ However, due to the degeneracy of Ω, we can only conclude that A|ωᵢ, α⟩ lies in Vᵢ.

Now, since vectors from different eigenspaces are orthogonal [Eq. (1.8.15)], ⟨ωⱼ, β| A |ωᵢ, α⟩ = 0 if |ωᵢ, α⟩ and |ωⱼ, β⟩ are basis vectors such that ωᵢ ≠ ωⱼ. Consequently, in this basis, A is block diagonal, which is called a block diagonal matrix for obvious reasons. The block diagonal form of A reflects the fact that when A acts on some element |ωᵢ, α⟩ of the eigenspace Vᵢ, it turns it into another element of Vᵢ. Within each subspace i, A is given by a matrix Aᵢ, which appears as a block in the equation above. Consider a matrix Aᵢ in Vᵢ. It is Hermitian since A is. It can obviously be diagonalized by trading the basis |ωᵢ, 1⟩, |ωᵢ, 2⟩, ..., |ωᵢ, mᵢ⟩ in Vᵢ that we started with, for the eigenbasis of A. Let us make such a change of basis in each eigenspace, thereby rendering A diagonal. Meanwhile what of Ω? It remains diagonal of course, since it is indifferent to the choice of orthonormal basis in each degenerate eigenspace. If the eigenvalues of A in subspace i are λᵢ⁽¹⁾, λᵢ⁽²⁾, ..., λᵢ⁽ᵐⁱ⁾ then we end up with Ω → diag[ω₁, ..., ω₁, ω₂, ..., ω₂, ...]

A → diag[λ₁⁽¹⁾, λ₁⁽²⁾, ..., λ₁⁽ᵐ¹⁾, λ₂⁽¹⁾, λ₂⁽²⁾, ..., λ₂⁽ᵐ²⁾, ...]

Q.E.D.

If A is not degenerate within any given subspace, for any k, l, and i, the basis we end up with is unique: the freedom Ω gave us in each eigenspace is fully eliminated by A. The elements of this basis may be named uniquely by the pair of indices ω and λ, as |ω, λ⟩, with λ playing the role of the extra label α. If A is degenerate within an eigenspace of Ω, if say λ₁⁽¹⁾ = λ₁⁽²⁾, there is a two-dimensional eigenspace from which we can choose any two orthonormal vectors for the common basis. It is then necessary to bring in a third operator F, that commutes with both Ω and A, and which will be nondegenerate in this subspace. In general, one can always find, for finite n, a set of operators {Ω, A, F, . . . } that commute with each other and that nail down a unique, common, eigenbasis, the elements of which may be labeled unambiguously as |ω, λ, φ, . . . ⟩. In our study of quantum mechanics it will be assumed that such a complete set of commuting operators exists if n is infinite.

Exercise 1.8.10. By considering the commutator, show that the following Hermitian matrices may be simultaneously diagonalized. Find the eigenvectors common to both and verify that under a unitary transformation to this basis, both matrices are diagonalized.

Ω = [1 0; 0 0], A = [0 1; 1 0]

Since Ω is degenerate and A is not, you must be prudent in deciding which matrix dictates the choice of basis.

Example 1.8.6. We will now discuss, in some detail, the complete solution to a problem in mechanics. It is important that you understand this example thoroughly, for it not only illustrates the use of the mathematical techniques developed in this chapter but also contains the main features of the central problem in quantum mechanics.

The mechanical system in question is depicted in Fig. 1.5. The two masses m are coupled to each other and the walls by springs of force constant k. If x₁ and x₂ measure the displacements of the masses from their equilibrium points, these coordinates obey the following equations, derived through an elementary application of Newton's laws: m d²x₁/dt² = -2k x₁ + k x₂ (1.8.24a)

m d²x₂/dt² = k x₁ - 2k x₂ (1.8.24b)

Figure 13. The coupled mass problem. All masses are m, all spring constants are k, and the displacements of the masses from equilibrium are x₁ and x₂.

The problem is to find x₁(t) and x₂(t) given the initial-value data, which in this case consist of the initial positions and velocities. If we restrict ourselves to the case of zero initial velocities, our problem is to find x₁(t) and x₂(t), given x₁(0) and x₂(0).

In what follows, we will formulate the problem in the language of linear vector spaces and solve it using the machinery developed in this chapter. As a first step, we rewrite Eq. (1.8.24) in matrix form: d²/dt² |x⟩ = Ω |x⟩ (1.8.25a)

where Ω = [-2k/m, k/m; k/m, -2k/m]

or in Dirac notation d²/dt² |x(t)⟩ = Ω |x(t)⟩ (1.8.26)

The abstract form of Eq. (1.8.26) is d²/dt² |x(t)⟩ = Ω |x(t)⟩ (1.8.26)

Equation (1.8.25a) is obtained by projecting Eq. (1.8.26) on the basis vectors |1⟩, |2⟩, which have the following physical significance: |1⟩ = [1; 0] (first mass displaced by unity, second mass undisplaced) (1.8.27a)

|2⟩ = [0; 1] (first mass undisplaced, second mass displaced by unity) (1.8.27b)

An arbitrary state, in which the masses are displaced by x₁ and x₂, is given in this basis by |x⟩ = |1⟩x₁ + |2⟩x₂ (1.8.28)

The abstract counterpart of the above equation is |x⟩ = |1⟩x₁ + |2⟩x₂ (1.8.29)

It is in this |1⟩, |2⟩ basis that Ω is represented by the matrix appearing in Eq. (1.8.25), with elements —2k / m, k/m, etc.

The basis |1⟩, |2⟩ is very desirable physically, for the components of |x⟩ in this basis (x₁ and x₂) have the simple interpretation as displacements of the masses. However, from the standpoint of finding a mathematical solution to the initial-value problem, it is not so desirable, for the components x₁ and x₂ obey the coupled differential equations (1.8.24a) and (1.8.24b). The coupling is mediated by the off-diagonal matrix elements Ω₁₂ = Ω₂₁ = k/m.

Having identified the problem with the |1⟩, |2⟩ basis, we can now see how to get around it: we must switch to a basis in which Ω is diagonal. The components of |x⟩ in this basis will then obey uncoupled differential equations which may be readily solved. Having found the solution, we can return to the physically preferable |1⟩, |2⟩ basis. This, then, is our broad strategy and we now turn to the details.

From our study of Hermitian operators we know that the basis that diagonalizes Ω is the basis of its normalized eigenvectors. Let |I⟩ and |II⟩ be its eigenvectors defined by Ω|I⟩ = -ω₁²|I⟩ (1.8.30a)

Ω|II⟩ = -ω₂²|II⟩ (1.8.30b)

We are departing here from our usual notation: the eigenvalue of Ω is written as -ω² rather than as ω in anticipation of the fact that Ω has eigenvalues of the form -ω², with ω real. We are also using the symbols |I⟩ and |II⟩ to denote what should be called | -ω₁²⟩ and | -ω₂²⟩ in our convention.

It is a simple exercise (which you should perform) to solve the eigenvalue problem of Ω in the |1⟩, |2⟩ basis (in which the matrix elements of Ω are known) and to obtain ω₁ = √(k/m), |I⟩ = (1/√2)(|1⟩ + |2⟩)

ω₂ = √(3k/m), |II⟩ = (1/√2)(|1⟩ - |2⟩)

R² = [11 (I → m), 4 + 21 — (0114 1] /2

If we now expand the vector |x(t)> in this new basis as |x(t)> = |I>xI(t) + |II>xII(t) (1.8.32)

[in analogy with Eq. (1.8.29)], the components xI and xII will evolve as follows: [RI cos ωI t - 0 XI0]

[RII 0 cos ωII XII]

= [ (1.8.33)

-0011 XII

We obtain this equation by rewriting Eq. (1.8.24) in the |I>, |II> basis in which Ω has its eigenvalues as the diagonal entries, and in which |x> has components xI and xII. Alternately we can apply the operator d² / dr² to both sides of the expansion of Eq. (1.8.32), and get 0 = D(56 + (ω²xI) + I +(ω² xII) (1.8.34)

Since |I> and |II> are orthogonal, each coefficient is zero.

The solution to the decoupled equations + ω²i xi = 0, i = I, II (1.8.35)

subject to the condition of vanishing initial velocities, is xi(t)=xi(0) cos ωi t, i= I, II (1.8.36)

As anticipated, the components of |x> in the |I>, |II> basis obey decoupled equations that can be readily solved. Feeding Eq. (1.8.36) into Eq. (1.8.32) we get |x(t)> = |I>xI(0) cos ωI t + |II>xII(0) cos ωII t (1.8.37a)

= |I><I|x(0)> cos ωI t + |II><II|x(0)> cos ωII t (1.8.37b)

Equation (1.8.37) provides the explicit solution to the initial-value problem. It corresponds to the following algorithm for finding |x(t)> given |x(0)>.

Step (1). Solve the eigenvalue problem of Ω.

Step (2). Find the coefficients xI(0) = <I|x(0)> and xII(0) = <II|x(0)> in the expansion |x(0)> = |I>xI(0) + |II >xII(0)

Step (3). Append to each coefficient xi(0) (i = I, II) a time dependence cos ωi t to get the coefficients in the expansion of |x(t)>.

Let me now illustrate this algorithm by solving the following (general) initial-value problem: Find the future state of the system given that at t= 0 the masses are displaced by x1(0) and x2(0).

Step (1). We can ignore this step since the eigenvalue problem has been solved [Eq. (1.8.31)].

Step (2).

xI(0)= <I|x(0)> = (1, 1) [x1(0) + x2(0)] / (2√2)

xII(0) = <II|x(0)> = (1, -1) [x1(0) - x2(0)] / (2√2)

Step (3).

|x(t)>=|I> [x1(0) + x2(0)] / (2√2) * cos ωI t + |II> [x1(0) - x2(0)] / (2√2) * cos ωII t The explicit solution above can be made even more explicit by projecting |x(t)> onto the |1>, |2> basis to find x1(t) and x2(t), the displacements of the masses. We get (feeding in the explicit formulas for ωI and ωII)

x1(t)= <1|x(t)> = <1|I> [x1(0) + x2(0)] / (2√2) * cos (k/m)¹/² t + <1|II> [x1(0) - x2(0)] / (2√2) * cos (3k/m)¹/² t = [x1(0) + x2(0)] / 2 * cos (k/m)¹/² t + [x1(0) - x2(0)] / 2 * cos (3k/m)¹/² t (1.8.38a)

using the fact that <1|I>= <I|1> = 1/2¹/² It can likewise be shown that x2(t) = [x1(0) + x2(0)] / 2 * cos (k/m)¹/² t - [x1(0) - x2(0)] / 2 * cos (3k/m)¹/² t (1.8.38b)

We can rewrite Eq. (1.8.38) in matrix form as [ x1(t) ]   [  (cos [(k/m)¹/²t] + cos [(3k/m)¹/²t])/2    (cos [(k/m)¹/²t] - cos [(3k/m)¹/²t])/2 ]   [ x1(0) ]

[ x2(t) ] = [  (cos [(k/m)¹/²t] - cos [(3k/m)¹/²t])/2    (cos [(k/m)¹/²t] + cos [(3k/m)¹/²t])/2 ] * [ x2(0) ]

(1.8.39)

This completes our determination of the future state of the system given the initial state.

The Propagator There are two remarkable features in Eq. (1.8.39): (1) The final-state vector is obtained from the initial-state vector upon multiplication by a matrix.

(2) This matrix is independent of the initial state. We call this matrix the propagator.

Finding the propagator is tantamount to finding the complete solution to the problem, for given any other initial state with displacements x1(0) and x2(0), we get x1(t) and x2(t) by applying the same matrix to the initial-state vector.

We may view Eq. (1.8.39) as the image in the |1>, |2> basis of the abstract relation |x(t)> = U(t)|x(0)> (1.8.40)

By comparing this equation with Eq. (1.8.37b), we find the abstract representation of U: U(t)= |I><I| cos ωI t+ |II><II| cos ωII t (1.8.41a)

= Σ |i><i| cos ωi t (1.8.41b)

i=I You may easily convince yourself that if we take the matrix elements of this operator in the |1>, |2> basis, we regain the matrix appearing in Eq. (1.8.39). For example U11= <1|U|1> = <1| { |I><I| cos (k/m)¹/² t + |II><II| cos (3k/m)¹/² t } |1> = <1|I><I|1> cos (k/m)¹/² t + <1|II><II|1> cos (3k/m)¹/² t = (1/√2)(1/√2) cos (k/m)¹/² t + (1/√2)(-1/√2) cos (3k/m)¹/² t = [cos (k/m)¹/² t - cos (3k/m)¹/² t] / 2

Notice that U(t) [Eq. (1.8.41)] is determined completely by the eigenvectors and eigenvalues of Ω. We may then restate our earlier algorithm as follows. To solve the equation i ħ d/dt |ψ> = Ω |ψ> (1) Solve the eigenvalue problem of Ω.

(2) Construct the propagator U in terms of the eigenvalues and eigenvectors.

(3) |x(t)>= U(t)|x(0)>.

The Normal Modes There are two initial states |x(0)> for which the time evolution is particularly simple. Not surprisingly, these are the eigenkets |I> and |II>. Suppose we have |x(0)>=|I>. Then the state at time t is |ψ(t)> = U(t)|I> = (|I><I| cos ωI t + |II><II| cos ωII t) |I> = |I> cos ωI t (1.8.42)

Thus the system starting off in |I> is only modified by an overall factor cos ωI t. A similar remark holds with |II>. These two modes of vibration, in which all (two) components of a vector oscillate in step are called normal modes.

The physics of the normal modes is clear in the |1>, |2> basis. In this basis |I> = [1, 1]ᵀ / √2 and corresponds to a state in which both masses are displaced by equal amounts. The middle spring is then a mere spectator and each mass oscillates with a frequency ωI = (k/m)¹/² in response to the end spring nearest to it. Consequently |I(t)> = [ cos [(k/m)¹/² t], cos [(k/m)¹/² t] ]ᵀ / √2 On the other hand, if we start with |II> = [1, -1]ᵀ / √2 the masses are displaced by equal and opposite amounts. In this case the middle spring is distorted by twice the displacement of each mass. If the masses are displaced by A and —A, respectively, each mass feels a restoring force of 3kA (2kA from the middle spring and kA from the end spring nearest to it). Since the effective force constant is keff= 3kA/A = 3k, the vibrational frequency is (3k/m)¹/² and |II(t)> = [ cos [(3k/m)¹/² t], -cos [(3k/m)¹/² t] ]ᵀ / √2 If the system starts off in a linear combination of |I> and |II> it evolves into the corresponding linear combination of the normal modes |I(t)> and |II(t)>. This is the content of the propagator equation |x(t)> = U(t)|x(0)> = |I><I|x(0)> cos ωI t+ |II><II|x(0)> cos ωII t = |I(t)> <I|x(0)> + |II(t)> <II|x(0)> Another way to see the simple evolution of the initial states |I> and |II> is to determine the matrix representing U in the |I>, |II> basis: U |I,II> = [ cos ωI t    0 ]

[ 0           cos ωII t ] (1.8.43)

You should verify this result by taking the appropriate matrix elements of U(t) in Eq. (1.8.41b). Since each column above is the image of the corresponding basis vectors (|I> or |II>) after the action of U(t), (which is to say, after time evolution), we see that the initial states |I> and |II> evolve simply in time.

The central problem in quantum mechanics is very similar to the simple example that we have just discussed. The state of the system is described in quantum theory by a ket |ψ> which obeys the Schrödinger equation i ħ d/dt |ψ> = H |ψ> where ħ is a constant related to Planck's constant h by ħ= h/2π, and H is a Hermitian operator called the Hamiltonian. The problem is to find |ψ(t)> given |ψ(0)>. [Since the equation is first order in t, no assumptions need be made about |ψ̇(0)>, which is determined by the Schrödinger equation to be ( — i/ħ)H|ψ (0)>.]

In most cases, H is a time-independent operator and the algorithm one follows in solving this initial-value problem is completely analogous to the one we have just seen: Step (1). Solve the eigenvalue problem of H.

Step (2). Find the propagator U(t) in terms of the eigenvectors and eigenvalues of H.

Step (3). |ψ(t)> = U(t)|ψ(0)>.

You must of course wait till Chapter 4 to find out the physical interpretation of |ψ>, the actual form of the operator H, and the precise relation between U(t) and the eigenvalues and eigenvectors of H.

Exercise 1.8.11. Consider the coupled mass problem discussed above.

(1) Given that the initial state is |1>, in which the first mass is displaced by unity and the second is left alone, calculate |ψ(0)> by following the algorithm.

(2) Compare your result with that following from Eq. (1.8.39).

Exercise 1.8.12. Consider once again the problem discussed in the previous example. (1) Assuming that i ħ d/dt |x> = Ω |x> has a solution |x(t)> = U(t)|x(0)> find the differential equation satisfied by U(t). Use the fact that |x(0)> is arbitrary.

(2) Assuming (as is the case) that Ω and U can be simultaneously diagonalized, solve for the elements of the matrix U in this common basis and regain Eq. (1.8.43). Assume

1.9. Functions of Operators and Related Concepts We have encountered two types of objects that act on vectors: scalars, which commute with each other and with all operators; and operators, which do not generally commute with each other. It is customary to refer to the former as c numbers and the latter as q numbers. Now, we are accustomed to functions of c numbers such as sin(x), log(x), etc. We wish to examine the question whether functions of q numbers can be given a sensible meaning. We will restrict ourselves to those functions that can be written as a power series. Consider a series f(x)= Σ an xⁿ (1.9.1)

n = 0 where x is a c number. We define the same function of an operator or q number to be f(Ω ) = Σ an Ωⁿ (1.9.2)

n = 0 This definition makes sense only if the sum converges to a definite limit. To see what this means, consider a common example: exp Ω = Σ Ωⁿ / n! (1.9.3)

n=0 Let us restrict ourselves to Hermitian operators. By going to the eigenbasis of Ω we can readily perform the sum of Eq. (1.9.3). Since

(1.9.4)

and

(1.9.5)

(1.9.6)

Since each sum converges to the familiar limit, the operator exp(Ω) is indeed well defined by the power series in this basis (and therefore in any other).

Exercise 1.9.1.* We know that the series

f(x) = Σ xⁿ

n=0

may be equated to the function f(x) = (1 − x)⁻¹ if |x| < 1. By going to the eigenbasis, examine when the g-number power series

Σ (Ωⁿ)/n!

n=0

of a Hermitian operator Ω may be identified with (1 − Ω)⁻¹.

Exercise 1.9.2.* If H is a Hermitian operator, show that U = exp(iH) is unitary. (Notice the analogy with c-numbers: if θ is real, u = e^(iθ) is a number of unit modulus.)

Exercise 1.9.3. For the case above, show that det U = 1.

**Derivatives of Operators with Respect to Parameters**

Consider next an operator O(λ) that depends on a parameter λ. Its derivative with respect to λ is defined to be

dO(λ)/dλ = lim_{Δλ→0} [O(λ + Δλ) − O(λ)] / Δλ.

If O(λ) is written as a matrix in some basis, then the matrix representing dO(λ)/dλ is obtained by differentiating the matrix elements of O(λ). A special case of O(λ) we are interested in is

exp(λΩ)

where Ω is Hermitian. We can show, by going to the eigenbasis of Ω, that

d exp(λΩ)/dλ = Ω exp(λΩ) = exp(λΩ) Ω. (1.9.7)

The same result may be obtained, even if Ω is not Hermitian, by working with the power series, provided it exists:

d/dλ Σ (λⁿ Ωⁿ)/n! = Σ (n λⁿ⁻¹ Ωⁿ)/n! = Σ (λⁿ⁻¹ Ωⁿ)/(n−1)! = Ω Σ (λᵐ Ωᵐ)/m! = Ω exp(λΩ)

n=0 n=1 m=0

Conversely, we can say that if we are confronted with the differential Eq. (1.9.7), its solution is given by

O(λ) = c exp(λΩ)

(It is assumed here that the exponential exists.) In the above, c is a constant (operator) of integration. The solution O = exp(λΩ) corresponds to the choice c = I.

In all the above operations, we see that Ω behaves as if it were just a c-number. Now, the real difference between c-numbers and g-numbers is that the latter do not generally commute. However, if only one g-number (or powers of it) enters the picture, everything commutes and we can treat them as c-numbers. If one remembers this mnemonic, one can save a lot of time.

If, on the other hand, more than one g-number is involved, the order of the factors is all important. For example, it is true that

exp(α + β) = exp(α) exp(β)

as may be verified by a power-series expansion, while it is not true that

exp(α) exp(β) = exp(α + β)

or that

exp(α) exp(β) exp(γ) = exp(α + β + γ)

unless [Ω, Θ] = 0. Likewise, in differentiating a product, the chain rule is

d/dλ [exp(λΩ) exp(λΘ)] = Ω exp(λΩ) exp(λΘ) + exp(λΩ) Θ exp(λΘ). (1.9.8)

We are free to move Ω through exp(λΩ) and write the first term as Ω exp(λΩ) exp(λΘ)

but not as exp(λΩ) Ω exp(λΘ)

unless [Ω, Θ] = 0.

**1.10. Generalization to Infinite Dimensions**

In all of the preceding discussions, the dimensionality (n) of the space was unspecified but assumed to be some finite number. We now consider the generalization of the preceding concepts to infinite dimensions.

Let us begin by getting acquainted with an infinite-dimensional vector. Consider a function defined in some interval, say, a < x < b. A concrete example is provided by the displacement f(x, t) of a string clamped at x = 0 and x = L (Fig. 1.6). Suppose we want to communicate to a person on the moon the string's displacement f(x), at some time t. One simple way is to divide the interval 0−L into 20 equal parts, measure the displacement f(xᵢ) at the 19 points x = L/20, 2L/20, . . . , 19L/20, and transmit the 19 values on the wireless. Given these f(xᵢ), our friend on the moon will be able to reconstruct the approximate picture of the string shown in Fig. 1.7.

If we wish to be more accurate, we can specify the values of f(x) at a larger number of points. Let us denote by fₙ(x) the discrete approximation to f(x) that coincides with it at n points and vanishes in between. Let us now interpret the ordered n-tuple {fₙ(x₁), fₙ(x₂), ..., fₙ(xₙ)} as components of a ket |fₙ⟩ in a vector space Vₙ:

|fₙ⟩ (1.10.1)

Figure 1.6. The string is clamped at x = 0 and x = L. It is free to oscillate in the plane of the paper.

Figure 1.7. The string as reconstructed by the person on the moon.

The basis vectors in this space are

|xᵢ⟩ (1.10.2)

corresponding to the discrete function which is unity at x = xᵢ and zero elsewhere. The basis vectors satisfy

⟨xᵢ | xⱼ⟩ = δᵢⱼ (orthogonality) (1.10.3)

Σ |xᵢ⟩⟨xᵢ| = I (completeness) (1.10.4)

i=1

Try to imagine a space containing n mutually perpendicular axes, one for each point xᵢ. Along each axis is a unit vector |xᵢ⟩. The function fₙ(x) is represented by a vector whose projection along the ith direction is fₙ(xᵢ):

|fₙ⟩ = Σ fₙ(xᵢ) |xᵢ⟩ (1.10.5)

To every possible discrete approximation gₙ(x), hₙ(x), etc., there is a corresponding ket |gₙ⟩, |hₙ⟩, etc., and vice versa. You should convince yourself that if we define vector addition as the addition of the components, and scalar multiplication as the multiplication of each component by the scalar, then the set of all kets representing discrete functions that vanish at x = 0, L and that are specified at n points in between, forms a vector space.

We next define the inner product in this space:

⟨fₙ|gₙ⟩ = Σ fₙ(xᵢ)gₙ(xᵢ) (1.10.6)

Two functions fₙ(x) and gₙ(x) will be said to be orthogonal if ⟨fₙ|gₙ⟩ = 0.

Let us now forget the man on the moon and consider the maximal specification of the string's displacement, by giving its value at every point in the interval 0−L. In this case f(x) is specified by an ordered infinity of numbers: an f(x) for each point x. Each function is now represented by a ket |f⟩ in an infinite-dimensional vector space and vice versa. Vector addition and scalar multiplication are defined just as before. Consider, however, the inner product. For finite n it was defined as

⟨fₙ|gₙ⟩ = Σ fₙ(xᵢ)gₙ(xᵢ)

i=1

in particular

⟨fₙ|fₙ⟩ = Σ |fₙ(xᵢ)|²

If we now let n go to infinity, so does the sum, for practically any function. What we need is the redefinition of the inner product for finite n in such a way that as n tends to infinity, a smooth limit obtains. The natural choice is of course

⟨fₙ|gₙ⟩ = Σ fₙ(xᵢ)gₙ(xᵢ) Δx, where Δx = L/(n + 1). (1.10.6')

If we now let n go to infinity, we get, by the usual definition of the integral,

⟨f|g⟩ = ∫ f*(x)g(x) dx (1.10.7)

⟨f|f⟩ = ∫ |f(x)|² dx (1.10.8)

If we wish to go beyond the instance of the string and consider complex functions of x as well, in some interval a < x < b, the only modification we need is in the inner product:

⟨f|g⟩ = ∫ f*(x)g(x) dx (1.10.9)

What are the basis vectors in this space and how are they normalized? We know that each point x gets a basis vector |x⟩. The orthogonality of two different axes requires that

⟨x|x'⟩ = 0, if x ≠ x' (1.10.10)

What if x = x'? Should we require, as in the finite-dimensional case, ⟨x|x⟩ = 1? The answer is no, and the best way to see it is to deduce the correct normalization. We start with the natural generalization of the completeness relation Eq. (1.10.4) to the case where the kets are labeled by a continuous index x' :

∫ |x'⟩⟨x'| dx' = I (1.10.11)

a to b

where, as always, the identity is required to leave each ket unchanged. Dotting both sides of Eq. (1.10.11) with some arbitrary ket |f⟩ from the right and the basis bra ⟨x| from the left,

⟨x| [∫ |x'⟩⟨x'| dx'] |f⟩ = ⟨x| I |f⟩ = ⟨x|f⟩. (1.10.12)

Now, ⟨x|f⟩, the projection of |f⟩ along the basis ket |x⟩, is just f(x). Likewise ⟨x'|f⟩ = f(x'). Let the inner product ⟨x|x'⟩ be some unknown function δ(x, x'). Since δ(x, x') vanishes if x ≠ x' we can restrict the integral to an infinitesimal region near x' = x in Eq. (1.10.12):

∫ δ(x, x') f(x') dx' = f(x) (1.10.13)

x−ε to x+ε

In this infinitesimal region, f(x') (for any reasonably smooth f) can be approximated by its value at x' = x, and pulled out of the integral:

f(x) ∫ δ(x, x') dx' = f(x) (1.10.14)

x−ε to x+ε

so that

∫ δ(x, x') dx' = 1. (1.10.15)

x−ε to x+ε

Clearly δ(x, x') cannot be finite at x' = x, for then its integral over an infinitesimal region would also be infinitesimal. In fact δ(x, x') should be infinite in such a way that its integral is unity. Since δ(x, x') depends only on the difference x − x', let us write it as δ(x − x'). The "function," δ(x − x'), with the properties

δ(x − x') = 0, if x ≠ x'

∫ δ(x − x') dx' = 1, for a < x < b (1.10.16)

is called the Dirac delta function and fixes the normalization of the basis vectors:

⟨x|x'⟩ = δ(x − x') (1.10.17)

It will be needed any time the basis kets are labeled by a continuous index such as x. Note that it is defined only in the context of an integration: the integral of the delta function δ(x − x') with any smooth function f(x') is f(x). One sometimes calls the delta function the sampling function, since it samples the value of the function f(x) at one point.

∫ δ(x − x') f(x') dx' = f(x) (1.10.18)

The delta function does not look like any function we have seen before, its values being either infinite or zero. It is therefore useful to view it as the limit of a more conventional function. Consider a Gaussian

g_λ(x − x') = (1/√(2πλ²)) exp[−(x − x')²/(2λ²)] (1.10.19)

as shown in Fig. 1.8a. The Gaussian is centered at x'=x, has width λ, maximum height (2πλ²)^(−1/2), and unit area, independent of λ. As λ approaches zero, g_λ becomes a better and better approximation to the delta function.

It is obvious from the Gaussian model that the delta function is even. This may be verified as follows:

δ(x − x') = ⟨x|x'⟩ i x'> = <x'lx>* = δ(x' — x)* = δ(x' — x) since the delta function is real.

Consider next an object that is even more peculiar than the delta function: its derivative with respect to the first argument x: δ(x — x') = — — δ(x — x') (1.10.20)

dx dx'

What is the action of this function under the integral? The clue comes from the Gaussian model. Consider dδ_A(x— x')/ dx= —dδ_A(x — x')/ dx' as a function of x'. As Λ shrinks, each bump at ± E will become, up to a scale factor, the δ function. The first one will sample — f(x — E) and the second one +f (x + E), again up to a scale, so that δ '(x — x') f(x) dx' = —df(x)/dx The constant of proportionality happens to be 1/2ε so that ∫ δ '(x — x') f(x) dx' = —df(x)/dx (1.10.21)

This result may be verified as follows: ∫ δ '(x — x') f(x) dx' = d/dx [ ∫ δ(x — x') f(x) dx' ] = d/dx [f(x)] = —f(x)/dx

Note that δ '(x — x') is an odd function. This should be clear from Fig. 1.8b or Eq. (1.10.20). An equivalent way to describe the action of the δ' function is by the equation δ'(x — x') = δ(x — x') — (1.10.22)

where it is understood that both sides appear in an integral over x' and that the differential operator acts on any function that accompanies the δ' function in the integrand. In this notation we can describe the action of higher derivatives of the delta function: d"δ(x — x')/dx" = δ(x — x') (1.10.23)

We will now develop an alternate representation of the delta function. We know from basic Fourier analysis that, given a function f(x), we may define its transform f(k)= 1/(2π)^{1/2} ∫ e^{-ikx} f(x) dx (1.10.24)

and its inverse f(x') = 1/(2π)^{1/2} ∫ e^{ikx'} f(k) dk (1.10.25)

Feeding Eq. (1.10.24) into Eq. (1.10.25), we get f(x') = 1/(2π) ∫ dk e^{ik(x'-x)} f(x) dx Comparing this result with Eq. (1.10.18), we see that ∫ dk e^{ik(x'-x)} = δ(x' — x) (1.10.26)

Exercise 1.10.1.* Show that δ(ax) = δ(x)/|a|. [Consider ∫ δ(ax) d(ax). Remember that δ(x)= δ(—x).]

Exercise 1.10.2.* Show that δ(f(x)) = Σ_i |1/f'(x_i)| δ(x - x_i) where x_i are the zeros of f(x). Hint: Where does δ(f(x)) blow up? Expand f(x) near such points in a Taylor series, keeping the first nonzero term.

Exercise 1.10.3.* Consider the theta function θ(x— x') which vanishes if x — x' is negative and equals 1 if x — x' is positive. Show that δ(x — x')= d/dx θ(x— x').

Operators in Infinite Dimensions Having acquainted ourselves with the elements of this function space, namely, the kets |f> and the basis vectors |x>, let us turn to the (linear) operators that act on them. Consider the equation Ω |f> = |f̃> Since the kets are in correspondence with the functions, Ω takes the function f(x) into another, f̃(x). Now, one operator that does such a thing is the familiar differential operator, which, acting on f(x), gives f̃(x)=df(x)/dx. In the function space we can describe the action of this operator as D |f> = |df/dx> where |df/dx> is the ket corresponding to the function df/dx. What are the matrix elements of D in the |x> basis? To find out, we dot both sides of the above equation with <x| , <x| D |f> = <x| df/dx> = df(x)/dx and insert the resolution of identity at the right place ∫ <x| D |x'> <x'| f > dx' = df/dx (1.10.27)

Comparing this to Eq. (1.10.21), we deduce that <x| D |x'>= D_{x,x'}= δ'(x— x')= δ(x— x') d/dx' (1.10.28)

It is worth remembering that D_{x,x'} = δ'(x — x') is to be integrated over the second index (x') and pulls out the derivative of f at the first index (x). Some people prefer to integrate δ'(x — x') over the first index, in which case it pulls out —df/dx'. Our convention is more natural if one views D_{x,x'} as a matrix acting to the right on the components f(x'),f(x') of a vector |f>. Thus the familiar differential operator is an infinite-dimensional matrix with the elements given above. Normally one doesn't think of D as a matrix for the following reason. Usually when a matrix acts on a vector, there is a sum over a common index. In fact, Eq. (1.10.27) contains such a sum over the index x'. If, however, we feed into this equation the value of D_{x,x'}, the delta function renders the integration trivial: ∫ δ(x — x') [df(x')/dx'] dx' = df/dx at x'= x.

Thus the action of D is simply to apply d/dx to f(x) with no sum over a common index in sight. Although we too will drop the integral over the common index ultimately, we will continue to use it for a while to remind us that D, like all linear operators, is a matrix.

Let us now ask if D is Hermitian and examine its eigenvalue problem. If D were Hermitian, we would have D_{x,x'} = D_{x',x}^* But this is not the case: D_{x,x'}= δ'(x — x')

while D_{x',x}^*= [δ'(x' — x)]* = δ'(x' — x)= —δ'(x — x')

But we can easily convert D to a Hermitian matrix by multiplying it with a pure imaginary number. Consider K= —iD which satisfies K_{x,x'} = [—iδ'(x' — x)]* = +iδ'(x' — x)= —iδ'(x— x')= K_{x',x}^* It turns out that despite the above, the operator K is not guaranteed to be Hermitian, as the following analysis will indicate. Let |f> and |g> be two kets in the function space, whose images in the X basis are two functions f(x) and g(x) in the interval a to b. If K is Hermitian, it must also satisfy <g| K |f>=<Kf|g>*=<f| K†|g>* =<f| K|g>* So we ask ∫∫ g*(x) <x| K |x'> f(x') dx dx' = ∫∫ [g*(x) (-i d/dx') δ(x - x') f(x')] dx dx' = -i ∫ g*(x) [df(x)/dx] dx Integrating the left-hand side by parts gives -i [g*(x)f(x)]_a^b + i ∫ (dg*(x)/dx) f(x) dx So K is Hermitian only if the surface term vanishes: —ig*(x)f(x) |_a^b = 0 (1.10.29)

In contrast to the finite-dimensional case, K_{x,x'} = K_{x',x}^* is not a sufficient condition for K to be Hermitian. One also needs to look at the behavior of the functions at the end points a and b. Thus K is Hermitian in the space consists of functions that obey Eq. (1.10.29). One set of functions that obey this condition are the possible configurations f(x) of the string clamped at x = 0, L, since f(x) vanishes at the end points. But condition (1.10.29) can also be fulfilled in another way. Consider functions in our own three-dimensional space, parametrized by r, θ, and φ (φ is the angle measured around the z axis). Let us require that these functions be single valued. In particular, if we start at a certain point and go once around the z axis, returning to the original point, the function must take on its original value, i.e., f(φ)=f(φ+2π)

In the space of such periodic functions, K= d/ dφ is a Hermitian operator. The surface term vanishes because the contribution from one extremity cancels that from the other: -i[g*(2π) f(2π) — g*(0) f(0)] = 0.

In the study of quantum mechanics, we will be interested in functions defined over the full interval —∞ <x< +∞. They fall into two classes, those that vanish as |x|→ ∞, and those that do not, the latter behaving as e^{ikx}, k being a real parameter that labels these functions. It is clear that K= d/dx is Hermitian when sandwiched between two functions of the first class or a function from each, since in either case the surface term vanishes. When sandwiched between two functions of the second class, the Hermiticity hinges on whether lim_{|x|→∞} e^{i(k-k')x} = 0.

If k= k', the contribution from one end cancels that from the other. If k ≠ k', the answer is unclear since e^{i(k-k')x} oscillates, rather than approaching a limit as |x|→ ∞.

Now, there exists a way of defining a limit for such functions that cannot make up their minds: the limit as |x|→ ∞ is defined to be the average over a large interval. According to this prescription, we have, say as x---*(x), lim_{x→∞} e^{ikx} — e^{ik'x} = lim_{L→∞} 1/L ∫_0^L e^{i(k-k')x} dx = 0 if k ≠ k' and so K is Hermitian in this space.

We now turn to the eigenvalue problem of K. The task seems very formidable indeed, for we have now to find the roots of an infinite-order characteristic polynomial and get the corresponding eigenvectors. It turns out to be quite simple and you might have done it a few times in the past without giving yourself due credit.

Let us begin with K|k>=k|k> (1.10.30)

Following the standard procedure, <x|K|k> = k<x|k> ∫ <x| K |x'> <x'| k> dx' = k ψ_k(x)

where by definition ψ_k(x)= <x | k>. This equation could have been written directly had we made the immediate substitution K= —i d/dx in the X basis. From now on we shall resort to this shortcut unless there are good reasons for not doing so.

The solution to the above equation is simply ψ_k(x)= A e^{ikx} (1.10.32)

where A, the overall scale, is a free parameter, unspecified by the eigenvalue problem. So the eigenvalue problem of K is fully solved: any real number k is an eigenvalue, and the corresponding eigenfunction is given by A e^{ikx}. As usual, the freedom in scale will be used to normalize the solution. We choose A to be (1/2π)^{1/2} so that |k> → 1/√(2π) e^{ikx} and <k|k'> = ∫ <k|x> <x|k'> dx = 1/(2π) ∫ e^{-i(k-k')x} dx = δ(k-k') (1.10.33)

(Since <k|k> is infinite, no choice of A can normalize |k> to unity. The delta function normalization is the natural one when the eigenvalue spectrum is continuous.)

der may have a question at this point. "Why was it assumed that the eigenvalue k was real? It is clear that the function Ae^{ikx} with k= k_1+ ik_2 also satisfies Eq. (1.10.31)." The answer is, yes, there are eigenfunctions of K with complex eigenvalues. If, however, our space includes such functions, K must be classified a non-Hermitian operator. (The surface term no longer vanishes since e^{ikx} blows up exponentially as x tends to either +∞ or -∞, depending on the sign of the imaginary part k_2.) In restricting ourselves to real k we have restricted ourselves to what we will call the physical Hilbert space, which is of interest in quantum mechanics. This space is defined as the space of functions that can be either normalized to unity or to the Dirac delta function and plays a central role in quantum mechanics. (We use the qualifier "physical" to distinguish it from the Hilbert space as defined by mathematicians, which contain only proper vectors, i.e., vectors normalizable to unity. The role of the improper vectors in quantum theory will be clear later.)

We will assume that the theorem proved for finite dimensions, namely, that the eigenfunctions of a Hermitian operator form a complete basis, holds in the Hilbert space. (The trouble with infinite-dimensional spaces is that even if you have an infinite number of orthonormal eigenvectors, you can never be sure you have them all, since adding or subtracting a few still leaves you with an infinite number of them.)

Since K is a Hermitian operator, functions that were expanded in the X basis with components f(x)= ⟨x|f⟩ must also have an expansion in the K basis. To find the components, we start with a ket |f⟩, and do the following: ⟨k|f⟩=∫_{-∞}^{∞} e^{-ikx} f(x) dx / (2π)^{1/2}  (1.10.34)

The passage back to the X basis is done as follows: f(x)= ⟨x|f⟩=∫⟨x|k⟩⟨k|f⟩ dk=∫_{-∞}^{∞} e^{ikx} f(k) dk / (2π)^{1/2}  (1.10.35)

Thus the familiar Fourier transform is just the passage from one complete basis |x⟩ to another, |k⟩. Either basis may be used to expand functions that belong to the Hilbert space.

The matrix elements of K are trivial in the K basis: ⟨k|K|k'⟩= k'⟨k|k'⟩= k' δ(k — k')  (1.10.36)

Now, we know where the K basis came from: it was generated by the Hermitian operator K. Which operator is responsible for the orthonormal X basis? Let us call it the operator X. The kets |x⟩ are its eigenvectors with eigenvalue x: X|x⟩ = x|x⟩  (1.10.37)

Its matrix elements in the X basis are ⟨x'|X|x⟩ = xδ(x' — x)  (1.10.38)

To find its action on functions, let us begin with X|f⟩=|ψ⟩ and follow the routine: ⟨x|X|f⟩ = ⟨x|X|x'⟩ ⟨x'|f⟩ dx' = xf(x)= ⟨x|ψ⟩ = ψ(x)

ψ(x) = xf(x)

Hereafter we will omit the qualifier "physical."

Thus the effect of X is to multiply f(x) by x. As in the case of the K operator, one generally suppresses the integral over the common index since it is rendered trivial by the delta function. We can summarize the action of X in Hilbert space as X|f(x)⟩ = |xf(x)⟩  (1.10.39)

where as usual |xf(x)⟩ is the ket corresponding to the function xf(x).

There is a nice reciprocity between the X and K operators which manifests itself if we compute the matrix elements of X in the K basis: ⟨k|X|k'⟩ = ∫_{-∞}^{∞} e^{-ikx} X e^{ik'x} dx / (2π)

= +i ∫ d/dx (1/2π ∫ e^{-ikx} e^{ik'x} dx)= i dk δ(k — k')

Thus if |g(k)⟩ is a ket whose image in the k basis is g(k), then X|g(k)⟩ = i dg(k)/dk  (1.10.40)

In summary then, in the X basis, X acts as x and K as —id/dx [on the functions f(x)], while in the K basis, K acts like k and X like i d/dk [on f(k)]. Operators with such an interrelationship are said to be conjugate to each other.

The conjugate operators X and K do not commute. Their commutator may be calculated as follows. Let us operate X and K in both possible orders on some ket |f⟩ and follow the action in the X basis: X|f⟩ -> xf(x)

K|f⟩ -> —i df(x)/dx So XK|f⟩ -> x(-i df(x)/dx)

KX|f⟩ -> —i d(xf(x))/dx = —i f(x) — i x df(x)/dx Therefore [X, K]|f⟩ -> x(-i df(x)/dx) — (-i f(x) — i x df(x)/dx) = if(x)

In the last step we have used the fact that δ(k' — k)= δ(k — k').

Since |f⟩ is an arbitrary ket, we now have the desired result: [X, K]= iℏ  (1.10.41)

This brings us to the end of our discussion on Hilbert space, except for a final example. Although there are many other operators one can study in this space, we restricted ourselves to X and K since almost all the operators we will need for quantum mechanics are functions of X and P= ℏK, where ℏ is a constant to be defined later.

Example 1.10.1: A Normal Mode Problem in Hilbert Space. Consider a string of length L clamped at its two ends x = 0 and L. The displacement ψ(x, t) obeys the differential equation ∂²ψ/∂t² = ∂²ψ/∂x²  (1.10.42)

Given that at t=0 the displacement is ψ(x, 0) and the velocity ∂ψ/∂t(x, 0) = 0, we wish to determine the time evolution of the string.

But for the change in dimensionality, the problem is identical to that of the two coupled masses encountered at the end of Section 1.8 [see Eq. (1.8.26)]. It is recommended that you go over that example once to refresh your memory before proceeding further.

We first identify ψ(x, t) as components of a vector |ψ(t)⟩ in a Hilbert space, the elements of which are in correspondence with possible displacements ψ, i.e., functions that are continuous in the interval 0 <x <L and vanish at the end points. You may verify that these functions do form a vector space.

The analog of the operator Ω in Eq. (1.8.26) is the operator ∂²/∂x². We recognize this to be minus the square of the operator K = —i∂/∂x. Since K acts on a space in which ψ(0) = ψ(L) = 0, it is Hermitian, and so is K². Equation (1.10.42) has the abstract counterpart d²|ψ(t)⟩/dt² = —K²|ψ(t)⟩  (1.10.43)

We solve the initial-value problem by following the algorithm developed in Example 1.8.6: Step (1). Solve the eigenvalue problem of —K².

Step (2). Construct the propagator U(t) in terms of the eigenvectors and eigenvalues.

Step (3). |ψ(t)⟩ = U(t)|ψ(0)⟩  (1.10.44)

The equation to solve is K²|ψ⟩ = k²|ψ⟩  (1.10.45)

In the X basis, this becomes d²ψ_k(x)/dx² = —k²ψ_k(x)  (1.10.46)

the general solution to which is ψ_k(x)= A cos kx+ B sin kx  (1.10.47)

where A and B are arbitrary. However, not all these solutions lie in the Hilbert space we are considering. We want only those that vanish at x =0 and x = L. At x = 0 we find ψ_k(0) = 0 = A  (1.10.48a)

while at x = L we find 0= B sin kL  (1.10.48b)

If we do not want a trivial solution (A = B = 0) we must demand sin kL =0, kL= mπ , (m= 1, 2, 3, ...)  (1.10.49)

We do not consider negative m since it doesn't lead to any further linearly independent solutions [sin(—x)= —sin x]. The allowed eigenvectors thus form a discrete set labeled by an integer m: ψ_m(x)= (2/L)^{1/2} sin (mπx/L)  (1.10.50)

where we have chosen B= (2/L)^{1/2} so that ∫_0^L ψ_m*(x) ψ_m'(x) dx= δ_{mm'}  (1.10.51)

Let us associate with each solution labeled by the integer m an abstract ket |m⟩: |m⟩ --(x basis)--> (2/L)^{1/2} sin (mπx/L)  (1.10.52)

If we project |ψ(t)⟩ on the |m⟩ basis, in which K² is diagonal with eigenvalues (mπ/L)², the components ⟨m|ψ(t)⟩ will obey the decoupled equations d²⟨m|ψ(t)⟩/dt² = —(mπ/L)² ⟨m|ψ(t)⟩, (m= 1, 2, ...)  (1.10.53)

in analogy with Eq. (1.8.33). These equations may be readily solved (subject to the condition of vanishing initial velocities) as ⟨m|ψ(t)⟩ = ⟨m|ψ(0)⟩ cos (mπt/L)  (1.10.54)

Consequently |ψ(t)⟩= Σ_m |m⟩⟨m|ψ(t)⟩ = Σ_m |m⟩⟨m|ψ(0)⟩ cos ω_m t, (1.10.55)

or U(t)= Σ_m |m⟩⟨m| cos ω_m t, (ω_m = mπ/L)  (1.10.56)

The propagator equation |ψ(t)⟩ = U(t)|ψ(0)⟩ becomes in the |x⟩ basis ⟨x|ψ(t)⟩ = ψ(x, t)

= ⟨x|U(t)|ψ(0)⟩ = ∫⟨x|U(t)|x'⟩ ⟨x'|ψ(0)⟩ dx'  (1.10.57)

It follows from Eq. (1.10.56) that ⟨x|U(t)|x'⟩=Σ_m ⟨x|m⟩ ⟨m|x'⟩ cos ω_m t = Σ_m (2/L) sin (mπx/L) sin (mπx'/L) cos ω_m t  (1.10.58)

Thus, given any ψ(x', 0), we can get ψ(x, t) by performing the integral in Eq. (1.10.57), using ⟨x|U(t)|x'⟩ from Eq. (1.10.58). If the propagator language seems too abstract, we can begin with Eq. (1.10.55). Dotting both sides with ⟨x| , we get ψ(x, t) = Σ_m ⟨x|m⟩ ⟨m|ψ(0)⟩ cos ω_m t = Σ_m (2/L)^{1/2} sin (mπx/L) [∫_0^L (2/L)^{1/2} sin (mπx'/L) ψ(x', 0) dx'] cos ω_m t  (1.10.59)

Given ψ(0), one must then compute the coefficients ⟨m|ψ(0)⟩.

Usually we will find that the coefficients ⟨m|ψ(0)⟩ fall rapidly with m so that a few leading terms may suffice to get a good approximation.

Exercise 1.10.4. A string is displaced as follows at t = 0: ψ(x, 0)= (2xh/L), 0 ≤ x ≤ L/2 ψ(x, 0)= (2h(L-x)/L), L/2 ≤ x ≤ L Show that ψ(x, t)= Σ_{m=1,3,5,...} (8h/(π² m²)) sin (mπx/2) cos (mπt/2L)

Review of Classical Mechanics

In this chapter we will develop the Lagrangian and Hamiltonian formulations of mechanics starting from Newton's laws. These subsequent reformulations of mechanics bring with them a great deal of elegance and computational ease. But our principal interest in them stems from the fact that they are the ideal springboards from which to make the leap to quantum mechanics. The passage from the Lagrangian formulation to quantum mechanics was carried out by Feynman in this path integral formalism. A more common route to quantum mechanics, which we will follow for the most part, has as its starting point the Hamiltonian formulation, and it was discovered mainly by Schrödinger, Heisenberg, Dirac, and Born.

It should be emphasized, and it will soon become apparent, that all three formulations of mechanics are essentially the same theory, in that their domains of validity and predictions are identical. Nonetheless, in a given context, one or the other may be more inviting for conceptual, computational, or simply aesthetic reasons.

2.1. The Principle of Least Action and Lagrangian Mechanics

Let us take as our prototype of the Newtonian scheme a point particle of mass m moving along the x axis under a potential V(x). According to Newton's Second Law, m d²x/dt² = -dV/dx (2.1.1)

If we are given the initial state variables, the position x(t₁) and velocity ẋ(t₁), we can calculate the classical trajectory x_cl(t) as follows. Using the initial velocity and acceleration [obtained from Eq. (2.1.1)] we compute the position and velocity at a time t₁ + Δt. For example, x₁(t₁ + Δt) = x(t₁) + ẋ(t₁)Δt

Having updated the state variables to the time t₁ + Δt, we can repeat the process again to inch forward to t₁ + 2Δt and so on.

The equation of motion being second order in time, two pieces of data, x(t) and ẋ(t₁), are needed to specify a unique x_cl(t). An equivalent way to do the same, and one that we will have occasion to employ, is to specify two space-time points (x_i, t_i) and (x_f, t_f) on the trajectory.

The above scheme readily generalizes to more than one particle and more than one dimension. If we use n Cartesian coordinates (x₁, x₂, ..., x_n) to specify the positions of the particles, the spatial configuration of the system may be visualized as a point in an n-dimensional configuration space. (The term "configuration space" is used even if the n coordinates are not Cartesian.) The motion of the representative point is given by m_j d²x_j/dt² = -∂V/∂x_j (2.1.2)

where m_j stands for the mass of the particle whose coordinate is x_j. These equations can be integrated step by step, just as before, to determine the trajectory.

In the Lagrangian formalism, the problem of a single particle in a potential V(x) is posed in a different way: given that the particle is at x_i and x_f at times t_i and t_f, respectively, what is it that distinguishes the actual trajectory x_cl(t) from all other trajectories or paths that connect these points? (See Fig. 2.1.)

The Lagrangian approach is thus global, in that it tries to determine at one stroke the entire trajectory x_cl(t), in contrast to the local approach of the Newtonian scheme, which concerns itself with what the particle is going to do in the next infinitesimal time interval.

The answer to the question posed above comes in three parts: (1) Define a function L called the Lagrangian, given by L = T - V, T and V being the kinetic and potential energies of the particle. Thus L = L(x, ẋ). The explicit t dependence may arise if the particle is in an external time-dependent field. We will, however, assume the absence of this t dependence.

(2) For each path x(t) connecting (x_i, t_i) and (x_f, t_f), calculate the action S[x(t)] defined by S[x(t)] = ∫_{t_i}^{t_f} L(x, ẋ) dt (2.1.3)

We use square brackets to enclose the argument of S to remind us that the function S depends on an entire path or function x(t), and not just the value of x at some time t. One calls S a functional to signify that it is a function of a function.

(3) The classical path is one on which S is a minimum. (Actually we will only require that it be an extremum. It is, however, customary to refer to this condition as the principle of least action.)

We will now verify that this principle reproduces Newton's Second Law.

The first step is to realize that a functional S[x(t)] is just a function of n variables as n → ∞. In other words, the function x(t) simply specifies an infinite number of values x(t₁), ..., x(t), ..., x(t_f), one for each instant in time t in the interval t_i < t < t_f, and S is a function of these variables. To find its minimum we simply generalize the procedure for the finite n case. Let us recall that if f = f(x₁, ..., x_n) = f(x); the minimum x° is characterized by the fact that if we move away from it by a small amount η in any direction, the first-order change δf(1) in f vanishes. That is, if we make a Taylor expansion: f(x° + η) = f(x°) + Σᵢ (∂f/∂xᵢ) ηᵢ + higher-order terms in η (2.1.4)

then δf(1) = Σᵢ (∂f/∂xᵢ) ηᵢ = 0 (2.1.5)

From this condition we can deduce an equivalent and perhaps more familiar expression of the minimum condition: every first-order partial derivative vanishes at x°. To prove this, for say, ∂f/∂x_k, we simply choose η to be along the ith direction. Thus ∂f/∂x_i = 0, i = 1, ..., n (2.1.6)

Let us now mimic this procedure for the action S. Let x_cl(t) be the path of least action and x_cl(t) + η(t) a "nearby" path (see Fig. 2.2). The requirement that all paths coincide at t_i and t_f means η(t_i) = η(t_f) = 0 (2.1.7)

Now S[x_cl + η] - S[x_cl] = ∫_{t_i}^{t_f} [L(x_cl + η, ẋ_cl + η̇) - L(x_cl, ẋ_cl)] dt = ∫_{t_i}^{t_f} [ (∂L/∂x) η + (∂L/∂ẋ) η̇ + higher-order terms ] dt = S[x_cl] + δS(1)

We set δS(1) = 0 in analogy with the finite variable case: 0 = δS(1) = ∫_{t_i}^{t_f} [ (∂L/∂x) η + (∂L/∂ẋ) η̇ ] dt

If we integrate the second term by parts, it turns into ∫_{t_i}^{t_f} (∂L/∂ẋ) η̇ dt = [ (∂L/∂ẋ) η ]_{t_i}^{t_f} - ∫_{t_i}^{t_f} d/dt(∂L/∂ẋ) η dt

The first of these terms vanishes due to Eq. (2.1.7). So that 0 = δS(1) = ∫_{t_i}^{t_f} [ ∂L/∂x - d/dt(∂L/∂ẋ) ] η dt (2.1.8)

Note that the condition δS(1) = 0 implies that S is extremized and not necessarily minimized. We shall, however, continue the tradition of referring to this extremum as the minimum. This equation is the analog of Eq. (2.1.5): the discrete variable is replaced by η(t); the sum over i is replaced by an integral over t, and ∂f/∂x_i is replaced by ∂L/∂x - d/dt(∂L/∂ẋ). There are two terms here playing the role of ∂f/∂x_i since L (or equivalently S) has both explicit and implicit (through the ẋ terms) dependence on x(t). Since η(t) is arbitrary, we may extract the analog of Eq. (2.1.6): ∂L/∂x - d/dt(∂L/∂ẋ) = 0, or t_i < t < t_f (2.1.9)

To deduce this result for some specific time t₀, we simply choose an η(t) that vanishes everywhere except in an infinitesimal region around t₀.

Equation (2.1.9) is the celebrated Euler-Lagrange equation. If we feed into it L = T - V, T = mẋ²/2, V = V(x), we get ∂L/∂ẋ = mẋ and ∂L/∂x = -dV/dx

so that the Euler-Lagrange equation becomes just d/dt(mẋ) = -dV/dx

which is just Newton's Second Law, Eq. (2.1.1).

If we consider a system described by n Cartesian coordinates, the same procedure yields d/dt(∂L/∂ẋᵢ) = ∂L/∂xᵢ (i=1,..., n) (2.1.10)

Now L = T - V = (1/2) Σ_j m_j ẋ_j² - V(x₁,..., x_n)

and V = V(x₁,..., x_n)

so that Eq. (2.1.10) becomes d/dt(m_i ẋ_i) = -∂V/∂x_i

which is identical to Eq. (2.1.2). Thus the minimum (action) principle indeed reproduces Newtonian mechanics if we choose L = T - V.

Notice that we have assumed that V is velocity-independent in the above proof. An important force, that of a magnetic field B on a moving charge is excluded by this restriction, since F_mag = qv × B, q being the charge of the particle and v = ẋ its velocity. We will show shortly that this force too may be accommodated in the Lagrangian formalism, in the sense that we can find an L that yields the correct force law when Eq. (2.1.10) is employed. But this L no longer has the form T - V. One therefore frees oneself from the notion that L = T - V; and views L as some function L(x_i, ẋ_i) which yields the correct Newtonian dynamics when fed into the Euler-Lagrange equations. To the reader who wonders why one bothers to even deal with a Lagrangian when all it does is yield Newtonian force laws in the end, I present a few of its main attractions besides its closeness to quantum mechanics. These will then be illustrated by means of an example.

(1) In the Lagrangian scheme one has merely to construct a single scalar L and all the equations of motion follow by simple differentiation. This must be contrasted with the Newtonian scheme, which deals with vectors and is thus more complicated.

(2) The Euler-Lagrange equations (2.1.10) have the same form if we use, instead of the n Cartesian coordinates x₁, ..., x_n, any general set of n independent coordinates q₁, q₂, ..., q_n. To remind us of this fact we will rewrite Eq. (2.1.10) as d/dt(∂L/∂q̇ⱼ) = ∂L/∂qⱼ (2.1.11)

One can either verify this by brute force, making a change of variables in Eq. (2.1.10) and seeing that an identical equation with xᵢ replaced by qⱼ follows, or one can simply go through our derivation of the minimum action condition and see that nowhere were the coordinates assumed to be Cartesian. Of course, at the next stage, in showing that the Euler-Lagrange equations were equivalent to Newton's, Cartesian coordinates were used, for in these coordinates the kinetic energy T and the Newtonian equations have simple forms. But once the principle of least action is seen to generate the correct dynamics, we can forget all about Newton's laws and use Eq. (2.1.11) as the equations of motion. What is being emphasized is that these equations, which express the condition for least action, are form invariant under an arbitrary change of coordinates. This form invariance must be contrasted with the Newtonian equation (2.1.2), which presumes that the x_i are Cartesian. If one trades the x_i for another non-Cartesian set of qⱼ, Eq. (2.1.2) will have a different form (see Example 2.1.1 at the end of this section).

Equation (2.1.11) can be made to resemble Newton's Second Law if one defines a quantity p_j = ∂L/∂q̇ⱼ (2.1.12)

called the canonical momentum conjugate to qⱼ, and the quantity Q_j = ∂L/∂qⱼ (2.1.13)

called the generalized force conjugate to qⱼ. Although the rate of change of the canonical momentum equals the generalized force, one must remember that neither is p is always a linear momentum (mass times velocity or "mv" momentum), nor is F always a force (with dimensions of mass times acceleration). For example, if q is an angle θ, p will be an angular momentum and τ a torque.

(3) Conservation laws are easily obtained in this formalism. Suppose the Lagrangian depends on a certain velocity q̇, but not on the corresponding coordinate q_i. The latter is then called a cyclic coordinate. It follows that the corresponding p_i is conserved:

d/dt (∂L/∂q̇) = 0. (2.1.14)

Although Newton's Second Law, Eq. (2.1.2), also tells us that if a Cartesian coordinate x_i is cyclic, the corresponding momentum mẋ_i is conserved, Eq. (2.1.14) is more general. Consider, for example, a potential V rom following any kind of strategy, the particle, in a sense, goes from (x_i, t) to (x_f, t_f) along all possible paths, giving equal weight to each! How it is that despite this, classical particles do seem to follow x_cl(t) is an interesting question that will be answered when we come to the path integral formalism of quantum mechanics.

2.5. The Hamiltonian Formalism In the Lagrangian formalism, the independent variables are the coordinates q, and velocities \dot{q}_i. The momenta are derived quantities defined by (2.5.1)

In the Hamiltonian formalism one exchanges the roles of \dot{q} and p: one replaces the Lagrangian L(q, \dot{q}) by a Hamiltonian H(q,p) which generates the equations of motion, and \dot{q} becomes a derived quantity, \dot{q}_i = \frac{\partial H}{\partial p_i} (2.5.2)

thereby completing the role reversal of the \dot{q}'s and the p's.

There exists a standard procedure for effecting such a change, called a Legendre transformation, which is illustrated by the following simple example. Suppose we have a function f(x) with \frac{df}{dx} = u(x)

(2.5.3)

Let it be possible to invert u(x) to get x(u). [For example if u(x)= x^3, x(u)= u^{1/3}, etc.] If we define a function g(u)= x(u)u— f(x(u))

(2.5.4)

then \frac{dg}{du} = \frac{dx}{du} u+ x(u)- \frac{df}{dx}\frac{dx}{du} = x(u)

(2.5.5)

That is to say, in going from f to g (or vice versa) we exchange the roles of x and u. One calls Eq. (2.5.4) a Legendre transformation and f and g Legendre transforms of each other.

More generally, if f=f(x_1, x_2, ..., x_n), one can eliminate a subset {x_i, i=1 to j} in favor of the partial derivatives u_i=\partial f/\partial x_i by the transformation g(u_i, x_k) = \sum_{i=1}^j u_i x_i - f(x_i, x_k)

(2.5.6)

It is understood in the right-hand side of Eq. (2.5.6) that all the x_i's to be eliminated have been rewritten as functions of the allowed variables in g. It can be easily verified that \frac{\partial g}{\partial x_k} = -\frac{\partial f}{\partial x_k} (2.5.7)

where in taking the above partial derivative, one keeps all the other variables in g constant.

We will often refer to q_1 , ..., q_n as q and p_1, ..., p_n as p.

2.5.1 Comparison of the Lagrangian and Hamiltonian Formalisms

## CHAPTER

Lagrangian formalism | Hamiltonian formalism --- | --- (1) The state of a system with n degrees of freedom is described by n coordinates (q_1 , ..., q_n) and n velocities (\dot{q}_1, ..., \dot{q}_n), or in a more compact notation by (q,\dot{q}). | (1) The state of a system with n degrees of freedom is described by n coordinates and n momenta (q_1, ...q_n; p_1, ...p_n) or, more succinctly, by (q, p).

(2) The state of the system may be represented by a point moving with a definite velocity in an n-dimensional configuration space. | (2) The state of the system may be represented by a point in a 2n-dimensional phase space, with coordinates (q_1, ..., q_n ; p_1, ..., p_n).

(3) The n coordinates evolve according to n second-order equations. | (3) The 2n coordinates and momenta obey 2n first-order equations.

(4) For a given q, several trajectories may pass through a given point in configuration space depending on \dot{q}. | (4) For a given q only one trajectory passes through a given point in phase space.

Applying these methods to the problem in question, we define H(q, p)= p \cdot \dot{q} - L(q, \dot{q})

(2.5.8)

where the \dot{q}'s are to be written as functions of q's and p's. This inversion is generally easy since L is a polynomial of rank 2 in \dot{q}, and p_i=\partial L / \partial \dot{q}_i is a polynomial of rank 1 in the \dot{q}'s, e.g., Eq. (2.2.7). Consider now \frac{\partial H}{\partial p_i} = \frac{\partial}{\partial p_i} \left( \sum_k p_k \dot{q}_k - L \right)

= \dot{q}_i + \sum_k p_k \frac{\partial \dot{q}_k}{\partial p_i} - \sum_k \frac{\partial L}{\partial \dot{q}_k} \frac{\partial \dot{q}_k}{\partial p_i} = \dot{q}_i + \sum_k p_k \frac{\partial \dot{q}_k}{\partial p_i} - \sum_k p_k \frac{\partial \dot{q}_k}{\partial p_i} = \dot{q}_i (2.5.10)

[There are no \dot{q} terms since q is held constant in \partial L/\partial \dot{q}_i; that is, q and p are independent variables.] Similarly, \frac{\partial H}{\partial q_i} = \frac{\partial}{\partial q_i} \left( \sum_k p_k \dot{q}_k - L \right)

= \sum_k p_k \frac{\partial \dot{q}_k}{\partial q_i} - \frac{\partial L}{\partial q_i} - \sum_k \frac{\partial L}{\partial \dot{q}_k} \frac{\partial \dot{q}_k}{\partial q_i} = -\frac{\partial L}{\partial q_i} (2.5.11)

We now feed in the dynamics by replacing (\partial L / \partial q_i) by \dot{p}_i and obtain Hamilton's canonical equations: \dot{q}_i = \frac{\partial H}{\partial p_i}, \quad \dot{p}_i = -\frac{\partial H}{\partial q_i} (2.5.12)

Note that we have altogether 2n first-order equations (in time) for a system with n degrees of freedom. Given the initial-value data, (q_i(0) , p_i(0)) , i= 1, . . n, we can integrate the equations to get (q_i(t), p_i(t)).

Table 2.1 provides a comparison of the Lagrangian and Hamiltonian formalisms.

Now, just as L may be interpreted as T−V if the force is conservative, so there exists a simple interpretation for H in this case. Consider the sum \sum p_i \dot{q}_i. Let us use Cartesian coordinates, in terms of which T = \frac{1}{2} \sum m_i \dot{x}_i^2 and \sum p_i \dot{q}_i = \sum (m_i \dot{x}_i) \dot{x}_i = 2T (2.5.13)

so that H = T + V (2.5.14)

the total energy. Notice that although we used Cartesian coordinates along the way, the resulting equation (2.5.14) is a relation among scalars and thus coordinate independent.

Exercise 2.5.1. Show that if T= \sum_{i,j} T_{ij}(q) \dot{q}_i \dot{q}_j, where \dot{q}'s are generalized velocities, p_i = 2T.

The Hamiltonian method is illustrated by the simple example of a harmonic oscillator, for which L = \frac{1}{2}m\dot{x}^2 - \frac{1}{2}kx^2 The canonical momentum is p = \frac{\partial L}{\partial \dot{x}} = m\dot{x} It is easy to invert this relation to obtain \dot{x} as a function of p: \dot{x} = p / m and obtain H(x, p)=T+ V= \frac{1}{2}m(p/m)^2 + \frac{1}{2}kx^2 = \frac{p^2}{2m} + \frac{1}{2}kx^2 (2.5.15)

The equations of motion are \dot{x} = \frac{\partial H}{\partial p} = \frac{p}{m} (2.5.16)

\dot{p} = -\frac{\partial H}{\partial x} = -kx (2.5.17)

These equations can be integrated in time, given the initial x and p. If, however, we want the familiar second-order equation, we differentiate Eq. (2.5.16) with respect to time, and feed it into Eq. (2.5.17) to get m\ddot{x} + kx = 0 Exercise 2.5.2. Using the conservation of energy, show that the trajectories in phase space for the oscillator are ellipses of the form (x/a)^2+(p/b)^2= 1, where a^2 = 2E/k and b^2 = 2mE.

Exercise 2.5.3. Solve Exercise 2.1.2 using the Hamiltonian formalism.

Exercise 2.5.4.* Show that H corresponding to L in Eq. (2.3.6) is H = (p_{cm}^2)/(2M)+ p^2/(2μ) + V(r), where M is the total mass, μ is the reduced mass, p_{cm} and p are the momenta conjugate to r_{cm} and r, respectively.

2.6. The Electromagnetic Force in the Hamiltonian Scheme The passage from L_{em} to its Legendre transform H_{em} is not sensitive in any way to the velocity-dependent nature of the force. If L_{em} generated the correct force laws, so will H_{em}, the dynamical content of the schemes being identical. In contrast, the velocity independence of the force was assumed in showing that the numerical value of H is T+ V, the total energy. Let us therefore repeat the analysis for the electromagnetic case. As L_{em} = \frac{1}{2}mv^2 - q\phi + \frac{q}{c} \mathbf{v} \cdot \mathbf{A} and p = \frac{\partial L}{\partial \mathbf{v}} = m\mathbf{v} + \frac{q}{c} \mathbf{A} Note that in this discussion, q is the charge and not the coordinate. The (Cartesian) coordinate r is hidden in the functions A(r, t) and \phi(r, t).

we have H = p \cdot \mathbf{v} - L_{em} = (m\mathbf{v} + \frac{q}{c} \mathbf{A}) \cdot \mathbf{v} - (\frac{1}{2}mv^2 - q\phi + \frac{q}{c} \mathbf{v} \cdot \mathbf{A})

= m v^2 - q\phi = T + q\phi (2.6.1)

Now, there is something very disturbing about Eq. (2.6.1): the vector potential A seems to have dropped out along the way. How is H_{em} to generate the correct dynamics without knowing what A is? The answer is, of course, that H is more than just T+V; it is T+ q\phi written in terms of the correct variables, in particular, in terms of p and not v. Making the change of variables, we get H = \frac{(\mathbf{p} - q\mathbf{A}/c)^2}{2m} + q\phi (2.6.2)

with the vector potential very much in the picture.

2.7. Cyclic Coordinates, Poisson Brackets, and Canonical Transformations Cyclic coordinates are defined here just as in the Lagrangian case and have the same significance: if a coordinate q_i is missing in H, then \frac{\partial H}{\partial q_i} = 0 (2.7.1)

Now, there will be other quantities, such as the energy, that may be conserved in addition to the canonical momenta. There exists a nice method of characterizing these in the Hamiltonian formalism. Let ω(p, q) be some function of the state variables, with no explicit dependence on t. Its time variation is given by \frac{d\omega}{dt} = \sum_i \left( \frac{\partial \omega}{\partial q_i} \dot{q}_i + \frac{\partial \omega}{\partial p_i} \dot{p}_i \right)

= \sum_i \left( \frac{\partial \omega}{\partial q_i} \frac{\partial H}{\partial p_i} - \frac{\partial \omega}{\partial p_i} \frac{\partial H}{\partial q_i} \right)

(2.7.2)

Another example is the conservation of L_z = xp_y - yp_x when V(x, y) = V(x^2 +y^2). There are no cyclic coordinates here. Of course, if we work in polar coordinates, V( r, \theta)= V( r), and L_z = m r^2 \dot{\theta} is conserved because it is the momentum conjugate to the cyclic coordinate \theta.

where we have defined the Poisson bracket (PB) between two variables ω(p, q) and η(p, q) to be {ω, η} = \sum_i \left( \frac{\partial ω}{\partial q_i} \frac{\partial η}{\partial p_i} - \frac{\partial ω}{\partial p_i} \frac{\partial η}{\partial q_i} \right)

(2.7.3)

It follows from Eq. (2.7.2) that any variable whose PB with H vanishes is constant in time, i.e., conserved. In particular H itself is a constant of motion (identified as the total energy) if it has no explicit t dependence.

Exercise 2.7.1.* Show that {ω, λη}= —{η, ω} {ω, λ+ η} = {ω, λ}+ {ω, η} {ω, λη} = {ω, λ}η+ λ{ω, η} Note the similarity between the above and Eqs. (1.5.10) and (1.5.11) for commutators.

Of fundamental importance are the PB between the q's and the p's. Observe that {q_i, q_j} = {p_i, p_j} =0 (2.7.4a)

{q_i, p_j} = δ_{ij} (2.7.4b)

since (q_i, p_i) are independent variables (\partial q_i/\partial q_j= δ_{ij}, \partial q_i/\partial p_j= 0, etc.). Hamilton's equations may be written in terms of PB as \dot{q}_i = \{q_i, H\} (2.7.5a)

\dot{p}_i = \{p_i, H\} (2.7.5b)

by setting ω = q_i or p_i in Eq. (2.7.2).

Exercise 2.7.2.* (i) Verify Eqs. (2.7.4) and (2.7.5). (ii) Consider a problem in two dimensions given by H =p_x^2+p_y^2 + ax^2 + by^2. Argue that if a = b, {H, L_z} must vanish. Verify by explicit computation.

Canonical Transformations We have seen that the Euler-Lagrange equations are form invariant under an arbitrary change of coordinates in configuration space q_i \rightarrow \tilde{q}_i (q_1 , ..., q_n), \quad i= 1, . . . , n (2.7.6a)

We assume the transformation is invertible, so we may write q in terms of \tilde{q}: q = q(\tilde{q}). The transformation may also depend on time explicitly [\tilde{q}= \tilde{q}(q, t)], but we do not consider such cases.

or more succinctly q \rightarrow \tilde{q}(q)

(2.7.6b) CLASSICAL MECHANICS The response of the velocities to this transformation follows from Eq. (2.7.6a): q̇_i = ∂Q_i / ∂q_j * q̇_j  (2.7.7)

The response of the canonical momenta may be found by rewriting ℋ in terms of (Q, Q̇) and taking the derivative with respect to q: p_i = ∂L(Q, Q̇) / ∂q_i  (2.7.8)

The result is (Exercise 2.7.8): p_i = ∂Q_j / ∂q_i * P_j  (2.7.9)

Notice that although L(Q, Q̇) enters Eq. (2.7.8), it drops out in Eq. (2.7.9), which connects p to the old variables. This is as it should be, for we expect that the response of the momenta to a coordinate transformation (say, a rotation) is a purely kinematical question.

A word of explanation about L(Q, Q̇). By L(Q, Q̇) we mean the Lagrangian (say T- V, for definiteness) written in terms of Q and Q̇. Thus the numerical value of the Lagrangian is unchanged under (q, q̇) -> (Q, Q̇); for (q, q̇) and (Q, Q̇) refer to the same physical state. The functional form of the Lagrangian, however, does change and so we should really be using two different symbols L(q, q̇) and L(Q, Q̇). Nonetheless we follow the convention of denoting a given dynamical variable, such as the Lagrangian, by a fixed symbol in all coordinate systems.

The invariance of the Euler-Lagrange equations under (q, q̇) -> (Q, Q̇) implies the invariance of Hamilton's equation under (q, p) -> (Q, P), i.e., (Q, P) obey Q̇_i = ∂ℋ / ∂P_i, Ṗ_i = - ∂ℋ / ∂Q_i  (2.7.10)

where ℋ(Q, P) is the Hamiltonian written in terms of Q and P. The proof is simple: we start with L(Q, Q̇), perform a Legendre transform, and use the fact that Q obeys Euler-Lagrange equations.

The transformation Q_i = Q_i(q_1, ..., q_n),  (2.7.11)

q̇_i = ∂Q_i / ∂q_j * q̇_j is called a point transformation. If we view the Hamiltonian formalism as something derived from the Lagrangian scheme, which is formulated in n-dimensional configuration space, this is the most general (time-independent) transformation which preserves the form of Hamilton's equations (that we can think of). On the other hand, if we view the Hamiltonian formalism in its own right, the backdrop is the 2n-dimensional phase space. In this space, the point transformation is unnecessarily restrictive. One can contemplate a more general transformation of phase space coordinates: Q_i = Q_i(q, p)

P_i = P_i(q, p)  (2.7.12)

Although all sets of 2n independent coordinates (Q, P) are formally adequate for describing the state of the system, not all of them will preserve the canonical form of Hamilton's equations. (This is like saying that although Newton's laws may be written in terms of any complete set of coordinates, the simple form m_i q̈_i = F_i is valid only if the q_i are Cartesian). If, however, (Q, P) obey the canonical equations (2.7.10), we say that they are canonical coordinates and that Eq. (2.7.12) defines a canonical transformation. Any set of coordinates (q_1, ..., q_n), and the corresponding momenta generated in the Lagrangian formalism (p_i = ∂L / ∂q̇_i), are canonical coordinates. Given one set, (q, p), we can get another, (Q, P), by the point transformation, which is a special case of the canonical transformation. This does not, however, exhaust the possibilities. Let us now ask the following question. Given a new set of coordinates (Q(q,p), P(q,p)), how can we tell if they are canonical [assuming (q, p) are]? Now it is true for any function F(q, p) that dF/dt = {F, ℋ}_{q,p} = Σ (∂F/∂q_i * ∂ℋ/∂p_i - ∂F/∂p_i * ∂ℋ/∂q_i)  (2.7.13)

Applying this to q_j we find q̇_j = Σ (∂q_j/∂q_i * ∂ℋ/∂p_i - ∂q_j/∂p_i * ∂ℋ/∂q_i)  (2.7.14)

If we view ℋ as a function of (Q, P) and use the chain rule, we get ∂ℋ/∂p_i = Σ (∂ℋ/∂Q_k * ∂Q_k/∂p_i + ∂ℋ/∂P_k * ∂P_k/∂p_i)  (2.7.15a)

and ∂ℋ/∂q_i = Σ (∂ℋ/∂Q_k * ∂Q_k/∂q_i + ∂ℋ/∂P_k * ∂P_k/∂q_i)  (2.7.15b)

Feeding all this into Eq. (2.7.14) we find, upon regrouping terms, q̇_j = Σ [ ∂Q_k/∂q_j * ∂ℋ/∂P_k + ∂P_k/∂q_j * (∂Q_k/∂P_j) ]  (2.7.16)

It can similarly be established that ṗ_j = Σ [ ∂Q_k/∂p_j * ∂ℋ/∂P_k + ∂P_k/∂p_j * (∂Q_k/∂P_j) ]  (2.7.17)

If Eqs. (2.7.16) and (2.7.17) are to reduce to the canonical equations (2.7.10) for any ℋ(Q, P), we must have ∂Q_k/∂q_j = 0 = ∂P_k/∂p_j ∂Q_k/∂p_j * ∂P_k/∂q_j - ∂Q_k/∂q_j * ∂P_k/∂p_j = δ_{jk}  (2.7.18)

These then are the conditions to be satisfied by the new variables if they are to be canonical. Notice that these constraints make no reference to the specific functional form of ℋ: the equations defining canonical variables are purely kinematical and true for any ℋ(Q, P).

Exercise 2.7.3. Fill in the missing steps leading to Eq. (2.7.18) starting from Eq. (2.7.14).

Exercise 2.7.4. Verify that the change to a rotated frame Q = x cos θ — y sin θ Y = x sin θ + y cos θ P_X = p_x cos θ — p_y sin θ P_Y = p_x sin θ + p_y cos θ is a canonical transformation.

Exercise 2.7.5. Show that the polar variables ρ = (x^2 + y^2)^1/2, φ = tan^{-1} (y / x), P_ρ = (x p_x + y p_y) / (x^2 + y^2)^1/2 P_φ = x p_y - y p_x are canonical. (ê_ρ is the unit vector in the radial direction.)

Exercise 2.7.6.* Verify that the change from the variables r_1, r_2, p_1, p_2 to R_cm, P_cm, r, and p is a canonical transformation. (See Exercise 2.5.4).

Exercise 2.7.7. Verify that Q = ln(q^{-1} sin p)

P = q cot p is a canonical transformation.

Exercise 2.7.8. We would like to derive here Eq. (2.7.9), which gives the transformation of the momenta under a coordinate transformation in configuration space: Q = Q(q), q̇_i = Σ (∂Q_i / ∂q_j) * q̇_j.

(1) Argue that if we invert the above equation to get q=q(Q), we can derive the following counterpart of Eq. (2.7.7): q̇_i = Σ (∂q_i / ∂Q_j) * Q̇_j.

(2) Show from the above that ∂q_i / ∂Q_j = (∂Q_j / ∂q_i)^{-1}.

(3) Now calculate p_i = ∂L(Q, Q̇) / ∂q̇_i = Σ (∂L / ∂Q̇_j) * (∂Q̇_j / ∂q̇_i). Use the chain rule and the fact that Q=Q(q) and not Q(q̇_1, q̇_2) to derive Eq. (2.7.9).

(4) Verify, by calculating the PB in Eq. (2.7.18), that the point transformation is canonical.

If (q, p) and (Q, P) are both canonical, we must give them both the same status, for Hamilton's equations have the same appearance when expressed in terms of either set. Now, we have defined the PB of two variables ω and σ in terms of (q, p) as {ω, σ}_{q,p} = Σ (∂ω/∂q_i * ∂σ/∂p_i - ∂ω/∂p_i * ∂σ/∂q_i)

Should we not also define a PB, {ω, σ}_{Q,P}, for every canonical pair (Q, P)? Fortunately it turns out that the PB are invariant under canonical transformations: {ω, σ}_{q,p} = {ω, σ}_{Q,P}  (2.7.19)

(It is understood that ω and σ are written as functions of Q and P on the right-hand side.)

Exercise 2.7.9. Verify Eq. (2.7.19) by direct computation. Use the chain rule to go from q,p derivatives to Q,P derivatives. Collect terms that represent PB of the latter.

Besides the proof by direct computation (as per Exercise 2.7.9 above) there is an alternate way to establish Eq. (2.7.19).

Consider first σ = ℋ. We know that since (q, p) obey canonical equations, ω̇ = {ω, ℋ}_{q,p} But then (Q, P) also obey canonical equations, so ω̇ = {ω, ℋ}_{Q,P} Now ω is some physical quantity such as the kinetic energy or the component of angular momentum in some fixed direction, so its rate of change is independent of the phase space coordinates used, i.e., ω̇ is the same, whether ω = ω(q, p) or ω(Q, P). So {ω, ℋ}_{q,p} = {ω, ℋ}_{Q,P} Having proved the result for what seems to be the special case σ = ℋ, we now pull the following trick. Note that nowhere in the derivation did we have to assume that ℋ was any particular function of q and p. In fact, Hamiltonian dynamics, as a consistent mathematical scheme, places no restriction on ℋ. It is the physical requirement that the time evolution generated by ℋ coincide with what is actually observed, that restricts ℋ to be T+ V. Thus ℋ could have been any function at all in the preceding argument and in the result Eq. (2.7.20) (which is just a relation among partial derivatives.) If we understand that ℋ is not T+ V in this argument but an arbitrary function, call it G, we get the desired result.

Active Transformations So far, we have viewed the transformation Q = Q(q, p)

P = P(q, p)

as passive: both (q, p) and (Q, P) refer to the same point in phase space described in two different coordinate systems. Under the transformation (q, p)—> (Q, P), the numerical values of all dynamical variables are unchanged (for we are talking about the same physical state), but their functional form is changed. For instance, under a change from Cartesian to spherical coordinates, ω (x, y, z) = x^2 + y^2 + z^2 -> ω(r, θ, φ) = r^2. As mentioned earlier, we use the same symbol for a given variable even if its functional dependence on the coordinates changes when we change coordinates.

Consider now a restricted class of transformations, called regular transformations, which preserve the range of the variables: (q, p) and (Q, P) have the same range. A change from one Cartesian coordinate to a translated or rotated one is regular (each variable goes from —∞ to +∞ before and after), whereas a change to spherical coordinates (where some coordinates are nonnegative, some are bounded by 2π, etc.) is not.

A regular transformation (q, p) -> (Q, P) permits an alternate interpretation: instead of viewing (Q, P) as the same phase space point in a new coordinate system, we may view it as a new point in the same coordinate system. This corresponds to an active transformation which changes the state of the system. Under this change, the numerical value of any dynamical variable ω(q, p) will generally change: ω (q, p) ≠ ω(Q, P), though its functional dependence will not: ω(Q, P) is the same function ω(q, p) evaluated at the new point (q= Q, p= P).

We say that ω is invariant under the regular transformation (q, p) -> (Q, P) if ω(q, p) = ω(Q, P)  (2.7.21)

(This equation has content only if we are talking about the active transformations, for it is true for any ω under a passive transformation.)

Whether we view the transformation (q, p) -> (Q, P) as active or passive, it is called canonical.

if they obey Eq. (2.7.18). As we shall see, only regular canonical transformations are physically interesting.

2.8. Symmetries and Their Consequences

Let us begin our discussion by examining what the word "symmetry" means in daily usage. We say that a sphere is a very symmetric object because it looks the same when seen from many directions. Or, equivalently, a sphere looks the same before and after it is subjected to a rotation around any axis passing through its center. A cylinder has symmetry too, but not as much: the rotation must be performed around its axis. Generally then, the symmetry of an object implies its invariance under some transformations, which in our example are rotations.

A symmetry can be discrete or continuous, as illustrated by the example of a hexagon and a circle. While the rotation angles that leave a hexagon unchanged form a discrete set, namely, multiples of 60°, the corresponding set for a circle is a continuum. We may characterize the continuous symmetry of the circle in another way. Consider the identity transformation, which does nothing, i.e., rotates by 0° in our example. This leaves both the circle and the hexagon invariant. Consider next an infinitesimal transformation, which is infinitesimally "close" to the identity; in our example this is a rotation by an infinitesimal angle ε. The infinitesimal rotation leaves the circle invariant but not the hexagon. The circle is thus characterized by its invariance under infinitesimal rotations. Given this property, its invariance under finite rotations follows, for any finite rotation may be viewed as a sequence of infinitesimal rotations (each of which leaves it invariant).

It is also possible to think of functions of some variables as being symmetric in the sense that if one changes the values of the variables in a certain way, the value of the function is invariant. Consider for example f(x, y) = x^2 + y^2.

If we make the following change x → x' = x cos θ - y sin θ, y → y' = x sin θ + y cos θ, (2.8.1)

in the arguments, we find that f is invariant. We say that f is symmetric under the above transformation. In the terminology introduced earlier, the transformation in question is continuous: its infinitesimal version is x → x' = x cos ε - y sin ε ≈ x - yε, y → y' = x sin ε + y cos ε ≈ xε + y (to order ε). (2.8.2)

Consider now the function H(q, p). There are two important dynamical consequences that follow from its invariance under regular canonical transformations.

I. If H is invariant under the following infinitesimal transformation (which you may verify is canonical, Exercise 2.8.2), δq_i = ε ∂g/∂p_i, δp_i = -ε ∂g/∂q_i, (2.8.3)

where g(q, p) is any dynamical variable, then g is conserved, i.e., a constant of motion. One calls g the generator of the transformation.

II. If H is invariant under the regular, canonical, but not necessarily infinitesimal, transformation (q, p) → (Q, P), and if (q(t), p(t)) is a solution to the equations of motion, so is the transformed (translated, rotated, etc.) trajectory (Q(t), P(t)).

Let us now analyze these two consequences.

Consequence I. Let us first verify that g is indeed conserved if H is invariant under the transformation it generates. Working to first order in ε, if we equate the change in H under the change of its arguments to zero, we get δH = (∂H/∂q_i)δq_i + (∂H/∂p_i)δp_i = (∂H/∂q_i)(ε ∂g/∂p_i) + (∂H/∂p_i)(-ε ∂g/∂q_i) = ε {H, g} = 0. (2.8.4)

But according to Eq. (2.7.2), {H, g} = 0 ⇒ g is conserved. (2.8.5)

(More generally, the response of any variable ω to the transformation is δω = ε {ω, g}. (2.8.6))

Consider as an example, a particle in one dimension and the case g=p. From Eq. (2.8.3), δx = ε ∂p/∂p = ε, δp = -ε ∂p/∂x = 0, (2.8.7)

which we recognize to be an infinitesimal translation. Thus the linear momentum p is the generator of spatial translations and is conserved in a translationally invariant problem. The physics behind this result is clear. Since p is unchanged in a translation, so is T = p^2/2m. Consequently V(x + ε) = V(x). But if the potential doesn't vary from point to point, there is no force and p is conserved.

Next consider an example from two dimensions with g = L_z = x p_y - y p_x. Here, δx = -yε (= ε ∂L_z/∂p_x), δy = xε (= ε ∂L_z/∂p_y), δp_x = -p_yε (= -ε ∂L_z/∂x), δp_y = p_xε (= -ε ∂L_z/∂y), (2.8.8)

which we recognize to be an infinitesimal rotation around the z axis, [Eq. (2.8.2)]. Thus the angular momentum around the z axis is the generator of rotations around that axis, and is conserved if H is invariant under rotations of the state around that axis. The relation between the symmetry and the conservation law may be understood in the following familiar terms. Under the rotation of the coordinates and the momenta, H doesn't change and so neither does T = |p|^2/2m. Consequently, V is a constant as we go along any circle centered at the origin. This in turn means that there is no force in the tangential direction and so no torque around the z axis. The conservation of L_z then follows.

Exercise 2.8.1. Show that p = p1 + p2, the total momentum, is the generator of infinitesimal translations for a two-particle system.

Exercise 2.8.2.* Verify that the infinitesimal transformation generated by any dynamical variable g is a canonical transformation. (Hint: Work, as usual, to first order in ε.)

Exercise 2.8.3. Consider H = p_x^2/(2m) + p_y^2/(2m) + (1/2)mω^2(x^2 + y^2), whose invariance under the rotation of the coordinates and momenta leads to the conservation of L_z. But H is also invariant under the rotation of just the coordinates. Verify that this is a noncanonical transformation. Convince yourself that in this case it is not possible to write δH as ε {H, g} for any g, i.e., that no conservation law follows.

Exercise 2.8.4.* Consider H = p_x^2 + p_y^2 + L_z which is invariant under infinitesimal rotations in phase space (the x-p plane). Find the generator of this transformation (after verifying that it is canonical). (You could have guessed the answer based on Exercise 2.5.2.).

The preceding analysis yields, as a by-product, a way to generate infinitesimal canonical transformations. We take any function g(q, p) and obtain the transformation given by Eq. (2.8.6). (Recall that although we defined a canonical transformation earlier, until now we had no means of generating one.) Given an infinitesimal canonical transformation, we can get a finite one by "integrating" it. The following examples should convince you that this is possible. Consider the transformation generated by g = H. We have δq_i = ε {q_i, H}, δp_i = ε {p_i, H}. (2.8.9)

But we know from the equations of motion that ẏ_i = {q_i, H}, etc. So δq_i = ε ẏ_i, δp_i = ε ṗ_i. (2.8.10)

Thus the new point in phase space (q, p) = (q + δq, p + δp) obtained by this canonical transformation of (q, p) is just the point to which (q, p) would move in an infinitesimal time interval ε. In other words, the motion of points in phase space under the time evolution generated by H is an active canonical transformation. Now, you know that by integrating the equations of motion, we can find (q(t), p(t)) at any future time, i.e., get the finite canonical transformation.

Consider now a general case of g ≠ H. We still have δq_i = ε {q_i, g}, δp_i = ε {p_i, g}. (2.8.11)

Mathematically, these equations are identical to Eq. (2.8.9), with g playing the role of the Hamiltonian. Clearly there should be no problem integrating these equations for the evolution of the phase space points under the "fake" Hamiltonian g and fake "time" ε. Let us consider for instance the case g = L_z which has units erg sec and the corresponding fake time ε = δθ, an angle. The transformation of the coordinates is δx = ε {x, L_z} = -ε y, δy = ε {y, L_z} = ε x. (2.8.12)

The fake equations of motion are dx/dδθ = -y, dy/dδθ = x. (2.8.13)

Differentiating first with respect to θ, and using the second, we get d^2x/dδθ^2 + x = 0, and likewise, d^2y/dδθ^2 + y = 0.

So x = A cos δθ + B sin δθ, y = C sin δθ + D cos δθ.

We find the constants from the "initial" (δθ = 0) coordinates and "velocities": A = x0, D = y0, B = (dx/dδθ)_0 = -y0, C = (dy/dδθ)_0 = x0. Reverting to the standard notation in which (x, y), rather than (x0, y0), labels the initial point and (x', y'), rather than (x, y), denotes the transformed one, we may write the finite canonical transformation (a finite rotation) as x' = x cos δθ - y sin δθ, y' = x sin δθ + y cos δθ. (2.8.14)

Similar equations may be derived for p_x and p_y in terms of p_x0 and p_y0.

Although a wide class of canonical transformations is now open to us, there are many that aren't. For instance, (q, p) → (-q, -p) is a discrete canonical transformation that has no infinitesimal version. There are also the transformations that are not regular, such as the change from Cartesian to spherical coordinates, which have neither infinitesimal forms, nor an active interpretation. We do not consider ways of generating these.

Consequence II. Let us understand the content of this result through an example before turning to the proof. Consider a two-particle system whose Hamiltonian is invariant under the translation of the entire system, i.e., both particles. Let an observer SA prepare, at t = 0, a state (x_01, x_02; p_01, p_02) which evolves as (x_1(t), x_2(t); p_1(t), p_2(t)) for some time and ends up in the state (x_T1, x_T2; p_T1, p_T2) at time T. Let us call the final state the outcome of the experiment conducted by SA. We are told that as a result of the translational invariance of H, any other trajectory that is related to this by an arbitrary translation a is also a solution to the equations of motion. In this case, the initial state, for example, is (x₁ + a, x₂ + a; p₁, p₂). The final state and all intermediate states are likewise displaced by the same amount. To an observer S_B, displaced relative to S_A by an amount a, the evolution of the second system will appear to be identical to what S_A saw in the first. Assuming for the sake of this argument that S_B had in fact prepared the second system, we may say that a given experiment and its translated version will give the same result (as seen by the observers who conducted them) if H is translationally invariant.

The physical idea is the following. For the usual reasons, translational invariance of H implies the invariance of V(x₁, x₂). This in turn means that V(x₁, x₂) = V(x₁ - x₂). Thus each particle cares only about where the other is relative to it, and not about where the system as a whole is in space. Consequently the outcome of the experiment is not affected by an overall translation.

Consequence II is just a generalization of this result to other canonical transformations that leave H° invariant. For instance, if H is rotationally invariant, a given experiment and its rotated version will give the same result (according to the observers who conducted them).

Let us now turn to the proof of the general result.

Proof: Imagine a trajectory (q(t), p(t)) in phase space that satisfies the equations of motion. Let us associate with it an image trajectory, (q'(t), p'(t)), which is obtained by transforming each point (q, p) to the image point (q', p') by means of a regular canonical transformation. We ask if the image point moves according to Hamilton's equation of motion, i.e., if q̇'_i = ∂H'/∂p'_i ,  ṗ'_i = -∂H'/∂q'_i if H is invariant under the transformation (q, p) → (q', p'). Now H(q, p), like any dynamical variable w(q, p), obeys Ḣ = {H, H} If (q, p) → (q', p') were a passive canonical transformation, we could write, since the PB are invariant under such a transformation, Ḣ = {H, H}_passive = ∂H'/∂q'_j ∂H/∂p'_j - ∂H'/∂p'_j ∂H/∂q'_j But it is an active transformation. However, because of the symmetry of H°, i.e., H(q, p) = H(q', p'), we can go through the very same steps that led to Eq. (2.7.16) from Eq. (2.7.14) and prove the result. If you do not believe this, you may verify it by explicit computation using H(q,p)=H(q',p'). A similar argument shows that Ḣ = -∂H'/∂q'_i So the image point moves according to Hamilton's equations. Q.E.D.

Exercise 2.8.5. Why is it that a noncanonical transformation that leaves H° invariant does not map a solution into another? Or, in view of the discussions on consequence II, why is it that an experiment and its transformed version do not give the same result when the transformation that leaves H° invariant is not canonical? It is best to consider an example. Consider the potential given in Exercise 2.8.3. Suppose I release a particle at (x = a, y=0) with (p_x= b, p_y= 0) and you release one in the transformed state in which (x=0, y= a) and (p_x= b, p_y=0), i.e., you rotate the coordinates but not the momenta. This is a noncanonical transformation that leaves H° invariant. Convince yourself that at later times the states of the two particles are not related by the same transformation. Try to understand what goes wrong in the general case.

As you go on and learn quantum mechanics, you will see that the symmetries of the Hamiltonian have similar consequences for the dynamics of the system.

A Useful Relation Between S and E

We now prove a result that will be invoked in Chapter 16: ∂S_cl(qf, tf; qi, ti)/∂tf = H where S_cl(qf, tf; qi, ti) is the action of the classical path from qi, ti to qf, tf and H is the Hamiltonian at the upper end point. Since we shall be working with problems where energy is conserved we may write ∂S_cl(qf, tf; qi, ti)/∂tf = E where E is the conserved energy, constant on the whole trajectory.

At first sight you may think that since S_cl = ∫_{ti}^{tf} L dt the right side must equal L and not -E. The explanation requires Fig. 2.5 wherein we have set qi= ti= 0 for convenience. The derivative we are computing is governed by the change in action of the classical path due to a change in travel by Δtf holding the end points qi and qf fixed. From the figure it is clear that now the particle takes a different classical trajectory x(t)= x_cl(t)+δ(t) with δ(0)=0, so that the total change in action comes from the difference in paths between t = 0 and t= tf as well as the entire action due to the extra travel between tf and tf+ Δtf. Only the latter is given by L Δtf. The correct answer is then δS_cl = ∫_{0}^{tf} [ (∂L/∂x)δ(t) + (∂L/ẋ)δ̇(t) ] dt + L(tf) Δtf = ∫_{0}^{tf} [ (∂L/∂x)δ(t) - d/dt (∂L/ẋ) δ(t) ] dt + L(tf) Δtf = 0 + [ (∂L/ẋ)δ(t) ]_{0}^{tf} + L(tf) Δtf = (∂L/ẋ)|_{tf} δ(tf) + L(tf) Δtf It is clear from the figure that δ(tf) = -ẋ(tf) Δtf so that δS_cl = - (∂L/ẋ) ẋ(tf) Δtf + L(tf) Δtf = - [ (∂L/ẋ) ẋ - L ]_{tf} Δtf = - (-E) Δtf = E Δtf from which the result follows.

Exercise 2.8.6. Show that ∂S_cl/∂qf = p(tf).

Exercise 2.8.7. Consider the harmonic oscillator, for which the general solution is x(t)=A cos ωt+ B sin ωt.

Express the energy in terms of A and B and note that it does not depend on time. Now choose A and B such that x(0) =x₁ and x(T)= x₂. Write down the energy in terms of x₁, x₂, and T. Show that the action for the trajectory connecting x₁ and x₂ is S_cl(x₁, x₂, T) = mω / (2 sin ωT) [ (x₁²+ x₂²) cos ωT – 2x₁x₂].

Verify that ∂S_cl/ ∂T= -E.

All Is Not Well with Classical Mechanics

It was mentioned in the Prelude that as we keep expanding our domain of observations we must constantly check to see if the existing laws of physics continue to explain the new phenomena, and that, if they do not, we must try to find new laws that do. In this chapter you will get acquainted with experiments that betray the inadequacy of the classical scheme. The experiments to be described were never performed exactly as described here, but they contain the essential features of the actual experiments that were performed (in the first quarter of this century) with none of their inessential complications.

3.1. Particles and Waves in Classical Physics

There exist in classical physics two distinct entities: particles and waves. We have studied the particles in some detail in the last chapter and may summarize their essential features as follows. Particles are localized bundles of energy and momentum. They are described at any instant by the state parameters q and q̇ (or q and p). These parameters evolve in time according to some equations of motion. Given the initial values q(t₀) and q̇(t₀) at time t₀, the trajectory q(t) may be deduced for all future times from the equations of motion. A wave, in contrast, is a disturbance spread over space. It is described by a wave function ψ(r, t) which characterizes the disturbance at the point r at time t.

In the case of sound waves, ψ is the excess air pressure above the normal, while in the case of electromagnetic waves, ψ can be any component of the electric field vector E. The analogs of q and q̇ for a wave are ψ and ∂ψ/∂t at each point r, assuming ψ obeys a second-order wave equation in time, such as ∇²ψ - (1/c²) ∂²ψ/∂t² = 0, which describes waves propagating at the speed of light, c. Given ψ(r, 0) and ∂ψ/∂t(r, 0) one can get the wave function ψ(r, t) for all future times by solving the wave equation.

Of special interest to us are waves that are periodic in space and time, called plane waves. In one dimension, the plane wave may be written as ψ(x, t)= A exp [i(2π/λ x - 2π/T t)]= A exp[iθ]  (3.1.1)

At some given time t, the wave is periodic in space with a period λ, called its wavelength, and likewise at a given point x, it is periodic in time, repeating itself every T seconds, T being called the time period. We will often use, instead of λ and T, the related quantities k =2π / λ called the wave number and ω =2π /T called the (angular) frequency. In terms of the phase θ in Eq. (3.1.1), k measures the phase change per unit length at any fixed time t, while ω measures the phase change per unit time at any fixed point x. This wave travels at a speed v= ω/k. To check this claim, note that if we start out at a point where θ= 0 and move along x at a rate x= (ω /k)t, θ remains zero. The overall scale A up front is called the amplitude. For any wave, the intensity is defined to be I=|ψ|². For a plane wave this is a constant equal to |A|². If ψ describes an electromagnetic wave, the intensity is a measure of the energy and momentum carried by the wave. [Since the electromagnetic field is real, only the real part of ψ describes it. However, time averages of the energy and momentum flow are still proportional to the intensity (as defined above) in the case of plane waves.]

Plane waves in three dimension are written as ψ(r, t)= A exp[i(k·r - ωt)], ω = |k|v  (3.1.2)

where each component k_i gives the phase changes per unit length along the ith axis. One calls k the wave vector.†

3.2. An Experiment with Waves and Particles (Classical)

Waves exhibit a phenomenon called interference, which is peculiar to them and is not exhibited by particles described by classical mechanics. This phenomenon is illustrated by the following experiment (Fig. 3.1a). Let a wave ψ =A exp[ikx] be incident on a screen with two slits S1 and S2. Unfortunately we also use k to denote the unit vector along the z axis. It should be clear from the context what it stands for.

beam of incident particles. (b) The pattern with both slits open according to classical mechanics (I1+2 = I1 + I2).

A beam of particles is incident normally on a screen with slits S1 and S2, which are a distance a apart. At a distance d parallel to it is a row of detectors that measures the intensity as a function of the position x measured along AB.

If we first keep only S1 open, the incident wave will come out of S1 and propagate radially outward. One may think of S1 as the virtual source of this wave ψ1, which has the same frequency and wavelength as the incident wave. The intensity pattern I1 = |ψ1|^2 is registered by the detectors. Similarly, if S2 is open instead of S1, the wave ψ2 produces the pattern I2 = |ψ2|^2. In both cases the arrival of energy at the detectors is a smooth function of x and t.

Now if both S1 and S2 are opened, both waves ψ1 and ψ2 are present and produce an intensity pattern I1+2 = |ψ1 + ψ2|^2.

The interesting thing is that I1+2 is not equal to I1 + I2, but rather is the interference pattern shown in Fig. 3.1b. The ups and downs are due to the fact that the waves ψ1 and ψ2 have to travel different distances d1 and d2 to arrive at some given x (see Fig. 3.1a) and thus are not always in step. In particular, the maxima correspond to the case d2 - d1 = nλ (n is an integer), when the waves arrive exactly in step, and the minima correspond to the case d2 - d1 = (2n + 1)λ/2, when the waves are exactly out of step. In terms of the phases θ1 and θ2, θ2(x) - θ1(x) = 2nπ at a maximum and θ2(x) - θ1(x) = (2n + 1)π at a minimum. One can easily show that the spacing Δx between two adjacent maxima is Δx = λd/a.

The feature to take special note of is that if xmin is an interference minimum, there is more energy flowing into xmin with just one slit open than with both. In other words, the opening of an extra slit can actually reduce the energy flow into xmin.

Consider next the experiment with particles (Fig. 3.2a). The source of the incident plane waves is replaced by a source of particles that shoots them toward the screen with varying directions but fixed energy. Let the line AB be filled with an array of particle detectors. Let us define the intensity I(x) to be the number of particles arriving per second at any given x. The patterns with S1 or S2 open are shown in (Fig. 3.2a). These look very much like the corresponding patterns for the wave. The only difference will be that the particles arrive not continuously, but in a staccato fashion, each particle triggering a counter at some single point x at the time of arrival. Although this fact may be obscured if the beam is dense, it can be easily detected as the incident flux is reduced.

What if both S1 and S2 are opened? Classical mechanics has an unambiguous prediction: I1+2 = I1 + I2. The reasoning is as follows: each particle travels along a definite trajectory that passes via S1 or S2 to the destination x. To a particle headed for S1, it is immaterial whether S2 is open or closed. Being localized in space it has no way of even knowing if S2 is open or closed, and thus cannot respond to it in any way. Thus the number coming via S1 to x is independent of whether S2 is open or not and vice versa. It follows that I1+2 = I1 + I2 (Fig. 3.2b).

The following objection may be raised: although particles heading for S1 are not aware that S2 is open, they certainly can be deflected by those coming out of S2, if, for instance, the former are heading for x1 and the latter for x2 (see Fig. 3.1a). This objection can be silenced by sending in one particle at a time. A given particle will of course not produce a pattern like I1 or I2 by itself, it will go to some point x. If, however, we make a histogram, the envelope of this histogram, after many counts, will define the smooth functions I1, I2, and I1+2. Now the conclusion I1+2 = I1 + I2 is inevitable.

This is what classical physics predicts particles and waves will do in the double-slit experiment.

3.3. The Double-Slit Experiment with Light

Consider now what happens when we perform the following experiment to check the classical physics notion that light is an electromagnetic wave phenomenon. We set up the double slit as in Fig. 3.1a, with a row of light-sensitive meters along AB and send a beam ψc = A e^(i(ky - ωt)) in a direction perpendicular to the screen. (Strictly speaking, the electromagnetic wave must be characterized by giving the orientation of the E and B vectors in addition to ω and k. However, for a plane wave, B is uniquely fixed by E. If we further assume E is polarized perpendicular to the page, this polarization is unaffected by the double slit. We can therefore suppress the explicit reference to this constant vector and represent the field as a scalar function ψc.) We find that with the slits open one at a time we get patterns I1 and I2, and with both slits open we get the interference pattern I1+2 as in Figs. 3.1a and 3.1b. (The interference pattern is of course what convinced classical physicists that light was a wave phenomenon.) The energy arrives at the detectors smoothly and continuously as befitting a wave.

Say we repeat the experiment with a change that is expected (in classical physics) to produce no qualitative effects. We start with S1 open and cut down the intensity. A very strange thing happens. We find that the energy is not arriving continuously, but in sudden bursts, a burst here, a burst there, etc. We now cut down the intensity further so that only one detector gets activated at a given time and there is enough of a gap, say a millisecond, between counts. As each burst occurs at some x, we record it and plot a histogram. With enough data, the envelope of the histogram becomes, of course, the pattern I1. We have made an important discovery: light energy is not continuous—it comes in bundles. This discrete nature is obscured in intense beams, for the bundles come in so fast and all over the line AB, that the energy flow seems continuous in space and time.

We pursue our study of these bundles, called photons, in some detail and find the following properties:

## 1. Each bundle carries the same energy E

## 2. Each bundle carries the same momentum p

3. E = pc. From the famous equation E^2 = p^2c^2 + m^2c^4, we deduce that these bundles are particles of zero mass.

## 4. If we vary the frequency of the light source we discover that

E = hω (3.3.1)

p = ℏk (3.3.2)

where ℏ = h/2π is a constant. The constant h is called Planck's constant, and has the dimensions of erg sec, which is the same as that of action and angular momentum. Its value is ℏ ≈ h/2π ≈ 10^{-27} erg sec (3.3.3)

For those interested in history, the actual experiment that revealed the granular nature of light is called the photoelectric effect. The correct explanation of this experiment, in terms of photons, was given by Einstein in 1905.

That light is made of particles will, of course, surprise classical physicists but will not imply the end of classical physics, for physicists are used to the idea that phenomena that seem continuous at first sight may in reality be discrete. They will cheerfully plunge into the study of the dynamics of the photons, trying to find the equations of motion for its trajectory and so on. What really undermines classical physics is the fact that if we now open both slits, still keeping the intensity so low that only one photon is in the experimental region at a given time, and watch the histogram take shape, we won't find that I1+2 equals I1 + I2 as would be expected of particles, but is instead an interference pattern characteristic of wave number k. This result completely rules out the possibility that photons move in well-defined trajectories like the particles of classical mechanics—for if this were true, a photon going in via S1 should be insensitive to whether S2 is open or not (and vice versa), and the result I1+2 = I1 + I2 is inescapable! To say this another way, consider a point xmin which is an interference minimum. More photons arrive here with either S1 or S2 open than with both open. If photons followed definite trajectories, it is incomprehensible how opening an extra pathway can reduce the number coming to xmin. Since we are doing the experiment with one photon at a time, one cannot even raise the improbable hypothesis that photons coming out of S1 collide with those coming out of S2 to modify (miraculously) the smooth pattern I1 + I2 into the wiggly interference pattern.

From these facts Born drew the following conclusion: with each photon is associated a wave ψ, called the probability amplitude or simply amplitude, whose modulus squared |ψ(x)|^2 gives the probability of finding the particle at x. [Strictly speaking, we must not refer to |ψ(x)|^2 as the probability for a given x, but rather as the probability density at x since x is a continuous variable. These subtleties can, however, wait.] The entire experiment may be understood in terms of this hypothesis as follows. Every incoming photon of energy E and momentum p has a wave function ψ associated with it, which is a plane wave with ω = E/ℏ and k = p/ℏ. This wave interferes with itself and forms the oscillating pattern |ψ(x)|^2 along AB, which gives the probability that the given photon will arrive at x. A given photon of course arrives at some definite x and does not reveal the probability distribution. If, however, we wait till several photons, all described by the same ψ, have arrived, the number at any x will become proportional to the probability function |ψ(x)|^2. Likewise, if an intense (macroscopic) monochromatic beam is incident, many photons, all described by the same wave and hence the same probability distribution, arrive at the same time and all along the line AB. The intensity distribution then assumes the shape of the probability distribution right away and the energy flow seems continuous and in agreement with the predictions of classical physics.

l electromagnetic theory. The main point to note, besides the probability interpretation, is that a wave is associated not with a beam of photons, but with each photon. If the beam is monochromatic, every photon is given by the same ψ and the same probability distribution. A large ensemble of such photons will reproduce the phenomena expected of a classical electromagnetic wave ψ and the probabilistic aspect will be hidden.

3.4. Matter Waves (de Broglie Waves)

That light, which one thought was a pure wave phenomenon, should consist of photons, prompted de Broglie to conjecture that entities like the electron, generally believed to be particles, should exhibit wavelike behavior. More specifically, he conjectured, in analogy with photons, that particles of momentum p will produce an interference pattern corresponding to a wave number k = p/ℏ in the double-slit experiment. This prediction was verified for electrons by Davisson and Germer, shortly thereafter. It is now widely accepted that all particles are described by probability amplitudes ψ(x), and that the assumption that they move in definite trajectories is ruled out by experiment.

But what about common sense, which says that billiard balls and baseballs travel along definite trajectories? How did classical mechanics survive for three centuries? The answer is that the wave nature of matter is not apparent for macroscopic phenomena since ℏ is so small. The precise meaning of this explanation will become clear only after we fully master quantum mechanics. Nonetheless, the following example should be instructive. Suppose we do the double-slit experiment with pellets of mass 1 g, moving at 1 cm/sec. The wavelength associated with these particles is λ = h/p ≈ 10⁻²⁶ cm, which is 10⁻¹³ times smaller than the radius of the proton! For any reasonable values of the parameters a and d (see Fig. 3.1b), the interference pattern would be so dense in x that our instruments will only measure the smooth average, which will obey I₁ + I₂ = I₁ + I₂ as predicted classically.

3.5. Conclusions The main objective of this chapter was to expose the inadequacy of classical physics in explaining certain phenomena and, incidentally, to get a glimpse of what the new (quantum) physics ought to look like. We found that entities such as the electron are particles in the classical sense in that when detected they seem to carry all their energy, momentum, charge, etc. in localized form; and at the same time they are not particlelike in that assuming they move along definite trajectories leads to conflict with experiment. It appears that each particle has associated with it a wave function ψ(x, t), such that |ψ(x, t)|² gives the probability of finding it at a point x at time t. This is called wave-particle duality.

The dynamics of the particle is then the dynamics of this function ψ(x, t) or, if we think of functions as vectors in an infinite-dimensional space, of the ket |ψ(t)⟩. In the next chapter the postulates of quantum theory will define the dynamics in terms of |ψ(t)⟩. The postulates, which specify what sort of information is contained in |ψ(t)⟩ and how |ψ(t)⟩ evolves with time, summarize the results of the double-slit experiment and many others not mentioned here. The double-slit experiment was described here to expose the inadequacy of classical physics and not to summarize the entire body of experimental results from which all the postulates could be inferred. Fortunately, the double-slit experiment contains most of the central features of the theory, so that when the postulates are encountered in the next chapter, they will appear highly plausible.

The Postulates: A General Discussion Having acquired the necessary mathematical training and physical motivation, you are now ready to get acquainted with the postulates of quantum mechanics. In this chapter the postulates will be stated and discussed in broad terms to bring out the essential features of quantum theory. The subsequent chapters will simply be applications of these postulates to the solution of a variety of physically interesting problems. Despite your preparation you may still find the postulates somewhat abstract and mystifying on this first encounter. These feelings will, however, disappear after you have worked with the subject for some time.

4.1. The Postulates The following are the postulates of nonrelativistic quantum mechanics. We consider first a system with one degree of freedom, namely, a single particle in one space dimension. The straightforward generalization to more particles and higher dimensions will be discussed towards the end of the chapter. In what follows, the quantum postulates are accompanied by their classical counterparts (in the Hamiltonian formalism) to provide some perspective.

Classical Mechanics | Quantum Mechanics I. The state of a particle at any given time is specified by the two variables x(t) and p(t), i.e., as a point in a two-dimensional phase space. | I. The state of the particle is represented by a vector |ψ(t)⟩ in a Hilbert space.

II. Every dynamical variable ω is a function of x and p: ω = ω(x, p). | II. The independent variables x and p of classical mechanics are represented by Hermitian operators X and P with the following matrix elements in the eigenbasis of X: ⟨x|X|x'⟩ = xδ(x − x'), ⟨x|P|x'⟩ = −iℏ ∂/∂x δ(x − x'). The operators corresponding to dependent variables ω(x, p) are given by Hermitian operators Ω(X, P) = ω(x → X, p → P).

III. If the particle is in a state given by x and p, the measurement of the variable ω will yield a value ω(x, p). The state will remain unaffected. | III. If the particle is in a state |ψ⟩, measurement of the variable corresponding to Ω will yield one of the eigenvalues ω with probability P(ω) = |⟨ω|ψ⟩|². The state of the system will change from |ψ⟩ to |ω⟩ as a result of the measurement.

IV. The state variables change with time according to Hamilton's equations: ẋ = ∂H/∂p, ṗ = −∂H/∂x. | IV. The state vector |ψ(t)⟩ obeys the Schrödinger equation iℏ d/dt |ψ(t)⟩ = H |ψ(t)⟩, where H(X, P) = ω(x → X, p → P) is the quantum Hamiltonian operator and H is the Hamiltonian for the corresponding classical problem.

4.2. Discussion of Postulates I, II, and III The postulates (of classical and quantum mechanics) fall naturally into two sets: the first three, which tell us how the system is depicted at a given time, and the last, which specifies how this picture changes with time. We will confine our attention to the first three postulates in this section, leaving the fourth for the next.

The first postulate states that a particle is described by a ket |ψ⟩ in a Hilbert space which, you will recall, contains proper vectors normalizable to unity as well as improper vectors, normalizable only to the Dirac delta functions. Now, a ket in such a space has in general an infinite number of components in a given basis. One wonders why a particle, which had only two independent degrees of freedom, x and p, in classical mechanics, now needs to be specified by an infinite number of variables. What do these variables tell us about the particle? To understand this we must go on to the next two postulates, which answer exactly this question. For the present let us note that the double-slit experiment has already hinted to us that a particle such as the electron needs to be described by a wave function ψ(x). We have seen in Section 1.10 that a function f(x) may be viewed as a ket |f⟩ in a Hilbert space. The ket |ψ⟩ of quantum mechanics is none other than the vector representing the probability amplitude ψ(x) introduced in the double-slit experiment.

When we say that |ψ⟩ is an element of a vector space we mean that if |ψ⟩ and |ψ'⟩ represent possible states of a particle so does α|ψ⟩ + β|ψ'⟩. This is called the principle of superposition. The principle by itself is not so new: we know in classical physics, for example, that if f(x) and g(x) [with f(0) = f(L) = g(0) = g(L) = 0] are two possible displacements of a string, so is the superposition αf(x) + βg(x). What is new is the interpretation of the superposed state α|ψ⟩ + β|ψ'⟩. In the case of the string, the state αf + βg has very different attributes from the states f and g: it will look different, have a different amount of stored elastic energy, and so on. In quantum theory, on the other hand, the state α|ψ⟩ + β|ψ'⟩ will, loosely speaking, have attributes that sometimes resemble that of |ψ⟩ and at other times those of |ψ'⟩. There is, however, no need to speak loosely, since we have postulates II and III to tell us exactly how the state vector |ψ⟩ is to be interpreted in quantum theory. Let us find out.

In classical mechanics when a state (x, p) is given, one can say that any dynamical variable ω has a value ω(x, p), in the sense that if the variable is measured the result ω(x, p) will obtain. What is the analogous statement one can make in quantum mechanics given that the particle is in a state |ψ⟩? The answer is provided by Postulates II and III, in terms of the following steps: Step 1. Construct the corresponding quantum operator Ω = ω(x → X, p → P), where X and P are the operators defined in postulate II.

Step 2. Find the orthonormal eigenvectors |ω⟩ of Ω and the corresponding eigenvalues ω, such that Ω|ω⟩ = ω|ω⟩.

Step 3. Expand |ψ⟩ in the basis of the |ω⟩'s: |ψ⟩ = Σ_ω c_ω |ω⟩, with c_ω = ⟨ω|ψ⟩.

Step 4. The probability that the measurement yields ω is |c_ω|² = |⟨ω|ψ⟩|². If the measurement yields ω, the state of the system becomes |ω⟩.

ω, and eigenvalues ω, of Q.

Step 3. Expand |ψ> in this basis: |ψ> = ∑_i c_i |ω_i>

Step 4. The probability P(ω) that the result ω will obtain is proportional to the modulus squared of the projection of |ψ> along the eigenvector |ω>, that is P(ω) ∝ |<ω|ψ>|². In terms of the projection operator P_ω = |ω><ω|, P(ω) ∝ |<ω|ψ>|² = <ψ|ω><ω|ψ> = <ψ|P_ω|ψ> = <ψ|P_ω†P_ω|ψ> = <P_ωψ|P_ωψ>.

There is a tremendous amount of information contained in these steps. Let us note, for the present, the following salient points.

The status of the two classes will be clarified later in this chapter.

(1) The theory makes only probabilistic predictions for the result of a measure- ment of Q. Further, it assigns (relative) probabilities only for obtaining some eigen- value ω of Q. Thus the only possible values of Q are its eigenvalues. Since postulate II demands that Q be Hermitian, these eigenvalues are all real.

(2) Since we are told that P(ω) ∝ |<ω|ψ>|², the quantity |<ω|ψ>|² is only the relative probability. To get the absolute probability, we divide |<ω_i|ψ>|² by the sum of all relative probabilities: P(ω_i) = |<ω_i|ψ>|² / ∑_i |<ω_i|ψ>|² = |<ω_i|ψ>|² / <ψ|ψ>   (4.2.1)

It is clear that if we had started with a normalized state |ψ'> = |ψ> / √(<ψ|ψ>)

we would have had P(ω) = |<ω|ψ>|²   (4.2.2)

If |ψ> is a proper vector, such a rescaling is possible and will be assumed hereafter. The probability interpretation breaks down if |ψ> happens to be one of the improper vectors in the space, for in this case <ψ|ψ> = δ(0) is the only sensible normalization. The status of such vectors will be explained in Example 4.2.2 below.

Note that the condition <ψ|ψ> = 1 is a matter of convenience and not a physical restriction on the proper vectors. (In fact the set of all normalized vectors does not even form a vector space. If |ψ> and |φ> are normalized, then an arbitrary linear combination, a|ψ> + b|φ> is not.)

Note that the relative probability distributions corresponding to the states |ψ> and |φ> when they are renormalized to unity, reduce to the same absolute probabil- ity distribution. Thus, corresponding to each physical state, there exists not one vector, but a ray or "direction" in Hilbert space. When we speak of the state of the particle, we usually mean the ket |ψ> with unit norm. Even with the condition <ψ|ψ> = 1, we have the freedom to multiply the ket by a number of the form e^{iδ} without changing the physical state. This freedom will be exploited at times to make the components of |ψ> in some basis come out real.

(3) If |ψ> is an eigenstate |ω_i>, the measurement of Q is guaranteed to yield the result ω_i. A particle in such a state may be said to have a value ω_i for Q in the classical sense.

(4) When two states |ω_1> and |ω_2> are superposed to form a (normalized)

state, such as |ψ> = (a|ω_1> + b|ω_2>) / √(|a|² + |b|²)

one gets the state, which upon measurement of Q, can yield either ω_1 or ω_2 with probabilities |a|² / (|a|² + |b|²) and |b|² / (|a|² + |b|²), respectively. This is the peculiar consequence of the superposition principle in quantum theory, referred to earlier. It has no analog in classical mechanics. For example, if a dynamical variable of the string in the state af + bg is measured, one does not expect to get the value corre- sponding to f some of the time and that corresponding to g the rest of the time; instead, one expects a unique value generally distinct from both. Likewise, the functions f and af (a real) describe two distinct configurations of the string and are not physically equivalent.

(5) When one wants information about another variable A, one repeats the whole process, finding the eigenvectors |A_i> and the eigenvalues A_i. Then P(A_i) = |<A_i|ψ>|² The bases of Q and A will of course be different in general. In summary, we have a single ket |ψ> representing the state of the particle in Hilbert space, and it contains the statistical prediction for all observables. To extract this information for any observable, we must determine the eigenbasis of the corresponding operator and find the projection of |ψ> along all its eigenkets.

(6) As our interest switches from one variable Q to another, A, so does our interest go from the kets |ω_i> to the kets |A_i>. There is, however, no need to change the basis each time. Suppose for example we are working in the Q basis in which |ψ> = ∑_i c_i |ω_i> = ∑_i |ω_i><ω_i|ψ> and P(ω_1) = |<ω_1|ψ>|². If we want P(A_i), we take the operator A (which is some given matrix with elements A_{ij} = <ω_i|A|ω_j>); find its eigenvectors |A_i> (which are column vectors with components <ω_j|A_i>), and take the inner product <A_i|ψ> in this basis: |ψ> = ∑_i |A_i><A_i|ψ>

Example 4.2.1. Consider the following example from a fictitious Hilbert space V_3(R) (Fig. 4.1). In Fig. 4.1a we have the normalized state |ψ>, with no reference to any basis. To get predictions on Q, we find its eigenbasis and express the state vector |ψ> in terms of the orthonormal eigenvectors |ω_1>, |ω_2>, and |ω_3> (Fig.

4.1b). Let us suppose |ψ> = (1/2)|ω_1> + (1/2)|ω_2> + (1/√2)|ω_3> This means that the values ω_1, ω_2, and ω_3 are expected with probabilities 1/4, 1/4, and 1/2, respectively, and other values of ω are impossible. If instead |ψ> were some eigenvector, say |ω_1>, then the result ω_1 would obtain with unit probability. Only a particle in a state |ψ> = |ω_i> has a well-defined value of Q in the classical sense. If we want P(A_i), we construct the basis |A_1>, |A_2>, and |A_3>, which can in general be distinct from the Q basis. In our example (Fig. 4.1c) there is just one common eigenvector |ω_3> = |A_3>.

Returning to our main discussion, there are a few complications that could arise as one tries to carry out the steps 1-4. We discuss below the major ones and how they are to be surmounted.

Complication 1: The Recipe Q = Q(x→X, p→P) Is Ambiguous. If, for example, Q = xp, we don't know if Q=XP or PX since xp=px classically. There is no universal recipe for resolving such ambiguities. In the present case, the rule is to use the symmetric sum: Q=(XP+PX)/2. Notice incidentally that symmetrization also renders Q Hermitian. Symmetrization is the answer as long as Q does not involve products of two or more powers of X with two or more powers of P. If it does, only experiment can decide the correct prescription. We will not encounter such cases in this book.

Complication 2: The Operator Q Is Degenerate. Let us say ω_1 = ω_2 = ω. What is P(ω) in this case? We select some orthonormal basis |ω,1> and |ω,2> in the eigenspace V_ω, with eigenvalue ω. Then P(ω) = |<ω,1|ψ>|² + |<ω,2|ψ>|² which is the modulus squared of the projection of |ψ> in the degenerate eigenspace.

This is the result we will get if we assume that ω_1 and ω_2 are infinitesimally distinct and ask for P(ω_1 or ω_2). In terms of the projection operator for the eigenspace, P_ω = |ω,1><ω,1| + |ω,2><ω,2|   (4.2.3a)

we have P(ω) = <ψ|P_ω|ψ>   (4.2.3b)

In general, one can replace in Postulate III P(ω) ∝ <ψ|P_ω|ψ> where P_ω is the projection operator for the eigenspace with eigenvalue ω. Then postulate III as stated originally would become a special case in which there is no degeneracy and each eigenspace is simply an eigenvector.

In our example from V_3(R), if ω_1 = ω_2 = ω (Fig. 4.1b) then P(ω) is the square of the component of |ψ> in the "x-y" plane.

Complication 3: The Eigen value Spectrum of Q Is Continuous. In this case one expands |ψ> as |ψ> = ∫ dω |ω><ω|ψ> One expects that as ω varies continuously, so will <ω|ψ>, that is to say, one expects <ω|ψ> to be a smooth function ψ(ω). To visualize this function one introduces an auxiliary one-dimensional space, called the ω space, the points in which are labeled by the coordinate ω. In this space ψ(ω) will be a smooth function of ω and is called the wave function in the ω space. We are merely doing the converse of what we did in Section 1.10 wherein we started with a function f(x) and tried to interpret it as the components of an infinite-dimensional ket |ψ> in the |x> basis. As far as the state vector |ψ> is concerned, there is just one space, the Hilbert space, in which it resides. The ω space, the A space, etc. are auxiliary manifolds introduced for the purpose of visualizing the components of the infinite-dimensional vector |ψ> in the Q basis, the A basis, and so on. The wave function ψ(ω) is also called the probability amplitude for finding the particle with Q = ω.

Can we interpret |<ω|ψ>|² as the probability for finding the particle with a value ω for Q? No. Since the number of possible values for ω is infinite and the total probability is unity, each single value of ω can be assigned only an infinitesimal probability. One interprets P(ω) = |<ω|ψ>|² to be the probability density at ω, by which one means that P(ω) dω is the probability of obtaining a result between ω and ω + dω). This definition meets the requirement that the total probability be unity, since ∫ P(ω) dω = ∫ |<ω|ψ>|² dω = ∫ <ψ|ω><ω|ψ> dω = <ψ| (∫ |ω><ω| dω) |ψ> = <ψ|ψ> = 1   (4.2.4)

If <ψ|ψ> = δ(0) is the only sensible normalization possible, the state cannot be normalized to unity and P(ω) must be interpreted as the relative probability density.

We will discuss such improper states later.

An important example of a continuous spectrum is that of X, the operator corresponding to the position x. The wave function 态矢在X基（或x空间）中的分量w(x)，通常直接被称为波函数，因为几乎总是使用X基。在上一章的讨论中，|ψ(x)|²被称为在给定x处找到粒子的概率，而非概率密度，以避免涉及细节。现在，是时候明确这一点了！

早在之前，我们曾思考为何一个经典粒子只需由两个数x和p定义，而现在却需要由一个具有无限多个分量的右矢来描述。答案现在很清楚了。经典粒子在任何给定时刻都有一个确定的位置。在指定其状态时，只需给出这个x的值。而量子粒子，在测量时可以取任何x值，因此必须给出所有可能结果的相对概率。

ψ>的部分信息包含在ψ(x)=<x|ψ>中，即|ψ>在X基中的分量。当然，在经典粒子的情况下，还需要指定动量p。在量子理论中，同样需要给出获得不同动量值的概率，但这不需要一个新的矢量来指定；同一个右矢|ψ>用动量算符P的本征右矢|p>展开，通过p空间中的波函数ψ(p)=<p|ψ>给出概率。

复杂性4：量子变量Ω没有经典对应物。即使是“点”粒子如电子，现在已知也携带“自旋”，这是一种内部角动量，即与其在空间中的运动无关的角动量。由于经典力学中缺少这种自由度，我们的公设并未告诉我们量子理论中用哪个算符来描述这个变量。正如我们将在第14章看到的，解决方案来自于直觉和半经典推理的结合。值得记住的是，无论公设构建得多么严谨，它们往往还需要直觉和经典思想的补充。

在讨论了从态矢量中提取统计信息的四步程序后，我们继续研究量子理论公设还告诉了我们什么。

态矢量的坍缩

我们现在考察公设III的另一个方面，即变量Ω的测量会改变态矢量（该态矢量通常是形如 |ψ> = Σ |ω><ω|ψ> 的叠加态），使其变为与测量中得到的本征值ω相对应的本征态|ω>。这种现象被称为态矢量的坍缩或约化。

我们首先注意到，任何关于测量过程影响的明确陈述，都预设了测量过程是某种确定的类型。例如，经典力学的公理认为，任何动力学变量都可以在不改变粒子状态的情况下被测量，这假设了测量是理想测量（符合经典方案）。但人们可以设想会改变状态的非理想测量；想象一下，在黑暗的房间里挥舞扫帚直到碰到枝形吊灯来定位它。使公设III深刻之处在于，其中所指的测量过程是一种理想的量子测量，从某种意义上说，这是人们所能做的最好的测量。我们现在通过一个例子来说明理想量子测量的概念和这个公设的内容。

考虑一个处于动量本征态|p>的粒子。公设告诉我们，如果测量此态的动量，我们保证会得到结果p，并且测量后状态将保持不变（因为|p>已经是所讨论算符P的本征态）。测量粒子动量的一种方法是康普顿散射，即一个具有确定动量的光子从粒子上反弹回来。

让我们假设粒子被迫沿x轴运动，并且我们发送一个能量为ℏω的右移光子，它从粒子上反弹后作为能量为ℏω'的左移光子返回。（我们如何知道光子能量是多少？我们假设我们有已知能发射和吸收任何给定能量光子的原子。）使用动量和能量守恒： cp' = cp + ℏ(ω + ω')

E' = E + ℏ(ω - ω')

现在可以从此数据重建粒子的初始和最终动量： p' = (E' - ℏω)/c p = (E - ℏω)/c

由于光子总是将能量损失给粒子（在粒子静止系中很清楚），ω' < ω，并且通过让ω → 0，我们可以使动量变化p' - p任意小。此后，当我们谈论动量测量时，这就是我们的意思。我们还将假设，对每一个动力学变量，都存在一个相应的理想测量。例如，我们将讨论理想位置测量，当对处于态|x>的粒子进行测量时，将以单位概率给出结果x，并使态矢量保持不变。

现在假设我们测量一个处于动量本征态|p>的粒子的位置。由于|p>是位置本征右矢|x>的和， |p> = ∫|x><x|p> dx 测量将迫使系统进入某个态|x>。因此，即使是理想位置测量也会改变不是位置本征态的状态。为什么位置测量会改变态|p>，而动量测量不会？答案是，理想位置测量使用具有无穷大动量的光子（正如我们将看到的），而理想动量测量使用具有无穷小动量的光子（正如我们已经看到的）。

这正是经典力学和量子力学之间的主要区别：在经典力学中，对任何变量ω的理想测量使任何态保持不变，而在量子力学中，对Ω的理想测量只使Ω的本征态保持不变。

测量的影响可以示意性地表示如下： P_ω |ψ> → |ψ> Ω被测量，ω得到 <P_ω|ψ>|^{1/2} 其中P_ω是与|ω>相关的投影算符，测量后的态已被归一化。如果ω是简并的， P_ω |ψ> → |ψ'> 其中P_ω是本征空间V_ω的投影算符。应特别注意以下一点：如果初始态|ψ>未知，且测量得到简并本征值ω，我们将无法确定测量后的态是什么，只能说它是本征值为ω的本征空间中的某个态。另一方面，如果初始态|ψ>已知，且测量得到简并值ω，则测量后的态已知为P_ω|ψ>（归一化后）。考虑我们来自V_3(R)的例子（图4.1b）。假设我们有ω1 = ω2 = ω3 = ω。让我们使用一个标准正交基{|ω,1>, |ω,2>, |ω,3>}，其中，通常，额外的标签1和2是必需的，用于区分简并本征空间中的基矢。如果在此基中，我们知道，例如， |ψ> = |ω,1> + |ω,2> + √2|ω,3> 并且测量给出值ω，则测量后的归一化态已知为 |ψ'> = 1/2 (|ω,1> + |ω,2>)

另一方面，如果初始态未知，且测量给出结果ω，我们只能说 a|ω,1> + b|ω,2> 其中a和b是任意实数。

请注意，尽管我们从测量中不知道a和b是什么，但它们并非任意。换句话说，系统在测量前有一个明确的态矢量|ψ>（尽管我们不知道|ψ>），在测量后也有一个明确的态矢量P_ω|ψ>（尽管我们只知道它位于子空间V_ω内）。

如何检验量子理论 125 经典力学的一个突出特点是它做出完全确定性的预测。例如，它可以预测一个在势V(x)中以动量p_i从x_i出发的粒子，将在2秒后以动量p_f到达x_f。为了检验这个预测，我们在t=0时将粒子释放于x_i，并具有p=p_i，然后在x_f等待，看粒子是否在t=2秒时以p=p_f到达那里。

另一方面，量子理论对处于态|ψ>的粒子做出统计预测，并声称此态根据薛定谔方程随时间演化。为了检验这些预测，我们必须能够： (1) 制备处于确定态|ψ>的粒子； (2) 在任何时间检验概率预测。

态矢量的坍缩为我们提供了一种制备确定态的好方法：我们从一个处于任意态|ψ>的粒子开始，并测量一个变量Ω。如果我们得到一个非简并本征值ω，我们就得到了态|ω>。（如果ω是简并的，则需要进一步测量。我们不准备讨论这个问题。）请注意，在量子理论中，测量不是告诉我们系统在测量前在做什么，而是告诉我们它在测量后立刻在做什么。（当然，它确实告诉我们原始态在测量后得到的态|ω>上有一定的投影。但与测量后状态的完整描述相比，这个信息微不足道。）

总之，假设我们制备了一个态|ω>。如果我们在之后立即测量某个变量A，这样态就不可能从|ω>改变，并且假设， |ω> = √3/2 |χ1> + √(-1/2) |χ2> + 0（其他项）

该理论预测X1和X2将分别以1/3和2/3的概率获得。如果我们的测量给出一个χ_i，i=1,2（或者更糟的是，一个不是任何本征值的λ！），那么这就是该理论的终点。所以让我们假设我们得到一个允许的值，比如χ1。这与理论一致，但并未完全证实它，因为χ1的概率本可以是1/30而不是1/3，而我们仍然可以得到χ1。因此，我们必须重复实验很多次。但我们不能重复这个实验…… with this particle, since after the measurement the state of the particle is |ξ>. We must start afresh with another particle in |ω>. For this purpose we require a quantum ensemble, which consists of a large number N of particles all in the same state |ω>. If a measurement of Ω is made on every one of these particles, approximately N/3 will yield a value ω₁ and end up in the state |ω₁> while approximately 2N/3 will yield a value ω₂ and end up in a state |ω₂>. For sufficiently large N, the deviations from the fractions 1/3 and 2/3 will be negligible. The chief difference between a classical ensemble, of the type one encounters in, say, classical statistical mechanics, and the quantum ensemble referred to above, is the following. If in a classical ensemble of N particles N/3 gave a result ω₁ and 2N/3 a result ω₂, one can think of the ensemble as having contained N/3 particles with Ω = ω₁ and the others with Ω = ω₂ before the measurement. In a quantum ensemble, on the other hand, every particle is assumed to be in the same state |ω> prior to measurement (i.e., every particle is potentially capable of yielding either result ω₁ or ω₂). Only after the measurement are a third of them forced into the state |ω₁> and the rest into |ω₂>.

Once we have an ensemble, we can measure any other variable and test the expectations of quantum theory. We can also prepare an ensemble, let it evolve in time, and study it at a future time to see if the final state is what the Schrödinger equation tells us it should be.

Example 4.2.2. An example of an ensemble being used to test quantum theory was encountered in the double-slit experiment, say with photons. A given photon of momentum p and energy E was expected to hit the detectors with a probability density given by the oscillating function |ψ(x)|². One could repeat the experiment N times, sending one such photon at a time to see if the final number distribution indeed was given by |ψ(x)|². One could equally well send in a macroscopic, monochromatic beam of light of frequency ω = E/ℏ and wave number k = p/ℏ, which consists of a large number of photons of energy E and momentum p. If one makes the assumption (correct to a high degree) that the photons are noninteracting, sending in the beam is equivalent to experimenting with the ensemble. In this case the intensity pattern will take the shape of the probability density |ψ(x)|², the instant the beam is turned on.

Example 4.2.3. The following example is provided to illustrate the distinction between the probabilistic descriptions of systems in classical mechanics and in quantum mechanics.

We choose as our classical system a six-faced die for which the probabilities P(n) of obtaining a number n have been empirically determined. As our quantum system we take a particle in a state |ψ>. Suppose we close our eyes, toss the die, and cover it with a mug. Its statistical description has many analogies with the quantum description of the state |ψ>: (1) The state of the die is described by a probability function P(n) before the mug is lifted.

(2) The only possible values of n are 1, 2, 3, 4, 5, and 6.

(3) If the mug is lifted, and some value—say n=3—is obtained, the function P(n) collapses to δ(n,3).

(4) If an ensemble of N such dice are thrown, NP(n) of them will give the result n (as N → ∞).

The corresponding statements for the particle in the state |ψ> are no doubt known to you. Let us now examine some of the key differences between the statistical descriptions in the two cases.

(1) It is possible, at least in principle, to predict exactly which face of the die will be on top, given the mass of the die, its position, orientation, velocity, and angular velocity at the time of release, the viscosity of air, the elasticity of the table top, and so on. The statistical description is, however, the only possibility in the quantum case, even in principle.

(2) If the result n=3 was obtained upon lifting the mug, it is consistent to assume that the die was in such a state even prior to measurement. In the quantum case, however, the state after measurement, say |ω₃>, is not the state before measurement, namely |ψ>.

(3) If N such dice are tossed and covered with N mugs, there will be NP(1) dice with n=1, NP(2) dice with n=2, etc. in the ensemble before and after the measurement. In contrast, the quantum ensemble corresponding to |ψ> will contain N particles all of which are in the same state |ψ> (that is, each can yield any of the values ω₁, ..., ω₆) before the measurement, and NP(ωᵢ) particles in |ωᵢ> after the measurement. Only the ensemble before the measurement represents the state |ψ>. The ensemble after measurement is a mixture of six ensembles representing the states |ω₁>, ..., |ω₆>.

Having seen the utility of the ensemble concept in quantum theory, we now define and discuss the two statistical variables that characterize an ensemble.

Expectation Value Given a large ensemble of N particles in a state |ψ>, quantum theory allows us to predict what fraction will yield a value ωᵢ if the variable Ω is measured. This prediction, however, involves solving the eigenvalue problem of the operator Ω. If one is not interested in such detailed information on the state (or the corresponding ensemble) one can calculate instead an average over the ensemble, called the expectation value, <Ω>. The expectation value is just the mean value defined in statistics: <Ω> = Σ P(ωᵢ)ωᵢ = Σ |<ωᵢ|ψ>|²ωᵢ = Σ <ψ|ωᵢ><ωᵢ|ψ>ωᵢ (4.2.5)

But for the factors ωᵢ multiplying each projection operator |ωᵢ><ωᵢ|, we could have used Σ |ωᵢ><ωᵢ| = 1. To get around this, note that Ω|ωᵢ> = ωᵢ|ωᵢ>. Feeding this in and continuing, we get <Ω> = Σ <ψ|Ω|ωᵢ><ωᵢ|ψ> Now we can use Σ |ωᵢ><ωᵢ| = 1 to get <Ω> = <ψ|Ω|ψ> (4.2.6)

This is an example of a mixed ensemble. These will be discussed in the digression on density matrices, which follows in a while.

There are a few points to note in connection with this formula.

(1) To calculate <Ω>, one need only be given the state vector and the operator Ω (say as a column vector and a matrix, respectively, in some basis). There is no need to find the eigenvectors or eigenvalues of Ω.

(2) If the particle is in an eigenstate of Ω, that is Ω|ψ> = ω|ψ>, then <Ω> = ω.

(3) By the average value of Ω we mean the average over the ensemble. A given particle will of course yield only one of the eigenvalues upon measurement. The mean value will generally be an inaccessible value for a single measurement unless it accidentally equals an eigenvalue. [A familiar example of this phenomenon is that of the mean number of children per couple, which may be 2.12, although the number in a given family is restricted to be an integer.]

The Uncertainty In any situation described probabilistically, another useful quantity to specify besides the mean is the standard deviation, which measures the average fluctuation around the mean. It is defined as ΔΩ = [< (Ω - <Ω>)² >]^{1/2} (4.2.7)

and often called the root-mean-squared deviation. In quantum mechanics, it is referred to as the uncertainty in Ω. If Ω has a discrete spectrum, (ΔΩ)² = Σ P(ωᵢ)(ωᵢ - <Ω>)² (4.2.8)

and if it has a continuous spectrum, (ΔΩ)² = ∫ P(ω)(ω - <Ω>)² dω (4.2.9)

Notice that ΔΩ, just like <Ω>, is also calculable given just the state and the operator, for Eq. (4.2.7) means just ΔΩ = [< (ψ| (Ω - <Ω>)² |ψ> >]^{1/2} (4.2.10)

Usually the expectation value and the uncertainty provide us with a fairly good description of the state. For example, if we are given that a particle has <X> = a and ΔX = A, we know that the particle is likely to be spotted near x = a, with deviations of order A.

So far, we have concentrated on the measurement of a single variable at a time. We now turn our attention to the measurement of more than one variable at a time. (Since no two independent measurements can really be performed at the same time, we really mean the measurement of two or more dynamical variables in rapid succession.)

Exercise 4.2.1 (Very Important). Consider the following operators on a Hilbert space V₂(C): Lₓ = 1/√2 [1 0 1; 0 0 0; 1 0 -1], Lᵧ = 1/√2 [-i 0 i; 0 0 0; i 0 -i], Lᵤ = [1 0 0; 0 0 0; 0 0 -1]

(1) What are the possible values one can obtain if Lᵤ is measured?

(2) Take the state in which Lᵤ = 1. In this state what are <Lₓ>, <Lₓ²>, and ΔLᵤ?

(3) Find the normalized eigenstates and the eigenvalues of Lₓ in the Lᵤ basis.

(4) If the particle is in the state with Lᵤ = -1, and Lₓ is measured, what are the possible outcomes and their probabilities?

(5) Consider the state |ψ> = [1/2; 1/√2; 1/2] in the Lᵤ basis. If Lᵤ² is measured in this state and a result +1 is obtained, what is the state after the measurement? How probable was this result? If Lᵤ is measured, what are the outcomes and respective probabilities?

(6) A particle is in a state for which the probabilities are P(Lᵤ = 1) = 1/4, P(Lᵤ = 0) = 1/2, and P(Lᵤ = -1) = 1/4. Convince yourself that the most general, normalized state with this property is |ψ> = (1/2)e^{iδ₁}|1,ᵤ> + (1/√2)e^{iδ₂}|0,ᵤ> + (1/2)e^{iδ₃}|-1,ᵤ>. It was stated earlier on that if |ψ> is a normalized state then the state e^{iα}|ψ> is a physically equivalent normalized state. Does this mean that the factors e^{iδ} multiplying the Lᵤ eigenstates are irrelevant? [Calculate for example P(Lₓ=0).]

Compatible and Incompatible Variables A striking feature of quantum theory is that given a particle in a state |ψ>, one cannot say in general that the particle has a definite value for a given dynamical variable Ω: a measurement can yield any eigenvalue ω for which <ω|ψ> is not zero. The exceptions are the states |ω>. A particle in one of these states can be said, as in classical mechanics, to possess a definite value for that variable.

To have a value ω for Ω, since a measurement is assured to give this result. To produce such states we need only take an arbitrary state |ψ⟩ and measure Ω. The measurement process acts as a filter that lets through just one component of |ψ⟩, along some |ω⟩. The probability that this will happen is P(ω) = |⟨ω|ψ⟩|².

We now wish to extend these ideas to more than one variable. We consider first the question of two operators. The extension to more than two will be straightforward. We ask:

Question 1. Is there some multiple filtering process by which we can take an ensemble of particles in some state |ψ⟩ and produce a state with well-defined values ω and λ for two variables Ω and Λ?

Question 2. What is the probability that the filtering will give such a state if we start with the state |ψ⟩?

To answer these questions, let us try to devise a multiple filtering scheme. Let us first measure Ω on the ensemble described by |ψ⟩ and take the particles that yield a result ω. These are in a state that has a well-defined value for Ω. We immediately measure Λ and pick those particles that give a result λ. Do we have now an ensemble that is in a state with Ω = ω and Λ = λ? Not generally. The reason is clear. After the first measurement, we had the system in the state |ω⟩, which assured a result ω for Ω, but nothing definite for Λ (since |ω⟩ need not be an eigenstate of Λ). Upon performing the second measurement, the state was converted to |λ⟩, and we are now assured a result for Λ, but nothing definite for Ω (since |λ⟩ need not be an eigenstate of Ω).

In other words, the second filtering generally alters the state produced by the first. This change is just the collapse of the state vector |ω⟩ = Σ_i c_i |ω_i⟩ into the eigenstate |λ⟩.

An exception occurs when the state produced after the first measurement is unaffected by the second. This in turn requires that |ω⟩ also be an eigenstate of Λ. The answer to the first question above is then in the affirmative only for the simultaneous eigenstates |ωλ⟩. The means for producing them are just as described above. These kets satisfy the equations

Ω|ωλ⟩ = ω|ωλ⟩ Λ|ωλ⟩ = λ|ωλ⟩

The question that arises naturally is: When will two operators admit simultaneous eigenkets? A necessary (but not sufficient) condition is obtained by operating the first equation with Λ, the second with Ω, and taking the difference:

(ΩΛ - ΛΩ)|ωλ⟩ = 0

Thus [Ω, Λ] must have eigenkets with zero eigenvalue if simultaneous eigenkets are to exist. A pair of operators Ω and Λ will fall into one of the three classes:

A. Compatible: [Ω, Λ] = 0 B. Incompatible: [Ω, Λ] = something that obviously has no zero eigenvalue C. Others

Class A. If two operators commute, we know a complete basis of simultaneous eigenkets can be found. Each element |ωλ⟩ of this basis has well-defined values for Ω and Λ.

Class B. The most famous example of this class is provided by the position and momentum operators X and P, which obey the canonical commutation rule [X, P] = iħ. Evidently we cannot ever have Ω|ψ⟩ = ω|ψ⟩ for any nontrivial |ψ⟩. This means there doesn't exist even a single ket for which both X and P are well defined. Any attempt to filter X is ruined by a subsequent filtering for P and vice versa. This is the origin of the famous Heisenberg uncertainty principle, which will be developed as we go along.

Class C. In this case there are some states that are simultaneous eigenkets. There is nothing very interesting we can say about this case except to emphasize that even if two operators don't commute, one can still find a few common eigenkets, though not a full basis. (Why?)

Let us now turn to the second question of the probability of obtaining a state |ωλ⟩ upon measurement of Ω and Λ in a state |ψ⟩. We will consider just case A; the question doesn't arise for case B, and case C is not very interesting. (You should be able to tackle case C yourself after seeing the other two cases.)

Case A. Let us first assume there is no degeneracy. Thus, to a given eigenvalue λ, there is just one ket and this must be a simultaneous eigenket |ωλ⟩. Suppose we measured Ω first. We get ω with a probability P(ω) = |⟨ω|ψ⟩|². After the measurement, the particle is in a state |ωλ⟩. The measurement of Λ is certain to yield the result λ. The probability for obtaining ω for Ω and λ for Λ is just the product of the two probabilities:

P(ω, λ) = |⟨ωλ|ψ⟩|²

Notice that if Λ were measured first and Ω next, the probability is the same for getting the results λ and ω. Thus if we expand |ψ⟩ in the complete common eigenbasis as

|ψ⟩ = Σ_{ω,λ} |ωλ⟩⟨ωλ|ψ⟩

then

P(ω, λ) = |⟨ωλ|ψ⟩|²

The reason for calling Ω and Λ compatible if [Ω, Λ] = 0 is that the measurement of one variable followed by the other doesn't alter the eigenvalue obtained in the first measurement and we have in the end a state with a well-defined value for both observables. Note the emphasis on the invariance of the eigenvalue under the second measurement. In the non-degenerate case, this implies the invariance of the state vector as well. In the degenerate case, the state vector can change due to the second measurement, though the eigenvalue will not, as the following example will show.

Consider two operators Ω and Λ on ℋ(ℝ). Let |ω₃λ₃⟩ be one common eigenvector. Let λ₁ = λ₂ = λ. Let ω₁ and ω₂ be the eigenvalues of Ω in this degenerate space. Let us use as a basis |ω₁λ⟩, |ω₂λ⟩, and |ω₃λ₃⟩. Consider a normalized state

|ψ⟩ = α|ω₃λ₃⟩ + β|ω₁λ⟩ + γ|ω₂λ⟩

Let us say we measure Ω first and get ω₃. The state becomes |ω₃λ₃⟩ and the subsequent measurement of Λ is assured to give a value λ₃ and to leave the state alone. Thus P(ω₃, λ₃) = |⟨ω₃λ₃|ψ⟩|² = α². Evidently P(ω₃, λ₃) = P(λ₃, ω₃).

Suppose that the measurement of Ω gave a value ω₁. The resulting state is |ω₁λ⟩ and the probability for this outcome is |⟨ω₁λ|ψ⟩|². The subsequent measurement of Λ will leave the state alone and yield the result λ with unit probability. Thus P(ω₁, λ) is the product of the probabilities:

P(ω₁, λ) = |⟨ω₁λ|ψ⟩|² = |β|²

Let us now imagine the measurements carried out in reverse order. Let the result of the measurement of Λ be λ. The state |ψ⟩ after measurement is the projection of |ψ⟩ in the degenerate λ eigenspace:

P_λ|ψ⟩ = β|ω₁λ⟩ + γ|ω₂λ⟩

where, in the expression above, the projected state has been normalized. The probability for this outcome is P(λ) = |β|² + |γ|², the square of the projection of |ψ⟩ in the eigenspace. If Ω is measured now, both results ω₁ and ω₂ are possible. The probability for obtaining ω₁ is |⟨ω₁λ|ψ⟩|² = |β|² / (|β|² + |γ|²). Thus, the probability for the result Λ = λ, Ω = ω₁, is the product of the probabilities:

P(λ, ω₁) = (|β|² + |γ|²) * (|β|² / (|β|² + |γ|²)) = |β|² = P(ω₁, λ)

Thus P(ω₁, λ) = P(λ, ω₁) independent of the degeneracy. But this time the state suffered a change due to the second measurement (unless by accident |ψ⟩ has no component along |ω₂λ⟩). Thus compatibility generally implies the invariance under the second measurement of the eigenvalue measured in the first. Therefore, the state can only be said to remain in the same eigenspace after the second measurement. If the first eigenvalue is non-degenerate, the eigenspace is one dimensional and the state vector itself remains invariant.

In our earlier discussion on how to produce well-defined states |ψ⟩ for testing quantum theory, it was observed that the measurement process could itself be used as a preparation mechanism: if the measurement of Ω on an arbitrary, unknown initial state gives a result ω, we are sure we have the state |ω⟩ = |ω⟩. But this presumes ω is not a degenerate eigenvalue. If Ω is degenerate, we cannot nail down the state, except to within an eigenspace. It was therefore suggested that we stick to variables with a nondegenerate spectrum. We can now lift that restriction. Let us say a degenerate eigenvalue ω for the variable Ω was obtained. We have then some vector in the ω eigenspace. We now measure another compatible variable Λ. If we get a result λ, we have a definite state |ωλ⟩, unless the value (ω, λ) itself is degenerate. We must then measure a third variable Φ compatible with Ω and Λ and so on. Ultimately we will get a state that is unique, given all the simultaneous eigenvalues: |ω, λ, φ, ...⟩. It is presumed that such a set of compatible observables, called a complete set of commuting observables, exists. To prepare a state for studying quantum theory then, we take an arbitrary initial state and filter it by a sequence of compatible measurements till it is down to a unique, known vector. Any nondegenerate operator, all by itself, is a "complete set."

Incidentally, even if the operators Ω and Λ are incompatible, we can specify the probability P(ω, λ) that the measurement of Ω followed by that of Λ on a state |ψ⟩ will give the results ω and λ, respectively. However, the following should be noted:

(1) P(ω, λ) ≠ P(λ, ω) in general.

(2) The probability P(ω, λ) is not the probability for producing a final state that has well-defined values ω and λ for Ω and Λ. (Such a state doesn't exist by the definition of incompatibility.) The state produced by the two measurements is just the eigenstate of the second operator with the measured eigenvalue.

The Density Matrix: A Digression So far we have considered ensembles of N systems all in the same state |ψ⟩. They are hard to come by in practice. More common are ensembles of N systems, n_i (i = 1, 2, . . . , k) of which are in the state |i⟩. (We restrict ourselves to the case where...

e 1i> is an element of an orthonormal basis.) Thus the ensemble is described by k kets |1>, |2>, . . . ,|k>, and k occupancy numbers n1, . . . , nk. A convenient way to assemble all this information is in the form of the density matrix (which is really an operator that becomes a matrix in some basis):

ρ = Σ p_i |i⟩⟨i| (4.2.20)

where p_i = n_i / N is the probability that a system picked randomly out of the ensemble is in the state |i>. The ensembles we have dealt with so far are said to be pure; they correspond to all p_i = 0 except one. A general ensemble is mixed.

Consider now the ensemble average of Q. It is

⟨Q⟩ = Σ ⟨i|Q|i⟩ p_i (4.2.21)

The bar on ⟨Q⟩ reminds us that two kinds of averaging have been carried out: a quantum average ⟨i|Q|i⟩ for each system in |i> and a classical average over the systems in different states |i>. Observe that

Tr(ρQ) = Σ ⟨i|ρQ|i⟩ = Σ ⟨i| (Σ p_j |j⟩⟨j|) Q |i⟩ = Σ p_j ⟨i|j⟩⟨j|Q|i⟩ = Σ p_j ⟨j|Q|i⟩ ⟨i|j⟩ = Σ p_i ⟨i|Q|i⟩ = ⟨Q⟩ (4.2.22)

The density matrix contains all the statistical information about the ensemble. Suppose we want, not ⟨Q⟩, but instead P(ω), the probability of obtaining a particular value ω. We first note that, for a pure ensemble,

P(ω) = |⟨ω|Ψ⟩|² = ⟨Ψ|ω⟩⟨ω|Ψ⟩ = ⟨Ψ|Φ_ω⟩ which combined with Eq. (4.2.22) tells us that

P(ω) = Tr(ρ_ω)

The following results may be easily established: (1) ρ† = ρ (2) Tr ρ = 1 (3) ρ² = ρ for a pure ensemble (4) ρ = (1/k) 𝟙 for an ensemble uniformly distributed over k states (5) Tr ρ² < 1 (equality holds for a pure ensemble) (4.2.23)

You are urged to convince yourself of these relations.

Example 4.2.4. To gain more familiarity with quantum theory let us consider an infinite-dimensional ket |ψ⟩ expanded in the basis |x⟩ of the position operator X:

|ψ⟩ = ∫ dx |x⟩ ψ(x)

We call ψ(x) the wave function (in the X basis). Let us assume ψ(x) is a Gaussian, that is, ψ(x) = A exp[—(x — a)²/2A²] (Fig. 4.2a). We now try to extract information about this state by using the postulates. Let us begin by normalizing the state:

⟨ψ|ψ⟩ = ∫ ⟨ψ|x⟩⟨x|ψ⟩ dx = ∫ |ψ(x)|² dx = A² ∫ exp[—(x—a)²/A²] dx = A² (π A²)^{1/2} (see Appendix A.2)

So the normalized state is

ψ(x) = [1/(π A²)^{1/4}] exp[—(x—a)²/2A²]

The probability for finding the particle between x and x + dx is

P(x) dx = |ψ(x)|² dx = [1/(π A²)^{1/2}] exp[—(x—a)²/A²] dx which looks very much like Fig. 4.2a. Thus the particle is most likely to be found around x = a, and chances of finding it away from this point drop rapidly beyond a distance A. We can quantify these statements by calculating the expectation value and uncertainty for X. Let us do so.

Now, the operator X defined in postulate II is the same one we discussed at length in Section 1.10. Its action in the X basis is simply to multiply by x, i.e., if ⟨x|ψ⟩ = ψ(x)

then,

⟨x|X|ψ⟩ = ∫ ⟨x|X|x'⟩⟨x'|ψ⟩ dx' = ∫ x δ(x— x')ψ(x') dx' = x ψ(x)

Using this result, the mean or expectation value of X is

⟨X⟩ = ⟨ψ|X|ψ⟩ = ∫ ⟨ψ|x⟩⟨x|X|ψ⟩ dx = ∫ ψ*(x) x ψ(x) dx = [1/(π A²)^{1/2}] ∫ x exp[—(x—a)²/A²] dx = a

If we define y = x— a,

⟨X⟩ = [1/(π A²)^{1/2}] ∫ (y + a) exp[—y²/A²] dy = a

We should have anticipated this result of course, since the probability density is symmetrically distributed around x = a.

Next, we calculate the fluctuations around ⟨X⟩ = a, i.e., the uncertainty

ΔX = [⟨(X — ⟨X⟩)²⟩]^{1/2} = [⟨X²⟩ — ⟨X⟩²]^{1/2} = [⟨ψ|X²|ψ⟩ — a²]^{1/2} (since ⟨ψ|X|ψ⟩ = ⟨X⟩ )

= [⟨X²⟩ — a²]^{1/2}

Now

⟨X²⟩ = [1/(π A²)^{1/2}] ∫ x² exp[—(x—a)²/A²] dx

Let y = x— a:

⟨X²⟩ = [1/(π A²)^{1/2}] ∫ (y² + 2ya + a²) exp[—y²/A²] dy = A² + 0 + a²

So ΔX = A/2^{1/2}.

So much for the information on the variable X. Suppose we next want to know the probability distribution for different values of another dynamical variable, say the momentum P.

(1) First we must construct the operator P in this basis.

(2) Then we must find its eigenvalues p, and eigenvectors |p⟩.

(3) Finally, we must take the inner product ⟨p|ψ⟩.

(4) If p is discrete, |⟨p|ψ⟩|² = P(p_i), and if p is continuous, |⟨p|ψ⟩|² = P(p), the probability density.

Now, the P operator is just the K operator discussed in Section 1.10 multiplied by ħ and has the action of —iħ d/dx in the X basis, for if

⟨x|ψ⟩ = ψ(x)

then

⟨x|P|ψ⟩ = ∫ ⟨x|P|x'⟩⟨x'|ψ⟩ dx' (Postulate II)

= ∫ [—iħ δ'(x — x')] ψ(x') dx' = —iħ dψ/dx

Thus, if we project the eigenvalue equation

P|p⟩ = p|p⟩ onto the X basis, we get

⟨x|P|p⟩ = p⟨x|p⟩ or

—iħ dψ_p(x)/dx = p ψ_p(x)

where ψ_p(x)= ⟨x|p⟩. The solutions, normalized to the Dirac delta function, are

ψ_p(x) = [1/(2πħ)^{1/2}] exp(ipx/ħ)

Now we can compute

⟨p|ψ⟩ = ∫ ⟨p|x⟩⟨x|ψ⟩ dx = ∫ ψ_p*(x) ψ(x) dx = [1/(2πħ)^{1/2}] [1/(π A²)^{1/4}] ∫ exp(—ipx/ħ) exp[—(x—a)²/2A²] dx = [1/(ħ^2 π A²)^{1/4}] exp[—p²A²/2ħ²] exp(—ipa/ħ)

The modulus of ψ(p) is a Gaussian (Fig. 4.2b) of width ħ/2^{1/2}A. It follows that ⟨P⟩ = 0, and ΔP = ħ/2^{1/2}A. Since ΔX = A/2^{1/2}, we get the relation ΔX ΔP = ħ/2

The Gaussian happens to saturate the lower bound of the uncertainty relation (to be formally derived in chapter 9) :

ΔX ΔP ≥ ħ/2

The uncertainty relation is a consequence of the general fact that anything narrow in one space is wide in the transform space and vice versa. So if you are a 110-lb weakling and are taunted by a 600-lb bully, just ask him to step into momentum space! =)

This is a good place to point out that the plane waves e^{ipx/ħ} are all improper vectors, i.e., vectors that can't be normalized to unity but only to the Dirac delta function) are introduced into the formalism as purely mathematical entities. Our inability to normalize them to unity translates into our inability to associate with them a sensible absolute probability distribution, so essential to the physical interpretation of the wave function. In the present case we have a particle whose relative probability density is uniform in all of space. Thus the absolute probability of finding it in any finite volume, even as big as our solar system, is zero. Since any particle that we are likely to be interested in will definitely be known to exist in some finite volume of such large dimensions, it is clear that no physically interesting state will be given by a plane wave. But, since the plane waves are eigenfunctions of P, does it mean that states of well-defined momentum do not exist? Yes, in the strict sense. However, there do exist states that are both normalizable to unity (i.e., correspond to proper vectors) and come arbitrarily close to having a precise momentum. For example, a wave function that behaves as e^{ip_0x/ħ} in a large region of space and tapers off to zero beyond, will be normalizable to unity and will have a Fourier transform so sharply peaked at p= p_0 that momentum measurements will only give results practically indistinguishable from p_0. Thus there is no conflict between the fact that plane waves are unphysical, while states of well-defined momentum exist, for "well defined" never means "mathematically exact," but only "exact to any measurable accuracy." Thus a particle coming out of some accelerator with some advertised momentum, say 500 GeV/c, is in a proper normalizable state (since it is known to be located in our laboratory) and not in a plane wave state corresponding to |p= 500 GeV/c⟩.

But despite all this, we will continue to use the eigenkets |p⟩ as basis vectors and to speak of a particle being in the state |p⟩, because these vectors are so much more convenient to handle mathematically than the proper vectors. It should, however, be borne in mind that when we say a particle is (coming out of the accelerator) in a state |p_0⟩, it is really in a proper state with a momentum space wave function so sharply peaked at p= p_0 that it may be replaced by a delta function δ(p— p_0).

The other set of improper kets we will use in the same spirit are the position eigenkets |x⟩, which also form a convenient basis. Again, when we speak of a particle being in a state |x_0⟩ we shall mean that its wave function is so sharply peaked at x= x_0 that it may be treated as a delta function to a good accuracy.

Thus, by the physical Hilbert space, we mean the space of interest to physicists, not one whose elements all correspond to physically realizable states.

Occasionally, the replacement of a proper wave function by its improper counterpart turns out to be a poor approximation. Here is an example from Chapter 19:

Consider the probability that a particle coming out of an accelerator with a nearly exact momentum scatters off a target and enters a detector placed far away, and not in the initial direction. Intuition says that the answer must be zero if the target is absent. This reasonable condition is violated if we approximate the initial state of the particle by a plane wave (which is nonzero everywhere). So we proceed as follows. In the vicinity of the target, we use the plane wave to approximate the initial wave function, for the two are indistinguishable over the (finite and small) range of influence of the target. At the detector, however, we go back to the proper wave (which has tapered off) to represent the initial state.

Exercise 4.2.2.* Show that for a real wave function ψ(x), the expectation value of momentum ⟨P⟩ = 0. (Hint: Show that the probabilities for the momenta ±p are equal.) Generalize this result to the case ψ = C ψ*, where ψ is real and C an arbitrary (real or complex) constant. (Recall that ψ and |ψ⟩ are ph Exercise 4.2.3. Show that if ψ(x) has mean momentum <p>, e^(ipx/ℏ) ψ(x) has mean momentum <p> + p.

Example 4.2.5. The collapse of the state vector and the uncertainty principle play a vital role in explaining the following extension of the double slit experiment. Suppose I say, "I don't believe that a given particle (let us say an electron) doesn't really go through one slit or the other. So I will set up a light source in between the slits to the right of the screen. Each passing electron will be exposed by the beam and I note which slit it comes out of. Then I note where it arrives on the screen. I make a table of how many electrons arrive at each x and which slit they came from. Now there is no escape from the conclusion that the number arriving at a given x is the sum of the numbers arriving via S₁ and S₂. So much for quantum theory and its interference pattern!" But the point of course is that quantum theory no longer predicts an interference pattern! The theory says that if an electron of definite momentum p is involved, the corresponding wave function is a wave with a well-defined wave number k = p/ℏ, which interferes with itself and produces a nice interference pattern. This prediction is valid only as long as the state of the electron is what we say it is. But this state is necessarily altered by the light source, which upon measuring the position of the electron (as being next to S₁, say) changes its wave function from something that was extended in space to something localized near S₁. Once the state is changed, the old prediction of interference is no longer valid. Now, once in a while some electrons will get to the detectors without being detected by the light source. We note where these arrive, but cannot classify them as coming via S₁ or S₂. When the distribution of just these electrons is plotted, sure enough we get the interference pattern. We had better, for quantum theory predicts it, the state not having been tampered with in these cases. The above experiment can also be used to demystify to some extent the collapse of the wave function under measurement. Why is it that even the ideal measurement produces unavoidable changes in the state? The answer, as we shall see, has to do with the fact that ℏ is not zero.

## CHAPTER

Consider the schematic set up in Fig. 4.3. Light of wavelength λ illuminates an electron (e⁻), enters the objective (O) of a microscope (M) and reaches our eye (E). If δθ is the opening angle of the cone of light entering the objective after interacting with electron, classical optics limits the accuracy of the position measurement by an uncertainty Δx ≈ λ / sin δθ. Both classically and quantum mechanically, we can reduce Δx to 0 by reducing λ to zero. In the latter description however, the improved accuracy in the position measurement is at the expense of producing an increased uncertainty in the x component (pₓ) of the electron momentum. The reason is that light of wavelength λ is not a continuous wave whose impact on the electron momentum may be arbitrarily reduced by a reduction of its amplitude, but rather a flux of photons of momentum p = 2πℏ / λ. As λ decreases, the collisions between the electron and the photons become increasingly violent. This in itself would not lead to an uncertainty in the electron momentum, were it not for the fact that the x component of the photons entering the objective can range from 0 to p sin δθ = 2πℏ sin δθ / λ. Since at least one photon must reach our eyes after bouncing off the electron for us to see it, there is a minimum uncertainty in the recoil momentum of the electron given by Δpₓ ≈ ℏ sin δθ / λ. Consequently, we have at the end of our measurement an electron whose position and momenta are uncertain by Δx and Δpₓ such that Δx Δpₓ ≈ ℏ. [The symbols Δx and Δpₓ are not precisely the quantities defined in Eq. (4.2.7) but are of the same order of magnitude.] This is the famous uncertainty principle. There is no way around it. If we soften the blow of each photon by increasing λ, or narrow the objective to better constrain the final photon momentum, we lose in resolution. This would be the ideal position measurement. More elaborate schemes, which determine the recoil of the microscope, are equally futile. Note that if ℏ were 0, we could have Δx and Δpₓ simultaneously 0. Physically, it means that we can increase our position resolution without increasing the punch carried by the photons. Of course ℏ is not zero and we can't make it zero in any experiment. But what we can do is to use bigger and bigger objects for our experiment so that in the scale of these objects ℏ appears to be negligible. We then regain classical mechanics. The position of a billiard ball can be determined very well by shining light on it, but this light hardly affects its momentum. This is why one imagines in classical mechanics that momentum and position can be well defined simultaneously.

Generalization to More Degrees of Freedom

Our discussion so far has been restricted to a system with one degree of freedom—namely, a single particle in one dimension. We now extend our domain to a system with N degrees of freedom. The only modification is in postulate II, which now reads as follows.

Postulate II. Corresponding to the N Cartesian coordinates x₁, . . . , xN describing the classical system, there exist in quantum theory N mutually commuting operators X₁, . . . , XN. In the simultaneous eigenbasis |x₁, x₂, . . . , xN> of these operators, called the coordinate basis and normalized as <x₁', x₂', . . . , xN' | x₁, . . . , xN> = δ(x₁' – x₁) . . . δ(xN' – xN), we have the following correspondence: |v> ↔ ψ(x₁, . . . , xN)

Xᵢ |x₁, . . . , xN> = xᵢ |x₁, . . . , xN> Pᵢ |x₁, . . . , xN> = –iℏ (∂/∂xᵢ) |x₁, . . . , xN> Pᵢ being the momentum operator corresponding to the classical momentum pᵢ. Dependent dynamical variables ω(x, p) are represented by operators Ω = ω(X, P). The other postulates remain the same. For example, |ψ(x₁, . . . , xN)|² dx₁ . . . dxN is the probability that the particle coordinates lie between x₁, x₂, . . . , xN and x₁ + dx₁, x₂ + dx₂, . . . , xN + dxN.

This postulate is stated in terms of Cartesian coordinates since only in terms of these can one express the operator assignments in the simple form Xᵢ → xᵢ, Pᵢ → –iℏ ∂/∂xᵢ. Once the substitutions have been made and the desired equations obtained in the coordinate basis, one can perform any desired change of variable before solving them. Suppose, for example, that we want to find the eigenvalues and eigenvectors of the operator H, corresponding to the classical variable H = (p₁² + p₂² + p₃²)/2m + x₁² + x₂² + x₃² (4.2.24), where x₁, x₂, and x₃ are the three Cartesian coordinates and p, the corresponding momenta of a particle of mass m in three dimensions. Since the coordinates are usually called x, y, and z, let us follow this popular notation and rewrite Eq. (4.2.24) as H = (pₓ² + pᵧ² + p_z²)/2m + x² + y² + z² (4.2.25). To solve the equation H|ω> = ω|ω> with H = P²/2m + X² + Y² + Z², we make the substitution |ω> ↔ ψ(x, y, z) etc. and get [–ℏ²/(2m) (∂²/∂x² + ∂²/∂y² + ∂²/∂z²) + x² + y² + z²] ψ(x, y, z) = ω ψ(x, y, z) (4.2.26). Once we have obtained this differential equation, we can switch to any other set of coordinates. In the present case the spherical coordinates r, θ, and φ recommend themselves. Since ∂²/∂x² + ∂²/∂y² + ∂²/∂z² = (1/r²) ∂/∂r (r² ∂/∂r) + (1/r² sinθ) ∂/∂θ (sinθ ∂/∂θ) + (1/r² sin²θ) ∂²/∂φ², Eq. (4.2.26) becomes [–ℏ²/(2m) (1/r² ∂/∂r (r² ∂ψ/∂r) + 1/(r² sinθ) ∂/∂θ (sinθ ∂ψ/∂θ) + 1/(r² sin²θ) ∂²ψ/∂φ²) + r² ψ] = ω ψ. (4.2.27). What if we wanted to go directly from H in spherical coordinates H = (p_r²/2m) + (p_θ²/2mr²) + (p_φ²/2mr² sin²θ) + r² to Eq. (4.2.27)? It is clear upon inspection that there exists no simple rule [such as p_r → –iℏ ∂/∂r] for replacing the classical momenta by differential operators in r, θ, and φ, which generates Eq. (4.2.27) starting from the H above. There does exist a complicated procedure for quantizing in non-Cartesian coordinates, but we will not discuss it, since the recipe eventually reproduces what the Cartesian recipe (which seems to work) yields so readily. There are further generalizations, namely, to relativistic quantum mechanics and to quantum mechanics of systems in which particles are created and destroyed (so that the number of degrees of freedom changes!). Except for a brief discussion of these toward the end of the program, we will not address these matters.

4.3. The Schrödinger Equation (Dotting Your i's and Crossing Your h's)

Having discussed in some detail the state at a given time, we now turn our attention to postulate IV, which specifies the change of this state with time. According to this postulate, the state obeys the Schrödinger equation iℏ d/dt |v(t)> = H |v(t)> (4.3.1). Our discussion of this equation is divided into three sections: (1) Setting up the equation, (2) General approach to its solution, (3) Choosing a basis for solving the equation.

Setting Up the Schrödinger Equation

To set up the Schrödinger equation one must simply make the substitution H → H(x → X, p → P), where H is the classical Hamiltonian for the same problem. Thus, The Hamiltonian for a harmonic oscillator is classically described by: A° = P² / 2m + (1/2) m ω² x² The corresponding quantum Hamiltonian operator is: H = P² / 2m + (1/2) m ω² x² In three dimensions, the Hamiltonian operator for the quantum oscillator is similarly: H = (P_x² + P_y² + P_z²) / 2m + (1/2) m ω² (X² + Y² + Z²)

assuming the force constant is the same in all directions.

If the particle in one dimension is subject to a constant force f, then H = P² / 2m - f x

For a particle of charge q in an electromagnetic field in three dimensions, the classical Hamiltonian is: H = [p - (q/c) A(r, t)]² / 2m + q φ(r, t)

In constructing the corresponding quantum Hamiltonian operator, we must use the symmetrized form: H = [ (p - (q/c)A) · (p - (q/c)A) ] / 2m + q φ since p does not commute with A, which is a function of X, Y, and Z.

In this manner one can construct the Hamiltonian H for any problem with a classical counterpart. Problems involving spin have no classical counterparts and some improvisation is called for. We will discuss this question when we study spin in some detail in Chapter 14.

General Approach to the Solution Let us first assume that H has no explicit t dependence. In this case the equation i ħ ∂|ψ⟩/∂t = H |ψ⟩ is analogous to equations discussed in Chapter 1 describing the coupled masses and the vibrating string, respectively. Our approach will once again be to find the eigenvectors and eigenvalues of H and to construct the propagator U(t) in terms of these. Once we have U(t), we can write |ψ(t)⟩ = U(t) |ψ(0)⟩ There is no need to make assumptions about |ψ(0)⟩ here, since it is determined by Eq. (4.3.1): i ħ ∂|ψ(0)⟩/∂t = -H |ψ(0)⟩ In other words, Schrödinger's equation is first order in time, and the specification of |ψ⟩ at t = 0 is sufficient initial-value datum.

Let us now construct an explicit expression for U(t) in terms of |E⟩, the normalized eigenkets of H with eigenvalues E which obey H |E⟩ = E |E⟩ This is called the time independent Schrödinger equation. Assume that we have solved it and found the kets |E⟩. If we expand |ψ(t)⟩ as |ψ(t)⟩ = Σ_E |E⟩ ⟨E|ψ(t)⟩ = Σ_E a_E(t) |E⟩ the equation for a_E(t) follows if we act on both sides with (i ħ ∂/∂t - H): 0 = (i ħ ∂/∂t - H) |ψ(t)⟩ = Σ_E (i ħ ∂a_E/∂t - E a_E) |E⟩ i ħ ∂a_E/∂t = E a_E where we have used the linear independence of the kets |E⟩. The solution to this equation is a_E(t) = a_E(0) e^{-iEt/ħ} or ⟨E|ψ(t)⟩ = ⟨E|ψ(0)⟩ e^{-iEt/ħ} so that |ψ(t)⟩ = Σ_E |E⟩ ⟨E|ψ(0)⟩ e^{-iEt/ħ} We can now extract U(t): U(t) = Σ_E |E⟩ ⟨E| e^{-iEt/ħ}

We have been assuming that the energy spectrum is discrete and nondegenerate. If E is degenerate, one must first introduce an extra label α (usually the eigenvalue of a compatible observable) to specify the states. In this case U(t) = Σ_{E,α} |E,α⟩ ⟨E,α| e^{-iEt/ħ} If E is continuous, the sum must be replaced by an integral.

The normal modes |ψ_E(t)⟩ = |E⟩ e^{-iEt/ħ} are also called stationary states for the following reason: the probability distribution P(ω) for any variable Ω is time-independent in such a state: P(ω, t) = |⟨ω|ψ(t)⟩|² = |⟨ω|E⟩|² e^{-iEt} e^{iEt} = |⟨ω|E⟩|² = P(ω, 0)

There exists another expression for U(t) besides the sum, Eq. (4.3.13), and that is U(t) = e^{-iHt/ħ} If this exponential series converges (and it sometimes does not), this form of U(t) can be very useful. (Convince yourself that |ψ(t)⟩ = e^{-iHt/ħ} |ψ(0)⟩ satisfies Schrödinger's equation.)

Since H (the energy operator) is Hermitian, it follows that U(t) is unitary. We may therefore think of the time evolution of a ket |ψ(t)⟩ as a "rotation" in Hilbert space. One immediate consequence is that the norm ⟨ψ(t)|ψ(t)⟩ is invariant: ⟨ψ(t)|ψ(t)⟩ = ⟨ψ(0)|U^†(t) U(t) |ψ(0)⟩ = ⟨ψ(0)|ψ(0)⟩ so that a state, once normalized, stays normalized. There are other consequences of the fact that the time evolution may be viewed as a rotation. For example, one can abandon the fixed basis we have been using, and adopt one that also rotates at the same rate as the state vectors. In such a basis the vectors would appear frozen, but the operators, which were constant matrices in the fixed basis, would now appear to be time dependent. Any physical entity, such as a matrix element, would, however, come out the same as before since ⟨φ|ψ⟩, which is the dot product of ⟨φ| and |ψ⟩, is invariant under rotations. This view of quantum mechanics is called the Heisenberg picture, while the one we have been using is called the Schrödinger picture. Infinitely many pictures are possible, each labeled by how the basis is rotating. So if you think you were born too late to make a contribution to quantum theory fear not, for you can invent your own picture. We will take up the study of various pictures in Chapter 18.

Let us now consider the case H = H(t). We no longer look for normal modes, since the operator in question is changing with time. There exists no fixed strategy for solving such problems. In the course of our study we will encounter a time-dependent problem involving spin which can be solved exactly. We will also study a systematic approximation scheme for solving problems with H(t) = H⁰ + H'(t) where H⁰ is a large time-independent piece and H'(t) is a small time-dependent piece.

What is the propagator U(t) in the time-dependent case? In other words, how is U(t) in |ψ(t)⟩ = U(t) |ψ(0)⟩ related to H(t)? To find out, we divide the interval (0—t) into N pieces of width Δ = t/N, where N is very large and Δ is very small. By integrating the Schrödinger equation over the first interval, we can write to first order in Δ: |ψ(Δ)⟩ = |ψ(0)⟩ - (i/ħ) H(0) Δ |ψ(0)⟩ = [1 - (i/ħ) H(0) Δ] |ψ(0)⟩ which, to this order, = exp[ - (i/ħ) H(0) Δ ] |ψ(0)⟩ [One may wonder whether in the interval 0—Δ, one must use H(0) or H(Δ) or H(Δ/2) and so on. The difference between these possibilities is of order Δ and hence irrelevant, since there is already one power of Δ in front of H.] Inching forth in steps of Δ, we get |ψ(t)⟩ ≈ Π_{n=0}^{N-1} [1 - (i/ħ) H(nΔ) Δ] |ψ(0)⟩ We cannot simply add the exponents to get, in the N→∞ limit, U(t) = exp[ - (i/ħ) ∫_0^t H(t') dt' ]

since [H(t₁), H(t₂)] ≠ 0 in general. For example, if H(t) = X² cos² ωt + P² sin² ωt then H(0) = X² and H(π/2ω) = P², and [H(0), H(π/2ω)] ≠ 0.

It is common to use the symbol, called the time ordered integral: T{ exp[ - (i/ħ) ∫_0^t H(t') dt' ] } = lim_{N→∞} Π_{n=0}^{N-1} exp[ - (i/ħ) H(nΔ) Δ ]

in such problems. We will not make much use of this form of U(t). But notice that being a product of unitary operators, U(t) is unitary, and time evolution continues to be a "rotation" whether or not H is time independent.

Whether or not H depends on time, the propagator satisfies the following conditions: U(t₃, t₂) U(t₂, t₁) = U(t₃, t₁)

U^{-1}(t₂, t₁) = U(t₁, t₂)

It is intuitively clear that these equations are correct. You can easily prove them by applying the U's to some arbitrary state and using the fact that U is unitary and U(t, t) = I.

Choosing a Basis for Solving Schrödinger's Equation Barring a few exceptions, the Schrödinger equation is always solved in a particular basis. Although all bases are equal mathematically, some are more equal than others. First of all, since H = H(X, P) the X and P basis recommend themselves, for in going to one of them the corresponding operator is rendered diagonal. Thus one can go to the X basis in which X → x and P → -iħ d/dx or to the P basis in which P → p and X → iħ d/dp. The choice between the two depends on the Hamiltonian. Assuming it is of the form (in one dimension)

H = T + V = P² / 2m + V(X)

the choice is dictated by V(X). Since V(X) is usually a more complicated function of X than T is of P, one prefers the X basis. Thus if H = P² / 2m + 1 / (2 cosh² x)

the equation H |E⟩ = E |E⟩ becomes in the X basis the second-order equation [ -ħ²/(2m) d²/dx² + 1/(2 cosh² x) ] ψ_E(x) = E ψ_E(x)

which can be solved. Had one gone to the P basis, one would have ended up with the equation [ p²/(2m) + 1 / (2 cosh² (iħ d/dp)) ] ψ_E(p) = E ψ_E(p)

which is quite frightening.

A problem where the P basis is preferred is that of a particle in a constant force field f, for which H = P² / 2m - f x In the P basis one gets a first-order differential equation [ iħ f d/dp + p²/(2m) ] ψ_E(p) = E ψ_E(p)

whereas in the X basis one gets the second-order equation [ -ħ²/(2m) d²/dx² - f x ] ψ_E(x) = E ψ_E(x)

The harmonic oscillator can be solved with equal ease in either basis since H is quadratic in X and P. It turns out to be preferable to solve it in a third basis in which neither X nor P is diagonal! You must wait till Chapter 7 before you see how this happens.

There exists a built-in bias in favor of the X basis. This has to do with the fact that the x space is the space we live in. In other words, when we speak of the probability of obtaining a value between x and x + dx if the variable X is measured, we mean simply the probability of finding the particle between x and x + dx in our space. One may thus visualize ψ(x) as a function in our space, whose modulus squared gives the probability density for finding a particle near x. Such a picture is useful in thinking about the double-slit experiment or the electronic states in a hydrogen atom.

But like all pictures, it has its limits. First of all it must be borne in mind that even though ψ(x) can be visualized as a wave in our space, it is not a real wave, like the electromagnetic wave, which carries energy, momentum, etc. To understand this point, consider a particle

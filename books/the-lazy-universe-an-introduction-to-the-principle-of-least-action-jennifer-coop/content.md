# The Lazy Universe An Introduction to the Principle of Least Action Jennifer Coopersmith Z Library

From the archives of the Dublin Institute for Advanced Studies

THE LAZY UNIVERSE An Introduction to the Principle of Least Action by Jennifer Coopersmith

Great Clarendon Street, Oxford, OX2 6DP, United Kingdom

Oxford University Press is a department of the University of Oxford.

It furthers the University’s objective of excellence in research, scholarship, and education by publishing worldwide. Oxford is a registered trademark of Oxford University Press in the UK and in certain other countries

The moral rights of the author have been asserted

First Edition published in 2017

Impression: 1

a retrieval system, or transmitted, in any form or by any means, without the prior permission in writing of Oxford University Press, or as expressly permitted by law, by licence or under terms agreed with the appropriate reprographics rights organisation. Enquiries concerning reproduction outside the scope of the above should be sent to the Rights Department, Oxford University Press, at the address above

You must not circulate this work in any other form and you must impose this same condition on any acquirer

Published in the United States of America by Oxford University Press 198 Madison Avenue, New York, NY 10016, United States of America

British Library Cataloguing in Publication Data Data available

Library of Congress Control Number: 2016953473

Printed and bound by CPI Group (UK) Ltd, Croydon, CR0 4YY

Links to third party websites are provided by Oxford in good faith and for information only. Oxford disclaims any responsibility for the materials contained in any third party website referenced in this work.

To Cornelius Lanczos (1893–1974)

and Murray John Peake (1952–)

“There’s husbandry in heaven” ACT II, SCENE I MACBETH SHAKESPEARE

Preface

The mathematician and physicist, Cornelius Lanczos (1893–1974), wrote one of the best books of physics explanation that has ever been written: The Variational Principles of Mechanics.¹ It explains the true meaning and philosophical content of the Principle of Least Action. The present book is a shorter and simplified version of that classic - but it is an original interpretation (anything taken directly from Lanczos is attributed and referenced by page number); it is also a paean to Lanczos.

Who is the book for? It is for you! It concerns a principle that underpins the whole of physics, so how could it not be important to understand even a tiny bit of it? The greatest theories have one common feature - they always bring in wisdom far-surpassing their original remit, extending into almost every walk of life. Therefore, one should not limit one’s area of study but rather follow the maxim: “The more you know, the more you can know; the more you understand, the more you can understand.”² Moreover, as well as an increased understanding of the world, you will be privy to a rarer reward - to “theories of excessive beauty”.³

It is true that the reader is assumed to have a background in the physical sciences, however a layreader could also read this book, with profit and enjoyment, by skim-reading the mathematics, or by reading just the Introduction (Chapter 1), the Final Words (Chapter 9), and the historical and popular chapters (2 and 8). Furthermore, the book is not a textbook: there are many equations, but the aim is to explain - why these equations and not others, and what do the equations mean?⁴

The appendices are usually at a more advanced level and condensed in style, but they may be entirely passed over without loss of continuity in the main text. Apart from the invaluable asset of seeing how a problem is solved, the reason for so many appendices is twofold: to provide a ¹ Lanczos C, The Variational Principles of Mechanics, University of Toronto Press (1949). All page numbers will refer to the fourth edition, Dover Publications, Inc. New York (1970), and we shall write ‘Lanczos, page x’.

² (author’s maxim)

³ Lanczos, page 229.

⁴ This is in contrast to the approach in Synge and Griffith, Principles of Mechanics, 3rd edition, McGraw-Hill Book Company, Inc (1959), page 413, where the advice is: “Do not attempt to see a physical meaning in these [mathematical] operations; it will not help.”

viii Preface

compact resource for the physicist (for example, a physicist on a beach holiday); and for the layreader to know what subject-headings to follow up at a later stage, if so desired. Enrichment material has been included but often as optional reading (in small font), or in parentheses, or footnotes. Also, we have avoided detailing all the qualifications, exemptions, and special cases, in order to be able to say things simply, and make bold statements.

Terminology: on the authority of both Lanczos, and Richard Feynman,⁵ we refer to all the appropriate principles - Hamilton’s Principle, Jacobi’s Principle, Lagrange’s Principle, and Maupertuis’s Principle - as Principles of Least Action, as they are generically so.

‘Variational Mechanics’ means any physics problem that uses the Principle of Least Action. Also, the fact that we usually say ‘least’ as opposed to ‘stationary’ is explained in the main text - see Section 6.6.

The University of La Trobe is thanked for granting me an honorary research associateship, and for the use of library and computing facilities. It was Joe Petrolito, Emeritus Professor of Engineering at La Trobe, Bendigo campus, who introduced me to the website of Edwin F Taylor, Senior Research Scientist Emeritus at the Massachusetts Institute of Technology (MIT). This led to a short but rewarding email correspondence.

At OUP, I thank Sönke Adlung and Ania Wronski. The use of LaTeX, Ubuntu, Gimp, Wikipedia, Google, Metapost, Scilab, and Mfpic are gratefully acknowledged. Mal Haysom and Deborah Peake are thanked for their help with the diagrams (Deborah drew the maze, the encumbered porcupine and Stevin’s ‘Wreath of Spheres’). George Rogers, librarian at DIAS, once again anticipated my needs and supplied superb images of Lanczos and of Hamilton, with no fuss. Most of all, I am grateful to Gerald Sussman, Panasonic Professor of Electrical Engineering at MIT, who undertook a critical reading of the book prior to printing.

The errors he identified have been corrected. Finally, I thank Murray Peake for helpful discussions on maths and physics, and for leading me to Lanczos in the first place.

If I have inspired any reader to seek out the work of the master, Cornelius Lanczos, then it will be ‘mission accomplished’.

⁵ Feynman RP, Feynman’s Lectures on Physics, Volume II, Chapter 19.

Contents

List of Figures xi 1 Introduction 1 2 Antecedents 12 3 Mathematics and physics preliminaries: of hills and plains and other things 31 4 The Principle of Virtual Work 59 5 D’Alembert’s Principle 88 6 Lagrangian Mechanics 107 7 Hamiltonian Mechanics 143 8 The whole of physics 183 9 Final words 192 A1.1 Newton’s Laws of Motion 197 A2.1 Portraits of the physicists 198 A3.1 Reversible displacements 201 A6.1 Worked examples in Lagrangian Mechanics 202 A6.2 Proof that T is a function of v² 217 A6.3 Energy conservation and the homogeneity of time 222 A6.4 The method of Lagrange Multipliers 225 A6.5 Generalized Forces 228 A7.1 Hamilton’s Transformation, examples 230 A7.2 Demonstration that the p’s are independent coordinates 232 A7.3 Worked examples in Hamiltonian Mechanics 233 A7.4 Incompressibility of the phase fluid 237 A7.5 Energy conservation in extended phase space 238 A7.6 Link between the action, S, and the ‘circulation’ 241 x Contents A7.7 Transformation equations linking p and q via S 243 A7.8 Infinitesimal canonical transformations 244 A7.9 Perpendicularity of wavefronts and rays 248 A7.10 Problems solved using the Hamilton-Jacobi Equation 250 A7.11 Quasi refractive index in mechanics 255 A7.12 Einstein’s link between Action and the de Broglie waves 256

List of Figures

## 1.1 The suitors’ puzzle

## 2.1 Weights, connected by a cord, on inclined planes

## 2.2 ‘Wreath of spheres’ draped over inclined planes (after Stevin)

## 2.3 Huygens’s canal-boat thought experiment

## 2.4 Brachystochrone, curve of ‘swiftest descent’. (schematic)

## 3.1 “Anamorphic Column” by Istvan Orosz

## 3.2 The path of a cannonball. (schematic)

## 3.3 Is the ladder stable?

## 3.4 The function, f(x), and some variations, fvar(x)

## 3.5 The distinction between df and δ

## 4.1 Weighted bar supported at one end

## 4.2 The ‘black box’

## 4.3 Knob and slider

## 4.4 Stability of a ladder

## 4.5 Two springs connected to a mass

## 4.6 Spring loaded with a weight

## 4.7 Soap bubble

## 5.1 Connected masses, ‘Half-Atwood’ and ‘Black Box’

## 5.2 ‘Fictitious Forces’, examples

## 5.3 Newton’s Bucket

## 7.1 Nicolas Poussin, A Dance to the Music of Time

## 7.2 An oscillating spring

## 7.3 Simple pendulum

## 7.4 Spinning top

## 7.5 Wavefront of common action in configuration space

## 7.6 Huygens’s wavelets

## 7.7 Construction of the next wavefront

A3.1 Washing-line seen through a window. 201 A6.1.1 Plane polar coordinates. 203 A6.1.2 Atwood’s Machine. 205 A6.1.3 The ‘Half-Atwood’ Machine. 206 A6.1.4 Mass attached to a spring. 207 A6.1.5 Spherical pendulum. 210 A6.1.6 Projectile motion. 211 A6.1.7 Electrical and mechanical systems compared. 214 xii List of Figures A6.1.8 One block sliding on another block. 215 A7.1 Coordinates for the spherical pendulum. 231

Introduction

It would be wonderful if there was one principle, simple to state, that could account for every process in the physical universe. But there is such a principle, a surprisingly well-kept secret, that accounts for almost every physical process. It is a principle that is more powerful than Newton’s ‘F = ma’, and a principle that doesn’t have energy conservation as a requirement in every scenario. We know that Newtonian Mechanics must be replaced when speeds are very high, or the masses are tiny, or huge - but this ‘new’ principle still applies in these extreme regimes. How can one principle explain so much? The clue comes from the deep wisdom of the eighteenth-century French philosophe, Jean le Rond d’Alembert:¹

“L’univers, pour qui saurait l’embrasser d’un seul point de vue, ne serait, s’il est permis de le dire, qu’un fait unique et une grande vérité.”

(“If one could grasp the whole Universe from one viewpoint, it would appear, if it is permitted to say this, as a unique fact and a great truth.”)

No one knows whether d’Alembert’s beautiful claim is correct but one thing is certain, if we cannot find one universal viewpoint then we will not arrive at one universal truth. For our viewpoint to be universal it is not a question of us all looking at the view from the same hilltop, rather, it is a requirement that all viewpoints are equivalent, and that there is just one universal rule or law or algorithm that solves the problem. Our new principle achieves this - but it seems incredible that one simple ‘algorithm’ could cope with all the specificity, variety, and complexity across the whole of p Physics. To make this plausible, we consider the following fable.

1 D’Alembert, JleR, Discours préliminaire de l’encyclopédie, 1751.

Figure 1.1 The suitors’ puzzle.

There once was a King and he set a fiendish puzzle for prospective suitors who wanted to marry his daughter, the beautiful princess. The King had constructed a maze and the successful suitor had to provide the princess with instructions for collecting treasure from a casket. The young suitors had a few hours to look at a map of the maze and prepare their instructions. The King then looked at their answers and quickly whittled away the number of competitors to just two. These two suitors, Alfredo and Bruno, had very different approaches to the puzzle. Alfredo provided detailed instructions for every route, advising the princess to sight the tall column, visible from a distance over the hedges, to let her nose guide her to the fragrance of the frangipani tree, and also to listen out for the sound of bells chiming in the bell-tower, and water splashing at the fountain. Bruno came forward with just a tiny scrap of paper on which it said, “Wherever you may find yourself, turn left at the next intersection. Eventually you will reach the casket.” (The King had assured the contestants that there were no disconnected ‘islands’ within the maze.)

The King, a veritable sage, awarded the hand of his daughter in marriage to this second suitor. The amazing thing about this suitor’s instructions is that they are very simple to state and they are universal - they apply to any maze (although the maze must satisfy certain geometrical restrictions, for example, it cannot contain disconnected islands). There is also another curious attribute of Bruno’s algorithm - it is local. The princess need only ever look as far ahead as the very next step (while always keeping an eye open for the casket). Although Alfredo’s instructions may be broken down into steps the method is not local in the true sense (there are references to distant features - the sound of the fountain, the smell of the frangipani, the sight and sound of the bells in the bell-tower).

This is only a story but it demonstrates some essential points. In our new principle the method is truly local, and this is never the case for Newtonian Mechanics, even when a path may be broken down into lots of tiny incremental steps. But most astounding of all we shall find that the ensuing equations are invariant, taking exactly the same form, no matter what the scenario or what coordinates are used. It is not even necessary that the setting is time-independent, or that the components are passive (so the maze could writhe and undulate with time, and the princess could affect the maze, say, by trimming the hedges as she passed by). The reason for this invariance is that we have at last found something absolute: it is not a universal timepiece, yardstick, or reference frame, for there are none, it is a principle, and one that applies across almost every area of physics. We introduce it by way of a brief historical aside.

One of the most awe-inspiring developments in physics has been the shift from Newton’s to Einstein’s view of gravity. In Newton’s Theory of Universal Gravitation, gravity is a force acting between bodies, however near or far. In Einstein’s Theory of Gravitation (the Theory of General Relativity), the force is completely dispensed with. It is replaced by a patchwork of reference frames, sufficiently small, but seamlessly joined together, and, instead of responding to a force, the orbiting body now responds to geometry - the ‘curvature’ of ‘space’. This is often represented heuristically by the image of, say, the Earth resting on a large two-dimensional surface, such as a trampoline, distorting this surface, and thereby affecting the trajectory of nearby small bodies, such as the Moon. These two theories - Newton’s and Einstein’s - are utterly different, and yet, amazingly, the experimental differences, for example, the predictions of the Moon’s orbit, are practically nil. It turns out that Einstein’s approach involves much more complicated calculations and, as we have just stated, barely any practical advantage - so why use it? The answer is that it has deeper explanatory power, it is applicable over a much greater range of problems, and it is philosophically more sound.

We have been talking just of gravitation, but the principle that we introduce explains not only gravitation but all kinds of problems in the physical sciences (statics and dynamics, optics, electricity and magnetism, quantum mechanics, physical chemistry, statistical mechanics, astronomy, materials science, hydrodynamics, quantum electrodynamics (QED), and so on); it also has deeper explanatory power, is applicable over a much greater range of problems, and is philosophically more sound. This principle is the Principle of Stationary Action (the PSA). It can be stated as:

The Principle of Stationary Action The physical system seeks out the ‘flattest’ region of ‘space’.

This is equivalent to choosing the ‘straightest’ possible path, which (usually) translates as the path of least ‘distance’. One more thing, whether considering the ‘flatness of space’ or the ‘straightness of paths’, or the ‘least distance’, only the ‘space’ nearby - that is to say, locally - needs to be inspected.

The subtitle of this book is the Principle of Least Action (PLA), but the principle just given is the Principle of Stationary Action (PSA)? ‘Stationary’ is a mathematical term meaning ‘at a flat point of ‘space’’ but whether that flat point implies a least path requires a further investigation - therefore the PSA is the more general principle, and incorporates the PLA. However, we shall find that the more stringent condition, the PLA, is the one we need, and later on we’ll switch to calling our principle: the Principle of Least Action. We’ll explain this in a later chapter (Section 6.6, Chapter 6).

Einstein’s Theory of Special Relativity, that preceded his theory of General Relativity, starts with two postulates: 1) the laws of physics take the same form in every reference frame, 2) the speed of light in a vacuum is a constant. These two postulates are strikingly different: the first postulate (the Principle of Relativity) is philosophical in character - Einstein coached us into realizing that physics just couldn’t be practised unless postulate 1) applied. On the other hand, postulate 2) appears to be empirical - the speed of light is constant, yes, but perhaps, in another Universe, it might have been variable? Similarly, in the case of the Principle of Stationary Action, the Principle has two postulates of very different natures. The first postulate, 1), we have already described - that the system ‘space’ is as ‘flat’ as possible, locally. This appears reasonable but rather abstract and philosophical; it sounds more like geometry than physics, and we need to know - ‘flat’ with respect to what? This is where the second postulate comes in, the one that contains the physical input. Postulate 2) states that what is actually being flattened is a certain specific physical quantity - ‘action’. This quantity has dimensions of energy × time, or linear momentum × distance, or angular momentum × angle, and so on. In one of its first incarnations, ‘action’ was given as ‘m v ds’, where m is the mass of a ‘free’ particle, v is its speed, and ds is a small distance along the particle’s path. As we have to do with a postulate, we cannot justify the choice by deduction from even more elemental principles. Nevertheless, ‘action’ does seem like a worthy candidate for a telling physical quantity - it is a scalar (a pure magnitude, having no direction - therefore more likely to be an invariant), it ‘spans the physical space’ (nothing crucial is missed out), and it does so in the simplest way possible (mvds is postulated rather than, say, m²v³d⁴s/dt⁴).

D’Alembert’s “one viewpoint” implies objectivity, and this is difficult to arrive at in everyday life where prejudice abounds. For example: we barely notice the reaction-force against the soles of our feet, or on our bottoms, that is present almost every minute of our lives (Einstein teaches us that we are thereby not in ‘free-fall’, and so do not serve as a ‘natural’ frame of reference); on the other hand, in the rapidly rotating ‘gravitron’ at the funfair, we feel pinned as if by a great weight but have no sensation of our spinning motion (we merely notice that we can barely nod or move our arms). When revisiting a park that we knew as a child, we find that it resembles a pocket handkerchief rather than a vast estate - is the slight increase in the height of our eyes the source of this change? No, it arises because we have undergone an enormous (non-local) translation in time, during which our brain has totally altered. We watch the waters sloshing about in a neighbour’s swimming pool - perhaps they have installed a wave-generating machine? Upon closer inspection we find no machine, but realize that ‘a giant hand’ - an Earth tremor - is gently rocking the pool: therefore our initial assumption of an isolated system, defined by the edges of the pool, is wrong.

What helps us to achieve objectivity in physics (as opposed to everyday life) is the fact that we are bound by the strictures of mathematical tests. The PSA is centred on a mathematical test - a ‘test of the flatness of ‘space’’ - which is remarkable for its ability to winnow away the distracting observer-dependent features and so arrive at the true invariant laws. It succeeds in this because it involves an ‘extremal’ feature of the mathematical landscape (something like ‘shortest route between Peshawar and Kabul’), and these features are unique in that they don’t depend upon the type of map or even the units used (the route is shortest whether we use a Mercator’s or a Peter’s projection, and whether we measure in feet or in metres). Before the test can be applied, we have to define what we mean by ‘space’. We follow the historical development, and return to our discussion of Newton.

You most likely know Newton’s Laws of Motion³ but we want now to give a different perspective of them, emphasizing the philosophical assumptions. An implicit premise of Newton’s Mechanics was the outstanding advance: ‘space’ and ‘physics’ are totally separate from each other. ‘Physics’ means forces, masses, and masses in motion. ‘Space’, following Descartes’ invention of the coordinate system, means the three everyday space dimensions (commonly designated x, y, and z), and the time, t. All of x, y, z, and t are assumed independent of each other, and each goes on to infinity. Gone are the sixteenth centu ry’s tendencies, empathies, abhorrences, and vortices; and Newton’s ‘space’ is empty, not full like Descartes’. (It is a void, which Newton does not abhor.) Next after ‘space’ come particles - bodies with no internal structure but having an intrinsic property, mass. By Law (Newton’s First), each ‘free’ particle is either at rest, or moves at constant speed and in a constant direction. Finally, forces, F, are introduced, such as an attractive force between one particle and another. A force has one effect and one effect only - it causes a particle to accelerate. This is where mass plays its role, it determines how big the acceleration shall be, for a given force. (Apart from this, mass is inert - it doesn’t depend on when or where the particle is, or on its state of motion.) All this is asserted in the Second Law, F = ma. (But it could all have been so much more complicated; the force could have left the motion unchanged but caused the mass to swell, or it could have caused an acceleration not in line with F, or caused a third-order change in the position, and so on.)

Influence of each particle considered on its own. (Again, it could have been more complicated, the force might have been cast anew for, say, each trio of particles.) Thus was born the idea of the ‘rigid body’, an extended body made up from separate particles, but which could itself be treated as if it were one single particle, with all its mass concentrated at one point. 325 years on from Newton’s ‘Principia’ it is hard to remain sufficiently impressed. As the philosopher, Schopenhauer, said, a theory passes from being rejected as ridiculous to being accepted but taken to be obvious. (There is then the third phase, when the theory is again rejected.) Consider Newton’s use of ‘acceleration’. It was already known, from Galileo’s Principle of Relativity, that uniform motion is relative to the observer. Newton turned this around: all non-uniform, that is to say, accelerated, motion is not relative to the observer, it can be known absolutely. Acceleration with respect to what? Answer, with respect to ‘space’. But as the accelerations are absolute, then Newton’s ‘space’ is absolute. So we have arrived back at Newton’s wonderful abstraction, an infinite ‘space’, an inert and absolute background to physical happenings.

With the PSA, every tenet of Newton’s Mechanics is challenged: the absolutes of Newton are avoided as every measure - whether it be a position, a speed, a direction, a time, and so on - is always defined with reference to something within the given system; action-at-a-distance does not occur - a global picture is built up, piece by piece, but by antennae which are sensitive only to conditions locally; the axes of ‘space’ no longer extend to infinity, are not necessarily independent of each other, and not necessarily independent of the masses within; and Newton’s modular approach, building up complexity from more and more complicated arrangements of particles, each taken singly, is replaced by a holistic ‘systems’ approach. Let’s explain this ‘systems’ approach by analogy. Bertrand Russell (philosopher and mathematician) quipped that the activities of mankind amounted to the redistribution of matter within 0.2% of the Earth, at its surface (this was before the era of space travel). To check Russell’s claim, we could exhaustively track the motion of every single person, throughout recorded history, and note what masses they were carrying and where they deposited them; or, we could estimate the matter-content of cities built, crops grown, monuments constructed, bodies buried, and so on. In the second, ‘systems’, approach, we have lost the simplicity of basic elements (a person, their movements, what they are carrying) and instead have more abstract concepts relating to the whole system (cities, roads, pyramids, etc.). Some totally new possibilities arise (‘the deceased’) that were not catered for (!) in the first approach. We end up with a static tally of the mass distribution. Another, more dynamic, example is given by the description of a football match. In the modular description we have only ‘players’ and ‘a football’; in the other approach, the ‘systems-view’, we have ‘defence-position’, ‘attack’, ‘tackling’, ‘dribbling the ball’, ‘goal-kick’, and so on. One counter-intuitive aspect of this systems-view is that we appear to have lost that quintessential feature of motion - its directionality. However, we soon realize that it is not lost but embedded in the whole-system structures (for example, ‘goal-kick’ has no absolute direction (say, 30 West) yet it conveys all the directional information required, and makes reference only to features within the system - the goalposts).

Returning now to the PSA, the method is as follows: (i) Instead of particles we have individual components of the system. These are chosen in a system-specific way. (They can be billiard balls, atoms, planets, lever arm, pendulum, capacitor, and so on, as the given problem demands); (ii) Instead of forces there are ‘scalar structure functions’, what in a previous life we have called the energy functions (the kinetic energy, and the potential energy); (iii) we identify all the independent ‘motions’ that the system can undergo. These ‘motions’ are the physical changes that happen naturally and that characterize the given system - what in a later life we shall call the ‘degrees of freedom’. (For example, the planet orbits, the lever arm rotates, swings swing, and roundabouts turn.) (iv) We come finally to the application of a principle, a principle that requires an exploration of the ‘space’ in which the physical problem occurs. Knowing all the ‘motions’, we then choose an alternative set of ‘motions’ that could occur. These motions are hypothetical - we have hypothesized them - however we are not free to hypothesize anything we like: the ‘motions’ must all be in the same given ‘space’ (each system has its own ‘system-space’), occur in the given time-window, and they must be ‘nearby’. Now these ‘motions’ imply certain amounts of kinetic energy and potential energy consumed or generated in the given time. From these energies we compute a certain quantity - the total action - used up in the given time. In short, we determine the total hypothetical action for this choice of hypothetical motions. We then continue the exploration and consider another choice of hypothetical motions and again determine the consequential hypothetical action. And so on. The principle then asserts that of all choices for hypothetical motions, the actual motions are those which make the change-in-action-between-choices come out to zero. More evocatively, the system finely adjusts itself, via the actual motions (acting in concert but instant by instant taking their marching orders from the scalar structure functions) in just such a way that the action used is least. That these subtly different versions - the italicized one and the evocative one - are the same will emerge during the course of this book.

Be reassured: these ideas are new and many and abstract; there is no way they can be understood in one go. It is useful to collect them together in one place, but not possible to convey all the nuances in a single paragraph. For example, we shall later on discover that sometimes the ‘space’ exploration is made explicitly by us (in the method known as the Principle of Virtual Work) and sometimes the mathematics takes care of it (in the Variational or Lagrangian Mechanics). Also, there is sometimes an elision made between the ‘motions’ as ‘degrees of freedom’ and the ‘motions’ as hypothetical ‘variations’. Did we write ‘hypothetical’? Yes, this is the piece de resistance: the ‘system-space’ is a virtual abstract space, and this is what finally enables us to achieve the required objectivity (the actual physical space could have this, that, or the other observer-bias, whereas the virtual abstract space is neutral).

Here is a summary of the main virtues of the PSA. (i) It does the job. (ii) As forces play no part in the method then ‘forces-of-constraint’ also play no part. Incredible but true. (iii) Better understanding of physics. We can now have ‘cat’ and ‘mouse’ instead of only ‘particles’ and ‘particle-particle interactions’. But a ‘cat’ is more than the sum of its ‘particles’. (iv) No hard and fast distinction between ‘active’ and ‘passive’ components. (Just as a river carves out the river-bed, and the river-bed determines the path of the river, so the ‘curvature of space’ affects the paths of bodies, and moving bodies affect the ‘curvature of space’.) (v) Philosophically superior: local (and this is all we ever detect experimentally); no pre-existing empty ‘space’ (just take the world as it is and then examine it); the system is what’s important. (vi) Global View. Even when ‘space’ is flat locally, ‘curvature’ can still arise globally - by patching together smaller regions with the requirement that there is no ‘puckering at the seams’. (vii) The PSA gives prominence to energy and to the whole system. Kinetic energy is shown to be a more fundamental and primitive concept than force. Also the dichotomy between kinetic energy and potential energy is explained. (viii) The PSA reveals a deep connection between symmetry and conserved properties. (Newton’s Mechanics does not lead naturally to any conservation laws except for one, the conservation of linear momentum.) (ix) In Newtonian Mechanics no attempt is given to show how robust the solution is (how it changes following small changes in the starting conditions) or to give ball-park estimates. The PSA, via Hamilton’s Mechanics, does address these questions. (x) Amazing unity of approach across almost the whole of physics. (Almost? The exceptions will be discussed in due course.)

Apart from the fact that the PSA is the keystone of physics, and therefore an indispensable tool for the professional engineer or physical scientist, there are two other reasons why we would like to awaken an appreciation of it, even a non-mathematical appreciation. The first is a pragmatic reason. We all know, roughly speaking, what space, time, mechanics, quantum mechanics, matter, and energy are about. These ideas have passed into the public domain. It would be inefficient to start from scratch in our science classes, and not even incorporate advances made during the seventeenth and eighteenth centuries. Somehow the PSA has got missed out - it is time to correct this. The second reason is aesthetic. The beauty of phy physics does not reside only in the beauty of the night sky, a rainbow, or a sunset. It resides even more in the interior logic, the principles which reach across vast areas of the physical world, unifying them into a self-consistent whole, and with the most economical set of starting premises. (One could call it the ‘Aha’ feeling.)

Alice (from Lewis Carroll’s Alice’s Adventures in Wonderland) tried so hard to get through the door in order to see the exquisitely beautiful garden beyond. Consider this garden as a metaphor for physics: it’s true that without mathematics we shall never be able to wander freely around this garden, but it would be wonderful indeed if we could just be lifted up to peer at it through the keyhole.

Antecedents

A new principle rarely arises completely out of the blue, there are usually vague presentiments in the air. Some precursors to the Principle of Least Action are described (we don’t attempt to give an exhaustive history).

Simon Stevin (1548–1620)

Stevin (Stevinus) was a ‘geometer’ from Bruges in Flanders. The discovery of which he was most proud concerns the condition for static equilibrium of weights on inclined planes (see Figure 2.1):

What relation must hold between the masses and the lengths of the triangle in order for the system to be in equilibrium? Our first guess might be to ‘resolve the forces’ into components, then balance the horizontal components to zero, and, finally, equate the vertical components to the weights. Stevin, in Antwerp in 1588, attacked the problem in a different way – (he was working 200 years before vectors, and 99 years before Newton’s forces).

The first remarkable thing Stevin did was to bring (hypothetical) motion into this static set-up. He recast the problem and imagined a chain of spherical masses that could circulate around the triangle, with the lower part of the chain hanging freely. Stevin idealized this arrangement: the chain could move in either direction, without friction, and would never get stuck on the pointy bits (imagine a little frictionless pulley at the apex of the triangle). Also, the mass had to be uniformly distributed along the chain – think of a bead chain like the ones used today to open and close Venetian blinds. Stevin argued that if the section of chain from A to X pulls more than the section from X to B then the chain will over-balance to the left. It will circulate anticlockwise (excuse the anachronism) until the original portion AX then occupies the arc Y to A. The entire length of chain that hangs freely below the little table, between A and B, can be ignored – by symmetry it is always in balance with itself. However, the replacement section of chain now lying along AX will again over-balance that new section now lying along XB. In other words, the new state, after circulation, is identical to the initial state. But this will always be true (the new state, after circulation, will always be identical to the initial state), and so the chain will always over-balance, and will keep circulating forever.

But a continuously circulating chain, without an engine to drive it, is absurd. This is the second remarkable step taken by Stevin – he considered ‘perpetual motion’ as self-evidently absurd, and used this as the basis for an argument (a reductio ad absurdum argument).1 To avoid the absurd outcome then the starting premise – section AX over-balances section XB – must be wrong; in other words, the initial distribution of masses, with the chain draping itself smoothly over the surfaces, must already be in equilibrium. This is a powerful proof, as it applies for an infinity of different starting states (different inclined planes).

Stevin realized he had discovered an eternal truth, and he displayed a diagram of his ‘Wreath of Spheres’ (clootcrans) as the frontispiece of his book on mechanics. The punchline, from our point of view, is that: without the use of forces, considering only gentle movements of the chain in harmony with the constraints (motion within certain surfaces), Stevin showed that, with respect to these motions, nothing changes, and equilibrium is maintained. In fact (going beyond Stevin’s own interpretation), the proof can be made to sound like pure geometry: for equilibrium, it is only necessary that the length of chain along an inclined plane is equal to the length of that inclined plane. Moreover, as any bumpy surface can be thought of as lots of tiny triangles, we have only to lie a uniform chain on this surface, with no bunching up or stretching out, and it will be in equilibrium.

Christiaan Huygens (1629–95)

Huygens, in Paris in 1656, tried to understand billiard-ball-type collisions but without the use of forces (this was some thirty years before Newton’s Principia, but billiards was a game that had been played since the fifteenth century). Then, as now, scientists were motivated by the thrill of showing that a great name was wrong. Descartes was the towering authority in the middle of the seventeenth century, and we shall see that three scientists (natural philosophers) in our story found errors in Descartes’ work – Fermat, Huygens, and Leibniz.

Back to Huygens. In his rules of collision, Descartes had claimed that a small body, hitting a larger body at rest, would never be able to shift it. Huygens knew that this couldn’t possibly be right – it didn’t agree with experiment.2 To show that Descartes was wrong, he used a remarkable demonstration. (Huygens might have been a bit apprehensive about contradicting the Cartesian view – Descartes had been a regular visitor to the Amsterdam home of Huygens’s parents, and his tutor was horrified to hear of the young Huygens’ ‘heresy’.)

Huygens’s remarkable demonstration consisted in putting the Principle of the Relativity of Motion (due to Galileo) to quantitative use – the first time this had ever been done.3 He imagined a ‘billiard-ball collision’ viewed simultaneously from two vantage points – from a smoothly coasting canal-boat, and from the canal-bank (undoubtedly his childhood in Amsterdam was an influence). Here is a picture of this thought-experiment, taken from the frontispiece of Huygens’s treatise.

It’s not clear from this picture whether the experiment was carried out on the boat or on the canal-bank. It doesn’t matter, so let’s say it happened on the boat. On the boat, the large mass hits a stationary smaller mass. Now we are free to choose the speed of the canal-boat so that it will exactly cancel out the incoming speed of the large mass when viewed from the bank. Then, as viewed from this bank, the small mass will collide with a stationary larger mass, and then cause this larger mass to move – and therefore Descartes is proved wrong.

The Relativity of Motion has been used to vet certain outcomes, but Huygens recognized that a general principle was at work: only those rules are correct which guarantee the same outcomes, no matter what frame of reference they are viewed from. The punchline: as with Stevin, certain ‘motions’ (in Huygens’s case, uniform motion of one reference frame with respect to another) have resulted in ‘no change’.

Huygens went on to use other symmetry arguments to develop his own rules of collision,6 and these were in better accord with experiment than Descartes’s rules. Although symmetry arguments alone didn’t answer to all possible outcomes, the telling point, for us, is that so much could be explained this way, and without the use of forces. Huygens noted in passing (drawing upon both his collision theory, and his theory of the compound pendulum) that a certain quantity was conserved: it was the total mv²… (m was the mass, and v the speed, of each body).

Gottfried Wilhelm Leibniz (1646–1716)

Huygens attached no great significance to the quantity mv². Leibniz, on the other hand, immediately realized its importance. He already knew of it from Galileo’s work on free-fall,7 but when he happened to learn of its conservation from Huygens (Huygens and Leibniz met regularly at the Académie Royale des Sciences in Paris) Leibniz built a whole new philosophy around it, calling it vis viva or ‘live force’. (Leibniz, from Hanover, introduced other ‘whole new philosophies’, fully justifying the German epithet, universal genius.) Straightaway, Leibniz made big play of how his new ‘live force’, mv², trumped Descartes’s ‘quantity of motion’, mv. (Leibniz’s paper was called “A brief demonstration of a famous error of Descartes and other learned men, concerning the claimed natural law according to which God always preserves the same quantity of motion; a law which they use incorrectly, even in mechanics”;8 the title, at any rate, was anything but brief.)

Leibniz’s mv² was essentially the same as our modern kinetic energy, ½mv² – it had no dependence on direction, it obviated the need to calculate accelerations, and, above all, it encouraged a ‘systems’ view. It was slowly learned, over the next 200 years, that energy existed in various scalar forms (the ‘structure functions’ of Chapter 1), and that altogether, within a closed system, it was conserved.9 We add that Leibniz’s philosophy also stressed another new idea (in common with Huygens) – the importance of symmetry: a free particle could not swerve to the left or the right as it had no ‘reason’ to do so (Leibniz’s Principle of Sufficient Reason). Leibniz was hundreds of years ahead of his time in using such arguments.

The dispute between Leibniz and the Cartesians evolved into a controversy between the Leibnizian school and the Newtonian school… between a whole-system view and an individual-particle view, and between ‘kinetic energy’ and ‘force’. Ultimately (as we shall find), it evolved into a contest between Newtonian Mechanics and the Principle of Least Action, a contest which, some say, still persists today.

Maximal/minimal properties

At the same time as conservation principles were beginning to hold sway, an alternative approach was coming in: nature was economical as well as conservatory with her resources. What was the measure of nature’s resources - time of travel? length of path? the total potential energy? Even while this was still unclear, it seemed to some philosophers self-evident that optimization was a crucial driver of physical processes. Chief among these natural philosophers was the great Swiss mathematician, Leonhard Euler (1707–83), who wrote: “nothing happens which has not some maximal or minimal property.”10 We shall meet him again in this chapter.

Max/min problems were already known about in antiquity. There is the story about the Phoenician princess, Dido. After running away from home, she reached the coast of North Africa and tried to buy some land.

9 Coopersmith, Et SC.

10 Euler L, ‘Additamentum I de curvis elasticis’, 1744, English translation in Oldfather et al, Leonhard Euler’s elastic curves, Isis 20 (1933) pp 72–160.

18 The Lazy Universe

Legend has it that she was allowed to purchase only as much land as could be encompassed by the hide of a bull. From this unpromising start, Dido cleverly maximized her land-area: she cut the hide into very thin strips and joined these end to end; she chose a plot by the sea so that the coastline would be part of the boundary; and she shaped the long strip of hide into the optimum shape - a semi-circle, up against the coast.

Heron of Alexandria (around AD 60) found that light reflected from a plane or curved surface took the shortest distance between the light-source and the detector (not counting missing out the mirror altogether). And Pappus of Alexandria, around 300 AD, observed that beehives had that special shape, hexagonal, which could hold the greatest volume of honey for the smallest expenditure of wax.

Our story becomes quantitative in the mid-seventeenth century with Pierre de Fermat (1601–65), French lawyer and ‘amateur’ natural philosopher. Fermat agreed with Heron’s results for the reflection of light but when it came to refraction he found that the path was not one of shortest distance but of least time. He elevated this to a general principle, his Principle of Least Time:11 “Nature operates by means and ways that are easiest and fastest.” Fermat was delighted with his Principle but “astonished”12 because his laws of refraction, while completely agreeing with Descartes’s laws, started from utterly opposite premises: Descartes (Fermat) required that light travelled faster (slower) in denser media.13 The Cartesians were not impressed - “The shortness of the time? Never.”14 By the way, we mentioned symmetry arguments in connection with Huygens, and Leibniz, but they are also present in Fermat’s Principle: for the reflection of light, the angle of incidence is equal to the angle of reflection.15 Also, another feature in Fermat’s Principle (the importance of this will be recognized much later), is that the correct path is not only the one taking 11 (in 1662, in a letter to de la Chambre) Goldstine H, History of the Calculus of Variations from the Seventeenth through the Nineteenth Century, Springer-Verlag, New York (1980).

12 Dugas R, A History of Mechanics, Dover Publications Inc. (1988).

13 Imagine how difficult it would have been to measure these speeds - or even know that light has a speed.

14 Dugas R, as above.

15 A symmetry rule applies in refraction as well: n sin θ i = n r sin θ r.

Antecedents 19

Figure 2.4 Brachystochrone, curve of ‘swiftest descent’. (schematic)

the least time, but the one whose time-of-travel is the same (to first-order) as the time-of-travel for neighbouring paths.

Isaac Newton (1643–1727), in his landmark work, familiarly known as “The Principia”,16 derived the optimum shape for a solid body so that it would move with the least resistance through a fluid. However, apart from this, and the ‘brachystochrone question’ - see below, there are no other examples where Newton tackled such max/min problems.

The Bernoullis of Basle in Switzerland exhibited an extremal property all of their own - they had the largest number of mathematical geniuses in one family (eight) that has ever been recorded. The brothers, Jakob and Johann Bernoulli, were at the start of it (born in 1654 and 1667 respectively), both brilliant but very competitive - they baited each other with silver ducats and impossible deadlines for the solution of difficult problems.

One famous problem was the search for the brachystochrone, the path of ‘swiftest descent’, taken up by Johann Bernoulli in 1696. A weight slides down a curve, and the question is: what shape must the curve have so that the travel time between given start-and end-positions is least? (Assume no friction, and that the destination point is not dead vertically down from the starting point.) Galileo Galilei (1564–1642) had already noted that the quickest path was not along the straight line connecting the points.

16 Newton, Isaac, The Mathematical Principles of Natural Philosophy, (1687) translated 1729 by Andrew Motte.

20 The Lazy Universe

Leibniz, Newton, de l’Hôpital, Tschirnhaus, and both Bernoullis all came up with solutions for this swiftest-descent curve. Newton’s had been submitted anonymously but Johann “recognized the lion by its claw”.17 Jakob and Johann both solved the problem but employed very different methods, each opening up grand new vistas in physics.

Jakob’s method was complicated and messy, but showed the way, ultimately, to more general techniques for max/min problems, a forerunner of Euler’s and Lagrange’s ‘calculus of variations’ (see Section 3.7, Chapter 3).

Johann’s method was a masterpiece of lateral thinking: he considered that the falling mass passed through successive sheets of ‘denser and denser gravity’, and was ‘refracted’ at each boundary in such a way that its total journey-time was least (a smooth curve was obtained by imagining thinner and thinner sheets). This was analogous to Fermat’s least-time path for light. Thus, Johann’s insight foreshadowed both Hamilton’s conjoining of light and matter into one theory (Chapter 7), and Einstein’s theory of gravitation (in which a freely-falling mass moves along a curved path, as dictated by the curvature of ‘space’ - the ‘gravitational refractive index’). Johann was centuries ahead of his time.

What was astounding for the contemporary mathematicians - and ever since - was that the brachystochrone turned out to have exactly the same shape as Huygens’ tautochrone,18 and both curves were the same as a third curve, the cycloid.19 As Johann Bernoulli wrote, “...you will be struck with astonishment when I say that this very same cycloid, the tautochrone of Huygens, is the brachystochrone we are seeking.”20 Before we move on from these wonderful old ‘chrones, the punchline is: whether ‘least time’ or ‘same time’, the optimized path is stationary - the total travel-time doesn’t change with respect to small variations in 17 Kline M, Mathematical Thought from Ancient to Modern Times, Oxford University Press (1972).

18 The tautochrone is the curve guaranteeing equal travel-times irrespective of (modest) variations in the starting position.

19 A cycloid is the curve traced out by, say, a pebble stuck in a tyre as a bicycle rolls forward.

20 Kline, as above, page 575.

Antecedents 21

either the whole-curve-shape or the start-time. (The term ‘stationary’ will be explained in Chapter 3.)

There were other curves that could be determined by the max/min method, for example, the curve of a hanging chain or suspension bridge, known as the catenary; and the ‘elastica’, the shape of a flexed metallic band (think of a metal ruler). This latter problem was investigated by Daniel Bernoulli (1700–82), the middle son of Johann, and the first true physicist (as opposed to mathematical physicist).21 The elastica could be determined, but what actually was the property being maximized or minimized? The following correspondence between Daniel Bernoulli and Leonhard Euler, from 250 years ago, makes fascinating reading:22

Bernoulli to Euler, 5 May 1739: “I have today a quantity of thoughts on elastic [metal] bands... I think that an elastic band which takes on of itself a certain curvature will bend in such a way that the live force will be a minimum, since otherwise the band would move of itself. I plan to develop this idea further in a paper; but meanwhile I should like to know your opinion on this hypothesis.”

Euler’s reply, 5 May 1739: That the elastic curve must have some maximum or minimum property I do not doubt... but what sort of expression should be a maximum was obscure to me at first; but now I see well that this must be the quantity of potential forces which lie in the bendings; but how this quantity is to be determined I am eager to learn from the piece which your Worship has promised.”

Bernoulli replies, 1742: My thoughts on the shapes of elastic bands, which I wrote on paper only higgledy-piggledy and long ago at that, I have not yet set in order.”

and again, from Bernoulli to Euler, 1743: “May your Worship reflect a little whether one could not deduce the curvature... directly from the principles of mechanics... I express the potential live force of the band by ∫ ds/r2... Since no one has perfected 21 Coopersmith, Et SC, Chapter 7.

22 Truesdell, C, introduction to Leonhardi Euleri, Opera Omnia, 2nd Series, Vols X and XI, Fussli, pp 173–4.

22 The Lazy Universe

the isoperimetric method23 as much as you [Euler], you will easily solve this problem of rendering ∫ ds/r2 a minimum.”

And in his famous paper24 the following year (1744) Euler writes: “although the curved shape assumed by an elastic band has long been known, nevertheless the investigation of that curve by the method of maxima and minima [could not be carried out until the] most perspicacious Daniel Bernoulli pointed out to me that the entire force stored in the curved elastic band may be expressed by a certain formula, which he calls the potential force, and that this expression must be a minimum in the elastic curve.”24

(In other words, Daniel needed help with the maths and Euler with the physics.) What is so fascinating is that we are witnessing not only the birth of variational mechanics, but also of kinetic energy (live force) and potential energy (potential live force). However, all these max/min problems were tackled individually, and it was not clear what if any overriding principle might encompass them all.

The Principle of Virtual Work

This principle will have a chapter to itself (Chapter 4). The first glimmerings of it, in the guise of the Principle of Virtual Velocities, are found in Aristotle’s analysis of the lever. When the lever is in balance, then the end with the heavier (lighter) load moves slower (faster) in proportion to its weight.

er). But, one may ask, if the lever is balanced, then the ends don’t move at all? Yes, that’s why these movements are called virtual, or ‘mathematically imagined’. This mathematical experiment is carried out in order that the criterion for balance may be established. (This will be explained in Chapters 3 and 4.) The same Principle was taken up by Stevin: “What is gained in the force is lost in the velocity”, and then again by Galileo. Galileo made an important advance in recognizing that it is only the velocity in the direction of the force which counts.

Finally, Johann Bernoulli, ever the clairvoyant, took up the Principle and realized its potential to solve all the problems of static equilibrium. (Before Johann, the Principle was limited to cases where there were just two forces, the ‘moving force’ and the ‘load’.) Bernoulli made significant improvements and took the Principle to a new level of generality:

(i) he applied the Principle to any number of forces - as many as the system demanded - (all in static equilibrium).

(ii) he no longer assumed that the virtual velocity was in inverse proportion to the force but, rather, considered the product of force and ‘virtual velocity in the direction of that force’. He called this product the ‘energy’.

(iii) he adopted a sign convention as follows - if the angle between force and velocity was acute (obtuse) then the product had a positive (negative) sign. (In modern parlance, the sign convention was the usual one for the ‘scalar product’ of two vectors.)

(iv) the criterion for equilibrium was that all these products, with appropriate signs, had to sum to zero.

Bernoulli’s revolutionary idea, a watershed in physics, was never published, but was written down as some throwaway remarks in a letter to Varignon in 1715. Fortunately, Varignon didn’t throw them away:

“In every case of equilibrium of forces, in whatever way they are applied and in whatever directions they act on [one] another, immediately or immediately, the sum of the positive energies will be equal to the sum of the negative energies taken positively.”

This is the first time that the word ‘energy’ appears in physics (an honour usually ascribed to Thomas Young in 1802).

One last thing, how did the Principle later get to be called the Principle of Virtual Work? The answer is that the Principle applies at an instant, and an instantaneous velocity is proportional to an instantaneous displacement (even while they are both ‘virtual’), and the scalar product of a force and a displacement is not just ‘energy’, it is that special kind of energy known as ‘work’. All this will be explained again in more detail in Chapter 4.

The Provenance of the Principle of Least Action: Maupertuis

Here is yet another principle in this plethora of principles, and it’s the one that will turn out to be the underlying principle, incorporating all the others. The principle arose out of successive generalizations of earlier principles:

(i) first, as we have already seen, there was Heron’s ‘shortest path’ for reflected light (second century AD),

(ii) then there was Fermat’s ‘Least Time’ for reflection and refraction (1662),

(iii) then Leibniz, in 1682, in his Principle of Least Resistance, pooh poohed Fermat’s Principle, for why should light make a choice between optimizing ‘time’ and optimizing ‘distance’? No, argued Leibniz, light takes the easiest path, the one for which the ‘resistance’ is least,

(iv) finally, Maupertuis, in 1644, extended Leibniz’s principle to cover the motion of light and bodies - he called it the Principle of Least Action.

The tale of Maupertuis and the Principle of Least Action is an entertaining one, redolent of the eighteenth century, and full of metaphysics, intrigue, and curious characters, and so we will let it divert us for a while. Lanczos whets our appetite with the following rousing words:

“[the eighteenth century] is the only period of cosmic thinking in the entire history of Europe since the time of the Greeks.”

Pierre-Louis Moreau de Maupertuis, son of a wealthy pirate, was born in St Malo, France (1698–1759). Maupertuis was variously a musketeer, geographer, amateur astronomer, biologist, moralist, linguist, and surveyor. In this last capacity, Louis XV commissioned him to lead an expedition to Lapland to measure the length of a degree along the Earth’s meridian; Maupertuis’s findings corroborated Newton’s predictions - that the Earth was flatter at the poles. Voltaire, famous French wit, and man of letters, was delighted and awarded Maupertuis the epithet ‘Earth-flattener’ (while also lampooning him for having brought two Lap women back to Paris). Voltaire later (around 1740) recommended Maupertuis to be President of the new Prussian Academy of Sciences being set up by Frederick the Great in Berlin (Frederick preferred French scholars, they represented the height of culture and refinement).

Around the early 1740s, Maupertuis discovered the Principle of Least Action, getting the germ of the idea, and the word ‘action’, from Leibniz’s Principle of Least Resistance, but extending the latter to cover the motion of bodies (Leibniz’s Principle considered only light). Maupertuis defined action as mvs, where m is the mass of the body, v its speed and s the path. For just one body the mass dropped away as merely a constant multiplying factor (its constancy was never in question at this stage in physics), and the quantity to be minimized was then the sum over vds, where ds was a small increment of distance travelled along the path.

The discovery of this principle was a turning point in Maupertuis’s career, he vaunted it and made it a cornerstone of his philosophy. In his essay “The laws of rest and of motion deduced from the attributes of God” he wrote:

“Whenever any change takes place in Nature, the amount of action expended in this change is always the smallest possible.”

Maupertuis also applied the principle to scenarios outside the purely physical realm (in his calculus of pleasure and pain, the total happiness was maximized and the total pain minimized) and, overstepping the mark (by modern standards anyway), argued that least action was proof of the existence of a “Supreme Being”.

The response to the principle was varied: the Leibnizians did not rate the principle as high as Leibniz’s conservation of ‘live force’; the atheists/materialists objected to Maupertuis’s use of the principle as proof of God’s existence; and some, especially the philosophe and encyclopaedist, d’Alembert, objected to the teleological implications - how did the body know which path was the minimum one? Just one philosopher was unequivocally on Maupertuis’s side - the great Euler.

Now one Samuel König (1712–57) had recently been elected to the Academy in Berlin, at Maupertuis’s invitation (König, Maupertuis, Voltaire, and Voltaire’s mistress, the marchioness, Mme du Châtelet, were all friends, promoting ‘Newtonianism’ in France, and often staying at Voltaire’s mansion at Cirey near Geneva). Nevertheless, König attacked Maupertuis’s Principle, saying that, on the one hand, Maupertuis had got it from Leibniz, and on the other hand, it wasn’t correct. Maupertuis demanded to see proof of Leibniz’s priority, which - said König - was in some letters that Leibniz had written to Hermann (a mathematician). König could not find the originals, which, apparently, were in the possession of a certain Henzi of Berne, who had been decapitated. Maupertuis was incensed, and wrote eleven times to Hermann’s heirs (via Johann Bernoulli (II) in Basle) asking them to hunt through all the old correspondence. Even so, the letters were not found (and they never have been). Maupertuis then arranged for a hearing of the Academy to determine whether König’s copies were forgeries. On the day (13th April 1752) Maupertuis was absent and Euler presided, but the result was a foregone conclusion (the Academicians were hardly impartial, as they relied on Maupertuis for their promotions). König was found guilty, appealed, lost again (8th June 1752), and then resigned from the Academy. Maupertuis, aware that these consequences made him unpopular, fought even more vigorously, and asked the Princess of Orange at the Hague to threaten König with dismissal from his post as Court librarian.

Then Voltaire got on the bandwagon, forgetting earlier epithets, and now criticizing Maupertuis for plagiarism, bad physics, being a tyrant, and anything else he could think of. This century saw the birth of satire and it was most unfortunate for Maupertuis to get on the wrong side of Voltaire, the facile princeps of satire. To top it all, Voltaire was in a dismal mood as Mme du Châtele had recently died in childbirth. He proceeded to write an entire book with the express purpose of pouring abuse on Maupertuis, casting him as a stupid, presumptuous fellow, the student of a certain Dr Akakia (‘kak’ would have sounded just as offensive in the eighteenth century as it does today).

Frederick II defended Maupertuis, the president of his Academy, and Euler also came to Maupertuis’s aid. In fact, Euler’s defence of Maupertuis’s priority was very generous, especially considering that Euler had found some serious errors in Maupertuis’s formulation, and had actually discovered the principle the year before Maupertuis! (Maupertuis’s formulation was vague and incorrect and he needed Euler to tidy it up, changing the sum into an integral, and showing that the principle was meaningless unless the conservation of energy applied). As Lanczos writes: “Although Euler must have seen the weakness of Maupertuis’ argument, he refrained from any criticism, and refrained from so much as mentioning his own achievements in this field, putting all his authority in favour of proclaiming Maupertuis as the inventor of the Principle of Least Action.” Principle of Least Action. Even knowing Euler’s extraordinarily generous and appreciative character, this self-effacing and self-denying modesty has no parallel in the entire history of science".

There has also been no parallel to Voltaire’s campaign of vilification. Maupertuis’s health was badly affected by the stress, and some while later he left Berlin for St Malo, still pursued by vitriolic volleys from Voltaire’s pen, never to return (Maupertuis died at a stop-over at Johann (II) Bernoulli’s in Basle).

The verdict of today? König was in all probability honest but naive and earnest, not appreciating that one must always allow the President of an Academy to have a face-saver. Maupertuis, although by all accounts an uppish fellow (“spoilt, intransigent, ... very short and always moving, with many tics, careless of his apparel.”32), nevertheless had genuinely stumbled into an idea of great and long-lasting importance. Although getting the initial idea from Leibniz - a source which Maupertuis didn’t deny - Maupertuis had taken it to a new level of generality (by applying it to masses). It is possible that Leibniz also proceeded to this step, but no evidence in the form of any original letters or papers was found at the time or since. Maupertuis’s outrage, and his attempts to track down Leibniz’s letters, appear genuine. It is true that Maupertuis was not in the first rank of mathematicians (mind you, being second to Leibniz and to Euler was not bad going) but, alone amongst his contemporaries, he did intuit the principle’s cosmic significance. Not even Euler had done this. Giving the last words to Euler: “This great geometer [Maupertuis] has not only established the principle [of Least Action] more firmly than I had done, but his method, more ubiquitous and penetrating than mine, has discovered consequences that I had not obtained.”33 and “nobody before the Illustrious President of our Academy [Maupertuis] has even suspected in what elements this principle was contained and how it could be accommodated to all cases. As regards myself, I only knew in a sure manner a posteriori the principle I used to determine trajectories; and I have ingenuously confessed that I was not in a position to establish its truth in another manner.”34 It seems that even the greatest of mathematicians can sometimes benefit from the intuitions of a generalist.

The Variational Mechanics This ends our brief survey of the antecedents. The Principle of Least Action proper was founded by Lagrange, and by Hamilton, with important contributions from d’Alembert, and from Jacobi. It is hardly surprising that this crowning glory of human thought should have been brought in by remarkable and unusual individuals.

Jean le Rond d’Alembert (1717–83) (the source of the quote heading Chapter 1) was a foundling, and given the name ‘Jean Le Rond’ from the church in Paris on whose steps he was left. The police traced his parentage to a famous salonniere and a cavalry officer. The salonniere never acknowledged her son but the Chevalier arranged for him to be fostered by a humble glazier and his wife. D’Alembert wrote his most famous works while living with his foster mother for 48 years. He finally “weaned”35 himself after 48 years, and then lived with his mistress, herself a famous salonniere. As well as being a mathematician and philosophe, d’Alembert was also joint editor of the famous Encyclopédie with Denis Diderot (until the two of them fell out, and d’Alembert left the enterprise to Diderot). The ‘d’Alembert’s Principle’ is explained in Chapter 5. It arises from his Traité de Dynamique, 1743, a work that seems to try to make every new idea as hard as possible to comprehend. (For example, it is startling for the modern mind to learn that mechanics is not empirical - according to d’Alembert, it is a purely rational subject.)

Joseph-Louis Lagrange (1736–1813), Italian by birth, was director of mathematics at the Prussian Academy of Sciences in Berlin (at the invitation of Euler and d’Alembert), then moved to revolutionary Paris in 1787, and continued his illustrious career as Professor at the École Normale (briefly), the École Polytechnique, the Bureau des Longitudes, and was a Senator in 1799. He managed to stay in favour on both sides of the French Revolution (1789) by cannily adopting his maxim: “every wise man [should] conform strictly to the rules of the country in which he is living, even if they are unreasonable.”36 He had a long happy marriage, was widowed, and then had a second long happy marriage; he expressly did not have children as they would be a distraction from work. One has the impression of a person who purposely led an uneventful life - this is often true of the most creative individuals.37 Lagrange discovered an outstanding method of minimizing integrals in max/min problems - the ‘calculus of variations’. Also outstanding was his ‘Method of Lagrange Multipliers’ (see Appendix A6.4). His masterpiece was the Mécanique analytique,38 published in 1788, the most comprehensive account of mechanics since Newton’s Principia from one hundred and one years earlier, and radical in being completely general (not tied to this or that mechanical scenario). It was unusual in another way - Lagrange announced in the preface that the work contained no diagrams, or mechanical arguments, but “solely algebraic operations”.39 William Rowan Hamilton (1805–65), from Dublin, Ireland, was a linguistic and mathematical prodigy. Aged eight, he unravelled the methods used by the American Calculating Boy, Zerah Colburn, and before his thirteenth birthday he knew thirteen languages. He later considered both poetry and mathematics as the wellsprings of his creativity (his friend, the poet William Wordsworth, tactfully told him to stick to mathematics). Due to the influence of another friend, the poet Samuel Taylor Coleridge, Hamilton was attracted by the idealist philosophy of the German philosopher, Immanuel Kant. Hamilton’s idealism also extended to his love affairs: his first love represented the ideal but remained on an abstract plane (she was forced by circumstance to marry another).

Hamilton was enormously impressed by Lagrange: he likened Lagrange to Shakespeare, and the Mécanique analytique to a scientific poem. It was this work which inspired him to the topic of mechanics which, like Lagrange, he tried to found in the most general possible terms, and purely algebraically. In fact, Hamilton’s mechanics (and optico-mechanical analogy) was so abstract and mathematically challenging that it lay unappreciated by all but one contemporary. From Hamilton’s optics and mechanics he came up with just one experimental prediction - that a beam of light rays would in certain cases be refracted into a 3-D cone of light. He was lauded for this - but in the main he was simply years ahead of his time, and the dividends were reaped only in the following century. His work is explained in Chapter 7.

The German mathematician, Carl Gustav Jacob Jacobi (1804–51), was that lone contemporary who did recognize Hamilton’s genius. In admiration, he coined the descriptor ‘canonical’ for Hamilton’s Equations - a curious choice for one of Jewish parentage, but perhaps Jacobi had the enthusiasm of the convert (he converted to Christianity while a student in Berlin).40 Readers may be familiar with Jacobi on account of ‘the Jacobian’ - a mathematical tool for transforming from one set of coordinates to another. Jacobi was indeed a great algebraicist, and his maxim was apparently “man muss immer umkehren” (“invert, always invert”). He enters our story as one who developed the ‘Hamilton-Jacobi Theory’ - a method for making Hamilton’s Mechanics workable (in the form reached by Hamilton, the equations were mostly too difficult to solve in any actual applications).

Portraits of the natural philosophers and physicists who discovered or used the Principle of Least Action are given in Appendix A2.1.

Mathematics and physics preliminaries: of hills and plains and other things

## 3.1 Coordinates

The programme of physics is the mapping of numbers onto physical things, then the carrying out of mathematical operations using these numbers, and then, finally, the translation back to the physical things, in other words, the making of physical predictions.1 However, there is no unique way to make the initial mapping or even to decide what needs to be mapped.

Galileo (1564–1642) was one of the first to stress that quantification was crucial - “This book [of the universe] is written in the mathematical language”2 he said. The first and most obvious quantity to be mapped was ‘length’ or ‘distance’. Galileo, in his famous experiments on freely-falling bodies, measured the distances travelled by those bodies (he used units such as dito, canna, and braccia3) and he realized that idealizing assumptions had to be made (about air resistance, friction, the flatness of a surface, the roundness of a ball, and so on). He also had the important realization that the different directions of ‘space’ were independent of each other. (For example, the horizontal and vertical distances travelled by a cannon ball could be calculated completely separately, but then could be combined to yield a parabolic path overall.)

Galileo's view of space was affected by his ideas about motion. His outstanding insight was that all motion is relative (his Principle of Relativity). This, in turn, had some outstanding implications: that there is no absolute state of motion, that there is no absolute state of rest, and that, left to itself, 4 a body travelling horizontally with constant speed will carry on travelling at that speed forever. This sounds a bit like Newton's First Law of Motion, still fifty years into the future, but, instead of Newton's 'inertial' motion, Galileo identified two kinds of 'natural' motion: vertical accelerated motion of a freely-falling body; and horizontal motion at constant speed of a body at a fixed distance from a gravitating centre. 5 Therefore Galileo's never-ending horizontal motion was not motion in a straight line, but was motion in a circle. In other words, for Galileo, all 'natural' motion was connected with a gravitating centre - either free-fall toward it, or circling around it - and the idea of motion proceeding infinitely and rectilinearly into empty space, seemingly for no reason, was unthinkable.

4 For example, the body is not propelled by a cannon, or impeded by air resistance.

5 Apart from these 'natural' motions, Galileo also identified 'forced' or 'violent' motions, the motion of things that were thrown, shot, or otherwise forcibly projected. A gravitating centre was a mass of planetary size.

Descartes (1596–1650) did think about it. In his view, the Universe had to be infinite in extent otherwise there would have to be a boundary and this would be counter to God's perfection. He introduced a new mathematical scheme which would change our worldview forever. 6 Space was represented by three 7 independent directions (x, y, and z 'axes'), infinite, straight, and at right angles to each other. The axes were marked off at regular intervals, and so an arbitrary point in space, P, could be identified ('coordinated') by three numbers, the coordinates (x, y, z). The consequences were extraordinary: in addition to the geometric proofs of the Ancient Greeks (the visual properties of straight lines, circles, triangles, and so on) there developed proofs that were purely algebraic (the equations of straight lines, circles, etc.). The techniques of this new 'coordinate geometry', meant that all the properties of parallel lines, right-angle triangles, and so on, could be explored even by a blind person, from within the space (there was no need for an extra dimension in which to view the shapes).

6 Actually, Fermat had the same idea independently of Descartes. Sometimes, when the time is ripe, then many thinkers have the same revolutionary ideas - but perhaps just two thinkers is not enough to draw conclusions in this case.

7 Descartes had just two axes, x and y, and it was Fermat who brought in the third, z.

Descartes not only extended Galileo's space to an infinite one, he also extended Galileo's conception of motion. While still holding onto Galileo's Principle of Relativity, he made it apply to all uniform motion, whether horizontal or not, and rejected Galileo's distinction between 'violent' and 'natural' motion. Also, curiously and presciently, despite his new infinite axes, Descartes thought that only local motion made any sense. 8

8 Westfall R, Force in Newton's Physics (1971) American Elsevier and Macdonald, London, page 59.

Newton (1643–1727), when a student, found a copy of Descartes's La Geometrie at a fair, and was about to throw the book away in disgust when his tutor persuaded him otherwise. 9 Descartes became one of the giants upon whose shoulders Newton stood, and Descartes's infinite space (and also his concept of 'inertial' motion) was passed on, through Newton, to succeeding generations. In 1687 Newton published his famous Principia 10 containing his three Laws of Motion (Appendix A1.1). The First Law relied upon a space that was universal and featureless - there were no absolute markers in it and so positions, distances, and uniform motions (that is, unaccelerated motions) could be determined only relatively (that is, relative to each other or to some imagined reference frame). By contrast, the forces and accelerations in the Second Law of Motion were absolute. To give an everyday example, a relation such as 'to-the-right-of' is not absolute - it depends on the position of your eye - whereas two magnets that are attracted accelerate toward each other and eventually collide howsoever you view them, and even howsoever you are moving as you view them. In summary, Newton's Laws required that there was one, true, absolute space, and that this space was a featureless, infinite, passive background to the events (forces and accelerations) within. 11

9 Westfall R, Never at Rest: a biography of Isaac Newton (1983) Cambridge University Press.

10 Newton I, The Mathematical Principles of Natural Philosophy (1687) translated 1729 by Andrew Motte.

11 Curiously, Newton's one, absolute space can be represented by an infinity of allowed ('inertial') reference frames - but it is to be understood that these are all equivalent to each other (they are identified in the next footnote).

One hundred and one years after Newton's Principia (1687), Lagrange published his Mécanique analytique (Analytical Mechanics) (1788), and changed the concept of 'coordinates' yet again. In Newton's worldview, particles and forces are dropped into space, an infinite Cartesian 'reference frame'. 12 Lagrange, however, uses coordinates that are tailored to the given scenario, and that must be reformulated for every new scenario. For example, consider going from a system with just one particle to one comprising N particles. According to Lagrange, the new system has 3N coordinates, (x_1, y_1, z_1, x_2, y_2, z_2, .... x_N, y_N, z_N), and therefore 3N dimensions of 'space' whereas, according to Newton, there are always just 3 space dimensions (x, y, and z) whatever the number of particles. The fundamental difference is that, in Lagrange's mechanics, particles are not dropped into space, they are space.

12 The reference frames may be in different positions, orientations, or have different states of uniform motion.

Lagrange went even further: not just particle-positions but any continuously graduated and quantifiable physical attributes can count as coordinates. For example, we can map the angle, θ, that a simple pendulum swings through; or the distance, s, that a bead travels as it moves along a curved wire; or the radial distance, r, and angles, θ and φ, of an orbiting satellite; and so on.

(there is no time-dependence) and dynamics (there is a time-dependence). However, Lagrange was the first physicist whose dynamics, on occasion, treated ‘time’ on a more equal footing with the other coordinates. He sometimes lumped all the coordinates, including time, together, making them all dependent on some new ‘dummy variable’. Time is special in yet another regard. When all but microscopic phenomena are investigated, time appears to flow, and always in one direction (from ‘the past’ to ‘the future’). It’s very strange to say, but this profound yet banal human experience of time plays no part whatsoever in the dynamics of either Newton or Lagrange. Even though the dynamics examines macroscopic effects (but, crucially, microscopic dissipative effects, like friction or air resistance,18 are ignored), there is no sense of time flowing, no difference between making time run forward or backward in the equations. As Einstein wrote: “...the distinction between past, present, and future is only an illusion, however persistent.”19

## 3.3 Degrees of Freedom

We have our coordinates, say, n of them for the given system. There may still be different coordinate representations, connected by transformation functions, for this given system (for example, we may use Cartesian, or spherical polar coordinates). Also, there may be extra conditions - such as the conditions of rigidity, incompressibility, or inextensibility. Say there are m such conditions. Then there will be only n–m truly independent coordinates. Now when we have explored lots of different coordinate representations, then that one using the smallest number of independent coordinates determines the ‘number of degrees of freedom’ of the given system. However, it must be admitted that the ‘smallest number of independent coordinates’ is a dry and overly formalistic criterion for something so important. Physically, the degrees of freedom are the defining characteristics of the given system - the irreducible, independent ‘motions’ of which the system is capable - and their explanatory power is just as important as the economy of coordinates.18

While the degrees-of-freedom is ultimately a somewhat slippery concept, it is, nevertheless, an inherent property of the given system, and not merely a property of this or that coordinate description.

Economy may be a good thing, but how can we be sure that we have enough coordinates to completely describe the system? This is really the same as asking how we can be sure we have taken account of all the effects. In this regard Einstein, as so often, comes to our aid. Suppose, for example, that we are monitoring waves breaking on the beach. The waves arrive every few seconds and have a wavelength of a metre or so, but then we realize that we forgot to take account of the swell with a wavelength of one or two kilometres. This swell was not noticeable on our length and time scales, and - this is Einstein’s message - if an effect isn’t noticeable then we don’t need to notice it.20 In other words, if we think we have enough q to describe the system, then we probably do.

## 3.4 A generalized mechanics

We have gone from Cartesian coordinates to generalized coordinates, and from Newton’s particles to ‘generalized particles’ (lever arm, pendulum bob, capacitor plates, and so on). Force will become generalized as well, but it is part of a whole change of tack. We move away from Newton’s outstanding and simple ‘F = ma’, to a new energy analysis in which ‘force’ is replaced by the ‘work done by a force’. We remember from high-school physics that the work done by a force, F, acting through an infinitesimal21 displacement, dr, is given by the scalar product F·dr. For example, for N Newtonian particles with position vectors, r, displacements, dr, and each subject to a force, F, then the total work done is: dW = F1·dr1 + ... + Fi·dri + ... + FN·drN (3.1)

What is rarely stressed is that this is a highly specialized definition in which Fi and dri are ‘rectangular vectors’, that is, they are referred to the rectangular22 axes, x, y, and z. Making the switch to the generalized coordinates, we have the generalized work: dW = Q1·dq1 + ... + Qi·dqi + ... + Q3N·dq3N (3.2)

where dqi are infinitesimal changes in the coordinates, qi, and the Qi are functions of these coordinates, Qi = Qi(q1, q2, ...q3N). Comparison of equations (3.1) and (3.2) suggests that the ‘Q’ may be regarded as stand-ins for the ‘F’. Yes, but note several things: the i in equations (3.1) and (3.2) have different ranges; the F is a vector and is the total force (including constraint- and internal-forces) on the ith Newtonian particle; ‘Q’ is not necessarily a vector,23 and applies to a ‘generalized particle’ as it goes through a ‘generalized displacement’, dq. This may all sound like mere formalistic pedantry, but our message will be that the formalism (the mathematics) has physical implications (and vice versa). For example, a ‘generalized particle’, by its nature, moves only in a certain way, in harmony with the constraints and kinematic conditions (a car travels along a road, but a 4-wheel-drive can go over the rough, while a person walks along a footpath24). As the ‘generalized particle’ moves harmoniously, that is, in keeping with the constraints and kinematic conditions, then it doesn’t do work against these constraints and kinematic conditions. Therefore the generalized forces, Q, do not include constraints and kinematic conditions - they represent applied or external effects only. This is a major difference between the forces and the generalized forces.

More to do with formalism: the total work in equation (3.2), sometimes symbolized U, is what, in the old classical physics, used to be called the ‘work function’. The term ‘function’ is used advisedly. ‘Work’ is a form of energy, yes, but it is a rather special kind of energy, having a functional dependence on the distribution of various macroscopic components (like the raising of weights, the stretching of a spring, and so on). Remembering also that there is a functional connection between the different coordinate representations (Section 3.3), then it is hardly surprising that the Q1, Q2, ... end up as being functions of the q1, q2, ... They may also be functions of t. The Q1, Q2, ... are known as the generalized forces. As already mentioned, they are not necessarily rectangular vectors, and do not necessarily have the dimensions of force. The only requirement is that, while the generalized displacements need not have the dimensions of length, and the generalized forces need not have the dimensions of force, each product, Qi·dqi, must have the dimensions of energy.

Although it seems that the work function must be less fundamental than the force (as it requires force in its definition), this mistaken hierarchy is partly due to historical accident (force was discovered first), and partly due to the fact that the force-analysis is simpler and more intuitive. But, in fact, it is the work done that is more fundamental. As Lanczos writes:25 “Although we are inclined to believe that force is something primitive and irreducible, the [variational] mechanics shows that it is not the force but the work done by the force which is of primary importance...” Now in the Newtonian Mechanics a force causes a particle to accelerate whereas in the Variational Mechanics the ‘work done’ causes a ‘generalized particle’ to change its kinetic energy. This is why Lanczos also writes: “the really fundamental quantity... is not the [rate of change of] momentum but the kinetic energy.”26 ‘Work done’ and ‘kinetic energy’ are both forms of energy, and this confirms our starting assertion that Newton’s ‘force-mechanics’ is being replaced by a new ‘energy-mechanics’.

We shall also find that the dichotomy is not just between force and energy, but between a whole-system feature (the work function or configuration-energy) and the individual energies (the kinetic energy of each individual mobile component). Now a system is evidently made up of its components, but the boundary between ‘whole’ and ‘parts’ is not always clear-cut. In the variational mechanics the motion of components, and even the mass of an individual component, can affect the ‘whole’, whereas in Newtonian Mechanics the influence between ‘F’ and ‘ma’ is all one way.

Curiously, while energy is in the ascendant in the Variational Mechanics, the well-known Principle of the Conservation of Energy will be relegated to a subordinate role, applying only in the special case where there is no explicit dependence on time. In the special case in which the work function, U, is time-independent and also doesn’t depend on the ‘speeds’, q1, q2, ...,27 then U is the same as the potential energy, V (actually, by convention, U = –V).

## 3.5 ‘Space’ - a mathematical testing-ground

We have generalized coordinates, generalized particles, and generalized forces; we also have need of a new generalized conception of ‘space’. A crucial requirement is that our choice of ‘space’ - a mere viewpoint - must not make any difference to the system being investigated. This requirement is certainly satisfied when switching between, say, rectilinear and curvilinear28 coordinates - this is a purely mathematical procedure effected by mathematical transformations between coordinates. However, we can go from one space,29 qi, to a second space, q′j, in another way - we can adopt two completely different physical models for the one given system (for example, we can model bells, or their clangers).

However, space and physical...

assumptions are intimately related. Let’s examine this relationship first in the familiar territory of Newtonian Mechanics. By Newton’s First Law of Motion, a free particle travels in a straight line at constant speed - but how shall we know that this particle, coasting along in empty (Newtonian) Space, is in fact moving through regular distance intervals in regular Time intervals, in other words, how shall we know that it is really moving in a straight line? We can only be assured of this by postulate - that there really are no forces operating, and that the universality and regularity of our rulers and clocks can be relied upon. How can we be assured that our free particle is not swerving to the left? Again, we can only be assured of this by postulate. Also, if the particle is not free but is subject to a force then it will have an acceleration determined by that force, and also by the particle’s mass. How can we be sure of this? Because we assert that our reference frame is definitively not accelerating, and also that the mass is constant between reference frames.

Notation: a dot over a symbol is a shorthand for d/dt.

Note that curvilinear coordinates, such as (r,θ,φ), do not make a flat ‘space’ become ‘curved’. The true meaning of ‘curved’ will be explained in Section 3.6.

Notation: we mostly drop apostrophes round the word space from now on. The curly brackets, {qi}, is a shorthand for the whole set of n coordinates: q1, q2,...,qn. The prime, q′j , means different space, it does not mean differentiation.

In the Variational Mechanics, a ‘free’ generalized particle is one that goes through its paces, its degrees of freedom, unhindered: the pendulum bob swings, a marble rolls down the marble-run, the Earth follows an elliptical orbit around the Sun, a pebble falls freely until the instant before it reaches the ground. So, ‘free particles’ can swerve, speed up, or slow down, - all accelerations - but accelerations can now be considered as ‘inertial’, and sometimes even define the new ‘straight’ lines of space. In effect, the concept of ‘inertial’ has also been generalized, but the new ‘inertial’ is no longer divorced from ‘space’. For example, ‘inertia’ can depend on the spatial distribution of mass (the ‘moment of inertia’ is often proportional to r2); and the response of an electrical circuit is dependent on the distribution in space of its components (merely curving a straight wire into a coil turns it into a new component - an electromagnet). What is perhaps less well appreciated is that time also affects space (the rate at which a bar magnet is pushed into or out of an electromagnet affects the strength of the induced currents; triangulation using lasers relies upon the regularity of clocks; and so on). Also, it is well attested that the presence of very large gravitating centres affects the surrounding space.

This interrelation between space and the given physical features makes the challenge of finding a fiducial viewpoint - the challenge of objectivity - seem insurmountable. But this challenge can be met, and what we require is a space that can serve as an agreed mathematical testing-ground - a mathematical-test-space. How we meet this requirement is rather clever: instead of using physical space, we construct a completely abstract space. We take the n generalized coordinates for the given system, q1, q2,...,qn, and plot them against n rectangular axes (straight lines meeting at right angles) - it’s as simple as that. And, in the same way as we have been used to associating the position of a point in physical space with the three coordinates, x, y, and z, we now associate the position of the system in abstract configuration space with the n coordinates q1, q2,...,qn. The ‘position of the system’ is known as the configuration point or C-point, and it represents the state of the whole system (the values of all the qs) at a given time. Finally, in the same way as we can track the actual motion of a particle along a trajectory as its position changes in time, so we can track the abstract motion of the C-point as it moves along a curve, its world-line, through time.

To emphasize that this configuration space is truly abstract, we consider an example from outside the realm of physics. Imagine a two-dimensional configuration space in which we plot the number of white chess pieces against the number of black chess pieces, as a given chess game proceeds. If the end-game is long and drawn out, with no pieces taken, then the C-point will remain fixed, even while the actual, physical disposition of the chess pieces keeps changing.

We now have our mathematical testing ground - configuration space - but what shall the mathematical test be? From the title of this book, we can guess that it will be a test of stationary or least action, but we must creep upon this more slowly.

## 3.6 Invariants: ‘space research’

The layperson’s perception of Einstein’s legacy is that he found that ‘everything is relative’. This couldn’t be more wrong: the true content of Einstein’s Principle of Relativity is that the important things are not relative, they are invariant (invariant with respect to different viewpoints, cf. d’Alembert’s quote at the start of Chapter 1).

Let’s compare two views - spaces - of one physical system. There is an important proviso, crucial to Variational Mechanics: the two spaces must be connected by coordinate transformation functions. In Figure 3.1 we see a column in the mirror-surface, and the same column in the table-top surface. We find that straight lines have become transformed into curves, and distances and angles are not preserved (for example, the grooves in the column are parallel in one space and diverging in the other space).

Nevertheless, there are certain geometric features that do remain the same between the two spaces: there is just one column, it always has exactly 10 straight grooves, and the leaves, whorls, and flowers are always at the top of the column (not half-way up). These are so-called topological features, and their importance lies in the fact that they are invariant between spaces. If our mechanics can be couched exclusively in terms of such invariant topological features then it has a chance of being universal.

What is the topological feature we use when it comes to mechanics? Comparing the spaces in Figure 3.1, two things can be noted. One is that the position of a point is not a very robust quantity, it can change from one space to another - for example, for a reference frame whose origin is in the middle of a flower, the petals are all the way around this origin; whereas for an origin sited on the tip of one petal, then all the other petals are to one side. The other noteworthy thing is that the smaller the portion of space that is investigated, the more closely the different mappings approach each other, topologically-speaking (curved line-segments approach straightness, line-segments that diverge in the large appear parallel in the small, and so on). So, better than the position of one point, P, is the difference in position of two points, P and Q; and better still than the difference in position of P and Q is the difference in position of P and Q as Q gets infinitesimally close to P.

We are familiar with using the ordinary differential calculus to determine the tangent line at a point, P, on a curve - we examine the slope as a nearby point gets arbitrarily close to P. In configuration space we are now in a space of n dimensions but we can analogously identify a space of (n–1) dimensions that is ‘tangent to’ the n-dimensional space at the point P. The branch of mathematics that deals with the rate of change of a ‘hyper-surface’ at a point is called differential geometry, and it is just what’s required in order to arrive at a topological feature that will be invariant. (The old-fashioned name, the absolute calculus, is better at reminding us of this asset.) We are about to find out that the topological feature that will be relevant in mechanics is the ‘stationary point’ (see Section 3.7) of the hyper-surface corresponding to the given configuration space.

Before returning to this discussion, let’s pause for a brief tour of the history of ‘space research’. We showed earlier (Section 3.5) that there was a link between the mechanical assumptions and the properties (the geometry) of space. Now it so happened that the predictions of Newton’s Mechanics and the geometry of Euclid’s space were so perfectly matched that (almost) everyone simply took it for granted that space - everyday physical space - was Euclidean. It came as something of a shock, therefore, when Einstein declared (in 1915, in his Theory of General Relativity) that physical space was not Euclidean. For example, Einstein predicted that it wasn’t true that the angles of a triangle would always sum to 180 no matter where the triangle was located, or that parallel lines remained parallel however far they were extended.

Actually, mathematicians in the nineteenth century had already discovered the possibility of non-Euclidean spaces but few realized that these abstract speculations could have any relevance to the real physical world. One who did realize this was the mathematical genius, Carl Friedrich Gauss (1777–1855). He tried to measure the angle-sum of a triangle defined by three mountain-tops - but the experiment was too crude to bring out the tiny deviation from 180. However Gauss made an outstanding theoretical discovery: the properties of a space could be determined algebraically, that is, from totally within that space (in Section 3.1 we remarked that Descartes’s coordinate geometry had likewise liberated us from the need to look at space from a higher dimension outside the space). Then there was Bernhard Riemann (1826–1866), who took Gauss’s investigations to a new level of generality (see below). (There were others, Bolyai, and Lobachevsky, but we won’t pursue them.)

Are the quintessential properties of a space determined solely by certain axioms concerning triangles, circles, parallel lines, and so on? Yes, the properties of a space are so-determined, but Riemann’s brilliant discovery was that the properties of space can be determined by examining just one formula—the formula for the infinitesimal ‘distance’ between neighbouring points, ds. Before Euclid, another ancient Greek had already come up with such a formula. This was Pythagoras (or, strictly speaking, the Pythagorean School), around 500 BCE, who promoted the famous formula known as Pythagoras’s Theorem:

Pythagoras’s Theorem, (ds)² = (dx)² + (dy)² (3.3)

Riemann realized some fundamental things: (i) Pythagoras’s Theorem not only told of the properties of right-angled triangles, but the function (ds) (the positive square root of (ds)²), was the ‘distance’ between two points; (ii) more than that, it was the shortest ‘distance’ between two points; (iii) most amazing of all, Pythagoras’s (ds)² was but one possibility—more generally, it could be written as:

(ds)² = g_{xx}(dx)(dx) + g_{xy}(dx)(dy) + g_{yx}(dy)(dx) + g_{yy}(dy)(dy) (3.4)

where the g are coefficients to be determined. In Pythagoras’s Theorem, it just so happens that we have the values g_{xx} = 1, g_{xy} = 0, g_{yx} = 0, and g_{yy} = 1. In other cases (other spaces), the g_{ij} need not have these particular values, and need not be constants—they could even be functions of x and y. This discussion has, so far, been in a space of only two dimensions, but Riemann generalized his ‘distance function’ still further to n dimensions:

Riemann’s distance function, (ds)² = Σ_{i,j=1}^n g_{ij} (dq_i)(dq_j) (3.5)

Most remarkable of all, Riemann showed that all the geometric properties of an n-dimensional space can be completely determined by just this ‘distance’, ds (the square root of the above equation). For example, if any of the coefficients, g_{ij}, are not constant but are functions of the coordinates, then the corresponding space is not ‘flat’ (Euclidean) but ‘curved’. This, finally, is what ‘curved’ means: it is a measure of the departure from Euclidean space, and is determined by certain functions (Riemann’s ‘curvature functions’) of the g_{ij}-coefficients. While the ‘distance’ is specific to the given space, its value is invariant as regards which coordinate representation has been adopted.

In view of our quest for invariant properties, Riemann’s distance function is obviously very important. In effect, Riemann’s distance function enables us to turn ‘space research’ on its head: instead of starting with Pythagoras’s Theorem (leading to a Euclidean space) we can instead start with a postulate of a certain distance function, ds, and then explore the consequential geometry of that space. (Any space characterized by a certain distance function, ds, will be called a Riemannian space.)

Optional: Some well-known cases are: (i) Euclidean space, ds = √[(dx)²+(dy)²], (ii) Fermat’s Principle, ds = time-of-flight along a light ray, (iii) Special Relativity, ds = ‘spacetime interval’ = √[(dx)²+(dy)²+(dz)²–c²(dt)²]), (iv) ds = √(2T) dt where T is the kinetic energy in a conservative system with no potential energy, (v) ds = √[2(E–V)] dt where (E–V) is the kinetic energy in a conservative system with potential energy V and total energy E, (vi) General Relativity, ds = dτ = an interval of ‘proper time’ (in units where c=1).

How does all this relate to ‘mechanics’ (pendula swinging, juggling clubs twirling, cantilever bridges, LC circuits, planets orbiting, starlight passing near the Sun, and so on)? All the definitions of ds just given (optional reading) are examples of special spaces for special cases. However in general mechanics we have bodies with mass, a potential energy function V, and V may be time-varying, and there may be additional constraints and kinematic conditions: in these most general cases, ds is an interval of action.

The function ds or ‘metric’ appropriate to our problem determines the ‘curvature’ of the space of that problem: and any mechanical problem (not just Einstein’s Gravitation) may be said to occur in a curved space. For example, a bead travelling along a bendy wire needs more force to move it through tighter twists—its space is not uniform, it is curved. Now a mechanical system with n degrees of freedom can be depicted using an n-dimensional configuration space, but if there are m conditions (the condition of moving along a wire, of maintaining the shape of a spinning top, of hanging on an inextensible cord, and so on) then the configuration space is reduced to a subspace of (n–m) dimensions. This subspace will usually be curved. For a problem with no potential energy and no explicit time-dependence, the C-point moves along a ‘geodesic’—the ‘straightest’/‘shortest’ path between given end-points—in this curved subspace. For problems with an external influence (there is a V) we can still establish what is the ‘geodesic’, but not determine the C-point’s speed along it. However, this extra information can be reconstructed afterward (using the condition of energy conservation). Finally, even if the external conditions are time-varying, we can add the time to the position coordinates, thereby increasing the dimensionality of the space by 1, and, again, determine the ‘geodesics’ of this new space. All told, the mechanical problem has been translated into a problem of (differential) geometry.

(It will not be possible to absorb these difficult new ideas in one go, their meaning will become more and more apparent as we proceed through the book.)

## 3.7 The Calculus of Variations

In this section we interrupt our story (it will be continued in Chapters 4 to 7) in order to explain some mathematical techniques. These techniques will be very helpful in the understanding of everything that follows—but they may be skipped over without too much loss of continuity.

3.7.1 Extremum problems—of hills and plains

Popularly, it is thought that hills and valleys are the antithesis of plains but actually hill-tops, valley-bottoms, and plains all have something in common. In extremum problems we are not trying to find the highest peak in a whole mountain range, but rather we are already on a given mountain and want to determine the position of the very top. Wherever we are on the mountain we ask ourselves—are we at the top yet, or does our next step take us even higher? In other words, the location of the highest point requires an inspection of the immediate—the local—surroundings. It is with respect to their local surroundings that hill-tops, valley-bottoms, and perfect plains are all the same—they are all flat. The extremum point of interest involves ‘no change’ relative to local, neighbouring points, and so it is called the ‘stationary point’ (it is said to exhibit ‘stationarity’).

In the variational mechanics, we still explore a ‘surface’, but it may have more than just the two dimensions of hills or plains (an n-dimensional surface is called a ‘hyper-surface’—as mentioned in an earlier footnote). Also, we are usually only interested in whether the conditions for stationarity have been met—whether the point in question happens to be a true extremum (a maximum or a minimum), or merely an inflection point, or a point within an extended flat plain, is irrelevant.

3.7.2 Three kinds of infinitesimal

Suppose we have a function, y, of n variables, x₁, x₂, ..., xₙ, that describes an n-dimensional space, a hyper-surface, y = y(x₁, ..., xₙ). We wish to determine whether the point P in this surface is stationary or not. As we have just seen, in order to establish whether a point is stationary, we must examine the region infinitesimally close by. However, there are three distinct ways in which to take an infinitesimal step.

(1) Actual displacements

We can explore from P to a nearby position, P', by allowing the variables x₁, x₂, ..., xₙ at P, to be displaced (change their values) by very small amounts, dx₁, dx₂, ..., dxₙ. You could say that we’ve put out tiny feelers in all the relevant directions. Then we draw the feelers back in, and ‘in the limit’ as P' reaches P, all the displacements are once again zero. This ‘limiting process’ is mathematical and not haphazard—the displacements scale down in unison, and must at every stage satisfy the function, y(x₁, ..., xₙ), and must at every stage maintain the proper proportions to each other as determined by any constraints. Only in this way can it be guaranteed that all the displacements will scale down and reach zero together. This mathematical down-sizing process implies that the difference between y(x₁+dx₁, x₂+dx₂, ..., xₙ+dxₙ) at P', and y(x₁, x₂, ..., xₙ) at P, called the ‘total differential’, dy, is given by the well-known rules of differential calculus:

dy = (∂y/∂x₁) dx₁ + (∂y/∂x₂) dx₂ + ... + (∂y/∂xₙ) dxₙ (3.6)

The condition for the stationarity of y at P is that dy at P is zero.

For simplicity, let us consider the one-dimensional case in which y is a function of just one variable, y = y(x). The n-dimensional ‘surface’ then reduces to the curve, y(x). (We assume that the functional form of y is known, and that it is continuous and differentiable.) The condition for stationarity at P then becomes: dy/dx = 0 at P. For example, y(x) could represent the vertical position of a cannonball as a function of time; or the vertical position of a cannonball as a function of its horizontal position; or the force on a spring as a function of the extension of the spring; or the torque on a lever-arm as a function of the angular displacement at the pivot; and so on. Let’s examine the second example, the path of the cannonball, shown in Figure 3.2.

height = y horizontal position = x

Figure 3.2 The path of a cannonball. (schematic)

It so happens that in this problem we know that y is the function y = –ax² + bx where a and b are constants. Suppose we want to determine whether y is stationary at the point P shown in the figure. There are two perspectives on this. From the physical, experimental, perspective, we can take successive The measurements of the ball’s position, plot the graph, and see whether or not the curve appears flat at P. From a purely mathematical perspective, we can use the well-known method of ‘calculating the differential’, dy/dx, and then check numerically and see if dy/dx is indeed equal to zero at P. (In the example shown, y = –ax² + bx, so dy/dx = –2ax + b, and this is equal to zero whenever x = b/(2a). So, we must examine whether x at P has the value b/(2a).)

Are these two perspectives, the physical and the mathematical, equivalent, leading to the same result? Amazingly, they are. It must be admitted that it’s impossible to make measurements that really do get smaller and smaller all the way to zero, yet, the important thing is that the cannonball really does undergo actual horizontal displacements (dx) as it whizzes through the sky, and there is, in principle, no objection to our physically sampling the curve anywhere we like.41 (Note that, from either perspective, we just ascertain the flatness, we don’t determine the height of the ball at P.)

(2) Virtual displacements Now, we consider a different kind of infinitesimal displacement called a virtual displacement, δx (or, in n dimensions, the virtual displacements, δx₁, δx₂, ..., δxₙ). To distinguish it from the previous kind of displacement we give it a different symbol, δ. We again wish to carry out a test of stationarity at the point P, and this again involves an investigation of the neighbourhood infinitesimally close by; but now, for various reasons, the displacements, δx₁, δx₂, ..., δxₙ, are not all physically possible. For example, they may imply bodies having infinite speeds, or displacements of physical components which can’t actually be moved (like the blocks in a Roman arch), and so on. We don’t let this stand in our way, but press right ahead and mathematically imagine the displacements instead. This was Lagrange’s brilliant idea (one of many).

Nevertheless, our mathematical imagination must be constrained. The new positions, (xᵢ + δxᵢ), must still satisfy the function y (it is, after all, this same ‘surface’ that we are exploring) and there may also be constraints between the displacements (this is just another way of saying that the variables may not all be independent of each other). In fact, we have exactly the same mathematical requirements as we had before, and so we can now write down exactly the same equation as before, but substituting δx for dx:

δy = (∂y/∂x₁)δx₁ + (∂y/∂x₂)δx₂ + ... + (∂y/∂xₙ)δxₙ (3.7)

Once again, the stationarity of y at P requires the zero-value of δy at P.

Thus, in case (1) we had both a mathematical and a physical perspective, whereas now, case (2), we retain the mathematical perspective but let the requirement for an actual physical perspective fall away.

Let’s consider a one-dimensional example. Suppose we have a ladder, of given mass, leaning against a wall; the wall is assumed completely smooth, but there is some contact friction between the ladder and the floor. We wish to determine the conditions for stationarity, that is, for static equilibrium at some position, P, of the foot of the ladder. Instead of balancing forces and/or balancing torques (the Newtonian method), we adopt a radically different procedure, and allow the foot of the ladder to be virtually displaced, very slightly, toward or away42 from the wall (Figure 3.3).

However, this displacement doesn’t actually happen, the foot of the ladder does not really slip through position P - it’s not a ‘falling-down-ladder’, it’s a ‘stable-ladder’ that we’re investigating. By contrast, the cannonball really does fly through position P in Figure 3.2. Thus, the infinitesimal mathematical displacements of the cannon ball are also actual physical displacements, whereas the infinitesimal displacements of the ladder are purely virtual displacements - they don’t actually happen, they are mathematically imagined.

(The problems in Figures 3.2 and 3.3 are worked through in Appendix A6.1 (problem 6), and Section 4.10, Chapter 4.)

There is just one more requirement to note about the virtual displacements - they must be reversible, that is to say, for any displacement, δxᵢ, a displacement in the reversed direction, –δxᵢ, must also be possible. This is to ensure that we can always approach the C-point from either the positive or negative directions (for each i), and this in turn ensures that we can ascertain whether the C-point is at a true stationary point, and not merely at a ‘false’ extremum existing on a boundary (see the washingline in Figure A3.1, Appendix A3.1).

Now, you may object that, if we are assuming a stable ladder, then we have presumed the very answer that we seek. This isn’t so, as we are really asking the question: “granted that the ladder is stable, then what are the mathematical conditions that are implied by this stability?” Note that while the displacements are virtual yet they must still satisfy the actual, physical constraint conditions (the ladder-foot moves only within the surface, it doesn’t burrow into the floor or jump into the air, and the whole ladder maintains its rigidity).

There’s no denying that the idea of virtual displacements is difficult and, at first glance, mysterious, but let’s argue the case for mathematical experimentation the other way around. The mathematician can imagine anything he/she wants to (infinite speeds, Dirac delta functions, bishops moving only diagonally, and so on); imagining is not the problem, but why should these physically impossible imaginings tell us anything physically useful, that is the question. There are two answers. First, although we have set up this artificial construction of virtual displacements, in fact it is only the point P itself that we’re interested in (the position of the C-point in configuration space) and at this point the distinction between dx and δx in effect disappears. Second, there are many precedents where mathematics has provided criteria that have no direct physical manifestation. For example, consider two rods moving in different directions at speeds close to c, the speed of light. Even though the rods move at speeds less than c, the mathematical point of intersection of the rods can move faster than c. Quantum mechanics abounds in cases where there are mathematical conditions for which there is no direct physical analogue (although, of course, the mathematics leads on to predictions which can be checked upon physically). There is one other telling example, the only other case where the adjective ‘virtual’ is used in physics. This occurs in geometrical optics, where extensions of actual light rays are mathematically imagined. If these virtual extensions intersect then we have a focused image but it is an image where there is no actual light.

We started this chapter with the broad assertion that “The programme of physics is the mapping of numbers onto physical things...” but now we are finding that the intersection of maths and physics is more murky than this suggests. In fact, the problem of understanding virtual displacements is entirely one of merging the physical and the mathematical worlds: if we were solving a problem in pure mathematics, then all the displacements would be of one kind - virtual - and no problems of understanding would arise.

(3) Imperfect displacements So far, we have had displacements, dx or δx, and we have been concerned with determining dy or δy, where y is a specific function that has been supplied beforehand. But what if there are displacements but there is no function y? For example, we might have a guinea pig nibbling its way through a biscuit: with each tiny bite more and more of the biscuit disappears, but we can’t express this as a functional relationship between bites and biscuit-shape. All we can say is that each actual, tiny bite, dx, causes an actual, tiny reduction in the biscuit, dy, called an ‘imperfect differential’. We use a bar over the top, dy̅, to show that this represents an actual tiny change, but we can’t say that it is the ‘d-of-y’ as we would have said in ordinary calculus. As there is no function, y, then we will not be able to use our usual mathematical weapons (differentiation, etc.). This case looks hopeless - how can it ever be incorporated into such a mathematical subject as the variational mechanics? Lagrange was not defeated, and with amazing ingenuity he devised a method of dealing with these imperfect differentials. But - enough already - we shall not be pursuing this further at this stage.43

We said that there were just three ways of taking an infinitesimal step but there is a fourth way - we can make an infinitesimal ‘whole path’ variation. We’ll discuss this in the next section.

3.7.3 The calculus of variations: stationary integral problems - a big step up in complexity

We have been concerned with determining the conditions when a function y is stationary (Section 3.7.2) but, beyond the usual ‘regularity’ requirements,44 we have said nothing about the function y itself. In problems of static equilibrium then y is a simple polynomial function (such as y = ax² + bx + c), but in more general mechanics, where motion is involved, then it turns out that y is generically a lot more complicated - it’s then a function-of-a-function-of-a-function. Specifically, y is then an integral, I, and this is a function of the integrand, F, where F is itself a function of f, which is itself a function of the independent variable, x:

y ≡ I = ∫ₐᵇ F(f(x), ḟ(x), x) dx (3.8)

(Also, as shown in this equation, one of the arguments of F is ḟ, which is a shorthand notation for the derivative, df/dx - the reason for its inclusion will be explained later on.) The reason why in dynamics we have to do with an integral, and a huge increase in complexity, will be explained in Chapter 6. For now, we concentrate solely on the mathematics. The problem will once again be, as in Section 3.7.2, to determine the virtual variation δy (now also called δI), and to see what conditions are required for it to equal zero. But what is δy when it comes to an integral? It will entail the variation of the ‘whole shape’ of a function between two end-points, a and b, rather than a displacement made at one ‘running’ point, x. We first look at some qualitative features of this sort of problem.

Extremum problems of this kind, where the stationarity of an integral is sought, occur in dynamics, and in general mechanics problems. We have met some cases already in Chapter 2: the brachystochrone curve; isoperimetric problems (for example, Dido’s quest to maximize the area)...

--- **脚注:** 41 However we can only do this to within a certain experimental precision.

42 The reason for insisting on these two directions is given in the main text, the paragraph after next.

43 If your appetite has been whetted, the method involves a technique known as ‘Lagrange multipliers’, Section 6.8.

44 y must be continuous, differentiable, and also finite and single-valued.

rea enclosed by a fixed strip of bullhide); Newton’s most streamlined solid; and even certain static problems (the equilibrium shape for a suspension bridge—the catenary). In all these cases we must determine the correct overall shape of some continuous function such as to make the integral, I, have a minimum or, more generally, a stationary value, δI = 0. Once again (as in Section 3.7.2, case (2)), we will use the technique of mathematical experimentation, but this time we will virtually ‘vary a function’ rather than virtually displace a variable.

What does it mean to ‘vary a function’? Looking back at equation (3.8), it seems that there are a number of ways in which the integral could be (virtually) altered: we could change any or all of F, f, f′, x, or the limits a or b. However, in fact, we ban all but one of these changes. First, it is in the nature of these problems that F is never altered, it is prescribed beforehand (in other words, F defines the very problem we are investigating and if we allow it to be changed we are, in effect, investigating a new problem). F might be the formula for an infinitesimal increment of time, ds/v; or the potential energy per unit length of hanging chain; or, in dynamics, as we shall find out in Chapter 6, it is the difference between the kinetic and potential energy functions.45 Second, we do not allow virtual changes in the independent variable, x. (Of course, x does actually change as we integrate from the limit x = a all the way to x = b, but there is never an introduced change, δx.) Talking of the limits, a and b, these also are fixed, and so is the value of f at these limits. So, what is left? The only thing we are allowed to change (to ‘vary’) is the function, f. Even f′ is not varied by us, it just changes consequentially as a result of the change in f.

Thus, here is yet another huge step up in complexity: instead of a ‘virtual displacement of a variable’ we have a ‘virtual variation of a function’. This variation is achieved by plucking out of the mathematical imagination an arbitrary function, φ(x), then scaling it by some ‘small’ arbitrary constant, ε, and adding the result to our starting function, f(x): variation of f f_var(x) = f(x) + εφ(x), a ≤ x ≤ b (3.9)

The variation can then be made infinitesimal by allowing ε to get arbitrarily close to zero. The conditions on φ(x) are that it must be continuous and differentiable, it must be ‘small’, and, at the integration limits x = a and x = b, it must be zero (in other words, the function is not varied at the ends of the integral). An example of a function, f(x), and some possible variations, f_var(x), is given in Figure 3.4. (Terminology and notation: a whole virtual path is known as a ‘variation of f(x)’ and is denoted f_var(x); the difference between f_var(x) and f(x) at a given x is sometimes called the ‘variation of f(x) at x’ and is denoted δf(x), in other words, δf(x) = εφ(x).)

The distinction between an actual differential, df, and a virtual variation, δf, must be borne in mind. While dx and δx are identical mathematically (Section 3.7.2), df and δf are utterly different mathematically. Because f is a function (that is, f = f(x)), then df is the usual ‘total differential’ that we are familiar with from ordinary calculus, and a finite df inescapably implies a finite actual displacement, dx, (see Figure 3.5). On the other hand, the virtual variation, δf, does not imply the virtual displacement, δx, but rather δf occurs at an ‘instantaneous’ value of x. This conforms to the rubric for these stationary integral problems—that a virtual displacement of the independent variable, δx, is not allowed.

The function, f(x)

a valid variation another valid variation an invalid variation Figure 3.4 The function, f(x), and some variations, f_var(x) (one dimension).

the function, f(x)

a variation, f_var(x)

δf(4.5)    dx    df δf(4.5) occurs exactly at x=4.5, whereas df occurs over an interval dx Figure 3.5 The distinction between df and δf (one dimension).

Now that we have established how our integral, I, is to be varied (by infinitesimal virtual variations in f), we can return to our overarching goal—to establish whether the integral is stationary with respect to these variations. In other words, does δI → 0 as δf(x) → 0? This is a mathematical problem of considerable difficulty, and it was solved in the eighteenth century first by Euler and then, more rigorously, by Lagrange. In honour of these great mathematicians, the solution is known as the Euler-Lagrange equation, and we shall simply present it rather than show how it was derived:46 The Euler-Lagrange Equation: d/dx (∂F/∂f′) – ∂F/∂f = 0 (3.10)

the solution to δI = δ∫_a^b F(f(x), f′(x), x) dx = 0 with respect to virtual variations, δf In the case of n dimensions we then have n functions, f_i, and n functions, f′_i, and instead of just one equation, we have a set of n simultaneous equations: The Euler-Lagrange Equations: d/dx (∂F/∂f′_i) – ∂F/∂f_i = 0 for i = 1,2,...,n (3.11)

the solution to: δI = δ∫_a^b F(f_1, f_2, ..., f_n; f′_1, f′_2, ..., f′_n; x) dx = 0 with respect to virtual variations, δf_1, δf_2, ..., δf_n There is still one loose end to tie up. At the beginning of this section we mentioned that one of the arguments of F is f′—why must this be so? (It would seem at first sight that as the function f is determined by solution of the Euler-Lagrange equation then f′ is also so-determined, and therefore f′ need not be specified separately as an argument?) Our frequent remark that the functions f and δf (and, by implication, F and δF) must be continuous has often been relegated to brackets and footnotes, but now we can see that this condition is crucial: there will be an infinite number of ways in which a path could be stationary and discontinuous, but only one way in which it could be stationary, satisfy the end-conditions, and still be continuous.47 In effect, the requirement of continuity is like lots of extra ‘boundary’ conditions all along the length of the path. The boundary conditions at the very ends of the varied path are provided by the upper and lower limits of the definite integral, however the ‘internal boundary conditions’ are provided by the function f′—the value of f′ at any given x ensures the continuity of f at that x. (This is mentioned again in Section 6.4, Chapter 6.)

We have been laying the mathematical groundwork—all will become clearer when the physical motivation for this mathematics is explained, and some worked examples are given (Chapter 6 and Appendix A6.1).

The Principle of Virtual Work

## 4.1 Introduction

Classical Mechanics deals with ‘statics’ (nothing is moving) and ‘dynamics’ (some parts are moving relative to other parts). We consider, in this chapter, the first of these.

If nothing is moving then the system is said to be in a state of static equilibrium. We have two methods of dealing with such static states, the method of Newtonian Mechanics, and the method known as the Principle of Virtual Work. Physicists have tended to use the first method, whereas engineers have used both methods, as appropriate. Thus the engineers are ahead of the physicists, showing the way for the last 150 years and more (the Principle of Virtual Work was first proposed by Johann Bernoulli in 1715 (see Chapter 2)).

There is a difficulty in comprehending these static states: how shall we know whether there are strong forces keeping a certain structure in balance—a Roman arch, a house of cards, taut cords meeting at a point—or whether the forces are weak, or even absent, and the various parts just happen to be adjacent to each other in space? Similarly, what is the evidence for the large amount of energy locked away in the still body of water in the reservoir of a hydroelectric power station, a column with a heavy weight on top, or a fully charged battery? Our instinctive response is to gently prod, shake, or tweak the system, trying to disturb it very slightly away from equilibrium. In this way, the forces and energies can reveal themselves. We shall find that this nudge to the system is pursued in a special way in the Principle of Virtual Work.

## 4.2 System of non-interacting particles

We start by considering a very simple scenario—a system made up just of forces and non-interacting particles. Particles are point masses, m_1, m_2, ..., that is, they have no extension and no internal structure (but they may have extra properties such as electric charge). Forces are applied externally, such as gravity, muscle strength, and so on. We seek to determine the magnitude of the forces necessary to achieve equilibrium.

Method 1, Newtonian Mechanics Consider that we have particles i = 1 to N, with position vectors, r_1, r_2, ..., r_N, acted upon by forces, F_1, F_2, ..., F_N respectively (the r_i and F_i are referred to the usual Cartesian axes (x, y, z)). To say that the system is in equilibrium is to say that the particles are not moving. But if nothing is moving then it is also true that nothing is accelerating; so, by Newton’s Second Law of Motion, there are no forces. Therefore we must have: Method 1, static equilibrium of a system of N non-interacting particles in Newtonian Mechanics F_1 = 0, F_2 = 0, ..., F_N = 0 (4.1)

This is a condition involving forces but what of the particles? And are there the same number of forces as particles? For answer, we note that: if there happens to be a force where there is no particle (the force acts in empty space somewhere) then this force is not relevant to the problem and can be ignored; if there happens to be a particle where there is no force then we can just as well say that there is a force but its magnitude is zero; and if there happen to be two or more forces acting at a given particle then the forces can be added to yield just one resultant force. On all counts (4.1) still holds and so, in all generality, the equilibrium condition for N non-interacting particles has N forces, one force acting at each particle, and each force is zero. It’s as simple as that.

Method 2, The Principle of Virtual Work The Principle of Virtual Work (P of VW) tackles the problem of static equilibrium in an entirely different way. The Principle first contrives a scenario in which each and every particle, i, simultaneously does an infinitesimal amount of virtual work, δw. Leavin g aside, for the moment, how this is contrived, and what 'virtual' means, note that 'work' is still defined, from Classical Mechanics, as the dot product of force and displacement. δω is therefore a scalar quantity, but one that can be positive or negative. ('Positive' when, along any given axis, the force and displacement vectors point the same way; 'negative' when, along any given axis, the force and displacement vectors point the opposite way.) The P of VW then asserts that the system will be in static equilibrium if, after summing these simultaneous contributions to virtual work, one contribution from each particle, the total virtual work is zero:

Method 2, static equilibrium of a system of N non-interacting particles in the Principle of Virtual Work

δω + δω + ... = δω = δωtotal = 0 (4.2)

1 2 i i=1 (cid:5)

In striking contrast to (4.1), forces are nowhere to be seen.

We now return to an explanation of what is virtual work. 'Work' is defined in the usual way as the 'work done by a particle acted upon by a force while the particle is displaced through a certain distance in a certain direction.' But Method 2 immediately presents us with a problem: in order to have finite contributions to work we need finite displacements but, at equilibrium, nothing is moving and so the displacements are all zero. Therefore, to rescue Method 2, we do something which at first sight appears like an act of intellectual prestidigitation - we invoke a small, hypothetical displacement, δr, one for each particle, i. This is the 'nudge' that was referred to at the end of the introduction. The symbol, δ, pronounced 'variation', reminds us that the displacements (and the consequent 'work done') are imagined, virtual, and form part of a purely mathematical experiment.

At first encounter this seems perplexing - why do we not actually, physically, tweak the system (say, use our finger to move a particle)? However, strange as it may seem, we shall find (Sections 4.5 and 4.9) that some virtual displacements cannot occur physically, and some physical displacements cannot occur virtually. We must simply accept the need for virtual displacements - imagined displacements that happen in an imagined mathematical landscape or 'space'. This 'space' is the 'configuration space' that was described in Chapter 3.

Conditions (4.1) and (4.2) appear utterly different, yet we may suspect that Methods 1 and 2 really boil down to the same thing. After all, work is the scalar product of force and displacement, and so if all the forces are zero then surely the work must also be zero, end of story? However,

this innocent line of reasoning turns out to be flawed. Methods 1 and 2 really are quite different, and for at least three reasons. For one thing, they concern totally different entities (Method 1 has to do with forces, Method 2 has to do with energy, specifically work), and for another, Method 1 involves lots of individual statements (F = 0, F = 0, ...) while Method 2 involves one grand statement which is a 1 2 sum. Finally, while Method 1 involves equating things to zero, Method 2 involves a mathematical procedure which goes beyond mere summing to zero and uses the variational calculus to carry out a 'test of flatness' or 'test of stationarity' (Chapter 3). We shall talk more about this later.

We would nevertheless like to bring out the resemblances between the two methods, and so we re-express (4.2) in terms of forces and displacements:

Static equilibrium in the Principle of Virtual Work, re-expressed F δr + F δr + ... = F δr = δωtotal = 0 (4.3)

1 1 2 2 i i · · · i=1 (cid:5)

The forces, F , F , ..., are external and have been supplied in the specification of the given problem. Despite these forces, the particles in 1 2 this example are 'free' (they don’t interact with each other, and are not constrained) and so each is free to be displaced in any direction. We can therefore choose the virtual displacement for each particle independently, and to be in any direction. So much for the direction but what of the magnitude of the displacement? We must understand that (4.3) is more than an equation, it is a 'test of stationarity' and therefore represents a limiting process. The sum must be zero in the limit as the magnitude of each displacement is reduced. The starting magnitude must be 'small' but it doesn’t matter what exactly it is (in the same way as, in differential calculus, we draw diminishing triangles on a curve in order to find the slope, but it doesn’t matter what size triangle we start with). So, for these independent particles, we can choose both the direction and (small) starting magnitude of the virtual displacements at random. Condition (4.3) is therefore a condensed version of the following infinite set of equations, each one corresponding to a different choice or set of virtual displacements:

F δr choice1 = 0 (4.4)

i · i i=1 (cid:5)

F δr choice2 = 0 (4.5)

i · i i=1 (cid:5)

F δr choice3 = 0 (4.6)

i · i i=1 (cid:5)

and so on.

The only way that this infinity of equations can be simultaneously satisfied is if all the forces are zero, F = 0, F = 0, ..., F = 0. We have 1 2 N returned to exactly the same result as the one derived from Method 1.

We see that Method 2, the Principle of Virtual Work, involves a much more complicated procedure in order to end up at exactly the same results as Method 1. Before explaining why this is justified, let’s check whether the Newtonian predictions are again reproduced by the P of VW when more complex equilibrium states are considered. Suppose we now allow for the particles to interact - to be bound together into a rigid body, for example.

## 4.3 Statics of a rigid body

What is the difference between a rigid body and a collection of particles? Lanczos poses the question most graphically: what is the difference between a sandstone rock and a pile of sand just happening to have exactly the same overall shape as the rock? He answers that we can try picking up 'the body' and moving it from one place to another (giving it a translation or a rotation). The rock will move as a whole, as a rigid body, whereas the sand-pile will disintegrate. This translation or rotation is a kind of physical nudge, but the body will only remain intact if the nudge is sufficiently gentle. Likewise, in applying the test of stationarity in the P of VW, we give the body a gentle virtual nudge. We now describe how this is achieved.

We can make the adjective 'gentle' more precise. The rock is rigid because there are internal forces (also called constraint, or reaction forces) between the particles, binding them together into a body. The virtual displacements will be sufficiently 'gentle' if they never go against these forces of reaction, and this will be the case if the body is always displaced (virtually) as a whole, and is never virtually squeezed, twisted, or stretched. This is guaranteed so long as we give every particle exactly the same virtual translation:

δr = δr for all particles i = 1 to N (4.7)

The resultant total virtual work due to these virtual translations is then:

N N F δr = δr F = δωtotal = 0 (4.8)

i i · · i=1 i=1 (cid:5) (cid:5)

The forces, F, are not the internal ones, but are the external forces that we seek to determine, and that ensure the equilibrium state. As δr is non-zero, (4.8) can only be satisfied if:

F = Fresultant = 0 (4.9)

i=1 (cid:5)

But this is just the standard result from Newtonian Mechanics: for equilibrium of a rigid body, the resultant external force must be zero.

A new development arises now that we are dealing with bodies rather than particles. A rigid body, having extension and having a shape, can be rotated.¹ This possibility brings in a new kind of virtual displacement - not just translations but also rotations. Again, the reaction forces must not come into (virtual) play, and this is assured by giving every particle (that is, every particle’s position vector, r) exactly the same virtual rotation about some common axis of rotation:

δθ = δθ for all particles i = 1 to N (4.10)

However, unlike (4.7), this universal rotation does still lead to different displacements, as these depend on the individual particle position vectors, as follows:

δr = δθ U r (4.11)

i i

¹ As a particle has no size then there is no evidence that it has been rotated. This is equivalent to saying that it cannot be rotated.

where U is a vector of unit length along the given axis of rotation. The virtual work of particle, i, due to the external force, F, acting at i, becomes:

i δω = F (δθ U r) = δθ U (r F) = δθ U M (4.12)² i i i i i i · × · × ·

where M = (r F) is known as the 'moment of the force' about the given axis of rotation. Therefore the total virtual work due to all particles is: i i

N N δωtotal = δθ U M = δθ U M (4.13)

i i · · i=1 i=1 (cid:5) (cid:5)

As δθ U is non-zero, the total virtual work can only be zero if:

M = Mresultant = 0 (4.14)

i=1 (cid:5)

which is the same as saying that U must be perpendicular to Mresultant. Again, this is the same as the result we expect from Newtonian Mechanics: for equilibrium of a rigid body, the resultant moment is zero.

## 4.4 A comparison between Newtonian Mechanics and the Principle of Virtual Work

The very simple scenarios in Sections 4.2 and 4.3 have been selected to demonstrate the complete equivalence of Newtonian Mechanics and the Principle of Virtual Work in these cases. It appears that the P of VW has served only to replicate Newtonian Mechanics, and at the cost of introducing obscure imaginary motions in a virtual space - but we should remember that the P of VW has arrived at these results, conditions (4.9) and (4.14), afresh and completely independently of Newtonian Mechanics. In order to bring out the new outlook and content of the P of VW we try a different tack: instead of introducing forces into (4.2) we introduce displacements into (4.1). Also, we consider a more general system in which particles can interact but are not necessarily bound into a rigid body. Each particle may be subject to an internal force, an external force, or both, in other words, each particle is acted upon by a net force, Fnet, which is the sum of the applied and constraint forces at i. (We shall in what follow use the terms 'applied' for 'external', and 'constraint' for 'internal'.) The Newtonian condition for equilibrium (Condition (4.1)) can then be written:

² We have used the result from vector algebra that a (b c) = b (c a).

· × · × Fnet = 0, Fnet = 0, ..., Fnet = 0 (4.15)

1 2 N

As the net force at each particle is zero, we are able to take its scalar product with any vector we like and still obtain zero. Exploiting this fact, we choose to take the scalar product of Fnet with whatever happens to be the virtual displacement at i. For this special choice-set, we arrive at:

(Fnet δr ) = 0, (F net δr ) = 0, ... (Fnet δr ) = 0 (4.16)

1 · 1 2 · 2 N · N

Adding lots of zeros together should still lead to zero, so we obtain: (Fnet δr )+(Fnet δr )+...+(Fnet δr ) = 0 (4.17)

1 · 1 2 · 2 N · N

Remembering that Fnet is made up from an external applied force, Fi appl, and an internal constraint force, Fcons, equation (4.17) becomes: (F appl +Fcons) δr + ...+(F appl +Fcons) δr =0 (4.18)

1 1 · 1 N N · N

But now, instead of considering everything on a particle-by-particle basis, we rather lump together all the Fi appl s, and lump together all the Fi cons s. In this way we arrive at: N N ∑(Fi appl δri)+ ∑(Fi cons δri) = 0 (4.19)

i=1 i=1

At this stage we introduce a brand new requirement, that the second term in (4.19), that is, the total virtual work of all the constraint forces, is zero: ∑(Fi cons δri) = 0 (4.20)

i=1

This is beautifully consistent: the total ‘constraint’ (for example, the ‘constraint’ of being a rigid body) has no internal movements within it, and so it also is a system in equilibrium, a mini-system to which the P of VW should apply.

As we still have equation (4.19) to be satisfied, along with (4.20), then it must be that the total virtual work of all the applied forces is also zero.

This, finally, is the P of VW as it is usually defined: ∑(Fi appl δri) = 0 (4.21)

i=1

Let us remind ourselves of (4.15), the Newtonian condition we started from: Fnet=0, Fnet=0, ..., Fnet=0 (4.22)

1 2 N

Comparing these two conditions, (4.21) and (4.22), we find that (4.21)

is making an utterly different claim to (4.22). In the P of VW there is just one zero condition, that condition is a sum, and constraint forces are conspicuous by their absence. Also, curiously, there is no longer a necessity for Newton’s Third Law of Motion (see Appendix A1.1) to be upheld (at the level of particle-particle interactions). This is because the sum in (4.21) means that the applied forces act as one system, there is no extra requirement for certain pairs of forces to cancel each other out. With the foreknowledge that physics contains many examples where Newton’s Third Law may be broken,3 there is every reason why the P of VW, rather than Newtonian Mechanics, will apply in these domains.

3 For example, the interaction between two electrons, one moving along a line at right angles to the motion of the other. See Feynman, Richard, The Feynman Lectures on Physics, Addison-Wesley, 1963, Volume II.

## 4.5 Virtual Displacements

We have talked much of forces and little about displacements but both occur in (4.21). The virtual displacements, as we have discussed above (Section 4.2, and 3.7.2) are displacements in an abstract space (configu- ration space), a space with axes that correspond to the degrees of freedom of our given problem. The ‘test of stationarity’ occurs at one point - the C-point - of this space. Although the virtual displacements are imagined this doesn’t mean we are free to imagine anything we like. We must follow some strict guidelines, as follows: How many virtual displacements are there?

The forces are given in the description of the problem, but the virtual displacements are chosen by us.4 They are chosen to occur wherever there is an applied force acting on a particle. If, by chance, we happen to do a virtual displacement where there isn’t a force, it won’t matter (it’s virtual work will be zero), but if there is an applied force acting on a particle somewhere and we don’t carry out a virtual displacement at this position then the ‘test of stationarity’ (the Principle of Virtual Work)

will fail, it won’t be ‘complete’.

When do the displacements occur?

The ‘test of stationarity’ is carried out at a test point, in other words, in an instant, that is to say, at one time. Therefore all the virtual displacements must happen simultaneously.

Where do the displacements occur?

Each virtual displacement, δri, must be located at the end of the respective vector, ri.5 What direction does the displacement have?

The direction of δri is arbitrary except that it must be ‘in harmony’ with any con- straints, which is the same thing as saying that it must be perpendicular to 4 In some advanced versions of the method of VW, the applied forces can be given a virtual variation instead of the displacements; we won’t be considering these versions.

5 The notation makes δri looks similar to ri whereas in fact they are quite different: δri is a displacement vector while ri is a position vector.

the reaction forces at i (see Section 4.8). Only in this way we can be sure that no virtual work will arise from these constraint or reaction forces.

Also, for any allowed direction, the virtual displacement could be +δr or –δr (the displacements are said to be ‘reversible’) and this ensures that the test point can be approached from the negative or positive side of any allowed direction. (See Appendix A3.1.)

What magnitude do the displacements have?

As mentioned before, we must appreciate that condition (4.21) is really a shorthand for a mathematical procedure (‘taking the limit’). For independent particles, each virtual displacement can have any starting magnitude, except that this magnitude must always be ‘small’ - as we can only examine a local region surrounding the test point. The ‘test of stationarity’ is then applied by simultaneously letting all the imagined displacements tend to zero-magnitude as the test point is approached.

If there are functional relations between the position vectors (relations given in advance in the description of the problem) then the virtual dis- placements will also have to satisfy these relations, as determined by the usual rules of differential calculus.6 How long do the displacements take?

As mentioned above, the ‘test of stationarity’ means that the displace- ments must happen simultaneously. They must also happen instantan- eously, that is, take no time to occur.7 As they are imagined rather than actual, this doesn’t pose a problem.

In summary, ‘virtuality’ means that the δri are ‘small’, happen simul- taneously, and do not cause a force, result from a force, or take any time to occur. Also, they can only be in directions that are ‘in harmony’ with any constraints and other ‘kinematical conditions’ that may pertain.

You may wonder why the displacements can depart from physicality as regards their duration, yet must bow to it as regards constraints and kinematical conditions? The answer is that, out of an infinity of pos- sible configuration spaces, we wish to investigate this one and not that one (that is, we wish to investigate the one that does correspond to our given system).

6 So, if, say, the given problem requires that r1 = (r2)3, then we must have δr1 = 3(r2)2δr2. Also, if, say, r1 = r2+r3, then δr1=δr2+δr3.

7 This is an example of virtual displacements which have no actual, physical, counterpart - mentioned in Method 2, Section 4.2.

## 4.6 The Principle of Virtual Work: Feynman’s

pivoting bar It will be easier to understand these abstract ideas if we use the P of VW to tackle a specific problem. We consider an example adapted from Feynman’s Lectures on Physics.8 A bar, 8 metres long, is supported on a fulcrum at one end (Figure 4.1). In the middle of the bar is a mass of 60kg, and at a distance of two metres from the support is a mass of 100kg. What value must the hanging mass, M, have in order that the bar is balanced (is in equilibrium)?

The three masses can be considered as ‘particles’, and the bar intro- duces a constraint or kinematical condition between these particles (assume that the mass of the bar itself is negligible, that it remains rigid while it pivots, and that there is no friction at the pivot or in the sliding of the pulley-cord). We imagine that M falls any arbitrary ‘small’ dis- tance, say, 4cm. The centre mass then rises 2cm, and the other mass rises 1cm. So we have virtual displacements –4cm, +2cm, and +1cm, and weights (applied forces) of MgN, 60gN, and 100gN, respectively (where ‘g’ is the magnitude of the acceleration due to gravity). Thus, the P of VW, (4.21), leads to:

## 4.7 Coordinates - an increase in generality

First we considered free particles, then particles constrained into a rigid body, then particles constrained any which way. Now we take yet another step toward increased generality, but this is not a small step, it is enormous, and will allow us to see the whole of physics in a new way. We will model the physical world employing not necessarily ‘particles’ but ‘things’; not ‘displacements’ but ‘motions’; not ‘applied forces’ but ‘applied generalized forces’. It is the far reach of the Principle of Virtual Work that gives us this licence; and as the crucial elements are now infinitesimal chunks of energy (condition (4.2)), so the crucial sub-elements are any quantities that combine together to yield energy.

It’s time to come clean; from the start of this chapter we have lulled you into a false sense of universality, and taken it for granted that the physical system is always reducible to forces, particles, and the position vectors of these particles. Also, we casually stated that the position vec- tors and forces were ‘referred to the usual Cartesian axes, x, y, and z’ (Section 4.2). But all the above assumptions are inessential and preju- dicial. The Cartesian coordinates are ‘rectangular’ (Chapter 3) but as soon as the physical system involves a rotation, a bend, a twist, spinning, orbiting, pivoting, spherical bodies, bubbles - anything curvy - then rect- angular coordinates are a poor choice, perhaps even an impossible one.

Although vectors offer such wonderful insights, and greatly facilitate the ease of solving problems such as ‘the equilibrium of taut cords meet- ing at a point’, ‘a swimmer swims diagonally across a uniformly flowing 9 In actual fact, the displacements are curved, being small arcs of circles traced out as the bar pivots.

river’, and so on Nevertheless, they lead to fiendish complications whenever curvy features are present.

Why didn’t The mechanics is ultimately built up from a framework of individual point-particles and forces, but often appears to avoid the need for internal forces by using whole constructs such as ‘rigid body’, ‘moment of inertia’, and so on. Also, the mechanics appears deceptively simple through familiarity (but remember, for example, the sheer variety of formulae needed for moment of inertia depending on whether the body is a sphere, spherical shell, cylindrical shell, rectangular parallelepiped, uniform slender rod, quarter circular rod, right circular cone, elliptic paraboloid, half torus, rectangular tetrahedron, and so on12).

Many of these techniques were developed by those geniuses of the eighteenth century, notably Leonhard Euler, and Daniel Bernoulli, and even earlier Newton had brilliantly demonstrated that the whole mass of the Earth could be said to act at the Earth’s centre (its ‘centre-of-mass’) as far as the Moon was concerned. These hard-won advances are now taken for granted, and we have forgotten that they contain many implicit assumptions, and that in most realistic cases the system can no longer be modelled as being made up of modular components like ‘point-particles’, ‘forces’, ‘central forces’, ‘normal reaction’, ‘transmissable force’, ‘forces transmitted infinitely fast’, ‘inextensible cord’, and so on. Then, Newtonian Mechanics fails to solve the problem. This comes as a shock – as we have been led to believe that Newtonian Mechanics fails only when the relativistic or quantum mechanics regimes are reached. Rather, we should realize how amazing it is that such simple elements (forces, point-particles, and accelerations) could ever have accounted correctly for so much.

12 Meriam J L and Kraige L G, Statics, Volume 1, Engineering Mechanics, 4th edition, John Wiley & Sons, Inc. (1998) Appendix D, Table D/4.

In summary, Newtonian Mechanics considers the infinity of particles, and the infinity of net forces, one by one, whereas the P of VW (by considering only virtual displacements/motions that are in harmony with the constraints, can thereby ignore these constraints and so) treats the whole body in one go.

## 4.9 Mechanics and geometry

We are witnessing a beguiling melding of geometry and physics. Already in Chapter 2, in Stevin’s ‘wreath of spheres’, we saw how the condition for equilibrium was guaranteed merely by a uniform draping (no gaps or bunching up) of a bead chain over the relevant surfaces; and in this chapter we have seen how geometric conditions (an object moves along a given curve, or on a given surface, and so on) is ultimately due to the presence of internal forces. Careful thinking and examination of many scenarios shows us even more: the virtual displacements must always be perpendicular to the reaction-forces. For example, in Feynman’s horizontal bar (see Section 4.6), while the displacement of each mass was vertical, in line with the applied force of gravity, yet the reaction-force acted along the length of the bar (preventing the masses from getting closer together or further apart – in other words, maintaining the rigidity of the bar). The displacements and the reaction-force were therefore at right-angles to each other.

A surprisingly tricky example is the case of a sliding block which is pushed across a table-top by a force, say, pushed by your finger (we ignore friction). The displacement of the block is anywhere on the surface whereas the reaction-force acts at right-angles to this surface preventing the block from burrowing down into the table. So far, this makes sense. But, hang on, there is also a reaction against your finger, from the block, and this reaction is in line with the block’s displacement. The trick is to appreciate that the block’s displacement due to the finger-push is an actual, not a virtual, displacement.13 We can hypothetically freeze the block (switch to a different reference frame) and get rid of the distraction of its actual motion. Then we realize that the finger can’t depress the block as if it were so much sponge-cake, as there is a reaction-force of the block against the finger. However, the finger is still allowed, infinitesimally, virtually, to move within the back face of the block, at right-angles to this reaction-force. This is a general result: for any virtual displacement, being ‘harmonious’ is the same thing as being in a direction perpendicular to the reaction forces.

13 We mentioned in Section 4.2, Method 2, how sometimes the actual physical displacement could not be chosen as the virtual displacement.

Optional: It is well known that at equilibrium the potential energy function, V, is not just stationary, it is at a minimum – in most cases. The P of VW cannot determine this, a further investigation is required. Why it is that V is usually at a minimum rather than a maximum will be explained later, in Chapter 6, Section 6.6.

## 4.10 More examples using the Principle of Virtual Work

(i) The ‘black box’

Of all the problems in Meriam and Kraige’s textbook, “Statics”,14 this simple set-up of connected pushrods is the most marvellous (see Figure 4.2). The pushrods, A and B, can slide in or out of a box. (They are capable only of linear motions but don’t need to be positioned in line with each other.) The pushrods are connected together by some series of reversible mechanical devices (racks and pinions, gears, hydraulic pistons, pulleys, levers, and so on) such that when rod A is pushed into the box then rod B gets pushed out, and when rod B is pushed into the box then rod A gets pushed out. We cannot see, hear, or in any other way detect the presence of these internal transmission mechanisms (the box is ‘black’), and we must assume that they act without friction or any other dissipation of energy. The question posed is: for every 1.0 unit of inward movement of pushrod A under the action of force, F₁, pushrod B moves outward from the box 0.25 units against the action of force, F₂. If F₁ = 100 N, determine the magnitude of F₂ for equilibrium (the state where the pushrods don’t move). We choose virtual displacements with directions as if pushrod A could drive B out of the box. Then the virtual work done by rod A is F₁ δr_A and is positive as the directions of F₁ and δr_A are the same (they are both directed into the box), while the virtual work done by rod B is F₂ δr_B and is negative as the directions of F₂ and δr_B are opposite (δr_B goes out of the box while F₂ is directed into the box). The total virtual work must be zero for equilibrium, and thus we must have F₁ δr_A = – F₂ δr_B or F₂ = 400.0 N.

14 Meriam J L and Kraige L G, Statics, Volume 1, Engineering Mechanics, 4th edition, John Wiley & Sons, Inc. (1998) page 449.

This problem is a marvel because it demonstrates an astounding fact – the problem is insoluble using Newtonian Mechanics.15

(ii) Knob and slider

This is another kind of ‘black box’ except that now the angular displacement of a knob, δθ, is linked to the linear displacement of a slider, δx. The knob is turned by applying a couple (‘turning force’) M (having units of Newton metres), and then the slider moves against a force, F (having units of Newtons). Assuming no dissipative losses within the ‘box’, for equilibrium the Principle of Virtual Work requires that M δθ + F δx = 0.

15 In Newtonian Mechanics we would be compelled to open up the box and assess the forces acting at each and every intersection.

(iii) Ladder leaning against a wall

What is the connection between the weight, W, and the horizontal friction force, F_horiz, for equilibrium of the ladder? We consider that the ladder is rigid and of uniform density – so its weight acts at its centre (halfway along its length, L). Also, we assume that the wall is smooth (frictionless) whereas there is contact friction from the floor (or else the ladder would fall down). If the top of the ladder has a vertical virtual displacement of δy then the bottom of the ladder will have a corresponding horizontal displacement of δx. This is because, although the displacements are virtual, they are still linked together by the constraint condition that the ladder’s length doesn’t change. That is, we have x² + y² = L, and so, differentiating, we must have 2x δx + 2y δy = 0, which implies δx = –(y/x) δy. Now, by similar triangles, when the top of the ladder falls through δy, the halfway point falls through δy/2. By the Principle of Virtual Work, the total virtual work due to the weight and the friction forces sums to zero: (W δy/2) + (– F_horiz δx) = 0. (W and δy are in the same direction and so the work due to the weight is positive; F_horiz and δx are in opposite directions and so the work due to friction is negative.) This means that W = 2 F_horiz y/x = 2 F_horiz tanθ, and therefore the final condition for equilibrium of the ladder is: θ = arctan(W/2F_horiz). (The analysis uses magnitudes only.)

Note that as δy and δx are along the wall and floor, respectively, then we have not needed to input the (perpendicular) reaction forces at the wall or against the floor. Note also that the frictional force is that due to static friction – so there are no actual displacements of the ladder; the Principle of Virtual Work must be used.

(iv) Two identical springs connected to a mass

The Newtonian method easily gives the condition for equilibrium: F₁ = – F₂. In the method of VW we have: – F₁ . δx + F₂ . –δx = 0. The displacement, δx, cancels out and then we are left with exactly the same condition as before, F₁ = – F₂. We see that the virtual work contributions are equal even while one spring is being extended and the other is being compressed – in other words, we learn that there is no essential difference between extending or compressing a spring (a fact which is a source of wonderment). It’s the same in Newtonian Mechanics (there’s no difference between extending or compressing a spring, within the spring’s elastic limit) but this similarity now arises for a different reason – because of the postulate that each spring obeys Hooke’s Law.

(v) A spring loaded with a weight

How much must a spring be compressed in order to balance the weight of a stone? (Assume the spring’s weight can be ignored.) The spring’s stiffness is k, its displacement is δx, the stone has mass, m, and the gravitational acceleration is g. We can consider just magnitudes as the problem is in one dimension (vertical). At equilibrium, balancing forces we have: mg = k δx, whereas balancing energies we have: gravitational energy, mg δx = stored spring energy, ½ k (δx)². But this implies that mg = ½ k δx, which is half what it was before. What has gone wrong? (You may want to cover up the text and think about this for a while before reading on.) The mistake was that In the energy-analysis, we did not approach the equilibrium state gradually. In reality, a displaced spring will not return to equilibrium straight away but will overshoot repeatedly, lose energy by dissipation, and only gradually attain equilibrium. This is curious: we are used to so many textbook problems in which we are told to neglect air-resistance, friction, and so on, but here is a problem where now ignoring dissipative effects leads to the wrong answer. This mistake crept in because we made a false identity between the actual displacement of the spring down to the equilibrium state, and the virtual displacement, δx, of the end of the spring once the equilibrium state had already been achieved.

Both (iv) and (v) are showing that, while the Newtonian method gives us a condition on the exact equilibrium position, the method of VW gives us something more, a condition on this exact position and also on the neighbourhood infinitesimally close to equilibrium.

(vi) Soap bubble The soap bubble has a higher pressure on the inside (let's call the pressure difference, ΔP) and so it would like to expand, but the surface tension makes it want to contract. Imagine a virtual increase in radius, δr, leading to a virtual volume increase, δV = 4πr²δr, and a virtual increase in surface area, δA = 8πrδr. The virtual work due to the pressure difference is –ΔPδV = –ΔP4πr²δr, and due to the surface tension is, 8γπrδr (where γ is the surface tension of the soap film, a measure of its stored energy per unit area). In fact, there are two surfaces (inner and outer surfaces of the film) and so for equilibrium we must have: –ΔP4πr²δr + 2·8γπrδr = 0. Therefore, a bubble of radius, r, will be stable so long as ΔP = 4γ/r.

(vii) The parallel-plate capacitor This is adapted from Feynman's Lectures on Physics, Vol II, Chapter 8. The spacing between the capacitor plates is increased virtually by δz, and the mechanical virtual work to do this is Fδz where F is the force between the plates. The virtual change in the capacitor's energy is δU = 1/2 Q²δ(1/C) = – 1/2 Q²δC where C is the capacitance and Q is the stored charge (it is assumed that Q has been kept constant). At equilibrium, the P of VW requires: Fδz = – 1/2 Q²δC (4.24)

The force is the electrical force of attraction between the plates, but from the P of VW we are learning that F is not affected by the detailed distribution of charge; everything is taken care of by the values of Q and C.

## 4.11 Lanczos's Postulate A

A marvellous leap forward in conceptual understanding was brought in by Lanczos, in his re-statement of the Principle of Virtual Work.¹⁶ The usual practice¹⁷ is to define the P of VW as we stated it before in Section 4.4, Σ (F_applied · δr) = 0 (4.25)

This sum is the first term in equation (4.19). Lanczos, on the other hand, homes in on the second term of equation (4.19), and defines the P of VW as: Σ (F_cons · δr) = 0 (4.26)

He then comments that constraint-forces are really the same thing as reaction-forces (we have explained this in Section 4.8) and so re-expresses the P of VW as: Σ (F_reaction · δr) = 0 (4.27)

Finally, he puts this in words, and emphasizes that it is a postulate by calling it Postulate A: ¹⁶ Lanczos, page 76.

¹⁷ See for example, Goldstein H, Classical Mechanics, Addison-Wesley (1980).

Lanczos's Postulate A "The virtual work of the forces of reaction is always zero for any virtual displacement which is in harmony with the given kinematic constraints."

But what has been the point of all this wordplay? I surmise that Lanczos's motivations were as follows. The applied forces (squashed spring, finger-push, gravity, electrostatic attraction, and so on) are usually given beforehand, supplied by the problem, and are in the form of scalar mathematical functions. Likewise, the overall kinematical conditions are usually predetermined and in the form of mathematical functions. The reaction forces, by contrast, are consequential—they are, as their name suggests, reactive, responsive, and they are ultimately microscopic in origin, and usually 'polygenic', that is, arising from many sources, and therefore not defined by a scalar mathematical function. Moreover, these reaction forces act 'cooperatively', as a system; and so it is from these forces that we obtain the most physical insight. Also, the bald statement of equation (4.27) does not remind us that this is a mathematical procedure that involves 'taking the limit'; and, crucially, that the δr must be only in directions allowed by the constraint and kinematic conditions. This essential requirement is brought out by the words 'in harmony with'. Finally, Lanczos is mindful to emphasize that the P of VW is a postulate, and does not come out of Newton's vector-force mechanics. But perhaps the most decisive reason for Lanczos to put the Principle of Virtual Work into words is that, as Postulate A, it will lead into the whole of the rest of mechanics (the variational method as applied to both statics and dynamics), and is therefore of astounding universality: "Postulate A is actually the only postulate of analytical mechanics, and is thus of fundamental importance."¹⁸

## 4.12 Concluding Remarks

There are some questions that we're not allowed to ask: Why does the P of VW work? Answer—we don't know, it just does.

How do the forces-of-reaction act cooperatively? Answer—we don't know, they just do.

¹⁸ Lanczos, page 76.

How can a test in a fictitious space tell us anything about the real world? We don't know, but it happens also in countless other circumstances. Consider the statistic, "an average family of 2.2 children"; evidently there can never be a family of this size but the statistic may still serve as a useful criterion. Also consider the example of the hypothetical money-transfers postulated by a financier in a 'test of portfolio value'.¹⁹ The money-transfers are subject to certain fees, interest rates, and exchange rates, but in order to actually buy and sell shares, or transfer money between accounts, some actual time is required. During this time, the financial conditions may change—and so the 'test of portfolio value' occurs in a virtual space.

But this is only half the answer. The utility of using a virtual space is that it can provide an absolute benchmark in a way that no actual physical space could ever do. This absoluteness and invariance of the results in the abstract test space is what comes about in the branch of mathematics known as 'differential geometry' (which used to be called 'absolute geometry'). The results are the same irrespective of what coordinates have been chosen or how the system has been modelled. We shall find that this remarkable invariance is a feature of the whole of Variational Mechanics (the P of VW, Principle of Least Action, Lagrangian Mechanics, and Hamiltonian Mechanics).

An enormous advantage of using the Principle of Virtual Work, as shown in the Examples, Section 4.10, is that we do not need to know the internal forces, the reaction forces, or the forces of constraint. However, a disadvantage of the P of VW is that when, on occasion, the applied force is not given in the form of a scalar mathematical function (for example, the applied force actually is a friction-force) then mathematical methods—the Variational Mechanics—cannot be used. On the other hand, as Lanczos notes,²⁰ given that ultimately all dissipative forces are microscopic in origin, with an appropriate mathematical form derivable from quantum theory, then ultimately it should be possible to apply the variational methods across the whole of physics.

Now the fact that the P of VW yields absolute answers—that's mathematics, but the fact that it's work that's minimized as opposed to some other quantity—that's physics. The innumerable cases where the P of VW succeeds and Newtonian Mechanics fails shows us that it is indeed work rather than force that is pre-eminent. In problems of exceptional simplicity, described in rectangular coordinates, it would be a mistake not to use Newtonian methods and benefit from the physically intuitive forces, but we must always remember that "force is a secondary quantity derived from... work."²¹ As Lanczos puts it: "we are inclined to believe that force is something primitive and irreducible, [however]... it is not the force but the work done by the force which is of primary importance."²² This is the main reason for using the Principle of Virtual Work: it is abstract, intuitively opaque, and mathematically complicated, but it is the way the physical world really is.

¹⁹ Murray Peake, private communication.

²⁰ Lanczos, Introduction, page xxv.

²¹ Lanczos, page 27.

²² Lanczos, page 27, edited and with italics added.

5 D'Alembert's Principle

## 5.1 Introduction

In the Principle of Virtual Work (the P of VW, Chapter 4) we have a method for analysing the condition known as static equilibrium or 'statics'. In this chapter we widen the scope to include 'dynamics'—mechanical scenarios in which there is motion between the parts of a system. Motion appears antithetical to statics and yet, in d'Alembert's Principle, we will discover a brilliant strategy for treating these dynamic cases; they will be treated, once again, as problems of 'equilibrium'. In essence, d'Alembert's Principle proclaims that the very motions are exactly such as to bring the system, instant by instant, back to 'equilibrium'—an equilibrium of a new, dynamic kind. The Principle relies on one radical new idea, d'Alembert's "stroke of genius:"¹ it is that a mass-in-accelerated-motion counts as a force. Previously, we had only Newtonian-type forces (cohesive, tensional, gravitational, electrical, magnetic), and these are all forces emanating from some source or other (a gravitating mass, an electric charge, a magnet, and so on). Now, with d'Alembert, we introduce a totally new type of force—a mass, merely by virtue of its motion, can act as a force. With hindsight, we see that this must be so—if 'motions' can counteract forces, then 'motions' must be forces. D'Alembert's programme is then to add this new category of force to the familiar applied-and constraint-forces, and apply the Principle of Virtual Work in the usual way.

D'Alembert's new force, called the force-of-inertia, or 'inertial force', occurs wherever there is a mass-in-accelerated-motion. A mass that is moving but not accelerating does not count as a force, and a geometric point that is accelerating but is massless (such as the geometric point of intersection between two accelerating rods) does not count as a force. Also, it is of no consequence to ask how the mass-in-accelerated-motion 1 Lanczos, page 88.

The Lazy Universe. Jennifer Coopersmith, Oxford University Press (2017).

© Jennifer Coopersmith. DOI 10.1093/acprof:oso/9780198743040.001.0001

D’Alembert’s Principle

gets to be accelerating—it could be subject to a force (such as an applied force), or it could be viewed from a reference frame that is accelerating, or a mixture of these. Howsoever it originates, the inertial force—let’s call it I — has all the usual attributes of a force: it has magnitude and direction, and it adds and ‘multiplies’ in the usual vectorial ways. The inertial force may therefore be added to the other forces, and then the Principle of Virtual Work may be employed.

Let us see how this happens. We consider a mechanical system composed of N particles (i = 1 to N) of mass, m, position vector, r, subject to applied forces, F appl, and/or constraint forces, F cons. From Section 4.8, Chapter 4, we remember that the applied- and constraint-forces have very different provenances: the applied forces are described by mathematical functions, specified beforehand in the given problem (for example, gravity follows an ‘inverse square law’), whereas the constraint forces (also called internal forces or reaction forces) are generally unknown and not expressible as a mathematical function (what is the force between particles in a taut cord, or in a rigid body, and so on?). Despite these different origins, we add together the applied- and constraint-forces acting on a given particle, and call this sum F net. Now, in the usual way (that is, in accordance with Newton’s Second Law of Motion), F net acting on the mass, m, causes it to accelerate, and so we must have F net = ma. But, by d’Alembert’s “stroke of genius”, this massy acceleration, in and of itself, constitutes a force. Even more than that, by postulate it constitutes a reactive force, a force that always opposes F net. Therefore, we define the inertial force, I, as being in the reverse direction to F net, that is, in the reverse direction to the acceleration:

Inertial force defined as: I = –F net = –ma (5.1)

Now the total force at i is the sum of I and F net; we call this the ‘effective force’, F eff:

F eff = F net + I for particle i (5.2)

Thus for N particles we end up with a system of forces, F eff_1, F eff_2, ..., F eff_N, and, by d’Alembert, we seek an equilibrium condition between these forces, even for this dynamics (non-statics) scenario.

This seems very nice until we realize with some surprise that, by equations (5.1) and (5.2), the F eff are all identically zero: F eff_1 = 0, F eff_2 = 0, ..., F eff_N = 0. Nevertheless, we are free to ‘multiply’ each zero F eff by a virtual displacement, δr, and we can be assured that each ‘product’, F eff · δr, will also be identically zero. We can then sum these zeros together and, of course, end up with zero:

∑ (F eff · δr) = 0 (5.3)

i=1 to N

While the correctness of this equation is not in doubt, the utility of it is unclear. For one thing, we still don’t know what the F eff actually are (we know that they’re identically zero, but we don’t know what is being equated to zero); we have been supplied with the applied forces, and we seek to determine the accelerations (the ones that will lead to ‘equilibrium’), but we are stymied by our lack of knowledge of the constraint-forces. Nevertheless, we press on, and try decomposing each F eff into its constituent force-types, that is, applied, constraint, and inertial forces. Equation (5.3) then becomes:

∑ ( (F appl + F cons + I) · δr ) = 0 (5.4)

i=1 to N

At this stage we do some rearranging of the three terms within the bracket—by exploiting the well-known rules of arithmetic. Thus, using the commutative and associative laws, we may group the threesome into (F appl + F cons) + I, F appl + (F cons + I), or (F appl + I) + F cons. Choosing the last one and using the distributive law, (5.4) becomes:

∑ ( (F appl + I) · δr ) + ∑ ( (F cons) · δr ) = 0 (5.5)

i=1 to N                      i=1 to N

At last, we have made some progress—we have herded all the troublesome (that is, unknown) constraint-forces into one group. The way forward is now clear: provided we insist that all the virtual displacements are in conformity with (in ‘harmony’ with) these constraint-forces, then we can be assured that the constraint-forces will do no virtual work. (This has been explained in Section 4.9, Chapter 4.) The constraint-forces, separately from all the other forces, will then make up a sub-system in equilibrium:

∑ ( (F cons) · δr ) = 0 (5.6)

i=1 to N

This saves us—it is simply unnecessary to know what the constraint forces are (their contribution to virtual work is zero). But, as we still require that the total virtual work from all sources equals zero (equation (5.5)), then it must be that the applied and inertial forces, taken together, also form a sub-system in equilibrium (their total virtual work must also be zero). This, finally, is what is conventionally referred to as d’Alembert’s Principle:

D’Alembert’s Principle, standard formulation ∑ ( (F appl + I) · δr ) = ∑ ( (F – ma) · δr ) = 0 (5.7)

i=1 to N                    i=1 to N

Note that although the sum goes from 1 to N, there is not necessarily an applied force at every i (there could be an accelerating mass-point even where the applied force happens to be zero).

There is yet one more change in nomenclature that we can introduce. The bracket (F appl – ma) is equivalent to one resultant force at i, and we can name this resultant force as we choose. Let us call it the ‘dynamics force’, F dyn, as we reach an equilibrium of a new dynamic kind, that is, an equilibrium where accelerations occur. We can then rewrite (5.7) finally as:

D’Alembert’s Principle ∑ ( F dyn · δr ) = 0 (5.8)

i=1 to N

This is exactly the same as the (standard definition of) the Principle of Virtual Work, see (4.21), as long as we pay no attention to the different naming conventions (F appl occurs in the P of VW, F dyn occurs in d’Alembert’s Principle)—but then what’s in a name?

Et voilà—dynamics has been reduced to statics. Well, almost; there is a difference between statics and dynamics, and this goes deeper than the mere statement of the Principle (definition (4.21) as opposed to definition (5.8)); the difference lies entirely in the solutions to (4.21) and to (5.8), in other words, the final equations are not the same. In statics we end up with statical relations (a weight might have to be located at a certain distance along a beam, a taut cord located at a certain angle, a weight squashes a spring to just such an extent, and so on) whereas in dynamics the Principle determines the accelerations of particles, and then if we wish to know how the positions of these particles change with time we will have to go on to solve the appropriate (2nd order) differential equations of motion.

Despite our success in combining both statics and dynamics into one Principle, there is much that is perplexing and disturbing about our ‘derivation’² (equations (5.1) to (5.8): naming, renaming, and shuffling packets of zero...). We have the feeling of whipping up a soufflé with no eggs, and, to compensate for the absence of eggs, whipping faster and faster. Before we return to this, it will help to examine a worked example.

## 5.2 A worked example

We provide a high-school physics example³ to show how d’Alembert’s Principle works in practice. A mass, m_1, slides across a table-top and is joined, by a rope going over a pulley, to another mass, m_2, which is falling under gravity (Figure 5.1 a). We make all the usual idealizations: m_1 slides without friction, the rope is taut and inextensible, there is no friction at the pulley, and the masses of the rope and pulley can be ignored. In fact, we can idealize the whole experimental arrangement as a ‘black box’ with m_1 approaching, m_2 receding, plus appropriate forces (Figure 5.1 b) (cf. problem (i) Section 4.10, Chapter 4).

The virtual displacements of m_1 and m_2 are always along the length of the rope (they’re ‘harmonious’). Also, as the rope-length is fixed, then this is a constraint which makes the motions of m_1 and m_2 not independent of each other, and we end up with δr_2 = δr_1, and a_2 = a_1 for the accelerations. From d’Alembert’s Principle, (5.7), we obtain: (F appl_1 + I_1) · δr_1 + (F appl_2 + I_2) · δr_2 = 0. Substituting δr_2 for δr_1, and a_2 for a_1 or a, and setting m_2 g = W = F appl_2, we find: (0 – m_1 a) · δr_1 + (m_2 g – m_2 a) · δr_2 = 0.

² The definition (5.8) was given so as to emphasize the identicality of d’Alembert’s Principle with the Principle of Virtual Work. From now on, we shall always use the definition of d’Alembert’s Principle as given in (5.7).

³ Year 12 VCE physics homework, Bendigo Senior Secondary College, 2013.

Figure 5.1 Connected masses a) “Half Atwood” version b) “Black box” version.

T I_1 δr_1 m_1 1 ‘black box’ δr_1 m_2 m_2 W_2 W_2

Cancelling δr_1 and rearranging, we arrive at the standard solution: a = m_2 g / (m_1 + m_2). Note that we have not needed to calculate the tension of the rope as this is a constraint force and does no virtual work (but in the method of Newtonian Mechanics we would need to determine the tension, or know this beforehand). Even more interesting is the role played by the mass, m_1. It undergoes an acceleration and therefore introduces an inertial force, I_1 (in the reverse direction to this acceleration), but this inertial force does not occur in tandem with any applied force. Rather, I_1 exists because of the mere fact of m_1’s acceleration, and we end up with the curious result that I_1 is the sole influence of m_1 on m_2—the (gravitational) weight of m_1, and its force-of-attachment to the rope, are both irrelevant as far as m_2 is concerned (provided that m_1 does indeed remain attached to the rope⁴). This is evidence that the inertial force truly exists, and is just like any other force.

## 5.3 Against intuition?

We return now to the question that we left dangling at the end of Section 5.1, and to other counter-intuitive aspects of d’Alembert’s Principle.

If the ‘derivation’ of d’Alembert’s Principle (equations (5.1) through to (5.8)) arose out of nothing more than the renaming and regrouping of packets of zero then this would indeed be paradoxical; however, the paradox is resolved when we appreciate that new knowledge has entered into the problem. (This is reminiscent of a well-known ‘paradox’ in probability—the tale of the three caskets, or the Monty Hall problem.⁵) Specifically, in equation (5.6) we have introduced an extra postulate (asserting that

⁴ As with all methods in the Variational Mechanics, d’Alembert’s Principle only works for sufficiently small virtual displacements leading to sufficiently small effects.

The virtual work of the constraint forces is zero, and this brings in the new knowledge that the motions of the mass-points are dependent on each other, and may even be tied together into 'super-structures' (wheel, lever, inclined plane, and so on). Extra knowledge has also been brought in by the requirement that the virtual displacements can't be in arbitrary directions but must be in harmony with these super-structures (and with any other kinematic conditions that may apply).

What about if there are no constraints, does d'Alembert's method then reduce to Newtonian Mechanics? Not necessarily - although it is true that the simpler the system is, the less is the difference between the methods, and the less apparent is the advantage of using d'Alembert's Principle. Consider the very simplest case: one particle, one applied force, and no constraints. We then have F = ma (from Newton's Second Law of Motion), and F - ma = 0 (from d'Alembert's Principle, (equation (5.7), after superscripts and subscripts have dropped away, and δr cancels out). It seems as if d'Alembert's Principle has offered nothing more than a trite rearrangement of Newton's Second Law. However Newton and d'Alembert are really posing utterly different questions. Newton asks - what is the motion of a particle given that the applied force is F? D'Alembert asks - what is the condition for equilibrium when there is a collection of forces? He finds that the condition is (forces) = 0 where it just so happens that the forces are 'F' and '–ma'. The wording is telling: Newton refers to 'a particle', in other words, to one particle; d'Alembert refers to a 'collection of forces', in other words to a whole system. But the differences go even deeper than this: Newton's Second Law is an equation in vector algebra, while d'Alembert's (forces) = 0 is a shorthand for a principle in the variational calculus: it is only true 'in the limit', and the virtual variations must be chosen wisely.

5 An ancient king needs to find a husband for the princess. The king has three identical caskets. He hides treasure in one of them and leaves the other two empty. Furthermore, he makes sure that no one but he knows which casket contains the treasure. In one go, the successful suitor must choose the casket containing the treasure. One day a suitor whom the King especially likes arrives at the palace. This suitor chooses a casket but before he gets to it the King quickly opens one of the other caskets, revealing emptiness. The King then gives the suitor the option of changing his original choice. The 'paradoxical' question is: in order to maximize his chance of winning the princess's hand in marriage, should the suitor change his choice or stay with his initial choice? This seems like a 'no-brainer' (of course the king's intervention won't change the odds) until we realize that the king is introducing extra knowledge into the problem...

The elemental system, 'one particle, one force', is so simple to state and easy to visualize that it leads us to suppose that scenarios of any degree of complexity can always be built up out of these basic elements. But this is not so, and the pathological simplicity has led us to false expectations. It is an example of the dictum "exceptionally simple cases make bad physical intuition"6 (in contrast to the lawyers' dictum "hard cases make bad law").

There are other counter-intuitive aspects of d'Alembert's Principle. The fact that the zero condition in (5.7) involves a sum allows for two surprising possibilities. First, it is possible to have some terms where F_appl != ma. There is no contradiction with Newton's Second Law as the ma_i are consequent upon the net force, F_net, they are not generated by just the applied force, F_appl. (Typically, the applied forces will exist at just a few mass-points, whereas the inertial forces will occur at every i, that is, wherever there is a mass in accelerated motion.) Second, and more alarming, it may occur that the interaction force (a genre of constraint force) between one particle and another particle is not 'equal and opposite', that is, there is nothing to prohibit F_int_ij != F_int_ji. This means that Newton's Third Law of Motion has failed. There is ample experimental confirmation of this7 - but note that the failure occurs only at this 'microscopic' level, the level of interacting particles: overall, at the 'whole-system' level, Newton's Third Law does still always apply.

There is yet one more aspect that is against our intuition. We have said that F_net leads to the massy accelerations, ma, but this doesn't rule out the possibility of these ma_i being generated in a totally different way (even when F_net is zero): the massy accelerations can occur merely as a consequence of an accelerating reference frame. But this then means that inertial forces can occur merely as a consequence of accelerations. This is very non-Newtonian and so will bring in some very non-Newtonian outcomes which we shall now investigate.

6 The author invented this dictum and used it first in a slightly different context; see Coopersmith, EtSC, Chapter 18.

7 Famously, this occurs in electrodynamics, such as the interaction between two electrons, with one electron approaching at right angles to the path of the other electron.

## 5.4 'Fictitious forces'

5.4.1 Introduction and examples

Let us generalize from the 'pathologically' simple scenario of just one particle and one force, and include the possibility of many particles, and of constraint or internal forces - is our system now of the most general kind? No, there is yet one more generalization we can make: we can remove the Newtonian prohibition against accelerating reference frames. We give a qualitative account of the consequences of allowing such accelerating reference frames (see Figures 5.2a to 5.2e).

Consider a system seen simultaneously from a reference frame that has no acceleration, REF, and from a reference frame that is accelerating, REF_acc. We will find that particles that were stationary in REF will be accelerating in REF_acc; and, per contra, there may be particles that were accelerating in REF and are no longer accelerating in REF_acc. Now, according to d'Alembert, a mass that accelerates constitutes a force. So, merely dependent on the reference frame, a force could come into existence which didn't exist beforehand. The consequences are not innocent, a force is not a tamething (applied to a person, it could make them feel nauseous, lose their balance, or tear them limb from limb). Such forces have in the past been called 'fictitious forces' - a misnomer, as these forces are every bit as real as applied- and constraint-forces, and their existence has been corroborated in countless experiments. (For example, the 'fictitious forces' associated with a rotating reference frame are the well-known centrifugal, and Coriolis forces8).

Let's look at some examples. Imagine that you are in a hotel room (a one-room cabin) with the window-shutters closed, in an armchair against the wall (Figure 5.2a). Unbeknownst to you, some prankster has mounted the whole cabin, at its centre, onto a strong bearing with rotary motor attached. The prankster turns the motor on and the room starts to spin (Figure 5.2b). Let's imagine that it spins exceptionally smoothly and quietly. What will you notice? You may feel a bit sick and you'll feel yourself being pushed against the chair-back.9 The hanging lamp near your chair gets tugged toward the outside wall. Also, some marbles on the floor suddenly start to move toward the edges of the room. They start rolling, radially outward, but they also feel, in addition, a sideways push, and so pursue a curved path toward the walls.

8 There are also the less well-known 'Euler forces' associated with a frame rotating non-uniformly, see Lanczos, page 105.

9 The faster the spin-rate, the greater your distance from the spin-axis, and the greater your mass, the more strongly you'll feel pinned to the chair.

You exchange stiff words with the management, switch to a new cabin, and promptly fall into a deep sleep. When you wake up later, you are relieved to find that everything is as usual, and you amuse yourself playing with the marbles, having a game of darts, and watching the goldfish in the goldfish-bowl. Everything appears utterly normal until you open the shutters and see - nothing. The view has disappeared and all you can see is a blue planet, far away. Room service (!?) informs you that you are now in Outer Space, on a rocket travelling dead straight and accelerating smoothly at 9.81 metres per second per second, (the engines are under the floor), and, not to worry, you have all the necessary oxygen, cabin pressure, supplies, shielding, and suchlike.

Your adventure is not over yet: you suddenly notice that every loose object in the room starts to accelerate linearly and gently toward the ceiling. This lasts for some minutes, gradually tailing off, until you notice that you feel weightless and see some marbles hanging motionless in mid-air (you are still on your chair, which is bolted to the floor, but you must now hold onto it). Room service informs you that you are still in Outer Space, but the rocket engines have been turned off. You enjoy the sensation of weightlessness, pushing off from the walls and doing somersaults with ease. Exhausted, you doze off in the chair again, (buckling yourself in). When you awake, you continue to feel weightless and are just about to indulge in some more acrobatics, when you look out the window and notice with horror that the Earth is close by and you are plummeting down toward it (that is, you're in free-fall).

Before you crash to your death, you just have time to ponder on the wisdom of d'Alembert: from within your room you feel only the combined force, (F_appl + I), and there is no way for you to distinguish between the effects due to an externally applied force and the effects due to your acceleration - in other words, F_appl and I are completely indistinguishable.

Now, if it so happens that the acceleration of your reference frame satisfies two conditions - it is in a straight line, and its magnitude doesn't change - then the 'fictitious' force in this special case is indistinguishable from a particular kind of external force - the one known as gravity.10 This was Einstein's celebrated Equivalence Principle. D'Alembert's Principle is more general inasmuch as the external force doesn't have to be gravity, but the Equivalence Principle is more general inasmuch as it applies not only to mechanics (bodies in motion) but to any physical effect whatsoever (heating, electricity, radioactivity, chemical action, and so on). In other words, all these effects will be unaltered when viewed from a reference frame

10 (for a sufficiently small room and short timescale).

that has zero acceleration and includes a gravitational field, or has a constant linear acceleration and does not include a gravitational field. Einstein subsequently generalized the Equivalence Principle in his landmark Principle of General Relativity: in a closed system, no physics experiment, of any kind, can distinguish between reference frames having any kind of motion (zero acceleration, uniform acceleration, or non-uniform acceleration¹¹).

This is all completely contrary to Newtonian Mechanics. Newton makes the distinction between a free body (there are no forces acting on it), and one that is subject to a force. By contrast, d’Alembert, Einstein, and modern physics, all make a distinction between a constrained body (moving only within a given surface, tied to a cord, and so on), and an unconstrained body-whether or not there may additionally be exter- nal influences. The importance of force is now downplayed, and we sometimes find (for example, in modern field theory) that it disappears altogether.

5.4.2 Critique, and some historic examples

One may try the objection that scenarios (a) and (c), and again (d) and (e), (Figure 5.2) do not have to yield the same outcomes as they are not identical (rocket engines are on and off, the Earth is near or far). This is true but, first, d’Alembert’s Principle, and the Principle of General Relativity, do not deny that F and I can be distinguished if you look out- side the cabin (that is, look outside the system, look at ‘the view’), and second, these Principles don’t prohibit identical outcomes for different scenarios, they only prohibit different outcomes for identical scenarios.

Let’s nevertheless, make things simpler by considering just one¹² scenario (which must, presumably, be identical to itself!) as seen from different view-points. For example, consider the Pluto-Charon system (and make the approximation that Pluto and Charon are perfectly rigid bodies travelling in circular orbits), and then sit the origin of the ref- erence frame: (a) on Pluto, (b) on Charon, and (c) at the centre-of-mass of the whole system (that is, on the line joining Pluto and Charon, just slightly outside Pluto’s body). Surely, as there is only one actual scenario, then d’Alembert’s Principle will guarantee the same ‘out- comes’ for each view-point? Yes, it does, but we can hardly say that the observed motions are the same in (a), (b), or (c). Now here’s a strange thing. Earlier on (in the spinning cabin) we showed that there were ‘fic- titious forces’ as a result of rotary motion (you were pinned to your chair, you felt a bit sick, the lamp no longer hung vertically down, and marbles started moving) but now, despite the fact that both Pluto and Charon are orbiting and spinning, yet there are no centrifugal or other ‘fictitious’ forces, no evidence of rotation whatsoever (apart from look- ing outside the system at ‘the view’, that is, the distant stars). How does this curious result arise? It arises because of the simplifying assump- tion-that Pluto and Charon are perfectly rigid bodies. In the cabin this assumption has not been made (humans are squishy, marbles are not stuck to the floor, the hanging lamp can swing). In fact, it is only through these non-rigid attributes that rotations can be noticed.

Another example is that of a bucket, spinning around its vertical axis of symmetry. The bucket would give no evidence of its acceler- ation unless it was filled with something non-rigid, like water. This is the famous example of Newton’s rotating-bucket experiment. Newton noted that, after spinning for a while, the surface of the water becomes curved, with the outer edges higher up than the level in the middle (Figure 5.3). Newton took this curved water-surface as a demonstra- tion that the bucket really is spinning (relative to an unobservable but absolutely stationary background Space).

Ernst Mach (nineteenth century physicist and philosopher) had an intriguing alternative idea. He saw that a) was not the true inverse of b)

(see Figure 5.3), as the bucket of water was not, in reality, surrounded by empty space but by the distant stars. If, in b), the distant stars were sta- tionary, then, in the true inverse of b) (say, c)) they should be rotating at the same rate¹³ but in the opposite direction to the bucket’s rotation.

As the background system of stars would then be different in b) and c), then this could account for foreground differences, like the differ- ent shape of the water’s surface. In effect, Mach asserted that the stars actually caused the water-surface to curve.

Nowadays we reject Newton’s absolutes (force, acceleration, Space), and we also reject Mach’s hypothesis. We can never carry out Mach’s hypothetical experiment of spinning or removing the heavens, and so we can never confirm or deny Mach; yet, his hypothesis is com- pletely against the spirit of d’Alembert’s Principle (and against the spirit of all variational mechanics, and Einstein’s Theory of General Relativity). While both Mach and d’Alembert agree that what is import- ant is the system, the whole system, and nothing but the system, yet, in d’Alembert’s Principle, the system does not extend to infinity, it only encompasses local effects and only makes local claims. This is more humble and more philosophically correct (‘pc’). In the variational mechanics, which includes d’Alembert’s Principle, the curving of the water-surface is due only to local interactions (neighbouring molecules), and local motions (of water molecules with respect to the centre of the bucket - a small distance). All this can be tested experimentally. Now, the bucket radius is smaller than the distance to the stars, yes, but how small is ‘local’? Ah, that depends...¹⁴

## 5.5 D’Alembert’s Principle and energy

There is one matter concerning d’Alembert’s Principle that we haven’t mentioned so far-the question of solvability, that is, can mathematical solutions to (5.7) be obtained? The applied forces are usually specified beforehand, and given in functional form (Hooke’s Law for a spring, Coulomb’s Law for electrostatic attraction, and so on) whereas the iner- tial forces (reversed accelerations of the mass-points) are not usually in functional form.¹⁵ This is because these accelerations have arisen from multiple influences-constraint forces as well as applied forces. An excel- lent demonstration of this is seen in the system of the roulette wheel and ball: here there are two applied forces-gravity and the push given to spin the wheel-but the resulting acceleration of the roulette-ball is all over the place-‘randomized’-due to the complexity of the mul- tiple constraint forces (the ridged and sloping surface of the spinning roulette wheel).

Now there is one special circumstance in which the (reversed)

accelerations can be expressed in functional form. Remember that d’Alembert’s Principle uses virtual displacements that are of our choos- ing (subject to any constraint and kinematical conditions): surely, we can choose the δrᵢ to coincide with the actual displacements, drᵢ, which really do occur? This would resolve our difficulties as the drᵢ are ‘perfect differentials’ and therefore amenable to mathematical solution. But, strange as it may seem, the actual displacements are not always per- missable as a stand-in for the virtual displacements. This is because the actual displacements, drᵢ, always take a finite time, dt, and during this finite time-interval the external conditions (applied forces, constraint forces, kinematical conditions, other external conditions) may change.

However, in the one special circumstance that all the external conditions are constant, independent of time, then there will be no contradiction in choosing the δrᵢ to be the same as the drᵢ.

In this special circumstance in which everything is in functional form, and everything is independent of time,¹⁶ some rather special out- comes follow. First, we will be able to express the applied forces as a time-independent ‘potential function’, V(r), satisfying Fᵢappl = –∂V/∂rᵢ (see Appendix A6.5). Second, we will be able to express the accelerations as aᵢ = r̈ᵢ. Third, as we have already explained, we are choosing to have δrᵢ = drᵢ. Making the appropriate substitutions into (5.7) we obtain: ∑ᵢ₌₁ᴺ (–∂V/∂rᵢ – mᵢr̈ᵢ) · δrᵢ = 0 (5.9)

The first term in the bracket, when summed over i, becomes the perfect differential, dV, and, provided that all the masses, mᵢ, are constant in time, the second term can be re-expressed as follows: ∑ᵢ₌₁ᴺ mᵢr̈ᵢ · δrᵢ = ∑ᵢ₌₁ᴺ mᵢr̈ᵢ · ṙᵢ dt = d/dt ∑ᵢ₌₁ᴺ (½ mᵢṙᵢ²) dt (5.10)

Does this remind us of anything? Yes, ½ (mᵢṙᵢ²) is the familiar kinetic energy function, T, and so the right-hand side of (5.10) is d(T) dt, which is the perfect differential, dT. So we can now rewrite (5.9) as: dV + dT = d(V+T) = 0 (5.11)

Finally, this can be integrated to give T+V = constant = E (5.12)

This is a familiar but fundamental result -the sum of the kinetic and potential energies of a mechanical system is a constant. To extract the importance of this, let’s collect together our starting assumptions: we have a mechanical system made up from particles and forces which can be modelled using rectangular coordinates; the applied forces derive from a time-independent potential function; the kinematical conditions remain constant in time; and the masses are also constant. One may think, well, it’s hardly surprising that we have a conservation prin- ciple given that we have assumed that everything is independent of time, that is to say, conserved. But this is to miss the point; what we have found is that, granted all the above assumptions, the well-known and fundamental law of the conservation of energy actually follows from d’Alembert’s Principle.

## 5.6 Review

D’Alembert, that brilliant but “sinister character”,17 discovered a Principle that causes some physicists to shudder even while, at the same time, it answers to almost all of physics: “All the different principles of mechanics are merely mathematically different formulations of d’Alembert’s Principle”.18 In d’Alembert’s Principle we have a method of treating a problem in dynamics as if it was a problem in statics (using the Principle of Virtual Work). This is down to d’Alembert’s “stroke of genius” - treating reversed massy accelerations as reactive ‘inertial’ forces. These inertial forces are added to the applied forces, and then the condition for ‘equilibrium’ is found in the usual way. Well, not quite in the usual Newtonian way: instead of the applied and reactive forces cancelling each other out in a pair-wise fashion, we generally have applied forces acting at just a few mass-points, and a melée of inertial forces, one for every accelerating mass. A further departure from Newtonian Mechanics is that instead of arriving at a balance of forces, we have a balance of energies - specifically, virtual work.

The tenets of d’Alembert’s Principle are: (1) The mechanical system is made up out of particles and forces, given in rectangular coordinates, (2) there are such things as ‘constraints’, and these are, in essence, forces, (3) moreover, these constraint forces are reactive forces, (4) massy reversed accelerations are, in essence, forces, (5) moreover, these massy reversed accelerations, known as ‘inertial forces’, are reactive forces, (6) at any instant, the total virtual work of the reactive constraint forces is zero, for virtual displacements that are in harmony with the constraints (Postulate A), (7) at any instant, the total virtual work of the applied forces and the reactive inertial forces is zero, for virtual displacements that are in harmony with the constraints.

The new modelling of physical reality is, at first acquaintance, rather strange, especially the newly introduced ‘inertial force’ which sounds oxymoronic, allying inertness with activity. However, this inertial force has been experimentally detected in countless scenarios (witness the centrifugal, and Coriolis forces, and the inertial force in Section 5.2) and, more than this, it brings in physical insight and philosophical ‘correctness’. First, d’Alembert’s Principle shows that, whether inertial or constraint, all the non-applied forces are ‘reactive’. Second, we have seen that d’Alembert’s Principle is sensitive to ‘F appl + I’ rather than to F appl and I taken separately (equation (5.7)). This means that there is no fundamental way of separating F appl and I, and so there is no way of determining that an applied force is absolutely external, or that a frame of reference is absolutely stationary, or that a frame of reference is absolutely accelerating. Considering I itself, we see also that the Principle is sensitive to ma rather than to m and a taken separately. It is therefore impossible to cleanly excise m away from a, and this leads to a departure from Newton’s passive, inert, conception of mass. For ‘fictitious forces’ (see Section 5.4), the strength of the force, far from being independent of mass, is actually proportional to it. In the special case of gravity this leads to an identity between the ‘gravitational charge’, m grav, and the mass, m (see the footnote for definitions19). Newton noticed this as a coincidence but for Einstein it was one of the clues that led him to the Equivalence Principle and then on to General Relativity. Also, in the centrifugal force, we see a dependence of the force on the speed, and the spatial distribution of mass, and for Coriolis forces, a dependence on the speed, and direction of the moving mass - all non-Newtonian features.

While some physicists have imagined that d’Alembert’s Principle is included within Newtonian Mechanics, and makes no further physical claims, assertions (4) to (7) are extra postulates which go beyond Newton’s Laws of Motion. The wider reach, increased explanatory power, and greater profundity of the Principle is not in doubt, and in modern physics we find that Newton’s Third Law doesn’t always apply, mass isn’t always constant, external conditions can vary with time, and energy is not always conserved (as the system isn’t necessarily closed), but it is always the case that the total virtual work of the ‘dynamical’ forces is zero (condition (5.8), Section 5.1). We can even go a step further than d’Alembert, and switch from a consideration of forces to virtual work, and recast the Principle as δω dyn total = 0. This is the cornerstone of classical, relativistic, and quantum mechanics, and so Lanczos’s words, repeated again here, are explained: ‘All the different principles of mechanics are merely mathematically different formulations of d’Alembert’s Principle’ (reference given earlier).

Given all this, we may wonder why d’Alembert’s Principle isn’t better known. The answer has little to do with the physical content of the Principle, and everything to do with the difficulty in solving it (obtaining the mathematical solutions). This is because of two surprising limitations: (1) the Principle still preserves a relic from Newton - it employs particles, forces, and rectangular coordinates, which leads to reactive accelerations that are ‘imperfect differentials’,20 and these are not amenable to mathematical solution; (2) despite our vaunting of it, d’Alembert’s Principle, being a special application of the Principle of Virtual Work, still applies only at one instant of time - curiously inappropriate for dynamics. An ingenious way of overcoming both limitations in one go is given in the next development, known as Lagrangian Mechanics.

20 Unlike the applied forces, the inertial forces are not in general described by a mathematical function, say, y, and so the inertial accelerations are not the ‘d-of-y’ - see the footnote in Section 5.5, and also Section 3.7.2.

Lagrangian Mechanics

Joseph-Louis Lagrange, in his great work, the Mécanique analytique (Analytical Mechanics),1 of 1788, discovered a general method for solving all the problems of mechanics, whether in statics or dynamics.

## 6.1 Introduction

The Principle of Virtual Work yields the condition for static equilibrium: it applies at one instant and then for all time (in other words, time doesn’t come into it). D’Alembert’s Principle, being a special case of the Principle of Virtual Work, also applies at just one instant but as we’re now in the realm of dynamics the conditions do change with time and so d’Alembert’s Principle must be reapplied at the very next instant, and then again at the next instant, and so on and so on. However what we would like is a method that frees us from the need to explicitly re-apply d’Alembert’s Principle, and, instead, enables us to mathematically track the motions continuously and over the whole time-interval of the problem. For example, in this more ‘holistic’ method we could have a provisional solution (a guess) spanning the whole time of the given dynamical problem (from t start to t end), and then we could ‘vary’ our whole-solution (have a guess that was a slightly different whole-solution), and then have some criterion for filtering out all but one of our guesses - the answer. Does this remind us of anything? Yes, it reminds us of minimum-path and isoperimetric problems - such as Dido’s question, Johann Bernoulli’s quickest-descent curve, and the shape of the catenary (see Chapter 2) - all solved using the method known as the ‘calculus of variations’ (Sections (3.7.2) and (3.7.3), Chapter 3). But perhaps we could use this same method, the calculus of variations, also in the case of general mechanics problems, as follows: we could embed d’Alembert’s Principle in a time integral, and then determine that whole-path through time which makes the integral stationary?

This is, in fact, exactly what we will do but there is one stumbling block that stands in our way: the calculus of variations involves analytical (mathematical) techniques and these can only be used when all the equations are in functional form (the f and F in equation 3.7.3-1 must be functions). The resolution? It turns out that we shall succeed if we restrict ourselves to just those cases where everything is in functional form. Thus, we shall insist that the applied forces arise from a work function, U, itself arising from a potential energy function, –V (for example, such that F i appl = –∂V/∂r i), and we shall also insist that any constraints and kinematical conditions are given in functional form.2

You may feel that this is all very well but we’ll just end up with a mechanics that only works when it works. However, this turns out to be a worthwhile exercise as ‘when it works’ seems to encompass most of physics! Better still, ‘when it works’ yields results that are stupendous, seeming to reward us with more physics, more insight, than ever we put in. So let’s run with it and see what happens.

## 6.2 Hamilton’s Principle - The Principle of Least Action

At any one time, t, d’Alembert’s Principle equates the total ‘dynamical’ virtual work, δω dyn total, to zero (end of Chapter 5)3 but, in dynamics, we require to integrate δω dyn through time between end times t a and t b, and then find the solution, that is, we require to solve ∫ t_a to t_b δω dyn total dt = 0.

However this integral is not solvable as it stands, and this is because δω dyn total is an imperfect differential (Chapter 3, Section 3.7.2c). It is imperfect for the reason that it contains the work done by the ‘inertial’ or ‘reactive’ accelerations, and these have arisen from the combined

1 Lagrange J-L, Mécanique analytique 1788, translated by Boissonade and Vagliente, Kluwer Academic, 1997.

The Lazy Universe. Jennifer Coopersmith, Oxford University Press (2017). © Jennifer Coopersmith. DOI 10.1093/acprof:oso/9780198743040.001.0001

2 There are a few exceptions, known as non-holonomic conditions, which we’ll come to later. Why does the potential energy have a minus sign? This is discussed in Section 6.6.

3 Notation: ‘Dynamical’ has been defined at the end of Section 5.1, Chapter 5. We denote the dynamical virtual work of one particle at one time as δω dyn i, and for all particles at one time as δω dyn total = Σ δω dyn i. The bar over He reminds us that the total differential is imperfect, and 'total' refers to 'all particles', not 'all times'.

Lagrangian Mechanics 109

influence of many sources. (Lanczos uses the Greek term 'polygenic' - arising from many sources - as opposed to 'monogenic' - arising from just one source.) But not all the contributions to δωdyn_total are imperfect: if only we could arrange things so that we collect together all the perfect bits that are in functional form, and tease out and isolate the difficult imperfect bits. Here's how.

We consider a system comprising N particles, m_i, with (rectangular) position vectors, r_i. We start by integrating d'Alembert's Principle, (5.7), Chapter 5, from time t_a to time t_b:

∫_t_a^t_b δωdyn_total dt = ∫_t_a^t_b Σ_i=1^N (F_appl_i - m_i a_i) · δr_i dt = 0  (6.1)

(As δωdyn_total at each instant is zero, then the integral of it over time is also zero.) The bracket in (6.1) can be separated into two terms:

∫_t_a^t_b Σ_i=1^N F_appl_i · δr_i dt – ∫_t_a^t_b Σ_i=1^N m_i a_i · δr_i dt = 0  (6.2)

Now, one of our assumptions is that there is a potential function, V, with perfect differential, δV = (∂V/∂r_i)δr_i = – F_appl_i · δr_i where F_appl_i = –∂V/∂r_i. The first term of (6.2) is therefore already in functional form:

∫_t_a^t_b Σ_i=1^N F_appl_i · δr_i dt may be written as – ∫_t_a^t_b δV dt

The second term in (6.2) is problematic as it contains the dreaded imperfect inertial accelerations - but we have some 'tricks' up our sleeve. First, we ameliorate matters by re-branding the accelerations as velocities:

a_i may be written as v_i may be written as d(v_i)/dt

This re-branding 'trick'4 is one we'll resort to again and again (see especially Chapter 7), and amazingly it works. (The reason why it works is hard to explain but, ultimately, it is due to the fact - as Hamilton intuited - that 'position' and 'momentum' are the fundamental variables, and so 'speed' (part of momentum) is a more fundamental and telling parameter than 'acceleration'. We'll return to this in Chapter 7.) Finally, assuming that the m_i are constant in time, we obtain:

∫_t_a^t_b Σ_i=1^N m_i a_i · δr_i dt may be written as ∫_t_a^t_b Σ_i=1^N d(m_i v_i)/dt · δr_i dt

The second 'trick' we use is a mathematical technique known as 'integration by parts':

∫_t_a^t_b Σ_i=1^N d(m_i v_i)/dt · δr_i dt =

∫_t_a^t_b Σ_i=1^N d(m_i v_i · δr_i)/dt dt – ∫_t_a^t_b Σ_i=1^N m_i v_i · d(δr_i)/dt dt  (6.3)

There is scope for modifying the last term in (6.3) by exploiting the fact that the operations d/dt and δ may be swapped around.5 This term may then be transformed as follows (taking note of the fact that d(r_i)/dt is the same as v_i):

∫_t_a^t_b Σ_i=1^N m_i v_i · d(δr_i)/dt dt = ∫_t_a^t_b Σ_i=1^N m_i v_i · δ(d(r_i)/dt) dt = ∫_t_a^t_b Σ_i=1^N m_i v_i · δv_i dt  (6.4)

Now, δ is an operation which, while it relates to the variational calculus (Sections (3.7.2b) and (3.7.3)), it nevertheless follows exactly the same rules as d/dt. So we know that

m_i v_i · δv_i may be written as δ(½ m_i v_i²)

This last expression, ½ m_i v_i², rings bells for us - it is the kinetic energy of particle i, and we will denote it by T_i, as T is a symbol commonly used for kinetic energy. (δT_i is then the variation in the kinetic energy of particle i.) Summing over all the masses (that is, over all the i's) we obtain the virtual variation in the total kinetic energy, δT.

Returning to equation (6.1), we substitute in all of these new expressions, and so finally arrive at:

∫_t_a^t_b δωdyn_total dt = – ∫_t_a^t_b δV dt – ∫_t_a^t_b Σ_i=1^N d(m_i v_i · δr_i)/dt dt + ∫_t_a^t_b δT dt

= 0  (6.5)

We have made huge progress. T and V are functions, and so we have succeeded in isolating and herding together all the difficult imperfect polygenic responses - they're all in the middle term on the right-hand side of (6.5). Even more fortuitous, this middle term, by this method of 'integration by parts', is a 'total differential' and so all of it becomes a boundary term:

∫_t_a^t_b Σ_i=1^N d(m_i v_i · δr_i)/dt dt = (Σ_i=1^N m_i v_i · δr_i)|_t_a^t_b  (6.6)

This helps - the messy bits are concentrated in just one term of (6.5), and even within this term they are concentrated (exist only) at the boundaries (the end-points of the path). But there's still one more 'trick' up our sleeve. It so happens that at these boundaries there is no variation. (Hamilton insisted on this - the integral in (6.5) was to be minimized for a function that remains fixed at the ends (fixed in both position and time6).) But this then means that the δr_i's are zero at t_a and zero at t_b, and so the whole boundary term is zero - it just disappears, pouffe! We have had one difficult bundle of imperfect inertial accelerations, but we never have to unwrap it, we can throw the whole bundle away.

Equation (6.5) thus simplifies to:

∫_t_a^t_b δωdyn_total dt = ∫_t_a^t_b δ(T–V) dt = 0  (6.7)

Now, in the same way as the order of d/dt and δ may be swapped (see above), the order of ∫ and δ may be swapped. So, the right-hand side of equation (6.7) finally turns into:

δ ∫_t_a^t_b (T–V) dt = 0  (6.8)

Hamilton's Principle

This equation has become known as Hamilton's Principle, after the Irish genius and mathematical physicist, William Rowan Hamilton (1805–65) - see Chapter 2. We shall hear more of Hamilton later (in the next chapter). As the integrand, (T–V), has the dimensions of energy, and as the integral is over time, then the left-hand side of equation (6.8) is a quantity of action - it asserts that the variation in the total action is zero, or, in other words, the action is stationary. In fact, we shall find (Section 6.6) that the action is not just stationary, it is minimized. So, Hamilton's Principle is thus a Principle of Least Action (we have the authority of Feynman to name it thus7). We at last have our Principle in the form of an equation - but now we must solve this equation. This is dealt with in the next section.

## 6.3 The solution of Hamilton's Principle:

Lagrange's Equations of Motion

We start by making Hamilton's Principle more compact by writing 'L' as a shorthand for 'T–V':

δ ∫_t_a^t_b (T–V) dt = 0 may be written as δ ∫_t_a^t_b L dt = 0

Hamilton's Principle

The letter 'L' was chosen to commemorate Lagrange, who formulated a least action principle which was the precursor of Hamilton's Principle. 'L' is known as 'the Lagrangian'. Now T and V are functions of r_j, ṙ_j, and t, and so L is likewise some function of r_j, ṙ_j, and t, where j runs over the number of particles in the system, say, N. (A historical note: in Lagrange's earlier version L was not allowed to be a function of t; Hamilton's Principle is more general in this regard.) Thus Hamilton's Principle, with all the arguments shown, becomes:

δ ∫_t_a^t_b L(r_1, r_2, ... r_N; ṙ_1, ṙ_2, ... ṙ_N; t) dt = 0  (6.9)

Let's refresh our memory of the calculus of variations from Section (3.7.3), Chapter 3. There we showed that the stationarity of a definite integral (with respect to infinitesimal variations in the shape of the line), required that:

δ ∫_x_a^x_b F(f_1, f_2, ... f_n; ḟ_1, ḟ_2, ... ḟ_n; x) dx = 0  (6.10)

In that section we claimed that, so long as the f_j and the ḟ_j were functions of x, and so long as F was a function of the f_j, ḟ_j, and x, then (6.10) could be solved by the Euler-Lagrange Equations.8 Now equations (6.9) and (6.10) bear more than a passing resemblance to each other. In fact, given that L is some, as yet, unspecified function of r_j, ṙ_j, and t, and F is some unspecified function of f_j, ḟ_j, and x, then, if the Euler-Lagrange Equations solve (6.10), might they not also solve (6.9), that is, solve Hamilton's Principle? Yes, but there is even one more remarkable step we can take: as L is 'some function' of r_j, ṙ_j, and t, so surely it is also 'some other function'9 of q_i, q̇_i, and t, where the q_i's are Lagrange's 'generalized coordinates'.10 We can thus write Hamilton's Principle, in its most general form, as:

δ ∫_t_a^t_b L(q_1, q_2, ... q_n; q̇_1, q̇_2, ... q̇_n; t) dt = 0  (6.11)

and we can be assured that it will be solved by the Euler-Lagrange equations:

d/dt (∂L/∂q̇_1) – ∂L/∂q_1 = 0 d/dt (∂L/∂q̇_2) – ∂L/∂q_2 = 0 d/dt (∂L/∂q̇_n) – ∂L/∂q_n = 0  (6.12)

(It is understood that all these n equations must be satisfied simultaneously.) As the independent variable is now the time, t, then (6.12) are equations of motion, and by convention the Euler-Lagrange Equations are then referred to as the 'Lagrange Equations of Motion' or simply as the 'Lagrange Equations'. These famous equations, the solution to Hamilton's Principle, can be written on one line as:

The Lagrange Equations of Motion d/dt (∂L/∂q̇_i) – ∂L/∂q_i = 0  i = 1,2,...,n  (6.13)

This is all very impressive, but we are left wondering whether we haven't been blinded by wool: can a mere change of symbols (F → L, f → q, ḟ → q̇, and x → t) really mean that we have gone from a useful technique (for solving, for example, Dido's problem, the brachystochrone problem, and the shape of the catenary) to a set of equations promising a solution to all of mechanics? The resolution will lie in the fact that, in going from the Euler-Lagrange Equations to the Lagrange Equations of Motion, we have done much more than a mere change of symbols. Before this is explained, we'll first treat a few simple and well-known mechanics problems by Hamilton's Principle and the Lagrange Equations of Motion - in other words, by the method known as 'Lagrangian Mechanics' - so that we can be awed by the power of our new weapons. (See the worked examples in Appendix A6.1).

## 6.4 What is happening physically

From solving problems (Appendix A6.1) we learn so much: that what counts as kinetic or potential energy depends on the frame of reference; that it isn’t necessary to calculate the constraint forces (the tension in a cord, the force that constrains a bead to a wire, and so on); that the same method and insights can be applied to very different systems (for example, electrical and mechanical systems); that the kinetic energy can contain constant terms, and terms that are linear in the speeds; that the potential energy can depend on velocity, and on time. But even without solving a single problem, something commands our attention and leaves us awestruck: run your eye over all the boxes shaded grey in Appendix A6.1 and you will be witness to a most remarkable thing—the applicability of just one set of equations. The systems are for different scenarios, each with their own forms for T and V, and yet the equations to be solved always have exactly the same form. Also, for any one system, the coordinates may be transformed,¹¹ or the system may be re-modelled into a different set of coordinates, and there may be time-dependent conditions imposed on these coordinates, and the total energy may not be a constant, and the reference frame may be moving, even accelerating; and yet in all these cases the equations to be solved—the Lagrange Equations—still have the same form, and the Lagrangian keeps its same value (say, 0.0561 Joules).¹²

Yet we are left feeling puzzled and circumspect: surely, merely by ‘sleight of maths’ (all the ‘tricks’ of Section 6.2, and the symbol-changes of Section 6.3), we can’t have arrived at a universally valid set of equations? To be able to minimize a definite integral, that is a very pretty skill, mathematically-speaking, but our perplexity has nothing to do with the mathematics, and everything to do with the application of it to physics. The perplexity will be resolved when we understand that some implicit physical assumptions have entered in along the way. Yes, we can re-model the system, or transform from one set of coordinates to another, but there are some underlying physical aspects that don’t change—the ‘degrees of freedom’. Yes, we can introduce some extra mathematical ‘conditions’ (equations between variables) but again something physical is implicated—the number of these ‘degrees of freedom’ is reduced. Yes, imposing certain boundary conditions gets rid of the ‘boundary term’ at a stroke—but what does this mean physically?

Let’s address the last question first. We remember Lanczos’s Postulate A—the ‘reactive’ constraint forces, leading to imperfect accelerations, do no virtual work. Now in the boundary term we again have a collection of imperfect accelerations (this time resulting from ‘reactive’ inertial forces), and we again find that they contribute nothing to the total virtual work. So it seems as if the boundary conditions are a special kind of constraint condition—and this makes plausible physical sense.

Note that Postulate A doesn’t apply to the perfect differential motions—we find that δT does not usually lead to zero variation in action; it is only δT in tandem with –δV that leads to stationary action. Remarkably, this applies both through time and at each instant of time (between the given end-times). That T and V are up to the task is, in a sense, not too surprising; we earlier on stipulated that they must be functions, and, as such, they impart a functional dependence on time.¹³ Combined with the boundary and continuity conditions, and maybe also extra constraint and kinematic conditions, this functional dependence is exactly such as to rule in one actual path, and to weed out all other paths from our enquiries. (Moreover, T and V are still up to the task, whether they are functions of \( q_i, \dot{q}_i, t \) or \( r_j, \dot{r}_j, t \).)

Another mathematical stipulation, introduced rather casually (just before Hamilton’s Principle, equation (6.8), Section 6.2), was that the order of \( \delta \) and \( \frac{d}{dt} \) may be swapped. This seemingly innocent swapping operation has physical implications: we go from virtual displacements at one instant, to a varied whole-path over a prescribed time-interval. Now, one may at first think that this extra whole-path requirement is unnecessary—surely, as the total virtual work is already zero at each and every instant,¹⁴ then it is guaranteed to be zero over the whole path in time? Yes, but while a minimized¹⁵ path does require that every sub-interval must also be minimal, this doesn’t mean that any collection of minimal sub-intervals will be just the right collection to yield the required whole path. In other words, the vanishing of the virtual work at every instant is a necessary but not a sufficient condition to generate the correct final path. This gives us some insight into an earlier question: at the end of Chapter 3 we wondered why the varied integral had \( \dot{q} \) as one of its arguments—surely a dependence on \( q \) is enough, as \( \dot{q} \) is merely consequential upon \( q \)? But now we begin to understand: in order for a collection of infinitesimal path segments to add up to the correct whole path, then each segment must join on smoothly and continuously with the next segment, and so on. This can only be guaranteed if the \( q \)-values are equal at the join. Or, in other words, the \( q \)-values are like an infinity of ‘interior boundary conditions’, existing all the way along the path. (The boundary conditions at the very ends are determined in another way—by the limits on the integral.)

What of the scalar energy functions, T and V? As mentioned earlier, we find that the total virtual work of variations in T cancels out with the total virtual work of variations in V, both instant by instant, and over the whole time of the given problem. But, in fact, we have none need to keep harking back to the form of energy known as work: we have progressed to a more general vision—variations in energy, pure and simple (δT and δV). Now, taken individually (that is, for each \( i \)), the T will not necessarily be the same as they were when modelling the system as point-particles and rectangular coordinates (compare T in examples (1) and (2), Appendix A6.1). Also, V may change as we go from one coordinate system to another. However the total Lagrangian, L, (defined as \( (T–V) \)), will be the same (have the same actual value, say 10 Joules). We say that L is invariant. This means that for any one system, howsoever that system is viewed or modelled, the L-value will remain unchanged.¹⁶ We’ll comment again on this wondrous outcome in Section 6.6, and discuss the forms of T and V in Section 6.5.

Let’s summarize some of the physical assumptions implicit in Lagrangian Mechanics: 1) the system can be modelled as ‘generalized particles’, \( q \), having individual ‘perfect motions’ with an, as yet unknown, functional dependence on time, 2) these individual ‘perfect motions’ imply an amount of ‘work’ which makes up one all-embracing scalar function known as T. Moreover, T is an energy function (known as the kinetic energy). The functional form of T depends on the modelling (the choice of \( q \)), and is known in advance, 3) the configurations and interactions¹⁷ of the \( q \), in other words the whole-system aspects, make up one all-embracing scalar function, V, which, of its nature, depends on the system, and is known in advance. Moreover, V is an energy function (known as the potential energy).

4) there may, as well, be extra constraints or conditions on or between the generalized particles, and these will manifest themselves in the form of known functional relationships between the \( q \) (the functions may also depend on \( \dot{q} \) or \( t \)), 5) the mêlée of imperfect re-active motions due to constraints ‘cancel each other out’ (their total virtual work is zero) at each instant, t, 6) the mêlée of imperfect re-active motions due to boundary conditions also leads to zero virtual work at each instant, t, 7) the virtual variations, δT and -δV, when these are considered together, bring the variation in total action to zero, at each instant, and over the whole time interval of the given problem, 8) the only functions (‘equations of motion’) for the \( q \) that can survive assumptions 1) to 7), along with the requirements of continuity, and boundary conditions (and also differentiability, and being finite), are the ones describing the actual motions.

That Nature does, in fact, conform to these requirements is borne out by the success of Lagrangian Mechanics and of the Principle of Least Action in physics.

## 6.5 The functions T and V

The generalized coordinates for a given system can usually be arrived at after thoughtful inspection of that system and seeing the ‘motions’ of which it is capable. But what of the functions T and V? We have merely said that they are supplied beforehand. Now we will examine what form they must take.

6.5.1 The form of T

For a single free particle (no forces acting) of mass, m, and velocity, v (in rectangular coordinates), the kinetic energy has the familiar form: \[ T = \frac{1}{2} m v^2 \] kinetic energy, ‘quadratic form’ (6.14)

Why does T have this ‘quadratic form’, is it essential? (The adjective ‘quadratic’ is to remind us that the speed is squared.) The physicists Landau and Lifshitz¹⁸ argue that, due to the homogeneity of space and time, the kinetic energy for a free particle cannot depend on position, r, or on time, t. Therefore (they argue), T must depend only on the velocity, v. Furthermore, the isotropy of space requires that no special directions are picked out, and so T must depend only on the magnitude of the velocity, that is, on v. This leads Landau and Lifshitz, finally, to conclude that T must depend only on the speed squared, \( T = T(v^2) \).

But there are questions to be asked of Landau and Lifshitz’s ‘derivation’. First, as well as no absolute position or time, we know that there is also no absolute velocity (it is impossible to tell, by any experiment within a given reference frame, at what uniform speed or direction the reference frame is travelling)—so how can there be a dependence on v or v, squared or not?

Second, why should a magnitude—the speed—only be arrived at by squaring? Why not, say, squaring followed by taking the square root? In fact, it can be shown that a squared dependence on speed is required. This can be shown in two ways: (i) A physics argument: The Principle of Relativity must always be upheld, and this can only be guaranteed by having a dependence on v². Two proofs of this (due to Maimon,¹⁹ and due to Ehlers et al²⁰) are given in Appendix A6.2.

(ii) A mathematical argument: the only way in which to arrive at a scalar invariant quantity from the vector quantity, v, is to take the ‘scalar product’, v · v, and this yields v².

¹⁸ Landau L, and Lifshitz E, Course in Theoretical Physics, vol 1, Mechanics, Pergamon Press, Oxford, 1960.

¹⁹ Maimon, Ron: former contributor to Physics Forum on the web; Maimon is an independent researcher in physics.

²⁰ Ehlers J, Rindler W, and Penrose R, ‘Energy conservation as the basis of relativistic mechanics II’, American Journal of Physics, 33(12) 1965, pages 995–7.

Upon reflection, we find that both arguments have a common feature: to obtain an absolute or invariant quantity we must always consider one quantity relative to another. So, in (i) we find that both proofs require a collision between two particles; and in (ii) we note that the scalar product, a · b, presumes two vectors. Even in the case of identical vectors, v · v, then one v is the ‘projected’ vector, and the other v is the ‘projectee’ vector; in other words, the ‘dimensionality’ of the problem is dual.²¹ (In differential geometry, we say that each v has come from a different ‘vector space’.)

However, a solution can sometimes lead to a new problem: what form shall we give to the kinetic energy of just one isolated particle? The resolution is that we are then compelled to define the kinetic energy as having the quadratic form (6.14). This leads to consistency in the theoretical modelling. (On the other hand, we could bow out altogether on the grounds that ‘one isolated particle’ is a pathological scenario—we can never check upon it experimentally because as soon as we bring in measuring equipment then the particle is no longer isolated. Once again, the author’s maxim is apt: “[pathologically] simple cases make bad physical intuition.”)

We are not done yet; in (6.14), there is still the question of mass, m. How did we arrive at ‘T is proportional to m’? To answer, we follow Maimon and use the empirical observations that mass is additive (the mass of many particles is the sum of their individual masses), and that for a particle of, say, double the mass, then its kinetic energy is doubled. These empirical findings mean that not only is T a function of v² but mass must occur as the coefficient of this function of v². So, we end up asserting that: T = ‘massy inertial factor’ × ‘some function of v²’, where the ‘massy inertial factor’ always includes m.²² Finally, when we are modelling the situation using generalized coordinates, then the standard form is: T = ‘massy inertial factor’ × ‘some function of q̇²’. (We’ll come back shortly to the question of the × factor, ½.)

We are still not done; look again at definition (6.14) and ask: How big is the mass, m? How big is the speed, v? For masses that are tiny, or huge, or speeds that are high, then (6.14) needs modification, and we are in the realms of quantum mechanics, Einstein’s Theory of General Relativity, and Einstein’s Theory of Special Relativity, respectively. However, a common feature of all great theories is that their wisdom extends beyond their conventional range of applicability. This is especially true of Special Relativity, which has not merely extended Newtonian Mechanics into a high-speed regime but has radically changed our understanding of all of physics, whatever the speed. (It was from Special Relativity that Einstein arrived at his most important single discovery, E = mc²—see below.) Of particular relevance in the present discussion: in Newtonian Mechanics there is no absolute speed, but in Special Relativity there is an absolute speed—the speed of light, c. However, in all the formulae of Special Relativity v always occurs as the ratio, v/c—so speed has, in effect, been converted into a ‘relative quantity’. Should we be concerned that in the standard form for T, (6.14), speed occurs on its own (that is, without c)? No, we are rescued in a different way. The method of Lagrangian Mechanics (and all Variational Mechanics) concerns a system, and we find that the speed is always relative to that system. In fact, in the Variational Mechanics, all the coordinates are relative to the end-points of the integral in Hamilton’s Principle, and so all the coordinates are relative to the system. This answers our earlier question over Landau and Lifshitz allowing v into the formulation, and is yet another reason why Lagrangian Mechanics rather than Newtonian Mechanics survives the transition to Einstein’s Relativistic Mechanics. (By the way, the factor, ½, must be included in order to ensure that the Special Relativistic kinetic energy reduces to the usual formulation of (6.14) in the limit of ‘low’ speed.)

²¹ The word ‘dimensionality’ will be explained near the beginning of Chapter 7.

²² There is still the question of how the ‘massy inertial factor’ is split between the two dual vectors: we could have 1 and m, or √(m/2) and √(m/2), and so on. The resolution will come with Hamilton’s p and q coordinates (Chapter 7), and it will be shown that all the massy-dependence goes to just one of the dual vectors.

Saving the most important till last, we come to Einstein’s most famous discovery, the best-known equation²³ in physics, E = mc². Einstein, himself, regarded this discovery—of the equivalence between mass and energy—as the single most important result to emerge from Special Relativity.²⁴ One consequence of this equivalence is that even if the particle slows to a standstill, and its kinetic energy is then zero, the particle still has mass, and so there is still some energy ‘left over’. Now, in Newtonian Mechanics, the zero-point of kinetic energy is arbitrary, and is generally set to zero. However, Einstein found that the ‘left over’ energy, sometimes called the ‘rest energy’, is not arbitrary—it is determined, and specific to the given particle.²⁵ It also happens to be enormous (1 gram of mass has a ‘rest-energy’ of some 90 million million Joules). Why are we usually so (blissfully) unaware of this huge ‘rest energy’? It is because, contained within mass, it happens to be an exceptionally stable way of storing energy. One further question on this: as the ‘rest energy’ is evidently a store of energy, should we not consider it as V instead of lumping it together with T? We’ll say more about this as we go along, and end up with a speculation in the concluding section of the chapter.

²³ We have left this iconic equation in its usual form, but, in fact, it depends on the notation for mass: if we use ‘m’ to mean ‘rest mass’, then the equation should be written E = mγc², where γ = 1/√(1–v²/c²).

²⁴ Einstein A, in Pais A, Subtle is the Lord: the Science and the Life of Albert Einstein, Oxford University Press, 2005.

Einstein’s famous equation applies not only to kinetic energy but implies that all energy is ‘massy’. This mass-energy equivalence is anticipated in Lagrange’s and later Hamilton’s Mechanics, which treats kinetic energy (rather than acceleration) as the true measure of inertia (see the next section, 6.6). It is therefore not surprising that Lagrangian Mechanics is well placed to accommodate Einstein’s Relativity Theory (it is only necessary to find the appropriate form for L) whereas Newton’s Mechanics must be totally replaced. One extra thing to say is that it is an empirical and not fully understood fact that mass, and hence also kinetic energy, are always positive quantities.²⁶

The standard form for T applies to free²⁷ particles. When considering more complicated scenarios, for example with interacting particles, or accelerating reference frames, then T can have terms just containing q, or unsquared-q, and so on (see Appendix 6.1, problem (10)). These occurrences do not contradict the ‘quadratic’ form of (6.14), as there we had a free particle and so space really was featureless (homogeneous); but when we consider interacting particles, and external conditions, then the space of the problem is no longer homogeneous, and so a dependence on q, q̇, q̈, ... can occur.²⁸

²⁵ Of course, it is determined from the mass, in accordance with Einstein’s famous equation—as we are talking of a particle, with no internal parts, then we can forget about internal energy states.

²⁶ W Rindler, Special Relativity, Oliver and Boyd, 1966, p87.

²⁷ Colliding particles may be considered free at all times except for the instant of collision; also, a uniformly rotating finite-sized rigid body may be considered as free.

²⁸ (For terms linear in q̇, you may be wondering about a contradiction with our earlier footnote that the system relates to a dual vector space. However, these linear terms occur when some constraint condition or potential energy term also contains a linear dependence on speed—and so, overall, the duality is maintained.)

6.5.2 The form of V

There is a standard form for T, (6.14), but none for V—it must be formulated afresh for each new system. This has led some physicists to speculate that V is in some sense less fundamental than T—more on this later (end of Sections 6.6 and 6.8). Now V arises from applied forces, and from ‘particle’-interactions, and as these depend on configuration—the positions of external features, the positions of the ‘particles’ with respect to one another—then V is explicitly a function of these position coordinates, V = V(q₁, q₂, ... qₙ). T has already hived off the dependence on the motions, q̇ (T is, after all, kinetic) and so we generally do not have V depending explicitly on q̇₁, q̇₂, ... (but see below). Finally, there is nothing we have said, at any stage in our development of Lagrangian Mechanics, that prevents L, and hence V, depending explicitly on time. So, altogether, our simplest form for V has it depending just on q, and t.

You may be wondering why we are allowing an explicit dependence on q and on t for V but not for T—in standard form (in the latter case we (or rather, Landau and Lifshitz) invoked the homogeneity of space and time to veto just such a dependence on q and on t). The explanation is that V, of its nature, describes whole-system attributes, and it can therefore depend on whole-system ‘configuration’ coordinates, whereas T—in standard form, of its nature, depends on individual or system-free attributes. Put differently, as far as V is concerned, q and t are not absolute but are defined with respect to the given system: the q describe the positions of particles relative to each other or to some external constraint, and t is relative to the prescribed end-times of the path, t₀ and t₁.

Does an explicit time-dependence in V (and, perhaps, in constraint or kinematic conditions) mean that energy conservation...

Is the conservation of energy not satisfied? Yes, in Lagrangian Mechanics it is not required that energy be conserved. Obviously, in the whole world, energy is still conserved, but an explicit time-dependence in V, or in the external conditions, allows for energy to come into the system from outside. For example: in the ‘variable energy cyclotron’ the magnetic field is steadily increased to ensure that an accelerating charged particle will stay in the same orbit, but the energy for the magnets must be fed into the system from the outside; in ‘Ehrenfest’s pendulum’, the length of the pendulum is slowly decreased—but hauling in the pendulum takes energy; a spinning turntable introduces centrifugal, Coriolis, and other effects—but the energy to spin the table has been externally supplied; and so on. We’ll have more to say on the conservation of energy in Section 6.7.

So much for V in standard form. Now, earlier on, we said that T was responsible for the dependence on speeds, but in fact there is nothing that prevents V depending explicitly on the speed coordinates, q, and there are some famous and important cases. One concerns the motion of a charged particle moving under the influences of electric fields, E, and magnetic fields, B. The force (known as the Lorentz force) is given by: F = q[E + (v × B)] (6.15)

(This is in units where c = 1. The q here refers to electric charge and not to a generalized coordinate). This implies a potential energy given by: V = qφ – qA · v (6.16)

where φ is some scalar potential and A is a vector potential. Note that, in this example, V depends on the velocity, v, of the particle (on the direction of motion as well as the speed). Just imagine the consternation when these effects were first discovered—when Oersted, then Faraday, and others, discovered that magnetized compass needles, iron filings, electric currents, and isolated charges could travel along curved lines, sometimes in closed loops neither starting or ending on a ‘source’, and (for a pure magnetic field) with the velocity, the field, and the force all at right angles to one another. Newton’s Mechanics is contravened, but Lagrangian Mechanics carries on as usual (it is only necessary to use Hamilton’s Principle with a Lagrangian given by L = T – qφ + qA · v).

Another example of velocity-dependent effects are Coriolis forces—those forces partly responsible for wind directions, and ocean currents. For a particle of mass, m, moving at speed, v, with respect to a rotating platform (with constant spin-rate, ω) then the Coriolis force acts sideways onto the particle’s motion, and is stronger the greater the particle’s mass, or speed. In symbols, the Coriolis force has magnitude 2mωv_radial, or 2mωv_tangential, and is tangential when the velocity is radial, and radial when the velocity is tangential. (Also, the Coriolis force doesn’t depend on the radius, and is distinct from the centrifugal force, another kind of velocity-dependent force.)

In most cases of velocity-dependent potentials the particle’s motion violates Newton’s Third Law of ‘action and reaction’, and its momentum is not conserved. However the generalized or canonical momentum (Section 6.8, and Chapter 7) is conserved, for example, for a moving charged particle (for a φ and A which are independent of position), the particle’s momentum is not conserved on its own, and the momentum of the electromagnetic field must make up the balance.

The energy function, L, was introduced rather casually in our ‘derivation’ of Hamilton’s Principle (see the beginning of Section 6.3). L, the ‘Lagrangian’, is the integrand in Hamilton’s Principle, and is of paramount importance in mechanics—but where does it come from, and why does it have the form ‘(T – V)’ when we are so much more familiar with ‘(T + V)’? We turn to Lanczos, as an explanation of the physical origins of L is given there and nowhere else.

At any instant, T is a function which describes the motions of all the particles, and these motions are a consequence of the ‘marching orders’ dictated by V. At the very next instant the particles will adopt new positions, and so the configuration has changed, and so the magnitude of V is different. This new V will influence the motion of the particles afresh, and so the T at the next instant will be different. This new T will again lead to the particles adopting new positions, and this will again imply a V with a different magnitude, and so on and so on. We therefore have an interplay between T and V, one which continues, instant by instant, from the start- to the end-time of the problem. Now, as T involves masses-in-motion, it can be seen as an inertial response to V (and this is consonant with Einstein’s mass-energy equivalence, coming over a hundred years later). This is reminiscent of the inertial response, ma, to Newton’s force, F. However, whereas in Newtonian Mechanics we treat one particle in isolation, and end up with an equality (between ma and F), in Lagrangian Mechanics we have a whole system, and end up with a balancing process between two scalar energy functions. How shall we choose between these postulates—Newton’s Second Law, and Hamilton’s Principle? It is not simply a question of switching from Newtonian to Lagrangian Mechanics when going from simple to complicated scenarios, but rather that Lagrangian Mechanics supersedes and totally replaces Newtonian Mechanics. This is because, despite what we have been coached to believe, it is kinetic energy which is the true measure of ‘inertia’, and kinetic energy rather than force which is the thing that is truly primitive and irreducible: ma = F is superseded by T ‘balances’ V (where ‘balances’ refers to a whole process, the application of a principle, and not merely to ‘equality’.)

Finally, why does L have exactly the form L = T – V and no other? It is because, while T and V must be in balance, they must also act in opposition to each other. If each could reinforce the other then this could lead to a runaway growth in energy—a very unphysical outcome. But if they act in opposition, or, in other words, if we must find the difference between them, then this can lead to a stable value for energy—a physically plausible outcome. Thus it is the difference between T and V that is important, and therefore V must carry a negative sign. According to Lanczos: “the excess of kinetic energy over potential energy is the most fundamental quantity in...mechanical problems.”

So, T opposes V rather than T and V reinforcing each other—but does this mean that Hamilton’s Principle will always lead to least action? (We require the action to be stationary, but this still leaves open the question of whether it is a maximum, a minimum, a saddle point, or a plateau.) The answer has been given in an interesting paper by Gray and Taylor. These authors show that we can have a true minimum (a pure minimum), and we can have a saddle point (a minimum and a maximum together), but it is never the case that there is a true maximum in the action. The argument is made intuitive in the following way. Consider the time-path of a particle in 2-D space using (x, y) coordinates (the one scenario where everyday space and configuration space are the same). Can we vary the path and make it shorter? Usually, unless the path already has the minimum length. Can we vary the path and make it longer? Always, just add more wiggles. Thus there is a difference between a minimum and a maximum: only the former can be guaranteed to be unique. The argument also seems physically intuitive in another way, on the grounds of economy—that is to say, it is more economical in action to have it minimized rather than maximized. As supporting evidence, we have the finding that for stable equilibrium (T = 0) V is at a minimum—a well-known result in statics.

Returning to the form of L, we note that this cannot be defined uniquely, for two reasons. First, the condition of stationarity (the equating to zero of the action integral in Hamilton’s Principle) will be unaffected if the whole integral, δ ∫ L dt, is multiplied by an arbitrary constant, ‘cons’. Second, the condition of stationarity will likewise be unaffected if the integrand, L, is changed to, L + df/dt. This doesn’t invalidate what we said earlier about L being an invariant—for any given system, the Lagrangian is not defined uniquely, but whatever choice we plump for then this L is invariant (with respect to a different choice of {q}, or to coordinate transformations—excluding re-scaling). This non-uniqueness of L is perhaps the reason why its invariance isn’t vaunted as much as the invariance of the Lagrange Equations: these Equations are invariant come what may. (Note that when we have non-holonomic conditions or polygenic forces, such as ‘friction’, the effect of these non-holonomic influences is to introduce a ‘right-hand side’ to the Lagrange Equations, see Appendix A6.5, and Lanczos, pages 146–7.)

Another comment concerns the sign of L. While T is always a positive quantity (m is positive, and the speed is real) we cannot go on to say that L is always positive, first because V has no absolute sign—it can be set to be positive or negative—and second because the multiplicative constant, cons, can be positive or negative.

One intriguing observation is that the condition of stationarity is sensitive to L, that is, to the whole of (T – V), rather than to T or V taken separately. Does this imply that there is some blurring of the distinction between what counts as kinetic energy and what counts as potential energy? The answer is yes. For example, in the case of a bead on a wire rotating with constant angular speed, ω (Problem (10) in Appendix A6.1), we have T = ½mṙ² + ½mr²ω² and V = 0, but we could just as well consider it as T = ½mṙ² and V = –½mr²ω². It makes no difference whatsoever to L, but in the second case we have lost some kinetic energy of the bead and gained a ‘centrifugal’ potential that didn’t exist beforehand. Such a shift in the assignment of energies can also occur as a result of a change in coordinates (a change in viewpoint), say, from a reference frame sited at the centre of rotation to one sited on the bead itself (see Sections 6.8 and 6.9).

This blurring between T and V is an example of how, in Lagrangian Mechanics, there is no hard and fast distinction made between a whole system and the individual components of that system. For example, consider the motion of a planet in its orbit around the Sun. The planet is a very small body but...

By comparison with the dimensions of its orbit, and with the size of the Sun. In the Newtonian analysis the planet is a 'particle' and doesn't affect its 'surroundings' but in Einstein's theory of General Relativity the planet does distort spacetime to a tiny extent, and this leads to a subtle change in its orbit - its precession advances. (In fact, it was just this tiny effect which led to one of the confirmations of General Relativity - the extra precession of the perihelion of Mercury.) Consider, also, the case of an electron moving parallel to a wire in which a current is flowing;38 the moving electron feels the magnetic field and is attracted toward the wire. But what happens if the system is viewed from a reference frame which moves such as to cancel out the motion of the exterior electron? The now-stationary electron feels no magnetic force, but, according to the Principle of Relativity, it must still be attracted to the wire. What happens is that the now-moving wire suffers a Special Relativistic effect known as 'length contraction'; the relative density of protons is thereby minutely increased, and so the wire acquires a net positive charge, and attracts the exterior electron, as before. The same overall outcome occurs in both reference frames - and this accords with the Principle of Relativity - but there has been some subtle switching between 'field energy' and kinetic energy, that is, between V and T. The method of Lagrangian Mechanics can be adapted for use in electromagnetism and in gravitation just because it has this whole-system outlook.

Despite the ambiguity between T and V, the former has a fundamental form, equation (6.14), and is always positive, whereas the latter is different for different systems, and has no universal form. This led some nineteenth-century physicists to think that T was in some sense more fundamental than V. Most notably, the great nineteenth-century physicist, James Clerk Maxwell (1831–79), wrote with regards to T, "...we are unable to conceive that any possible addition to our knowledge could explain the energy of motion [T] or give us a more perfect knowledge of it than we have already"39 whilst with regards to V, "...the progress of science is continually opening up new views of the forms and relations of different kinds of potential energy."40 Also, Heinrich Hertz (1857–94), (the first to detect radio waves), went so far as to suggest that there was, at an elemental level, only kinetic energy - in the form of microscopic motions - and that these hidden motions accounted for the effects known as V. (We make brief mention of this again at the end of Section (6.8).)

## 6.7 Noether’s Theorem, and the definition of energy

Let’s bypass T and V and consider the relationship of L directly on the generalized coordinates, L = L(q(t), q(t); t).41 We will now consider those cases in which V, and any external conditions, do not depend explicitly on time. Then, while we still have q = q(t) and q = q(t),42 nevertheless t will not occur explicitly in V or in the external conditions, and so t will also not occur in the argument of the function for L. Therefore we will have the special time-independent form, L = L(q(t), q(t)).

i i ˙ ˙

39 Maxwell J-C, The Theory of Heat, 1871, Dover Publications, (2001), p301.

40 The Theory of Heat, as above, p302.

41 This is an abbreviated way of writing L = L(q1, q2, ... qn; q1, q2, ... qn; t).

˙ ˙ ˙ 42 (These are, in fact, the very 'equations of motion' that we wish to solve in mechanics.)

We postulate that time is homogeneous - there are no absolute markers in it, and no times are more special than other times as regards the applicability of our laws of physics.43 Pertinent to our present discussion is the law of physics known as Hamilton’s Principle, and we find that as time is homogeneous then it should not matter what the absolute end-times of the action integral are. So, we could displace the whole action integral through a small constant time interval, ǫ, and this displacement should make no difference whatsoever to the outcome:

δ L(q(t), q(t)) dt = δ L(q(t), q(t)) dt = 0 (6.17)

i i i i ˙ ˙ ∫_{t_a}^{t_b} ∫_{t_a+ǫ}^{t_b+ǫ}

By definition, shifting the limits of integration through +ǫ is equivalent to shifting ('transforming') the time coordinate through –ǫ. Thus we arrive at:

δ L(q(t), q(t)) dt = δ L(q(t–ǫ), q(t–ǫ)) d(t–ǫ)

i i i i ˙ ˙ ∫_{t_a+ǫ}^{t_b+ǫ} ∫_{t_a}^{t_b} = δ L(q(t–ǫ), q(t–ǫ)) dt = 0 (6.18)

i i ∫_{t_a}^{t_b}

We could just as well say that we have a new time coordinate, say, τ = t–ǫ, and it hasn’t made any difference to anything. So far so unexceptionable - but it turns out that this is only the beginning.

A hundred years ago, the mathematician Emmy Noether (1882–1935) obtained an outstanding theorem with repercussions across the whole of field theory. Her theorem, in words, is that if the action integral has no explicit dependence on a given coordinate, q, or t, then it will be invariant with respect to certain infinitesimal transformations of this coordinate, and the system will then exhibit a symmetry or conservation law concerning this coordinate. A specific symmetry will arise for any 'absent' coordinate but here we consider the time coordinate.

We may begin to suspect that these infinitesimal transformations are the same as a variation (the δ-process, see Chapter 3, Section 3.7), but one aspect that rings a minatory warning is the fact that Noether has included t as one of the coordinates that may be transformed, whereas from Section 3.7 we remember that variation of the independent coordinate, t, is not allowed. More alarming still, Noether does not restrict the transformation of t to a fixed translation but allows ǫ to be a function44 of time - so we could have τ = t–ǫ(t). It is now not at all obvious that our translation in time will make no difference and maintain the homogeneity of time (we are, in effect, allowing time to become bunched up or stretched out between the end-times of the integral).

43 (Pretend we don’t know about the Big Bang.)

It turns out, however, that even in the case of such inconstant translations invariance of the action principle can be assured. There is one crucial thing that must be taken into account in this more general case: not only does L change, but dt changes also, and it is no longer sufficient for L on its own to be invariant but rather it is the whole product, L dt, which must be invariant. We can follow through the mathematics (Appendix A6.3) or jump straight to the result: for a system with time-independent external conditions, the action integral is invariant with respect to an infinitesimal translation in time, ǫ(t), provided that the following conservation rule applies:

d/dt (∂L/∂q̇_i) q̇_i – L = constant (6.19)

What is this mysterious left-hand side that is equal to a constant, in other words, it stays the same for all times? (As neither t_a nor t_b appear in (6.19) then the conservation rule is independent of these specific end-times.) Let’s begin to answer this by choosing our simplest time-independent case-study: T = ½ m q̇_i^2, V = V(q_i), and, by definition, L = T–V. Then ∂L/∂q̇_i = m q̇_i for all i, and so the left-hand side of (6.19) becomes:

m(q̇_i)^2 – L = 2T–L = T+V (6.20)

The constant on the right-hand side of equation (6.19) can then be identified with the right-hand side of equation (6.20), T+V, which in turn can be identified with E, the total energy. In other words, we have found that the total energy is a constant.

So, we have assumed time-independent conditions and out pops the result that the total energy, E, is conserved - the well-known 'law of the conservation of energy'. The emergence of a conservation law may appear unsurprising given that V and all the external conditions were taken to be time-independent, that is to say, 'conservative'; but remember that we have not brought in energy conservation as an extra condition but have deduced it, and only by asserting the validity of Hamilton’s Principle, and that time is homogeneous.45 What will emerge later (in the work of Hamilton, Chapter 7) is that [ (∂L/∂q̇_i) q̇_i - L] is a more general form for the total energy, and moreover it is not necessary that the total energy satisfies E = T+V. Indeed, there can arise mechanical systems which have terms which are linear rather than quadratic in q̇_i, or where T is more complicated than ½ m q̇_i^2. Such systems, if they are independent of time, still satisfy an energy conservation law but it takes the more general form of equation (6.19), which holds for any time-independent Lagrangian.

44 (albeit a function that is infinitesimal, continuous, and differentiable)

## 6.8 External conditions

Every now and again in mathematics, physics, or technology, somebody comes up with a new idea, technique, or gizmo, that is simple to state but is sheer genius. For example, we have Stevin’s 'Wreath of Spheres' (Chapter 2), Torricelli’s barometer, Pascal’s 'triangle', the Newcomen engine, Watt’s 'parallel motion', and so on. Lagrange’s method for dealing with the 'condition equations' - the 'method of Lagrange multipliers' - is one such gem. We deal with it in this section.

‘Conditions’ are functional relations, f(q_1, q_2, q_3, ...), between the generalized coordinates - examples include ‘constraint conditions’ (a block slides on a given surface without friction; a cord maintains a certain length; a body is rigid; and so on), and ‘kinematic conditions’ (a block slides down an inclined plane resting on a trolley, and meanwhile the whole trolley moves uniformly along tracks; a bicycle wheel spins about the axle at a constant rate and in a plane at right angles to the spin-axis; and so on). So far in this chapter we have only mentioned these ‘conditions’ in passing, as extra equations to be satisfied after the Lagrange Equations have been solved. But there is a way of incorporating the condition equations from the start - using the method of Lagrange multipliers. We explain the method in mathematical detail in Appendix A6.4.

45 In A 6.3 we have used a slightly different derivation to Lanczos in order to emphasize the link between E-conservation and the homogeneity of time.

The mathematical arguments are pretty, and the method of Lagrange multipliers enables us to solve otherwise insoluble problems, but we are also very impressed by the fact that the method means something physically. Now in Appendix A6.4 we show how the potential energy, V, has the extra conditions, ‘λf’, added on, and so we end up with a new potential...

potential energy, V_new = V + λf. However, Hamilton’s Principle applies in the usual way, and is sensitive to the whole of V_new in one go, and pays no heed to its separate components, ‘V’ and ‘λf’. The important physical meaning to extract is that no ultimate distinction can be made between potential energy and external conditions.46 This ties in with what we have claimed earlier (Chapters 4 and 5) - that ‘constraints’ and ‘kinematic conditions’ are due to forces, and these forces are ultimately indistinguishable from the applied forces (arising from the potential energy function). It also ties in with the insight derived from d’Alembert’s Principle (Section 5.4): there is no ultimate difference between an applied force and a ‘fictitious’ force (say, due to an accelerating reference frame). Finally, as we just learned in Section 6.6, Hamilton’s Principle is sensitive to the whole of T–V and not to T and V separately. We can therefore expand our previous remark and state that: no ultimate distinction can be made between potential energy, kinetic energy, and external conditions. We have come a long way from Newton’s absolute external force, causing an absolute acceleration, relative to an absolutely stationary and passive Space, and an absolute and passive Time.

There is even one more thing to say about the physical implications of ‘condition equations’. In Chapters 3 and 4 we learned that while the degrees of freedom are slippery to define yet they relate to the very essence of the given problem. However we also know that when there are conditions between coordinates, these coordinates are no longer independent of each other, and so the number of degrees of freedom has been reduced.

Optional extras For n generalized coordinates and m condition-equations the number of degrees of freedom is reduced from n to n–m. This can be demonstrated geometrically: the n generalized coordinates move within an n-dimensional abstract ‘space’ (the configuration space), however the m conditions reduce this to a more restricted (n–m)-dimensional ‘space’ within the original ‘space’.

46 (over sufficiently small length- and time-scales)

Although we have indicated that the method of Lagrange multipliers requires functional relations between coordinates, actually, it can also be used in the case of ‘non-holonomic’ conditions, such as: the walls of a gas container; a ball rolling on a surface; a spinning top; and others.47

Finally, in a totally original analysis, Lanczos48 shows that the Lagrange multipliers account for microscopic effects (the microscopic reactive forces that maintain the given constraints). The consequential motions, being microscopic, are ‘hidden’, and they fluctuate in time (are time-dependent), even while the macroscopic system may be conservative. Hertz (end of Section 6.6) wondered whether such ‘hidden’ motions were the underlying source of all force. In other words, he speculated that kinetic energy (rather than force, or potential energy) was the primitive element in physics.

## 6.9 Symmetries and conservation laws

There is an important kind of ‘condition’ which brings in great physical insight: the condition known as symmetry. If a system displays symmetry with respect to a given coordinate, q, then this means it remains unaltered after a ‘small’ change, δq, in that coordinate.49 Equivalently, if the system is symmetrical with respect to a certain q_i then it doesn’t depend on that q_i, that is, ∂L/∂q_i = 0 and q_i is known as an ‘ignored’ or ‘absent’ coordinate. (Note that L still depend on q_i_dot - or else we would have to concede that the system has one less degree of freedom than originally anticipated.)

For example, if a merry-go-round is symmetrical about its axis of rotation then the system does not identify any special angles, or, in other words, q = θ doesn’t occur in L. We say that space is ‘isotropic’ (the same in all directions). Likewise, if a brick can be displaced through a small translation, δx, and nothing in the world changes as a consequence, then the system does not identify any special positions, or, in other words, q = x doesn’t occur in L. We say that space is homogeneous (the same at all points).

47 Goldstein, H, Classical Mechanics, 2nd ed, page 12; Lanczos, page 146.

48 Lanczos, pp143–5.

49 This is a kind of symmetry known as a continuous symmetry, as opposed to a non-continuous symmetry such as the symmetry following reflection in a mirror.

Because of the Lagrange Equations, something special happens in the case of these symmetrical systems. If, say, it is the kth coordinate that is ignorable then L does not depend on q_k and so ∂L/∂q_k = 0 but the Lagrange Equation for q_k then implies: d/dt (∂L/∂q_k_dot) = 0 and thus ∂L/∂q_k_dot = constant (6.21)

We shall, in the next chapter, learn to identify ∂L/∂q_k_dot with the ‘momentum’, p_k, associated with q_k, but for now we note the important result: a symmetry leads to a conservation law; a system with translational symmetry leads to a conservation rule for momentum; and a system with rotational symmetry leads to a conservation rule for angular momentum (Noether’s Theorem, section 6.7).50

Everything we have just said for symmetries with respect to some position coordinate or other, q, applies equally well for a symmetry with respect to the time coordinate, t. In fact, we have met this case already. In Section (6.7) we considered a Lagrangian with no explicit dependence on time, and found that a symmetry - invariance of the system after a translation in time - meant that a conservation law emerged: the law of the conservation of energy. We can also argue this another way: as t doesn’t occur explicitly it is an ‘ignorable’ variable and may be eliminated from L; and as a consequence of carrying out this elimination a ‘condition equation’ is introduced - the very condition that energy is conserved (the maths is shown in Appendix A7.5).

Carl Jacobi (1804–51) tackled the problem of particle motion in this reduced form (that is, with the time coordinate eliminated51) and this led to Jacobi’s Principle in which ∫mvds must be minimized. (In other words, Jacobi had returned to Maupertuis’s Principle of Least Action from a hundred years earlier - see Chapter 2.) What Jacobi thereby determined was the path or ‘geodesic’ of a particle through space, but - as befits a model in which time has been eliminated - he determined nothing about the rate at which the particle moves along this path. (This motion in time can be reconstructed afterward by imposing the condition that energy is conserved.) Now in the special case where energy is conserved and there are no external forces (no V), it turns out that the path is straight, and the particle must move along this path with constant speed. Does this sound familiar? Yes - we have recovered the famous ‘law of inertia’, asserted (in so many words) by Leonardo da Vinci, Galileo, Descartes, and Newton: “A free particle moves [solely under its own inertia] in a straight line with constant speed”.

Even more impressive, Jacobi’s Principle can be extended and then leads to a generalized ‘law of inertia’: we take the free ‘particle’ to be the C-point of a mechanical system of arbitrary complexity and in n dimensions. This C-point moves along a world-line in an n-dimensional Riemannian space - and we find that the paths are the straightest lines in that Riemannian space - the ‘geodesics’ (see Section 3.6 for a mention of Riemannian spaces). We give two examples: (1) a particle is constrained to stay on a given two-dimensional curved surface, with no external forces; (2) in Einstein’s Theory of Gravitation, a planet moves in a Riemann space of four dimensions - spacetime - and its motion is governed by the ‘law of inertia’ with no external force of gravity. The only difference between these two examples is that in (2) the curvature of space is an actual property of the physical world,52 and not a consequence of this or that constraint.

Let us return to our discussions at the beginning of this section - to a consideration of symmetry. We can argue that the ‘law of inertia’ is upheld because of certain fundamental symmetries: the particle moves in a straight line because space is homogeneous and isotropic - there is no reason for it to prefer left or right; and it moves at constant speed because, in addition, time is homogeneous and isotropic53 - there is no reason for the particle to move faster or slower. But Lagrangian Mechanics is better: yes, these symmetries may apply, but there is no claim that they extend infinitely far. Even more important, the particle follows the ‘straightest’ path not only because of local symmetries, but because the ‘straightest’ path is also the ‘shortest’ path (between given end-points). And finally, the criterion ‘shortest’ path is more general - it still holds even when there are no symmetries, that is, even when there are external influences, and even when these external influences change in time.

50 (Note that, as Lagrangian Mechanics is always a local theory, so these rotations and translations must be ‘small’.)

51 It’s a bit more complicated than straightforward elimination: first the time is re-branded as the (n+1)th position coordinate, t = q_{n+1}. The time can therefore no longer serve as the independent variable, and all (n+1) ‘position’ coordinates are given instead as functions of some new parameter, say, τ. In so doing, it is found that the new Lagrangian depends on q_{n+1}_dot but not on q_{n+1} (the differentiation is with respect to τ). Thus q_{n+1} is an ignorable coordinate, and may be eliminated.

52 (the physical world that actually has a large gravitating body, the Sun, about which the planet orbits.)

53 We must be careful: macroscopically, time does not seem to be the same forward and backward; and the Big Bang seems to flag one time as more special than the rest.

## 6.10 Conclusions

The basic elements of Lagrangian Mechanics are the generalized coordinates, {q}, the Lagrangian function, L = T–V, and the time, t. For each new problem, or even for each new modelling of any one problem, the {q} are chosen afresh, and the functions T and V may change; and yet we have the remarkable finding that the Lagrange Equations always have the same form:

d/dt (∂L/∂q_i_dot) – ∂L/∂q_i = 0    i = 1,2,...,n

The invariance of these equations,54 and their near-universal applicability across the whole of physics, inspires our awe:

“Was it a God who wrote these signs Which soothe the inner tumult’s raging, Which fill the lonely heart with joy And, with mysteriously hidden might, Unriddle Nature’s forces all around?”

Goethe’s Faust55 (Faust gazing at the Macrocosmos)

Why are the Lagrange Equations invariant? In view of our discussion in Section 3.6 about differential geometry, that is, the absolute calculus, it is not surprising that the true invariant things are connected with infinitesimal changes of one quantity.

54 For example, under a change of generalized coordinates.

55 Johann Wolfgang von Goethe, Faust, Part One, “Study”.

relative to another, that is, with partial differential equations. Furthermore, the reason why these Equations are invariant is that they derive from an 'extremal' condition. But geometry alone cannot tell us which invariant topological features will have physical significance; it is only the physics that can answer why it is exactly 'action' that must be minimized.

There is no general, turn-the-handle, way of solving the Lagrange Equations, but by wisely choosing the coordinates - taking full advantage of any prior knowledge of super-structures, symmetries, constraints, and kinematic conditions - we can make the solution easier to obtain, or make a problem tractable as opposed to intractable.

We can argue this even more strongly - the increased tractability, mathematically-speaking, means that our wiser modelling of the system actually has more physical meaning - in other words, there really are such things as flexing beams, capacitors, spinning tops, wires with currents in them, gyroscopes, the Solar System, smoothly flowing rivers, and so on, and these things cannot, in general, be built up from the even simpler elements of particles, and forces-between-particles.

Wise modelling (incorporating physical knowledge into the system) also confers many computational advantages to Lagrangian Mechanics over Newton's force-mechanics. We have no need to determine the constraint-or reaction-forces (the tension in the cord, the reaction at a pivot, the internal forces maintaining the rigidity of a beam, and so on), or to determine the acceleration (a tricky vector quantity) for each particle in the system. We have only to deal with the single scalar function, L, and this function then determines the entire dynamics of the given system.

We still have the overarching requirement that Einstein's Principle of Relativity is to be upheld. This is to ensure that the same events will be present, regardless of the reference frame. Consider our earlier example of an electron being attracted to a wire: yes, this 'event' is the same in both the moving and stationary reference frames - the electron is always attracted to the wire. But what of the speed of approach of the electron, and the electron's mass, momentum, and kinetic energy - must these all be unchanged between reference frames? It turns out that the only dynamic system-property that is guaranteed invariance is the 'least δ(total action)'.

Now L is made up of the energy functions, T and V. We have made a good case for T having the fundamental form of a 'massy inertial factor' multiplying 'some-function-of-q²', but T may also include a constant term, and terms which are linear in the speed; and V usually depends just on position, but may also include a constant term, and terms which are linear in the speed. There is evidently much overlap in the definitions of T and V, so what then is the fundamental difference between them? It is well known that T relates to motions, while V relates to configurations, but, even more fundamentally, T relates to the energy of individual components, while V relates to whole-system energies. However, there is still the possibility of ambiguity between the two. For example, in earlier discussions (Sections 6.5 and 6.6), we pondered about how to classify rest-mass, being, on the one hand, a static store of energy (so it could be part of V), and, on the other hand, part of the identity of an individual component (so it could be classified as T). This ambiguity is consonant with the fact that L is sensitive to the whole of T–V, rather than to T and V taken separately. This allows for an interplay between T and V, an interplay that is borne out in nature, and that looks forward to modern physics (field theory, statistical mechanics, quantum theory, gravitation theory, and other disciplines). This is in contrast to Newtonian Mechanics, in which a particle is a particle is a particle - it never affects the space (Space and Time) that it inhabits.

The interplay between T and V occurs through time and not just at one time. So, time has 'configurational' aspects, and may sometimes be treated as a quasiposition coordinate (for example, time may be treated as the (n+1)th 'position' coordinate - see the footnote in Section 6.9). Thus we see, in Lagrangian Mechanics, a softening of the formerly sharp distinction between time and space. 'Time' always remains special, but, nevertheless, it is sometimes considered on an equal footing with the other 'position' coordinates - and in this way Lagrangian Mechanics foreshadows Einstein's Relativistic Mechanics, in which space and time are no longer independent of each other, but form a continuum known as spacetime.

The previous two paragraphs show us that Lagrangian Mechanics, and not Newtonian Mechanics, survives the transition to Einstein's Theories of Special and General Relativity. This is because Variational Mechanics (which includes Lagrangian Mechanics) is more 'philosophically correct'. Newtonian Mechanics postulates the prior existence of an absolute Space and Time whereas Einstein's Gravitation Theory takes the existence of the masses as givens; this is more correct when we reflect that all our observations really have been made in the presence of large gravitating masses. Also, the Variational Mechanics only makes local claims (and then the local pieces are joined together, with the condition that the joins must always be smooth). This also is more correct when we remember that 'far away' and 'long ago' are always conjecture, we can never have direct experience of them.

We have claimed near-universal rather than universal applicability for Lagrangian Mechanics - when does it fail? First, the method of Lagrangian Mechanics relies on everything being in functional form (see Sections 3.7 and 6.1). This requirement isn't always met, chiefly in the case of dissipative or frictional effects. However, these dissipative effects are due ultimately to microscopic interactions and, as Lanczos suggests, if we could obtain the functional forms from quantum theory, then variational methods would be applicable after all. Second, we must admit that most real-life problems are just too complicated for any analytical mechanics, whether Newtonian or Lagrangian (but Hamiltonian Mechanics, Chapter 7, will rescue some of these problems); then we must resort to curve-fitting, simulations, and other numerical methods.

In summary: Lagrangian Mechanics is a local theory; the time and position coordinates are not required to be independent of each other; T has inertial attributes; in fact, T and V have inertial attributes (and this accords with Einstein's finding that the mass-energy equivalence applies to all types of energy); the sharp division between geometry and external conditions has broken down; and 'energy' rather than 'force' is the true determinant of what happens. What we have not mentioned is that the Variational Mechanics also shows the way into Quantum Mechanics. This will be looked at in Chapter 7, which charts the next great advance, brought about by Hamilton.

**Chapter 7: Hamiltonian Mechanics**

"A dance to the music of time"

Nicolas Poussin, c. 1640

**7.1 Introduction: ask less from more**

The outstanding achievements of Lagrange are still not the last word in mechanics, and it was an Irish mathematical prodigy, William Rowan Hamilton, who, in the nineteenth century, took mechanics to its highest form. Hamilton was in awe of Lagrange, referring to him as a Shakespeare, and to the *Mécanique analytique* as a scientific poem; it was this work which attracted him to the topic of mechanics. Hamilton understood that even if the equations of motion were sometimes too difficult to solve one could nevertheless obtain important qualitative information - but only if one used the right choice of variables. His crucial advance was to discover what were the true, most telling, variables of mechanics.

We are familiar with the fact that the choice of variables (coordinates) can make all the difference to the tractability of a problem in mechanics. For example, a lever can be modelled as a near infinity of atoms, or as a 'lever arm' with just one position coordinate (the angle, θ) and the condition of 'rigidity'. We are inclined to think that the second version is an improvement over the first, but Hamilton realized that it is not always best to have the sparest, most economical description; sometimes even an increase in the number of coordinates can lead to greater insights.

Specifically, Hamilton brought in a doubling of the number of coordinates in any mechanics problem. This was no mere doubling of the number of dimensions (as would be the case in going from, say, a class of 25 children to a class of 50 children) but a doubling in the 'dimensionality' of the problem (as in going from 'children' to 'boys' and 'girls'). This analogy is useful but too simple, it doesn't demonstrate Hamilton's further requirement - that the two kinds of variable must be dynamically related. A better analogy is the example of a semiconductor crystal: an electron may occasionally be missing from a given lattice site, and then there will be a 'hole'. The positions of the holes are necessarily implied by the positions of the electrons but in practice the holes take on a life of their own, and it is useful to map both the electrons and the holes independently from each other. Another example has to do with the rings of Saturn. The rings are made up of particles, and for each particle we could tabulate both its radius and its speed even though if one is known the other is automatically determined. The data-table can then be trawled through as many times as necessary: we may, for example, look for all particles orbiting beyond a certain radius, and then on another occasion look for all particles with a speed below a certain threshold. However...

er, Hamilton’s Mechanics is so much more than a matter of picking out trends in a spreadsheet. Consider the suggestive analogy of a picture, which, as we know, is made up from an array of pixels. The amount of input data is doubled up by the simple expedient of viewing the picture with two eyes as opposed to one. In especially contrived stereographic pictures this doubling-up reveals previously hidden objects and a hidden depth. Likewise, we shall find that Hamilton’s doubling of variables leads to hidden depths of understanding.

## 7.2 The optical theory: extraordinary genius

We have learned in the previous chapters that Lagrangian Mechanics can be cast as a question in geometry (an ‘extremal’ condition in an abstract space). Similarly, Hamilton’s big advance was also inspired by geometry. When a youth of only seventeen years, Hamilton was musing on the problem of mathematically describing an ‘optical system’ – a system comprising a tight bundle of light-rays, starting at a common source, and then passing through various lenses and mirrors. His aim was to find the most general description possible of the optical system – one mathematical formulation that would serve whatever the arrangement of lenses or mirrors, and a formulation that was not to depend on the physical nature of light, that is, whether light is a wave or a particle. Hamilton came to the realization that as the rays pass through a system of this, that, or the other lenses and mirrors there are certain geometrical properties that remain unchanged: the ray-tips define a surface – a ‘surface of simultaneous arrival time’ – and if the rays leave such a ‘surface’ at right angles, then they will leave all subsequent ‘surfaces of simultaneous arrival time’ at right angles. (The same geometry applies for arrivals, that is, if the rays arrive at such a ‘surface’ at right angles, then they will arrive at all subsequent ‘simultaneous surfaces’ at right angles.) We call this geometric property the ‘ray property’. Given the exceedingly fast speed of light, this remarkable observation was available only to Hamilton’s mind’s eye, not to his actual eye.

Hamilton knew of Descartes’s epoch-changing discovery, made almost two hundred years earlier, that geometrical properties (Euclid’s axioms about planes, triangles, parallel lines, and so on) could be described purely algebraically, that is, by algebraic functions of coordinates. (It was, in fact, Descartes who brought in the very idea of ‘coordinates’.) This led Hamilton to wonder whether he could explain the ‘ray property’ purely by an algebraic function of coordinates. In mathematics, the geometric property of being a surface can indeed be expressed as a function: f_surface = 0, where f_surface is some algebraic function of the relevant surface coordinates. But Hamilton also appreciated that, because of Fermat’s Principle of Least Time, then one such ‘surface of simultaneous arrival time’ is functionally linked in some way to any subsequent ‘surface of simultaneous arrival time’. Now Fermat’s Principle dictates that the ‘distance’ (in time) between these surfaces has to be a minimum – but can this ‘minimum distance’ itself be reformulated as an algebraic function? Even for a mathematician of Hamilton’s calibre, this was a complicated thing to do. Hamilton was not daunted (he was barely 18 years old) and he looked at this complexity from an astoundingly audacious angle, as we now explain.

Using the Principle of Least Time, the ‘least-time distance’ for a light ray travelling between specified initial and final positions, q_i and q_f, can be determined. Having done this, the whole process can be repeated but for a slightly different choice of initial and final positions, say, q_i' and q_f'. A slightly different ‘least distance’ will ensue. This evaluation can be repeated again and again, in each case for slightly different end-state coordinates, and in each case yielding slightly different ‘distances’. The audacious question Hamilton asked was: could this ‘least distance’ be a function, perhaps even an algebraic function, of these end-state coordinates? The answer he found was – yes, the ‘distance’ was an algebraic function, let’s call it, f_distance, of the end-state coordinates, and the end-state coordinates alone. (Readers may be reminded of other scenarios in physics where there is function that depends only on end-coordinates: for example, a conservative potential energy field, or a ‘function-of-state’ in thermodynamics.)

Thus Hamilton came to the realization that there were two overarching algebraic functions that completely described the system of rays: first there was the function that determined the surface of simultaneous arrival time, f_surface, and then there was the function, f_distance, that was the ‘distance’ between two such surfaces. So far, this was genius of an ordinary kind; next came the hallmark of extraordinary genius – for Hamilton had to decide what coordinates to use, and then to find what the functions actually were.

## 7.3 Hamilton’s Mechanics – the right coordinates

The problem was first solved for the case of optics. Hamilton’s work in optics, “Theory of Systems of Rays”³, was published in 1828 and in it he introduced his ‘characteristic function’, so-called because it completely characterised the given optical system (the arrangement of mirrors and lenses, and the refractive indices of the media). This ‘characteristic function’ is the function, f_distance, and it depends only on the start and end position-coordinates of the light rays. In addition, Hamilton also determined the function, f_surface, (for example, for light rays which arrived in parallel at a concave mirror and were then focused to a point, f_surface was the function known as the ‘caustic surface’).

It would be over ten years before Hamilton’s work on mechanics appeared yet the seeds were already evident in the earlier Optical Theory, as Hamilton understood that the geometric ‘ray property’ arises in any system governed by a minimum principle. (It was later proved that the reverse is also true: a minimum principle arises from the ‘ray property’.) What was the minimum principle operating in mechanics? Hamilton knew it had to be a principle concerning action rather than time – after all, it was he who had brought in Hamilton’s Principle (see Chapter 6), a generalization of Lagrange’s Least Action Principle, itself an overhaul of Maupertuis’s Least Action Principle. But what is the equivalent of a ray when it comes to mechanics? Hamilton’s answer: it is the worldline of a single ‘whole-system’ point moving in an abstract multi-dimensional space. We have met this before: the whole-system point is the C-point (Chapter 6), and its worldline in configuration space is equivalent to a ‘ray’. In summary, in optics there are light rays in everyday 3-D space, influenced by lenses and mirrors, and subject to a principle of least time; while in mechanics there are fictitious C-points moving along ‘rays’ in the multi-dimensional abstract configuration space, and subject to a principle of least action: and in both optics and mechanics the ‘rays’ exhibit the ‘ray property’.

We must now consider what the functions, f_surface and f_distance, are in mechanics, and what coordinates should be used. Despite certain inescapable differences⁴ between optics and mechanics, the former is much simpler to visualize, and therefore offers valuable insights into mechanics. In the optical system, the ‘simultaneous surface’ really is a 2-D surface in everyday 3-D space⁵. In mechanics, the ‘surface of common action’ is a complicated thing known as a hyper-surface⁶, and yet by analogy with light it still has certain geometrical properties – the ‘ray property’ – as if it were an ordinary 2-D surface: in optics f_surface has two dimensions; in mechanics, f_surface has two dimensionalities (the terminology was explained in Section 7.1). This means that in mechanics f_surface depends on two coordinates for each particle on the ‘surface’. Finally, going back to the introduction section of this chapter, we suspect that these two surface-coordinates for one particle may be dynamically related to each other. So much for f_surface, for the moment.

In mechanics, the function f_distance links two ‘surfaces of common action’ together and so, like f_surface, it also must have a dimensionality of two (we have just one mechanics problem, and the dimensionality of a problem can’t change halfway through the analysis). However, this dual dimensionality comes about in a new way. We remember that f_distance arises from an integral, that is, an integral between two end-states. The requirement for a dimensionality of two is therefore most easily and suggestively satisfied if we adopt these start-and end-‘positions’ for each ‘ray’ as the dual coordinates for f_distance in mechanics.

To sum up, we have made a good case for f_distance depending on end-state coordinates, one on each of two different ‘surfaces’; and a good case for f_surface depending on two dynamically-related coordinates, both on one ‘surface’. It now remains to ascertain what exactly these two dynamically-related surface-coordinates will be. (Note that, in this mechanics scenario, there is also the possibility of f_distance and f_surface depending on the time, t.)

We are satisfied that f_distance depends on the two end-positions for each ray, but where will the duality come from in the case of f_surface? We cannot hope to bootstrap the modelling of physics from plausibility arguments alone – at some point a daring visionary has to come along and show us the way (and then their theory must make predictions, and then these must be tested against experiment). Nevertheless, there is just one more ‘plausibility argument’ that we can follow. Remember that in our explanation of the variational calculus (Section 3.7, Chapter 3) we stated that the integr

--- ³ Hamilton WR, “Theory of Systems of Rays”, Transactions of the Royal Irish Academy, vol 15(1828) pp 69–174.

⁴ For example, in optics, the light rays arrive at their ‘geometric surface’ at the same time, whereas, in mechanics, the C-points arrive at their ‘surfaces’ at different times but at common values for action.

⁵ (for example, for a point light-source, a spherical surface centred on this source receives the rays simultaneously and at right-angles)

⁶ A hyper-surface is a surface in more than two dimensions.

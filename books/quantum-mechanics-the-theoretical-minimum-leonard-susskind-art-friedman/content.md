# Quantum Mechanics The Theoretical Minimum Leonard Susskind Art Friedman Z Library

> 来源文件：pre_Quantum_Mechanics_The_Theoretical_Minimum_Leonard_Susskind_Art_Friedman_Z_Library.txt
> 字符数（约）：363536
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

QUANTUM MECHANICS The Theoretical Minimum LEONARD SUSSKIND and ART FRIEDMAN

From the bestselling author of The Theoretical Minimum, a DIY introduction to the math and science of quantum mechanics.

First he taught you classical mechanics. Now, physicist Leonard Susskind has teamed up with data engineer Art Friedman to present the theory and associated mathematics of the strange world of quantum mechanics.

In this follow-up to The Theoretical Minimum, Susskind and Friedman provide a lively introduction to this famously difficult field, which attempts to understand the behavior of sub-atomic objects through mathematical abstractions. Unlike other popularizations that shy away from quantum mechanics’ weirdness, Quantum Mechanics embraces the utter strangeness of quantum logic. The authors offer crystal-clear explanations of the principles of quantum states, uncertainty and time dependence, entanglement, and particle and wave states, among other topics, and each chapter includes exercises to ensure mastery of each area. Like The Theoretical Minimum, this volume runs parallel to Susskind’s eponymous Stanford University-hosted continuing education course.

An approachable yet rigorous introduction to a famously difficult topic, Quantum Mechanics provides a tool kit for amateur scientists to learn physics at their own pace.

Advance Praise for Quantum Mechanics

“This is quantum mechanics for real. This is the good stuff, the most mysterious aspects of how reality works, set out with crystalline clarity. If you want to know how physicists really think about the world, this book is the place to start.” — Sean Carroll, physicist, California Institute of Technology, and author of The Particle at the End of the Universe

“Susskind does a wonderful job of carefully going through in great detail the story of the simplest quantum system. As advertised, it’s the theoretical minimum, but a great place for someone to start on the road to a serious understanding of the mysteries of quantum physics.” — Peter Woit, Professor of Mathematics, Columbia University, and author of Not Even Wrong: The Failure of String Theory and the Search for Unity in Physical Law

About the Authors

Leonard Susskind has been the Felix Bloch Professor in Theoretical Physics at Stanford University since 1978. He is the author (with George Hrabovsky) of The Theoretical Minimum, as well as The Black Hole War and The Cosmic Landscape. He lives in Palo Alto, California.

Art Friedman is a data consultant who previously spent fifteen years at Hewlett-Packard as a software engineer. A lifelong student of physics, he lives in Mountain View, California.

This book is the second volume of the Theoretical Minimum series. The first volume, The Theoretical Minimum: What You Need to Know to Start Doing Physics, covered classical mechanics, which is the core of any physics education. We will refer to it from time to time simply as Volume I. This second book explains quantum mechanics and its relationship to classical mechanics. The books in this series run parallel to Leonard Susskind’s videos, available on the Web through Stanford University (see www.theoreticalminimum.com for a listing). While covering the same general topics as the videos, the books contain additional details, and topics that don’t appear in the videos.

Also by Leonard Susskind The Theoretical Minimum: What You Need To Know to Start Doing Physics (with George Hrabovsky)

The Black Hole War The Cosmic Landscape

Copyright © 2014 by Leonard Susskind and Art Friedman Published by Basic Books, A Member of the Perseus Books Group Books published by Basic Books are available at special discounts for bulk purchases in the United States by corporations, institutions, and other organizations. For more information, please contact the Special Markets Department at the Perseus Books Group, 2300 Chestnut Street, Suite 200, Philadelphia, PA 19103, or call (800) 810–4145, ext. 5000, or e-mail special.markets@perseusbooks.com.

ISBN 978-0-465-03667-7 A Member of the Perseus Books Group www.basicbooks.com s.com.

Designed by Art Friedman and Leonard Susskind Hilbert’s Place drawings were created by Margaret Sloan.

A CIP catalog record for this book is available from the Library of Congress.

ISBN (hardcover): 978-0-465-03667-7 ISBN (ebook): 978-0-465-08061-8 10 9 8 7 6 5 4 3 2 1 For our parents, who made it all possible: Irene and Benjamin Susskind George and Trudy Friedman Contents Prologue xv Introduction xix 1 Systems and Experiments 1 2 Quantum States 35 3 Principles of Quantum Mechanics 51 4 Time and Change 93 5 Uncertainty and Time Dependence 129 6 Combining Systems: Entanglement 149 7 More on Entanglement 183 8 Particles and Waves 235 9 Particle Dynamics 273 10 The Harmonic Oscillator 311

## Appendix

Preface Albert Einstein, who was in many ways the father of quan- tum mechanics, had a notorious love-hate relation with the subject. His debates with Niels Bohr—Bohr completely ac- ceptingofquantummechanicsandEinsteindeeplyskeptical— are famous in the history of science. It was generally ac- cepted by most physicists that Bohr won and Einstein lost.

Myownfeeling,Ithinksharedbyagrowingnumberofphysi- cists, is that this attitude does not do justice to Einstein’s views.

Both Bohr and Einstein were subtle men. Einstein tried very hard to show that quantum mechanics was inconsis- tent; Bohr, however, was always able to counter his argu- ments. But in his final attack Einstein pointed to something so deep, so counterintuitive, so troubling, and yet so ex- citing, that at the beginning of the twenty-first century it has returned to fascinate theoretical physicists. Bohr’s only answer to Einstein’s last great discovery—the discovery of entanglement—was to ignore it.

The phenomenon of entanglement is the essential fact of quantum mechanics, the fact that makes it so different from classical physics. It brings into question our entire un- xii PREFACE derstanding about what is real in the physical world. Our ordinary intuition about physical systems is that if we know everything about a system, that is, everything that can in principlebeknown,thenweknoweverythingaboutitsparts.

If we have complete knowledge of the condition of an auto- mobile,thenweknoweverythingaboutitswheels,itsengine, its transmission, right down to the screws that hold the up- holstery in place. It would not make sense for a mechanic to say, “I know everything about your car but unfortunately I can’t tell you anything about any of its parts.” But that’s exactly what Einstein explained to Bohr— in quantum mechanics, one can know everything about a system and nothing about its individual parts—but Bohr failed to appreciate this fact. I might add that generations of quantum textbooks blithely ignored it.

Everyone knows that quantum mechanics is strange, but I suspect very few people could tell you exactly in what way.

This book is a technical course of lectures on quantum me- chanics, but it is different than most courses or most text- books. The focus is on the logical principles and the goal is not to hide the utter strangeness of quantum logic but to bring it out into the light of day.

I remind you that this book is one of several that closely follow my Internet course series, the Theoretical Minimum.

My coauthor, Art Friedman, was a student in these courses.

The book benefited from the fact that Art was learning the subject and was therefore very sensitive to the issues that might be confusing to the beginner. During the course of writing, we had a lot of fun, and we’ve tried to convey some of that spirit with a bit of humor. If you don’t get it, ignore it.

Leonard Susskind WhenIcompletedmymaster’sdegreeincomputerscienceat Stanford, IcouldnothaveguessedthatI’dreturnsomeyears latertoattendLeonard’sphysicslectures. Myshort“career” in physics ended many years earlier, with the completion of my bachelor’s degree. But my interest in the subject has remained very much alive.

It appears that I have lots of company—the world seems filled with people who are genuinely, deeply interested in physics but whose lives have taken them in different direc- tions. This book is for all of us.

Quantum mechanics can be appreciated, to some degree, onapurelyqualitativelevel. Butmathematicsiswhatbrings itsbeautyintosharpfocus. Wehavetriedtomakethisamaz- ing body of work fully accessible to mathematically literate nonphysicists. I think we’ve done a fairly good job, and I hope you’ll agree.

No one completes a project like this without lots of help.

ThepeopleatBrockman,Inc.,havemadethebusinessendof things seem easy, and the production team at Perseus Books has been top-notch. My sincere thanks go to TJ Kelleher, Rachel King, and Tisse Takagi. It was our good fortune to work with a talented copy editor, John Searcy.

I’m grateful to Leonard’s (other) continuing education students for routinely raising thoughtful, provocative ques- tions, and for many stimulating after-class conversations.

xiv PREFACE Rob Colwell, Todd Craig, Monty Fros t, and John Nash offered constructive comments on the manuscript. Jeremy Branscome and Russ Bryan reviewed the entire manuscript in detail, and identified a number of problems.

I thank my family and friends for their kind support and enthusiasm. I especially thank my daughter, Hannah, for minding the store.

Besides her love, encouragement, insight, and sense of humor, my amazing wife, Margaret Sloan, contributed about a third of the diagrams and both Hilbert’s Place illustrations. Thanks, Maggie.

At the start of this project, Leonard, sensing my real motivation, remarked that one of the best ways to learn physics is to write about it. True, of course, but I had no idea how true, and I’m grateful that I had a chance to find out. Thanks a million, Leonard.

Art Friedman

Prologue

Art looks over his beer and says, “Lenny, let’s play a round of the Einstein-Bohr game.”

“OK, but I’m tired of losing. This time, you be Artstein and I’ll be L-Bore. You start.”

“Fair enough. Here’s my first shot: God doesn’t play dice. Ha-ha, L-Bore, that’s one point for me.”

“Not so fast, Artstein, not so fast. You, my friend, were the first one to point out that quantum theory is inherently probabilistic. Heh heh heh, that’s a two-pointer!”

“Well, I take it back.”

“You can’t.”

“I can.”

“You can’t.”

Few people realize that Einstein, in his 1917 paper, ”On the Quantum Theory of Radiation,” argues that the emission of gamma rays is governed by a statistical law.

A Professor and a Fiddler Walk into a Bar

Volume I was punctuated by short conversations between Lenny and George, fictional personas who were loosely based on two John Steinbeck characters. The setting for this volume of the Theoretical Minimum series is inspired by the stories of Damon Runyon. It’s a world filled with crooks, con artists, degenerates, smooth operators, and do-gooders. Plus a few ordinary folks, just trying to get through the day. The action unfolds at a popular watering hole called Hilbert’s Place.

Into this setting stroll Lenny and Art, two greenhorns from California who somehow got separated from their tour bus. Wish them luck. They will need it.

What to Bring

You don’t need to be a physicist to take this journey, but you should have some basic knowledge of calculus and linear algebra. You should also know something about the material covered in Volume I. It’s OK if your math is a bit rusty. We’ll review and explain much of it as we go, especially the material on linear algebra. Volume I reviews the basic ideas of calculus.

Don’t let our lighthearted humor fool you into thinking that we’re writing for airheads. We’re not. Our goal is to make a difficult subject “as simple as possible, but no simpler,” and we hope to have a little fun along the way. See you at Hilbert’s Place.

Margaret Sloan

Introduction

Classical mechanics is intuitive; things move in predictable ways. An experienced ballplayer can take a quick look at a fly ball, and from its location and its velocity, know where to run in order to be there just in time to catch the ball. Of course a sudden unexpected gust of wind might fool him, but that’s only because he didn’t take into account all the variables. There is an obvious reason why classical mechanics is intuitive: humans, and animals before them, have been using it many times every day for survival. But no one ever used quantum mechanics before the twentieth century. Quantum mechanics describes things so small that they are completely beyond the range of the human senses. So it stands to reason that we did not evolve an intuition for the quantum world. The only way we can comprehend it is by rewiring our intuitions with abstract mathematics. Fortunately, for some odd reason, we did evolve the capacity for such rewiring.

Ordinarily, we learn classical mechanics first, before even attempting quantum mechanics. But quantum physics is much more fundamental than classical physics. As far as we know, quantum mechanics provides an exact description of every physical system, but some things are massive enough that quantum mechanics can be reliably approximated by classical mechanics. That’s all that classical mechanics is: an approximation. From a logical point of view, we should learn quantum mechanics first, but very few physics teachers would recommend that. Even this course of lectures—the Theoretical Minimum series—began with classical mechanics. Nevertheless, in these quantum lectures, classical mechanics will play almost no role except near the end, well after the basic principles of quantum mechanics have been explained. I think this is really the right way to do it, not just logically but pedagogically as well. That way we don’t fall into the trap of thinking that quantum mechanics is basically just classical mechanics with a couple of new gimmicks thrown in. By the way, quantum mechanics is technically much easier than classical mechanics.

The simplest classical system—the basic logical unit for computer science—is the two-state system. Sometimes it’s called a bit. It can repre sent anything that has only two states: a coin that can show heads or tails, a switch that is on or off, or a tiny magnet that is constrained to point either north or south. As you might expect, especially if you studied the first lecture of Volume I, the theory of classical two-state systems is extremely simple—boring, in fact. In this volume, we’re going to begin with the quantum version of the two-state system, called a qubit, which is far more interesting. To understand it, we will need a whole new way of thinking—a new foundation of logic.

Lecture 1 Systems and Experiments

Lenny and Art wander into Hilbert’s Place.

Art: What is this, the Twilight Zone? Or some kind of fun house? I can’t get my bearings.

Lenny: Take a breath. You’ll get used to it.

Art: Which way is up?

## 1.1 Quantum Mechanics Is Different

What is so special about quantum mechanics? Why is it so hard to understand? It would be easy to blame the “hard mathematics,” and there may be some truth in that idea. But that can’t be the whole story. Lots of nonphysicists are able to master classical mechanics and field theory, which also require hard mathematics.

Quantum mechanics deals with the behavior of objects so small that we humans are ill equipped to visualize them at all. Individual atoms are near the upper end of this scale in terms of size. Electrons are frequently used as objects of study. Our sensory organs are simply not built to perceive the motion of an electron. The best we can do is to try to understand electrons and their motion as mathematical abstractions.

“So what?” says the skeptic. “Classical mechanics is filled to the brim with mathematical abstractions—point masses, rigid bodies, inertial reference frames, positions, momenta, fields, waves—the list goes on and on. There’s nothing new about mathematical abstractions.” This is actually a fair point, and indeed the classical and quantum worlds have some important things in common. Quantum mechanics, however, is different in two ways:

1. Different Abstractions. Quantum abstractions are fundamentally different from classical ones. For example, we’ll see that the idea of a state in quantum mechanics is conceptually very different from its classical counterpart. States are represented by different mathematical objects and have a different logical structure.

2. States and Measurements. In the classical world, the relationship between the state of a system and the result of a measurement on that system is very straightforward. In fact, it’s trivial. The labels that describe a state (the position and momentum of a particle, for example) are the same labels that characterize measurements of that state. To put it another way, one can perform an experiment to determine the state of a system. In the quantum world, this is not true. States and measurements are two different things, and the relationship between them is subtle and nonintuitive.

These ideas are crucial, and we’ll come back to them again and again.

## 1.2 Spins and Qubits

The concept of spin is derived from particle physics. Particles have properties in addition to their location in space. For example, they may or may not have electric charge, or mass. An electron is not the same as a quark or a neutrino. But even a specific type of particle, such as an electron, is not completely specified by its location. Attached to the electron is an extra degree of freedom called its spin. Naively, the spin can be pictured as a little arrow that points in some direction, but that naive picture is too classical to accurately represent the real situation. The spin of an electron is about as quantum mechanical as a system can be, and any attempt to visualize it classically will badly miss the point.

We can and will abstract the idea of a spin, and forget that it is attached to an electron. The quantum spin is a system that can be studied in its own right. In fact, the quantum spin, isolated from the electron that carries it through space, is both the simplest and the most quantum of systems.

The isolated quantum spin is an example of the general class of simple systems we call qubits—quantum bits—that play the same role in the quantum world as logical bits play in defining the state of your computer. Many systems—maybe even all systems—can be built up by combining qubits. Thus in learning about them, we are learning about a great deal more.

## 1.3 An Experiment

Let’s make these ideas concrete, using the simplest example we can find. In the first lecture of Volume I, we began by discussing a very simple deterministic system: a coin that can show either heads (H) or tails (T). We can call this a two-state system, or a bit, with the two states being H and T. More formally we invent a “degree of freedom” called σ that can take on two values, namely +1 and −1. The state H is replaced by σ = +1 and the state T by σ = −1.

Classically, that’s all there is to it.

is to the space of states. The system is either in state σ = +1 or σ = −1 and there is nothing in between. In quantum mechanics, we’ll think of this system as a qubit.

Volume I also discussed simple evolution laws that tell us how to update the state from instant to instant. The simplest law is just that nothing happens. In that case, if we go from one discrete instant (n) to the next (n+1), the law of evolution is σ(n+1) = σ(n). (1.1)

Let’s expose a hidden assumption that we were careless about in Volume I. An experiment involves more than just a system to study. It also involves an apparatus A to make measurements and record the results of the measurements. In the case of the two-state system, the apparatus interacts with the system (the spin) and records the value of σ. Think of the apparatus as a black box1 with a window that displays the result of a measurement. There is also a “this end up” arrow on the apparatus. The up-arrow is important because it shows how the apparatus is oriented in space, and its direction will affect the outcomes of our measurements. We begin by pointing it along the z axis (Fig. 1.1). Initially, we have no knowledge of whether σ = +1 or σ = −1. Our purpose is to do an experiment to find out the value of σ. Before the apparatus interacts with the spin, the window is blank (labeled with a question mark in our diagrams). After it measures σ, the window shows a +1 or a −1. By looking at the apparatus, we determine the value of σ. That whole process constitutes a very simple experiment designed to measure σ.

Now that we’ve measured σ, let’s reset the apparatus to neutral and, without disturbing the spin, measure σ again. Assuming the simple law of Eq. 1.1, we should get the same answer as we did the first time. The result σ = +1 will be followed by σ = +1. Likewise for σ = −1. The same will be true for any number of repetitions. This is good because it allows us to confirm the result of an experiment. We can also say this in the following way: The first interaction with the apparatus A prepares the system in one of the two states. Subsequent experiments confirm that state. So far, there is no difference between classical and quantum physics.

Now let’s do something new. After preparing the spin by measuring it with A, we turn the apparatus upside down and then measure σ again (Fig. 1.2). What we find is that if we originally prepared σ = +1, the upside down apparatus records σ = −1. Similarly, if we originally prepared σ = −1, the upside down apparatus records σ = +1. In other words, turning the apparatus over interchanges σ = +1 and σ = −1. From these results, we might conclude that σ is a degree of freedom that is associated with a sense of direction in space. For example, if σ were an oriented vector of some sort, then it would be natural to expect that turning the apparatus over would reverse the reading. A simple explanation is that the apparatus measures the component of the vector along an axis embedded in the apparatus. Is this explanation correct for all configurations?

If we are convinced that the spin is a vector, we would naturally describe it by three components: σ_x, σ_y, and σ_z. When the apparatus is upright along the z axis, it is positioned to measure σ_z.

So far, there is still no difference between classical physics and quantum physics. The difference only becomes apparent when we rotate the apparatus through an arbitrary angle, say π/2 radians (90 degrees). The apparatus begins in the upright position (with the up-arrow along the z axis). A spin is prepared with σ = +1. Next, rotate A so that the up-arrow points along the x axis (Fig. 1.3), and then make a measurement of what is presumably the x component of the spin, σ_x.

If in fact σ really represents the component of a vector along the up-arrow, one would expect to get zero. Why? Initially, we confirmed that σ was directed along the z axis, suggesting that its co

1“Black box” means we have no knowledge of what’s inside the apparatus or how it works. But rest assured, it does not contain a cat.

component along x must be zero. But we get a surprise when we measure σ_x: Instead of giving σ_x = 0, the apparatus gives either σ_x = +1 or σ_x = −1. A is very stubborn—no matter which way it is oriented, it refuses to give any answer other than σ_x = ±1. If the spin really is a vector, it is a very peculiar one indeed.

Nevertheless, we do find something interesting. Suppose we repeat the operation many times, each time following the same procedure, that is: • Beginning with A along the z axis, prepare σ_z = +1.

• Rotate the apparatus so that it is oriented along the x axis.

• Measure σ_x.

The repeated experiment spits out a random series of plus-ones and minus-ones. Determinism has broken down, but in a particular way. If we do many repetitions, we will find that the numbers of σ_x = +1 events and σ_x = −1 events are statistically equal. In other words, the average value of σ_x is zero. Instead of the classical result—namely, that the component of σ along the x axis is zero—we find that the average of these repeated measurements is zero.

Now let’s do the whole thing over again, but instead of rotating A to lie on the x axis, rotate it to an arbitrary direction along the unit vector n̂. Classically, if σ were a vector, we would expect the result of the experiment to be the component of σ along the n̂ axis. If n̂ lies at an angle θ with respect to z, the classical answer would be σ = cosθ. But as you might guess, each time we do the experiment we get σ = +1 or σ = −1. However, the result is statistically biased so that the average value is cosθ.

The situation is of course more general. We did not have to start with A oriented along z. Pick any direction m̂ and start with the up-arrow pointing along m̂. Prepare a spin so that the apparatus reads +1. Then, without disturbing the spin, rotate the apparatus to the direction n̂, as shown in Fig. 1.4. A new experiment on the same spin will give random results ±1, but with an average value equal to the cosine of the angle between n̂ and m̂. In other words, the average will be n̂ · m̂.

The quantum mechanical notation for the statistical average of a quantity Q is Dirac’s bracket notation ⟨Q⟩. We may summarize the results of our experimental investigation as follows: If we begin with A oriented along m̂ and confirm that σ = +1, then subsequent measurement with A oriented along n̂ gives the statistical result ⟨σ⟩ = n̂ · m̂.

What we are learning is that quantum mechanical systems are not deterministic—the results of experiments can be statistically random—but if we repeat an experiment many times, average quantities can follow the expectations of classical physics, at least up to a point.

## 1.4 Experiments Are Never Gentle

Every experiment involves an outside system—an apparatus—that must interact with the system in order to record a result. In that sense, every experiment is invasive. This is true in both classical and quantum physics, but only quantum physics makes a big deal out of it. Why is that so?

Classically, an ideal measuring apparatus has a vanishingly small effect on the system it is measuring. Classical experiments can be arbitrarily gentle and still accurately and reproducibly record the results of the experiment. For example, the direction of an arrow can be determined by reflecting light off the arrow and focusing it to form an image. While it is true that the light must have a small enough wavelength to form an image, there is nothing in classical physics that prevents the image from being made with arbitrarily weak light. In other words, the light can have an arbitrarily small energy content.

In quantum mechanics, the situation is fundamentally different. Any interaction that is strong enough to measure some aspect of a system is necessarily strong enough to disrupt some other aspect of the same system. Thus, you can learn nothing about a quantum system without changing something else.

This should be evident in the examples involving A and σ. Suppose we begin with σ_z = +1 along the z axis. If we measure σ_z again with A oriented along z, we will confirm the previous value. We can do this over and over without changing the result. But consider this possibility: Between successive measurements along the z axis, we turn A through 90 degrees, make an intermediate measurement, and turn it back to its original direction. Will a subsequent measurement along the z axis confirm the original measurement? The answer is no. The intermediate measurement along the x axis will leave the spin in a completely random configuration as far as the next measurement is concerned. There is no way to make the intermediate determination of the spin without completely disrupting the final measurement. One might say that measuring one component of the spin destroys the information about another component. In fact, one simply cannot simultaneously know the components of the spin along two different axes, not in a reproducible way in any case. There is something fundamentally different about the state of a quantum system and the state of a classical system.

## 1.5 Propositions

The space of states of a classical system is a mathematical set. If the system is a coin, the space of states is a set of two elements, H and T. Using set notation, we would write {H,T}. If the system is a six-sided die, the space of states has six elements labeled {1,2,3,4,5,6}. The logic of set theory is called Boolean logic. Boolean logic is just a formalized version of the familiar classical logic of propositions.

A fundamental idea in Boolean logic is the notion of a truth-value. The truth-value of a proposition is either true or false. Nothing in between is allowed. The related set theory concept is a subset. Roughly speaking, a proposition is true for all the elements in its corresponding subset and false for all the elements not in this subset. For example, if the set represents the possible states of a die, one can consider the proposition A: The die shows an odd-numbered face.

The corresponding subset contains the three elements {1,3,5}.

Another proposition states B: The die shows a number less than 4.

The corresponding subset contains the states {1,2,3}.

Every proposition has its opposite (also called its negation). For example, not A: The die does not show an odd-numbered face.

The subset for this negated proposition is {2,4,6}.

There are rules for combining propositions into more complex propositions, the most important being or, and, and not. We just saw an example of not, which gets applied to a single subset or proposition. And is straightforward, and applies to a pair of propositions. It says they are both true. Applied to two subsets, and gives the elements common to both, that is, the intersection of the two subsets. In the die example, the intersection of subsets A and B is the subset of elements that are both odd and less than 4. Fig. 1.5 uses a Venn diagram to show how this works.

The or rule is similar to and, but has one additional subtlety. In everyday speech, the word or is generally used in the exclusive sense—the exclusive version is true if one or the other of two propositions is true, but not both. However, Boolean logic uses the inclusive version of or, which is true if either or both of the propositions are true. Thus, according to the inclusive or, the proposition Albert Einstein discovered relativity or Isaac Newton was English is true. So is Albert Einstein discovered relativity or Isaac Newton was Russian.

The inclusive or is only wrong if both propositions are false. For example, Albert Einstein discovered America or Isaac Newton was Russian.

The inclusive or has a set theoretic interpretation as the union of two sets: it denotes the subset containing anything in either or both of the component subsets. In the die example, (A or B) denotes the subset {1,2,3,5}.

Space of States for a Single Die Subset A: Die shows an odd-numbered face. 1 3 5 Subset B: Die shows a number < 4. 2 4 6 Figure 1.5: An Example of the Classical model of State Space. Subset A represents the proposition “the die shows an odd-numbered face.” Subset B: “The die shows a number < 4.” Dark shading shows the intersection of A and B, which represents the proposition (A and B). White numbers are elements of the union of A with B, representing the proposition (A or B).

## 1.6 Testing Classical Propositions

Let’s return to the simple quantum system consisting of a single spin, and the various propositions whose truth we could test using the apparatus A. Consider the following two propositions: A: The z component of the spin is +1.

B: The x component of the spin is +1.

Each of these is meaningful and can be tested by orienting A along the appropriate axis. The negation of each is also meaningful. For example, the negation of the first proposition is not A: The z component of the spin is −1.

But now consider the composite propositions (A or B): The z component of the spin is +1 or the x component of the spin is +1.

(A and B): The z component of the spin is +1 and the x component of the spin is +1.

Consider how we would test the proposition (A or B). If spins behaved classically (and of course they don’t), we would proceed as follows: • Gently measure σ and record the value. If it is +1, we are finished: the proposition (A or B) is true. If σ_z is −1, continue to the next step.

• Gently measure σ_x. If it is +1, then the proposition (A or B) is true. If not, this means that neither σ_x nor σ_z was equal to +1, and (A or B) is false.

There is an alternative procedure, which is to interchange the order of the two measurements. To emphasize this reversal of ordering, we’ll call the new procedure (B or A): • Gently measure σ_x and record the value. If it is +1 we are finished: The proposition (B or A) is true. If σ_x is −1 continue to the next step.

• Gently measure σ_z. If it is +1, then (B or A) is true. If not, it means that neither σ_x nor σ_z was equal to +1, and (B or A) is false.

In classical physics, the two orders of operation give the same answer. The reason for this is that measurements can be arbitrarily gentle—so gentle that they do not affect the results of subsequent measurements. Therefore, the proposition (A or B) has the same meaning as the proposition (B or A).

## 1.7 Testing Quantum Propositions

Now we come to the quantum world that I described earlier. Let us imagine a situation in which someone (or something) unknown to us has secretly prepared a spin in the σ_z = +1 state. Our job is to use the apparatus A to determine whether the proposition (A or B) is true or false. We will try using the procedures outlined above.

We begin by measuring σ_z. Since the unknown agent has set things up, we will discover that σ_z = +1. It is unnecessary to go on: (A or B) is true. Nevertheless, we could test σ_x just to see what happens. The answer is unpredictable. We randomly find that σ_x = +1 or σ_x = −1. But neither of these outcomes affects the truth of proposition (A or B).

But now let’s reverse the order of measurement. As before, we’ll call the reversed procedure (B or A), and this time we’ll measure σ_x first. Because the unknown agent set the spin to +1 along the z axis, the measurement of σ_x is random. If it turns out that σ_x = +1, we are finished: (B or A) is true. But suppose we find the opposite result, σ_x = −1. The spin is oriented along the −x direction. Let’s pause here briefly, to make sure we understand what just happened. As a result of our first measurement, the spin is no longer in its original state σ_z = +1. It is in a new state, which is either σ_x = +1 or σ_x = −1. Please take a moment to let this idea sink in. We cannot overstate its importance.

Now we’re ready to test the second half of proposition (B or A). Rotate the apparatus A to the z axis and measure σ_z. According to quantum mechanics, the result will be randomly ±1. This means that there is a 25 percent probability that the experiment produces σ_x = −1 and σ_z = −1. In other words, with a probability of 1/4, we find that (B or A) is false; this occurs despite the fact that the hidden agent had originally made sure that σ_z = +1.

Evidently, in this example, the inclusive or is not symmetric. The truth of (A or B) may depend on the order in which we confirm the two propositions. This is not a small thing; it means not only that the laws of quantum physics are different from their classical counterparts, but that the very foundations of logic are different in quantum physics as well.

What about (A and B)? Suppose our first measurement yields σ_z = +1 and the second, σ_x = +1. This is of course a possible outcome. We would be inclined to say that (A and B) is true. But in science, especially in physics, the truth of a proposition implies that the proposition can be verified by subsequent observation. In classical physics, the gentleness of observation implies that subsequent experiments are unaffected and will confirm an earlier experiment. A coin that turns up Heads will not be flipped to Tails by the act of observing it—at least not classically. Quantum mechanically, the second measurement (σ_x = +1) ruins the possibility of verifying the first. Once σ_x has been prepared along the x axis, another measurement of σ_z will give a random answer. Thus (A and B) is not confirmable: the second piece of the experiment interferes with the possibility of confirming the first piece.

If you know a bit about quantum mechanics, you probably recognize that we are talking about the uncertainty principle. The uncertainty principle doesn’t apply only to position and momentum (or velocity); it applies to many pairs of measurable quantities. In the case of the spin, it applies to propositions involving two different components of σ. In the case of position and momentum, the two propositions we might consider are: A certain particle has position x.

That same particle has momentum p.

From these, we can form the two composite propositions: The particle has position x and the particle has momentum p.

The particle has position x or the particle has momentum p. Awkward as they are, both of these propositions have meaning in the English language, and in classical physics as well. However, in quantum physics, the first of these propositions is completely meaningless (not even wrong), and the second one means something quite different from what you might think. It all comes down to a deep logical difference between the classical and quantum concepts of the state of a system. Explaining the quantum concept of state will require some abstract mathematics, so let’s pause for a brief interlude on complex numbers and vector spaces. The need for complex quantities will become clear later on, when we study the mathematical representation of spin states.

## 1.8 Mathematical Interlude: Complex Numbers

Everyone who has gotten this far in the Theoretical Minimum series knows about complex numbers. Nevertheless, I will spend a few lines reminding you of the essentials. Fig. 1.6 shows some of their basic elements. A complex number z is the sum of a real number and an imaginary number. We can write it as z = x + iy, where x and y are real and i² = −1. Complex numbers can be added, multiplied, and divided by the standard rules of arithmetic. They can be visualized as points on the complex plane with coordinates x, y. They can also be represented in polar coordinates: z = re^{iθ} = r(cosθ + i sinθ). Adding complex numbers is easy in component form: just add the components. Similarly, multiplying them is easy in their polar form: Simply multiply the radii and add the angles: r₁e^{iθ₁} r₂e^{iθ₂} = (r₁r₂)e^{i(θ₁+θ₂)}. Every complex number z has a complex conjugate z* that is obtained by simply reversing the sign of the imaginary part. If z = x + iy = re^{iθ}, then z* = x − iy = re^{−iθ}. Multiplying a complex number and its conjugate always gives a positive real result: z*z = r². It is of course true that every complex conjugate is itself a complex number, but it’s often helpful to think of z and z* as belonging to separate “dual” number systems. Dual here means that for every z there is a unique z* and vice versa. There is a special class of complex numbers that I’ll call “phase-factors.” A phase-factor is simply a complex number whose r-component is 1. If z is a phase-factor, then the following hold: z*z = 1, z = e^{iθ}, z = cosθ + i sinθ.

## 1.9 Mathematical Interlude: Vector Spaces

1.9.1 Axioms For a classical system, the space of states is a set (the set of possible states), and the logic of classical physics is Boolean. That seems obvious and it is difficult to imagine any other possibility. Nevertheless, the real world operates along entirely different lines, at least whenever quantum mechanics is important. The space of states of a quantum system is not a mathematical set; it is a vector space. Relations between the elements of a vector space are different from those between the elements of a set, and the logic of propositions is different as well. Before I tell you about vector spaces, I need to clarify the term vector. As you know, we use this term to indicate an object in ordinary space that has a magnitude and a direction. Such vectors have three components, corresponding to the three dimensions of space. I want you to completely forget about that concept of a vector. From now on, whenever I want to talk about a thing with magnitude and direction in ordinary space, I will explicitly call it a 3-vector. A mathematical vector space is an abstract construction that may or may not have anything to do with ordinary space. It may have any number of dimensions from 1 to ∞ and it may have components that are integers, real numbers, or even more general things. The vector spaces we use to define quantum mechanical states are called Hilbert spaces. We won’t give the mathematical definition here, but you may as well add this term to your vocabulary. When you come across the term Hilbert space in quantum mechanics, it refers to the space of states. A Hilbert space may have either a finite or an infinite number of dimensions. In quantum mechanics, a vector space is composed of elements |A⟩ called ket-vectors or just kets. Here are the axioms we will use to define the vector space of states of a quantum system (z and w are complex numbers).

numbers):

## 1. The sum of any two ket-vectors is also a ket-vector:

|A(cid:3)+|B(cid:3) = |C(cid:3).

## 2. Vector addition is commutative:

|A(cid:3)+|B(cid:3) = |B(cid:3)+|A(cid:3).

## 3. Vector addition is associative:

(|A(cid:3)+|B(cid:3))+|C(cid:3) = |A(cid:3)+(|B(cid:3)+|C(cid:3)).

4. There is a unique vector 0 such that when you add it to any ket, it gives the same ket back: |A(cid:3)+0 = |A(cid:3).

## 5. Given any ket |A(cid:3), there is a unique ket −|A(cid:3) such that

|A(cid:3)+(−|A(cid:3)) = 0.

6. Given any ket |A(cid:3) and any complex number z, you can multiply them to get a new ket. Also, multiplication by a scalar is linear: |zA(cid:3) = z|A(cid:3) = |B(cid:3).

## 7. The distributive property holds:

z{|A(cid:3)+|B(cid:3)} = z|A(cid:3)+z|B(cid:3)

{z +w}|A(cid:3) = z|A(cid:3)+w|A(cid:3).

Axioms 6 and 7 taken together are often called linearity. Ordinary 3-vectors would satisfy these axioms except for one thing: Axiom 6 allows a vector to be multiplied by any complex number. Ordinary 3-vectors can be multiplied by real numbers (positive, negative, or zero) but multiplication by complex numbers is not defined. One can think of 3-vectors as forming a real vector space, and kets as forming a complex vector space. Our definition of ket-vectors is fairly abstract. As we will see, there are various concrete ways to represent ket-vectors as well.

1.9.2 Functions and Column Vectors Let’s look at some concrete examples of complex vector spaces. First of all, consider the set of continuous complex-valued functions of a variable x. Call the functions A(x). You can add any two such functions and multiply them by complex numbers. You can check that they satisfy all seven axioms. This example should make it obvious that we are talking about something much more general than three-dimensional arrows.

Two-dimensional column vectors provide another concrete example. We construct them by stacking up a pair of complex numbers, α1 and α2, in the form (cid:4) (cid:5)

and identifying this “stack” with the ket-vector |A(cid:3). The complex numbers α are the components of |A(cid:3). You can add two column vectors by adding their components: (cid:4) (cid:5) (cid:4) (cid:5) (cid:4) (cid:5)

α β α +β 1 1 1 1 + = .

α β α +β 2 2 2 2 Moreover, you can multiply the column vector by a complex number z just by multiplying the components, (cid:4) (cid:5) (cid:4) (cid:5)

α zα 1 1 z = .

α zα 2 2 Column vector spaces of any number of dimensions can be constructed. For example, here is a five-dimensional column vector: ⎛ ⎞ ⎜ ⎟ ⎜ α 2 ⎟ ⎜ ⎟ ⎜ α 3 ⎟.

⎝ ⎠ Normally, we do not mix vectors of different dimensionality.

1.9.3 Bras and Kets As we have seen, the complex numbers have a dual version: in the form of complex conjugate numbers. In the same way, a complex vector space has a dual version that is essentially the complex conjugate vector space. For every ket-vector |A(cid:3), there is a “bra” vector in the dual space, denoted by (cid:2)A|. Why the strange terms bra and ket? Shortly, we will define inner products of bras and kets, using expressions like (cid:2)B|A(cid:3) to form bra-kets or brackets. Inner products are extremely important in the mathematical machinery of quantum mechanics, and for characterizing vector spaces in general.

Bra vectors satisfy the same axioms as the ket-vectors, but there are two things to keep in mind about the correspondence between kets and bras: 1. Suppose (cid:2)A| is the bra corresponding to the ket |A(cid:3), and (cid:2)B| is the bra corresponding to the ket |B(cid:3). Then the bra corresponding to |A(cid:3)+|B(cid:3)

is (cid:2)A|+(cid:2)B|.

2. If z is a complex number, then it is not true that the bra corresponding to z|A(cid:3) is (cid:2)A|z. You have to remember to complex-conjugate. Thus, the bra corresponding to z|A(cid:3)

is (cid:2)A|z ∗ .

In the concrete example where kets are represented by column vectors, the dual bras are represented by row vectors, with the entries being drawn from the complex conjugate numbers. Thus, if the ket |A(cid:3) is represented by the column ⎛ ⎞ ⎜ ⎟ ⎜ α 2 ⎟ ⎜ ⎟ ⎜ α 3 ⎟, ⎝ ⎠ then the corresponding bra (cid:2)A| is represented by the row (cid:2) (cid:3)

α∗ α∗ α∗ α∗ α∗ .

1 2 3 4 5

1.9.4 Inner Products You are no doubt familiar with the dot product defined for ordinary 3-vectors. The analogous operation for bras and kets is the inner product. The inner product is always the product of a bra and a ket and it is written this way: (cid:2)B|A(cid:3).

The result of this operation is a complex number. The axioms for inner products are not too hard to guess:

## 1. They are linear:

(cid:2)C|{ |A(cid:3)+|B(cid:3) } = (cid:2)C|A(cid:3)+(cid:2)C|B(cid:3).

## 2. Interchanging bras and kets corresponds to complex conjugation:

(cid:2)B|A(cid:3) = (cid:2)A|B(cid:3)∗ .

Exercise 1.1: a) Using the axioms for inner products, pro {(cid:2)A|+(cid:2)B|}|C(cid:3) = (cid:2)A|C(cid:3)+(cid:2)B|C(cid:3).

b) Prove (cid:2)A|A(cid:3) is a real number.

In the concrete representation of bras and kets by row and column vectors, the inner product is defined in terms of components: (cid:2)B|A(cid:3) = β1* β2* β3* β4* β5* ⎛ ⎜ ⎜ ⎜ ⎜ ⎜ ⎝ α1 α2 α3 α4 α5 ⎞ ⎟ ⎟ ⎟ ⎟ ⎟ ⎠ = β1α1 + β2α2 + β3α3 + β4α4 + β5α5. (1.2)

The rule for inner products is essentially the same as for dot products: add the products of corresponding components of the vectors whose inner product is being calculated.

Exercise 1.2: Show that the inner product defined by Eq. 1.2 satisfies all the axioms of inner products.

Using the inner product, we can define some concepts that are familiar from ordinary 3-vectors: • Normalized Vector: A vector is said to be normalized if its inner product with itself is 1. Normalized vectors satisfy, (cid:2)A|A(cid:3) = 1.

For ordinary 3-vectors, the term normalized vector is usually replaced by unit vector, that is, a vector of unit length.

• Orthogonal Vectors: Two vectors are said to be orthogonal if their inner product is zero. |A(cid:3) and |B(cid:3) are orthogonal if (cid:2)B|A(cid:3) = 0.

This is the analog of saying that two 3-vectors are orthogonal if their dot product is zero.

1.9.5 Orthonormal Bases When working with ordinary 3-vectors, it is extremely useful to introduce a set of three mutually orthogonal unit vectors and use them as a basis to construct any vector. A simple example would be the unit 3-vectors that point along the x, y, and z axes. They are usually called ˆi, ˆj, and k ˆ. Each is of unit length and orthogonal to the others. If you tried to find a fourth vector orthogonal to these three, there wouldn’t be any—not in three dimensions anyway. However, if there were more dimensions of space, there would be more basis vectors. The dimension of a space can be defined as the maximum number of mutually orthogonal vectors in that space.

Obviously, there is nothing special about the particular axes x, y, and z. As long as the basis vectors are of unit length and are mutually orthogonal, they comprise an orthonormal basis.

The same principle is true for complex vector spaces. One can begin with any normalized vector and then look for a second one, orthogonal to the first. If you find one, then the space is at least two-dimensional. Then look for a third, fourth, and so on. Eventually, you may run out of new directions and there will not be any more orthogonal candidates. The maximum number of mutually orthogonal vectors is the dimension of the space. For column vectors, the dimension is simply the number of entries in the column.

Let’s consider an N-dimensional space and a particular orthonormal basis of ket-vectors labeled |i(cid:3). The label i runs from 1 to N. Consider a vector |A(cid:3), written as a sum of basis vectors: |A(cid:3) = ∑ αi |i(cid:3). (1.3)

The αi are complex numbers called the components of the vector, and to calculate them we take the inner product of both sides with a basis bra (cid:2)j|: (cid:2)j|A(cid:3) = ∑ αi (cid:2)j|i(cid:3). (1.4)

Next, we use the fact that the basis vectors are orthonormal. This implies that (cid:2)j|i(cid:3) = 0 if i is not equal to j, and (cid:2)j|i(cid:3) = 1 if i = j. In other words, (cid:2)j|i(cid:3) = δij. This makes the sum in Eq. 1.4 collapse to one term: (cid:2)j|A(cid:3) = αj. (1.5)

Thus, we see that the components of a vector are just its inner products with the basis vectors. We can rewrite Eq. 1.3 in the elegant form |A(cid:3) = ∑ |i(cid:3)(cid:2)i|A(cid:3).

Lecture 2 Quantum States

Art: Oddly enough, that beer made my head stop spinning. What state are we in?

Lenny: I wish I knew. Does it matter?

Art: It might. I don’t think we’re in California anymore.

## 2.1 States and Vectors

In classical physics, knowing the state of a system implies knowing everything that is necessary to predict the future of that system. As we’ve seen in the last lecture, quantum systems are not completely predictable. Evidently, quantum states have a different meaning than classical states. Very roughly, knowing a quantum state means knowing as much as can be known about how the system was prepared. In the last chapter, we talked about using an apparatus to prepare the state of a spin. In fact, we implicitly assumed that there was no more fine detail to specify or that could be specified about the state of the spin.

The obvious question to ask is whether the unpredictability is due to an incompleteness in what we call a quantum state. There are various opinions about this matter. Here is a sampling: • Yes, the usual notion of quantum state is incomplete. There are “hidden variables that, if only we could access them, would allow complete predictability. There are two versions of this view. In version A, the hidden variables are hard to measure but in principle they are experimentally available to us. In version B, because we are made of quantum mechanical matter and therefore subject to the restrictions of quantum mechanics, the hidden variables are, in principle, not detectable.

• No, the hidden variables concept does not lead us in a profitable direction. Quantum mechanics is unavoidably unpredictable. Quantum mechanics is as complete a calculus of probabilities as is possible. The job of a physicist is to learn and use this calculus.

I don’t know what the ultimate answer to this question will be, or even if it will prove to be a useful question. But for our purposes, it’s not important what any particular physicist believes about the ultimate meaning of the quantum state. For practical reasons, we will adopt the second view.

In practice, what this means for the quantum spin of Lecture 1 is that, when the apparatus A acts and tells us that σ_z = +1 or σ_z = −1, there is no more to know, or that can be known. Likewise, if we rotate A and measure σ_x = +1 or σ_x = −1, there is no more to know. Likewise for σ_y or any other component of the spin.

## 2.2 Representing Spin States

Now it’s time to try our hand at representing spin states using state-vectors. Our goal is to build a representation that captures everything we know about the behavior of spins. At this point, the process will be more intuitive than formal. We will try to fit things together the best we can, based on what we’ve already learned. Please read this section carefully. Believe me, it will pay off.

Let’s begin by labeling the possible spin states along the three coordinate axes. If A is oriented along the z axis, the two possible states that can be prepared correspond to σ_z = ±1. Let’s call them up and down and denote them by ket-vectors |u⟩ and |d⟩. Thus, when the apparatus is oriented along the z axis and registers +1, the state |u⟩ has been prepared.

On the other hand, if the apparatus is oriented along the x axis and registers −1, the state |l⟩ has been prepared. We’ll call it left. If A is along the y axis, it can prepare the states |i⟩ and |o⟩ (in and out). You get the idea.

The idea that there are no hidden variables has a very simple mathematical representation: the space of states for a single spin has only two dimensions. This point deserves emphasis:

All possible spin states can be represented in a two-dimensional vector space.

We could, somewhat arbitrarily,¹ choose |u⟩ and |d⟩ as the two basis vectors and write any state as a linear superposition of these two. We’ll adopt that choice for now. Let’s use the symbol |A⟩ for a generic state. We can write this as an equation,

|A⟩ = α_u |u⟩ + α_d |d⟩,

where α_u and α_d are the components of |A⟩ along the basis directions |u⟩ and |d⟩. Mathematically, we can identify the components of |A⟩ as

α_u = ⟨u|A⟩ α_d = ⟨d|A⟩. (2.1)

These equations are extremely abstract, and it is not at all obvious what their physical significance is. I am going to tell you right now what they mean: First of all, |A⟩ can represent any state of the spin, prepared in any manner. The components α_u and α_d are complex numbers; by themselves, they have no experimental meaning, but their magnitudes do. In particular, α_u*α_u and α_d*α_d have the following meaning:

• Given that the spin has been prepared in the state |A⟩, and that the apparatus is oriented along z, the quantity α_u*α_u is the probability that the spin would be measured as σ_z = +1. In other words, it is the probability of the spin being up if measured along the z axis.

• Likewise, α_d*α_d is the probability that σ_z would be down if measured.

The α values, or equivalently ⟨u|A⟩ and ⟨d|A⟩, are called probability amplitudes. They are themselves not probabilities. To compute a probability, their magnitudes must be squared. In other words, the probabilities for measurements of up and down are given by

P_u = ⟨A|u⟩⟨u|A⟩ P_d = ⟨A|d⟩⟨d|A⟩. (2.2)

Notice that I have said nothing about what σ_z is before it is measured. Before the measurement, all we have is the vector |A⟩, which represents the potential possibilities but not the actual values of our measurements.

Two other points are important: First, note that |u⟩ and |d⟩ are mutually orthogonal. In other words,

⟨u|d⟩ = 0 ⟨d|u⟩ = 0. (2.3)

The physical meaning of this is that, if the spin is prepared up, then the probability to detect it down is zero, and vice versa. This point It is so important, I’ll say it again: Two orthogonal states are physically distinct and mutually exclusive. If the spin is in one of these states, it cannot be (has zero probability to be) in the other one. This idea applies to all quantum systems, not just spin.

But don’t mistake the orthogonality of state-vectors for orthogonal directions in space. In fact, the directions up and down are not orthogonal directions in space, even though their associated state-vectors are orthogonal in state space.

The second important point is that for the total probability to come out equal to unity, we must have α*α_u + α*α_d = 1. (2.4)

This is equivalent to saying that the vector |A⟩ is normalized to a unit vector: ⟨A|A⟩ = 1.

This is a very general principle of quantum mechanics that extends to all quantum systems: the state of a system is represented by a unit (normalized) vector in a vector space of states. Moreover, the squared magnitudes of the components of the state-vector, along particular basis vectors, represent probabilities for various experimental outcomes.

## 2.3 Along the x Axis

We said before that we can represent any spin state as a linear combination of the basis vectors |u⟩ and |d⟩. Let’s try doing this now for the vectors |r⟩ and |l⟩, which represent spins prepared along the x axis. We’ll start with |r⟩. As you recall from Lecture 1, if A initially prepares |r⟩, and is then rotated to measure σ_z, there will be equal probabilities for up and down. Thus, α*α_u and α*α_d must both be equal to 1/2. A simple vector that satisfies this rule is |r⟩ = (1/√2) |u⟩ + (1/√2) |d⟩. (2.5)

There is some ambiguity in this choice, but as we will see later, it is nothing more than the ambiguity in our choice of exact directions for the x and y axes.

Next, let’s look at the vector |l⟩. Here is what we know: when the spin has been prepared in the left configuration, the probabilities for σ_z are again equal to 1/2. That is not enough to determine the values α*α_u and α*α_d, but there is another condition that we can infer. Earlier, I told you that |u⟩ and |d⟩ are orthogonal for the simple reason that, if the spin is up, it’s definitely not down. But there is nothing special about up and down that is not also true of right and left. In particular, if the spin is right, it has zero probability of being left. Thus, by analogy with Eq. 2.3, ⟨r|l⟩ = 0 ⟨l|r⟩ = 0.

This pretty much fixes |l⟩ in the form |l⟩ = (1/√2) |u⟩ − (1/√2) |d⟩. (2.6)

Exercise 2.1: Prove that the vector |r⟩ in Eq. 2.5 is orthogonal to vector |l⟩ in Eq. 2.6.

Again, there is some ambiguity in the choice of |l⟩. This is called the phase ambiguity. Suppose we multiply |l⟩ by any complex number z. That will have no effect on whether it is orthogonal to |r⟩, though in general the result will no longer be normalized (have unit length). But if we choose z = e^{iθ} (where θ can be any real number), then there will be no effect on the normalization because e^{iθ} has unit magnitude. In other words, α*α_u + α*α_d will remain equal to 1. Since a number of the form z = e^{iθ} is called a phase-factor, the ambiguity is called the phase ambiguity. Later, we will find out that no measurable quantity is sensitive to the overall phase-factor, and therefore we can ignore it when specifying states.

## 2.4 Along the y Axis

Finally, this brings us to |i⟩ and |o⟩, the vectors representing spins oriented along the y axis. Let’s look at the conditions they need to satisfy. First, ⟨i|o⟩ = 0. (2.7)

This condition states that in and out are represented by orthogonal vectors in the same way that up and down are. Physically, this means that if the spin is in, it is definitely not out.

There are additional restrictions on the vectors |i⟩ and |o⟩. Using the relationships expressed in Eqs. 2.1 and 2.2, and the statistical results of our experiments, we can write the following: ⟨o|u⟩⟨u|o⟩ = 1/2 ⟨o|d⟩⟨d|o⟩ = 1/2 ⟨i|u⟩⟨u|i⟩ = 1/2 ⟨i|d⟩⟨d|i⟩ = 1/2. (2.8)

In the first two equations, |o⟩ takes the role of |A⟩ from Eqs. 2.1 and 2.2. In the second two, |i⟩ takes that role. These conditions state that if the spin is oriented along y, and is then measured along z, it is equally likely to be up or down.

We should also expect that if the spin were measured along the x axis, it would be equally likely to be right or left. This leads to additional conditions: ⟨o|r⟩⟨r|o⟩ = 1/2 ⟨o|l⟩⟨l|o⟩ = 1/2 ⟨i|r⟩⟨r|i⟩ = 1/2 ⟨i|l⟩⟨l|i⟩ = 1/2. (2.9)

These conditions are sufficient to determine the form of the vectors |i⟩ and |o⟩, apart f From the phase ambiguity. Here is the result: |i⟩ = √½ |u⟩ + √½ |d⟩ |o⟩ = √½ |u⟩ − √½ |d⟩. (2.10)

Exercise 2.2: Prove that |i⟩ and |o⟩ satisfy all of the conditions in Eqs. 2.7, 2.8, and 2.9. Are they unique in that respect?

It’s interesting that two of the components in Eqs. 2.10 are imaginary. Of course, we’ve said all along that the space of states is a complex vector space, but until now we have not had to use complex numbers in our calculations. Are the complex numbers in Eqs. 2.10 a convenience or a necessity? Given our framework for spin states, there is no way around them. It’s somewhat tedious to demonstrate this, but the steps are straightforward. The following exercise gives you a road map. The need for complex numbers is a general feature of quantum mechanics, and we’ll see more examples as we go.

2.5. COUNTING PARAMETERS

Exercise 2.3: For the moment, forget that Eqs. 2.10 give us working definitions for |i⟩ and |o⟩ in terms of |u⟩ and |d⟩, and assume that the components α, β, γ, and δ are unknown: |i⟩ = α|u⟩ + β|d⟩ |o⟩ = γ|u⟩ + δ|d⟩.

a) Use Eqs. 2.8 to show that α*α = β*β = γ*γ = δ*δ = .

b) Use the above result and Eqs. 2.9 to show that α*β + αβ* = γ*δ + γδ* = 0.

c) Show that α*β and γ*δ must each be pure imaginary. If α*β is pure imaginary, then α and β cannot both be real. The same reasoning applies to γ*δ.

## 2.5 Counting Parameters

It’s always important to know how many independent parameters it takes to characterize a system. For example, the generalized coordinates we used in Volume I (referred to as q) each represented an independent degree of freedom. That approach freed us from the difficult job of writing explicit equations to describe physical constraints. Along similar lines, our next task is to count the number of physically distinct states there are for a spin. I will do it in two ways, to show that you get the same answer either way.

The first way is simple. Point the apparatus along any unit 3-vector n̂ and prepare a spin with σ = +1 along that axis. If σ = −1, you can think of the spin as being oriented along the −n̂ axis. Thus, there must be a state for every orientation of the unit 3-vector n̂. How many parameters does it take to specify such an orientation? The answer is of course two. It takes two angles to define a direction in three-dimensional space.

Now, let’s consider the same question from another perspective. The general spin state is defined by two complex numbers, α_u and α_d. That seems to add up to four real parameters, with each complex parameter counting as two real ones. But recall that the vector has to be normalized as in Eq. 2.4. The normalization condition gives us one equation involving real variables, and cuts the number of parameters down to three.

As I said earlier, we will eventually see that the physical properties of a state-vector do not depend on the overall phase-factor. This means that one of the three remaining parameters is redundant, leaving only two—the same as the number of parameters we need to specify a direction in three-dimensional space. Thus, there is enough freedom in the expression α_u |u⟩ + α_d |d⟩ to describe all the possible orientations of a spin, even though there are only two possible outcomes of an experiment along any axis.

## 2.6 Representing Spin States as Column Vectors

So far, we have been able to learn a lot by using the abstract forms of our state-vectors, that is, |u⟩ and |d⟩ and so forth. These abstractions help us focus on mathematical relationships without worrying about unnecessary details. However, soon we will need to perform detailed calculations on spin states, and for that we’ll need to write our state-vectors in column form. Because of “phase indifference,” the column representations are not unique, and we’ll try to choose the simplest and most convenient ones we can find.

As usual, we’ll start with |u⟩ and |d⟩. We need them to have unit length, and to be mutually orthogonal. A pair of columns that satisfies these requirements is |u⟩ = (1, 0)^T (2.11)

|d⟩ = (0, 1)^T. (2.12)

With these column vectors in hand, it will be easy to create column vectors for |r⟩ and |l⟩ using Eqs. 2.5 and 2.6, and for |i⟩ and |o⟩ using Eqs. 2.10. We’ll do that in the next lecture, where these results are needed.

## 2.7 Putting It All Together

We have covered a lot of ground in this lecture. Before moving on, let’s take stock of what we’ve done. Our goal was to synthesize what we know about spins and vector spaces. We figured out how to use vectors to represent spin states, and in the process we got a glimpse of the kind of information a state-vector contains (and does not contain!). Here is a brief outline of what we did:

• Based on our knowledge of spin measurements, we chose three pairs of mutually orthogonal basis vectors. Pairwise, we named them |u⟩ and |d⟩, |r⟩ and |l⟩, and |i⟩ and |o⟩. Because the basis vectors |u⟩ and |d⟩ represent physically distinct states, we were able to assert that they are mutually orthogonal. In other words, ⟨u|d⟩ = 0. The same holds for |r⟩ and |l⟩, and also for |i⟩ and |o⟩.

• We found that it takes two independent parameters to specify a spin state, and then we arbitrarily chose one of the orthogonal pairs, |u⟩ and |d⟩, as our basis vectors for representing all spin states—even though the two complex numbers in a state-vector require four real numbers to specify them. How did we get away with this? We were clever enough to notice that these four numbers are not all independent.4 The normalization constraint (total probability must equal 1) eliminates one independent parameter, and “phase indifference” (the physics of a state-vector is unaffected by its overall phase-factor) eliminates a second.

• Having chosen |u⟩ and |d⟩ as our main basis vectors, we figured out how to represent the other two pairs of basis vectors as linear combinations of |u⟩ and |d⟩, using additional orthogonality and probability-based constraints.

• Finally, we established a way to represent our main basis vectors as columns. This representation is not unique. In the next lecture, we’ll use our |u⟩ and |d⟩ column vectors to derive column vectors for the two other bases.

While achieving these concrete results, we got a chance to see some state-vector mathematics in action and learn something about how these mathematical objects correspond to physical spins. Although we will focus on spin, the same concepts and techniques apply to other quantum systems as well. Please take a little time to assimilate the material we’ve covered so far before moving on to the next lecture. As I said at the beginning, it will really pay off.

Lecture 3 Principles of Quantum Mechanics

Art: I’m not like you, Lenny. My brain just wasn’t built for quantum mechanics.

Lenny: Nah, mine wasn’t either. Just can’t really visualize the stuff. But I’ll tell you, I once knew a guy who thought just like an electron.

Art: What happened to him?

Lenny: Art, all I’m gonna tell you is that it sure wasn’t pretty.

Art: Hmm, I guess that gene didn’t fly.

No, we were not built to sense quantum phenomena; not the same way we were built to sense classical things like force and temperature. But we are very adaptable creatures and we’ve been able to substitute abstract mathematics for the missing senses that might have allowed us to directly visualize quantum mechanics. And eventually we do develop new kinds of intuition.

This lecture introduces the principles of quantum mechanics. In order to describe those principles, we’ll need some new mathematical tools. Let’s get started.

## 3.1 Mathematical Interlude: Linear Operators

3.1.1 Machines and Matrices

States in quantum mechanics are mathematically described as vectors in a vector space. Physical observables—the things that you can measure—are described by linear operators. We’ll take that as an axiom, and we’ll find out later (in Section 3.1.5) that operators corresponding to physical observables must be Hermitian as well as linear. The correspondence between operators and observables is subtle, and understanding it will take some effort.

Observables are the things you measure. For example, we can make direct measurements of the coordinates of a particle; the energy, momentum, or angular momentum of a system; or the electric field at a point in space. Observables are also associated with a vector space, but they are not state-vectors. They are the things you measure—σ would be an example—and they are represented by linear operators. John Wheeler liked to call such mathematical objects machines. He imagined a machine with two ports: an input port and an output port. In the input port you insert a vector, such as |A⟩. The gears turn and the machine delivers a result in the output port. This result is another vector, say |B⟩.

Let’s denote the operator by the boldface letter M (for “machine”). Here is the equation to express the fact that M acts on the vector |A⟩ to give |B⟩: M|A⟩ = |B⟩.

Not every machine is a linear operator. Linearity implies a few simple properties. To begin with, a linear operator must give a unique output for every vector in the space. We can imagine a machine that gives an output for some vectors, but just grinds up others and gives n Nothing. This machine would not be a linear operator. Something must come out for anything you put in.

The next property states that when a linear operator M acts on a multiple of an input vector, it gives the same multiple of the output vector. Thus, if M|A⟩ = |B⟩, and z is any complex number, then Mz|A⟩ = z|B⟩.

The only other rule is that, when M acts on a sum of vectors, the results are simply added together: M{|A⟩+|B⟩} = M|A⟩+M|B⟩.

To give a concrete representation of linear operators, we return to the row and column vector representation of bra- and ket-vectors that we used in Lecture 1. The row-column notation depends on our choice of basis vectors. If the vector space is N-dimensional, we choose a set of N orthonormal (orthogonal and normalized) ket-vectors. Let’s label them |j⟩, and their dual bra-vectors ⟨j|.

We are now going to take the equation M|A⟩ = |B⟩ and write it in component form. As we did in Eq. 1.3, we’ll represent an arbitrary ket |A⟩ as a sum over basis vectors: |A⟩ = Σ_j α_j |j⟩. Here, we’re using j as an index rather than i so you won’t be tempted to think that we’re talking about the in spin state.

Now, we’ll represent |B⟩ in the same way and plug both of these substitutions into M|A⟩ = |B⟩. That gives M Σ_j α_j |j⟩ = Σ_j β_j |j⟩.

The last step is to take the inner product of both sides with a particular basis vector ⟨k|, resulting in Σ_j ⟨k|M|j⟩ α_j = Σ_j β_j ⟨k|j⟩. (3.1)

To make sense of this result, remember that ⟨k|j⟩ is zero if j and k are not equal, and 1 if they are equal. That means that the sum on the right side collapses to a single term, β_k.

On the left side, we see a set of quantities Σ_j ⟨k|M|j⟩ α_j. We can abbreviate ⟨k|M|j⟩ with the symbol m_{kj}. Notice that each m_{kj} is just a complex number. To see why, think of M operating on |j⟩ to give some new ket-vector. The inner product of ⟨k| with this new ket-vector must be a complex number. The quantities m_{kj} are called the matrix elements of M and are often arranged into a square N × N matrix. For example, if N = 3, we can write the symbolic equation M = ⎛ m_{11} m_{12} m_{13} ⎞ ⎝ m_{21} m_{22} m_{23} ⎠ ⎝ m_{31} m_{32} m_{33} ⎠. (3.2)

This equation involves a slight abuse of notation that would give a purist indigestion. The left side is an abstract linear operator and the right side is a concrete representation of it in a particular basis. Equating them is sloppy but it should not cause confusion.

Now let’s revisit Eq. 3.1 and replace ⟨k|M|j⟩ with m_{kj}. We get Σ_j m_{kj} α_j = β_k. (3.3)

We can write this in matrix form as well. Eq. 3.4 becomes ⎛ m_{11} m_{12} m_{13} ⎞ ⎛ α_1 ⎞ ⎛ β_1 ⎞ ⎝ m_{21} m_{22} m_{23} ⎠ ⎝ α_2 ⎠ = ⎝ β_2 ⎠. (3.4)

⎝ m_{31} m_{32} m_{33} ⎠ ⎝ α_3 ⎠ ⎝ β_3 ⎠

You’re probably familiar with the rule for matrix multiplication, but I will remind you just in case. To compute the first entry on the right, β_1, take the first row of the matrix and “dot” it into the α column: β_1 = m_{11} α_1 + m_{12} α_2 + m_{13} α_3.

For the second entry, dot the second row of the matrix with the α column: β_2 = m_{21} α_1 + m_{22} α_2 + m_{23} α_3.

And so on. If you are not familiar with matrix multiplication, run to your computer and look it up right away. It’s a crucial part of our tool kit, and I will assume you know it from now on.

There are both advantages and disadvantages to representing vectors and linear operators concretely with columns, rows, and matrices (known collectively as components). The advantages are obvious. Components provide a completely explicit set of arithmetic rules for working the machine. The disadvantage is that they depend on a specific choice of basis vectors. The underlying relationships between vectors and operators is independent of the particular basis we choose, and the concrete representation obscures that fact.

3.1.2 Eigenvalues and Eigenvectors

In general, when a linear operator acts on a vector, it will change the direction of the vector. This means that what comes out of the machine will not just be the input vector multiplied by a number. But for a particular linear operator, there will be certain vectors whose directions are the same when they come out as they were when they went in. These special vectors are called eigenvectors. The definition of an eigenvector of M is a vector |λ⟩ such that M|λ⟩ = λ|λ⟩. (3.5)

The double use of λ is admittedly a little confusing. First of all, λ (as opposed to |λ⟩) is a number—generally a complex one, but still a number. On the other hand, |λ⟩ is a ket-vector. Furthermore, it is a ket with a very special relationship to M. When |λ⟩ is fed into the machine M, all that happens is that it gets multiplied by the number λ. I’ll gi Let me give you an example. If M is the 2×2 matrix 1 2 2 1 then it’s easy to see that the vector just gets multiplied by 3 when M acts on it. Try it out. M also happens to have another eigenvector: −1 When M acts on this eigenvector, it multiplies the vector by a different number, namely −1. On the other hand, if M acts on the vector the vector is not simply multiplied by a number. M alters the direction of the vector as well as its magnitude.

Just as the vectors that get multiplied by numbers when M acts on them are called eigenvectors of M, the constants that multiply them are called eigenvalues. In general, the eigenvalues are complex numbers. Here is an example that you can work out for yourself. Take the matrix 0 −1 M = 1 0 and show that the vector is an eigenvector with eigenvalue −i.

Linear operators can also act on bra-vectors. The notation for multiplying ⟨B| by M is ⟨B|M.

I will keep the discussion short by telling you the rule for this type of multiplication. It is most simple in component form.

Remember that bra-vectors are represented in component form as row vectors. For example, the bra ⟨B| might be represented by ⟨B| = β₁* β₂* β₃* .

The rule is again just matrix multiplication. With a slight abuse of notation, ⟨B|M = β₁* β₂* β₃* m₁₁ m₁₂ m₁₃ m₂₁ m₂₂ m₂₃ . (3.6)

m₃₁ m₃₂ m₃₃ 3.1.3 Hermitian Conjugation You might think that if M|A⟩ = |B⟩ then ⟨A|M = ⟨B|, but if you do you are wrong. The problem is complex conjugation. Even when Z is just a complex number, if Z|A⟩ = |B⟩, it is not generally true that ⟨A|Z = ⟨B|. You have to complex-conjugate Z when going from kets to bras: ⟨A|Z* = ⟨B|. Of course, if Z happens to be a real number, then complex conjugation has no effect—every real number is equal to its own complex conjugate.

What we need is a concept of complex conjugation for operators. Let’s look at the equation M|A⟩ = |B⟩ in component notation, mⱼᵢ αᵢ = βⱼ , and form its complex conjugate, mⱼᵢ* αᵢ* = βⱼ* .

We would like to write this equation in matrix form, using bras instead of kets. In doing this, we have to remember that bra-vectors are represented by rows, not columns. For the result to work out correctly, we also need to rearrange the complex conjugate elements of the matrix M. The notation for this rearrangement is M†, as explained below. Our new equation is ⟨A|M† = α₁* α₂* α₃* m₁₁* m₂₁* m₃₁* m₁₂* m₂₂* m₃₂* . (3.7)

m₁₃* m₂₃* m₃₃* Look carefully at the difference between the matrix in this equation and the matrix in Eq. 3.6. You will see two differences. The most obvious is the complex conjugation of each element, but you can also see a difference in the element indices. For example, where you see m₂₃ in Eq. 3.6, you see m₃₂* in Eq. 3.7. In other words, the rows and columns have been interchanged.

When we change an equation from the ket form to the bra form, we must modify the matrix in two steps:

## 1. Interchange the rows and the columns

## 2. Complex-conjugate each matrix element

In matrix notation, interchanging rows and columns is called transposing and is indicated by a superscript T. Thus, the transpose of the matrix M is m₁₁ m₁₂ m₁₃ m₁₁ m₂₁ m₃₁ m₂₁ m₂₂ m₂₃ = m₁₂ m₂₂ m₃₂ .

m₃₁ m₃₂ m₃₃ m₁₃ m₂₃ m₃₃ Notice that transposing a matrix flips it about the main diagonal (the diagonal from the upper left to the lower right). The complex conjugate of a transposed matrix is called its Hermitian conjugate, denoted by a dagger. You could think of the dagger as a hybrid of the star-notation used in complex conjugation and the T used in transposition. In symbols, M† = (Mᵀ)* To summarize: if M acts on the ket |A⟩ to give |B⟩, then it follows that M† acts on the bra ⟨A| to give ⟨B|. In symbols: If M|A⟩ = |B⟩, then ⟨A|M† = ⟨B|.

3.1.4 Hermitian Operators Real numbers play a special role in physics. The results of any measurements are real numbers. Sometimes, we measure two quantities, put them together with an i (forming a complex number), and call this number the result of a measurement. But it’s actually just a way of combining two real measurements. If we want to be pedantic, we might say that observable quantities are equal to their own complex conjugates. That’s of course just a fancy way of saying they are real. We are going to find out very soon that quantum mechanical observables are represented by linear operators. What kind of linear operators? The kind that are the closest thing to a real operator. Observables 在量子力学中，可观测量由线性算符表示，这些算符等于它们自身的厄米共轭。它们被称为厄米算符，以法国数学家查尔斯·埃尔米特命名。厄米算符满足性质 M = M†。

用矩阵元素表示，这可以写成 m_ji = m_ij*。

换句话说，如果你将一个厄米矩阵沿主对角线翻转，然后取其复共轭，结果与原矩阵相同。厄米算符（和矩阵）具有一些特殊性质。第一个性质是它们的特征值都是实数。我们来证明它。

假设 λ 和 |λ⟩ 代表厄米算符 L 的一个特征值和相应的特征向量。用符号表示， L|λ⟩ = λ|λ⟩。

那么，根据厄米共轭的定义， ⟨λ|L† = ⟨λ|λ*。

然而，由于 L 是厄米的，它等于 L†。因此，我们可以将这两个方程重写为 L|λ⟩ = λ|λ⟩ (3.8)

和 ⟨λ|L = ⟨λ|λ*。 (3.9)

现在，用 ⟨λ| 乘方程 3.8，用 |λ⟩ 乘方程 3.9。它们变成 ⟨λ|L|λ⟩ = λ ⟨λ|λ⟩ 和 ⟨λ|L|λ⟩ = λ* ⟨λ|λ⟩。

显然，要使这两个方程都成立，λ 必须等于 λ*。换句话说，λ（因此任何厄米算符的特征值）必须是实数。

我们现在来介绍基本的数学定理——我称之为基本定理——它是量子力学的基础。基本思想是，量子力学中的可观测量由厄米算符表示。这是一个非常简单的定理，但极其重要。我们可以更精确地表述如下：

基本定理 • 厄米算符的特征向量构成一个完备集。这意味着该算符能生成的任何向量都可以展开为其特征向量的和。

• 如果 λ₁ 和 λ₂ 是厄米算符的两个不相等的特征值，那么相应的特征向量是正交的。

• 即使两个特征值相等，相应的特征向量也可以选择为正交的。这种情况，即两个不同的特征向量具有相同的特征值，有一个名称：称为简并。当两个算符具有共同的特征向量时，就会出现简并，如第 5.1 节所述。

可以将基本定理总结如下：厄米算符的特征向量构成一个正交归一基。我们来证明它，从第二个要点开始。

根据特征向量和特征值的定义，我们可以写出 L|λ₁⟩ = λ₁|λ₁⟩ L|λ₂⟩ = λ₂|λ₂⟩。

现在，利用 L 是厄米的（它自身的厄米共轭）这一事实，我们可以将第一个方程翻转成一个左矢方程。因此， ⟨λ₁|L = λ₁⟨λ₁| L|λ₂⟩ = λ₂|λ₂⟩。

现在，技巧应该很明显了，但我还是详细说明一下。取第一个方程并与 |λ₂⟩ 形成内积。然后，取第二个方程并与 ⟨λ₁| 形成内积。结果是 ⟨λ₁|L|λ₂⟩ = λ₁⟨λ₁|λ₂⟩ ⟨λ₁|L|λ₂⟩ = λ₂⟨λ₁|λ₂⟩。

通过相减，我们得到 (λ₁ - λ₂)⟨λ₁|λ₂⟩ = 0。

因此，如果 λ₁ 和 λ₂ 不同，内积 ⟨λ₁|λ₂⟩ 必须为零。换句话说，这两个特征向量必须是正交的。

接下来，我们来证明即使 λ₁ = λ₂，两个特征向量也可以选择为正交的。假设 L|λ₁⟩ = λ|λ₁⟩ L|λ₂⟩ = λ|λ₂⟩。 (3.10)

换句话说，有两个不同的特征向量具有相同的特征值。很明显，这两个特征向量的任何线性组合也是具有相同特征值的特征向量。有了这种自由度，总是可以找到两个正交的线性组合。

我们来看看如何做。考虑这两个特征向量的任意线性组合： |A⟩ = α|λ₁⟩ + β|λ₂⟩。

在两边作用 L，我们得到 L|A⟩ = αL|λ₁⟩ + βL|λ₂⟩， L|A⟩ = αλ|λ₁⟩ + βλ|λ₂⟩， 最终 L|A⟩ = λ(α|λ₁⟩ + β|λ₂⟩) = λ|A⟩。

这个方程证明，|λ₁⟩ 和 |λ₂⟩ 的任何线性组合也是 L 的特征向量，具有相同的特征值。根据假设，这两个向量是线性无关的——否则，它们就不会代表不同的态。我们还假设它们张成 L 的特征值为 λ 的特征向量子空间。有一个直接的过程，称为格拉姆-施密特过程，用于在给定一组张成子空间的独立向量的情况下，找到子空间的正交归一基。用简单的英语来说，我们可以通过将它们写成 |λ₁⟩ 和 |λ₂⟩ 的线性组合来找到两个正交归一的特征向量。我们概述 the Gram-Schmidt procedure below, in Section 3.1.6.

The final part of the theorem states that the eigenvectors are complete. In other words, if the space is N-dimensional, there will be N orthonormal eigenvectors. The proof is easy and I will leave it to you.

Exercise 3.1: Prove the following: If a vector space is N-dimensional, an orthonormal basis of N vectors can be constructed from the eigenvectors of a Hermitian operator.

3.1.6 The Gram-Schmidt Procedure Sometimes we encounter a set of linearly independent eigenvectors that do not form an orthonormal set. This typically happens when a system has degenerate states—distinct states that have the same eigenvalue. In that situation, we can always use the linearly independent vectors we have, to create an orthonormal set that spans the same space. The method is the Gram-Schmidt procedure I alluded to earlier.

Fig. 3.1 illustrates how it works for the simple case of two linearly independent vectors. We start with the two vectors V⃗₁ and V⃗₂, and from these we construct two orthonormal vectors, v̂₁ and v̂₂.

Figure 3.1: The Gram-Schmidt Procedure. Given two linearly independent vectors, V⃗₁ and V⃗₂, that are not necessarily orthogonal, we can construct two orthonormal vectors, v̂₁ and v̂₂. V⃗₂⊥ is an intermediate result used in the construction process. We can extend this procedure to larger sets of linearly independent vectors.

The first step is to divide V⃗₁ by its own length, |V⃗₁|, which gives us a unit vector parallel to V⃗₁. We’ll call that unit vector v̂₁, and v̂₁ becomes the first vector in our orthonormal set. Next, we project V⃗₂ onto the direction of v̂₁ by forming the inner product ⟨V⃗₂|v̂₁⟩. Now, we subtract ⟨V⃗₂|v̂₁⟩ from V⃗₂. We’ll call the result of this subtraction V⃗₂⊥. You can see in Fig. 3.1 that V⃗₂⊥ is orthogonal to v̂₁. Lastly, we divide V⃗₂⊥ by its own length to form the second member of our orthonormal set, v̂₂. It should be clear that we can extend this procedure to larger sets of linearly independent vectors in more dimensions. For instance, if we had a third linearly independent vector, say V⃗₃, pointing out of the page, we would subtract its projections onto each of the unit vectors v̂₁ and v̂₂, and then divide the result by its own length.¹

## 3.2 The Principles

We are now fully prepared to state the principles of quantum mechanics, so without further ado, let’s do it.

The principles all involve the idea of an observable, and they presuppose the existence of an underlying complex vector space whose vectors represent system states. In this lecture, we present the four principles that do not involve the evolution of state-vectors with time. In Lecture 4, we will add a fifth principle that addresses the time development of system states.

An observable could also be called a measurable. It’s a thing that you can measure with a suitable apparatus. Earlier, we spoke about measuring the components of a spin, σₓ, σᵧ, and σᵤ. These are examples of observables. We’ll come back to them, but first let’s look at the principles: • Principle 1: The observable or measurable quantities of quantum mechanics are represented by linear operators L.

I realize that this is the kind of hopelessly abstract statement that makes people give up on quantum mechanics and take up surfing instead. Don’t worry—its meaning will become clear by the end of the lecture. We’ll soon see that L must also be Hermitian. Some authors regard this as a postulate, or basic principle. We have chosen instead to derive it from the other principles. The end result is the same either way: the operators that represent observables are Hermitian.

• Principle 2: The possible results of a measurement are the eigenvalues of the operator that represents the observable. We’ll call these eigenvalues λᵢ. The state for which the result of a measurement is unambiguously λᵢ is the corresponding eigenvector |λᵢ⟩. Don’t unpack your surfboard just yet.

Here’s another way to say it: if the system is in the eigenstate |λᵢ⟩, the result of a measurement is guaranteed to be λᵢ.

• Principle 3: Unambiguously distinguishable states are represented by orthogonal vectors.

• Principle 4: If |A⟩ is the state-vector of a system, and the observable L is measured, the probability to observe value λᵢ is P(λᵢ) = ⟨A|λᵢ⟩⟨λᵢ|A⟩. (3.11)

I’ll remind you that the λᵢ are the eigenvalues of L, and |λᵢ⟩ are the corresponding eigenvectors.

These brief statements a These ideas are hardly self-explanatory, and we’ll need to flesh them out. For the moment, let’s accept the first item, namely that every observable is identified with a linear operator. We can already begin to see that an operator is a way of packaging up states along with their eigenvalues, which are the possible results of measuring those states. These ideas should become clear as we move forward.

Let’s recall some important points from our earlier discussion of spins. First of all, the result of a measurement is generally statistically uncertain. However, for any given observable, there are particular states for which the result is absolutely certain. For example, if the spin-measuring apparatus A is oriented along the z axis, the state |u⟩ always leads to the value σ = +1. Likewise, the state |d⟩ never gives anything but σ = −1. Principle 1 gives us a new way to look at these facts. It implies that each observable (σ_x, σ_y, and σ_z) is identified with a specific linear operator in the two-dimensional space of states describing the spin.

When an observable is measured, the result is always a real number drawn from a set of possible results. For example, if the energy of an atom is measured, the result will be one of the established energy levels of the atom. For the familiar case of the spin, the possible values of any of the components are ±1. The apparatus never gives any other result. Principle 2 defines the relation between the operator representing an observable and the possible numerical outputs of the measurement. Namely, the result of a measurement is always one of the eigenvalues of the corresponding operator. Thus, each component of the spin operator must have two eigenvalues equal to ±1.

Principle 3 is the most interesting. At least I find it so. It speaks of unambiguously distinct states, a key idea that we have already encountered. Two states are physically distinct if there is a measurement that can tell them apart without ambiguity. For example, |u⟩ and |d⟩ can be distinguished by measuring σ_z. If you are handed a spin and told that it is either in the state |u⟩ or the state |d⟩, to find out which of the two states is the right one, all you have to do is align A with the z axis and measure σ_z. There is no possibility of a mistake. The same is true for |l⟩ and |r⟩. You can distinguish them by measuring σ_x.

But suppose instead that you are told the spin is in one of the two states, |u⟩ or |r⟩ (up or right). There is nothing you can measure that will unambiguously tell you the spin’s true state. Measuring σ_z won’t do it. If you get σ_z = +1, it is possible that the initial state was |r⟩ since there is a 50 percent probability of getting this answer in the state |r⟩. For that reason, |u⟩ and |d⟩ are said to be physically distinguishable, but |u⟩ and |r⟩ are not. One might say that the inner product of two states is a measure of the inability to distinguish them with certainty. Sometimes this inner product is called the overlap. Principle 3 requires physically distinct states to be represented by orthogonal state-vectors, that is, vectors with no overlap. Thus, for spin states, ⟨u|d⟩ = 0 but ⟨u|r⟩ = 1/√2.

Finally, Principle 4 quantifies these ideas in a rule that expresses the probabilities for various outcomes of an experiment. If we assume that a system has been prepared in state |A⟩, and subsequently the observable L is measured, then the outcome will be one of the eigenvalues λ_i of the operator L. But, in general, there is no way to tell for certain which of these values will be observed. There is only a probability—let us call it P(λ_i)—that the outcome will be λ_i. Principle 4 tells us how to calculate that probability, and it is expressed in terms of the overlap of |A⟩ and |λ_i⟩. More precisely, the probability is the square of the magnitude of the overlap:

P(λ_i) = |⟨A|λ_i⟩|²

or, equivalently,

P(λ_i) = ⟨A|λ_i⟩⟨λ_i|A⟩.

You might be wondering why the probability is not the overlap itself. Why the square of the overlap? Keep in mind that the inner product of two vectors is not always positive, or even real. Probabilities, on the other hand, are both positive and real. So it would not make sense to identify P(λ_i) with ⟨A|λ_i⟩. But the square of the magnitude, ⟨A|λ_i⟩⟨λ_i|A⟩, is always positive and real and thus can be identified with the probability of a given outcome.

An important consequence of the principles is as follows: The operators that represent observables are Hermitian. The reason for this is twofold. First, since the result of an experiment must be a real number, the eigenvalues of an operator L must also be real.

observable. Secondly, the eigenvectors that represent unambiguously distinguishable results must have different eigenvalues, and must also be orthogonal. These conditions are sufficient to prove that L must be Hermitian.

## 3.3 An Example: Spin Operators

It may be hard to believe, but single spins—as simple as they are—still have a lot more to teach us about quantum mechanics, and we plan to milk them for all they’re worth. Our goal in this section is to write down the spin operators in concrete form, as 2 × 2 matrices. Then, we’ll get to see how they work in specific situations. We’ll build up our spin operators and state-vectors shortly. But before we dive into the details, I’d like to say a little more about how operators are related to physical measurements. The relationship is a subtle one, and we’ll say more about it as we go.

As you know, physicists recognize various types of physical quantities, such as scalars and vectors. It should come as no surprise, then, that an operator associated with the measurement of a vector (such as spin) has a vector character of its own.

In our travels so far, we have seen more than one kind of vector. The 3-vector is the most straightforward and serves as a prototype. It’s a mathematical representation of an arrow in three-dimensional space, and is often represented by three real numbers, written out as a column matrix. Because their components are real-valued, 3-vectors are not quite rich enough to represent quantum states. For that, we need bras and kets, which have complex-valued components.

What sort of vector is the spin operator σ? It is definitely not a state-vector (a bra or a ket). It’s not exactly a 3-vector either, but it does have a strong family resemblance because it’s associated with a direction in space. In fact, we will frequently use σ as though it were a simple 3-vector. However, we’ll try to keep things straight by calling σ a 3-vector operator.

But what does that actually mean? In physical terms, it means this: Just as a spin-measuring apparatus can only answer questions about a spin’s orientation in a specific direction, a spin operator can only provide information about the spin component in a specific direction. To physically measure spin in a different direction, we need to rotate the apparatus to point in the new direction. The same idea applies to the spin operator—if we want it to tell us about the spin component in a new direction, it too must be “rotated,” but this kind of rotation is accomplished mathematically. The bottom line is that there is a spin operator for each direction in which the apparatus can be oriented.

## 3.4 Constructing Spin Operators

Now, let’s work out the details of spin operators. The first goal is to construct operators to represent the components of spin, σ_x, σ_y, and σ_z. Then we’ll build on those results to construct an operator that represents a spin component in any direction. As usual, we begin with σ_z. We know that σ_z has definite, unambiguous values for the states |u⟩ and |d⟩, and that the corresponding measurement values are σ_z = +1 and σ_z = −1. Here is what the first three principles tell us:

• Principle 1: Each component of σ is represented by a linear operator.

• Principle 2: The eigenvectors of σ_z are |u⟩ and |d⟩. The corresponding eigenvalues are +1 and −1. We can express this with the abstract equations σ_z |u⟩ = |u⟩ σ_z |d⟩ = −|d⟩. (3.12)

• Principle 3: States |u⟩ and |d⟩ are orthogonal to each other. This can be expressed as ⟨u|d⟩ = 0. (3.13)

Recalling our column representations of |u⟩ and |d⟩ from Eqs. 2.11 and 2.12, we can write Eqs. 3.12 in matrix form as (σ_z)_{11} (σ_z)_{12}   1   1 (σ_z)_{21} (σ_z)_{22} = 0   0 and (σ_z)_{11} (σ_z)_{12}   0   0 (σ_z)_{21} (σ_z)_{22} = − 1   1.

There is only one matrix that satisfies these equations. I leave it as an exercise to prove (σ_z)_{11} (σ_z)_{12}   1   0 (σ_z)_{21} (σ_z)_{22} = 0  −1 or, more concisely, σ_z = 1   0 0  −1. (3.17)

Exercise 3.2: Prove that Eq. 3.16 is the unique solution to Eqs. 3.14 and 3.15.

This is our very first example of a quantum mechanical operator. Let’s summarize what went into it. First, some experimental data: there are certain states that we called |u⟩ and |d⟩, in which the measurement of σ_z gives unambiguous results ±1. Next, the principles told us that |u⟩ and |d⟩ are orthogonal and are eigenvectors of a linear operator σ_z. Finally, we learned from the principles that the corresponding eigenvalues are the observed (or measured) values, again ±1. That’s all it takes to derive Eq. 3.17.

Can we do the same for the other two components of spin, σ_x and σ_y? Yes, we can. The eigenvectors of σ_x are |r⟩ and |l⟩, with the eigenvalues +1 and −1 respectively. In equation form, σ_z |r⟩ = |r⟩ σ_z |l⟩ = −|l⟩. (3.18)

Recall that |r⟩ and |l⟩ are linear superpositions of |u⟩ and |d⟩: |r⟩ = 1/√2 |u⟩ + 1/√2 |d⟩ |l⟩ = 1/√2 |u⟩ − 1/√2 |d⟩. (3.19)

Substituting the appropriate column vectors for |u⟩ and |d⟩, we get |r⟩ = (1/√2, 1/√2)^T |l⟩ = (1/√2, −1/√2)^T.

To make Eqs. 3.18 concrete, we can write them in matrix form: (σ_x) (σ_x) (1/√2, 1/√2)^T = (1/√2, 1/√2)^T and (σ_x) (σ_x) (1/√2, −1/√2)^T = −(1/√2, −1/√2)^T.

If you write these equations out in longhand form, they turn into four easily solved equations for the matrix elements (σ_x)_11, (σ_x)_12, (σ_x)_21, and (σ_x)_22. Here is the solution: (σ_x)_11 (σ_x)_12 = 0 1 (σ_x)_21 (σ_x)_22 = 1 0 or σ_x = (0 1; 1 0).

Finally, we can do the same for σ_y. The eigenvectors of σ_y are the in and out states |i⟩ and |o⟩: |i⟩ = 1/√2 |u⟩ + i/√2 |d⟩ |o⟩ = 1/√2 |u⟩ − i/√2 |d⟩.

In component form, these equations become |i⟩ = (1/√2, i/√2)^T |o⟩ = (1/√2, −i/√2)^T, and an easy calculation gives σ_y = (0 −i; i 0).

To summarize, the three operators σ_x, σ_y, and σ_z are represented by the three matrices σ_z = (1 0; 0 −1)

σ_x = (0 1; 1 0)

σ_y = (0 −i; i 0). (3.20)

These three matrices are very famous and carry the name of their discoverer. They are the Pauli matrices.4

## 3.5 A Common Misconception

This is a convenient time to warn you about a potential hazard. The correspondence between operators and measurements is fundamental in quantum mechanics. It is also very easy to misunderstand. Here’s what is true about operators in quantum mechanics:

## 1. Operators are the things we use to calculate eigenvalues and eigenvectors

2. Operators act on state-vectors (which are abstract mathematical objects), not on actual physical systems.

## 3. When an operator acts on a state-vector, it produces a new state-vector

Having said what is true about operators, I want to warn you about a common misconception. It is often thought that measuring an observable is the same as operating with the corresponding operator on the state. For example, suppose we are interested in measuring an observable L. The measurement is some kind of operation that the apparatus does to the system, but that operation is in no way the same as acting on the state with the operator L. For example, if the state of the system before we do the measurement is |A⟩, it is not correct to say that the measurement of L changes the state to L|A⟩.

To make sense of this, let’s look closely at an example. Fortunately, the spin example of the previous subsection is just what we need. Recall Eqs. 3.12: σ_z |u⟩ = |u⟩ σ_z |d⟩ = −|d⟩.

In these situations, there is no trap because |u⟩ and |d⟩ are eigenvectors of σ_z. If the system is prepared in, say, the |d⟩ state, a measurement will definitely give the result −1, and the σ_z operator transforms the prepared state into the corresponding post-measurement state, −|d⟩. The state −|d⟩ is the same as |d⟩ except for a multiplicative constant, so the two states are really the same. No problems here.

But now let’s review the action of σ_z on the prepared state |r⟩, which is not one of its eigenvectors. From Eq. 3.19, we know that |r⟩ = 1/√2 |u⟩ + 1/√2 |d⟩.

Acting on this state-vector with σ_z gives the result σ_z |r⟩ = 1/√2 σ_z |u⟩ + 1/√2 σ_z |d⟩ or σ_z |r⟩ = 1/√2 |u⟩ − 1/√2 |d⟩. (3.21)

OK, here is our trap. Despite what you might think, the state-vector on the right-hand side of Eq. 3.21 is definitely not the state that would result from a measurement of σ_z. That measurement result would be either +1, leaving the system in state |u⟩, or −1, leaving it in state |d⟩. Neither of these results would leave the system state-vector in the superposition represented by Eq. 3.21.

But surely that state-vector must have something to do with the measurement result? In fact, it does. We’ll find part of the answer in Lecture 4, where we’ll see how the new state-vector allows us to calculate the probabilities of each possible outcome of the measurement. However, the result of a measurement cannot be properly described without taking the apparatus into account.

4Along with the 2×2 identity matrix, they are also quaternions.

as part of the system. What actually does happen during a measurement is the subject of Section 7.8.

## 3.6 3-Vector Operators Revisited

Now, let’s revisit the idea of a 3-vector operator. I have called σ_x, σ_y, and σ_z the components of spin along the three axes, implying that they are the components of some kind of 3-vector. This is a good time to return to the two notions of vectors that come up all the time in physics. First, there is your garden-variety vector in ordinary three-dimensional space, which we’ve decided to call a 3-vector. As we’ve seen, a 3-vector has components along the three directions of space.

The other completely distinct meaning of the term vector is the state-vector of a system. Thus, |u⟩ and |d⟩, |r⟩ and |l⟩, and |i⟩ and |o⟩ are state-vectors in a two-dimensional space of spin states. What about σ_x, σ_y, and σ_z? Are they vectors, and if so, what kind?

Clearly, they are not state-vectors; they are operators (written as matrices) that correspond to the three measurable components of spin. In fact, these 3-vector operators represent a new type of vector. They are different both from state-vectors, and from ordinary 3-vectors. However, because spin operators behave so much like 3-vectors, it does no harm to think of them in that way, and that’s what we’ll do here.

We measure spin components by orienting the apparatus A along any one of the three axes and then activating it. But then why not orient A along any axis and measure the component of σ along that axis? In other words, take any unit 3-vector n̂ with components n_x, n_y, and n_z, and orient the apparatus A with its arrow along n̂. Activating A would then measure the component of σ along the axis n̂. There must be an operator that corresponds to this measurable quantity.

If σ really behaves like a 3-vector, then the component of σ along n̂ is nothing but the ordinary dot product of σ and n̂.⁵,⁶ Let’s denote that component of σ by σ_n, so that σ_n = σ · n̂ or, in expanded form, σ_n = σ_x n_x + σ_y n_y + σ_z n_z. (3.22)

To clarify the meaning of this equation, keep in mind that the components of n̂ are just numbers. They themselves are not operators. Eq. 3.22 describes a vector-operator that is constructed as the sum of three terms, each containing a numerical coefficient n_x, n_y, or n_z. To be more concrete, we can write Eq. 3.22 in matrix form:

σ_n = n_x ( 0 1; 1 0 ) + n_y ( 0 -i; i 0 ) + n_z ( 1 0; 0 -1 ).

Or even more explicitly, we can combine these three terms into a single matrix:

σ_n = ( n_z, n_x - i n_y; n_x + i n_y, -n_z ). (3.23)

What is this good for? Not much, until we find the eigenvectors and eigenvalues of σ_n. But once we do that, we will know the possible outcomes of a measurement along the direction of n̂. And we will also be able to calculate probabilities for those outcomes. In other words, we will have a complete picture of spin measurements in three-dimensional space. That is pretty darn cool, if I say so myself.

⁵ We’ll start using the notation σ, except when referring to components, such as σ_x.

⁶ The careful reader may object, because the result of this “ordinary” dot product is a 2×2 matrix rather than a scalar, so it’s not quite ordinary. Perhaps there is some comfort in the fact that the resulting matrix operator corresponds to a vector component, which is a scalar. It all works out in the end.

## 3.7 Reaping the Results

We are now positioned to make some real calculations, something that should make your inner physicist jump for joy. Let’s look at the special case where n̂ lies in the x–z plane, which is the plane of this page. Since n̂ is a unit vector, we can write n_x = cosθ, n_y = sinθ, n_z = 0, where θ is the angle between the z axis and the n̂ axis. Plugging these values into Eq. 3.23, we can write σ_n = ( cosθ, sinθ; sinθ, -cosθ ).

Exercise 3.3: Calculate the eigenvectors and eigenvalues of σ_n. Hint: Assume the eigenvector λ has the form ( cosα; sinα ), where α is an unknown parameter. Plug this vector into the eigenvalue equation and solve for α in terms of θ. Why did we use a single parameter α? Notice that our suggested column vector must have unit length.

Here are the results: λ = 1, |λ⟩ = ( cos(θ/2); sin(θ/2) ) and λ = -1, |λ⟩ = ( -sin(θ/2); cos(θ/2) ).

Notice some important facts. First, the two eigenvalues are again +1 and −1. This should come as no surprise; the apparatus A can only give one of these two answers no matter which way it points. But it’s good to see this come out of the equations. The second fact is that the two eigenvectors are orthogonal.

We are now ready to make an experimental prediction. Suppose A initially points along the z axis and that we prepare a spin in the up state |u⟩.

id:3). Then, we rotate A so that it lies along the n̂ axis. What is the probability of observing σ = +1? According to Principle 4, and using the row and column expansions of ⟨u| and |λ⟩, the answer is P(+1) = |⟨u|λ⟩|² = cos²(θ/2). (3.24) Similarly, for the same setup, P(−1) = |⟨u|λ⟩|² = sin²(θ/2). (3.25) With this result, we have come nearly full circle. When introducing spins, we made the claim that if we prepare a large number of them in the up state and then measure their component along n̂, at angle θ to the z axis, then the average value of the measured results would be cosθ—the same result we would get for a simple 3-vector in classical physics. Does our mathematical framework give the same result? It had better! If a theory disagrees with experiment, it’s the theory that has to leave town. Let’s see how well our theory holds up so far. Unfortunately, we need to cheat a little by using an equation that we will not fully explain until the next lecture. This is the equation that tells us how to calculate the average value (also called the expectation value) of a measurement. Here it is: ⟨L⟩ = Σᵢ λᵢ P(λᵢ). (3.26) It’s worth mentioning that Eq. 3.26 is just a standard formula for an average value. It’s not unique to quantum mechanics. To calculate the expectation value of a measurement corresponding to the operator L, we multiply each eigenvalue by its probability, and then sum the results. Of course, the operator we’re looking at now is just σ, and we already have all the values we need. Let’s plug them in. Using Eqs. 3.24 and 3.25, along with our known eigenvalues, we can write ⟨σ⟩ = (+1)cos²(θ/2) + (−1)sin²(θ/2) or ⟨σ⟩ = cos²(θ/2) − sin²(θ/2). If you remember your trigonometry, this gives ⟨σ⟩ = cosθ, which agrees perfectly with experiment. Yes! We’ve done it! Having come this far, you might want to try your hand on a slightly more general problem. As before, we start with the apparatus A pointing in the z direction. But now, once the spin has been prepared in the up state, we can rotate A to an arbitrary direction in space for the second set of measurements. In this situation, n ≠ 0. Go ahead and try it. Exercise 3.4: Let n_z = cosθ, n_x = sinθcosφ, and n_y = sinθsinφ. Angles θ and φ are defined according to the usual conventions for spherical coordinates (Fig. 3.2). Compute the eigenvalues and eigenvectors for the matrix of Eq. 3.23. Figure 3.2: Spherical Coordinates. This diagram illustrates conventional spherical coordinate labels r, θ, and φ. It also illustrates the conversion to Cartesian coordinates: x = rsinθcosφ, y = rsinθsinφ, and z = rcosθ. You could also try working out a much more elaborate example involving two directions, n̂ and m̂. In this setup, A not only ends up in an arbitrary direction; it also starts out in a (different) arbitrary direction. Exercise 3.5: Suppose that a spin is prepared so that σ = +1. The apparatus is then rotated to the n̂ direction and σ is measured. What is the probability that the result is +1? Note that σ = σ · m̂, using the same convention we used for σ. The answer is the square of the cosine of half the angle between m̂ and n̂. Can you show it? 3.8 The Spin-Polarization Principle There is an important theorem that you can try to prove. I will call it The Spin-Polarization Principle: Any state of a single spin is an eigenvector of some component of the spin. In other words, given any state |A⟩ = α_u |u⟩ + α_d |d⟩, there exists some direction n̂, such that (σ · n̂) |A⟩ = |A⟩. This means that for any spin state, there is some orientation of the apparatus A such that A will register +1 when it acts. In physics language, we say that the states of a spin are characterized by a polarization vector, and along that polarization vector the component of spin is predictably +1, assuming of course that you know the state-vector. An interesting consequence of this theorem is that there is no state for which the expectation values of all three components of spin are zero. There is a quantitative way to express this. Consider the expectation value of the spin along the direction n̂. Since |A⟩ is an eigenvector of (σ · n̂) (with eigenvalue +1), it follows that the expectation value can be expressed as ⟨σ · n̂⟩ = 1. On the other hand, the expectation value of the perpendicular components of σ are zero in the state |A⟩. It follows that the squares of the expectation values of all three components of σ sum to 1. Moreover, this is true for any state: ⟨σ_x⟩² + ⟨σ_y⟩² + ⟨σ_z⟩² = 1. (3.27) Remember this fact. We will come back to it in Lecture 6. Lecture 4 Time and Change There is a massive, quiet, intimidating man sitting alone at the end of the b Art: His T-shirt says “−1.” Art: Who is that “Minus One” guy over in the corner? The bouncer?

Lenny: He’s way more than a bouncer. He’s THE LAW. Without him, this whole place would fall apart.

## 4.1 A Classical Reminder

In Volume I, it took a little more than a page to explain what a state is in classical mechanics. The quantum version has taken three lectures, three mathematical interludes, and according to my rough count, about 17,000 words to get to the same place. But I think the worst is over. We now know what a state is. However, just as in classical physics, knowing the states of a system is only half the story. The other half involves a rule about how states change with time. That’s our next job.

Let me just give you a quick reminder about the nature of change in classical physics. In classical physics, the space of states is a mathematical set. The logic is Boolean, and the evolution of states over time is deterministic and reversible. In the simplest examples we considered, the state-space consisted of a few points: Heads and Tails for a coin, {1,2,3,4,5,6} for a die. The states were pictured as a set of points on the page, and the time evolution was just a rule telling you where to go next. A law of motion consisted of a graph with arrows connecting the states. The main rule—determinism—was that wherever you are in the state-space, the next state is completely specified by the law of motion. But there was also another rule called reversibility. Reversibility is the requirement that a properly formulated law must also tell you where you were last. A good law corresponds to a graph with exactly one arrow in and one arrow out at each state.

There is another way to describe these requirements. I called it the minus first law, because it underlies everything else. It says that information is never lost. If two identical isolated systems start out in different states, they stay in different states. Moreover, in the past they were also in different states. On the other hand, if two identical systems are in the same state at some point in time, then their histories and their future evolutions must also be identical. Distinctions are conserved. The quantum version of the minus first law has a name—unitarity.

## 4.2 Unitarity

Let us consider a closed system that at time t is in the quantum state |Ψ⟩. (The use of the Greek letter Ψ [psi] for quantum states is traditional when considering the evolution of systems.) To indicate that the state was |Ψ⟩ at the specific time t, let’s complicate the notation a bit and call the state |Ψ(t)⟩. Of course, this notation suggests a bit more than just “the state was |Ψ⟩ at time t.” It also suggests that the state may be different at different times. Thus, we think of |Ψ(t)⟩ as representing the entire history of the system.

The basic dynamical assumption of quantum mechanics is that if you know the state at one time, then the quantum equations of motion tell you what it will be later. Without loss of generality, we can take the initial time to be zero and the later time to be t. The state at time t is given by some operation that we call U(t), acting on the state at time zero. Without further specifying the properties of U(t), this tells us very little except that |Ψ(t)⟩ is determined by |Ψ(0)⟩.

Let’s express this relation with the equation |Ψ(t)⟩ = U(t)|Ψ(0)⟩. (4.1)

The operation U is called the time-development operator for the system.

## 4.3 Determinism in Quantum Mechanics

At this point, we need to draw some careful distinctions. We are setting up U(t) in such a way that the state-vector will evolve in a deterministic manner. Yes, you heard me correctly—the time evolution of the state-vector is deterministic. This is nice because it provides us with something we can try to predict. But how does that square with the statistical character of our measurement results?

As we’ve seen, knowing the quantum state does not mean that you can predict the result of an experiment with certainty. For example, knowing that the state of a spin is |r⟩ may tell you the outcome of a measurement of σ_z but tells you nothing about a measurement of σ_x or σ_y. For this reason, Eq. 4.1 is not the same as classical determinism. Classical determinism allows us to predict the results of experiments. The quantum evolution of states allows us to compute the probabilities of the outcomes of later experiments. This is one of the core differences between classical and quantum mechanics. It goes back to the relationship between states and measurements we mentioned at the very beginning of this book. In classical mechanics, there’s no real difference between states and measurements. In quantum mechanics, the difference is profound.

## 4.4 A Closer Look at U(t)

Conventional quantum mechanics places a couple of requirements on U(t). First, it require U(t) to be a linear operator. That is not very surprising. The relationships between states in quantum mechanics are always linear. It goes along with the idea that the state-space is a vector space. But linearity is not the only thing that quantum mechanics requires of U(t). It also requires the quantum analog of the minus first law: the conservation of distinctions.

Recall from the last lecture that two states are distinguishable if they are orthogonal. Being orthogonal, two different basis vectors represent two distinguishable states. Suppose that |Ψ(0)⟩ and |Φ(0)⟩ are two distinguishable states; in other words, there is a precise experiment that can tell them apart, and therefore they must be orthogonal: ⟨Ψ(0)|Φ(0)⟩ = 0.

The conservation of distinctions implies that they will continue to be orthogonal for all time. We can express this as ⟨Ψ(t)|Φ(t)⟩ = 0 (4.2)

for all values of t. This principle has consequences for the time-development operator U(t). To see what they are, let’s flip the ket-vector Eq. 4.1 to its bra-vector counterpart: ⟨Ψ(t)| = ⟨Ψ(0)|U†(t). (4.3)

Notice the dagger that indicates Hermitian conjugation. Now, let’s plug Eqs. 4.1 and 4.3 into Eq. 4.2: ⟨Ψ(0)|U†(t)U(t)|Φ(0)⟩ = 0. (4.4)

To examine the consequences of this equation, consider an orthonormal basis of vectors |i⟩. Any basis will do. The orthonormality is expressed in equation form as ⟨i|j⟩ = δ_ij, where δ_ij is the usual Kronecker symbol.

Next, let’s take |Φ(0)⟩ and |Ψ(0)⟩ to be members of this orthonormal basis. Substituting into Eq. 4.4 gives ⟨i|U†(t)U(t)|j⟩ = 0 (i ≠ j)

whenever i and j are not the same. On the other hand, if i and j are the same, then so are the output vectors U(t)|i⟩ and U(t)|j⟩. In that case, the inner product between them should be 1. Therefore, the general relation takes the form ⟨i|U†(t)U(t)|j⟩ = δ_ij.

In other words, the operator U†(t)U(t) behaves like the unit operator I when it acts between any members of a basis set. From here it is an easy matter to prove that U†(t)U(t) acts like the unit operator I when it acts on any state. An operator U that satisfies U†U = I is called unitary. In physics lingo, time evolution is unitary.

Unitary operators play an enormous role in quantum mechanics, representing all sorts of transformations on the state-space. Time evolution is just one example. Thus, we conclude this section with a fifth principle of quantum mechanics: • Principle 5: The evolution of state-vectors with time is unitary.

Exercise 4.1: Prove that if U is unitary, and if |A⟩ and |B⟩ are any two state-vectors, then the inner product of U|A⟩ and U|B⟩ is the same as the inner product of |A⟩ and |B⟩. One could call this the conservation of overlaps. It expresses the fact that the logical relation between states is preserved with time.

## 4.5 The Hamiltonian

In the study of classical mechanics, we became familiar with the idea of an incremental change in time. Quantum mechanics is no different in this respect: we may build up finite time intervals by combining many infinitesimal intervals. Doing so will lead to a differential equation for the evolution of the state-vector. To that end, we replace the time interval t with an infinitesimal time interval ε and consider the time-evolution operator for this small interval.

There are two principles that go into the study of incremental changes. The first principle is unitarity: U†(ε)U(ε) = I. (4.5)

The second principle is continuity. This means that the state-vector changes smoothly. To make this precise, first consider the case in which ε is zero. It should be obvious that in this case the time-evolution operator is merely the unit operator I. Continuity means that when ε is very small, U(ε) is close to the unit operator, differing from it by something of order ε. Thus, we write U(ε) = I − iεH. (4.6)

You may wonder why I put a minus sign and an i in front of H. These factors are completely arbitrary at this stage. In other words, they are a convention that has no content. I used them with an eye toward the future, when we will recognize H as something familiar from classical physics.

We will also need an expression for U†. Remembering that Hermitian conjugation requires the complex conjugation of coefficients, we find that U†(ε) = I + iεH†. (4.7)

Now we plug Eqs. 4.6 and 4.7 into the unitarity condition of Eq. 4.5: (I + iεH†)(I − iεH) = I.

Expanding to first order in ε, we find H† − H = 0 or, in a format that is more illuminating, H† = H. (4.8)

This last equation expresses the unitarity condition. But it also says that H is a Hermitian operator. This has great significance. We can now say that H is an observable, and has a c Complete set of orthonormal eigenvectors and eigenvalues. As we proceed, H will become a very familiar object, namely the quantum Hamiltonian. Its eigenvalues are the values that would result from measuring the energy of a quantum system. Exactly why we identify H with the classical concept of a Hamiltonian, and its eigenvalues with energy, will become clear shortly.

Let’s return now to Eq. 4.1 and specialize it to the infinitesimal case t = ε. Using Eq. 4.6, we find |Ψ(ε)⟩ = |Ψ(0)⟩ − iεH|Ψ(0)⟩. This is just the kind of equation that we can easily turn into a differential equation. First, we transpose the first term on the right side over to the left side, and then divide by ε: (| in our equations.

## 4.7 Expectation Values

Let’s take a short break to discuss an important aspect of statistics, namely the idea of an average value or mean value. We mentioned this idea briefly in the previous lecture, but now it’s time to take a closer look.

In quantum mechanics, average values are called expectation values. (In some ways, this is a poor choice of words; I’ll tell you why later.) Suppose we have a probability function for the outcome of an experiment that measures an observable L. The outcome must be one of L’s eigenvalues, λ_i, and the probability function is P(λ_i). In statistics, that average (or mean) value is denoted by a bar over the quantity being measured. The average of the observable L would be L̄. In quantum mechanics, the standard notation is different, having grown out of Paul Dirac’s clever bra-ket notation. We represent the average value of L with the notation ⟨L⟩. We’ll soon see why the bra-ket notation is so natural, but first let’s discuss the meaning of the term average.

From a mathematical point of view, an average is defined by the equation

⟨L⟩ = Σ_i λ_i P(λ_i). (4.11)

In other words, it is a weighted sum, weighted with the probability function P.

Alternatively, the average can be defined in an experimental way. Suppose a very large number of identical experiments is made, and the outcomes are recorded. Let’s define the probability function in a direct observational manner. We identify P(λ_i) as the fraction of observations whose result was λ_i. The definition 4.11 is then identified with the experimental average of the observations. The basic hypothesis of any statistical theory is that if the number of trials is large enough, the mathematical and experimental notions of probability and average will agree. We will not question this hypothesis.

I’ll now prove an elegant little theorem that explains the bra-ket notation for averages. Suppose that the normalized state of a quantum system is |A⟩. Expand |A⟩ in the orthonormal basis of eigenvectors of L:

|A⟩ = Σ_i α_i |λ_i⟩. (4.12)

Just for fun, with no particular agenda in mind, let’s compute the quantity ⟨A|L|A⟩. The meaning of this should be clear: First act on |A⟩ with the linear operator L. Then, take the inner product of the result with the bra ⟨A|. Let’s do the first step by letting L operate on both sides of Eq. 4.12:

L|A⟩ = Σ_i α_i L|λ_i⟩.

Remember that the vectors |λ_i⟩ are eigenvectors of L. Using the fact that L|λ_i⟩ = λ_i |λ_i⟩, we can write

L|A⟩ = Σ_i α_i λ_i |λ_i⟩.

The last step is to take the inner product with ⟨A|. We do that by expanding the bra ⟨A| in eigenvectors on the right-hand side, and then using the orthonormality of the eigenvectors. The result is

⟨A|L|A⟩ = Σ_i (α_i^* α_i) λ_i. (4.13)

Using the probability principle (Principle 4) to identify (α_i^* α_i) with the probability P(λ_i), we immediately see that the expression on the right side of Eq. 4.13 is the same as the expression on the right side of Eq. 4.11. That is to say,

⟨L⟩ = ⟨A|L|A⟩. (4.14)

Thus, we have a quick rule to compute averages. Just sandwich the observable between the bra and ket representations of the state-vector.

In the previous lecture (Section 3.5), we promised to explain how the action of a Hermitian operator on a state-vector is related to the results of physical measurements. Armed with our knowledge of expectation values, we can now keep that promise. If we look back at Eq. 3.21, we see an example of an operator, σ, acting on state-vector |r⟩ to produce a new state-vector. We can view this equation as half of the calculation for the expectation value of the measurement σ—the right-hand part of the sandwich, if you will. The rest of that calculation involves taking the inner product of this state-vector with the dual vector ⟨r|. So when σ acts on |r⟩ in Eq. 3.21, it produces a state-vector from which we can calculate the probabilities of each σ measurement outcome.

## 4.8 Ignoring the Phase-Factor

In previous lectures, we said that we can ignore the overall phase-factor of a state-vector, and promised to explain why in a later section. Having worked out the rule for averages, we’ll take a short detour to keep that promise.

What does it mean to “ignore the overall phase-factor”? It means we can multiply any state-vector by a constant factor e^{iθ}, where θ is a real number, without changing the state-vector’s physical meaning. To see this, let’s multiply Eq. 4.12 by e^{iθ} and call the result |B⟩:

|B⟩ = e^{iθ} |A⟩ = e^{iθ} Σ_j α_j |λ_j⟩. (4.15)

Note that we changed the index in the summation from i to j to avoid confusion.

ion. It’s easy to see that |B(cid:3) has the same magnitude as |A(cid:3), because eiθ has a magnitude of one: (cid:2)B|B(cid:3) = (cid:2)Ae −iθ|e iθ A(cid:3) = (cid:2)A|A(cid:3).

The same pattern of cancellation preserves other quantities as well. For example, |A(cid:3)’s probability amplitudes α be- come eiθα for |B(cid:3), so the probability amplitudes are differ- ent. However, it’s the actual probability, not the amplitude, 4.9. CONNECTIONS TO CLASSICAL MECHANICS 109 that has physical meaning. If a system is in state |B(cid:3), and we perform a measurement, the result will be the eigenvalue of |λ (cid:3) with probability ∗ −iθ iθ ∗ α e e α = α α , j j j j which is the same result we would get for state |A(cid:3). Finally, let’s use the same trick for the expectation value of a Her- mitian operator L. Applying Eq. 4.14 to state |B(cid:3), we can write (cid:2)L(cid:3) = (cid:2)B|L|B(cid:3).

Using Eq. 4.15 for |B(cid:3), we get (cid:2)L(cid:3) = (cid:2)Ae −iθ|L|e iθ A(cid:3)

or (cid:2)L(cid:3) = (cid:2)A|L|A(cid:3).

In other words, L has the same expectation value in state |B(cid:3) as it does in state |A(cid:3). Promise kept.

## 4.9 Connections to Classical

Mechanics The average, or expectation value, of an observable is the closest thing in quantum mechanics to a classical value. If 110 LECTURE 4. TIME AND CHANGE the probability distribution for an observable is a nice bell- shaped curve, and not too broad, then the expectation value really is the value that you expect to measure. If a system is so big and heavy that quantum mechanics is not too impor- tant, then the expectation value of an observable behaves almost exactly according to classical equations of motion.

For this reason, it is interesting and important to find out how expectation values change with time.

First of all, why do they change with time? They change with time because the state of the system changes with time.

Suppose the state at time t is represented by ket |Ψ(t)(cid:3) and bra(cid:2)Ψ(t)|.TheexpectationvalueoftheobservableLattime t is (cid:2)Ψ(t)|L|Ψ(t)(cid:3).

Let’sseehowthischangesbydifferentiatingitwithrespectto t and using the Schr¨odinger equation for the time derivatives of |Ψ(t)(cid:3) and (cid:2)Ψ(t)|. Using the product rule for derivatives, we find that (cid:2)Ψ(t)|L|Ψ(t)(cid:3) = (cid:2)Ψ˙(t)|L|Ψ(t)(cid:3)+(cid:2)Ψ(t)|L|Ψ˙ (t)(cid:3), dt where, as usual, the dot means time derivative. L itself has no explicit time dependency, so it just comes along for the ride. Now, plugging in the bra and ket versions of Schr¨odinger’s equation (Eq. 4.10), we get d i i (cid:2)Ψ(t)|L|Ψ(t)(cid:3) = (cid:2)Ψ(t)|HL|Ψ(t)(cid:3)− (cid:2)Ψ(t)|LH|Ψ(t)(cid:3)

dt h¯ h¯ 4.9. CONNECTIONS TO CLASSICAL MECHANICS 111 or, more concisely, d i (cid:2)Ψ(t)|L|Ψ(t)(cid:3) = (cid:2)Ψ(t)| [HL−LH] |Ψ(t)(cid:3). (4.16)

dt h¯ If you are used to ordinary algebra, Eq. 4.16 has a strange appearance. The right-hand side contains the combination HL−LH, a combination that would ordinarily be zero. But linear operators are not ordinary numbers: when they are multiplied (or applied sequentially), the order counts. In general, when H acts on L|Ψ(cid:3), the result is not the same as when L acts on H|Ψ(cid:3). In other words, except for spe- cial cases, HL (cid:6)= LH. Given two operators or matrices, the combination LM−ML is called the commutator of L with M, and it is denoted by a special symbol: LM−ML = [L,M].

It’s worth noticing that [L,M] =− [M,L] for any pair of operators. Armed with the notation for commutators, we can now write Eq. 4.16 in a simple form: d i (cid:2)L(cid:3) = (cid:2)[H,L](cid:3) (4.17)

dt h¯ or, equivalently, d i (cid:2)L(cid:3) = − (cid:2)[L,H](cid:3). (4.18)

dt h¯ 112 LECTURE 4. TIME AND CHANGE This is a very interesting and important equation. It relates the time derivative of the expectation value of an observable L to the expectation value of another observable, namely −i[L,H].

¯h Exercise 4.2: Prove that if M and L are both Hermitian, i[M,L] is also Hermitian. Note that the i is important. The commutator is, by itself, not Hermitian.

If we assume that the probabilities are nice, narrow, bell- shaped curves, then Eq. 4.18 tells us how the peaks of the curves move with time. Equations like this are the closest thing in quantum mechanics to the equations of classical physics. Sometimes we even omit the angle brackets in such equations and write them in a shorthand form: dL i = − [L,H]. (4.19)

dt h¯ But keep in mind that a quantum equation of this type should be in the middle of a sandwich, with a bra (cid:2)Ψ| on one side, and a ket |Ψ(cid:3) on the other. Alternatively, we can think of it as an equation that tells us how the centers of probability distributions move around.

Does Eq. 4.19 have a familiar look to it? If not, go back to Lectures 9 and 10 in Volume I, where we learned about the Poisson bracket formulation of classical mechanics. On 4.9. CONNECTIONS TO CLASSICAL MECHANICS 113 page 172, the following equation can be found:3 F˙ = {F,H} (4.20)

In this equation, {F,H} is not a commutator; it is a Poisson bracket. But still, Eq. 4.20 is suspiciously similar to Eq. 4.19. In fact, there is a close parallel between commutators and Poisson brackets, and their algebraic properties are quite similar. For example, if F and G represent operators, both commutators and Poisson brackets change their sign when F and G are interchanged. Dirac discovered this, and realized that it represents an important structural connection between the mathematics of classical mechanics and that of quantum mechanics. The formal identification between commutators and Poisson brackets is [F,G] ⇐⇒ ih¯{F,G}. (4.21)

To facilitate comparison with Eq. 4.19, we can substitute the symbols L and H that we’ve been using in this section.

[L,H] ⇐⇒ ih¯{L,H}. (4.22)

Let’s try and make this identification as clear as possible. If we start with Eq. 4.19, dL i = − [L,H], dt h¯ and then use the identification of Eq. 4.22 to write the classical analog, the result is dL i = − (ih¯{L,H})

dt h¯ or dL = {L,H}, dt which matches the pattern of Eq. 4.20 exactly.

Exercise 4.3: Go back to the definition of Poisson brackets in Volume I and check that the identification in Eq. 4.21 is dimensionally consistent. Show that without the factor h¯, it would not be.

Equation 4.21 solves a riddle. In classical physics, there is no difference between FG and GF. In other words: classically, commutators between ordinary observables are zero. From Eq. 4.21, we see that commutators in quantum mechanics are not zero, but that they are very small. The classical limit (the limit at which classical mechanics is accurate) is also the limit at which h¯ is negligibly small. Therefore, it is also the limit at which commutators are very small in human units.

## 4.10 Conservation of Energy

How can we tell whether something is conserved in quantum mechanics? What do we even mean by saying that an observable—call it Q—is conserved? At the very minimum, we mean that its expectation value ⟨Q⟩ does not change with time (unless of course the system is disturbed). An even stronger condition is that ⟨Q²⟩ (or the expectation value of any power of Q) does not change with time.

Looking at Eq. 4.19, we can see that the condition for ⟨Q⟩ not to change is [Q,H] = 0.

In other words, if a quantity commutes with the Hamiltonian, its expectation value is conserved. We can make this statement stronger. Using the properties of commutators, it’s easy to see that if [H,Q] = 0, then [Q², H] = 0, or even more generally, [Qⁿ, H] = 0, for any n. It turns out that we can make a stronger claim: if Q commutes with the Hamiltonian, the expectation values of all functions of Q are conserved. That’s what conservation means in quantum mechanics.

The most obvious conserved quantity is the Hamiltonian itself. Since any operator commutes with itself, one can write [H,H] = 0, which is exactly the condition that H is conserved. As in classical mechanics, the Hamiltonian is another word for the energy of a system—it’s a definition of energy. We see that under very general conditions, energy is conserved in quantum mechanics.

## 4.11 Spin in a Magnetic Field

Let’s try out the Hamiltonian equations of motion for a single spin. We will first need to specify a Hamiltonian. Where do we get it from? In general, the answer is the same as in classical physics: derive it from experiment, borrow it from some theory that we like, or just pick one and see what it does. But in the case of a single spin, we don’t have many options. Let’s start with the unit operator I. Since I commutes with all operators, if it were the Hamiltonian, nothing would change with time. Remember, the time-dependence of an observable is given by the commutator of the observable with the Hamiltonian.

The only other choice is a sum of the spin components. In fact, that’s exactly what we would get from experimental observation of a real spin—say an electron’s spin—in a magnetic field. A magnetic field B⃗ is a 3-vector—ordinary vector in space—and is specified by three Cartesian components, Bₓ, Bᵧ, and B_z. When a classical spin (a charged rotor) is put into a magnetic field, it has an energy that depends on its orientation. The energy is proportional to the dot product of the spin and the magnetic field. The quantum version of this is H ∼ σ⃗ ·B⃗ = σₓBₓ + σᵧBᵧ + σ_zB_z, where the symbol ∼ means “proportional to.” Remember that σₓ, σᵧ, and σ_z represent the components of the spin operator in the above quantum version.

Let’s take a simple example in which the magnetic field lies along the z axis. In that case, the Hamiltonian is proportional to σ_z. For convenience, we’ll absorb all the numerical constants, including the magnitude of the field (but not h¯), into a single cons ℏω H = σ_z. (4.23)

The reason for the 2 in the denominator will become clear soon.

Our goal is to find out how the expectation value of the spin varies with time—in other words, to determine ⟨σ_x(t)⟩, ⟨σ_y(t)⟩, and ⟨σ_z(t)⟩. To do this, we just go back to Eq. 4.19, and plug in these components of L. We get ⟨σ̇_x⟩ = - (1/ℏ)⟨[σ_x, H]⟩ ⟨σ̇_y⟩ = - (1/ℏ)⟨[σ_y, H]⟩ ⟨σ̇_z⟩ = - (1/ℏ)⟨[σ_z, H]⟩. (4.24)

Plugging in H = (ℏω/2)σ_z from Eq. 4.23, we get ⟨σ̇_x⟩ = -iω ⟨[σ_x, σ_z]⟩ ⟨σ̇_y⟩ = -iω ⟨[σ_y, σ_z]⟩ ⟨σ̇_z⟩ = -iω ⟨[σ_z, σ_z]⟩. (4.25)

The things we are computing on the left side of the equations are supposed to be real quantities. The factor i in these equations seems like trouble. Fortunately, the commutation relations between σ_x, σ_y, and σ_z will save the day. By plugging in the Pauli matrices from Eq. 3.20, it’s easy to verify that [σ_x, σ_y] = 2iσ_z [σ_y, σ_z] = 2iσ_x [σ_z, σ_x] = 2iσ_y. (4.26)

Each of these equations also has an i, which will cancel the i in Eqs. 4.25. Notice that the factors of 2 also cancel, resulting in some very simple equations: ⟨σ̇_x⟩ = -ω⟨σ_y⟩ ⟨σ̇_y⟩ = ω⟨σ_x⟩ ⟨σ̇_z⟩ = 0. (4.27)

Does this look familiar? If not, go back to Volume I, Lecture 10. There, we studied the classical rotor in a magnetic field. The equations were exactly the same, except that instead of expectation values, we were studying the actual motion of a deterministic system. Both there and here, the solution is that the 3-vector-operator σ (or the 3-vector L in Volume I) precesses like a gyroscope around the direction of the magnetic field. The precession is uniform, with angular velocity ω.

This similarity to classical mechanics is very pleasing, but it’s important to take note of the difference. Exactly what is precessing? In classical mechanics, it’s just the x and y components of angular momentum. In quantum mechanics, it’s an expectation value. The expectation value for a σ_z measurement does not change with time, but the other two expectation values do. Regardless, the result of each individual measurement of each spin component is still either +1 or −1.

Exercise 4.4: Verify the commutation relations of Eqs. 4.26.

## 4.12 Solving the Schrödinger Equation

The iconic Schrödinger equation that appears on T-shirts has this form: iℏ ∂Ψ(x)/∂t = - (ℏ^2/2m) ∂^2Ψ(x)/∂x^2 + U(x)Ψ(x).

At this point, let’s not worry about the meaning of the symbols except to note that it is an equation that tells you how something changes with time. (The “something” is a representation of the state-vector of a particle.)

The iconic Schrödinger equation is a special case of a more general equation that we’ve already met in Eq. 4.9. It is part definition and part principle of quantum mechanics. As a principle, it says that the state-vector changes continuously with time, in a unitary way. As a definition, it defines the Hamiltonian, and therefore the observable called energy. Eq. 4.10, ℏ ∂|Ψ⟩/∂t = -iH|Ψ⟩, is sometimes called the time-dependent Schrödinger equation. Because the Hamiltonian operator H represents energy, the observable values of energy are just the eigenvalues of H. Let’s call these eigenvalues E_j and the corresponding eigenvectors |E_j⟩. By definition, the relation between H, E_j, and |E_j⟩ is the eigenvalue equation H|E_j⟩ = E_j|E_j⟩. (4.28)

This is the time-independent Schrödinger equation, and it’s used in two different ways.

If we work in a particular matrix basis, then the equation determines the eigenvectors of H. One puts in a particular value of the energy E_j and looks for the ket-vector |E_j⟩ that solves the equation.

It is also an equation that determines the eigenvalues E_j. If you put in an arbitrary value of E, in general there will not be a solution for the eigenvector. Let’s take a very simple example: Suppose the Hamiltonian is the matrix (ℏω/2)σ_z. Since σ_z has only two eigenvalues, namely ±1, the Hamiltonian also has only two eigenvalues, ±ℏω/2. If you put any other value on the right-hand side of Eq. 4.28, there will not be a solution. Because the operator H represents energy, we often call E_j the energy eigenvalues and |E_j⟩ the energy eigenvectors of the system.

Exercise 4.5: Take any unit 3-vector n and form the operator H = (ℏω/2) σ · n.

Find the energy eigenvalues and eigenvectors by solving the time-independent Schrödinger equation. Recall that Eq. 3.23 gives σ · n in component form.

Let’s suppose we have found all the energy eigenvalues E_j and the corresponding eigenvectors |E_j⟩. We can now use that information to solve the t time-dependent Schrödinger equation. The trick is to use the fact that the eigenvectors form an orthonormal basis and then expand the state-vector in that basis. Let the state-vector be called |Ψ⟩ and write |Ψ⟩ = ∑_j α_j |E_j⟩.

Since the state-vector |Ψ⟩ changes with time and the basis vectors |E_j⟩ do not, it follows that the coefficients α_j must also depend on time: |Ψ(t)⟩ = ∑_j α_j(t)|E_j⟩. (4.29)

Now feed Eq. 4.29 into the time-dependent equation. The result is ∑_j α̇_j(t)|E_j⟩ = −(1/ħ) ∑_j H α_j(t)|E_j⟩.

Next, we use the fact that H|E_j⟩ = E_j |E_j⟩ to get ∑_j α̇_j(t)|E_j⟩ = −(1/ħ) ∑_j E_j α_j(t)|E_j⟩ or, regrouping, ∑_j (α̇_j(t) + (i/ħ) E_j α_j(t)) |E_j⟩ = 0.

The final step should be easy to see. If a sum of basis vectors equals zero, every coefficient must be zero. Hence, for each eigenvalue E_j, α_j(t) must satisfy the simple differential equation dα_j(t)/dt = −(i/ħ) E_j α_j(t).

This, of course, is the familiar differential equation for an exponential function of time, in this case with an imaginary exponent. The solution is α_j(t) = α_j(0)e^{-iE_j t/ħ}. (4.30)

This equation tells us how the α_j change with time. It is quite general and not restricted to spins, provided that the Hamiltonian does not depend explicitly on time. This is our first example of the deep connection between energy and frequency, which recurs over and over throughout quantum mechanics and quantum field theory. We will return to it often.

In Eq. 4.30, the factors α_j(0) are the values of the coefficients at time zero. If we know the state-vector |Ψ⟩ at time zero, then the coefficients are given by the projections of |Ψ⟩ on the basis eigenvectors. We can write this as α_j(0) = ⟨E_j|Ψ(0)⟩. (4.31)

Now let’s put the whole thing together and write the full solution of the time-dependent Schrödinger equation: |Ψ(t)⟩ = ∑_j α_j(0) e^{-iE_j t/ħ} |E_j⟩.

When we use Eq. 4.31 to replace α_j(0), this equation becomes |Ψ(t)⟩ = ∑_j ⟨E_j|Ψ(0)⟩ e^{-iE_j t/ħ} |E_j⟩. (4.32)

Eq. 4.32 can be written in the more elegant form, |Ψ(t)⟩ = ∑_j |E_j⟩⟨E_j|Ψ(0)⟩ e^{-iE_j t/ħ}, (4.33)

which emphasizes that we’re summing over the basis vectors.

You may wonder how we just happen to “know” |Ψ(0)⟩. The answer depends on the circumstances, but usually, we assume we can use some apparatus to prepare the system in a known state.

Before we discuss the bigger meaning of these equations, I want to restate them as a recipe. I’ll assume you already know enough about the system and its space of states to get started.

## 4.13 Recipe for a Schrödinger Ket

## 1. Derive, look up, guess, borrow, or steal the Hamiltonian operator H

## 2. Prepare an initial state |Ψ(0)⟩

3. Find the eigenvalues and eigenvectors of H by solving the time-independent Schrödinger equation, H|E_j⟩ = E_j |E_j⟩.

4. Use the initial state-vector |Ψ(0)⟩, along with the eigenvectors |E_j⟩ from step 3, to calculate the initial coefficients α_j(0): α_j(0) = ⟨E_j|Ψ(0)⟩.

5. Rewrite |Ψ(0)⟩ in terms of the eigenvectors |E_j⟩ and the initial coefficients α_j(0): |Ψ(0)⟩ = ∑_j α_j(0)|E_j⟩.

What we’ve done so far is to expand the initial state-vector |Ψ(0)⟩ in terms of the eigenvectors |E_j⟩ of H. Why is that basis better than any other? Because H tells us how things evolve with time. We will use that knowledge now.

6. In the above equation, replace each α_j(0) with α_j(t) to capture its time-dependence. As a result, |Ψ(0)⟩ becomes |Ψ(t)⟩: |Ψ(t)⟩ = ∑_j α_j(t)|E_j⟩.

## 7. Using Eq. 4.30, replace each α_j(t) with α_j(0)e^{-iE_j t/ħ}:

|Ψ(t)⟩ = ∑_j α_j(0)e^{-iE_j t/ħ}|E_j⟩. (4.34)

## 8. Season according to taste

We can now predict the probabilities for each possible outcome of an experiment as a function of time, and we are not restricted to energy measurements. Suppose L has eigenvalues λ_j and eigenvectors |λ_j⟩. The probability for outcome λ_j is P_j(t) = |⟨λ_j|Ψ(t)⟩|^2.

Exercise 4.6: Carry out the Schrödinger Ket recipe for a single spin. The Hamiltonian is H = ωħσ_z/2 and the final observable is σ_x. The initial state is given as |u⟩ (the state in which σ_z = +1).

After time t, an experiment is done to measure σ_x. What are the possible outcomes and what are the probabilities for those outcomes?

Congratulations! You have now solved a real quantum mechanics problem for an experiment that can actually be carried out in the laboratory. Feel free to pat yourself on the back.

## 4.14 Collapse

We’ve seen how the state-vector evolves between t The time that a system is prepared in a given state and the time that it is brought into contact with an apparatus and measured. If the state-vector were the main focus of observational physics, we would say that quantum mechanics is deterministic. But experimental physics is not about measuring the state-vector. It is about measuring observables. Even if we know the state-vector exactly, we don’t know the result of any given measurement. Nevertheless, it is fair to say that between observations, the state of a system evolves in a perfectly definite way, according to the time-dependent Schrödinger equation.

But something different happens when an observation is made. An experiment to measure L will have an unpredictable outcome, but after the measurement is made, the system is left in an eigenstate of L. Which eigenstate? The one corresponding to the outcome of the measurement. But this outcome is unpredictable. So it follows that during an experiment the state of a system jumps unpredictably to an eigenstate of the observable that was measured. This phenomenon is called the collapse of the wave function.4

To put it another way, suppose the state-vector is |ψ⟩ = Σ α_j |λ_j⟩ just before the measurement of L. Randomly, with probability |α_j|^2, the apparatus measures a value λ_j and leaves the system in a single eigenstate of L, namely |λ_j⟩. The entire superposition of states collapses to a single term.

This strange fact—that the system evolves one way between measurements and another way during a measurement—has been a source of contention and confusion for decades. It raises a question: Shouldn’t the act of measurement itself be described by the laws of quantum mechanics?

The answer is yes. The laws of quantum mechanics are not suspended during measurement. However, to examine the measurement process itself as a quantum mechanical evolution, we must consider the entire experimental setup, including the apparatus, as part of a single quantum system. We’ll discuss that topic—how systems are combined into composite systems—in Lecture 6. But first, a few words about uncertainty.

4We have not yet explained what a wave function is, but we’ll do so shortly, in Section 5.1.2.

Lecture 5 Uncertainty and Time Dependence

Lenny: Good evening, General. Nice to see you again.

The General: Lenny? Is that you? It’s been forever. Well, a long time anyway. Who’s your friend?

Lenny: His name is Art. Art, shake hands with General Uncertainty.

## 5.1 Mathematical Interlude: Complete Sets of Commuting Variables

5.1.1 States That Depend On More Than One Measurable

The physics of a single spin is extremely simple, and that’s what makes it so attractive as an illustrative example. But that also means there’s a lot it can’t illustrate. One property of a single spin is that its state can be fully specified by the eigenvalue of a single operator, say σ_z. If the value of σ_z is known, then no other observable—such as σ_x—can also be specified. As we have seen, measuring either of these quantities destroys any information we may have had about the other one.

But in more complicated systems, we may have multiple observables that are compatible; that is, their values can be known simultaneously. Here are two examples:

• A particle moving in three-dimensional space. A basis of states for this system is specified by the position of the particle, but this takes three position coordinates. Thus, we have states that are specified by three numbers, |x,y,z⟩. We will see later that all three spatial coordinates of a particle can be simultaneously specified.

• A system composed of two physically independent spins; in other words, a system of two qubits. Later, we will see how to combine systems to form bigger systems. But for now we can just say that the two-spin system can be described by two observables. Namely, we have a state in which both spins are up, another in which both are down, another in which the first is up while the second is down, and another in which these spins are reversed. To put it more briefly, we can characterize the two-spin system by two observables: the z component of the first spin and the z component of the second spin. Quantum mechanics does not forbid simultaneous knowledge of these two observables. In fact, one can choose any component of one spin and any component of the other spin. Quantum mechanics allows simultaneous knowledge of both.

In these situations, we need multiple measurements to fully characterize the state of the system. For example, in our two-spin system, we measure each spin separately and associate these measurements with two different operators. We’ll call these operators L and M.

A measurement leaves the system in an eigenstate (consisting of a single eigenvector), corresponding to the value (an eigenvalue) that was measured. If we measure both spins in a two-spin system, the system winds up in a state that is simultaneously an eigenvector of L and an eigenvector of M. We call this a simultaneous eigenvector of the operators L and M.

The two-spin example gives us something concrete to think about, but keep in mind that our results will be far more general—they will apply to any system that is characterized by two different operators. And as you might guess, there is nothing magic about the number two. The ideas presented here generalize to larger systems that require many operators to characterize them.

To work with two different compatible operators, we’ll need two sets of labels for their basis vectors. We’ll use the labels λ and μ. The symbols λ and μ are the eigenvalues of L and M. The subscripts i and a run over all the possible outcomes of measurements of L and M. We assume that there is a basis of state-vectors |λ_i, μ_a⟩ that are simultaneous eigenvectors of both observables. In other words,

L|λ_i, μ_a⟩ = λ_i |λ_i, μ_a⟩ M|λ_i, μ_a⟩ = μ_a |λ_i, μ_a⟩.

To make these equations a little less precise but a little easier to read, I will sometimes leave out the subscripts:

L|λ, μ⟩ = λ|λ, μ⟩ M|λ, μ⟩ = μ|λ, μ⟩.

In order to have a basis of simultaneous eigenvectors, the operators L and M must commute. This is easy to see. We begin by acting on any of the basis vectors with the product LM, and then use the fact that the basis vector is an eigenvector of both:

LM|λ, μ⟩ = Lμ|λ, μ⟩,

or

LM|λ, μ⟩ = λμ|λ, μ⟩.

The eigenvalues λ, μ are of course just numbers and it doesn’t matter which one appears first when we multiply them. Thus, if we reverse the order of these operators, and let the operator ML act on the same basis vector, we get the same result:

LM|λ, μ⟩ = ML|λ, μ⟩,

or, more succinctly,

[L, M] |λ, μ⟩ = 0, (5.1)

where the right-hand side represents the zero vector. This result would not be very helpful if it were only true for a particular basis vector. But the reasoning that leads us to Eq. 5.1 is valid for any of the basis vectors. That’s enough to ensure that the operator [L, M] = 0. If an operator annihilates every member of a basis, it must also annihilate every vector in the vector space. An operator that annihilates every vector is exactly what we mean by the zero operator.

Thus, we prove that if there is a complete basis of simultaneous eigenvectors of two observables, the two observables must commute. It turns out that the converse of this theorem is also true: if two observables commute, then there is a complete basis of simultaneous eigenvectors of the two observables. To put it simply, the condition for two observables to be simultaneously measurable is that they commute.

As we mentioned earlier, this theorem is more general. One may need to specify a larger number of observables to completely label a basis. Regardless of the number of observables that are needed, they must all commute among themselves. We call this collection a complete set of commuting observables.

5.1.2 Wave Functions

Now we’ll introduce a concept called the wave function. For now, ignore the name; in general, the quantum wave function may have nothing to do with waves. Later, when we study the quantum mechanics of particles (Lectures 8–10), we’ll find out about the connection between wave functions and waves.

Suppose we have a basis of states for some quantum system. Let the orthonormal basis vectors be called |a, b, c, ...⟩, where a, b, c, ... are the eigenvalues of some complete set of commuting observables A, B, C, .... Now, consider an arbitrary state vector |Ψ⟩. Since the vectors |a, b, c, ...⟩ are an orthonormal basis, |Ψ⟩ can be expanded in terms of them:

|Ψ⟩ = ∑_{a,b,c,...} ψ(a,b,c,...) |a,b,c,...⟩.

The quantities ψ(a,b,c,...) are the coefficients that enter the expansion. Each of them is also equal to the inner product of |Ψ⟩ with one of the basis vectors:

ψ(a,b,c,...) = ⟨a,b,c,...|Ψ⟩. (5.2)

The set of coefficients ψ(a,b,c,...) is called the wave function of the system in the basis defined by the observables A, B, C, .... The mathematical definition of a wave function is given by Eq. 5.2, which seems formal and abstract, but the physical meaning of the wave function is profoundly important. According to the basic probability principle of quantum mechanics, the squared magnitude of the wave function is the probability for the commuting observables to have values a, b, c, ...:

P(a,b,c,...) = ψ*(a,b,c,...) ψ(a,b,c,...).

The form of the wave function depends on which observables we choose to focus on. That’s because calculations for two different observables rely on different sets of basis vectors. For example, in the case of a single spin, the inner products

ψ(u) = ⟨u|Ψ⟩

and

ψ(d) = ⟨d|Ψ⟩

define the wave function in the σ basis, while ψ(r) = (cid:2)r|Ψ(cid:3)

and ψ(l) = (cid:2)l|Ψ(cid:3)

define the wave function in the σ basis.

An important feature of the wave function follows from the fact that the total probability sums to one: (cid:12)

ψ (a,b,c,...) ψ(a,b,c,...) = 1.

a,b,c,...

136 LECTURE 5. UNCERTAINTY & TIME DEP 5.1.3 A Note About Terminology The term wave function, as used in this book, refers to the collection of coefficients (also called components) that mul- tiply the basis vectors in an eigenfunction expansion. For example, if we expand a state-vector |Ψ(cid:3) as follows, (cid:12)

|Ψ(cid:3) = α |ψ (cid:3), j j where the |ψ (cid:3) are the orthonormal eigenvectors of a Her- mitian operator, the collection of coefficients α —the things we called ψ(a,b,c,...) just above—is what we mean by the wave function. In situations where the state-vector is ex- pressed as an integral rather than a sum, the wave function is continuous rather than discrete.

So far, we have been careful to distinguish the wave func- tion from the state-vectors |ψ (cid:3), and this is a common con- vention. However, some authors refer to wave functions as thoughthey arethestate-vectors. Thisambiguoususeofter- minology can be confusing. It becomes less confusing when you realize that a wave function really can represent a state- vector. It is reasonable to think of the α coefficients as the coordinates of the state-vector in a specific basis of eigen- vectors. This is similar to saying that a set of Cartesian coordinates represents a particular point in 3-space relative to a specific coordinate frame. To avoid confusion, just try to be aware of which convention is being followed. In this book, we will generally use uppercase symbols, such as Ψ, to represent state-vectors, and lowercase symbols, such as ψ, to represent wave functions.

5.2. MEASUREMENT 137

## 5.2 Measurement

Let’s return to the concept of measurement. Suppose we measure two observables L and M in a single experiment, and the system is left in a simultaneous eigenvector of these two observables. As we learned in Section 5.1.1, this means that L and M must commute.

But what if they don’t commute? Then, in general, it is not possible to have unambiguous knowledge of both. Later on, we will make this more quantitative in the form of the uncertainty principle, Heisenberg’s being a special case.

Let’s go back to our touchstone, the problem of a single spin. Any observable of a spin is represented by a 2 × 2 Hermitian matrix, and any such matrix has the form (cid:4) (cid:5)

r w w∗ r(cid:6)

with the diagonal elements being real and the other two be- ing complex conjugates. The implication is that it takes ex- actly four real parameters to specify this observable. In fact, there is a neat way to write any spin observable in terms of the Pauli matrices, σ , σ , and σ , and one more matrix: the x y z unit matrix I. As you recall, (cid:4) (cid:5)

0 1 σ = 1 0 (cid:4) (cid:5)

0 −i σ = i 0 138 LECTURE 5. UNCERTAINTY & TIME DEP (cid:4) (cid:5)

1 0 σ = z 0 −1 (cid:4) (cid:5)

1 0 I = .

0 1 Any 2 × 2 Hermitian matrix L can be written as a sum of four terms, L = aσ +bσ +cσ +dI, x y z where a, b, c, and d are real numbers.

Exercise 5.1: Verify this claim.

The unit operator I is officially an observable because it is Hermitian, but it’s a very boring one. There is only one possible value this trivial observable can have, namely 1, and every state-vector is an eigenvector. If we ignore I, then the most general observable is a superposition of the three spin components σ , σ , and σ . Can any pair of spin components x y z be simultaneously measured? Only if they commute. But it is easy to calculate the commutators for these spin compo- nents. Just use the matrix representation to multiply them in both orders, and then subtract.

The commutation relations we listed in Eqs. 4.26, [σ ,σ ] = 2iσ x y z 5.3. THE UNCERTAINTY PRINCIPLE 139 [σ ,σ ] = 2iσ y z x [σ ,σ ] = 2iσ , z x y tell us straightaway that no two spin components can be simultaneously measured, because the right-hand sides are not zero. In fact, no two components of the spin along any axes can be simultaneously measured.

## 5.3 The Uncertainty Principle

Uncertainty is one of the hallmarks of quantum mechanics, but it is not always the case that the result of an experiment is uncertain. If a system is in an eigenstate of an observable, then there is no uncertainty about the result of measuring that observable. But whatever the state, there is always uncertainty about some observable. If the state happens to be an eigenvector of one Hermitian operator—call it A— then it will not be an eigenvector of other operators that don’t commute with A. Thus, as a rule, if A and B do not commute,thentheremustbeuncertaintyinoneortheother, if not both.

The iconic example of this mutual uncertainty is the Heisenberg Uncertainty Principle, which in its original form had to do with the position and momentum of a particle.

But Heisenberg’s ideas can be expanded into a m much more general principle that applies to any two observables that happen not to commute. An example would be two components of a spin. We now have all the ingredients necessary to derive the general form of the uncertainty principle.

## 5.4 The Meaning of Uncertainty

We need to be very certain about what we mean by uncertainty if we want to quantify it. Let’s suppose the eigenvalues of the observable A are called a. Then, given a state |Ψ⟩, there is a probability distribution P(a) with the usual properties. The expectation value of A is the ordinary average: ⟨Ψ|A|Ψ⟩ = ∑ aP(a).

Roughly speaking, this means that P(a) is centered around the expectation value. What we will mean by “the uncertainty in A” is the so-called standard deviation. To compute the standard deviation, begin by subtracting from A its expectation value. We define the operator Ā to be: Ā = A−⟨A⟩.

By defining Ā in this way, we have subtracted an expectation value from an operator, and it’s not completely clear what that means. Let’s take a closer look. The expectation value is itself a real number. Every real number is also an operator, namely an operator proportional to the identity or unit operator I. To make the meaning clear, we can write Ā in a more complete form: Ā = A−⟨A⟩I.

The probability distribution for Ā is exactly the same as the distribution for A except that it is shifted so that the average of Ā is zero. The eigenvectors of Ā are the same as those of A and the eigenvalues are just shifted so that their average is zero as well. In other words, the eigenvalues of Ā are ā = a−⟨A⟩.

The square of the uncertainty (or standard deviation) of A, which we call (ΔA)², is defined by (ΔA)² = ∑ ā² P(a) (5.3)

or (ΔA)² = ∑ (a−⟨A⟩)² P(a). (5.4)

This may also be written as (ΔA)² = ⟨Ψ|Ā²|Ψ⟩.

If the expectation value of A is zero, then the uncertainty ΔA takes the simpler form (ΔA)² = ⟨Ψ|A²|Ψ⟩.

In other words the square of the uncertainty is the average value of the operator A².

## 5.5 Cauchy-Schwarz Inequality

The uncertainty principle is an inequality that says the product of the uncertainties of A and B is larger than something that involves their commutator. The basic mathematical inequality is the familiar triangle inequality. It says that in any vector space, the magnitude of one side of a triangle is less than the sum of the magnitudes of the other two sides. For real vector spaces, we derive |X||Y| ≥ |X ·Y| (5.5)

from the triangle inequality, |X|+|Y| ≥ |X +Y|.

## 5.6 The Triangle Inequality and the Cauchy-Schwarz Inequality

The triangle inequality is motivated, of course, by the properties of ordinary triangles, but it’s actually far more general and applies to a large class of vector spaces. You can get the basic idea by looking at Fig. 5.1, where the sides of the triangle are taken to be ordinary geometric vectors in a plane. The triangle inequality is just the statement that the sum of any two sides is bigger than the third side, and the underlying idea is that the shortest path between two points is a straight line. The shortest path between point 1 and point 3 is side Z, and the sum of the other two sides is certainly bigger.

Figure 5.1: The Triangle Inequality. The sum of the lengths of vectors X⃗ and Y⃗ is greater than or equal to the length of vector Z⃗. (The shortest path between two points is a straight line.)

The triangle inequality can be expressed in more than one way. We’ll start with the basic definition and then massage it into the form we need. We know that |X|+|Y| ≥ |Z|.

If we think of X and Y as vectors that can be added, we can write the above as |X⃗|+|Y⃗| ≥ |X⃗ +Y⃗|.

If we square this equation, it becomes |X⃗|² +|Y⃗|² +2|X⃗||Y⃗| ≥ |X⃗ +Y⃗|² .

But the right-hand side can be expanded as |X⃗ +Y⃗|² = |X⃗|² +|Y⃗|² +2(X⃗ ·Y⃗).

Why? Because |X⃗ +Y⃗|² is just (X⃗ +Y⃗)·(X⃗ +Y⃗). Collecting these results, we get |X⃗|² +|Y⃗|² +2|X⃗||Y⃗| ≥ |X⃗|² +|Y⃗|² +2(X⃗ ·Y⃗).

Now, we just subtract |X⃗|² +|Y⃗|² from each side and then divide by 2, leaving us with |X⃗||Y⃗| ≥ X⃗ ·Y⃗. (5.6)

This is another form of the triangle inequality. It says that, given any two vectors X⃗ and Y⃗, the product of their lengths is greater than or equal to their dot product. This is no surprise—the dot product is often defined as X⃗ ·Y⃗ = |X⃗||Y⃗|cosθ, where θ is the angle between the two vectors. But we know that the cosine of an angle always stays in the range −1 to +1, so the right-hand side must always be less than or equal to |X(cid:9)||Y(cid:9)|. This relationship is true for vectors in two dimensions, three dimensions, or an arbitrary number of di- mensions. It’seventrueforvectorsincomplexvectorspaces.

It’s generally true for vectors in any vector space, provided 5.6. TRIANGLE & C-S INEQUALITIES 145 the length of the vector is defined as the square root of the vector’s inner product with itself. As we go forward, we plan to use Inequality 5.6 in the squared form, that is, |X(cid:9)|2|Y(cid:9)|2 ≥ (X(cid:9) ·Y(cid:9)) 2 or |X(cid:9)|2|Y(cid:9)|2 ≥ |X(cid:9) ·Y(cid:9)|2 . (5.7)

In this form, it’s called the Cauchy-Schwarz inequality.

For complex vector spaces, the triangle inequality takes a slightly more complicated form. Let |X(cid:3) and |Y(cid:3) be any two vectors in a complex vector space. The magnitudes of the three vectors |X(cid:3), |Y(cid:3), and |X(cid:3)+|Y(cid:3) are (cid:19)

|X| = (cid:2)X|X(cid:3)

(cid:19)

|Y| = (cid:2)Y|Y(cid:3)

(cid:19)

|X +Y| = ((cid:2)X|+(cid:2)Y|)(|X(cid:3)+|Y(cid:3)) (5.8)

We now follow the same steps as we did for the real case: First write |X|+|Y| ≥ |X +Y|.

146 LECTURE 5. UNCERTAINTY & TIME DEP Then square it and simplify: 2|X||Y| ≥ |(cid:2)X|Y(cid:3)+(cid:2)Y|X(cid:3)|. (5.9)

This is the form of the Cauchy-Schwarz inequality that will lead to the uncertainty principle. But what does it have to do with the two observables A and B? We’ll find out by cleverly defining |X(cid:3) and |Y(cid:3).

## 5.7 The General Uncertainty

Principle Let |Ψ(cid:3) be any ket and let A and B be any two observables.

We now define |X(cid:3) and |Y(cid:3) as follows: |X(cid:3) = A|Ψ(cid:3)

|Y(cid:3) = iB|Ψ(cid:3). (5.10)

Notice the i in the second definition. Now, substitute 5.10 into 5.9 to get (cid:19)

2 (cid:2)A2(cid:3)(cid:2)B2(cid:3) ≥ |(cid:2)Ψ|AB|Ψ(cid:3)−(cid:2)Ψ|BA|Ψ(cid:3)|. (5.11)

The minus sign is due to the factor of i in the second defini- tion in 5.10. Using the definition of a commutator, we find that (cid:19)

2 (cid:2)A2(cid:3)(cid:2)B2(cid:3) ≥ |(cid:2)Ψ|[A,B]|Ψ(cid:3)|. (5.12)

5.7. GENERAL UNCERTAINTY PRINCIPLE 147 Let’ssupposeforthemomentthatAandBhaveexpectation values of zero. In that case, (cid:2)A2(cid:3) is just the square of the uncertainty in A, that is, (ΔA)2, and (cid:2)B2(cid:3) is just (ΔB)2.

Thus we can rewrite Eq. 5.12 as ΔA ΔB ≥ |(cid:2)Ψ|[A,B]|Ψ(cid:3)|. (5.13)

Reflect on this mathematical inequality for a moment. On the left side, we see the product of the uncertainties of the two observables A and B in the state Ψ. The inequality says that this product cannot be smaller than the right side, which involves the commutator of A and B. Specifically, it says that the product of the uncertainties cannot be smaller than half the magnitude of the expectation value of the com- mutator.

The general uncertainty principle is a quantitative ex- pression of something we already suspected: if the commu- tator of A and B is not zero, then both observables cannot simultaneously be certain.

But what if the expectation value of A or B is not zero?

In that case, the trick is to redefine two new operators in which the expectation values have been subtracted off: A¯ = A−(cid:2)A(cid:3)

B¯ = B−(cid:2)B(cid:3).

Then repeat the whole process, replacing A and B with A¯ and B¯ . The following exercise serves as a guide.

148 LECTURE 5. UNCERTAINTY & TIME DEP Exercise 5.2: 1) Show that ΔA 2 = (cid:2)A¯2(cid:3) and ΔB 2 = (cid:2)B¯2(cid:3).

2) Show that [A¯ ,B¯] = [A,B].

3) Using these relations, show that ΔA ΔB ≥ 1|(cid:2)Ψ|[A,B]|Ψ(cid:3)|.

Later, in Lecture 8, we will use this very general version of theuncertaintyprincipletoprovetheoriginalformofHeisen- berg’s Uncertainty Principle: The product of the uncertain- ties of the position and momentum of a particle cannot be less than half of Planck’s constant.

Lecture 6 Combining Systems: Entanglement Art: This is a pretty friendly place after all. Except for Minus One, I don’t see too many loners.

Lenny: Mingling is only natural at a place like this. And not just because it’s cramped. Just keep track of your wallet and don’t get too entangled.

## 6.1 Mathematical Interlude:

Tensor Products 6.1.1 Meet Alice and Bob Figuring out how systems combine to make bigger systems is a large part of what we do in physics. I hardly need to tell you that an atom is a collection of nucleons and electrons, each of which could be considered a quantum system in its own right.

150 LECTURE 6. ENTANGLEMENT When talking about composite systems, it’s easy to get bogged down in formal language like System A and System B. Most physicists prefer lighter-weight, informal language instead, and Alice and Bob have become near-universal sub- stitutes for A and B. We can think of Alice and Bob as pur- veyors of composite systems and laboratory setups of every description. Their inventory and expertise are limited only by our imaginations, and they gladly tackle difficult or dan- gerous assignments like jumping into black holes. They’re true geek superheroes!

Let’ssayth Alice and Bob have provided two systems—Alice’s system and Bob’s system. Alice’s system—whatever it is—is described by a space of states called S_A, and similarly Bob’s system is described by a space of states called S_B. Now let’s say that we want to combine the two systems into a single composite system. Before going any further, let’s be more specific about the systems we’re starting with. For example, Alice’s system could be a quantum mechanical coin with two basis states H and T. Of course, a classical coin must be in either one state or the other, but a quantum coin can exist in a superposition: α_H |H⟩ + α_T |T⟩.

You’ll notice that I’ve used an unusual notation for Alice’s ket-vectors. This is to distinguish them from Bob’s kets. The new notation is intended to discourage us from adding vectors in Alice’s space S_A to vectors in Bob’s space S_B. Alice’s S_A is a two-dimensional vector space—it is defined by the two basis vectors |H⟩ and |T⟩.

Bob’s system might also be a coin, but then again it might be something else. Let’s assume it’s a quantum die. Bob’s space of states S_B would then be six-dimensional, with the basis |1⟩ |2⟩ |3⟩ |4⟩ |5⟩ |6⟩ denoting the six faces of the die. Just like Alice’s coin, Bob’s die is quantum mechanical, and the six states can be superposed in a similar way.

6.1.2 Representing the Combined System Now imagine that Bob’s and Alice’s systems both exist, and form a single composite system. The first question is: How could we construct the state-space—call it S_AB—for the combined system? The answer is to form the tensor product of S_A and S_B. The notation for this operation is S_AB = S_A ⊗ S_B.

To define S_AB, it is enough to specify its basis vectors. The basis vectors are exactly what you might expect. The top half of Fig. 6.1 shows a table whose columns correspond to Bob’s six basis vectors and whose rows correspond to Alice’s two basis vectors. Each box in the table denotes a basis vector for the S_AB system. For example, the box labeled H4 represents a state in S_AB in which the coin shows Heads and the die shows the number 4. In the combined system, there are twelve basis vectors altogether.

There are various ways to represent these states symbolically. We could represent the H4 state using explicit notation, as |H⟩ ⊗ |4⟩ or |H⟩|4⟩. Usually, it’s more convenient to use the composite notation |H4⟩. This emphasizes that we’re talking about a single state with a two-part label. The left half labels Alice’s subsystem, and the right half labels Bob’s. The explicit and composite notations both have the same meaning—they refer to the same state.

Once the basis vectors are listed—in this case, twelve of them—we can combine them linearly to form arbitrary superpositions. Thus, the tensor product space in this case is twelve-dimensional. A superposition of two of these basis vectors might look like α_h3 |H3⟩ + α_t4 |T4⟩.

In each case, the first half of the state-label describes the state of Alice’s coin, and the second half describes the state of Bob’s die.

Sometimes, we’ll need to refer to an arbitrary basis vector in S_AB. To do that, we’ll use ket-vectors that look like this, |ab⟩, or like this, |a′ b′⟩.

In this notation, the a or a′ (or whatever the left-hand character of the label happens to be) represents one of Alice’s states, and the b or b′ represents one of Bob’s states.

There is one aspect of this notation that is tricky. Even though our S_AB state-labels are doubly indexed, ket-vectors like |ab⟩ or |H3⟩ represent a single state of the combined system. In other words, we’re using a double index to label a single state. This will take some getting used to. Alice’s part of the state-label is always on the left and Bob’s part is always on the right—keeping Alice and Bob in alphabetical order makes this convention easy to remember.

The rules are the same for more general systems. The only difference is that the two A-states and the six B-states would be replaced by N_A and N_B states respectively, and the tensor product would have dimension N_AB = N_A N_B.

Systems with three or more components can be represented by tensor products of three or more state spaces.

ces, but we won't do that here.

Now that we've described Alice's and Bob's separate spaces S_A and S_B, as well as the combined space S_AB, there's still one more bit of notation to set up. Alice has a set of operators, labeled σ, that act on her system. Bob has a similar set for his system, which we can label τ, so we don't mix them up with Alice's. Alice may have several σ operators, and likewise Bob may have several τ operators. With this framework in hand, we're ready to explore composite systems in greater depth. Later on, in Lecture 7, we'll explain how to work with tensor product operators in component form—expressed as matrices and column vectors.

By now, there should be no doubt in your mind that quantum physics is different from classical physics, right down to its logical roots. In this lecture and the next one, I am going to hit you even harder with this idea. We are going to discuss an aspect of quantum physics that is so different from classical physics that, as of this writing, it has puzzled—and aggravated—physicists and philosophers for almost 80 years. It drove its discoverer, Einstein, to the conclusion that something very deep is missing from quantum mechanics, and physicists have been arguing about it ever since. As Einstein realized, in accepting quantum mechanics, we are buying into a view of reality that is radically different from the classical view.

## 6.2 Classical Correlation

Before we get to quantum entanglement, let's spend a few minutes on what we might call classical entanglement. In the following experiment, Alice (A) and Bob (B) will get some help from Charlie (C).

Charlie has two coins in his hands—a penny and a dime. He mixes them up and holds them out, one in each hand, to Alice and Bob, and gives one coin to each of them. No one looks at the coins and no one knows who has which. Then, Alice gets on the shuttle to Alpha Centauri while Bob stays in Palo Alto. Charlie has done his job and doesn't matter anymore (sorry, Charlie).

Before Alice's big trip, Alice and Bob synchronize their clocks—they have done their relativity homework and accounted for time dilation and all that. They agree that Alice will look at her coin just a second or two before Bob looks at his.

Everything proceeds smoothly, and when Alice gets to Alpha Centauri she indeed looks at her coin. Amazingly, the instant she looks at it, she immediately knows exactly what coin Bob will see, even before he looks. Is this crazy? Have Alice and Bob succeeded in breaking relativity's most fundamental rule, which states that information cannot go faster than the speed of light?

Of course not. What would violate relativity would be for Alice's observation to instantly tell Bob what to expect. Alice may know what coin Bob will see but she has no way to tell him—not without sending him a real message from Alpha Centauri, and that would take at least the four years required for light to make the trip.

Let's do this experiment many times, either with many Alice-Bob pairs or with the same pair spread out over time. In order to be quantitative, Charlie (he's back now, having accepted our apology) paints a "σ = +1" on each penny and a "σ = −1" on each dime. If we assume that Charlie really is random in the way he shuffles the coins, then the following facts will emerge:

• On average, both A and B will get as many pennies as dimes. Calling the values of A's observations σ_A and B's observations σ_B, we can express this fact mathematically as ⟨σ_A⟩ = 0 ⟨σ_B⟩ = 0. (6.1)

• If A and B record their observations and then get together back in Palo Alto to compare them, they will find a strong correlation.¹ For each trial, if A observed σ_A = +1, then B observed σ_B = −1, and vice versa. In other words, the product σ_A σ_B always equals −1: ⟨σ_A σ_B⟩ = −1.

Notice that the average of the products (of σ_A and σ_B) is not equal to the product of the averages—Eqs. 6.1 tell us that ⟨σ_A⟩⟨σ_B⟩ is zero. In symbols, ⟨σ_A⟩⟨σ_B⟩ ≠ ⟨σ_A σ_B⟩, or ⟨σ_A σ_B⟩ − ⟨σ_A⟩⟨σ_B⟩ ≠ 0. (6.2)

¹Actually, it's a perfect correlation in this example.

This indicates that Alice's and Bob's observations are correlated. In fact, the quantity ⟨σ_A σ_B⟩ − ⟨σ_A⟩⟨σ_B⟩ is called the statistical correlation between Bob's and Alice's observations. It's called the statistical correlation even if it is zero. When the statistical correlation is nonzero, we say the observations are correlated. The source of this correlation is the fact that originally Alice and Bob were in the same location and Charlie had one of each type of coin. The correlation remained when Alice went to Alpha Centauri simply because the coins didn't change during the trip. There is absolutely nothing strange about this or about But Inequality 6.2.

It is a very common property of statistical distributions. Suppose you have a probability distribution P(a,b) for two variables a and b. If the variables are completely uncorrelated, then the probability will factorize: P(a,b) = P(a)P(b), (6.3)

where P(a) and P(b) are the individual probabilities for a and b. (I added subscripts to the function symbols as a reminder that they could be different functions of their arguments.) It is easy to see that if the probability factorizes in this fashion, then there is no correlation; in other words, the average of the product is the product of the averages.

Exercise 6.1: Prove that if P(a,b) factorizes, then the correlation between a and b is zero.

Let me use an example to illustrate the kind of situation that leads to factorized probabilities. Suppose that instead of a single Charlie, there are two Charlies—Charlie-A and Charlie-B—who have never communicated. Charlie-B mixes up his two coins and gives one to Bob—the other one is discarded. Charlie-A does exactly the same thing except that he gives a coin to Alice instead. This is the type of situation that leads to factorized product probabilities with no correlation.

In classical physics we use statistics and probability theory when we are ignorant about something that is, in principle, knowable. For example, after mixing up the coins in the first experiment, Charlie could have made a gentle observation (a quick peek) and then let Alice and Bob have their coins. This would have made no difference in the result. In classical mechanics, the probability distribution P(a,b) represents an incomplete specification of the system state. There is more to know—more that could be known—about the system. In classical physics, the use of probability is always associated with an incompleteness of knowledge relative to all that could be known.

A related point is that complete knowledge of a system in classical physics implies complete knowledge of every part of the system. It would not make any sense to say that Charlie knew everything that could be known about the system of two coins but was missing information about the individual coins.

These classical concepts are deeply ingrained in our thinking. They are the foundation of our instinctual understanding of the physical world, and it’s very hard to get past them. But get past them we must, if we are to understand the quantum world.

## 6.3 Combining Quantum Systems

Charlie’s two coins formed a single classical system, composed of two classical subsystems. Quantum mechanics also allows us to combine systems, as we found out in the Mathematical Interlude on tensor products (Section 6.1).

Alice and Bob have kindly agreed to provide a variant of the coin/die system they loaned us for the Interlude on tensor products. Instead of a coin and a die, the new system is built up from two spins, meaning that we’ll have a chance to put our knowledge of single spins to work.

As before, we will sometimes use the oddball notation |a⟩ to remind us that Alice’s state-vectors are not in the same state-space as Bob’s, and that we’re not allowed to add them together. On the other hand, recall that each member of an orthonormal basis for S_AB is labeled by a pair of vectors, one from S_A and one from S_B. We will make frequent use of the notation |ab⟩ to label a single basis vector of the combined system. These doubly indexed basis vectors can be added together, and we’ll be doing that a lot.

As we explained in the Interlude, labeling a basis vector with a pair of indices takes some getting used to. You should think of the pair ab as a single index labeling a single state. Let’s look at an example. Consider some linear operator M acting on the space of states of the composite system. As usual, it can be represented as a matrix. The matrix elements are constructed by sandwiching the operator between basis vectors. Thus, the matrix elements of M are expressed as ⟨a′b′|M|ab⟩ = M_{a′b′,ab}.

Each row of the matrix is labeled with a single index (a′b′) of the composite system and each column with (ab).

The vectors |ab⟩ are taken to be orthonormal, which means that their inner products are zero unless both labels match. This does not mean that a matches b, but rather that ab matches a′b′. We can also express this idea using the Kronecker delta symbol: ⟨ab|a′b′⟩ = δ_{aa′} δ_{bb′}.

The right side is zero unless a = a′ and b = b′. If the labels do match, the inner product is one.

Now that we have the basis vectors, any linear superposition of them is allowed. Thus, any state in the composite system can be expanded as |Ψ⟩ = Σ_{a,b} ψ(a,b)|ab⟩.

## 6.4 Two Spins

Returning to our example, let’s imagine two spins: Alice’s and Bob’s. To put it in a context that we can visualize, imagine that the spins are attached to two particles and that the two particles are fixed in space at two nearby but different locations.

Alice and Bob each have their own apparatuses, called A and B respectively, that they can use to prepare states and measure spin components. Each can be independently oriented along any axis.

We are going to need names for the two spins. When we only had one spin, we simply called it σ, and it had three components along the x, y, and z axes. Now we have two spins, and the question is how to label them without cluttering the symbols with too many sub- and superscripts. We could call them σA and σB, and the components, σAx, σBx, and so on. For me, that’s just too many subscripts to keep track of, especially on the blackboard. Instead, I’ll follow the same convention we used in the Interlude on tensor products. I’ll call Alice’s spin σ and assign the next letter in the Greek alphabet, τ, to Bob’s spin. The full sets of components for Alice’s and Bob’s spins are σx, σy, σz and τx, τy, τz.

According to the principles that we laid out earlier, the space of states for the two-spin system is a tensor product. We can make a table of the four states, just as we did in the Interlude. This time, it’s a 2×2 square, comprising four basis states. Let’s work in a basis in which the z components of both spins are specified. The basis vectors are |uu⟩, |ud⟩, |du⟩, |dd⟩, where the first part of each label represents the state of σ, and the second part represents τ. For example, the first basis vector |uu⟩ represents the state in which both spins are up. The vector |du⟩ is the state in which Alice’s spin is down and Bob’s spin is up.

## 6.5 Product States

The simplest type of state for the composite system is called a product state. A product state is the result of completely independent preparations by Alice and Bob, in which each uses his or her own apparatus to prepare a spin. Using explicit notation, suppose Alice prepares her spin in state α_u |u⟩ + α_d |d⟩ and Bob prepares his in the state β_u |u⟩ + β_d |d⟩.

We assume each state is normalized: α_u* α_u + α_d* α_d = 1 β_u* β_u + β_d* β_d = 1. (6.4)

And in fact these separate normalization equations for each subsystem play a crucial role in defining product states. If they did not hold, we would not have a product state. The product state describing the combined system is |product state⟩ = (α_u |u⟩ + α_d |d⟩) ⊗ (β_u |u⟩ + β_d |d⟩), where the first factor represents Alice’s state and the second factor represents Bob’s. Expanding the product and switching to composite notation, the right-hand side becomes α_u β_u |uu⟩ + α_u β_d |ud⟩ + α_d β_u |du⟩ + α_d β_d |dd⟩. (6.5)

The main feature of a product state is that each subsystem behaves independently of the other. If Bob does an experiment on his own subsystem, the result is exactly the same as it would be if Alice’s subsystem did not exist. The same is true for Alice, of course.

Exercise 6.2: Show that if the two normalization conditions of Eqs. 6.4 are satisfied, then the state-vector of Eq. 6.5 is automatically normalized as well. In other words, show that for this product state, normalizing the overall state-vector does not put any additional constraints on the α’s and β’s.

I’ll mention here that tensor products and product states are two different things, despite their similar-sounding names.2 2Sometimes, we’ll use the term tensor product space, or just product space, instead of tensor product.

A tensor product is a vector space for studying composite systems. A product state is a state-vector. It’s one of the many state-vectors that inhabit a product space. As we will see, most of the state-vectors in the product space are not product states.

## 6.6 Counting Parameters for the Product State

Let’s consider the number of parameters it takes to specify such a product state. Each factor requires two complex numbers (α_u and α_d for Alice, β_u and β_d for Bob), which means we need four complex numbers altogether. That’s equivalent to eight real parameters. But recall that the normalization conditions in Eqs. 6.4 reduce this by two. Furthermore, the overall phases of each state have no physical significance, so the total number of real parameters is four. That’s hardly surprising: it took two parameters to describe the state of a single spin, so two independent spins require four.

## 6.7 Entangled States

The principles of quantum mechanics allow us to superpose basis vectors in more general ways than just product states. The most general vector in the composite space of states is ψ_uu |uu⟩ + ψ_ud |ud⟩ + ψ_du |du⟩ + ψ_dd |dd⟩, where we have used the subscripted symbols ψ (instead of α and β) to represent the complex coefficients. Again, we have four complex numb ers, but this time we only have one normalization condition, ψ*ψ + ψ*ψ + ψ*ψ + ψ*ψ = 1, uu uu ud ud du du dd dd and only one overall phase to ignore. The result is that the most general state for a two-spin system has six real parameters. Evidently, the space of states is richer than just those product states that can be prepared independently by Bob and Alice. Something new is going on. The new thing is called entanglement.

Entanglement is not an all-or-nothing proposition. Some states are more entangled than others. Here is an example of a maximally entangled state—a state that’s as entangled as it can be. It is called the singlet state, and it can be written as |sing⟩ = (1/√2) (|ud⟩ − |du⟩).

The singlet state cannot be written as a product state. The same is true for the triplet states, (1/√2) (|ud⟩ + |du⟩)

(1/√2) (|uu⟩ + |dd⟩)

(1/√2) (|uu⟩ − |dd⟩), which are also maximally entangled. The reason for calling them singlet and triplet will be explained later.

Exercise 6.3: Prove that the state |sing⟩ cannot be written as a product state.

What is it about maximally entangled states that is so fascinating? I can sum this up in two statements: • An entangled state is a complete description of the combined system. No more can be known about it.

• In a maximally entangled state, nothing is known about the individual subsystems.

How can that be? How could we know as much as can possibly be known about the Alice-Bob system of two spins, and yet know nothing about the individual spins that are its sub-components? That’s the mystery of entanglement, and I hope that by the end of this lecture you will understand the rules of the game, even if the deeper nature of entanglement remains a paradox.

## 6.8 Alice and Bob’s Observables

So far, we’ve discussed the space of states of the Alice-Bob two-spin system, but not its observables. Some of these observables are obvious, even if their mathematical representation is not. In particular, using their apparatuses A and B, Alice and Bob can measure the components of their spins: σ_x, σ_y, σ_z and τ_x, τ_y, τ_z.

How are these observables represented as Hermitian operators in the composite space of states? The answer is simple. Bob’s operators act on Bob’s spin states exactly as they would if Alice had never shown up. The same goes for Alice.

Let’s review how the spin operators act on the states of a single spin. First, let’s look at Alice’s spin: σ_z |u⟩ = |u⟩ σ_z |d⟩ = −|d⟩ σ_x |u⟩ = |d⟩ σ_x |d⟩ = |u⟩ σ_y |u⟩ = i|d⟩ σ_y |d⟩ = −i|u⟩. (6.6)

Of course, Bob’s setup is identical to Alice’s, so we can write a parallel set of equations showing how the components of τ act on Bob’s states: τ_z |u⟩ = |u⟩ τ_z |d⟩ = −|d⟩ τ_x |u⟩ = |d⟩ τ_x |d⟩ = |u⟩ τ_y |u⟩ = i|d⟩ τ_y |d⟩ = −i|u⟩. (6.7)

Now let’s consider how the operators should be defined when acting on the tensor product states, |uu⟩, |ud⟩, |du⟩, and |dd⟩. The answer is that when σ acts, it just ignores Bob’s half of the state label. There are many possible combinations of operators and states, but I will pick a few at random. You can fill in the others, or look them up in the appendix.

Starting with Alice’s operators, we find that σ_z |uu⟩ = |uu⟩ σ_z |du⟩ = −|du⟩ σ_x |ud⟩ = |dd⟩ σ_x |dd⟩ = |ud⟩ σ_y |uu⟩ = i|du⟩ σ_y |du⟩ = −i|uu⟩ τ_z |uu⟩ = |uu⟩ τ_z |du⟩ = |du⟩ τ_x |ud⟩ = |uu⟩ τ_x |du⟩ = |dd⟩ τ_y |uu⟩ = i|ud⟩ τ_y |dd⟩ = −i|du⟩. (6.8)

Again, the rule is that Alice’s spin components act only on the Alice half of the composite system. The Bob half is a passive spectator that does not participate. In terms of symbols, when σ_x, σ_y, or σ_z acts, Bob’s half of the spin state does not change. And when Bob’s τ spin operators act, Alice’s half is similarly passive.

We are being a little loose with our notation. The vectors of a tensor product space are new vectors, built up from the vectors of two smaller spaces. Technically, the same is true for the operators. If we were being pedantic, we would insist on writing the tensor product versions of σ_z and τ_x as σ_z ⊗ I and I ⊗ τ_x, respectively, where I is the identity operator.

In fact, we can highlight two important properties of tensor product operators by rewriting the equation σ_z |du⟩ = −|du⟩ (6.9)

as (σ_z ⊗ I) (|d⟩ ⊗ |u⟩) = (σ_z |d⟩ ⊗ I |u⟩)

= (−|d⟩ ⊗ |u⟩). (6.10)

This notation is cumbersome, and we’ll usually stick to the simpler language of Eq. 6.9. However, the language of Eq. 6.10 makes two things clear:

## 1. A compos

The tensor operator σ ⊗ I is operating on a composite vector |d⟩⊗|u⟩ to produce a new composite vector −|d⟩⊗|u⟩.

2. Alice’s half (the left half) of the composite operator only affects her half of the composite vector. Likewise, Bob’s half of the operator only affects his half of the vector.

We’ll have more to say about composite operators in the next section. Furthermore, in Lecture 7, the language of Eq. 6.10 will help us see how to work with tensor products in component form.

Exercise 6.4: Use the matrix forms of σ_x, σ_y, and σ_z and the column vectors for |u⟩ and |d⟩ to verify Eqs. 6.6. Then, use Eqs. 6.6 and 6.7 to write the equations that were left out of Eqs. 6.8. Use the appendix to check your answers.

Exercise 6.5: Prove the following theorem: When any one of Alice’s or Bob’s spin operators acts on a product state, the result is still a product state. Show that in a product state, the expectation value of any component of σ⃗ or τ⃗ is exactly the same as it would be in the individual single-spin states.

This last exercise proves something important about product states. In a product state, every prediction about Bob’s half of the system is exactly the same as it would have been in the corresponding single-spin theory. The same goes for Alice. An example of this property of product states involves what I called the Spin-Polarization Principle in Lecture 3. A useful way to state that principle is: For any state of a single spin, there is some direction for which the spin is +1. As I explained, this means that the expectation values of the components satisfy the equation ⟨σ_x⟩² + ⟨σ_y⟩² + ⟨σ_z⟩² = 1, (6.11) which tells us that not all the expectation values can be zero. This fact continues to hold for all product states. However, it does not hold for the entangled state |sing⟩. In fact, for the |sing⟩ state the right-hand side of Eq. 6.11 becomes zero, as we’ll show next.

Recall that the entangled state |sing⟩ is defined as |sing⟩ = √(1/2) (|ud⟩ − |du⟩). Let’s look at the expectation values of σ in this state. We have all the machinery we need to compute them. First, let’s consider ⟨σ_z⟩: ⟨σ_z⟩ = ⟨sing|σ_z|sing⟩ = ⟨sing|σ_z √(1/2) (|ud⟩ − |du⟩). Here is where Eqs. 6.8 come in (along with Exercise 6.4, which completes this set of equations!). They tell us how σ acts on each basis vector. The result is ⟨sing|σ_z|sing⟩ = ⟨sing|√(1/2) (|ud⟩ + |du⟩) or ⟨σ_z⟩ = (⟨ud| − ⟨du|) √(1/2) (|ud⟩ + |du⟩). A quick inspection shows that this is equal to zero. Next, let’s consider ⟨σ_x⟩: ⟨σ_x⟩ = ⟨sing|σ_x|sing⟩ = ⟨sing|σ_x √(1/2) (|ud⟩ − |du⟩) or ⟨σ_x⟩ = (⟨ud| − ⟨du|) √(1/2) (|dd⟩ − |uu⟩). Again, this equation gives us zero. Finally, let’s look at ⟨σ_y⟩: ⟨σ_y⟩ = ⟨sing|σ_y|sing⟩ = (⟨ud| − ⟨du|) √(1/2) (i|dd⟩ + i|uu⟩). As you may have guessed, we are left with zero once more. Thus, we have shown that for the state |sing⟩, ⟨σ_z⟩ = ⟨σ_x⟩ = ⟨σ_y⟩ = 0, and indeed all expectation values of σ are zero. Needless to say, the same is true for the expectation values of τ. Clearly, |sing⟩ is very different from a product state. What does all this say about the measurements we can make?

If the expectation value of a component of σ is zero, it means that the experimental outcome is equally likely to be +1 or −1. In other words, the outcome is completely uncertain. Even though we know the exact state-vector, |sing⟩, we know nothing at all about the outcome of any measurement of any component of either spin.

Perhaps this means that the state |sing⟩ is somehow incomplete—that there are details of the system that we were sloppy about and didn’t measure. After all, earlier we saw a perfectly classical example in which Alice and Bob knew nothing about their coins until they actually looked at them. How is the quantum version different?

In our “classical entanglement” example involving Alice, Bob, and Charlie, it is perfectly clear that there was more to know. Charlie could have sneaked a peek at the coins without changing anything, because classical measurements can be arbitrarily gentle.

Might there be so-called hidden variables in the quantum system? The answer is that according to the rules of quantum mechanics, there is nothing to know beyond what is encoded in the state-vector—in the present case, |sing⟩. The state-vector is as complete a description of a system as it is possible to make. So it seems that in quantum mechanics, we can know everything about a composite system—everything there is to know, anyway—and still know nothing about its constituent parts. This is the true weirdness of entanglement, which so disturbed Einstein.

## 6.9 Composite Observables

Let’s imagine a quantum mechanical Alice-Bob-Charlie setup. Charlie’s role is to prepare two spins in the entangled state |sing⟩. Then, without looking at the spins (remember, quantum measurements are not gentle), he gives one spin to Alice and one to Bob. Although Alice and Bob know exactly what state the combined system is in, they can predict nothing about the outcome of their individual measurements.

But surely knowing the exact state of the composite system must tell them something, even if the state is highly entangled. And in fact it does. However, to understand what it tells them, we have to consider a wider family of observables than the ones that Alice and Bob can measure separately, each using only his or her own detector. As it turns out, there are observables that can only be measured by using both detectors. The results of such experiments can only be known to Alice or Bob if they come together and compare notes.

The first question is whether Alice and Bob can simultaneously measure their own observables. We have seen that there are quantities that cannot be simultaneously measured. In particular, two observables that do not commute cannot both be measured without the measurements interfering with each other. But for Alice and Bob, it is easy to see that every component of σ commutes with every component of τ. This is a general fact about tensor products. The operators that act on the two separate factors commute with one another. Therefore, Alice can make any measurement on her spin and Bob can make any measurement on his, without either interfering with the other’s experiment.

Let’s suppose Alice measures σ_z and Bob measures τ_z, and then they multiply the results. In other words, they conspire to measure the product τ_z σ_z.

The product τ_z σ_z is an observable that is mathematically represented by first applying σ_z to a ket and then subsequently applying τ_z. Keep in mind that these are just the mathematical operations that define a new operator: they are different from the act of performing a physical measurement. You don’t need an apparatus to multiply two operators; you just need a pencil and paper. Let’s see what happens if we apply the product τ_z σ_z to the state |sing⟩:

τ_z σ_z √ (|ud⟩−|du⟩).

First, using the table in Eqs. 6.8, apply σ_z:

τ_z σ_z √ (|ud⟩−|du⟩) = τ_z √ (|ud⟩+|du⟩).

Now, apply τ_z to get

τ_z σ_z √ (|ud⟩−|du⟩) = √ (−|ud⟩+|du⟩).

Notice that the end result is just to change the sign of |sing⟩:

τ_z σ_z |sing⟩ = −|sing⟩.

Evidently, |sing⟩ is an eigenvector of the observable τ_z σ_z with eigenvalue −1. Let’s examine the significance of this result. Alice measures σ_z and Bob measures τ_z; when they come together and compare results, they find they’ve measured opposite values. Sometimes, Bob measures +1 and Alice measures −1. Other times, Alice measures +1 and Bob measures −1. The product of the two measurements is always −1.

There should be nothing surprising in this result. The state-vector |sing⟩ is a superposition of two vectors, |ud⟩ and |du⟩, both of which comprise two spins with opposite z components. The situation is altogether similar to the classical example involving Charlie and his two coins.

But now we come to something that has no classical analog. Suppose that instead of measuring the z components of their spins, Alice and Bob measure the x components. To find out how their outcomes are correlated, we must study the observable τ_x σ_x.

Let’s act on |sing⟩ with this product. Here are the steps:

τ_x σ_x |sing⟩ = τ_x σ_x √ (|ud⟩−|du⟩)

= τ_x √ (|dd⟩−|uu⟩)

= √ (|du⟩−|ud⟩)

or, more simply,

τ_x σ_x |sing⟩ = −|sing⟩.

Now this is a bit surprising: |sing⟩ is also an eigenvector of τ_x σ_x with eigenvalue −1. It is far less obvious from just looking at |sing⟩ that the x components of the two spins are always opposite. Nevertheless, every time Alice and Bob measure them, they find that σ_x and τ_x have opposite values.

At this point, you will probably not be surprised to learn that the same thing is true for the y components.

Exercise 6.6: Assume Charlie has prepared the two spins in the singlet state. This time, Bob measures τ_x and Alice measures σ_x. What is the expectation value of σ_y τ_x? What does this say about the correlation between the two measurements?

Exercise 6.7: Next, Charlie prepares the spins in a different state, called | T⁺, where |T⁺⟩ = √2 (|ud⟩ + |du⟩).

In these examples, T stands for triplet. These triplet states are completely different from the states in the coin and die examples. What are the expectation values of the operators σ_z τ_z, σ_x τ_x, and σ_y τ_y?

What a difference a sign can make!

Exercise 6.8: Do the same for the other two entangled triplet states, |T⁰⟩ = √2 (|uu⟩ + |dd⟩)

|T⁻⟩ = √2 (|uu⟩ − |dd⟩), and interpret.

Finally, let’s consider one more observable. This one cannot be measured by Alice and Bob making separate measurements with their individual apparatuses, even if they come together and compare notes. Nevertheless, quantum mechanics insists that some kind of apparatus can be built to measure the observable.

The observable I am referring to can be thought of as the ordinary dot product of the vector-operators σ⃗ and τ⃗: σ⃗ · τ⃗ = σ_x τ_x + σ_y τ_y + σ_z τ_z.

One might think that a value for this observable can be found if Bob measures all components of τ, while Alice measures all components of σ; then they could multiply the components and add them up. The problem is that Bob cannot simultaneously measure the individual components of τ, because they don’t commute. Likewise, Alice cannot measure more than one component of σ at a time. To measure σ⃗·τ⃗, a new kind of apparatus must be built, one that measures σ⃗·τ⃗ without measuring any individual component. It’s far from obvious how that could be done. Here is a concrete example of how such a measurement could be carried out: Some atoms have spins that are described in the same way as electron spins. When two of these atoms are close to each other—for example, two neighboring atoms in a crystal lattice—the Hamiltonian will depend on the spins. In some situations, the neighboring spins’ Hamiltonian is proportional to σ⃗ · τ⃗. If that happens to be the case, then measuring σ⃗·τ⃗ is equivalent to measuring the energy of the atomic pair. Measuring this energy is a single measurement of the composite operator and does not entail measuring the individual components of either spin.

Exercise 6.9: Prove that the four vectors |sing⟩, |T⁺⟩, |T⁰⟩, and |T⁻⟩ are eigenvectors of σ⃗·τ⃗. What are their eigenvalues?

Take a look at your results from this last exercise. Do you see why one of these state-vectors is called the singlet, while the other three are called triplets? The reason is that if you look at their relation to the operator σ⃗·τ⃗, the singlet is an eigenvector with one eigenvalue, and the triplets are all eigenvectors with a different degenerate eigenvalue.

Here is a good exercise that combines the concept of entanglement with the concepts of time and change from Lecture 4. Use it to review the ideas of unitary time evolution and the meaning of the Hamiltonian.

Exercise 6.10: A system of two spins has the Hamiltonian H = σ⃗ · τ⃗. What are the possible energies of the system, and what are the eigenvectors of the Hamiltonian?

Suppose the system starts in the state |uu⟩. What is the state at any later time? Answer the same question for initial states of |ud⟩, |du⟩, and |dd⟩.

Lecture 7 More on Entanglement

Hilbert’s Place, summer 1935: Two scruffy regulars come through the swinging doors, in the midst of an intense conversation. The one with the wild grayish hair and frayed sweater says, “No, I will not accept your theory unless you can tell me what the elements of physical reality are.”

The other one looks around, throws up his hands in obvious frustration, and says to Art and Lenny, “There he goes again. Elements of physical reality, EPRs, EPRs, that’s all he ever thinks about. Albert, stop being obsessive and just accept the facts.”

“Never! I cannot accept that one can know everything there is to know about a thing, and still know nothing about its parts. That’s utter nonsense, Niels.”

“Sorry, Albert. That’s just the way it is. Here, let me buy you a beer.”

In this lecture, we will look at entanglement in greater depth. To do that, we’ll need some additional mathematical tools. First, we’ll find out how to work with tensor products in component form. Then, we’ll learn about a new operator called the density matrix. These tools are not inherently hard to master, but they do require some patience and a fair amount of index wrangling.

## 7.1 Mathematical Interlude: Tensor Products in Component Form

In Lecture 6, we explained how to form the tensor product of two vector spaces using the abstract notation of bras, kets, and operator symbols like σ. How does that translate into columns, rows, and matrices?

Building tensor products from matrices and column vectors is not hard. The rules are straightforward, as we’ll see below. The tricky part is understanding why these rules work—why they allow us to build matrices and column vectors that have the properties we want. We’ll tackle the issue in two different ways. First, we’ll build composite operators using the tried-and-true method we developed in Lecture 3. Then we’ll show you how to build composite operators directly from their component operators.

7.1.1 Building Tensor Product Matrices from Basic Principles

Back in Lecture 3, we showed you how to write any observable M in matrix form, relative to a specific basis. Take a moment to review Eqs. 3.1 through 3.4. In that section, we calculated the numerical values m_jk of M’s matrix elements with the expression m_jk = ⟨j|M|k⟩, (7.1)

where |j⟩ and |k⟩ represent the basis vectors. Each |j⟩,|k⟩ combination generates a different matrix element.1

Our plan is to apply this formula to some tensor product operators and see what we get. Because of our double-indexing convention for tensor product basis vectors, the “sandwiches” in these equations will look a little different from the ones in Eq. 7.1. On each end of the sandwich, we will cycle through the basis vectors |uu⟩, |ud⟩, |du⟩, and |dd⟩.2 To keep things simple, we’ll use the operator σ_z ⊗ I as an example, where I is the identity operator. As we have seen, σ_z ⊗ I acts on Alice’s half of the state-vector with σ_z, and does absolutely nothing to Bob’s half. Because we are working in a four-dimensional vector space, the resulting matrix will be 4×4. Omitting multiple ⊗ symbols to avoid visual clutter, we can write the matrix like this: σ_z ⊗ I = ⎛ ⎞ ⟨uu|σ_z I|uu⟩ ⟨uu|σ_z I|ud⟩ ⟨uu|σ_z I|du⟩ ⟨uu|σ_z I|dd⟩ ⎜ ⎟ ⎜ ⎟ ⟨ud|σ_z I|uu⟩ ⟨ud|σ_z I|ud⟩ ⟨ud|σ_z I|du⟩ ⟨ud|σ_z I|dd⟩ ⎟ ⎜ ⎟ ⎜ ⎟.

⟨du|σ_z I|uu⟩ ⟨du|σ_z I|ud⟩ ⟨du|σ_z I|du⟩ ⟨du|σ_z I|dd⟩ ⎟ ⎝ ⎠ ⟨dd|σ_z I|uu⟩ ⟨dd|σ_z I|ud⟩ ⟨dd|σ_z I|du⟩ ⟨dd|σ_z I|dd⟩ (7.2)

To evaluate these matrix elements, we could allow σ_z and I to operate either to the left or to the right. Let’s assume σ_z operates to the left and I operates to the right. Since I does nothing, all we care about is what σ_z does to the bra vector on its left. And within that bra vector, σ_z only acts on the leftmost (that is, Alice’s) state-label. Using the rules we’ve already worked out (see Eqs. 6.6 and 6.7), we can carry out all of these σ_z operations to obtain a matrix of inner products: ⎛ ⎞ ⟨uu|uu⟩ ⟨uu|ud⟩ ⟨uu|du⟩ ⟨uu|dd⟩ ⎜ ⎟ ⎜ ⎟ ⟨ud|uu⟩ ⟨ud|ud⟩ ⟨ud|du⟩ ⟨ud|dd⟩ ⎟ σ_z ⊗ I = ⎜ ⎜ ⎟ ⎟.

−⟨du|uu⟩ −⟨du|ud⟩ −⟨du|du⟩ −⟨du|dd⟩ ⎟ ⎝ ⎠ −⟨dd|uu⟩ −⟨dd|ud⟩ −⟨dd|du⟩ −⟨dd|dd⟩ (7.3)

Because these eigenvectors are orthonormal, the matrix reduces to ⎛ ⎞ 1 0 0 0 ⎜ ⎟ σ_z ⊗ I = ⎜ ⎝ 0 1 0 0 ⎟ ⎠. (7.4)

0 0 −1 0 0 0 0 −1

How do we write the eigenvectors |uu⟩, |ud⟩, |du⟩, and |dd⟩ as column vectors? For now, I’ll just tell you that we’ll represent |uu⟩ and |du⟩ as ⎛ ⎞ ⎛ ⎞ 1 0 ⎜ ⎟ ⎜ ⎟ |uu⟩ = ⎜ ⎝ 0 ⎟ ⎠, |du⟩ = ⎜ ⎝ 0 ⎟ ⎠. (7.5)

0 1 0 0

Let’s see what happens when σ_z ⊗ I operates on these column vectors. Applying the matrix to |uu⟩ results in ⎛ ⎞⎛ ⎞ ⎛ ⎞ 1 0 0 0 1 1 ⎜ ⎟⎜ ⎟ ⎜ ⎟ ⎜ 0 1 0 0 ⎟⎜ 0 ⎟ ⎜ 0 ⎟ ⎝ 0 0 −1 0 ⎠⎝ 0 ⎠ = ⎝ 0 ⎠.

0 0 0 −1 0 0

In other words, (σ_z ⊗ I)|uu⟩ = |uu⟩, just as we expect. What if we apply the same matrix to the column vector |du⟩ in Eqs. 7.5? Carrying out the matrix multiplication results in −|du⟩, just as it should.

7.1.2 Building Tensor Product Matrices from Component Matrices

The above method for calculating matrix elements is very general—it works for all observables. If we need to construct the tensor product of two operators, and we already know the matrix elements of the building blocks, we can combine them directly. Here is the rule for combining 2×2 matrices to form 4×4 matrices: A⊗B = [A_11 B_11  A_12 B_11 A_11 B_21  A_12 B_21] (7.6)

or ⎛ ⎞ A_11 B_11  A_11 B_12  A_12 B_11  A_12 B_12 ⎜ ⎟ A⊗B = ⎜ ⎝ A_11 B_21  A_11 B_22  A_12 B_21  A_12 B_22 ⎟ ⎠. (7.7)

A_21 B_11  A_21 B_12  A_22 B_11  A_22 B_12 A_21 B_21  A_21 B_22  A_22 B_21  A_22 B_22

The same pattern works for matrices of any size. This kind of matrix multiplication n is sometimes called the Kronecker product, a term that only applies to matrices—it’s the matrix version of the tensor product. The Kronecker product of two 2×2 matrices is a 4×4 matrix, and the pattern is similar for matrices of arbitrary size. In general, the Kronecker product of an m×n matrix and a p×q matrix is an mp×nq matrix.

All of this applies perfectly well to column and row vectors, which are just specialized matrices. The tensor product of two 2 × 1 column vectors is a 4 × 1 column vector. If a and b are 2 × 1 column vectors, their tensor product looks like this:

a ⊗ b = ⎛ a₁₁b₁₁ ⎞ ⎜ a₁₁b₂₁ ⎟ ⎜ a₂₁b₁₁ ⎟ ⎝ a₂₁b₂₁ ⎠. (7.8)

Let’s see how this works out for Alice and Bob. First, we’ll construct the four tensor product basis vectors, using |u⟩ and |d⟩ as building blocks. Recall Eqs. 2.11 and 2.12 from Lecture 2,

|u⟩ = ⎛ 1 ⎞, |d⟩ = ⎛ 0 ⎞.

⎝ 0 ⎠        ⎝ 1 ⎠

If we plug the appropriate combinations of |u⟩ and |d⟩ into Eq. 7.8, our four 4×1 column vectors are

|uu⟩ = |u⟩ ⊗ |u⟩ = ⎛ 1 ⎞ ⎜ 0 ⎟ ⎜ 0 ⎟ ⎝ 0 ⎠

|ud⟩ = |u⟩ ⊗ |d⟩ = ⎛ 0 ⎞ ⎜ 1 ⎟ ⎜ 0 ⎟ ⎝ 0 ⎠

|du⟩ = |d⟩ ⊗ |u⟩ = ⎛ 0 ⎞ ⎜ 0 ⎟ ⎜ 1 ⎟ ⎝ 0 ⎠

|dd⟩ = |d⟩ ⊗ |d⟩ = ⎛ 0 ⎞ ⎜ 0 ⎟ ⎜ 0 ⎟ ⎝ 1 ⎠. (7.9)

Next, we’ll use the rule from Eq. 7.7 to combine the operators σ_z and τ_x. Using Eqs. 3.20 to define matrices σ_z and τ_x, this rule gives the tensor product matrix

σ_z ⊗ τ_x = ⎛ 1  0 ⎞ ⊗ ⎛ 0  1 ⎞ = ⎛ 0  1  0  0 ⎞ ⎝ 0 -1 ⎠   ⎝ 1  0 ⎠   ⎜ 1  0  0  0 ⎟ ⎜ 0  0  0  1 ⎟ ⎝ 0  0  1  0 ⎠.

Let’s compare this result with the product of σ_x and τ_z,

σ_x ⊗ τ_z = ⎛ 0  1 ⎞ ⊗ ⎛ 1  0 ⎞ = ⎛ 0  0  1  0 ⎞ ⎝ 1  0 ⎠   ⎝ 0 -1 ⎠   ⎜ 0  0  0  1 ⎟ ⎜ 1  0  0  0 ⎟ ⎝ 0  1  0  0 ⎠.

Notice that σ_x ⊗ τ_z is not the same as σ_z ⊗ τ_x. That is natural, because they represent different observables.

So far, so good. But next, we’ll see something a little more interesting. With the help of a few exercises, we’ll try to convince you that the Kronecker product really is the tensor product for matrices—in other words, that Alice’s half of the matrix only affects her half of the column vector, and likewise for Bob. This is tricky because of the way the Kronecker product mixes up the elements of its building blocks.

As an example, let’s look at how σ_z ⊗ τ_x acts on |ud⟩. Translating the abstract symbols into components, we can write

(σ_z ⊗ τ_x)|ud⟩ = ⎛ 0  1  0  0 ⎞ ⎛ 0 ⎞   ⎛ 1 ⎞ ⎜ 1  0  0  0 ⎟ ⎜ 1 ⎟ = ⎜ 0 ⎟.

⎜ 0  0  0  1 ⎟ ⎜ 0 ⎟   ⎜ 0 ⎟ ⎝ 0  0  1  0 ⎠ ⎝ 0 ⎠   ⎝ 0 ⎠

But the column vector on the right-hand side corresponds to |uu⟩ in Eqs. 7.9. Translated back into abstract notation, this becomes

(σ_z ⊗ τ_x)|ud⟩ = |uu⟩.

This is exactly what we want—a matrix representation of our abstract operators and state-vectors that replicates their known behavior.

The following exercise will help crystallize the idea that the σ-half of σ ⊗ τ only affects Alice’s half of the state-vector, and that the τ-half only affects Bob’s. The one after that provides some practice working out the matrix elements of an operator, assuming that we already know what the operator does to each basis vector.

Exercise 7.1: Write the tensor product I⊗τ as a matrix, and apply that matrix to each of the |uu⟩, |ud⟩, |du⟩, and |dd⟩ column vectors. Show that Alice’s half of the state-vector is unchanged in each case. Recall that I is the 2×2 unit matrix.

Exercise 7.2: Calculate the matrix elements of σ_z ⊗ τ_x by forming inner products as we did in Eq. 7.2.

The third exercise is a bit tedious, but it really nails things down. Consider the equation

(A⊗B) (a⊗b) = (Aa⊗Bb). (7.10)

As in Eqs. 7.7 and 7.8, A and B represent 2×2 matrices (or operators), and a and b represent 2×1 column vectors. The exercise asks you to expand the equation into components and show that the left side matches the right side.

Exercise 7.3: a) Rewrite Eq. 7.10 in component form, replacing the symbols A, B, a, and b with the matrices and column vectors from Eqs. 7.7 and 7.8.

b) Perform the matrix multiplications Aa and Bb on the right-hand side. Verify that each result is a 4×1 matrix.

c) Expand all three Kronecker products.

d) Verify the row and column sizes of each Kronecker product: • A⊗B: 4×4 • a⊗b: 4×1 • Aa⊗Bb: 4×4 e) Perform the matrix multiplication on the left-hand side, resulting in a 4×1 column vector. Each row should be the sum of four separate terms.

f) Finally, verify that the resulting column vectors on the left and right sides are identical.

## 7.2 Mathematical Interlude: Outer Products

Given a bra ⟨φ| and a ket |ψ⟩, we can form the inner product ⟨φ|ψ⟩. As we’ve seen, the inner product is a complex number. However, there is another kind of product called the outer product, written |ψ(cid:3)(cid:2)φ|.

The outer product is not a number; it is a linear operator.

Let’s consider what happens when |ψ(cid:3)(cid:2)φ| acts on another ket |A(cid:3): |ψ(cid:3)(cid:2)φ| |A(cid:3).

In these examples, we’re using spacing instead of parentheses to show the grouping of operations. Remember that all operations with bras, kets, and linear operators are associative, which means we’re allowed to group them any way we like, as long as we keep the same ordering from left to right.3 The action of the outer product operator is very simple and can be defined as |ψ(cid:3)(cid:2)φ| |A(cid:3) ≡ |ψ(cid:3) (cid:2)φ|A(cid:3).

3Sometimes we can change left-to-right ordering as well, but that requires more care.

In other words, we take the inner product of (cid:2)φ| with |A(cid:3) (the result is a complex number) and multiply it by the ket |ψ(cid:3).

The bra-ket notation is so efficient that it practically forces the definition on us. That was the genius of Paul Dirac. It’s easy to prove that the outer product can also act on bras: (cid:2)B| |ψ(cid:3)(cid:2)φ| ≡ (cid:2)B|ψ(cid:3) (cid:2)φ|.

A special case is the outer product of a ket with its corresponding bra, |ψ(cid:3)(cid:2)ψ|. Assuming that |ψ(cid:3) is normalized, this operator is called a projection operator. Here is how it acts: |ψ(cid:3)(cid:2)ψ| |A(cid:3) = |ψ(cid:3) (cid:2)ψ|A(cid:3)

Note that the result is always proportional to |ψ(cid:3). A projection operator can be said to project a vector onto the direction defined by |ψ(cid:3). Here are some properties of projection operators that you can easily prove (remember that |ψ(cid:3) is normalized to 1): • Projection operators are Hermitian.

• The vector |ψ(cid:3) is an eigenvector of its projection operator with eigenvalue 1: |ψ(cid:3)(cid:2)ψ| |ψ(cid:3) = |ψ(cid:3)

• Any vector orthogonal to |ψ(cid:3) is an eigenvector with eigenvalue zero. Thus, the eigenvalues of |ψ(cid:3)(cid:2)ψ| are all either 0 or 1, and there is only one eigenvector with All we are doing is averaging over Bob’s ignorance of the state prepared by Alice. But now we can combine the terms into a single expression by defining a density matrix ρ that encodes Bob’s knowledge. In this case the density matrix is half the projection operator onto |φ⟩ plus half the projection operator onto |ψ⟩, ρ = ½|ψ⟩⟨ψ| + ½|φ⟩⟨φ|.

We’ve now packaged all of Bob’s knowledge of the system into a single operator ρ. At this point, the rule to compute expectation values becomes very simple: ⟨L⟩ = Tr ρL. (7.13)

We can generalize this. Suppose that Alice tells Bob that she has prepared one of several states—call them |φ₁⟩, |φ₂⟩, |φ₃⟩, and so on. Moreover, she specifies probabilities P₁, P₂, P₃, ... for each of these states. Bob can still package all his knowledge into a density matrix: ρ = P₁|φ₁⟩⟨φ₁| + P₂|φ₂⟩⟨φ₂| + P₃|φ₃⟩⟨φ₃| + ....

Furthermore, he can use exactly the same rule, Eq. 7.13, to compute the expectation value.

When the density matrix corresponds to a single state, it is a projection operator that projects onto that state. In this case, we say that the state is pure. A pure state represents the maximum amount of knowledge that Bob can have of a quantum system. But in the more general case, the density matrix is a mix of several projection operators. We then say that the density matrix represents a mixed state.

I have used the term density matrix, but strictly speaking, ρ is an operator. It only becomes a matrix when a basis is chosen. Suppose we choose the basis |a⟩. The density matrix is just the matrix representation of ρ with respect to this basis: ρ = ⟨a|ρ|a'⟩.

aa' If the matrix representation of L is L_{a',a} then 7.13 takes the form ⟨L⟩ = Σ_{a,a'} L_{a',a} ρ_{a,a'}. (7.14)

## 7.4 Entanglement and Density Matrices

Classical physics also has its notion of pure and mixed states, although they are not called by those names. Just to illustrate, let’s consider a system of two particles moving along a line. According to the rules of classical mechanics, we can calculate the orbits of the particles if we know the values of their positions (x₁ and x₂) and momenta (p₁ and p₂) at a certain instant in time. The state of the system is thus specified by four numbers: x₁, x₂, p₁, and p₂. If we know these four numbers, we have as complete a description of the two-particle system as it is possible to have: there is no more to know. We can call this a pure classical state.

Often, however, we don’t know the exact state, but only some probabilistic information. That information can be encoded in a probability density ρ(x₁, x₂, p₁, p₂). A classical pure state is just a special case of a probability density, in which ρ is nonzero at only one point. But more generally, ρ will be smeared out, in which case we could call it a classical mixed state.⁵ When ρ is smeared out, it means our knowledge of the system state is incomplete. The more smeared out it is, the greater our ignorance.

One thing should be completely obvious from this example: if you know the pure state for the combined two-particle system, then you know everything about each particle. In other words, a pure state for two classical particles implies a pure state for each of the individual particles.

But this is exactly what is not true in quantum mechanics when a system is entangled. The state of a composite system can be absolutely pure, but each of its constituents must be described by a mixed state.

Let’s take a system composed of two parts, A and B. It could be two spins or any other composite system. In this case, we will suppose that Alice has complete knowledge of the state of the combined system. In other words, she knows the wave function Ψ(a,b). There is nothing missing from her knowledge of the combined system. Nevertheless, Alice is not interested in B. Instead, she wishes to find out as much as she can about A without looking at B. She selects an observable L that belongs to A, and that does nothing to B when it acts. The rule for calculating the expectation value of L is ⟨L⟩ = Σ_{a'b',ab} Ψ*(a'b') L_{a'b',ab} Ψ(ab). (7.15)

So far, this is entirely general. However, if the observable L is associated only with A, then it acts trivially on the b-index and we can write the expectation value as ⟨L⟩ = Σ_{a',a} Σ_{b} Ψ*(a'b) L_{a',a} Ψ(ab). (7.16)

Now, Alice can summarize all of her knowledge, at least for the purpose of studying A, in terms of a matrix ρ: ρ = Σ_{b} Ψ*(a'b) Ψ(ab).

= Ψ(α)Ψ*(α'). (7.17)

αα' Surprisingly, Eq. 7.16 has exactly the same form as Eq. 7.14 for expectation value of a mixed state. Indeed, only in the very special case of a product state will ρ have the form of a projection operator. In other words, despite the fact that the composite system is described by a perfectly pure state, the subsystem A must be described by a mixed state.

There’s a subtle point about our notation for density matrices that’s worth noticing: in Eq. 7.17, the right-hand index of ρ, that is, the α' index, corresponds to the complex conjugate state-vector Ψ*(α'b) in the summation. This is a consequence of our convention L = ⟨α|L|α'⟩ αα' for labeling the matrix elements of an operator L. Applying this convention to ρ = |Ψ⟩⟨Ψ| results in ρ = ⟨α|Ψ⟩⟨Ψ|α'⟩, αα' or ρ = Ψ(α)Ψ*(α').

αα'

## 7.5 Entanglement for Two Spins

Before leading you further into the world of entanglement, I’ll give you a simple definition and a quick warm-up exercise. If Alice only has a single spin in a known state, her density matrix is defined to be ρ = ψ(α)ψ*(α').

αα' This equation tells you how to calculate an element of Alice’s density matrix. If we stick with our familiar σ basis, each index α and α' can take the values up and down, so Alice has a 2×2 density matrix.

Exercise 7.4: Calculate the density matrix for |Ψ⟩ = α|u⟩ + β|d⟩.

Answer: ψ(u) = α; ψ*(u) = α* ψ(d) = β; ψ*(d) = β* ρ = [ α*α  α*β ]

[ β*α  β*β ]

α'α Now try plugging in some numbers for α and β. Make sure they are normalized to 1. For example, α = √(1/2), β = √(1/2).

This simple example is a good way to understand the properties of density matrices. You can refer back to it as we look at the more complex example of an entangled state.

Suppose we know the wave function of a composite system, for example ψ(a,b), but we are only interested in Alice’s subsystem. In other words, we want to keep track of everything that Alice can ever measure. Do we have to know the whole wave function? Or is there some way to get rid of Bob’s variables? The answer to the latter question is yes; we can capture Alice’s complete description in terms of a density matrix ρ.

Let’s consider an observable L of Alice’s system. Like any observable, it can of course be represented as a matrix: L = ⟨α' b'|L|ab⟩.

α'b',ab Remember, for the composite system, the pair ab is really a single index labeling a basis vector.

When we say, “L is an Alice-observable,” what we mean is that L does nothing to Bob’s half of the state-label. This forces some restrictions on the form of L. The idea is to filter out (set equal to zero) any of L’s matrix elements that have the effect of changing Bob’s half of the state-label. In other words, L has the special form L = L_{α'α} δ_{b'b}. (7.18)

α'b',ab This simple-looking equation requires some explanation, and you may want to review the material on tensor products in component form, in the Interlude on tensor products (Section 6.1). The left-hand side of the equation is an element of a 4×4 matrix. Each of its two indices can take four distinct values: uu, ud, du, or dd. What about the right-hand side? The matrix element L_{α'α} also has two indices, but each of them can take only two distinct values: u or d. In fact, the same symbol L refers to two different matrices on each side of Eq. 7.18.

At first glance, it appears as though we have equated a 4 × 4 matrix to a 2 × 2 matrix, and indeed that would be a problem. However, the factor δ_{b'b} makes everything work out. The term L_{α'α} δ_{b'b} is an element of the tensor product of two 2 × 2 matrices, and that tensor product is a 4 × 4 matrix.6 Here is the way to read Eq. 7.18: The 4 × 4 matrix L_{α'b',ab} can be factored into a tensor product of the two 2×2 matrices L_{α'α} and δ_{b'b}, where δ_{b'b} is equivalent to the 2×2 identity matrix.

Now, let’s calculate the expectation value of L (the 4 × 4 version) using the full apparatus of the composite system: ⟨Ψ|L|Ψ⟩ = Σ ψ*(a',b') L_{a'b',ab} ψ(a,b).

a,b,a',b' As I warned, there are lots of indices. But it gets simpler if we use the special form of the matrix L. The factor δ_{b'b} in Eq. 7.18—a Kronecker delta—filters out any elements that change Bob’s half of the label, and leaves the others intact. It tells us to set b' = b to get ⟨Ψ|L|Ψ⟩ = Σ ψ*(a',b) L_{a'a} ψ(a,b). (7.19)

a',a For the moment, let’s ignore the sums over a and a', and concentrate instead on the sum over b. We encounter the quantity ρ_{a'a} = Σ ψ*(a',b) ψ(a,b). (7.20)

b The 2×2 matrix ρ 是 Alice 的密度矩阵。请注意，ρ_{a'a} 不依赖于任何 b 索引，因为它已经对 b 求和过了。它纯粹是 Alice 变量 a 和 a' 的函数。实际上，我们在方程中保留 b 只是为了让下一节的例子更容易理解。

我们可以通过将 Eq. 7.20 中的 ρ 代入来简化 Eq. 7.19。L（2×2 版本）的期望值变为： ⟨L⟩ = Σ_{a',a} ρ_{a'a} L_{a,a'}。 (7.21)

通过对 b 求和，我们将一个 4×4 矩阵简化为一个 2×2 矩阵。这是合理的。我们预期作用于复合系统的算符是 4×4 矩阵，而 Alice 的算符是 2×2 矩阵。

请注意，Eq. 7.21 的右边是对角矩阵元素的求和。换句话说，它是矩阵 ρL 的迹，我们可以写成： ⟨L⟩ = Tr(ρL)。

教训是：要计算 Alice 的密度矩阵 ρ，我们可能需要知道完整的波函数，包括对 Bob 变量的依赖。但一旦我们知道 ρ，就可以忘记它的来源，并用它来计算关于 Alice 观测的任何东西。作为一个简单的例子，我们可以用 ρ 来计算概率 P(a)，即如果进行测量，Alice 的系统将处于状态 a 的概率。要确定 P(a)，我们从 P(a,b) 开始，即组合系统处于状态 |ab⟩ 的概率。那就是： P(a,b) = ψ*(a,b)ψ(a,b)。

根据概率的标准规则，如果我们对 b 求和，就得到 a 的概率： P(a) = Σ_b ψ*(a,b)ψ(a,b)。

这只是密度矩阵中的一个对角元素： P(a) = ρ_{aa}。 (7.22)

以下是密度矩阵的一些性质： • 密度矩阵是厄米的： ρ_{a'a} = ρ_{aa'}*。

• 密度矩阵的迹为 1： Tr(ρ) = 1。

Eq. 7.22 应该有助于澄清这一点，因为左边是一个概率。

• 密度矩阵的特征值都是正数，并且介于 0 和 1 之间。由此可知，如果任何一个特征值是 1，那么所有其他特征值都是 0。你能解释这个结果吗？

• 对于纯态： ρ² = ρ Tr(ρ) = 1 • 对于混合态或纠缠态： ρ² ≠ ρ Tr(ρ) < 1

最后两个性质为我们提供了一种清晰的数学方法来区分纯态和混合态。纠缠态的一个子系统（例如单态中 Alice 的那一半）被认为是混合态。

值得花一点时间更好地理解这两个性质。为了简化，我们将假设 ρ 是一个对角矩阵——换句话说，它的所有非对角元素都为零。这种简化没有损失，因为 ρ 是厄米的，而且事实证明，每个厄米矩阵都可以在某个基中表示为对角形式。⁷

计算对角矩阵的平方很简单：你只需要对每个元素进行平方。由于 ρ 代表一个混合态，并且 ρ 的对角元素之和必须为 1，因此 ρ 的对角元素都不能等于 1。否则，ρ 将代表一个纯态。因此，ρ 必须至少有两个小于 1 的正对角元素。对这些元素进行平方会得到一个新矩阵 ρ²，其元素更小。这解释了 ρ 的两个混合态性质。

在你尝试下一个练习之前，我还要提一下迹的另一个性质。事实证明，迹有许多有趣的数学性质。它更有用的性质之一是两个矩阵乘积的迹不依赖于它们的乘法顺序。换句话说： Tr(AB) = Tr(BA)， 即使 AB ≠ BA。

我提到这一点是因为你有时会看到密度矩阵的迹写成 Tr(Lρ)，而不是 Tr(ρL)。这两个表达式是等价的。

练习 7.5： a) 证明 [a  0; 0  b]² = [a² 0; 0  b²]。

b) 现在，假设 ρ = [1/3  0; 0  2/3]。

计算 Tr(ρ) 和 Tr(ρ²)。

c) 如果 ρ 是一个密度矩阵，它代表纯态还是混合态？

练习 7.6：使用 Eq. 7.22 证明如果 ρ 是一个密度矩阵，那么 Tr(ρ) = 1。

## 7.6 一个具体例子：计算 Alice 的密度矩阵

到目前为止，对密度矩阵的讨论对一些读者来说可能有点抽象。这里有一个详细的例子，应该有助于使密度矩阵更加清晰。回顾 Eq. 7.20 中 Alice 密度矩阵的定义： ρ_{a'a} = Σ_b ψ*(a,b) ψ(a',b)。 (7.23)

现在，考虑态矢量 |Ψ⟩ = (1/√2)(|ud⟩ + |du⟩)。

请注意，两个基矢的系数是 1/√2，而另外两个…… two have coefficients of zero. The state is normalized because the sum of the squared coefficients is 1. Also, all four coefficients happen to be real, which simplifies the process of complex conjugation.

Let’s calculate Alice’s density matrix for this state. First, for all possible inputs a and b, we’ll list the values of ψ(a,b). Recall that these are just the basis vector coefficients: ψ(u,u) = 0 ψ(u,d) = √ ψ(d,u) = √ ψ(d,d) = 0.

Next, we’ll use these four equations to calculate each element of Alice’s density matrix by expanding the summation of Eq. 7.23. In the expansion, notice that for every factor of the form ψ∗(a,b)ψ(a',b), Bob’s input is the same for both factors. We discard any terms that do not have this property. This is what we mean by “setting b' equal to b in the summation.” Here is the expansion: ρ_uu = ψ∗(u,u)ψ(u,u) + ψ∗(u,d)ψ(u,d) = ρ_ud = ψ∗(u,u)ψ(d,u) + ψ∗(u,d)ψ(d,d) = 0 ρ_du = ψ∗(d,u)ψ(u,u) + ψ∗(d,d)ψ(u,d) = 0 ρ_dd = ψ∗(d,u)ψ(d,u) + ψ∗(d,d)ψ(d,d) = .

These values are the elements of a 2×2 matrix: ρ = (1/2) * [1 0; 0 1]. (7.24)

The trace of our matrix is 1. And our density matrix is done.8

Exercise 7.7: Use Eq. 7.24 to calculate ρ². How does this result confirm that ρ represents an entangled state? We’ll soon discover that there are other ways to check for entanglement.

Exercise 7.8: Consider the following states: |ψ⟩ = |uu⟩ + |ud⟩ + |du⟩ + |dd⟩ |ψ⟩ = √ (|uu⟩ + |dd⟩)

|ψ⟩ = 3|uu⟩ + 4|ud⟩.

For each one, calculate Alice’s density matrix and Bob’s density matrix. Check their properties.

## 7.7 Tests for Entanglement

Suppose I gave you a wave function ψ(a,b) for the composite S_AB system. How could you tell whether the corresponding state is entangled? I am not referring to an experimental test but to a mathematical procedure. A related question is whether there are varying degrees of entanglement. If there are, how could you quantify them?

Entanglement is the quantum mechanical generalization of correlation. In other words, it indicates that Alice can learn something about Bob’s half of the system by measuring her own. In the classical example of the previous lecture, I illustrated the idea of correlation using coins. If Alice observes the coin that Charlie gave her, she not only knows whether her own coin is a penny or a dime; she also knows which coin Bob has. That’s the experimental picture. The mathematical indication of correlation is that the probability function P(a,b) does not factorize (that is, it does not look like Eq. 6.3). Whenever the probability distribution does not factorize, there are nonzero correlations as I described in Inequality 6.2.

7.7.1 The Correlation Test for Entanglement

Let’s assume that A is an Alice observable and B is a Bob observable. The correlation between them is defined in terms of the average values (also known as the expectation values) of the individual observables, and of their product. Suppose that ⟨A⟩, ⟨B⟩, ⟨AB⟩ are these expectation values. The correlation C(A,B) between A and B is defined as C(A,B) = ⟨AB⟩ − ⟨A⟩⟨B⟩.

Exercise 7.9: Given any Alice observable A and Bob observable B, show that for a product state, the correlation C(A,B) is zero.

From this exercise, we can learn something about entanglement. If a system is in a state where one can find any two observables A and B that are correlated—meaning that C(A,B) ≠ 0—then the state is entangled. Correlations are defined to lie in the range −1 to +1. These extreme values represent the greatest possible negative and positive correlations. The greater the magnitude of C(A,B), the more entangled is the state. If C(A,B) = 0, then there is no correlation (and no entanglement) at all.

7.7.2 The Density Matrix Test for Entanglement

To calculate correlations, you have to know about both Bob’s part and Alice’s part of the system, along with the system wave function. But there is another test for entanglement that only requires us to know Alice’s (or Bob’s) density matrix. Let’s suppose that the state |Ψ⟩ is a product state of a Bob factor |φ⟩ and an Alice factor |ψ⟩. That means the composite wave function is also the product of a Bob factor and an Alice factor: ψ(a,b) = ψ(a)φ(b).

Now, let’s work out Alice’s density matrix. We use the definition in Eq. 7.20 to get ρ = Σ_{a,a'} ψ*(a)ψ(a') φ*(b)φ(b).

But if Bob’s state is normalized, then Σ_b φ*(b)φ(b) = 1, which makes Alice’s density matrix particularly simple: ρ = Σ_{a,a'} ψ*(a)ψ(a'). (7.25)

Notice that it only depends on the Alice variables. Perhaps it’s not very surprising that everything we need to know abo

8Art’s a poet, and he’s not even aware of it.

But Alice’s system is contained in Alice’s wave function.

Now, I’m going to prove a key theorem about the eigenvalues of Alice’s density matrix, under the assumption of a product state. It is true only for unentangled states and serves to identify them. The theorem says that for any product state, Alice’s (or Bob’s) density matrix has exactly one nonzero eigenvalue, and that eigenvalue is exactly 1. We begin the theorem by writing the eigenvalue equation for the matrix ρ:

ρ α = λα .

a'a a' a a'

In other words, the matrix ρ acting on the column vector α gives back the same vector multiplied by an eigenvalue λ. Using the simple form of ρ in Eq. 7.25, we can write

∑ ψ(a) ψ*(a')α = λα . (7.26)

a a'

Now, you may notice a couple of things. First, the quantity ∑ ψ*(a')α has the form of an inner product. If the column vector α is orthogonal to ψ, then the left side of Eq. 7.26 is zero. Such a vector is an eigenvector of ρ with eigenvalue zero.

If the dimension of Alice’s space of states is N, then there are N − 1 vectors orthogonal to ψ. Each one of them is an eigenvector of ρ with eigenvalue 0. That leaves only one possible direction for an eigenvector with a nonzero eigenvalue, namely the vector ψ(a). In fact, if we plug in α = ψ(a), we do indeed find that it is an eigenvector of ρ with eigenvalue 1.

To summarize the theorem: If the composite Alice-Bob system is in a product state, then Alice’s (or Bob’s) density matrix has one and only one eigenvalue equal to 1, and all the rest are zero. Moreover, the eigenvector with a nonzero eigenvalue is nothing but the wave function of Alice’s half of the system.

In this situation, Alice’s system is in a pure state. All of Alice’s observations are described as if Bob and his system never existed and Alice had an isolated system described by the wave function ψ(a).

The opposite extreme of a pure state is a maximally entangled state. Maximally entangled states are states of a combined system in which nothing is known about either subsystem, even though they are complete descriptions of the system as a whole—as complete as quantum mechanics allows. The state |sing⟩ is a maximally entangled state.

When Alice calculates her density matrix for a maximally entangled state, she finds something very disappointing: the density matrix is proportional to the unit matrix. All the eigenvalues are equal, and given that they all sum to unity, each eigenvalue is equal to 1/N. In other words,

ρ = δ . (7.27)

a'a a'a

Why is Alice disappointed? Go back to Eq. 7.22. This equation says that the probability for a particular state a is the diagonal element of ρ, but Eq. 7.27 tells us that all the probabilities are equal. What could be less informative than a probability distribution so structureless that every possible outcome is equally probable?

Maximal entanglement implies a complete lack of information about Alice’s subsystem for experiments that only involve that one subsystem. On the other hand, it implies a large correlation between Alice’s and Bob’s measurements. For the singlet state, if Alice measures any component of her spin, she automatically knows the result Bob would get if he were to measure the same component of his spin. This is exactly the kind of knowledge that is precluded in a product state.

So in each type of state, some things are predictable and some are not. In a product state, we can make statistical predictions about measurements made on each separate subsystem, but Alice’s measurements tell her nothing about Bob’s system. In a maximally entangled state, on the other hand, Alice can predict nothing about her own measurements, but she knows a great deal about the relation between her outcomes and Bob’s.

## 7.8 The Process of Measurement

We have seen that quantum systems evolve in what look like irreconcilably different ways: by unitary evolution between measurements, and by wave function collapse when measurements take place. This circumstance has led to some of the most contentious debates and confusing claims about so-called reality. I’m going to steer away from those debates and stick to the facts. Once you know how quantum mechanics works, you can decide for yourself whether you think there is a problem.

Let’s begin by noting that every measurement involves a system and an apparatus. But if quantum mechanics is a consistent theory, then it should be possible to combine the system and apparatus into a single bigger system. For simplicity let’s take the system to be a single spin. The apparatus A is the same one that we used in the very first lecture. The window in the apparatus can show three possible readings. The first is blank—it represents the neutral state of the apparatus before it comes in contact with the spin. The two other readings record the two po possible outcomes of the measurement: +1 or −1.

If the apparatus is a quantum system (of course, it must be), then it is described by a space of states. In the simplest description, the apparatus has exactly three states: a blank state and two outcome states. Thus, the basis vectors for the apparatus are |b⟩, |+1⟩, |−1⟩.

Meanwhile, the basis states of the spin can be taken to be the usual up and down states: |u⟩, |d⟩.

From these two sets of basis vectors, we can build up a composite (tensor product) space of states that has the six basis vectors |u,b⟩, |u,+1⟩, |u,−1⟩, |d,b⟩, |d,+1⟩, |d,−1⟩.

The detailed mechanics of what takes place when system meets apparatus may be complicated, but we are free to make some assumptions about how the combined system evolves. Let’s assume the apparatus starts in the blank state and the spin starts in the up state. After the apparatus interacts with the spin, the final state (by assumption) is |u,+1⟩.

In other words, the interaction leaves the spin unchanged but flips the apparatus to the +1 state. We write this as |u,b⟩ → |u,+1⟩. (7.28)

Similarly, we can require that if the spin is in the down state, it flips the apparatus to the −1 state: |d,b⟩ → |d,−1⟩. (7.29)

So by looking at the apparatus after it interacts with the spin, you can tell what the spin was initially. Now, let’s assume that the initial spin state is more general, namely α_u |u⟩ + α_d |d⟩.

If we include the apparatus as part of the system, the initial state is α_u |u,b⟩ + α_d |d,b⟩. (7.30)

This initial state is a product state, specifically a product of the initial spin state and the blank apparatus state. You can check that it is completely unentangled.

Exercise 7.10: Verify that the state-vector in 7.30 represents a completely unentangled state.

Because we know from Eqs. 7.28 and 7.29 how the individual terms in 7.30 evolve, we can easily determine the final state: α_u |u,b⟩ + α_d |d,b⟩ → α_u |u,+1⟩ + α_d |d,−1⟩.

This final state is an entangled state. In fact, if α_u = −α_d, it is the maximally entangled singlet state. Indeed, one can look at the apparatus and immediately tell what the spin state is: if the apparatus reads +1, the spin is up, and if it reads −1, the spin is down. Moreover, the probability that the final apparatus shows +1 is |α_u|^2.

This number represents a probability—it’s exactly the same as the original probability that the spin was up. In this description of a measurement, no collapse of the wave function takes place. Instead, entanglement between the apparatus and the system just happens by unitary evolution of the state-vector.

The only problem is that, in a certain sense, we have merely delayed the difficulty. It is not very satisfying to be told that the apparatus “knows” the spin state unless the experimenter—let’s say Alice—is allowed to look at the apparatus. Isn’t it true that when she does so, she will collapse the wave function of the composite system? Yes and no. For all of Alice’s purposes, yes; she will conclude that the apparatus, and the spin, are in one of the two possible configurations and will proceed accordingly.

But now let’s bring Bob into the picture. So far, he has not interacted with the spin, the apparatus, or Alice. From his point of view, all three form a single quantum system. No wave function collapse took place when Alice looked at the apparatus. Instead, Bob says that Alice became entangled with the other two component systems.

That’s all well and good, but what happens when Bob looks at Alice? For his purposes, he has collapsed the wave function. But then there is good old Charlie ...

Does the last entity to look at the system collapse the wave function, or does it just get entangled? Or is there a last looker? I won’t try to answer these questions, but what should be apparent is that quantum mechanics is a consistent calculus of probabilities for a certain kind of experiment involving a system and an apparatus. We use it, and it works, but when we try to ask questions about the underlying “reality,” we get confused.

## 7.9 Entanglement and Locality

Does quantum mechanics violate locality? Some people think so. Einstein railed against the “spooky action at a distance” (spukhafte Fernwirkung) that he claimed was implied by quantum mechanics. And John Bell became almost a cult figure by proving that quantum mechanics is nonlocal.

On the other hand, most theoretical physicists, particularly those who study quantum field theory, which is riddled with entanglement, would claim the opposite: quantum mechanics done correctly ensures locality.

The problem, of course, is that the two groups mean different things by locality. Let’s begin with the quantum field theorist’s understanding of the term.

From this point of view, locality has only one meaning: it is impossible to send a signal faster than the speed of light. I will show you how quantum mechanics enforces this rule.

First, let me expand the definition of Alice’s system and Bob’s system. So far, I have used the term Alice’s system to mean some system that Alice carries with her and can do experiments on. For the rest of this section, I will use the term to mean something else: Alice’s system consists not only of some system that she carries, but also the apparatus that she uses, and even herself. The same thing, of course, goes for Bob’s system. The basis ket-vectors |a describe everything that Alice can interact with. Likewise, the ket-vectors |b describe everything that Bob can interact with. And the tensor product states |ab describe the combination of Alice’s and Bob’s worlds.

We will assume that Alice and Bob may have been close enough to interact sometime in the past, but at present Alice is on Alpha Centauri and Bob is in Palo Alto. The Alice-Bob wave function is ψ(ab), and it may be entangled. Alice’s complete description of her system, her apparatus, and herself is contained in her density matrix ρ: ρ = ψ*(ab)ψ(ab). (7.31)

Consider this question: Can Bob, at his end, do anything to instantly change Alice’s density matrix? Keep in mind that Bob can only do things that the laws of quantum mechanics allow. In particular, Bob’s evolution, whatever causes it, must be unitary. In other words, it must be described by a unitary matrix U. The matrix U represents whatever happens to Bob’s system, whether or not Bob does an experiment. It acts on the wave function to produce a new wave function, which we’ll call the “final” wave function: ψ_final(ab) = U ψ(ab). We can also write the complex conjugate of this wave function: ψ*_final(a'b) = ψ*(a'b') U†. Notice that we added primes to some of the symbols to avoid mixing them up in the next step.

Now, let’s calculate Alice’s new density matrix. We’ll use Eq. 7.31, but we’ll replace the original wave functions with the final ones: ρ = ψ*(a'b'') U† U ψ(ab'). There are lots of indices flying around now, but the math isn’t as hard as it looks. In fact, look at how the U matrices enter through the combination U† U. This combination is just the matrix product U†U. But recall that U is unitary. This tells you that the product U†U is the unit matrix δ. As before, this amounts to an instruction to include all the terms where b'' = b', and to ignore all the others. With this simplification, we get ρ = ψ*(ab)ψ(ab). This is exactly the same as Eq. 7.31. In other words, ρ is exactly the same as it was before U acted. Nothing that happens at Bob’s end has any immediate effect on Alice’s density matrix, even if Bob and Alice are maximally entangled. This means that Alice’s view of her subsystem (her statistical model) remains exactly as it was. This remarkable result may seem surprising for a maximally entangled system, but it also guarantees that no faster-than-light signal has been sent.

## 7.10 The Quantum Sim: An Introduction to Bell’s Theorem

It’s interesting that unitarity played a prominent role in guaranteeing that no signal can be sent instantaneously. If U had not been unitary, Alice’s final density matrix would indeed have been affected by Bob.

What was it, then, that disturbed Einstein so much that he spoke of spooky action at a distance? To answer this question, it’s important to understand that he and Bell were talking about a totally different notion of locality. To illustrate this, I am going to invent a computer game. What my new computer game does is try to fool you into thinking there is a quantum spin in a magnetic field inside the computer. You get to do experiments to test this possibility. See Fig. 7.1 for a schematic.

Here’s how it works: Inside the computer, the memory stores two complex numbers, α_u and α_d, subject to the usual normalization rule, α*_u α_u + α*_d α_d = 1. At the beginning of the game, the α coefficients are initialized at some value. The computer then solves the Schrödinger equation to update the α’s exactly as if they were the components of the spin’s state-vector.

The computer also stores the classical three-dimensional orientation of the apparatus in the form of two angles or a vector.

用户可以随时按下M按钮来测量自旋（未显示）。在两次测量之间，自旋状态根据薛定谔方程演化。键盘允许你设置这些角度并随意更改。内存中还存储了一个元素，即表示仪器窗口中数字的值（+1或−1）。计算机屏幕显示仪器。作为实验者，你可以选择仪器的朝向。还有一个测量按钮M，用于激活仪器。

程序的最后一个元素是随机数生成器，它以概率α*α和α*α分别产生测量结果+1或−1。请记住，随机数生成器并非真正的随机数生成器；它们是随机数模拟器。它们基于完全经典的确定性机制，使用π的数字等来生成数字。尽管如此，它们足以迷惑你。

游戏开始，计算机持续更新αu和αd的值。你等待任意长时间，然后按下M按钮。接着，在随机数生成器的帮助下，游戏产生一个显示在屏幕上的结果。根据这个结果，计算机通过坍缩更新状态。如果结果是+1，αd的值重置为零，αu的值重置为1。如果结果是−1，αu的值重置为1，αd的值重置为零。然后，薛定谔方程接管，直到你再次按下M。

作为一个好的实验者，你进行多次试验并收集统计数据，将其与量子力学预测进行比较。如果一切正常，你会得出结论：量子力学是对计算机中发生过程的正确描述。当然，计算机仍然是完全经典的，但它毫无困难地模拟了量子自旋。

接下来，让我们尝试用两台计算机A和B模拟两个量子自旋。如果自旋从乘积态开始且从未相互作用，我们可以在两台计算机上分别进行游戏，无需任何交互。但现在，爱丽丝、鲍勃和查理回来帮助我们。查理想要创建一个纠缠对。他首先用电缆连接两台计算机形成一台计算机，我们假设电缆可以发送瞬时信号。在内存中，组合计算机现在存储四个复数：αuu、αud、αdu、αdd，并使用薛定谔方程更新这些数字。每台计算机屏幕显示一个仪器。爱丽丝的屏幕显示A，鲍勃的屏幕显示B。每个虚拟仪器可以独立定向，并且可以由各自的M按钮独立激活。当按下任一M按钮时，联合内存（在随机数生成器的帮助下）向相应仪器发送信号并产生结果。

这个设备能模拟双自旋系统的量子力学吗？是的，它可以——只要连接计算机的电缆不断开，并且只要它能瞬时发送消息。但除非系统处于乘积态并保持乘积态，否则断开两台计算机将破坏模拟。

我们能证明这一点吗？答案也是肯定的——这正是贝尔定理的核心内容。任何试图在空间上分离爱丽丝和鲍勃仪器的量子力学经典模拟，都必须有一根瞬时电缆连接独立的计算机和一个存储并更新态矢量的中央内存。

但这是否意味着违反局域性的信息可以通过电缆发送？如果允许爱丽丝、鲍勃和查理做任何非相对论经典系统能做的事情，那么是的。但如果只允许模拟量子操作的操作，那么答案是否定的。正如我们所看到的，量子力学不允许爱丽丝的密度矩阵受到鲍勃行动的影响。

这个问题不是量子力学的问题。它是用经典布尔计算机模拟量子力学的问题。这就是贝尔定理的内容：经典计算机必须用瞬时电缆连接才能模拟纠缠。

## 7.11 纠缠总结

在量子力学迫使我们接受的所有反直觉概念中，纠缠可能是最难接受的。对于一个完整状态描述不包含其任何单个子组件信息的系统，没有经典的类比。非局域性甚至难以定义。解决这些问题的最佳方式是内化数学。以下是我们关于纠缠所学内容的简明总结。特别是，我们试图描绘出纠缠之间的差异。

led, unentangled, and partially entangled states by creating "rap sheets" for three specific examples—the singlet state, a product state, and a "near singlet" state. We hope this format will help clarify the mathematical similarities and differences. Please take some time to review this material and work the exercises before moving on.

State-Vector Rap Sheet 1 Name: Product State (No Entanglement)

Wanted for: Excessive Locality, Impersonating a Classical System Description: Each subsystem is fully characterized. There are no correlations between Alice’s and Bob’s systems.

State-Vector: α_u β_u |uu⟩ + α_u β_d |ud⟩ + α_d β_u |du⟩ + α_d β_d |dd⟩ Normalization: α_u*α_u + α_d*α_d = 1, β_u*β_u + β_d*β_d = 1 Density Matrix: Alice’s density matrix has exactly one nonzero eigenvalue, which equals 1. The eigenvector with this nonzero eigenvalue is the wave function of Alice’s subsystem. The same goes for Bob.

Wave Function: Factorized: ψ(a)φ(b)

Expectation Values: ⟨σ_x⟩² + ⟨σ_y⟩² + ⟨σ_z⟩² = 1 ⟨τ_x⟩² + ⟨τ_y⟩² + ⟨τ_z⟩² = 1 Correlation: ⟨σ_z τ_z⟩ − ⟨σ_z⟩⟨τ_z⟩ = 0

State-Vector Rap Sheet 2 Name: Singlet State (Maximum Entanglement)

Wanted for: Nonlocality, Complete Quantum Weirdness Description: The composite system as a whole is fully characterized. There is no information about Alice’s or Bob’s subsystems.

State-Vector: (1/√2) (|ud⟩ − |du⟩)

Normalization: ψ_uu*ψ_uu + ψ_ud*ψ_ud + ψ_du*ψ_du + ψ_dd*ψ_dd = 1 Density Matrix: Full Composite System: ρ² = ρ, and Tr(ρ²) = 1.

Alice’s Subsystem: Density matrix is proportional to the unit matrix, having equal eigenvalues that add up to 1. Hence, each measurement outcome is equally likely. ρ² ≠ ρ, and Tr(ρ²) < 1.

Wave Function: Not Factorized: ψ(a,b)

Expectation Values: ⟨σ_z⟩, ⟨σ_x⟩, ⟨σ_y⟩ = 0 ⟨τ_z⟩, ⟨τ_x⟩, ⟨τ_y⟩ = 0 ⟨τ_z σ_z⟩, ⟨τ_x σ_x⟩, ⟨τ_y σ_y⟩ = −1 Correlation: ⟨σ_z τ_z⟩ − ⟨σ_z⟩⟨τ_z⟩ = −1

State-Vector Rap Sheet 3 Name: "Near-Singlet" (Partial Entanglement)

Wanted for: Indecision, General Wishy-Washiness, Trouble Telling up from down Description: There is some information about the composite system, and some about each subsystem. Incomplete in each case.

State-Vector: 0.6|ud⟩ − √0.4|du⟩ Normalization: ψ_uu*ψ_uu + ψ_ud*ψ_ud + ψ_du*ψ_du + ψ_dd*ψ_dd = 1 Density Matrix: Full Composite System: ρ² ≠ ρ, and Tr(ρ²) < 1.

Alice’s Subsystem: ρ² ≠ ρ, and Tr(ρ²) < 1.

Wave Function: Not Factorized: ψ(a,b)

Expectation Values: ⟨σ_z⟩ = 0.2 ⟨σ_x⟩, ⟨σ_y⟩ = 0; ⟨τ_z⟩ = −0.2 ⟨τ_x⟩, ⟨τ_y⟩ = 0 ⟨τ_x σ_x⟩ = −2√0.24 Correlation: ⟨σ_z τ_z⟩ − ⟨σ_z⟩⟨τ_z⟩ = −0.96 for this example.

For partially entangled states in general, correlation is between −1 and +1, but not exactly 0.

Exercise 7.11: Calculate Alice’s density matrix for σ for the "near-singlet" state.

Exercise 7.12: Verify the numerical values in each rap sheet.

Lecture 8 Particles and Waves Art and Lenny have had enough entanglement for now. They’re ready for something simpler.

Lenny: Hey Hilbert, do you have anything in one dimension?

Hilbert: Let me check. Single dimensions are very popular lately. Sometimes we run out.

Art: I’d settle for something classical, if that’s all you have.

Hilbert: Not here, friend. We’d lose our license.

Art: Good point.

To the person in the street, quantum mechanics is all about light being particles and electrons being waves. But up until now, I’ve hardly mentioned particles, and the only mention of waves has been the wave function, which so far has had nothing to do with waves. So when do we get to the "real" quantum mechanics?

The answer, of course, is that real quantum mechanics is not so much about particles and waves as it is about the nonclassical logical principles that govern their behavior. Particle-wave duality is an easy extension of the things you’ve already learned, as we’ll see in this lecture. But before we get into the physics, I want to review some mathematics, some of which is old—it appeared in earlier lectures—and some of which is new.

## 8.1 Mathematical Interlude: Working with Continuous Functions

8.1.1 Wave Function Review We’ll be using the language of wave functions in this lecture, so let’s review some of that material before we dive in. In Lecture 5, we discussed wave functions as abstract objects, without explaining what they had to do with either waves or functions. Before correcting this omission, I will review what we discussed earlier.

Begin by picking an observable L, with eigenvalues λ and eigenvectors |λ⟩. Let |Ψ⟩ be a state-vector. Since the eigenvectors of a Hermitian operator form a complete orthonormal basis, the vector |Ψ⟩ can be expanded as |Ψ⟩ = ψ(λ) |λ⟩. (8.1)

As you recall from Sections 5.1.2 and 5.1.3, the quantities ψ(λ) are called the wave function of the system. But notice: the specific form of ψ(λ) depends on the specific observable L that we initially choose. If we pick a different observable, the wave function (along with the basis vectors and eigenvalues) will be different, even though we’re still talking about the same state. Therefore, we should qualify the statement that ψ(λ) is the wave function associated with |Ψ⟩. To be more precise, we should say that ψ(λ) is the wave function in the L-basis. If we use the orthonormality properties of the basis vectors, ⟨λ_i | λ_j⟩ = δ_ij, then the wave function in the L-basis may also be identified with the inner products (or projections) of the state-vector |Ψ⟩ onto the eigenvectors |λ⟩: ψ(λ) = ⟨λ|Ψ⟩.

You can think of the wave function in two ways. First of all, it is the set of components of the state-vector in a particular basis. These components can be stacked up to form a column vector: ⎛ ψ(λ_1) ⎞ ⎜ ψ(λ_2) ⎟ ⎜ ψ(λ_3) ⎟.

⎝ ... ⎠ Another way to think of the wave function is as a function of λ. If you specify any allowable value of λ, the function ψ(λ) produces a complex number. One can therefore say that ψ(λ) is a complex-valued function of the discrete variable λ. When thought of in this way, linear operators become operations that are applied to functions, and give back new functions.

One last reminder: the probability for an experiment to have outcome λ is P(λ) = ψ*(λ)ψ(λ).

8.1.2 Functions as Vectors Up until now, the systems we have studied have had finite dimensional state-vectors. For example, the simple spin is described by a two-dimensional space of states. For this reason, the observables have had only a finite number of possible observable values. But there are more complicated observables that can have an infinite number of values. An example is a particle. The coordinates of a particle are observables, but, unlike spin, the coordinates have an infinite number of possible values. For instance, a particle moving along the x axis can be found at any real value of x. In other words, x is a continuously infinite variable. When the observables of a system are continuous, the wave function truly becomes a function of a continuous variable. To apply quantum mechanics to this kind of system, we have to expand the idea of vectors to include functions.

Functions are functions, and vectors are vectors—they seem like different things, so in what sense are functions vectors? If you think of vectors as arrows pointing in three-dimensional space, then they are not the same as functions. But if you take the broader view of vectors as a set of mathematical objects satisfying certain postulates, then functions can indeed form a vector space. Such a vector space is often called a Hilbert space after the mathematician David Hilbert.

Let’s consider the set of complex functions ψ(x) of a single real variable x. By complex functions, I mean that for each x, ψ(x) is a complex number. On the other hand, the independent variable x is an ordinary real variable. It can take on any real value from −∞ to +∞.

Now, let’s nail down what we mean when we say “Functions are vectors.” This is not a loose analogy or a metaphor. With appropriate restrictions (that we’ll come back to), functions like ψ(x) satisfy the mathematical axioms that define a vector space. We mentioned this idea briefly in Section 1.9.2, and now we’ll make full use of it. Looking back at the axioms that define a complex vector space (in Section 1.9.1), we can see that complex functions satisfy all of them:

## 1. The sum of any two functions is a function

## 2. The addition of functions is commutative

## 3. The addition of functions is associative

4. There is a unique zero function such that when you add it to any function, you get the same function back.

5. Given any function ψ(x), there is a unique function −ψ(x) such that ψ(x)+(−ψ(x)) = 0.

## 6. Multiplying a function by any complex number gives a function and is linear

## 7. The distributive property holds, which means that

z[ψ(x)+φ(x)] = zψ(x)+zφ(x)

[z +w]ψ(x) = zψ(x)+wψ(x), where z and w are complex numbers.

All of this implies that we can identify the functions ψ(x) with the ket-vectors |Ψ⟩ in an abstract vector space. Not surprisingly, we can also define bra vectors. The bra vector ⟨Ψ| corresponding to the ket |Ψ⟩ is identified with the complex conjugate function ψ*(x).

To use this idea effectively, we’ll need to generalize some of the items in our mathem mathematical tool kit. In earlier lectures, the labels that identified wave functions were members of some finite discrete set—for example, the eigenvalues of some observable. But now the independent variable is continuous. Among other things, this means that we cannot sum over it using ordinary sums. I think you know what to do, though. Here are function-oriented replacements for three of our vector-based concepts, two of which you will easily recognize: • Integrals replace sums.

• Probability densities replace probabilities.

• Dirac delta functions replace Kronecker deltas.

Let’s look at these items more closely.

Integrals Replace Sums: If we really wanted to be rigorous, we would begin by replacing the x axis by a discrete set of points separated by a very small distance ε, and then take the limit ε → 0. It would take several pages to justify each step. But we can avoid this trouble by a few intuitive definitions, such as replacing sums with integrals. Schematically, this concept can be written as ∑ → ∫ dx.

For example, if we want to compute the area under a curve, we divide the x axis up into tiny segments and then add up the areas of a large number of rectangles, exactly as we do in elementary calculus. When we let the segments shrink to zero size, the sum becomes an integral.

Let’s consider a bra ⟨Ψ| and a ket |Φ⟩ and define their inner product. The obvious way to do this is to replace the summation in Eq. 1.2 with an integral. We define the inner product to be ⟨Ψ|Φ⟩ = ∫ ψ*(x)φ(x)dx. (8.2)

Probability Densities Replace Probabilities: Later, we will identify P(x) = ψ*(x)ψ(x)

as a probability density for the variable x. Why a probability density and not just a probability? If x is a continuous variable, then the probability that it will have any exact value is typically zero. A more useful question to ask is: What is the probability that x lies between two values, x = a and x = b? Probability densities are defined so that this probability is given by an integral: P(a,b) = ∫_a^b P(x) dx = ∫_a^b ψ*(x)ψ(x) dx.

Because the total probability should be 1, we can define a normalized vector by ∫_{-∞}^∞ ψ*(x)ψ(x) dx = 1. (8.3)

Dirac Delta Functions Replace Kronecker Deltas: So far, this should be very familiar. The Dirac delta function may be less so. The delta function is the analog of the Kronecker delta, δ_{ij}. The Kronecker delta is defined to be 0 for i ≠ j and 1 for i = j. But it can also be defined another way. Consider any vector F in a finite dimensional space. It is easy to see that the Kronecker delta satisfies ∑_j δ_{ij} F_j = F_i.

That’s because the only nonzero term in the sum is the one where j = i. Within the summation, the Kronecker symbol filters out all the F’s except F_i. The obvious generalization is to define a new function that has similar filtering properties when used inside an integral. In other words, we want a new entity δ(x−x')

with the property that, for any function F(x), ∫_{-∞}^∞ δ(x−x') F(x')dx' = F(x). (8.4)

Eq. 8.4 defines this new entity, called the Dirac delta function, which turns out to be an essential tool in quantum mechanics. But despite its name, it isn’t really a function in the usual sense. It is zero whenever x ≠ x', but when x = x' it is infinite. In fact it is just infinite enough that the area under δ(x) equals 1. Roughly speaking, it is a function that is nonzero over an infinitesimal interval ε, but on that interval it has the value 1/ε. Thus, its area is 1, and, more importantly, it satisfies Eq. 8.4. The function √n e^{-(nx)^2} approximates the delta function reasonably well as n becomes very large. Fig. 8.1 plots this approximation for increasing values of n. Even though we stop at n = 10, a very small value, notice that the graph has already become very narrow and sharply peaked.

8.1.3 Integration by Parts Before discussing linear operators, we’ll take a short detour to remind you of a technique called integration by parts. It’s fairly simple, and indispensable for our purposes. We’ll be using it again and again. Suppose we take two functions, F and G, and consider the differential of their product FG. We can write d(FG) = FdG+GdF or d(FG)−GdF = FdG.

Taking the definite integral gives us ∫_a^b d(FG) - ∫_a^b GdF = ∫_a^b FdG or [FG]_a^b - ∫_a^b GdF = ∫_a^b FdG.

This is the standard formula that you may remember from calculus. But in quantum mechanics the limits of integration tend to span the entire axis, and our wave functions must go to zero at infinity to be properly normalized. Therefore, the first term of this expression will always evaluate to zero. With that in mind, we can use a simplified version of integration by parts: ∫_{-∞}^∞ F (dG/dx) dx = - ∫_{-∞}^∞ G (dF/dx) dx.

This form is correct as long as F and G go to zero appropriately at infinity, so that the boundary term becomes zero. You will do yourself a big favor if you just memorize this pattern: Switch the derivative from one factor of the integrand to the other at the cost of a minus sign.

8.1.4 Linear Operators Bras and kets are half the story in quantum mechanics; the other half is the concept of linear operators and, in particular, Hermitian operators. This raises two questions: • What is meant by a linear operator on a space of functions?

• What is the condition for a linear operator to be Hermitian?

The concept of a linear operator is simple enough: it’s a machine that acts on a function and gives another function. When it acts on the sum of two functions, it gives the sum of the individual results. When it acts on a complex numerical multiple of a function, it gives the same multiple of the original result. In other words, it is (surprise!) linear.

Let’s look at some examples. One simple operation we can perform on a function ψ(x) is to multiply it by x. That gives a new function xψ(x), and you can easily check that the action is linear. We’ll represent the “multiply by x” operator with the symbol X. By definition, then, X ψ(x) = x ψ(x). (8.5)

Here’s another example. Define D to be the differentiation operator: D ψ(x) = dψ(x)/dx. (8.6)

Exercise 8.1: Prove that X and D are linear operators.

This, of course, is a minute subset of the possible linear operators that can be constructed, but we will soon see that X and D play a very central role in the quantum mechanics of particles.

Now, let’s consider the property of Hermiticity. A convenient way to define a Hermitian operator is through its matrix elements, by sandwiching it between a bra and a ket. You can sandwich an operator L in two different ways: ⟨Ψ|L|Φ⟩ or ⟨Φ|L|Ψ⟩.

In general, there is no simple relation between these two sandwiches. But in the case of a Hermitian operator (for which, by definition, L† = L) there is a simple relation: the two sandwiches are complex conjugates of each other: ⟨Ψ|L|Φ⟩ = ⟨Φ|L|Ψ⟩*.

Let’s see whether the operators X and D are Hermitian. Recalling that X ψ(x) = x ψ(x), and using the inner product formula Eq. 8.2, we can write ⟨Ψ|X|Φ⟩ = ∫ ψ*(x) x φ(x) dx and ⟨Φ|X|Ψ⟩ = ∫ φ*(x) x ψ(x) dx.

Because x is real, it’s easy to see that these two integrals are complex conjugates of each other, and therefore that X is Hermitian.

What about the operator D? In this case, the two sandwiches are ⟨Ψ|D|Φ⟩ = ∫ ψ*(x) (dφ(x)/dx) dx (8.7)

and ⟨Φ|D|Ψ⟩ = ∫ φ*(x) (dψ(x)/dx) dx. (8.8)

To determine if D is Hermitian, we need to compare these two integrals and see if they are complex conjugates of each other. In this form, it’s a bit difficult to tell. The trick is to do the second integral by parts. As we explained, integration by parts allows you to switch the derivative from one factor in the integrand to the other, as long as you change the sign at the same time. Therefore, the integral in Eq. 8.8 can be rewritten as ⟨Φ|D|Ψ⟩ = - ∫ (dφ*(x)/dx) ψ(x) dx. (8.9)

Now, we just need to compare the two expressions in Eqs. 8.7 and 8.9, which turns out to be easy. Because of the minus sign, it’s clear that they are definitely not complex conjugates of each other. Instead, their relationship is captured by ⟨Ψ|D|Φ⟩ = -⟨Φ|D|Ψ⟩*, which is the diametric opposite of what we wanted. Unlike the X operator, D is not Hermitian. Instead, it satisfies D† = -D.

An operator with this property is called anti-Hermitian. Although anti-Hermitian and Hermitian operators are opposites, it’s very easy to go from one to the other. All you have to do is multiply by the imaginary number i or -i. Therefore we can use D to construct an operator that is Hermitian, namely -iħD.

If we look at the action of this new Hermitian operator on wave functions, we find that -iħDψ(x) = -iħ (dψ(x)/dx). (8.10)

Keep this formula in mind. It will soon play a leading role in defining a very important property of particles—their momentum.

## 8.2 The State of a Particle

In classical mechanics, the “state of 一个“系统”指的是在已知作用力的情况下，预测该系统未来所需的一切信息。当然，这包括构成系统的所有粒子的位置以及这些粒子的动量。从经典力学的角度看，瞬时位置和动量是完全独立的变量。例如，对于一个质量为 m 的粒子沿一维 x 轴运动，系统的瞬时状态由一对 (x, p) 描述。坐标 x 是粒子的位置，p = mẋ 是其动量。这两个变量共同定义了系统的相空间。如果我们还知道粒子所受的力是其位置的函数，那么哈密顿方程允许我们计算其在所有未来时刻的位置和动量。它们定义了相空间中的一种流动。

由此，人们可能会猜测，一个粒子的量子态将由标记为位置和动量的态基所张成： |x, p⟩。

波函数将是这两个变量的函数： ψ(x, p) = ⟨x, p|Ψ⟩。

然而，这是不正确的。我们已经看到，在经典物理中可以同时知道的事物，在量子力学中可能不行。例如，自旋的不同分量，比如 σ_z 和 σ_x。一个人不能同时知道两个分量；因此，不存在两个分量都被指定的态。对于 x 和 p 也是如此：同时指定两个值是“过分”的。无论我们讨论的是自旋 (σ_z, σ_x) 还是位置和动量 (x, p)，这种不相容性最终是一个实验事实。

那么，对于 x 轴上的粒子，如果我们不能同时知道 x 和 p，我们能知道什么？答案是 x 或 p；因为根据位置和动量算符的数学性质，两者不对易。但我强调，这不是你能够提前预测的；它是数十年实验观察的结晶。

如果粒子的位置是一个可观测量，那么必须有一个与之关联的厄米算符。显而易见的候选者是算符 X。理解位置这个直观概念与数学算符 X 之间这种基本联系的第一步，是求出 X 的本征矢和本征值。本征值是可能被观测到的位置值，而本征矢代表具有确定位置的态。

8.2.1 位置的本征值和本征矢

下一个显而易见的问题是：测量 X 的可能结果是什么，以及在哪些态中它具有确定的（可预测的）值？换句话说，它的本征值和本征矢是什么？我们从 X 开始。X 的本征方程是 X|Ψ⟩ = x |Ψ⟩， 其中本征值记为 x。用波函数表示，这变为 x ψ(x) = x ψ(x)。 (8.11)

这最后一个方程看起来很奇怪。x 乘以一个函数怎么可能与同一个函数成正比？表面上看，这似乎不可能。但让我们深入探究。我们可以将方程 8.11 重写为 (x - x) ψ(x) = 0。

当然，如果一个乘积为零，那么至少其中一个因子必须为零。但其他因子可能不为零。因此，如果 x ≠ x，那么 ψ(x) = 0。这是一个非常强的条件。它表明，对于给定的本征值 x，函数 ψ(x) 只能在一个点上非零，即在 x = x 处。

对于一个普通的连续函数，这个条件将是致命的：没有合理的函数可以除了在一个点之外处处为零，而仅在该点非零。但这正是狄拉克 δ 函数 δ(x - x)

的性质。

显然，每一个实数 x 都是 X 的一个本征值，相应的本征矢是函数（我们常称之为本征函数），它们在 x = x 处无限集中。其含义很清楚：波函数 ψ(x) = δ(x - x)

代表粒子正好位于 x 轴上 x 点的态。

当然，代表已知位于 x 的粒子的波函数除了在 x 处之外处处为零，这是非常合理的。否则还能怎样呢？但看到数学证实了这种直觉是令人欣慰的。

考虑一个态 |Ψ⟩ 和一个位置本征态 |x⟩ 的内积： ⟨x|Ψ⟩。

利用方程 8.2，我们得到 ⟨x|Ψ⟩ = ∫_{-∞}^{∞} δ(x - x) ψ(x) dx。

根据方程 8.4 中给出的 δ 函数的定义，这个积分计算结果为 ⟨x|Ψ⟩ = ψ(x)。 (8.12)

因为这对任何 x 都成立，我们可以去掉下标，写出一般方程 ⟨x|Ψ⟩ = ψ(x)。 (8.13)

换句话说，沿 x 方向运动的粒子的波函数 ψ(x)，是态矢量 |Ψ⟩ 在位置本征矢上的投影。我们也将 ψ(x) 称为位置表象中的波函数。

8.2.2 Momentum and Its Eigenvectors Position is intuitive; momentum is less so, particularly in quantum mechanics. It will only be later that we see the connection between the operator that we identify with momentum and the familiar classical concept of mass times velocity. But I assure you that we will make the connection. For now, let’s take the abstract mathematical route. The momentum operator in quantum mechanics is called P, and it is defined in terms of the operator −iD: −iD = −i d/dx.

As we saw earlier in Eq. 8.10, we need the factor −i to make this operator Hermitian.

We could just define P to be −iD, but if we did, we would run into a problem later when we connect these ideas to those of classical physics. The reason should be clear—there’s a dimensional mismatch. In classical physics, the units of momentum are mass times velocity—in other words, mass times length divided by time (ML/T). On the other hand, the operator D has units of inverse length, or 1/L. The resolution of the mismatch is provided by Planck’s constant ℏ, which has units of ML²/T. The correct relation between P and D is therefore P = −iℏD (8.14)

or, in terms of its action on wave functions, Pψ(x) = −iℏ dψ(x)/dx. (8.15)

Quantum physicists often use units in which ℏ is exactly one, and in that way simplify the equations. As tempting as it is, we won’t do that here.

Let’s work out the eigenvectors and eigenvalues of P. The eigen-equation in abstract vector notation is P|Ψ⟩ = p|Ψ⟩, (8.16)

where the symbol p is an eigenvalue of P. Eq. 8.16 can also be expressed in terms of wave functions. Using the identification P = −iℏ d/dx, we can write the eigen-equation as −iℏ dψ(x)/dx = pψ(x)

or dψ(x)/dx = (ip/ℏ) ψ(x).

This is a type of equation that we’ve run into before. The solution has the form of an exponential: ψ_p(x) = A e^{ipx/ℏ}.

The subscript p is just a reminder that ψ_p(x) is the eigenvector of P with the specific eigenvalue p. It is a function of x, but it is labeled by an eigenvalue of P.

The constant A multiplying the exponential is not determined by the eigenvector equation. That’s nothing new; the eigenvalue equation never tells us the overall normalization of the wave function. As a rule, we fix the constant by requiring the wave function to be normalized to unit probability. An example that goes all the way back to Section 2.3 is the eigenvector of the x component of spin: |r⟩ = (1/√2) |u⟩ + (1/√2) |d⟩.

The factor 1/√2 is there to make sure the total probability is 1.

Normalizing the eigenvectors of P is a more subtle operation, but the result is simple. The factor A is only slightly more complicated than in the spin case. To save time, I will tell you the answer and leave it for you to prove later. The correct factor is A = 1/√(2π). Thus, ψ_p(x) = (1/√(2π)) e^{ipx/ℏ}. (8.17)

A point of some interest follows from Eqs. 8.13 and 8.17. The inner product of a position eigenvector |x⟩ and a momentum eigenvector |p⟩ has a very simple and symmetric form: ⟨x|p⟩ = (1/√(2π)) e^{ipx/ℏ} ⟨p|x⟩ = (1/√(2π)) e^{-ipx/ℏ}. (8.18)

The second equation is simply the complex conjugate of the first. These results are easy to verify if you keep in mind that |x⟩ is represented by a delta function. I’d like to mention two important points before moving further: 1. Eq. 8.17 represents a momentum eigenfunction in the position basis. In other words, although it represents a momentum eigenstate, it is a function of x, and not an explicit function of p.

2. We’ve been using the symbol ψ for both position and momentum eigenstates. A mathematician might not approve of using the same symbol for two different functions, but physicists do it all the time. ψ(x) is just the generic symbol for whatever function we happen to be discussing.

At this juncture, we begin to get a glimmer of why the wave function is called the wave function. What you should notice is that the eigenfunctions (wave functions representing eigenvectors) of the momentum operator have the form of waves—sine waves and cosine waves, to be precise. In fact, we can now see one of the most fundamental aspects of the wave-particle duality of quantum mechanics. The wavelength of the function e^{ipx/ℏ} is given by λ = 2πℏ/p because the value of the function is unchanged if we add 2πℏ/p to the variable x: e^{ip(x+2πℏ/p)/ℏ} = e^{ipx/ℏ} e^{2πi} = e^{ipx/ℏ}.

Let’s pause for a moment to discuss the importance of this connection between momentum and wavelength. It’s not just important: in many ways, it is the relationship that defined twentieth-century physics. Over the last hundred years, physicists have primarily been concerned with uncovering the laws of the microscopic world. This has meant figuring out how objects are built out of smaller objects. The examples are obvious: molecules are made from atoms; atoms from electrons and nuclei; nuclei from protons and neutrons. These subnuclear particles are const constructed out of quarks and gluons. And the game goes on as scientists search for ever smaller and more hidden entities.

All of these objects are too small to see with the best optical microscopes, let alone the naked eye. The reason is not just that our eyes are insufficiently sensitive. The more important fact is that eyes and optical microscopes are sensitive to the visible spectrum, which comprises wavelengths at least a few thousand times longer than the size of an atom. As a rule, you can’t resolve objects much smaller than the wavelength you’re using to look at them. For this reason, the story of twentieth-century physics was in large part a quest for smaller and smaller wavelengths of light—or any other kind of wave. In Lecture 10, we will discover that light of a given wavelength is composed of photons whose momentum is related to the wavelength by exactly the relation λ = 2πħ / p.

The implication is that to probe objects of ever smaller size one needs photons (or other objects) of ever larger momentum. Large momentum inevitably means large energy. It’s for that reason that the discovery of the microscopic properties of matter required increasingly powerful particle accelerators.

## 8.3 Fourier Transforms and the Momentum Basis

The wave function ψ(x) has the important role of determining the probability for finding the particle at position x: P(x) = ψ*(x)ψ(x).

As we will see, no experiment can determine both the position and momentum of a particle simultaneously. But if we forego determining anything about the position, momentum can be measured precisely. The situation is quite analogous to that of the x and z components of a spin. Either value can be measured, but not both.

What is the probability that a particle has momentum p if we choose to measure it? The answer is a straightforward generalization of the principles laid down in Lecture 3. The probability that a momentum measurement will give momentum p is P(p) = |⟨p|Ψ⟩|². (8.19)

The entity ⟨p|Ψ⟩ is called the wave function of |Ψ⟩ in the momentum representation. Naturally, it is a function of p and is denoted by a new symbol: ψ̃(p) = ⟨p|Ψ⟩. (8.20)

It is now clear that there are two ways to represent a state-vector. One way is in the position basis and the other is in the momentum basis. Both wave functions—the position wave function ψ(x) and the momentum wave function ψ(p)—represent exactly the same state-vector |Ψ⟩. It follows that there must be some transformation between them such that if you know ψ(x), the transformation produces ψ(p), and vice versa. In fact, the two representations are Fourier transforms of each other.

8.3.1 Resolving the Identity We are about to see the great power of the Dirac bra-ket notation in simplifying complicated things. First, let’s recall an important idea from earlier lectures. Suppose we define an orthonormal basis of states through the eigenvectors of some Hermitian observable. Call the basis vectors |i⟩. In Lecture 7, I explained a very useful trick, and now we are going to see just how useful it is. It’s called resolving the identity. The trick given in (Eq. 7.11) is to write the identity operator I (the operator that acts on any vector to give the same vector) in the form I = Σ_i |i⟩⟨i|.

Because momentum and position are both Hermitian, the sets of vectors |x⟩ and |p⟩ each define basis vectors. By replacing summation with integration we discover two ways to resolve the identity: I = ∫ dx |x⟩⟨x| (8.21)

and I = ∫ dp |p⟩⟨p|. (8.22)

Let’s suppose that we know the wave function of the abstract vector |Ψ⟩ in the position representation. By definition, it is equal to ψ(x) = ⟨x|Ψ⟩. (8.23)

Now suppose we want to know the wave function ψ(p) in the momentum representation. Here are the steps laid out in detail:

• First, use the definition of the momentum-representation wave function: ψ̃(p) = ⟨p|Ψ⟩.

• Now, insert the unit operator between the bra- and ket-vectors, in the form given in Eq. 8.21: ψ̃(p) = ∫ dx ⟨p|x⟩⟨x|Ψ⟩.

• The expression ⟨x|Ψ⟩ is just the wave function ψ(x), and ⟨p|x⟩ is given to us by the second equation of Eqs. 8.18: ⟨p|x⟩ = (1/√(2πħ)) e^{-i p x / ħ}.

• Putting it all together, we find that ψ̃(p) = (1/√(2πħ)) ∫ dx e^{-i p x / ħ} ψ(x). (8.24)

This equation shows us exactly how to transform a given wave function in the position representation into the corresponding wave function in the momentum representation. What is it good for? Suppose the position wave function for some particle is known; however, the goal of your experiment is to measure the momentum, and you want to know the probability of observing momentum p. The procedure is to first calculate ψ(p) by using 使用公式8.24，然后计算概率 \tilde{\psi}^*\tilde{\psi}。

反过来也同样容易。假设我们知道 \tilde{\psi}(p) 并希望恢复 \psi(x)。这次，我们使用公式8.22来分解恒等式。步骤如下（注意它们与之前的步骤惊人地相似）： • 首先，使用位置表象波函数的定义： \psi(x) = \langle x|\Psi\rangle • 现在，在bra-和ket-矢量之间插入单位算符，形式如公式8.22所示： \psi(x) = \int dp \langle x|p\rangle \langle p|\Psi\rangle。

• 表达式 \langle p|\Psi\rangle 就是波函数 \tilde{\psi}(p)，而 \langle x|p\rangle 由公式8.18给出。但这次，是两个公式中的第一个。

\langle x|p\rangle = \frac{1}{\sqrt{2\pi}} e^{i p x / \hbar}。

• 将所有内容放在一起，我们发现 \psi(x) = \frac{1}{\sqrt{2\pi}} \int dp e^{i p x / \hbar} \tilde{\psi}(p)。

让我们再看一下从位置到动量来回转换的两个公式。注意它们多么对称。唯一的不对称是一个公式包含 e^{i p x / \hbar}，另一个包含 e^{-i p x / \hbar}： \tilde{\psi}(p) = \frac{1}{\sqrt{2\pi}} \int dx e^{-i p x / \hbar} \psi(x)

\psi(x) = \frac{1}{\sqrt{2\pi}} \int dp e^{i p x / \hbar} \tilde{\psi}(p)。 (8.25)

公式8.25总结的位置和动量表象之间的关系是，它们是彼此的互逆傅里叶变换。事实上，这些是傅里叶分析领域的核心方程。我希望你注意到，使用狄拉克优雅的符号推导这些方程是多么容易。

## 8.4 对易子与泊松括号

早些时候，在第4讲中，我们阐述了关于对易子的两个重要原理。第一个与经典力学和量子力学之间的联系有关；第二个与不确定性有关。我现在将通过展示这些原理与 X 和 P 的关系来结束这个非常长的讲座。

我们将从对易子与经典物理的联系开始。你可能还记得，我们发现对易子与泊松括号有极大的相似性，我们在公式4.21中明确了这种关系。如果我们将本讲中使用的算符符号 L 和 M 代入，我们得到 [L, M] \Leftrightarrow i\hbar\{L, M\}, (8.26)

这提醒我们，量子运动的方程与其经典对应物非常相似。这表明，通过计算可观测量 X 和 P 的对易子，我们可能会学到一些东西。幸运的是，这很容易做到。

首先，让我们看看乘积 XP 作为算符作用于任意波函数 \psi(x) 时做了什么。回顾公式8.5和8.15，我们可以写出 X\psi(x) = x\psi(x)

P\psi(x) = -i\hbar \frac{d\psi(x)}{dx}。

这些方程共同告诉我们乘积 XP 如何作用于 \psi(x)： XP\psi(x) = -i\hbar x \frac{d\psi(x)}{dx} (8.27)

现在，让我们尝试以相反的顺序使用 X 和 P： PX\psi(x) = -i\hbar \frac{d}{dx} [x\psi(x)]。

要计算这个最后的表达式，我们只需使用乘积 x\psi(x) 的标准微分规则。使用这个规则，很容易看出 PX\psi(x) = -i\hbar x \frac{d\psi(x)}{dx} - i\hbar \psi(x)。 (8.28)

现在，我们将从公式8.27中减去公式8.28，以展示对易子如何作用于波函数： [X, P]\psi(x) = XP\psi(x) - PX\psi(x)

或 [X, P]\psi(x) = i\hbar \psi(x)。

换句话说，当对易子 [X, P] 作用于任何波函数 \psi(x) 时，它所做的只是将 \psi(x) 乘以数字 i\hbar。我们可以通过写作来表达这一点 [X, P] = i\hbar。 (8.29)

这本身极其重要。X 和 P 不对易的事实是理解它们为何不能同时被测量的关键。但当我们把这个方程与等价式8.26（它将对易子与经典泊松括号联系起来）进行比较时，事情变得更加有趣。事实上，公式8.29表明相应的经典泊松括号是 \{x, p\} = 1， 这正是坐标与其共轭动量之间的经典关系（见第一卷，第10讲，公式8）。最终，正是这种联系解释了为什么量子动量的概念与经典概念相关联。

使用第5讲中的一般不确定性原理，我们现在可以专门针对情况 [X, P] = i\hbar。

和 \Delta X \Delta P \geq \frac{\hbar}{2}。

我们将在下一节中进行。

现在让我们回忆涉及对易子的第二个原理。在第4讲中，我们发现两个可观测量 L 和 M 不能同时确定，除非它们对易。如果它们不对易，你就不能在不干扰 M 的测量的情况下测量 L。不可能找到两个不对易可观测量的共同本征向量。这导致了一般不确定性原理。

## 8.5 海森堡不确定性原理

现在，女士们先生们，这就是你们一直等待的。终于：海森堡不确定性原理。

海森堡不确定性原理是量子力学最著名的结果之一：它不仅断言粒子的位置和动量不能同时被知道，而且它 also provides an exact quantitative limit for their mutual uncertainties. At this point, I suggest that you revisit Lecture 5, where I explained the general uncertainty principle. We did all the work there, and now we get to reap the benefits.

As we’ve seen, the general uncertainty principle puts a quantitative limit on the simultaneous uncertainties of two observables A and B. This idea was captured in Inequality 5.13: ΔA ΔB ≥ |(cid:2)Ψ|[A,B]|Ψ(cid:3)|.

Now let’s apply this principle directly to the position and momentum operators X and P. In this case, the commutator is just a number and its expectation is that same number. Replacing A and B with X and P gives ΔX ΔP ≥ |(cid:2)Ψ|[X,P]|Ψ(cid:3)|, and replacing [X,P] with ih¯ results in ΔX ΔP ≥ |ih¯(cid:2)Ψ|Ψ(cid:3)|.

But (cid:2)Ψ|Ψ(cid:3) equals 1, and the end result is ΔX ΔP ≥ h¯.

No experiment can ever beat this limitation. You can try your best to determine a particle’s momentum and position simultaneously in a reproducible manner, but no matter how careful you are, the uncertainty in the position times the uncertainty in the momentum will never be less than 1h¯.

As we saw in Section 8.2.1, the wave function of an eigenstate of X is highly concentrated about some point x; in this eigenstate, the probability is also perfectly localized. On the other hand, the probability P(x) for a momentum eigenstate is uniformly spread over the entire x axis. To see this, let’s take the wave function in Eq. 8.17 and multiply it by its complex conjugate: (cid:2) (cid:3)(cid:2) (cid:3)

1 1 1 ψ p ∗ (x)ψ p (x) = √ e −i h¯ px √ e ip h¯ x = .

2π 2π 2π

The result is completely uniform, with no peaks anywhere on the x axis. Evidently, a state with definite momentum is completely uncertain in its position.

Fig. 8.2 illustrates the definition of uncertainty for the position variable x. In the top half of the figure, you can see that the uncertainty Δx is a measure of how spread out the function is in relation to its expectation value (cid:2)x(cid:3). The label d shows the deviation of one point in relation to (cid:2)x(cid:3); this may be a positive or negative quantity. The uncertainty Δx is the result of an averaging process over all possible d’s and characterizes the function as a whole. To prevent the positive d’s from canceling the negative ones, each d value is squared during this averaging process.

The bottom half of Fig. 8.2 shows how the calculation can be simplified by shifting the origin to coincide with (cid:2)x(cid:3). The numerical value of Δx is unchanged by this shift.

Figure 8.2: Uncertainty Basics. Top: (cid:2)x(cid:3) to right of origin. Deviations d may be positive or negative. Overall uncertainty Δx (> 0) derived from the average value of d2. Bottom: Origin shifted right, (cid:2)x(cid:3) = 0, Δx has same value.

Lecture 9 Particle Dynamics

Art and Lenny expected some action at Hilbert’s Place. But all the state-vectors were absolutely still—frozen, you might say.

Lenny: This is boring, Art. Doesn’t anything ever happen around here? Hey Hilbert, why is this joint so still?

Hilbert: Oh, don’t worry. Things will pick up as soon as the Hamiltonian gets here.

Art: The Hamiltonian? He sounds like a real operator.

## 9.1 A Simple Example

The first two volumes of the Theoretical Minimum series have largely focused on two questions. The first is: What do we mean by a system and how do we describe the momentary states of a system? As we’ve seen, the classical and quantum answers to this question are very different. Classical phase space—the space of coordinates and momenta—is replaced in quantum theory by the linear vector space of states.

The second big question is: How do states change with time? In both classical mechanics and quantum mechanics, the answer is according to the minus first law. In other words, states change so that information and distinctions are never erased. In classical mechanics, this principle led to Hamilton’s equations and Liouville’s theorem. Earlier, in Lecture 4, I explained how in quantum mechanics this law led to the principle of unitarity, which in turn led to the general Schrödinger equation.

Lecture 8 was all about the first question: How do we describe the state of a particle? Now, in the current lecture, we come to the second question, which we might rephrase: How do particles move in quantum mechanics?

In Lecture 4, I laid out the basic rules for how quantum states change with time. The essential ingredient is the Hamiltonian H, which in both classical and quantum mechanics represents the total energy of a system. In quantum mechanics, the Hamiltonian controls the time evolution of a system through the time-dependent Schrödinger equation: ∂|Ψ(cid:3)

ih¯ = H|Ψ(cid:3). (9.1)

∂t

This lecture is all about the Original Schrödinger Equation—the equation that Schrödinger wrote down to describe a quantum mechanical particle. The Original Schrödinger Equation is a special case of Eq. 9.1. The motion of ordinary (nonrelativistic) particles in classical mechanics is governed by a Hamiltonian, equal to the kinetic energy plus the potential energy. We will soon come to the quantum version of this Hamiltonian, but first let’s look at a Hamiltonian that’s even simpler.

We’ll start with the simplest Hamiltonian I can think of. In this case, the Hamiltonian operator H is a fixed constant times the momentum operator P: H = cP. (9.2) This example is rarely written down, though it turns out to be quite instructive. The constant c is a fixed number. Is cP a reasonable Hamiltonian for a particle? Yes it is, and in a moment we’ll find out what kind of particle it describes. For now, just notice that Eq. 9.2 is different from what we might expect for a nonrelativistic particle. In other words, it’s not P²/2m. This simpler example is worth exploring first, just to see how the mathematical apparatus works.

How do we represent this example in terms of wave functions ψ(x) in the position basis? We’ll start by plugging our operators into the time-dependent Schrödinger equation (Eq. 9.1): iℏ ∂ψ(x,t)/∂t = −ciℏ ∂ψ(x,t)/∂x. Notice that we’re now writing ψ as a function of both x and t. Canceling the iℏ terms gives us ∂ψ(x,t)/∂t = −c ∂ψ(x,t)/∂x, (9.3) which is a pretty simple equation. In fact, any function of (x−ct) is a solution. By “function of (x−ct),” I mean any function that depends not on x and t separately, but only on the combination (x−ct). To see how this works, just consider an arbitrary function ψ(x − ct) and look at its derivatives. If you take the partial with respect to x, you just get ∂ψ(x−ct)/∂x because the derivative of (x−ct) with respect to x is 1. But if you take the partial with respect to t, you get −c ∂ψ(x−ct)/∂t. It’s clear that this combination of derivatives satisfies Eq. 9.3; therefore any function of this form solves the Schrödinger equation.

Now, let’s see how a function ψ(x−ct) behaves. What does it look like? How does it evolve with time? Suppose we start by looking at a snapshot at t = 0. We can call the snapshot ψ(x) because it tells us what ψ looks like at every point in space at the specific time t = 0. Of course, we don’t want just any function of (x−ct). We want the total probability ∫ ψ*(x)ψ(x)dx from −∞ to ∞ to equal 1. In other words, we want ψ(x) to fall off nicely to zero at infinity so that the integral doesn’t blow up. Figure 9.1 shows ψ(x) schematically. With these characteristics, it makes sense to call ψ(x) a wave packet.

Now that we’ve described the snapshot ψ(x) at t = 0, what happens if we let time move forward? As t increases, the wave packet keeps the exact same shape. Every feature of the complex-valued function ψ(x,t) moves with uniform velocity c to the right.¹

I had a reason for giving the name c to our constant—the symbol c often stands for the speed of light. So is this particle a photon? No, not really. But our description of this hypothetical particle is pretty close to the correct description of a neutrino that moves at the speed of light. (Real neutrinos probably move at a speed that is immeasurably smaller than the speed of light.) This Hamiltonian would be a very good description of a one-dimensional neutrino except for one problem: the particle described by our wave function can only move to the right. To round out this description, we would have to add another possibility—that the particle could also move to the left!²

Our right-going zax³ has another oddball feature—its energy can be either positive or negative. This is because the P operator, as a vector, can take on positive or negative values. In general, the energy of a particle with negative momentum is negative, and the energy of a particle with positive momentum is positive. I won’t say more about this except that the problem of negative energy for this kind of particle was solved by Dirac, who used it to establish the theoretical basis for antiparticles. For our purposes, we can ignore this issue and simply allow the energy of our particle to be either positive or negative.

Since the wave function of our particle moves rigidly down the x axis, so does the probability distribution. As a result, the expectation value of x moves in exactly the same way, which is to say that it moves to the right with velocity c. That’s the essential quantum mechanics of this system. However, there is another important thing to keep in mind. When we said the velocity c is a fixed constant, we

¹ This includes both the real and the imaginary parts of ψ(x).

² Our right-going particles remind me of Dr. Seuss’s classic story “The Zax,” and I’m tempted to call them “right-going zaxons.” There’s no telling how the story would have turned out if Theodor Geisel had known more about neutrinos.

³ There. I’ve said it.

don't kidding. Our particle can only exist in a state where it moves at this particular velocity. It can never slow down or speed up.

How does this compare with the classical description of such a particle? Starting with the same Hamiltonian, a classical physicist would just write Hamilton’s equations. With H = cP, Hamilton’s equations are

∂H/∂p = ẋ

and

∂H/∂x = −ṗ.

Carrying out the partial derivatives, these become

∂H/∂p = ẋ = c

and

∂H/∂x = −ṗ = 0.

Thus, in the classical description of our particle, the momentum is conserved, and the position moves with fixed velocity c. In the quantum mechanical description, the whole probability distribution and the expectation value move with velocity c. In other words, the expectation value of position behaves according to the classical equations of motion.

## 9.2 Nonrelativistic Free Particles

Only massless particles can move at the velocity of light, and I might add, they can only move at that velocity. All known particles other than photons and gravitons are massive and can move at any velocity less than c. When they move with a velocity much less than c, they are said to be nonrelativistic and their motion is governed by ordinary Newtonian mechanics, at least classically. The earliest application of quantum mechanics was to the motion of nonrelativistic particles.

I showed earlier (in Lectures 4 and 8) that Poisson brackets play the same mathematical role in classical mechanics as commutators do in quantum mechanics. Written with these constructs, the classical and quantum mechanical equations of motion are almost identical in form. In particular, the Hamiltonian comes into play in the same way with Poisson brackets as it does with commutators. So, if you want to write down the quantum mechanical equations of a system whose classical physics you already know, it’s very reasonable to try using the classical Hamiltonian, translated into operator form.

For a nonrelativistic free particle, the natural Hamiltonian to try is p²/2m. When we say the particle is free, what we really mean is that no forces are acting on it, and therefore we can ignore potential energy. All we care about is the kinetic energy, which is defined as

T = mv²/2.

As you recall, the momentum for a classical particle is

p = mv.

The Hamiltonian is just the kinetic energy, which we can write in terms of the momentum p. This gives us

H = mv²/2 = p²/2m

for the Hamiltonian of a classical nonrelativistic free particle. Unlike the right-going zaxon of the previous example, the energy of this particle does not depend on its direction of motion. That’s because the energy is proportional to p² rather than p itself. So we’ll start with a particle whose energy is p²/2m and work out the Schrödinger equation (the original one that Schrödinger discovered) for a free particle.

Our plan is to follow the same process we used in the previous example, using the Hamiltonian to write a time-dependent Schrödinger equation. As usual, the left side of the equation is

iħ ∂ψ/∂t.

We’ll derive the right-hand side by rewriting the classical Hamiltonian—the kinetic energy—as an operator. The classical kinetic energy is

p²/2m.

The quantum version replaces p with P:

H = P²/2m.

What is the meaning of this? As we’ve seen, the operator P is defined as

P = −iħ ∂/∂x.

The square of P is just the operator that you get by allowing P to act twice in succession. Thus,

P² = (−iħ ∂/∂x)(−iħ ∂/∂x),

or

P² = −ħ² ∂²/∂x²,

and the Hamiltonian becomes

H = −(ħ²/2m) ∂²/∂x².

Finally, if we equate the left- and right-hand sides of the time-dependent Schrödinger equation, we get

iħ ∂ψ/∂t = −(ħ²/2m) ∂²ψ/∂x². (9.4)

This is the traditional Schrödinger equation for an ordinary nonrelativistic free particle. It is a particular kind of wave equation, but, in contrast to the previous example, waves of different wavelength (and momenta) move with different velocities. Because of this, the wave function does not maintain its shape. Unlike the zaxon wave function, it tends to spread out and fall apart. This is shown schematically in Fig. 9.2.

Figure 9.2: Typical Wave Packet for a Nonrelativistic Free Particle. Top: The initial wave packet is compact and highly localized. Bottom: Over time, the wave packet moves to the right and spreads out.

## 9.3 Time-Independent Schrödinger Equation

We are going to solve the time-dependent Schrödinger equation for nonrelativistic free particles, but first we need to solve the time-independent version. The time-independent equation is essentially the eigenvector equation for the Hamiltonian,

H|Ψ⟩ = E|Ψ⟩,

written explicitly in terms of the wave function ψ(x):

−(ħ²/2m) ∂²ψ(x)/∂x² = Eψ(x). (9.5)

It’s very easy to find a complete set of eigenvectors that satisfy this equation. In fact, momentum eigenvectors do the job. Let’s t 试用函数 ψ(x) = e^{ipx/ℏ} (9.6)

作为一个可能的解。进行求导后，我们发现这个函数确实是方程9.5的解，只要我们设 E = p^2 / 2m。 (9.7)

这应该不足为奇——毕竟，在方程9.5中，E代表一个能量本征值。

练习9.1：将方程9.6代入方程9.5，推导方程9.7。

正如我们在第4.13节所看到的，定态薛定谔方程的每一个解都允许我们构造一个含时解。我们所需要做的就是将定态解——在本例中是 e^{ipx/ℏ} ——乘以 e^{-iEt/ℏ} = e^{-ip^2t/(2mℏ)}。因此，一组完整的解可以写成 ψ(x,t) = exp[i(px - p^2t/(2m))/ℏ]。

任何解都是这些解的求和或积分： ψ(x,t) = ∫ ψ̃(p) exp[i(px - p^2t/(2m))/ℏ] dp。

你可以从t=0时的任意波函数开始，通过傅里叶变换找到ψ(p)，并让它演化。形状会改变，因为不同p值的波以不同的速度传播。但是，正如我们很快将看到的，整个波包将以速度⟨p⟩/m传播，就像经典粒子一样。

这个简单的通解有一个重要的含义。除其他外，它表明动量表象的波函数随时间以一种非常简单的方式变化： ψ̃(p,t) = ψ̃(p) exp[-ip^2t/(2mℏ)]。

换句话说，只有相位随时间变化，而幅度保持不变。这之所以有趣，是因为概率P(p)根本不随时间变化。当然，这是动量守恒的结果，但它只在粒子不受力作用时才成立。

## 9.4 速度与动量

到目前为止，我还没有解释算符P与经典动量概念——即质量乘以速度，或 v = p/m (9.8)

——之间的联系。我们所说的量子力学粒子的速度是什么意思？最简单的答案是，我们指的是平均位置⟨Ψ|X|Ψ⟩的时间导数： v = d⟨Ψ|X|Ψ⟩/dt 或者更具体地说，用波函数表示， v = ∫ ψ*(x,t) x ∂ψ(x,t)/∂t dx。

为什么⟨Ψ|X|Ψ⟩会随时间变化？因为ψ依赖于时间，而且事实上我们确切地知道它是如何依赖的。ψ的时间演化由含时薛定谔方程支配。我们可以利用这一事实来推导⟨Ψ|X|Ψ⟩如何随时间变化。我曾用这种方法——通过蛮力计算——它需要好几页纸。幸运的是，你在前面课程中学到的抽象方法使其更容易；事实上，我们在第4讲中已经完成了大部分工作。实际上，在我们继续之前，我建议你复习第4讲，特别是从开头到方程4.17出现的部分。重述方程4.17： d⟨L⟩/dt = (i/ℏ) ⟨[H, L]⟩。

换句话说：任何可观测量L的期望值的时间导数由i/ℏ乘以哈密顿量与L的对易子的期望值给出。将此原理应用于速度v，我们发现 v = (1/2mh̄) ⟨[P^2, X]⟩。 (9.9)

现在，我们所要做的就是计算P^2和X的对易子。几个简单的步骤表明 [P^2, X] = P[P, X] + [P, X]P。 (9.10)

这个关系可以通过展开每个对易子并发现一些明显的消去来确认。

练习9.2：通过展开两边并比较结果来证明方程9.10。

最后一步使用了标准对易关系 [P, X] = -iℏ。

将其代入方程9.10，并将结果代入方程9.9，我们发现 v = ⟨P⟩/m 或者，也许更熟悉的形式是 ⟨P⟩ = mv。 (9.11)

我们已经证明了我们想要证明的：动量等于质量乘以速度，或者更准确地说，平均动量等于质量乘以速度。

为了更好地理解这意味着什么，让我们假设波函数具有波包或相当窄的波峰的形式。x的期望值将大致位于波峰的中心。方程9.11告诉我们，波包的中心按照经典规则p = mv运动。

## 9.5 量子化

在继续讨论量子力学中的力这个主题之前，我想暂停一下，讨论一下我们已经做了什么。我们从一个众所周知且值得信赖的经典系统——自由粒子——开始，并将其量子化。我们可以将这个过程归纳如下： 1. 从一个经典系统开始。这意味着一组坐标x和动量p。在我们的例子中，只有一个坐标和一个动量，但这个过程很容易推广。坐标和动量成对出现，x_i和p_i。经典系统还有一个哈密顿量，它是x和p的函数。

## 2. 将经典相空间替换为线性向量空间。在位置表象中，状态空间由一个依赖于坐标的波函数ψ(x)表示。

在一般情况下，所有坐标都适用。

## 3. 将 x 和 p 替换为算符 X 和 P。每个 X 作用于波函数时，将其乘以 x。每个 P 按以下规则作用：

P → -iℏ ∂/∂x。

4. 当这些替换完成后，哈密顿量成为一个算符，可用于含时或不含时的薛定谔方程。含时方程告诉我们波函数如何随时间变化。不含时形式则允许我们找到哈密顿量的本征矢和本征值。

这种量子化过程是将经典方程转换为量子方程的手段。它已被反复应用于从粒子运动到量子电动力学的各个领域；甚至有人尝试（虽不成功）对爱因斯坦的引力理论进行量子化。正如我们在一个简单案例中所见，该过程保证了期望值的运动与经典运动密切相关。

这一切引出了一个“鸡与蛋”的问题：哪个在先——经典理论还是量子理论？物理学的逻辑起点应该是经典的还是量子的？我认为答案显而易见。量子力学是对自然的真实描述。经典力学虽然优美而简洁，但终究是一种近似。粗略地说，当波函数以波包形式保持形状时，它才成立。有时，我们很幸运，一个系统的量子理论可以通过从一个熟悉的经典系统出发并对其进行量子化来猜测——而这仅仅是一种猜测。有时这确实有效。从经典粒子力学推导出的电子量子运动就是一个例证。从麦克斯韦方程组推导出的量子电动力学是另一个例证。但有时没有经典理论可作为起点。粒子的自旋没有真正的经典对应物。而广义相对论的量子化在很大程度上已经失败。量子理论可能比经典理论更为根本，后者通常应被理解为一种近似。

话虽如此，我现在将继续对粒子的运动进行量子化，但这次将纳入力的效应。

## 9.6 力

如果所有粒子都是自由的，世界将会是一个乏味的地方。力使粒子做出有趣的事情，例如将它们自己组装成原子、分子、巧克力棒和黑洞。作用在任何给定粒子上的力，是宇宙中所有其他粒子施加在它身上的力的总和。在实践中，我们通常假设我们知道所有其他粒子在做什么，并用一个势能函数来替代它们对所研究粒子的影响。这在经典力学和量子力学中都是成立的。

势能函数记为 V(x)。在经典力学中，它与粒子所受的力通过以下方程相关： F(x) = -∂V/∂x。

如果运动是一维的，偏导数可以替换为常导数，但我将保持原样。如果我们将此方程与牛顿第二定律 F = ma 结合，得到： m d²x/dt² = -∂V/∂x。

在量子力学中，我们采用不同的方法；我们写出哈密顿量并求解薛定谔方程。将势能纳入这个方案是直接了当的。势能 V(x) 变成一个算符 V，被添加到哈密顿量中。

V 是什么类型的算符？如果我们用波函数的语言而非抽象的右矢和左矢来思考，答案最容易表达。当算符 V 作用于任何波函数 ψ(x) 时，它将波函数乘以函数 V(x)。

V|ψ⟩ → V(x)ψ(x)。

与经典力学一样，一旦包含力，粒子的动量就不守恒了。事实上，牛顿运动定律可以表述为： dp/dt = F 或 dp/dt = -∂V/∂x。 (9.12)

量子化的规则要求我们将 V(x) 添加到哈密顿量中，⁴ H = P²/(2m) + V(x)， (9.13)

并以明显的方式修改薛定谔方程： iℏ ∂ψ/∂t = -ℏ²/(2m) ∂²ψ/∂x² + V(x)ψ Eψ = -ℏ²/(2m) ∂²ψ/∂x² + V(x)ψ。 (9.14)

这有什么影响？附加项当然会影响 ψ 随时间变化的方式。如果波包的平均位置要遵循经典轨迹，这当然是必须的。为了验证我们的推理，让我们看看它是否确实如此。首先，方程 9.11 仍然成立吗？它应该成立，因为动量与速度之间的关系不受力的影响。

由于 H 中添加了一个新项，在 X 和 H 的对易子中也会出现一个新项。这可能会修改方程 9.9 中速度的表达式，但很容易看出这并没有发生。新项涉及 X 与 V(x) 的对易子。

--- ⁴ 严格来说，这对自由粒子也成立。然而，在自由粒子的情况下，我们将 V(x) 设为 0。 ). But multiplying by x and multiplying by a function of x are operations that commute. In other words, [X,V(x)] = 0. Therefore, the connection between velocity and momentum is unaffected by forces in quantum mechanics, as is the case in classical mechanics.

The more interesting question is: Can we understand the quantum version of Newton’s law? As stated above, this law can be written as dp/dt = F.

Let’s calculate the time derivative of the expectation value of P. Again, the trick is to commute P with the Hamiltonian: d⟨P⟩/dt = (i/2mh̄)⟨[P², P]⟩ + (i/h̄)⟨[V, P]⟩. (9.15)

The first term is zero because an operator commutes with any function of itself. To compute the second term, we’ll use an equation that we haven’t proved yet: [V(x), P] = i h̄ dV(x)/dx. (9.16)

Plugging Eq. 9.16 into Eq. 9.15, we get d⟨P⟩/dt = -⟨dV/dx⟩.

Now, let’s prove Eq. 9.16. Letting the commutator act on a wave function, we can write [V(x), P]ψ(x) = V(x)(-iħ d/dx)ψ(x) - (-iħ d/dx)V(x)ψ(x). (9.17)

This is easily simplified and results in Eq. 9.16. Thus, we have shown that d⟨P⟩/dt = -⟨dV/dx⟩, (9.18)

which is the quantum analog of Newton’s equation for the time rate of change of momentum.

Exercise 9.3: Show that the right-hand side of Eq. 9.17 simplifies to the right-hand side of Eq. 9.16. Hint: First expand the second term by taking the derivative of the product. Then look for cancellations.

## 9.7 Linear Motion and the Classical Limit

You might think we have proved that the expectation value of X exactly follows the classical trajectory. But what we’ve actually proved is quite different. This difference exists because the average of a function of x is not the same as the function of the average of x. If Eq. 9.18 had read d⟨P⟩/dt = -dV(⟨x⟩)/d⟨x⟩ [This is wrong]

(and, let me emphasize, it does not), then indeed we would say that the average position and momentum satisfy the classical equations. But in reality the classical equations are only approximations, good whenever we can replace the average of dV/dx by the function of the average of x. When is it reasonable to do this? The answer is whenever the V(x) varies slowly compared to the size of the wave packet. If V varies rapidly across the wave packet, the classical approximation will break down. In fact, in that situation a nice, narrow wave packet will get broken up into a badly scattered wave that has no resemblance to the original wave packet. The probability function will also get scattered. Then you’ll have no choice but to solve the Schrödinger equation.

Let’s look at this point more closely. Mathematically, we’ve made no assumptions about the shapes of our wave packets. But we have tacitly thought of them as being nicely shaped functions with a single maximum, smoothly trailing off to zero in the positive and negative directions. This condition, though not explicit in our mathematical assumptions, does have a real impact on whether a particle behaves the way classical mechanics would lead us to expect.

Figure 9.3: Bimodal (Two-Humped) Function, Centered at x = 0. Note that ⟨x⟩ = 0, but Δx > 0.

To illustrate this point, let’s consider a slightly “weird” wave packet. Fig. 9.3 shows a bimodal wave packet (having two maxima), centered at the origin of the x axis. Now, let’s consider some function of x, say F(x), where F represents force. The expectation value of F(x) is not the same as the function F of the expectation value of x. In other words, ⟨F(x)⟩ ≠ F(⟨x⟩).

The right-hand side is a function of the center of the wave packet. It is not the same as the left-hand side, which corresponds to our results from the previous section—⟨F(x)⟩ has the same form as the right-hand side of Eq. 9.18.5

Let me give you an example where these two expressions could be extremely different. Suppose that F is equal to x squared: F = x². And suppose the wave packet looks like Fig. 9.3. What’s the expectation value of x? It’s zero, and so is F(⟨x⟩), because F(0) = 0² = 0. On the other hand, what is the expectation value of x²? It’s greater than zero. So when a wave packet is not a nice, single bump that is mainly characterized by its center, it’s not always true that the time rate of change of the momentum is the force evaluated at the expectation value of x. It’s only when the wave function is concentrated over a fairly narrow range that the expectation value of F(x) is the same as F(⟨x⟩). So we have cheated a little in saying our quantum equation of motion looks classical. That depends on the wave packet being coherent and well localized.

Everything else being equal, when the mass of a particle is large, the wave function tends to be very well concentrated. If there are no very sharp spikes in the potential function V(x), then it will be a good approximation to replace ⟨F(x)⟩ with F(⟨x⟩). When V(x) has spikes, however, the wave packet tends to break up. For example, suppose we have a nice wave packet moving to the right, and it hits a point structure, like an atom, with a potential function similar to Fig. 9.4. The wave packet will spread out and disintegrate. If, on the other hand, it hits a very smooth potential, then it will go through the smooth potential, moving more or less according to the classical equations of motion. We don’t expect quantum mechanics to reproduce classical mechanics in every possible circumstance. We expect it to reproduce classical mechanics in circumstances where it should—where the particles are heavy, the potentials are smooth, and nothing causes the wave function to disintegrate or scatter.6

Figure 9.4: Spiky Potential Function. Potential functions with sharp peaks tend to cause wave functions to scatter. The smaller these features are in relation to the wave packet, the more the wave packet will scatter, and the less “classical” it will become.

What physical situations lead to “bad potentials” that break up the wave function? Suppose a potential has features that have a certain size associated with them. Think of Fig. 9.4 on steroids, with lots of large, closely packed spikes. Suppose we call the size of these features δx, and that δx is significantly smaller than the incoming particle’s uncertainty in position: δx < Δx. If the sharp features of V(x) exist on a scale that is much smaller than the size of the incoming wave packet, the packet will break into a lot of little pieces. Each one will scatter off in a different direction. Roughly speaking, when the features of the potential are shorter than the wavelength of the incoming particle, the wave function will tend to break up.

Let’s say you take a bowling ball and ask, “What is Δx?” We can use the uncertainty principle to gain some intuition about this question. Typically, Δp × Δx is bigger than ℏ. But in many reasonable cases it’s of order ℏ: ΔpΔx ∼ ℏ. Now, p is about as concentrated as it can be, but for an ordinary macroscopic object, the uncertainty relation is pretty much saturated—the left-hand side is roughly equal to ℏ. The reasons for this are very complicated, and I won’t go into them here. Instead, let’s assume this is true and work out the implications. What is Δp? It’s mΔv, which gives us mΔvΔx ∼ ℏ.

Rearranging the symbols, we can then write ΔvΔx ∼ ℏ/m or Δx ∼ ℏ/(mΔv). Now, if I put a bowling ball on the ground, I know very well that the uncertainty in its velocity is not very big. As the ball gets heavier and heavier, you might expect the uncertainty in velocity to get smaller and smaller. But, in any case, the right-hand side has an m in the denominator, and regardless of Δv, as m gets smaller, Δx will get bigger. And in particular, it will tend to get bigger than the features in the potential.

In the quantum mechanical limit where m is very small and Δx tends to be big, the wave function will move under the influence of a ragged potential, which it sees as being much sharper and more featured than the wave function itself. That’s when the wave function breaks up. On the other hand, as m gets very large, Δx gets small. For a large bowling ball, the wave packet might be very concentrated. When it moves through a spiky potential, this tiny wave function encounters a potential whose features are (comparatively) very broad. Moving through broad smooth features does not break the wave function into pieces. Large masses and smooth potentials characterize the classical limit. A particle with low mass, moving through an abrupt potential, behaves like a quantum mechanical system.

What about electrons? Are they massive enough to behave classically? The answer depends on the interplay between the potential and the mass. For example, if you have two capacitor plates separated by a centimeter, with a smooth electric field between them, then the electron will move across the gap like a nice, coherent, almost classical particle. On the other hand, the potential associated with the nucleus of an atom always has a sharp feature in it. If an electron wave packet hits this potential, it will scatter all over the place.

Before leaving this topic, I’d like to mention minimum-uncertainty wave packets. These are wave packets where ΔxΔp is equal to ℏ/2 (as opposed to being greater). In other words, in these cases, ΔxΔp is as small as quantum mechanics allows. These wave packets have the form of a Gaussian curve, and they’re often called Gaussian wave packets. Over time, they spread out and flatten. Such wave packets are not that common, but they do exist. A bowling ball at rest is a good approximation. In Lecture 10, we’ll see that the ground state of a harmonic oscillator is a Gaussian wave packet.

## 9.8 Path Integrals

Classical Hamiltonian mechanics focuses on the step-by-step incremental changes in the state of a system. But there is another way to formulate mechanics—the Principle of Least Action—in which the focus is on entire histories. For a particle, this means looking at the full trajectory of the particle from some initial time to some final time. The content of the two approaches is the same, but the emphasis is different. Hamiltonian mechanics zeros in on some instant and tells you how the system changes between that instant and the next. The least action principle steps back and takes a global look. One can imagine nature sampling all possible trajectories and picking the one that minimizes the action between a pair of fixed initial and final points.7

Quantum mechanics also has a Hamiltonian description that concentrates on incremental changes. It’s called the time-dependent Schrödinger equation, and it’s very general. As far as we know, it can be used to describe all physical systems. Still, it seems fair to ask, as Richard Feynman did almost seventy years ago, whether there is a way to look at quantum mechanics that pictures whole histories. In other words, is there a formulation that parallels the Principle of Least Action? I will not explain Feynman’s path integral description in detail in this lecture, but just to whet your appetite I’ll give you a hint of how it works.

First, let me very briefly remind you of the classical least action principle as I explained it in Volume I. Suppose that a classical particle starts at position x₁ at time t₁ and arrives at position x₂ at time t₂ (Fig. 9.5). The question is: What is the trajectory that it took between t₁ and t₂?

According to the least action principle, the actual trajectory is the one of minimum action. Action is of course a technical term, and it stands for the integral of the Lagrangian between the endpoints of the trajectory. For simple systems,7 the Lagrangian is the kinetic energy minus the potential energy. Thus, for a particle that moves in one dimension, the action is

A = ∫ L(x, ẋ) dt (9.19)

or

A = ∫ [½ mẋ² − V(x)] dt.

The idea is to try out all possible trajectories connecting the two end points, and calculate A for each one of them. The winner is the one that has the least action.8,9

Now, let’s turn to quantum mechanics. The idea of a well-defined trajectory between two points makes no sense in quantum mechanics because of the uncertainty principle. However, a question that we can ask is: Given that a particle starts out at (x₁, t₁), what is the probability that it will show up at (x₂, t₂) if an observation of its position is made?

As always in quantum mechanics, the probability is the square of the absolute value of a complex amplitude. The global version of quantum mechanics asks:

Given that a particle starts out at (x₁, t₁), what is the amplitude that it will show up at (x₂, t₂)?

Let’s call that amplitude C(x₁, t₁; x₂, t₂) or, more simply, just C₁,₂. The initial state of the particle is |Ψ(t₁)⟩ = |x₁⟩. Over the time interval between t₁ and t₂, the state evolves to

|Ψ(t₂)⟩ = e^{−iH(t₂−t₁)} |x₁⟩. (9.20)

The amplitude to detect the particle at |x₂⟩ is just the inner product of |Ψ(t₂)⟩ with |x₂⟩. Its value is

C₁,₂ = ⟨x₂| e^{−iH(t₂−t₁)} |x₁⟩. (9.21)

In other words, the amplitude to go from x₁ to x₂ over the time interval t₂−t₁ is constructed by sandwiching e^{−iH(t₂−t₁)} between the initial and final positions. To simplify th formula, let's define t₂ - t₁ to be t. Then the amplitude is C₁,₂ = ⟨x₂|e^{-iHt}|x₁⟩. (9.22)

Now, let's break the time interval t into two smaller intervals of size t/2 (see Fig. 9.6). The operator e^{-iHt} can be written as the product of two operators: e^{-iHt} = e^{-iHt/2} e^{-iHt/2}. (9.23)

By inserting the identity operator in the form I = ∫dx|x⟩⟨x|, (9.24)

we can rewrite the amplitude as C₁,₂ = ∫dx⟨x₂|e^{-iHt/2}|x⟩⟨x|e^{-iHt/2}|x₁⟩. (9.25)

This form of the equation looks more complicated, but has a very interesting interpretation. Let me put it in words. The amplitude to get from x₁ to x₂ over time interval t is an integral over an intermediate position x. The integrand is the amplitude to go from x₁ to x over the time interval t/2 multiplied by the amplitude to go from x to x₂ over another time interval t/2.

Fig. 9.6 shows the same idea in visual terms. Classically, to go from x₁ to x₂, the particle must pass through an intermediate point x. But in quantum mechanics the amplitude to go from x₁ to x₂ is an integral over all possible intermediate points.

We can carry this idea further and divide the time interval into a great many tiny intervals, as illustrated in Fig. 9.7. I won't write out the complicated formulas, but the idea should be clear. For each tiny time interval, say of size ε, we include a factor e^{-iεH}.

Then, between each pair of factors, we insert the identity so that the amplitude C₁,₂ becomes a multiple integral over all the intermediate locations. The integrand is built from products of expressions with the form ⟨x_{i+1}|e^{-iεH}|x_i⟩.

If we define U(ε) as U(ε) = e^{-iεH}, then we can write the entire product as ⟨x₂|U^N|x₁⟩ or ⟨x₂|UUUU...|x₁⟩.

In this equation, U appears N times as a factor, where N is the number of epsilon steps. We can then insert identity operators between the U's.

Such an expression can be called the amplitude for the given path. But the particle does not travel along a particular path. Instead, in the limit of a large number of infinitesimal time intervals, the amplitude is an integral over all possible paths between the end points. The elegant fact that Feynman discovered is that the amplitude for each path bears a simple relation to a familiar expression from classical mechanics—the action for that path. The exact expression for each path is e^{iA/ℏ}, where A is the action for the individual path.

Feynman's formulation can be summarized by a single equation: C₁,₂ = ∫_{paths} e^{iA/ℏ}. (9.26)

The path integral formulation is not merely an elegant mathematical trick; it has real power. In fact, it can be used to derive both Schrödinger equations, and all the commutation relations of quantum mechanics. But it really comes into its own in the context of quantum field theory, where it is the principal tool for formulating the laws of elementary particle physics.

Lecture 10 The Harmonic Oscillator Art: I think I see it, Lenny. The whole picture is slowly coming into focus. Minus One, General Uncertainty, entangled pairs, the Hamiltonian—even the degenerates. What's next?

Lenny: Oscillations, Art. Vibrations. You're a fiddler—play us a last tune tonight. Something with good vibes.

Of all the ingredients that go into building a quantum description of the world, two stand out as especially fundamental. The spin, or qubit, of course is one of them. In classical logic, everything can be built out of yes-no questions. Similarly, in quantum mechanics, every logical question boils down to a question about qubits. We spent a lot of time in earlier lectures learning about qubits. In this lecture, we'll learn about the second basic ingredient of quantum mechanics—the harmonic oscillator.

The harmonic oscillator isn't a particular object like a hydrogen atom or a quark. It's really a mathematical framework for understanding a huge number of phenomena. This concept of the harmonic oscillator also exists in classical physics, but it really comes to the fore in quantum theory.

One example of a harmonic oscillator is a particle moving under a linear restoring force; for example, the iconic weight on the end of a spring. An idealized spring satisfies Hooke's law: the force on the displaced mass is proportional to the distance it has been displaced. We call the force a restoring force because it pulls the mass back toward the equilibrium position.

Another example is a marble rolling back and forth at the bottom of a bowl, with no energy being lost to friction. What characterizes these systems is a potential energy function that looks like a parabola: V(x) = kx². (10.1)

The constant k is called the spring constant. If we recall that the force on an object is minus the gradient of V, we find that the force on the object is F = −kx. (10.2)

negative sign tells us that the force acts opposite to the displacement and pulls the mass back toward the origin.

Why are harmonic oscillators so prevalent in physics? Because almost any smooth function looks like a parabola close to a minimum of the function. Indeed, many kinds of systems are characterized by an energy function that can be approximated by a quadratic function of some variable representing a displacement from equilibrium. When disturbed, these systems will all oscillate about the equilibrium point.

Here are some other examples: • An atom situated in a crystal lattice. If the atom is displaced slightly from its equilibrium position, it gets pushed back with an approximately linear restoring force. This motion is three-dimensional and really consists of three independent oscillations.

• The electric current in a circuit of low resistance often oscillates with a characteristic frequency. The mathematics of circuits is identical to the mathematics of masses attached to springs.

• Waves. If the surface of a pond is disturbed, it sends out waves. Someone watching at a particular location will see the surface oscillate as the wave passes by. This motion can be described as simple harmonic motion. The same goes for sound waves.

• Electromagnetic waves. Just like any other wave, a light wave or a radio wave oscillates when it passes you. The same mathematics that describes the oscillating particle also applies to electromagnetic waves.

The list goes on and on but the math is always the same. Just to have an example in mind, let’s picture the oscillator as a weight hanging from a spring. Needless to say, we hardly need quantum mechanics to describe an ordinary weight and spring, so let’s imagine a very tiny version of this same system and then quantize it.

## 10.1 The Classical Description

Let’s use y to denote the height of the hanging weight. We’ll choose the origin so that the weight is at y = 0 when it’s in equilibrium—that is when the weight is hanging at rest. To study this system classically, we can use the Lagrangian method that we learned about in Volume I. The kinetic and potential energies are 1/2 mẏ² and 1/2 ky² respectively.

As you recall, the Lagrangian is the kinetic energy minus the potential energy: L = 1/2 mẏ² - 1/2 ky².

First, we’ll put the Lagrangian into a certain standard form by changing from y to another variable that we will call x. This coordinate is not something new. It still represents the displacement of the mass. By switching from y to x, we’re just making a convenient change of units. Let’s define the new variable as x = √m y.

In terms of x, the Lagrangian becomes L = 1/2 ẋ² - 1/2 ω² x². (10.3)

The constant ω is defined as ω = √(k/m) and happens to be the frequency of the oscillator.

By making this change of variables, we can describe every oscillator in exactly the same form. In this form, oscillators are distinguished from each other only by their frequency ω.

Now, let’s use Lagrange’s equations to work out the equations of motion. For this one-dimensional system, there is only one Lagrange equation, namely ∂L/∂x = d/dt (∂L/∂ẋ). (10.4)

Carrying out these operations on Eq. 10.3, we find that ∂L/∂ẋ = ẋ. (10.5)

This is called the canonical momentum conjugate to x. Differentiating with respect to time gives d/dt (∂L/∂ẋ) = ẍ, (10.6)

and now we have the right-hand side of Eq. 10.4. Turning to the left-hand side, we find that ∂L/∂x = -ω² x. (10.7)

Setting the left and right sides (Eqs. 10.7 and 10.6) of the Lagrange equation equal to each other, we get -ω² x = ẍ. (10.8)

This equation is, of course, equivalent to F = ma. Why is there a minus sign? Because the force is a restoring force—its direction is opposite to the direction of the displacement. By now you have seen this type of equation enough to know that the solution contains sines and cosines. The general solution is x = A cos(ωt) + B sin(ωt), (10.9)

which shows us that ω is indeed the frequency of the oscillator. When we differentiate twice, we pull out a factor of ω².

Exercise 10.1: Find the second time derivative of x in Eq. 10.9, and thereby show that it solves Eq. 10.8.

## 10.2 The Quantum Mechanical Description

Now, let’s return to our microscopic version of the weight-and-spring system—let’s say no bigger than a single molecule. At first, this seems ridiculous. How could we ever build a spring that small? But in fact nature provides all sorts of microscopic springs. Many molecules consist of two atoms—for example, a heavy atom and a light one. There are forces holding the molecule in equilibrium with the atoms separated by a certain distance. When the light atom is displaced, it will be attracted back to the equilibrium location. The molecule is a miniature version of the weight-and-spring system, but is so small that we have to use quantum mechanics to understand it.

Having worked out the classical Lagrangian, let’s try to build a quantum mechanical description of our system. The first thing we need is a space of states. As we’ve seen, the state of a particle moving on a line is represented by a wave function ψ(x). There are many possible system states, and each one is represented by a different wave function. A function ψ(x) is defined in such a way that ψ∗(x)ψ(x) is the probability density (the probability per unit interval) to find the particle at position x: ψ∗(x)ψ(x) = P(x).

In this equation, P(x) represents the probability density. We now have a sort of kinematics—a specification of what the system states are.

Can ψ(x) be any function at all? Aside from the requirement that it must be continuous and differentiable, the only extra condition is that the total probability of finding the particle at any position must be 1: ∫_{-∞}^{+∞} ψ∗(x)ψ(x)dx = 1. (10.10)

This would not seem to be much of a restriction. Whatever the right-hand side of this equation is, we could always multiply ψ by some constant to make the integral equal to 1—unless the integral is either zero or infinity. Since ψ∗(x)ψ(x) is positive, we don’t have to worry about zero, but infinity is a different matter altogether; there are lots of functions that would make the integral in Eq. 10.10 blow up. The conditions for a sensible wave function thus include the requirement that ψ falls to zero fast enough that the integral converges. Functions that meet this condition are called normalizable.

There are two questions we might ask about our harmonic oscillator: • How does the state-vector change as a function of time? To answer this question, we need to know the Hamiltonian.

• What are the oscillator’s possible energies? These are also determined by the Hamiltonian.

So to know anything useful we need the Hamiltonian. Fortunately, we can derive it from the Lagrangian, and I’ll remind you how in a moment. But first recall that the canonical momentum conjugate to x is defined as ∂L/∂ẋ.¹ Combining this with Eq. 10.5, we get p = ∂L/∂ẋ = ẋ.

Using the straightforward definition from classical mechanics, we find that the Hamiltonian for the harmonic oscillator is H = pẋ − L, where p is the canonical momentum conjugate to x, and L represents the Lagrangian.² We could work directly from this definition, but instead we’ll take a shortcut. Because the Lagrangian is the kinetic energy minus the potential energy, the Hamiltonian is the kinetic energy plus the potential energy—in other words, the total energy. The Hamiltonian for the oscillator can therefore be written H = (1/2)ẋ² + (1/2)ω²x².

So far, so good, but we’re not quite finished. We’ve expressed kinetic energy in terms of velocity; in quantum mechanics, however, we need to represent our observables as operators, and we don’t have a velocity operator. To take care of this, we’ll have to recast things in terms of position and canonical momentum, which does have a standard operator form. Rewriting the Hamiltonian in terms of canonical momentum is easy because p = ∂L/∂ẋ = ẋ, which allows us to write H = (1/2)p² + (1/2)ω²x². (10.11)

That’s the classical Hamiltonian. We can now turn it into a quantum mechanical equation by reinterpreting x and p as operators, defined by their action on ψ(x). As we’ve done before, we’ll use the boldface symbols, X and P, to distinguish our quantum operators from their classical counterparts, x and p. From previous lectures, we know exactly how these operators work. X just multiplies the wave function by the position variable: X|ψ(x)⟩ = xψ(x).

And P takes the same form it does for other one-dimensional problems: P|ψ(x)⟩ = −iℏ ∂/∂x ψ(x).

Now, we can figure out the action of the Hamiltonian on a wave function by letting P act twice on the wave function. This is the same procedure we followed in Lecture 9. In other words, H|ψ(x)⟩ = [ (1/2)(−iℏ ∂/∂x)(−iℏ ∂/∂x) + (1/2)ω²x² ] ψ(x), or H|ψ(x)⟩ = [ −(ℏ²/2) ∂²/∂x² + (1/2)ω²x² ] ψ(x). (10.12)

We’re using partial derivatives because in general ψ also depends on another variable, time. Time is not an operator and does not have the same status as x, but the state-vector does change with time, and we therefore treat time as a parameter. The partial derivative indicates that we’re describing the system “at a fixed time.”

## 10.3 The Schrödinger Equation

Eq. 10.12 shows how the Hamiltonian operates on ψ. Now, let’s put it to work. As we said in the previous section, one of its jobs is to tell you how the state-vector changes with time. So let’s write out the time-dependent Schrödinger equation: i ∂ψ/∂t = Hψ.

Substituting for H using 10.12, we get i ∂ψ/∂t = [ −(ℏ²/2) ∂²ψ/∂x² + (1/2)ω²x² ψ ] / ℏ. (10.13)

This equation says that if you know w ψ (both the real and imaginary parts) at some particular time, you can predict what it will be at a future time. Notice that the equation is complex—it contains ias a factor. This means that even ifψ starts out being real-valued at time t = 0, it will very shortly develop an imaginary part. Any solution ψ must therefore be a complex function of x and t.

You can solve this equation in a number of ways. For example, you can solve it numerically on a computer. Start with a known value of ψ(x) and update it slightly by calcu- lating the derivative. Once you have the derivative, calcu- late how ψ(x) changes in a small increment of time. Then, 322 LECTURE 10. THE HARMONIC OSCILLATOR add this incremental change to ψ(x) and keep doing it over and over. It turns out that ψ(x) will do some interesting things—it will move around somehow. In fact, under certain circumstances, it will form a wave packet that moves around very much like a harmonic oscillator.

## 10.4 Energy Levels

The other thing you can do with the Hamiltonian is calcu- late the energy levels of the oscillator, by finding the energy eigenvectors and eigenvalues. As we learned in Lecture 4, once you know these eigenvectors and eigenvalues, you can figure out the time dependence without solving any differ- ential equations. That’s because you already know the time dependence of each energy eigenvector. You may want to review the Schr¨odinger’s Ket recipe we gave in Section 4.13.

For now, let’s concentrate on finding the energy eigen- vectors themselves, using the time-independent Schro¨dinger equation: H|ψ (cid:3) = E|ψ (cid:3).

E E The subscript E indicates that ψ is the eigenvector for a particular eigenvalue E. This equation defines two things: the wave functions ψ (x) and the energy levels E. Let’s make things less abstract by expanding H using Eq. 10.12: h¯ 2 ∂2ψ (x) 1 − E + ω 2 x 2 ψ (x) = Eψ (x). (10.14)

2 ∂x2 2 E E To solve this equation, we must: 10.4. ENERGY LEVELS 323 • Find the allowable values of E that permit a mathe- matical solution.

• Find the eigenvectors and possible eigenvalues of the energy.

This is a little trickier than you might think. There turns out to be a solution to the equation for every value of E, including all the complex numbers, but most solutions are physically absurd. If we just start at some point and solve the Schr¨odinger equation by making little incremental steps, we will almost always find that ψ(x) grows or “blows up” as x becomes large. In other words, we may be able to find solutions to the equation, but only very rarely will we find a normalizable solution.

In fact, for most values of E, including all the complex numbers, the solutions of Eq. 10.14 grow exponentially as x approaches ∞, −∞, or both. This type of solution makes no physical sense; it tells us that there is an overwhelm- ing probability that the oscillator coordinate is infinitely far away. Clearly, we want to impose some condition that gets rid of such solutions. So let’s impose one: Physical solutions of the Schr¨odinger equation must be normalizable.

This is a very powerful constraint. In fact, for almost all values of E, there are no normalizable solutions. But for certain very special values of E such solutions do exist, and we will find them.

324 LECTURE 10. THE HARMONIC OSCILLATOR

## 10.5 The Ground State

What is the lowest possible energy level for a harmonic oscil- lator? In classical physics, the energy can never be negative because the Hamiltonian has an x2 term and a p2 term; to minimize energy, we just set p and x equal to zero. But in quantum mechanics, that’s asking too much. The uncer- tainty principle says that you can’t set both x and p equal to zero. The best you can do is find a compromise state in which x and p are not too spread out. Because you have to compromise, the lowest possible energy will not be zero.

Neither p2 nor x2 will be zero. Because the operators X2 and P2 can have only positive eigenvalues, the harmonic os- cillator has no negative energy levels, and in fact, it has no state with zero energy either.

If all the energy levels of a system must be positive, there must be a lowest allowable energy and a wave function to go with it. This lowest energy level is called the ground state and is denoted by ψ (x). Keep in mind that the subscript 0 does not mean that the energy is zero; it means that it is the lowest allowable energy.

There is a very useful mathematical theorem that helps identify the ground state. We won’t prove it here, but it is very simple to state: The ground-state wave function for any potential has no zeros and it’s the only energy eigenstate that has no nodes.

So all we have to do to find the ground state of our har- monic oscillator is to find a nodeless solution for some value 10.5. THE GROUND STATE 325 of E. It doesn’t matter how we find it—we can use mathe- matical tricks, make guesses, or just ask the professor. Let’s use the latter method. (I’ll play the role of the professor.)

Figure 10.1: Har Harmonic Oscillator Ground State Here is a function that works: ψ(x) = e^{-ωx^2 / 2ℏ}. (10.15)

This function is shown schematically in Fig. 10.1. As you can see, it’s concentrated near the origin, where we expect the lowest energy state to be concentrated. It goes to zero very quickly as it moves away from the origin, so the integral of the probability density is finite. And, importantly, it has no nodes. So it has a chance of being our ground state.

Let’s see if we can figure out what the Hamiltonian does to this function. The first term of the Hamiltonian (the left side of Eq. 10.14) tells us to apply the operator -ℏ^2 / 2 * ∂^2/∂x^2 to ψ(x). Let’s calculate that term, one derivative at a time.

The first step is ∂ψ(x)/∂x = - (ω/2ℏ) * (2x) * e^{-ωx^2 / 2ℏ}, which simplifies to ∂ψ(x)/∂x = - (ωx/ℏ) * e^{-ωx^2 / 2ℏ}.

When we take the second derivative, there will be two terms because of the product rule: ∂^2ψ(x)/∂x^2 = - (ω/ℏ) * e^{-ωx^2 / 2ℏ} + (ω^2 x^2 / ℏ^2) * e^{-ωx^2 / 2ℏ}.

Let’s plug this result back into Eq. 10.14, and at the same time replace ψ on the right side with our guess, e^{-ωx^2 / 2ℏ}: -ℏ^2/2 * [ - (ω/ℏ) e^{-ωx^2 / 2ℏ} + (ω^2 x^2 / ℏ^2) e^{-ωx^2 / 2ℏ} ] + 1/2 m ω^2 x^2 e^{-ωx^2 / 2ℏ} = E e^{-ωx^2 / 2ℏ}.

After canceling the terms proportional to x^2 e^{-ωx^2 / 2ℏ}, we discover the remarkable fact that solving the Schrödinger equation just reduces to solving (ℏω/2) e^{-ωx^2 / 2ℏ} = E e^{-ωx^2 / 2ℏ}.

As you can see, the only way we can solve this equation is to set the energy E equal to ℏω/2. In other words, we’ve found not only the wave function but also the value of the ground-state energy. Calling the ground-state energy E_0, we can write E_0 = ℏω/2. (10.16)

The ground-state wave function, meanwhile, is just the Gaussian function the professor gave us: ψ_0(x) = e^{-ωx^2 / 2ℏ}.

He’s a clever fellow, that professor.

## 10.6 Creation and Annihilation Operators

Over the course of these lectures, we have seen two ways of thinking about quantum mechanics. They go all the way back to Heisenberg and Schrödinger. Heisenberg liked algebra, matrices, and, had he known what to call them, linear operators. Schrödinger, by contrast, thought in terms of wave functions and wave equations, the Schrödinger equation being one famous example. Of course, the two ways of thinking are not contradictory; functions form a vector space and derivatives are operators.

So far, in our study of the harmonic oscillator we have focused on functions and differential equations. But the more powerful tool in many cases—particularly for the harmonic oscillator—is the operator method. It reduces the entire study of wave functions and wave equations to a very small number of algebraic tricks, which almost always involve the commutation relations. In fact, whenever you see a pair of operators, my advice is to figure out their commutator. If the commutator is a new operator that you haven’t seen before, find its commutator with the original pair. That’s when the fun happens.

Obviously, this advice can lead to an unending chain of boring computations. But once in a while you may get lucky and find a set of operators that close under commutation. Whenever that happens, you’re in business; as we will see, operator methods have tremendous power.

Now, let’s apply this approach to our harmonic oscillator. We begin with the Hamiltonian expressed in terms of the operators P and X: H = (P^2 + ω^2 X^2) / 2. (10.17)

To figure out the rest of the energy levels, we’ll use some tricks. The idea is to cleverly use the properties of X and P (in particular, the commutation relation [X,P] = iℏ) to construct two new operators, called creation and annihilation operators. When a creation operator acts on an energy eigenvector (or eigenfunction), it produces a new eigenvector that has the next higher energy level. An annihilation operator does just the opposite: it produces an eigenvector whose energy is one level lower than the energy of the eigenvector it started with. So, roughly speaking, the thing that they create and annihilate is energy. They’re also called raising and lowering operators. But remember: operators act on state vectors, not on systems. To see how these operators work, let’s rewrite the Hamiltonian in the form H = (P^2 + ω^2 X^2) / 2. (10.18)

This is a classical as well as a quantum mechanical Hamiltonian, and it would be just as correct to use the lowercase symbols p and x. However, we’re using the boldface P and X because we plan to focus on the quantum mechanical Hamiltonian.

Let’s start by doing a manipulation that is correct for classical physics but will require some modification for quantum mechanics. In the parentheses above, we have a sum of squares. Using the formula a^2 + b^2 = (a+ib)(a−ib), it seems that we can rewrite the Hamiltonian as H “ = ” (P+iωX)(P−iωX), (10.19)

and that’s almost correct. Why almost? Because quantum mechanically, P and X do not commute, and we need to be careful about the order.

But the order of operations. Let’s expand our factored expression and see how it might differ from the original Hamiltonian in Eq. 10.18. Keeping careful track of the order of factors, we can expand the expression as follows:

(P + iωX)(P − iωX) = (P² + iωXP − iωPX − i²ω²X²)

= (P² + iω(XP − PX) − i²ω²X²)

= (P² + iω(XP − PX) + ω²X²)

= (P² + ω²X²) + iω(XP − PX).

Look at the right-hand set of parentheses in the final line. We have seen that expression before—it’s the commutator of X and P. In fact, we already know its value: (XP − PX) = [X, P] = iℏ.

Thus, the expression for our factored Hamiltonian becomes (P² + ω²X²) + iωiℏ or (P² + ω²X²) − ωℏ.

In other words, the factored expression we started out with in Eq. 10.19 is actually smaller than the Hamiltonian by ωℏ. To recover the actual Hamiltonian, we need to add the ωℏ back in: H = (P + iωX)(P − iωX) + ωℏ/2.

Rewriting the Hamiltonian this way and that way may seem like an exercise in futility, but trust me, it’s not. First of all, the last term is just an additive constant that adds the numerical value ωℏ to every energy eigenvalue. We can ignore it for now. Later, after we’ve solved the rest of the problem, we can add it back in. The guts of the problem are found in the expression (P + iωX)(P − iωX). It turns out that these two factors, (P + iωX) and (P − iωX), have some very remarkable properties. In fact, they are the raising and lowering operators (or creation and annihilation operators) that I told you about earlier. For now, these are just names, but as we go along we’ll see that the names were well chosen.

The obvious definitions would be a₋ = (P − iωX)

for the lowering operator, and a₊ = (P + iωX)

for the raising operator. But history sometimes preempts the obvious. Historically, the raising and lowering operators have been defined with an extra factor in front of them. Here are the official definitions: a₋ = (P − iωX) / √(2ωℏ), (10.20)

a₊ = −i(P + iωX) / √(2ωℏ). (10.21)

If we use these definitions, the Hamiltonian starts to look very simple: H = ωℏ(a₊a₋ + 1/2). (10.22)

There are only two properties of a₊ and a₋ that we need to know. The first is that they are Hermitian conjugates of each other. That follows from their definitions. The other property is what really gives them juice. The commutator of a₊ and a₋ is [a₋, a₊] = 1.

This is easy to prove. First, we use the definitions to write [a₋, a₊] = [(P − iωX), (P + iωX)] / (2ωℏ).

The next step is to use the commutation relations [X, X] = 0, [P, P] = 0, and [X, P] = iℏ. Apply these to the above equation, and you will quickly find that [a₋, a₊] = 1.

We can make the Hamiltonian in Eq. 10.22 even simpler by defining a new operator, N = a₊a₋, called the number operator. Once again, this is just a name, but as we’ll see, it’s a very good name. Stated in terms of the number operator, the Hamiltonian becomes H = ωℏ(N + 1/2). (10.23)

So far, all we’ve done is define some symbols, a₊, a₋, and N, that make the Hamiltonian look deceptively simple; it’s not clear that we are actually any closer to figuring out the energy eigenvalues. To proceed further, let’s recall my earlier advice: whenever you see two operators, commute them. In this case, we already know one commutator: [a₋, a₊] = 1. (10.24)

Next, let’s find the commutator of the raising and lowering operators with the number operator N. We’ll do this by brute force. Here are the steps: [a₋, N] = a₋N − Na₋ = a₋a₊a₋ − a₊a₋a₋.

Now, we’ll combine the terms in the form [a₋, N] = (a₋a₊ − a₊a₋)a₋.

This looks complicated until we notice that the expression in the parentheses is just [a₋, a₊], which just happens to be 1. Using this fact to simplify, we get [a₋, N] = a₋.

We can do the same thing with a₊ and N. The result is almost the same except for the sign. Here is the whole list of commutators in one neat package: [a₋, a₊] = 1 [a₋, N] = a₋ [a₊, N] = −a₊. (10.25)

This is what you might call a commutator algebra: a set of operators that closes under commutation. Commutator algebras have wonderful properties that make them one of the theoretical physicist’s favorite tools. We are now going to see the power of this commutator algebra in the iconic example of the harmonic oscillator, using it to find the eigenvalues and eigenvectors of N. Once we know these, we can immediately read off the eigenvalues of H from Eq. 10.23. The trick is to use a kind of induction procedure: we begin by supposing we have an eigenvalue and eigenvector of N. Call the eigenvalue n and the eigenvector |n⟩. By definition, N|n⟩ = n|n⟩.

Now, let’s consider a new vector, obtained by acting on |n⟩ with a₊. Let’s prove that the result is a different eigenvector of N, with a different eigenvalue. Again, we accomplish this by straightforward application of the commutation relations. We’ll start by writing the expression N(a⁺|n⟩) in a slightly more complicated form, N(a⁺|n⟩) = [a⁺N−(a⁺N−Na⁺)]|n⟩.

The expression in brackets on the right-hand side is the same as Na⁺, with the term a⁺N added and then subtracted. But notice that the expression in parentheses is the last of the commutators from Eqs. 10.25. If we plug that in, we get N(a⁺|n⟩) = a⁺(N+1)|n⟩.

The last step is to use the fact that |n⟩ is an eigenvector of N with eigenvalue n. That means we can replace (N + 1) with (n+1): N(a⁺|n⟩) = (n+1)(a⁺|n⟩). (10.26)

As always, when we run on autopilot, we have to keep our eyes open for interesting results. Eq. 10.26 is interesting. It says that the vector a⁺|n⟩ is a new eigenvector of N with eigenvalue (n+1). In other words, given the eigenvector |n⟩, we have discovered another eigenvector whose eigenvalue is increased by 1. All of this can be summarized by the equation a⁺|n⟩ = |n+1⟩. (10.27)

Obviously, we can do this again and again to find the eigenvectors |n+2⟩, |n+3⟩, and so on. Remarkably, we find that if there is an eigenvalue n, there must be an infinite sequence of eigenvalues above it, spaced by integers. The name raising operator seems well chosen.

What about the lowering operator? Not surprisingly, we find that a⁻|n⟩ produces an eigenvector whose eigenvalue is one unit lower: a⁻|n⟩ = |n−1⟩. (10.28)

This suggests that there must be an unending sequence of eigenvalues below n, but that can’t be correct. We already know that the ground state has positive energy, and because H = ℏω(N+1/2) the downward sequence must end. But the only possible way it can end is for there to be an eigenvector |0⟩ such that when a⁻ acts on it, the result is zero. (We should not confuse |0⟩ with the zero vector.³) Symbolically, this can be expressed as a⁻|0⟩ = 0. (10.29)

Being the lowest energy state, |0⟩ is the ground state, and its energy is E = ℏω/2. It is an eigenvector of N with an eigenvalue 0. We often say that the ground state is annihilated by a⁻.

So you see, the abstract construction of a⁺, a⁻, and N paid off. It allowed us to find the entire spectrum of harmonic oscillator energy levels without solving a single difficult equation. This spectrum consists of the energy values, E = ℏω(n+1/2) = ℏω(1/2, 3/2, 5/2,...). (10.30)

This quantization of harmonic oscillator energy levels was one of the first results of quantum mechanics, and arguably the most important. The hydrogen atom is a wonderful example of quantum mechanics, but it is, after all, just the hydrogen atom. The harmonic oscillator, on the other hand, shows up everywhere, from crystal vibrations to electric circuits to electromagnetic waves. The list goes on. Even macroscopic oscillators, like a child on a swing, have quantized energy levels, but the presence of Planck’s constant in Eq. 10.30 means that the spacing between levels is so tiny that they are completely undetectable.

The unending spectrum of positive energy levels for a harmonic oscillator is sometimes called a tower, and sometimes called a ladder. It is illustrated schematically in Fig. 10.2.

## 10.7 Back to Wave Functions

This exercise has amply demonstrated the remarkable power of operator algebras, and the operator method is indeed remarkable. But it’s also very abstract. Is it useful in helping us find wave functions, which are more concrete and easier to visualize? Absolutely.

Let’s begin with the ground state. We just saw in Eq. 10.29 that the ground state is the unique state that is annihilated by a⁻. Now, let’s rewrite Eq. 10.29 in terms of the position and momentum operators, and the ground-state wave function ψ(x): √(P−iωX)ψ(x) = 0, 2ωℏ or, dividing by the constant factor, (P−iωX)ψ(x) = 0.

If we now replace P with −iℏ d/dx, we get a first-order differential equation that is much simpler than the second-order Schrödinger equation: dψ/dx = (ωx/ℏ) ψ(x).

This is a simple differential equation that you can easily solve. Or, you can just check that the ground-state wave function e^(−ωx²/2ℏ)

in Eq. 10.15 solves it. Calculating the wave functions for the excited (nonground) states is even easier—we don’t even have to solve any equations. Let’s go up the ladder to n = 1. We can do that by applying a⁺ to the ground state. Let’s call the wave function of this new state ψ₁(x).

√1 To avoid dragging the constant −i/ 2ωℏ around in our calculations, we’ll just drop it in our definition of a+. This only affects the numerical coefficient. The resulting equation is ψ₁(x) = (P + iωX)ψ₀(x)

or ψ₁(x) = (−iℏ + iωx) e^{−ωℏx²/2}.

Factoring out the i, we get ψ₁(x) = i (−ℏ + ωx) e^{−ωℏx²/2}.

The “hardest” part of working this out is performing an easy derivative of e^{−ωℏx²/2}. Here is the result: ψ₁(x) = 2iωx e^{−ωℏx²/2}, or ψ₁(x) = 2iωx ψ₀(x).

The only important difference between ψ₀ and ψ₁ is the presence of the factor x in ψ₁. This has an effect: it causes the wave function of the first excited state to have a zero, or node, at x = 0. This is a pattern that continues as we go up the ladder: each successive excited state has an additional node. We can see this pattern emerge by calculating the second excited state at n = 2. All we have to do is apply a+ again: ψ₂(x) = i (−ℏ + ωx) x e^{−ωℏx²/2}.

We can see right away that the ωx term will result in an ωx² term. The −∂/∂x, meanwhile, will result in two terms because of the product rule for derivatives. One of these terms will come from the exponential (producing another ωx). The other will come from taking the derivative of x. It’s clear that what we’ll end up with is a quadratic polynomial. If we work out these derivatives, the resulting wave function is ψ₂(x) = (−ℏ + 2ωx²) e^{−ωℏx²/2}.

And so it goes, all the way up the ladder. We can see another pattern here: each eigenfunction is a polynomial in x multiplied by e^{−ωℏx²/2}. Because the exponential goes to zero faster than any of these polynomials grows, each eigenfunction approaches zero asymptotically as x goes to plus or minus infinity. Also, because the degree of each polynomial is one greater than the degree of the previous one, each eigenfunction has one more zero than the previous one.⁴ This also explains why successive eigenfunctions alternate between being symmetric and antisymmetric. Specifically, eigenfunctions with polynomials of even degree are symmetric, while those with polynomials of odd degree are antisymmetric. The polynomials in this sequence are very well-known. They’re called the Hermite polynomials. The ground-state eigenfunction e^{−ωx²/2}, which appears in all of these higher-energy eigenfunctions, is symmetric in x.

Figure 10.3 displays the eigenfunctions for several different energy levels. Each successive eigenfunction oscillates more rapidly than the one before it. This corresponds to an increase in momentum. The more rapidly the wave function oscillates, the greater the momentum of the system. At higher energy levels, the wave function also becomes more spread out. In physical terms, this means the mass is moving farther from the equilibrium point, and moving faster.

These eigenfunctions contain another important lesson. Although they approach zero asymptotically (quite rapidly) they never quite reach zero. That means there is a small but finite chance of finding the particle “outside the bowl” that defines its potential energy function. This phenomenon, known as quantum tunneling, is completely unknown in classical physics.

⁴ It turns out that these zeros occur for real values of x, but that’s not obvious from what we’ve seen. In a physical sense, the zeros seem a little weird, because they are points where the moving mass will never be found, even though it’s merrily whizzing back and forth.

## 10.8 The Importance of Quantization

We’ve climbed a high mountain in these lectures, but it’s not the last mountain. Looking out from the present vantage point, we can get a glimpse of the enormous landscape of quantum field theory. That’s material for another book. Or maybe three. But still, we can see a bit of the terrain from where we are.

Consider the example of electromagnetic radiation in a cavity, as shown in Fig. 10.4. In this context, a cavity is a region of space bracketed by a pair of perfectly reflecting mirrors that keep the radiation bouncing endlessly back and forth. Think of the cavity as a long metallic tube that the radiation can travel along in both directions.

There are many wavelengths that can fit into the cavity. Let’s consider waves of length λ. Like all waves, these waves oscillate, very much like a mass on the end of a spring. But it’s important not to get confused here: the oscillators are not masses attached to springs. What’s really oscillating are the electric and magnetic fields. For each wavelength, there is a mathematical harmonic oscillator describing the amplitude or strength of the field. That’s a lot of harmonic oscillators all running simultaneously. Fortunately, however, they all oscillate independently, so we can focus our attention on waves of one particular wavelength and ignore all the others.

Figure 10.3: Harmonic oscillator eigenfunctions.

谐振子本征函数。左侧显示振幅，右侧显示概率。能量较高的波函数振荡更快，分布更广。

谐振子只有一个重要的数字——即它的频率。你可能已经知道如何计算波长为λ的波的频率： ω = 2πc / λ。

在经典物理学中，频率当然就是频率。但在量子力学中，频率决定了振子的能量量子。换句话说，波长为λ的波所包含的能量必须是 (n+1/2)ℏω。

项 (1/2)ℏω 对我们的目的并不重要。它被称为零点能，我们可以忽略它。如果忽略，波长为λ的波的能量变为 E = n * 2πℏc / λ， 其中n可以是任何从零开始的整数。换句话说，电磁波的能量是以不可分割的单位量子化的，单位为 2πℏc / λ。

对于经典物理学家来说，这非常奇怪。无论你做什么，能量总是以不可分割的单位出现。

你可能已经知道这些单位被称为光子。事实上，光子只是量子谐振子中量子化能量单位的另一个名称。但我们也可以用另一种方式描述相同的事实。由于不可分割，光子可以被视为基本粒子。一个被激发到第n个量子态的波可以被视为n个光子的集合。

单个光子的能量是多少？很简单。它就是增加一个单位所需的能量，即 E(λ) = 2πℏc / λ。

在这里，我们可以看到一个主导物理学超过一个世纪的现象：光子的波长越短，其能量就越高。考虑到短波长光子在能量上代价高昂，物理学家为什么会对制造它们感兴趣？答案是为了看得更清楚。正如第1讲中所讨论的，要分辨一个给定大小的物体，你必须使用该大小或更小的波长。要看到一个人形，几英寸的波长就足够了。要看到一粒微小的灰尘，你可能需要波长小得多的可见光。要分辨质子的各个部分，波长必须小于10^-15米，而相应的光子必须具有非常高的能量。归根结底，这一切都回到了谐振子。

至此，朋友们，我们结束了《理论最小值》系列的这一卷。我期待在《狭义相对论》中与你们再见。

## 附录

泡利矩阵 σ_z = [[1, 0], [0, -1]]

σ_x = [[0, 1], [1, 0]]

σ_y = [[0, -i], [i, 0]]

自旋算符的作用 |u⟩ = [[1], [0]]  ⇐⇒  σ_z|u⟩ = |u⟩ σ_x|u⟩ = |d⟩ σ_y|u⟩ = i|d⟩

|d⟩ = [[0], [1]]  ⇐⇒  σ_z|d⟩ = -|d⟩ σ_x|d⟩ = |u⟩ σ_y|d⟩ = -i|u⟩

|r⟩ = [[1/√2], [1/√2]]  ⇐⇒  σ_z|r⟩ = |l⟩ σ_x|r⟩ = |r⟩ σ_y|r⟩ = -i|l⟩

|l⟩ = [[1/√2], [-1/√2]]  ⇐⇒  σ_z|l⟩ = |r⟩ σ_x|l⟩ = -|l⟩ σ_y|l⟩ = i|r⟩

|i⟩ = [[1/√2], [i/√2]]  ⇐⇒  σ_z|i⟩ = |o⟩ σ_x|i⟩ = i|o⟩ σ_y|i⟩ = |i⟩

|o⟩ = [[1/√2], [-i/√2]]  ⇐⇒  σ_z|o⟩ = |i⟩ σ_x|o⟩ = -i|i⟩ σ_y|o⟩ = -|o⟩

基变换 |r⟩ = (1/√2)|u⟩ + (1/√2)|d⟩ |l⟩ = (1/√2)|u⟩ - (1/√2)|d⟩ |i⟩ = (1/√2)|u⟩ + (i/√2)|d⟩ |o⟩ = (1/√2)|u⟩ - (i/√2)|d⟩

n̂方向的自旋分量矢量表示 σ_n = σ · n̂

分量形式 σ_n = σ_x n_x + σ_y n_y + σ_z n_z

更具体地 σ_n = n_x [[0, 1], [1, 0]] + n_y [[0, -i], [i, 0]] + n_z [[1, 0], [0, -1]]

合并为单个矩阵 σ_n = [[n_z, n_x - i n_y], [n_x + i n_y, -n_z]]

自旋算符乘法表关于符号的说明：表3中的符号i有两种不同的用法。在ket内部，例如|io⟩，它是状态标签的一部分——io表示“in-out”。但当i出现在ket符号外部时，如i|oo⟩，它表示虚数单位。

表1：上下基 2-自旋本征矢 |uu⟩ |ud⟩ |du⟩ |dd⟩ σ_z |uu⟩ |ud⟩ -|du⟩ -|dd⟩ σ_x |du⟩ |dd⟩ |uu⟩ |ud⟩ σ_y i|du⟩ i|dd⟩ -i|uu⟩ -i|ud⟩ τ_z |uu⟩ -|ud⟩ |du⟩ -|dd⟩ τ_x |ud⟩ |uu⟩ |dd⟩ |du⟩ τ_y i|ud⟩ -i|uu⟩ i|dd⟩ -i|du⟩

表2：左右基 2-自旋本征矢 |rr⟩ |rl⟩ |lr⟩ |ll⟩ σ_z |lr⟩ |ll⟩ |rr⟩ |rl⟩ σ_x |rr⟩ |rl⟩ -|lr⟩ -|ll⟩ σ_y -i|lr⟩ -i|ll⟩ i|rr⟩ i|rl⟩ τ_z |rl⟩ |rr⟩ |ll⟩ |lr⟩ τ |rr⟩ −|rl⟩ |lr⟩ −|ll⟩ τ −i|rl⟩ i|rr⟩ −i|ll⟩ i|lr⟩ Table 3: In-Out Basis 2-Spin Eigenvectors |ii⟩ |io⟩ |oi⟩ |oo⟩ σ |oi⟩ |oo⟩ |ii⟩ |io⟩ σ i|oi⟩ i|oo⟩ −|ii⟩ −|io⟩ σ |ii⟩ |io⟩ −|oi⟩ −|oo⟩ τ |io⟩ |ii⟩ |oo⟩ |oi⟩ τ i|io⟩ −i|ii⟩ i|oo⟩ −i|oi⟩ τ |ii⟩ −|io⟩ |oi⟩ −|oo⟩

Index 2 × 2 matrices, combining, 188 bra-ket notation for, 106–107 3-vector operators, 75, 83–85, 119 defining, 105–106 3-vectors, 25, 27, 74–75, 83 See also Expectation values orthogonal unit vectors and, Average value, 105 32–33 Axioms, vector space, 24–27 4 × 4 matrices, from combined 2 × 2 matrices, 188 Basis of simultaneous eigenvectors, Addition 131–133 of complex numbers, 23 Basic vectors, 32–34, 38, 40, 41, vector, 26 48–49, 54, 55, 64, 67, 97, Amplitude, 39, 108, 342, 343 98, 106, 120–125, 130–136, for paths, 306–309 173, 185, 189, 191,195, 196, and rule, 14, 15, 20 198, 202, 204, 208, 210, 211, Annihilation operators, 327–337 219, 224, 236, 237, 251, 258, Anti-Hermitian operator, 250 260–263, 275 Antisymmetric eigenfunctions, 341 components, 56 Apparatus, measurement and, 5–13, entangled states, 165–167 37–38, 71, 75, 81–82, 83–84, 91, labeling, 150.151, 152, 153, 154, 126–127, 180, 219–224, 227–230 160–163 Associative property, 26, 193, 239 product states, 163–165 Atoms, 259, 290, 311 Bell, John, 223, 227 in crystal lattice, 313 Bell’s theorem, 227–231 hydrogen, 336–337 Boolean logic, 13–18 quantum mechanics and, 2, 71, Bracket notation, 11 149, 316 Bra-ket notation, 105 size of, 104 for averages, 106–107 spins of, 180–181 Bras (bra vectors), 28–30, 240 wave packets and, 297, 301 inner product and, 30–32 Average,140–141, 157–158, 213, 271, linear operators and, 58–59 286, 288, 292, 295 outer products and, 194 Canonical momentum, 315, 318–320 Commuting variables, complete sets Canonical momentum conjugate to of, 129–136 x, 315, 318–320 wave functions, 134–136 Cartesian coordinates, 89, 116, Complex conjugate, 23 136 Complex conjugate numbers, 28, 30 Cartesian representation, of complex Complex conjugation, for operators, number, 22 59–61 Cauchy-Schwarz inequality, 142 Complex numbers, 21–30, 34, 38, triangle inequality and, 142–146 42, 44 Change addition of, 23 in classical physics, 94 eigenvalues and, 58 continuity and, 100 multiplication of, 23 unitarity and incremental, 100 phase-factors, 24 Classical entanglement, 155–160 representations of, 22 Classical equations, quantization Complex vector spaces, orthonormal and, 289–290 basis and, 33 Classical limit, 295–301 Component matrices, building Classical physics tensor product matrices from, change in, 94 188–192 change in expectation values over Component, 56 time and, 109–114 of 3-vector, 25, 74–75, 83, 116 commutators and, 266–268 addition of, 27 momentum in, 255 of angular momentum, 119 particle dynamics and, 279 of basis vector, 56 pure and mixed states and, of generic state, 38 199–200 inner products and, 31, 34 quantum mechanics vs., 2–3 multiplication of, 28 testing propositions of, 16–18 of phase factor, 24 Collapse of the wave function, of spin, 9, 13, 16–17, 20, 37, 69, 126–127 71, 75, 77, 83–84, 87, 90–91, Column vectors, 27–28, 49 116–117, 119, 130–131, 138– kets and, 29 139, 162, 167–168, 170, 174– spin states as, 47 175, 176, 178–179, 180–181, Commutation relations, 118, 119, 218, 222, 251, 257, 260, 349 138–139, 287, 309, 328, 332, of spin operator, 71–72, 75, 116 334 of state-vector, 40, 227, 237, 336n Commutative property, 26 of system, 154, 222 Commutator algebra, 334–337 of vector, 8, 9–10 Commutators, 111–116, 138, 142, wave functions and, 136 146, 147, 269, 280, 287, 293, Component form 294, of addition, 23, 27–28 classical physics and, 266–268 of bra-vectors, 59 operators and, 328, 330, 332, 333, equation in, 54, 59, 79 334, 335 of multiplication, 58–59 Poisson brackets and, 112–114, of tensor product operators, 155, 265–268 171–172, 184, 188, 204 Component matrices, 188–192 two-spin system and, 203–217, Composite observables, 175–181 231 Composite operator Density matrix test for composite vectors and, 171 entanglement, 214–218 energy and measurement of, Determinism 180–181 in classical physics, 94 Composite state, two spin, 161–181 in quantum mechanics, 9–11, 96 Composite systems Dirac, Paul, 105, 113, 194, 278 mixed and pure states and, Dirac delta functions, 241, 242–245, 200–201 253 observables in, 167–175 Dirac’s bracket notation, 11 product states, 163–165 Distributive property, 26 representing, 151–155 Dot product, 30, 31, 144, 180 tensor products and, 150–155 Down states, 219–221 See also Entanglement Dual number systems, 23 Composite vectors, composite operators and, 171 Eigen-equation, 256 Conservation of distinctions, Eigenfunctions, 253 97–99 alternation between being Conservation of energy, 114–1 Antisymmetric, 99 Conservation of overlaps, 340–341 Continuity, 100–101 for energy levels, 341, 343 Continuous functions, 236–250 functions as vectors, 238–245 integration by parts, 245–246 linear operators, 246–250 wave functions and, 236–238 Correlation energy, 121, 322–323 of near-singlet state, 234 of product state, 232 of singlet state, 233 Correlation test for entanglement, 213–214 Creation operators, 327–337 Crystal lattice, atom in, 313 Degeneracy, 64 Density matrices, 184, 196–199 calculating, 210–212 entanglement and, 199–202 of near-singlet state, 234 notation for, 201–202 of product state, 232 properties of, 207 for single spin, 202–203 of singlet state, 233 summary of, 231–234 tests for, 212–218 for two spins, 161–163, 202–210 Euler-Lagrange equations, 305n Eigenstate, collapse of the wave function and, 126–127 Eigenvalues, 56–59, 70, 71–72 of density matrix, 207, 215–217 of Hermitian operators, 62–63 of operators, 80 of position, 252–254 of spin operator, 76, 77–78 Eigenvectors, 56–59, 70 of annihilation operator, 328 of creation operator, 328 defined, 57 energy, 121, 322–323 of Hermitian operator, 64–67 of momentum, 255–260 of operators, 80 of position, 252–254 of projection operator, 194 simultaneous, 131–133 of spin operator, 76, 77–80 Einstein, Albert, 155, 175, 223, 227 Electric current, 313 Electromagnetic radiation in cavity, 342–345 Electromagnetic waves, 313 Electrons, 2, 149, 259, 301 spin of, 3–4, 116, 180, 290 wave packets and, 301 waves and, 235 Energy conservation of, 114–115 composite operator and, 180–181 creation and annihilation operators and, 328–337 frequency and, 123 harmonic oscillator and, 314–316, 317–319 of particle with negative momentum, 278 of photon, 345 See also Hamiltonian Energy eigenvalues, 121, 322–323 Energy eigenvectors, 121, 322–323 Energy levels eigenfunctions for, 341, 343 harmonic oscillators and, 322–323, 336–337, 338 Entangled states, 165–167 Entanglement, 149–181 Bell’s Theorem and, 227–231 classical, 155–160 combining quantum systems, 160–161 composite observables, 175–181 correlation test for, 213–214 density matrices and, 184, 199–202, 210–212 density matrix test for, 214–218 entangled states, 165–167 example: calculating a density matrix, 210–212 locality and, 223–226 of near-singlet state, 234 observables and, 167–175 process of measurement and, 218–223 of product state, 163–165, 232 of singlet state, 233 Expectation values, 87–88, 91, 105–108 change over time in, 109–114 conservation of, 115 correlation test for entanglement and, 213–214 for density matrix, 198 of entangled state, 172–175 of near-singlet state, 234 particle dynamics and, 278–279 of product state, 232 of projection operator, 195–196 of singlet state, 233 in spin over time, 116–119 Experiments apparatus and, 5–13 invasiveness of, 12–13 probabilities for outcomes of (see Probabilities for experimental outcomes)

two-state system, 4–11 Feynman, Richard, 302, 309 Forces, 290–294 Fourier transforms, 260–261, 265, 285 Frequency energy and, 123 of harmonic oscillator, 344–345 Functions Dirac delta, 241, 242–245, 253 Gaussian, 327 normalizable, 318 potential, 291, 297–298 probability, 105–106, 213, 295 as vectors, 238–245 vector space, 27–28 zero, 239 See also Continuous functions; Eigenfunctions; Wave functions Fundamental theorem of quantum mechanics, 64 Gaussian curve, 301 Gaussian function, 327 Gaussian wave packets, 301 General Schrödinger equation, 102, 274 General uncertainty principle, 146–148, 268, 269–270 Gluons, 259 Gram-Schmidt procedure, 67–69 Gravitons, 280 Ground states, 324–327 annihilation of, 336 wave functions for, 337–339 Hamiltonian, 99–102 canonical momentum and, 319–320 conservation of, 115 entanglement and, 181 for harmonic oscillator, 318–320, 321, 322–323, 324–326, 329–334, 336 motion of particles and, 274–278 nonrelativistic free particles and, 280–283 quantum, 101, 103 spin in magnetic field, 116–119 time evolution of system and, 274 Hamiltonian operator, Schrödinger ket and, 124 Hamilton’s equations, 274, 279 Harmonic oscillator, 311–346 annihilation operators, 327–337 classical description, 314–316 creation operators, 327–337 Heisenberg Uncertainty Principle, 139–140, 148, 269–271 Hermite, Charles, 62 Hermite polynomials, 341 Hermitian density matrices as, 207, 208 momentum as, 262 position as, 262 projection operators as, 194 Hermitian conjugation/conjugate, 59–61, 62, 63, 65, 97–98, 100, 332 Hermitian matrix, 62, 137–138, 195n, 208 Hermitian observable, 262 Hermitian operators, 52, 101, 112, 138, 255 action on state-vector, 107–108 in composite space of states, 168 eigenvector of, 139, 236, 262 expectation value of, 109 linear operators as, 70, 73–74, 246–250 orthonormal bases and, 64–67 orthonormal edge vectors of, 136 overview, 61–63 particles and, 252 trace of, 196 Hilbert, David, 239 Hilbert spaces, 25, 239 Hooke’s law, 312 Hydrogen atom, 336–337 Identity, resolving, 261–264 Identity operator, from projection operators, 194 jection energy levels, 322–323 operators, 195 ground state, 324–327 Inner products, 28–29, 30–32, 193 Integrals, replacing sums, 240, 241 Integration by parts, 245–246 Kets (ket vectors), 28–30 axioms of, 25–27 composite systems and, 153–154 inner product, 30–32 Schrödinger, 124–126 Kinematics, 317 Kronecker delta, 205 replaced by Dirac delta functions, 241, 242–245 Kronecker product, 188–192, 205n Kronecker symbol, 98, 161 Lagrange equation, 314–316 Lagrangian, 302–303, 314–316, 318, 319 Law of evolution, 5 Least action principle, 301–305 Linearity, 27, 53 Linear motion, 295–301 Linear operators, 52–69, 246–250 eigenvalues, 56–59 eigenvectors, 56–59 Gram-Schmidt procedure, 67–69 Hermitian conjugation, 59–61 Hermitian operators, 61–63 Hermitian operators, orthonormal bases and, 64–67 machines and matrices, 52–56 observables and, 69–70, 73 outer product as, 193–196 properties of, 53 time-development operator, 97 Liouville’s theorem, 274 Locality defined, 223–224 Einstein vs. Bell and, 227 entanglement and, 223–226 Lowering operators (annihilation operators), 327–337 density matrices and, 208–209 Machines, matrices and, 52–56 Magnetic field, spin in, 116–119 Mathematical concepts complete sets of commuting variables, 129–136 complex numbers, 21–24 continuous functions, 236–250 functions as vectors, 238–245 integration by parts, 245–246 linear operators, 52–69, 246–250 outer products, 193–196 tensor products, 149–155 tensor products in component form, 184–192 vector spaces, 24–34 Matrices 4x4, 188 machines and, 52–56 Pauli, 80, 118, 137 tensor product, building, 185–192 2x2, 188 [is this entry out of lexical sequence?]

Matrix elements, 55 Matrix multiplication, 56, 59 Matrix notation, transposing in, 60–61 Maximally entangled state, 217, 221 Maxwell’s equations, 290 Mean value, 105 Measurables, states that depend on more than one, 129–133 Measurement, 137–139 apparatus and, 5–11, 219–223 collapse of the wave function and, 126–127 multiple, 129–133 operators and, 80–82 process of, 218–223 states and, 2–3 Minimum-uncertainty wave packets, 301 Minus first law, 94, 274 quantum version of, 94–95, 97 Mixed states, 198, 199–200 composite system and, 200–201 Momentum canonical, 315, 318–320 connection between quantum and classical physics, 268 eigenfunctions and, 341 eigenvectors of, 255–260 forces and, 292–294 Heisenberg Uncertainty Principle and, 269 proposition for, 20–21 velocity and, 286–288, 293 wavelength and, 259–260 Momentum basis, 260–265 Momentum operator, 255–257 Momentum representation, of wave function, 260–265 Motion of particles. See Particle dynamics Multiplication 3-vector, 75, 83–85, 119 of column vector, 28 of complex numbers, 23 matrix, 56, 59 vector, 26 Near-singlet state correlation, 234 density matrix, 234 description of, 234 entanglement status of, 234 expectation values, 234 normalization, 234 state-vector, 234 wave function, 234 Negation, 14 Neutrino, 3 moving at speed of light, 277–278 Newton’s law, 291, 292 quantum version of, 293–294 Nonlocality, 231 Nonrelativistic free particles, 280–283 Normalizable functions, 318 Normalization of near-singlet state, 234 of product state, 232 of singlet state, 233 Normalized vector, 32, 40 not rule, 14 Number operator, 332–333 Observables complete set of commuting, 133 composite, 175–181 composite system, 167–175 defined, 52 linear operators and, 69–70, 73 multiple, 130–131 Observations, collapse of the wave function and, 126–127 Operator method harmonic oscillator and, 328–337 wave functions and, 337–342 Operators annihilation, 327–337 anti-Hermitian, 250 commutators and, 328, 334 composite, 171, 180–181 creation, 327–337 Hamiltonian, 124 Hermitian (see Hermitian operators)

identity, 195 linear (see Linear operators)

measurement and, 80–82 misconception regarding, 81–82 momentum, 255–257 number, 332–333 projection, 194–195 spin, 74–80 state-vectors and, 80–81 time-development, 95, 97–99 time-evolution, 99–102 unitary, 95, 97–99 zero, 133 Original Schrödinger equation, 274 nonrelativistic free particle and, 281–283 or rule, 14, 15, 19 Orthogonal basis vectors, 48 Orthogonal states, 39–40, 97 Orthogonal state-vectors, 70, 72 Orthogonal vectors, 32, 64–67, 70 Orthonormal bases, 32–34 Gram-Schmidt procedure, 67–69 Hermitian operators and, 64–67 Outer products, 193–196 Overlap, 72, 73 Parameters, counting, 45–47 Partial derivatives, time and, 320–321 Particle dynamics, 273–309 example, 273–279 forces, 290–294 linear motion and classical limit, 295–301 nonrelativistic free particles, 280–283 path integrals, 301–309 Position representation, of wave function, 260–262, 263–265 Potential functions, 291 spiky, 297–298 Precession, of spin in magnetic field, 119 Principle of Least Action, 301–305 Principle Principle of Stationary Action quantization, 288–290 Probabilities for experimental outcomes, 8, 19, 48–49, 70, 72–73, 87–90, 238, 306 replaced by probability densities, 241, 242 Schrödinger ket and, 124–126 Probability entanglement and, 206–207, 222 wave function and, 260–261, 264, 270 Probability amplitudes, 39, 108–109 Probability density, 199, 317, 325 replacing probabilities, 241, 242 Probability distribution, 110, 112, 213 in classical mechanics, 158–159 particle dynamics and, 278–279 uncertainty and, 140–141 Probability function, 105–106, 213, 295 Product states, 163–165 correlation, 232 counting parameters for, 165 density matrix, 232 density matrix test for entanglement and, 215–218 description of, 232 entanglement status, 232 expectation values, 232 normalization, 232 state-vector, 232 wave function, 232 Projection operators, 194 properties of, 194–195 Propositions classical, 13–16 classical, testing, 16–18 quantum, testing, 18–21 Pure states, 198, 199–200 composite system and, 200–201 density matrices and, 207–209, 217 Quarks, 3, 259, 311 Qubits, 3–4, 5, 311 measuring system of two, 130–131 Raising operators (creation operators), 327–337 Real numbers, quantum mechanics and, 61–63 Reversibility, 94 Row vectors, bras and, 29–30 Schrödinger, Erwin, 327 Schrödinger equations generalized (see Time-dependent Schrödinger equation)

original, 274, 281–283 path integrals and, 309 solving, 119–124 spin state evolution and, 227–230 time-dependent (see Time-dependent Schrödinger equation)

for time derivatives, 110–112 time-independent, 120–121, 124, 283–285, 286, 289 Schrödinger ket, 124–126 Schrödinger’s Ket, 102 Sets, Boolean logic and, 13–16 Simultaneous eigenvectors, 131–133 Singlet state, 166–167, 181 correlation, 233 density matrix, 233 description of, 233 entanglement status of, 233 expectation values, 233 normalization, 233 state-vector, 233 wave function, 233 Space of states, 4–5, 13, 16, 24, 25, 37, 40, 44, 71, 94, 124, 150–151, 160, 162, 165, 166, 167–168, 216, 219, 238, 274, 289, 317 Speed of light, particles moving at, 277–278 Spherical coordinates, 89–90 Spin 3-vector operators and, 83–85 along the x axis, 41–42 along the y axis, 42–45 density matrix for, 202–203 expectation values of, 87–88, 91 interaction with apparatus, 5–13 in magnetic field, 116–119 number of distinct states for, 45–47 quantum, 3–4, 36–37, 227, 229–340 uncertainty principle and, 20 See also Qubits; Two spins Spin components, simultaneous measurement of, 138–139 Spin operators, 74–75 constructing, 75–80 Spin-Polarization Principle, 90–91, 172 Spin states as column vectors, 47 density matrix for, 202–203 expectation values of, 87–88, 91 interaction with apparatus, 5–13 in magnetic field, 116–119 number of distinct states for, 45–47 quantum, 3–4, 36–37, 227, 229–340 uncertainty principle and, 20 See also Qubits; Two spins State-labels, for composite system, 152, 153, 154, 160–161 State of system, in classical vs. quantum physics, 21, 273–274 State space, Boolean logic and, 13–16 State-vectors, 70 action of Hermitian operator on, 107–108 as complete description of system, 175 evolution of with time, 99 of near-singlet state, 234 operators and, 80–81 phase-factor and, 108–109 physical properties of, 46 of product state, 163–165, 232 representing spin states using, 37–40 of singlet state, 233 time derivative of, 102 time evolution of, 95–96 tors, 47 wave functions and, 136 representing, 37–40 See also Bras (bra vectors); Kets (ket vectors); Singlet state; Triplet states

Schrödinger’s equation and evolution of, 227–230

Spring constant, 312

Statistical correlation, 158

Standard deviation, 140, 141

Subset, 13, 14, 15–16

Sums, integrals replacing, 240

Symmetric eigenfunctions, 340–341

Systems number of parameters characterizing, 45–47 quantum, combining, 160–161 See also Composite systems; Two-spin system

Tensor products, 149–155, 165, 176

Tensor products in composite form, 184–192 building tensor product matrices from basic principles, 185–187 building tensor product matrices from component matrices, 188–192

Tests for entanglement, 212–218

Time change in expectation values over, 109–114 conservation of distinctions and, 97–99 determinism and, 96 partial derivatives and, 320–321 time-evolution operator, 99–102 unitarity, 95, 98–99 See also Schrödinger equations

Time dependence, 116, 125, 286, 322. See also Uncertainty

Time-dependent Schrödinger equation, 102 harmonic oscillation and, 321–323 particle dynamics and, 274, 275–276, 289, 302 solving, 120, 121–124 state of system and, 126

Time derivatives, 102 Schrödinger equation for, 110–112

Time-development operator, 95 conservation of distinctions and, 97–99

Time evolution, 274 determinism and, 96 entanglement and, 181 unitary operators and, 98–99

Time-evolution operator, 99–102

Time-independent Schrödinger equation, 120–121, 124 particle dynamics and, 283–285, 286, 289

Trace normalized, 32, 40 of density matrix, 206, 207, 209 of projection operator, 195, 196 properties of, 209

Trajectories, path integrals, 301–309

Transposing, 60–61

Triangle inequality, 142–146

Triplet states, 166–167, 179, 181

Truth-value, 13–14

Two spins, 161–181 entanglement for, 202–210

Two-spin system Bell’s theorem and, 230–231 density matrix of, 202–212, 214–218, 226, 231

Two-state system, experiment on, 4–11

Uncertainty Cauchy-Schwarz inequality, 142 defined, 140–141 triangle inequality and Cauchy-Schwarz inequality, 142–146

Uncertainty principle, 20, 139–140, 146–148 Heisenberg, 139–140, 148

Unitarity, 95, 98–99, 100

Unitary evolution, 218, 222, 225

Unitary matrix, 225

Unitary operators, 95, 97–99

Unitary time evolution, 181

Unit matrix, 137 density matrix and, 217

Unit (normalized) vector, 32 state of system and, 40

Unit operator, as observable, 138

Up states, 71, 87–88, 219–220, 221–222

Vector addition, 26

Vectors basis (see Basis vectors)

column, 27–28, 29, 47, 49 concept of, 24–25 functions as, 238–245 normalized, 32, 40 orthogonal, 32, 64–67, 70 polarization, 91 quantum states and, 35–37 row, 29–30 three-(3-vector), 25, 27, 32–33, 74–75, 83 unit, 32, 40 See also Bras (bra vectors); Eigenvectors; Kets (ket vectors)

Vector space, 24–34 axioms, 24–27 bras, 28–30 column vectors, 27–28 functions and, 27–28, 239–240 inner products, 30–32 kets, 28–30 orthonormal bases, 32–34 tensor product as, 165 triangle inequality and, 142–146

Velocity momentum and, 286–288, 293 of quantum mechanical particle, 286–288

Venn diagram, 14, 16

Wave functions, 134–135, 236–238 action of Hamiltonian on, 320–321 calculating density matrices and, 206–207 collapse of, 126–127 entanglement and, 212–213 ground-state, 324–327 locality and, 225–226 measurement and collapsing, 218, 222–223 momentum and, 255–259 momentum representation, 260–265 of near-singlet state, 234 operator method and, 337–342 position representation, 254, 260–262, 263–265 of product state, 232 representing particles, 253–254 of singlet state, 233 state-vectors and, 136

Wavelength, momentum and, 259–260

Wave packets, 295–301 bimodal, 296–297 Gaussian, 301 harmonic oscillation and, 322 minimum-uncertainty, 301 moving at fixed speed, 276–277 for nonrelativistic free particle, 283

Waves, 235–236 harmonic oscillator and, 313

Wheeler, John, 52

x axis, spins along, 41–42

y axis, spins along, 42–45

Zaxon, 278

Zero function, 239

Zero operator, 133

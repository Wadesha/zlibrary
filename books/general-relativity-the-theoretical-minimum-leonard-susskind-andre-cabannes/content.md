# General Relativity The Theoretical Minimum Leonard Susskind Andre Cabannes Z Library

General Relativity The Theoretical Minimum What You Need to Know to Start Doing Physics Leonard Susskind & Andre Cabannes

One book at a time, the Theoretical Minimum series makes the power and grandeur of physics accessible.

First came classical mechanics, then quantum mechanics and special relativity. Now, physicist Leonard Susskind, assisted by a new collaborator, Andre Cabannes, returns to tackle Einstein's masterpiece: the general theory of relativity. Starting from the equivalence principle and covering the necessary mathematics of Riemannian spaces and tensor calculus, Susskind and Cabannes explain the link between gravity and geometry. They delve into black holes, establish Einstein field equations, and solve them to describe gravity waves. The authors provide vivid explanations that, to borrow a phrase from Einstein himself, are as simple as possible (but no simpler).

An approachable yet rigorous introduction to one of the most important topics in physics, General Relativity is a must-read for anyone who wants a deeper knowledge of the universe's real structure.

GENERAL RELATIVITY This book is the fourth volume of The Theoretical Minimum series.

The first volume, The Theoretical Minimum: What You Need to Know to Start Doing Physics, covered classical mechanics, which is the core of any physics education. We will refer to it from time to time simply as volume 1. The second book, volume 2, explains quantum mechanics and its relationship to classical mechanics. Volume 3 covers special relativity and classical field theory. This fourth volume expands on that to explore general relativity.

Also by Leonard Susskind Special Relativity and Classical Field Theory: The Theoretical Minimum Quantum Mechanics: The Theoretical Minimum The Theoretical Minimum: What You Need to Know to Start Doing Physics The Black Hole War: My Battle with Stephen Hawking to Make the World Safe for Quantum Mechanics The Cosmic Landscape: String Theory and the Illusion of Intelligent Design An Introduction to Black Holes, Information and the String Theory Revolution: The Holographic Universe

GENERAL RELATIVITY THE THEORETICAL MINIMUM LEONARD SUSSKIND & ANDRE CABANNES ALLEN LANE an imprint of PENGUIN BOOKS ALLEN LANE UK I USA I Canada I Ireland I Australia India I New Zealand I South Africa Allen Lane is part of the Penguin Random House group of companies whose addresses can be found at global.penguinrandomhouse.com.

To my family —LS To my parents, who taught me work and tenacity —AC

Contents Lecture 1: Equivalence Principle and Tensor Analysis 1 Lecture 2: Tensor Mathematics 53 Lecture 3: Flatness and Curvature 85 Lecture 4: Geodesics and Gravity 121 Lecture 5: Metric for a Gravitational Field 165 Lecture 6: Black Holes 197 Lecture 7: Falling into a Black Hole 235 Lecture 8: Formation of a Black Hole 263 Lecture 9: Einstein Field Equations 295 Lecture 10: Gravitational Waves 331

Preface This fourth volume in The Theoretical Minimum (TTM) series on general relativity is the natural continuation of the third volume on special relativity.

In special relativity, Einstein, starting from a very simple principle - the laws of physics should be the same in indistinguishable Galilean referentials - deeply clarified in a couple of papers published in 1905 the various disturbing observations physicists had made and the equations they had written in the last years of the nineteenth and the first years of the twentieth century concerning light and other phenomena.

Special relativity led to a strange description of space-time where time and space were inextricably mingled. For instance, it explained how particles whose lifetime is measured in fractions of a second can have, in our referential, a travel time from the Sun to Earth of more than eight minutes.

Then, from 1907 until 1915, essentially alone, Einstein reproduced his feat starting now from another very simple principle - acceleration and uniform gravity are equivalent. He generalized special relativity to a space-time containing massive bodies. The theory is called general relativity (GR). It led to an even stranger description of space-time where masses bend light and more generally warp space and time.

In lecture 1, we prepare the groundwork. We show how the equivalence principle inescapably leads to the bending of light rays by massive bodies.

Lecture 2 is devoted to tensor mathematics because in GR we must frequently change referentials and the equations relating coordinates in one referential to coordinates in another are tensor equations.

Then a large part of the theory is expressed using tensor equations because they have the great quality that if they hold in one referential, they hold in all of them.

Lectures 3, 4, and 5 are devoted to the geometry of Riemannian space and Minkowskian space-time because it can be said, very summarily, that gravity is geometry in a Minkowskian space-time.

In lectures 6, 7, and 8, we explore black holes, not so much because they are interesting astronomical phenomena per se, than because they are the equivalent in Minkowskian space-time of point masses in Newtonian mechanics. Space-time however presents a stranger behavior in the vicinity of a black hole than Newtonian space in the vicinity of a point mass. Understanding well black holes, the metric they create, their horizon, time and gravity in the vicinity of their horizon, the way people in and out of a black hole can communicate, etc. is a prerequisite to understanding GR.

In lecture 9 we sketch the derivation of Einstein field equations. And in lecture 10 we present a simple application predicting gravity waves.

This book, as the preceding ones in the series, is adapted from a course I gave for several years, with much pleasure, at Stanford in the Continuing Studies program to an audience of adults.

My coauthor this time is Andre Cabannes. Even though he is not a professional scientist, his scientific training, including a Stanford doctorate and a couple of years of teaching applied mathematics at the Massachusetts Institute of Technology (MIT), helped him assist me.

May Einstein's way of doing physics - starting from the simplest principles and pursuing dauntlessly the mathematics and the physics to their ultimate consequences, however unsettling they may be - as I have strived to show in this book, be a source of inspiration to young and future physicists.

Leonard Susskind Palo Alto, California Fall 2022

Ten years ago, when two of my children, then in their late teens, were studying sciences to enter the French system of grandes ecoles, I decided to brush up what I had learned in the seventies in order to accompany them in their studies. I discovered that the Internet had profoundly changed the learning landscape. Beside reading books, one could now also take excellent free courses on the Net. I leisurely attended courses in mathematics, physics, computer science, etc. from MIT, Stanford, and other places.

The subject matters often were better explained, the courses more lively and easier to understand, than what I had experienced in the past. One could choose courses by the world's best teachers.

Among these courses was The Theoretical Minimum series by Leonard Susskind, famous among other reasons for his pioneering work on string theory. I liked them so much that when I discovered that two of his filmed physics courses had already been transformed into books, I decided to translate them in French. Later I also translated the third book. Then, since the next volume didn't exist in English yet, I took up writing the English notes as well, having in mind that this work might turn out to be useful. After a lot more work with Professor Susskind and Basic Books team, volume 4 in The Theoretical Minimum series, on general relativity, that you hold in your hands is the result.

I belong to the group of people to whom these so-called Continuing Studies courses were intended: individuals who studied physics at the undergraduate and sometimes graduate level when they were students, then did other things in life, but kept an interest in sciences and would like to have some exposure to where physics stands today at a level above plain vulgarization. Indeed, personally, I have always found vulgarization more confusing and harder to understand than real explanations with some equations.

Leonard's courses gave me access to Lagrangian classical mechanics, quantum mechanics, and classical field theory with a clarity that I had never known before. With his pedagogy and presentation it becomes a pleasure to learn. Of course, it is all the more true when there is no examination of any sort at the end. But the courses and books turned out to be useful for students as well, to prepare for more advanced and academic studies.

So whether you are someone who only wants to have some real understanding of what general relativity is about - the stuff on gravitation that is geometry, masses that bend space, light, and time, black holes out there that you should avoid falling into, gravity waves that we can now detect from the collisions of black holes a billion light years away - or whether you want to study the subject in more depth, I hope you will find this book both interesting and useful.

waves that we begin to detect, etc. - or you are a student in physics who wants to have a first presentation of general relativity, this book is for you.

Andre Cabannes Saint-Cyr-sur-mer, French Riviera Fall 2022

Lecture 1: Equivalence Principle and Tensor Analysis

Andy: So if I am in an elevator and I feel really heavy, I can’t know whether the elevator is accelerating or you mischievously put me on Jupiter?

Lenny: That’s right, you can’t.

Andy: But, at least on Jupiter, if I keep still, light rays won’t bend.

Lenny: Oh yes they will.

Andy: Hmm, I see.

Lenny: And if you are falling into a black hole, beware, things will get really strange. But, don’t worry, I’ll shed some light on this.

Andy: Er, bent or straight?

Introduction Equivalence principle Accelerated reference frames Curvilinear coordinate transformations Effect of gravity on light Tidal forces Non-Euclidean geometry Riemannian geometry Metric tensor Mathematical interlude: Dummy variables Mathematical interlude: Einstein summation convention First tensor rule: Contravariant components of vectors Mathematical interlude: Vectors and tensors Second tensor rule: Covariant components of vectors Covariant and contravariant components of vectors and tensors

2 General Relativity

Introduction General Relativity is the fourth volume in The Theoretical Minimum (TTM) series. The first three were devoted respectively to classical mechanics, quantum mechanics, and special relativity and classical field theory. The first volume laid out the Lagrangian and Hamiltonian description of physical phenomena and the principle of least action, which is one of the fundamental principles underlying all of physics (see volume 3, lecture 7 on fundamental principles and gauge invariance). They were used in the first three volumes and will continue in this and subsequent ones.

Physics extensively uses mathematics as its toolbox to construct formal, quantifiable, workable theories of natural phenomena. The main tools we used so far are trigonometry, vector spaces, and calculus, that is, differentiation and integration. They have been explained in volume 1 as well as in brief refresher sections in the other volumes. We assume that the reader is familiar with these mathematical tools and with the physical ideas presented in volumes 1 and 3. The present volume 4, like volumes 1 and 3 (but unlike volume 2), deals with classical physics in the sense that no quantum uncertainty is involved.

We also began to make light use of tensors in volume 3 on special relativity and classical field theory. Now with general relativity we are going to use them extensively. We shall study them in detail. As the reader remembers, tensors generalize vectors. Just as vectors have different representations, with different sets of numbers (components of the vector) depending on the basis used to chart the vector space they form, this is true of tensors as well. The same tensor will have different components in different coordinate systems. The rules to go from one set of components to another will play a fundamental role. Moreover, we will work mostly with tensor fields, which are sets of tensors, a different tensor attached to each point of a space. Tensors were invented by Ricci-Curbastro and Levi-Civita1 to develop work of Gauss2 on curvature of surfaces and Riemann3 on non-Euclidean geometry. Einstein4 made extensive use of tensors to build his theory of general relativity. He also made important contributions to their usage: the standard notation for indices and the Einstein summation convention.

In Savants et ecrivains (1910), Poincare5 writes that “in mathematical sciences, a good notation has the same philosophical importance as a good classification in natural sciences.” In this book we will take care to always use the clearest and lightest notation possible.

Equivalence Principle Einstein’s revolutionary papers of 1905 on special relativity deeply clarified and extended ideas that several other physicists and mathematicians - Lorentz,6 Poincare, and others - had been working on for a few years. Einstein investigated the consequences of the fact that the laws of physics, in particular the behavior of light, are the same in different inertial reference frames. He deduced from that a new explanation of the Lorentz transformations, of the relativity of time, of the equivalence of mass and energy, etc.

After 1905, Einstein began to think about extending the principle of relativity to any kind of reference frames, frames that may be accelerating with respect to one another, not just inertial frames. An inertial frame is one where Newton’s laws, relating forces and motions, have simple expressions. Or, if you prefer a more vivid image, and you know how to juggle, it is a frame of reference in which you can juggle with no problem - for instance in a railway car moving uniformly, without jerks or accelerations of any sort. After ten years of efforts to build a theory extending the principle of relativity to frames with acceleration and taking into account gravitation in a novel way, Einstein published his work in November 1915. Unlike special relativity, which topped off the work of many, general relativity is essentially the work of one man.

We shall start our study of general relativity pretty much where Einstein started. It was a pattern in Einstein’s thinking to start with a really simple elementary fact, which almost a child could understand, and deduce these incredibly far-reaching consequences. We think that it is also the best way to teach it, to start with the simplest things and deduce the consequences.

So we shall begin with the equivalence principle. What is the equivalence principle? It is the principle that says that gravity is in some sense the same thing as acceleration. We shall explain precisely what is meant by that, and give examples of how Einstein used it. From there, we shall ask ourselves: what kind of mathematical structure must a theory have for the equivalence principle to be true? What kind of mathematics must we use to describe it?

Most readers have probably heard that general relativity is a theory not only about gravity but also about geometry. So it is interesting to start at the beginning and ask what is it that led Einstein to say that gravity has something to do with geometry.

What does it mean to say that “gravity equals acceleration”? You all know that if you are in an accelerated frame of reference, say, an elevator accelerating upward or downward, you feel an effective gravitational field. Children know this because they feel it.

What follows may be overkill, but making some mathematics out of the motion of an elevator is useful to see in a very simple example how physicists transform a natural phenomenon into mathematics, and then to see how the mathematics is used to make predictions about the phenomenon.

Before proceeding, let’s stress that the following study on an elevator, and the laws of physics as perceived inside it, is simple. Yet it is a first presentation of very important concepts. It is fundamental to understand it very well. Indeed, we will often refer to it. In lectures 4 to 9, it will strongly help us understand acceleration, gravitation, and how gravitation “warps” space-time.

So let’s imagine the Einstein thought experiment where somebody is in an elevator; see figure 1. In later textbooks, it got promoted to a rocket ship. But I have never been in a rocket ship, whereas I have been in an elevator. So I know what it feels like when it accelerates or decelerates. Let’s say that the elevator is moving upward with a velocity v.

Figure 1: Elevator and two reference frames.

So far the problem is one-dimensional. We are only interested in the vertical direction. There are two reference frames: one is fixed with respect to Earth. It uses the coordinate z. The other is fixed with respect to the elevator. It uses the coordinate z'. A point P anywhere along the vertical axis has two coordinates: coordinate z in the stationary frame, and coordinate z' in the elevator frame.

For instance, the floor of the elevator has coordinate z' = 0. Its z-coordinate is the distance L, which is obviously a function of time. So we can write for any point P zf = z — L(t) (1)

We are going to be interested in the following question: if we know the laws of physics in the frame z, what are they in the frame zf?

One warning about this lecture: at least at the start, we are going to ignore special relativity. This is tantamount to saying that we are pretending that the speed of light is infinite, or that we are talking about motions so slow that the speed of light can be regarded as infinitely fast. You might wonder: if general relativity is the generalization of special relativity, how did Einstein manage to start thinking about general relativity without including special relativity?

The answer is that special relativity has to do with very high velocities, while gravity has to do with heavy masses. There is a range of situations where gravity is important but high velocities are not. So Einstein started out thinking about gravity.

1 Gregorio Ricci-Curbastro (1853-1925) and his student Tullio Levi-Civita (1873-1941) were Italian mathematicians. Their most important joint paper is “Methodes de calcul differentiel absolu et leurs applications,” in Mathematische Annalen 54 (1900), pp. 125-201. They did not use the word tensor, which was introduced later by other people.

2 Carl Friedrich Gauss (1777-1855), German mathematician.

3 Bernhard Riemann (1826-1866), German mathematician.

4 Albert Einstein (1879-1955), German, Swiss, German again, and finally American physicist.

5 Henri Poincare (1854-1912), French mathematician.

6 Hendrik Antoon Lorentz (1853-1928), Dutch physicist.

y for slow velocities, and only later combined it with special relativity to think about the combination of fast velocities and gravity. And that became the general theory.

Let’s see what we know for slow velocities. Suppose that z and z' are both inertial reference frames. That means, among other things, that they are related by uniform velocity: z' = vt (2)

We have chosen the coordinates such that when t = 0, they line up. At t = 0, for any point, z and z' are equal. For instance, at t = 0 the elevator’s floor has coordinate 0 in both frames. Then the floor starts rising, its height z' equaling vt. So for any point we can write equation (1). In view of equation (2), it becomes z' = z — vt (3)

Notice that this is a coordinate transformation involving space and time. For readers who are familiar with volume 3 of TTM on special relativity, this naturally raises the question: what about time in the reference frame of the elevator? If we are going to forget special relativity, then we can just say that t' and t are the same thing. We don’t have to think about Lorentz transformations and their consequences. So the other half of the coordinate transformation would be t' = t.

We could also add to the stationary frame a coordinate x going horizontally and a coordinate y jutting out of the page. Correspondingly, coordinates x' and y' could be attached to the elevator; see figure 2. The x-coordinate will play a role in a moment with a light beam. As long as the elevator is not sliding horizontally, x' and x can be taken to be equal. Same for y' and y.

For the sake of clarity of the drawing in figure 2, we offset a bit the elevator to the right of the z-axis. But think of the two vertical axes as actually sliding on each other, and at t = 0 the two origins O and O' coincide. Once again, the elevator moves only vertically.

## 1. Equivalence Principle and Tensor Analysis

Figure 2: Elevator and two reference frames, three axes in each case.

Finally our complete coordinate transformation is z' = z — vt, t' = t, x' = x, y' = y (4).

It is a coordinate transformation of space-time coordinates. For any point P in space-time, it expresses its coordinates in the moving reference frame of the elevator as functions of its coordinates in the stationary frame. It is rather trivial. Only one coordinate, namely z, is involved in an interesting way.

Let us look at a law of physics expressed in the stationary frame. Take Newton’s law of motion F = ma applied to an object or a particle. The acceleration a is z'', where z is the vertical coordinate of the particle. So we can write F = mz'' (5).

As we know, z'' is the second time derivative of z with respect to time - it is called the vertical acceleration - and F of course is the vertical component of force. The other components we will take to be zero. Whatever force is exerted, it is exerted vertically. What could this force be due to? It could be related to the elevator or not. There could be some charge in the elevator pushing on the particle. Or it could just be a force due to a rope attached to the ceiling and to the particle that pulls on it. There could be a field force along the vertical axis. Any kind of force could be acting on the particle. Whatever the causes, we know from Newton’s law that the equation of motion of the particle, expressed in the original frame of reference, is given by equation (5).

8 General Relativity What is the equation of motion expressed in the primed frame? This is very easy. All we have to do is figure out what the original acceleration is in terms of the primed acceleration. What is the primed acceleration? It is the second derivative with respect to time of z'. Using the first equation in equations (4) z' = z — vt, one differentiation gives z'' = z' — v, and a second one gives z''' = z''. The accelerations in the two frames of reference are the same.

All this should be familiar. But I want to formalize it to bring out some points. In particular, I want to stress that we are doing a coordinate transformation. We are asking how the laws of physics change in going from one frame to another. What can we now say about Newton’s law in the primed frame of reference? We substitute z' for z in equation (5). As they are equal, we get F = mz'' (6).

We found that Newton’s law in the primed frame is exactly the same as Newton’s law in the unprimed frame. That is not surprising. The two frames of reference are moving with uniform velocity relative to each other. If one of them is an inertial frame, the other is an inertial frame. Newton taught us that the laws of physics are the same in all inertial frames. It is sometimes called the Galilean principle of relativity. We just formalized it.

Let’s turn to an accelerated reference frame.

## 1. Equivalence Principle and Tensor Analysis

Accelerated Reference Frames

Suppose that z' from figure 1 is increasing in an accelerated way. The height of the elevator’s floor is now given by z' = ½gt² (7).

We use the letter g for the acceleration because we will discover that the acceleration mimics a gravitational field - as we feel when we take an elevator and it accelerates. We know from volume 1 of TTM on classical mechanics or from high school, that this is a uniform acceleration. Indeed, if we differentiate z'(t) with respect to time, after one differentiation we get z' = gt, which means that the velocity of the elevator increases linearly with time. After a second differentiation with respect to time, we get z'' = g.

This means that the acceleration of the elevator is constant. The elevator is uniformly accelerated upward. The equations connecting the primed and unprimed coordinates are different from equations (4). The transformation for the vertical coordinates is now z' = z - ½gt² (8).

The other equations in equations (4) don’t change: t' = t, x' = x, y' = y.

These four equations are our new coordinate transformation to represent the relationship between coordinates that are accelerated relative to each other.

We will continue to assume that in the z, or unprimed, coordinate system, the laws of physics are exactly what Newton taught us. In other words, the stationary reference frame is inertial, and we

10 General Relativity have F = mz''. But the primed frame is no longer inertial. It is in uniform acceleration relative to the unprimed frame. Let’s ask what the laws of physics are now in the primed frame of reference. We have to do the operation of differentiating twice over again on equation (8). We know the answer: z'' = z' - g (9).

Ah ha! Now the primed acceleration and the unprimed acceleration differ by an amount g. To write Newton’s equations in the primed frame of reference, we multiply both sides of equation (9) by m, the particle mass, and we replace mz'' by F. We get mz'' = F — mg (10).

We have arrived at what we wanted. Equation (10) looks like a Newton equation, that is, mass times acceleration is equal to some term. That term, F — mg, we call the force in the primed frame of reference. You notice, as expected, that the force in the primed frame of reference has an extra term: the mass of the particle times the acceleration of the elevator, with a minus sign.

What is interesting about the “fictitious force” —mg, in equation (10), is that it looks exactly like the force exerted on the particle by gravity on the surface of the Earth or the surface of any kind of large massive body. That is why we called the acceleration g. The letter g stood for gravity. It looks like a uniform gravitational field. Let me spell out in what sense it looks like gravity. The special feature of gravity is that gravitational forces are proportional to mass - the same mass that appears in Newton’s equation of motion. We sometimes say that the gravitational mass is the same as the inertial mass. That has deep implications.

If the equation of motion is F = ma (11), and the force itself is proportional to mass, then the mass cancels in equation (11). That is a characteristic of gravitational forces: for a small object moving in a gravitational force field, its motion doesn’t depend on its mass. An example is the motion of the Earth about the Sun. It is independent of the mass of the Earth. If you know where the Earth is at time t, and you know

## 1. Equivalence Principle and Tensor Analysis

its velocity at that time, then you can predict its trajectory. You don’t need to know what the Earth’s mass is.

Equation (10) is an example of fictitious force - if you want to call it that - mimicking the effect of gravity. Most people before Einstein considered this largely an accident. They certainly knew that the effect of acceleration mimics the effect of gravity, but they didn’t pay much attention to it. It was Einstein who said: look, this is a deep principle of nature that gravitational forces cannot be distinguished from the effect of an accelerated reference frame. If you are in an elevator without windows and you feel that your body has some weight, you cannot say whether the elevator, with you inside, is resting on the surface of a planet or, far away from any massive body in the universe, some impish devil is accelerating your elevator. That is the equivalence principle. It extends the relativity principle, which said you can juggle in the same way at rest or in a railway car in uniform motion. With a simple example, we have equated accelerated motion and gravity. We have begun to explain what is meant by the sentence: “gravity is in some sense the same thing as acceleration.”

We have to discuss this result a bit, though. Do we really believe it totally or does it have to be qualified? Before we do that, let’s draw some pictures of what these various coordinate transformations look like.

Curvilinear Coordinate Transformations

Let’s first consider the case where z'(t) is proportional to t. That is when we have z' = z — vt.

In figure 3, every point - also called event - in space-time has a pair of coordinates z and t in the stationary frame an and also a pair of coordinates z' and t' in the elevator frame. Of course, t' = t and we left out the two other spatial coordinates x and y, which don't change between the stationary frame and the elevator. We represented the time trajectories of fixed z with dotted lines and of fixed z' with solid lines.

A fundamental idea to grasp is that events in space-time exist irrespective of their coordinates, just as points in space don't depend on the map we use. Coordinates are just some sort of convenient tags. We can use whichever we like. We'll stress it again after we have looked at figures 3 and 4.

Figure 3: Linear coordinate transformation. The coordinates (z', t') are represented in the basic coordinates (z, t). An event is a point on the page. It has one set of coordinates in the (z, t) frame and another set in the (z', t') frame. Here the transformation is simple and linear. That is called a linear coordinate transformation between the two frames of reference. Straight lines go to straight lines, not surprisingly since Newton tells us that free particles move in straight lines in an inertial frame of reference. What is a straight line in one frame had therefore better be a straight line in the other frame. Not only do free particles move in straight lines in space, when we add x and y, but their trajectories are straight lines in space-time - straight in space and with uniform velocity.

Let's do the same thing for the accelerated coordinate system. The transformation equation is now equation (8) linking z' and z. The other coordinates don't change. Again, in figure 4, every point in space-time has two pairs of coordinates (z, t) and (z', t'). The time trajectories of fixed z, represented with dotted lines, don't change. But now the time trajectories of fixed z' are parabolas lying on their side. We can even represent negative times in the past. Think of the elevator that was initially moving downward with a negative velocity but a positive acceleration g (in other words, slowing down). Then the elevator bounces back upward with the same acceleration g. Each parabola is just shifted relative to the previous one by one unit to the right.

Figure 4: Curvilinear coordinate transformation. What figure 4 illustrates is, not surprisingly, that straight lines in one frame are not straight lines in the other frame. They become curved lines. As regards the lines of fixed t or fixed t', they are of course the same horizontal straight lines in both frames. We haven't represented them.

We should view figure 4 as just two sets of coordinates to locate each point in space-time. One set of coordinates has straight axes, while the second - represented in the first frame - is curvilinear. Its lines z' = constant are actually curves, while its lines t' = constant are horizontal straight lines. So it is a curvilinear coordinate transformation.

Let's insist on the way to interpret and use figure 4 because it is fundamental to understand it very well if we want to understand the theory of relativity - special relativity and even more importantly general relativity. The page represents space-time - here, one spatial dimension and one temporal dimension.. Points (= events) in space-time are points on the page. An event does not have two positions on the page, i.e., in space-time. It has only one position on the page. But this position can be located, mapped "charted" one also says, using several different systems of reference. A system of reference, also called a frame of reference, is nothing more than a complete set of "labels," if you will, attaching one label (consisting of two numbers, because our space-time here is two-dimensional) to each point, i.e., to each event.

In a two-dimensional space, the system of reference can be geometrically simple, like orthogonal Cartesian axes in the plane. However this is not a necessity. For one thing, on Earth, which is not a plane, the axes are not straight lines. The usual axes used by cartographers and mariners are meridians and parallels. But on a 2D surface, be it a plane or not, we can imagine quite fancy or intricate curvilinear lines to serve as a frame of reference - so long as it attaches unequivocally two numbers to each (by definition, fixed) point. This is what figure 4 does in the space-time made of one temporal and one spatial dimension represented on the page. We will see many more in lecture 2.

Something Einstein understood very early is this: There is a connection between gravity and curvilinear coordinate transformations of space-time. Special relativity was only about linear transformations - transformations that take uniform velocity to uniform velocity. Lorentz transformations are of that nature. They take straight lines in space-time to straight lines in space-time. However, if we want to mock up gravitational fields with the effect of acceleration, we are really talking about transformations of coordinates of space-time that are curvilinear. That sounds extremely trivial. When Einstein said it, probably every physicist knew it and thought: "Oh yeah, no big deal." But Einstein was very clever and very persistent. He realized that if he followed very far the consequences of this, he could then answer questions that nobody knew how to answer.

Let's look at a simple example of a question that Einstein answered using the curved coordinates of space-time representing acceleration, and consequently, if the two are the same, gravity. The question is: what is the influence of gravity on light?

Effect of Gravity on Light

When Einstein first asked himself the question "what is the influence of gravity on light"? around 1907, most physicists would have answered: "There is no effect of gravity on light. Light is light. Gravity is gravity. A light wave moving near a massive object moves in a straight line. It is a law of light that it moves in straight lines. And there is no reason to think that gravity has any effect on it."

But Einstein said: "No, if this equivalence principle between acceleration and gravity is true, then gravity must affect light. Why? Because acceleration affects light." It was again one of these arguments that you could explain to a clever child.

Let's imagine that, at t = 0, a flashlight (today we might use a laser pointer) emits a pulse of light in a horizontal direction from the left side of the elevator; see figure 5. The light then travels across to the right side with the usual speed of light c. Since the stationary frame is assumed to be an inertial frame, the light moves in a straight line in the stationary frame.

gt elevator light beam x = 0 z = 0 £ = 0 ------------------------------------------- Figure 5: Trajectory of a light beam in the stationary reference frame. The equations for the light ray are x = ct (12) z = 0 The first of these equations just says that the light moves across the elevator with the speed of light - no surprise here.

The second says that in the stationary frame the trajectory of the light beam is horizontal. Let's express the same equations in terms of the primed coordinates. The first equation becomes x' = ct And the second takes the more interesting form z' = -½gt² It says that as the light ray moves across the elevator, at the same time the light ray accelerates downward - toward the floor - just as if gravity were pulling it. We can even eliminate t from the two equations and get an equation for the curved trajectory of the light ray: z' = - (g/2c²) x'² (13) Thus, the trajectory, in the primed frame of reference, is a parabola, not a straight line.

But, said Einstein, if the effect of acceleration is to bend the trajectory of a light ray, then so must be the effect of gravity.

Andy: Gee Lenny, that's really simple. Is that all there is to it? Lenny: Yup Andy, that's all there is to it. And you can bet that a lot of physicists were kicking themselves for not thinking of it.

To summarize, in the stationary frame, the photon trajectory (figure 5) is a straight line, while in the elevator reference frame, it is a parabola (figure 6). Let's imagine three people arguing. I am in the elevator, and I say: "Gravity is pulling the light beam down." You are in the stationary frame, and you say: "No, it's just that the elevator is accelerating upward; that makes it look like the light beam moves on a curved trajectory." And Einstein says: "They are the same thing!"

Figure 6: Trajectory of a light beam in the elevator reference frame. This proved to him that a gravitational field must bend a light ray. As far as I know, no other physicist understood this at the time.

In conclusion, we have learned that it is useful to think about curvilinear coordinate transformations in space-time. When we do think about curvilinear coordinates transformations, the form of Newton's laws changes. One of the things that happen is that apparent gravitational fields materialize, which are physically indistinguishable from ordinary gravitational fields. Well, are they really physically indistinguishable? For some purposes yes, but not for all. So let's turn now to real gravitational fields, namely gravitational fields of gravitating objects like the Sun or the Earth.

Tidal Forces Figure 7 represents the Earth, or the Sun, or any massive body. The gravitational acceleration doesn't point vertically on the page. It points toward the center of the body. It is pretty obvious that there is no way that you could do a coordinate transformation like we did in the preceding section that would remove the effect of the gravitational field. Yet, if you are in a small laboratory in space and that laboratory is allowed to simply fall toward Earth, or toward whatever massive object you are considering, then you will think that in that laboratory there is no gravitational field.

Figure 7: Gravitational field of a massive object, and small laboratory falling toward the object, experiencing inside itself no gravitation.

Exercise 1: If we are falling freely in a uniform gravitational field, prove that we feel no gravity and that things float around us like in the International Space Station.

But, again, there is no way globally to introduce a coordinate transformation that is going to get rid of the fact that there is a gravitational field pointing toward the center. For instance, a very simple transformation similar to equations (12) might get rid of the gravity in a small portion on one side of the Earth, but the same transformation will increase the gravitational field on the other side. Even more complex transformations would not solve the problem.

One way to understand why we can’t get rid of gravity is to think of an object that is not small compared to the gravitational field. My favorite example is a 2000-mile man who is falling in the Earth’s gravitational field; see figure 8. Because he is so big, different parts of his body feel different gravitational fields. Remember that the farther away you are, the weaker is the gravitational field.

His head feels a weaker gravity than his feet. His feet are being pulled harder than his head. He feels like he is being stretched, and that stretching sensation tells him that there is a gravitating object nearby. The sense of discomfort that he feels, due to the nonuniform gravitational field, cannot be removed by switching to a free-falling reference frame. Indeed, no change of mathematical description whatsoever can change this physical phenomenon.

Figure 8: A 2000-mile man falling toward Earth.

The forces he feels are called tidal forces, because they play an important role in the phenomenon of tides, too. They cannot be removed by a coordinate transformation. Let’s also see what happens if he is falling not vertically but sideways, staying perpendicular to a radius. In that case his head and his feet will be at the same distance from Earth. Both will be subjected to the same force in magnitude pointing to Earth. But since the force directions are radial, they are not parallel. The force on his head and the force on his feet will both have a component along his body. A moment’s thought will convince us that the tidal forces will compress him, his feet and head being pushed toward each other. This sense of compression is again not something that we can remove by a coordinate transformation. Being stretched or shrunk, or both, by the Earth’s gravitational field - if you are big enough - is an invariant fact.

In summary, it is not quite true that gravity is equivalent to going to an accelerated reference frame.

Andy: Aha! So Einstein was wrong after all.

Lenny: Well, Einstein was wrong at times, but no, Andy, this was not one of those times. He just had to qualify his statement and make it a bit more precise.

What Einstein really meant was that small objects, for a small length of time, cannot tell the difference between a gravitational field and an accelerated frame of reference.

It raises the following question: if I present you with a force field, does there exist a coordinate transformation that will make it vanish? For example, the force field inside the elevator In 3D Euclidean space we live in. By unfurling the page, we can make its flatness obvious again.

Einstein realized that there was a great deal of similarity in the two questions of whether a geometry is non-flat and whether a spacetime has a real gravitational field in it. Riemann had studied the first question. But Riemann had never dreamt about geometries that have a minus sign in the definition of the square of the distance. He was thinking about geometries that were non-Euclidean but were similar to Euclidean geometry - not Minkowski geometry.

Let’s start with the mathematics of Riemannian geometry, that is, of spaces where the distance between two points may not be the Euclidean distance, but in which the square of the distance is always positive.8

We look at two points in a space; see figure 11. In our example there are three dimensions, therefore three axes, X1, X2, and X3. There could be more. Thus a point has three coordinates, which we can write as Xm, where m is understood to run from 1 to 3 or to whatever number of axes there is. And a little shift between one point and another nearby has three components, which can be denoted AXm or, if it is to become an infinitesimal, dXm. 8In mathematics, they are called positive definite distances.

If this space has the usual Euclidean geometry, the square of the length of dXm is given by Pythagoras theorem dS2 = (dX1)2 + (dX2)2 + (dX3)2 + also add more rigid elements diagonally. This would create a lattice as shown in figure 15. But any reasonably dense lattice, sort of triangulating the surface, would do as well. Suppose furthermore that the Tinkertoy elements are hinged together in a way that lets them freely move in any direction from each other.

Imagine that we lift our lattice from the surface. Sometimes it will keep its shape rigidly, sometimes it won’t. It will not keep its shape if it is possible to go from the initial shape to a new shape without forcing any Tinkertoy element to be stretched or compressed or bent.

In some cases it will even be possible to lay it out flat. It is the case, for instance, in figure 10 going from the shape on the right to the shape on the left - which is just a flat page.

Exercise 2: Is it possible to find a curved surface and a lattice of rods arranged on it that cannot be flattened out, but can change shape?

Answer: Yes. According to Gauss’s Theorema Egregium, which we invite the reader to look up, a surface can be modified without stretching or compressing it as long as we preserve everywhere its Gaussian curvature. For instance, it is possible to change in such a way a section of a hyperbolic paraboloid.

We shall see that the initial surface being able to take other shapes or not corresponds to the g_mn’s of equation (15) having certain mathematical properties. The collection of g_mn’s has a name. It is called the metric tensor. It is the mathematical object that enables us to compute the distance between two neighboring points on our Riemannian surface. Mind you, the g_mn’s are functions of X (the points of the manifold). So, strictly speaking, we are talking about a tensor field. But it is customary to talk casually of the metric tensor, keeping in mind that the collection of its components depends on X.

When the lattice of Tinkertoy elements can be laid out flat, the geometry of the surface is said to be intrinsically flat, or just flat. We will define it more rigorously later.

Sometimes, on the other hand, the lattice of little rods cannot be laid out flat. For example on the sphere, if we initially lay out a lattice triangulating a large chunk of the sphere, we won’t be able to lay it out on a flat plane.

The question we have to address is this: if I made a lattice of little rods covering a surface, and I gave you the length of each rod, without yourself building the lattice how could you tell me whether it is a flat space or an intrinsically curved space, which cannot be flattened and laid out on a flat plane?

Let’s formulate the problem more precisely and mathematically. We start from the metric tensor which is a function of position, in some set of coordinates. Keep in mind that there are many different possible sets of curvilinear coordinates on the surface, and in every set of coordinates the metric tensor will look different. It will have different components, just like the same 3-vector in ordinary 3D Euclidean space has different components depending on the basis used to represent it, but in addition the components will vary with position in different ways.

I select one set of coordinates and I give you the metric tensor of my surface. In effect I tell you the distance between every pair of neighboring points. The question is: is my surface flat or not?

To answer that question, you may think of “checking π.” Here is the way it would go. Think of a 2D surface embedded in the usual 3D Euclidean space as shown in figure 12. You select a point and mark out a disk around it. Then you measure its radius r as well as its circumference C, and you divide C by 2r. If you get 3.14159... you would say that the surface is flat. Otherwise you would say that it is not flat, it is intrinsically curved. Notice that this procedure is good for a two-dimensional surface, under certain conditions. Anyway it is not so great for higher-dimensional surfaces.

What is the mathematics of taking a metric tensor and asking if its space is flat? What does it mean for it to be flat? By definition, it means this: The space is flat if we can find a coordinate transformation, that is, a different set of coordinates, in which, at any point on the surface, the distance formula for dS² becomes just (dX¹)² + (dX²)² + ... + (dXⁿ)², as it would be in Euclidean geometry.

It is not necessary that the initial g_mn(X) form everywhere the unit matrix, with ones on the diagonal and zeroes elsewhere - as if equation (15) were just Pythagoras theorem. But we must find a coordinate transformation that brings it to that form.

In that sense, it has a vague similarity with the question of whether you can find a coordinate transformation that removes the gravitational field. In fact, it turns out not to be a vague similarity at all but a close parallel. The question is: can we find a coordinate transformation that removes the curvy character of the metric tensor g_mn?

To answer that geometric question, we have to do some mathematics essential to relativity. It is not possible to understand general relativity without it. The mathematics is tensor analysis plus some differential geometry. At first it looks annoying because we have to deal with all these indices floating around, and different coordinate systems, and partial derivatives of components, etc. But once we get used to it, we will see that it is simple. It was invented, as said, by Ricci-Curbastro and Levi-Civita at the end of the nineteenth century to build on works of Gauss and Riemann. It was further simplified by Einstein, who set rules for the position of indices and astutely got rid of most summation symbols.

Before explaining what is the Einstein summation convention eliminating most summation symbols, let’s spend a few moments explaining the simple concept of dummy variable.

Mathematical Interlude: Dummy Variables

We are accustomed to equations where all the variables have a substantial mathematical or physical meaning. A physical example is equation (7), reproduced here: s = ½gt² This famous equation was found by Galileo Galilei in the first half of the seventeenth century, before the invention of calculus. In fact, it is one of the equations that triggered the invention of calculus by Newton and Leibniz. It describes the fall of an object: s stands for the distance of fall as a function of time, g stands for the acceleration on the surface of the Earth, and t stands for time.

Another even simpler and purely mathematical example is A = ab where a is the length of a rectangle, b is its width, and A is its area.

But we are also familiar with equations where one of the variables is only a handy mathematical notation without a substantial meaning. A simple example is the well-known identity expressing the value of the sum of all the squares of the integers from 1 to m: m(m + 1)(2m + 1) / 6 = Σ n² for n=1 to m Here the variable m has a substantial meaning: it is the number up to which we sum. But the variable n on the right-hand side does not have such a substantial meaning. We could rewrite the equation as: m(m + 1)(2m + 1) / 6 = Σ k² for k=1 to m It would be exactly the same equation.

The variable n, or the variable k, is called a dummy variable. It is only used to conveniently express the sum.

We will meet many formulas containing one or several dummy variables, usually expressing sums, in general relativity. They are so frequent that Einstein came up with a rule to simplify them. His rule, or convention, turned out to be not only a great simplification, but also a very useful notational device to write general relativity equations, providing a guide rail as well as having a meaning on its own. The convention is the topic of the next mathematical interlude. Later in this lecture and in the rest of the book, we will discover its remarkable usefulness.

Mathematical Interlude: Einstein Summation Convention

As we go along, we will see that certain patterns keep recurring in the equations. One such pattern involves expressions in which an index such as μ is repeated in a single expression. Here is an example. For the moment it doesn’t matter what it means; it’s just a pattern that we will see over and over.

g_μν U^μ V^ν There are a few things to note. First of all, there is a summation over μ, which means that μ is a dummy index. It is just another name, in the specific context of vectors and tensors, for a dummy variable. As a consequence, what letter we use doesn’t matter. The expressions with μ as above, or with ν as below, represent exactly the same thing, whence, as we saw, the term dummy.

g_νμ U^ν V^μ

Secondly, the dummy index appears twice in the same expression - not once, not three times, twice.

Finally, the repeated index occurs once as a superscript and once as a subscript. I often say that it appears once upstairs and once downstairs. That’s the pattern: a sum over an index that appears once upstairs and once downstairs.

Einstein’s famous trick - the so-called Einstein summation convention - was just to leave out the summation sign. The rule is: whenever we see something like g_μν U^μ V^ν, we automatically sum over the index μ.

We can readily apply the convention to formula (15) that we met earlier expressing the general form of the metric in a Riemannian space (or for that matter in any coordinate system in general relativity).

in a Minkowskian space as well, we shall see). It was.

dS² = Σₘ Σₙ gₘₙ(X) dXₘ dXₙ

With the Einstein summation convention it becomes dS² = gₘₙ(X) dXₘ dXₙ Simpler! Isn’t it?

Usually, not forgetting that the gₘₙ components depend on X, i.e., remembering that the metric tensor is actually a tensor field, we simplify it even further to dS² = gₘₙ dXₘ dXₙ

Andy: Did it really take Einstein to invent the summation convention?

Lenny: I guess it did. When I was a student, I read Einstein’s famous 1916 paper “The Foundation of the General Theory of Relativity.” It was my habit when I learned new physics to write out the equations as I read them. At the start of the paper, the equations were written as anyone else would write them. Here’s his equation 2: dXₐ = δₐᵦ dXᵦ

But then all of a sudden, right after equation 7, Einstein casually remarks that there is always a summation when indices appear twice.¹² So from now on, he said, well just keep that in mind and stop writing the summation sign. It’s pretty clear that he just got tired of writing them. I was pretty tired of writing them too. What a relief it was.

End of interlude on Einstein summation convention.

Let’s return to the metric and its various forms in several different coordinate systems. To find a set of coordinates that make equation (15) become equation (14) is a more involved procedure than just diagonalizing the matrix gₘₙ. The reason is that there is not one matrix. As we stressed, each component gₘₙ depends on X.

It is the same tensor field, but it has a different matrix at each point.¹³ You cannot diagonalize them all at the same time. At a given point, you can indeed diagonalize gₘₙ(X) even if the surface is not flat. It is equivalent to working locally in the tangent plane of the surface at X, and orthogonalizing the coordinate axes there. But you cannot say that a surface is flat because it can be made at any given point locally to look like the Euclidean plane.

Let’s examine equation (14) more closely. It can be written in terms of a special matrix whose components are the Kronecker-delta symbol δₘₙ, defined in the following way.¹⁴ First of all, δₘₙ is zero unless m = n. For example, in three dimensions δ₁₂, δ₁₃, and δ₂₃ are all zero, but δ₁₁, δ₂₂, and δ₃₃ are nonzero. In other words, at each point the Kronecker-delta symbol is a diagonal matrix.

Secondly, the diagonal elements are all equal to 1: δ₁₁ = δ₂₂ = δ₃₃ = 1

Armed with the Kronecker-delta and the Einstein summation convention, we can rewrite equation (14) in the compact form, dS² = δₘₙ dXₘ dXₙ (17)

To determine if a space is flat, we look for a coordinate transformation, X → Y, that turns gₘₙ into δₘₙ everywhere. Remember that X and Y represent the same point P. This point P is simply located with two different reference systems, which, as we stressed, are nothing more than some geometric labeling procedure.

Later, the points P will be events in space-time, and the Kronecker-delta will be replaced by a slightly more involved diagonal matrix in Minkowski geometry (also called Minkowskian or Einsteinian geometry), but many of the ideas will remain unchanged. However let’s not go too fast, and for the moment let’s stay in Riemannian geometry. Riemannian geometry is everywhere locally Euclidean. It can be thought of as “Euclidean geometry on a piece of rubber.” For most metrics it is not possible to find a coordinate transformation that transforms everywhere the gₘₙ into δₘₙ. It is only when the space is intrinsically flat that we can.

In summary, I give you the metric tensor of my surface, that is, the gₘₙ of equation (15), which we now write dS² = gₘₙ(X) dXₘ dXₙ

The question I ask you is: can you, by a coordinate transformation X → Y, reduce it to equation (17)? That is, in the Y system, dS² = δₘₙ dYₘ dYₙ

There is no need to write δₘₙ(Y), since the Kronecker-delta symbol by definition has a unique form. However, for the sake of clarity, we will sometimes still write δₘₙ(y) because it reminds us of which system of coordinates we are using.

If the answer is yes, the space is called flat. If it is no, the space is called curved. Of course, the space could have some portions that are flat. There could exist a set of coordinates such that in a region the metric tensor is the Kronecker-delta. But the surface is called flat only if it is everywhere flat.

This becomes a pure mathematics problem: given a tensor field gₘₙ(X) on a multidimensional space (which mathematicians call a manifold), how do we figure out if there is a coordinate transformation that would change it into the Kronecker-delta symbol?

To answer that question, we have to understand better how things transform when we make coordinate transformations. That is the subject of tensor analysis. We begin to present the subject in the rest of this lecture, and will treat it in more depth in lecture 2.

The analogy between tidal forces and curvature actually is not an analogy, it is a very precise equivalence. In the general theory of relativity, the way you diagnose tidal forces (or said more accurately, their generalization) is by calculating the curvature tensor.

A flat space is defined as a space where the curvature tensor is zero everywhere. Therefore it is a very precise correspondence.

Simply stated: Gravity is curvature.

But we will come to this conclusion as we get through tensor analysis. Obviously, in trying to determine whether we can transform away gₘₙ(X) and turn it into the trivial δₘₙ(y), the first question to ask is: how does gₘₙ(X) transform when we change coordinates? We have to introduce notions of tensor analysis that are rather easy.

We shall express the first tensor rule, then present a mathematical interlude spelling out some general facts on vectors and tensors, then present the second tensor rule.

We will conclude this copious lecture again with some general considerations on covariant and contravariant components of vectors and tensors.

First Tensor Rule: Contravariant Components of Vectors Sometimes tensor notations are a bit of a nuisance because of all the indices. At first we can get confused by them. But soon we will discover that the manipulations obey strict rules and turn out to be rather simple.

We shall begin with a simpler thing than gₘₙ(X). Suppose that there are two sets of coordinates on our surface: a set of coordinates and a second set that we could call X' as we did earlier. But then we would be running into horrible notations with cluttered expressions like X'¹. So we denote the second set of coordinates Yₘ. To be very explicit, if we are on a space of dimension N, the same point P has coordinates [ X¹(P), X²(P), ... ,Xᴺ(P) ]

and also has coordinates [ y¹(P), y²(P),... ,yᴺ(P) ]

The X’s and Y’s are related because if you know the coordinates of a point P in one set of coordinates, then in principle you know where the point is. Therefore you also know its coordinates in the other coordinate system. Thus each coordinate Xₘ is a function of all the coordinates Yₙ. We can use whatever dummy index we want if that helps avoid confusion. We will simply write Xₘ(Y)

Likewise each Yₘ is assumed to be a known function of all the Xₙ’s: Yₘ(X)

In short, we have two coordinate systems, each one a function of the other. The correspondence is one-to-one since these are coordinate systems. And we assume that the functions are nice and smooth.

Now we ask: how do the differential elements dXₘ transform? The collection of differential elements dXₘ is a small vector, as shown in figure 16. Remember that the vector itself is a pair of points (an origin and an end). It is independent of the coordinate system. But in order to work with it, it is useful to express it using its components dXₘ.

dXₘ Figure 16: Small displacement expressed in the X coordinate system. The notation dXₘ is used to represent the small vector dXₘ = [dX¹, dX², ... ,dXᴺ]

Said another way, when we change X a little bit, the point P moves to a nearby point Q, and the displacement is dXₘ.

Let’s look at the same displacement, expressed in the Y coordinate system. We want to know how dYₘ can be expressed in terms of the dXᵣ’s. It is an elementary result of calculus that dYₘ = (∂yₘ/∂xₚ) dXᵖ or using the summation convention, dYₘ = (∂yₘ/∂xₚ) dXᵖ (18)

Let’s spell out even more explicitly what equation (18) says: the total change of some particular component is the sum of the rate of change of Yₘ when you change only X¹, times the little change in X¹, namely dX¹, plus the rate of change of Yₘ when you change only X², times the little change in X², namely dX², and so forth up to Xᴺ and dXᴺ because equation (18) means a sum over the dummy index p going from 1 to N.

We now turn to some general considerations on vectors and tensors. So far we have used several times the term tensor (tensor calculus, metric tensor, curvature tensor, first tensor rule, etc.), without explaining what is a tensor! As the reader has understood, it is a fundamental mathematical tool in general relativity. You may even remember that “it extends the concept of vector.” But that is certainly not a sufficient explanation to grasp what it is.

We won’t go into a full fledged exposition of linear algebra and tensors - which the reader may find in any good manual on the subject. However, as I have done several times in The Theoretical Minimum series, for instance, when I dared to explain in volume 1 integral calculus or partial differentiation in brief interludes of a few pages, because we needed those tools for classical mechanics, it is time in this lecture for a third mathematical interlude presenting in some detail vectors and tensors.

Mathematical Interlude: Vectors and Tensors Let’s begin with the simplest notion of a tensor, namely a scalar. A scalar S(X) is a function of position with the property that it has the same value in every coordinate system. For that reason, we could also denote it S(P), but we want to insist on the coordinate system we chose to use, so we write instead S(X). For the same scalar in the Y coordinate system, we will temporarily use the notation S'(Y). (Later we will use S(Y) and S(X) for both, because it is clearer when we talk about the chain rule.)

Its transformation properties are trivial: it doesn’t transform at all. An example drawn from meteorology would be the temperature at a point in space. The transformation property of a scalar reflects this triviality, S'(Y) = S(X)

In the case of temperature, this says that the temperature at a point is just a number.* 15 It does not depend on the orientation of the coordinate system at that point. Note too that scalars do not have components, or perhaps more accurately, they have only one component: the value of the scalar itself.

Let’s turn to the next simple kind of tensors, namely vectors. We shall see that there are two kinds.

We all have an intuitive idea of what a vector in a Riemannian geometry is. It is a little arrow, usually attached to a point in space. It points in a direction and it has a magnitude. An example, again from meteorology, would be the wind velocity.

In a Riemannian geometry, a vector is a thing unto itself, but given a coordinate system and a metric, it can be described by components in one of two ways: either contravariant or covariant components.

Since the terms can be a little confusing, let’s stress right away that what are called the contravariant components of a vector are the good old components with which we construct the vector as a linear combination of the basis vectors.

We will see that we can also attach to a vector another set of numbers, called its covariant components. They are not its ordinary contravariant components, but something else, the geometrical meaning of which will be explained in lecture 2. The contravariant and covariant components of a vector will be simply related to each other with the help of the metric.

These components, like the components of the metric itself, will vary when the coordinates system changes. For the moment, however, let’s not think of a metric, only of a system of coordinates X and a system of coordinates Y. We position ourselves at a point P. At this point, we consider a set of numbers attached to it and that depends on the coordinate system.

Disregarding any geometric interpretation, this set of numbers can be viewed as an abstract “vector.” As said, we are in the case where the vector will change with the coordinate system.

In that case we will have two kinds of vectors: covariant or contravariant vectors. Notice I said covariant or contravariant vectors - not covariant or contravariant components. Later, when we have introduced a metric, we can put the two together to describe a single kind of vector (the intuitive arrow) in two ways.

What is it that makes a collection of numbers like dX™ a contravariant vector, rather than just a collection of numbers? The answer is the transformation properties under a coordinate transformation. Equation (18) defines the paradigm for the transformation of a contravariant vector.

A contravariant vector is a set of numbers Vm that transform as follows: dYm (VV = (19)

(7-A r In this equation the variables V are the components of the vector in the X coordinate system and (V') are the components in the Y system. Looking back at equation (18), we see that the differential displacement dXm is a contravariant vector.

There are a couple of things to note. First of all, I have used the summation convention so that the index p is summed over. Secondly, the index p in the expression dYm/dXp is a downstairs index. That’s a convention that we have already mentioned in the interlude on Einstein summation convention and that the reader will have to remember: when an upstairs index occurs in the denominator of an expression, it counts as a downstairs index.

Generally speaking, in a “level” expression (i.e., with no denominator) or in the numerator of a fraction, a superscript index is called a contravariant index. And a subscript index is a called a covariant index. But, as we said, according to the summation convention, a superscript in the denominator of a fraction acts like a covariant index.

Let’s move on to the second kind of vector - a covariant vector. If the iconic contravariant vector is the displacement dXm, the iconic covariant vector is the gradient of a scalar S(X).

Its components are given by the derivatives of the scalar along the coordinate axes: dS(X)

(20)

dXp Clearly these components depend on the choice of coordinates, and will transform when the coordinates are transformed. For example, suppose we transform from the X to the Y system. To compute the components of the gradient in the Y system, we use a version of the chain rule of calculus (see lecture 2 of volume 1 of TTM, in which the chain rule is explained). We get dS dS dXp (21)

dY™ dXp dY™ From this we can abstract the general rule for the transformation of a covariant vector: 9Xp = w, — (22)

Thus, in equation (18), we met the first example of transformation of a tensor, because an ordinary vector, corresponding for instance to the position of a point, or to a displacement (in other words, a translation), or to a velocity, etc., is a contravariant vector, which is a simple kind of tensor.

Indeed, we now have the expressions, in two different coordinate systems, of the small displacement of a point on the surface (figure 16). They are dXm and dYm. Let’s repeat that the dXm and dYm are two sets of components for the same displacement. And we know how to go from one set to the other.

Figure 17, which completes figure 16, shows the small displacement, and also locally the two sets of coordinates.

By now the reader has understood that equation (18) is simply the transformation property of the components of the displacement vector when this displacement vector (which is itself a well-defined geometric object, being defined independently of any coordinate system16) is expressed in the X system and in the Y system.

Figure 17: Small displacement, and two sets of coordinates. The small vector has components (dX1, dX2) shown, but also (dV1, dV2) not shown.

Note on terminology: because we will deal with vectors that can have contravariant expressions but also covariant expressions, we will prefer to speak of the contravariant components of a vector or the covariant components of a vector.

In short, the term contravariant comes from the fact that if we change the unit vectors in the coordinate system, for instance if we simply divide the length of each of them by ten, the components of a vector representing a translation will be multiplied by ten. Turning to the other term, covariant comes from the fact that, in the same kind of change of coordinates, the components of a gradient will be divided by ten.

The interlude presented the simplest kind of tensors: tensors of rank 0, which are simply scalars; and tensors of rank 1, which are contravariant vectors and covariant vectors. The next kinds of tensors, of rank 2 or more, will be presented in the last section of this lecture.

Second Tensor Rule: Covariant Components of Vectors Although we have already mentioned it cursorily in the preceding mathematical interlude, for the sake of symmetry, let’s spell out the second tensor rule concerning the covariant components of vectors. These vectors are used to represent other things than position or translation or velocity or acceleration, etc. The reader may primarily think of gradients of scalar fields.

Examples of scalar fields are the temperature, the atmospheric pressure, the Higgs field, whatever has, at any point in the space, a value that is not multidimensional but simply a number, and that doesn’t change if we change coordinates.

wind velocity is not a scalar field because at every point it has a vector value. It is a vector field. It is important to note the following point, which should clarify things:

If we tried to consider only the first component of the vector representing the wind, we would not get a scalar field, because it would not be invariant under change of coordinates.

Thus the gradient of a scalar function is a vector (in the sense of a collection of components). But it is not an ordinary vector. Indeed, its components don’t transform in the same way as do the contravariant components of ordinary vectors.

We saw earlier that an application of the chain rule gave us equation (21), which we reproduce here: dS/dYm = (dS/dXp) * (dXp/dYm)

Denoting by (W')^m the gradient of S with respect to the Y’s, and by W its gradient with respect to the X’s, it can be rewritten as equation (22), which we also reproduce, attributing it a new number: (W')^m = (dXp/dYm) * W^p (23)

Equation (23) doesn’t apply only to gradients; it is the fundamental equation linking the primed and unprimed versions of the covariant components of a vector, that is, its components in the Y system and in the X system.

Notice that the indices m of W' and p of W are downstairs. The index p is a dummy index that is to be summed over as it also appears upstairs in dXp. It is a nice example of the very useful Einstein summation convention and of its smooth workings.

Let’s rewrite equations (19) and (23) next to each other, and relabel them: Contravariant components (V')^m = V^p * (dYm/dXp) (24a)

Covariant components (W')_m = W_p * (dXp/dYm) (24b)

They look very much alike except that dYm/dXp appears in the first one, and the inverse, dXp/dYm, in the second.

Let’s recall one last time that displacements, or positions, or velocities, etc., are described with vectors having contravariant components. We saw that these change contrary to the basis change. Gradients, on the other hand, are described with vectors the components of which change like the basis change. That is why their components are called covariant. But these vectors are different from the somewhat more intuitive contravariant vectors.

In mathematics, vectors with covariant components are sometimes viewed as vectors in the dual space of the primary vector space under consideration. They are then dual vectors like linear forms are. But we won’t adopt this approach. For us vectors will be things that have a one-indexed collection of contravariant components and also of covariant components.

Equations (24a) and (24b) are fundamental equations for this course. The reader needs to understand them, become familiar and at ease with them, because they are absolutely central to the entire subject of general relativity. You need to know where the indices go for different kinds of objects, and how these objects transform. That is in some sense what general relativity is all about: the transformation properties of different kinds of objects.

Covariant and Contravariant Components of Vectors and Tensors

We have seen two ways to think about an ordinary vector. First of all, we can think of it like we have learned in high school: it is a displacement with a length and a direction, that is, an arrow in a space. This is geometrically well defined even before we consider any basis.

We can also think of it more abstractly as some object that has components. These components depend on the basis. If the components transform in a certain way when we change basis, namely according to equation (24a), then the object behaves exactly like our good old vectors. Therefore we can also equate the object to an ordinary vector. In tensor analysis we call them vectors whose components are contravariant.

Similarly, some other objects have components that transform according to equation (24b). They cannot be equated to our old ordinary vectors, but to other geometric things. We mentioned that mathematicians view them as dual vectors. We will just call this second type of object vectors whose components are covariant. In fact, we will see in lecture 2 that our abstract vectors have a contravariant version and a covariant version.

In tensor calculus, of which general relativity makes heavy use,17 paradoxically for those people who have a geometric mind or intuition, it is often useful, at least at first, to forget about the geometric interpretation of the objects we manipulate, and to focus only on how collections of numbers attached to points in our space behave when we change systems coordinates.

A vector - be it with contravariant or covariant components - is a special case of a tensor. Following what we just said, we are not going to define tensors geometrically. For us, at first, tensors will be things that are defined by the way they transform. The way they transform means the way they change (or if you prefer, their components change) when we go from one set of coordinates to another. Later we will give a geometric interpretation of some tensors. We will also go deeper into contravariant and covariant components. We will see that an object with one index can have a contravariant version and a covariant version. All this will be developed in the next lecture. For the time being, let’s continue to proceed step by step in our construction of the mathematical tools necessary for general relativity.

The next step, for us now, is to talk about tensors with more than one index.

The best way to approach tensors with several indices is to consider a special, very simple case to start with. Let’s imagine the “product” of two vectors with contravariant components.18 We consider the two vectors with contravariant components, V and U, and we consider the following product: V^m U^n

Without further ado, we will now always use the convention that contravariant components, or contravariant indices referring to these components, are noted upstairs.

The vectors V and U don’t have to come from the same space. If the dimensionality of the space of V is M, and the dimensionality of the space of U is N, there are M x N such products. As usual, we use the notation V^m U^n to denote one product as well as the collection of all of them - just like V^m denotes one component of the vector V, but is also a notation, showing explicitly the position of the index, and therefore the nature of the full vector V itself.

Let’s define T^mn as T^mn = V^m U^n (25)

Notice that it matters where and in which order we write the indices of T^mn, because, for instance, T^mn is not the same as T^nm. The reader is invited to explain why. Soon we will also see combinations of indices upstairs and downstairs.

Product T^mn is a special case of tensor of rank 2. Rank 2 means that the collection of component products has two indices. It runs over two ranges: m runs from 1 to M, and n runs from 1 to N. For example, if both V and U come from a four-dimensional space, there will be 16 components V^m U^n. In that case T^mn, as we saw, represents one component but also the entire collection of 16 components.

How does T^mn transform?

For example V^m and U^n could be the components of the vectors V and U in the unprimed frame of reference, the reference frame using the X coordinates. Since we know how the individual components transform, when we go to the Y coordinates, we can figure out how T transforms. Let’s call (T')^mn the mn-th component of the tensor in the primed frame: (T')^mn = (V')^m (U')^n

Then using equation (24a) twice, this can be rewritten as (T')^mn = [V^p (dYm/dXp)] * [U^q (dYn/dXq)]

The four terms on the right-hand side are just four numbers, so we can change their order and write it (T')^mn = (dYm/dXp) * (dYn/dXq) * V^p U^q

Finally, V^p U^q is just T^pq. So the way T transforms is (T')^mn = (dYm/dXp) * (dYn/dXq) * T^pq (26)

We found in the special case of a product of ordinary vectors how T transforms. Now this leads us to the following definition:

Anything that transforms according to equation (26) is called a tensor of rank 2 with two contravariant indices.

If there were more indices upstairs, the rule would be adapted in the obvious manner. A tensor of rank 3, all indices contravariant, would transform like this: (T')^mnp = (dYm/dXr) * (dYn/dXs) * (dYp/dXt) * T^rst

What kinds of things are tensors like that? Many things. Products of vectors are particular examples, but there are other things that are not products and still are tensors according to this definition.

We are going to see that the metric object gmn is a tensor. But it is a tensor with covariant indices. So to finish this lecture, let’s see how things with covariant indices transform. Equation (24b) shows how an object with only one covariant index transforms. It is a tensor of rank 1 of covariant type.

Let’s begin again with the particular case of the product of two covariant vectors W and Z, or to speak less casually, two vectors with covariant components.

The components. Their product transforms as follows: dXp dXq (w')m(z')n = Wpzq

Here we have discovered a new transformation property of a thing with two covariant indices, that is, two downstairs indices.

More generally let’s consider an object that we will denote Tmn. It is no longer simply a product of vectors but a different object. However, the letter T signals that it is something that will still be a tensor. It is a tensor with two lower indices, and it transforms according to Of the angle between the coordinate axes. We may also have to correct for units that are not unit distances on the axes. Yet the page is intrinsically flat, be it rolled or not in the embedding 3D Euclidean space. It is easy to find a set of coordinates Y’s that will transform equation (1) into the Pythagoras theorem. On the pages of primary school notebooks, they are usually shown. It doesn’t disturb us to look at them, interpret them, and use them to locate a point, even when the page is furled.

Our ultimate mathematical goal, concerning the geometry of space-time in general relativity, matches closely the question we addressed in the previous lecture of whether there is a real gravitational field or the apparent gravitational field is just due to an artifact of funny space-time coordinates. For instance, in figure 4 of lecture 1, the curvilinear coordinates were due to the accelerated frame we were using, not to tidal forces. The space-time was intrinsically flat. So we want to tackle the mathematical question: Given the metric of a space-time as in equation (1), is the space-time really flat or not? Or, to put it another way, are there tidal forces or not?

The mathematical question is a hard one. It will keep us busy during this lecture and the next.

As said in the introduction, we will first consider the question in a Riemannian geometry, where distance is defined locally and is always positive.

However, before we come to that, we need to get better acquainted with tensors. We began to talk about them in lecture 1. We introduced the basic contravariant and covariant transformation rules. In this lecture, we want to give a more formal presentation of tensors.

Scalars and vectors are special cases of tensors. Now we are interested in the general category of tensors.

Scalar, Vector, and Tensor Fields

For us, tensors are indexed collections of values that depend on coordinate systems. Moreover they transform according to certain rules when we go from one coordinate system to another.

We are going to be interested in spaces such that at every point P of the space - the point P being located by its coordinates X in some system - there may be some physical quantities associated with that point. Such a function, which to each point of a space associates a thing (a scalar, a vector, a tensor, etc.), is called a field (respectively a scalar field, a vector field, and tensor field, etc.). The things or quantities that will interest us will be tensors. There will also be all kinds of quantities that will not be tensors. However we will mostly be interested in tensor fields.

The simplest kind of tensor field is a scalar field S(X). It is a function that to every point in space associates a number, and everybody, no matter what coordinate system they use, agrees on the value of that scalar. So the transformation property in going, let’s say, from the Xm coordinates to the Ym coordinates is simply that the value of S at a given point P doesn’t change.

We could use extremely cumbersome notations to express this fact in the most unambiguous way. But we will simply denote it s'(r) = s(X) (2). The right-hand side and the left-hand side denote the value of the same field at the same point P, one in the V-system, the other in the X-system. The multidimensional quantity Y is the coordinates of P in the V-system, while X is the coordinates of P in the X-system. For convenience, we add a prime to S when we talk of its value at P using the K-coordinates. We saw in lecture 1 that sometimes we do without the prime sign (for instance, when we invoked the chain rule), but here we will keep it for the sake of clarity. With practice, equation (2) will become clear and unambiguous.

Remember that not all functions mapping the space onto the real numbers are scalar fields. They must also not change under a change of coordinates. For instance, when looking at a vector field in some coordinate system, if we decided to look only at its first component, it would not be a scalar field.

Let’s represent, on a two-dimensional surface, the X coordinate system. Now, to avoid confusion, let’s not embed the surface in any larger Euclidean space. But it can be truly curved.

Any point P of the surface can be located knowing the values of its two coordinates X1 and X2 in the X-system. Pay attention to the fact that we placed the indices of the coordinates upstairs, in other words, for the time being, we use superscripts.

Of course, we could think of a higher-dimensional space. There would then be more coordinates. Globally, we denote them Xm.

Now on the same space, there could be another coordinate system, a V-system, to locate points, as shown in figure 3. In our figure, the point P has coordinates (2, 2) in the X-system and (5, 3) in the V-system. Of course, these coordinates don’t have to be integers. They can take their values in the set of real numbers.

What is important to note is that at any point P, there are two collections of coordinates: X™ and Ym. The Xm and Ym are related. At any point P, each coordinate Xm is a function of all the Ym. And conversely. We write it this way: Xm = Xm(Y) (3a), ym = Y™(X) (3b). Equation (3a) is a coordinate transformation, and equation (3b) is its inverse. They can be pretty complicated, as long as they are one-to-one. We will also assume that the functions defined by equations (3a) and (3b) are continuous, and that we can differentiate them when need be, but nothing more.

Scalar fields transform trivially. If you know the value of S at a point P, you know it no matter what coordinate system you use.

Next are vectors. For us they come in two flavors. There are contravariant vectors, which we denote with an upstairs index Vm. And there are covariant vectors, which we denote with a downstairs index Vm. We spoke about them in the last lecture. Now we are going to delve deeper into their geometrical interpretation. What does it mean intuitively to be contravariant or to be covariant?

Geometric Interpretation of Contravariant and Covariant Components of a Vector

In this section and the mathematical interlude that follows, in order to distinguish as clearly as possible vectors from numbers, we shall use boldface for vectors and normal-face for numbers. In the subsequent sections on tensor mathematics and the following, however, we will revert to normal-face for everything. Even though boldface for vectors has advantages, it comes at the price of more cluttered equations. And equations of general relativity are already complicated enough!

Let’s consider a coordinate system, and draw its axes as straight lines because we are not interested at the moment in the fact that the coordinates may be curved and may vary in direction from place to place. We could also think of them locally, where every manifold is approximately flat (a smooth surface, locally, is like a plane) and every coordinate system is formed of approximately straight lines, or surfaces if we are in more than two dimensions.

We are mostly concerned with the fact that the coordinate axes may not be perpendicular, and with the implications of that non-perpendicularity of these coordinates. Furthermore the distance between two axes, say X1 = 0 and X1 = 1, is not necessarily 1. The values of the coordinates are just numerical labels, which don’t directly refer to distances.

Now let’s introduce some ordinary vectors pointing along the coordinates axes. On our two-dimensional surface, we introduce two vectors, ei and 62, as shown in figure 4.

If we had three dimensions, there would be a third vector 63 sticking out of the page, possibly slanted. We can label these vectors Ci. As the index i goes from 1 to the number of dimensions, the geometric vectors e;’s correspond to the various directions of the coordinate system.

Next in our geometric explanation of contravariant and covariant components of vectors, we consider an arbitrary ordinary vector V; see figure 5.

We have known since high school that the vector V can be expanded into a linear combination of the e;’s: v = V1^ + V2e2 + V3e3 (4). On the right-hand side of this formula, the quantities that are vectors are the e^s. The Vx’s are just a collection of numbers. As we explained in lecture 1, they are the contravariant components of the vector V in the ez basis.

In summary, the contravariant components are the expansion coefficients of V, i.e., the numbers that we have to put in front of the three vectors ei, 62, and 63 to express a given vector as a sum of vectors colinear to those of the basis. This jibes with what we have said previously: the most usual vectors (used for position, translation, velocity, etc.) are contravariant vectors.

Earlier, I said that in Riemannian geometry a vector is just a vector - neither contravariant nor covariant - but that it has contravariant and covariant components. Our next job is to understand what the covariant components of the same vector V mean.

To take a peep into what’s coming: to the vector V, we will attach another collection of numbers, this time denoted Vj’s. They won’t be the numbers to put in front of the units vectors ei and 62 to construct a linear combination equal to V. They will be other thing But first, a short interlude.

Mathematical Interlude: Dot Product of Two Vectors

Let’s recall the elementary concept of the dot product between two vectors. I will keep it simple, assuming that you have seen it before (for instance, on page 27 of volume 1 of TTM).

Given any two vectors V and W, their dot product is defined as follows: V · W = |V| |W| cosθ (5)

where |V| and |W| stand for the lengths of the vectors V and W, and θ is the angle between the two vectors. For example, if V and W are pointing in the same direction (θ = 0), then the dot product is just the product of their lengths. If on the other hand they point in opposite directions (θ = π), then the dot product is minus the product of their lengths. If V and W are orthogonal (θ = π/2), their dot product is zero.

If we have an orthonormal basis at our disposal, then if V has the components V1, V2, ..., VN in that basis and W has the components W1, W2, ..., WN, where N is the dimension of the space, we know that the dot product also has the simple expression V · W = V1W1 + V2W2 + ... + VNWN (6)

Exercise 1: Prove that, in an orthonormal basis, equation (5) is equivalent to equation (6).

Hint: Do it in two dimensions. Then - it is slightly more involved - we encourage you to try to do it in any dimension.

End of interlude.

We shall consider the dot products of V with the ei’s. Note that (V · ei) is a number, whereas ei is a vector. For that reason the dot product is also called the scalar product.

By definition, the numbers (V · e1), (V · e2), ..., (V · eN) are called the covariant components of the vector V. We denote them with subscripts: Vi = V · ei (7)

Andy: Hey Lenny, when I went to high school and learned about vectors, the teacher never said covariant or contravariant components. Just plain old components. What gives?

Lenny: Yeah, that’s because the teacher was using ordinary Cartesian coordinates. I’ll explain:

Cartesian coordinates are perpendicular to each other, and the ei’s are unit vectors. In that case the contravariant and covariant components are exactly the same. But if the coordinates are more general - for example, if they intersect at peculiar angles - then they won’t be the same at all.

Andy: This is crazy, Lenny. Why don’t we just use the good old high school Cartesian coordinates and avoid all this complexity?

Lenny: Good question. You tell me.

Andy: Oh yeah, I forgot. In curved spaces there are no Cartesian coordinates.

Lenny: Yup.

Let’s see how we can relate the contravariant components and the covariant components Vn. To reach that goal, we take the dot product of each side of equation (4) with en. This yields V · en = Vmem · en (8)

The left-hand side, V · en, is what we just defined as Vn. But the quantities em · en are something new. Note that they have two lower indices, which might lead us to expect that they are the components of a tensor of some sort. In fact, we will see that em · en turns out to be the metric tensor, expressed in the ei’s basis.

Pay attention also to the fact that on the right-hand side of equation (8) there is a sum to be done. The index m is a dummy index, to be summed over. This simplification of our work on vectors and their various components is a nice aftereffect of the summation convention.

Let’s see how this connection between em · en and the metric tensor comes about.

The squared length of a vector is the dot product of the vector with itself. Let’s calculate the length of V. Using twice equation (4) we write (for the squared length)

V · V = Vmem · Vnen (9)

We must use two different indices m and n. Indeed, recall that, in the implicit summation formula Vmem, the symbol m is only a dummy index. So in order not to mix things up, we use another dummy index n for the second expression of V. If you are not yet totally at ease with Einstein summation convention, remember that, written explicitly, the right-hand side of equation (9) means nothing more than (V1e1 + V2e2 + V3e3) · (V1e1 + V2e2 + V3e3)

But now, using the distributive property of the dot product, the right-hand side of equation (9) can be reorganized as V · V = VmVn(em · en) (10)

The quantity em · en we call gmn. So equation (10) becomes V · V = VmVngmn (11)

This is exactly what the metric tensor is supposed to do; namely it tells us how to compute the square of the length - and therefore the length - of a vector. The vector could be, for instance, a small displacement dX.

In the following, in order not to clutter notations, we won’t use boldface to denote vectors when we talk about dX’s. And eventually, beginning with the next section, “Tensor Mathematics,” we will altogether get rid of boldface for vectors.

In the case of a vector dX, equation (11) would be the computation of the square of the length of a little interval between two neighboring points dX · dX = dXmdXngmn which is written more customarily dX · dX = gmn dXmdXn (12)

We now have a better understanding of the difference between covariant and contravariant indices, that is to say the covariant and contravariant components of a vector: Contravariant components are the coefficients we use to construct a vector V out of the basis vectors. Covariant components are the dot products of V with the basis vectors.

The two types of components describe different geometric things. They would, however, be the same if we were speaking of ordinary Cartesian coordinates - meaning by that a basis made of vectors mutually orthogonal and each of unit length.

We inserted that discussion in order to give the reader some geometric idea of what covariant and contravariant mean and also what the metric tensor is. For a given collection of basis vectors ei’s and a given vector V, we summarize all this in the next box.

We shall also include another important formula.

There is indeed a very important equation relating the contravariant components of a vector with its covariant components. It uses the metric tensor gmn. The relation is Vn = gnmV^m (13)

We leave it to the reader to prove this. We will also meet the relation in the other direction with the help of the twice contravariant form of the metric, namely the tensor gn m. But this, we will see later.

For the time being, let’s recapitulate the important relations we established.

V = Vm em Vn = V · en gmn = em · en Vn = gnmV^m

These relations are essential. We will make frequent use of them in the construction of the theory of general relativity.

Let’s just make one more comment about the case when the coordinates axes are Cartesian coordinates from an orthonormal basis. Then, as we saw, the contravariant and the covariant components of V are the same, and the metric tensor is the unit matrix. Let’s stress that this means that the basis vectors are perpendicular and of unit length.

Indeed, they could be orthogonal without being of unit length. In polar coordinates (see figure 14 of lecture 1), the basis vectors at any point P on the sphere are orthogonal, but they are not all of unit length. The longitudinal basis vector has a length that depends on the latitude. We have to use a coefficient equal to the cosine of the latitude. That is why, on the sphere of radius one, to compute the square of the length of an element dS, we can use Pythagoras theorem, but we must add dθ2 + cos2θ dφ2 (see formula (16) of lecture 1).

We now come to the tensor mathematics that we will need throughout the rest of the book.

Tensor Mathematics

As we have said now several times, and we’ll say it again, tensors are objects that are characterized by the way they transform under coordinate transformations. Let’s just review quickly what we have found, and then go further. The transformation properties of the contravariant and covariant components of a vector were given in equations (24a) and (24b) of lecture 1. I repeat them here, with new labels.

Contravariant components (V')m = Vp ∂Ym/∂Xp (15a)

Covariant components (V')n = Vp ∂Xp/∂Yn (15b)

Let’s go to tensors of higher rank. A tensor of higher rank simply means a tensor with more indices. Again, for the sake of pedagogy and completeness in this second lecture, there is some overlap with what we said at the end of the first lecture.

We start with a tensor of rank 2, with one contravariant index and one covariant index. It is a mathematical “thing” represented in a given basis by a collection of numbers.4 These numbers are indexed with two indices. Furthermore in another basis the same “thing” is represented by another collection of numbers and the two collections satisfy specific transformation rules related to the relationship between the two bases. Let’s consider the tensor in a Y basis, that is to say, a Y-coordinate system. We denote it (T')m n.

The simplest example of such a thing would be the outer product of two vectors, one with a contravariant index and one with a covariant index. By “outer product of the vectors” we mean the collection of all the products of components.5 What makes the thing a tensor is its transformation property. So let’s write it (T')m n = (W')m (V')n = (∂Ym/∂Xp Wp) (∂Xq/∂Yn Vq) (16)

This tells us how a tensor of rank 2, with one contravariant and one covariant index, transforms. For each index on the left-hand side, there must be a ∂Y/∂X or a ∂X/∂Y on the right-hand side. You simply track where the indices go.

Let’s do another example of a tensor of rank 2 with two covariant indices: (T')mn How does it transform? By now you should begin to be able to write it mechanically (T')mn = ∂Xp/∂Ym ∂Xq/∂Yn Tpq (17)

These rules are very general. If you take a tensor with any number of indices, the pattern is always the same. To express the transformation rules from an unprimed system X to a primed system Y, you introduce partial derivatives, in one sense or the other as we did, on the right-hand side, and you sum over repeated indices.

4 A tensor does have a geometric re presentation that by definition doesn't depend on the basis used. But in this course, we won't spend much time on this aspect of tensors. For us, in general relativity, it is the transformation properties of their components that are essential.

The outer product is sometimes called the tensor product.

Notice one important property of tensors. If they are zero in one frame, they are necessarily zero in any frame. This is obvious for scalars: if a scalar is 0 in one frame, it is 0 in every frame, because its value depends only on the geometric point where it is measured, not the coordinates of that point. Now suppose a vector V is zero in some frame, let's say the X-frame. To say that V is zero doesn't mean that some component is equal to zero, it means all of its components are zero. Equation (15a) or equation (15b) then show that they are all going to be zero in any frame. Likewise with any tensor, if all of its components are null in one frame, that is, in one coordinate system, then all of its components are null in every frame.

That has an important and very useful consequence: once we have written down an equation equating two tensors in one frame, for instance T^{plmn} = T_{plmn} + U^{pqr}V_{pqr} it can be rewritten as T^{plmn} = T_{plmn} + U^{pqr}V_{pqr} Thus, considering that T — U is still a tensor (see the next section, "Tensor Algebra"), we see that if two tensors are equal in one frame, they are equal in any frame.

That is the basic value of tensors. They allow you to express equations of various kinds, equations of motion, equations of whatever you are working on, in a form where the same exact equation will be true in any coordinate system. That is of course a deep advantage to thinking about tensors.

We will also meet and use extensively other objects that will not be tensors. Unfortunately it will be possible for them to be zero in some frames and not zero in other frames. This will make life a bit more complicated for us, but we will see how to deal with it.

Tensors have a certain invariance to them. Their components are not invariant. They change from one frame to another. But the statement that a tensor is equal to another tensor is frame-independent. Incidentally, when you write a tensor equation, the components have to match. It doesn't make sense to write an equation like W_p, where p is contravariant and q covariant, equals T_{pq}, where both indices are contravariant. Of course, you can write whatever you like, but if, let's say in one coordinate system, the equation W_p = T_{pq} happened to be true (for all pairs p, q, these are only numbers after all, so it is not meaningless), then it would usually not be true in another. So normally we wouldn't write equations like that.

One more point concerning vectors and higher-rank tensors: in Euclidean geometry, or in non-Euclidean geometry with a positive definite distance, for V = W to be true, it is necessary and sufficient that the magnitude of V — W be equal to zero.

But this statement is not true in the Minkowski geometry of relativity, where the proper distance between two events may be zero without them being the same event. The magnitude of a vector and the vector itself are two different things. The magnitude of a vector is a scalar, whereas the vector is a complex object. It has components. It points in a direction. To say that two vectors are equal means that their magnitudes are the same and their directions are the same. A tensor of higher rank is yet a more complicated object, which points in several directions. It has some aspect of it that points in one direction and some aspects that point in other directions. We will talk a bit about their geometry. But for the moment we define them by their transformation properties.

The next topic in tensor mathematics is operations on tensors. It usually bears the specific name of tensor algebra.

Tensor Algebra

What can we do with tensors that will produce new tensors? We are not interested at this point in operations we can do with tensors that produce other kinds of objects that are not tensors. We are interested in the operations we can do with tensors that will produce new tensors. That way we will be able to build equations having the very useful feature that they are frame-independent.

First of all we can multiply a tensor by a number. The result will still be a tensor. That rule is obvious and we don't need to spend time on it.

We shall examine three additional algebraic operations.

1. Addition of tensors. We can add two tensors of the same type, that is, of the same rank and the same numbers of contravariant and covariant indices. Addition of course also includes subtraction. If you multiply a tensor by a negative number and then add it, you are doing a subtraction.

2. Multiplication of tensors. We can multiply any pair of tensors to make another tensor.

3. Contraction of a tensor. From certain tensors we can produce tensors of lower rank.

Adding tensors. You only add tensors if their indices match and are of the same kind. For example, if you have a tensor T = T_{m...}^n... with a collection of upstairs contravariant indices and a collection of downstairs covariant indices, and you have another tensor of the same kind S = S_{m...}^n..., in other words their indices match exactly, then you are allowed to add them and construct a new tensor, which we can denote T + S. It is constructed in the obvious way: each component of the sum (T + S)_{m...}^n... is just the sum of the corresponding components of T and S. It is obvious too to check that T + S transforms as a tensor with the same rules as T and S. The same is true of T — S. It is a tensor. This is the basis for saying that tensor equations are the same in every reference frame, because T — S = 0 is a tensor equation.

Multiplication of tensors. Unlike addition, multiplication of tensors can be done with tensors of different rank and type. The rank of a tensor is its number of indices. We know that the two types, for each index, are contravariant or covariant. We can multiply T_{lmn} by S_{pq}. The tensor multiplication being not much more than the multiplication of components and of the number of indices, we will get a tensor of the form P_{lpqn}.

Let's see again the simple example we already met: the tensor multiplication, also called tensor product, of two vectors. Suppose V^m is a vector with a contravariant index. Let's multiply it by a vector W_n with a covariant index. This produces a tensor with one upstairs index m and one downstairs index n: V^m W_n = T^m_n (18)

A tensor is a set of values indexed by zero (in the case of a scalar), one (in the case of a vector), or several indices. This tensor T of equation (18) is a set of values (which, as we said many times, depend on the coordinate system in which we look at it) indexed by two indices m and n, respectively of contravariant and covariant type. It is a tensor of rank 2, contravariant in one index and covariant in the other.

We could have done the multiplication with some other vector X_n. This would have produced some other tensor: V^m X_n = U^m_n (19)

The tensor product is sometimes denoted with the sign ⊗. Equations (18) and (19) would then be written as V^m ⊗ W_n = T^m_n V^m ⊗ X_n = U^m_n

In this book we denote the tensor product by just writing the tensors next to each other.

The tensor product of two vectors generalizes to the product of any tensors. We produce a tensor of higher rank by just juxtaposing somehow all the components of the multiplicands.

How many components does V^m X_n have? Since we are going to work mostly with 4-vectors in space-time, let's take V and X to be both 4-vectors. Each is a tensor of rank 1 with a contravariant index. Their tensor product U is a tensor of rank 2. It has 16 independent components, each of which is the ordinary multiplication of two numbers: U^11 = V^1 X^1, U^12 = V^1 X^2, U^13 = V^1 X^3, ...

... U^43 = V^4 X^3, U^44 = V^4 X^4

Observe that the tensor product of two vectors is not their dot product. We will see how the dot product of two vectors is related to tensor algebra in a moment. The dot product has only one component, not 16, and you might suspect that it is a scalar. You'd be right. It is a frame-independent number.

Typically the tensor product of two tensors is a tensor of different rank than either one of the multiplicands. The only way you can make a tensor of the same rank is for one of the factors to be a scalar. A scalar is a tensor of rank 0. You can always multiply a tensor by a scalar. Take any scalar S and multiply it by, say, V^m. You get another tensor of rank 1, i.e., another vector. It is simply V elongated by the value of S. But generally you get back a tensor of higher rank with more indices obviously.

Contraction. Contraction is also an easy algebraic process. But in order to prove that the contraction of a tensor leads to a tensor, we need a small theorem. No mathematician would call it a theorem. They would at most call it a lemma. Here is what the lemma says. Consider the following quantity:6 ∂X^b / ∂Y^m * ∂Y^m / ∂X^a Remember that the presence of m upstairs and downstairs means implicitly that there is a sum to be performed over m. Expression (20) is the same as ∂X^b / ∂Y^m * ∂Y^m / ∂X^a

6 We begin to use also letters a, b, c, etc. for indices because there just aren't enough letters in the m range or the p range for our needs.

What is the object in expression (20) or (21)? Do you recognize what it is? It is the change in X^b when we change Y^m a little bit, times the change in Y^m when you change X^a a little bit, summed over m. That is, we change Y^1 a little bit, then we change Y^2 a little bit, etc. What is expression (21) supposed to be?

Let's go over it in detail. Instead of X^b, consider any function F. Suppose F depends on (Y^1, Y^2, ..., Y^M) and each Y^m depends on X^a. Then, from elementary calculus, the quantity ∂F / ∂Y^m * ∂Y^m / ∂X^a is nothing more than the partial derivative derivative of F with respect to Xα (partial because there can be other Xn,s on which the Ym,s depend). That is ∂F/∂Xα = (∂Ym/∂Xα) (∂F/∂Ym)

What if F happens to be Xb? Well, there is nothing special in the formulas. We get ∂Xb/∂Xα = (∂Ym/∂Xα) (∂Xb/∂Ym)

What is ∂Xb/∂Xα? It looks trivial. The Xn’s are independent variables, so the partial derivative of one with respect to another is either 1, if they are the same, or 0 otherwise. So ∂Xb/∂Xα is the Kronecker-delta symbol. We shall denote it δ^b_α. Notice that we use an upper index and a lower index. We shall find out that δ^b_α itself also happens to be a tensor. That is a little weird because it is just a set of numbers. But it is a tensor with one contravariant and one covariant index.

Now that we have spelled out the little lemma we need in order to understand index contraction, let’s do an example. Then we’ll define contraction more generally.

Consider a tensor built out of two vectors, one with a contravariant index and the other with a covariant index: T^mn = V^m W^n (22)

What contraction means is: take any upper index and any lower index and set them to be the same and sum over them. In other words, take V^m W_m (23)

Expression (23) means V^1 W_1 + V^2 W_2 + V^3 W_3 + ... + V^M W_M, if M is the dimension of the space we are working with. We have identified an upper index with a lower index. We are not allowed to do this with two upper indices, nor with two lower indices. But we can take an upper index and a lower index. Let’s see how expression (23) transforms. For that, look at the transformation rule applied first to expression (22). We already know that it is a tensor. Here is how it transforms: (T^mn)' = (∂y^m/∂x^p) (∂y^n/∂x^q) T^pq (24)

Equation (24) is the transformation property of the tensor T^mn, which has one index upstairs and one index downstairs.

Now let m = n and contract the indices by identifying the upper and the lower index and sum over them. On the left-hand side we get (V^m W_m)' How many indices does it have? Zero. So the contraction of T^mn did create another tensor, namely a scalar.

We can check what equation (24) says. It should confirm that (V^m W_m)' is the same as V^m W_m. Now our little lemma comes in handy. On the right-hand side of (24), when we set m = n and sum over m, the sum of the products of partial derivatives is δ^p_q.

So the right-hand side is V^p W_p. But p or m are only dummy indices, therefore equation (24) says indeed that (V^m W_m)' = V^m W_m

It is easy to prove, and the reader is encouraged to do it, that if you take any tensor with a bunch of indices, any number of indices upstairs and downstairs, T^{...}_{...} (25)

and you contract a pair of them (one contravariant and one covariant), say r and q, you get T^{...r...}_{...r...} (26)

where the expression implicitly means a sum of components over r, and this is a new tensor.

Notice that the tensor of expression (25) has six indices, whereas the tensor of expression (26) has only four.

Notice also two more things: 1. If we looked at V_m W_n, we would be dealing with a tensor that cannot be contracted. The analog of equation (24) would involve ∂y_m/∂x^p ∂y_n/∂x^q This quantity doesn’t become the Kronecker-delta when we set m = n and sum over it. The sum (V_m)' (W^n)' would not be equal to V^m W_m.

2. The dot product of two vectors V and W is the contraction of the tensor V^m W_n. But in that case one vector must have a contravariant index, and the other a covariant index.

In other words, contraction is the generalization of the dot product, also called inner product, of two vectors. We are going to deal with inner products as soon as we work again with the metric tensor.

More on the Metric Tensor Of all the tensors in Riemannian geometry, the metric tensor is the most important. In equations (14) we described its construction in terms of the basis vectors e_m’s: g_{mn} = e_m · e_n Let’s now define it on its own terms abstractly. These are things we have already covered before, but let’s do them again now that we have more practice with tensors.

To define the metric tensor, consider a differential element dX^m that represents the components of a displacement vector dX located at a point P as in figure 6. And we consider an infinitesimal displacement, which we call dX.

The contravariant components of dX are the coefficients of the vector dX in the expansion given by equation (4). In the case of three dimensions, dX = dX^1 e_1 + dX^2 e_2 + dX^3 e_3 (27)

What is the length of that displacement vector? To answer that, we need to know more about the geometry - in particular we need to know the metric tensor g_{mn}(X) and how it varies from place to place. Writing the length of dX as dS, the generalization of the Pythagoras theorem is dS^2 = g_{mn}(X) dX^m dX^n (28)

Mathematical Interlude: The Metric is a Symmetric Tensor Any rank-2 tensor - let’s call it T - can be written as a sum of a symmetric tensor and an antisymmetric tensor, T_{mn} = S_{mn} + A_{mn} where the symmetric part satisfies S_{mn} = S_{nm} and the antisymmetric part satisfies A_{mn} = -A_{nm} It follows that dS^2 = S_{mn} dX^m dX^n + A_{mn} dX^m dX^n Notice that because A is antisymmetric, the second term will always be zero. Thus without any loss of generality, we may assume that the metric tensor is symmetric: g_{mn} = g_{nm} The metric, like any other rank-2 tensor, can be displayed as a matrix with N^2 components. For example, if the space is four-dimensional, the metric would be a 4 x 4 matrix with 16 components, but because it is symmetric there are only 10 independent components, as shown in figure 7.

Similarly in a three-dimensional space there would be six independent components in g_{mn}. In two dimensions there would be three.

End of interlude

So far we haven’t proved that g_{mn} is a tensor. I called it the metric tensor, but let’s now prove that it is indeed such an object. The basic guiding principle is that the length of a vector is a scalar, and that everybody agrees on that length. People using different coordinate systems won’t agree on the components of dX (see figure 6), but they will agree on its length. Let’s write again the length of dX, or rather its square: dS^2 = g_{mn}(X) dX^m dX^n (29)

Now let’s go from the X-coordinates to the y-coordinates. Because dS^2 is invariant, the following holds: g_{mn}(X) dX^m dX^n = g_{pq}(Y) dY^p dY^q (30)

Then let’s use this elementary calculus fact: dX^m = (∂x^m/∂y^p) dY^p (31)

Plug expression (31) for dX^m and for dX^n into (30). We get g_{mn}(X) (∂x^m/∂y^p) (∂x^n/∂y^q) dY^p dY^q = g_{pq}(Y) dY^p dY^q (32)

The two sides of equation (32) are expressions of the same quadratic form in the dY^p’s. That can only be true if the coefficients are the same. Therefore we have established the following transformation property: g_{pq}(Y) = (∂x^m/∂y^p) (∂x^n/∂y^q) g_{mn}(X) (33)

This is precisely the transformation property of a tensor with two covariant indices. So we discovered that the metric tensor is indeed really a tensor. It transforms as a tensor. This will have numerous applications.

The metric tensor has two lower indices because it multiplies the differential displacements dX^m’s in equation (29), which have upper indices.

The metric tensor can also be viewed as a matrix with m n indices. Remembering that g_{ij} = g_{ji}, it is the following matrix, which we still denote g_{mn}, [ g_{11} g_{12} g_{13} g_{14} ]

[ g_{12} g_{22} g_{23} g_{24} ]

[ g_{13} g_{23} g_{33} g_{34} ]

[ g_{14} g_{24} g_{34} g_{44} ]

It is a symmetric matrix.

There is one more fact about this matrix, that is, about the tensor thought of as a matrix. It has eigenvalues. These eigenvalues are positive and never zero.

The reason that the eigenvalues are never zero is because a zero eigenvalue would correspond to an eigenvector of length zero. But there is no vector of length zero (unless of course its components are all zero). In Riemannian geometry every direction has a positive length associated with it.

The Matrix Inverse of the Metric What do we know about matrices that are symmetric and whose eigenvalues are all nonzero? Answer: they have inverses. The matrix of the metric tensor - denoted g for simplicity - has an inverse g^{-1} whose components are themselves the components of a tensor, albeit with contravariant elements. The components of g^{-1} are written g^{mn}.

In matrix terms the product of the matrices g and g^{-1} is the identity matrix. This is represented by the formal equation g^{-1} g = the unit matrix In terms of components, it takes the form g_{mp} g^{pn} = δ_m^n (34)

where δ_m^n is the identity matrix.

Equation (34) is the definition of the matrix inverse, but it is also a tensor equation. We’ve already seen that the Kronecker-delta δ_m^n is a tensor with one lower and one upper index. That’s enough to prove that g^{pn} is a tensor with two upper indices.

In fact the three tensors g_{mn}, g^{mn}, and δ_m^n are really just a single tensor written in three forms - the first with two covariant indices, the second with two contravariant indices, and the third with a covariant and a contravariant index.

The fact that there is a metric tensor with downstairs indices and a metric tensor with upstairs indices will play an important role.

So far everything we have seen on tensors was easy. It is essentially learning and getting accustomed to the notation.

This lecture was about tensor algebra. The next lecture deals with tensor calculus: in particular with the dark art of parallel transporting tensors, differentiating tensors, and most importantly building a curvature tensor from the derivatives.

It is the curvature tensor that will tell us if a geometry is flat or curved, and in general relativity whether a gravitational field exerts tidal forces. Similarly, we saw that a rank-1 tensor, i.e., what we called in lecture 1 an abstract vector, has a contravariant form and a covariant form.

Lecture 3: Flatness and Curvature

Lenny: Today, we shall study the difference between flat space and non-flat space.

Andy: I guess I know: we can always tile a plane with an infinite number of identical flat square tiles. And that’s unrelated to the fact that we may, for some reason, use curvilinear coordinates. But we cannot tile in such a way the surface of the Earth.

Lenny: That’s exactly right.

Andy: But the 3D space, we can always fill with identical cubes! I remember from my kindergarten days.

Lenny: Only locally. Globally, we’re not sure what’s the shape of the universe. We will talk about it in the next volume.

Andy: Oh, I get it. It’s like: Think globally, act locally.

Lenny: Sort of. This is the kind of gentle answer one makes to a suggestion that bears no relation to the subject. :-)

Introduction General relativity in modern physics Riemannian geometry Gaussian normal coordinates Covariant derivatives Christoffel symbols Curvature tensor

Introduction

General relativity has a reputation for being very difficult. I think the reason is that it is very difficult. It is calculation-intensive: symbols, indices, awe-inspiring equations. There are ways people have invented to express things in more condensed notations, but just learning them in itself is a task. Things like vierbeins, forms, spinors, and twistors and all sorts of other mathematical objects. You could call many of them just notational devices if you like. And they do simplify the equations. So I sometimes feel that in presenting these things the way I do, it is sort of like Maxwell¹ who wrote down every single equation of his set of Maxwell equations. At first he wrote twenty altogether. Now we write only four. We don’t usually write all components of the equations. We put them together into vector notation and so forth. If we are smart, we can even avoid the indices by inventing symbols like del, curl, or Laplacian. The same thing could be done to some extent for general relativity. But in the end the computational techniques are unquestionably harder.

I will tend to downplay the computational side of things and concentrate on the principles. If you are really interested in doing the computations in general relativity, there are packages. You just put in the metric as a function of position, and the computer will spit out the various tensors that you ask it for: Riemann tensors, Ricci tensors, Einstein tensors, this kind of tensor, that kind of tensor. Then you can say, without even looking at the results: “Okay, please Mr. Computer, set the Einstein tensor equal to the energy momentum tensor and tell me what comes out.” So, yes, computers can do a lot better than us.

General Relativity in Modern Physics

When I was a young physicist in the 1960s, general relativity was a bit of a backwater in theoretical physics. Partly this was because the technology for detecting the subtle non-Newtonian effects mostly did not yet exist. But also physicists like myself, who were interested in the fundamental aspects of the subject, had other fish to fry. Elementary particle physics - both theoretical and experimental - was in its golden age with new discoveries almost every year.

Things have changed since then. New technologies allowed new experiments and astronomical observations, which finally cleared any doubt about the correctness and importance of general relativity. It became clear that Einstein’s theory was absolutely central to cosmology - the study of the origin and structure of the universe. Black holes were discovered at the centers of galaxies. It became urgent to have computational tools to numerically solve the equations of general relativity. That entailed a deeper understanding of those equations. The field of numerical relativity was born and flourished.

On a more theoretical side, string theory, which was originally designed to understand particle physics, provided new and powerful tools for analyzing gravity. Perhaps even more important were the clashes that were being discovered between quantum mechanics and general relativity. By the year 2000 there was no alternative: the dominant question for theoretical physicists was to understand how quantum physics and general relativity could be reconciled, or even unified.

There was more. One of the big surprises for me was the way the theoretical tools of gravity and quantum gravity found application to other fields, including condensed matter physics and quantum computer science. In short, general relativity is no longer a backwater. It is the mainstream.

Riemannian Geometry

This is the last lecture in which we will be studying Riemannian geometry as such, without really discussing gravity. In the next lecture we will really get into gravity. What do all these manipulations of tensors have to do with gravity? We already had a glimpse of the answer in the first lecture.

The problem of finding out whether there is a real gravitational field, as opposed to just some artifact of curvy coordinates, is mathematically identical to the problem of finding out if a certain geometry - characterized by its metric tensor - is flat or not. Let’s think of a two-dimensional space or “manifold” to begin with. That means a surface S where each point is located with two real coordinates X1 and X2, see figure 12 of lecture 1, where it is shown embedded in the usual 3D space for convenience.

We assume that S has a metric that defines infinitesimal lengths, the squares of which are given by dS2 = gmn(X) dXm dXn (1)

where m and n run over the indices {1, 2}.

A flat geometry is one for which all Euclid’s axioms, including the famous fifth one called Euclid’s postulate, are correct.² There are points, lines, parallel lines, distances, right angles, etc., all the stuff we learned in high school that is called Euclidean geometry. Moreover, the surface S - if we think of it embedded in 3D - is not necessarily a plane, but can be laid out on a plane without imposing any distortion, stretching, or compression, on its intrinsic geometry. Such surfaces in 3D are called developable. Cylinders and cones are examples.

A flat geometry is one where we can find another system of coordinates Y such that at any point P, now located by those Y-coordinates, the metric has a simple form ds2 = (dr1)2 + (dy2)2 (2)

Such a transformation is always possible locally at any given point P, because locally any smooth surface is like a plane. But it is not always possible to find such a transformation globally over the whole surface. In other words, given an arbitrary metric tensor that varies from place to place - assuming it is smooth and has all the good differential properties - finding such coordinates doesn’t always have a solution. And determining whether there exists one or not is in general a difficult problem.

The bad way to approach it is to search through all possible coordinate systems Y and see whether the transformed metric is the Kronecker matrix. This would take an infinite amount of time. We need a better technique. The better technique is to search for a diagnostic quantity, built out of the metric and its derivatives, that we, or the computer, can calculate. If it is zero everywhere, then the space is flat. If it is nonzero at some location, this will tell us that the space shows some curvature there.

In the two-dimensional case, the diagnostic quantity that does the job is called the Gaussian curvature. More generally in higher dimensions, it is the curvature tensor. It’s a bit of a slog, but it’s worth the effort. Once we have mastered the curvature tensor, we have a very powerful tool, both for pure geometry and for understanding gravity.

What do we start with? We start with a space. And a space means, first of all, a number of dimensions. In Riemannian geometry the number of dimensions can be any positive integer. In principle you can even have a zero-dimensional space, but that is just a point! There isn’t much to be said about the geometry of a point. So let’s go to the next number of dimensions.

Andy: Lenny, you don’t seem to be well-versed in Leibniz’s monads.³ Actually a space consisting of only one point is fascinating! :-)

Lenny: Evidently Leibniz thought so - Newton not so much. :-(

A one-dimensional space is either an infinite line or a closed curve - that is, a loop. If it is a closed curve, what is it intrinsically characterized by? One thing and only one: the total length of the curve. Every loop is equivalent to every other loop of the same length. In other words - just think about it for a moment - take a piece of rope that closes on itself to form a loop and has a certain length. Wiggle it or curve it in any kind of way, it can always still be mapped into or put on top of another piece of rope of exactly the same length. To a one-dimensional bug living on the loop, there is no more - just the length. All the bug can do is count the number of steps it takes to walk around the loop. For instance, the bug might make an initial mark someplace, then go around the loop till it comes back to the mark, and record the number

¹ James Clerk Maxwell (1831-1879), Scottish theoretical physicist.

² It was called a postulate because for 2000 years people thought that it was “really true in reality,” until their epistemology got more sophisticated.

³ Leibniz’s monads didn’t lead to any interesting understanding of the world. One then wonders why he devised such a weird concept. The reason is probably to be found in his invention of integral calculus, which met with fantastic success and rested on infinitesimal quantities. Monads are cousins of t hose. But, if infinitesimals - put on a firm footing in the nineteenth century - turned out to be very useful to this day, monads did not.

of steps that it took. That is the only thing the bug can say, or measure, about the loop.

In short, in one-dimensional spaces, there is no notion of curvature, only a notion of length. The reader might find this strange, because when we drive on a road - a one-dimensional space - there are straight sections and there are turns! That is correct, but one must understand that the notion of turns on a road is meaningful only if we consider the road embedded in a space of at least two dimensions, that is, a plane or surface, or a 3D space, etc.

Two-dimensional spaces are where things start to be more complicated - and more interesting. There are flat ones. And there are curved ones. A flat one is a plane. A curved one could be a sphere. It could be a space with bumps, the surface of the Earth including the mountains and the valleys. It could even have a weird topology, for instance the surface of a donut, also called a torus. You can poke another hole in the torus and make a torus with two holes, and so forth.

Things only get worse as the dimension increases. The sheer variety of different types of spaces in three-, four-, and higher-dimensional spaces is bewildering, but luckily we only need to know about a few simple cases.

Let us come to our main goal of finding a tensor that can distinguish whether a space is flat or curved by whether the tensor is zero or not. Why a tensor? Because flatness does not depend of the choice of coordinates. And tensors, if they are zero in one frame, then they are zero in all frames. The curvature tensor is traditionally denoted R in honor of Riemann. We will see that the curvature tensor is of rank 4, meaning it has four indices.

If an N-dimensional space is flat, we can choose coordinates in which the metric has the form ds² = (dY¹)² + (dY²)² + ... + (dYᴺ)² or, using the Kronecker-delta symbol, ds² = δᵢⱼ dYⁱ dYʲ

To what extent can we force the metric to look like this by a choice of coordinates? In general the best we can do is to make the metric tensor be approximately δᵢⱼ over a small region of space surrounding a point.

Here is a theorem that will be very useful to us: At any given point P in the space, we can find a system of coordinates in which the metric is δₘₙ to first order in small deviations from the point; see figure 1. In general, unless the space is flat, the attempt will fail beyond first order.

Such coordinates are called Gaussian normal coordinates at the point P. Here is how we proceed. We position ourselves at point P and we move along any first direction as straight as we possibly can. Later we will learn what is meant by “as straight as we possibly can”; it will mean along a geodesic. So you make as straight a curve as you can.

Figure 1: Displacement of length ΔS along the surface and along the tangent plane in the same direction. The coordinates are represented on the tangent plane at P. We could have represented them too - slightly curved - on the surface itself.

As an example, suppose that you are a little bug driving a tiny car on a two-dimensional surface. You move along the surface pointing your steering wheel straight ahead. That’s what I mean by “as straight as you can.”

That defines one coordinate axis. Then you come back to point P. You have some surveying tools to figure out which other directions make a right angle with the first line. On a two-dimensional surface there is only one other direction (in one sense or the other). In three dimensions, there is a whole plane. You go off in an orthogonal direction, again as straight as you can. That way you build a complete set of coordinates based on those directions.

The theorem says that at every point P of the surface, you can choose Gaussian normal coordinates such that, at that point whose coordinates are, say, we have gₘₙ = δₘₙ You can do that in more than one way. If you found coordinates for which equation (5) is true, you can obviously rotate the coordinates. This will produce a different set of axes such that equation (5) in the new set is still true. In figure 1, think of pivoting the coordinate system around P.

The theorem says, furthermore, that at point P once you have chosen the directions, you can also choose the X’s such that the derivative of any element of the metric tensor gₘₙ(X) at that point with respect to any direction in space, Xʳ, can be set equal to zero: ∂gₘₙ / ∂Xʳ = 0

The proof is actually very simple. It is just a counting argument. You count how many independent variables you have, and how many constraints they must satisfy.

Equation (6) will be true, at a given point, only for the first derivatives. Unless the space is flat, the derivatives of higher order at that point won’t be zero: ∂²gₘₙ / ∂Xʳ∂Xˢ ≠ 0

So, at a point, there is no content really in saying that the metric can be chosen to be, so to speak, flat-like. Up to the first derivatives included, that can always be done.

It is in the second derivatives of the metric tensor that the flatness or non-flatness of the space somehow starts to show up.

How do we prove it? As said, this is actually not hard. Let’s do it. We set the point of interest, which we called P, of coordinates X₀, to be the origin: X₀ = 0

Now suppose that we have some general metric and some coordinates Y in which the metric has some form that does not satisfy equations (6).

Let’s look for some X’s, which will be functions of the Y’s, and choose them in the following way: at the place where X = 0, in other words at the origin, let’s also assume that Y = 0. So the two sets of coordinates have the same origin. That means that X will start out just equal to Y plus something quadratic in Y: Xᵐ = Yᵐ + Cₘₙᵧ Yⁿ Yᵖ plus some more complicated terms. We are simply expanding each Xᵐ in powers of Y¹, Y², ..., Yᴺ, where N is the number of dimensions of the space.

How many such Cₘₙᵧ are there? Suppose we work in four dimensions. Then there are 10 distinct combinations YⁿYᵖ, because YⁿYᵖ = YᵖYⁿ. For each m and we have four when m runs from 1 to 4. That means there are 40 independent coefficients.

Now how many independent components of g are there? Answer: 10. So there are 40 equations (6). Finally we have reached 40 equations to solve for 40 unknowns. That allows us to be sure, at point P, not only that gₘₙ(X) = δₘₙ, but also that the derivatives of gₘₙ and δₘₙ will match up to quadratic order. It means that we will be able to solve the 40 equations (6), and, moreover, that we will fail to set the left-hand sides of equations (7) equal to zero.

To summarize: at any point P, a smooth space (or surface, or manifold) is locally flat. We can approximate it by its tangent space, as in figure 1. And we can construct coordinates X’s such that P is located at the origin and the metric tensor has the form gₘₙ(X) = δₘₙ + o(X)

where o(X) represents terms of second order and higher. We interpret equation (9) as saying that the metric is locally Euclidean up to second order.

The fact that we cannot generally satisfy the equations to higher order demonstrates that generally spaces are not flat.

Our next goal is to learn to differentiate tensor fields with respect to position, so as to produce new tensors. This is a subtle business that will lead to the very important notion of the covariant derivative of a tensor.

To differentiate a tensor with respect to position, we could think: “Okay. Let’s take the components of the tensor - for instance, contravariant components - and just differentiate them.” That would yield a new collection of components - with one more index - which would be simply the derivatives of the components of the initial tensor. But we would run into a problem. Let’s see what the problem is.

Think for instance of the derivatives of a vector. We could differentiate each component with respect to each direction. We can certainly do that. This would produce a two-dimensional collection of values. But it would not be a tensor. Here is why.

Consider a surface and a point P on it, figure 2. We have two sets of coordinates on the surface, coordinates X and coordinates Y. If the space is flat, for X we just use ordinary flat Cartesian coordinates. Or if the space is curved, we use a set of Gaussian normal coordinates at P, that is, coordinates X that are locally, at P, as straight and orthogonal as possible, as we explained. And there is another set of coordinates Y, for instance the initial ones. For convenience, at P we chose X such that the X²-axis is tangent to the Y²-axis. Remember that we can rotate the Gaussian coordinates that we built so that they suit whatever purpose we have. So it’s not a problem to make the X²-axis parallel to the Y²-axis.

Figure 2: Surface viewed at P with Gaussian normal coordinates X, and arbitrary curvy coordinates Y.

Think of a vector field defined over the surface. The vector field is made of a different vector at every point. In order not to clutter the picture, these vectors are not shown on figure 2 yet. There is one at P and there are plenty around P - one at each point.

Before we ask how to differentiate a vector field, let’s ask what it would mean for the vector field to be constant in space. We run into the following difficulty: because the space is curved, it becomes hard to compare the vector at one point with the vector at another point.

The coordinates X cannot be chosen to be everywhere flat. Then what exactly do we mean by saying that a vector at one poi 一个向量在点P是否等于另一个点Q的向量？这本身没有意义，因为要比较P点的向量和Q点的向量，除非我们在整个曲面上有很好定义的平坦坐标，否则没有唯一的方法。让我们详细看看这一点。

如果空间真的是平坦的，那么我们就知道曲面上一个点P的向量与另一个点Q的向量相同意味着什么；见图3。这意味着它们指向相同的方向并且长度相同。因此在X坐标系中，它们具有相同的分量。

图3：两个相等的向量，在P点和Q点。

它们在Y坐标系中的分量又如何呢？

为了清楚地理解正在发生的事情，让我们考虑一个特例。

假设两个向量在X轴方向上都垂直指向上方；见图4。在这种情况下，Vp在平坦坐标中只有一个X2分量。Vq也是如此。它们在X轴方向上有相同的分量。

Vp和Vq在V坐标系中的分量相同吗？

答案：否。沿着V轴，Vq有一个Y1分量和一个Y2分量，而Vp只有一个Y2分量。

很明显，即使向量Vp和Vq是相同的，它们在Y坐标系中的分量也不相同。

无论是协变分量还是逆变分量，情况都会是这样：当我们在曲线坐标系中时，我们不容易判断两个相隔点的向量是否相等。

此外，更糟糕的是——或者说更有趣的是——在弯曲空间中只有曲线坐标。

图4：两个相等的垂直向量，在P点和Q点。（我们表示了Y轴坐标网格在P点附近的一部分，但没有表示X轴坐标。在X轴坐标中，网格近似于欧几里得几何中的矩形。）

另一种表达相同意思的方式是，向量V的第m个分量对坐标系的第r个方向的导数，在一个坐标系中可能为零，而在另一个坐标系中可能不为零： 它甚至可能像图3或图4那样，在一个坐标系中Vm的所有导数都为零，而在另一个坐标系中不为零。这将是因为坐标的变换，而不是因为向量本身在变化。

你明白我们的意思了：表示向量的所有导数都等于零的方程在一个参考系中可能成立，但在另一个参考系中不成立。因此它不能是一个张量方程。让我们强调这一事实： 向量分量的普通导数本身不构成一个张量。

如果它们是张量的分量，我们会将这个量视为一个具有m指标和r指标的2阶张量。但如果它是一个张量，以下事实必须成立：如果Tmr在一个参考系或一个坐标系中为零，那么它在每个坐标系中都为零。然而，对于这个Tmr来说，这并不成立——不是因为向量可能从一点变化到另一点，而是如我们所说明的，因为坐标的方向发生了变化。

我们需要一个比简单微分其分量更好的向量导数定义。我们需要某种在某个参考系中为零，则在每个参考系中都为零的东西。

以下是我们将如何定义向量的导数。首先注意，要定义在点P的导数，我们只需要考察P点附近的点。我们要做的第一件事是在点P构造一组高斯法坐标。记住：高斯法坐标在P点附近尽可能直。它们在整个空间中有明确的定义，并且在P点的邻域内构成一个近似欧几里得的坐标系。因此，我们将向量场的所有向量重新用在P点局部平坦的欧几里得坐标X来表示。

为了从几何上遵循这个过程，让我们再次看向量场中的两个向量：与点P对应（或“附着”）的向量，以及另一个与附近点Q对应的向量，如图5所示。为了清晰起见，也让第二个向量与第一个略有不同。然后假设高斯法坐标在整个P点邻域内都是非常好的平坦坐标。在视觉上将向量Vq平移，使其起点与Vp的起点相同，然后观察Vq和Vp之间的差异。

在高斯法坐标中，Vq与Vp之差的分量正是我们将用来定义向量场在P点导数的那种元素。例如，如果我们关注沿PQ方向的导数，它大约是向量Vq - Vp除以P和Q之间的小距离。但我们关注的是V沿X轴方向的导数。

图5：对应于两个相邻点的向量。

现在，在P点，高斯法坐标中的导数dVm/dXr定义了V在P点的导数。

最后，如果我们想使用我们最初的V坐标系，我们将采用由P点高斯法坐标中的微分所产生的双索引偏导数集合。我们将其视为一个张量；也就是说，我们将这个集合视为X坐标系中一个张量的分量。然后我们使用连接X和Y的张量方程将其变换回V坐标系。

这必然会产生一个张量，因为当从任意V坐标系变换到X坐标系时，它给出相同的结果。

当我们考察一般坐标y中的向量导数时，我们将得到两项之和：一项是因为向量可能正在变化，另一项是因为坐标可能正在变化。正如我们所看到的，坐标可能会移动，可能会从你下面旋转出去，即使向量没有变化；见图3和图4。

在研究这两项之前，让我们将这个规定作为一个系统的程序重复一遍。

我们有一个向量场V，定义在配备任意坐标系Y的空间上。我们要计算V在点P的导数。那么我们遵循以下步骤：

## 1. 变换坐标，在P点使用高斯法坐标，我们称之为X（注意，它们在整个曲面上有效，并且在P点附近近似平坦）。

## 2. 使用X坐标系，以通常的方式在P点对V进行微分。

## 3. 将我们得到的偏导数集合视为X坐标系中一个2阶张量的分量。

## 4. 切换回我们原始的坐标系Y，并使用连接X和Y的张量方程，在该原始系统中重新表示我们得到的张量。

让我们看看我们得到了什么，然后对每一项进行评论。我们发现，使用这个新定义，在P点的导数是旧导数加上另一项的修正： 这里是如何读方程(10)：

## 1. 符号DrVm根据定义是在X中对Vm沿第r个方向的偏导数，它来自该过程，即在高斯法坐标X中，然后重新用V坐标表示。

## 2. 项drVm是在V坐标系中直接计算的Vm对Y中第r个方向的普通偏导数。注意dr是的简写。

3. 最后，— Vt是由于坐标Y本身在P点邻域内变化而产生的额外项。负号纯粹是约定。方程(10)右边的这整个第二项显然必须与Vt成正比。如果你将Vt的大小加倍，它也必须加倍大。Vt前面的系数T*m是在微分过程中出现的一个新的数学对象。我们将更多地讨论它。

项Vt没有与向量相关的导数，因为它不是来自向量正在变化的事实。它来自坐标在P点邻域内正在变化的事实。

方程(10)的右边就是你如果取一个向量，在高斯法坐标中对它进行微分，然后将双索引的导数集合作为一个张量变换到其他坐标系中所得到的结果。在任何其他坐标系中，你将得到该坐标系中的通常导数减去一个对象乘以V本身的分量。通常，Vt表示对t求和。方程(10)在任何任意坐标系中都成立。当然，Vm的或Vt的以及T*m依赖于坐标系。注意，r*m不是一个数：它们是一个三索引集合。

我们成功地定义了一种向量的导数，它实际上是一个张量。它被称为Vm的协变导数。

安迪：太酷了！我猜它之所以被称为协变导数，是因为指标在下方。

伦尼：聪明，安迪！但是错的。在这个上下文中，术语“协变”与指标的位置无关。它仅仅意味着该过程返回另一个张量。你可以提升指标使其变为逆变分量，它将是协变导数的逆变分量。明白吗？

安迪：啊？别讲太快...

伦尼：我告诉你：忘掉协变；我们就叫它shmovariant导数吧。

安迪：我想我明白了。所以方程(10)是shmovariant导数的协变分量？

伦尼：是的。现在我们可以回去叫它协变导数了吗？

克里斯托费尔符号这些系数有两个名字：联络系数和克里斯托费尔符号。

名字联络系数源于它们连接相邻点，并告诉我们如何计算向量场从一个点到另一个附近点的变化率，即使坐标系可能正在变化。

它们也被称为克里斯托费尔符号，以埃尔温·克里斯托费尔命名。它们偶尔也被称为“Christ awful”符号，因为 they seem complicated. With some practice, however, the reader will discover that they are not that complicated. They are just an extra linear term. But I grant you that they are complicated and unlikeable enough. Let’s investigate what follows from the definition of the covariant derivative and the Christoffel symbols. We are not going to prove every single fact we state, because there are just too many little pieces. But they are easy to check.

It follows from the definition of the covariant differentiation - namely, to differentiate a vector V at a point P, go to a set of Gaussian normal coordinates at P, differentiate the vector in the ordinary manner, treat the object you obtain as a tensor with two indices, change coordinates, etc. - that the Christoffel symbols have a symmetry: Γrmn = Γrnm. There are generalized Riemannian geometries, also called geometries with torsion, in which this symmetry is not true. But those geometries are not widely in use in ordinary gravitational theory. The geometry of general relativity is the Minkowski-Einstein geometry, which is an extension of Riemannian geometry with a non-positive definite metric. But it doesn’t involve torsion. So the Christoffel symbols we will use will be symmetric as in (11).

## 3. Flatness and Curvature

To build our physical intuition, let’s observe that calculating the derivative in Gaussian normal coordinates, which are almost flat, or as flat as can be, and then treating what we obtain as an object in its own right, is very similar to what we do in gravitational theory when we evaluate something in a free-falling frame. For example, in lecture 1, in a free-falling frame we calculated how light moved across an elevator, and then we transformed it to the frame of reference in which the elevator was accelerating. That is closely related to the operations we have been doing in this lecture: we calculate something because we know how to do it in coordinates that are as flat as possible. That would be a free-falling frame in general relativity. Then we transform it in any coordinate we like, accelerated coordinates or anything we need, and we translate the statement from one coordinate system to another. In the construction of the covariant derivative, the calculation of the variation of a vector from point to point is done first in Gaussian normal coordinates, and then it is transformed in any coordinate system. Equation (10), reproduced here DrVn = ∂rVn - Γrt Vt (12) is the form that you get for the corresponding collection of components. It is a tensor. However, ∂rVn is not a tensor. Therefore Γrtn cannot be a tensor. And Γr cannot be a tensor either.

We will see that the Γ’s are built up out of the derivatives of the metric ∂rgmn. In fact in a coordinate system in which the derivatives of the metric are zero, the Christoffel symbols are zero. But a tensor, if it is zero in one coordinate system, is zero in every coordinate system - that’s, among other things, what makes them so useful. So that is another way to see that they can’t be tensors.

Let’s look now at the covariant derivative of higher-rank tensors, because we will need this for curvature. Suppose that we have a tensor with more than one index, say Tmn, and we want to differentiate it covariantly along the r-th axis. We denote the resulting tensor DrTmn. Its expression is the analog of equation (12), except that for every index in the tensor Tmn, there will be a term like Γrt. Let’s see in more detail how it works.

We start by working only on the m index, letting n be passive. Writing the equivalent of (12), we get DrTmn ≈ ∂rTmn - VrmTtn — . . . This is only a part of what we want. We have to do exactly the same with the n index, letting this time m be passive: DrTmn ≈ ∂rTmn - TrmTtn - VrnTmt (13) That is the form of the covariant derivative at point P of the tensor Tmn. The rule is the same: we switch to Gaussian normal coordinates at P, and we do the ordinary differentiation of the tensor with respect to each direction Xr. This adds one more index to the collection of components that formed Tmn. Then we re-express the new tensor in the original coordinate system with the usual tensor equations (equations (16) and (17) of lecture 2 and their generalizations).

This allows us to differentiate any tensor. At the moment we are only dealing with tensors with covariant indices. We will come in a moment to tensors with contravariant indices.

The reader may wonder: what is all this intricate business of covariant differentiation of tensors for? It is for comparing things at different points. We want to be able to talk about rates of variation of things along coordinate lines, with objects that have an existence irrespective of the system of coordinates we work with.

Remember that a vector in ordinary three dimensions has an existence irrespective of the basis we are using. For certain works and calculations with it - not all of them - we need a representation of the vector in a basis. The collection of components to represent it and work with it is different from one basis to another, but the vector we are talking about is the same.

Where are we going to use covariant derivatives? Answer: in field equations. Field equations are going to be differential equations that represent how a field changes from one place to another. But we want them to be the same equations in every reference frame. We don’t want to write down equations that are specific to some peculiar frame. We want them to be valid in general. That is, if they are true in one frame, they will be true in all frames. That means they have to be tensor equations. So we have to know how to differentiate tensors to get other tensors.

Another point worth stressing: the Christoffel coefficients will be present in equation (13) even in a flat space - like a plane, or this page, or the ordinary 3D Euclidean space - if you chose funny coordinates; see figure 1 of lecture 2. That is an important point: terms like ΓrmTtn are there even in flat space if you are using funny coordinates. In fact if you choose any coordinates in which the derivatives of the gmn’s are not zero, that is, in which the coordinates vary from point to point sinuously (viewed from an embedding space, for instance), terms like ΓrmTtn will be present. The presence of terms like ΓrmTtn in the covariant derivative of a tensor is not a characteristic feature of curved spaces, it is a feature of curved coordinates.

To begin to use our new tool, let’s apply equation (13) to the metric tensor itself. There is something special, however, about the metric tensor: in Gaussian normal coordinates, its derivatives are all zero. It’s easy to check. But that in turn implies the following fact:

The covariant derivative of the metric tensor is zero. This simple observation turns out to be very powerful. It is what allows us to compute the Christoffel symbols. Let’s write equation (13) for the metric tensor: Γr9mn ≈ ∂rgmn - Γrrngtn - Γrn9mt We know that this is zero, because, as said, the ordinary derivative of the metric tensor in Gaussian normal coordinates is zero. So, in any coordinate system, we have ∂r9mn - Γrm9tn - Γrn9mt = 0 (14a) Let’s write the same equation, except with permutation of the indices. It is a little trick to get as much juice from the Christoffel symbols as we can and, eventually, via some nice cancellations, to be able to isolate one Christoffel symbol and express it in terms of the ordinary partial derivatives of g with respect to the axes in any coordinate system. Equation (14a) becomes ∂m9rn - Γmr9tn - Γmn9rt = 0 The middle term, by symmetry, can be rewritten interchanging m and r: ∂m9rn - Γrm9tn - Γmn9rt = 0 (14b) Similarly we can write ∂n9rm - Γrn9tm - Γmn9rt = 0 (14c) Let’s write these three interesting equations next to each other to look at them more conveniently: dr9mn - Γrm9tn - Γ rn9mt = 0 dm9rn - Γrm9tn - Γmn9rt = 0 (15) dn9rm - Γrn9tm - Γmn9rt = 0 How can we add them, or subtract them, or do something clever, to isolate only one of the terms with a gamma?

## 3. Flatness and Curvature

Let’s add equation (14b) to (14c) and subtract (14a). Of course, we will get dngrrn + dmgrn — 9rgmn plus some other terms. But the middle term of (14a), will disappear, and so will the last term of (14a), Γ*n<7mt. We will be left with twice the same last term with a gamma, Γ^n5rt. So we are in luck: (14b) + (14c) — (14a) yields ∂n9rm + ∂m9rn - 9rgmn = 2Γmngrt (16) We are still not done. We would like to get Γ^n by itself. Our goal, indeed, is to find out what the Christoffel symbols are in terms of derivatives of the metric. We are almost there. The reader may have guessed what we are going to do. Notice that equation (16) shows that if all the derivatives of the metric are zero, then the Christoffel symbols must be zero. How are we going to get rid of the grt on the right-hand side of equation (16)? The answer It comes from recalling that Γ has an inverse. We saw that in the form of matrix equations, as well as in the form of tensor equations; see equation (34) of lecture 2. We multiply both sides of equation (16) by the inverse tensor, and move also the factor 2. It yields Γ^m_{n} = 1/2 g^{mq} [ ∂_n g_{mq} + ∂_m g_{nq} - ∂_q g_{mn} ] (17)

This is the expression of the Christoffel symbols in terms of the ordinary derivatives of the metric tensor.

It is rather simple. The indices m and n are symmetric. You can interchange them, the Christoffel symbol won’t change. There are two positive terms and one negative term. It is not very complicated. The problem is that there is a boatload of them. When you think about a four-dimensional space and let all the coefficients range from 1 to 4, there is just a lot of Christoffel symbols. That is what makes doing calculations in general relativity a very tedious business. Intrinsically there is nothing hard about it. But doing a calculation in a general relativity context usually fills page after page of nothing more complicated than just computing these derivatives and assembling them together.

Equation (17) holds for any coordinate system and any metric tensor. Notice that all our calculations are at one point P. Whatever coordinate system our manifold is equipped with, we position ourselves at a point on it, consider the metric tensor there, and calculate the gammas there with equation (17). The use of Gaussian normal coordinates at P was just for intermediate reasoning, calculation, and proof purposes. We are now back in the initial coordinate system of our space. The g_{mn}, g^{mn}, and Γ^m_{n} all depend on P; they are fields. But equation (17) is general. At every point, it expresses the connection coefficients - the other name for the Christoffel symbols - in terms of the derivatives of g. These connection coefficients enable us to figure out how any vector or tensor varies when we move a bit along a coordinate line.

The problem with the Christoffel symbols is that they are not tensors.⁹ They can be zero in one frame of reference and not zero in another. For example, in a set of Gaussian normal coordinates at point P, all of the Γ^m_{n} are equal to zero. This can be seen in many ways. Since the metric tensor in that case is constant (even equal to the Kronecker-delta tensor, but that is not necessary), equation (17) tells us that Γ^m_{n} = 0. Yet in some other coordinate systems, the Christoffel symbols are not.

We mentioned several times that even in an intrinsically flat space, we can have coordinates such that the metric tensor is not constant. Then the Christoffel symbols won’t be zero. Let’s repeat: the Christoffel symbols are related to the coordinate system, not to the intrinsic geometry of the space.

A sphere is intrinsically non-flat. In the polar coordinates θ and φ (see lecture 1, figure 14), the components of g are not constant, therefore the Christoffel symbols are not zero in that system of coordinates. Even on a sphere, however, at any given point we can build a set of Gaussian normal coordinates - like maps do - then the Christoffel symbols at that point will be zero.

⁹At this point, after pages of higher mathematics, the reader may like to pause and remember a simple and familiar example of something very useful, yet which doesn’t have the nice properties of a tensor: at a point P, an ordinary contravariant vector is a tensor (of rank 1 with one superscript index), but the first component of the vector is not a scalar tensor (a tensor of rank 0), because it will change depending on the coordinate system.

Exercise 1: Explain why the space can be flat and nevertheless the Christoffel symbols not zero.

Exercise 2: Explain why the covariant derivative of the metric tensor is always zero.

Exercise 3: On Earth, with the polar coordinates θ for latitude and φ for longitude, find 1. the metric tensor g_{mn} 2. its inverse g^{mn} 3. the Christoffel symbols at point (θ, φ).

When we meet all this for the first time, it appears conceptually tricky. But at the end of the day, the rule is simple: calculate the Christoffel symbols and, in many contexts, replace ordinary derivatives with covariant derivatives.

You could write your equations in Gaussian normal coordinates. Then they would just involve ordinary derivatives, and we would not have to wade through a river of Christoffel symbols. But if you want the same equations in general coordinates, then replace the ordinary derivatives by covariant derivatives.

That is the procedure. It will require the reader to think about it. You will have to sit down, carefully follow the reasoning, do the exercises we propose and many more. Then what we are doing will become clear.

Curvature Tensor What is curvature? It is easiest to start with two-dimensional curvature. Intuitively it is easy to understand: it is a characteristic of something that is round and cannot be flattened out. But we are going to give it some more mathematical definition. How do we probe for curvature?

Let’s begin by drawing a space that is curved. A sphere is curved, yet a curved surface that resembles a cone will be more illuminating for our purpose. It is going to be a cone with a round summit; see figure 6.

Figure 6: Cone with a rounded summit.

Think of the top of a mountain the sides of which are nice and flat like those of a volcano, and the top is round.

If you are away from the top of the mountain, below the dotted line, around you the surface is flat.¹⁰ It may not look flat because, like the furled page in figure 10 of lecture 1, we represented the mountain embedded in 3D Euclidean space. But the surface is what mathematicians call developable: any section with no hole in it, cut from the side of the mountain, can be flattened onto a plane without distortion.

The rounded cone only differs from a flat space in the vicinity of the summit. To see that, just take the same space below the dotted line but continue it so that it really does form a genuine cone.

¹⁰ Technically it is flat because one of its two principal one-dimensional curvatures is zero. Consequently its Gaussian curvature, which is the product of the two, is zero, and it can be shown that the surface (below the dotted line) necessarily can be unfurled into a flat one. For a good chapter on curves and surfaces, see, for instance, the book that Andy is a fan of by Alexandrov, Kolmogorov & Lavrentiev, Mathematics, Dover, 1999, chapter VII.

Figure 7: Genuine cone.

Then slice the cone along a generatrix, i.e., a straight line on the cone going to the top. And open it up. You can lay out flat on a plane the shape that you get. It is a disk with a missing piece, see figure 8.

Figure 8: Cone opened up and laid flat (smaller scale and smaller angle than in figure 7).

The missing piece is called the deficit angle, or the conical deficit. We can see that the bigger the conical deficit is, the pointier the cone will be.

Now, on the flat surface of figure 8, let’s consider a collection of identical vectors arranged around the shape as shown in figure 9. On the flat surface, all the vectors point in the same direction. But when we fold the shape to form the cone, we see that the vectors no longer point in the same direction. Think of them as very small so that they don’t have to be bent. The first one on the left is along a generatrix, but the last one on the right points away from it.

Figure 9: Identical vectors.

We can describe this effect another way. Let’s suppose that our bug on the surface has a short vector - a pointer that points in some direction lying within the surface. Whenever the bug moves, it is very careful to keep the direction of the vector fixed. In three dimensions, it might do this with the aid of a gyroscope, and you can imagine a similar apparatus in two dimensions.

You might think that if the bug travels in a closed circuit, when it gets back to the starting point its vector will point in the same direction as when it started. But you’d be wrong if its orbit took it around the tip of the cone; in that case the vector will undergo a rotation. You can see that in figure 9.¹¹ The angle of the rotation is the same as the conical deficit.

Exactly the same is true on the rounded cone of figure 6: if we take a vector on the flat side, below the dotted line, and we carry it around the mountain in such a way that, when the surface is opened up and laid on a plane, the vector is always pointing in the same direction, by the time we get back to the other side, it will be pointing in a rotated direction.

That is the effect of curvature: when you parallel transport a vector in a closed loop around a region with curvature, the vector undergoes a rotation, despite all your efforts to keep it parallel to its initial direction.

¹¹ It is also clearly shown in figure 3 of lecture 4.

There is another way to say this, which is equivalent and actually more useful. Consider a curved space with some curvature at point P, as in figure 10. Take a vector field and differentiate it along one axis (first displacement in figure 10). Then differentiate it along the second axis (second displacement in figure 10). That is, you consider the vector field at P; then you move a bit along one axis and consider the new value of the vector field at T; then you move another bit along the second axis and consider the value of the vector field at Q.

Over each displacement, the vector will change. How will it change? The vector will change typically by differentiating it along the two axes in sequence. We first differentiate the vector along one axis and then differentiate it along the second axis. This will produce a small change in the vector due to the two derivatives.

Figure 10: Displacements to differentiate a vector.

along two axes. The total change in the vector consists of two changes. And that total change is proportional to a second derivative. That is true in any coordinates: if, to compare the vectors at Q and at P, you compared the vector at I with the vector at P, and then compared the vector at Q with the vector at I, what you would be calculating is the second partial derivative of the vector with respect to the two directions.

In figure 10, if the first displacement is along the direction Xs and the second displacement along the direction Xr, then the variation of the m-th component of the vector V - let’s say it has covariant indices - would be

DrDsVm (18)

This expression is calculated covariantly. In Gaussian normal coordinates, expression (18) would just contain ordinary derivatives.

We could have also gone in the other direction, as in figure 11. That is to say, we could have gone first in the r direction and then in the s direction and calculated the way the vector changes from P to J and then from J to Q.

The variation of V would then be

D9DrVm (19)

Ordinarily, and in flat space in general, expression (18) and expression (19) are equal to each other:

DrDsVm = DsDrVm (20)

This is just a version of the fact, in calculus, that the partial derivatives of a nicely behaved function of several variables can be taken in the order you like (see interlude 3 in volume 1 of TTM).

Equation (20) is not true in curved space. In that case the difference between the two sequences of differentiation, which is

DrDsVm - DsDrVm

can be thought of as taking the vector around the closed loop P -> I -> Q -> J -> P.

Let’s go back to our cone, either the genuine cone (figure 7) or the cone with a rounded top but looking at the part below the dotted line (figure 6). Consider a vector field that, when the cone is opened and laid flat, is constant. Fold the flat shape to form the cone. We discovered that if we follow the vector field on a closed loop around the top, we don’t get back to the same vector we started with. This is due to the following fact, which is important enough to stress:

In flat space covariant derivatives are interchangeable. In curved space they are not.

That will enable us to test whether the space is flat or not. We will test whether differentiating tensors, and in particular vectors, in opposite order gives the same result.

*   If the answer is yes everywhere in the space for any vector, then the space is flat.

*   If we discover that there are places in the space where the order of differentiation gives different answers, then we know that the space has some kind of defect in it (like the point of the genuine cone) or has curvature (like the summit of the rounded cone).

All we have to do is compute the second covariant derivatives of a vector in opposite order and compare them. In principle it is not complicated. In practice it will be a little complicated, but will remain manageable. We have all the tools at our disposal. Now it is a mechanical operation, consisting of pure plug-ins. We will sketch the steps, and then give the answer.

We start with a vector expressed with covariant components: Vn We compute its covariant derivative in the r direction: DrVn Then we differentiate this, still covariantly, in the s direction: D9DrVn (21)

After completing this step, we will interchange the indices s and r and subtract.

Let’s replace the first covariant derivative of Vn, with respect to r, by its expression given in equation (12). We get D9DrVn = Ds [DrVn - r’tnVt]

Notice that [DrVn - r’tnVt] is a tensor. We know how to differentiate it: use equation (13). Continue to crank mechanically the calculations.

In the end, the difference between the two second-order covariant derivatives yields a tensor, denoted R’tsn, multiplied by Vt: DsDrVn - DrDsVn = R’tsnVt (22)

Here is the tensor: R’tsn = Drr’tn - Dsr’tn + r’tn r’Ls - r’Ls r’tn (23)

There are two terms involving derivatives of Christoffel symbols and two terms that are sums over p of products of Christoffel symbols.

The tensor R’tsn is the curvature tensor, also called the Riemann curvature tensor or Riemann-Christoffel tensor.

It has a complicated expression. It is even more complicated when you remember that the Christoffel symbols are given by the equation r’tn = 1/2 gtp [ gmn9rn + gng9rm - 9rgmn ]

Let’s see what are the elements in the curvature tensor given by equation (23). The Christoffel symbols involve derivatives of g. So differentiating again produces second derivatives of g. Remember that the second derivatives of g are the things that we cannot generally set equal to zero. For the first derivatives of g, we saw that we can find a frame of reference where they are equal to zero. But for the second derivatives of g, we can’t. So by the time we are finished calculating the curvature tensor, the second derivatives of g have come into it. The second derivatives are testing and probing out the geometry of the surface a little more thoroughly than just the first derivatives. In a similar way, in the theory of functions, when at a point x you know f(x) and f’(x) and f''(x), you are better off than if you just know f(x) and its first derivative f’(x).

Thus the curvature tensor contains second derivatives of the metric g, and it has squares or quadratic things involving first derivatives of g. It is a complicated creature. If we were to actually write it in terms of the metric, or we were to try to calculate it for a given metric, it could rapidly fill up pages. But conceptually what it is doing is simply calculating the difference in a vector if you transport it around the loop in figure 11, keeping it parallel to itself, as much as you can locally at every point, until you have come all the way around. It calculates the little change in a vector in parallel transport going around a loop.

The curvature tensor has a complicated formula, but we can calculate it. We can put the metric tensor into a computer and ask the computer: “Is the curvature tensor 0?” It is even better if you have software that can do algebra. If you have the metric in some algebraic form, you can do all the operations of equations (17) and (23) and then test out whether the curvature tensor is zero everywhere. If the curvature tensor is zero everywhere, that is, all its components are zero everywhere, then your space is flat.

We shall study the curvature tensor a little more. As said, it is a complicated thing. Its main use is to tell us whether the space is flat. And, if not, how unflat it is.

It is closely related to a quantity in gravitational physics. Can you guess which one? A local quantity that tells you that the space is not flat. It must be something telling you whether there is really a gravitational field present or not. Answer: it is the tidal forces. It is exactly related to tidal forces, those things that in a gravitational field squeeze bodies one way and stretch them another way. Tidal forces are represented by the curvature tensor.

Here is another way to get a feel for what the curvature tensor is. Imagine a surface that is flat away from a point in the center where there is a bulge. It doesn’t have to be a rounded cone. It can simply be a plane with a bulge, as in figure 12.

You have a small structure of Tinkertoy sticks, all hinged at their extremities, so that their directions can move freely from each other, while remaining attached. At first, the probing structure lies flat, without stress or distortion, in a flat part of the surface, because the probe is itself flat.

Then you start moving the probe. While you move it in the flat region, nothing happens to it. It remains perfectly happy. It doesn’t get stretched, it doesn’t get distorted or deformed. This would have also been the case on the side of the rounded cone away from the summit, by the way.

What happens when you try to move the probe into the curved region? Then it simply can’t follow the curvature without having to stretch or compress some of its lengths. It has to follow the metric properties of the curved space. In particular, if you go around the probe, what you are doing somehow is sampling the double covariant derivatives of equation (18) or (19). You are going to find out that various angles between sticks change from their value in flat space. The lengths of the sticks shift too; they get stressed, they get deformed. The measure of how much the probe gets stressed locally is given by the curvature tensor.

The curvature is an important property because, if you are in a region where there is curvature, you can feel it, either with tidal forces in a gravitational field or with the probe in the experiment of figure 12.

Uniform gravitational fields don’t have curvature. That is why in free fall, in a perfectly uniform gravitational field, you simply feel nothing. Indeed, uniform gravitational fields don’t create tidal forces. Of course, perfectly uniform gravitational fields don’t really exist in nature. You can simulate one with acceleration, but you cannot see one in nature. They exist only approximately on the surface of big massive objects, if you limit yourself to a small solid angle. This leads us to a last remark.

Tidal forces, or curvature on a surface, have a bigger effect on bigger objects. The 2000-mile man in free fall toward the Earth will feel tidal forces more strongly than a free-falling bacteria. Similarly, in figure 12, if the probe is small compared to the bulge, it won’t be much deformed when it goes over it. Whereas, if it were a bigger Tinkertoy structure, made for instance of many more hexagons, covering a larger area, it would be severely distorted.

ger region of the plane, like floor tiles, but still hinged so that any two connected sticks can change their direction from each other, but not their length, then the probe would feel the curvature more strongly.

Let’s pause and see where we have arrived. At the end of this third lecture, we have reached the curvature tensor. It is complicated. Its expression is given by equation (23). I wish we could do without the sea of symbols and indices, but that is not possible if we really want to understand the nature of the curvature tensor. Nevertheless, the essential point is that we can compute it. Often you will be presented with the metric tensor in some analytic form. There will be a formula for it. With the formula you can do differentiation. Everything will consist then of analytic functions that you can calculate.

Therefore we have finally reached our initial goal. Remember that it was to find a method to determine whether a space is flat. By definition, the space is flat if there exists a set of coordinates in which the metric tensor is everywhere equal to the Kronecker-delta tensor.

The idea of trying out every possible set of coordinates, and checking them at every point, was not a practical solution. So we found the curvature tensor. If it is zero everywhere, then we can find a set of coordinates such that the metric tensor is everywhere equal to the Kronecker-delta tensor. You just position yourself at any fixed point and start to build Euclidean coordinates, like we did when we built Gaussian normal coordinates. If our space has no curvature, these Euclidean coordinates won’t be limited to a small vicinity.

In summary: • The space is flat if and only if the curvature tensor is everywhere equal to zero.

• The curvature tensor has a complicated form given by equation (23). But when we know the metric, the curvature tensor can be computed at every point of the space. Therefore it is a practical tool.

Notice that knowing the metric of the space at every point is not a stringent condition; it is the basic knowledge we must have about it. If we don’t know its metric, we really don’t know what our space looks like.

We are finished with our mathematical study of Riemannian geometry, metrics, tensors, curvature, etc. The interested reader who wants to go further into the mathematical aspects of these topics can open any good manual on differential geometry oriented toward applications. As far as we are concerned, our new toolbox is now complete. We are ready to use it.

In the next lecture, we will enter into gravity land. We will see what has to change to go from Riemann geometry to Einstein geometry. Then we will study a famous simple example: the Schwarzschild geometry. It is the geometry of a black hole, a star, or any gravitating mass.

Lecture 4: Geodesics and Gravity

Andy: Lenny, if I keep going straight ahead, following my nose, do I follow a geodesic?

Lenny: Yup, that’s the idea. But what straight ahead means depends on the geometry of the surface. It’s affected by the presence of masses.

Andy: So a guy on a drunk going from bar to bar, crossing the street several times, he follows a geodesic?

Lenny: Well I suppose you could say that the bars are like masses; they exert an attractive force.

Introduction Parallel transport Tangent vectors and geodesics Example of calculations with Christoffel symbols More on geodesics Space-time Special relativity Uniform acceleration Uniform gravitational field Motion of a particle

Introduction In this lecture we gradually move from Riemannian geometry, where the squared distance between two points is always a positive number, to Minkowski geometry, where the squared “distance” between two points, i.e., two events in space-time, can be positive, null, or negative.

Let’s begin by recalling the basic formulas established in the previous lecture on Riemannian geometry. Many of them will transfer with no change, but the metric will be less intuitive.

The covariant derivative of the simplest kind of tensor (leaving aside scalars), when we consider a covariant vector,1 is given by the formula Drvm = drvm - (1)

where is called a Christoffel symbol.

For a tensor with more covariant indices, the formula is a simple generalization of equation (1), carrying an extra term with a Christoffel symbol for each index. For instance DrTmn = drTmn — r rmTtn — (2)

Equations (1) and (2) are valid in any coordinate system. At any given point, if we are locally using a coordinate system that is as close as possible to Cartesian, then the Christoffel symbols are zero, and the right-hand sides reduce to their first terms, that is, to ordinary derivatives.

We now turn to a specific tensor: the metric tensor. Cartesian coordinates are by definition a coordinate system in which the metric does not depend on the point P, moreover is equal to the Kronecker-delta tensor. A space in which such a system can be found is called flat.

Similarly, locally, a Gaussian normal coordinate system is one in which the metric tensor is locally the Kronecker-delta tensor up to second order (that is, still behaving like the Kronecker tensor in the first order but not in the second). Therefore, at any given point P, in a set of Gaussian normal coordinates at that point, the ordinary partial derivatives of the components of the metric tensor are zero: ∂r∂gmn = 0 (3)

We saw in the previous lectures that, for us, vectors are abstract things which have a contravariant form, i.e., a collection of contravariant components, and also a covariant form. When we talk about a covariant vector, we mean, to be more rigorous, a vector expressed with its covariant components.

This is true only in a set of Gaussian normal coordinates at the given point.

As a consequence, considering the way we have defined it, the covariant derivative (which is always itself a tensor) of the metric tensor in any coordinate system, at any point P on the surface, is equal to zero: Dr ∂gmn = 0 (4)

Looking again at the Christoffel symbols appearing in equations (1) and (2), we saw in many ways why they are not tensors. Unlike tensors, they can be zero in one coordinate system and not zero in another. We calculated their value, in any given coordinate system, in terms of the ordinary partial derivatives of the components of the metric tensor: Fmri — 2 & t &n9rm “1“ dm9nr dr9mn ] (5)

Equation (5) shows again that if the ordinary partial derivatives of the metric tensor components are zero, as is the case in a best local coordinate system, then the Christoffel symbols are zero in that coordinate system. If they were tensors, they would have to be zero in any coordinate system, but they are not.

Andy: Lenny, how can I remember equation (5)?

Lenny: Same way as the Gettysburg Address. Just memorize it.

Covariant derivatives are designed to study the rate of variation of tensors, when we move in space, in a way that is frame-independent. They are rather complicated objects if we write them out in full. Christoffel symbols are a shorthand for simplifying them.

Equation (1) was the covariant derivative of a vector with covariant components. Let’s talk about the covariant derivative of a vector with contravariant components. We denote it DrVm As always it starts out with an ordinary partial derivative, and there is another term. The calculations are exactly the same as what we did to calculate the covariant derivative of a covariant vector. To do them, remember the following trick: there is a simple relation between the covariant form and the contravariant form of a vector. We can write V™ = g^Pyp It is a variant of the fourth of equations (14) in lecture 2. Then take the covariant derivative of each side. Since in a best set of coordinates,2 the covariant derivative is a standard derivative, it is easy to verify that it will satisfy the rule of differentiation for a product (see lecture 2 in volume 1 of TTM): Dr V™ = (Drgmp)Vp + gmp(Dr Vp) (6)

On the right-hand side appears the covariant derivative of the inverse metric. Just like Drgmp = 0, see equation (4), it is easy to prove that it must also be true for the inverse metric: Drgmp = 0. Therefore the first term disappears, and equation (6) becomes DrVm = gmp(DrVp) (7)

We know how to calculate the covariant derivative of a vector with lower indices: it is equation (1). If you plug that in equation (7), after some algebraic manipulation you will find the formula for covariantly differentiating a vector with a contravariant index, that is, with an upper index. Here is the result: DrVm = drVm + (8)

As before, the formula begins with a simple derivative. Then it has a term that would be zero in a set of best coordinates, because the covariant derivatives would simply be the ordinary ones. However they are not zero in general coordinates. In this second term with the Christoffel symbol, there is a sum over t. Generally speaking in equation (8), we check that all the indices are in place as expected. The only peculiarity is the plus sign instead of the minus sign that appeared in the covariant derivative of a vector with a lower index, as in equation (1). That minus sign was a convention. Here too, but it must be the opposite sign.

2That is the informal way we call local Gaussian coordinates.

Just as we generalized the covariant derivative of a covariant vector to tensors with covariant indices when we went from equation (1) to equation (2), we can generalize the covariant derivative to a tensor with any collection of lower and upper indices. A lower index will entail an extra term with a Christoffel symbol with a minus sign, while an upper index will entail an extra term with a Christoffel symbol with a plus sign.

We arrive at the idea of parallel transport. We already touched upon it in the previous lecture. But let’s now spell it out in detail.

Parallel Transport Suppose we have a curved surface, or a higher-dimensional curved space, and some vector field defined on it. That is, at every point of our space, there is attached a vector. In what follows, to start with, the vectors of the vector field will always be in the tangent plane - or in the higher tangent flat space - to the space.

We are interested in knowing, when we move along a curve on the space, as in figure 1, whether the field stays parallel to itself. In the figure we have represented the space and the curve, but neither the vectors of the vector field nor the curvilinear coordinates on the surface.

Figure 1: Vector field and curve on a space.

At each point of the curve, imagine there is a vector. Let’s move along the curve. What we want to know is whether the vector (or if you prefer, the field) stays parallel to itself. “Parallel to itself” between X and X + dX on the curve means the following: The vector stays parallel to itself, when we move from X to X + dX, by definition if its covariant derivative in the direction of the curve at that point X is 0.

The covariant derivative is the difference between the vectors at X + dX and at X, as they are written in best local coordinates, divided by the components of dX. Let’s write again the tensor that is the covariant derivative of a contravariant vector: dVn DmVn = — +VnmrVr (9)

Now we want to consider the derivative along the trajectory or curve. How does the vector change from point to point? That simply corresponds to taking the covariant derivative DmVn and multiplying it by dXm. Hence, the small change in the vector is DmVndXm (10)

This formula accounts for the fact that the coordinates themselves may evolve as we go from point to point. That is the essence of covariant derivative.

Expression (10) is the small change in the vector V in going from one point to its neighbor, measured by the change of its components in a set of best coordinates and then considered abstractly in any coordinate system. Let’s give it a name: DVn = DmVndXm (11)

is the covariant change in the vector going from one point to a neighboring point on the trajectory.

Let’s express this covariant change with the building blocks we have. We multiply the right-hand side of equation (9) by dXm and get dVn DVn = g^dX™ + T” rVrdXm (12)

The first term on the right-hand side has a simple interpretation. It is the ordinary differential change in V disregarding anything related to a possible change in coordinates. We denote it dVn.

Equation (12) becomes DVn = dVn + r^r VrdXm (13)

The formula reads as follows: the covariant change in V is equal to the ordinary change in V plus a term equal to a Christoffel symbol multiplied by Vr and by dXm. This second term is of course a double sum following the summation convention.

Equation (13) is the formula that tells you how a vector changes from point to point.

Suppose we are interested in finding a vector that is parallel to itself as we move along the curve. “Parallel to itself” means that it doesn’t change as we move from X to X + dX. At each point X, we erect some best coordinates, and in those coordinates we test whether the vector is changing. If it doesn’t change in the first order - i.e., its first derivative is zero - we say: good, the vector is constant along the little segment. We go to the next little segment, erect best coordinates at the new point, and test again. We do that all along the curve. If the sequence of tests say that the vector never changes in the first order, the vector is said to be parallel to itself along the curve.

In summary, if all along the curve the vector V satisfies dVn + r^rVrdXm = 0 (14)

then the vector maintains a relationship of being parallel to itself.

Taking a vector from one point and transporting it like this along a given curve, in such a way that it stays parallel to itself, is called parallel transport. Making up a benign neologism, we say that we “parallel-transport” the vector.

A very important fact about parallel transport on a curved space is that it is trajectory-dependent. On the surface in figure 2, if we start at point A, take a vector V there, which lives in the tangent plane, and parallel-transport it to B, then the vector we end up with at B will depend on the path we followed from A to B.

In figure 2, we represent the vector V at A and suggested its evolution along two paths. We did not represent any coordinate system. Indeed, it is important to understand that parallel transport is dependent on the trajectory, but is independent of any coordinate system used to locate points on the surface. At each point, anyway, we use a set of best local coordinates to do the infinitesimal parallel transport of the vector there. When we arrive at B, the final vector we end up with depends not only on V of course, but also on the path we followed. The final vector depends on the bumps and troughs we encountered along the path, that is on the local curvatures along the path. Even if we came back to the same point A, depending on the loop we followed, we would end up with one or another vector. If there exists a flat connected region - i.e., flat and with no hole - and we follow a loop entirely in that region we will end up with the same vector V.

Figure 2: Parallel-transporting V from A to B. Depending on the path followed, the end vector at B is not the same.

We already saw this phenomenon on the cone - pointy or rounded, it doesn’t matter - in the previous lecture. When we started with a vector on the side of the cone and parallel-transported it around the cone, we did not end up with the same vector. An alternative path would be not to go around the top of the cone, in which case we would end up with the same vector. This illustrates that two paths don’t always lead to the same result; see figure 3.

Remember that the side of a cone is flat according to our definition, even though we see it embedded in 3D and in ordinary language it is not flat. The side of a cone is intrinsically flat, because any section of it with no hole can be laid out on a plane without exerting any distortion on it. More mathematically, any connected section of the side is flat because there exists a coordinate system the metric of which is the Kronecker-delta tensor over the whole section.

Figure 3: Parallel-transport of the vector V on a cone along two different paths, both starting and ending at A.

Parallel-transporting a vector, that is, moving it on the surface while making sure that its covariant derivative remains null, also preserves its length. It can be shown as a consequence of equation (14).

The next topic will concern tangent vectors to a curve, and whether the tangent vector stays constant or not. When the tangent vector stays parallel to itself, we will see that the curve is a geodesic.

Geodesics are intuitive. However they are a bit trickier than we may think. For instance, on the cone of figure 4, if we go from A to B around the cone as shown (in 3D, staying parallel to the horizontal plane), we don’t follow a geodesic.

Figure 4: Going from A to B on a cone.

We will see that geodesics are shortest curves. In figure 4, going from A to B as shown is not a shortest curve. It becomes evident if we think of a very flat cone.

On Earth, boats and airplanes try to follow geodesics because they are the most economic routes. They are the so-called great circles. When, while we are sitting on an airplane, going to a very distant destination, the crew shows on a screen our trajectory, we are often surprised to discover that we do not follow a “straight” line. That is because a great circle is not mapped into a straight line on the usual flat representations of the Earth.

Tangent Vectors and Geodesics We arrive at the notion of tangent vector to a curve and of geodesic.

On a surface where we consider two points A and B, a geodesic between A and B is a curve with certain properties. It can be defined in several ways:

## 1. The curve with the shortest distance between A and B is a geodesic

## 2. A curve whose length is stationary when you wiggle it is a geodesic

3. A third, better definition looks at what happens locally along the curve: a curve that at each point is as straight as possible is a geodesic.

Of course, this last definition is more intuitive than mathematical. Let’s make it more precise. If at each point along the curve, the covariant derivative of the tangent vector3 is zero, that is, if the tangent vector doesn’t change, then the curve is as straight as possible.

Let’s try to build more intuition about geodesics before turning to the mathematics. Imagine a curved terrain, as in figure 5. For convenience, it is a two-dimensional example, but there is nothing special about two-dimensional spaces in defining the notion of geodesic. Secondly, imagine that we are driving a car on this terrain. And assume that the size of the car, in particular the distance between the front wheels, is small by comparison with any curvature and that the steering wheel is locked in the straight-ahead position. We start from A in some direction, and driving straight in the above sense - never turning the steering wheel - we end up at B. Our trajectory will wind between the hills. We may also start from the top of a hill, that is, from a point with clear curvature, that doesn’t change anything. The curve that we will execute with our car in the space, keeping the steering wheel straight, will nevertheless be as straight as possible. It will be a geodesic in the space.

Another way to characterize a geodesic is to say that the tangent vector along the curve is constant. We have an intuitive perception of what the tangent vector is. But let’s define it more precisely.

Consider a curve, and a point at coordinate X on it. And take a neighboring point; see figure 6. The points X and X + dX are separated by dX, which we can also denote, in tensor style, dXm. Consider a vector the origin of which is at X, going through X + dX, and of length one. Then take the limit when the second point X + dX approaches the first point X. The resulting vector is called the tangent vector to the curve at X.

Figure 6: Construction of the tangent vector at a point.

Consider the distance dS between the two points X and X + dX. As we remember, it is defined by dS2 = gmn dXm dXn (15)

The way we construct the tangent vector in the X coordinate system is very simple. The m-th component of that vector is dXm / dS (16)

It can be proved that equation (16) produces a vector of length one. The exercise is left to the reader. There is one such vector at each point along the curve. That, as said, is what we call the tangent vector. It points in the direction between two neighboring points and is of length one.

Let’s turn our attention to curves the tangent vector of which is constant. If we plug in the tangent vector in equation (14), these curves satisfy the following equation: dtn + Γ^n_mr dXm = 0 (17)

Equation (17) holds because once you have set your steering wheel straight ahead, you are moving in as straight a line as you can. So the covariant change of the tangent vector is zero. Next we give an example to build our intuition.

Example of Calculations with Christoffel Symbols Building a correct intuition about geodesics is important because it is easy to be misled. This is particularly true when the surface has curvature - like a round hill. Indeed, the embedding 3D space in which we ordinarily view the intrinsic curvature of the surface suggests that the tangent vector changes when in fact it doesn’t.

Consider a point P on the surface of a sphere; see figure 7. Mathematicians call such a surface a 2-sphere, because its points can be located with two coordinates. Let’s use the ordinary latitude θ and longitude φ, and the ordinary distance we are familiar with, for instance on Earth.

The objective of the exercise is to show that a meridian is a geodesic. In other words, when we follow a meridian, the tangent vector doesn't change.

Exercise 1: We are on a 2-sphere of radius one with polar coordinates θ and φ, as in figure 7.

## 1. Show that the metric tensor of the ordinary distance is

g = (1   0       )

(0   sin²θ )

## 2. Express the eight Christoffel symbols using this metric. Show that

Γ^2_12 = Γ^2_21 = (sin θ cos θ)⁻¹ and all the others are zero.

3. Show that the tangent vector to a meridian has everywhere components t¹ = 1 and t² = 0.

4. Show that the tensor that is the covariant derivative of this tangent vector is (0             0         )

(0   -cot θ )

5. Show that if we follow a meridian, the covariant change of the tangent vector is always zero.

Doing this exercise will show you that the actual calculations with Christoffel symbols, even on a simple example, quickly fill pages. It will also show you that even on a surface with curvature there are paths where the tangent vector doesn’t change. These are the geodesics.

In the exercise we looked at a meridian, because the polar coordinates make it simple to study, but by symmetry any great circle is a geodesic.

In figure 7, we might feel that the tangent vector changes when we move along a meridian, but that is because we look at the 2-sphere embedded in 3D Euclidean space.

If we turned our steering wheel, however, and in the tangent plane swerved from our straight path, that would be another story. Then the tangent vector of our trajectory would change.

More on Geodesics We can write equation (17) of a geodesic in a slightly neater form. Let’s divide both sides of the equation by dS, that is, by the little distance between two neighboring points with coordinates X and X + dX, see figure 6.

Equation (17) becomes dtn/dS + Γ^n_mr (dXm/dS) = 0 But dXm/dS is tm, so we can rewrite equation (17) as dtn/dS + Γ^n_mr tm = 0 (18)

This equation only involves the tangent vector. Of course, it also involves the Christoffel symbols, but let’s suppose they are given. Then equation (18) is the “equation of motion” of a geodesic.

One more thing: since the tangent vector t itself is a derivative, we can write the left-hand side as a second derivative: d²tⁿ/dS² + Γ^n_mr (dtᵐ/dS) tʳ + Γ^n_mr tᵐ tʳ = 0 (19)

Does this look familiar? If we were to think of S as some measure of time as we moved along the curve, then, on the left, the second derivative of position would be acceleration. Thus if S were like time, or were increasing uniformly with time, equation (19) would read like this: an acceleration is equal to something that depends on the metric and on the components of the tangent vector. We might even see on the right a kind of force.

For the time being, let’s just observe that equation (19) has the look of a Newton equation: acceleration is equal to something that depends on the gravitational field, because, as we will see, the metric is the gravitational field. We will see that equation (19) replaces Newton’s equation for the motion of a particle in a gravitational field. In other words, in some sense a particle in a gravitational field moves along the straightest possible trajectory. But it moves along the straightest possible trajectory not just through space but through space-time.

Space-Time So far we have been studying the mathematics of curved spaces, as Riemann would have understood it. Yet Riemann’s spaces were, so to speak, ordinary curved spaces in which distance was governed locally by Pythagoras theorem (in an appropriate reference frame). In particular, in Riemann’s spaces the square of the distance is always positive. General relativity, however, is not just about space; it is a theory of space-time geometry.

The coordinates of space-time are the coordinates of space, x, y, z, and time t. Frequently we will use the more symmetrical notation: x = X¹, y = X², z = X³, ct = X⁰ where c is the speed of light.

Space-time also has a natural measure of distance along curves or between points, called events in space-time, be they neighboring points or not. As in Riemannian geometry, in Minkowski geometry the distance is generally expressed through its square. But in Minkowski space this square can be zero for distinct events, or even be negative.

Let’s begin with flat space-time in the analog of Cartesian coordinates. The theory of flat space-time is of course special relativity - the subject of volume 3 of TTM. You will recall that in special relativity the squared space-time distance is given by4 (Δτ)² = (Δt)² - (ΔX)² where (ΔX)² is shorthand for (Δx)² + (Δy)² + (Δz)². We may also use the more relativistic notation just mentioned (Δτ)² = (ΔX⁰)² - (ΔX)² There are three possibilities: (Δτ)² can be positive, in which case the separation between the two points is said to be time-like; it can be negative, in which case the separation is space-like; or it can be zero, in which case the separation is light-like.

When the interval is time-like, we refer to Δτ as the proper time between the points. When (Δτ)² is negative, we redefine things and call √((ΔX)² - (Δt)²) the proper distance between the points.

4 For simplicity we are using units in which the speed of light is equal to 1. The more general formula is (Δτ)² = (Δt)² - (1/c²)(ΔX)².

That leaves the case Δτ = 0. Such an interval is called null. It represents two events that can be joined by a light ray in space-time. A null interval is also called light-like.

In flat space these definitions apply to any pair of events, far away, close, even infinitesimally close. When the events are infinitesimally close, the square of the proper distance is rewritten (dτ)² = (dX⁰)² - (dX)² We have put parentheses around all the intervals to make it clear that we take the square of the interval, but in later equations we will drop these parentheses when they are not necessary, assuming the meaning of the notation is clear. Thus the previous equation will simply be written dτ² = (dX⁰)² - dX² (20)

Remember too that X⁰ is the same thing as t.

Figure 8: Proper time τ between two events P and Q. (When we write Δτ², we mean (Δτ)²; same comment for the other intervals.)

When dτ² is negative, it is conventional to rewrite equation (20) as dt² - dX² = -dS² where S is called the proper distance. (The speed of light squared is in front of dt². But we took it to be equal to 1.)

Another convention is to write equation (20) as dS² = g_μν dX^μ dX^ν (21a)

or dτ² = -g_μν dX^μ dX^ν (21b)

where readers who have read volume 3 on special relativity are familiar with the notation with a Greek upper index: X^μ = x According to standard convention, this is also sometimes noted X^μ = (X⁰, X¹, X², X³)

where the Greek index μ runs over 0 to 3.

When we use a Latin index, we mean only the three spatial coordinates, that is, if you read Xⁱ, this means that i runs over 1, 2, and 3. In other words, Xⁱ runs only over the spatial coordinates.

Let’s comment on equation (21a). The indices μ and ν run over 0 to 3. The equation has exactly the same form as the usual equation for the distance in Riemannian geometry that we have already often used; see equation (1) of lecture 3, for instance.

The only new thing in the Minkowski geometry is the metric tensor or its corresponding matrix. It is still diagonal, but it has a minus 1 corresponding to the time axis, and three plus 1’s for the space axes. As it plays a central role, it has a name. We use the Greek letter η (pronounced “eta”) to name this matrix. And we write it η_μν (pronounced “eta mu nu”): η = diag(-1, 1, 1, 1) (22)

With this form for the metric tensor, we can check that equation (21b) expressing the proper time is the same equation.

dr2 = dt2 — dx2 — dy2 — dz2 Thus far we have been speaking about special relativity. In general relativity, the metric tensor becomes a function of space and time. We then call it (where X stands for an event in space-time, i.e., a point with four coordinates). Equation (21b) becomes dr2 = -g^(X) dX» dXy (23). There is one more important thing, which we must stress at the outset, concerning the metric tensor in relativity. What is the difference between the matrix of equation (22) and the identity matrix of Euclidean metric? Well, it has a minus 1 in first position. But more importantly, there is an invariant concept about g^X)': it has one negative eigenvalue and three positive eigenvalues. These four signs define its so-called signature. In general relativity, no matter how curved the space-time, or otherwise unfamiliar, the signature of the Minkowski metric will always be the same: three pluses and one minus, or denoted more compactly, (-+++).

We are not going to spend much time dealing with this mathematical notion. Fortunately the equations of general relativity automatically guarantee that the signature is always (—I- ++). What does it mean that there is one negative eigenvalue and three positive? It means that there is one dimension of time and three dimensions of space. We could write a metric with two minus signs on the diagonal. It would correspond to a crazy space with two time dimensions and two space dimensions. Fortunately that is not only disallowed, but it can never occur if the equations of general relativity are correctly solved.

Other than that, all that we have done in Riemannian geometry, all the equations involving metrics, covariant derivatives, curvature, geodesics, etc. will be exactly the same in the Minkowski-Einstein space-time geometry of general relativity.

Now comes a big question: What does flat mean in space-time? It no longer means that there is a coordinate system in which the metric is the Kronecker-delta. It now means there is a coordinate system in which the metric has the form of equation (22). In Riemannian geometry, global flatness required the existence of a metric built with the Kronecker symbol everywhere. Similarly, in space-time, global flatness requires the existence of a system of coordinates in which the metric has the form everywhere.

How do we check whether the space-time is curved? We proceed exactly analogously as we did in Riemannian geometry.

Here is a recap of the analogies that we have already made so far, as well as those we shall see: Flat spaces Euclidean geometry —> Minkowski geometry Kronecker 6 tensor —> rj tensor Newtonian physics —> special relativity Non-flat spaces (always locally flat)

Curved metric —> gravitational field Riemannian geometry —> Einstein general relativity

Before going into a space whose curvature is due to real gravitational fields, i.e., to the presence of massive bodies, we shall spend some time with a “flat” space in Minkowski geometry.

We will wind up looking at it in polar coordinates - not ordinary polar coordinates but hyperbolic polar coordinates. The name is awe-inspiring, but the concept is simple and well adapted to space-time and particles moving in it, notably particles accelerating in it. Since we know from lecture 1 that there is a link between gravity and acceleration, and our ultimate goal is to describe relativistic motion of particles in gravitational fields, it is natural to start with studying particles accelerating in the framework of special relativity.

## 4. Geodesics and Gravity

Special Relativity We are in the space-time of special relativity, which we call a Minkowski space. Its metric is defined by the tensor (24)

-1 0 0 0 \ 0 1 0 0 0 0 1 0 0 0 0 1/ Our objective is to define the notion of a uniformly accelerated reference frame in special relativity.

We have already met a uniformly accelerated frame in lecture 1 when we illustrated the principle of equivalence with a uniformly accelerated elevator. The gravitational field of the Earth (in a small region where it can be viewed as uniform) and the apparent field we experienced in the elevator being uniformly accelerated were indistinguishable. But in lecture 1 we used Newtonian physics.

In special relativity, there is a difficulty with the notion of a uniformly accelerated reference frame. It is no longer as simple and intuitive as in Newtonian mechanics.

Let’s see what is the difficulty, and how we deal with it. Consider a bunch of point-like observers, separated by a fixed distance, as in figure 9. Think of them as forming a frame.

Figure 9: Points in space with a fixed separation. We want to accelerate them “uniformly.” Suppose that the observers are accelerating along the X-axis, each having the same constant acceleration. We would think that they would remain the same distance apart. That is true in Newtonian mechanics, but in special relativity distances, time and simultaneity behave oddly as the velocity grows.

If we gave all the observers the same acceleration, we would discover that, viewed from the rest frame of the first observer, the distance to the second observer would grow. If there were strings between the observers, as they started simultaneously moving, those strings would stretch and eventually break. That is not what we would think of a uniformly accelerated reference frame, as we are accustomed to from non-relativistic physics. What is nice in non-relativistic physics, about a uniformly accelerated reference frame, is that it keeps the same structure, the same shape. The distances between points stay the same. If you had strings connecting the points, they wouldn’t get stretched. But that is not so in relativity.

There is a second difficulty about the simplistic idea of uniform acceleration in special relativity: In the naive conception of a uniformly accelerated reference frame, if we waited long enough, the observers would eventually exceed the speed of light. However in the theory of relativity, particles that we can observe never exceed the speed of light.

Uniform acceleration, to the extent that it exists and makes good physical sense, is not as simple as just moving the points in figure 9 all with the same acceleration.

We are going to construct what a relativist (i.e., a specialist in relativity theory) would call a uniformly accelerated reference frame. To do so, it will be helpful to go back to Euclidean space in polar coordinates, as in figure 10.

Surprisingly enough, the uniformly accelerated coordinate system in relativistic space-time is the analog of polar coordinates in ordinary space.

Here are some equations, expressing the coordinate transformation from polar to Cartesian coordinates, with which the reader should be familiar: x = r cos 0, (25) y = r sin 0. We also have cos2 0 + sin2 0 = 1 (26) which is the same as saying that 2,2 2 x + y = r (27). Finally there are two more equations to remember: cos 0 = (e^{i0} + e^{-i0}) / 2i (28), sin 0 = (e^{i0} - e^{-i0}) / 2i. You can check that cos2 0 plus sin2 0 is equal to 1. It is a simple identity, true for all possible 0. Equations (25) to (28) are the basic equations governing ordinary polar coordinates.

What is the equation of a circle around the origin? It is just r = constant. Imagine a point moving around the circle with uniform velocity, therefore uniform angular velocity. Then the magnitude of the acceleration of that point is constant around the circle, the vector acceleration constantly pointing toward the center of the circle.

What does it have to do with relativity? We will see that in relativity we write almost the same equations to define a uniformly accelerated point.

We turn to the basic diagrammatic representation of space-time, which is the analog in special relativity of figure 10 in Newtonian physics. It is figure 11.

In figure 11, we see the light cone: the two diagonal straight lines. From volume 3, we know that they represent the trajectory of a light ray starting at time 0 from the origin and going either to the right or to the left. Remember that in the simplest Minkowski diagram, shown below, there is only one spatial dimension. Everything moves on the straight X-axis in space.

Figure 11: Light cone. It would actually be a cone if we had two spatial coordinates. Pay attention to the fact that in this familiar Minkowski diagram there is only one spatial dimension.

Notations: We use the variables X and T because later we will make a change of coordinates and arrive at variables y and t (little t) when we study a uniformly accelerated frame like the elevator of lecture 1. We will discover that uniformly accelerated frames produce a fictitious gravity, like we already observed in lecture 1.

Let’s consider for a moment the analog of the circle in figure 10, but in Minkowski space. The circle of course is the locus of points a fixed distance from the origin: 2.2 2 x +y = r. By analogy we can consider the locus of all points a fixed spacelike Minkowski distance from the origin in figure 11. It has the form of a hyperbola: X2 - T2 = r2. This suggests the following definition of a uniformly accelerated particle in special relativity.

For the moment, we will define a uniformly accelerated observer as one moving on a hyperbola as shown in figure 11. It is clearly not moving with constant velocity along the X-axis but is accelerating. Indeed, constant velocity would correspond to a straight line with a slope higher than 45’ because things don’t go faster than the speed of light.

In figure 11, we see that from the past until time 0 (i.e., the lower part of the diagram beneath the X-axis), the point or particle or observer (henceforth we shall talk of observers, rather than particles, in these positions), moves, spatially on the hyperbola, and in time uniformly.

the X-axis, to the left to a minimum point M. At M its velocity has come to zero. Therefore, in the (X, T) diagram, at M the tangent to the trajectory is vertical. After point M, the observer changes course going again to the right. In the Minkowski diagram, as the point moves up and up, the tangent to the trajectory gets closer and closer to 45°, that is, the observer moves on the X-axis closer and closer to the speed of light, without ever exceeding it.

Equations (25) describing a circle centered at O have an analog for the hyperbola in figure 11. The equations are obtained by simply replacing the trigonometric functions sin and cos by their hyperbolic counterparts, sinh and cosh. The correspondence is cos θ → cosh ω sin θ → sinh ω

The mathematical definitions of the hyperbolic sine and cosine functions are very similar to those of ordinary sine and cosine. But, unlike in equations (28), there is no more i = √(-1) coefficient in the exponents and the denominator: cosh a = (e^a + e^{-a}) / 2  (29)

sinh a = (e^a - e^{-a}) / 2

Analogously to equation (26), the reader can verify that cosh² ω − sinh² ω = 1  (30)

The coordinates of a point P in the (X, T) diagram are now X = r cosh ω  (31)

T = r sinh ω

Equations (31) define r and ω from X and T. The parameter ω is not a geometric angle. But when we move along a hyperbola with the light ray trajectories as asymptotes (figure 11), it is what increases from −∞ to +∞, just like θ was the parameter that changed as we moved along a circle centered at the origin. On such a hyperbola, r doesn’t change. The parameter ω plays on the hyperbola the role of the angle on the circle. It is sometimes called the hyperbolic angle.

As before, equations (31) express nothing more than a coordinate transformation between the Minkowski coordinates (X, T) and the hyperbolic coordinates (r, ω). Recall that an event in spacetime corresponds to one point on the page. It can be located by its Minkowski coordinates (X, T) or by its hyperbolic coordinates (r, ω), or by any other system we like. That’s what frames of reference are: the mathematics changes, but the physics (i.e., the spacetime and what happens in it) doesn’t.

In figure 12, all the points on the hyperbola have the same r. It is called the hyperbolic radius. Its value is the distance between O and M. It characterizes the curve. On the other hand, the hyperbolic angle ω increases up to infinity as we move on the hyperbola closer and closer to its asymptote, that is, as the observer moves spatially farther and farther away to the right on the X-axis.

Thus we have in Minkowski geometry the analog of the circle in Euclidean geometry: the hyperbola, as in figures 11 and 12, in hyperbolic polar coordinates given by equations (31), corresponds to a constant value r and to the parameter ω going from −∞ to +∞. This will be handy to study a uniformly accelerated particle because by definition it moves along such a trajectory.

The analog of equation (27) on a circle becomes, on a hyperbola, X² − T² = r²  (32)

Of the two coordinates r and ω, one of them is space-like, the other time-like. You can probably guess which is which, but let’s go through the reasoning. On the X-axis, cosh a = 1, so if we move to the right on this axis, we just increase r. Therefore r is like a space coordinate.

On the other hand, if from point M we travel upward on the hyperbola of figure 12, r stays fixed and we increase ω. Going upward is the analogy with traveling around the circle in figure 10 with increasing angle, but in this case it moves us in a time-like direction. So ω is like a time coordinate.

On the hyperbola in figure 12, ω is proportional to the proper time measured along the trajectory. More precisely it is the proper time τ measured in units of r: ω = τ / r

If the observer who is at a fixed value of r carried a wristwatch, it would register a proper time rω along the trajectory.

Just as there was a uniformity to the circle - at any point you could define the radius r and it was constant - there is an analogous uniformity to the hyperbola: the hyperbolic radius r is constant on a hyperbola. Figure 13 shows hyperbolas for different values of r.

Let’s return to the family of accelerated observers, separated by the same distance (as shown at first in figure 9). They are represented in figure 13.

At fixed values of ω, the distances between the observers corresponding to r = 1, r = 2, r = 3, etc., are always the same. If in figure 13 we define the proper distance between two points M and N to be |MN|, then by construction |MN| = |NP|

But it is not hard to show that the equal spacing of observers is also true at a later value of ω: |MN| = |NP| = |RS| = |ST|

This can be checked with the tools we learned in volume 3 on special relativity.

Exercise 2: In figure 13, what is the speed, relative to the stationary frame, of the observer who sees R, S', and T as simultaneous events?

Uniform Acceleration

All of what we just saw means that as the Lorentz frame of reference accelerates, the distance between neighboring observers does in fact stay the same. However, there is a price to be paid. What is different from a non-relativistic accelerated frame of reference, is that the accelerations along the different trajectories corresponding to r = 1, r = 2, r = 3, etc. are different.

One can see this intuitively by looking at the various trajectories in figure 14.

Figure 14: The hyperbola with a very small r corresponds to a very high acceleration.

On the hyperbola with a very small r, the trajectory makes a sudden change of direction when it comes close to the origin, and then speeds off to the right again very fast. That indicates that the trajectory has a large acceleration. By contrast, the trajectories farther out to the right have a much gentler change of direction, indicating a smaller acceleration.

This was all intuitive, but so far we have not defined relativistic acceleration in any systematic way.

To do so, let’s first begin with velocity.

• The ordinary velocity of a particle is a 3-vector defined by the time-derivative of its spatial position. This is expressed by v = dx / dt • The relativistic velocity is a 4-vector defined by u = dX^μ / dτ where τ is the proper time along the trajectory.

As long as the particle is moving slowly, the space components of the relativistic velocity are very close to the ordinary velocities v.

Similarly for acceleration, the relativistic acceleration is also a 4-vector defined by a = du / dτ

What do we mean when we say that the acceleration is constant along a hyperbolic trajectory? We mean that the proper length of a is constant. In other words, |a|² = (a¹)² − (a⁰)² = constant

Recall that X⁰ and X¹ refer to T and X in figure 14.

Let’s check it for a motion along the hyperbolic trajectory with r = 1. Using equations (31) and the fact that ω and the proper time τ are the same for r = 1, the trajectory is described by X = cosh τ T = sinh τ

Now it’s very easy to compute the components of the acceleration. Using the properties of sinh and cosh, from these formulas one easily finds that a¹ = cosh τ a⁰ = sinh τ

Finally using the identity cosh² τ − sinh² τ = 1, we get |a|² = 1

Thus we indeed find that the magnitude of the acceleration is constant on the hyperbola corresponding to r = 1. The same is true (with a different acceleration) on each hyperbola of figure 14. We leave it as an exercise to prove it. More precisely, for an arbitrary r, the magnitude of the acceleration is |a| = 1 / r  (33)

Let’s come to questions of units, as we have already done in volume 3 of TTM. Equation (33) does not look consistent unit-wise. What is the unit of acceleration? It is length divided by time divided by time, i.e., [L]/[T]². Let’s rewrite this dimension as 1 / ([L][T]²)

It is clear that to restore the units in equation (33), all we need to do is introduce a factor c²: |a| = c² / r  (34)

This means that for a fixed radius r, at human scale - say, r = 1 meter - the acceleration of a particle (or an observer on the corresponding hyperbola) in figure 9 is extremely strong. We have to go to a very large r before we get to trajectories with a moderate acceleration.

By the way, the acceleration on a given trajectory in figure 14, for example the acceleration at point N on the hyperbola r = 2, is the ordinary acceleration. And it is the constant acceleration we would experience all along the trajectory.

Uniform Gravitational Field

We have introduced a somewhat arbitrary set of coordinates X, T for our stationary frame. In that set of coordinates, we are now going to write the equation of motion for a geodesic in the so-called accelerated coordinates r, ω. We will see that the equations look very much like a particle falling in a uniform gravitational field.

Let’s first talk about the metric of the Euclidean plane in ordinary polar coordinates as shown in figure 10: dS² = r² dθ² + dr²  (35)

The matrix for this two-dimensional metric has the form g_mn = [[r², 0], [0, 1]]  (36)

Why is it not the Kronecker-delta? It is not because the space is curved, but because the coordinates are curvilinear. The space itself is flat. Indeed, it is the plane, and we can go back to Cartesian coordinates (x, y) in which the metric is the Kronecker-delta.

Staying in the flat plane, the analog with the hyperbolic coordinates (r, ω) is dS² = r² dω² − dr²  (37)

We are still considering only two dimensions, the time T and one spatial coordinate X. For the moment we ignore Y and Z.

The particle of interest is falling in a gravitational field along an axis denoted X (in the usual Minkowski diagram it is horizontal, but we are used to it).

The coordinates Y and Z would be the other spatial coordinates. But they don’t matter for the problem we are discussing. The two coordinates that we will be interested in are u and r. Equation (37) is the metric.

Note: This might be a good place to go back and review what we did in lecture 1 when we looked at Newton’s equation in the frame of a uniformly accelerated elevator. We are going to do something similar, but in Minkowski space.

Recall from the previous section that the formula for the acceleration is c2. To be on familiar ground, we want to set this equal to g, the acceleration on the surface of the Earth, approximately 9.80 meters per second squared, but let’s use 10. It gives. We have to go out this distance from O to find an observer with acceleration g. The speed of light is c = 3 x 108 meters per second, so c2 is approximately 1017. That gives R equal to about 1016 meters. Therefore we have to go out ten thousand billion kilometers to find an observer with approximately the acceleration we are familiar with on the surface of the Earth.

So let’s go there!

And while there, if we don’t move too much along the r direction, the acceleration g = c2/R won’t change much. It is similar to moving on a vertical axis near the surface of the Earth: the gravitational field doesn’t change much.

We will now analyze what an observer in an elevator at position R is feeling when the elevator is accelerating uniformly (i.e., evolving in time along a hyperbola that is almost vertical). In figure 15, the spatial axis is horizontal, therefore the elevator is somehow on its side. But of course we should think of it as vertical - we are used to this presentation of the spatial axis in a Minkowski diagram. We will show that there is a fictitious gravity.

Since we are focusing on the vicinity of the point R, let’s introduce a new spatial coordinate y measuring the distance from R. In order to reach, in the vicinity of R, equations that look as much as possible like the Minkowski equations we are familiar with, we will also change the time variable.

We define y = r - R (38). All the observers with a small value of y have approximately the same acceleration g. Then we rewrite the metric of equation (37) using the new local coordinate y (note that dr = dy): dτ2 = (R2 + 2Ry + y2) dw2 - dy2 (39). Let’s present it as dτ2 = (1 + 2y/R + y2/R2) dw2 - dy2 (40). We will simplify it by focusing on a limited region around R.

One more step concerning coordinates: as said, we also introduce a new 对于每个坐标7，右侧有一系列项——准确地说是十项，因为7为了与相对论中的标准符号保持一致，最好使用i和y。我们留给读者在这些虚变量中换成通常的符号。

## 4. 测地线与引力

因为γ在μ和ν上是对称的。幸运的是，只要电梯运动缓慢，并且我们感兴趣的物体（即坐标为y的粒子）运动缓慢，它们中的大多数都极其小。在这些条件下，只有一种组合是显著的。

慢速运动下dt/dτ的值是多少？它本质上是1，因为在那种情况下，时间与原时几乎相同。

在方程(45)的右侧，微分元素是粒子四维速度的分量。我们刚刚看到本质上为1。

空间分量对τ的导数是什么？它们与它们的实际普通空间速度成正比。我们假设空间速度远小于光速，因此方程(45)右侧唯一重要的贡献来自τ和μ是时间指标的情况。让我们用t代替0表示时间指标。方程(45)简化为 (46)

右侧必须是引力。它必须是引力势能的导数。

让我们回到我们之前在方程(5)中看到的克里斯托费尔符号用度规表示的表达式，我们在此以略有不同的形式重写： Γᵖᵣₛ = ½ ( ∂gₚᵣ/∂xₛ + ∂gₚₛ/∂xᵣ - ∂gᵣₛ/∂xᵖ )

(47)

我们需要一个具有两个时间协变指标和一个空间逆变指标的符号。空间指标是y。在项gᵧᵧ中，唯一不可忽略的是gᵧᵧ，它等于1。由于t就是我们标记的t，xᵧ就是我们标记的y，我们得到 Γʸₜₜ = ½ ( ∂gᵧₜ/∂t + ∂gᵧₜ/∂t - ∂gₜₜ/∂y )

160 广义相对论和这两项为零。因此最终 Γʸₜₜ = -½ ∂gₜₜ/∂y 方程(46)可以改写为 d²y/dτ² = ½ ∂gₜₜ/∂y (48)

像(48)这样的方程，其中空间变量y对时间的二阶导数与某个量对y的一阶导数成正比，让我们想起具有势能的运动方程。不知何故，½gₜₜ必须是势能的相反数。但我们看到它确实是在m=1的情况下的负势能，也称为引力势。

在方程(42)中，即 dτ² = (1 + 2gy)dt² - dy² gₜₜ是定义dS²的度规中的系数(1 + 2gy)，它与dτ²相同，只是符号相反。因此，½ ∂gₜₜ/∂y = g。方程(48)最终变成 d²y/dτ² = -g (49)

这就是均匀引力场中粒子的运动方程。我们经历了一个相当复杂的推导才得到它，但在此过程中我们学到了以下几点：

## 1. 时空具有度规。在任意坐标中，度规可能具有相当复杂的结构。然而，在匀加速坐标中，它几乎是闵可夫斯基度规，只是方程(42)中多了额外的项2gy。

## 2. 时空中的测地线运动方程——至少在事物运动缓慢，即牛顿近似有效的情况下——就是均匀引力场中的牛顿方程。

8这意味着将分母中出现c的项设为0。

## 4. 测地线与引力

均匀引力场、恒定加速度、与-g的等效性等，正如我们所预期的。但为了正确分析物理，我们使用了度规、克里斯托费尔符号、测地线等，遵循了一个数学上相当繁琐的过程。

爱因斯坦猜到了它。粒子在时空中沿测地线运动的假设是他的起点，他沿着相反的方向前进。他知道匀加速坐标系，但不知道克里斯托费尔符号。在我们自己的推导过程中的某个地方，就是他开始的地方。对于匀加速——在牛顿近似下——度规简单地由方程(42)给出。

我们从第一讲出发，当时我们在平坦的牛顿空间中研究加速电梯，从而产生某种引力。我们已经证明，在闵可夫斯基-爱因斯坦时空中，匀加速参考系同样会产生有效的引力场。

但到目前为止，我们还没有涉及到真实的引力场。我们观察到的引力场不是真实的引力场，因为我们的整个分析发生在平坦时空中。

如果我们取方程(42)的度规并计算曲率张量，它将恰好为零，表明存在坐标使得度规具有简单形式dτ² - dX²。因此我们正在经历的引力实际上完全是由加速参考系引起的，而不是任何真实的引力物质。

我们可以猜测真实引力物质的影响。在方程(42)中，引力物体的引力势是什么？它是-G/y。

9按照惯例，对于均匀引力场，引力势在地面处取为零，并随高度增加到+∞，而对于物体产生的径向场，引力势在无穷远处取为零，并随半径趋于零而趋向-∞。这就是为什么y现在在分母中并且有一个负号。

162 广义相对论我们可以预期，当我们研究真实引力场的度规时，我们会得到类似这样的形式： dτ² = (1 - 2GM/y)dt² - dy² (50)

其中G是牛顿常数，M是引力物体的质量，如图17所示。

图17：质量为M的引力物体和引力势-G/y。

这几乎是史瓦西度规，但不完全。我们将推导出引力物体的史瓦西度规是什么。

方程(50)将导致一个奇怪的现象。当y很大时，项2GM/y很小。这是好的，因为(1 - 2GM/y)是正的。但当y等于2GM时，一些疯狂的事情发生了。dt²前面的系数变为零。系数改变符号的那个点y被称为黑洞的视界。

10对于地球，假设其所有质量几乎集中在一个点，视界将是9毫米。

真实的引力场和史瓦西度规将是下一讲的主题。我们不会完全从我们已知的内容推导度规。为了推导它，我们需要场方程。我们还没有讨论它们，直到第9讲才会讨论。

到目前为止，我们只讨论了几何、平坦、曲率、测地线等。当我们最终到达相对论的时空及其奇特的几何时，我们最终通过一个小示范展示了，在时空中的匀加速参考系中，沿测地线的运动如何产生牛顿方程。

在第5讲中，我们将最终进入一个时空，与我们在这里研究的不同，我们在这里只发现了基本上平坦时空中的有效11曲率，那里将有引力质量产生时空的真实曲率。

我们将开始研究黑洞，以及由这种东西产生的时空度规，因为黑洞是广义相对论中最简单的天体——相当于牛顿物理学中的质点。

11我们记住，有效是相对于真实而言的。

第5讲： 引力场度规 Andy：啊，我们现在来谈这个神秘的名字：史瓦西。这一直让我困惑。它是否意味着他是黑洞之子？

Lenny：不。但卡尔·史瓦西与爱因斯坦方程一起做了一些基础工作，得出了黑洞必须存在的假说。

Andy：但它们是什么？

Lenny：耐心点！它们就来了。然而，我们有一些工作先要做。

Andy：我能看到它们在视界上隐约出现。

类时、类空和类时间隔以及光锥测地线和欧拉-拉格朗日方程史瓦西度规黑洞黑洞的事件视界光的运动类时、类空和类时间隔以及光锥让我们从类时、类空和类时间隔开始。为此，我们回到狭义相对论来详细说明它的含义。

我们多次讨论过度规。我们称之为原时。原时的平方定义为 dτ² = dt² - dx² - dy² - dz² (1)

166 广义相对论记住方程(1)是在我们使用光速c=1的单位时原时的表达式。它的完整表达式显式地包含了光速为 dτ² = dt² - (dx² + dy² + dz²) (2)

对于时空的四个变量t, x, y, z，也可以使用更相对论的符号X⁰, X¹, X², X³。方程(1)变为 dτ² = (X⁰)² - (X¹)² - (X²)² - (X³)² (1')

方程(2)变为 dτ² = (X⁰)² - [(X¹)² + (X²)² + (X³)²] (2')

让我们也回忆一下，当我们使用带有拉丁指标的符号Xμ时，我们指的是三维空间坐标向量(X¹, X², X³)，而当我们使用带有希腊指标的符号Xμ时，我们指的是完整的四维向量(X⁰, X¹, X², X³)，其中指标为0的第一个坐标是时间。

图1：通常的闵可夫斯基图中的平坦时空，以及由四维向量dXμ表示的小位移。

有时在方程(2)中显式引入光速，或其具有相对论符号(2')的变体，理由是

## 5. 引力场度规

在特定情况下保持对什么是小和什么是大的跟踪。例如，如果我们想进入非相对论极限，即一切运动都很慢 ing slowly, it is good to put back c because it reminds us that it is much bigger than any other velocities in the problem. And it makes it easy to see which terms can be neglected and which cannot.

In what follows, unless it is necessary to show explicitly c, we will set it equal to 1. Notice that in the standard Minkowski diagram of special relativity, because we take c = 1, light rays have a slope at 45°.1 When we represent two spatial dimensions beside the time dimension, light cones have a generatrix tilted at 45°.

Let’s look at the sign of dr². Of course, when we look at real numbers, their square is always positive. But dr² is not defined as the square of a real number, it is defined by equation (1) or (2). It can be positive, null, or negative, depending on whether dx² + dy² + dz² is smaller than dt², equal to it, or bigger than it.

If dr² > 0, then the little element dX^μ in figure 1 on the preceding page is said to be time-like. It contains more time than it contains space, so to speak. Its vertical component is bigger than its horizontal component. Its slope is greater than 45°.

Figure 2: Time-like interval.

The time-like nature of dX^μ in this case, can also be described in terms of a light cone, shown in figure 2. If we represent two spatial coordinates x and y, in addition to the time coordinate t, and a light cone whose center is at X, then dr² > 0 means that the little 4-vector dX^μ lies in the interior of the cone. It could also lie in the backward direction in the same picture, pointing to the past. Either way, dX^μ is called a time-like interval.

1 One also meets an alternative diagram where instead of t the vertical axis charts ct, and light rays are still at 45° irrespective of the units.

168 General Relativity Space-like is exactly the opposite of time-like. It corresponds to dr² < 0, or equivalently dx² + dy² + dz² greater than dt². In that case, we usually define another quantity dS called the proper distance. Let’s temporarily reintroduce explicitly c to recall what it is. By definition the square of the proper distance is dS² = dx² + dy² + dz² — c²dt² (3)

When we are in units where c = 1, dS² has the same form as dr², shown in equation (1), except for a change of signs. Otherwise, in general, we have dS² = —c²dr².

Space-like vectors are those for which dS² > 0. If we represent as before the cone at X, a space-like little interval dX^μ is shown in figure 3.

Figure 3: Space-like interval.

Finally there are light-like vectors. They are those for which dr² = 0, and therefore equivalently dS² = 0. In the standard diagram, their slope is at 45°. They are trajectories of light rays, and they lie on the surface of the cone of figure 3.

Those are the three kinds of 4-vectors in Minkowski space.

Just for a moment, consider what it would mean if there were two positive signs and two negative signs instead of one positive sign, and three negative signs in the definition of the metric. This would correspond to two time dimensions. It doesn’t mean anything in physics. There are never two time dimensions. There is always one time and three space dimensions. Can you imagine a world with two times? Personally I cannot imagine what it would mean to have two different time dimensions. So we will simply take the view that it is not an option: there is always one time-like dimension in the metric of equation (1), or its variant forms, and three space-like.

That doesn’t mean that there is a unique direction that is time-like. There are many time-like directions pointing within the light cone of figure 2.

The invariant property, corresponding to the fact that at any point there is one time and three space variables, concerns the metric tensor. We are familiar with the expression of the metric tensor as follows: dr² = -g_μν dX^μ dX^ν (4)

The minus sign in front of g_μν is a convention. When we choose to use dS², the square of the infinitesimal proper distance, it is given by the same expression but without the minus sign.

Let’s stress the following important point about the proper time dτ, whose square is defined by equation (4): it is the time recorded by a clock accompanying the particle along its trajectory - its wristwatch if you will. In other words, it has a physical practical meaning, which is often useful to remember. Of course, for particles going slowly - and by “slowly” we mean up to thousands of miles per second - the proper time is essentially the same as the standard time t of the stationary observer in the stationary frame of figure 1. This is easily derived from equation (2), because c is very big compared to ordinary velocity, or to the spatial components of the 4-velocity. (Go to volume 3 of TTM on special relativity, if you need to brush up on these ideas.)

Similarly, the proper distance dS, along the trajectory of a particle, is distance measured by a meter stick carried along by the particle.

In summary, proper distance, √dS², really is a distance. And proper time, √dr², really is a time. Let’s keep that in mind.

Equation (3) is the definition of the metric with the coordinates (t, x, y, z). It can always be written in terms of a matrix. In 170 General Relativity this case (and we are back to c = 1), it is the matrix η_μν shown here η_μν = ( -1 0 0 0 )

( 0  1 0 0 )

( 0  0 1 0 ) (5)

( 0  0 0 1 )

Remember that it is the analog in Minkowski space of the Kronecker-delta, which is simply the unit matrix, in Euclidean space.

The matrix η_μν has obviously three positive eigenvalues and one negative eigenvalue. That is the invariant story: there is always only one negative eigenvalue in the metric. In special relativity as well as in general relativity, that will still be the case whatever the metric is and whatever the coordinate system is. Since the metric, in general, depends on the point in space-time where we look at it, this invariance statement will be true at any point.

A metric that would have two negative eigenvalues or three negative eigenvalues, would have more than one time dimension (not to be confused with a time-like direction, of which there are many - they are those inside the Minkowski cone2). We just don’t even think about several time dimensions. Several time axes is something that physics does not seem to have a use for.

The concepts of time-like, space-like, and light-like displacements are not restricted to special relativity. They apply generally whatever the metric, and whatever the point we consider. In the preceding discussion, we were in the flat space of special relativity, but the concepts apply in general relativity where the space is intrinsically not flat.

Now we shall consider a metric more general than η_μν. We denote it g_μν(X). At every X (i.e., every event in space-time), there is a matrix. Furthermore that matrix must have one negative and three positive eigenvalues. In other words, wherever you stand, you should experience a world with one time dimension and three space dimensions, or more exactly a metric with one negative eigenvalue and three positive.

2 Another name for the light cone.

## 5. Metric for a Gravitational Field

That means that every point in space has a light cone associated with it; see figure 4. These light cones can be tilted and change shape depending on the curvy aspect of the coordinates at each point.

Figure 4: Light cone at each point.

But at each point the metric has three positive and only one negative eigenvalue. And at each point there is the notion of time-like displacement, space-like displacement, and light-like displacement.

The property of having a certain number of eigenvalues positive and a certain number negative is called the signature of the metric. Recall that we already presented the concept of signature in lecture 4 (in the paragraph following equation (23) of that lecture). What is the signature of the metric of ordinary flat space? I’m not talking about ordinary space-time, I just mean the page you are reading. It is + + +. And the signature of the Minkowski metric in special relativity with three spatial coordinates is — + + +.

When somebody gives us a metric, or wherever we get it from - we might get it as a present in the mail, or we might have calculated it from some equations of motion, or some field equations - we should make sure that that metric has the signature — + + +. If it doesn’t, it means something’s wrong. Moreover, not only should we have that signature at some point, but we should have it at every point in space-time.

Notice that the shape of the light cone, in particular its angle of openness, is a pure coordinate issue; see figures 2, 3, and 4. In particular, if in the standard Minkowski metric and representation 172 General Relativity of figure 2, we chose units such that the speed of light is not 1, but for instance the huge number 3 x 10⁸, the cone would be extremely flat, and the picture not very useful. We already mentioned that in volume 3 on classical field theory and special relativity.

So much on the signature of the metric.

In this lecture, our ultimate objective is to study the metric around a massive body, and more specifically around a special kind of massive body: a black hole. But first, let’s revisit geodesics in space-time, deriving them in a different way than what we did before.

Geodesics and Euler—Lagrange Equations We learned in lecture 4 the definition of a geodesic in space-time.3 We used the corresponding equation - equation (19) of lecture 4 - in the example of a free particle moving in a uniformly accelerated reference frame. A geodesic is a curve whose tangent vector stays parallel to itself all along the curve. Said in another, more informal way, it is a trajectory where we always go straight.

In this lecture, we are going to use a different definition, which in many ways is more useful. But let us first recall the original definition:4 d²X^μ/dτ² + Γ^μ_ρσ (dX^ρ/dτ) (dX^σ/dτ) = 0 (6)

The left-hand side is the derivative of the tangent vector along so me curve, which all along the curve should be equal to the double sum involving Christoffel symbols of the right-hand side. That is the standard definition of a geodesic.

A geodesic in ordinary curved space, i.e., Riemannian space, is a rather intuitive concept: it is a curve that minimizes ordinary distance. On Earth, for instance, it is a portion of great circle. In space-time it is less intuitive. We already gave a technical definition related to “straightness,” and mentioned others in lecture 4. We will now study it as the result of a minimization problem.

It was equation (19) of chapter 4. Here we write it with r instead of S, and with the more explicit expressions for the tangent vector components on the right-hand side.

Remember that in lecture 4, we also mentioned another: it is the analog of the definition of a geodesic in ordinary space, that is, the curve of shortest distance between two points. Or better yet, it is the curve between two points whose length is stationary. Remember too that on a geodesic the covariant derivative of the tangent vector is everywhere zero.

Another way to arrive at equation (6) is to “extremelize” - by that I mean make minimum - the length of the curve between two points.

Let’s start with ordinary space to refresh our memory on geodesics. So we are on the page of this book, or a curved version of the page with hills and valleys, for instance after it stayed in the rain and then dried. We take two points in that space and any curve between them, as shown in figure 5. We calculate the distance along the curve.

Figure 5: Determination of a geodesic between A and B. When the space is flat, it is the straight segment joining them.

Then we search for the curve that minimizes its length, denoted shortest curve on the figure.

How to calculate it? Let’s spell out the logic. We start, as said, with any curve C between A and B. There are plenty of them shown in grey in figure 5. On that selected curve C, whichever it is, for each little segment along the curve, we have

dS² = gₘₙ(X) dXᵐ dXⁿ (7)

dS = √gₘₙ(X) dXᵐ dXⁿ (8)

This is just Pythagoras theorem applied to a little segment on curve C. Then we add them all up. This gives the distance along the curve C we have selected:

S = ∫ √gₘₙ(X) dXᵐ dXⁿ (9)

along curve C

Finally we look for the curve C that makes S minimum or extremum. That’s the logic. By now we are familiar with the mathematics that implements this logic. We learned it in volume 1 of TTM on classical mechanics. It is a problem in calculus of variation, analogous to minimizing the action of a particle along a trajectory.

In other words, we can think of equation (9) as expressing the action of a particle moving from A to B along curve C. Then the rule for calculating the geodesic is to “extremelize” that quantity, or more accurately to make it stationary. The equation that tells us how to minimize a quantity like S in equation (9) is called the Euler-Lagrange equation.

When we go from the principle of least action to the Euler-Lagrange equation, the principle of least action turns into a differential equation involving a Lagrangian. Typically, when rewritten as explicitly as possible, the Euler-Lagrange equation becomes an equation of the type F = ma. Going from minimizing the quantity in equation (9) to equation (6) is exactly the same operation. In fact equation (6) looks like equating an acceleration to something. That thing is a kind of force.

Now let’s come back to relativity and to our actual problem of geodesic, where we are not concerned with ordinary distance but with proper distance, or equivalently proper time. If we want to express the quantity to be minimized, which involves proper time, we deal with almost exactly the same expression as in equation (9) except for a minus sign in front of the metric. From equation (4) we find that the proper time between point 1 and point 2 in space-time is given by

∫ √-gₘₙ(X) dXᵐ dXⁿ (10)

This is the expression that we will want to minimize. Notice that a time-like geodesic maximizes proper time (it is one of the explanations of the twin paradox). The usual definition of action is proportional to minus the proper time:

action = -m ∫ √-gₘₙ(X) dXᵐ dXⁿ

Minimizing action means maximizing expression (10).

Let’s suppose that the expression defined by equation (10) really corresponds to the motion of a particle that starts at point 1 and ends at point 2 in space-time, as in figure 6. The action we are interested in depends on one more quantity. It depends on the mass m of the particle. The actual action then is

A = -m ∫ √-gₘₙ(X) dXᵐ dXⁿ (11)

This is a definition of the mass. We will find out that putting a coefficient called mass here is important for thinking about energy and so forth; and the minus sign is strictly a convention in the definition of mass. We want to make this action A stationary.

What do we do with the right-hand side of equation (11)? A priori it is a completely unrecognizable object to work on with our mathematical toolbox. That is, it is just a sum of infinitely many infinitely small elements. But where is the differential element? What is the variable to integrate over? Usually for us, an integral we know how to calculate, or at least manipulate, has the form

∫ F( some variable ) d some variable

where the variable may be some spatial quantity or may be time, or some other clearly identified physical quantity. Normally we don’t see integrals where beneath the integral there is a square root, and inside the square root there is a product of differentials like dXᵐ dXⁿ. Remember that we already met the same kind of integral in volume 3 on special relativity.

Figure 7: Breaking the trajectory into little time segments dt.

To start with, let’s break up the trajectory of the particle into little time segments dt, as in figure 7. Equation (11) becomes

A = -m ∫ √-gₘₙ(X) (dXᵐ/dt) (dXⁿ/dt) dt² (12)

Some of the differentials dX^μ are in fact dt, because t is one of the four coordinates in X^μ = (t, x, y, z). Remember that we set c = 1; otherwise X^μ would be (ct, x, y, z). That would produce a coefficient c² in factor next to the mass m. We will reinsert c² in the next section when we study the Schwarzschild metric.

What happens when we have dt/dt? It is just 1. And what happens when we have dx/dt or the analog with y or z? It is just the ordinary velocity. We can also pull dt² out of the square root and obtain a standard differential element dt in the integral:

A = -m ∫ √-gₘₙ(X) (dXᵐ/dt) (dXⁿ/dt) dt (13)

At each time t, the quantity √-gₘₙ(X) (dXᵐ/dt) (dXⁿ/dt) which is integrated over time, has a definite value along the trajectory. It is a certain function of the velocity and the position X. Thus we have transformed our expression (11) for the action into a conventional integral over time along the trajectory in figure 7.

The integrand in equation (13) (where we put m back beneath the integral sign) is the Lagrangian. It is the quantity that, in the calculation of a geodesic, plays exactly the same role as the Lagrangian when we apply the principle of least action to calculate the trajectory of a particle in classical non-relativistic physics. Action, by definition, is equal to the integral of the Lagrangian, which is itself a function of velocities and positions:

A = ∫ L(X, Ẋ) dt (14)

In summary, “extremelizing” the action given by equation (13) brings us back to a problem that we already met in classical mechanics, in volume 1. How do we find an equation of motion from an action? In order to do that, we solve the Euler-Lagrange equation (or equations) that the Lagrangian must satisfy.

In our present problem, the Lagrangian is

L = -m √-gₘₙ(X) (dXᵐ/dt) (dXⁿ/dt) (15)

Incidentally, is the quantity inside the square root positive? Can we take its square root, even though there is a minus sign in front of it? Answer: yes, it is positive. The quantity -gₘₙ(X) dXᵐ dXⁿ is the square of the proper time over a small element dX along the trajectory; see equation (1). It is always positive for a time-like trajectory. And, as we already said in lecture 4 (as well as in many places in volume 3), particles always move on time-like trajectories. It is equivalent to saying that they never exceed the speed of light.

This is a point worth stressing: Particles do not move faster than the speed of light. Therefore, on the standard Minkowski diagram, the trajectory of a particle never has a tangent with a slope lower than 45°. The simplest example of course is a particle that doesn’t move in the referential of the Minkowski diagram: its trajectory in space-time is vertical. We also saw that fact with the hyperbolas on which a collection of observers were moving simultaneously when we studied the concept of uniform acceleration in lecture 4. That is why in figures 6 and 7 we were careful to draw curves with tangents always higher than 45°.

To finish on this remark: a space-like trajectory would be one where the point moves faster than the speed of light. But this is impossible. Thus on a space-like interval (for instance the simplest one: a horizontal segment), we necessarily see many different particles (this is obvious also because the time is the same).

Let’s recall what are the Euler-Lagrange equations that the Lagrangian must satisfy. First of all we are going to partially differentiate L with respect to each of the variables X^μ. But the first of these variables, which is the derivative of time with respect to time, is just 1. There is no corresponding equation. We are only

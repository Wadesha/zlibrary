# Gateway to Mathematics s00004 006 0017 7

> 来源文件：pre_Gateway_to_Mathematics_s00004_006_0017_7.txt
> 字符数（约）：13659
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Paul Calter Research 108 Bluebird Lane Randolph Center, VT 05061 USA pcalter@sover.net

Gateway to Mathematics: Equations of the St. Louis Arch

Abstract. Eero Saarinen's Gateway Arch in St. Louis has the form of a catenary, that is, the form taken by a suspended chain. The catenary can be reproduced empirically, but it can also be precisely formulated mathematically. The catenary is similar to the paraboloid in shape, but differs mathematically. Catalan architect Antoni Gaudi used the catenary to great effect in his Church of the Sagrada Familia in Barcelona, but he also used the paraboloid as well.

keywords: arch, St. Louis Arch, Eero Saarinen, Gateway to the West, Gateway Arch, catenary, parabola, hanging chain

An arch consists of two weaknesses which, leaning one against the other, make a strength.

Leonardo da Vinci

Introduction

When building a circular masonry arch, a builder was likely to construct a wooden form on which the stones or bricks were laid, the shape being traced with pegs and string or a radius bar. But for larger arches, and those made of steel, fabricated at a steelyard and assembled on-site, it is useful to work from an equation. If fact, equations of geometric figures like the circle were not even available until René Descartes developed analytic geometry in the seventeenth century.

Fig. 1.

An equation of the arch will give the height y of any point on the arch at a given horizontal distance x. Both distances are measured from chosen axes. An equation is, of course, meaningless unless one knows the x and y axes, and the origin, the point where they intersect.

For example, here are the equations for the circular, pointed, parabolic and elliptical arches shown in fig. 1, if the axes are placed as shown. Changing the position of an axis would change the equation.

Circular: y = √(r² - x²)

Pointed: y = √(r² - x²)

Elliptical: y = b √(1 - x²/a²)

Parabolic: y = kx²

Note that for the parabola, we have taken the origin at the vertex of the curve, and the positive y axis vertically downward.

Turning to the St. Louis arch, note that we have three curves, for the intrados, the extrados, and the centerline (fig. 2). What I call the centerline is the curve connecting the centroids of the cross-section.

Fig. 2.

The cross-section of the arch is an equilateral triangle, whose centroid is at the intersections of the three medians (fig. 3). For an equilateral triangle, that same point is also the orthocenter (the intersections of the altitudes) the incenter (intersection of the angle bisectors) and, for good measure, the circumcenter (intersection of the perpendicular bisectors of the sides.)

Fig. 3.

The Catenary

The published equation of the centerline of the St Louis arch, with the constants rounded to three digits, is y = 68.8(cosh 0.01x - 1)

Let us break it down. First, what is a cosh? It is one of the six hyperbolic functions. The hyperbolic functions are analogous to the circular functions, but are based on the hyperbola rather than the circle. In particular, the hyperbolic cosine is defined as cosh ax = (e^(ax) + e^(-ax)) / 2

So with a = 0.01, our arch equation becomes y = 68.8( (e^(0.01x) + e^(-0.01x)) / 2 - 1 )

Fig. 4 shows the graph of that equation. Notice that the curve opens upwards, but we can correct that simply by inverting the curve. We then take the origin at the high point, with the y axis downward and along the centerline of the curve.

Fig. 4.

The constants in the arch equation, 68.8, 0.010, 2, and –1, serve to scale the curve to the proper height and width, and to shift the curve vertically. Let us disregard them, just for now, and try to make sense of the catenary equation.

To our arch equation, in simplified form becomes y = e^x + e^(-x)

Now this equation may still be daunting to some, so I will try to break it down, explain each piece, and then put it back together.

Exponential Growth

Let us start with that letter e. It is not like the constant a in our earlier equation, that stands for any constant value. It is a very special number, and has a particular value.

There are different ways to arrive at the value of this number e, but perhaps the most intuitive starts with the familiar idea of compound interest, like that given by a bank.

If you invest P dollars at an interest rate n, you would have an amount y after x years, y = P(1+n)^x dollars

For example, $500 invested at 6.5% for 8 years gives y = 500(1+0.065)^8 = $827.50

For this example, the interest was compounded once a year.

Now suppose we compound interest m times per year. We would now have mx interest periods, but for each the interest rate would be n/m.

y = P(1 + n/m)^(mx)

Repeating our example with int Interest compounded monthly gives y = 500(1 + 0.065/12)^12 = $893.83 or another $12.33.

Fine, but what does this have to do with the number e? We will see if we now ask, what if the interest were not computed in discrete steps, but continuously? Suppose m were not 12 or 365 or 1000, but infinite.

Let us make the substitution k = m, so that our equation for compound interest becomes y = P(1 + 1/k)^(knx), which can be written y = P[(1 + 1/k)^k]^(nx).

Now as m gets very large, and k also gets very large, what happens to the quantity inside the brackets? Let us calculate some values.

k       1 + 1/k       (1 + 1/k)^k 1       2.0000000000  2.00000 10      1.1000000000  2.59374 100     1.0100000000  2.70481 1000    1.0010000000  2.71692 10000   1.0001000000  2.71815 100000  1.0000100000  2.71827 1000000 1.0000010000  2.71828 We get the surprising result that as m becomes infinite, the value of the expression in the brackets settles down to a specific value, about 2.7183. That value is called e.

Now replacing (1+1/k)^k by e in our formula for compound interest gives the formula for continuous growth or exponential growth: y = Pe^(nx).

Does that look familiar? Its one of the expressions in our arch equation, with P = 1 and n = 1.

Populations offer an example of exponential growth; the greater the population the faster it grows, or The rate of growth is proportional to the amount.

Fig. 5 is a graph of exponential growth, with P = 1 and n = 1.

Exponential Decay Now lets look at the other term in the catenary equation, e^(-x). The minus sign in the exponent is all that is needed to change the equation from describing exponential growth into one that describes exponential decay (fig. 6).

As an example, take a hot cup of coffee. It is the temperature difference between the coffee and the room air that drives heat out of the coffee. As the coffee cools, the temperature difference decreases, so the rate of temperature drop decreases. As with population growth, The rate of change of temperature is proportional to the temperature T.

In calculus notation, dT/dt = kT The Hanging Chain Now let us plot the growth and decay curves on the same axes, and also graph their sum. Note that the sum of the growth and decay curves combine to form the catenary.

The seventeenth-century Dutch mathematician Christian Huygens named the curve catenarius, after the Latin word for chain. The reason for that name is that this curve describes the shape of a uniform chain or flexible rope hanging from two points.

What does a hanging chain have to do with exponential growth and decay?

Let us look at the forces on a small section of cable. Fig. 7 shows the tensions TU and T resolved into vertical and horizontal components.

We note the following: – The two horizontal forces H must be equal and opposite, as there are no other horizontal forces acting on this section of cable.

– The vertical force V is equal to half the weight of the cable below that point, the other half being supported on the right-hand side.

– As we go lower along the cable, the vertical force V decreases a constant amount for each foot of cable.

– As the vertical force decreases, the angle θ of the resultant decreases, as the horizontal force H is constant.

Thus the slope of the curve decreases as we move along it, so the rate of change in vertical distance is proportional to the distance along the curve. But for steeper parts of the curve, the vertical displacement is approximately equal to the distance along the curve (fig. 8).

The rate of change of vertical distance is approximately proportional to the vertical distance.

Comparing this with temperature drop in our coffee cup, we saw that The rate of change of temperature was proportional to the temperature T of the coffee.

In calculus notation, For drop in temperature: For drop in height: dT/dt = kT ≅ dy/dx = ky So the descending portion of the curve, at least where it is steep, behaves something like exponential decay. In a similar way we can show that the rising portion of the curve exhibits some characteristics of exponential growth.

Why use a catenary for the St. Louis Arch?

With the hanging chain, the weight of the links gets resolved into tensions that always act along the curve, and never at right angles to it. There is pure tension throughout. Similarly for the catenary arch, the weight of the arch acts along the centerline of the arch, and there are no shear forces perpendicular to the centerline.

Why is a hanging chain described by the catenary equation?

We glibly stated that a hanging chain follows the catenary curve, but why? The proof of that statement is a standard problem in many mechanics or differential equation textbooks. This one is from Murray Spiegel’s Applied Differential Equations.

Equations, Prentice-Hall, 1958.

We start with a bit of chain or rope with one end at the low point C of the curve. It is acted on by three forces, H, W, and T (fig. 9).

From the equations of equilibrium, Tsinθ=W Tcosθ= H

Dividing gives sinθ W dy =tanθ= =slope at P= cosθ H dx

Taking the derivative, noting that H is a constant d2y 1 dW = (1)

dx2 H dx

Here is the change in load per unit horizontal distance. We will do two derivations: one for the suspension bridge and another for the catenary.

For a suspension bridge for which the weight of the cable is negligible compared to the weight of the roadway, this change in load is constant, and equal to the weight per foot of the roadway, which I’ll call w (fig. 10). Then Eq. (1) becomes d2y w dx2 H

Integrating gives dy w = x+C dx H

But dy/dx = 0 at x = 0, so C1 = 0. Integrating again, y= x2 +C 2H

We can now shift the y axis so that y = 0 at x = 0. Then C 2 will be zero. So, replacing the constant w/2H by k, we get the equation of a parabola y =kx2

Turning now to the catenary, the load per unit distance along the curve, dW/ds, is constant, and has the value w, but the load per unit horizontal distance is not constant. For the steeper parts of the curve, the load per unit horizontal distance is greater than for less steep portions.

So we must write an expression for dW/dx as a function of x.

dW ⎛dW ⎞⎛dx⎞ =w=⎜ ⎟⎜ ⎟ ds ⎝ dx ⎠⎝ds⎠

So, dW ds =w (2)

dx dx

Now let us look at a section of the curve so small that it can be considered straight (fig. 11).

By the Pythagorean theorem, 2 2 2 ⎛ds⎞ ⎛dy⎞ ⎛dx⎞ ⎜ ⎟ =⎜ ⎟ +⎜ ⎟ ⎝dx⎠ ⎝dx⎠ ⎝dx⎠

from which, with dx/dx = 1, ds ⎛dy⎞ = ⎜ ⎟ dx ⎝dx⎠

So from (2), dW ⎛dy⎞ =w 1+⎜ ⎟ dx ⎝dx⎠

Substituting into (1) gives d2y w ⎛dy⎞ 2 = 1+⎜ ⎟ (3)

dx2 H ⎝dx⎠

Here we have a second-order differential equation which we now solve for y. Let dp H = p and =C dx w

So (3) becomes dp 1 = 1+ p2 dx C

Separating variables, c dp =dx 1+ p2

Integrating, using a rule from a table of integrals, In⎜ ⎛ p+ p2 +1⎟ ⎞ = x +C ⎝ ⎠ C

But p= dy/dx =0 at x = 0, so C= 0. Going to exponential form, p+ p2 +1=exC

We now solve this equation for p. First we isolate the radical: p2 +1=exC − p

Squaring both sides, p2 +1=e2xC −2pexC + p2 2pexC =e2xC −1 1⎛e2xC ⎞ p= ⎜ −e−xC⎟ 2⎜ exC ⎟ 1( ) dy p= exC −e−xC = 2 dx

Replacing p by dy/dx and integrating again, y= C ∫exC ⎜ ⎛dx ⎟ ⎞ − −C ∫e−xC ⎜ ⎛−dx ⎟ ⎞ 2 ⎝ C ⎠ 2 ⎝ C ⎠ C( )

y= exC +e−xC +C

We can shift the y axis so that C= 0. Our equation then becomes ⎛exC +e−xC ⎞ y=C⎜ ⎟, ⎜ 2 ⎟ ⎝ ⎠

the equation of the catenary.

Catenary and parabola compared

If we draw a parabola that has the same height and width as the St. Louis arch would have the equation y=0.00699x2

Fig. 12 shows this equation plotted together with the actual arch equation.

Notice that the catenary is flatter than the parabola. This is due to the weight distribution for each.

The suspension bridge has the same weight per horizontal foot, while the catenary does not. There is relatively more weight away from the centerline, where the curve is steeper. Thus there is more chain in each one-foot interval towards the ends than at the center. This tends to make the catenary lower away from the centerline.

About the author

Paul A. Calter is Professor Emeritus of Mathematics at Vermont Technical College. He has interests in both the fields of mathematics and art. He received his B.S. from Cooper Union and his M.S. from Columbia University, both in engineering, and his Masters of Fine Arts Degree at Vermont College of Norwich University. Calter has taught mathematics for over twenty-five years and is the author of ten mathematics textbooks and a mystery novel. He has been an active painter and sculptor since 1968, has participated in dozens of art shows, and has permanent outdoor sculptures at a number of locations in Vermont. Calter developed the Mathematics Across the Curriculum course "Geometry in Art & Architecture" and has taught it at Dartmouth and Vermont Technical College, as well as giving workshops and lectures on the subject. He presented a paper on the survey of a doorway by Michelangelo in the Laurentian Library in Florence at the Nexus 2000 conference on architecture and mathematics. Calter developed a trigonometric method for non-contact measurements of facades and presented his method at the first Nexus conference in 1996. His book, Squaring the Circle: Geometry in Art and Architecture, is due out in January 2007.

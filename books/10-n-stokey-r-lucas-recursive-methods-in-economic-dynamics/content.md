# Recursive Methods in Economic Dynamics (Stokey & Lucas)
> hy3 忠实校订

economic models.
Today, in every field of application, we have theories that deal explicitly with rational economic agents operating through time in stochastic environments.
The idea of an economic equilibrium has undergone a similar evolution: it no longer carries the connotation of a system at rest.
Powerful methods are now available for analyzing theoretical models with equilibrium outcomes described by the same kinds of complicated stochastic processes that we use to describe observed economic behavior.
These theoretical developments are based on a wide variety of results in economics, mathematics, and statistics: the contingent-claim view of economic equilibria introduced by Arrow (1953) and Debreu (1959), the economic applications of the calculus of variations pioneered long ago by Ramsey (1928) and Hotelling (1931), the theory of dynamic programming of Bellman (1957) and Blackwell (1965).
Our goal in this book is to provide self-contained treatments of these theoretical ideas that form the basis of modern economic dynamics.
Our approach is distinguished by its systematic use of recursive methods, methods that make it possible to treat a wide variety of dynamic economic problems—both deterministic and stochastic—from a fairly unified point of view.
To illustrate what we mean by a recursive approach to economic dynamics, we begin with a list of concrete examples, drawn from the much longer list of applications to be treated in detail in later chapters.
These examples also serve to illustrate the kinds of substantive economic questions that can be studied by the analytical methods in this book.
First consider an economy that produces a single good that can be either consumed or invested.
The quantity consumed yields immediate utility to the single decision-maker, a “social planner.” The quantity invested augments the capital stock, thereby making increased production possible in the future.
What is the consumption—investment policy that maximizes the sum of utilities over an infinite planning horizon?
Next consider an economy that is otherwise similar to the one just described, but that is subject to random shocks affecting the amount of output that can be produced with a given stock of capital.
How should the consumption-investment decision be made if the objective is to maximize the expected sum of utilities?
Suppose a worker wishes to maximize the present value of his earnings.
In any period he is presented with a wage offer at which he can work one unit of time or zero.
If he works, he takes the earnings and retains the same job next period.
If he does not work, he searches, an activity that yields him a new wage offer from a known probability distribution.
What decision rule should he adopt if his goal is to maximize the expected present discounted value of his lifetime earnings?
A store manager has in stock a given number of items of a specific type.
Demand is stochastic, so in any period he may either stock out and forgo the sales he would have made with a larger inventory or incur the costs of carrying over unsold items.
At the beginning of each period he can place an order for more items.
The cost of this action includes a fixed delivery charge plus a charge per item ordered.
The order must be placed before the manager knows the current period demand.
If his goal is to maximize the expected discounted present value of profits, when should he place an order; and when an order is placed, how large should it be?
An economy is endowed with a fixed number of productive assets that have exogenously given yields described by a stochastic process.
These assets are privately owned, and claims to all of them are traded on a competitive equities market.
How are the competitive equilibrium prices in this market related to consumer preferences over consumption of goods and to the current state of the yield process?
How is the answer to this question altered if assets can be produced?
A monopolist faces a stochastically shifting demand curve for his product.
His current production capacity is determined by his past investments, but he has the option to invest in additions to capacity, additions that will be available for production in the future.
What investment strategy maximizes the expected discounted present value of profits?
Alternatively, suppose there are many firms in this industry.
In competitive equilibrium what are the investment strategies for all of these firms, and what do they imply for the behavior of industry production and prices?
These problems evidently have much in common.
In each case a decision-maker—a social planner, a worker, a manager, an entire market, a firm, or collection of firms—must choose a sequence of actions through time.
In the first example there is no uncertainty, so the entire sequence may as well be chosen at the outset.
In the other five examples the environment is subject to unpredictable outside shocks, and it is clear that the best future actions depend on the magnitudes of these shocks.
Consider how we might formulate each of these problems mathematically and what we might mean by a recursive approach to each.
The first example is the problem of optimal savings that Frank Ramsey formulated and solved in 1928.
Ramsey viewed the problem as one of maximizing a function (total utility) of an infinity of variables (consumption and capital stock at each date) subject to the constraints imposed by the technology.
He set up the problem in continuous time and applied the calculus of variations to obtain a very sharp characterization of the utility-maximizing dynamics: the capital stock should converge monotonically to the level that, if sustained, maximizes consumption per unit of time.
In the Ramsey problem the feature of the production possibility set that changes over time is the current stock of capital.
This observation suggests that an alternative way preferences take the additively separable form (2) Σ_{t=0}^∞ β^t U(c_t) where the discount factor is 0 < β < 1, and where the current-period utility function U: R+ → R is bounded, continuously differentiable, strictly increasing, and strictly concave, with lim_{c→0} U'(c) = ∞.
Households do not value leisure.
Now consider the problem faced by a benevolent social planner, one whose objective is to maximize (2) by choosing sequences {(c_t, k_{t+1}, l_t)}_{t=0}^{∞} subject to the feasibility constraints in (1), given k_0 > 0.
Two features of any optimum are apparent.
First, it is clear that output will not be wasted.
That is, (1b) will hold with equality for all t, and we can use it to eliminate c_t from (2).
Second, since leisure is not valued and the marginal product of labor is always positive, it is clear that an optimum requires l_t = 1, all t.
Hence c_t and y_t represent both capital and output per worker and capital and output in total.
It is therefore convenient to define f(k) = F(k, 1) + (1 — δ)k to be the total supply of goods available per worker, including undepreciated capital, when beginning-of-period capital is k.
Exercise 2.1 Show that the assumptions on F above imply that f: R+ → R is continuously differentiable, strictly increasing, and strictly concave, with f(0) = 0, f'(k) > 0, lim_{k→0} f'(k) = ∞, lim_{k→∞} f'(k) = 1 - δ.
The planning problem can then be written as (3) max Σ_{t=0}^∞ β^t U(c_t) {(c_t,k_{t+1})}_{t=0}^{∞} (4) s.t. 0 ≤ k_{t+1} ≤ f(k_t) - c_t, t = 0,1,..., k_0 > 0 given.
Although ultimately we are interested in the case where the planning horizon is infinite, it is instructive to begin with the (much easier!) problem of a finite horizon.
If the horizon in (3) were a finite value T instead of infinity, then (3)—(4) would be an entirely standard concave programming problem.
With a finite horizon, the set of sequences {k_{t+1}}_{t=0}^{T} satisfying (4) is a closed, bounded, and convex subset of R^{T+1}, and the objective function (3) is continuous and strictly concave.
Hence there is exactly one solution, and it is completely characterized by the Kuhn-Tucker conditions.
To obtain these conditions note that since f(0) = 0 and U'(0) = ∞, it is clear that the inequality constraints in (4) do not bind except for k_{T+1}, and it is also clear that k_{T+1} = 0.
Hence the solution satisfies the first-order and boundary conditions (5) β^t f'(k_t) U'(f(k_t) — k_{t+1}) — U'(c_{t-1}) = β^{t-1} [f'(k_t) — 1], t = 1,2,...,T, (6) k_{T+1} = 0, k_0 > 0 given.
Equation (5) is a second-order difference equation in k_t, hence it has a two-parameter family of solutions.
The unique optimum for the maximization problem of interest is the one solution in this family that in addition satisfies the two boundary conditions in (6).
The following exercise illustrates how (5)—(6) can be used to solve for the optimum in a particular example.
Exercise 2.2.
Let f(k) = k^α, 0 < α < 1, and let U(c) = ln(c).
(No, this does not fit all of the assumptions we placed on f and U above, but go ahead anyway.) a.
Write (5) for this case and use the change of variable z_t = k_{t+1}/k_t to convert the result into a first-order difference equation in z_t.
Plot z_{t+1} against z_t and plot the 45° line on the same diagram. b.
The boundary condition (6) implies that z_T = 0.
Using this condition, show that the unique solution is z_t = 1 — (αβ)^{T-t+1}, t=1,2,...,T+1. c.
Check that the path for capital (7) k_{t+1} = αβ k_t [1 — (αβ)^{T-t}] / [1 — (αβ)^{T-t+1}], t=0,1,...,T, given k_0, satisfies (5)—(6).
Now consider the infinite-horizon version of the planning problem in Exercise 2.2.
Note that if T is large, then the coefficient of k_t in (7) is essentially constant at αβ for a very long time.
For the solution to the infinite-horizon problem, can we not simply take the limit of the solutions in (7) as T approaches infinity?
After all, we are discussing households that discount the future at a geometric rate!
Taking the limit in (7), we find that (8) k_{t+1} = αβ k_t, t = 0,1,...
In fact, this conjecture is correct: the limit of the solutions for the finite-horizon problems is the unique solution to the infinite-horizon problem.
This is true both for the parametric example in Exercise 2.2 and for the more generally posed problem.
But proving it involves establishing the legitimacy of interchanging the operators “max” and “lim_{T→∞}”; and doing this is more challenging than one might guess.
Instead we will pursue a different approach.
Equation (8) suggests another conjecture: that for the infinite-horizon problem in (3)—(4), for any U and f, the solution takes the form (9) k_{t+1} = g(k_t), t=0,1,..., where g: R+ → R+ is a fixed savings function.
Our intuition suggests that this must be so: since the planning problem takes the same form every period, with only the beginning-of-period capital stock changing from one period to the next, what else but k_t could influence the choice of k_{t+1} and c_t?
Unfortunately, Exercise 2.2 does not offer any help in pursuing this conjecture.
The change of variable exploited there is obviously specific to the particular functional forms assumed, and a glance at (5) confirms that no similar method is generally applicable.
The strategy we will use to pursue this idea involves ignoring (5) and (6) altogether and starting afresh.
Although we stated this problem as one of choosing infinite sequences {(c_t, k_{t+1})}_{t=0}^{∞} for consumption and capital, the problem that in fact faces the planner in period t = 0 is that of choosing today’s consumption, c_0, and tomorrow’s beginning-of-period capital, k_1, and nothing else.
The rest can wait until tomorrow.
If we knew the planner’s preferences over these two goods, we could simply maximize the appropriate function of (c_0, k_1) over the opportunity set defined by (1b), given k_0.
But what are the planner’s preferences over current consumption and next period’s capital?
Suppose that (3)—(4) had already been solved for all possible values of k_0.
Then we could define a function v: R+ → R by taking v(k_0) to be the value of the maximized objective function (3), for each k_0 ≥ 0.
A function of this sort is called a value function.
With v so defined, v(k_1) would give the value of the utility from period 1 on that could be obtained with a beginning-of-period capital stock k_1 and β v(k_1) would be the value of this utility discounted back to period 0.
Then in terms of this value function v, the planner’s problem in period 0 would be (10) max [U(c_0) + β v(k_1)] {c_0,k_1} s.t. c_0 + k_1 = f (k_0), c_0, k_1 ≥ 0, k_0 > 0 given.
If the function v were known, we could use (10) to define a function g: R+ → R as follows: for each k_0 ≥ 0, let k_1 = g(k_0) and c_0 = f (k_0) — g(k_0) be the values that attain the maximum in (10).
With g so defined, (9) would completely describe the dynamics of capital accumulation from any given initial stock k_0.
We do not at this point “know” v, but we have defined it as the maxi14 2 / An Overview mized objective function for the problem in (3)—(4).
Thus, if solving (10) provides the solution for that problem, then v(k_0) must be the maximized objective function for (10) as well.
That is, v must satisfy v(k_0) = max {U[f (k_0) — k_1] + β v(k_1)}, {c_0,k_1} where, as before, we have used the fact that goods will not be wasted.
Notice that when the problem is looked at in this recursive way, the time subscripts have become a nuisance: we do not care what the date is.
We can rewrite the problem facing a planner with current capital stock k as (11) v(k) = max {U[f(k) — y] + β v(y)}. {y} This one equation in the unknown function v is called a functional equation, and we will see later that it is a very tractable mathematical object.
The study of dynamic optimization problems through the analysis of such functional equations is called dynamic programming.
If we knew that the function v was differentiable and that the maximizing value of y—call it g(k)—was interior, then the first-order and envelope conditions for (11) would beU'[f(R) - g(k)] = βU'[g(k)], and (v = f'(R)U'(F(A) - gC')) respectively.
The first of these conditions equates the marginal utility of consuming current output to the marginal utility of allocating it to capital and enjoying augmented consumption next period.
The second condition states that the marginal value of current capital, in terms of total discounted utility, is given by the marginal utility of using the capital in current production and allocating its return to current consumption.
Exercise 2.3 We conjectured that the path for capital given by (8) was optimal for the infinite-horizon planning problem, for the functional forms of Exercise 2.2. a.
Use this conjecture to calculate v by evaluating (2) along the consumption path associated with the path for capital given by (8). b.
Verify that this function v satisfies (11).
Suppose we have established the existence of an optimal savings policy either by analyzing conditions (5)—(6) or by analyzing the functional equation (11).
What can we do with this information?
For the particular parametric example in Exercises 2.2 and 2.3, we can solve for g with pencil-and-paper methods.
We can then use the resulting difference equation (8) to compute the optimal sequence of capital stocks {k_t}.
This example is a carefully chosen exception: for most other parametric examples, it is not possible to obtain an explicit analytical solution for the savings function g.
In such cases a numerical approach can be used to compute explicit solutions.
When all parameters are specified numerically, it is possible to use an algorithm based on (11) to obtain an approximation to g.
Then {k_t} can be computed using (9), given any initial value k_0.
In addition, there are often qualitative features of the savings function g, and hence of the capital paths generated by (9), that hold under a very wide range of assumptions on f and U.
Specifically, we can use either (5)-(6) or the first-order and envelope conditions for (11), together with assumptions on U and f, to characterize the optimal savings function g.
We can then, in turn, use the properties of g so established to characterize solutions {k_t} to (9).
The following exercise illustrates the second of these steps.
Exercise 2.4 a.
Let f be as specified in Exercise 2.1, and suppose that the optimal savings function g is characterized by a constant savings rate, g(k) = sf(k), all k, where s > 0.
Plot g, and on the same diagram plot the 45° line.
The points at which g(k) = k are called the stationary solutions, steady states, rest points, or fixed points of g.
Prove that there is exactly one positive stationary point k*. b.
Use the diagram to show that if f_y > 0, then the sequence {k_t} given by (9) converges to k* as t → ∞.
That is, let {k_t} be a sequence satisfying (9), given some k_0 = 0.
Prove that lim_{t→∞} k_t = k*, for any k_0 > 0.
Show that this convergence is monotonic.
Can it occur in a finite number of periods? c.
This exercise contains most of the information that can be established about the qualitative behavior of a sequence generated by a deterministic dynamic model.
The stationary points have been located and characterized, their stability properties established, and the motion of the system has been described qualitatively for all possible initial positions.
We take this example as a kind of image of what one might hope to establish for more complicated models, or as a source of reasonable conjectures.
(Information about the rate of convergence to the steady state k*, for k_t near k*, can be obtained by taking a linear approximation to g in a neighborhood of k*.
Alternatively, numerical simulations can be used to study the rate of convergence over any range of interest.) From the discussion above, we conclude that a fruitful way of analyzing a stationary, infinite-horizon optimization problem like the one in (3)-(4) is by examining the associated functional equation (11) for this example—and the difference equation (9) involving the associated policy function.
Several steps are involved in carrying out this analysis.
First we need to be sure that the solution(s) to a problem posed in terms of infinite sequences are also the solution(s) to the related functional equation.
That is, we need to show that by using the functional equation we have not changed the problem.
Then we must develop tools for studying equations like (11).
We must establish the existence and uniqueness of a value function v satisfying the functional equation and, where possible, develop qualitative properties of v.
We also need to establish properties of the associated policy function g.
Finally we must show how qualitative properties of g are translated into properties of the sequences generated by g.
Since a wide variety of problems from very different substantive areas of economics all have this same mathematical structure, we want to develop these results in a way that is widely applicable.
Doing this is the task of Part II. 2.2 A Stochastic Model of Optimal Growth The deterministic model of optimal growth discussed above has a variety of stochastic counterparts, corresponding to different assumptions about the nature of the uncertainty.
In this section we consider a model in which the uncertainty affects the technology only, and does so in a specific way.
Assume that output is given by y_t = z_t f(k_t) where {z_t} is a sequence of independently and identically distributed (i.i.d.) random variables, and f is defined as it was in the last section.
The shocks may be thought of as resulting from crop failures, technological breakthroughs, and so on.
The feasibility constraints for the economy are then k_{t+1} + c_t = y_t = z_t f(k_t), all t, all {z_t}.
Assume that the households in this economy rank stochastic consumption sequences according to the expected utility they deliver, where their underlying (common) utility function takes the same additively separable form as before: E[u(c_0, c_1, ...)] = E[∑_{t=0}^∞ β^t u(c_t)].
Here E(·) denotes expected value with respect to the probability distribution of the random variables {c_t}_{t=0}^∞.
Now consider the problem facing a benevolent social planner in this stochastic environment.
As before, his objective is to maximize the objective function in (2) subject to the constraints in (1).
Before proceeding, we need to be clear about the timing of information, actions, and decisions, about the objects of choice for the planner, and about the distribution of the random variables {z_t}_{t=0}^∞.
Assume that the timing of information and actions in each period is as follows.
At the beginning of period t the current value z_t of the exogenous shock is realized.
Thus, the pair (z_t, k_t), and hence the value of total output z_t f(k_t), are known when consumption c_t takes place and end-ofperiod capital k_{t+1} is accumulated.
The pair (z_t, k_t) is called the state of the economy at date t.
As we did in the deterministic case, we can think of the planner in period 0 as choosing, in addition to the pair (c_0, k_1), an infinite sequence {c_t, k_{t+1}}_{t=0}^∞ describing all future consumption and capital pairs.
In the stochastic case, however, this is not a sequence of numbers but a sequence of contingency plans, one for each period.
Specifically, consumption c_t and end-of-period capital k_{t+1} in each period t = 1, 2, ... are contingent on the realizations of the shocks z_1, z_2, ... , z_t.
This sequence of realizations is information that is available when the decision is being carried out but is unknown in period 0 when the decision is being made.
Technically, then, the planner chooses among sequences of functions, where the tth function in the sequence has as its arguments the history (z_1, ... , z_t) of shocks realized between the time the plan is drawn up and the time the decision is carried out.
The feasible set for the planner is theset of pairs $(c, k)$ and sequences of functions $\{c_t(\cdot), k_{t+1}(\cdot)\}_{t=0}^{T-1}$ that satisfy (1) for all periods and all realizations of the shocks.
For any element of this set of feasible contingency plans, the exogenously given probability distribution of the shocks determines the distribution of future consumptions, so the expectation in (2) is well defined.
The next exercise indicates the issues involved when one views the problem directly as one of choosing a sequence of contingency plans.
Exercise 2.5 Consider the finite-horizon version of the planning problem, with the objective function in (2), the constraints in (1), and the horizon $T$.
Assume that the shocks $\{z_t\}_{t=0}^T$ take on only the finite list of values $d_1,\dots,d_n$; and assume that the probabilities of these outcomes are $\pi_1,\dots,\pi_n$, respectively in each period.
State the first-order conditions for this problem.
(This is mainly bookkeeping, but working out the details is instructive.
Begin by making a list of all decision variables.
In what Euclidean space does the planner’s feasible set lie?) This is one way of setting out the problem of optimal growth under uncertainty.
There is another way, the analogue of the recursive formulation for the deterministic case.
Here we let $V(z)$ be the value of the maximized objective (2) when the initial state is $(k, z)$.
Then a choice $(c, y)$ of current consumption $c$ and end-of-period capital $y$ yields current utility $U(c)$ and implies that the system next period will be in the state $(y, z')$, where $z'$ will be chosen by “nature” according to the fixed distribution governing the exogenous shocks.
The maximum expected utility that can be obtained from this position is $v(y, z')$; so its discounted value as viewed in the current period, with $z'$ unknown, is $\beta E[v(y, z')]$.
These considerations motivate the functional equation (3) $v(k, z) = \max_{0 \leq y \leq f(k)} \{U(f(k) - y) + \beta E[v(y, z')]\}$.
The study of (3) yields the optimal choice of capital $y^* = g(k, z)$ as a function of the state $(k, z)$ at the time the decision is taken.
From this recursive point of view, then, the stochastic optimal growth problem is formally very similar to the deterministic one. 2.2 Stochastic Growth 19 The methods used to characterize the optimal policy in the stochastic case are completely analogous to those used for the deterministic case.
If we assume differentiability and an interior optimum, the first-order condition for (3) is $U'(c) = \beta E[v_y(y, z')]$.
This condition implicitly defines a policy function $g$ that has as its arguments the two state variables $k$ and $z$.
Then the optimal capital path is given by the stochastic difference equation (4) $k_{t+1} = g(k_t, z_t)$, where $\{z_t\}$ is an i.i.d. sequence of random shocks.
The following exercise looks at (3)-(4) for the special case of log utility and Cobb-Douglas technology studied in the last section.
Exercise 2.6 Let $U(c) = \ln(c)$ and $f(k) = Ak^\alpha$, $0 < \alpha < 1$, as we did in Exercises 2.2—2.4.
Conjecture that an optimal policy is, as before, $k_{t+1} = \alpha \beta z_t k_t$, all $t$, all $\{z_t\}$.
Calculate the value of the objective function (2) under this policy, given $k_0 = k$ and $z = z$, and call this value $v(k, z)$.
Verify that the function $v$ so defined satisfies (3).
Working out the dynamics of the state variable $k$ that are implied by the policy function $g$ is quite different in the stochastic case.
Equation (4) and its specialization (5) are called (first-order) stochastic difference equations, and the random variables $\{k_t\}$ generated by such equations are called a (first-order) Markov process.
It is useful to recall the results obtained for the deterministic difference equation in Exercise 2.4 and to think about possible analogues for the stochastic case.
Clearly, the sequence $\{k_t\}$ described by (5) is not going to converge to any single value in the presence of the recurring shocks $z_t$.
Can anything be said about its behavior?
Taking logs in (5), we obtain $\ln(k_{t+1}) = \ln(\alpha \beta) + \alpha \ln(k_t) + \ln(z_t)$.
Since the shocks $z_t$ are i.i.d. random variables, so are the logs $\{\ln(z_t)\}$.
Now suppose that the latter are normally distributed, with common mean $\mu_z$ and variance $\sigma_z^2$.
Exercise 2.7 Given $k_0$, show that $\{\ln(k_t)\}_{t=1}^\infty$ is a sequence of normally distributed random variables with means $\mu_t$ and variances $\sigma_t^2$.
Find these means and variances and calculate their limiting values as $t \to \infty$.
In this example, then, the sequence of probability distributions for the random variables $\{k_t\}$ converges as $t$ increases without bound.
Moreover, the combination of linearity and normality permits explicit pencil-and-paper calculation of the distributions of all the $k_t$’s.
This type of calculation is not possible in general, but convergence of the sequence of distribution functions for the $k_t$’s to a limiting distribution can be verified under much broader assumptions.
The basic idea is as follows.
Let the sequence $\{k_t\}$ be described by (5) but drop the assumption that the $z_t$’s are log-normally distributed.
Instead let $G$ be the (common) cumulative distribution function for the $z_t$’s.
Then given the initial capital stock $k_0 > 0$, next period’s stock $k_1$ is a random variable whose cumulative distribution function—call it $\Psi_1$—is determined by $G$.
In particular, for any $a > 0$, $\Psi_1(a) = \Pr\{k_1 < a\} = \Pr\{\alpha \beta z_0 k_0^\alpha < a\} = \Pr\{z_0 < a/(\alpha \beta k_0^\alpha)\} = G(a/(\alpha \beta k_0^\alpha))$.
Thus $k_0$ and $G$ determine the distribution function $\Psi_1$ of $k_1$.
Since the same logic holds for any successive pair of periods, we can define the function (6) $H(a, b) = \Pr\{k_{t+1} = a | k_t = b\} = G(a/(\alpha \beta b^\alpha))$, $\forall a, b > 0$. $H$ is called a transition function.
With $H$ so defined, the sequence of distribution functions $\{\Psi_t\}$ for the $k_t$’s is given inductively by (7) $\Psi_{t+1}(a) = \Pr\{k_{t+1} = a\} = \int H(a, b) d\Psi_t(b)$, $t = 0, 1, \dots$, where the distribution $\Psi_0$ is simply a mass point at the given initial value $k_0$. 2.2 Stochastic Growth 21 More generally, given a stochastic difference equation of the form in (5) and given a distribution function $G$ for the exogenous shocks, we can construct a transition function $H$ as we did in (6).
Then for any initial value $k_0 > 0$, the sequence $\{\Psi_t\}$ of distribution functions for the $k_t$’s is given by (7).
Exercise 2.7 suggests that if $g$ and $G$ are in some suitable families, then $H$ is such that this sequence converges (in some sense) to a limiting distribution function $\Psi$ satisfying (8) $\Psi(\cdot) = \int H(\cdot, b) d\Psi(b)$.
A distribution function $\Psi$ satisfying (8) is called an invariant distribution for the transition function $H$.
The idea is that if the distribution $\Psi$ gives a probabilistic description of the capital stock $k_t$ in any period $t$, then it also describes the distribution of the capital stock in periods $t+1, t+2, \dots$.
An invariant distribution is thus a stochastic analogue to a stationary point of a deterministic system.
Now suppose that $g$ and $G$ are given and that the associated transition function $H$ has a unique stationary distribution $\Psi$.
Suppose further that for any $k_0 > 0$, the sequence $\{\Psi_t\}$ defined by (7) converges to $\Psi$.
Let $h$ be a continuous function and consider the sample average $(1/T) \sum_{t=1}^T h(k_t)$ for this function, along some sample path.
One might expect that this sample average is, for long time horizons, approximately equal to the mathematical expectation of $h$ taken with respect to the limiting distribution $\Psi$.
That is, one might expect that (9) $\lim_{T \to \infty} \frac{1}{T} \sum_{t=1}^T h(k_t) = \int h(k) d\Psi(k)$, at least along most sample paths.
A statement of this sort is called a law of large numbers.
Later we will specify precisely what is meant by “most sample paths” and will develop conditions under which (9) holds.
When (9) does hold, we can calculate the sample average on the left in (9) from observed time series, calculate the integral on the right in (9) from the theory, and use a comparison of the two as a test of the theory.
The first calculation is easy.
Much of this book is concerned with methods for carrying out the second.
As the discussion above suggests, the techniques of dynamic programming are, if anything, even more useful for analyzing stochastic models.22 2 / An Overview than they are for looking at deterministic problems.
Exercise 2.5 illustrates the complexity of looking at stochastic, dynamic problems in terms of sequences, even when the horizon is finite.
On the other hand, we will see later that functional equations like (3) are no more difficult to handle than their deterministic counterparts.
The main ingredients are a convenient language for talking about distributions for stochastic shocks and a few basic results about expectation operators like the one in (3).
The solution to a functional equation like (3) involves an optimal policy function g like the one in (4), and hence we are interested in studying the properties of time series produced by systems like (4).
This analysis is significantly harder than the analysis of solutions to deterministic difference equations, but it is not unmanageable.
Clearly a stability theory for stochastic systems requires several things.
First we must define precisely what convergence means for a sequence of distribution functions.
Then we need to develop sufficient conditions on transition functions, like the function H above, to ensure that H has a unique invariant distribution and that the sequence of distribution functions given by (7) converges, in the desired sense, to that invariant distribution.
Finally, to connect the theory to observed behavior, we must develop conditions under which a law of large numbers holds.
The reader should not be surprised that carrying out this agenda requires laying some preliminary groundwork.
Some definitions, notation, and basic results from modern probability theory are needed, as well as some basic information about Markov processes.
This preliminary material, as well as the analysis of stochastic recursive models, is the content of Part III. 2.3 Competitive Equilibrium Growth In the last two sections we were concerned exclusively with the allocation problem faced by a hypothetical social planner.
In this section we show that the solutions to planning problems of this type can, under appropriate conditions, be interpreted as predictions about the behavior of market economies.
The argument establishing this is based, of course, on the classical connection between competitive equilibria and Pareto optima.
These connections hold under fairly broad assumptions, and in later chapters we will establish them in a very general setting.
At that time we will also show that in situations where the connection between competitive equilibria and Pareto optima breaks down, as it does in the presence of taxes or other distortions, the study of competitive equilibria can be carried out by a direct analysis of the appropriate first-order conditions.
Recall that in the models discussed above there were many identical households, and we took the (common) preferences of these households to be the preferences attributed to the social planner.
In addition, there were many identical firms, all with the same constant-returns-to-scale technology, so the technology available to the economy was the same as that available to each firm.
Thus, the planning problems considered in Sections 2.1 and 2.2 were Pareto problems for economies with many agents.
That is, they can be viewed as problems of maximizing a weighted average of households’ utilities, specialized to a case where all households had identical tastes and were given equal weight, and hence received identical allocations.
Thus the solutions to planning problems of the type we considered were Pareto-optimal allocations.
In this section we show that these allocations are exactly the ones that correspond to competitive equilibria.
For simplicity we restrict attention here to the case of certainty and of a finite time horizon.
Suppose that we have solved the finite-horizon optimal growth problem of Section 2.1 and that {(c_t*, k_{t+1}*)}_{t=0}^T is the solution.
Our goal is to find prices that support these quantities as a competitive equilibrium.
However, we must first specify the ownership rights of households and firms, as well as the structure of markets.
It is crucial to be specific on these matters.
Assume that households own all factors of production and all shares in firms and that these endowments are equally distributed across households.
Each period households sell factor services to firms and buy the goods produced by firms, consuming some and accumulating the rest as capital.
Assume that firms own nothing; they simply hire capital and labor on a rental basis to produce output each period, sell the output produced back to households, and return any profits that result to shareholders.
Finally, assume that all transactions take place in a single once-and-for-all market that meets in period 0.
All trading takes place at that time, so all prices and quantities are determined simultaneously.
No further trades are negotiated later.
After this market has closed, in periods t = 0,1,...,T, agents simply deliver the quantities of factors and goods they have contracted to sell and receive those they have contracted to buy.
Assume that the convention for prices in this one big market is as follows.
Let p_t be the price of a unit of output delivered in period t for t= 0, 1,..., T, expressed in abstract units-of-account.
Let w_t be the price of a unit of labor delivered in period t, expressed in units of goods in period t, so that w_t is the real wage.
Similarly let r_t be the real rental price of capital in period t.
Given the prices {(p_t, w_t, r_t)}_{t=0}^T, the problem faced by the representative firm is to choose input demands and output supplies {(k_t, l_t, y_t)}_{t=0}^T that maximize net discounted profits.
Thus its decision problem is T (1) max Π = Σ_{t=0}^T β^t [p_t y_t - w_t l_t - r_t k_t] T (2) s.t. y_t ≤ F(k_t, l_t), t=0,1,...,T.
Given the same price sequence, the typical household must choose demand for consumption and investment, and supplies of current capital and labor, {(c_t, i_t, x_{t+1}, k_{t+1}, l_t)}_{t=0}^T, given initial capital holdings x_0.
In making these choices the household faces several constraints.
First, the total value of goods purchased cannot exceed the total value of wages plus rental income plus profits the household receives.
Second, the household’s holdings of real capital in each period t + 1 are equal to its holdings in period t net of depreciation, plus any new investment.
Third, the quantity of each factor supplied by the household in each period must be nonnegative but cannot exceed the quantity available to it in that period.
Finally, consumption and capital holdings must be nonnegative.
Thus its decision problem is T (3) max Σ_{t=0}^T β^t U(c_t) T (4) s.t. Σ_{t=0}^T p_t (c_t + i_t) ≤ Σ_{t=0}^T [w_t l_t + r_t k_t + π_t] (5) x_{t+1} = (1 - δ)x_t + i_t, t= 0,1,..., T, given x_0; (6) 0 ≤ l_t ≤ h, 0 ≤ k_t ≤ x_t, t=0,1,...,T; (7) c_t ≥ 0, i_t ≥ 0, t=0,1,...,T.
Note that c_t and x_{t+1}, and capital supplied to firms, k_{t+1}, are required to be nonnegative.
However, gross investment, i_t, may be negative.
This assumption is the one that was made, implicitly, in Section 2.1.
A competitive equilibrium is a set of prices {(p_t, r_t, w_t)}_{t=0}^T, an allocation {(y_t, l_t, k_t)}_{t=0}^T for the typical firm, and an allocation {(c_t, i_t, x_{t+1}, k_{t+1}, l_t)}_{t=0}^T for the typical household, such that, a. {(y_t, l_t, k_t)}_{t=0}^T solves (1)—(2) at the stated prices; b. {(c_t, i_t, x_{t+1}, k_{t+1}, l_t)}_{t=0}^T solves (3)—(7) at the stated prices; c. all markets clear: k_t = x_t, l_t = h, and c_t + i_t = y_t, all t.
To find a competitive equilibrium, we begin by conjecturing that it has certain features.
Later we will verify that these conjectures are correct.
First, since the representative household’s preferences are strictly monotone, we conjecture that goods prices are strictly positive for each period: p_t > 0, all t.
Also, since both factors have strictly positive marginal products, we conjecture that both factor prices are strictly positive for all periods: w_t > 0 and r_t > 0, all t.
Finally, since in equilibrium marketsclear, we let \(k_t^j = k^j\) and \(n_t^j = n^j\), all \(t\), denote the quantities of capital and labor traded.
Now consider the typical firm.
If the price of goods is strictly positive in each period, then the firm supplies to the market all of the output that it produces each period.
That is, (2) holds with equality, for all \(t\).
Also, note that since the firm simply rents capital and hires labor for each period, its problem is equivalent to a series of one-period maximization problems.
Hence its input demands solve \[ \max_{k^j, n^j} P^j F(k^j, n^j) - r k^j - w n^j, \quad t=0,1,\ldots, T. \] It then follows that (real) factor prices must be equal to marginal products: \[ r = F_k(k^j, n^j), \quad t=0,1,\ldots,T, \] \[ w = F_n(k^j, n^j), \quad t=0,1,\ldots,T. \] Since \(F\) is homogeneous of degree one, when we substitute from (9) and (10) into (8), we find that \(\pi^j = 0\).
Note, too, that \(k_{T+1}^j = 0\).
Next consider the typical household.
Since supplying available factors causes no disutility to the household, in every period it supplies all that is available.
That is, \(n_t^h = \bar{n}\) and \(k_t^h = k_t\), all \(t\).
Using these facts and substituting from (5) to eliminate \(i\) we can write the household’s problem as \[ \max_{\{c_t, k_{t+1}\}} \sum_{t=0}^{T} \beta^t U(c_t) \] subject to \[ \sum_{t=0}^{T} P^t \left[ c_t + k_{t+1} - (1 - \delta)k_t - \bar{w}n - r k_t \right] \le 0, \] \[ c_t \ge 0, \quad k_{t+1} \ge 0, \quad t=0,1,\ldots,T; \] given \(k_0 = x_0\).
Since \(\lim_{c \to 0} U'(c) = \infty\), the nonnegativity constraints on the \(c_t\)’s in (13) are never binding.
Hence the first-order conditions for the household are \[ \beta^t U'(c_t) - \lambda P^t = 0, \] \[ \lambda P^t (r_{t+1} + 1 - \delta) - \lambda P^{t+1} = 0, \] with equality if \(k_{t+1} > 0\), \(t=0,1,\ldots,T\); where \(\lambda\) is the multiplier associated with the budget constraint (12).
Therefore a competitive equilibrium is characterized by quantities and prices \(\{(c_t^*, k_{t+1}^*, p_t^*, r_t^*, w_t^*)\}_{t=0}^{T}\), with all goods and factor prices strictly positive, such that \(\{(k^{j*}, n^{j*})\}_{j=1}^{J}\) solves (8) at the given prices, \(\{(c_t^*, k_{t+1}^*)\}_{t=0}^{T}\) solves (11)—(13) at the given prices, \(k_0 = x_0\), \(k_{T+1} = 0\), and in addition \[ c_t^* = F(k_t^*, \bar{n}) + k_t^* - (1 - \delta)k_t^*, \quad \text{all } t. \] Now that we have defined and partially characterized a competitive equilibrium for the economy of Section 2.1, we can be more specific about the connections between equilibrium and optimal allocations that we referred to earlier.
First note that if \(\{(c_t^*, k_{t+1}^*, p_t^*, r_t^*, w_t^*)\}_{t=0}^{T}\) is an equilibrium, then \(\{(c_t^*, k_{t+1}^*)\}_{t=0}^{T}\) is a solution to the planning problem discussed in Section 2.1.
To prove this we need only show that \(\{(c_t^*, k_{t+1}^*)\}_{t=0}^{T}\) is Pareto optimal.
Suppose to the contrary that \(\{(c_t, k_{t+1})\}_{t=0}^{T}\) is a feasible allocation and that \(\{c_t\}\) yields higher total utility in the objective function (1).
Then this allocation must violate (12), or the household would have chosen it.
But if (12) is violated, then (16) implies that \[ \sum_{t=0}^{T} P^{*t} \left[ F(k_t^*, \bar{n}) - r_t^* k_t^* - w_t^* \bar{n} \right] > 0 = \pi^j, \] contradicting the hypothesis that \(\{(k_t^{j*}, n_t^{j*} = \bar{n})\}_{t=0}^{T}\) was a profit-maximizing choice of inputs.
This result is a version of the first fundamental theorem of welfare economics.
Conversely, suppose that \(\{(c_t^*, k_{t+1}^*)\}_{t=0}^{T}\) is a solution to the planner’s problem in Section 2.1.
Then \(\{k_t^*\}_{t=0}^{T}\) is the unique sequence satisfying the first-order and boundary conditions \[ \beta^t [F(k_t^*, \bar{n}) + (1 - \delta)k_t^* - k_{t+1}^*]^u = \beta^{t+1} [F(k_{t+1}^*, \bar{n}) + (1 - \delta)k_{t+1}^* - k_{t+2}^*]^u, \] \[ k_{T+1}^* = 0, \quad k_0^* = x_0; \] and \(\{c_t^*\}\) is given by \[ c_t^* = f(k_t^*) - k_{t+1}^*, \quad t=0,1,\ldots,T, \] where the function \(f(k) = F(k, \bar{n}) + (1 - \delta)k\) is as defined in Section 2.1.
To construct a competitive equilibrium with these quantities, we must find supporting prices \(\{(P_t^*, r_t^*, w_t^*)\}_{t=0}^{T}\).
To do this, note that (9) and (15) together suggest that goods prices must satisfy \[ P_t^* / P_0^* = f'(k_t^*), \quad t=1,2,\ldots,T, \] where \(P_0^* > 0\) is arbitrary, and (9) and (10) imply that real wage and rental rates must satisfy \[ r_t^* = f'(k_t^*) - (1 - \delta), \quad t=1,2,\ldots,T, \] \[ w_t^* = F_n(k_t^*, \bar{n}), \quad t=1,2,\ldots,T. \] It is not difficult to verify that these prices together with the quantities in (17)-(19) constitute a competitive equilibrium, and we leave the proof as an exercise.
This result is a version of the second fundamental theorem of welfare economics.
Exercise 2.8 Show that at the prices given in (20)—(22), the allocation \(\{(c_t^*, k_{t+1}^*)\}_{t=0}^{T}\) defined in (17)-(19) is utility maximizing for the household [solves (11)—(13)]; that the allocation \(\{(k^{j*}, n^{j*} = \bar{n})\}\) is profit maximizing for the firm [solves (8)]; and that \(\{(c_t^*, k_{t+1}^*)\}_{t=0}^{T}\) satisfies (16).
We also leave it as an exercise to show that the same quantities and prices constitute a competitive equilibrium if firms instead of households are the owners of capital.
Exercise 2.9 Suppose that households are prohibited from owning capital directly.
Instead, firms own all of the initial capital stock \(k_0\) and also make all future investments in capital.
Households own all shares in firms, and returns to the latter now include returns to capital.
Modify the statements of the firm’s and the household’s problems to fit these arrangements and show that the quantities in (17)-(19) together with the prices in (20)—(22) still constitute a competitive equilibrium.
We have interpreted these equilibrium prices and quantities as being determined in a single market-clearing operation.
But there is another way to think of an economy as arriving at the quantities and prices calculated above.
Suppose that the agents meet in a market at the beginning of every period, not just in period 0.
In the market held in period \(t\) agents trade current-period labor, rental services of existing capital, and final output.
In addition, one security is traded: a claim to one unit of final output in the subsequent period.
In each period, factor and bond prices are expressed in terms of current-period goods.
Notice that with a sequence of markets the household must form expectations about future prices in order to arrive at its decisions in the market in period \(t\).
In particular, its expectations about future consumption goods prices and future rental rates on capital affect its current consumption-savings decision.
Thus some assumption is needed about how these expectations are formed.
Suppose, for example, that the household has perfect foresight about all future prices.
(This assumption is the specialization for a deterministic context of the more general notion of rational expectations.) Although we do not carry out the proof here, it is not hard to show that, under the assumption of perfect foresight, this set of markets is equivalent to the one above in the sense that the competitive equilibrium allocation is the same for the two settings, and the prices are closely related.
Exercise 2.10 Suppose that the market structure is as described above.
Modify the statements of the firm’s and the household’s problems to fit these arrangements.
Show that under perfect foresight the quantities in (17)—(19), the factor prices in (21)—(22), and the bond prices \[ \beta U'(c_{t+1}) / U'(c_t) = P_{t+1} / P_t, \quad t=0,1,\ldots,T-1, \] constitute a competitive equilibrium.
(In fact, for the representative household economy here, the sequential market structure can be even further simplified by eliminating securities markets.
Since the net supply of such securities is zero, in equilibrium each household has a net demand of zero for each of the securities.
Hence, if these markets are simply shut down, the remaining prices and the real allocation are unaltered.
This conclusion does not hold, however, in an economy with heterogeneous households.) We have, then, two examples of market economies: one with complete markets in the Arrow-Debreu sense, the other with markets limited to spot transactions in factors of production, goods, and one-period securities.
Both economies reproduce the optimal path of capital accumulation discussed in Section 2.1, provided agents in the sequence economy have perfect foresight about future prices.
There is yet a third way in which the solution to the optimal growth model of Section 2.1 can be interpreted as a competitive equilibrium, one that is closely related to the dynamic programming approach ofnistic, recursive systems over time: the theory of stability for autonomous difference equations.
We first review results on global stability and then treat local stability.
We conclude with several economic applications of these methods and with some examples that illustrate the types of behavior possible in unstable systems.
Stochastic systems, like those we saw in Section 2.2, are treated in Part II (Chapters 7-14).
In generalizing the analysis of Chapters 4–6 to include stochastic shocks, a variety of approaches are possible.
We have chosen to take a modern attack, one that allows us to deal with very general classes of stochastic shocks when looking at dynamic programming problems, and that yields additional benefits later when we study the stochastic counterpart of stability theory.
To take this approach, we must first develop some of the basic tools of the theory of measure and integration.
This background is presented in Chapters 7 and 8.
Chapter 7 is a self-contained treatment of the definitions and results from measure theory that are needed in later chapters; and Chapter 8 contains an introduction to Markov processes, the natural generalization of the stochastic difference equations discussed above.
With these mathematical preliminaries in place, Chapter 9 deals with stochastic dynamic programming, paralleling Chapter 4 as closely as possible.
The rewards from Chapters 7 and 8 are apparent here (we hope!).
With the appropriate notation and results in hand, the arguments used in Chapter 9 to study stochastic models are fairly simple extensions of those in Chapter 4.
Chapter 10 then provides a variety of economic applications, drawn from a number of different substantive areas.
Some of these are stochastic analogues to models discussed in Chapter 5; others are entirely new.
Chapters 11 and 12 survey results on convergence, in various senses, for Markov processes: extensions of the ideas sketched in Section 2.2 to a much wider variety of problems.
This material is the body of theory suited to characterizing the dynamics for state variables generated by optimal policy functions for stochastic dynamic programs.
Substantive economic applications of these methods are discussed in Chapter 13.
Some of these applications are continuations of those discussed in Chapter 10, others are new.
Chapter 14 provides a law of large numbers for Markov processes.
The use of recursive systems within a general equilibrium framework, as illustrated in Section 2.3 above, is the subject of Part IV (Chapters 15-18).
Chapter 15 returns at a more abstract level to the connections between Pareto-optimal and competitive equilibrium allocations.
In particular, we there review the two fundamental theorems of welfare economics in a way that applies to the kinds of infinite dimensional commodity spaces that arise in dynamic applications.
We also treat the issue of constructing prices for problems involving infinite time horizons and/or uncertainty.
Chapter 16 then contains a number of applications, designed to illustrate how a variety of planning problems can be interpreted as market equilibria.
When a market equilibrium is also the solution to a benevolent social planner’s problem, this fact vastly simplifies the analysis.
However, there are many market situations of great interest—situations in which markets are subject to distortions due to taxes, external effects, or various kinds of market imperfections—that cannot be analyzed in this way.
In many such cases it is still possible to construct recursive equilibria directly, using the line of argument discussed briefly in Section 2.3.
Chapter 17 presents several mathematical results, fixed-point theorems, that have proved useful in such cases, and illustrates their application.
In Chapter 18 we conclude with further illustrations of these methods. 2.5 Bibliographic Notes Modern growth theory began with Frank Ramsey's (1928) classic paper and then lay dormant for almost 30 years.
(Although a substantial body of literature on growth developed during the 1930s and 1940s, this work is quite different from the neoclassical theory of growth both in motivation and in terms of the specific models used: its goal was to show that high, persistent rates of unemployment are a necessary feature of long-run growth, and the models used generally featured fixed-proportions technologies.) The field was reawakened by the work of Solow (1956) and Swan (1956) and has been active ever since.
The work by Solow and Swan, and much that followed immediately, relied on the assumption that households save a fixed proportion of their income.
These models were meant to be descriptive rather than prescriptive, and no attempt was made to model households’ preferences and expectations.
Households’ preferences finally reentered the discussion when economists looked at the issue of growth from a normative point of view.
The deterministic theory of optimal growth, of which the one-sector model discussed in Section 2.1 is the simplest case, was developed independently and simultaneously by Cass (1965) and Koopmans (1965).
A stochastic model that incorporated shocks to production, like the one discussed in Section 2.2, was first studied by Brock and Mirman (1972) and by Mirman and Zilcha (1975).
The first modern treatment of the connections between Pareto optima and competitive equilibria was provided by Arrow (1951) for the case where the commodity space is a finite-dimensional Euclidean space.
This treatment applies, for example, to the finite-horizon optimal growth problem discussed in Section 2.3.
Debreu (1954) showed that the same line of argument holds in certain infinite-dimensional spaces, and his is the treatment that we will need later to deal with infinite-horizon models.
The interpretation of a competitive equilibrium in terms of a sequence of markets can also be made for stochastic models.
To make this interpretation, it must be assumed that agents have rational expectations in the sense of Muth (1961).
See Radner (1972) for a pioneering general equilibrium application of this idea.
# PART II
Deterministic Models
## 3 Mathematical Preliminaries
In Chapter 2 the optimal growth problem max Σ β^t U(c_t) {c_t, x_{t+1}}_{t=0}^∞ s.t. c_t + x_{t+1} = f(x_t), c_t ≥ 0, x_t ≥ 0, t ≥ 0, given x_0, was seen to lead to the functional equation (1) v(k) = max_{0 ≤ y ≤ f(k)} [U(f(k) - y) + βv(y)].
The purpose of this chapter and the next is to show precisely the relationship between these two problems and others like them and to develop the mathematical methods that have proved useful in studying the latter.
In Section 2.1 we argued in an informal way that the solutions to the two problems should be closely connected, and this argument will be made rigorous later.
In the rest of this introduction we consider alternative methods for finding solutions to (1), outline the one to be pursued, and describe the mathematical issues it raises.
In the remaining sections of the chapter we deal with these issues in turn.
We draw upon this material extensively in Chapter 4, where functional equations like (1) are analyzed.
In (1) the functions U and f are given—they take specific forms known to us—and the value function v is unknown.
Our task is to prove the existence and uniqueness of a function v satisfying (1) and to deduce its properties, given those of U and f.
The classical (nineteenth-century) approach to this problem was the method of successive approximations, and it works in the following very commonsensical way.
Begin by taking an initial guess that a specific function, call it v_0, satisfies (1).
Then define a new function, v_1, by (2) v_1(k) = max_{0 ≤ y ≤ f(k)} {U[f(k) - y] + βv_0(y)}.If it should happen that u1(k) = vo(k), for all k = 0, then clearly vo is a solution to (1).
Lucky guessing (cf.
Exercise 2.3) is one way to establish the existence of a function satisfying (1), but it is notoriously unreliable.
The method of successive approximations proceeds in a more systematic way.
Suppose, as is usually the case, that v_i ≠ vo.
Then use v_i as a new guess and define the sequence of functions {v_n} recursively by (3) v_{n+1}(k) = max {u(f(k) - y) + β v_n(y)} n = 0,1,2,---- 0 ≤ y ≤ f(k) The hope behind this iterative process is that as n increases, the successive approximations v_n get closer to a function v that actually satisfies (1).
That is, the hope is that the limit of the sequence {v_n} is a solution v.
Moreover, if it can be shown that lim_{n→∞} v_n is the same for any initial guess vo, then it will follow that this limit is the only function satisfying (1).
(Why?) Is there any reason to hope for success in this analytical strategy?
Recall that our reason for being interested in (1) is to use it to locate the optimal capital accumulation policy for a one-sector economy.
Suppose we begin by choosing any feasible capital accumulation policy, that is, any function g_o satisfying 0 ≤ g_o(k) ≤ f(k), all k ≥ 0. [An example is the policy of saving a constant fraction of income: g_o(k) = θ f(k), where 0 ≤ θ < 1.] The lifetime utility yielded by this policy, as a function of the initial capital stock k0, is w_o(k0) = Σ_{t=0}^∞ β^t u(f(k_t) - g_o(k_t)) where k_{t+1} = g_o(k_t), t = 0, 1, 2,....
The following exercise develops a result about (g_o, w_o) that is used later.
Exercise 3.1 Show that w_o(k) = u(f(k) - g_o(k)) + β w_o(g_o(k)), all k ≥ 0.
If the utility from the policy g_o is used as the initial guess for a value function—that is, if v_o = w_o—then (2) is the problem facing a planner who can choose capital accumulation optimally for one period but must follow the policy g_o in all subsequent periods.
Thus v_1(k) is the level of lifetime utility attained, and the maximizing value of y—call it g_1(k)—is the optimal level for end-of-period capital.
Both v_1 and g_1 are functions of beginning-of-period capital k.
Notice that since g_o(k) is a feasible choice in the first period, the planner will do no worse than he would by following the policy g_o from the beginning, and in general he will be able to do better.
That is, for any feasible policy g_o and associated initial value function vo, v_1(k) = max_y {u(f(k) - y) + β v_o(y)} ≥ u(f(k) - g_o(k)) + β v_o(g_o(k)) = u(f(k) - g_o(k)) + β w_o(g_o(k))  [since vo = w_o] = w_o(k);  [by Exercise 3.1] Now suppose the planner has the option of choosing capital accumulation optimally for two periods but must follow the policy g_o thereafter.
If y is his choice for end-of-period capital in the first period, then from the second period on the best he can do is to choose g_1(y) for end-of-period capital and enjoy total utility v_1(y).
His problem in the first period is thus max_y[u(f(k) - y) + β v_1(y)], subject to the constraints in (1).
The maximized value of this objective function was defined, in (3), as v_2(k).
Hence it follows from (4) that v_2(k) = max_y {u(f(k) - y) + β v_1(y)} = max_y {u(f(k) - y) + β [u(f(y) - g_o(y)) + β v_o(g_o(y))]} = v_2(k).
Continuing in this way, one establishes by induction that v_{n+1}(k) ≥ v_n(k), all k, n = 0,1, 2, … .
The successive approximations defined in (3) are improvements, reflecting the fact that planning flexibility over longer and longer finite horizons offers new options without taking any other options away.
Consequently it seems reasonable to suppose that the sequence of functions {v_n} defined in (3) might converge to a solution v to (1).
That is, the method of successive approximations seems to be a reasonable way to locate and characterize solutions.
This method can be described in a somewhat different and much more convenient language.
As we showed in the discussion above, for any function w: R → R, we can define a new function—call it Tw: R → R—by (5) (Tw)(k) = max {u(f(k) - y) + β w(y)}. 0 ≤ y ≤ f(k) When we use this notation, the method of successive approximations amounts to choosing a function v_o and studying the sequence {v_n} defined by v_{n+1} = Tv_n, n = 0, 1, 2,....
The goal then is to show that this sequence converges and that the limit function v satisfies (1).
Alternatively, we can simply view the operator T as a mapping from some set C of functions into itself: T: C → C.
In this notation solving (1) is equivalent to locating a fixed point of the mapping T, that is, a function v ∈ C satisfying v = Tv, and the method of successive approximations is viewed as a way to construct this fixed point.
To study operators T like the one defined in (5), we need to draw on several basic mathematical results.
To show that T maps an appropriate space C of functions into itself, we must decide what spaces of functions are suitable for carrying out our analysis.
In general we want to limit attention to continuous functions.
This choice raises the issue of whether, given a continuous function w, the function Tw defined by (5) is also continuous.
Finally, we need a fixed-point theorem that applies to operators like T on the space C we have selected.
The rest of the chapter deals with these issues.
In Section 3.1 we review the basic facts about metric spaces and normed vector spaces and define the space C that will be used repeatedly later.
In Section 3.2 we prove the Contraction Mapping Theorem, a fixed-point theorem of vast usefulness.
In Section 3.3 we review the main facts we will need about functions, like Tw above, that are defined by maximization problems. 3.1 Metric Spaces and Normed Vector Spaces The preceding section motivates the study of certain functional equations as a means of finding solutions to problems posed in terms of infinite sequences.
To pursue the study of these problems, as we will in Chapter 4, we need to talk about infinite sequences {x_t}_{t=0}^∞ of states, about candidates for the value function v, and about the convergence of sequences of various sorts.
To do this, we will find it convenient to think of both infinite sequences and certain classes of functions as elements of infinite-dimensional normed vector spaces.
Accordingly, we begin here with the definitions of vector spaces, metric spaces, and normed vector spaces.
We then discuss the notions of convergence and Cauchy convergence, and define the notion of completeness for a metric space.
Theorem 3.1 then establishes that the space of bounded, continuous, real-valued functions on a set X ⊂ R is complete.
We begin with the definition of a vector space.
### DEFINITION A
(real) vector space X is a set of elements (vectors) together with two operations, addition and scalar multiplication.
For any two vectors x, y ∈ X, addition gives a vector x + y ∈ X; and for any vector x ∈ X and any real number α ∈ R, scalar multiplication gives a vector αx ∈ X.
These operations obey the usual algebraic laws; that is, for all x,y,z ∈ X, and α, β ∈ R: a. x + y = y + x; b. x + (y + z) = (x + y) + z; c. α(x + y) = αx + αy; d.
(α + β)x = αx + βx; and e.
(αβ)x = α(βx).
Moreover, there is a zero vector 0 ∈ X that has the following properties: f. x + 0 = x; and g. 0x = 0.
Finally, h. 1x = x.
The adjective “real” simply indicates that scalar multiplication is defined taking the real numbers, not elements of the complex plane or some other set, as scalars.
All of the vector spaces used in this book are real, and the adjective will not be repeated.
Important features of a vector space are that it has a “zero” element and that it is closed under addition and scalar multiplication.
Vector spaces are also called linear spaces.
Exercise 3.2 Show that the following are vector spaces: a. any finite-dimensional Euclidean space R^n; b. the set X = {x ∈ R^2: x = αz, some α ∈ R}, where z ∈ R^2.the set \(X\) consisting of all infinite sequences \((x_0, x_1, x_2, \dots)\), where \(x_i \in \mathbb{R}\), all \(i\); d. the set of all continuous functions on the interval \([a, b]\).
Show that the following are not vector spaces: e. the unit circle in \(\mathbb{R}^2\); f. the set of all integers, \(\mathbb{J} = \{\dots, -1, 0, +1, \dots\}\); g. the set of all nonnegative functions on \([a, b]\). "To discuss convergence in a vector space or in any other space, we need to have the notion of distance.
The notion of distance in Euclidean space is generalized in the abstract notion of a metric, a function defined on any two elements in a set the value of which has an interpretation as the distance between them.
### DEFINITION A
metric space is a set \(S\), together with a metric (distance function) \(\rho: S \times S \to \mathbb{R}\), such that for all \(x, y, z \in S\): a. \(\rho(x, y) \geq 0\), with equality if and only if \(x = y\); b. \(\rho(x, y) = \rho(y, x)\); and c. \(\rho(x, z) = \rho(x, y) + \rho(y, z)\).
The definition of a metric thus abstracts the four basic properties of Euclidean distance: the distance between distinct points is strictly positive; the distance from a point to itself is zero; distance is symmetric; and the triangle inequality holds.
Exercise 3.3 Show that the following are metric spaces. a.
Let \(S\) be the set of integers, with \(\rho(x, y) = |x - y|\). b.
Let \(S\) be the set of integers, with \(\rho(x, y) = 0\) if \(x = y\), \(1\) if \(x \neq y\). c.
Let \(S\) be the set of all continuous, strictly increasing functions on \([a, b]\), with \(\rho(x, y) = \max_{t \in [a,b]} |x(t) - y(t)|\). d.
Let \(S\) be the set of all continuous, strictly increasing functions on \([a, b]\) with \(\rho(x, y) = \int_a^b |x(t) - y(t)| \, dt\). e.
Let \(S\) be the set of all rational numbers, with \(\rho(x, y) = |x - y|\). f.
Let \(S = \mathbb{R}\), with \(\rho(x, y) = f(|x - y|)\), where \(f: \mathbb{R} \to \mathbb{R}\) is continuous, strictly increasing, and strictly concave, with \(f(0) = 0\).
For vector spaces, metrics are usually defined in such a way that the distance between any two points is equal to the distance of their difference from the zero point.
That is, since for any points \(x\) and \(y\) in a vector space \(S\), the point \(x - y\) is also in \(S\), the metric on a vector space is usually defined in such a way that \(\rho(x, y) = \|x - y\|\).
To define such a metric we need the concept of a norm.
### DEFINITION A
normed vector space is a vector space \(S\), together with a norm \(\|\cdot\|: S \to \mathbb{R}\), such that for all \(x, y \in S\) and \(\alpha \in \mathbb{R}\): a. \(\|x\| = 0\), with equality if and only if \(x = 0\); b. \(\|\alpha x\| = |\alpha| \|x\|\); and c. \(\|x + y\| \leq \|x\| + \|y\|\) (the triangle inequality).
Exercise 3.4 Show that the following are normed vector spaces. a.
Let \(S = \mathbb{R}^4\) with \(\|x\| = (\sum_{i=1}^4 x_i^2)^{1/2}\) (Euclidean space). b.
Let \(S = \mathbb{R}^4\), with \(\|x\| = \max_i |x_i|\). c.
Let \(S = \mathbb{R}^4\), with \(\|x\| = \sum_{i=1}^4 |x_i|\). d.
Let \(S\) be the set of all bounded infinite sequences \((x_1, x_2, \dots)\), \(x_i \in \mathbb{R}\), all with \(\|x\| = \sup_i |x_i|\).
(This space is called \(\ell^\infty\).) e.
Let \(S\) be the set of all continuous functions on \([a, b]\), with \(\|x\| = \sup_{t \in [a,b]} |x(t)|\).
(This space is called \(C[a, b]\).) f.
Let \(S\) be the set of all continuous functions on \([a, b]\), with \(\|x\| = \int_a^b |x(t)| \, dt\).
It is standard to view any normed vector space \((S, \|\cdot\|)\) as a metric space, where the metric is taken to be \(\rho(x, y) = \|x - y\|\) for all \(x, y \in S\).
The notion of convergence of a sequence of real numbers carries over without change to any metric space.
### DEFINITION A
sequence \(\{x_n\}_{n=0}^\infty\) in \(S\) converges to \(x \in S\), if for each \(\varepsilon > 0\), there exists \(N_\varepsilon\) such that (1) \(\rho(x_n, x) < \varepsilon\), all \(n \geq N_\varepsilon\).
Thus a sequence \(\{x_n\}\) in a metric space \((S, \rho)\) converges to \(x \in S\) if and only if the sequence of distances \(\{\rho(x_n, x)\}\), a sequence in \(\mathbb{R}\), converges to zero.
In this case we write \(x_n \to x\).
Verifying convergence directly involves having a “candidate” for the limit point \(x\) so that the inequality (1) can be checked.
When a candidate is not immediately available, the following alternative criterion is often useful.
### DEFINITION A
sequence \(\{x_n\}_{n=0}^\infty\) in \(S\) is a Cauchy sequence (satisfies the Cauchy criterion) if for each \(\varepsilon > 0\), there exists \(N_\varepsilon\) such that (2) \(\rho(x_n, x_m) < \varepsilon\), all \(n, m \geq N_\varepsilon\).
Thus a sequence is Cauchy if the points get closer and closer to each other.
The following exercise illustrates some basic facts about convergence and the Cauchy criterion.
Exercise 3.5 a.
Show that if \(x_n \to x\) and \(x_n \to y\); then \(x = y\).
That is, if \(\{x_n\}\) has a limit, then that limit is unique. b.
Show that if a sequence \(\{x_n\}\) is convergent, then it satisfies the Cauchy criterion. c.
Show that if a sequence \(\{x_n\}\) satisfies the Cauchy criterion, then it is bounded. d.
Show that \(x_n \to x\) if and only if every subsequence of \(\{x_n\}\) converges to \(x\).
The advantage of the Cauchy criterion is that, in contrast to (1), (2) can be checked with knowledge of \(\{x_n\}\) only.
For the Cauchy criterion to be useful, however, we must work with spaces where it implies the existence of a limit point.
### DEFINITION A
metric space \((S, \rho)\) is complete if every Cauchy sequence in \(S\) converges to an element in \(S\).
In complete metric spaces, then, verifying that a sequence satisfies the Cauchy criterion is a way of verifying the existence of a limit point in \(S\).
Verifying the completeness of particular spaces can take some work.
We take as given the following FACT The set of real numbers \(\mathbb{R}\) with the metric \(\rho(x, y) = |x - y|\) is a complete metric space.
Exercise 3.6 a.
Show that the metric spaces in Exercises 3.3a, b and 3.4a–e are complete and that those in Exercises 3.3c–e and 3.4f are not.
Show that the space in 3.3c is complete if “strictly increasing” is replaced with “nondecreasing.” b.
Show that if \((S, \rho)\) is a complete metric space and \(S'\) is a closed subset of \(S\), then \((S', \rho)\) is a complete metric space.
A complete normed vector space is called a Banach space.
The next example is no more difficult than some of those in Exercise 3.6, but since it is important in what follows and illustrates clearly each of the steps involved in verifying completeness, we present the proof here.
### THEOREM 3.1
Let \(X \subset \mathbb{R}\) and let \(C(X)\) be the set of bounded continuous functions \(f: X \to \mathbb{R}\) with the sup norm, \(\|f\| = \sup_{x \in X} |f(x)|\).
Then \(C(X)\) is a complete normed vector space.
(Note that if \(X\) is compact then every continuous function is bounded.
Otherwise the restriction to bounded functions must be added.)
**Proof.** That \(C(X)\) is a normed vector space follows from Exercise 3.4e.
Hence it suffices to show that if \(\{f_n\}\) is a Cauchy sequence, there exists \(f \in C(X)\) such that \(\|f_n - f\| \to 0\).
That is, for any \(\varepsilon > 0\) there exists \(N_\varepsilon\) such that \(\|f_n - f\| < \varepsilon\), all \(n \geq N_\varepsilon\).
Three steps are involved: to find a “candidate” function \(f\); to show that \(\{f_n\}\) converges to \(f\) in the sup norm; and to show that \(f \in C(X)\) (that \(f\) is bounded and continuous).
Each step involves its own entirely distinct logic.
Fix \(x \in X\); then the sequence of real numbers \(\{f_n(x)\}\) satisfies \(|f_n(x) - f_m(x)| \leq \sup_{t \in X} |f_n(t) - f_m(t)| = \|f_n - f_m\|\).
Therefore it satisfies the Cauchy criterion; and by the completeness of the real numbers, it converges to a limit point—call it \(f(x)\).
The limiting values define a function \(f: X \to \mathbb{R}\) that we take to be our candidate.
Next we must show that \(\|f_n - f\| \to 0\) as \(n \to \infty\).
Let \(\varepsilon > 0\) be given and choose \(N_\varepsilon\) so that \(n, m \geq N_\varepsilon\) implies \(\|f_n - f_m\| < \varepsilon/2\).
Since \(\{f_n\}\) satisfies the Cauchy criterion, this can be done.
Now for any fixed \(x \in X\) and all \(n, m \geq N_\varepsilon\), \(|f_n(x) - f_m(x)| \leq \|f_n - f_m\| < \varepsilon/2\).
Let \(m \to \infty\); then \(f_m(x) \to f(x)\), so we have \(|f_n(x) - f(x)| = \lim_{m \to \infty} |f_n(x) - f_m(x)| \leq \varepsilon/2 < \varepsilon\).
Thus \(\|f_n - f\| \leq \varepsilon/2 < \varepsilon\), all \(n \geq N_\varepsilon\).
Since \(\varepsilon > 0\) was arbitrary, the desired result then follows.
Finally, we must show that \(f\) is bounded and continuous.
Boundedness is obvious.
To prove that \(f\) is continuous, we must show that for every \(\varepsilon > 0\) and every \(x \in X\), there exists \(\delta > 0\) such that \(|f(x) - f(y)| < \varepsilon\) if \(\|x - y\| < \delta\), where \(\|\cdot\|\) is the Euclidean norm on \(\mathbb{R}\).
Let \(\varepsilon\) and \(x\) be given.
Choose \(k\) so that \(\|f - f_k\| < \varepsilon/3\); since \(f_n \to f\) (in the sup norm), such a choice is possible.
Then choose \(\delta\) so thatlx — lle < 5 implies | f(x) - f(y)| < e/3.
Since fi is continuous, such a choice is possible.
Then |f(x) − f(y)| = |f(x) − f_z| + |f_z − f_y| + |f_y − f(y)| = |f(x) − f_z| + |T_x − T_z| <e. ■ Although we have organized these component arguments into a theorem about a function space, each should be familiar to students of calculus.
Convergence in the sup norm is simply uniform convergence.
The proof above is then just an amalgam of the standard proofs that a sequence of functions that satisfies the Cauchy criterion uniformly converges uniformly and that uniform convergence “preserves continuity.” Exercise 3.7 a.
Let C¹[a, b] be the set of all continuously differentiable functions on [a, b] = X ⊂ ℝ, with the norm ‖·‖ = sup_{x∈X} {|f(x)| + |f'(x)|}.
Show that C¹[a, b] is a Banach space. [Hint.
Notice that sup |f(x)| + sup |f'(x)| = ‖f‖ = max{sup |f(x)|, sup |f'(x)|}.] b.
Show that this set of functions with the norm ‖·‖ = sup_{x∈X} |f(x)| is not complete.
That is, give an example of a sequence of functions that is Cauchy in the given norm that does not converge to a function in the set.
Is this sequence Cauchy in the norm of part (a)? c.
Let Cᵏ[a, b] be the set of all k times continuously differentiable functions on [a, b] = X ⊂ ℝ, with the norm ‖·‖ = ∑_{i=0}^k a_i max_{x∈X} |f^{(i)}(x)|, where f^{(i)} = d^i f(x)/dx^i.
Show that this space is complete if and only if a_i > 0, i = 0,1,...,k. 3.2 The Contraction Mapping Theorem In this section we prove two main results.
The first is the Contraction Mapping Theorem, an extremely simple and powerful fixed point theorem.
The second is a set of sufficient conditions, due to Blackwell, for establishing that certain operators are contraction mappings.
The latter are useful in a wide variety of economic applications and will be drawn upon extensively in the next chapter.
We begin with the following definition.
### DEFINITION L
et (S, ρ) be a metric space and T: S → S be a function mapping S into itself.
T is a contraction mapping (with modulus β) if for some β ∈ (0, 1), ρ(Tx, Ty) ≤ βρ(x, y), for all x, y ∈ S.
Perhaps the most familiar examples of contraction mappings are those on a closed interval S = [a, b], with ρ(x, y) = |x − y|.
Then T: S → S is a contraction if for some β ∈ (0, 1), |Tx − Ty| ≤ β|x − y|, all x, y ∈ S with x ≠ y.
That is, T is a contraction mapping if it is a function with slope uniformly less than one in absolute value.
Exercise 3.8 Show that if T is a contraction on S, then T is uniformly continuous on S.
The fixed points of T, the elements of S satisfying Tx = x, are the intersections of Tx with the 45° line, as shown in Figure 3.1.
Hence it is clear that any contraction on this space has a unique fixed point.
This conclusion is much more general.
### THEOREM 3.2
(Contraction Mapping Theorem) If (S, ρ) is a complete metric space and T: S → S is a contraction mapping with modulus β, then a.
T has exactly one fixed point v in S, and b. for any v₀ ∈ S, ρ(Tⁿ v₀, v) = βⁿ ρ(v₀, v), n = 0,1,2,....
**Proof.** To prove (a), we must find a candidate for v, show that it satisfies Tv = v, and show that no other element w ∈ S does.
Define the iterates of T, the mappings {Tⁿ}, by T⁰x = x, and Tⁿx = T(Tⁿ⁻¹x), n = 1, 2, . . .
Choose v₀ ∈ S, and define {vₙ}ₙ₌₀ by vₙ₊₁ = Tvₙ, so that vₙ = Tⁿ v₀.
By the contraction property of T, ρ(v₁, v₀) = ρ(Tv₀, v₀) ≤ βρ(v₀, v₀) = 0.
Actually, we start from ρ(vₙ₊₁, vₙ) = βⁿ ρ(v₁, v₀).
Then p(v_n, v_{n-1}) = β^{n-1} ρ(v₁, v₀).
D Y a f(x) a V x Figure 3.1 Continuing by induction, we get (1) ρ(v_{n+k}, v_n) = βⁿ ρ(v_k, v₀), n = 1, 2, ..
Hence, for any m > n, ρ(v_m, v_n) ≤ ρ(v_m, v_{m-1}) + … + ρ(v_{n+1}, v_n) + ρ(v_n, v_n) = [β^{m-1} + … + βⁿ + βⁿ] ρ(v₁, v₀) = βⁿ [β^{m-n-1} + … + 1] ρ(v₁, v₀) (2) ≤ [1 / (1 - β)] βⁿ ρ(v₁, v₀), where the first line uses the triangle inequality and the second follows from (1).
It is clear from (2) that {vₙ} is a Cauchy sequence.
Since S is complete, it follows that vₙ → v ∈ S.
To show that Tv = v, note that for all n and all v₀ ∈ S, ρ(Tv, v) ≤ ρ(Tv, Tⁿ v₀) + ρ(Tⁿ v₀, v) = βρ(v, Tⁿ⁻¹ v₀) + ρ(Tⁿ v₀, v).
We have demonstrated that both terms in the last expression converge to zero as n → ∞; hence ρ(Tv, v) = 0, or Tv = v.
Finally, we must show that there is no other function w ∈ S satisfying Tw = w.
Suppose to the contrary that w ≠ v is another solution.
Then 0 < a = ρ(w, v) = ρ(Tw, Tv) ≤ βρ(w, v) = βa, which cannot hold, since β < 1.
This proves part (a).
To prove part (b), observe that for any n ≥ 1, ρ(Tⁿ v₀, v) = ρ{T(Tⁿ⁻¹ v₀), Tv} ≤ βρ(Tⁿ⁻¹ v₀, v) so that (b) follows by induction. ■ Recall from Exercise 3.6b that if (S, ρ) is a complete metric space and S' is a closed subset of S, then (S', ρ) is also a complete metric space.
Now suppose that T: S → S is a contraction mapping, and suppose further that T maps S' into itself, T(S') ⊂ S' (where T(S') denotes the image of S' under T).
Then T is also a contraction mapping on S'.
Hence the unique fixed point of T on S lies in S'.
This observation is often useful for establishing qualitative properties of a fixed point.
Specifically, in some situations we will want to apply the Contraction Mapping Theorem twice: once on a large space to establish uniqueness, and again on a smaller space to characterize the fixed point more precisely.
The following corollary formalizes this argument.
### COROLLARY 1
Let (S, ρ) be a complete metric space, and let T: S → S be a contraction mapping with fixed point v ∈ S.
If S' is a closed subset of S and T(S') ⊂ S', then v ∈ S'.
If in addition T(S') ⊂ S'' ⊂ S', then v ∈ S''.
**Proof.** Choose v₀ ∈ S', and note that {Tⁿ v₀} is a sequence in S' converging to v.
Since S' is closed, it follows that v ∈ S'.
If in addition T(S') ⊂ S'', then it follows that v = Tv ∈ S''. ■ Part (b) of the Contraction Mapping Theorem bounds the distance ρ(Tⁿ v₀, v) between the nth approximation and the fixed point in terms of the distance ρ(v₀, v) between the initial approximation and the fixed point.
However, if v is not known (as is the case if one is computing v), then neither is the magnitude of the bound.
Exercise 3.9 gives a computationally useful inequality.
Exercise 3.9 Let (S, ρ), T, and v be as given above, let β be the modulus of T, and let v₀ ∈ S.
Show that ρ(Tⁿ v₀, v) ≤ [βⁿ / (1 - β)] ρ(Tv₀, T² v₀).
The following result is a useful generalization of the Contraction Mapping Theorem.
### COROLLARY 2
(N-Stage Contraction Theorem) Let (S, ρ) be a complete metric space, let T: S → S, and suppose that for some integer N, Tᴺ: S → S is a contraction mapping with modulus β.
Then a.
T has exactly one fixed point in S, and b. for any v₀ ∈ S, ρ(Tᵏ v₀, v) ≤ β^{⌊k/N⌋} ρ(v₀, v), k = 0,1, 2,....
**Proof.** We will show that the unique fixed point v of Tᴺ is also the unique fixed point of T.
We have ρ(Tv, v) = ρ{T(Tᴺ v), Tᴺ v} = ρ{Tᴺ (Tv), Tᴺ v} ≤ βρ(Tv, v).
Since β ∈ (0, 1), this implies that ρ(Tv, v) = 0, so v is a fixed point of T.
To establish uniqueness, note that any fixed point of T is also a fixed point of Tᴺ.
Part (b) is established using the same argument as in the proof of Theorem 3.2. □ The next exercise shows how the Contraction Mapping Theorem is used to prove existence and uniqueness of a solution to a differential equation.
Exercise 3.10 Consider the differential equation and boundary condition dx(s)/ds = f[x(s)], all s ≥ 0, with x(0) = c ∈ ℝ.
Assume that f: ℝ → ℝ is continuous, and for some β > 0 satisfies the Lipschitz condition |f(a) − f(b)| ≤ β|a − b|, all a, b ∈ ℝ.
For any t > 0, consider C[0, t], the space of bounded continuous functions on [0, t] with the sup norm.
Recall from Theorem 3.1 that this space is complete. a.
Show that the operator T defined by (Tx)(s) = c + ∫₀ˢ f(x(τ)) dτ, 0 ≤ s ≤ t, maps C[0, t] into itself.
That is, show that if x is bounded and continuous on [0, t], then so is Tx. b.
Show that for some t > 0, T is a contraction on C[0, t]. c.
Show that the unique fixed point of T on C[0, t] is a differentiablefunction, and hence that it is the unique solution on [0, 7] to the given differential equation.
Another useful route to verifying that certain operators are contractions is due to Blackwell.
### THEOREM 3.3
(Blackwell’s sufficient conditions for a contraction) Let \( X \subset \mathbb{R}^l \), and let \( B(X) \) be a space of bounded functions \( f: X \to \mathbb{R} \), with the sup norm.
Let \( T: B(X) \to B(X) \) be an operator satisfying a.
(monotonicity) \( f, g \in B(X) \) and \( f(x) \geq g(x) \), for all \( x \in X \), implies \( (Tf)(x) \geq (Tg)(x) \), for all \( x \in X \); b.
(discounting) there exists some \( \beta \in (0, 1) \) such that \[ [T(f + a)](x) \leq (Tf)(x) + \beta a, \quad \text{all } f \in B(X), a \geq 0, x \in X. \] [Here \( (f + a)(x) \) is the function defined by \( (f + a)(x) = f(x) + a \).] Then \( T \) is a contraction with modulus \( \beta \).
**Proof.** If \( f(x) \geq g(x) \) for all \( x \in X \), we write \( f \geq g \).
For any \( f, g \in B(X) \), \[ f = g + (f - g). \] Then properties (a) and (b) imply that \[ Tf \geq Tg + \beta \|f - g\| = Tg + \beta \|f - g\| \mathbf{1}, \] where \( \mathbf{1} \) is the constant function equal to 1.
Reversing the roles of \( f \) and \( g \) gives by the same logic \[ Tg \geq Tf + \beta \|f - g\| \mathbf{1}. \] Combining these two inequalities, we find that \( \|Tf - Tg\| = \beta \|f - g\| \), as was to be shown. \( \blacksquare \) In many economic applications the two hypotheses of Blackwell’s theorem can be verified at a glance.
For example, in the one-sector optimal growth problem, an operator \( T \) was defined by \[ (Tv)(k) = \max_{0 \leq y \leq f(k)} \{ u(y) + \beta v[f(k) - y] \}. \] If \( u(y) = w(y) \) for all values of \( y \), then the objective function for which \( Tw \) is the maximized value is uniformly higher than the function for which \( Tv \) is the maximized value; so the monotonicity hypothesis (a) is obvious.
The discounting hypothesis (b) is equally easy, since \[ T(v + a)(k) = \max_{0 \leq y \leq f(k)} \{ u(y) + \beta [v(f(k) - y) + a] \} \] \[ = \max_{0 \leq y \leq f(k)} \{ u(y) + \beta v(f(k) - y) \} + \beta a \] \[ = (Tv)(k) + \beta a. \] Blackwell’s result will play a key role in our analysis of dynamic programs. 3.3 The Theorem of the Maximum We will want to apply the Contraction Mapping Theorem to analyze dynamic programming problems that are much more general than the examples that have been discussed to this point.
If \( x \) is the beginning-of-period state variable, an element of \( X \subset \mathbb{R}^l \), and \( y \in X \) is the end-of-period state to be chosen, we would like to let the current period return \( F(x, y) \) and the set of feasible \( y \) values, given \( x \), be specified as generally as possible.
On the other hand, we want the operator \( T \) defined by \[ (Tv)(x) = \sup_{y \in \Gamma(x)} [F(x, y) + \beta v(y)] \] to take the space \( C(X) \) of bounded continuous functions of the state into itself.
We would also like to be able to characterize the set of maximizing values of \( y \), given \( x \).
To describe the feasible set, we use the idea of a correspondence from a set \( X \) into a set \( Y \): a relation that assigns a set \( \Gamma(x) \subset Y \) to each \( x \in X \).
In the case of interest here, \( Y = X \).
Hence we seek restrictions on the correspondence \( \Gamma: X \leadsto X \) describing the feasibility constraints and on the return function \( F \), which together ensure that if \( v \in C(X) \) and \( (Tv)(x) = \sup_{y \in \Gamma(x)} [F(x, y) + \beta v(y)] \), then \( Tv \in C(X) \).
Moreover, we wish to determine the implied properties of the correspondence \( G(x) \) containing the maximizing values of \( y \) for each \( x \).
The main result in this section is the Theorem of the Maximum, which accomplishes both tasks.
Let \( X \subset \mathbb{R}^l \), let \( Y \subset \mathbb{R}^m \), let \( f: X \times Y \to \mathbb{R} \) be a (single-valued) function; and let \( \Gamma: X \leadsto Y \) be a (nonempty, possibly multivalued) correspondence.
Our interest is in problems of the form \( \sup_{y \in \Gamma(x)} f(x, y) \).
If for each \( x \), \( f(x, \cdot) \) is continuous in \( y \) and the set \( \Gamma(x) \) is nonempty and compact, then for each \( x \) the maximum is attained.
In this case the function \[ h(x) = \max_{y \in \Gamma(x)} f(x, y) \] is well defined, as is the nonempty set \[ G(x) = \{ y \in \Gamma(x) : f(x, y) = h(x) \} \] of \( y \) values that attain the maximum.
In this section further restrictions on \( f \) and \( \Gamma \) will be added, to ensure that the function \( h \) and the set \( G \) vary in a continuous way with \( x \).
There are several notions of continuity for correspondences, and each can be characterized in a variety of ways.
For our purposes it is convenient to use definitions stated in terms of sequences.
### DEFINITION A
correspondence \( \Gamma: X \leadsto Y \) is lower hemi-continuous (l.h.c.) at \( x \) if \( \Gamma(x) \) is nonempty and if, for every \( y \in \Gamma(x) \) and every sequence \( x_n \to x \), there exists \( N \geq 1 \) and a sequence \( \{y_n\}_{n=N}^{\infty} \) such that \( y_n \to y \) and \( y_n \in \Gamma(x_n) \), all \( n \geq N \). [If \( \Gamma(x') \) is nonempty for all \( x' \in X \), then it is always possible to take \( N = 1 \).]
### DEFINITION A
compact-valued correspondence \( \Gamma: X \leadsto Y \) is upper hemi-continuous (u.h.c.) at \( x \) if \( \Gamma(x) \) is nonempty and if, for every sequence \( x_n \to x \) and every sequence \( \{y_n\} \) such that \( y_n \in \Gamma(x_n) \), all \( n \), there exists a convergent subsequence of \( \{y_n\} \) whose limit point \( y \) is in \( \Gamma(x) \).
Figure 3.2 displays a correspondence that is l.h.c. but not u.h.c. at \( x_1 \); is u.h.c. but not l.h.c. at \( x_2 \); and is both u.h.c. and l.h.c. at all other points.
Note that our definition of u.h.c. applies only to correspondences that are compact-valued.
Since all of the correspondences we will be dealing with satisfy this requirement, the restriction will not be binding.
(A definition of u.h.c. for all correspondences is available, but it is stated in terms of images of open sets.
For our purposes this definition is much less convenient, and its wider scope is never useful.)
### DEFINITION A
correspondence \( \Gamma: X \leadsto Y \) is continuous at \( x \in X \) if it is both u.h.c. and l.h.c. at \( x \).
A correspondence \( \Gamma: X \leadsto Y \) is called l.h.c., u.h.c., or continuous if it has that property at every point \( x \in X \).
The following exercises highlight some important facts about upper and lower hemi-continuity.
Note that if \( T: X \to Y \), then for any set \( K \subset X \), we define \[ \Gamma(K) = \{ y \in Y : y \in \Gamma(x), \text{ for some } x \in K \}. \] Exercise 3.11 a.
Show that if \( \Gamma \) is single-valued and u.h.c., then it is continuous. b.
Let \( \Gamma: \mathbb{R}^l \leadsto \mathbb{R}^{l+m} \) and define \( \phi: \mathbb{R}^l \leadsto \mathbb{R}^m \) by \[ \phi(x) = \{ y \in \mathbb{R}^m : (x, y) \in \Gamma(x) \text{ for some } y \in \mathbb{R}^m \}. \] Show that if \( \Gamma \) is compact-valued and u.h.c., then so is \( \phi \). c.
Let \( \phi: X \leadsto Y \) and \( \psi: X \leadsto Y \) be compact-valued and u.h.c., and define \( \Gamma = \phi \cup \psi \) by \[ \Gamma(x) = \{ y \in Y : y \in \phi(x) \cup \psi(x) \}, \quad \text{all } x \in X. \] Show that \( \Gamma \) is compact-valued and u.h.c. d.
Let \( \phi: X \leadsto Y \) and \( \psi: X \leadsto Y \) be compact-valued and u.h.c., and suppose that \[ \Gamma(x) = \{ y \in Y : y \in \phi(x) \cap \psi(x) \} \neq \emptyset, \quad \text{all } x \in X. \] Show that \( \Gamma \) is compact-valued and u.h.c. e.
Show that if \( \phi: X \leadsto Y \) and \( \psi: Y \leadsto Z \) are compact-valued and u.h.c., then the correspondence \( \psi \circ \phi = \Gamma: X \leadsto Z \) defined by \[ \Gamma(x) = \{ z \in Z : z \in \psi(y), \text{ for some } y \in \phi(x) \} \] is also compact-valued and u.h.c. f.
Let \( \Gamma_i: X \to Y_i, i = 1, \dots, k \), be compact-valued and u.h.c.
Show that \( \Gamma: X \leadsto Y = Y_1 \times \dots \times Y_k \) defined by \[ \Gamma(x) = \{ y \in Y : y = (y_1, \dots, y_k), \text{ where } y_i \in \Gamma_i(x), i = 1, \dots, k \} \] is also compact-valued and u.h.c. g.
Show that if \( \Gamma: X \leadsto Y \) is compact-valued and u.h.c., then for any compact set \( K \subset X \), the set \( \Gamma(K) \subset Y \) is also compact. [Hint.
To show that \( \Gamma(K) \) is bounded, suppose the contrary.
Let \( \{y_n\} \) be a divergent sequence in \( \Gamma(K) \), and choose \( \{x_n\} \) such that \( y_n \in \Gamma(x_n) \), all \( n \).] Exercise 3.12 a.
Show that if \( \Gamma \) is single-valued and l.h.c. then it is continuous. b.
Let \( \Gamma: \mathbb{R}^l \leadsto \mathbb{R}^{l+m} \) and define \( \phi: \mathbb{R}^l \leadsto \mathbb{R}^m \) by \[ \phi(x) = \{ y \in \mathbb{R}^m : (x, y) \in \Gamma(x), \text{ for some } y \in \mathbb{R}^m \}. \] Show that if \( \Gamma \) is l.h.c. then so is \( \phi \). c.
Let \( \phi: X \leadsto Y \) and \( \psi: X \leadsto Y \) be l.h.c., and define \( \Gamma = \phi \cup \psi \) by \[ \Gamma(x) = \{ y \in Y : y \in \phi(x) \cup \psi(x) \}, \quad \text{all } x \in X. \] Show that \( \Gamma \) is l.h.c. d.
Let \( \phi: X \leadsto Y \) and \( \psi: X \leadsto Y \) be l.h.c., and suppose that \[ \Gamma(x) = \{ y \in Y : y \in \phi(x) \cap \psi(x) \} \neq \emptyset, \quad \text{all } x \in X. \] Show by example that \( \Gamma \) need not be l.h.c.
Show that if \( \phi \) and \( \psi \) are both convex-valued, and if \( \text{int } \phi(x) \cap \text{int } \psi(x) \neq \emptyset \), then \( \Gamma \) is l.h.c. at \( x \). e.
Show that if \( \phi: X \leadsto Y \) and \( \psi: Y \leadsto Z \) are l.h.c., then the correspondence \( \psi \circ \phi = \Gamma: X \leadsto Z \) defined by \[ \Gamma(x) = \{ z \in Z : z \in \psi(y), \text{ for some } y \in \phi(x) \} \] is also l.h.c. f.
Let \( \Gamma_i: X \leadsto Y_i, i = 1, \dots, k \), be l.h.c.
Show that \( \Gamma: X \leadsto Y = Y_1 \times \dots \times Y_k \) defined by \[ \Gamma(x) = \{ y \in Y : y = (y_1, \dots, y_k), \text{ where } y_i \in \Gamma_i(x), i = 1, \dots, k \} \] is l.h.c.
The next two exercises show some of the relationships between constraints stated in terms of inequalities involving continuous functions.and those stated in terms of continuous correspondences.
These relationships are extremely important for many problems in economics, where constraints are often stated in terms of production functions, budget constraints, and so on.
Exercise 3.13 a.
Let T: R_y > R_x be defined by T(x) = [0, x].
Show that T is continuous. b.
Let f: R^4 > R_+ be a continuous function, and define the correspondence T: R^4 → R_+ by T(x) = (0, f(x)].
Show that T is continuous. c.
Let f_i: R_x × R^z > R_, i=1,...,n be continuous functions.
Define T: R_x × R^z → R_+ by 1 T(x, z) = {y ∈ R^h: 0 < Σ p_i S f_i for i = 1,...,n and Σ y < 4}. i=1 " Show that T is continuous.
Exercise 3.14 a.
Let H(x,y): R^l × R^m → R be continuous, strictly increasing in its first l arguments, strictly decreasing in its last m arguments, with H(0, 0) = 0.
Define T: R^l → R^m by T(x) = { y ∈ R^m: H (x, y) = 0}.
Show that if T(x) is compact-valued, then T is continuous at x. b.
Let H(x, y): R^l × R^m → R be continuous and concave, and define T as in part (a).
Show that if T(x) is compact-valued and there exists some y ∈ T(x) such that H (x, y) > 0, then T is continuous at x. c.
Define H: R^l × R^m → R by H(x, y) = 1 - max{|x|, |y|}, and define T(x) as in part (a).
Where does T fail to be l.h.c.?
When trying to establish properties of a correspondence T: X → Y, it is sometimes useful to deal with its graph, the set A = {(x,y) ∈ X × Y: y ∈ T (x)}.
The next two results provide conditions on A that are sufficient to ensure the upper and lower hemi-continuity respectively of T.
### THEOREM 3.4
Let T: X → Y be a nonempty-valued correspondence, and let A be the graph of T.
Suppose that A is closed, and that for any bounded set X' ⊂ X, the set T(X') is bounded.
Then T is compact-valued and u.h.c.
**Proof.** For each x ∈ X, T(x) is closed (since A is closed) and is bounded (by hypothesis).
Hence T is compact-valued.
Let x* ∈ X, and let {x_n} ⊂ X with x_n → x*.
Since T is nonempty-valued, we can choose y_n ∈ T(x_n), all n.
Since x_n → x*, there is a bounded set X' ⊂ X containing {x_n} and x*.
Then by hypothesis T(X') is bounded.
Hence {y_n} ⊂ T(X') has a convergent subsequence, call it {y_{n_k}}; let y* be the limit point of this subsequence.
Then {(x_{n_k}, y_{n_k})} is a sequence in A converging to (x*, y*); since A is closed, it follows that (x*, y*) ∈ A.
Hence y* ∈ T(x*), so T is u.h.c. at x*.
Since x* was arbitrary, this establishes the desired result. □ To see why the hypothesis of boundedness is required in Theorem 3.4, consider the correspondence T: R_> R defined by T(0) = 0, and T(x) = {0, 1/x}, all x > 0.
The graph of T is closed, but T is not u.h.c. at x = 0.
The next exercise is a kind of converse to Theorem 3.4.
Exercise 3.15 Let T: X → Y be a compact-valued u.h.c. correspondence with graph A.
Show that if X is compact then A is compact.
The next theorem deals with lower hemi-continuity.
For any x ∈ R^l and any ε > 0, let B(x, ε) denote the closed ball of radius ε about x.
### THEOREM 3.5
Let T: X → Y be a nonempty-valued correspondence, and let A be the graph of T.
Suppose that A is convex; and that for any bounded set X' ⊂ X there is a bounded set Y' ⊂ Y such that T(x) ∩ Y' ≠ ∅, all x ∈ X'.
Then T is l.h.c. at every interior point of X.
**Proof.** Choose y* ∈ T(x*) and {x_n} ⊂ X with x_n → x*.
Choose ε > 0 such that the set X' = B(x*, ε) ⊂ X.
Note that for some N, x_n ∈ X', all n ≥ N; without loss of generality we take N = 1.
Let D denote the boundary of the set X'.
Every point x_n has at least one representation as a convex combination of x* and a point in D.
For each n, choose α_n ∈ [0, 1] and d_n ∈ D such that x_n = α_n d_n + (1 − α_n) x*.
D is a bounded set and x_n → x* so α_n → 0.
Choose Y' such that T(x) ∩ Y' ≠ ∅, all x ∈ X'.
Then for each n, choose y_n ∈ T(d_n) ∩ Y', and define z_n = α_n y_n + (1 − α_n) y*, all n.
Since (d_n, y_n) ∈ A, all n, (x*, y*) ∈ A, and A is convex, it follows that (x_n, z_n) ∈ A, all n.
Moreover, since α_n → 0 and all of the y_n lie in the bounded set Y', it follows that z_n → y*.
Hence {(x_n, z_n)} lies in A and converges to (x*, y*), as was to be shown. □ To see why x* must be an interior point, consider the case where X' is a disk and A is an inverted cone that is slanted so the tip is directly above the boundary of X'.
Let x* be the point below the tip of the cone, and take a sequence {x_n} along the boundary of the disk.
Then each set T(x_n) is a single point, but T(x*) is an interval.
We are now ready to answer the questions: Under what conditions do the function h(x) defined by the maximization problem in (1) and the associated set of maximizing y values G(x) defined in (2) vary continuously with x?
An answer is provided in the following theorem.
### THEOREM 3.6
(Theorem of the Maximum) Let X ⊂ R^l and Y ⊂ R^m, let f: X × Y → R be a continuous function, and let T: X → Y be a compact-valued and continuous correspondence.
Then the function h: X → R defined in (1) is continuous, and the correspondence G: X → Y defined in (2) is nonempty, compact-valued, and u.h.c.
**Proof.** Fix x ∈ X.
The set P(x) is nonempty and compact, and f(x, ·) is continuous; hence the maximum in (1) is attained, and the set G(x) of maximizers is nonempty.
Moreover, since G(x) ⊂ T(x) and T(x) is compact, it follows that G(x) is bounded.
Suppose y_n → y, and y_n ∈ G(x), all n.
Since T(x) is closed, y ∈ T(x).
Also, since h(x) = f(x, y_n), all n, and f is continuous, it follows that f(x,y) = h(x).
Hence y ∈ G(x); so G(x) is closed.
Thus G(x) is nonempty and compact, for each x.
Next we will show that G(x) is u.h.c.
Fix x, and let {x_n} be any sequence converging to x.
Choose y_n ∈ G(x_n), all n.
Since T is u.h.c., there exists a subsequence {y_{n_k}} converging to y ∈ T(x).
Let z ∈ T(x).
Since T is l.h.c., there exists a sequence z_{n_k} → z, with z_{n_k} ∈ T(x_{n_k}), all k.
Since f(x_{n_k}, y_{n_k}) ≥ f(x_{n_k}, z_{n_k}), all k, and f is continuous, it follows that f(x, y) ≥ f(x, z).
Since this holds for any z ∈ T(x), it follows that y ∈ G(x).
Hence G is u.h.c.
Finally, we will show that h is continuous.
Fix x, and let {x_n} be any sequence converging to x.
Choose y_n ∈ G(x_n), all n.
Let h = lim sup h(x_n) and h = lim inf h(x_n).
Then there exists a subsequence {x_{n_k}} such that h = lim f(x_{n_k}, y_{n_k}).
But since G is u.h.c., there exists a subsequence of {y_{n_k}}, call it {y_{n_{k_j}}}, converging to y ∈ G(x).
Hence h = lim f(x_{n_{k_j}}, y_{n_{k_j}}) = f(x, y) = h(x).
An analogous argument establishes that h(x) = h.
Hence {h(x_n)} converges, and its limit is h(x). □ The following exercise illustrates through concrete examples what this theorem does and does not say.
Exercise 3.16 a.
Let X = R, and let T(x) = Y = [-1, 1], all x ∈ X.
Define f: X × Y → R by f(x, y) = xy^3.
Graph G(x); show that G(x) is u.h.c. but not l.h.c. at x = 0. b.
Let X = R, and let T(x) = [0, 4], all x ∈ X.
Define f(x,y) = max{2 − (y − 1)^2, x + 1 − (y − x)^2}.
Graph G(x) and show that it is u.h.c.
Exactly where does it fail to be l.h.c.? c.
Let X = R^l, T(x) = {y ∈ R: −x ≤ y ≤ x}, and f(x,y) = cos(y).
Graph G(x) and show that it is u.h.c.
Exactly where does it fail to be l.h.c.?
Suppose that in addition to the hypotheses of the Theorem of the Maximum the correspondence T is convex-valued and the function f is strictly concave in y.
Then G is single-valued, and by Exercise 3.11a it is a continuous function—call it g.
The next two results establish properties of g.
Lemma 3.7 shows that if f(x, y) is close to the maximized value f(x, g(x)), then y is close to g(x).
Theorem 3.8 draws on this result to show that if {f_n} is a sequence of continuous functions, each strictly concave in y, converging uniformly to f, then the sequence of maximizing functions {g_n} converges pointwise to g.
The latter convergence is uniform if X is compact.
### LEMMA 3.7
Let X ⊂ R^l and Y ⊂ R^m.
Assume that the correspondence T: X → Y is nonempty, compact- and convex-valued, and continuous, and let A be the graph of T.
Assume that the function f: A → R is continuous and that f(x, ·) is strictly concave, for each x ∈ X.
Define the function g: X → Y by g(x) = argmax_{y ∈ T(x)} f(x, y).g(x) = argmax f(x, y). y∈Γ(x) Then for each ε > 0 and x ∈ X, there exists δ > 0 such that y ∈ Γ(x) and |f[x, g(x)] − f(x, y)| < δ, implies ||g(x) − y|| < ε.
If X is compact, then δ can be chosen independently of x.
**Proof.** Note that under the stated assumptions g is a well-defined, continuous (single-valued) function.
We first prove the claim for the case where X is compact.
Note that in this case A is a compact set by Exercise 3.15.
For each ε > 0, define Aε = {(x, y) ∈ A: ||g(x) − y|| = ε}.
If Aε = ∅ for all ε > 0, then Γ is single-valued and the result is trivial.
Otherwise there exists ε > 0 sufficiently small such that for all 0 < ε < ε0, the set Aε is nonempty and compact.
For any such ε, let δ = min (x,y)∈Aε |f[x, g(x)] − f(x, y)|.
Since the function being minimized is continuous and Aε is compact, the minimum is attained.
Moreover, since [x, g(x)] ∈ Aε for all x ∈ X, it follows that δ > 0.
Then y ∈ Γ and ||g(x) − y|| = ε implies |f[x, g(x)] − f(x, y)| ≥ δ as was to be shown. ∎ If X is not compact, the argument above can be applied separately for each fixed x ∈ X. ∎
### THEOREM 3.8
Let X, Y, T, and Γ be as defined in Lemma 3.7.
Let {fn} be a sequence of continuous (real-valued) functions on A; assume that for each n and each x ∈ X, fn(x, ·) is strictly concave in its second argument.
Assume that f has the same properties and that fn → f uniformly (in the sup norm).
Define the functions gn and g by gn(x) = argmax fn(x, y), n = 1, 2,..., and y∈Γ(x) g(x) = argmax f(x, y). y∈Γ(x) Then gn → g pointwise.
If X is compact, gn → g uniformly.
**Proof.** First note that since gn(x) is the unique maximizer of fn(x, ·) on Γ(x), and g(x) is the unique maximizer of f(x, ·) on Γ(x), it follows that 0 < f[x, g(x)] − fn[x, gn(x)] ≤ f[x, g(x)] − f[x, gn(x)] + f[x, gn(x)] − fn[x, gn(x)] ≤ 2||f − fn|| for all x ∈ X.
Since fn → f uniformly, it follows immediately that for any δ > 0, there exists Nδ = 1 such that (3) 0 < f[x, g(x)] − fn[x, gn(x)] ≤ 2||f − fn|| < δ for all x ∈ X, all n ≥ Nδ.
To show that gn → g pointwise, we must establish that for each ε > 0 and x ∈ X, there exists Nε = 1 such that (4) ||gn(x) − g(x)|| < ε, all n ≥ Nε.
By Lemma 3.7, it suffices to show that for any δ > 0 and x ∈ X there exists Nδ = 1 such that (5) |f[x, g(x)] − fn[x, gn(x)]| < δ, all n ≥ Nδ.
From (3), it follows that any Nδ = Nδ has the required property.
Suppose X is compact.
To establish that gn → g uniformly, we must show that for each ε > 0 there exists N = 1 such that (4) holds for all x ∈ X.
By Lemma 3.7, it suffices to show that for any δ > 0, there exists N = 1, such that (5) holds for all x ∈ X.
From (3) it follows that any N = Nδ has the required property. ∎ 3.4 Bibliographic Notes For a more detailed discussion of metric spaces, see Kolmogorov and Fomin (1970, chap. 2) or Royden (1968, chap. 7).
Good discussions of normed vector spaces can be found in Kolmogorov and Fomin (1970, chap. 4) and Luenberger (1969, chap. 2), both of which also treat the Contraction Mapping Theorem.
Blackwell’s sufficient condition is Theorem 5 in Blackwell (1965).
The Theorem of the Maximum dates from Berge (1963, chap. 6), and can also be found in Hildenbrand (1974, pt.
I.B).
Both of these also contain excellent treatments of upper and lower hemi-continuity.
We are grateful to David Levine and Michael Jansson for pointing out that the argument in Theorem 3.5 applies only on the interior of the set.
## 4 Dynamic Programming under Certainty
Posed in terms of infinite sequences, the problems we are interested in are of the form (SP) sup ∑_{t=0}^∞ β^t F(x_t, x_{t+1}) {x_{t+1}} s.t. x_{t+1} ∈ Γ(x_t), t=0,1,2,..., x0 ∈ X given.
Corresponding to any such problem, we have a functional equation of the form (FE) u(x) = sup [F(x, y) + βu(y)], all x ∈ X. y∈Γ(x) In this chapter we establish the relationship between solutions to these two problems and develop methods for analyzing the latter.
Exercise 4.1 a.
Show that the one-sector growth model discussed at the beginning of Chapter 3 can be expressed as in (SP). b.
Show that the many-sector growth model sup ∑_{t=0}^∞ β^t U(c_t) {c_t,k_t} s.t.
(k_t, c_t, k_{t+1}) ∈ Z, t=0,1,2,..., given k0 ∈ R_+^k, where Z ⊂ R_+^{2k+1} is a fixed production set, can also be written this way. 4.1 Principle of Optimality As we hinted in the last chapter and will show in this one, some very powerful—and relatively simple—mathematical tools can be used to study the functional equation (FE).
To take advantage of these, however, we must show that solutions to (FE) correspond to solutions to the sequence problem (SP).
In Section 4.1 we rigorously establish the connections between solutions to these two problems, connections that Richard Bellman called the Principle of Optimality.
Section 4.2 then develops the main results of the chapter: existence, uniqueness, and characterization theorems for solutions to (FE) under the assumption that the return function F is bounded.
The case where F displays constant returns to scale is treated in Section 4.3, and the case where F is an arbitrary unbounded return function in Section 4.4.
Section 4.5 treats the relationship between the dynamic programming approach to optimization over time and the classical (variational) approach.
Section 4.6 contains references for further discussion of some of the mathematical and economic ideas.
In Chapter 5 we illustrate how the methods developed in Sections 4.2—4.4 can be applied to a wide variety of economic problems. 4.1 The Principle of Optimality In this section we study the relationship between solutions to the problems (SP) and (FE).
(Note that “sup” has been used instead of “max” in both, so that we can ignore—for the moment—the question of whether the optimum is attained.) The general idea, of course, is that the solution v to (FE), evaluated at x0, gives the value of the supremum in (SP) when the initial state is x0 and that a sequence {x_{t+1}}_0 attains the supremum in (SP) if and only if it satisfies (1) u(x_t) = F(x_t, x_{t+1}) + βu(x_{t+1}), t= 0,1,2,....
Richard Bellman called these ideas the Principle of Optimality.
Intuitive as it is, the Principle requires proof.
Spelling out precisely the conditions under which it holds is our task in this section.
The main results are Theorem 4.2, establishing that the supremum function v* for the sequence problem (SP) satisfies the functional equation (FE), and Theorem 4.3, establishing a partial converse.
The “partial” nature of the converse arises from the fact that a boundedness condition must be imposed.
Theorems 4.4 and 4.5 then deal with the characterization of optimal policies.
Theorem 4.4 shows that if {x_{t+1}}_0 is a sequence attaining the supremum in (SP), then it satisfies (1) for v = v*.
Conversely, Theorem 4.5 establishes that any sequence {x_{t+1}}_0 that satisfies (1) for v = v*, and also satisfies a boundedness condition, attains the supremum in (SP).
The four theorems taken together thus establish conditions under which solutions to (SP) and to (FE) coincide exactly, and optimal policies are those that satisfy (1).
To begin we must establish some notation.
Let X be the set of possible values for the state variable x.
In this section we will not need to impose any restrictions on the set X.
It may be a subset of a Euclidean space, a set of functions, a set of probability distributions, or any other set.
Let Γ: X—> X be the correspondence describing the feasibility constraints.
That is, for each x ∈ X, Γ(x) is the set of feasible values for the state variable next period if the current state is x.
Let A be the graph of Γ: A = {(x,y) ∈ X × X: y ∈ Γ(x)}.
Let the real-valued function F: A > R be the one-period return function, and let β = 0 be the (stationary) discount factor.
Thus the “givens” for the problem are X, Γ, F, and β.
First we must establish conditions under which the problem (SP) is well defined.
That is, we must find conditions under which the feasibleequation (FE) has at most one solution satisfying (8).
In summary, we have established two main results about solutions to (FE).
Theorem 4.2 shows that v* satisfies (FE).
The functional equation may have other solutions as well, but Theorem 4.3 shows that these extraneous solutions always violate (8).
Hence a solution to (FE) that satisfies (8) is v*.
The following example is a case where (FE) has an extraneous solution in addition to v*.
Consider a consumer whose objective function is simply discounted consumption.
The consumer has initial wealth x₀ ∈ X = ℝ, and he can borrow or lend at the interest rate β⁻¹ − 1, where β ∈ (0, 1).
There are no constraints on borrowing, so his problem is simply max  Σ βⁱcₜ t=0 s.t.  0 ≤ cₜ ≤ xₜ − βxₜ₊₁, t= 0,1,..., x₀ given.
Since consumption is unbounded, the supremum function is obviously v*(x) = +∞, all x.
Now consider the recursive formulation of this problem.
The return function is F(x, y) = x − βy, and the correspondence describing the feasible set is T(x) = (−∞, β⁻¹x]; so the functional equation is u(x) = sup_{y∈Tx)} [x − βy + βu(y)].
The function v*(x) = +∞ satisfies this equation, as Theorem 4.2 implies, but the function u(x) = x does, too.
But since the sequence xₜ = β⁻ᵗx₀, t= 0,1,..., is in Π(x₀), (8) does not hold and Theorem 4.3 does not apply.
The next exercise gives two variations on Theorem 4.3 that are sometimes useful when (8) does not hold.
Exercise 4.3 Let X, T, F, and β satisfy Assumptions 4.1—4.2.
Let v be a solution to (FE) with lim sup βᵗv(xₜ) = 0, all x₀ ∈ X, all (x₀, x₁, . . .) ∈ Π(x₀), a.
Show that v = v*. b.
Suppose in addition that for each x₀ ∈ X and x ∈ Π (x₀), there exists x’ = (x₀, x₁, x₂,...) ∈ Π(x₀) such that limₜ→∞ βᵗv(xₜ) = 0 and v(x’) = v(x).
Show that v = v*.
Our next task is to characterize feasible plans that attain the optimum, if any do.
Call a feasible plan x ∈ Π(x₀) an optimal plan from x₀ if it attains the supremum in (SP), that is, if v(x) = v*(x₀).
The next two theorems deal with the relationship between optimal plans and those that satisfy the policy equation (1) for v = v*.
The next theorem shows that optimal plans satisfy (1).
### THEOREM 4.4
Let X, T, F, and β satisfy Assumptions 4.1—4.2.
Let x* ∈ Π (x₀) be a feasible plan that attains the supremum in (SP) for initial state x₀.
Then (9) v* (xₜ) = F (xₜ, xₜ₊₁) + βv*(xₜ₊₁), t= 0,1,2,....
**Proof.** Since x* attains the supremum, (10) v* (xₜ) = v(x*) = F (xₜ, xₜ₊₁) + βv*(x*ₜ₊₁) = v(x*) = F (xₜ, xₜ₊₁) + βv(x*’), all x ∈ T(xₜ).
In particular, the inequality holds for all plans with x₁ = x*₁.
Since (xₜ, x₂, x₃, ...) ∈ (x*ₜ) implies that (x₀, x*₁, x₂, x₃, ...) ∈ T(x₀), it follows that v(x’) = v(x*’), all x’ ∈ Π(x*ₜ).
Hence v(x*’*) = v(x*).
Substituting this into (10) gives (9) for t = 0.
Continuing by induction establishes (9) for all t. = 76 4 1 Dynamic Programming under Certainty The next theorem provides a partial converse to Theorem 4.4.
It shows that any sequence satisfying (9) and a boundedness condition is an optimal plan.
### THEOREM 4.5
Let X, T, F, and β satisfy Assumptions 4.1—4.2.
Let x* ∈ Π (x₀) be a feasible plan from x₀ satisfying (9), and with (11) lim sup βᵗv*(x*ₜ) = 0.
Then x* attains the supremum in (SP) for initial state x₀.
**Proof.** Suppose that x* ∈ Π(x₀) satisfies (9) and (11).
Then it follows by an induction on (9) that v*(x₀) = v*(x*ₜ) + βᵗ v*(x*ₜ₊₁), n= 1,2,...
Then using (11), we find that v*(x₀) = v(x*).
Since x* ∈ Π(x₀), the reverse inequality holds, establishing the result. # The consumption example used after Theorem 4.3 can be modified to illustrate why (11) is needed.
Let preferences be as specified before, so that cₜ = xₜ − βxₜ₊₁ = F(x, xₜ₊₁), all t.
However, let us prohibit indebtedness by requiring xₜ = 0, all t.
Then in sequence form the problem is max  Σ βⁱ(xₜ − βxₜ₊₁) t=0 s.t. 0 ≤ xₜ₊₁ ≤ β⁻¹xₜ, t= 0,1,..., x₀ given.
If we cancel all of the offsetting terms in the objective function, it follows immediately that the supremum function is v*(x₀) = x₀, all x₀ ≥ 0.
It is also clear that v* satisfies the functional equation v*(x) = max_{y∈Tx)} [(x − βy) + βv*(y)], all x, as Theorem 4.2 implies.
Now consider plans that attain the optimum.
Given any x₀ ≥ 0, the set of feasible plans Π(x₀) consists of the sequences (x₀, 0, 0, 0, … (x₀, β⁻¹x₀, 0, 0, ...), (x₀, β⁻¹x₀, β⁻²x₀, 0, . . . etc., and all convex combinations thereof.
Hence every feasible plan satisfies (9).
It is straightforward to verify that, as Theorem 4.5 implies, any plan that satisfies (11) as well yields utility v*(x₀) = x₀.
(Essentially, it does not matter when consumption occurs as long as it occurs in finite time.) On the other hand, the feasible plan xₜ = β⁻ᵗx₀, t = 0, 1,..., (in each period invest everything and consume nothing) yields discounted utility of zero, for all x₀ = 0.
For x₀ > 0, however, it violates (11), so Theorem 4.5 does not apply.
We will call any nonempty correspondence G: X ⇉ X, with G(x) ⊆ T(x), all x ∈ X, a policy correspondence, since the set G(x) is a feasible set of actions if the state is x.
If G is single-valued, we will call it a policy function and denote it by a lowercase g.
If a sequence x = (x₀, x₁, . . .) satisfies xₜ₊₁ ∈ G(xₜ), t = 0,1, 2,..., we will say that x is generated from x₀ by G.
Finally, we will define the optimal policy correspondence G* by G*(x) = {y ∈ T(x): v*(x) = F(x, y) + βv*(y)}.
Then Theorem 4.4 shows that every optimal plan {xₜ} is generated from G*, and Theorem 4.5 shows that any plan {xₜ} generated from G*—if, in addition, it satisfies (11)—is an optimal plan. 4.2 Bounded Returns In this section we study functional equations of the form (1) v(x) = max_{y∈Tx)} [F (x, y) + βv(y)], under the assumption that the function F is bounded and the discount factor β is strictly less than one.
As above, let X be the set of possible values for the state variable; let T: X ⇉ X be the correspondence describing the feasibility constraints; let A = {(x, y) ∈ X × X : y ∈ T(x)} be the graph of T; let F:A → ℝ be the return function; and let β ∈ (0, 1) be the discount factor.
Throughout this section, we will impose the following two assumptions on X, T, F, and β.
ASSUMPTION 4.3 X is a convex subset of ℝⁿ, and the correspondence T : X ⇉ X is nonempty, compact-valued, and continuous.
ASSUMPTION 4.4 The function F: A → ℝ is bounded and continuous, and 0<β<1.
It is clear that under Assumptions 4.3—4.4, Assumptions 4.1—4.2 hold, so the sequence problem corresponding to (1) is well defined.
Moreover, Theorems 4.2—4.5 imply that under these assumptions solutions to (1) coincide exactly—in terms of both values and optimal plans—to solutions of the sequence problem.
The requirement that X be a subset of a finite-dimensional Euclidean space could be relaxed in much of what follows, but at the expense of a substantial additional investment in terminology and notation.
(Recall that the definitions of u.h.c. and l.h.c. provided in Chapter 3 applied only to correspondences from one Euclidean space to another.) However, most of the arguments in this section apply much more broadly.
Also note that the assumption that X is convex is not needed for Theorems 4.6 and 4.7.
If M is a bound for |F (x, y)|, then the supremum function v* satisfies |v*(x)| ≤ M/(1 − β), all x ∈ X.
In this case it is natural to seek solutions to (1) in the space C(X) of bounded continuous functions f: X → ℝ, with the sup norm: ||f|| = sup_{x∈X}|f(x)|.
Clearly, any solution to (1) in C(X) satisfies the hypothesis of Theorem 4.3 and hence is the supremum function.
Moreover, given a solution v ∈ C(X) to (1), we can define the policy correspondence G: X ⇉ X by (2) G(x) = {y ∈ T(x): v(x) = F(x, y) + βv(y)}, and Theorems 4.4 and 4.5 imply that for any x₀ ∈ X, a sequence {xₜ} attains the supremum in the sequence problem if and only if it is generated by G.
The rest of the section proceeds as follows.
Define the operator T on C(X) by(3) (Tf)(x) = max | F(x, y) + βf(y) | y∈I(x) 4.2 Bounded Returns 79 so (1) becomes v = Tv.
First, if we use only the boundedness and continuity restrictions in Assumptions 4.3 and 4.4, Theorem 4.6 establishes that T: C(X) → C(X), that T has a unique fixed point in C(X), and that the policy correspondence G defined in (2) is nonempty and u.h.c.
Theorem 4.7 establishes that under additional monotonicity restrictions on F and I, v is strictly increasing.
Theorem 4.8 establishes that under additional concavity restrictions on F and convexity restrictions on T, v is strictly concave and G is a continuous (single-valued) function.
Theorem 4.9 shows that if {vₙ} is a sequence of approximations defined by vₙ = Tⁿv₀, with v₀ appropriately chosen, then the sequence of associated policy functions {gₙ} converges uniformly to the optimal policy function g given by (2).
Finally, Theorem 4.11 establishes that if F is continuously differentiable, then v is, too.
### THEOREM 4.6
Let X, I, F, and β satisfy Assumptions 4.3 and 4.4, and let C(X) be the space of bounded continuous functions f: X → ℝ, with the sup norm.
Then the operator T maps C(X) into itself, T: C(X) → C(X); T has a unique fixed point v ∈ C(X); and for all v₀ ∈ C(X), (4) |Tⁿv — v| ≤ βⁿ|v₀ — v|, n = 0,1,2,....
Moreover, given v, the optimal policy correspondence G: X ⇒ X defined by (2) is compact-valued and u.h.c.
**Proof.** Under Assumptions 4.3 and 4.4, for each f ∈ C(X) and x ∈ X, the problem in (3) is to maximize the continuous function [F(x, y) + βf(y)] over the compact set I(x).
Hence the maximum is attained.
Since both F and f are bounded, clearly Tf is also bounded; and since F and f are continuous, and I is compact-valued and continuous, it follows from the Theorem of the Maximum (Theorem 3.6) that Tf is continuous.
Hence T: C(X) → C(X).
It is then immediate that T satisfies the hypotheses of Blackwell’s sufficient conditions for a contraction (Theorem 3.3).
Since C(X) is a Banach space (Theorem 3.1), it then follows from the Contraction Mapping Theorem (Theorem 3.2), that T has a unique fixed point v ∈ C(X), and (4) holds.
The stated properties of G then follow from the Theorem of the Maximum, applied to (1).
It follows immediately from Theorem 4.3 that under the hypotheses of Theorem 4.6, the unique bounded continuous function v satisfying (1) is the supremum function for the associated sequence problem.
That is, Theorems 4.3 and 4.6 together establish that under Assumptions 4.3–4.4 the supremum function is bounded and continuous.
Moreover, it then follows from Theorems 4.5 and 4.6 that there exists at least one optimal plan: any plan generated by the (nonempty) correspondence G is optimal.
To characterize v and G more sharply, we need more information about F and I.
The next two results show how Corollary 1 to the Contraction Mapping Theorem can be used to obtain more precise characterizations of v and G.
ASSUMPTION 4.5 For each y, F(·, y) is strictly increasing in each of its first arguments.
ASSUMPTION 4.6 I is monotone in the sense that x = x' implies I(x) ⊂ I(x').
### THEOREM 4.7
Let X, I, F, and β satisfy Assumptions 4.3–4.6, and let v be the unique solution to (1).
Then v is strictly increasing.
**Proof.** Let C'(X) ⊂ C(X) be the set of bounded, continuous, nondecreasing functions on X, and let C"(X) ⊂ C'(X) be the set of strictly increasing functions.
Since C'(X) is a closed subset of the complete metric space C(X), by Theorem 4.6 and Corollary 1 to the Contraction Mapping Theorem (Theorem 3.2), it is sufficient to show that T[C'(X)] ⊂ C"(X).
Assumptions 4.5 and 4.6 ensure that this is so.
ASSUMPTION 4.7 F is strictly concave; that is, F(λ(x, y) + (1 — λ)(x', y')) > λF(x,y) + (1 — λ)F(x', y'), all (x, y), (x',y') ∈ A, and all λ ∈ (0, 1), and the inequality is strict if x ≠ x'.
ASSUMPTION 4.8 I is convex in the sense that for any 0 < λ ≤ 1, and x,x' ∈ X, y ∈ I(x) and y' ∈ I(x') implies λy + (1 — λ)y' ∈ I[λx + (1 — λ)x']. 4.2 Bounded Returns 81 Assumption 4.8 implies that for each x ∈ X the set I(x) is convex and there are no “increasing returns.” Note that since X is convex, Assumption 4.8 is equivalent to assuming that the graph of I (the set A) is convex.
### THEOREM 4.8
Let X, I, F, and β satisfy Assumptions 4.3–4.4 and 4.7–4.8; let v satisfy (1); and let G satisfy (2).
Then v is strictly concave and G is a continuous, single-valued function.
**Proof.** Let C'(X) ⊂ C(X) be the set of bounded, continuous, weakly concave functions on X, and let C"(X) ⊂ C'(X) be the set of strictly concave functions.
Since C'(X) is a closed subset of the complete metric space C(X), by Theorem 4.6 and Corollary 1 to the Contraction Mapping Theorem (Theorem 3.2), it is sufficient to show that T[C'(X)] ⊂ C"(X).
To verify that this is so, let f ∈ C'(X) and let x₀, x₁ ∈ X, λ ∈ (0,1), and x_λ = λx₀ + (1 — λ)x.
Let y_i ∈ I(x) attain (Tf)(x_i), for i = 0, 1.
Then by Assumption 4.8, y_λ = λy₀ + (1 — λ)y₁ ∈ I(x_λ).
It follows that (Tf) (x_λ) = F (x_λ, y_λ) + βf (y_λ) > λ[F (x₀, y₀) + βf(y₀)] + (1 — λ)[F (x₁, y₁) + βf(y₁)] = λ(Tf)(x₀) + (1 — λ)(Tf)(x₁), where the first line uses (3) and the fact that y_λ ∈ I(x_λ); the second uses the hypothesis that f is concave and the concavity restriction on F in Assumption 4.7; and the last follows from the way y₀ and y₁ were selected.
Since x₀ and x₁ were arbitrary, it follows that Tf is strictly concave, and since f was arbitrary, that T[C'(X)] ⊂ C"(X).
Hence the unique fixed point v is strictly concave.
Since F is also concave (Assumption 4.7) and, for each x ∈ X, I(x) is convex (Assumption 4.8), it follows that the maximum in (3) is attained at a unique y value.
Hence G is a single-valued function.
The continuity of G then follows from the fact that it is u.h.c.
(Exercise 3.11).
Theorems 4.7 and 4.8 characterize the value function by using the fact that the operator T preserves certain properties.
Thus if v₀ has property 82 4 Dynamic Programming under Certainty P and if P is preserved by T, then we can conclude that each function in the sequence {Tⁿv₀} has property P.
Then, if P is preserved under uniform convergence, we can conclude that v also has property P.
The same general idea can be used to establish facts about the policy function g, but we need to establish the sense in which the approximate policy functions—the functions gₙ that attain Tⁿv₀—converge to g.
The next result draws on Theorem 3.8 to address this issue.
### THEOREM 4.9
(Convergence of the policy functions) Let X, I, F, and β satisfy Assumptions 4.3–4.4 and 4.7–4.8, and let v and g satisfy (1) and (2).
Let C'(X) be the set of bounded, continuous, concave functions f: X → ℝ, and let v₀ ∈ C'(X).
Let {(vₙ, gₙ)} be defined by vₙ₊₁ = Tvₙ, n=0,1,2,..., and gₙ(x) = argmax [F (x,y) + βvₙ(y)], n = 0,1,2,... y∈I(x) Then gₙ → g pointwise.
If X is compact, then the convergence is uniform.
**Proof.** Let C"(X) ⊂ C'(X) be the set of strictly concave functions f: X → ℝ.
As shown in Theorem 4.8, v ∈ C"(X).
Moreover, as shown in the proof of that theorem, T[C'(X)] ⊂ C"(X).
Since v₀ ∈ C'(X), it then follows that every function vₙ, n = 1,2,..., is strictly concave.
Define the functions {fₙ} and f by fₙ(x, y) = F(x, y) + βvₙ(y), n= 1,2,..., and f(x, y) = F(x, y) + βv(y).
Since F satisfies Assumption 4.7, it follows that each function fₙ, n = 1, 2,..., is strictly concave, as is f.
Hence Theorem 3.8 applies and the desired results are proved.
The next exercise deals with the case where the state space X is finite or countable, as it is in computational applications.
Exercise 4.4.
Let X = {x₁, x₂,...} be a finite or countable set; let the correspondence I: X ⇒ X be nonempty and finite-valued; let A = 4.2 Bounded Returns 83 {(x, y) ∈ X × X: y ∈ I(x)}; let F: A → ℝ be a bounded function; and let 0 <β <1.
Let B(X) be the set of bounded functions f: X → ℝ, with the sup norm.
Define the operator T by (3).a.
Show that \( T: B(X) \to B(X) \); that \( T \) has a unique fixed point \( v \in B(X) \); that (1) holds for all \( v \in B(X) \); and that the optimal policy correspondence \( G: X \rightrightarrows X \) defined by (2) is nonempty.
Let \( H \) be the set of functions \( h: X \to X \) such that \( h(x) \in I(x) \), all \( x \in X \).
For any \( h \in H \), define the operator \( T_h \) on \( B(X) \) by \( (T_h f)(x) = F[x, h(x)] + B f[h(x)] \). b.
Show that for any \( h \in H \), \( T_h: B(X) \to B(X) \), and \( T_h \) has a unique fixed point \( w_h \in B(X) \).
Let \( h_0 \in H \) be given, and consider the following algorithm.
Given \( h_n \), let \( w_n \) be the unique fixed point of \( T_{h_n} \).
Given \( w_n \), choose \( h_{n+1} \) so that \[ h_{n+1}(x) \in \arg\max_{y \in I(x)} \{ F(x, y) + B w_n(y) \}. \] c.
Show that the sequence of functions \( \{w_n\} \) converges to \( v \), the unique fixed point of \( T \). [Hint.
Show that \( w_0 = T w_0 \) and \( w_1 = T w_1 \), ...] An algorithm based on Exercise 4.4 involves applying the operators \( T_h \) – operators that require no maximization – repeatedly and applying \( T \) only infrequently.
Since maximization is usually the expensive step in these computations, the savings can be considerable.
Once the existence of a unique solution \( v \in C(X) \) to the functional equation (1) has been established, we would like to treat the maximum problem in that equation as an ordinary programming problem and use the standard methods of calculus to characterize the policy function \( g \).
For example, consider the functional equation for the one-sector growth model: \[ u(x) = \max_{0 \le y \le f(x)} \{ U[f(x) - y] + B v(y) \}. \] If we knew that \( v \) was differentiable (and that the solution to the maximum problem in (1) was always interior), then the policy function \( g \) would be given implicitly by the first-order condition \[ U'[f(x) - g(x)] - B v'[g(x)] = 0. \] Moreover, if we knew that \( v \) was twice differentiable, the monotonicity of \( g \) could be established by differentiating (5) with respect to \( x \) and examining the resulting expression for \( g' \).
However, the legitimacy of these methods depends upon the differentiability of the functions \( U, f, v, \) and \( g \).
We are free to make whatever differentiability assumptions we choose for \( U \) and \( f \), but the properties of \( v \) and \( g \) must be established.
We turn next to what is known about this issue.
It has been shown by Benveniste and Scheinkman (1979) that under fairly general conditions the value function \( v \) is once differentiable.
That is, (5) is valid under quite broad conditions.
However, known conditions ensuring that \( v \) is twice differentiable (and hence that \( g \) is once differentiable) are extremely strong (see Araujo and Scheinkman 1981).
Thus differentiating (5) is seldom useful as a way of establishing properties of \( g \).
However, in cases where \( g \) is monotone, it is usually possible to establish that fact by a direct argument involving a first-order condition like (5).
We begin with the theorem proved by Benveniste and Scheinkman. **THEOREM 4.10** (Benveniste and Scheinkman) Let \( X \subset \mathbb{R}^l \) be a convex set, let \( V: X \to \mathbb{R} \) be concave, let \( x_0 \in \text{int } X \), and let \( D \) be a neighborhood of \( x_0 \).
If there is a concave, differentiable function \( W: D \to \mathbb{R} \), with \( W(x_0) = V(x_0) \) and with \( W(x) \le V(x) \) for all \( x \in D \), then \( V \) is differentiable at \( x_0 \), and \[ V_i(x_0) = W_i(x_0), \quad i = 1,2,\dots,l. \] **Proof.** Any subgradient \( p \) of \( V \) at \( x_0 \) must satisfy \[ p(x - x_0) \le V(x) - V(x_0) = W(x) - W(x_0), \quad \text{all } x \in D, \] where the first inequality uses the definition of a subgradient and the second uses the fact that \( W(x) \le V(x) \), with equality at \( x_0 \).
Since \( W \) is differentiable at \( x_0 \), \( p \) is unique, and any concave function with a unique subgradient at an interior point \( x_0 \) is differentiable at \( x_0 \) (cf.
Rockafellar 1970, Theorem 25.1, p. 242). \(\square\) Figure 4.1 illustrates the idea behind this result.
Applying this result to dynamic programs is straightforward, given the following additional restriction. **ASSUMPTION 4.9** \( F \) is continuously differentiable on the interior of \( A \). **THEOREM 4.11** (Differentiability of the value function) Let \( X, T, F, \) and \( B \) satisfy Assumptions 4.3–4.4 and 4.7–4.9, and let \( v \) and \( g \) satisfy (1) and (2).
If \( x_0 \in \text{int } X \) and \( g(x_0) \in \text{int } I(x_0) \), then \( v \) is continuously differentiable at \( x_0 \), with derivatives given by \[ v_i(x_0) = F_i[x_0, g(x_0)], \quad i = 1,2,\dots,l. \] **Proof.** Since \( g(x_0) \in \text{int } I(x_0) \) and \( I \) is continuous, it follows that \( g(x_0) \in \text{int } I(x) \), for all \( x \) in some neighborhood \( D \) of \( x_0 \).
Define \( W \) on \( D \) by \[ W(x) = F[x, g(x_0)] + B v[g(x_0)]. \] Since \( F \) is concave (Assumption 4.7) and differentiable (Assumption 4.9), it follows that \( W \) is concave and differentiable.
Moreover, since \( g(x_0) \in I(x) \) for all \( x \in D \), it follows that \[ W(x) = \max_{y \in I(x)} [F(x, y) + B v(y)] = v(x), \quad \text{all } x \in D, \] with equality at \( x_0 \).
Hence \( v \) and \( W \) satisfy the hypotheses of Theorem 4.10, and the desired results follow immediately. \(\square\) Note that the proof requires only that \( F \) be differentiable in its first \( l \) arguments.
With differentiability of the value function established, it is often straightforward to show that the optimal policy function \( g \) is monotone, and to bound its slope. **Exercise 4.5.** Consider the first-order condition (5).
Assume that \( U, f, \) and \( v \) are strictly increasing, strictly concave, and once continuously differentiable, and that \( 0 < g(x) < f(x) \), all \( x \).
Use (5) to show that \( g \) is strictly increasing and has slope less than the slope of \( f \).
That is, \[ 0 < g(x') - g(x) < f(x') - f(x), \quad \text{if } x' > x. \] [Hint.
Refer to Figure 4.2.] In specific applications it is often possible to obtain much sharper characterizations of \( v \) or of \( G \) or of both than those provided by the theorems above.
It is useful to keep in mind that once the existence and uniqueness of the solution to (1) has been established, the right side of that equation can be treated as an ordinary maximization problem.
Thus whatever tools can be brought to bear on that problem should be exploited.
But such arguments usually rely on properties of \( F \) or of \( I \) or of both that are specific to the application at hand.
The problems in Chapter 5 provide a variety of illustrations of specific arguments of this type.
It should also be emphasized that even in cases that do not quite fit the assumptions of this section, arguments similar to the ones above can often be used.
In this sense the results above should be viewed as suggestive, not (by any means) definitive.
Sections 5.12 and 5.15 illustrate this point, as do many other applications in the literature.
One particularly good illustration is the case of dynamic programming problems that exhibit constant returns to scale, to which we turn next. **4.3 Constant Returns to Scale** We sometimes wish to work with return functions \( F \) that are unbounded.
For example, in the one-sector model of optimal growth, any utility function of the form \( U(c) = (c^{1-\sigma} - 1)/(1 - \sigma), \sigma \neq 1 \), together with any technology of the form \( f(k) = k^\alpha, 0 < \alpha < 1 \), leads to an unbounded return function.
In this case and others like it, Assumption 4.4 is violated if \( X \) is taken to be all of \( \mathbb{R}_+ \).
There are several ways to deal with problems of this type.
In some cases it is natural to restrict the state space to be a compact set \( X \subset \mathbb{R}^l \).
If \( I \) is compact-valued and continuous and if \( F \) is continuous, then with this restriction on \( X \) imposed, \( F \) is bounded on the compact set \( A \).
In these cases the arguments in Section 4.2 can be applied directly.
Thus a judicious choice of the state space is very often all that is needed to apply those arguments to problems in which utility functions, profit functions, and so on, are unbounded.
Illustrations of this method are given in Sections 5.1 and 5.9.
However, there are also many interesting cases where the state space cannot be so restricted.
For example, no model of capital accumulation in which the technology permits sustained growth can be treated in this way.
In this section and the next, we describe two ways in which the arguments in Section 4.2 can be adapted to models with unbounded returns.This section deals with systems in which the return function and feasibility constraints both display constant returns to scale, and the constraints have the further property that feasible sequences {x} cannot grow "too fast." First we show that Theorems 4.2–4.5 hold for problems of this type, so solutions to the functional equation correspond exactly to solutions of the original problem posed in terms of sequences, in terms of both values and policies.
Theorems 4.12 and 4.13 then establish that the functional equation has a unique solution, and that this solution and the associated policy correspondence are homogeneous of degree one.
Throughout this section we let X be a convex cone in ℝᴺ.
That is, X ⊂ ℝᴺ is a convex set with the property that x ∈ X implies λx ∈ X, for any λ ≥ 0.
For example, ℝᴺ and ℝᴺ₊ are both convex cones.
In place of Assumptions 4.3 and 4.4, we will use the following restrictions.
As in Section 4.2, let Γ denote the graph of T.
ASSUMPTION 4.10 X ⊂ ℝᴺ is a convex cone.
The correspondence T : X → X is nonempty, compact-valued, and continuous, and for any x ∈ X, y ∈ T(x) implies λy ∈ T(λx), all λ ≥ 0.
That is, the graph of T is a cone.
In addition, for some α ∈ (0, 1), ‖y‖ ≤ α‖x‖, all x ∈ X and y ∈ T(x), (where ‖·‖ denotes the Euclidean norm on ℝᴺ).
ASSUMPTION 4.11 β ∈ (0,1); and F : A → ℝ is continuous and homogeneous of degree one, and for some 0 < B < ∞, |F(x, y)| ≤ B(‖x‖ + ‖y‖), all (x, y) ∈ A.
Assumption 4.10 says that the correspondence T describing the feasibility constraints shows constant returns to scale, and it bounds the rate of growth of {‖x_t‖} for feasible sequences {x_t} by α⁻¹.
Assumption 4.11 says that the return function F displays constant returns to scale, and it imposes a uniform bound on the ratio of F to the norm of its arguments.
Under Assumptions 4.10–4.11 we have the following results.
Exercise 4.6 Show that under Assumptions 4.10–4.11, a. ‖x_t‖ ≤ αᵗ‖x_0‖, t = 1,2,..., all x_0 ∈ X, all {x} ∈ Γ(x_0); b.
Assumptions 4.1–4.2 hold; and c. the supremum function v*: X → ℝ defined in Section 4.1 is homogeneous of degree one, and for some 0 < c < ∞, satisfies |v*(x)| = c‖x‖, all x ∈ X.
Part (b) of this exercise establishes that under Assumptions 4.10–4.11, Theorems 4.2 and 4.4 hold.
That is, the supremum function v* satisfies the functional equation, and every optimal sequence {x_t} (if any exist) is generated from the policy correspondence G associated with v*.
Moreover, v* has the properties established in part (c) of the exercise.
Our next task is to choose an appropriate space of functions within which to look for solutions to the functional equation and then to define an appropriate operator on that space.
In view of the results in Exercise 4.6c, it is natural to seek solutions to the functional equation within the space of functions f: X → ℝ that are continuous and homogeneous of degree one, and bounded in the sense that |f(x)|/‖x‖ < +∞ all x ∈ X, x ≠ 0.
To capture the latter fact, it is useful to use the norm ‖f‖ = max_{‖x‖=1} |f(x)|.
Let H(X) be the space of functions f: X → ℝ that are continuous and homogeneous of degree one, and bounded in the norm in (1).
Define the operator T on H(X) by (2) (Tf)(x) = sup_{y∈T(x)} [F(x, y) + βf(y)].
Exercise 4.7 a.
Show that H(X), with the norm in (1), is a complete normed vector space. b.
Show that under Assumptions 4.10 and 4.11, T: H(X) → H(X).
It follows directly from Exercise 4.6a that for any f ∈ H(X), |f(x)| ≤ ‖f‖‖x‖ = c‖x‖ ≤ α‖x‖‖f‖ = α‖x‖‖f‖, all x ∈ X, all {x} ∈ Γ(x).
Since αβ < 1, it then follows that the hypotheses of Theorems 4.3 and 4.5 hold.
Therefore v* is the only solution in H(X) to the functional equation, and every sequence {x_t} generated by the associated policy correspondence G is optimal.
Thus the Principle of Optimality applies to this type of constant-returns-to-scale problem.
The contraction property of the operator T can be verified by using a modification of Blackwell’s sufficient conditions for a contraction (Theorem 3.3).
For any function f that is homogeneous of degree one and for any a ≥ 0, we will in this context define the function f + a by (f + a)(x) = f(x) + a‖x‖, (where here and below we drop the subscript ‖·‖).
It is immediate that f + a is also homogeneous of degree one.
### THEOREM 4.12
Let X ⊂ ℝᴺ be a convex cone, and let H(X) be as above, with the norm in (1).
Let T: H(X) → H(X) satisfy a.
(monotonicity) f, g ∈ H and f ≥ g implies Tf ≥ Tg; b.
(discounting) there exists γ ∈ (0, 1) such that for all f ∈ H and all a ≥ 0, T(f + a) ≤ Tf + γa.
Then T is a contraction with modulus γ.
**Proof.** By homogeneity of degree one, f(x) = ‖f‖‖x‖, all f ∈ H, all x ≠ 0.
Choose any f, g ∈ H(X).
Then f(x) = g(x) + [f(x) − g(x)] = g(x) + ‖f − g‖‖x‖[f(x)/‖f‖‖x‖ − g(x)/‖g‖‖x‖] = g(x) + ‖f − g‖‖x‖[f(x)/‖f‖‖x‖ − g(x)/‖g‖‖x‖] = g(x) + ‖f − g‖‖x‖[f(x)/‖f‖‖x‖ − g(x)/‖g‖‖x‖] all x ≠ 0.
That is, f = g + ‖f − g‖‖x‖.
Hence monotonicity and discounting respectively imply that Tf = T(g + ‖f − g‖) ≤ Tg + γ‖f − g‖.
Reversing the roles of f and g and combining the two results, we find that ‖Tf − Tg‖ ≤ γ‖f − g‖, as was to be shown. # Our next result uses this theorem to establish that the operator T defined in (2) is a contraction with modulus αβ.
### THEOREM 4.13
Let X, T, F, and β satisfy Assumptions 4.10 and 4.11, and let H(X) be as above.
Then the operator T defined in (2) has a unique fixed point v ∈ H(X).
In addition (3) ‖Tⁿv₀ − v‖ = (αβ)ⁿ‖v₀ − v‖, n = 0,1,2,..., all v₀ ∈ H(X); and the associated policy correspondence G: X → X is compact-valued and u.h.c.
Moreover, G is homogeneous of degree one: for any x ∈ X, y ∈ G(x) implies λy ∈ G(λx), all λ > 0.
**Proof.** As shown in Exercise 4.7, H(X) is a complete metric space and T: H(X) → H(X).
Clearly T satisfies the monotonicity condition of Theorem 4.12.
Choose f ∈ H(X) and a > 0.
Then T(f + a)(x) = sup_{y∈T(x)} [F(x, y) + β(f + a)(y)] = sup_{y∈T(x)} [F(x, y) + βf(y) + βa‖y‖] ≤ sup_{y∈T(x)} [F(x, y) + βf(y)] + αβa‖x‖ = (Tf)(x) + αβa‖x‖, where the third line uses Assumption 4.10.
Since x ∈ X was arbitrary, it follows that T(f + a) = Tf + αβa.
Hence T satisfies the discounting condition, and, by Theorem 4.12, T is a contraction of modulus αβ.
It then follows from the Contraction Mapping Theorem (Theorem 3.2) that T has a unique fixed point v ∈ H(X) and that (3) holds.
That G is u.h.c. and compact-valued then follows from the Theorem of the Maximum (Theorem 3.6).
Finally, suppose that y ∈ G(x).
Then y ∈ T(x) and v(x) = F(x, y) + βv(y).
It then follows from Assumption 4.10 that λy ∈ T(λx) and from the homogeneity of F and v that v(λx) = F(λx, λy) + βv(λy).
Hence λy ∈ G(λx). □ Exercise 4.8 Call a function f: X → ℝ quasi-concave if x ≠ x’, f(x) = f(x’) and θ ∈ (0, 1) implies f[θx + (1 − θ)x'] ≥ f(x’).
Call f strictly quasi-concave if the last inequality is strict. a.
Show that if X ⊂ ℝᴺ is a convex cone and f: X → ℝ is homogeneous of degree one and quasi-concave, then f is concave. b.
Assume in part (a) that f is strictly quasi-concave.
Show that if x, x’ ∈ X and x ≠ λx’, for any λ ≥ 0, then f(θx + (1 − θ)x') > θf(x) + (1 − θ)f(x'), all θ ∈ (0, 1). c.
Under what conditions is the fixed point v of the operator T defined in (2) strictly quasi-concave? [Hint.
Look at the proof of Theorem 4.8 and apply parts (a) and (b) of this exercise.] d.
Under what conditions is v differentiable? 4.4 Unbounded Returns In this section we present a theorem that is useful when Assumptions 4.1–4.2 hold, so that the supremum function v* satisfies the functional equation (Theorem 4.2), but the boundedness hypothesis needed for Theorem 4.3 does not hold.
In such cases the functional equation may have other solutions as well.
The main result of this section is Theorem 4.14, which gives sufficient conditions for a solution to the functional equation to be the supremum function v*.
We then show how this resultcan be applied to two economic models with specific functional forms.
The first is a one-sector model of optimal growth with a logarithmic utility function and a Cobb-Douglas production function; the second is an investment model with a quadratic objective function and linear constraints.
The proof of Theorem 4.14 exploits only the monotonicity of the operator T, defined on the set of all functions \( f: X \to \mathbb{R} \), by \[ (Tf)(x) = \sup_{y \in \Gamma(x)} [F(x, y) + \beta f(y)]. \] The idea behind the proof is to start with a function \( \phi \) that is an upper bound for \( v^* \) and then to apply the operator T to \( \phi \), iterating down to a fixed point. **THEOREM 4.14** Let \( X \), \( \Gamma \), \( F \), and \( \beta \) satisfy Assumptions 4.1—4.2, and let \( M \), \( u \), and \( v^* \) be defined as they were in Section 4.1.
Suppose there is a function \( \phi: X \to \mathbb{R} \) such that (1) \( T\phi \le \phi \), (2) \( \lim_{n \to \infty} (\beta^n \phi)(x) = 0 \), all \( x_0 \in X \), all \( x \in M(x) \); (3) \( u(x) \le \phi(x_0) \), all \( x_0 \in X \), all \( x \in M(x) \); If the function \( v: X \to \mathbb{R} \) defined by \[ v(x) = \lim_{n \to \infty} (T^n \phi)(x) \] is a fixed point of T, then \( v = v^* \). **Proof.** First we will show that \( v \) is well defined and that \( v \le v^* \).
Since the operator T is monotone, (1) implies that \( T^{n+1} \phi = T^n(T\phi) \le T^n \phi \), all \( n \).
Hence for each \( x \in X \), \( \{ (T^n \phi)(x) \} \) is a decreasing sequence.
If the sequence converges, then \( v(x) \) is the limiting value; if the sequence diverges, then \( v(x) = -\infty \).
Thus \( v \) is well defined and \( v \le \phi \).
It then follows from (2) that \( v \) satisfies the hypotheses in Exercise 4.3.
Hence \( v \le v^* \).
Next we will show that \( v = v^* \).
Since Assumptions 4.1—4.2 hold, Theorem 4.2 implies that \( Tv^* = v^* \).
Moreover, (3) implies that \( v^* \le \phi \).
Hence by the monotonicity of T, \( v^* = Tv^* \le T\phi \), continuing by induction, \( v^* \le T^n \phi \), all \( n \), establishing the desired result.
This theorem is particularly useful in the study of the unit elasticity and linear-quadratic models described above.
For these cases it is easy to guess at a solution to the functional equation (cf.
Exercise 2.3); Theorem 4.14 then ensures that this guess does indeed provide a solution to the problem at hand.
Moreover, as will be seen below, in these examples the value function and policy function have convenient closed forms that involve only a finite number of parameters.
This fact makes these two parametric structures especially useful for constructing examples, for computational purposes, and for econometric estimation.
We will apply Theorem 4.14 first to the unit elastic form of the one-sector optimal growth model: \[ \max_{\{k_{t+1}\}} \sum_{t=0}^{\infty} \beta^t \ln(k_t - k_{t+1}) \] \[ \text{s.t.} \quad 0 \le k_{t+1} \le k_t^\alpha, \quad t=0,1,2,\ldots, \] where \( \alpha, \beta \in (0, 1) \), and the set \( X \) is the open interval \( (0, \infty) \).
The return function is unbounded above and below on this interval.
(Note that even if we were to restrict attention to the set \( X' = (0, 1] \) of maintainable capital stocks, the return would be unbounded below.) Since \( \Gamma(k) = (0, k^\alpha] \), clearly Assumption 4.1 holds for all \( k \in X \).
To apply Theorem 4.14 to this problem we must also show that Assumption 4.2 holds.
To do this note that the technology constraint implies that \( \ln(k_{t+1}) \le \alpha \ln(k_t) \), all \( t \).
Given \( k_0 \), it then follows that any feasible path \( \{ k_t \} \in \Pi(k_0) \) satisfies \[ \ln(k_t) \le \alpha^t \ln(k_0), \quad \text{all } t. \] Hence for any \( k_0 \) and any feasible path \( \{ k_t \} \in \Pi(k_0) \), the sequence of oneperiod returns satisfies (4) \( F(k_t, k_{t+1}) = F(k_t, k_t^\alpha) = \ln(k_t - k_t^\alpha) \ge \alpha^t \ln(k_0) \), all \( t \).
Therefore \[ \lim_{T \to \infty} \sum_{t=0}^{T} \beta^t F^+(k_t, k_{t+1}) \ge \lim_{T \to \infty} \sum_{t=0}^{T} \beta^t [\alpha^t \ln(k_0)] = \ln(k_0)/(1 - \alpha\beta), \] all \( \{ k_t \} \in \Pi(k_0) \), all \( k_0 > 0 \), where \( F^+ \) is as defined in Section 4.1.
Hence Assumption 4.2 holds.
Next we need a function \( \phi \) that is an upper bound for the supremum function \( v^* \).
Since (4) implies that \[ v^*(k) \le \alpha \ln(k)/(1 - \alpha\beta), \quad \text{all } k> 0, \] we may take \( \phi(k) = \alpha \ln(k)/(1 - \alpha\beta) \).
With \( \phi \) so defined, clearly (1)—(3) hold.
Moreover, with T defined by \[ (Tf)(k) = \sup_{0 \le y \le k^\alpha} [\ln(k - y) + \beta f(y)], \] we can verify by direct calculation that \[ (T^n \phi)(k) = \alpha^n \ln(k) + \ln\left(1 - \alpha\beta + \alpha^2\beta + \dots + \alpha^n\beta^{n-1}\right) + \frac{\alpha\beta}{1 - \alpha\beta} \ln(\alpha\beta), \quad n=1,2,\dots \] This sequence converges to \[ v(k) = \frac{\alpha \ln(k)}{1 - \alpha\beta} + \ln\left(1 - \alpha\beta\right) + \frac{\alpha\beta}{1 - \alpha\beta} \ln(\alpha\beta). \] Recall from Exercise 2.3 that this function \( v \) is a fixed point of \( T \).
Hence by Theorem 4.14, \( v = v^* \).
Moreover, since Theorem 4.5 applies, the associated policy function, the constant saving rate policy \( g(k) = \alpha\beta k^\alpha \), generates the optimal sequence of capital stocks.
Theorem 4.14 is also applicable to problems with quadratic return functions.
There is an extensive literature on such problems, but a simple economic example suffices to illustrate the main ideas.
Let \( X = \mathbb{R} \), and let \( \Gamma(x) = \mathbb{R} \), all \( x \in \mathbb{R} \).
Consider the return function (5) \( F(x, y) = ax - bx^2/2 - c(y - x)^2/2 \), \( a,b,c > 0 \).
Think of the term \( ax - bx^2/2 \) as describing a firm's net revenue when its capital stock is \( x \), and the term \( c(y - x)^2/2 \) as the cost of changing the capital stock from \( x \) to \( y \).
Then, given a constant interest rate \( r > 0 \), the problem facing the firm is \[ \max_{\{x_{t+1}\}} \sum_{t=0}^{\infty} \delta^t \left[ a x_t - \frac{b}{2} x_t^2 - \frac{c}{2} (x_{t+1} - x_t)^2 \right], \] where \( \delta = 1/(1 + r) \).
To apply Theorem 4.14 to this problem, first note that the return function \( F \) in (5) is bounded above by \( a^2/(2b) \).
Hence the function \( \phi \) defined by \( \phi(x) = a^2/(2b(1-\delta)) \), all \( x \in \mathbb{R} \), satisfies (1)—(3).
Moreover, it follows by induction that the functions \( T^n\phi \) take the form: \[ (T^n \phi)(x) = \alpha_n x - \frac{\beta_n}{2} x^2 + \gamma_n, \] where the coefficients of these quadratic functions are given recursively by \( \alpha_0 = \beta_0 = 0 \), \( \gamma_0 = a^2/(2b(1-\delta)) \), and (6) \( \beta_{n+1} = \frac{b + \delta \beta_n + \delta c \beta_n}{1 + \delta c \beta_n} \) (7) \( \alpha_{n+1} = \frac{a + \delta c \beta_n \alpha_n}{1 + \delta c \beta_n} \) (8) \( \gamma_{n+1} = \gamma_n + \frac{(a + \delta c \beta_n \alpha_n)^2}{2b(1 + \delta c \beta_n)} \), \( n=0,1,\dots \).
It is a simple exercise to verify from (6) that \( \beta_{n+1} > \beta_n \), where \( \delta - 1 < \delta + c \), and then from (7) and (8) that \( \alpha_{n+1} > \alpha_n \) and \( \gamma_{n+1} > \gamma_n \).
The limit function \( v(x) = ax - \beta x^2/2 + \gamma \) clearly satisfies the functional equation, and hence Theorem 4.14 implies that it is the supremum function \( v^* \).
The associated policy function is \( g(x) = (a + \delta c \beta x)/(b + \delta \beta + \delta c \beta) \), and it follows from Theorem 4.5 that any sequence \( \{ x_t \} \) generated from it is optimal.
In this particular example, it would make economic sense to restrict \( \{ x_t \} \) to the interval \( X' = [0, a/b] \), since negative capital has no interpretation and accumulating more capital than \( a/b \) is costly and decreases revenues. \( F \) is bounded on \( X' \times X' \), so with this restriction the theory of Section 4.2 would apply.
But the computational advantage of quadratic returns stems from the fact that marginal returns are linear in the state variable(s).
Thus if all maxima are described by first-order conditions, the optimal policy function is also linear in the state variable(s).
Hence the convenience of the quadratic form is realized only if maxima are attained at interior points of the feasible set.
Setting \( X = \mathbb{R} \) and \( \Gamma(x) = \mathbb{R} \), all \( x \in X \), ensures that this is the case.
After obtaining a solution, we can always check to see if it satisfies economically reasonable restrictions.
(Note that in the example above, if \( x \) is in the interval \( [0, a/b] \), then the optimal sequence \( x_{t+1} = g(x_t), t=0,1,\dots \), remains in this interval for all \( t \).) ## 4.5 Euler Equations Theorem 4.14 is also useful in dealing with many-dimensional quadratic problems.
An upper bound \( \phi \) satisfying (1)—(3) is easy to calculate, since any concave quadratic is bounded above.
The iterates \( T^n\phi \) are readily computed, since they are defined by a finite number of parameters.
If the sequence converges, Theorem 4.14 implies that the limit function is the supremum function and Theorem 4.5 implies that the linear policy that attains it is optimal.
If the problem is strictly concave, there are no other optimal policies. ## 4.5 Euler Equations There is a classical (eighteenth-century) mode of attack on the sequence problem (SP) \( \sup_{\{x_{t+1}\}_{t=0}^{\infty}} \sum_{t=0}^{\infty} \beta^t F(x_t, x_{t+1}) \) \[ \text{s.t.} \quad x_{t+1} \in \Gamma(x_t), \quad t=0,1,2,\dots, \] \[ x_0 \in X \text{ given}, \] that involves treating it as straightforward programming problem in the decision variables \( \{x_{t+1}\}_{t=0}^{\infty} \).
Necessary conditions for an optimal program can be developed from the observation that if \( \{ x_t^* \}_{t=0}^{\infty} \) solves the problem (SP), given \( x_0 \), then for \( t = 0, 1, \dots \), \( x_{t+1}^* \) must solve (1) \( \max_{y \in \Gamma(x_t^*)} [F(x_t^*, y) + \beta F(y, x_{t+2}^*)] \)for necessary conditions for continuous-time problems, but it has become standard in economics to use it for the discrete-time analogues of these conditions.) In most cases the adaptation from one setting to the other is straightforward, and in fact many of the applications we discuss in Chapter 5 were originally formulated and studied in continuous time.
There are many good texts discussing the mathematical techniques used for such problems, the calculus of variations, and the closely related Maximum Principle of Pontryagin et al.
(1962).
Arrow and Kurz (1970) and Kamien and Schwartz (1981) are excellent examples.
## 5 Applications of Dynamic Programming under Certainty
This chapter contains some economic problems that illustrate how the methods developed in the last chapter can be applied.
Some of the problems are straightforward exercises and can be solved as presented.
Others are more open-ended, and in these cases specific results can be obtained only if additional assumptions are imposed.
The problems are not ordered in terms of difficulty. 5.1 The One-Sector Model of Optimal Growth In Chapter 2 we introduced the problem of optimal growth in a one-good economy: (1) max ∑ βᵗU[f(xₜ) - xₜ₊₁], {xₜ₊₁}ₜ₌₀ s.t. 0 ≤ xₜ₊₁ = f(xₜ), t=0,1,..., given x₀ ≥ 0.
This problem is defined by the parameter β, the functions U: R₊ → R and f: R₊ → R₊, and the initial capital stock x₀.
The assumptions we will use for preferences are (U1) 0<β<1; (U2) U is continuous; (U3) U is strictly increasing; (U4) U is strictly concave; (U5) U is continuously differentiable.
For the technology we assume that (T1) f is continuous; (T2) f(0) = 0, and for some x̄>0: x < f(x) < x, all 0 ≤ x < x̄, and f(x) < x, all x > x̄; (T3) f is strictly increasing; (T4) f is (weakly) concave; (T5) f is continuously differentiable.
Note that [0, x̄] is the set of maintainable capital stocks; let X = (0, x̄].
Note, too, that (U3) and (T3) justify the assumption, implicit in (1), that free disposal is never used.
Corresponding to the problem in (1), we have the functional equation (2) v(x) = max {U[f(x) - y] + βv(y)}. 0 ≤ y ≤ f(x) Exercise 5.1 a.
Show that under (U1)—(U3) and (T1)-(T3), the hypotheses of Theorems 4.2—4.5 are satisfied. b.
Show that under (U1)—(U3) and (T1)-(T3), the hypotheses of Theorems 4.6 and 4.7 are satisfied.
From part (a) we conclude that solutions to (1) and (2) coincide exactly.
From part (b) we conclude that there exists a unique bounded continuous function v satisfying (2) and that the optimal policy correspondence G is nonempty and u.h.c.
Hence a maximizing sequence for (1) exists, for each x₀ ∈ X, and v(x₀) gives the present discounted value of total utility from an optimal sequence.
We also conclude that the function v is strictly increasing.
A sharper characterization of v and G requires additional structure.
Exercise 5.1 c.
Show that under (U1)—(U4) and (T1)-(T4), the hypotheses of Theorem 4.8 are satisfied.
From part (c) we conclude that under the additional restrictions, v is strictly concave, and the optimal policy correspondence G is single-valued and continuous.
Finally, consider the issue of differentiability. 5.4 Growth with Technical Progress Exercise 5.1 d.
Assume that (U1)—(U5) and (T1)-(T5) hold, and let G = g.
Show that if g(x) ∈ (0, f(x)), then v is differentiable at x and v'(x) = U'[f(x) - g(x)]f'(x).
Provide restrictions on U or f or both that, in addition to the assumptions above, guarantee that 0 < g(x) < f(x), all 0 < x < x̄.
What can be said about the differentiability of v at x when these assumptions fail?
What can be said when g(x) = 0 or g(x) = f(x)? e.
To emphasize their dependence on the discount factor β, write the value and policy functions as v(x, β) and g(x, β).
Show that g(x, β) is increasing in β. 5.2 A "Cake-Eating" Problem Consider the model in Section 5.1, with preferences satisfying (U1)—(U5) and with the technology f(k) = k, all k ∈ R₊.
Exercise 5.2 a.
Show that f satisfies (T1) and (T3)—(T5) and that any x̄ > 0 can be used to define X. b.
For U(c) = ln(c), find the value function v and the policy function g explicitly. c.
What can be said about v and g in general? 5.3 Optimal Growth with Linear Utility Consider the model in Section 5.1, with a technology f satisfying assumptions (T1)—(T5), with β satisfying (U1), and with U(c) = c, all c ∈ R₊.
Exercise 5.3 a.
Indicate which results from Exercise 5.1 hold under these assumptions and which do not. b.
Define k* = max_{k≥0} [βf(k) - k].
Show that for some s > 0, if k < k*, then v(k) = f(k) - k* + βv(k*) - βv(s). c.
Characterize the optimal policy as fully as possible. 5.4 Growth with Technical Progress The model presented in Section 5.1 can be viewed as describing an economy in which the size of the population, the (inelastic) supply of labor per capita, and the technology are all constant over time.
In this problem we will retain the first two of these assumptions, but drop the third.
Instead, assume that technological change increases the supply of effective labor units each period by the factor (1 + A) > 1.
Suppose in addition that the production function F(K, L), which has capital and effective labor units as arguments, shows constant returns to scale, and assume that capital depreciates at the rate δ > 0.
Finally, suppose that the preferences of the representative consumer over consumption C are of the form U(C) = Cᵞ/γ, where γ < 1. [For γ = 0, this utility function is interpreted as U(C) = ln(C).] Then letting I denote gross investment, we can write the optimal growth problem as max ∑ βᵗ Cᵢᵞ/γ {Cₜ, Iₜ}ₜ₌₀ s.t.
Cₜ + Iₜ = F(Kₜ, Lₜ), all t; Lₜ₊₁ = (1 + A)Lₜ, all t; Kₜ₊₁ = (1 - δ)Kₜ + Iₜ, all t; K₀, L₀ > 0 given.
It is easiest to analyze this problem by renormalizing all variables by the factor (1 + A).
Without loss of generality, we may choose units of labor so that L₀ = 1.
Then define kₜ = Kₜ/Lₜ, cₜ = Cₜ/Lₜ, iₜ = Iₜ/Lₜ, all t.
In addition define the function f: R₊ → R₊ by f(k) = F(1, k).
Note that if F is strictly increasing, strictly concave, and continuously differentiable, then f also has these properties.
Using these definitions, we can write the optimal growth problem as max ∑ [β(1 + A)⁻¹]ᵗ cₜᵞ/γ {cₜ, iₜ}ₜ₌₀ s.t. cₜ + iₜ = f(kₜ), all t; kₜ₊₁ = [(1 - δ)kₜ + iₜ] / (1 + A), all t; k₀ > 0 given. 5.6 Learning by Doing Exercise 5.4 Write the functional equation for the renormalized problem and show that, if A(1 + A)^(γ⁻¹) < 1, the analysis of Section 5.1 goes through without change. 5.5 A Tree-Cutting Problem Consider a tree whose growth is described by the function h.
That is, if kₜ is the size of the tree in period t, then kₜ₊₁ = h(kₜ), t = 0, 1,....
Assume that the price of wood p and the interest rate r are both constant over time; let p = 1 and β = 1/(1 + r).
Assume that it is costless to cut down the tree.
Exercise 5.5 a.
If the tree cannot be replanted, present value maximization leads to the functional equation v(k) = max {p k, β v[h(k)]}.
Under what assumptions about h is there a simple rule describing when the tree ought to be cut down and sold? b.
Suppose that when the tree is cut down, another can be planted in its place.
When this tree is cut down another can be planted, and so on.
Assume that the cost of replanting, c ≥ 0, is constant over time.
Under what assumptions about h and c is there a simple rule describing when trees should be harvested? 5.6 Learning by Doing Consider a monopolist producing a new product; we are interested in the case where the production function for the product displays learning by doing.
Specifically, suppose that the unit cost of production within each period t is a constant, ĉ, but that unit cost falls over time as a function of cumulative experience.
Let qₜ denote production and Qₜ denote cumulative experience at the beginning of period t: Q₀ = 0 and Qₜ₊₁ = Qₜ + qₜ, t=0,1,....economic interpretation of the absence of a nonnegativity constraint on gross investment?
How must the analysis of this problem be altered if there are lower and upper bounds on gross investment?
That is, how does the solution change if the constraints (1 − δ)k ≤ y_t+1 ≤ (1 − δ) + α_t, t = 0,1,..., for some α > 0 are added to the firm’s problem? b.
Suppose instead that the total cost of investment is a convex function c of the level of gross investment, where c: R → R, is strictly increasing, strictly convex, and differentiable, with c(0) = 0.
Then the firm’s problem is max ∑ β^t [p_t f(k_t) − c(k_{t+1} − (1 − δ)k_t)] k_{t+1}≥0 Formulate the functional equation for this problem, and characterize the solution v and the policy function g as fully as possible.
Derive the Euler equations and compare them with the Euler equations in part (a). c.
Suppose that in addition to capital there is a variable input, labor.
Let F(k, 0) be the production function, and let w > 0 be the wage rate.
Consider the firm’s “short-run” problem: Let Π(k) = max_{l≥0} {pF(k, l) − wl}.
Under what conditions on F are Π and the “short-run” labor demand function l = l(k) well defined?
Under what conditions does Π have the properties ascribed to f in parts (a) and (b)? 5.10 Investment with Constant Returns Suppose that we modify the model in Section 5.9 so that output z depends negatively on end-of-period capital y, due to internal technological “adjustment costs.” That is, let z = F(k, y) where F: R₊ × R₊ → R₊.
Let F be continuously differentiable, increasing in k, and decreasing in y.
Assume that F exhibits constant returns: F(λk, λy) = λF(k, y), all λ > 0; and that F is strictly quasi-concave: if (k°, y°) = θ(k, y) + (1 − θ)(k', y'), θ ∈ (0,1), then F(k°, y°) > min{F(k, y), F(k', y')}, where (k°, y°) = θ(k, y) + (1 − θ)(k', y').
Also assume that the marginal adjustment cost becomes arbitrarily high as the rate of growth of capital approaches α > 0.
That is, for some α > 0, lim_{y→(1+α)k} F_y(k, y) > −∞.
Let δ ∈ (0, 1) be the depreciation rate and q > 0 the price of capital.
Define v*(k_0) = max ∑ β^t [p_t F(k_t, y_t) − q [y_t − (1 − δ)k_t]}] y_t≥0 s.t.
(1 − δ)k_t ≤ y_t ≤ (1 + α)k_t, all t; k_0 > 0 given.
Exercise 5.10 a.
Show that v* is homogeneous of degree one.
Consider the corresponding functional equation: v(k) = max {p F(k, y) − q [y − (1 − δ)k] + β v(y)}.
(1−δ)k≤y≤(1+α)k Exercise 5.10 b.
Show that any function v satisfying the functional equation is also homogeneous of degree one. c.
Characterize as fully as possible solutions to the functional equation and the corresponding policy correspondence.
What needs to be assumed about α and δ?
What is the relationship between solutions to the functional equation and solutions to the sequence problem? 5.11 Recursive Preferences Let L be the space of sequences c = (c_0, c_1,.. .), with c_t ∈ R^L, t = 0,1, ..., that are bounded in the norm ‖c‖ = sup_t ‖c_t‖, where ‖·‖ is the Euclidean norm on R^L.
For any c = (c_0, c_1, ...), define c_t = (c_t, c_{t+1}, ...), t ≥ 0, c^t = (0, ..., 0, c_t, c_{t+1}, ...) ∈ L.
We have so far been dealing with preferences u: L → R of the form u(c) = ∑_{t=0}^∞ β^t U(c_t), where β ∈ (0, 1) and U: R^L → R is bounded and continuous.
Exercise 5.11 a.
Show that any function u: L → R of this form is bounded and is continuous in the norm ‖·‖.
Let S be the vector space of all bounded continuous functions u: L → R, with the norm |u| = sup_{c∈L} |u(c)|.
Exercise 5.11 b.
Show that S is complete.
Is it true that lim_{t→∞} |u(c) − u(c^t)| = 0, all u ∈ S?
For any β ∈ (0, 1) and U: R → R, we can define an operator T: S → S by (Tu)(c) = U(c_0 + β u(c_1)).
Exercise 5.11 c.
Show that the function u ∈ S defined by u(c) = ∑_{t=0}^∞ β^t U(c_t) is the unique fixed point of T.
A much larger class of utility functions on L can be defined in an analogous way.
Let W: R^L × S → R be a continuous function with the following properties: (W1) W(0, 0) = 0; (W2) for any z ∈ S, W(·, z): R^L → R is bounded; and (W3) for some β ∈ (0, 1), |W(x, z) − W(x, z’)| ≤ β ‖z − z’‖, all x ∈ R^L and z, z’ ∈ S.
We will call a function W with these properties an aggregator function.
W(x, z) is interpreted as the utility enjoyed from now on if x ∈ R^L is consumed today and if consumption from tomorrow on yields z ∈ S utils as of tomorrow.
Two additional properties of W will be useful.
(W4) W is increasing; (W5) W is concave.
Exercise 5.11 d.
Let W satisfy (W1)–(W3), and define the operator T_W: S → S by (T_W u)(c) = W[c_0, u(c_1)].
Show that T_W has a unique fixed point u_W ∈ S and that |u_W(c) − u_W(c^t)| ≤ β^t sup_{c∈L} |u_W(c)|, all c ∈ L.
Show that if (W4) holds then u_W is increasing; show that if (W5) holds then u_W is concave. e.
Assume that W is continuously differentiable.
Obtain an expression for the marginal rate of substitution between c_t and c_{t+k} as a function of c, t, k. 5.12 Theory of the Consumer with Recursive Preferences Consider an infinitely lived consumer with preferences given by u ∈ S, where u(c) = W[c_0, u(c_1)], all c ∈ L, and W is an aggregator function as defined in Section 5.11.
The problem facing this consumer is (1) max u(c) s.t. ∑_{t=0}^∞ R^t p_t c_t ≤ A, c∈L where p_t ∈ R^L_+ is a constant vector of spot prices; R = 1/(1 + r), where r > 0 is a constant rate of interest; and A is his initial wealth.
The functional equation for this problem is (2) v(A) = max W(C, v(R[A − p·C])), C∈Γ(A) where Γ(A) = {C ∈ R^L_+: p·C ≤ A}.
Exercise 5.12 a.
Modify Theorems 4.2–4.5 to relate (1) and (2). b.
Show that (2) has a unique bounded continuous solution v and that the consumer demand function C = C(p, A) is well defined, continuous, and homogeneous of degree zero in (p, A). c.
Under what conditions is v continuously differentiable?
Assuming these conditions hold, state and interpret the first-order conditions for the problem (2). d.
Let h: R → S be a bounded, continuously differentiable, strictly increasing function, with h(0) = 0.
Define W̃(C, a) = h(W[h^{-1}(C), h^{-1}(a)]).
Show that the demand functions from (2) implied by W̃ coincide with those for W.
Is W̃ necessarily an aggregator function as defined in Section 5.11, provided W is? 5.13 A Pareto Problem with Recursive Preferences Consider a two-person pure exchange economy in which both agents have preferences of the type described in Section 5.11.
Assume that there is a single consumption good available each period.
Hence the commodity space is the space of all bounded sequences c = (c_0, c_1, ...); with c_t ∈ R, all t.
Feasible consumption sequences for either agent are sequences c with c_t ≥ 0, all t.
The two agents are characterized by aggregator functions W_i: R × S → S, i = 1, 2; let u_i, i = 1, 2, be the corresponding preferences over feasible consumption sequences.
The economy has an endowment of one unit of consumption good each period.
Hence, in any period t, if agent 1 gets c_t, agent 2 gets 1 − c_t.
Let I = {c = {c_t}: 0 ≤ c_t ≤ 1, all t} be the space of feasible allocations for agent 1.
Let 1 denote the sequence (1, 1, 1,...) and 0 = (0, 0, 0,...), and let J_i = [u_i(0), u_i(1)], i = 1, 2, be the sets of possible utilities for the two agents.
Let S be the space of continuous functions f: I → I, with the sup norm.
Consider the operator T defined by (Tf )(x) = max_{y∈J_2} W_1(c, f(y)), s.t.
W_2(1 − c, y) = x.
Exercise 5.13 a.
Show that T: S → S and that T is a contraction. b.
What is the relationship between the unique fixed point v of T and the function v* defined on I by v*(x) = sup_{c∈I} u_1(c) s.t. u_2(1 − c) = x? 5.14 An (s, S) Inventory Problem Consider a manager who can sell up to one unit of a certain product each period, at a price p.
If he has x = 0 units in stock, he can sell min{x, 1} units.
He can also order any amount y of new goods, to be delivered at the beginning of next period, at a cost c_0 + c_1 y, paid now.interval [4, B) ⊆ [0, 1).
If he charges a price P = A, then with probability one all consumers buy the product and the seller gets no new information.
Clearly he never chooses a price less than A.
If he chooses a price P = B, then with probability one he sells nothing and gains no new information.
Clearly he never sets a price greater than B.
If he sets a price P ∈ (A, B), then the probability that R = P is (B − P)/(B − A); this is the probability that consumers buy the product and his posterior beliefs are a uniform distribution on [P, B).
Conversely, with probability (P − A)/(B − A), he sells nothing and his posterior beliefs are a uniform distribution on [A, P).
Let v(A, B) denote the expected discounted profits of the seller when he knows that the reservation price is uniformly distributed on [A, B) ⊆ [0, 1).
Then v must satisfy the functional equation v(A, B) = sup { (1 − δ)P + δ[ ((B − P)/(B − A)) v(P, B) + ((P − A)/(B − A)) v(A, P) ] }.
This functional equation does not quite fit the framework developed in Section 4.2, since the planner cannot choose next period’s state.
Rather, he can only choose an action, the price; next period’s state is then a random function of the price.
However, the arguments used in Section 4.2 can be modified to fit this case.
Let D = { (x, y) ∈ [0, 1]²: x < y}.
Let C be the space of bounded continuous functions f: D → R, with the sup norm.
Define the operator T on C by: (Tf)(A, B) = sup { (1 − δ)P + δ[ ((B − P)/(B − A)) f(P, B) + ((P − A)/(B − A)) f(A, P) ] }.
Exercise 5.16 a.
Show that T: C → C, and that T satisfies Blackwell’s sufficient conditions for a contraction.
Hence T has a unique fixed point v ∈ C.
Use Corollary 1 to the Contraction Mapping Theorem to show that v is homogeneous of degree one.
Since v is homogeneous of degree one, there exists a bounded continuous function w: [0, 1] → R+ such that v(A, B) = B w(A/B), for 0 < A < B < 1.
Define a = A/B and p = P/B.
It then follows that v(A, P) = P w(A/P) = B p w(a/p), and v(P, B) = B w(p).
Substituting these expressions into the functional equation above and dividing through by B, we find that w satisfies w(a) = sup { (1 − δ)p + δ [ ((p − a)/(p − a)) w(1) + ((p − a)/(p − a)) w(a/p) ] }? ...
(equation appears garbled in OCR) Exercise 5.16 b.
Show that w is strictly increasing and weakly convex, with w(1) = 1/(1 − δ). [Hint.
What operator is w a fixed point of?] What properties does this imply for v?
It is reasonable to conjecture that, if the interval [A, B] is sufficiently small, then it is optimal to set the price equal to A; that is, it is optimal simply to set the highest price for which it is known with certainty that consumers will buy.
If this policy is adopted, the seller does not gain any new information.
Hence he will face exactly the same problem next period and will set a price of A.
To show that this is the case, it is convenient to work with the transformed problem.
In terms of the transformed problem, the conjecture above is that the optimal policy function g corresponding to w has the following form: there exists some ā such that g(a) = a, for all a ∈ [0, ā].
Note that, if this conjecture is correct, then w(a) = a/(1 − δ), for all a ∈ [0, ā].
Exercise 5.16 c.
Use the functional equation for w to verify that this conjecture is correct and to show that ā = 1/(2 − δ). 5.17 A Consumption-Savings Problem Consider a consumer with preferences ∑_{t=0}^{∞} β^t U(c_t) over infinite consumption sequences c = (c₀, c₁, ...), where U: R → R is continuously differentiable, strictly increasing, and strictly concave, and where 0 < β < 1.
The function U need not be bounded.
The consumer has a constant income J > 0 each period, and in addition has initial wealth x₀ = 0 in period 0.
The consumer can save, but he cannot borrow.
The interest rate r is constant over time, and the interest factor R = (1 + r) satisfies 0 < R < 1/β.
Exercise 5.17 a.
State the consumer’s problem in sequence form, and state the corresponding functional equation.
Show that the supremum function v*: R+ → R for the sequence problem is well defined and that it satisfies the functional equation.
Show that for any fixed x₀ ≥ 0, if the plan x* ∈ Π(x₀) attains the supremum for the sequence problem, then it satisfies v*(x*) = U(J + x₀) − x₁/R) + β v*(x₁), t=0,1,...
For this problem, we can construct both v* and the associated optimal policy function g* by conjecturing the form of the solution and then establishing that the conjecture is correct.
Specifically, we will construct a function v: R+ → R that satisfies (1) v(x) = sup_{0≤y≤(x+J)R} [ U(J + x − y/R) + β v(y) ], and establish that v = v*.
We will also show that the policy function g associated with v generates all of the optimal plans for the problem in part (a).
Since RB < 1 and J > 0, we conjecture that the consumer exhausts his initial wealth in finite time and then simply consumes his income J > 0 in every period thereafter.
To check whether this conjecture is correct, construct g: R+ → R and v: R+ → R as follows.
We conjecture that for initial wealth in some interval [0, m₁], the consumer’s optimal policy is to consume his current income J > 0 plus his entire initial wealth x > 0 in the initial period (saving nothing), and in every subsequent period to consume his income J > 0.
Define m₁ by U'(J + m₁) = R β U'(J).
Then let g(x) = 0, x ∈ [0, m₁]; v(x) = U(J + x) + β U(J)/(1 − β), x ∈ [0, m₁].
Exercise 5.17 b.
Show that m₁ > 0 is well defined.
Show that v is continuous, strictly increasing, and strictly concave.
Show that v is continuously differentiable on [0, m₁), with v'(x) = U'(J + x), x ∈ [0, m₁).
Next we conjecture that for initial wealth in some interval (m₁, m₂], the consumer’s optimal plan is to consume part of his wealth in period 0 and to save the quantity y/R ∈ [0, m₁].
Then from period t = 1 on, he follows the plan described in part (b).
Define h: (0, m₁] → R+ by (2) U'[J + h(y) − y/R] = R β v'(y).
We conjecture that h(y) is the level of initial wealth that induces the consumer to save y/R and thus begin the subsequent period with initial wealth of y.
Exercise 5.17 c.
Show that h is continuous and strictly increasing, with lim_{y↓0} h(y) = m₁.
Define m₂ = lim_{y↑m₁} h(y), and let (3) g(x) = h⁻¹(x), x ∈ (m₁, m₂], (4) v(x) = U[J + x − g(x)/R] + β v(g(x)), x ∈ (m₁, m₂].
Exercise 5.17 d.
Show that m₂ > m₁.
Show that g is continuous and strictly increasing on (m₁, m₂].
Show that g is continuous at the point x = m₁.
Show that v is continuous, strictly increasing, and strictly concave on (m₁, m₂].
Show that v is continuously differentiable on (m₁, m₂), with (5) v'(x) = U'[J + x − g(x)/R], x ∈ (m₁, m₂). e.
Show that v and v’ are both continuous at the point m₁.
Continue by induction.
Given v on (m_{n-1}, m_n); define h: (m_{n-1}, m_n) → R+ by (2) and let m_{n+1} = h(m_n).
Then define g and v on (m_n, m_{n+1}] by (3)–(4).
Exercise 5.17 f.
Show that the properties of h, g, v, and v’ described in parts (c)–(e) hold on all of R+. g.
Show that v satisfies the functional equation (1).
Show that v = v*, where v* is the supremum function for the sequence problem in part (a). [Hint.
Show that x_t ≤ R^t (x + W), for all t, for all x ∈ H(x₀), for all x₀ = 0, where W = R J/(R − 1) is the discounted value of the consumer's income stream in period 0.] h.
Show that for any initial wealth x₀ > 0, the sequence x_{t+1} = g(x_t); t= 0,1,..., is the unique optimal plan for the sequence problem in part (a).
Show that 0 < g(x') − g(x) ≤ (1 − βR)/ (βR) (x' − x), with equality only if g(x) = g(x') = 0. 5.18 Bibliographic Notes The models in Sections 5.1, 5.3, 5.4, and 5.8 are all samples from the enormous literature on the theory of growth developed largely in the 1960s.
Most of this literature is carried out in continuous time, but it is easily restated in discrete time; and in no case discussed here is any change in substance involved in the translation.
Burmeister and Dobell(1970) is the best single reference to this body of theory.
Ramsey (1928) solved a version of the one-sector problem in Section 5.1, but with a discount factor equal to one.
Since the objective function for this problem does not, in general, converge, he studied the problem min_{x*} {U[f(x*)] - U[f(x) - x*]}, where x* is the capital stock that maximizes f(x) − x.
This objective is bounded above by zero.
The undiscounted problem clearly cannot be studied using the methods of Section 4.2, but try the theory of Sections 4.4 and 4.5.
The model of optimal growth with discounting in Section 5.1 was first studied by Cass (1965) and Koopmans (1965).
The type of exogenous technological change treated in Section 5.4 was first studied in Solow (1956), in the context of a nonoptimizing model of growth.
Solutions of the type found in Section 5.3 are called bang-bang solutions.
A two-sector model of this type that is a little more interesting is studied in Uzawa (1964).
The tree-cutting, or wine-aging, or cattle-fattening problem in Section 5.5 comes up in many different economic settings.
See Brock, Rothschild, and Stiglitz (1989) for a continuous-time analysis that is both simpler and more complete than is possible with our formulation here.
The problem of a monopolist with a learning-by-doing technology in Section 5.6 was studied by Clarke, Darrough, and Heineke (1982).
Parts (b) and (c) of this problem are from Stokey (1986).
The formulation of the individual human capital accumulation problem in Section 5.7 is taken from Rosen (1976).
Earlier dynamic analyses of this decision problem can be found in Becker (1962) and Ben-Porath (1967).
The model in Section 5.8 uses the human capital accumulation technology introduced by Rosen to obtain an aggregate growth model, a simplification of models described in Uzawa (1965) and in Lucas (1988).
Sections 5.9 and 5.10 provide samplings from the microeconomic literature on the investment decision of a single firm.
Part (a) of Exercise 5.9 is a discrete-time version of Jorgenson (1963).
Part (b) is from the model discussed in Eisner and Strotz (1963), later elaborated with variations in Lucas (1967a), Gould (1968), and Treadway (1969).
Mortensen (1973) provides the definitive treatment of the many-capital-goods version of this model.
The model in Section 5.10 is a constant-returns version of the one in Lucas (1967b).
Note that the term constant returns is ambiguous in a dynamic context: Gould (1968) uses it in a way different from that used in Section 5.10, and Kydland and Prescott (1982) use it in still a third way.
The recursive preferences analyzed in Section 5.11 were first studied in Koopmans (1960).
The analysis by Koopmans, Diamond, and Williamson (1964) is a useful sequel.
Uzawa (1968) proposes a continuous-time version of recursive preferences, which is generalized in Epstein (1987).
Sections 5.11—5.13 are taken directly from Lucas and Stokey (1984).
It is clear from Denardo (1967) that dynamic programming methods can be applied with recursive preferences that have a contraction property.
Early applications of this idea to economics are Beals and Koopmans (1969), Iwai (1972), and Boyer (1975).
The (s, S) models in Sections 5.14 and 5.15 are adapted from Scarf (1959), although the specific results here are new.
The (much harder) stochastic version of this problem is a classic, popularly thought to be thoroughly understood.
In fact, results have been obtained only for special cases.
For examples, see Arrow, Karlin, and Scarf (1958).
Section 5.16 is taken from Aghion, Bolton, and Jullien (1988).
See Rebelo (1987) or Jones and Manuelli (1987) for analyses of models similar to the one in Section 5.17, but with interest rates exceeding 1/β − 1. **6 Deterministic Dynamics** In Chapter 4 we established that problems of the form (SP) max_{\{x_{t+1}\}_{t=0}^\infty} \sum_{t=0}^\infty \beta^t F(x_t, x_{t+1}), s.t. x_{t+1} ∈ T(x_t), t = 0,1,..., given x_0 could be analyzed by studying the related functional equation (FE) v(x) = max_{y \in T(x)} [F(x, y) + \beta v(y)]. [Recall that X ⊂ \mathbb{R}^n is the state space; T: X \rightrightarrows X is a nonempty correspondence describing the feasibility constraints; A = {(x,y) \in X \times X : y \in T(x)} is the graph of T; F: A \to \mathbb{R} is the one-period return function; and \beta \in (0,1) is the discount factor.] Under Assumptions 4.3—4.4 and 4.7—4.9, there is a unique bounded continuous function v satisfying (FE) (Theorem 4.6); v is strictly concave, and the associated optimal policy function g defined by v(x) = F(x, g(x)) + \beta v(g(x)) is single-valued and continuous (Theorem 4.8); and given x_0, the sequence \{x_t\} defined by x_{t+1} = g(x_t), t = 0,1,..., is the unique solution to (SP) (Theorems 4.4 and 4.5).
If, in addition, Assumption 4.9 holds, then v is once differentiable at each point x for which g(x) \in \operatorname{int} T(x) (Theorem 4.11).
Suppose that Assumptions 4.3—4.4 and 4.7—4.9 hold and that the solution is everywhere interior.
In this case the first-order and envelope conditions from (FE) (1) 0 = F_y[x, g(x)] + \beta v'[g(x)], (2) v'(x) = F_x[x, g(x)], provide further information on g.
Equivalently, under these assumptions any sequence \{x_t\}_{t=0}^\infty that satisfies the Euler equations and transversality condition (3) 0 = F_x(x_t, x_{t+1}) + \beta F_x(x_{t+1}, x_{t+2}), t = 0,1,2,..., (4) 0 = \lim_{t \to \infty} \beta^t F_x(x_t, x_{t+1}) \cdot x_t is the unique solution to (SP), given x_0 (Theorem 4.15).
This chapter is concerned with methods for using (1)—(4) to characterize the behavior of solutions to (SP), either directly or by characterizing the function g.
In a numerical sense the problem (SP) has already been solved in Chapter 4.
Given (X, T, A, F, \beta), the functions v and g can be calculated, and the solution, given by x_{t+1} = g(x_t), t = 0,1,..., computed from any initial state x_0.
But this approach requires a particular specification of the constraints, return function, and discount factor, and gives no information about how the solution would be altered if these were changed.
It is often possible, however, to establish qualitative facts about solution paths for fairly wide classes of return functions, discount factors, and so on.
There is no single procedure for obtaining such characterizations, and sometimes an ad hoc approach to (1)—(2) or (3)—(4) is best.
Still, there are two standard lines of attack that are widely applicable, and we discuss them here.
In Section 6.1, we first discuss two examples, designed to illustrate that the properties of solution paths may be very simple or quite complicated.
Theorem 6.1 then shows that any function g in a very large class is the optimal policy function for some dynamic program and hence that the range of possible dynamics for solutions to (SP) is very broad.
This theorem indicates in advance that properties like stability are simply not in the cards as general features of solutions to problems like (SP).
On the contrary, solutions to problems of the form (SP) may cycle, explode, or display “chaotic” behavior. **6.1 One-Dimensional Examples 133** We do not attempt to review all of these possibilities here; the literature is vast and Section 6.6 contains suggestions for further reading.
Instead, in the remainder of the chapter we confine our attention to a review of two general methods that are often useful for establishing the global or local stability of solutions to (SP).
We do this because in most cases a large part of the positive content of dynamic economic models consists of their predictions about steady-state behavior.
The stability of the steady state is thus a crucial issue.
There are two relatively simple general methods for deciding whether a particular system is stable.
The first, known as the method of Liapounov, relies on information about the function g and is used for establishing global stability; it is discussed in Section 6.2.
The second approach is based on linear approximations to the Euler equations.(3) \((x - x') + [F(x, y) - F(x', y)]\) \(+ \beta [L(y) - L(y')] \geq 0,\) with equality if and only if \((x, y) = (x', y')\).
We also know that the first-order and envelope conditions hold: (4) \(L'(g(x)) = - \beta v'[g(x)], \quad \text{all } x \in X,\) (5) \(F_x(x, g(x)) = v'(x), \quad \text{all } x \in X.\) At any stationary point \(x\), (4) and (5) imply (6) \(v'(x) = F_x(x, x) = - \beta F_y(x, x)/\beta = -F_y(x, x).\) These are the facts we have to work with.
Now setting \(y = g(x)\) and \(x' = g(x')\) (i.e., \(x' = x\) and substituting from (4)–(6) into (3), we find that (7) \((x - x)[v'(x) - v'(x)] - \beta[g(x) - x] \cdot \{v'[g(x)] - v'(x)\} = 0,\) with equality if and only if \([x, g(x)] = (x, x)\).
But this in turn implies that \(L[g(x)] = L(x)/\beta.\) Hence if \(\beta = 1\), \(L\) is a Lyapunov function.
Our analysis in Chapter 4 did not cover the undiscounted case \(\beta = 1\), but the Euler equations (1) continue to define a dynamic system in this case.
When \(\beta = 1\) the necessary condition for a stationary point, \(F_x(x, x) + \beta F_y(x, x) = 0\), is also a sufficient condition for \(x\) to maximize the strictly concave function \(F(x, x)\) over \(x \in X\).
Hence there can be at most one stationary point in this case.
Then (7) together with Lemma 6.2 implies that if such a stationary point exists, it is globally stable.
For the discounted case, \(\beta < 1\), the best we can do is to go over the derivation of (7), to see whether there are possibilities for strengthening the inequality.
Equations (4)–(6) do not offer any such opportunities, but (3) does.
Since it is the \(\beta\) in (7) that needs to be offset, evidently a sufficient condition for \(L[g(x)] = L(x)\), all \(x\), is that (8) \(\beta(x - y) [F_x(x, y) - F_x(x, x)]\) \( + (y - x) [F_y(x, y) - F_y(x, x)] = 0, \quad \text{all } (x, y) \in A.\) This condition has the important virtue that it can be checked using the return function only, without calculating \(v\) or \(g\).
The following exercise provides an example.
Exercise 6.4 Let \(X = \mathbb{R}\) and suppose that \(F\) is a strictly concave quadratic function, with derivatives \(F_x(x, y) = a + b(x - y) + c(y - x),\) and \(F_y(x, y) = - \beta a + c(x - y) + d(y - x),\) where \(b > 0\), \(d > 0\), and \(bd - c^2 > 0\).
Then \(x\) is the unique stationary point.
Show that a sufficient condition for (8) is \(bd - (1 + \beta) c^2/4 = 0\). 6.3 Linear Systems and Linear Approximations There is a well-developed stability theory for systems of linear difference equations, systems of the form (1) \(x_{t+1} = a_0 + A x_t, \quad t = 0, 1, \dots,\) where \(x_t \in \mathbb{R}^n\) and where the \(n\)-vector \(a_0\) and the \(n \times n\) matrix \(A\) are constant.
If in (FE) the return function \(F\) is quadratic and \(L(x) = \|x\|^2\), all \(x\), then the optimal policy function \(g\) is linear and direct use can be made of this theory.
This was illustrated in Section 4.4 for the case \(n = 1\).
Even when \(g\) is not linear, it is often useful to study a suitable linear approximation to the dynamic system described by \(g\).
In this section we review the theory of linear systems and linear approximations; and in Section 6.4 we show how this theory can be used to study systems arising from dynamic programming problems.
Consider the system in (1).
Assume that the matrix \(I - A\) is nonsingular, so that \(x = (I - A)^{-1} a_0\) is the unique stationary point and the deviations \(z_t = x_t - x\) satisfy (2) \(z_{t+1} = A z_t, \quad t = 0, 1, \dots.\) The solution to (2) is obviously \(z_t = A^t z_0\), but this is not very informative unless we can characterize the behavior of the sequence \(\{A^t\}\).
To do this we use the fact that any square matrix \(A\) can be written as (3) \(A = B \Lambda B^{-1},\) where \(B\) is nonsingular and \(\Lambda\) is a Jordan matrix.
A Jordan matrix, in turn, is a block-diagonal matrix \(\Lambda = \begin{bmatrix} \Lambda_1 & 0 & \cdots & 0 \\ 0 & \Lambda_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \Lambda_k \end{bmatrix},\) where each block has the form \(\Lambda_i = \begin{bmatrix} \lambda_i & 1 & 0 & \cdots & 0 \\ 0 & \lambda_i & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_i & 1 \\ 0 & 0 & \cdots & 0 & \lambda_i \end{bmatrix}.\) The numbers \(\lambda_i\) — in general, complex — on the diagonal of the \(i\)-th block are all the same, the entries immediately above the diagonal are ones, and all other entries are zeros.
The numbers \(\lambda_1, \dots, \lambda_k\) are the distinct characteristic roots of \(A\): the solutions to \(\det(A - \lambda I) = 0\).
This equation is called the characteristic equation of \(A\) or of (1), and the expression \(\det(A - \lambda I)\) is called the characteristic polynomial.
Thus if \(A\) has \(n\) distinct characteristic roots, its Jordan matrix \(\Lambda\) is diagonal.
The point of writing \(A\) as in (3) becomes clear if we use the matrix \(B\) to define the new variable (5) \(w_t = B z_t = B (x_t - x), \quad t = 0, 1, \dots.\) Then using (2) and (3), we find that \(w_{t+1} = \Lambda w_t\), so (6) \(w_t = \Lambda^t w_0, \quad t = 1, 2, \dots.\) This result represents progress, because powers of Jordan matrices are easy to calculate.
If \(\Lambda\) is as shown in (4), then \(\Lambda^t = \begin{bmatrix} \Lambda_1^t & 0 & \cdots & 0 \\ 0 & \Lambda_2^t & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \Lambda_k^t \end{bmatrix}, \quad t = 1, 2, \dots,\) where each block has the form \(\Lambda_i^t = \begin{bmatrix} \lambda_i^t & t \lambda_i^{t-1} & \cdots & \binom{t}{m-1} \lambda_i^{t-m+1} \\ 0 & \lambda_i^t & \cdots & \binom{t}{m-2} \lambda_i^{t-m+2} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_i^t \end{bmatrix}.\) Each row of \(\Lambda_i^t\) contains zeros to the left of the diagonal, and the first terms in the expansion of \((\lambda_i + 1)^t\) on and to the right of the diagonal.
Using (5)–(8), we can summarize what is known about the stability properties of (1) in two theorems.
### THEOREM 6.3
Let \(a_0\) be an \(n\)-vector and let \(A\) be an \(n \times n\) matrix.
Suppose the matrix \(I - A\) is nonsingular, and let \(x = (I - A)^{-1} a_0\).
Then \(\lim_{t \to \infty} x_t = x\) for every sequence \(\{x_t\}\) satisfying (1), if and only if the characteristic roots of \(A\) are all less than one in absolute value.
**Proof.** Let \(B\) be a nonsingular matrix and \(\Lambda\) a Jordan matrix satisfying (3).
Let \(\{x_t\}\) be any sequence satisfying (1), and let \(\{w_t\}\) be defined by (5).
Clearly \(x_t \to x\) if and only if \(w_t \to 0\).
It is immediate from (6)–(8) that \(w_t \to 0\) if the characteristic roots of \(A\) — the diagonal elements of \(\Lambda\) — are all less than one in absolute value.
It is also evident that this condition is necessary if the convergence is to take place for every choice of \(w_0\), and hence for every \(x_0\). \(\square\) In addition, (5) and (6) give us the solution for \(x_t\) in a usable form: (9) \(x_t = x + B \Lambda^t B^{-1} (x_0 - x).\) If some of the characteristic roots of \(A\) have absolute value greater than or equal to one, (9) still holds, of course, and whether or not a particular sequence \(\{x_t\}\) converges to \(x\) depends on the initial value \(x_0\).
However, the set of \(x_0\) values for which (1) is stable can be characterized very sharply in terms of the matrices \(A\) and \(B\).
### THEOREM 6.4
Let \(a_0\) be an \(n\)-vector and let \(A\) be an \(n \times n\) matrix.
Suppose the matrix \(I - A\) is nonsingular, and let \(x = (I - A)^{-1} a_0\).
Let \(B\) be a nonsingular matrix and \(\Lambda\) a Jordan matrix satisfying (3), and suppose that the first \(m\) diagonal elements of \(\Lambda\) are less than one in absolute value, and the last \(n - m\) are equal to or greater than one.
Let \(\{x_t\}\) be a sequence satisfying (1).
Then \(\lim_{t \to \infty} x_t = x\) if and only if \(x_0\) satisfies (10) \(x_0 = x + B w_0, \quad \text{where } w_{0t} = 0, \quad t = m+1, \dots, n.\)
**Proof.** Let \(m\) be the number of characteristic roots of \(A\), including repetitions, that are less than one in absolute value.
Then the matrices \(B\) and \(\Lambda\) in (3) can be chosen so that the first \(m\) diagonal elements of \(\Lambda\) are less than one in absolute value, and the last \(n - m\) are equal to or greater than one.
(In general, both groups contain repeated roots.) Let \(\{x_t\}\) be any sequence satisfying (1), and let \(\{w_t\}\) be defined by (5).
Clearly \(x_t \to x\) if and only if \(w_t \to 0\).
It is immediate from (6)–(8) that \(\lim_{t \to \infty} w_t = 0\) if and only if the last \(n - m\) coordinates of \(w_0\) are all zero.
It then follows from (5) that the initial values \(x_0\) that are consistent with stability are those that satisfy (10). \(\square\) Note that the initial values \(x_0\) for which the system is stable — that is, satisfying (10) — form an \(m\)-dimensional subspace of \(\mathbb{R}^n\); this subspace is called the stable manifold of (1).
Note, too, that for initial values in this subspace, it is clear from (7)–(9) that the speed of convergence to the stationary point \(x\) is determined by the value of the largest characteristic root that is less than one in absolute value.
Theorems 6.3 and 6.4 both have counterparts as local results for nonlinear systems, and it is these counterparts that have the widest applicability in economics.
Let \(X \subset \mathbb{R}^n\), let \(h: X \to X\), and consider the difference equation (11) \(x_{t+1} = h(x_t), \quad t = 0, 1, \dots.\) Let \(\bar{x}\) be a stationary point of \(h\).
The general idea is to find a linearapproximation to A at x* and hope that, if x0 is sufficiently close to x, the solution to the linear system is a good approximation to the solution to (11).
Common sense suggests that this idea will work for stable systems, since for these, if x0 is close to x, then so are all the terms in the sequence {x}.
Hence the approximation remains good as t → ∞.
Here we simply state the main results, the counterparts to Theorems 6.3 and 6.4, respectively.
(See Scheinkman (1973) for a full treatment.)
### THEOREM 6.5
Let X be a stationary point of (11) and suppose that h is continuously differentiable in a neighborhood N of X.
Let A = [h(x*)] be the n × n (Jacobian) matrix of first derivatives of h = (h',..., h"), evaluated at x, and assume that I — A is nonsingular.
Then if the n characteristic roots of A are all less than one in absolute value, there is a neighborhood U ⊂ N such that if {x} is a solution to (11) with x0 ∈ U, then lim xt = X.
### THEOREM 6.6
Let the hypotheses of Theorem 6.5 hold, but assume that A has m roots that are less than one in absolute value and n — m roots that are equal to or greater than one.
Then there is a neighborhood U ⊂ N, and a continuously differentiable function φ: U → Rⁿ⁻ᵐ for which the matrix [∂φi(X)] has rank n — m, such that if {x} is a solution to (11) with x0 ∈ U and φ(x0) = 0, then lim xt = X.
Like its counterpart in the linear case, the set of x values satisfying φ(x) = 0 is called the stable manifold of the system (11).
Since φ(x) = 0 is a system of n — m equations in n unknowns, one may think of solving it for the last n — m coordinates (Xm+1, ... , Xn), given values (x1, ... , Xm) for the first m coordinates.
Constructing a solution in this fashion is possible if (and only if) the (n — m) × (n — m) matrix ∂φ1/∂Xm+1  ...  ∂φ1/∂Xn ...       ...  ... ∂φn-m/∂Xm+1 ... ∂φn-m/∂Xn is nonsingular. 6.4 Euler Equations To apply the stability theory of the last section to the problem of characterizing solutions to dynamic programs, it would seem natural to use a linear approximation to the optimal policy function g.
But, in general, we do not have enough information to do this.
In particular, we do not typically know that g is differentiable.
The strategy that does work is to use instead a linear approximation to the Euler equations.
Let (X, Π, A, F, B) satisfy Assumptions 4.3–4.4 and 4.7–4.9.
Recall from Theorem 4.15 that sufficient conditions for an interior solution to the problem (SP) are then the Euler equations and transversality condition: (1a) 0 = Fy(xt, xt+1) + βFx(xt+1, xt+2), t=0,1,2,..., (1b) 0 = lim β^t Fx(xt, xt+1) · xt. t→∞ Moreover, under these assumptions, the optimal solution is unique.
Thus, our study of local stability in this section involves establishing additional conditions on F and B under which the following holds.
Condition 6.1 There exists a point x* ∈ X and a neighborhood U of x*, such that for every x0 ∈ U, there exists a sequence {x}₀^∞ satisfying (1a) and with xt → x*.
Since convergence to X clearly implies (1b), any such sequence is the unique optimal solution starting from x0.
To pursue this strategy, we will consider first the case when F is quadratic, so that the Euler equations are linear and Theorem 6.4 can be applied.
Results for this case are summarized in Theorem 6.8, which gives sufficient conditions for the global stability of linear–quadratic systems.
Then we will examine how Theorem 6.6 can be applied to a much wider class of return functions.
Results for this more general case are summarized in Theorem 6.9, which gives sufficient conditions for the local stability, in the neighborhood of a stationary point, of a nonlinear system.
If F is quadratic, its first derivatives are linear; hence they can be written in the form F(x, y) = Fy + Fxx + Fxy y, and F(x, y) = Fy + Fyx + Fyy y, where the l-vectors Fy, Fx and the 1 × l matrices Fxx, Fxy (= Fyx), Fyy are all constants.
In this notation, the Euler equations (1a) are (2) 0 = Fx + βFx + Fxx xt + (Fxy + βFxx)xt+1 + βFxy xt+2.
Assume that the matrix (Fxx + Fxx + βFxx + βFxx) is nonsingular, so that (2) has a unique stationary point, x* = -(Fxx + Fxx + βFxx + βFxx)^{-1} (Fx + βFx), and let zt = xt — x*.
Assume, too, that Fyy is nonsingular.
(These assumptions may not be easy to verify in particular applications.) Then (2) can be written (3) 0 = βFxy zt+2 + (Fxy + βFxx)zt+1 + (Fxx + βFxx)zt.
Equation (3) is a second-order linear system in zt, and we have a theory of first-order linear systems.
It is convenient, therefore, to define Zt to be the “stacked” vector with Zt' = (zt+1, zt) ∈ R²ˡ, and to write (3) as Zt+1 = [ 0   I ] Zt = A Zt, -K -J where A is a 2l × 2l matrix, where J = -β^{-1} Fyy^{-1} (Fxy + βFxx), K = -β^{-1} Fyy^{-1} Fxy, T and 0 are l × l matrices.
Exercise 6.5 Show that if Fyy and (Fxx + Fxx + βFxx + βFxx) are nonsingular, then A and (J — A) are also nonsingular.
Everything hinges, then, on the 2l characteristic roots of the matrix A.
They are characterized in the following lemma.
### LEMMA 6.7
Assume that Fyy and (Fxx + Fxx + βFxx + βFxx) are nonsingular, and let the matrix A be as defined in (4).
Then, if λ is a characteristic root of A, so is (βλ)^{-1}.
**Proof.** If λ is a root of A, then the matrix A — λI is singular.
That is, for some stacked vector x ≠ 0, with x' = (x1, x0) ∈ R²ˡ [ -λI    I ] [x1] = [0] [ -K  -J-λI ] [x0]   [0] Hence, x1 and x0 must satisfy -λx1 + x0 = 0 and -Kx1 - Jx0 = λx0.
Since A is nonsingular, the root λ cannot be 0.
Since x ≠ 0, the second of these equations then implies that x1 ≠ 0 and x0 ≠ 0.
Then substituting from the first equation into the second, we find that (K + λJ - λ² I) x0 = 0.
Since x0 ≠ 0, this implies that λ is a characteristic root of A if and only if K + λJ - λ² I is singular, or 0 = det(K + λJ - λ² I) = det[-β^{-1} Fyy^{-1} Fxy - λβ^{-1} Fyy^{-1} (Fxy + βFxx) - λ² I].
Since Fyy is nonsingular, this is equivalent to (5) 0 = det[βFxy + λ(Fxy + βFxx) + λ² Fyy].
Summing up the argument to this point, we have shown that λ is a characteristic root of A if and only if (5) holds.
Now suppose λ satisfies (5); then it is sufficient to show that (5) also holds for λ = (βλ)^{-1}.
Substituting λ = (βλ)^{-1} into (5), we obtain det[βFxy + (βλ)^{-1} (Fxy + βFxx) + (βλ)^{-2} Fyy] = det[βFxy + λ^{-1} β^{-1} (Fxy + βFxx) + λ^{-2} β^{-2} Fyy] = (βλ)^{-2} det[β^3 λ^2 Fxy + β^2 λ (Fxy + βFxx) + β Fyy].
Since Fyy + βFxx is symmetric, the matrix in brackets is just the transpose of the one in (5).
Hence its determinant is zero if and only if (5) holds. □ Thus the 2l roots of A come in almost-reciprocal pairs: if λi is a root, so is (βλi)^{-1}.
This fact implies that l roots are greater than or equal to β^{-1/2} > 1 in absolute value, and l are smaller.
That is, no more than l roots are smaller than one in absolute value.
The following theorem shows that if exactly l roots are smaller, then the linear–quadratic model is globally stable.
### THEOREM 6.8
Let F: R²ˡ → R be a strictly concave, quadratic function; let T(x) = R all x ∈ R and let 0 < β < 1.
Assume that the matrices (Fxx + Fxx + βFxx + βFxx) and Fyy are nonsingular, and let X be the unique stationary point.
Assume that the matrix A defined in (4) has l characteristic roots less than one in absolute value.
Then for every x0 ∈ Rˡ, there exists a unique solution {x} to the problem (SP).
This sequence satisfies (2) and has lim xt = X.
**Proof.** Fix x0.
Then any sequence satisfying (2) and (1b) is a solution to (SP).
Since F is strictly concave, there is at most one such sequence.
Hence it suffices to establish existence.
Let B be a nonsingular matrix and Λ a Jordan matrix, each composed of l × l blocks, such that B^{-1}AB = A = [ Λ   0 ] [ 0   Bs ] where Λ has diagonal elements less than one in absolute value.
First we will show that given (x1, x0) ∈ R²ˡ the unique sequence {x} satisfying (2) has xt → X if and only if (7) Bo1(x1 — x*) + Boo(x0 — x*) = 0.
Then we will show that for any x0 ∈ Rˡ, there exists a value x1 satisfying this restriction.Exercise 6.7 f.
Verify that for the parameter values given above, (0.29, 0.18) is an optimal two-cycle. g.
Determine the local stability of the two-cycle (0.29, 0.18). [Hint.
Use the Euler equation to define the “stacked” system K_{t+2} = H(K_t, H(K_t)) where H is even.
Take a linear approximation to this system around the stationary point K = (0.29, 0.18), and determine whether one of the characteristic roots is less than one in absolute value.] A Firm with Adjustment Costs Consider the dynamics of capital accumulation for the firm with convex adjustment costs introduced in Section 5.9.
There is one capital good, k, and f (k) is the firm’s net operating profit (sales less payments for labor and materials) when its capital stock is k.
Assume that f is strictly increasing, strictly concave, and twice continuously differentiable, with f(0) = 0, lim_{k→∞} f(k) = +∞, and lim_{k→∞} f'(k) = 0.
Capital depreciates at the constant rate δ ∈ (0, 1) per period, and in any period the total cost of investment is a function c of the level of gross investment.
That is, c[K_{t+1} − (1 − δ)K_t] is the total cost of investment if this period’s capital is K_t and next period’s is K_{t+1}.
Assume that c is strictly increasing, strictly convex, and twice continuously differentiable, with c(0) = 0.
The firm’s objective is to maximize the sum of net receipts, discounted at the constant rate β; so its functional equation is V(K_t) = max_{K_{t+1}} {f(K_t) − c[K_{t+1} − (1 − δ)K_t] + βV(K_{t+1})}.
Exercise 6.8 a.
Characterize the stationary capital stock(s) k for this firm. b.
Use the method of Section 6.1 to study the global stability of k. c.
Use the method of Section 6.4 to study the local stability of k.
A Constant-Returns-to-Scale Industry Consider a publicly owned firm whose output q in period t depends on its beginning-of-period capital stock x_t, and its end-of-period capital stock x_{t+1}.
In particular, suppose that its technology is homogeneous of degree one: q_t = x_t φ(x_{t+1}/x_t).
Assume that φ: [0, a] → R, for some 1 < a < ∞, and that φ is strictly decreasing, strictly concave, and twice continuously differentiable, with φ(0) > 0, φ(a) = 0, lim_{u→∞} φ'(u) = −∞.
Assume that capital depreciates at the constant rate δ ∈ (0, 1) per period and that in any period new capital goods can be purchased at the constant price θ > 0.
Let S(q) be a measure of the benefits that accrue to society if the firm produces the quantity q.
Assume that S: R+ → R, is bounded, strictly increasing, strictly concave, and twice continuously differentiable.
Assume that society discounts benefits by the constant factor β ∈ (0, 1) per period.
Consider the problem of maximizing net consumer surplus: max_{x_1, x_2, ...} Σ_{t=0}^∞ β^t [S(x_t φ(x_{t+1}/x_t)) − θ(x_{t+1} − (1 − δ)x_t)].
The functional equation for this problem can be written as V(x) = max_{y} {S[x φ(y/x)] − θ(y − (1 − δ)x) + βV(y)}.
Exercise 6.9 a.
Prove that the functional equation has a unique continuous bounded solution V; that V is strictly increasing and strictly concave; that the optimal policy function g is continuous and singlevalued; and that V is once differentiable, with V'(x) = S'[x φ(g(x)/x)][φ(g(x)/x) − (g(x)/x) φ'(g(x)/x)] + θ(1 − δ), where λ = g(x)/x. b.
Use the envelope condition above to prove that g is increasing. c.
Write the Euler equation, and prove that there is a unique, positive stationary point x* > 0. d.
Prove that the Euler equation is locally stable in a neighborhood of x*. e.
Use (b)–(d) to prove that if x_0 > 0, the solution to x_{t+1} = g(x_t) converges monotonically to x*.
(In Section 16.4 we show that a solution to this problem is also a rational expectations or perfect foresight equilibrium for an industry with many firms, each with the constant returns technology above, and for which S is the integral under the market demand curve.) A Consumer with Recursive Preferences Consider a specialization of the consumer of Section 5.12, whose preferences over sequences of a single consumption good are given implicitly by an aggregator function W: R+ × R → R.
He has wealth x, which he divides into savings y ∈ [0, x] and current consumption, x − y.
There is a fixed interest factor R = 1/(1 + r); so if he saves y, his wealth next period is Ry.
His functional equation is therefore V(x) = max_{0 ≤ y ≤ x} W[x − y, V(Ry)].
Maintain the assumptions of Section 5.11, so that the value function V has the properties derived in Exercise 5.12, and so that there is a unique optimal savings policy y = g(x).
This question is concerned with characterizing g and the wealth sequence {x_t} defined by x_{t+1} = R^{-1}g(x_t).
A useful general strategy is to begin by seeking restrictions on W that guarantee uniqueness of a stationary point.
Sufficient conditions for this are often sufficient for local and even global stability as well.
If x is a stationary wealth level, then clearly x = R^{-1}g(x) and the associated consumption is x − g(x) = x(1 − R).
Exercise 6.10 a.
Show that x* is a stationary wealth level if and only if for some Z ∈ R, (x*, Z) satisfy the two equations R = W_z[x*(1 − R), Z] and Z = W[x*(1 − R), Z]. b.
Provide sufficient conditions on W to guarantee existence and uniqueness of a solution (x*, Z) to this pair of equations. c.
What can be said about stationary points if W is additively separable, that is, if W(x, v) = U(x) + βv?
Characterize all optimal wealth sequences under this assumption. d.
Derive the Euler equation for the consumer whose preferences are not additively separable. e.
Provide sufficient conditions on W to guarantee that a stationary solution, if it exists, is locally stable. f.
Can you prove global stability under the same restrictions found in (e)? 6.6 Bibliographic Notes The stability proof for the one-sector growth model in Section 6.1 is due to Sangmoon Hahm.
Earlier proofs of the same result, in continuous time, can be found in Cass (1965) and Koopmans (1965).
Theorem 6.1 is from Boldrin and Montrucchio (1986).
See Boldrin and Montrucchio (1984) for a useful introduction to the literature on the possible pathologies of optimal growth paths.
Burmeister (1980, chap. 4) gives a useful discussion of sufficient conditions for the uniqueness of stationary points in models with many capital goods.
See also Brock (1973) and Brock and Burmeister (1976).
The term value loss, as applied in Section 6.2, dates from Radner (1961).
McKenzie (1987) provides an invaluable survey of the stability theory for both undiscounted and discounted problems that stemmed from this work.
For global stability theory applied to the discounted problem, see especially Brock and Scheinkman (1976), Cass and Shell (1976), Rockafellar (1976), and Scheinkman (1976).
Kurz (1968) and Sutherland (1970) provided early counterexamples to any general global stability result for multisector growth models.
The basic source for the stability theory of both linear and nonlinear differential equation systems is Coddington and Levinson (1955).
Pontryagin (1962) is a very readable introduction to this topic.
For a rigorous adaptation of this theory to the study of autonomous difference equation systems, see Scheinkman (1973).
Our treatment in Section 6.3 draws heavily on this source.
Lemma 6.7 is due to Levhari and Liviatan (1972).
# PART III
Stochastic Models
## 7 Measure Theory and Integration
Most of the results in Chapter 4 carry over almost without change to situations in which the return function is subject to stochastic shocks and the objective is to maximize the expected value of discounted returns.
But to show that this is so, it is convenient to draw upon some of the terminology and results from modern probability theory and from the theory of Markov processes.
The required material is set out in this chapter and the next.
The following example illustrates the advantages of a modern approach.Consider the stochastic growth model described in Chapter 2.
Output f(x)z is determined by the size of the capital stock, x, and a stochastic technology shock, z, where the latter is assumed to be independently and identically distributed over time.
Hence the functional equation for optimal growth is (1) u(x, z) = max {U[f(x)z — y] + BE[u(y, z’)]}, 0≤y≤f(x)z where y is end-of-period capital and z’ is next period's shock, and z’ is unknown at the time y is chosen.
To study this equation we need to spell out what is meant by the expression E(-).
One way to do this is to assume that z takes on values in a finite or countably infinite set, z ∈ Z = {z₁, z₂,..., zₙ, . .} and that probabilities (π₁, π₂,..., πₙ,...) are assigned to these possibilities.
Since the πs are probabilities, we require that πᵢ ≥ 0, i=1,2,..., and Σᵢ₌₁∞ πᵢ = 1.
In this case (1) can be written as u(x, z) = max {U[f(x)z — y] + Σᵢ₌₁∞ πᵢ u(y, zᵢ)}. 0≤y≤f(x)z It is a simple exercise to extend the analysis of Chapter 4 to include equations like this one.
Alternatively, one might wish to carry out the study of (1) under the hypothesis that z takes on values in an interval, z ∈ Z = [a, b], and that probabilities are assigned to subsets by using a continuous density function π(z).
Then for any interval [c, d] ⊂ [a, b], for example, Pr{z ∈ [c, d]} = ∫_c^d π(z) dz, and the probability interpretation requires that π(z) ≥ 0, all z ∈ [a, b], and ∫_a^b π(z) dz = 1.
In this case (1) can be written as u(x, z) = max {U[f(x)z — y] + ∫_a^b u(y, z') π(z') dz'}. 0≤y≤f(x)z Again, the analysis of Chapter 4 can be extended to include functional equations like this one.
Both these formulations, discrete and continuous, arise in many economic applications, and it is an obvious—if unfortunate—fact that neither is a special case of the other.
In addition, it is easy to think of economic problems that mix discrete and continuous elements.
For example, in inventory problems the probability distribution over the stock is often described by a continuous density over strictly positive values, together with a positive probability on the value zero.
In this chapter we show that these discrete, continuous, and mixed cases—and more complicated possibilities as well—can all be treated in a unified way.
Our concern in the rest of this chapter is to develop a framework for dealing with probability measures on a state space, where an element in the state space may include a description of exogenous random shocks (like the technology shocks z in the growth example above), or a description of endogenous state variables (like the capital stock x above), or both.
At this point, though, we do not need to distinguish among these cases: we simply denote the state space by S and note that, to develop the mathematical tools we need, the elements in the set S can be anything.
In later chapters the state spaces we deal with are often finite or countably infinite sets, like the set Z = {z₁, z₂, .. .} in the first example above, or uncountable subsets of ℝᵇ like the interval [a, b] in the second example.
The approach to be developed here, which is based on measure theory, applies much more broadly, however; and no gain in simplicity would result if we were to restrict discussion to these particular cases.
Accordingly, the next sections develop, at a general level and in a self-contained way, as much of the theory of measure and integration as is needed to streamline later discussions.
It is not a complete treatment of the subject, as this would lead us too far afield.
(Many excellent texts are available; for example, see Bartle 1966 or Royden 1968.) But before proceeding, in the remainder of this section we outline the main concepts in the context of a discrete state space.
If the state space is finite or countably infinite, S = {s₁, s₂, . . .}, a probability distribution is an assignment of numbers (π₁, π₂, . . .) to the points (s₁, s₂, . . .), with πᵢ ≥ 0, all i, and Σᵢπᵢ = 1.
The interpretation is that πᵢ is the probability that sᵢ occurs, πᵢ = Pr{s = sᵢ}.
Such an assignment of probabilities to the elements of S leads to a natural assignment of probabilities to subsets of S.
For any set A ⊂ S, let I_A = {i: sᵢ ∈ A} be the set of indices of elements in A.
Then define the function μ by μ(A) = Σᵢ∈I_A πᵢ = Pr{s ∈ A}, each A ⊂ S.
The function μ is an example of a measure.
Note that the domain of μ is a family of subsets and that this family includes the empty set ∅ and the set S itself.
Note, too, that μ has the following properties: μ(A) ≥ 0, all A ⊂ S; μ(∅) = 0; μ(S) = 1; and for any collection A₁, A₂, . . . of pairwise disjoint subsets, μ(∪ᵢAᵢ) = Σᵢμ(Aᵢ).
Finally, note that for any real-valued function f on S, the expected value of f (with respect to the probability measure μ) is E(f) = Σᵢ f(sᵢ)μ({sᵢ}).
If the set S is uncountable—for example, if S is an interval—it is not possible to define a function (measure) on the class of all subsets of S that has the obvious adding-up property for unions of disjoint sets: something must be dropped.
It is more important to maintain the adding-up property, and hence we must limit the assignment of probabilities to a smaller family of subsets.
The rest of this chapter is organized as follows.
Section 7.1 deals with the issue of what families are suitable to serve as the domain of a measure, a discussion that leads to the definition of a measurable space.
Measures, including probability measures as a special case, are defined in Section 7.2, and we will see that certain measures capture the notions of length in ℝ¹, area in ℝ², and so forth.
(Clearly these are not probability measures, since they do not assign the value one to the whole space.) We will also see that any measure defined on an appropriate small class of sets can be extended to a useful large class.
The next two sections deal with defining the expected value operator E(:).
In the example above, E(f) can be defined for any real-valued function f.
But if S is an uncountable set, expected values cannot be defined for arbitrary functions.
A suitable class of functions—measurable functions—is introduced in Section 7.3, and in Section 7.4 we develop the theory of integration, of which expectation operators are a special case.
Section 7.5 deals with product spaces; Section 7.6 contains a proof of the Monotone Class Lemma; and Section 7.7 deals with conditional expectation.
For the reader who is anxious to get on with the analysis of stochastic functional equations, only Sections 7.1—7.4 and the first part of Section 7.5 are needed.
With that material in hand, the reader can, with no loss in continuity, proceed directly to Chapter 8 and beyond. 7.1 Measurable Spaces Given a set S, we may ask: On what collection 𝓕 of subsets of S are measures, including probability measures, to be defined?
To deal with this question, it is useful to have a terminology for discussing certain families of subsets.
We define first a sigma-algebra (σ-algebra) of sets.
### DEFINITION L
et S be a set and let 𝓕 be a family of subsets of S. 𝓕 is called a σ-algebra if a.
S ∈ 𝓕; b.
A ∈ 𝓕 implies Aᶜ = S\A ∈ 𝓕; and c.
Aₙ ∈ 𝓕, n = 1,2,..., implies ∪ₙ=1^∞ Aₙ ∈ 𝓕.
Thus, a σ-algebra is closed under complementation and countable union. [Since ∩ₙ=1^∞ Aₙ = (∪ₙ=1^∞ Aₙᶜ)ᶜ, it is also closed under countable intersection.] A pair (S, 𝓕) where S is a set and 𝓕 is a σ-algebra of its subsets is called a measurable space.
Any set A ∈ 𝓕 is called an 𝓕-measurable set, or—if 𝓕 is understood— simply a measurable set.
For a trivial example of a measurable space, let S be any set and let 𝓕 consist of the two sets S and ∅.
At the opposite extreme, let S be any set and let 𝓕 be the collection of all subsets of S.
This σ-algebra is routinelyused if \(S\) is a finite or countable set, as it was in the first example in the introduction.
If \(S\) is an uncountable set, like the interval \([a, b]\) in the continuous example in the introduction, the collection of all subsets of \(S\) is still a well-defined \(\sigma\)-algebra.
However, a look ahead to our ultimate goal shows that it is not possible to let \(\mathcal{F}\) be the set of all subsets and then to define, in an internally consistent way, measures that capture our ideas of probability, length, area, and so on.
The \(\sigma\)-algebra of all subsets is too big a class to be useful when \(S\) is uncountable.
For these cases, however, it is possible to build up a useful class \(\mathcal{F}\) starting from sets that we obviously want to be able to deal with.
To do this, note that for any set \(S\) and any collection \(\mathcal{A}\) of subsets of \(S\), we can consider the \(\sigma\)-algebras containing \(\mathcal{A}\).
There is at least one: the family of all subsets of \(S\).
Moreover, as the following exercise shows, the intersection of all the \(\sigma\)-algebras containing \(\mathcal{A}\) is itself a \(\sigma\)-algebra containing \(\mathcal{A}\).
It is the smallest one, and it is called the \(\sigma\)-algebra generated by \(\mathcal{A}\). **Exercise 7.1** Prove that for any set \(S\) and any collection \(\mathcal{A}\) of its subsets, the intersection of all the \(\sigma\)-algebras containing \(\mathcal{A}\) is a \(\sigma\)-algebra containing \(\mathcal{A}\).
An important example of a \(\sigma\)-algebra generated in this way is the following one for \(\mathbb{R}^1\).
Let \(\mathcal{A}\) be the collection of all open intervals, that is, all sets of the form \((-\infty, b)\), \((a, b)\), \((a, +\infty)\), and \((-\infty, +\infty)\).
Note that every \(\sigma\)-algebra containing \(\mathcal{A}\) must also contain all of the closed intervals.
(Why?) The smallest \(\sigma\)-algebra containing all of the open sets is a class that is used in many applications.
It is called the Borel algebra for \(\mathbb{R}^1\) and is denoted by \(\mathcal{B}^1\); any set in \(\mathcal{B}^1\) is called a Borel set. **Exercise 7.2** Show that \(\mathcal{B}^1\) is also the \(\sigma\)-algebra generated by all the closed intervals; or by all the half-open intervals \((a, b]\); or by all the half-rays \((a, +\infty) = \{x \in \mathbb{R}: x > a\}\).
For higher dimensional Euclidean spaces or for any other metric space \((S, \rho)\), the Borel algebra is defined in an analogous way: it is always the smallest \(\sigma\)-algebra containing the open balls, that is, containing all sets of the form \(A = \{s \in S: \rho(s, s_0) < \delta\}\), where \(s_0 \in S\) and \(\delta > 0\).
For \(S = \mathbb{R}^n\) with the Euclidean metric, the Borel algebra is denoted by \(\mathcal{B}^n\).
One can show that \(\mathcal{B}^n\) is also the \(\sigma\)-algebra generated by the open rectangles, sets of the form \(A = \{x \in \mathbb{R}^n: x_i \in (a_i, b_i), i = 1, \ldots, n\}\); or (as it was in Exercise 7.2) by the closed or half-open rectangles.
We often want to take \(S\) to be a Borel set in a Euclidean space, like the interval \([a, b] \subset \mathbb{R}^1\) in the continuous example in the introduction.
In these cases we want to let \(\mathcal{F}\) be the appropriate restriction of the Borel sets.
Thus, for any Borel set \(S\) in \(\mathbb{R}^n\) we define \(\mathcal{B}_S = \{A \in \mathcal{B}^n: A \subset S\}\) to be the Borel sets that are subsets of \(S\). **Exercise 7.3** Show that if \(S \in \mathcal{B}^n\) then \(\mathcal{B}_S\) is a \(\sigma\)-algebra. ## 7.2 Measures Given a measurable space \((S, \mathcal{F})\), we consider next the problem of assigning values with the interpretation of size or probability—in a consistent way—to all of the sets in \(\mathcal{F}\).
The definition of a measure spells out what we mean by consistency. **DEFINITION** Let \((S, \mathcal{F})\) be a measurable space.
A measure is an extended real-valued function \(\mu: \mathcal{F} \to \overline{\mathbb{R}}\) such that a. \(\mu(\emptyset) = 0\); b. \(\mu(A) \geq 0\), all \(A \in \mathcal{F}\); c. if \(\{A_n\}_{i=1}^{\infty}\) is a countable, disjoint sequence of subsets in \(\mathcal{F}\), then \(\mu\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} \mu(A_i)\).
Thus a measure is nonnegative, assigns zero to the null set, and is countably additive.
If \(\mu(S) < \infty\), then \(\mu\) is finite. 7.2 Measures 171 **DEFINITION** A measure space is a triple \((S, \mathcal{F}, \mu)\), where \(S\) is a set, \(\mathcal{F}\) is a \(\sigma\)-algebra of its subsets, and \(\mu\) is a measure defined on \(\mathcal{F}\).
Given a measure space \((S, \mathcal{F}, \mu)\), we say that a proposition holds \(\mu\)-almost everywhere (\(\mu\)-a.e.) if there exists a set \(A \in \mathcal{F}\) with \(\mu(A) = 0\) such that the proposition holds on the complement of \(A\).
If the measure \(\mu\) is understood, then we say simply that the proposition holds almost everywhere (a.e.).
For example, given a measure space \((S, \mathcal{F}, \mu)\), two functions \(f\) and \(g\) on \(S\) are equal almost everywhere (\(f = g\), a.e.) if \(f(s) = g(s)\) for \(s \in S \setminus A\), where \(A \in \mathcal{F}\) and \(\mu(A) = 0\).
Or, a sequence \(\{f_n\}\) of functions on \(S\) converges a.e. to a function \(f\) if there exists \(A \in \mathcal{F}\) with \(\mu(A) = 0\) such that \(\lim_{n \to \infty} f_n(s) = f(s)\), all \(s \in S \setminus A\).
If \(\mu(S) = 1\), then \(\mu\) is a probability measure and \((S, \mathcal{F}, \mu)\) is called a probability space.
In this case any measurable set \(A \in \mathcal{F}\) is called an event, and \(\mu(A)\) is called the probability of the event \(A\).
For a probability space, the phrase almost surely (a.s.) is used interchangeably with almost everywhere.
One example of a probability space is provided in the introduction.
There, \(S = \{s_1, s_2, \ldots\}\) is a finite or countable set; \(\mathcal{F}\) is the \(\sigma\)-algebra consisting of all its subsets; and \(\mu\) is defined by using the probabilities \(\pi_1, \pi_2, \ldots\) of the individual elements of \(S\).
Hence \((S, \mathcal{F}, \mu)\) is a probability space.
Does the second example in the introduction provide another?
For the set \(S = [a, b]\), we would like to take the \(\sigma\)-algebra to be the Borel subsets of \(S\), \(\mathcal{F} = \mathcal{B}_S\).
For open, half-open, and closed intervals, we can take the measure \(L\) to be given by \[ L((a, b]) = L((a, b)) = L([a, b)) = L([a, b]) = \int_a^b \tau(s) \, ds, \] where \(\tau\) satisfies \(\int_a^b \tau(s) \, ds = 1\).
Clearly \(L\) is well defined for these sets.
Moreover, it is clear that we can then extend the definition of \(L\) (in (1)) to complements and to finite unions and intersections of intervals.
However, we have no way—yet—of being sure that this measure can be extended in a consistent way to all of the Borel subsets of \([a, b]\).
We will return to this example later.
The next exercise demonstrates two useful ways to construct measures.
The following one develops an important property of measures. **Exercise 7.4** Let \((S, \mathcal{F})\) be a measurable space; let \(\lambda\) and \(\nu\) be measures on it. a.
Show that \(\Lambda: \mathcal{F} \to \mathbb{R}\), defined by \(\Lambda(A) = \lambda(A) + \nu(A)\), is a measure on \((S, \mathcal{F})\). b.
Let \(B \in \mathcal{F}\).
Show that \(\Lambda: \mathcal{F} \to \mathbb{R}\) defined by \(\Lambda(A) = \lambda(A \cap B)\) is a measure on \((S, \mathcal{F})\). **Exercise 7.5** Let \((S, \mathcal{F}, \mu)\) be a measure space, with \(A, B \in \mathcal{F}\).
Show that if \(A \subset B\), then \(\mu(A) \leq \mu(B)\), and if in addition \(\mu(A) < \infty\), then \(\mu(B \setminus A) = \mu(B) - \mu(A)\).
The next theorem provides a result that will be used later in establishing a basic property of integrals; it is also a good illustration of the implications of countable additivity. **THEOREM 7.1** Let \((S, \mathcal{F}, \mu)\) be a measure space. a.
If \(\{A_n\}_{n=1}^{\infty}\) is an increasing sequence in \(\mathcal{F}\), that is, if \(A_n \subset A_{n+1}\), all \(n\), then \(\mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \lim_{n \to \infty} \mu(A_n)\). b.
If \(\{B_n\}_{n=1}^{\infty}\) is a decreasing sequence in \(\mathcal{F}\), that is, if \(B_{n+1} \subset B_n\), all \(n\), and if \(\mu(B_m) < \infty\) for some \(m\), then \(\mu\left(\bigcap_{n=1}^{\infty} B_n\right) = \lim_{n \to \infty} \mu(B_n)\). **Proof.** a.
If \(\mu(A_n) = \infty\) for any \(n\), then the result is trivial.
Suppose \(\mu(A_n) < \infty\), all \(n\).
Let \(A_0 = \emptyset\).
Then \(\{A_n \setminus A_{n-1}\}\) is a sequence of disjoint sets in \(\mathcal{F}\), and \(\bigcup_{i=1}^{\infty} A_i = \bigcup_{i=1}^{\infty} (A_i \setminus A_{i-1})\).
Then using the result of Exercise 7.5, we find that \[ \mu\left( \bigcup_{n=1}^{\infty} A_n \right) = \mu\left( \bigcup_{i=1}^{\infty} (A_i \setminus A_{i-1}) \right) = \sum_{i=1}^{\infty} \mu(A_i \setminus A_{i-1}) \\ = \lim_{N \to \infty} \sum_{i=1}^{N} \mu(A_i \setminus A_{i-1}) \\ = \lim_{N \to \infty} \sum_{i=1}^{N} [\mu(A_i) - \mu(A_{i-1})] = \lim_{N \to \infty} \mu(A_N), \] proving the first claim. 7.2 Measures 173 b.
Without loss of generality, assume that \(\mu(B_1) < \infty\).
Then it is sufficient to show that \[ \mu(B_1) - \mu\left( \bigcap_{n=1}^{\infty} B_n \right) = \mu(B_1) - \lim_{n \to \infty} \mu(B_n), \] or, with the result of Exercise 7.5 applied to each side, that \[ \mu\left( B_1 \setminus \bigcap_{n=1}^{\infty} B_n \right) = \lim_{n \to \infty} [\mu(B_1) - \mu(B_n)] = \lim_{n \to \infty} \mu(B_1 \setminus B_n). \] But \(\{B_1 \setminus B_n\}\) is an increasing sequence in \(\mathcal{F}\), and \(\bigcup_{n=1}^{\infty} (B_1 \setminus B_n) = B_1 \setminus \bigcap_{n=1}^{\infty} B_n\).
Therefore, applying the first result yields \[ \mu\left( \bigcup_{n=1}^{\infty} (B_1 \setminus B_n) \right) = \mu\left( B_1 \setminus \bigcap_{n=1}^{\infty} B_n \right) = \lim_{n \to \infty} \mu(B_1 \setminus B_n), \] as was to be shown. \(\square\) In (1) we used a density function \(\tau\) on an interval \([a, b]\) to define a measure on subintervals of \([a, b]\), but we did not establish that the domain of this measure could be extended to all the Borel subsets of \([a, b]\).
We can now return, but in a more abstract way, to the question of the extension of measures defined on a small family of sets to measures defined on an appropriate \(\sigma\)-algebra.
We first define a useful small family of sets, an algebra; then define a measure on such a family; and finallypresent an extension theorem.
### DEFINITION L
et \(S\) be a set, and let \(\mathcal{A}\) be a family of its subsets. \(\mathcal{A}\) is called an algebra if 1. \(S \in \mathcal{A}\); 2. \(A \in \mathcal{A}\) implies \(A^c = S \setminus A \in \mathcal{A}\); and 3. \(A_1, A_2, \ldots, A_n \in \mathcal{A}\) implies \(\bigcup_{i=1}^n A_i \in \mathcal{A}\).
Thus an algebra is closed under complementation and finite union.
Clearly, then, an algebra is in an important sense smaller than a \(\sigma\)-algebra.
Exercise 7.6 a.
Let \(S = \mathbb{R}\), and let \(\mathcal{A}\) be the family of all complements and finite unions of sets of the form \((-\infty, b)\), \((a, b)\), \((a, +\infty)\), \((-\infty, +\infty)\).
Show that \(\mathcal{A}\) is an algebra. [Hint.
Show that every set in \(\mathcal{A}\) can be written as the union of a finite number of disjoint, half-open intervals.] b.
Show that the Borel algebra is the smallest \(\sigma\)-algebra containing \(\mathcal{A}\).
The definition of a measure on an algebra is very close to the one for a \(\sigma\)-algebra, but there is one important difference.
### DEFINITION L
et \(S\) be a set, and let \(\mathcal{A}\) be an algebra of its subsets.
Then a measure on \(\mathcal{A}\) is a real-valued function \(\mu\) satisfying a. \(\mu(\emptyset) = 0\); b. \(\mu(A) \geq 0\), all \(A \in \mathcal{A}\); and c. if \(\{A_i\}\) is any disjoint sequence of sets in \(\mathcal{A}\) with \(\bigcup_{i=1}^\infty A_i \in \mathcal{A}\), then \(\mu(\bigcup_{i=1}^\infty A_i) = \sum_{i=1}^\infty \mu(A_i)\).
The crucial difference between this definition and the one for measures on \(\sigma\)-algebras is that the measure of a countable union of disjoint sets is defined for an algebra only if that countable union is contained in the algebra.
Clearly this restriction makes it easier to define a measure on an algebra—especially if the algebra has been chosen (with malice aforethought) to exclude awkward infinite unions.
Exercise 7.7 a.
Let \(S = \mathbb{R}\), and let \(\mathcal{A}\) be as defined in Exercise 7.6.
Show that length is a measure on \(\mathcal{A}\), where by length we mean the function \(\lambda\) defined by 1. \(\lambda(\emptyset) = 0\); 2. \(\lambda((a, b]) = b - a\); 3. \(\lambda((-\infty, b]) = \lambda((a, +\infty)) = \lambda((-\infty, +\infty)) = +\infty\) 4. \(\lambda(\bigcup_i (a_i, b_i]) = \sum_i (b_i - a_i)\) if the intervals are disjoint. b.
Let \(S = (a, b] \subset \mathbb{R}\), and let \(\mathcal{A}\) be the algebra of subsets of \(S\) consisting of all finite unions and complements of half-open intervals \((c, d]\), \(a < c < d \leq b\).
Show that (1) can be used to define a measure \(\lambda\) on \(\mathcal{A}\), and that \(\lambda(S) = 1\).
Defining measures on algebras rather than \(\sigma\)-algebras is clearly more convenient.
On the other hand, we generally find it most convenient to work with a \(\sigma\)-algebra.
The next two theorems show that we can have the best of both worlds.
### THEOREM 7.2
(Carathéodory Extension Theorem) Let \(S\) be a set, \(\mathcal{A}\) an algebra of its subsets, and \(\mu\) a measure on \(\mathcal{A}\).
Let \(\mathcal{F}\) be the smallest \(\sigma\)-algebra containing \(\mathcal{A}\).
Then there exists a measure \(\mu^*\) on \(\mathcal{F}\) such that \(\mu^*(A) = \mu(A)\), all \(A \in \mathcal{A}\).
This theorem leaves open the possibility that there may be more than one extension of \(\mu\) to all of \(\mathcal{F}\).
To rule out this possibility, we need the following definition.
### DEFINITION L
et \(S\) be a set, \(\mathcal{A}\) an algebra of subsets of \(S\), and \(\mu\) a measure on \(\mathcal{A}\).
If there is a countable sequence of sets \(\{A_i\}\) with \(\mu(A_i) < \infty\), all \(i\), and \(S = \bigcup_i A_i\), then \(\mu\) is \(\sigma\)-finite.
Clearly, any probability measure is \(\sigma\)-finite.
The next theorem shows that the extension of a \(\sigma\)-finite measure is unique.
### THEOREM 7.3
(Hahn Extension Theorem) Let \(S, \mathcal{A}, \mu\) and \(\mathcal{F}\) be as specified in Theorem 7.2.
If \(\mu\) is \(\sigma\)-finite, then the extension \(\mu^*\) to \(\mathcal{F}\) is unique.
We omit the proofs of Theorems 7.2 and 7.3; they are not particularly difficult, but they do require a substantial additional investment in terminology and are available in any standard text on measure theory.
Instead, we will focus on applications of the theorems.
Let \(\mathcal{A}\) be the algebra of subsets of \(\mathbb{R}\) defined in Exercise 7.6.
Let \(\lambda\) be the measure on \(\mathcal{A}\), namely, length, defined in Exercise 7.7a; and note that since \(\mathbb{R}\) is the union of a countable set of intervals of length one, this measure is \(\sigma\)-finite.
Hence by Theorems 7.2 and 7.3, \(\lambda\) has a unique extension to the smallest \(\sigma\)-algebra containing \(\mathcal{A}\), the Borel sets.
Thus length defines a unique measure on the Borel sets.
The argument is exactly analogous in higher dimensional Euclidean spaces.
In Section 7.1 we observed that the Borel sets in \(\mathbb{R}^n\) are generated by the half-open rectangles, that is, sets of the form \(\{x \in \mathbb{R}^n: a < x \leq b\}\), where \(a, b \in \mathbb{R}^n\) and \(a < b\).
Hence, if a measure can be defined on the algebra consisting of all complements and finite unions of these rectangles, it can be extended in a unique way to the Borel sets.
In this way, area can be defined on \(\mathbb{R}^2\), volume on \(\mathbb{R}^3\), and so on.
Theorems 7.2 and 7.3 can be used in exactly the same way to generate probability measures.
Let \(S, \mathcal{A}\), and \(\lambda\) be as given in Exercise 7.7b.
Then Theorems 7.2 and 7.3 imply that the measure \(\lambda\) on \(\mathcal{A}\) has a unique extension to the Borel subsets of \([a, b]\).
That is, (1) does indeed define a measure on the Borel sets of \([a, b]\).
In higher dimensional Euclidean spaces the argument is analogous: begin with the algebra \(\mathcal{A}\) consisting of complements and finite unions of half-open rectangles.
For any measure defined on \(\mathcal{A}\), for example by a density, there exists an extension to all of the Borel sets.
These are the basic facts about measures that will be used in the rest of this chapter and those that follow.
Before proceeding, however, it is useful to state one additional definition.
Given a measure space \((S, \mathcal{F}, \mu)\), one would think that if \(A \in \mathcal{F}\) has measure zero, then \(B \subset A\) would, too. \(B\) may not be in \(\mathcal{F}\), however, and hence \(\mu(B)\) may be undefined.
This gap is filled by the idea of the completion of a measure space.
Let \((S, \mathcal{F}, \mu)\) be a measure space.
Let \(A \in \mathcal{F}\) be any set with measure zero, and let \(C\) be any subset of \(A\).
Let \(\mathcal{C}\) be the family of all such sets.
That is, \[ \mathcal{C} = \{C \subset S: C \subset A \text{ for some } A \in \mathcal{F} \text{ with } \mu(A) = 0\}. \] Now consider starting with any set \(B \in \mathcal{F}\), and then adding and subtracting from it sets in \(\mathcal{C}\).
The completion of \(\mathcal{F}\) is the family \(\mathcal{F}'\) of sets constructed in this way.
That is, \[ \mathcal{F}' = \{B' \subset S: B' = (B \cup C_1) \setminus C_2, B \in \mathcal{F}, C_1, C_2 \in \mathcal{C}\}. \] That is, \(\mathcal{F}'\) consists of all the subsets of \(S\) that differ from a set in \(\mathcal{F}\) by a subset of a set of \(\mu\)-measure zero.
If \(\mathcal{F}'\) is the completion of \(\mathcal{F}\), a measure \(\mu\) on \((S, \mathcal{F})\) can be extended to \((S, \mathcal{F}')\) in the obvious way: let \(\mu'(B') = \mu(B)\) for any set \(B'\) in \(\mathcal{F}'\) that differs from \(B \in \mathcal{F}\) by a subset of a set in \(\mathcal{F}\) of measure zero.
Exercise 7.8 Let \((S, \mathcal{F}, \mu)\) be a measure space, and let \(\mathcal{F}'\) be the completion of \(\mathcal{F}\).
Show that \(\mathcal{F}'\) is a \(\sigma\)-algebra.
For any Euclidean space \(\mathbb{R}^n\), the completion of the Borel sets is a family called the Lebesgue measurable sets, and the extension to this family of the measure corresponding to length, area, and so on is called Lebesgue measure.
When restricted to the Borel sets it is called either Lebesgue measure or Borel measure.
We will use the latter term.
Both the Borel sets and the Lebesgue sets are commonly used in \(\mathbb{R}^n\), and when a set in \(\mathbb{R}^n\) 7.3 Measurable Functions 177 is referred to as measurable, without reference to a particular \(\sigma\)-algebra, either may be intended (or it may be that it does not matter which is used).
The Carathéodory Extension Theorem can in fact be proved for completions of measures.
### THEOREM 7.2
' (Carathéodory Extension Theorem) Let \(S\) be a set, \(\mathcal{A}\) an algebra of its subsets, and \(\mu\) a measure on \(\mathcal{A}\).
Let \(\mathcal{F}'\) be the completion of the smallest \(\sigma\)-algebra containing \(\mathcal{A}\).
Then there exists a measure \(\mu'\) on \(\mathcal{F}'\), such that \(\mu'(A) = \mu(A)\), all \(A \in \mathcal{A}\).
Note that the Hahn Extension Theorem still implies that if \(\mu\) is \(\sigma\)-finite, then \(\mu'\) is unique. 7.3 Measurable Functions In the two examples in the introduction, we were interested in defining probability measures on the state space \(S\) so that we could talk sensibly about expressions like \(E(f)\), the expected value of a real-valued function \(f\) defined on \(S\).
We need to ask, then, for which functions can expressions like \(E(f)\) be reasonably interpreted.
As with the assignment of measures to sets, the class of all functions \(f: S \to \mathbb{R}\) is too large to work with, but we want as large a class as we can usefully manipulate.
It is as follows.
### DEFINITION G
iven a measurable space \((S, \mathcal{F})\), a real-valued functionExercise 7.14 Let (S, 𝒮) be a measurable space, and let f: S → ℝ be an 𝒮-measurable function.
Show that the inverse image of every Borel set in ℝ is in 𝒮.
That is, f⁻¹(A) ∈ 𝒮 for all A ∈ ℬ.
(Hint.
First show that the inverse image of every open set in ℝ belongs to 𝒮.
Then show that the class of sets in ℝ whose inverse image belongs to 𝒮 is a σ-algebra.] The last exercise can be used to establish the very useful fact that compositions of Borel measurable functions are Borel measurable.
That is, if f: ℝ → ℝ and g: ℝ → ℝ are both Borel measurable, then the function h: ℝ → ℝ defined by h(x) = g[f(x)] is also Borel measurable.
To see this, recall that f is Borel measurable if (1) holds.
Thus it is sufficient to show that for any Borel set A, the inverse image h⁻¹(A) = f⁻¹[g⁻¹(A)] is a Borel set.
It follows immediately from Exercise 7.14 that this is so.
The same is not true if Lebesgue measure is used.
That is, if f and g are Lebesgue measurable functions, then h need not be Lebesgue measurable.
To see this, note that if f and g are Lebesgue measurable, then Exercise 7.14 implies that for any Borel set A, the inverse images f⁻¹(A) and g⁻¹(A) are Lebesgue sets.
Now let A = (—∞, a], and consider the inverse image h⁻¹(A) = f⁻¹[g⁻¹(A)].
The set B = g⁻¹(A) is a Lebesgue set but need not be a Borel set.
Thus f⁻¹(B) need not be a Lebesgue set, and h need not be Lebesgue measurable.
For this reason, we will always want to use the Borel sets rather than the Lebesgue sets as our σ-algebra when dealing with a Euclidean space.
Finally, we can extend the definition of measurability to functions from any measurable space into any other measurable space.
### DEFINITION L
et (S, 𝒮) and (T, 𝒯) be measurable spaces.
Then the function f: S → T is measurable if the inverse image of every measurable set is measurable, that is, if {s ∈ S: f(s) ∈ A} ∈ 𝒮 for all A ∈ 𝒯.
That is, f: S → T is measurable if the pre-image of each measurable set is measurable.
Thus, as Exercise 7.14 shows, our earlier definition was a specialization of this one in which (S, 𝒮) = (ℝ, ℬ).
An immediate consequence of this definition is that compositions of measurable functions are measurable.
That is, if (S, 𝒮), (T, 𝒯), and (U, 𝒰) are measurable spaces, and f: S → T and g: T → U are measurable functions, then h: S → U defined by h(s) = g(f(s)) is a measurable function.
(But, as shown above, if the spaces involved are Euclidean spaces, this conclusion must be interpreted carefully.) Exercise 7.15 Show that a function f: ℝ^m → ℝ^n, where f(x) = (f₁(x), ..., f_m(x)), is measurable if and only if each of the functions f_i: ℝ → ℝ, i = 1,...,m, is Borel-measurable.
Finally, the following definition and theorem are needed in Section 9.1, where the Principle of Optimality for stochastic systems is treated.
Although the theorem is very easy to state, the proof is quite difficult, and we omit it.
### DEFINITION L
et (S, 𝒮) and (T, 𝒯) be measurable spaces, and let T be a correspondence of S into T.
Then the function h: S → T is a measurable selection from T if h is measurable and h(s) ∈ T(s) for all s ∈ S.
### THEOREM 7.6
(Measurable Selection Theorem) Let S ⊂ ℝ and T ⊂ ℝ^n be Borel sets, with their Borel subsets 𝒮 and 𝒯.
Let T: S → T be a (nonempty) compact-valued and u.h.c. correspondence.
Then there exists a measurable selection from T.
(For a proof, see Hildenbrand 1974, Proposition 1 on p. 22 and Lemma 1 on p. 55.) 7.4 Integration We began this chapter by noting that the task of incorporating stochastic elements into our theory would be simplified if we had a unified way of dealing with the expected value E[v(y, z')] that appeared in the examples in the introduction.
We have seen how to define a probability space (Z, 𝒜, P) for the random shocks, and the reader has probably guessed, correctly, that the function v will be required to be 𝒜-measurable.
In this section we combine these two pieces—measure spaces and measurable functions—to develop the theory of integration.
The integral developed here (called the Lebesgue integral if we are dealing with Euclidean space and Lebesgue measure) is more general than the Riemann integral and includes it, as well as operations like Σ f(s_i) involving discrete probabilities, as special cases.
The difference between the two is illustrated by the following example.
Consider a function f: [a, b] → ℝ^+.
To compute the Riemann integral, we consider the sum Σ y_i (a_i - a_{i-1}), where a = a_0 ≤ a_1 = ... = a_n = b so that (a_i - a_{i-1}) is the length of the ith interval.
Suppose, in addition, that y_i ≤ f(x) for x ∈ [a_{i-1}, a_i], all i.
Then the sum above is the area under a step function that is less than f.
The supremum over all such step functions is called the lower Riemann integral.
Similarly, using y_i = f(x) for x ∈ [a_{i-1}, a_i], all i, gives a step function greater than f.
The infimum of the sum over all such step functions is the upper Riemann integral.
If the two coincide, the function f is called Riemann integrable, and the common value is the Riemann integral ∫_a^b f(x) dx.
The important point is that the approximations are made by taking successively finer grids on the x-axis, that is, by choosing a_i's that are closer together.
The Lebesgue integral of f on [a, b] is defined in terms of Σ y_i μ(A_i), where y_0 ≤ y_1 ≤ ... ≤ y_n, A_i = {x : y_{i-1} ≤ f(x) < y_i}, and μ(A_i) is the Lebesgue measure of the set A_i.
The Lebesgue integral is defined by taking y_i's that are closer together, that is, by taking successively finer grids on the y-axis.
Exercise 7.16 Let f: [0, 1] → [0, 1] be defined by f(x) = 1 if x is rational, 0 if x is irrational.
Show, by calculating the upper and lower Riemann integrals of f, that the Riemann integral does not exist.
Of course, the Lebesgue and Riemann integrals coincide when the latter exists.
The advantage of the Lebesgue integral is that it is defined for a broader class of functions and thus allows more limiting operations.
Moreover, Lebesgue’s theory of integration can be extended to real-valued functions on any measure space (S, 𝒮, μ).
For example, if μ is a probability measure, ∫_S f(s) μ(ds) is the expected value of the random variable f with respect to the distribution μ.
Throughout this section we take (S, 𝒮, μ) to be a fixed measure space, and measurable always means 𝒮-measurable.
Let M(S, 𝒮) be the space of measurable, extended real-valued functions on S, and let M^+(S, 𝒮) be the subset consisting of nonnegative functions.
Note, however, that simple functions take values in ℝ rather than ℝ̅.
We begin with the definition of the integral of a nonnegative, measurable, simple function.
### DEFINITION L
et φ ∈ M^+(S, 𝒮) be a measurable simple function, with the standard representation φ(s) = Σ_{i=1}^n a_i χ_{A_i}(s).
Then the integral of φ with respect to μ is ∫ φ dμ = Σ a_i μ(A_i).
The following exercise establishes the linearity of the integral for simple functions.
Exercise 7.17 Show that if φ, ψ ∈ M^+(S, 𝒮) are simple functions and c ≥ 0, then ∫ (φ + ψ) dμ = ∫ φ dμ + ∫ ψ dμ, and ∫ cφ dμ = c ∫ φ dμ.
The definition of the integral can be extended from simple functions to all of M^+(S, 𝒮) as follows.
### DEFINITION F
or f ∈ M^+(S, 𝒮), the integral of f with respect to μ is ∫ f dμ = sup ∫ θ dμ, where the supremum is over all simple functions θ in M^+(S, 𝒮) with 0 ≤ θ ≤ f.
If A ∈ 𝒮, then the integral of f over A with respect to μ is ∫_A f dμ = ∫_S χ_A f dμ.
When there is no possibility for confusion, we denote the integrals above by the more concise ∫ f dμ and where the inequality follows from Fatou’s Lemma.
Hence ∫ f dμ ≤ lim inf ∫ fₙ dμ.
Since g ≥ f, g ≥ 0, another application of Fatou’s Lemma gives ∫ g dμ - ∫ f dμ = ∫ (g - f) dμ ≤ lim inf ∫ (g - fₙ) dμ = lim inf (∫ g dμₙ - ∫ f dμₙ) = ∫ g dμ - lim sup ∫ fₙ dμ.
Hence lim sup ∫ fₙ dμ ≤ ∫ f dμ.
Combining the two results gives the desired conclusion. □ Notice that if the functions {fₙ} are uniformly bounded and μ is a finite measure, then the Lebesgue Dominated Convergence Theorem applies trivially: simply take g to be the constant function equal to the uniform bound on the fₙ’s.
We will make extensive use of this fact later, since we will often be dealing with bounded functions.
In Exercise 7.21 we saw that a measure λ on (S, 𝒮) could be obtained by integrating a function f ∈ M₊(S, 𝒮) with respect to a measure μ.
The next two results pursue the converse.
To state them we need the following definitions. **DEFINITIONS** Let λ and μ be finite measures on (S, 𝒮).
If for every A ∈ 𝒮, μ(A) = 0 implies λ(A) = 0, then λ is absolutely continuous with respect to μ, written λ ≪ μ.
If there is a set A ∈ 𝒮 such that μ(B) = μ(A ∩ B) for all B ∈ 𝒮, then λ is concentrated on A.
If there are disjoint sets A, B ∈ 𝒮 such that λ is concentrated on A and μ is concentrated on B, then λ and μ are mutually singular, written λ ⊥ μ. --- It is clear that if λ is obtained by integrating f ∈ M₊(S, 𝒮) with respect to a measure μ then λ is absolutely continuous with respect to μ.
The Radon-Nikodym Theorem proves the converse: that every measure λ that is absolutely continuous with respect to μ can be obtained as such an integral.
It also establishes that the function to be integrated is, in a certain sense, unique.
This theorem is extremely useful and very easy to state.
However, the proof of existence is rather difficult, and we omit it.
(See Bartle 1966, pp. 85-87, or Royden 1968, pp. 238-240.) **THEOREM 7.11 (Radon-Nikodym Theorem)** Let λ and μ be σ-finite positive measures on (S, 𝒮), with λ ≪ μ.
Then there is an integrable function h such that λ(A) = ∫_A h(s) μ(ds), for all A ∈ 𝒮.
The function h is unique in the sense that if g also has this property, then g = h μ-a.e. *Proof of uniqueness.* Let (S, 𝒮), μ and λ be given.
Suppose that there are two measurable functions g and h such that ∫_A g dμ = λ(A) = ∫_A h dμ, for all A ∈ 𝒮.
(5) Since both g and h are measurable, so is the function g - h.
Hence the set X = {s ∈ S: g(s) - h(s) > 0} is in 𝒮, and it follows from (5) that for A = X, ∫_X (g - h) dμ = ∫_X g dμ - ∫_X h dμ = 0.
Hence by Exercise 7.24a, μ(X) = 0.
Reversing the roles of g and h and repeating the argument, we then find that g = h, μ-a.e. □ The function h satisfying (5) is called the Radon-Nikodym derivative of λ with respect to μ, written dλ/dμ.
Our next result draws on this theorem to show that any two measures can be uniquely represented as the sums of “common” and mutually singular parts. **LEMMA 7.12** Let λ₁ and λ₂ be finite measures on (S, 𝒮).
Then there is a triple of measures γ, α₁, and α₂ such that λᵢ = γ + αᵢ, i = 1,2, and α₁ ⊥ α₂. *Proof.* Let μ = λ₁ + λ₂.
Then μ is a finite measure on (S, 𝒮), and λ₁ and λ₂ are both absolutely continuous with respect to μ.
Hence by the Radon-Nikodym Theorem, there exist nonnegative, integrable functions h₁ and h₂ such that λᵢ(A) = ∫_A hᵢ(s) μ(ds), for all A ∈ 𝒮, i= 1,2.
Define the function h by h(s) = min{h₁(s), h₂(s)} for all s ∈ S, and note that h is nonnegative and integrable.
Hence we can define the measures γ, α₁, and α₂ by γ(A) = ∫_A h(s) μ(ds), for all A ∈ 𝒮, and αᵢ(A) = ∫_A [hᵢ(s) - h(s)] μ(ds), for all A ∈ 𝒮, i = 1,2.
Define B = {s ∈ S: h₁(s) > h(s)} and C = {s ∈ S: h₂(s) > h(s)}.
Clearly B and C are disjoint and lie in 𝒮, with α₁ concentrated on B and α₂ on C, so that α₁ ⊥ α₂. □ ## 7.5 Product Spaces In this section we define product spaces, show how measures can be defined on such spaces, and develop a basic property of sets and functions in such spaces.
Let (X, ℬ) and (Y, 𝒞) be measurable spaces, and let Z be the Cartesian product of X and Y: Z = X × Y = {z = (x, y): x ∈ X, y ∈ Y}.
To define a σ-algebra of subsets of Z that is a natural product of ℬ and 𝒞, we first define an algebra of subsets of Z in terms of ℬ and 𝒞.
A set C = A × B ⊂ Z is a **measurable rectangle** if A ∈ ℬ and B ∈ 𝒞.
Let ℰ be the set of all measurable rectangles, and let 𝒜 be the set of all finite unions of measurable rectangles. **Exercise 7.27** Show that 𝒜 is an algebra and that every set in 𝒜 can be written as the finite union of disjoint measurable rectangles.
Let 𝒬 = σ(ℰ) × 𝒞 be the σ-algebra generated by ℰ.
The measurable space (Z, 𝒬) is called the **product space**.
The next exercise establishes an important fact about the Borel σ-algebras. **Exercise 7.28** Show that 𝒞(ℝᵏ × ℝˡ) = 𝒞(ℝᵏ) × 𝒞(ℝˡ) for all k, l = 1, …, where 𝒞(ℝⁿ) denotes the Borel sets in ℝⁿ.
The next result provides an extremely useful tool for defining measures on product spaces, one that is used extensively in the next section. **THEOREM 7.13** Let (X, ℬ), (Y, 𝒞), ℰ, and 𝒜 be as specified above.
Let ω: ℰ → ℝ₊ have the following properties: a. ω(∅) = 0; and b. if {Cᵢ} = {(Aᵢ × Bᵢ)}ᵢ=1ⁿ is a sequence of disjoint sets in ℰ and ⋃ᵢ Cᵢ is in 𝒜, then ω(⋃ᵢ Cᵢ) = ∑ᵢ ω(Cᵢ).
Then there is a measure on 𝒬 that coincides with ω on ℰ. *Proof.* Let ω: ℰ → ℝ₊ satisfying (a) and (b) be given.
It was shown in Exercise 7.27 that any set in 𝒜 can be written as the finite union of disjoint sets in ℰ.
Suppose that E ∈ 𝒜, and that ⋃ᵢ Cᵢ = E = ⋃ⱼ Dⱼ are two such ways of writing E.
We will show that ∑ᵢ ω(Cᵢ) = ∑ⱼ ω(Dⱼ), and define γ(E) to be their common value.
Since each Cᵢ and each Dⱼ is a rectangle, so is each set Eᵢⱼ = Cᵢ ∩ Dⱼ.
Moreover, the Eᵢⱼ’s are all disjoint, and Cᵢ = ⋃ⱼ Eᵢⱼ for all i, and Dⱼ = ⋃ᵢ Eᵢⱼ for all j.
Hence by property (b) above, ∑ⱼ ω(Eᵢⱼ) = ω(⋃ⱼ Eᵢⱼ) = ω(Cᵢ) for all i, and ∑ᵢ ω(Eᵢⱼ) = ω(⋃ᵢ Eᵢⱼ) = ω(Dⱼ) for all j.
Hence ∑ᵢ ω(Cᵢ) = ∑ᵢ ∑ⱼ ω(Eᵢⱼ) = ∑ⱼ ∑ᵢ ω(Eᵢⱼ) = ∑ⱼ ω(Dⱼ).
This proves that γ is well defined on 𝒜.
Properties (a) and (b) ensure that γ is a measure. □ It follows immediately from Theorem 7.13, together with the Carathéodory and Hahn Extension Theorems (Theorems 7.2 and 7.3), that to define a measure on a product space, it is sufficient to find a function ω defined on the measurable rectangles that satisfies (a) and (b) of Theorem 7.13.
The result in Theorem 7.13 can be extended in the obvious way to any space that is the product of a finite number of measurable spaces.
Since this is the version that we will need later, we state the required result here.
Let (Xₖ, 𝒮ₖ), k = 1 …, n, be measurable spaces, and let Z = X₁ × … × Xₙ be the Cartesian product of the Xₖ’s.
Call a set C ⊂ Z a **measurable rectangle** if C = A₁ × … × Aₙ, where Aₖ ∈ 𝒮ₖ, k = 1,…,n.
As above, let ℰ be the family of all measurable rectangles, let 𝒜 be the algebra consisting of all finite unions of measurable rectangles, and let 𝒬 be the σ-algebra generated by ℰ or by 𝒜.
We leave it as an exercise to show that the obvious analogue of Theorem 7.13 holds. **Exercise 7.29** Let ω: ℰ → ℝ₊ have the following properties: a. ω(∅) = 0; and b. if {Cᵢ} = {(Aᵢ¹ × … × Aᵢⁿ)}ᵢ=1ᵐ is a sequence of disjoint sets in ℰ and ⋃ᵢ Cᵢ is in ℰ, then ω(⋃ᵢ Cᵢ) = ∑ᵢ ω(Cᵢ).
Show that ω can be extended to a measure on 𝒬.
Our final result is a very basic and very appealing property of sets and functions in product spaces.
Before stating it, we need the following definitions.
Let (X, ℬ) and (Y, 𝒞) be measurable spaces, and let (Z, 𝒬) be the product space. **DEFINITION** Let E ⊂ Z and x ∈ X.
Then the **x-section of E** is the set (in Y) Eₓ = {y ∈ Y: (x, y) ∈ E}.
The **y-section of E**, (a set in X) denoted Eᵧ, is defined similarly. **DEFINITION** Let f: Z → ℝ and let x ∈ X.
Then the **x-section of f** is the function fₓ: Y → ℝ defined by fₓ(y) = f(x, y).
The **y-section of f**, fᵧ: X → ℝ, is defined similarly.
Thus the x-section of a set E in X × Y is simply the cross section of E atthe chosen x value, and a y-section of E is a cross section at the chosen y value.
An x-section of a real-valued function f on X x Y is found by fixing x at the chosen value and viewing f as a function of y only.
Similarly, a y-section of f is found by fixing y and viewing f as a function of x only.
The next theorem shows that every section of a measurable set is measurable, as is every section of a measurable function.
### THEOREM 7.14
Let (X, ℱ) and (Y, 𝒢) be measurable spaces, and let (Z, ℰ) be the product space.
If the set E in Z is ℰ-measurable, then every section of E is measurable; and if the function f: Z → ℝ is ℰ-measurable, then every section of f is measurable.
**Proof.** Let ℱ be the class of sets in ℰ with measurable x-sections.
We will show that ℱ contains the measurable rectangles and is a σ-algebra.
Let E be a measurable rectangle: E = A × B, where A ∈ ℱ and B ∈ 𝒢.
Let x ∈ X; then E_x = B if x ∈ A, ∅ if x ∉ A.
Since B, ∅ ∈ 𝒢, each set E_x is measurable.
Hence ℱ contains the measurable rectangles.
Suppose that E ∈ ℱ.
Then (E^c)_x = (E_x)^c, and the latter is in 𝒢.
Hence ℱ is closed under complementation.
Finally, let {E_n} be a countable sequence in ℱ.
Then (∪_{n=1}^∞ E_n)_x = ∪_{n=1}^∞ (E_n)_x.
Since each set (E_n)_x is in 𝒢 and 𝒢 is a σ-algebra, their union is also in 𝒢.
Hence ℱ is closed under countable union.
Let f: Z → ℝ be a measurable function, and let x ∈ X and a ∈ ℝ.
Then the set {y ∈ Y: f_x(y) > a} is simply the x-section of the set {(x, y) ∈ X × Y: f(x, y) > a}.
Hence the desired conclusion follows immediately from the result above.
It follows immediately from Theorem 7.14, together with Exercise 7.28, that if the Borel σ-algebras are used in Euclidean space, then sections of measurable sets and measurable functions are measurable.
This is a fact that we will use extensively later.
Notice that this is not true if the Lebesgue sets are used instead of the Borel sets.
Exercise 7.30 Show that ℒ₂ is not equal to ℒ₁ × ℒ₁, where ℒ denotes the Lebesgue measurable sets in ℝ. [Hint: Construct a set in ℝ² that is ℒ₂-measurable but has a section that is not ℒ₁-measurable.] The next exercise establishes that compositions of functions in product spaces are measurable.
Exercise 7.31 Let (S, 𝒮), (W, 𝒲), (X, 𝒳), (Y, 𝒴), and (Z, 𝒵) be measurable spaces.
Let f: W → Y and g: X → Z and h: Y × Z → ℝ be measurable functions.
Show that φ: W × X → ℝ defined by φ(w, x) = h(f(w), g(x)) is measurable. 7.6 The Monotone Class Lemma Many situations arise in which we want to establish that some property P holds for all sets in a certain σ-algebra 𝒜.
If 𝒜 is the σ-algebra generated by a family of sets, one way to do this is to show that a.
P holds for every set in 𝒜, and b. the family of sets for which P holds is a σ-algebra.
This is the method that was used above in the proof of Theorem 7.14.
This line of reasoning is often useful, but in some cases (b) is difficult to establish directly.
In this section we show that the same conclusion can be established by strengthening (a) and weakening (b).
To begin, we need the following definition.
### DEFINITION A
monotone class is a nonempty collection 𝒞 of sets such that 𝒞 contains a. the union of every nested increasing sequence A₁ ⊂ A₂ ⊂ ... of sets in 𝒞; b. the intersection of every nested decreasing sequence A₁ ⊃ A₂ ⊃ ... of sets in 𝒞. 200 7 Measure Theory and Integration We then have the following facts. 1.
Every σ-algebra is a monotone class. 2.
If 𝒜 is a nonempty collection of subsets of S, then there is a smallest monotone class containing 𝒜.
This is called the monotone class generated by 𝒜. 3.
If 𝒜 is a nonempty collection of subsets of S, then the σ-algebra generated by 𝒜 contains the monotone class generated by 𝒜. 4.
If a monotone class is an algebra, then it is a σ-algebra.
Fact (1) is obvious.
To prove (2), use an argument like the one in Exercise 7.1 for the smallest σ-algebra containing 𝒜.
To prove (3), note that every σ-algebra containing 𝒜 is a monotone class containing 𝒜.
A trivial example where the monotone class generated by 𝒜 is strictly smaller than the σ-algebra generated by 𝒜 is S = {0, 1}, 𝒜 = {{0}}, 𝒞 = {{0}, ∅}, 𝒜 = {∅, {0}, {1}, {0, 1}}.
To prove (4), note that if 𝒞 is an algebra, then it is closed under complementation and finite union.
Hence, given any sequence of sets Aₙ in 𝒞, we can construct the increasing sequence Bₙ defined by B₁ = A₁, Bₙ = Bₙ₋₁ ∪ Aₙ for n = 2, 3, ....
Then ∪_{n=1}^∞ Aₙ = ∪_{n=1}^∞ Bₙ, and the latter is in 𝒞.
Hence 𝒞 is closed under countable union.
The following lemma establishes an extremely useful fact about monotone classes generated by algebras.
### LEMMA 7.15
(Monotone Class Lemma) Let S be a set and let 𝒜 be an algebra of subsets of S.
Then the monotone class 𝒞 generated by 𝒜 is the same as the σ-algebra 𝒮 generated by 𝒜.
**Proof.** From fact (3) above, we have 𝒞 ⊂ 𝒮.
Hence by (4) it suffices to show that 𝒞 is an algebra.
Since 𝒜 is an algebra and 𝒜 ⊂ 𝒞, it follows that ∅, S ∈ 𝒞.
Hence it suffices to show that 𝒞 is closed under complementation and finite intersection.
For each A ∈ 𝒞, define 𝒞(A) = {B ∈ 𝒞: A ∩ B ∈ 𝒞, A ∩ B^c ∈ 𝒞, and A^c ∩ B ∈ 𝒞}. 7.6 The Monotone Class Lemma 201 Now suppose that 𝒞(A) = 𝒞 for all A ∈ 𝒞.
Then A, B ∈ 𝒞 implies (A ∩ B) ∈ 𝒞; and since S ∈ 𝒞, it follows that A ∈ 𝒞 implies A^c ∈ 𝒞.
That is, 𝒞 is closed under complementation and finite intersection.
Hence it suffices to show that 𝒞(A) = 𝒞 for all A ∈ 𝒞.
First we will show that each 𝒞(A) is a monotone class.
To see this, fix A and suppose that {Bₙ} is an increasing sequence in 𝒞(A).
Then the sequences {A ∩ Bₙ}, {A ∩ Bₙ^c}, and {A^c ∩ Bₙ} are all in 𝒞.
But each of these sequences is monotone.
Therefore, since 𝒞 is a monotone class, A ∩ (∪_n Bₙ) = ∪_n (A ∩ Bₙ), A^c ∩ (∪_n Bₙ) = ∪_n (A^c ∩ Bₙ), and A ∩ (∪_n Bₙ)^c = A ∩ (∩_n Bₙ^c) = ∩_n (A ∩ Bₙ^c) are all in 𝒞.
Hence (∪_n Bₙ) is in 𝒞(A).
A similar argument holds if {Bₙ} is a decreasing sequence.
Hence 𝒞(A) is a monotone class.
Next note that since 𝒜 is an algebra and 𝒜 ⊂ ∪_{A∈𝒞} 𝒞(A), it follows that 𝒜 ⊂ 𝒞(A) for all A ∈ 𝒜.
Then, since each 𝒞(A) is a monotone class and 𝒞 is the smallest monotone class containing 𝒜, it follows that 𝒞(A) = 𝒞 for all A ∈ 𝒜.
Finally, since B ∈ 𝒞(A) implies A ∈ 𝒞(B) for all A, B ∈ 𝒞, it follows that 𝒞(A) ⊂ 𝒞(B) for all A, B ∈ 𝒞.
Hence 𝒞(B) = 𝒞 for all B ∈ 𝒞, as was to be shown.
A very useful result follows immediately from the Monotone Class Lemma.
Let 𝒜 be an algebra of sets, let 𝒮 be the σ-algebra generated by 𝒜, and P be some property of sets.
Then to establish that P holds for all sets in 𝒮, it suffices to show that a.
P holds for all sets in the algebra 𝒜; and b. the family of sets for which P holds is a monotone class.
It is often easier to prove that the family of sets for which a property holds is a monotone class than it is to prove that the family is a σ-algebra.
We will often want to use this type of argument to show that a property P holds for all sets in a product σ-algebra ℱ × 𝒢.
Therefore, by 202 7 Measure Theory and Integration Exercise 7.27 and the Monotone Class Lemma, it will suffice to show that a.
P holds for all finite unions of disjoint measurable rectangles, and b. the family of sets ℰ for which P holds is a monotone class. 7.7 Conditional Expectation Let (Ω, ℱ, P) be a probability space, and let A be any measurable set with P(A) > 0.
Then for any measurable set B, it is standard usage to call P(B ∩ A)/P(A) the conditional probability of the event B given A, and to use Pr(B|A) or P(B|A) to denote this value.
Note that it follows immediately from Exercise 7.4 that B ↦ P(B ∩ A)/P(A) is itself a probability measure on (Ω, ℱ).
Then, for any measurable, real-valued function f, it is standard to call ∫_A f dP / P(A) the conditional expectation of f given A and to use E(f|A) to denote this value.
These definitions are fine as far as they go, but they do not cover all situations of interest.
For example, let (Ω, ℱ) be the unit square [0, 1]², with the Borel sets, and let P be the probability measure corresponding to...to the uniform density on the square.
That is, $\mu(B) = \lambda_2(B)$, all $B \in \mathcal{N}$, where $\lambda_2$ denotes Borel measure on $\mathbb{R}^2$.
Now choose any $a \in [0, 1]$, and let $A = \{(x, y) \in Q: x = a\}$.
Thus, the set $A$ is simply a vertical “slice” from the square.
Consider the problem of defining conditional probabilities and conditional expectations given $A$.
Since $\mu(A) = 0$, the formulas above are of no use; in fact, they suggest that conditional probabilities and conditional expectations are undefined.
Common sense says, however, that they ought to be defined as follows.
For any $B \in \mathcal{F}$, let $\alpha(B) = \lambda_1(A \cap B)$, where $\lambda_1$ denotes Borel measure on $\mathbb{R}^1$.
That is, $\alpha$ should be the probability measure corresponding to the uniform density on the set $A$.
Conditional expectations given $A$ can then be defined exactly as before.
In both of these examples we have shown how to calculate a number that can be interpreted as the conditional expectation of a fixed function $f$ given the occurrence of a fixed event $A \in \mathcal{F}$.
As we have seen, a number can be calculated in each case, but the procedure is different for the two.
Moreover, there are other cases of interest that cannot be dealt with by either of these procedures.
An alternative strategy is needed, one that is less direct but has the virtue of applying to all situations.
This method proceeds by defining the conditional expectation of a given function $f: Q \to \mathbb{R}$ as itself a function, call it $g$, which also maps $Q$ to $\mathbb{R}$.
This function is constructed so that for sets $A \in \mathcal{F}$ of interest, $g(\omega)$ is constant on $A$, and the value $g(\omega)$, $\omega \in A$, is interpreted as $E(f|A)$.
Clearly, the construction of the function $g$ requires choosing a suitable family $\{A_i\}$ of sets in $\mathcal{N}$.
The rest of this section is organized as follows.
First we look more carefully at situations like the first example above and show how the function $g$ is defined.
We then derive an important property of the pair $(f, g)$ and show that this property can be used to define the function $g$ in situations where the direct strategy fails.
Finally, we verify that the conditional expectation of $f$, given $A$, can be found by evaluating $g$ at any point $\omega \in A$; and that the conditional probability of any event $B$, given $A$, can be found by taking $f$ to be the indicator function $\chi_B$.
Let $(Q, \mathcal{F}, \mu)$ be a fixed probability space.
Call a family of subsets $\{A_i\}_{i \in H}$ of $Q$ a measurable partition (of $Q$) if the following three conditions hold: $A_i \in \mathcal{F}$, all $i \in H$; $\bigcup_{i \in H} A_i = Q$; $A_i \cap A_j = \emptyset$, all $i \neq j$.
Thus each partition element must be a measurable set; their union must be the entire space $Q$; and they must be pairwise disjoint.
We call a measurable partition countable if the index set $H$ is countable.
Given $(Q, \mathcal{F}, \mu)$, let $\{A_i\}_{i=1}^\infty$ be any countable, measurable partition of $Q$, with $\mu(A_i) > 0$, all $i$.
Then as noted above, for each set $A_i$ we can define the conditional probability of any event by $\Pr(B|A_i) = \alpha_i(B) = \mu(B \cap A_i)/\mu(A_i)$, all $B \in \mathcal{F}$, and the conditional expectation of any integrable function $f$ by $E(f|A_i) = \int f d\alpha_i$, all $f \in L^1(Q, \mathcal{F}, \mu)$.
Notice that it follows directly from these two definitions that $\sum_i E(f|A_i)\mu(A_i) = \int f d\mu$, all $f \in L^1(Q, \mathcal{F}, \mu)$.
Next, let $\mathcal{A}$ be the $\sigma$-algebra generated by the family of sets $\{A_i\}$, and note that $\mathcal{A} \subset \mathcal{F}$.
Define the function $E(f|\mathcal{A}): Q \to \mathbb{R}$ by (3) $E(f|\mathcal{A})(\omega) = E(f|A_i)$, all $\omega \in A_i$, all $A_i$, i.e., Thus $E(f|\mathcal{A})$ is an $\mathcal{A}$-measurable function that takes the constant value $E(f|A_i)$ on each set $A_i$.
Note carefully the distinction between $E(f|\mathcal{A})$ and $E(f|A_i)$.
For any fixed function $f$, the former is simply a real number, for each $A_i$, whereas the latter is a function mapping $Q$ to $\mathbb{R}$.
In what follows it is useful to rewrite (3) as (4) $E(f|\mathcal{A})(\omega) = \sum_i E(f|A_i)\chi_{A_i}(\omega)$, all $\omega \in Q$.
What properties does the function $E(f|\mathcal{A})$ have?
Let $C$ be any set in $\mathcal{A}$.
Since $\{A_i\}$ is a countable partition of $Q$, there is a countable set $J \subset$ $\{1, 2, ...\}$ such that $C = \bigcup_{j \in J} A_j$, and (5) $\chi_C(\omega) = 1$ iff $\omega \in A_j$ for some $j \in J$, i.e., $\chi_C(\omega) = \sum_{j \in J} \chi_{A_j}(\omega)$.
Integrating $E(f|\mathcal{A})$ over the set $C$ and using this fact, we find that $\int_C E(f|\mathcal{A}) d\mu = \int \sum_{j \in J} E(f|A_j)\chi_{A_j} d\mu$ $= \sum_{j \in J} \int E(f|A_j)\chi_{A_j} d\mu$ $= \sum_{j \in J} E(f|A_j)\mu(A_j)$ $\sum_{j \in J} \int_{A_j} f d\mu$ $= \int_{\bigcup_{j \in J} A_j} f d\mu$ $= \int_C f d\mu$, where the first line uses (4); the second uses the Lebesgue Dominated Convergence Theorem; the third uses a basic fact about integrals of indicator functions; the fourth uses (5); the fifth uses (2); and the last uses the fact that $C = \bigcup_{j \in J} A_j$.
This establishes that over any set $C \in \mathcal{A}$, the integrals of the $\mathcal{F}$-measurable function $f$ and of the $\mathcal{A}$-measurable function $E(f|\mathcal{A})$ are equal.
To extend the concept of conditional expectation to $\sigma$-algebras not generated by a countable partition, we will use this last property to develop a method for defining a function $E(f|\mathcal{A})$, given any integrable function $f$ and any $\sigma$-algebra $\mathcal{A} \subset \mathcal{F}$.
### DEFINITION L
et $(Q, \mathcal{F}, \mu)$ be a probability space; let $\mathcal{A} \subset \mathcal{F}$ be a $\sigma$-algebra; and let $f: Q \to \mathbb{R}$ be an integrable function.
Then the conditional expectation of $f$ relative to $\mathcal{A}$ is an $\mathcal{A}$-measurable function $E(f|\mathcal{A}): Q \to \mathbb{R}$ such that (6) $\int_C E(f|\mathcal{A}) d\mu = \int_C f d\mu$, all $C \in \mathcal{A}$.
The following theorem shows that an $\mathcal{A}$-measurable function $E(f|\mathcal{A})$ satisfying (6) always exists and that it is unique in an appropriate sense.
### THEOREM 7.16
Let $(Q, \mathcal{F}, \mu)$ be a probability space; let $\mathcal{A} \subset \mathcal{F}$ be a $\sigma$-algebra; and let $f: Q \to \mathbb{R}$ be an integrable function.
Then there exists an $\mathcal{A}$-measurable function $E(f|\mathcal{A})$ satisfying (6).
This function is unique in the sense that if $g$ also satisfies (6), then $E(f|\mathcal{A}) = g$, a.e.
**Proof.** Consider first the case where $f \geq 0$.
Define the set function $\nu: \mathcal{A} \to \mathbb{R}$ by $\nu(C) = \int_C f d\mu$, all $C \in \mathcal{A}$.
Since $f$ is integrable, $\int_Q f d\mu < \infty$ so that $\nu$ is finite-valued.
Clearly $\nu$ is also countably additive, and hence it is a measure on $\mathcal{A}$.
Moreover, $\mu(C) = 0$ implies that $\nu(C) = 0$, so $\nu$ is absolutely continuous with respect to $\mu$.
Hence by the Radon-Nikodym Theorem (Theorem 7.11), there exists an $\mathcal{A}$-measurable function $E(f|\mathcal{A})$, unique in the sense claimed, such that $\nu(C) = \int_C E(f|\mathcal{A}) d\mu$, all $C \in \mathcal{A}$.
If $f$ takes on both positive and negative values, apply the argument above separately to $f^+$ and $f^-$, and let $E(f|\mathcal{A}) = E(f^+|\mathcal{A}) - E(f^-|\mathcal{A})$. $\square$ Theorem 7.16 can be used as follows.
Suppose that we are interested in calculating conditional expectations and probabilities, given events $A_i$, $i \in H$, where the family of sets $\{A_i\}_{i \in H}$ is a measurable partition of $Q$.
Let $\mathcal{A}$ be the $\sigma$-algebra generated by the family $\{A_i\}$.
Given any integrable function $f$, define $E(f|\mathcal{A})$ by Theorem 7.16.
Notice that the requirement that $E(f|\mathcal{A})$ be $\mathcal{A}$-measurable implies that $E(f|\mathcal{A})$ is constant on each of the sets $A_i$ in the partition.
(Why?) Hence for any partition element $A_i$, and any $\omega \in A_i$, (7) $E(f|A_i) = E(f|\mathcal{A})(\omega)$, since for any $C \subset A_i$ in $\mathcal{A}$, $\int_C E(f|\mathcal{A}) d\mu = \int_C f d\mu$, and if $C = A_i$, $E(f|A_i) \mu(A_i) = \int_{A_i} f d\mu$, so $E(f|A_i) = \int_{A_i} f d\mu / \mu(A_i)$.
Notice that if $\mu(A_i) > 0$, then $E(\chi_B|A_i) = \frac{1}{\mu(A_i)} \int_{A_i} \chi_B d\mu$, all $\omega \in A_i$.
Hence for any set $A_i$ of positive measure, $E(f|A_i) = E(f|\mathcal{A})(\omega)$, all $\omega \in A_i$, where $E(f|\mathcal{A})$ is defined by (6) and $E(f|A_i)$ is defined by (1) if we set $A = A_i$.
That is, our formal definition of conditional expectation coincides with our intuitive notion whenever the latter is well defined.
Similarly, to obtain the conditional probability $\Pr(B|A_i)$ of any event $B \in \mathcal{F}$, simply take $f$ to be the indicator function of $B$, $\chi_B$.
Then (7) implies that $E(\chi_B|\mathcal{A})(\omega) \mu(A_i) = \int_{A_i} \chi_B d\mu = \mu(B \cap A_i)$, all $\omega \in A_i$, all $i \in H$.
If $\mu(A_i) > 0$, then $E(\chi_B|\mathcal{A})(\omega) = \mu(B \cap A_i)/\mu(A_i)$, all $\omega \in A_i$.
That is, for any set $B$ of positive measure, $E(\chi_B|\mathcal{A})$ as defined by Theorem 7.16 coincides with our earlier definition of conditional probability.
Therefore we define $\Pr(B|A_i)$ for all sets $A_i$ by (8) $\Pr(B|A_i) = E(\chi_B|\mathcal{A})(\omega)$, all $\omega \in A_i$, all $i \in H$.
Exercise 7.32 Let $(Q, \mathcal{F}, \mu)$ be given, and let $\{A_i\}_{i=1}^\infty$ be a countable, measurable partition of $Q$.
Define the index set $J \subset \{1, 2, ...\}$ so that $\mu(A_i) > 0$, all $i \in J$; $\mu(A_i) = 0$, all $i \notin J$.
Let $\mathcal{A}$ be the $\sigma$-algebra generated by $\{A_i\}_{i \in J}$.a.
Let f be an integrable function on Ω.
Describe explicitly the equivalence class of functions E(f|σ).
On what set(s) A_i, if any, can functions in this equivalence class differ? b.
Let B ∈ ℱ be any event.
Describe explicitly the equivalence class of functions E(1_B|σ).
On what set(s) A_i, if any, does Pr(B|A_i) as defined in (8) differ for different members of this equivalence class?
Exercise 7.33 Let (Ω, ℱ) be the unit square [0, 1]², with its Borel subsets, and let μ be a probability measure on (Ω, ℱ) defined by a continuous density.
That is, there exists a continuous function p: Ω → ℝ such that μ(B) = ∫_B p(ω) dλ(ω), all B ∈ ℱ, where λ denotes Borel measure on ℝ².
Let {A_n}_{n∈ℕ} be the following family of subsets of Ω: A_n = {(x, y) ∈ Ω: x < 1/n}, n ∈ [0, 1] = ℕ Let σ be the σ-algebra generated by the family {A_n}. a.
Let f be an integrable function on Ω.
Describe explicitly the equivalence class of functions E(f|σ). b.
Let B ∈ ℱ be any event.
Describe explicitly the equivalence class of functions E(1_B|σ). --- We have defined conditional expectation relative to a σ-algebra σ ⊂ ℱ.
It is easy enough to relate this definition to the more familiar idea of the expectation of one random variable conditional on another.
Let f and g be two random variables on (Ω, ℱ).
Let G be the σ-algebra generated by the sets of the form {ω ∈ Ω: g(ω) ≤ a}, a ∈ ℝ.
(We call G the σ-algebra generated by the random variable g.) Then G ⊂ ℱ and the function E(f|G) is well defined by (6).
We will write E(f|σ) and E(f|g) interchangeably.
Finally, it is convenient to develop here a property of conditional expectations that we will use later.
Let (Ω, ℱ, μ) be a given; let σ₁ ⊂ σ₂ ⊂ ℱ be two σ-algebras, one contained in the other; and let f: Ω → ℝ be any integrable function.
Then E(f|σ₁) and E(f|σ₂) are σ₁-measurable and σ₂-measurable functions respectively on Ω.
Moreover, (6) implies that ∫_C E(f|σ₂) dμ = ∫_C f dμ, all C ∈ σ₂ ⊂ ℱ Now consider the σ₂-measurable function E(f|σ₂): Ω → ℝ.
The conditional expectation of this function, given σ₁, is the σ₁-measurable function E[E(f|σ₂)|σ₁].
We then have ∫_C E[E(f|σ₂)|σ₁] dμ = ∫_C E(f|σ₂) dμ = ∫_C f(ω) dμ(ω) = ∫_C E(f|σ₁) dμ, all C ∈ σ₁, where the first line uses (6); the second uses (9) and the fact that C ∈ σ₁ ⊂ σ₂; and the last uses (9) again.
This fact is referred to as the law of the iterated expectation.
Stated a little differently, it says that if σ₁ ⊂ σ₂, then ∫_C [f - E(f|σ₂)] dμ = 0, all C ∈ σ₁. 7.8 Bibliographic Notes There are many good texts on measure theory.
Bartle (1966) and Royden (1968) are excellent introductory texts; Halmos (1974) is perhaps the most complete treatment of the subject.
The material here follows Bartle most closely.
Chung (1974) is an excellent introduction to probability theory that uses a measure-theoretic approach throughout.
Our treatment of conditional expectation in Section 7.7 is based on his Section 9.1.
Neveu (1965), Breiman (1968), and Shiryayev (1984) are also good introductory treatments.
Léve (1977), which is very complete, is extremely useful as a reference. ---
## 8 Markov Processes
In this chapter we draw on the language and results of the last to develop a suitable method for incorporating exogenous stochastic shocks into dynamic programs.
To preserve the recursive structure of such models, clearly we must require that the exogenous shocks have a recursive structure as well.
Shocks that have this structure, in an appropriate sense, are called Markov processes; in this chapter we define Markov processes and discuss some of their basic properties.
In the introduction to Chapter 7 we presented two ways of incorporating stochastic shocks into a functional equation, according to whether the space of possible values for the exogenous shocks was a discrete set or an interval in ℝ¹.
We can now write both of these in a unified way.
Let (Z, Σ) be a measurable space; let P be a probability measure on (Z, Σ); and as in the discussion of functional equations under certainty, let X be a subset of a Euclidean space.
Then we can consider the functional equation (1) u(x, z) = sup [F(x, y, z) + β ∫_Z u(y, z') P(dz', z)], y∈T(x,z) Here x is the current value of the endogenous state variable, z is the current value of the exogenous shock, y is the value of the endogenous state variable next period, and z' is the (currently unknown) value of next period’s shock.
The interpretation of (1) is that the current shock z is known at the time y is chosen, and that z may affect the current-period return, or the set of y values available for next period, or both.
This equation includes as special cases both of those described in the introduction to Chapter 7, as well as other cases, and it is fine as far as it goes.
For our purposes, however, it does not go quite far enough.
With the specification in (1), the exogenous shocks are assumed to be drawn from the same fixed distribution P each period.
That is, (1) excludes the possibility of period-to-period dependence (serial correlation) in the values of the shocks.
Since many types of shocks (for example, temperature or rainfall) display such patterns, this is a serious drawback.
To allow for such dependence, we must allow the current value of the shock to affect the probability measure over the shock next period.
Thus, we are led to consider functional equations of the form (2) u(x, z) = sup [F(x, y, z) + β ∫_Z u(y, z') Q(dz', z)], y∈T(x,z) where for each z ∈ Z, Q(·, z) is a probability measure on Σ.
With the specification in (2), the current value of the exogenous shock determines which probability measure is relevant for next period’s shock. [Note that the example in (1) is a special case of (2) in which Q does not depend on its first argument.] Functions Q with the appropriate features are called transition functions, and we begin in Section 8.1 below by defining transition functions and developing several of their properties.
To state the sequence problem corresponding to (2) requires having a notation for sequences of shocks.
In Section 8.2 we define the spaces in which such sequences lie and show how a transition function can be used to define probability measures over those spaces.
We also provide formal definitions of the terms stochastic process and Markov process and show that a transition function as defined in Section 8.1 defines a Markov process.
In Section 8.3 we develop a result that is useful in evaluating expectations of functions of Markovian shocks.
This material is drawn upon in Section 9.1, where we develop the connections between solutions to functional equations like (2) and solutions to the corresponding sequence problems (the Principle of Optimality for stochastic dynamic programs).
Finally, in Section 8.4 we illustrate a standard line of argument used to prove that a function has the properties required of a transition function.
To do this we prove that a transition function can be defined from a first-order stochastic difference equation.
A similar argument is developed in Section 9.6, where we show that the solution to a functional equation like (1) or (2) defines a transition function on the space (S, 𝒮) = (X × Z, 𝒳 × Σ), the state space for the system.
Thus, even if the exogenous shocks are independently drawn in each period, as in (1), the motion over time of the state variable s = (x, z) is described by a Markov process.
This fact in turn motivates the study of convergence results for Markov processes in Chapters 11 and 12, the stochastic analogue of the stability theory in Chapter 6.
Although the material in Section 8.1 is needed before proceeding to Chapters 9–13, the material in Sections 8.2–8.4 is not, and the reader who is anxious to get on with the analysis of stochastic functional equations can skip to Part III.tions is invited to skip them.
There is no loss in continuity in proceeding directly from Section 8.1 to Section 9.2 (the analysis of stochastic functional equations) and then to Chapters 10-13 (economic applications of stochastic dynamic programming, convergence results for Markov processes, and applications of the convergence results). 8.1 Transition Functions In this section we define precisely the family of functions \( Q \) that can be used to incorporate stochastic shocks into a functional equation, and we develop some of their basic properties.
We begin with the following definition. **DEFINITION** Let \((Z, \Sigma)\) be a measurable space.
A transition function is a function \(Q: Z \times \Sigma \rightarrow [0, 1]\) such that a. for each \(z \in Z\), \(Q(z, \cdot)\) is a probability measure on \((Z, \Sigma)\); and b. for each \(A \in \Sigma\), \(Q(\cdot, A)\) is a \(\Sigma\)-measurable function.
The interpretation is that \(Q(z, A)\) is the probability that the next period's shock lies in the set \(A\), given that the current shock is \(z\).
That is, \[ Q(z, A) = \Pr\{\xi_{t+1} \in A \mid \xi_t = z\}, \] where \(\xi_t\) denotes the (random) state in period \(t\).
(The precise meaning of this notation will be made clear in Section 8.2.) (Notice that with \(Q\) as specified here, the probability measure over the shock in any period can depend only upon the value of the shock in one previous period.
In some applications one might want to allow dependence on several lagged values.
It is shown in Exercise 8.11 that, by expanding the state space appropriately, any such system can be modeled with only one lag.) Associated with any transition function \(Q\) on a measurable space \((Z, \Sigma)\) are two operators, both of which are used repeatedly later.
The first is an operator on \(\Sigma\)-measurable functions; the other is an operator on probability measures on \((Z, \Sigma)\).
We turn next to defining these operators and establishing their properties.
For any \(\Sigma\)-measurable function \(f\), define \(Tf\) by \[ (Tf)(z) = \int_Z f(z') Q(z, dz'), \quad \text{all } z \in Z. \tag{1} \] Since for each \(z \in Z\), \(Q(z, \cdot)\) is a probability measure, it follows that \(Tf\) is well defined if \(f\) is either nonnegative or bounded.
We interpret \((Tf)(z)\) as the expected value of the function \(f\) next period, given that the current state is \(z\).
For any probability measure \(\mu\) on \((Z, \Sigma)\), define \(T^*\mu\) by \[ (T^*\mu)(A) = \int_Z Q(z, A) \mu(dz), \quad \text{all } A \in \Sigma. \tag{2} \] Since for each \(A \in \Sigma\), \(Q(\cdot, A)\) is bounded and \(\Sigma\)-measurable, it follows that \(T^*\mu\) is well defined.
We interpret \((T^*\mu)(A)\) as the probability that the state next period lies in the set \(A\), if the current state is drawn according to the probability measure \(\mu\).
That is, \(T^*\mu\) is the probability measure over the state next period if \(\mu\) is the probability measure over the current state.
Recall that for any measurable space \((Z, \Sigma)\), \(M^*(Z, \Sigma)\) is the space of nonnegative, \(\Sigma\)-measurable, extended real-valued functions; and \(B(Z, \Sigma)\) is the space of bounded, \(\Sigma\)-measurable, real-valued functions.
In addition, define \(A(Z, \Sigma)\) to be the space of probability measures on \((Z, \Sigma)\).
The next two theorems deal with the properties of \(T\) viewed as an operator on \(M^*(Z, \Sigma)\) or \(B(Z, \Sigma)\), and of \(T^*\) viewed as an operator on \(A(Z, \Sigma)\).
The proofs of both theorems make use of the Monotone Convergence Theorem (Theorem 7.8). **THEOREM 8.1** The operator \(T\) defined in (1) maps the space of nonnegative, \(\Sigma\)-measurable, extended real-valued functions into itself; that is, \(T: M^*(Z, \Sigma) \rightarrow M^*(Z, \Sigma)\). *Proof.* Choose \(f \in M^*(Z, \Sigma)\).
Since \(f\) is nonnegative and measurable, \(Tf\) is well defined, although it may take on the value \(+\infty\).
To see that \(Tf\) is measurable, first consider any indicator function for a measurable set: \(f = \chi_A\), where \(A \in \Sigma\).
Then \[ (T\chi_A)(z) = \int_Z \chi_A(z') Q(z, dz') = \int_A Q(z, dz') = Q(z, A), \quad \text{all } z \in Z. \] Hence by property (b) in the definition of a transition function, \(T\chi_A\) is a measurable function.
Next consider any nonnegative simple function \(\phi \in M^*(Z, \Sigma)\), and let \(\phi = \sum_{i=1}^n a_i \chi_{A_i}\) be its standard representation.
Then \[ \begin{aligned} (T\phi)(z) &= \int_Z \left[ \sum_{i=1}^n a_i \chi_{A_i}(z') \right] Q(z, dz') \\ &= \sum_{i=1}^n a_i \left[ \int_Z \chi_{A_i}(z') Q(z, dz') \right] \\ &= \sum_{i=1}^n a_i (T\chi_{A_i})(z), \quad \text{all } z \in Z. \end{aligned} \] Since each function \(T\chi_{A_i}\) is \(\Sigma\)-measurable, it follows from Exercise 7.12 that \(T\phi\) is also \(\Sigma\)-measurable.
Finally, let \(f \in M^*(Z, \Sigma)\).
Then by Theorem 7.5 there exists an increasing sequence of simple functions \(\{\phi_n\}\) in \(M^*(Z, \Sigma)\) converging pointwise to \(f\).
Hence \[ \begin{aligned} (Tf)(z) &= \int_Z f(z') Q(z, dz') \\ &= \int_Z \left[ \lim_{n \to \infty} \phi_n(z') \right] Q(z, dz') \\ &= \lim_{n \to \infty} \int_Z \phi_n(z') Q(z, dz') \\ &= \lim_{n \to \infty} (T\phi_n)(z), \quad \text{all } z \in Z, \end{aligned} \] where the second line uses the Monotone Convergence Theorem.
Hence the sequence of measurable functions \(\{T\phi_n\}\) converges pointwise to \(Tf\), so that by Theorem 7.4, \(Tf\) is measurable. \(\square\) **COROLLARY** The operator \(T\) defined in (1) maps the space of bounded, \(\Sigma\)-measurable functions into itself; that is, \(T: B(Z, \Sigma) \rightarrow B(Z, \Sigma)\). *Proof.* Since for each \(z \in Z\), \(Q(z, \cdot)\) is a probability measure, it is clear that \(0 \leq f \leq m\) implies that \(0 \leq Tf \leq m\).
Choose \(f \in B(Z, \Sigma)\); apply the argument above to \(f^+\) and \(f^-\); and note that since \(Tf^+\) and \(Tf^-\) are bounded, \(Tf = Tf^+ - Tf^-\). \(\square\) The proof of Theorem 8.1 shows why property (b) in the definition of a transition function is needed.
The following exercise establishes the linearity of the operator \(T\). **Exercise 8.1** Let \(f, g \in B(Z, \Sigma)\) and \(\alpha, \beta \in \mathbb{R}\).
Show that \(T(\alpha f + \beta g) = \alpha Tf + \beta Tg\).
We turn next to the operator \(T^*\). **THEOREM 8.2** The operator \(T^*\) defined in (2) maps the space of probability measures on \((Z, \Sigma)\) into itself; that is, \(T^*: A(Z, \Sigma) \rightarrow A(Z, \Sigma)\). *Proof.* Choose \(\mu \in A(Z, \Sigma)\).
Since \(Q \geq 0\), it is clear that \(T^*\mu \geq 0\).
Also, since \(Q(z, \emptyset) = 0\) and \(Q(z, Z) = 1\), all \(z \in Z\), it follows that \((T^*\mu)(\emptyset) = 0\) and \((T^*\mu)(Z) = 1\).
Hence it suffices to show that \(T^*\mu\) is countably additive.
Let \(\{A_i\}\) be a disjoint sequence in \(\Sigma\), with \(A = \bigcup_i A_i\).
Then \[ \begin{aligned} (T^*\mu)(A) &= (T^*\mu)\left( \bigcup_i A_i \right) \\ &= \int_Z Q\left(z, \bigcup_i A_i\right) \mu(dz) \\ &= \int_Z \sum_i Q(z, A_i) \mu(dz) \\ &= \sum_i \int_Z Q(z, A_i) \mu(dz) \\ &= \sum_i (T^*\mu)(A_i), \end{aligned} \] where the second line follows from the Monotone Convergence Theorem (cf.
Exercise 7.22), and the third uses the fact that for each \(z \in Z\), \(Q(z, \cdot)\) is a probability measure [property (a) in the definition of a transition function]. \(\square\) The following exercise establishes the linearity of \(T^*\). **Exercise 8.2** Let \(\mu, \nu \in A(Z, \Sigma)\), and \(\alpha \in (0, 1)\).
Show that \(T^*[\alpha \mu + (1 - \alpha)\nu] = \alpha T^*\mu + (1 - \alpha)T^*\nu\).
The operator \(T\) is called the Markov operator associated with \(Q\), and \(T^*\) is called the adjoint of \(T\).
The following theorem shows the intimate connections between these two operators. **THEOREM 8.3** Let \(Q\) be a transition function on the measurable space \((Z, \Sigma)\), and let the operators \(T\) and \(T^*\) be defined by (1) and (2).
Then for any function \(f \in M^*(Z, \Sigma)\), \[ \int_Z (Tf)(z) \mu(dz) = \int_Z f(z') (T^*\mu)(dz'), \quad \text{all } \mu \in A(Z, \Sigma). \tag{3} \] *Proof.* We will prove the result in three steps, showing in turn that (3) holds for all indicator functions of measurable sets, all measurable simple functions, and all nonnegative measurable functions.
First, let \(A \in \Sigma\) be any measurable set, and let \(\chi_A\) be the indicator function for \(A\).
Then as shown in the proof of Theorem 8.1, \((T\chi_A)(z) = Q(z, A)\), all \(z \in Z\).
Hence for any \(\mu \in A(Z, \Sigma)\), \[ \begin{aligned} \int_Z (T\chi_A)(z) \mu(dz) &= \int_Z Q(z, A) \mu(dz) \\ &= (T^*\mu)(A) \\ &= \int_Z \chi_A(z') (T^*\mu)(dz'). \end{aligned} \] Hence (3) holds if \(f\) is the indicator function of a measurable set.
Next, let \(\phi\) be any nonnegative measurable simple function, and let \(\phi = \sum_{i=1}^n a_i \chi_{A_i}\) be its standard representation.
Then \[ \begin{aligned} \int_Z (T\phi)(z) \mu(dz) &= \int_Z \left[ \sum_{i=1}^n a_i (T\chi_{A_i})(z) \right] \mu(dz) \\ &= \sum_{i=1}^n a_i \int_Z (T\chi_{A_i})(z) \mu(dz) \\ &= \sum_{i=1}^n a_i \int_Z \chi_{A_i}(z') (T^*\mu)(dz') \\ &= \int_Z \left[ \sum_{i=1}^n a_i \chi_{A_i}(z') \right] (T^*\mu)(dz') \\ &= \int_Z \phi(z') (T^*\mu)(dz'), \end{aligned} \] where the first and last lines use the definition of \(\phi\), the second uses linearity of the integral, the third uses the result for indicator functions, and the fourth and fifth use linearity of the integral and the definition of \(\phi\).
Hence (3) holds for all measurable simple functions.
Finally, choose \(f \in M^*(Z, \Sigma)\).
Then by Theorem 7.5, there exists an increasing sequence of measurable simple functions \(\{\phi_n\}\) in \(M^*(Z, \Sigma)\) converging pointwise to \(f\).
And, as shown above, for any \(\mu \in A(Z, \Sigma)\), \[ \int_Z (T\phi_n)(z) \mu(dz) = \int_Z \phi_n(z') (T^*\mu)(dz'), \quad n = 1, 2, \dots \tag{4} \] The rest of the proof consists of two applications of the Monotone Convergence Theorem (Theorem 7.8) to develop expressions for the limits on each side of (4) as \(n \rightarrow \infty\).P(w, A) for w ∈ W, A ∈ Σ Q(i, w'), A(x) = f if w ∈ A; all w, w' ∈ W; all A, B ∈ Σ, defines a transition function on (Z, Σ). [Hint.
Use Theorem 7.13 and the Monotone Class Lemma.] 8.5 Bibliographic Notes Doob (1953, chap.
V) and Gihman and Skorohod (1974, chap.
II, sects. 4 and 5) both contain excellent discussions of transition functions and Markov processes.
A general proof that, given a transition function on a measurable space, there exists a corresponding stochastic process—the construction of (Z, Σ, P) in Section 8.2—is due to Ionescu-Tulcea.
The proof may be found in Shiryayev (1984, Theorem 2, pp. 247-249), Neveu (1965, sect.
V.1), or Gihman and Skorohod (1974, Theorem 3, pp. 81-82).
Our discussion of stochastic kernels in Section 8.3 also draws heavily on the treatment in the lattermost.
The proof of Theorem 8.9 follows the one in Futia (1982, Theorem 5.2), where a slightly more general version is given.
## 9 Stochastic Dynamic Programming
With the mathematical background in place, we are ready to study dynamic programming models that incorporate stochastic shocks.
We study two specifications of the problem.
The first of these parallels more closely the treatment of the deterministic model in Chapter 4, but the second is more general.
The two approaches can beinformation that will be available in period t.
For t = 1, this information is the sequence of shocks (z_1, …, z_t).
He chooses this sequence of functions to maximize the expected discounted sum of returns, where the expectation is over realizations of the shocks.
To spell this out precisely, we must decide what functions are available to the decision-maker and what probability measures are used to evaluate the returns they generate.
Define the product spaces (Z^t, Σ_t), t = 1, 2,..., and let X = (z_1,...,z_t) ∈ Z^t denote a partial history of shocks in periods 1 through t.
### DEFINITION A
plan is a value τ_0 ∈ X and a sequence of measurable functions τ_t: Z^t → X, t = 1, 2,....
The interpretation is that τ_t(z^t) is the value for x^t that will be chosen in period t if the partial history of shocks observed in periods 1 through t is z^t.
### DEFINITION A
plan τ is feasible from s_0 ∈ S if (1a) τ_0 ∈ Γ(s_0), (1b) τ_t(z^t) ∈ Γ[m_{t-1}(z^{t-1}), z_t], for all z^t ∈ Z^t, t = 1, 2,....
The constraints in (1a) and (1b) are the exact analogue of the feasibility constraints in the deterministic case, but the measurability requirements on the τ's have no counterpart in the deterministic case.
Let Π(s_0) denote the set of plans that are feasible from s_0.
Our first question is, Under what conditions is Π(s_0) nonempty, for all s_0 ∈ S?
In the deterministic case, the set of feasible plans was nonempty if the correspondence Γ was nonempty.
Here we must also ensure that the measurability requirements can be met.
To do this we need the following assumption.
ASSUMPTION 9.1 Γ is nonempty-valued and the graph of Γ is (Σ × ℰ)-measurable.
In addition, Γ has a measurable selection; that is, there exists a measurable function h: S → X such that h(s) ∈ Γ(s), all s ∈ S.
Recall that for the case where X and Z are subsets of Euclidean spaces, Theorem 7.6 provides a sufficient condition for Γ to have a measurable selection.
The following result follows immediately from this assumption.
### LEMMA 9.1
Let (X, ℰ), (Z, Σ), and Γ be given.
Under Assumption 9.1, Π(s_0) is nonempty for all s_0 ∈ S.
**Proof.** Choose a measurable selection h from Γ.
Fix s_0 ∈ S, and define τ by τ_0 = h(s_0), τ_t(z^t) = h[m_{t-1}(z^{t-1}), z_t], for all z^t ∈ Z^t, t = 1,2,....
Clearly τ satisfies (1a) and (1b) and τ_0 is measurable.
That each τ_t = 1, 2,..., is measurable then follows by induction from the fact that compositions of measurable functions are measurable (Exercise 7.31).
Since s ∈ S was arbitrary, the desired result is established.
A plan τ constructed in this way by using the same measurable selection h from Γ in every period t is said to be stationary or Markov, since the action it prescribes for each period t depends only on the state s = [m_{t-1}(z^{t-1}), z_t] in that period.
Nonstationary plans can be constructed by using different measurable selections h_t in each period.
Next, consider how total, discounted, expected returns are calculated for a feasible plan.
Given the transition function Q on (Z, Σ) and the initial state (x_0, z_0) = s_0 ∈ S, define the probability measures μ(z_0): Σ → [0, 1], t = 1,2,..., as we did in Section 8.2.
Recall that the domain of F is the set A, the graph of τ.
Let A = {C ∈ ℝ × X × Z: C ⊂ A} It is straightforward to show that under Assumption 9.1, A is a σ-algebra.
Notice that if F is A-measurable, then by Exercise 7.31, for any s_0 ∈ S and any τ ∈ Π(s_0), F[x_0, τ_{t-1}(z^{t-1}), z_t], z_t] is A-measurable, for t = 1, 2… Hence for the stochastic case the following is the counterpart of Assumption 4.2.
ASSUMPTION 9.2.
F: A→ ℝ is A-measurable, and either (a) or (b) holds, (a) F ≥ 0 or F ≤ 0.
(b) For each (x_0, z_0) = s_0 ∈ S and each plan τ ∈ Π(s_0), F[x_0, τ_{t-1}(z^{t-1}), z_t], z_t] is μ(z_0, ·)-integrable, t = 1, 2… and the limit F[x_0, τ_0, z_0] + lim Σ_{t=1}^n β^{t-1} E[ F[m_{t-1}(z^{t-1}), τ_t(z^t)], z_{t+1}] μ(z_0, dz_{t+1}) n→∞ exists (although it may be plus or minus infinity).
Notice that if (a) holds, then the limit in (b) is well defined.
Assumption 9.2 ensures that, for each s_0 ∈ S, we can define the functions u_n(·, s_0): Π(s_0) → ℝ, n = 0, 1,..., by u_0(τ, s_0) = F[x_0, τ_0, z_0], u_n(τ, s_0) = F[x_0, τ_0, z_0] + Σ_{t=1}^n β^{t-1} E[ F[m_{t-1}(z^{t-1}), τ_t(z^t)], z_{t+1}] μ(z_0, dz_{t+1}).
Thus u_n(τ, s_0) is the sum of expected discounted returns in periods 0 through n from the plan τ if the initial state is s_0.
Assumption 9.2 also ensures that for each s_0 ∈ S we can define u(·, s_0): Π(s_0) → ℝ to be the limit of this series as the horizon recedes: u(τ, s_0) = lim_{n→∞} u_n(τ, s_0).
Thus u(τ, s_0) is the (infinite) sum of expected discounted returns from the plan τ if the initial state is s_0.
Under Assumptions 9.1 and 9.2, the function u(·, s) is well defined on the nonempty set Π(s), for each s ∈ S.
In this case we can define the supremum function v*: S → ℝ by (2) v*(s) = sup_{τ ∈ Π(s)} u(τ, s).
That is, v* is the unique function satisfying the following two conditions: (3) v*(s) ≥ u(τ, s), for all τ ∈ Π(s); (4) v*(s) = lim_{k→∞} u(τ^k, s), for some sequence {τ^k}_{k=1}^∞ in Π(s).
Now consider the functional equation corresponding to the sequence problem in (2): (5) v(x, z) = sup_{y ∈ Γ(x, z)} [F(x, y, z) + β ∫ v(y, z') Q(z, dz')].
If there exists a function v satisfying (5), then we can also define the associated policy correspondence G by (6) G(x, z) = {y ∈ Γ(x, z): v(x, z) = F(x, y, z) + β ∫ v(y, z') Q(z, dz').
If G is nonempty and if there exists a measurable selection from G, then we say that τ is generated by G from s_0 if it is formed in the following way.
Let g_0, g_1, … be a sequence of measurable selections from G, and define τ by τ_0 = g_0(s_0); τ_t(z^t) = g_t[m_{t-1}(z^{t-1}), z_t], for all z^t ∈ Z^t, t = 1,2,....
Since g_t(·) ∈ G(s) ⊂ Γ(s), for all s ∈ S, it is clear that τ satisfies (1a) and (1b); and since each g_t is measurable, it is also clear that τ is measurable (by the argument used in the proof of Lemma 9.1).
Hence a plan τ generated by G from s_0 is feasible from s_0.
Let Assumptions 9.1 and 9.2 hold, so that v* is well defined, and , Consider the relationship between solutions to (2) and to (5) and (6).
For the deterministic case we had two theorems connecting the supremum function v* with solutions v to the functional equation, and two theorems connecting optimal plans (when they exist) with plans generated by the policy correspondence G (when that correspondence is nonempty).
Theorem 4.2 showed that if the total discounted returns from any feasible plan are well defined, then the supremum function v* satisfies the functional equation.
Theorem 4.3 showed, conversely, that a solution v to the functional equation, if it satisfies a certain boundedness condition, is the supremum function.
Theorems 4.4 and 4.5 showed that every optimal plan is generated by G and, conversely, that any plan generated by G and satisfying a boundedness condition is optimal.
For the stochastic case the results concerning the value function are somewhat weaker.
First, there is no analogue to Theorem 4.2.
Even under conditions ensuring that the supremum function v* is well defined, that function may not be measurable.
Hence the integral in the functional equation may not be well defined.
Later in this section we will provide an example due to Blackwell that illustrates this fact.
Similarly, because of measurability requirements it may be difficult to verify that (4) holds except by displaying a plan that attains the supremum.
Thus the stochastic analogue to Theorem 4.3 requires that the policy correspondence G associated with the function v of interest be nonemptyvalued and permit a measurable selection.
Under these assumptions, a plan can be generated from G.
The results in Theorems 4.4 and 4.5 do have close analogues in the stochastic case.
For the stochastic case, then, we have two main results.
The first provides sufficient conditions for a solution v to the functional equation to be the supremum function, and for plans generated by the associated policy correspondence G to attain the supremum.
It is the analogue ofTheorems 4.3 and 4.5 for the deterministic model and uses a similar boundedness assumption.
### THEOREM 9.2
Let \((X, \sigma)\), \((Z, \varepsilon)\), \(Q\), \(T\), \(F\), and \(\beta\) be given.
Let Assumptions 9.1 and 9.2 hold, and let \(v^*\) be defined by (2).
Let \(v\) be a measurable function satisfying the functional equation (5), and such that \[ \lim_{n \to \infty} \int F[\tau_n(z^n), \tau(z^n), z_n] \beta^n \, dQ(z^n) = 0, \] all \(\tau \in \Pi(s_0)\), all \((x_0, z_0) = s_0 \in S\).
Let \(G\) be the correspondence defined by (6), and suppose that \(G\) is nonempty and permits a measurable selection.
Then \(v = v^*\), and any plan \(\tau^*\) generated by \(G\) attains the supremum in (2).
**Proof.** As noted above, under Assumptions 9.1 and 9.2, \(v^*\) is well defined.
Suppose that \(v: X \times Z \rightarrow \mathbb{R}\) satisfies the stated hypotheses.
To show that \(v = v^*\), it suffices to show that \(v\) satisfies (3) and (4).
Choose any \((x_0, z_0) = s_0 \in S\).
Then for any \(\tau \in \Pi(s_0)\), \[ \begin{aligned} v(s_0) &= \sup_{\tau \in \Pi(s_0)} \left[ F(x_0, \tau_0, z_0) + \beta \int_{}^{} v[\tau_1(z_1), z_1] Q(z_0, dz_1) \right] \\ &= F(x_0, \tau_0, z_0) + \beta \int v[\tau_1(z_1), z_1] Q(z_0, dz_1) \\ &= u[\tau(s_0), s_0] + \beta \int \left\{ \sup_{\tau' \in \Pi(\tau_1(z_1), z_1)} \left[ F[\tau_1(z_1), \tau_1'(z_1), z_1] \right. \right. \\ &\qquad\qquad\qquad\left. \left. + \beta \int v[\tau_2'(z_2), z_2] Q(z_1, dz_2) \right] \right\} Q(z_0, dz_1) \\ &= u[\tau(s_0), s_0] + \beta \int \left\{ F[\tau_1(z_1), \tau_1'(z_1), z_1] \right. \\ &\qquad\qquad\qquad\left. + \beta \int v[\tau_2'(z_2), z_2] Q(z_1, dz_2) \right\} Q(z_0, dz_1) \\ &= u[\tau(s_0), s_0] + \beta \int v[\tau_1(z_1), z_1] Q(z_0, dz_1), \end{aligned} \] where the first and fourth lines each use the fact that \(v\) satisfies (5); the second and fifth each use the fact that \(\tau\) is feasible from \(s_0\); the third uses the definitions of \(u\) and \(v^*\); and the sixth uses the definition of \(u\), and uses Exercise 8.8 to justify combining the two integrals into one operation.
It then follows by induction that \[ v(s_0) = u[\tau(s_0), s_0] + \beta^n \int v[\tau_n(z^n), z_n] \beta^n \, dQ(z^n), \] \(n = 1, 2, 3, \dots\) Taking the limit as \(n \rightarrow \infty\) and using (7), we conclude that \(v(s_0) = u[\tau(s_0), s_0]\).
Since \(\tau \in \Pi(s_0)\) was arbitrary, it follows that \(v\) satisfies (3).
To show that \(v\) also satisfies (4), let \(\tau^*\) be any plan generated by \(G\) from \(s_0\); under the stated hypotheses for \(G\) there is at least one such plan.
Then the argument above can be repeated with equality at every step.
Hence (4) holds for the sequence \(\tau = \tau^*\), \(k = 1, 2, \dots\).
Since \(s_0 \in S\) was arbitrary, this establishes that \(v = v^*\). □ Our next main result, Theorem 9.4, is a partial converse to Theorem 9.2.
It states that under somewhat stronger hypotheses a plan is optimal only if it is generated (a.e.) by \(G\).
But before proving this theorem we need one more definition and one preliminary result.
Given any \(s_0 \in S\), \(\tau \in \Pi(s_0)\), and \(z_0 \in Z\), define the continuation of \(\tau\) following \(z_0\), call it \(C(\tau, z_0)\), as follows: (8a) \(C_0(\tau, z_0) = \tau_0(z_0)\), (8b) \(C_t(\tau, z_0) = \tau_t(z^t)\), all \(z^t \in Z^t\), \(t = 1, 2, \dots\).
Thus, each function \(C_t(\cdot; \tau, z_0): Z^t \rightarrow X\), \(t = 0, 1, 2, \dots\), is simply the \(z^t\)-section of the function \(\tau_t\).
Hence by Theorem 7.14 these functions are measurable.
Moreover, it is clear that they satisfy the feasibility constraints in (1a) and (1b).
Hence for each \(z^t \in Z^t\), \(C(\tau, z_1)\) is a feasible plan from \((\tau_1(z_1), z_1)\).
Exercise 9.1 Show that if \(\tau \in \Pi(s_0)\), then \(x[C(\tau, z_1), (\tau_0, z_1)]\) is a measurable function of \(z_1\). [Hint: Use Theorem 7.14 and Exercise 7.31.] Our next result establishes that \(u\), evaluated at a plan and its continuations, satisfies a recursive relation analogous to the one in the functional equation.
The lemma requires the following strengthening of Assumption 9.2.
ASSUMPTION 9.3 If \(F\) takes on both signs, there is a collection of nonnegative, measurable functions \(L_t: S \rightarrow \mathbb{R}\), \(t = 0, 1, \dots\), such that for all \(\tau \in \Pi(s_0)\) and all \(s_0 \in S\) \[ |F(x_0, \tau_0, z_0)| \leq L_0(s_0), \] \[ |F[\tau_t(z^t), \tau_{t+1}(z^{t+1}), z_{t+1}]| \leq L_t(s_0), \text{ all } z^{t+1} \in Z^{t+1}, t = 1, 2, \dots \] and \[ \sum_{t=0}^{\infty} \beta^t L_t(s_0) < \infty. \]
### LEMMA 9.3
Let \((X, \sigma)\), \((Z, \varepsilon)\), \(Q\), \(T\), \(F\), and \(\beta\) be given.
Suppose that Assumptions 9.1–9.3 hold.
Then for any \((x_0, z_0) = s_0 \in S\) and any \(\tau \in \Pi(s_0)\), (9) \(u(\tau, s_0) = F(x_0, \tau_0, z_0) + \beta \int u[C(\tau, z_1), (\tau_0, z_1)] Q(z_0, dz_1)\), where for each \(z_1 \in Z\), \(C(\tau, z_1)\) is the continuation of \(\tau\) following \(x_1\).
**Proof.** Let \((x_0, z_0) = s_0 \in S\) and \(\tau \in \Pi(s_0)\) be given, and suppose that \(F \geq 0\).
Under Assumption 9.2, \(u(\tau, s_0)\) is well defined, and (10) \(u(\tau, s_0) = F(x_0, \tau_0, z_0) + \lim_{n \to \infty} \sum_{t=1}^{n} \int \beta^t F[\tau_t(z^t), \tau_{t+1}(z^{t+1}), z_{t+1}] Q(z^t, dz_{t+1})\).
For the second term on the right we have \[ \begin{aligned} \lim_{n \to \infty} \sum_{t=1}^{n} \int \beta^t F[\tau_t(z^t), \tau_{t+1}(z^{t+1}), z_{t+1}] Q(z^t, dz_{t+1}) &= \lim_{n \to \infty} \int \left\{ \sum_{t=1}^{n} \beta^t F[\tau_t(z^t), \tau_{t+1}(z^{t+1}), z_{t+1}] \right\} Q(z_0, dz^n) \\ &= \int \left\{ \lim_{n \to \infty} \sum_{t=1}^{n} \beta^t F[\tau_t(z^t), \tau_{t+1}(z^{t+1}), z_{t+1}] \right\} Q(z_0, dz^n) \\ &= \int \left\{ \beta F[\tau_0(z_0), \tau_1(z_1), z_1] \right. \\ &\qquad \left. + \beta \int \left\{ \sum_{t=2}^{n} \beta^{t-1} F[\tau_t(z^t), \tau_{t+1}(z^{t+1}), z_{t+1}] \right\} Q(z_1, dz_2) \right\} Q(z_0, dz_1) \\ &= \int \beta \left\{ F[\tau_0(z_0), \tau_1(z_1), z_1] \right. \\ &\qquad \left. + \beta \int u[C(\tau, z_2), (\tau_1(z_1), z_2)] Q(z_1, dz_2) \right\} Q(z_0, dz_1) \\ &\quad + \cdots \\ &\quad + \int \cdots \int \left\{ \beta^n \sum_{t=n+1}^{\infty} \beta^{t-n} F[\tau_t(z^t), \tau_{t+1}(z^{t+1}), z_{t+1}] \right\} \\ &\qquad \times Q(z^n, dz^{n+1}) \right\} Q(z_0, dz^n) \\ &= \int \beta \left\{ F[\tau_0(z_0), \tau_1(z_1), z_1] \right. \\ &\qquad \left. + \beta \int u[C(\tau, z_2), (\tau_1(z_1), z_2)] Q(z_1, dz_2) \right\} Q(z_0, dz_1), \end{aligned} \] where the first line uses Exercise 8.8 to justify breaking up the integral over \(Z^t\) into two parts, the second uses the Monotone Convergence Theorem (Theorem 7.8) to exchange the order of limit and integration (cf.
Exercise 7.22), the third uses (8a) and (8b), and the last again uses the definition of \(u\).
Substituting into (10) then gives the desired result.
If \(F \leq 0\), the argument above can be applied to the function \(-F\).
If \(F\) takes on both signs, then Assumption 9.3 holds.
Define the sequence of functions \(H_n: Z \rightarrow \mathbb{R}\) by \[ \begin{aligned} H_1(z_1) &= \beta F[\tau_0(z_0), \tau_1(z_1), z_1] \\ H_n(z_1) &= \beta \left\{ F[\tau_0(z_0), \tau_1(z_1), z_1] \right. \\ &\qquad \left. + \beta \int \left\{ \sum_{t=2}^{n} \beta^{t-2} F[\tau_t(z^t), \tau_{t+1}(z^{t+1}), z_{t+1}] \right\} Q(z_1, dz_2) \right\}, \quad n = 2, 3, \dots \end{aligned} \] Assumption 9.3 implies that there exists a constant \(L = \sum_{t=0}^{\infty} \beta^t L_t(s_0)\) with the property that \(|H_n(z_1)| \leq L\), all \(z_1 \in Z\), all \(n\).
Hence the argument above applies, with the Lebesgue Dominated Convergence Theorem (Theorem 7.10) justifying the change in the order of limit and integration. □ The crucial steps in this proof are the use of Exercise 8.8 to break up the integration over \(Z^t\) into two steps, and the application of the Monotone Convergence Theorem or the Lebesgue Dominated Convergence Theorem to justify changing the order of limit and integration.
Notice that it is the latter step that requires the assumption that either \(F\) takes on only one sign or else Assumption 9.3 holds.
Clearly there are many variations on the latter assumption—variations involving more complicated bounds on \(F\)—that could also be used to justify this step.
With Lemma 9.3 in hand we are ready to prove the next main result of this section: if Lemma 9.3 applies, then any plan \(\tau^*\) that attains the supremum in (2) is generated (a.e.) by \(G\).
### THEOREM 9.4
Let \((X, \sigma)\), \((Z, \varepsilon)\), \(Q\), \(T\), \(F\), and \(\beta\) be given.
Let Assumptions 9.1–9.3 hold, and define \(v^*\) by (2).
Assume that \(v^*\) is measurable and satisfies (5), and define the correspondence \(G\) by (6).
Assume that \(G\) is nonempty and permits a measurable selection.
Let \((x_0, z_0) = s_0 \in S\), and let \(\tau^* \in \Pi(s_0)\) be a plan that attains the supremum in (2) for initial condition \(s_0\).
Then there exists a plan \(\tau^\circ\) generated by \(G\) from \(s_0\) such that \[ \tau_0 = \tau_0^*, \quad \text{and} \] \[ \tau_t(z^t) = \tau_t^*(z^t), \quad Q\text{-a.e.}, \quad t = 1, 2, \dots \]
**Proof.** Notice that under the stated hypotheses, Theorem 9.2 and Lemma 9.3 apply.
Let \(\tau^*\) be a plan that attains the supremum in (2).
Since \(G\) is defined by (6), it is sufficient to show that (11a) \(v^*(s_0) = F(x_0, \tau_0^*, z_0) + \beta \int v^and since 7& E II(s₀) and τ = 7%, (13) implies that [ uicenr®, 2), (s, z₀)I_QCo der) = | ulcers, a), (wt, u)I_QGo, da).
By Exercise 7.24, these two inequalities together imply that X[C(ma 21), ( 帝 21)] = x[C(mh 2), ( z)], Q(zo, )]-a.e.
It then follows from (14) that (15) v¥(r₀, 21) = u[C(a*, 21), (7, z)], Q(zo, )]-a.e.
Hence v*(s₀) = u(a*, s₀) = F(s₀, a*, z₀) + B ∫ u[C(a*, z), (τ, a)]Q(zo, da) = F(t, wh, z₀) + B ∫ ord, z₀)Q_Co, da), where the second line uses Lemma 9.3, and the last uses (15) and Exercise 7.24.
Hence (11a) holds, as was to be shown.
Use an analogous argument, with (15) in place of (12) as the starting point, to show that (11b) holds for t = 1, and continue by induction.
The following exercise treats the case where F is bounded above or below, but not by zero, and Assumptions 9.2b and 9.3 fail.
The exercise shows that if B < 1, then this case can be treated by an argument analogous to the one used if F takes on only one sign.
Exercise 9.2 Suppose that F is s-measurable, F is uniformly bounded above or below (not necessarily by zero), and B < 1. a.
Show that w(-, s₀): II(s₀) → R is well defined.
Show that if in addition Assumption 9.1 holds, then v* is well defined. b.
Show that Theorem 9.2, Lemma 9.3, and Theorem 9.4 still hold.
These are the main results for the first formulation discussed in the introduction.
Next we turn to a brief discussion of what can happen if the hypotheses of Theorem 9.2 fail.
The main problem is that v* may not be a measurable function, even if T and Q are well behaved and F is measurable.
If this happens, the integral in the functional equation is not defined for v = v*, so v* does not satisfy the functional equation.
To see that v* may be nonmeasurable, consider the following example, taken from Blackwell (1965).
Let X = Z = [0, 1], with the Borel sets B and &, and let T() = [0, 1], all s ∈ S.
Thus Assumption 9.1 is satisfied.
Let the transition function be Q(z′|C) = {1 if z′ ∈ C {0 if z′ ∉ C, all z′ ∈ Z, all C ∈ B.
Hence the sequence of shocks (z₀, z₁ …) is a constant sequence with probability one.
Let E ⊂ X × Z = [0, 1]² be a Borel-measurable set with the following property: the projection of E onto Z, the set Proj_z E = {z ∈ Z: (y, z) ∈ E, for some y ∈ X}, is not Borel-measurable.
(Unfortunately, sets E of this sort exist; see Behnke et al. 1974, pp. 465–474.) Define the return function F by F(y, z) = {1 if (y, z) ∈ E {0 if (y, z) ∉ E, and let 0 < B < 1; then clearly Assumption 9.2 holds.
Moreover, for any initial state s₀, the optimum is attained by a feasible plan of the form π_t(z^t) = ξ, all z′ ∈ Z, t = 1, 2, ..., where ξ is chosen so that (ξ, z₀) ∈ E, if any such ξ exists.
That is, the optimum can always be attained by a policy that is constant over time.
Since Proj_z E is not a Borel set, however, the value function v* is not measurable.
To see where the problem arises, define a global plan to be one that is defined for all initial states.
That is, a global plan P is a sequence of measurable functions P_t: S × Z^t → X, t = 0, 1, ....
For any global plan P and any s ∈ S, let P^s denote the s-section of P; clearly any such section is a plan according to the original definition.
Call a global plan feasible if for each s ∈ S, P^s is feasible from s.
It is straightforward to show that, if P is a feasible global plan and if Assumption 9.2 holds, then x(P·, s) is a measurable function of s.
Now recall that if v* is well defined it is the unique function satisfying (3) and (4).
Suppose that this is the case, and for each s ∈ S, choose a sequence {ξ_k(s)}_{k=1}^∞ satisfying (4).
These sequences can be used in the obvious way to define a sequence of functions {P^k}: P^k_t(z^t) = ξ_k(z_t), all s ∈ S; z^t ∈ Z^t; t = 0, 1, ...; k = 1, 2, ....
Now the s-section of each function P^k is simply π_k and hence is a feasible plan from s ∈ S.
Hence we can define the functions w_k: S → R by w_k(s) = u(π_k, s) = u(ξ_k, s), all s ∈ S, k = 1, 2, ....
Taking the limit as k → ∞, we find that lim_{k→∞} w_k(s) = lim_{k→∞} u(ξ_k, s), all s ∈ S.
If each of the functions P^k is a global plan—that is, if it satisfies the measurability requirements—then each of the functions w_k is measurable.
In this case the pointwise limit of these functions, v*, is also measurable.
However, the assumptions imposed thus far do not ensure that the P^k’s satisfy the measurability requirements of a global plan.
In the remaining sections of this chapter, we will impose continuity restrictions on the return function F and on the correspondence describing the feasibility constraints that are sufficient to ensure that v* is continuous and that optimal policies exist.
Before doing that, however, in the rest of this section we will discuss the relationship between solutions to sequence problems and to the corresponding functional equations for the second type of situation described in the introduction.
The arguments are very similar to the ones above, and we will leave most of them as exercises.
Let (X, B), (Z, B), (S, B), Q, and δ be as specified before.
In addition, let (Y, Y) be a measurable space.
The set Y is the set of possible actions the decision-maker may take.
In each period t the decision-maker chooses an action from a specified subset of feasible alternatives in the set Y.
The constraints on these choices are described by a correspondence T: X × Z → Y; that is, T(x, z) is the set of feasible actions if the current state is (x, z).
Define A to be the graph of T: A = {(x, y, z) ∈ X × Y × Z: y ∈ T(x, z)}.
The one-period return function F is defined on this set, F: A → R; that is, F(x, y, z) is the current-period return if the current state is (x, z) and the action y ∈ T(x, z) is chosen.
We must also describe the evolution of the variable x.
Let D = {(x, y) ∈ X × Y: y ∈ T(x, z), for some z ∈ Z}, and let b: D × Z → X be the law of motion for the state variable.
That is, x' = b(x, y, z') is the next period’s value for the endogenous state variable, if x is the current value, the action y is taken, and z’ is the value of next period’s exogenous shock.
Thus, the givens for this problem are (X, B), (Y, Y), (Z, B), Q, T, F, B, and b.
Viewed in sequence form the problem is as follows.
In period t = 0, with s₀ known, the decision-maker chooses an action y₀ and a sequence of functions describing actions to be taken in later periods.
As before, the decision to be carried out in period t can depend upon the information available in that period, the partial history of shocks z^t.
### DEFINITION A
plan is a sequence of functions π = {π_t}_{t=0}^∞, where π_t: Z^t → Y is B^t-measurable, t = 1, 2, ....
A plan π is feasible from s₀ if in addition it satisfies (1a') y₀ ∈ T(x₀, z₀); (1b') π_t(z^t) ∈ T[x_t(z^t), z_t], all z^t ∈ Z^t, t = 1, 2, ..., where the functions x_t: Z^t → X, t = 1, 2, ... are defined recursively by (16a) x₁(z₁) = b(x₀, y₀, z₁), all z₁ ∈ Z; (16b) x_t(z^t) = b[x_{t-1}(z^{t-1}), π_{t-1}(z^{t-1}), z_t], all z^t ∈ Z^t, t = 2, 3, ....
Thus, a plan consists of a sequence of functions describing the action y in each period t as a measurable function of the history of shocks z in periods 1 through t.
A feasible plan is one that in addition satisfies the feasibility constraints described by T, given the law of motion b.
For each s₀ ∈ S, let II(s₀) denote the set of all feasible plans from s₀; and for any plan π ∈ II(s₀), define xπ = {x_t} as in (16).
Two conditions are needed to ensure that II(s) is nonempty.
One is exactly analogous to the condition in Assumption 9.1; the other is a restriction on the law of motion b.
ASSUMPTION 9.1’ T is nonempty-valued; the graph of T is (B × Y × B)measurable; and T has a measurable selection.
That is, there exists a measurable function h: B → Y such that h(s) ∈ T(s), all s ∈ S.
In addition, the function b: D × Z → X is measurable.
Exercise 9.3 Show that under Assumption 9.1’, II(s) is nonempty, all s ∈ S.sufficiently large.
Hence as n → ∞ the first term in (3) vanishes and Q(z, ) = Q(z, ) is a fixed probability measure.
Moreover, the functions h_n(z') = f(z', ) - f(z', ), n = 1, 2,..., are all measurable; the sequence of functions {h_n} converges pointwise to the zero function; and each term in the sequence is bounded above by the constant function 1.
Hence by the Lebesgue Dominated Convergence Theorem (Theorem 7.10), lim ∫ h_n(z') Q(z, dz') = ∫ lim h_n(z') Q(z, dz') = 0, and the second term in (3) also vanishes.
Alternatively, suppose that Z is a compact set in ℝ^k.
The fact that Q has the Feller property implies that the first term in (3) vanishes as n → ∞.
Moreover, since z_n → z, it follows that there exists a compact set D ⊂ X such that z_n ∈ D, all n and z ∈ D.
Since f is continuous, it is uniformly continuous on the compact set D × Z.
That is, for every ε > 0, there exists N = N(ε) such that |f(y, z') - f(y, z_n)| < ε, all n > N, all z' ∈ Z.
Hence the second term in (3) vanishes as n → ∞.
That weak monotonicity in y is preserved is obvious.
To see that strict monotonicity is preserved, choose y, y' ∈ X such that y ≠ y'.
Then f(y, z) < f(y', z) for all z ∈ Z.
The desired conclusion then follows from Exercises 7.18 and 7.24.
To see that concavity is preserved, choose y, y' ∈ X, with y ≠ y', and for any θ ∈ (0, 1), let y_θ = θy + (1 - θ)y'.
If f is concave in y, then (Mf y)(θy + (1 - θ)y', z) = ∫ f(θy + (1 - θ)y', z') Q(z, dz') (4) > θ ∫ f(y, z') Q(z, dz') + (1 - θ) ∫ f(y', z') Q(z, dz') = θ (Mf)(y, z) + (1 - θ) (Mf)(y', z), all z ∈ Z, all θ ∈ (0, 1).
If f is strictly concave in y, then f(θy + (1 - θ)y', z') > θ f(y, z') + (1 - θ) f(y', z'), all z' ∈ Z, all θ ∈ (0, 1), and it follows from Exercises 7.18 and 7.24 that the inequality in (4) is also strict. □ **9.2 Bounded Returns** In some situations the requirement that the set Z ⊂ ℝ^k be compact is very unattractive.
In fact, it can be dispensed with; but the proof of Lemma 9.5 becomes more complicated.
We defer this proof until Section 12.6, when the required mathematical tools will have been developed.
With Lemma 9.5 in hand, it is straightforward to show that all of the results proved for deterministic dynamic programs have analogues when stochastic shocks are added.
The next two assumptions are analogues to those used throughout Section 4.2. **ASSUMPTION 9.6** The correspondence T: X × Z ⇉ X is nonempty, compact-valued, and continuous. **ASSUMPTION 9.7** The function F: A → ℝ is bounded and continuous, and β ∈ (0, 1).
If Z is a countable set, we interpret Assumption 9.6 to mean that for each fixed z ∈ Z, the correspondence T(·, z): X ⇉ X is nonempty, compact-valued, and continuous.
Similarly, in this case Assumption 9.7 means that for each fixed z ∈ Z, the function F(·, ·, z): A_z → ℝ (the z-section of F) is continuous.
The following exercise shows that under these assumptions, Theorems 9.2 and 9.4 hold. **Exercise 9.6** Show that under Assumptions 9.4—9.7, Assumptions 9.1—9.3 are satisfied.
(Hint: Use the Measurable Selection Theorem (Theorem 7.6).] Under these same assumptions, we have the following basic result. **THEOREM 9.6** Let (X, 𝒳), (Z, 𝒵), Q, T, F and β satisfy Assumptions 9.4—9.7, and define the operator T on C(S) by (5) (Tf)(x, z) = sup_{y ∈ T(x, z)} [F(x, y, z) + β ∫ f(y, z') Q(z, dz')].
Then T: C(S) → C(S); T has a unique fixed point v in C(S) and for any u₀ ∈ C(S), ‖Tu₀ - v‖ ≤ β^n ‖u₀ - v‖, n = 1, 2,....
Moreover, the correspondence G: S ⇉ X defined by (6) G(x, z) = {y ∈ T(x, z): v(x, z) = F(x, y, z) + β ∫ v(y, z') Q(z, dz')} is nonempty, compact-valued, and u.h.c. **Proof.** Fix f ∈ C(S).
Then it follows from Lemma 9.5 that (Mf)(y, z) = ∫ f(y, z') Q(z, dz') is a bounded continuous function of (y, z).
Moreover, since Q(z, ) is a probability measure, M(f + c) = Mf + c, for any constant function c.
Hence the proof of Theorem 4.6 applies without change. □ To obtain sharper characterizations of the unique fixed point of T, more structure is needed.
We examine in turn the consequences of monotonicity, concavity, and differentiability. **ASSUMPTION 9.8** For each (y, z) ∈ X × Z, F(·, y, z): A_y → ℝ is strictly increasing. **ASSUMPTION 9.9** For each z ∈ Z, T(·, z): X ⇉ X is increasing in the sense that x ≤ x' implies T(x, z) ⊂ T(x', z). **THEOREM 9.7** Let (X, 𝒳), (Z, 𝒵), Q, T, F and β satisfy Assumptions 9.4—9.9, and let v be the unique fixed point of the operator T in (5).
Then for each z ∈ Z, v(·, z): X → ℝ is strictly increasing. **Proof.** Let C'(S) ⊂ C(S) be the set of bounded continuous functions f on S that are nondecreasing in their first ℓ arguments, and let C"(S) ⊂ C'(S) be the set of functions that are strictly increasing in those arguments.
Since C'(S) is a closed subspace of the complete metric space C(S), by Corollary 1 to the Contraction Mapping Theorem (Theorem 3.2), it is sufficient to show that T[C'(S)] ⊂ C'(S).
Under Assumptions 9.8 and 9.9, Lemma 9.5 ensures that this is so. □ Next we consider concavity.
Assumption 9.10 is a concavity restriction on F, and Assumption 9.11 is a convexity restriction on T. **ASSUMPTION 9.10** For each z ∈ Z, F(·, ·, z): A_z → ℝ satisfies F(θ(x, y) + (1 - θ)(x', y'), z) ≥ θ F(x, y, z) + (1 - θ) F(x', y', z), all θ ∈ (0, 1), and all (x, y), (x', y') ∈ A_z; and the inequality is strict if x ≠ x'. **ASSUMPTION 9.11** For all z ∈ Z and all x, x' ∈ X, y ∈ T(x, z) and y' ∈ T(x', z) implies θy + (1 - θ)y' ∈ T[θx + (1 - θ)x', z], all θ ∈ [0, 1].
Since the set X is convex, Assumption 9.11 is equivalent to assuming that for each z ∈ Z, the set T(x, z) is convex.
In particular, Assumption 9.11 implies that T(x) is a convex set for each x ∈ X, and that there are no increasing returns. **THEOREM 9.8** Let (X, 𝒳), (Z, 𝒵), Q, T, F, and β satisfy Assumptions 9.4—9.7 and 9.10—9.11; let v be the unique fixed point of the operator T in (5); and let G be the correspondence defined by (6).
Then for each z ∈ Z, v(·, z): X → ℝ is strictly concave and G(·, z): X → X is a continuous (single-valued) function. **Proof.** Let C'(S) ⊂ C(S) be the set of bounded continuous functions on S that are weakly concave jointly in their first ℓ arguments, and let C"(S) ⊂ C'(S) be the subset consisting of functions that are strictly concave jointly in those arguments.
Since C'(S) is a closed subspace of the complete metric space C(S), by Corollary 1 to the Contraction Mapping Theorem (Theorem 3.2), it is sufficient to show that T[C'(S)] ⊂ C"(S).
Under Assumptions 9.10 and 9.11, Lemma 9.5 ensures that this is so. □ As it does in the deterministic case, concavity ensures that the sequence of approximate policy functions {g_n} converges to the optimal policy function g. **THEOREM 9.9** Let (X, 𝒳), (Z, 𝒵), Q, T, F, and β satisfy Assumptions 9.4—9.7 and 9.10—9.11; let C'(S) ⊂ C(S) be the set of bounded continuous functions that are weakly concave jointly in their first ℓ arguments; let v ∈ C'(S) be the unique fixed point of the operator T in (5); and let g = G be the (single-valued) function defined by (6).
Let v₀ ∈ C'(S), and define {(v_n, g_n)} by v_n = Tv_{n-1}, and g_n(x, z) = argmax_{y ∈ T(x, z)} [F(x, y, z) + β ∫ v_{n-1}(y, z') Q(z, dz')], n = 1, 2,....
Then g_n → g pointwise.
If X and Z are both compact, then the convergence is uniform. **Proof.** Let C"(S) ⊂ C'(S) be as defined in the proof of Theorem 9.8; as shown there T[C'(S)] ⊂ C"(S) and v ∈ C"(S).
Let v₀ ∈ C'(S), and define the functions {f_n} and f by f_n(s, y) = F(x, y, z) + β ∫ v_{n-1}(y, z') Q(z, dz'), n = 1, 2,..., and f(s, y) = F(x, y, z) + β ∫ v(y, z') Q(z, dz').
Since v₀ ∈ C'(S), each function v_n, n = 1, 2,..., is in C"(S), as is v.
Hence for any s = (x, z) ∈ S = X × Z, the functions {f_n(s, ·)} and f(s, ·) are all strictly concave in y.
Therefore Theorem 3.8 applies. □ For concave problems with interior solutions, the differentiability of the value function can also be established. **ASSUMPTION 9.12** For each fixed z ∈ Z, F(·, ·, z) is continuously differentiable in (x, y) on the interior of A_z. **THEOREM 9.10** Let (X, 𝒳), (Z, 𝒵), Q, T, F, and β satisfy Assumptions 9.4—9.7 and 9.12.
Let v be the unique fixed point of the operator T in (5), and let g = G be the (single-valued) function defined by (6).
Then v is continuously differentiable in (x, y) on the interior of S, and9.7 and 9.10—9.12; let \( v \in C'(S) \) be the unique fixed point of the operator \( T \) in (5), and let \( g = G \) be the function defined by (6).
If \( x_0 \in \text{int} X \) and \( g(x_0, z_0) \in \text{int} T(x_0, z_0) \), then \( v(\cdot, z_0) \) is continuously differentiable in \( x \) at \( x_0 \), with derivatives given by \( v_i(x_0, z_0) = F_i[x_0, g(x_0, z_0), z_0] \), \( i = 1, \dots, l \).
**Proof.** Let \( x_0 \in \text{int} X \) and \( g(x_0, z_0) \in \text{int} T(x_0, z_0) \).
Then there is some open neighborhood \( D \) of \( x_0 \) such that \( g(x, z_0) \in \text{int} T(x, z_0) \), all \( x \in D \).
Hence we can define \( W: D \to \mathbb{R} \) by \[ W(x) = F[x, g(x, z_0), z_0] + B \int_S v[g(x, z_0), z'] Q(z_0, dz'). \] Clearly \( W \) is concave and continuously differentiable on \( D \) and \( W(x) = v(x, z_0) \), all \( x \in D \), with equality at \( x_0 \).
Hence Theorem 4.10 applies, establishing the desired result. \(\square\) In some applications it is reasonable to expect that the value function is monotone in \( z \) as well as in \( x \).
Clearly this requires that \( Z \) be a set for which monotonicity is well defined; thus, if \( Z \) is a countable set, we will assume that \( Z = \{1, 2, \dots\} \).
We will also need restrictions on \( F \) and \( T \) analogous to Assumptions 9.8 and 9.9, and an additional restriction on the transition function \( Q \).
ASSUMPTION 9.13 For each \( (x, y) \in X \times Y \), \( F(x, y, \cdot): Z \to \mathbb{R} \) is strictly increasing.
ASSUMPTION 9.14 For each \( x \in X \), \( T(x, \cdot) \) is increasing in the sense that \( z \leq z' \) implies \( T(x, z) \subset T(x, z') \).
ASSUMPTION 9.15 \( Q \) is monotone; that is, if \( f: Z \to \mathbb{R} \) is nondecreasing, then the function \( (Mf)(z) = \int_Z f(z') Q(z, dz') \) is also nondecreasing.
### THEOREM 9.11
Let \( (X, \mathcal{X}) \), \( (Z, \mathcal{Z}) \), \( Q \), \( T \), \( F \), and \( B \) satisfy Assumptions 9.4— 9.7 and 9.13—9.15; and let \( v \in C(S) \) be the unique fixed point of the operator \( T \) in (5).
Then for each \( x \in X \), \( v(x, \cdot) \) is strictly increasing.
**Proof.** Let \( C'(S) \subset C(S) \) be the set of bounded continuous functions on \( X \times Z \) that are nondecreasing in \( z \), and let \( C''(S) \subset C'(S) \) be the subset consisting of functions that are strictly increasing in \( z \).
Since \( C'(S) \) is a closed subspace of the complete metric space \( C(S) \), by Corollary 1 to the Contraction Mapping Theorem, it is sufficient to show that \( T[C'(S)] \subset C''(S) \).
Fix \( x \in X \); suppose that \( f(x, \cdot): Z \to \mathbb{R} \) is nondecreasing; and choose \( z_1 < z_2 \).
Let \( y_1 \in T(x, z_1) \) attain the maximum in (5) for \( z = z_1 \).
Then \[ (Tf)(x, z_1) = F(x, y_1, z_1) + B \int_S f(y_1, z') Q(z_1, dz') \] \[ < F(x, y_1, z_2) + B \int_S f(y_1, z') Q(z_2, dz') \] \[ \leq \max_{y \in T(x, z_2)} \left[ F(x, y, z_2) + B \int_S f(y, z') Q(z_2, dz') \right] \] \[ = (Tf)(x, z_2), \] where the second line uses Assumptions 9.13 and 9.15 and the third uses Assumption 9.14.
Hence \( (Tf)(x, \cdot) \) is strictly increasing, as was to be shown. \(\square\) In the remainder of this section we show that the results above all have close parallels for the case where the functional equation has the form in (2).
Let \( (X, \mathcal{X}) \), \( (Z, \mathcal{Z}) \), \( (S, \mathcal{S}) \), \( Q \), and \( B \) be as specified above.
In addition let \( (Y, \mathcal{Y}) \) be a measurable space of actions available to the decision-maker; let \( T: X \times Z \rightrightarrows Y \) be a correspondence describing the feasibility constraints; let \( A \) be the graph of \( T \); let \( F: A \to \mathbb{R} \) be the one-period return function; let \[ D = \{(x, y) \in X \times Y : y \in T(x, z) \text{ for some } z \in Z\}; \] and let \( \phi: D \times Z \to X \) be the law of motion for \( x \).
To characterize solutions to the functional equation (2), we are interested in the operator \( T \) defined by \[ (Tf)(x, z) = \sup_{y \in T(x, z)} \left[ F(x, y, z) + B \int_S f(\phi(x, y, z'), z') Q(z, dz') \right]. \] Clearly we must retain Assumptions 9.4 and 9.5.
We also need to restrict the set of feasible actions \( Y \) and to place a continuity assumption on the law of motion \( \phi \).
ASSUMPTION 9.16 \( Y \) is a convex Borel set in \( \mathbb{R}^k \) with its Borel subsets \( \mathcal{Y} \).
ASSUMPTION 9.17 \( \phi: D \times Z \to X \) is continuous.
If \( Z \) is a countable set, then we interpret Assumption 9.17 to mean that for each \( z \in Z \), the \( z \)-section of \( \phi \), the function \( \phi(\cdot, \cdot, z): D \to X \) is continuous.
With these additional assumptions, we have the following parallel to Lemma 9.5.
### LEMMA 9.18
Let \( (X, \mathcal{X}) \), \( (Y, \mathcal{Y}) \), \( (Z, \mathcal{Z}) \), \( Q \), and \( \phi \) satisfy Assumptions 9.4, 9.5, 9.16, and 9.17.
Then for any continuous function \( f: X \times Z \to \mathbb{R} \), the function \( h: D \times Z \to \mathbb{R} \) defined by \[ h(x, y, z) = \int_S f(\phi(x, y, z'), z') Q(z, dz') \] is also continuous.
**Proof.** Let \( u = (x, y) \) and define \( \psi(u, z') = f(\phi(u, z'), z') \); since \( f \) and \( \phi \) are continuous, so is \( \psi \).
It then follows from Lemma 9.5 that \[ h(u, z) = \int_S \psi(u, z') Q(z, dz') \] is continuous. \(\square\) With this result in hand, it is straightforward to mimic the results in Exercise 9.6 and in Theorems 9.6—9.11; the required steps are presented in the following exercise.
Note that the range of \( T \) is now \( Y \), so \( A \) is now a subset of \( X \times Y \times Z \).
Rather than restate Assumptions 9.6—9.14, however, we merely note that the appropriate modifications must be made.
Exercise 9.7 a.
Let \( (X, \mathcal{X}) \), \( (Y, \mathcal{Y}) \), \( (Z, \mathcal{Z}) \), \( Q \), \( T \), \( F \), \( \phi \), and \( B \) satisfy Assumptions 9.4—9.7 and 9.16—9.17.
Show that Assumptions 9.1— 9.3 hold. b.
Assume the assumptions in part (a) hold, and let \( T \) be the operator defined in (7).
Show that \( T: C(S) \to C(S) \); that \( T \) has a unique fixed point \( v \in C(S) \); and that for any \( v_0 \in C(S) \), \( T^n v_0 \) converges to \( v \) and \[ \|T^n v_0 - v\| \leq B^n \|v_0 - v\|, \quad n = 1, 2, \dots. \] Also show that the correspondence \( G: X \times Z \rightrightarrows Y \) defined by \[ G(x, z) = \{y \in T(x, z) : v(x, z) = F(x, y, z) + B \int_S v(\phi(x, y, z'), z') Q(z, dz')\} \] is nonempty, compact-valued, and u.h.c. c.
Show that if, in addition, Assumptions 9.8 and 9.9 hold and \( \phi \) is nondecreasing in each of its first \( l \) arguments, then \( v \) is strictly increasing in each of its first \( l \) arguments. d.
Suppose that, in addition to the assumptions in part (a), Assumptions 9.10 and 9.11 hold and that, for each \( z' \in Z \), the function \( \phi(\cdot, \cdot, z') \) is concave.
Show that \( v \) is strictly concave jointly in its first \( l \) arguments and that \( G \) is a continuous (single-valued) function. e.
Show that under the assumptions in part (d) the sequence of policy functions \( \{g_n\} \) defined as in Theorem 9.9 converges pointwise to the optimal policy function \( g \); show that if \( X \times Z \) is compact the convergence is uniform. f.
Let the assumptions in part (d) hold, let Assumption 9.12 hold, and assume that the law of motion \( \phi(y, z') \) does not depend on \( x \).
Suppose that \( (x_0, z_0) \in \text{int}(X \times Z) \) and \( g(x_0, z_0) \in \text{int} T(x_0, z_0) \).
Show that \( v(\cdot, z_0) \) is differentiable in \( x \) at \( x_0 \) and that \( v_i(x_0, z_0) = F_i[x_0, g(x_0, z_0), z_0] \), \( i = 1, \dots, l \). g.
Suppose that, in addition to the assumptions in part (a), Assumptions 9.13—9.15 hold.
Show that \( v(x, \cdot) \) is strictly increasing in \( z \). 9.3 Constant Returns to Scale In Section 4.3 we noted that dynamic programs with constant returns to scale are often of economic interest but are, obviously, inconsistent with the assumption of bounded returns.
We saw there, however, that for the deterministic model the arguments used in the bounded-returns case could be modified to fit the case of constant returns to scale.
The same is true for the stochastic model, and the adaptation is completely analogous.
We outline the argument in this section, leaving the main results as exercises.
As in the last section, we take as given \( (X, \mathcal{X}) \), \( (Z, \mathcal{Z}) \), \( Q \), \( T \), \( F \), and \( B \).
We maintain Assumption 9.5 on the behavior of the shocks.
To incorporate constant returns to scale, we replace Assumptions 9.4, 9.6, and 9.7 with the following.
As before we take \( A \) to be the graph of \( T \).
ASSUMPTION 9.18 \( X \subset \mathbb{R}^l \) is a convex cone, with its Borel subsets \( \mathcal{X} \).
ASSUMPTION 9.19 The correspondence \( T: X \times Z \rightrightarrows Y \) is nonempty, compact-valued, and continuous; for any \( (x, z) \in X \times Z \), \[ y \in T(x, z) \text{ implies } \lambda y \in T(\lambda x, z) \text{ all } \lambda \geq 0; \] and for some \( a \in (0, B^{-1}) \), \[ \|y\| \leq a \|x\|, \text{ all } y \in T(x, z), \text{ all } (x, z) \in X \times Z. \] ASSUMPTION 9.20 The function \( F: A \to \mathbb{R} \) is continuous; for each \( z \in Z \), the function \( F(\cdot, \cdot, z): A \to \mathbb{R} \) is homogeneous of degree one; for some \( c > 0 \), \[ F(x, y, z) \leq c (\|x\| + \|y\|), \text{ all } (x, y) \in A; \] and the discount factor is \( B \in (0, 1) \).
The next exercise shows that the Principle of Optimality holds under these assumptions.
Exercise 9.8 Show that under Assumptions 9.5 and 9.18—9.20, Assumptions 9.1—9.3 hold. [Hint.
Show that \[ |F(x_0, y_0, z_1) + \dots + B^{t-1} F(x_{t-1}, y_{t-1}, z_t)| \leq B (c + a) \|x_0\|, \] all \( z_1, \dots, z_t \in Z \), all \( t = 1, 2, \dots \), all \( (x_0, y_0) \in A \), all \( x_0 \in X \).]= Q(1, 1) = 9 let Q(1, 1) = Q(1, 0) = 1; and let g(x, 2) = bx + (1 — b)z, where b ∈ (0, 1).
Let P be the transition function on (X × Z, 𝒜 × ℬ) defined in Theorem 9.13.
Show that for the random variables {(x_t, z_t)} generated by P starting from some given initial point (x_0, z_0), Pr(x_{t+1} ∈ A | x_t, z_t) is not equal to Pr(x_{t+1} ∈ A | x_t).
Finally, the following exercise deals with the case where the functional equation has the form in (2).
Exercise 9.17 Let (X, 𝒜), (Y, ℬ), and (Z, ℂ) be measurable spaces; let Q be a transition function on (Z, ℂ); and let φ: Y × Z → X and g: Y × Z → Y be measurable functions.
Define H(x, z, A) = {y ∈ Y: (g(x, z, y), z') ∈ A}, all x ∈ X, z ∈ Z, A ∈ 𝒜. a.
Show that P(x, z, A × B) = Q(x, g(x, z, A), B, z) all x ∈ X, z ∈ Z, A ∈ ℬ, B ∈ ℂ, defines a transition function on (X × Z, 𝒜 × ℂ).
(Hint.
Recall the proof of Theorem 9.4.) b.
Show that if Assumptions 9.4, 9.5, 9.16, and 9.17 hold, and if g is continuous, then P has the Feller property. 9.7 Bibliographic Notes Most of the references cited in Section 4.6 were also drawn upon in this chapter.
In particular, Section 9.1 is based on Blackwell (1965).
Bill Sudderth and Erwan Quintin pointed out to us that an exact analogue of Theorem 4.2 holds for the stochastic case if universal measurability is used instead of Borel measurability.
See Bertsekas and Shreve (1978) for an argument.
Dynkin and Yushkevich (1979) and Gihman and Skorohod (1979) also present methods that apply when the hypotheses of Theorems 9.2 and 9.4 fail because of measurability problems.
Blume, Easley, and O’Hara (1982) pursue a differentiability argument that applies to the second of the two formulations in Section 9.1.
Assume that the exogenous shocks {z} are i.i.d., with a distribution described by a continuous density q.
Also assume that the shock z is an argument of the law of motion φ, but not of F or g.
In this case the functional equation has the form v(x) = sup {F(x, y) + β ∫ v[φ(x, y, z)] dq(z)}. y∈Γ(x) Finally, assume that for each (x, y) the function (x, y, *): Z → X is one-toone and continuously differentiable; let h: X × Y × X → Z denote the inverse.
Under these conditions, we can use the change of variable w = φ(x, y, z) to rewrite the functional equation as u(x) = sup {F(x, y) + ∫ v(w) q[h(x, y, w)] |h_w(x, y, w)| dw}, y∈Γ(x) where h_w is the derivative of h with respect to its third argument.
Notice that x appears on the right side of this equation only as an argument of the functions F, q_h, and h_w, not of v.
Hence if F, g, and φ are sufficiently smooth and if the maximum on the right is attained in the interior of Γ(x), we can guarantee that the value and policy functions have derivatives of any order we like.
The assumptions needed to carry this line to success are obviously more restrictive than those we have used in Section 9.2.
But in applications where they hold, one has a great deal of information about the value function that is not available by any other means.
The use of the Euler equations to construct optimal plans in quadratic problems, discussed briefly in Section 9.5, is discussed more fully and is illustrated with examples in Sargent (1979).
For the seminal use of direct empirical tests based on Euler equations, see Hall (1978).
## 10 Applications of Stochastic
Dynamic Programming In this chapter we illustrate how the methods developed in Chapter 9 can be used to study a variety of economic problems.
Some are stochastic analogues to problems in Chapter 5, and it will sharpen your intuition to compare results.
Others are problems with no, or with trivial, deterministic counterparts. 10.1 The One-Sector Model of Optimal Growth A stochastic analogue to the optimal growth problem studied in Section 5.1 can be obtained by adding random shocks to the production function.
For simplicity assume that these shocks enter multiplicatively.
This specification leads to the problem (1) sup E {∑_{t=0}^∞ β^t U(c_t)} {c_t} s.t. c_t + x_{t+1} = f(x_t, z_t), t= 0,1,..., x_0 given, x_t ≥ 0 and z_t given, where the expectation is over the sequence of shocks {z_t}.
This problem is defined by the parameter β; the functions U: ℝ_+ → ℝ and f: ℝ_+ × Z → ℝ; and a specification for the sequence of shocks {z_t}.
For the latter assume that (Z1) Z = [1, z], where 1 < z < ∞, with the Borel sets ℬ.
(Z2) {z_t} is an i.i.d. sequence of shocks, each drawn according to the probability measure A on (Z, ℬ). 288 We will also impose the restrictions on U, f, and f used in Section 5.1.
To begin with, assume that (U1)—(U4) and (T1)-(T4) of that earlier problem hold. [Notice that, as in the deterministic problem, the monotonicity restrictions on U and f justify solving out for consumption in (1).] Exercise 10.1 a.
Replace E(·) in (1) with a precisely specified sum of integrals.
Describe precisely the set of feasible plans for (1).
The functional equation corresponding to (1) is (2) v(x, z) = max {u(c, y) + β ∫ v(y, z') dA(z')}. c+y=zf(x) Under Assumptions (T1)-(T4), we can define x̄ as the unique positive value satisfying x̄ = zf(x̄).
It is obviously convenient to restrict the capital stock to lie in the interval X = [0, x̄] and to take v as defined on S = X × Z.
Exercise 10.1 b.
Show that there exists a unique bounded continuous function v satisfying (2) and that the associated optimal policy correspondence G is nonempty, compact-valued, and u.h.c.
What can be said about the relationship between the pair (v, G) and the solution to the sequence problem in part (a)? c.
Show that v is strictly increasing and strictly concave in its first argument and that G is a continuous single-valued function; call this function g. d.
Show that g has the form g(x, z) = h[zf(x)], where h is continuous and strictly increasing.
Notice that this implies that g is strictly increasing in both of its arguments.
Show that the optimal consumption policy c = φ(x, z) - g(x, z) is also strictly increasing in both of its arguments. e.
Assume in addition that (U5) and (T5) hold.
Show that if g(x, z) ∈ (0, zf(x)), then v is continuously differentiable at (x, z), with derivatives v_x(x, z) = U'[zf(x) - g(x, z)] zf'(x) and v_z(x, z) = U'[zf(x) - g(x, z)] f(x).
Next, suppose that instead of (Z2) we have (Z3) Q is a transition function on (Z, ℬ), and Q has the Feller property.
The sequence of random shocks {z_t} is a Markov process generated by Q.
Exercise 10.1 f.
Show that if (Z2) is replaced by (Z3), the conclusions in (a)—(c) are unchanged.
Does the policy function g take the form in part (d) in this case?
Is g necessarily increasing in z?
Show that if Q is monotone, then v and g are both increasing in z.
Which parts of (e) still hold? 10.2 Optimal Growth with Two Capital Goods Consider the following modification of the model above.
Let (U1)—(U5) and (Z1)—(Z2) hold, but suppose that there are two types of capital, x_1 and x_2.
Assume that there is a single output and that the production function f: ℝ^3_+ → ℝ satisfies (T1) and (T3)-(T5).
Assume that capital depreciates completely within each period and that output can be consumed or used as either type of capital.
The technology constraints are then 0 ≤ y_1, y_2, and y_1 + y_2 ≤ af(x_1, x_2).
Exercise 10.2 a.
What additional restriction on f ensures that the set of sustainable capital stocks is compact? b.
State the optimal growth problem for this economy in sequence form; state the corresponding functional equation.
Show that there exists a unique bounded continuous function v satisfying the functional equation and that v is strictly increasing, strictly concave, and once differentiable in its first two arguments.
Show that the associated policy correspondence is a continuous, single-valued function, g. c.
Show that if ∂f/∂x_1 is increasing in x_2 and ∂f/∂x_2 is increasing in x_1, then g(s) = [g_1(s), g_2(s)] is strictly increasing in all its arguments.d.
Show that this model can be reformulated in terms of only one endogenous state variable and that the analysis in Section 10.1 applies to the reformulated model. 10.3 Optimal Growth with Many Goods In this problem we show that the methods in Chapter 9 can be used to analyze the standard many-sector optimal growth model under uncertainty.
This model is the obvious generalization of the two above to include an arbitrary number of consumption and capital goods.
Let (Z, F) and Q be a measurable space and transition function that satisfy Assumption 9.5; let (Z', F') and (z_t), z ∈ Z, t=1,2,..., be as defined in Section 8.2.
Consider an economy in which in every period and every state of the world there are l capital goods and M consumption goods.
A consumption allocation for the representative consumer in this economy is a sequence c = {c_t}_{t=0}^\infty, where c_t: Z^t → R^M is an F_t-measurable function, all t.
The preferences of the representative consumer are given by U_0 = E_0 \sum_{t=0}^\infty \beta^t U(c_t), where U: R^M → R is bounded, continuous, strictly increasing, and strictly concave, and where β ∈ (0, 1).
Let (X, G), with X ⊂ R^l, satisfy Assumption 9.4.
The technology is described by a correspondence Φ: X × Z → R^M × X, where (c, y) ∈ Φ(x, z) means that the pair (c, y) of consumption goods and end-of-period capital goods is jointly producible given the pair (x, z) of beginning-of-period capital goods and current technology shock.
Assume that a. Φ is nonempty, compact-valued, convex-valued, and continuous; b. if x, x' ∈ X, z ∈ Z, x = x', and (c, y) ∈ Φ(x, z), then (c, y) ∈ Φ(x', z); c. if x, x' ∈ X, z ∈ Z, θ ∈ [0, 1], (c, y) ∈ Φ(x, z), and (c', y') ∈ Φ(x', z), then [θc + (1-θ)c', θy + (1-θ)y'] ∈ Φ(θx + (1-θ)x', z).
To apply the analysis of Section 9.2, define the correspondence T: X × X × Z → X, the set A ⊂ X × X × Z, and the return function F: A → R by T(x, z) = {y ∈ X: (c, y) ∈ Φ(x, z) for some c ∈ R^M}; A = {(x, y, z) ∈ X × X × Z: y ∈ T(x, z)}; F(x, y, z) = \max_{c} U(c) \text{ s.t. } (c, y) ∈ Φ(x, z).
Exercise 10.3 a.
Show that T, A, and F are well defined and satisfy Assumptions 9.6—9.11.
It then follows immediately from Theorems 9.6—9.8 that there exists a unique solution to the functional equation v(x, z) = \max_{y ∈ T(x,z)} \left[ F(x, y, z) + \beta \int v(y, z') Q(z, dz') \right]; that for each fixed z ∈ Z, v(·, z) is strictly increasing in each of its first l arguments and strictly concave jointly in its first l arguments; and that the optimalC.
Show that \( v \) is strictly increasing in both arguments and strictly concave in its first argument.
Show that the optimal policy correspondences associated with \( v \) is a (single-valued) continuous function; call this the function \( g \).
Show that for each \( (x, z) \in X \times Z \), \( g(x, z) \) lies in the interior of \( X \).
Show that for each \( z \in Z \), \( v(\cdot, z) \) is continuously differentiable and that for each \( z \in Z \), \( g(x, z) \) is strictly increasing in \( x \), but with a slope strictly less than one.
(Refer to Figure 10.2.) Notice that these facts imply that the growth rate in aggregate capacity, \( g(x, z)/x \), is decreasing in current capacity \( x \). e.
Show that for each \( x \in X \), \( g(x, \cdot) \) is nondecreasing in \( z \), and is strictly increasing at points where gross investment is strictly positive: where \[ g(x, z) > (1 - \delta)x. \] (Refer to Figure 10.3.) Notice that these facts imply that the growth rate in aggregate capacity, \( g(x, z)/x \), is strictly increasing in the state of current demand, \( z \).
Next, consider the long-run behavior of the aggregate capital stock under the assumption that the demand shocks are i.i.d.
That is, suppose that there is a probability measure \( A \) on \( (Z, \mathcal{L}) \) such that \( Q(z, \cdot) = A(\cdot) \), all \( z \in Z \).
Exercise 10.4 Which, if any, of the conclusions in parts (a)–(e) are changed under the assumption of i.i.d. shocks to demand?
Show that under this assumption, the optimal policy function does not depend on \( z \); that is, it can be written as simply \( g(x) \).
Hence for any \( x_0 > 0 \) the unique optimal plan is given by the deterministic difference equation \( x_{t+1} = g(x_t) \), \( t = 0, 1, \ldots \).
Show that for any \( x_0 > 0 \) the optimal sequence \( \{x_t\} \) converges to a stationary point \( \bar{x} \) that is independent of \( x_0 \).
Under what assumptions on demand and costs is \( \bar{x} \) strictly positive? 10.5 Production and Inventories 297 \[ \text{Figure 10.3} \] 10.5 Production and Inventory Accumulation In markets for many agricultural commodities, inventories play an important role in smoothing the stochastic shocks to supply that result from fluctuations in the weather.
In this section we study the determination of consumption, production, and inventories in such a setting.
Here, as in Section 10.4, we study the problem of maximizing total (consumers’ plus producers’) surplus.
As noted there, the arguments to be discussed in Chapter 15 can be used to show that the solution to this problem can be interpreted as a competitive equilibrium allocation.
Assume that demand is constant over time and is described by the inverse demand curve \( D: \mathbb{R}_+ \rightarrow \mathbb{R}_+ \).
That is, \( D(q) \) is the market-clearing price when \( q > 0 \) is the quantity supplied.
Assume that \( D \) is continuous, strictly decreasing, with \( 0 < D(0) < \infty \), and \( \lim_{q \rightarrow \infty} D(q) = 0 \).
Let \( U: \mathbb{R}_+ \rightarrow \mathbb{R} \) be defined by \[ U(q) = \int_0^q D(s) \, ds, \quad \text{all } q \in \mathbb{R}_+, \] so that \( U \) describes total consumers’ surplus (the area under the demand curve).
Assume that \( \lim_{q \rightarrow \infty} U(q) < \infty \).
The technology is as follows.
In each period \( t \), the planner must decide how to allocate the beginning-of-period stock of goods \( x_t \) (stocks carried over from last period plus the current harvest) between final consumption \( c_t \) and end-of-period stocks \( y_t \) to be carried over to the next period.
He must also decide how much input \( n_t \) (labor and so on) to devote to production.
Let \( \psi(y) \) denote the cost of holding (end-of-period) inventories of \( y \ge 0 \) units; assume that \( \psi: \mathbb{R}_+ \rightarrow \mathbb{R}_+ \) is strictly increasing, strictly convex, and continuously differentiable, with \( \psi(0) = 0 \) and \( \psi'(0) = 0 \).
Let \( c(n) \) denote the cost of devoting inputs of \( n \ge 0 \) to production; assume that \( c: \mathbb{R}_+ \rightarrow \mathbb{R}_+ \) is strictly increasing, strictly convex, and continuously differentiable, with \( c(0) = 0 \) and \( c'(0) = 0 \).
The uncertainty in this model concerns the size of the harvest.
Let \( \Omega = [0, \bar{\omega}] \) be an interval in \( \mathbb{R}_+ \), let \( \mathcal{B} \) be the Borel sets of \( \Omega \), and let \( A \) be a probability measure on \( (\Omega, \mathcal{B}) \).
Assume that \( f(n_{t-1}, \omega_t) \) is the size of the harvest if \( n_{t-1} \) is the input in period \( t-1 \) and \( \omega \) is the realization of the random shock in period \( t \).
The shocks are i.i.d. over time, with probabilities given by \( A \).
Exercise 10.5 a.
Cost and output have been specified as strictly convex and linear functions respectively of the quantity of input.
Show, by redefining “units of input” (in a nonlinear fashion), that this is equivalent to specifying cost and output as linear and strictly concave respectively in the “quantity of input.” Let \( x_t \), \( y_t \), and \( \omega_t \) be as described above.
Then the surplus-maximization problem is \[ \sup_{\{y_t, n_t\}_{t=0}^{\infty}} \mathbb{E} \left\{ \sum_{t=0}^{\infty} \beta^t \left[ U(x_t - y_t) - \psi(y_t) - c(n_t) \right] \right\} \] s.t. \[ x_{t+1} = f(n_t, \omega_{t+1}) + y_t, \quad \text{all } t, \] \[ x_t \ge 0, \quad n_t \ge 0, \quad \text{all } t, \] given \( x_0 \).
Exercise 10.5 b.
Give a precise statement of the problem in (1) in sequence form, and show that the supremum function for that problem is well defined.
What can be said about the relationship between the supremum function and solutions to the functional equation \[ v(x) = \sup_{y \ge 0, n \ge 0} \left\{ U(x - y) - \psi(y) - c(n) + \beta \int_{\Omega} v(f(n, \omega) + y) \, A(d\omega) \right\}? \] What can be said about the relationship between optimal plans for the sequence problem and the policy correspondence for (2)?
Explain briefly why the current value of the exogenous shock does not appear as a state variable in (2). c.
Show that there exists a unique bounded continuous function \( v: \mathbb{R}_+ \rightarrow \mathbb{R} \) satisfying (2).
What argument is needed to take care of the fact that the maximization is over an unbounded set?
Show that \( v \) is strictly increasing and strictly concave.
Let \( Y(x) \) and \( N(x) \) denote the maximizing values of \( y \) and \( n \), respectively, as functions of \( x \).
Show that \( Y \) and \( N \) are single-valued and continuous.
Show that \( v \) is differentiable and that \( v'(x) = U'[x - Y(x)] \).
To characterize the behavior of consumption, labor input, and inventories more sharply, it is useful to look at the first-order conditions \[ U'[x - Y(x)] + \psi'[Y(x)] = \beta \int_{\Omega} v'[f(N(x), \omega) + Y(x)] \, A(d\omega), \tag{3} \] with equality if \( Y(x) > 0 \); \[ c'[N(x)] = \beta \int_{\Omega} v'[f(N(x), \omega) + Y(x)] f_n(N(x), \omega) \, A(d\omega), \tag{4} \] with equality if \( N(x) > 0 \).
Exercise 10.5 d.
Show that consumption, \( c(x) = x - Y(x) \), is strictly increasing in the beginning-of-period stock, \( x \).
Storage and production are both ways of increasing the total supply available next period.
Next we will show that a higher beginning-of-period stock \( x \) leads to more storage and less production.
Exercise 10.5 e.
Let \( x_2 > x_1 \).
Suppose that \( Y(x_2) = Y(x_1) \) and \( Y(x_1) > 0 \).
Use (3) to show that this implies that \[ \beta \int_{\Omega} v'[Y(x_1) + f(N(x_1), \omega)] \, A(d\omega) > \beta \int_{\Omega} v'[Y(x_1) + f(N(x_2), \omega)] \, A(d\omega), \tag{5} \] and hence that \( N(x_2) > N(x_1) \).
Use (4) to show that this, in turn, implies that \[ \beta \int_{\Omega} v'[Y(x_1) + f(N(x_1), \omega)] f_n(N(x_1), \omega) \, A(d\omega) < \beta \int_{\Omega} v'[Y(x_1) + f(N(x_2), \omega)] f_n(N(x_2), \omega) \, A(d\omega). \tag{6} \] Next we will use (5) and (6) to obtain a contradiction to the hypothesis that \( Y(x_2) = Y(x_1) \) and \( Y(x_1) > 0 \).
Define \[ \phi(\omega) = v'[Y(x_1) + f(N(x_2), \omega)] - v'[Y(x_1) + f(N(x_1), \omega)]. \] Since \( Y(x_2) = Y(x_1) \) and \( N(x_2) > N(x_1) \), it follows immediately that \( \phi(\omega) \ge 0 \) as \( \omega \ge \bar{\omega} \), where \( \bar{\omega} = [Y(x_1) - Y(x_1)]/[N(x_2) - N(x_1)] > 0 \).
Then (5) and (6) respectively state that \( \mathbb{E}[\phi(\omega)] < 0 \) and \( \mathbb{E}[\phi(\omega)\omega] > 0 \).
Exercise 10.5 f.
Show that this is a contradiction.
Hence if \( x_2 > x_1 \), then either \( Y(x_2) > Y(x_1) \) or \( Y(x_2) = Y(x_1) = 0 \).
Exercise 10.5 g.
Show that \( N(x) > 0 \), all \( x \), so that (4) always holds with equality.
Use this fact and the result established in part (e) to show that \( x_2 > x_1 \) implies that \( N(x_2) < N(x_1) \).
How would this result be changed if \( c'(0) > 0 \)? 10.6 Asset Prices in an Exchange Economy In this problem we study the determination of equilibrium asset prices in a pure exchange economy.
There are a finite number of productive assets, each in fixed supply, that produce random quantities of the single consumption good each period; we call these dividends.
Thus, an asset is a claim to a stochastic dividend stream.
We normalize units of assets so earnings during each period.
The decision problem for this worker is defined by 8, L @, and the probability distribution over new wage offers.
Assume that 0 < θ < 1, and let U: R+ → R+ be continuously differentiable, strictly increasing, and strictly concave, with U(0) = 0 and U’(0) < ∞.
Assume that all wage offers lie in the interval W = [0, w̄], and let f be a density on that interval.
It is possible, but awkward, to set up this problem in sequence form.
To do so we need two exogenous state variables.
The first is d ∈ D = {0, 1}, where d = 0 or 1 is interpreted respectively as meaning that the worker does or does not lose his job at the beginning of the current period, given that he chose to work last period.
The second is z ∈ Z = [0, w̄], where z is interpreted as the worker’s current wage offer, given that he chose to search last period.
In addition there is one endogenous state variable, the current wage w ∈ W.
In each period, given his current wage offer w, the worker chooses an action y ∈ Y = {0, 1}, where y = 0 or 1 is interpreted respectively as meaning that the worker chooses to search or to work at his current job.
Exercise 10.7 a.
What is the law of motion φ: W × Y × D × Z → W for this model?
That is, describe w_{t+1} in terms of (w_t, y_t, d_t, z_t). b.
Formulate the worker’s decision problem as a choice of functions mapping partial histories (d^t, z^t) = [(d_1, z_1), ..., (d_t, z_t)] of exogenous shocks into actions and current wage offers that satisfy the law of motion above, given the initial state (w_0, d_0, z_0).
Show that the supremum function v* for this problem is well defined and depends only on w_0 (not on d_0 or z_0).
The recursive formulation of this problem is much simpler and more natural.
For notational convenience, drop the asterisk and let v be the Supremum function for the problem in (b).
Suppose that a worker's Current wage offer is w, that he chooses to work at this wage for one Period, and that he will follow an optimal policy (if one exists) forever after.
Then his expected present discounted value of utility is U(w) + β[(1 − θ)v(w) + θv(0)].
If he chooses to search instead, his expected utility is 0+ β∫_0^{w̄} v(w') f(w') dw'.
Combining these possibilities, we find that v must satisfy (1) v(w) = max {U(w) + β[(1 − θ)v(w) + θv(0)], ∫_0^{w̄} v(w') f(w') dw' }, Exercise 10.7 c.
Show that there exists a unique bounded continuous function v satisfying (1) and that v is the supremum function for the problem in part (b).
Show that v is weakly increasing.
The value function v can be characterized more sharply by exploiting special features of (1).
First, define (2) A = β∫_0^{w̄} v(w') f(w') dw', and note that v(0) = A.
Exercise 10.7 d.
Show that there is a unique w* ∈ W such that v(w*) = U(w*) + β[(1 − θ)v(w*) + θA] = A.
It follows from part (d) that w* is the unique value satisfying (3) U(w*) = (1 − β)A.
Exercise 10.7 e.
Show that v has the form (4) v(w) = A if w < w*, U(w) + βθA / [1 − β(1 − θ)] if w = w*, as shown in Figure 10.4.
Equation (4) gives the solution v to (1) in terms of A and w*.
The value of A is in turn given in terms of v by (2), and the value of w* by (3).
Exercise 10.7. f.
Use (2) and (4) to show that (5) 0 = ∫_{w*}^{w̄} [U(w) − U(w*)] f(w) dw, where F(w) = ∫_0^w f(w') dw' is the cumulative distribution function corresponding to f.
Equations (3) and (5) are now two equations in the unknown parameters w* and A.
Combining them to eliminate A gives (6) [1 + β(1 − θ) − βF(w*)]U(w*) = β ∫_{w*}^{w̄} U(w) f(w) dw.
Exercise 10.7 g.
Show that there is a unique value w* satisfying (6).
Parts (d)—(g) completely characterize the value function v: it is given by (4) with w* as determined in part (g) and A then given by (3) or (5).
From (1) we see that the optimal decision rule for the worker is simply: if the current wage is at least w*, work; if not, search.
Call w* the reservation wage.
Exercise 10.7 h.
How does the reservation wage depend on the parameters β and θ? i.
What can be said about the effect of changes in the variance of the wage distribution on the expected utility of the worker?
Figure 10.4 --- 10.8 The Dynamics of the Search Model Let W = [0, w̄] with its Borel subsets 𝒲, and let L be a probability measure on (W, 𝒲).
Let w* ∈ (0, w̄], and let A = [w*, w̄].
In the search model of the last problem, we showed that if a worker follows an optimal strategy, then his wage offers {w_t} are a Markov process on (W, 𝒲) with transition function (1a) P(w_{t+1} ∈ B | w_t) = f(B) for all B ∈ 𝒲, if w_t ∈ A^c, (1b) P(w_{t+1} ∈ B | w_t) = 0 if 0 ∉ B and w_t ∉ B, 1 − θ if 0 ∈ B and w_t ∉ B, θ if 0 ∈ B and w_t ∈ B, 1 if 0 ∈ B and w_t ∈ B, if w_t ∈ A.
Here W = [0, w̄] is the set of possible wage offers; f is the probability measure over wage offers if the worker is searching; A = [w*, w̄] is the set of acceptable wage offers; and A^c = [0, w*) is the set of unacceptable offers.
(We adopt the convention that the worker accepts the wage w*.) Here we study the long-run behavior of this Markov process.
That is, we ask: Given an initial probability measure μ_0 on (W, 𝒲), what can we say about the sequence of probability measures μ_t = (T*)^t μ_0, n = 1, 2,..., where T* is the adjoint operator associated with P (cf.
Section 8.1)?
Because the transition function P is so simple, it is possible to answer this question very explicitly using ad hoc arguments.
Let μ_0 be an initial probability measure on (W, 𝒲), and define the sequence {μ_t} as above.
Then the probability that the worker is unemployed (searching) in any period t is μ_t(A^c).
We begin by determining the sequence {μ_t(A^c)}_{t≥0} of unemployment probabilities.
To do this, we note that the probability that the worker is unemployed in period t + 1 is equal to the probability that he is unemployed in period t and draws an unacceptable wage, plus the probability that he is employed in period t and loses his job.
Hence, as (1a) and (1b) imply, μ_{t+1}(A^c) = ∫_{W} P(w_{t+1} ∈ A^c | w_t) μ_t(dw_t) = μ_t(A^c)F(w*) + μ_t(A)θ = μ_t(A^c)F(w*) + [1 − μ_t(A^c)]θ (2) = θ + μ_t(A^c)[F(w*) − θ], t = 0, 1,....
That is, the sequence {μ_t(A^c)} is described by the first-order difference equation (2).
Exercise 10.8 a.
Show that the difference equation (2) is stable and that lim_{t→∞} μ_t(A^c) = θ / [1 + θ − F(w*)]. b.
Let C ⊂ A^c be any measurable set of unacceptable wage offers.
Use the same reasoning as above to show that if 0 ∈ C, then μ_{t+1}(C) = θ + μ_t(A^c) [F(C) − θ], t = 0, l,..., and lim_{t→∞} μ_t(C) = [F(C) / (1 + θ − F(w*))] θ. c.
Show that if 0 ∉ C, then μ_t(C) = μ_0(C) [F(C)]^t, t = 0, 1,..., and lim_{t→∞} μ_t(C) = 0.
For any measurable set C ⊂ A, the probabilities are also easily determined.
The probability that in period t + 1 the worker has a wage in the set C ⊂ A is simply the probability that he is searching in period t and draws a wage in the set C, plus the probability that he had a wage in the Set C last period and retained his job.
Thus, as (1a) and (1b) imply, μ_{t+1}(C) = ∫_{W} P(w_{t+1} ∈ C | w_t) μ_t(dw_t) = μ_t(A^c)F(C) + μ_t(C) (1 − θ), t = 0, 1,....
Exercise 10.8 c.
Show that for any measurable set C ⊂ A of acceptable wage offers, lim_{t→∞} μ_t(C) = [F(C) / (1 + θ − F(w*))] (1 − θ). d.
Interpret the results in (3)—(6).
What is the average wage for employed workers in this economy?
What is the distribution of the length of unemployment spells? 10.9 Variations on the Search Model Once the basic structure of the search model in Sections 10.7 and 10.8 is understood, it is easy to think of variations that capture realistic features that are abstracted from in the original version.
It would be tedious to work through all such variations in detail, but it is instructive to think some of them through at least to the point of formulating the appropriate analogue to the functional equation.
Exercise 10.9 a.
Suppose wage offers follow a Markov process with transition function Q on (W, 𝒲).
Assume that Q is monotone and has the Feller property.
How does this change the functional equation?[Equation (1) in Section 10.7] and Figure 10.4? b.
Suppose the worker is endowed with one unit of time each period, which he divides between \( l \) units of leisure and \( 1 - l \) units of work or search.
His utility function is \( U(c, l) \).
He can choose his hours if he works at all.
Thus, if his current wage is \( w \), and he chooses to work \( 1 - l \) units of time, his current consumption (equal to his current earnings) is \( c = (1 - l)w \).
If he searches, the probability of obtaining any offer is \( 1 - \gamma \) so with probability \( \gamma \) he draws a wage offer of zero.
Reformulate the functional equation for this case. c.
Suppose that the job-loss probability \( \delta \) is zero, but that each worker spends exactly \( T + 1 \) periods in the work force.
Specifically, a worker enters the labor force at age \( t = 0 \) with no job (an initial wage offer of zero) and hence will spend at least one period searching.
The objective function for a worker just entering the labor force is thus \( E[\sum_{t=0}^{T} \beta^t U(c_t)] \).
What is the functional equation for the value \( v_t(w) \) for a worker of age \( t \) who begins with a wage offer \( w \)?
What can be said about the sequence \( w_1, \dots, w_T \) of age-specific reservation wages? d.
Retain the assumptions of part (c), and assume the following demographics.
In each period, all age \( T + 1 \) workers retire, and an equal number of age zero workers enter.
Thus, in each period there are an equal number of workers at each of the ages \( t = 0, 1, \dots, T \).
What do the age-specific unemployment rates look like for such an economy?
What is the shape of the age-earnings profile, the sequence of age-specific average wages?
What shapes of age-specific unemployment rate functions could one obtain by combining this model with the original model of Section 10.7? e.
Suppose that \( x \in X = [0, 1] \) is an index of labor market conditions and that \( f(\cdot, x), x \in X \), is a family of density functions on the interval \( W = [0, \bar{w}] \).
Thus \( f(\cdot, x) \) describes the distribution of offers the worker faces if market conditions are \( x \).
Assume that this family of density functions has the monotone likelihood ratio property.
That is, for any \( x' > x \), the ratio \( f(w, x') / f(w, x) \) is increasing in \( w \).
Let \( g: X \to \mathbb{R} \) also be a density function.
Modify the search model in Section 10.7 as follows.
Assume that whenever a worker becomes unemployed, there is a random draw of \( x \) from the distribution given by \( g \).
The value of \( x \) is fixed as long as the worker continues searching, but the worker does not observe \( x \) directly.
(He does know that it is a random draw from the distribution \( g \).) However, the worker can make inferences about \( x \) based on the wage offers he observes.
Thus the worker can use Bayes’s rule to update his beliefs about \( x \) while he is searching.
How must the functional equation (1) in Section 10.7 be modified to incorporate \( x \)?
How does the reservation wage of a worker who has been searching for \( n \) periods depend on the offers he has received? 10.10 A Model of Job Matching Rather than thinking of a job as being characterized by its wage rate, one may think of it as being described by a productivity variable that is specific to a particular worker-task “match.” Here is a simple, discrete version of this idea.
A worker must choose among a continuum of possible tasks.
At any given task, in any period he produces a return of 1 with probability \( \theta \) or 0 with probability \( 1 - \theta \).
Returns on a given task are serially independent.
There is no way to tell one’s proficiency \( \theta \) at a particular task short of trying it out, but one’s \( \theta \) on any task is drawn from a known distribution with the density function \( \lambda \) on [0, 1].
Once a worker chooses a task, he can keep it as long as he wants or he can leave it and draw a new task from \( \lambda \).
Suppose a worker has engaged in a specific task for \( n \) periods and has achieved \( k \in \{0, 1, \dots, n\} \) successes.
His probability of a success at this task in any future period, conditional on \( k \) successes in \( n \) trials to date, is then given by the density \( f(\theta, n, k) \).
For any \( (\theta, n, k) \), an application of Bayes’s rule gives \[ f(\theta, n, k) = \frac{\lambda(\theta) [\theta^k (1-\theta)^{n-k}]}{\int_0^1 \lambda(\theta) [\theta^k (1-\theta)^{n-k}] d\theta}, \] since given \( \theta \), the probability of \( k \) successes in \( n \) independent trials is given by the binomial formula.
Then the expected return \( \alpha(n, k) \) on the next trial, if he remains on this task, is \[ \alpha(n, k) = \int_0^1 \theta f(\theta, n, k) d\theta = \frac{\int_0^1 \theta^{k+1} (1-\theta)^{n-k} \lambda(\theta) d\theta}{\int_0^1 \theta^k (1-\theta)^{n-k} \lambda(\theta) d\theta}. \] Exercise 10.10 a.
Suppose \( \lambda \) is the uniform density on [0, 1]; that is, \( \lambda(\theta) = 1 \), all \( \theta \in [0, 1] \).
Show that \( f(\theta, n, k) \) is the beta density with parameters \( (k + 1, n + 1 - k) \): \[ f(\theta, n, k) = \frac{\Gamma(n+2)}{\Gamma(k+1)\Gamma(n+1-k)} \theta^k (1-\theta)^{n-k}, \] where \( \Gamma(x) = \int_0^\infty t^{x-1} e^{-t} dt \). b.
Suppose \( \lambda \) is the beta density with parameters \( (\alpha, \beta) \); that is, \[ \lambda(\theta) = \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha)\Gamma(\beta)} \theta^{\alpha-1} (1-\theta)^{\beta-1}, \quad \theta \in (0, 1), \] [so part (a) is the special case \( \alpha = \beta = 1 \)].
Show that \[ f(\theta, n, k) = \frac{\Gamma(\alpha + \beta + n)}{\Gamma(\alpha + k)\Gamma(\beta + n - k)} \theta^{\alpha+k-1} (1-\theta)^{\beta+n-k-1}. \] c.
Show that if \( \lambda \) is as specified in (b), then \[ \alpha(n, k) = \frac{\alpha + k}{\alpha + \beta + n}. \] d.
Show that \( \alpha(n, k) \) as given in (c) satisfies \[ 0 < \alpha(n, k) < 1, \quad \alpha(n, k+1) > \alpha(n, k), \\ \alpha(n+1, k) < \alpha(n, k), \quad \alpha(n+1, k+1) > \alpha(n, k), \\ k = 0,1,\dots,n; \quad n = 1,2,\dots. \] e.
Show that if \( \{k_n\} \) is a sequence of positive integers with \( k_n \le n \) and \( \lim_{n \to \infty} k_n/n = p \), then \( \lim_{n \to \infty} \alpha(n, k_n) = p \).
Do these properties hold for an arbitrary density \( \lambda \) with \( \lambda(\theta) > 0 \) on (0, 1)?
Now consider the decision problem of a worker who has been engaged on a given task for \( n \) periods and has produced \( k \) successes.
Let \( v(n, k) \) denote the expected present value, with the discount factor \( \beta \), of his earnings under optimal behavior.
If he remains at his present task, he has an expected current return of \( \alpha(n, k) \) (his success probability), a probability of \( \alpha(n, k) \) of moving to state \( (n + 1, k + 1) \), and a probability of \( 1 - \alpha(n, k) \) of moving to \( (n + 1, k) \).
If he chooses a new task, his expected current return is \( \alpha(0, 0) = \int_0^1 \theta \lambda(\theta) d\theta \), and he moves to the state \( (1, 1) \) with probability \( \alpha(0, 0) \) or to \( (1, 0) \) with probability \( 1 - \alpha(0, 0) \).
Hence \( v(n, k) \) must satisfy \[ v(n, k) = \max \left\{ \alpha(n, k) + \beta \left[ \alpha(n, k) v(n+1, k+1) + [1 - \alpha(n, k)] v(n+1, k) \right], \\ \alpha(0, 0) + \beta \left[ \alpha(0, 0) v(1, 1) + [1 - \alpha(0, 0)] v(1, 0) \right] \right\}. \] The domain of \( v \) is thus the triangular array \( D \) of integers \( n = 0,1,\dots \), \( k = 0,1,\dots,n \), and the range of \( v \) is the interval [0, \( 1/(1 - \beta) \)].
Let \( S \) be the space of functions \( f: D \to [0, 1/(1 - \beta)] \), with the norm \[ \|f\| = \sup_{(n,k) \in D} |f(n,k)|. \] Exercise 10.10 f.
Prove that there is a unique \( v \in S \) satisfying (1). g.
Prove that if \( \alpha(n, k) \) has the properties in part (d), then \( v(n, k) \) is nonincreasing in \( n \) for each fixed \( k \), nondecreasing in \( k \) for each fixed \( n \); and if \( \{k_n\} \) is a sequence of positive integers with \( k_n \le n \) and \( \lim_{n \to \infty} k_n/n = p \), then \[ \lim_{n \to \infty} v(n, k_n) = \max \left\{ \frac{\alpha(0,0)}{1 - \beta}, \frac{p}{1 - \beta} \right\}. \] The policy correspondence, which takes states \( (n, k) \) into choices 1 (stay on the job) and 0 (leave), is multivalued for some states \( (n, k) \).
(Which ones?) Let us select a policy function by assuming that the worker stays on the job if he is indifferent.
Exercise 10.10 h.
Prove that there exists a sequence \( \{j_n\}_{n=1}^\infty \) of integers such that the optimal policy is given by \[ d(n,k) = \begin{cases} 1 & \text{if } k \ge j_n, \\ 0 & \text{if } k < j_n. \end{cases} \] Show that this sequence satisfies \[ j_n \le n, \quad \text{and} \quad j_{n+1} = j_n, \quad n = 1,2,\dots. \] i.
What is the average wage in this economy for workers with job seniority \( n \), for \( n \in \{0, 1, 2, \dots\} \)? 10.11 Job Matching and Unemployment If we interpret the wage rate in the search model of Section 10.7 as a worker’s expected return on a specific task, that model and the jobmatching model of Section 10.10 are obviously complementary.
Suppose, for example, that workers in Section 10.7 do not immediately draw a new task the period after they leave one but instead must spend one period unemployed.
Exercise 10.11 a.
Modify the functional equation of Section 10.7 to suit this new situation.
How are the answers to parts (f), (g), and (h) of Exercise 10.7 affected? , $p^*$.
Example 2 Let $s = 3$, and suppose that $\Pi$ has the form $$ \Pi = \begin{bmatrix} 1-\gamma & \gamma/2 & \gamma/2 \\ 0 & 1/2 & 1/2 \\ 0 & 1/2 & 1/2 \end{bmatrix} $$ where $\gamma \in (0, 1)$.
If the system starts out in state $s_1$, then in the next period with probability $(1-\gamma)$ it stays in that state, and with probability $\gamma$ it leaves.
Given that it leaves, it is equally likely to go to state $s_2$ or $s_3$.
Note that if it leaves the state $s_1$, it cannot return.
A state is called transient if there is a positive probability of leaving and never returning.
If the initial state is $s_2$ or $s_3$, the situation is similar to that in Example 1; here $E = \{s_2, s_3\}$ is the only ergodic set.
By direct calculation we find that in this example $$ \Pi^n = \begin{bmatrix} (1-\gamma)^n & \delta/2 & \delta/2 \\ 0 & 1/2 & 1/2 \\ 0 & 1/2 & 1/2 \end{bmatrix} $$ where $\delta_n = 1 - (1 - \gamma)^n$.
Since $\gamma \in (0, 1)$, it follows that $$ \lim_{n\to\infty} \Pi^n = \begin{bmatrix} 0 & 1/2 & 1/2 \\ 0 & 1/2 & 1/2 \\ 0 & 1/2 & 1/2 \end{bmatrix}. $$ Thus, with probability one the system eventually leaves the state $s_1$ and enters the ergodic set.
Note that in this case, as in Example 1, $\{\Pi^n\}$ converges, and each row of the limit matrix is an invariant distribution. **11.1 / Markov Chains** &nbsp;&nbsp;&nbsp; 323 Example 3 Next suppose that $\Pi$ has the form $$ \Pi = \begin{bmatrix} \Pi_1 & 0 \\ 0 & \Pi_2 \end{bmatrix} $$ where $\Pi_1$ and $\Pi_2$ are $k \times k$ and $(l-k) \times (l-k)$ Markov matrices respectively, each with strictly positive elements.
Then $$ \Pi^{2n} = \begin{bmatrix} \Pi_1^{2n} & 0 \\ 0 & \Pi_2^{2n} \end{bmatrix} $$ and $$ \Pi^{2n+1} = \begin{bmatrix} \Pi_1^{2n+1} & 0 \\ 0 & \Pi_2^{2n+1} \end{bmatrix} $$ for even- and odd-numbered transitions respectively.
If the system begins in a state in the set $C_1 = \{s_1, \ldots, s_k\}$, then after any even number of steps it is back in the set $C_1$, and after any odd number of steps it is in the set $C_2 = \{s_{k+1}, \ldots, s_l\}$.
If the system starts out in $C_2$, the reverse is true.
In this example, as in the first, there is only one ergodic set, all of $S$, but that ergodic set has cyclically moving subsets.
Obviously $\{\Pi^n\}$ does not converge in this case, but the two subsequences for odd and even steps do.
For example, suppose that $k = l - k = 2$ and that $\Pi_1$ and $\Pi_2$ are both equal to $\Pi$ of Example 1.
Then as $n$ increases, $$ \Pi^{2n} \to \begin{bmatrix} 1/2 & 1/2 & 0 & 0 \\ 1/2 & 1/2 & 0 & 0 \\ 0 & 0 & 1/2 & 1/2 \\ 0 & 0 & 1/2 & 1/2 \end{bmatrix}, $$ $$ \Pi^{2n+1} \to \begin{bmatrix} 1/2 & 1/2 & 0 & 0 \\ 1/2 & 1/2 & 0 & 0 \\ 0 & 0 & 1/2 & 1/2 \\ 0 & 0 & 1/2 & 1/2 \end{bmatrix}, $$ for even- and odd-numbered transitions.
Thus $\{\Pi^n\}$ does not converge. --- **324** &nbsp;&nbsp;&nbsp; **11 / Strong Convergence of Markov Processes** On the other hand, the following average does: $$ P = \begin{bmatrix} 1/4 & 1/4 & 1/4 & 1/4 \\ 1/4 & 1/4 & 1/4 & 1/4 \\ 1/4 & 1/4 & 1/4 & 1/4 \\ 1/4 & 1/4 & 1/4 & 1/4 \end{bmatrix}. $$ Note, too, that each row of this limit matrix, $p^* = (1/4, 1/4, 1/4, 1/4)$, is an invariant distribution.
Example 4 Next suppose that $\Pi$ has the form $$ \Pi = \begin{bmatrix} \Pi_1 & 0 \\ 0 & \Pi_2 \end{bmatrix} $$ where $\Pi_1$ and $\Pi_2$ are Markov matrices of dimension $k \times k$ and $(l-k) \times (l-k)$ respectively, each with strictly positive elements.
The $n$-step transitions are then given by $$ \Pi^n = \begin{bmatrix} \Pi_1^n & 0 \\ 0 & \Pi_2^n \end{bmatrix}. $$ Thus, if the system starts out in the set $E_1 = \{s_1, \ldots, s_k\}$, then it stays in that set forever.
The same is true if the system starts out in the set $E_2 =$ $\{s_{k+1}, \ldots, s_l\}$.
In this case, then, there are two ergodic sets.
Clearly the sequence $\{\Pi^n\}$ converges if and only if $\{\Pi_1^n\}$ and $\{\Pi_2^n\}$ both converge.
Suppose that $\Pi_1$ and $\Pi_2$ are both as specified in Example 1.
Then $$ \lim_{n\to\infty} \Pi^n = \begin{bmatrix} 1/2 & 1/2 & 0 & 0 \\ 1/2 & 1/2 & 0 & 0 \\ 0 & 0 & 1/2 & 1/2 \\ 0 & 0 & 1/2 & 1/2 \end{bmatrix}. $$ Thus there are two invariant distributions, $p_1 = (1/2, 1/2, 0, 0)$ and $p_2 =$ $(0, 0, 1/2, 1/2)$, and the system converges to one or the other, depending on the initial state.
Note, too, that all convex combinations of $p_1$ and $p_2$ are invariant distributions as well. **11.1 / Markov Chains** &nbsp;&nbsp;&nbsp; 325 Example 5 Finally, consider a case where there are three states, and $$ \Pi = \begin{bmatrix} 1-\gamma & \alpha\gamma & \beta\gamma \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} $$ where $\alpha, \beta, \gamma \in (0, 1)$ and $\alpha + \beta = 1$.
Here, as in Example 2, $s_1$ is a transient state; however, there are two ergodic sets: $E_1 = \{s_2\}$ and $E_2 =$ $\{s_3\}$.
If the system starts out in state $s_1$ and leaves, the conditional probability of going to $E_1$ is $\alpha$ and to $E_2$ is $\beta$.
If the state is $s_2$ or $s_3$, it remains constant forever after.
The $n$-step transition matrix in this case is $$ \Pi^n = \begin{bmatrix} (1-\gamma)^n & \alpha\delta_n & \beta\delta_n \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, $$ where $\delta_n = 1 - (1 - \gamma)^n$.
Since $\gamma \in (0, 1)$, it then follows that $$ \lim_{n\to\infty} \Pi^n = \begin{bmatrix} 0 & \alpha & \beta \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}. $$ In this case $\{\Pi^n\}$ converges; each row of the limit matrix is an invariant distribution; and the row corresponding to the transient state is a convex combination of the rows corresponding to the ergodic sets.
These five examples illustrate all possible types of limiting behavior for finite Markov chains.
We will establish this fact in the remainder of the section, studying the existence and uniqueness of an ergodic set, the existence and uniqueness of an invariant distribution, and the convergence of the sequences $\{(1/n)\sum_{i=0}^{n-1} \Pi^i\}$ or $\{\Pi^n\}$ or both.
Theorems 11.1, 11.2, and 11.4 deal with these questions under successively Stronger assumptions about $\Pi$.
Let $S = \{s_1, \ldots, s_l\}$, let the stochastic matrix $\Pi = [\pi_{ij}]$ define the transition probabilities, and let $\Pi^n = [\pi_{ij}^{(n)}]$ denote the powers of $\Pi$ [Note that $\pi_{ij}^{(n)}$ is not in general equal to $(\pi_{ij})^n$.] Our first result requires no further restrictions on $\Pi$. --- **326** &nbsp;&nbsp;&nbsp; **11 / Strong Convergence of Markov Processes** **THEOREM 11.1** Let $S = \{s_1, \ldots, s_l\}$ be a finite set, and let the stochastic matrix $\Pi$ define transition probabilities on $S$.
Then a. $S$ can be partitioned into $M \ge 1$ ergodic sets and $Q$ transient set. b.
The sequence $\{(1/n) \sum_{i=0}^{n-1} \Pi^i\}$ converges to a stochastic matrix $Q$.
That is, $\lim_{n\to\infty} (1/n) \sum_{i=0}^{n-1} \Pi^i = Q$, for any sequence $\{p_n = \{\pi_{ij}\}\}$ where $p_0 \in A$. c.
Each row of $Q$ is an invariant distribution, so $p_0 Q$ is an invariant distribution for each $p_0 \in A$ and every invariant distribution for $\Pi$ is a convex combination of the rows of $Q$. *Proof of (a).* Call $j$ a consequent of $i$ if $\pi_{ij}^{(n)} > 0$ for some $n \ge 1$.
Call $s_i$ a transient state if it has at least one consequent $j$ for which $\pi_{ji}^{(n)} = 0$, all $n \ge 1$.
Thus, a state is transient if and only if there is a positive probability of not returning to it.
Call a state $i$ recurrent if for every $j$ that is a consequent of $i$, $i$ is also a consequent of $j$.
To show that $S$ can be partitioned as claimed, we will begin by showing that $S$ has at least one recurrent state.
Suppose the contrary.
Then $\pi_{ii} < 1$ for all $i$ (otherwise $s_i$ would be recurrent).
Since $s_1$ is transient, there exists a state—call it $s_2$—and $N_1 \ge 1$ such that $\pi_{12}^{(N_1)} > 0$ and $\pi_{21}^{(n)} = 0$, $n = 1, 2, \ldots$.
Then since $\pi_{21}^{(1)} = 0$, $\pi_{21}^{(n)} = 0$, $n = 1, 2, \ldots$, and $s_2$ is transient, there exists a state—call it $s_3$—and $N_2 \ge 1$ such that $\pi_{23}^{(N_2)} > 0$ and $\pi_{32}^{(n)} = 0$, $n = 1, 2, \ldots$.
Moreover, since $0 = \pi_{ji}^{(n)} = \sum_k \pi_{jk}^{(m)}\pi_{ki}^{(n-m)}$, $n = 1, 2, \ldots$, it follows that $\pi_{ji}^{(n)} = 0$, $n = 1, 2, \ldots$.
Continuing by induction, we conclude that $\pi_{ii} < 1$ and $\pi_{ji}^{(n)} = 0$ for $j \neq i$, $n \ge 1$, which contradicts the fact that $\Pi$ is a stochastic matrix.
Next we will show that if the state $s_i$ is recurrent and $j$ is a consequent of $i$, then $i$ is a consequent of $j$ and $s_j$ is also recurrent.
Suppose that $s_i$ is recurrent and that $j$ is a consequent of $i$.
Since $s_i$ is recurrent, not transient, it follows that $\pi_{ji}^{(N)} > 0$ for some $N \ge 1$, so $i$ is a consequent of $j$.
Next, suppose that $k$ is a consequent of $j$.
Then $\pi_{jk}^{(L)} > 0$, for some $L \ge 1$.
But this implies that $\pi_{ik}^{(N+L)} = \pi_{ij}^{(N)}\pi_{jk}^{(L)} > 0$, so $k$ is a consequent of $i$.
Since $s_i$ is recurrent, it then follows that $\pi_{ki}^{(K)} > 0period b for k = 1, 2,...; and the average over these distributions for the first n periods is given by n-1 1 1 ES_m = ∑_{h=0}^{∞} p_t^{(n)} = p0 [Π^h - R^h].
N h=0 k=0 π 20 Define A^(n) = (1/n) ∑_{t=0}^{n-1} Π^t, and note that since it is an average of stochastic matrices, each A^(n) is itself a stochastic matrix.
We will first characterize the behavior of the long-run average probabilities by examining the behavior of A as n → ∞ and then will show that if S is a finite set, the sequence {A^(n)} converges.
First we will show that there exists a subsequence—call it n_k—such that {A^(n_k)} converges.
To see this, note that each of the sequences {a_{ij}^(n)}_{n=1}^{∞}, i,j = 1,..., l, lies on the compact interval [0, 1].
Hence there exists a subsequence of the n's—call it n'—for which {a_{ij}^(n')} converges.
Then, by the same reasoning, there exists a subsequence of the n''s, call it n'', for which {a_{ij}^(n'')} also converges, etc.
Since there are only a finite number of elements to consider, continuing by induction establishes the desired conclusion.
Note, too, that this argument establishes that every subsequence of {A^(n)} contains a convergent subsequence.
Let Q be the limit of some convergent subsequence {A^(n_k)}: lim_{k→∞} A^(n_k) = Q.
Then pre- and postmultiplying by Π, we find that lim_{k→∞} (1/n_k) ∑_{t=0}^{n_k-1} Π^{t+1} = Q = ΠQ. lim_{k→∞} (1/n_k) ∑_{t=0}^{n_k-1} Π^{t+1} = ΠQ.
Since the two averages in these equations differ only by the terms Π^{n_k}/n_k and p0Π^{n_k}/n_k, both of which go to zero as k → ∞, the two limits are equal.
Hence Q = ΠQ = QΠ.
This fact in turn implies that Q = ΠQΠ = Q.
Thus Q is an invariant distribution matrix.
We have defined Q to be the limit of the subsequence {A^(n_k)}.
From the remaining terms in {A^(n)} we can extract another convergent subsequence; call its limit A.
Then since Q = QΠ = ΠQ, n = 1, 2,..., it follows that Q = QA = AQ, and, with the roles of Q and A reversed, that A = AQ = QA.
Hence A = Q.
Since the choice of subsequences converging to A and Q was arbitrary, it follows that lim_{n→∞} A^(n) = Q, and hence that p0Q = lim_{n→∞} p0A^(n) = lim_{n→∞} p0 (1/n) ∑_{t=0}^{n-1} Π^t, all p0 ∈ A^l.
**Proof.** of (c).
Finally we will show that each of the rows of Q is an invariant distribution and that every invariant distribution is a convex combination of these rows.
As shown above QΠ = Q; that is, each row of Q is an invariant distribution.
Conversely, suppose that r = (r_1, ..., r_l) is an invariant distribution.
Then ∑_{j=1}^{l} r_j a_{ji}^{(n)} = r_i, i = 1,..., l, n = 1, 2,..., so ∑_{j=1}^{l} r_j a_{ji}^{(n)} = r_i.
Taking the limit as n → ∞, we obtain ∑_{j=1}^{l} r_j q_{ji} = r_i, i = 1,..., l, so r is a convex combination of the rows of Q. ∎ This theorem applies to all of the five examples above, and they illustrate the variety of behavior that is consistent with its conclusions.
There may be one ergodic set or more than one, and in addition there may be a transient set; the sequence {Π^n} may or may not converge, but the sequence of averages {A^(n)} = {(1/n) ∑_{t=0}^{n-1} Π^t} necessarily converges; and the rows of the limiting matrix Q are invariant distributions.
For the case of finite chains, then, given any initial probability distribution, the long-run average probabilities over states converge.
In particular, if the initial state is s_i, then the long-run average probabilities are given by the ith row of the matrix Q.
If p0 is an initial probability distribution over states, then the long-run average probabilities are given by p0Q.
Note that we have not ruled out the possibility of multiple ergodic sets or cyclically moving subsets within any ergodic set.
There is a close connection between the M ergodic sets and the M invariant distributions described in Theorem 11.1.
To see it note that we can, without loss of generality, order the states so that all of the transient states come first, and the states in each ergodic class appear in a block.
With this ordering of the states, the transition matrix Π takes the (almost block diagonal) form Π = [ F   R_{01}  R_{02}  ...
R_{0M} 0   R_{11}   0     ...   0 0    0     R_{22}  ...   0 :    :      :      :     : 0    0      0     ...
R_{MM} ] Note that each matrix R_{11}, ..., R_{MM} is a stochastic matrix; hence Theorem 11.1 applies to each one, and we can define Q_j = lim_{n→∞} (1/n) ∑_{t=0}^{n-1} R_{jj}^t, j = 1,..., M.
On the other hand, R_{00} is not a stochastic matrix; otherwise F would be an ergodic set.
That is, R_{00} has at least one row sum that is strictly less than one.
Exercise 11.1 Show that when Π has the form above, Q has the form Q = [ R_{00}∞   Q_1   Q_2   ...
Q_M 0      Q_1   Q_2   ...
Q_M 0      Q_1   Q_2   ...
Q_M :      :     :          : 0      Q_1   Q_2   ...
Q_M ] where the rows within each matrix Q_j are all identical and where the column vectors u_j sum to the unit vector.
Show that the ith element in u_j is the probability of a transition, eventually, to the set E_j.
Since all the rows within each matrix Q_j are identical, it follows that if the system begins in any state in the ergodic class E_j, the long-run average probabilities are the same.
The same is true if the initial position is described by any probability distribution that assigns zero probability to all states outside of E_j.
The M distinct rows of the matrices Q_1,..., Q_M correspond to the M ergodic classes.
The first block of rows, those corresponding to initial states in F, are convex combinations of the others.
If the system begins in a transient state, then the long-run average probabilities are determined by the probability of eventually getting into each of the various ergodic classes.
Thus in the case of a finite state space we can, for an arbitrary transition matrix Π, establish the existence of at least one ergodic class and, accordingly, one invariant distribution.
To obtain sharper results, we must impose additional structure on the transition matrix Π.
The next theorem provides a necessary and sufficient condition to ensure that there is a unique ergodic class.
That is, it rules out cases like Examples 4 and 5.
### THEOREM 11.2
Let S = {s_1,..., s_l} be a finite set, and let the stochastic matrix Π define transition probabilities on S.
Then Π has a unique ergodic set if and only if there exists a state s_k such that the following holds: for every i ∈ {1,..., l}, there exists n ≥ 1 such that (Π^n)_{ki} > 0.
In this case Π has a unique invariant distribution, call it p*; each row of Q is equal to p*; and for any p0, p0Q = p*.
**Proof.** Suppose that the stated condition holds for some state s_k.
Then s_k cannot be transient and is a consequent of every state s_i, i = 1,..., l.
Hence there is at most one ergodic set.
The other claim follows immediately from Theorem 11.1.
Conversely, suppose that there is only one ergodic class, E, and choose s_k ∈ E.
Since every element of E is a consequent of s_k, it follows that the stated condition holds for every s_k ∈ E.
Consider next any s_i ∈ F.
Since s_i is transient, it is a consequent of some s_j ∈ E with p_{ij}^{(m)} > 0 for some m ≥ 1.
Hence (Π^{m+n})_{ki} = ∑_{r} p_{kr}^{(m)} p_{ri}^{(n)} ≥ p_{kj}^{(m)} p_{ji}^{(n)} > 0 for some n ≥ 1.
Thus the condition holds for all i ∈ {1,..., l}.
Our final result provides a condition that, in addition to ensuring that the set of the ergodic set, rules out cyclically moving subsets within any ergodic set.
That is, it rules out cases like Example 3.
Under this condition the sequence {Π^n}, not just the sequence of time averages, converges.
Since by Theorem 11.2 each row of Q is equal to the invariant distribution p*, it then follows that the sequence of distributions {p0Π^n} converges to p* for all p0 ∈ A^l.
Moreover, the convergence is at a geometric rate that is uniform in p0.
There are many ways to establish this result; the proof we will present uses the Contraction Mapping Theorem.
The idea is to show that if Π defines a contraction mapping on A^l, then the fixed point of this mapping is the vector p* and the convergence of {p0Π^n} is geometric.
We will also show that the converse is true: if p0Π^n → p* for all p0 ∈ A^l, then for some N ≥ 1, Π^N defines a contraction mapping on A^l.
Lemma 11.3 provides a sufficient condition for Π to define a contraction mapping on A^l.
Theorem 11.4 uses this condition to obtain the results described above.family.
As before, if the smaller family is appropriately chosen, a different, strictly weaker, definition of convergence is obtained.
Alternatively, (2) can be strengthened by requiring some sort of uniformity in the rate of convergence.
As the discussion thus far should suggest, whether convergence of probability measures is defined in terms of measures of sets or in terms of expected values of functions is purely a matter of convenience.
As we saw above for setwise convergence, and will see later for other convergence concepts, the definitions of interest can be expressed either way.
We still have not resolved the question of choosing a convergence concept.
Is setwise convergence the “right” concept?
Or should we use something stronger?
Or something weaker?
This question does not have a single answer, but it is important to understand clearly what the various concepts do and do not entail.
A particularly useful example in this regard is the following deterministic system.
Let S = (0, 1], and consider the deterministic process governed by the difference equation s_{t+1} = s_t/2.
This system is globally asymptotically stable, converging to the stationary point s* = 0 from any initial point s_0 ∈ S.
Now let ℱ be the Borel sets of S, and let P be the transition function on (S, ℱ) defined by P(s, {s/2}) = 1, so that P corresponds precisely to the deterministic process.
Let Λ_n be the probability measure that is a unit mass at the point 1/2^n, for n = 0, 1, 2,....
Then starting the system at the point s_0 = 1 is exactly the same as taking Λ_0 to be the probability measure over the state in period t = 0, and {Λ_n}_{n=1} is the sequence of probability measures over the state in subsequent periods.
What can we say about the sequence {Λ_n}?
Clearly the only candidate for a limiting measure is a unit mass at zero; call this measure Λ.
However, if we take the measurable function f(s) = 1 if s = 0, = 0 if s ≠ 0, then ∫f dΛ_n = 0, n = 0, 1, 2,..., but ∫f dΛ = 1.
Thus, (2) fails: the sequence {Λ_n} does not converge setwise to Λ or to anything else.
It seems perverse to define convergence for stochastic systems in a way that excludes our notion of convergence for deterministic systems.
We can see what the problem is by recalling the definition of convergence for deterministic systems.
A sequence {s_n} in a space S converges to s if the distance between s_n and s goes to zero as n gets large.
Our ordinary definition of convergence thus requires a metric on the space S, and we count on the metric to capture our idea of what it means for two points to be “close.” Stated somewhat differently, we choose our metric so that if s_n is close to s, then functions of the state—at least, the ones we care about—take on similar values whether the state is s_n or s.
That is, we choose the metric on S so that functions of interest are continuous in the chosen metric.
Then the fact that {s_n} converges to s implies that {f(s_n)} converges to f(s), for all functions f of interest.
Notice that in the example above, for any continuous function f, lim_{n→∞} ∫f dΛ_n = lim_{n→∞} f(1/2^n) = f(0) = ∫f dΛ.
This example and others like it motivate the following concept of convergence.
### DEFINITION L
et (S, ρ) be a metric space; let ℱ be the Borel sets of S; let {Λ_n} and Λ be measures in A(S, ℱ); and let C(S) be the space of bounded, continuous, real-valued functions on S.
Then {Λ_n} converges weakly to Λ if (3) lim_{n→∞} ∫f dΛ_n = ∫f dΛ, all f ∈ C(S).
Thus, in the deterministic example above, the sequence {Λ_n} does converge weakly to Λ.
Clearly (2) implies (3), but in general (3) does not imply (2).
That is, setwise convergence implies weak convergence, but in general the reverse is not true.
(The exception occurs when ρ is the discrete metric, so ℱ is the family of all subsets of S.
In this case every function is both measurable and continuous, B(S, ℱ) = C(S), and setwise convergence and weak convergence are equivalent.
This is why the issue of choosing a convergence concept did not arise in our treatment in Section 11.1 of systems with a finite state space.) Weak convergence is very often all that we really care about in the context of describing the dynamics of an economic system.
Accordingly, we make a detailed study of it in Chapter 12.
In the remainder of this Chapter, however, we look briefly at a stronger concept than setwise convergence.
This concept is easily stated in terms of a strengthening of (2).
### DEFINITION L
et (S, ℱ) be a measurable space and let {Λ_n} and Λ be measures in A(S, ℱ).
Then {Λ_n} converges strongly to Λ if (2) is satisfied, and if in addition the rate of convergence is uniform for all f ∈ B(S, ℱ) such that ||f|| = sup_{s∈S} |f(s)| < ∞.
The uniformity condition in this definition may look odd.
It looks less so when restated as a strengthening of (1), as will be done later.
There are two reasons for beginning with a study of strong convergence.
First, since strong convergence implies weak convergence, establishing the former is one way of establishing the latter.
Second, the results established in Section 11.1 for finite state spaces have very close parallels in terms of strong convergence results for arbitrary state spaces, and it is instructive to see what conditions are needed in the more general case.
In Section 11.3 we characterize strong convergence in terms of measures of sets.
Then in Section 11.4 we study the issue of strong convergence for Markov processes with an arbitrary state space.
We show there that all of the results obtained in Section 11.1 for finite Markov chains have quite close parallels.
In particular, we provide a fairly simple condition that is both necessary and sufficient for the strong convergence of a Markov process to a unique limiting measure, independent of the initial measure.
In Chapter 12 we take up the study of weak convergence, again beginning with a study of alternative characterizations and proceeding to the study of Markov processes.
We will not make further use of the concept of setwise convergence. 11.3.
Characterizations of Strong Convergence In this section and the next, let (S, ℱ) be an arbitrary measurable space, let A(S, ℱ) be the set of probability measures on (S, ℱ), and let B(S, ℱ) be the space of bounded, measurable functions f : S → ℝ with the sup norm, ||f|| = sup_{s∈S} |f(s)|.
The main results in this section are as follows.
We first define a norm, the total variation norm, on the set A(S, ℱ) and show (Theorem 11.6) that convergence in this norm is equivalent to the uniform convergence of measures of all sets in ℱ.
We then show (Theorem 11.7) that convergence in the total variation norm is also equivalent to strong convergence as defined in the last section.
Taken together then, these two theorems show that, as for setwise convergence, strong convergence has equivalent characterizations in terms of measures of sets or in terms of integrals of functions.
Finally, we show (Theorem 11.8) that endowed with the total variation norm, the set A(S, ℱ) is a complete metric space.
This last result is drawn upon in our study of strong convergence of Markov processes in Section 11.4, where we apply the Contraction Mapping Theorem.
In order to define the norm of interest, we must introduce the appropriate vector space.
To do this, we need the following definition.
### DEFINITION F
or any two finite measures μ₁, μ₂ on a measurable space (S, ℱ), the set function ν: ℱ → ℝ defined by ν(C) = μ₁(C) - μ₂(C), all C ∈ ℱ, is called a signed measure on ℱ.
We will use ℳ(S, ℱ) to denote the space of signed measures on (S, ℱ).
It is straightforward to show that ℳ(S, ℱ) is a vector space.
We define the total variation norm on this space by (1) ||μ|| = sup ∑ |μ(A_i)|, where the supremum is over all finite partitions of S into disjoint measurable subsets.function on (S, F), and assume that P satisfies Condition D for (, F, N).
Suppose in addition that if A is any set of positive μ-measure, then for each s ∈ S there exists n ≤ I such that P^n(s, A) > 0.
Then a.
S has only one ergodic set; b.
T* has only one invariant measure, call it π*; and c. lim_{n→∞} (1/N) Σ_{i=0}^{N-1} T^{*i} μ = π*, for all μ ∈ A(S, F).
**Proof.** If the stated condition holds, then clearly there is only one ergodic set.
Parts (b) and (c) then follow immediately from Theorem 11.9. □ Next we look at a condition that is necessary and sufficient to establish the strong convergence of the sequence of probability measures {T^{*n}μ}, and not just the sequence of averages, to a unique limit π*, independent of μ₀, and at a uniform rate.
Like the proof of Theorem 11.4 for Markov chains, the following proof is based on the Contraction Mapping Theorem.
It was shown in Exercise 8.4 that for any N ≥ 1, the operator T^{*N} maps the set of probability measures A(S, F) into itself; and it was shown in Lemma 11.8 that the space A(S, F), with the total variation norm, is a complete metric space.
As will be shown in Lemma 11.11, the following strengthening of Condition D is sufficient for the operator T^{*N} associated with P to be a contraction, for some N ≥ 1.
CONDITION M: There exists ε > 0 and an integer N ≥ 1 such that for any A ∈ F, either P^N(s, A) ≥ ε, all s ∈ S, or P^N(s, A) ≤ 1 - ε, all s ∈ S.
Exercise 11.5: Let (S, F) be a measurable space, and let P be a transition function. a.
Show that the examples in parts (c) and (e) of Exercise 11.4 satisfy Condition M. b.
Show that if P satisfies Condition M, then it satisfies Condition D. c.
Let S = {0, 1}, and let P(s, A) = { 1 if s ∈ A, { 0 otherwise, s = 1, 2.
Show that P satisfies Condition D but does not satisfy Condition M.
### LEMMA 11.11
: Let (S, F) be a measurable space; let A(S, F) be the space of probability measures on (S, F); let P be a transition function on (S, F); and let T* be the adjoint operator associated with P.
If P satisfies Condition M for N = 1 and ε > 0, then T* is a contraction of modulus (1 - ε) on the space A(S, F) with the total variation norm.
**Proof.** Suppose P satisfies Condition M for N = 1 and ε > 0.
Choose any μ₁, μ₂ ∈ A(S, F).
By Lemma 7.12, we can choose finite positive measures λ, ν₁, and ν₂ such that μᵢ = λ + νᵢ, i = 1,2, and ν₁ ⊥ ν₂.
Then using Lemma 11.5, we have ‖T*μ₁ - T*μ₂‖ = ‖T*ν₁ - T*ν₂‖ = 2 sup | ∫ P^N(s, A) ν₁(ds) - ∫ P^N(s, A) ν₂(ds) | A∈F Fix any A, A' ∈ F, and without loss of generality suppose that P(s, A) ≥ ε, all s ∈ S.
Then 2|∫ P(s, A) ν₁(ds) - ∫ P(s, A) ν₂(ds)| = 2(1 - ε)ν₁(S) = (1 - ε) ‖μ₁ - μ₂‖ where the first line uses the fact that ν₁(S) = 1 - λ(S) = ν₂(S), and the second uses the fact that ν₁ ⊥ ν₂.
Since A ∈ F was arbitrary it follows that ‖T*μ₁ - T*μ₂‖ = (1 - ε) ‖μ₁ - μ₂‖. □ Using this lemma, it is straightforward to show that Condition M is necessary and sufficient for the strong convergence of a Markov process to a unique invariant measure, independent of the initial measure μ₀, at a geometric rate that is uniform in μ₀.
For any s ∈ S, let δₛ denote the probability measure that is a unit mass at the point s.
### THEOREM 11.12
: Let (S, F) be a measurable space; let A(S, F) be the space of probability measures on (S, F), with the total variation norm; let P be a transition function on (S, F); and let T* be the adjoint operator associated with P.
If P satisfies Condition M for N = 1 and ε > 0, then there exists a unique probability measure π* ∈ A(S, F) such that (i) ‖T^{*n}μ₀ - π*‖ ≤ (1 - ε)^n ‖μ₀ - π*‖, all μ₀ ∈ A(S, F), n = 1, 2,....
Conversely, if (1) holds, then Condition M is satisfied for some N ≥ 1 and ε > 0.
**Proof.** Suppose that Condition M holds for N = 1 and ε > 0.
Then by Lemma 11.11, T*: A(S, F) → A(S, F) is a contraction of modulus 1 - ε.
Since A(S, F) is complete (Lemma 11.8), the conclusions then follow from the Contraction Mapping Theorem (Theorem 3.2).
Conversely, suppose that (1) holds.
Choose s ∈ S.
Using Lemma 11.5, we have for all A ∈ F, 2 |P^N(s, A) - π*(A)| = ‖P^N(·, A) - π*(A)‖ = ‖T^{*N}δₛ - π*‖ ≤ (1 - ε)^N ‖δₛ - π*‖ ≤ 2(1 - ε)^N.
Choose K sufficiently large that (1 - ε)^K ≤ 1/4.
Let A, A' ∈ F be given, and without loss of generality suppose that π*(A) = 1/2.
Then |P^{NK}(s, A) - π*(A)| ≤ 1/4, so P^{NK}(s, A) ≥ 1/4.
Since s ∈ S was arbitrary, Condition M holds for N = NK and ε = 1/4. □ The main attraction of this convergence result is that Condition M is easy to verify in some applications.
This fact is illustrated in Sections 13.1, 13.2, and 13.5. 11.5 Bibliographic Notes Many excellent treatments of Markov chains are available.
The material in Section 11.1 is based on Doob (1953, sect.
V.2).
Kemeny and Snell (1960), Chung (1967), and Kemeny, Snell, and Knapp (1976) are also excellent sources.
Green (1976) contains a result related to Theorem 11.4.
Some writers use the term Markov chain to refer to any Markov process with a discrete time parameter, regardless of the nature of the state space.
What we call a Markov chain is then referred to as a finite state Markov chain.
Condition D is due to Doeblin; it is discussed in detail in Doob (1953, sect.
V.5), where a proof of Theorem 11.9 can also be found.
An alternative line of proof uses the fact that Doeblin’s condition holds if and only if the operator associated with the transition function is quasi-compact.
A proof of this fact is available in Futia (1982, Theorem 4.9).
Neveu (1965, sect.
V.3) contains a proof of Theorem 11.9 based on this fact.
Both lines of proof also establish that convergence is at a uniform geometric rate.
Tweedie (1975) provides an alternative—and quite different—set of sufficient conditions for convergence, conditions that may hold when the rate of convergence is not uniform.
We are grateful to C.
Ionescu Tulcea for bringing to our attention Condition M.
It is discussed in Onicescu (1969), where Theorem 11.12 also appears.
The proof offered here, based on the Contraction Mapping Theorem, is new.
See Dynkin (1965), Rosenblatt (1971), and Gihman and Skorohod (1974) for more extensive treatments of general Markov processes.
## 12 Weak Convergence of
Markov Processes In this chapter we continue our study of the convergence of Markov processes.
As in Chapter 11, we will be concerned with sequences {μₙ}ₙ=0 of probability measures defined by μₙ₊₁ = T*μₙ, where μ₀ is a fixed initial probability measure and T* is the operator associated with a fixed transition function P.
Recall that a probability measure π* is said to be invariant under T* if it is a fixed point of T*, that is, if π* = T*π*.
In Theorem 11.12 we provided a necessary and sufficient condition on P for convergence in the total variation norm of the sequence {μₙ} to a unique invariant measure π*, for all initial probability measures μ₀.
For the reasons discussed in Section 11.2, however, strong convergence is in many situations more than we expect or care about.
Thus, in the present chapter we develop conditions that are sufficient to establish the weak convergence of the sequence {μₙ} to a unique invariant measure.
These conditions are considerably different from those required for strong convergence, and, as some of the applications in Chapter 13 illustrate, they are often extremely easy to verify.
Since weak convergence is defined in terms of continuous functions, we must impose much more structure on the state space (S, F) here than we did in Chapter 11, where it was any measurable space.
In Section 12.1, which contains general results on the characterization of weak convergence, we assume that (S, ρ) is a metric space and F is the σ-algebra generated by the open sets of S.
In the sections that follow we further restrict the analysis and assume that S is a Borel subset of a finitedimensional Euclidean space.a. \(\lim_{n \to \infty} \int f \, d\mu_n = \int f \, d\mu\), all \(f \in C(S)\); b. for every closed set \(F\), \(\limsup_{n \to \infty} \mu_n(F) \leq \mu(F)\); c. for every open set \(G\), \(\liminf_{n \to \infty} \mu_n(G) \geq \mu(G)\); d. \(\lim_{n \to \infty} \mu_n(A) = \mu(A)\), for every set \(A \in \mathcal{F}\) with \(\mu(\partial A) = 0\).
**Proof.** (a) \(\Rightarrow\) (b).
Suppose that (a) holds, and let \(F\) be a closed set.
Then by Lemma 12.1, given any \(\varepsilon > 0\) there exists a continuous function \(f\) such that \(0 \leq f \leq 1\), \(f \geq 1_F\), and \(\int f \, d\mu < \mu(F) + \varepsilon\).
Taking the limit as \(n \to \infty\) and using (a), we find that \[ \limsup_{n \to \infty} \mu_n(F) \leq \lim_{n \to \infty} \int f \, d\mu_n = \int f \, d\mu \leq \mu(F) + \varepsilon. \] Since \(\varepsilon > 0\) was arbitrary, (b) follows.
(b) \(\Rightarrow\) (a).
Suppose that (b) holds, and let \(f\) be a continuous function with \(0 \leq f(s) \leq 1\), all \(s \in S\).
For each integer \(k \geq 1\), define the sets \(\{F_{k,i}\}\) as in (3).
Then as shown in the proof of Lemma 12.2, (4) holds.
Hence \[ \int f \, d\mu_n = \sum_{i=1}^k \frac{i-1}{k} \mu_n(F_{k,i}), \quad \text{all } n, k. \] Since \(f\) is continuous, the sets \(F_{k,i}\) are all closed.
Therefore, fixing \(k\) and taking the limit as \(n \to \infty\), and using (b), we obtain \[ \limsup_{n \to \infty} \int f \, d\mu_n \leq \limsup_{n \to \infty} \sum_{i=1}^k \frac{i-1}{k} \mu_n(F_{k,i}) \leq \sum_{i=1}^k \frac{i-1}{k} \mu(F_{k,i}). \] Using (4) again, we find that \[ \sum_{i=1}^k \frac{i-1}{k} \mu(F_{k,i}) \leq \int f \, d\mu. \] Using these two inequalities and letting \(k \to \infty\), we conclude that \[ \limsup_{n \to \infty} \int f \, d\mu_n = \int f \, d\mu. \] Similarly, for the continuous function \(g = 1 - f\) we have \[ 1 - \liminf_{n \to \infty} \int f \, d\mu_n = \limsup_{n \to \infty} \int g \, d\mu_n = \int g \, d\mu = 1 - \int f \, d\mu. \] Combining these two results gives \[ \limsup_{n \to \infty} \int f \, d\mu_n = \int f \, d\mu = \liminf_{n \to \infty} \int f \, d\mu_n, \] so (a) holds.
If \(a < t < b\), apply the argument above to the function \(f = ( \cdot - a)/\) (with appropriate adjustments) and then linearity of the integral implies that the conclusion also holds.
(b) \(\Leftrightarrow\) (c).
This follows immediately from complementation.
(b) \(\Rightarrow\) (d).
Suppose that (b) holds, and let \(A \in \mathcal{F}\) be any set with \(\mu(\partial A) = 0\).
Since \(\mu(\partial A) = 0\), it follows that \(\mu(A) = \mu(A^\circ) = \mu(\bar{A})\).
Then since \(A^\circ\) is open and \(\bar{A}\) is closed and since (c) holds if (b) does, it follows that \[ \mu(A^\circ) = \mu(A) \leq \liminf_{n \to \infty} \mu_n(A^\circ) \leq \liminf_{n \to \infty} \mu_n(A), \] \[ \limsup_{n \to \infty} \mu_n(A) \leq \limsup_{n \to \infty} \mu_n(\bar{A}) \leq \mu(\bar{A}) = \mu(A). \] Hence \(\lim_{n \to \infty} \mu_n(A) = \mu(A)\).
(d) \(\Rightarrow\) (b).
Suppose (d) holds, and let \(F\) be any closed set.
For distinct \(\delta\)'s, the boundaries of the closed sets \(\{s \in S: p(s, F) = \delta\}\) are disjoint.
Hence only a countable number of them can have positive measure under \(\mu\), and—avoiding these—we can choose a decreasing sequence \(\{\delta_k\}\) converging to zero such that \[ \mu(\partial F_k) = 0 \quad \text{for } F_k = \{s \in S: p(s, F) = \delta_k\}, \quad k=1,2,\dots \] Since \(F \subset F_k\) for each \(k\), it follows that \(\mu_n(F) \leq \mu_n(F_k)\), all \(n, k\).
Then holding \(k\) fixed, taking the limit as \(n \to \infty\), and using (d), we have \[ \limsup_{n \to \infty} \mu_n(F) \leq \lim_{n \to \infty} \mu_n(F_k) = \mu(F_k). \] Since \(\{F_k\}\of {F_n} that converges on the points z_1, ..., z_N.
Hence the sequence {F_N}_{N=1}^\infty converges at all the points of R^d with rational coordinates.
Let G(z_i) = lim_{N→∞} F_N(z_i), i=1,2, ….
On the rest of R_0 let G(x) = inf_{s>x} G(z_i).
Clearly G satisfies property (D1) of Theorem 12.7.
To see that it satisfies (D3), first note that since each function F_N is a distribution function, (D3) holds for F_N.
Hence for a and b with rational coordinates, ∑_{i=1}^n P(a + b δ_i) = lim_{N→∞} ∑_{i=1}^n F_N(a + b δ_i) = 0, N→∞ where δ = b - a and the δ_i's are as specified before.
If a or b or both have some irrational coordinates, choose sequences s_i ↓ 0 and ε_i ↓ 0 in R^d such that a + s_i and (b - a) + ε_i have rational coordinates for each i and G(a + b δ) = lim_{i→∞} G(a + s_i + b δ + ε_i δ), i=1,2,...
Then ∑_{i=1}^n G(a + b δ) = lim_{i→∞} ∑_{i=1}^n G(a + s_i + b δ + ε_i δ) = 0.
Hence G also satisfies (D3) of Theorem 12.7.
However, G need not be continuous from above.
To make it so, define the function F by F(x) = lim_{δ→0} G(x + δ·1), x ∈ R^d, where 1 = (1, 1, ..., 1).
If G is continuous at x, then F(x) = G(x); otherwise, F(x) is the right-hand limit of G at x.
Clearly F satisfies (D1) and (D2) of Theorem 12.7.
To see that it also satisfies (D3), note that since G satisfies (D3), ∑_{i=1}^n F(a + b δ) = lim_{δ→0} ∑_{i=1}^n G(a + δ·1 + b δ) = 0.
Also, note that if F is continuous at x, then so is G, so F(x) =Let \( f \) be a continuous function on \( S \).
Note that since \( P \) has the Feller property, \( Tf \) is also continuous; and since \( S \) is compact, \( f \) is bounded.
Fix \( \varepsilon > 0 \).
Since \( \omega_{n_k} \to \omega \) and since \( f \) and \( Tf \) are both continuous, it follows that for some \( K_1 \) sufficiently large, \[ |(f, \omega_{n_k}) - (f, \omega)| < \varepsilon/3 \quad \text{and} \quad |(Tf, \omega_{n_k}) - (Tf, \omega)| < \varepsilon/3, \quad \text{all } k \geq K_1. \] Moreover, for any \( N \geq 1 \), \[ |(f, \omega_{n_k}) - (T^N f, \omega_{n_k})| = \left| \sum_{n=0}^{N-1} \left[ (f, P^n \omega_{n_k}) - (f, P^{n+1} \omega_{n_k}) \right] \right| = \left| \sum_{n=0}^{N-1} \left[ (f, P^n \omega_{n_k}) - (Tf, P^n \omega_{n_k}) \right] \right| \] here the third line uses Theorem 8.3.
Hence for some \( K_2 \) sufficiently large, \[ |(f, \omega_{n_k}) - (T^N f, \omega_{n_k})| < \varepsilon/3, \quad \text{all } k \geq K_2. \] Using the triangle inequality and the three bounds above, we conclude that for any \( \varepsilon > 0 \) there exists \( K = 1 \) such that \[ |(f, \omega_{n_k}) - (Tf, \omega)| \leq |(f, \omega_{n_k}) - (T^N f, \omega_{n_k})| + |(T^N f, \omega_{n_k}) - (T^N f, \omega)| + |(T^N f, \omega) - (Tf, \omega)| < \varepsilon, \quad \text{all } k \geq K. \] Since \( \varepsilon > 0 \) was arbitrary, it follows that \[ (f, \omega) = (Tf, \omega) = (f, T^*\omega), \tag{1} \] where the second equality again uses Theorem 8.3.
Since \( f \) is an arbitrary continuous function, (1) holds for all \( f \in C(S) \).
Hence by Corollary 2 to Theorem 12.6, \( \omega = T^*\omega \).
Notice that the example in Exercise 12.8 satisfies the hypotheses of this theorem.
That is, Theorem 12.10 does not rule out the existence of multiple invariant measures or cycles.
To rule out these possibilities and guarantee convergence of the sequence \( \{T^{*n}\mu_0\} \) to a unique invariant measure requires stronger assumptions.
Recall from Section 8.1 that for \( S \subset \mathbb{R}^d \) a transition function \( P \) on \( (S, \mathcal{S}) \) is monotone if for any bounded, increasing function \( f \), the function \( Tf \) is also increasing.
(Here we use increasing in the weak sense.) Thus we defined monotonicity of a Markov process in terms of the way the operator \( T \) acts on increasing functions.
The assumption that \( P \) is monotone is used in establishing the stronger convergence result in Theorem 12.12 below.
As with the Feller property, however, monotonicity has equivalent characterizations in terms of \( P \) or \( T^* \), and it is useful to look at them.
In particular, for our purposes it is useful to characterize monotone processes in terms of \( T^* \).
To do this, we first need to define the following partial ordering on the set \( \mathcal{P}(S, \mathcal{S}) \) of probability measures. **DEFINITION** Let \( \mu, \nu \in \mathcal{P}(S, \mathcal{S}) \).
Then \( \mu \) dominates \( \nu \) if \( (f, \mu) \geq (f, \nu) \) for any increasing function \( f \in B(S, \mathcal{S}) \).
That is, \( \mu \) dominates \( \nu \) if any bounded increasing function \( f \), when integrated against \( \mu \), gives a value that is at least as high as the one obtained when it is integrated against \( \nu \).
If \( \mu \) dominates \( \nu \), we will write \( \mu \succeq \nu \).
The following exercise shows that in \( \mathbb{R}^1 \) monotonicity of the distribution functions and dominance of probability measures are equivalent, but that in higher dimensions, the latter is stronger. **Exercise 12.9** a.
Let \( S \subset \mathbb{R}^d \) and let \( \mu, \nu \in \mathcal{P}(S, \mathcal{S}) \).
Show that if \( \mu \succeq \nu \), then the corresponding distribution functions satisfy \( F_\mu(s) \geq F_\nu(s) \), all \( s \in S \). b.
Show that for \( \mathbb{R}^1 \) the converse is also true. c.
Give an example in \( \mathbb{R}^2 \) where the converse does not hold.
The next result, which we use later, draws on this exercise.
It shows that if a sequence of probability measures is "squeezed" between two other sequences, both converging weakly to the same limit, then it also converges weakly to that limit. **Exercise 12.10** Let \( S = [a, b] \subset \mathbb{R}^1 \); and let \( \{\mu_n\}, \{\nu_n\}, \) and \( \{\lambda_n\} \) be sequences in \( \mathcal{P}(S, \mathcal{S}) \), with \( \mu_n \preceq \lambda_n \preceq \nu_n \), all \( n \).
Show that if \( \mu_n \Rightarrow \mu \) and \( \nu_n \Rightarrow \mu \), then \( \lambda_n \Rightarrow \mu \). [Hint.
Let \( \{F_{\mu_n}\}, \{F_{\nu_n}\}, \{F_{\lambda_n}\} \) and \( \{F_\mu\} \) be the distribution functions corresponding to \( \{\mu_n\}, \{\nu_n\}, \{\lambda_n\} \) and \( \{\mu\} \) respectively, and let \( C \subset [a, b] \) be the set of points at which \( F_\mu \) is continuous.
Use part (a) of Exercise 12.9 and Theorem 12.8.] Using the notion of dominance for probability measures, we have the following alternative characterizations of monotonicity for a Markov process in terms of \( T^* \) and \( \succeq \). **Exercise 12.11** Show that the following statements are equivalent: a. \( f \in B(S, \mathcal{S}) \) and \( f \) increasing implies \( Tf \) increasing (monotonicity); b. \( \mu, \nu \in \mathcal{P}(S, \mathcal{S}) \) and \( \mu \succeq \nu \) implies \( T^*\mu \succeq T^*\nu \); and c. \( s, s' \in S \) and \( s \preceq s' \) implies \( P(s, \cdot) \preceq P(s', \cdot) \). [Hint.
Use Theorem 8.3.] This exercise shows that a Markov process is monotone if and only if \( T^* \) preserves dominance relationships between probability measures.
We call a sequence \( \{\mu_n\} \) of probability measures monotone if they are ordered by dominance, that is, if \( \mu_{n+1} \succeq \mu_n \), all \( n \), or \( \mu_{n+1} \preceq \mu_n \), all \( n \).
The next exercise shows that if \( S \) is a closed, bounded rectangle \( [a, b] \subset \mathbb{R}^d \) and if \( P \) is monotone and has the Feller property, then the sequences \( \{T^{*n}\delta_a\} \) and \( \{T^{*n}\delta_b\} \) converge weakly to invariant measures. **Exercise 12.12** Let \( S = [a, b] \subset \mathbb{R}^d \).
Show that if \( P \) is monotone and has the Feller property, then the sequences \( \{T^{*n}\delta_a\} \) and \( \{T^{*n}\delta_b\} \) are monotone increasing and decreasing sequences respectively, and they converge weakly to (possibly different) invariant measures. [Hint.
Use monotonicity to show that each sequence converges weakly.
Then use the Feller property to show that each limit is an invariant measure.] Are the hypotheses of Exercise 12.12—compactness, monotonicity, and the Feller property—enough to ensure weak convergence to a unique invariant measure?
The following example shows that they are not: there still may be multiple ergodic sets. **Exercise 12.13** Let \( S = [a, b] \subset \mathbb{R}^1 \), and let \( h: S \to S \) and \( H: S \to S \) be the two functions shown in Figure 12.4.
Consider the following transition function: \[ P(s, A) = \frac{\lambda(A \cap [h(s), H(s)])}{\lambda([h(s), H(s)])}, \] where \( \lambda \) denotes Lebesgue measure on \( \mathbb{R}^1 \).
That is, for each \( s \in S \), \( P(s, \cdot) \) is the measure corresponding to a uniform density on the interval \( [h(s), H(s)] \). a.
Show that \( P \) is monotone and has the Feller property. b.
Show that the indicated sets \( E_1 \) and \( E_2 \) are distinct ergodic sets, and that the set \( F \) is a transient set. c.
Show that the sequences \( \{T^{*n}\delta_a\} \) and \( \{T^{*n}\delta_b\} \) do not have the same limit.
Exercise 12.13 shows that to ensure uniqueness of the invariant measure, we must impose enough "mixing" on the transition function to rule out the kind of behavior shown in Figure 12.4.
This is done in Assumption 12.1 below.
Lemma 12.11 then shows that if this condition holds, the expected value of any bounded, measurable, nondecreasing function is bounded above and below in a particular way.
Theorem 12.12 then draws on this result to establish sufficient conditions for uniqueness of the invariant measure \( \mu^* \), and weak convergence of the sequence \( \{T^{*n}\mu_0\} \) to \( \mu^* \) for any initial probability measure \( \mu_0 \). **ASSUMPTION 12.1** There exists \( c \in S \), \( \delta > 0 \), and \( N \geq 1 \) such that \( P^N(a, [c, b]) \geq \delta \) and \( P^N(b, [a, c]) \geq \delta \). **Exercise 12.14** Show that if \( P \) is monotone and satisfies Assumption 12.1 for \( (c, \delta, N) \), then \[ P(s, [a, c]) \geq \delta \quad \text{and} \quad P(s, [c, b]) \geq \delta, \quad \text{all } s \in S. \] **LEMMA 12.1** Let \( S = [a, b] \subset \mathbb{R}^1 \).
Assume that \( P \) is monotone and satisfies Assumption 12.1 for \( (c, \delta, N) \).
Then for any bounded, measurable, nondecreasing function \( f \), \[ \delta f(c) + (1 - \delta) f(a) \leq (T^* f)(s) \leq \delta f(c) + (1 - \delta) f(b), \quad \text{all } s \in S. \tag{2} \] **Proof.** Let \( A = [a, c] \); then by Assumption 12.1 and Exercise 12.14, \( P^N(s, A) \geq \delta \), all \( s \in S \).
Hence \[ (T^N f)(s) = \int_S f(s') P^N(s, ds') = \int_A f(s') P^N(s, ds') + \int_{A^c} f(s') P^N(s, ds') \] \[ \geq f(c) P^N(s, A) + f(a) P^N(s, A^c) \geq \delta f(c) + (1 - \delta) f(a), \] where the last line uses the fact that \( f(c) \geq f(a) \) and \( P^N(s, A) \geq \delta \).
This establishes the first inequality in (2); a similar argument establishes the second.
We are now ready to prove our final result. **THEOREM 12.12** Let \( S = [a, b] \subset \mathbb{R}^1 \).
If \( P \) is monotone, has the Feller property, and satisfies Assumption 12.1, then \( P \) has a unique invariant probability measure \( \mu^* \), and \( T^{*n}\mu_0 \Rightarrow \mu^* \), all \( \mu_0 \in \mathcal{P}(S, \mathcal{S}) \). **Proof.** By Exercise 12.12, the sequences \( \{T^{*n}\delta_a\} \) and \( \{T^{*n}\delta_b\} \) both converge weakly, and their limits \( \mu^* \) and \( \nu^* \) are invariant measures.
Since \( \delta_b \succeq \mu_0 \succeq \delta_a \), all \( \mu_0 \in \mathcal{P}(S, \mathcal{S}) \), and \( T^* \) is monotone, it follows that \[ T^{*n}\delta_b \succeq T^{*n}\mu_0 \succeq T^{*n}\delta_a, \quad n = 1, 2, \ldots, \quad \text{all } \mu_0 \in \mathcal{P}(S, \mathcal{S}). \]where the last line uses Theorem 7.1 and the fact that {E,(ε)} is a decreasing sequence with n 忌 1Exs) = 0.
Since this holds for every s > 0 not in the countable set A, it follows that (1) holds. a 12.7 Bibliographic Notes Our discussion of weak convergence in Section 12.1—12.3 is based on Billingsley (1968, chap. 1 and app.
II), which is an excellent source for results on weak convergence in a variety of spaces.
Billingsley (1979, chap. 5) contains much complementary material, including a good discussion of Helly’s Theorem.
Feller (1971, chap.
VIII) contains a good discussion of convergence of distribution functions.
A one-dimensional version of Theorem 12.12, the monotonicity result in Section 12.4, is proved in Theorem 1 of Razin and Yahav (1979).
Hopenhayn and Prescott (1987) strengthen this result by dropping the assumption that the transition function has the Feller property.
See Torres (1988) for an excellent discussion of monotonicity in its various forms.
The analysis in Section 12.5 follows closely that in Manuelli (1985).
## 13 Applications of Convergence Results
for Markov Processes This chapter consists of applications of the convergence results for Markov processes reviewed in Chapters 11 and 12.
Some of the economic models discussed here were introduced in Chapter 10, and we draw on results established there; others are new. 13.1 A Discrete-Space (s, S) Inventory Problem The linear inventory problem discussed in Section 5.14 can also be formulated with stochastic demand.
Let the manager begin the period with a stock x.
He must immediately decide whether to place an order or not.
If he does order, he can bring his stock up to any level y at a cost of co + ( — x).
After this decision is made, total demand for the product, call it z is drawn from a known distribution.
The manager then earns revenues of pz if his inventory exceeds z, and p times his inventory otherwise.
Itis a natural conjecture, on the basis of the analysis in Section 5.14, that the solution to this problem takes the form of an (s, S) policy, where s is the stock level below which it is optimal to place an order and S is the Optimal size of total inventories after an order is placed.
But this conjecture is false unless more structure is placed on the distribution of demand.
In this section we add such structure.
We study an integer version of the problem that is similar to the one studied in Section 5.15 and examine the dynamics of the finite-state Markov chain that optimally managed inventories follow.
In Section 13.2 we consider a situation in which demand has a continuous distribution.
There we simply assume that an (s, S) policy is followed—ignoring the question of whether it is optimal— and study the resulting Markov process. 389 Let product demand z take on the value 1 with probability θ, or 0 with probability 1 — θ.
We consider integer-valued stocks only: x = 0, 1, 2,....
Then clearly an optimal policy has s = 0: there is no reason for the manager to place an order before he has stocked out, since one unit meets the maximum possible demand.
Let v(x) be the expected, present discounted value of profits if the current stock is x and an optimal ordering policy is followed.
Then v must satisfy the functional equation (1) v(x) = θ[p + βv(x − 1)] + (1 − θ)βv(x), x = 1,2,..., and the value v(0) must satisfy (2) v(0) = max [−co − cy + v(y)). y∈{1,2,..} Exercise 13.1 a.
Show that under suitable restrictions on the parameters of the problem there is a function v satisfying (1) and (2), and a finite optimal order size S that solves (2).
Characterize S in terms of co, 1, β, p, and θ.
Given S, optimally managed inventories are a Markov process with the state space {0, 1, 2, .. }.
Exercise 13.1 _b.
What is the transition matrix for this process?
What are the ergodic and transient sets?
Are there any cyclically moving subsets? c.
Prove that this process has a unique invariant distribution and that the system converges to it from any initial distribution.
Characterize this invariant distribution in terms of S. 13.2 A Continuous-State (s, S) Process In this section we retain the other features of the model above but assume that demand takes values in the interval Z = [0, Z].
It is easy enough to write out the functional equation for this problem (try it), but, as one might guess from Section 5.14, the analysis is hard going.
Here we simply assume that an (s, S) policy is followed and focus on characterizing the dynamics of inventories given this assumption.
Let ℬ denote the Borel sets of Z, and let L be a probability measure on (Z, ℬ).
Assume that the sequence of demands {zₜ} is i.i.d., with common distribution H each period.
It is natural to assume that s < Z (why?), and we will do so.
Under these assumptions, inventories {xₜ} are a Markov process with state space X = [0, ∞).
In particular, max {xₜ − zₜ, 0} if xₜ > s, (1) xₜ₊₁ = max {S − zₜ, 0} otherwise.
Exercise 13.2 a.
Write the transition probability P(x, A) corresponding to (1) for the case when A is an interval.
Show that this is sufficient to define a transition function on (X, 2^X).
Does P have the Feller property?
As in the last section, the ergodic set for this problem is [0, S] and the transient set is (S, ∞).
Since any invariant measure for the process is concentrated on [0, S], it is convenient to begin by studying the process on the smaller state space consisting of [0, S] and its Borel subsets.
After studying the convergence of the process on this state space, we can treat behavior on (S, ∞) by side arguments.
This simplifying device is a standard.
For this process, we can apply Theorem 11.12 to prove that there exists a unique invariant measure μ*, and that for any initial measure on [0, S], the sequence {P^t μ} converges strongly to μ*.
We do this by verifying the hypotheses of Condition M via the sufficient condition given in Exercise 11.5a.
Exercise 13.2 b.
Show that there is an integer N = 1 and an δ > 0 such that P^N (x, {0}) > δ, all x ∈ [0, S]. 13.3 The One-Sector Model of Optimal Growth Consider again the stochastic growth model with independent shocks studied in Section 10.1.
For present purposes it is convenient to take Output rather than the capital stock as the state variable and to use the second of the two formulations of a stochastic dynamic programming problem introduced in Section 9.1.
The functional equation for the optimal growth problem is then (1) v(x) = max_{0≤y≤x}[u(x−y) + β ∫ v(f(y)z) H(dz)].
Thus x is the quantity of output available (after production has taken place) in the current period, y is the quantity carried over as capital to be used in production next period, and x — y is the quantity consumed.
Next period, a shock z to the technology is drawn from the distribution H.
Then f(y)z units of output are available next period, the new state.
We maintain Assumptions (U1)—(U5) from Section 5.1 on preferences and Assumptions (Z1)—(Z2) from Section 10.1 on the shocks.
We add the following assumption, which ensures that H assigns positive probability to all nondegenerate subintervals of Z = [1, b]: (Z3) for some a > 0, H((a, b]) = a(b − a), all (a,b] ⊂ Z.
We also maintain Assumptions (T1)—(T5) from Section 5.1 on the production function f, with the following important exception.
We modify (T2) so that positive output is producible even with no capital: f(0) > 0.
We also assume that βf’(0) > 1.
The reason for these two assumptions will soon be clear.
As we did in Section 10.1, let x̄ > 0 be the unique value satisfying x̄ = Zf(x̄); and let X = (0, x̄], with its Borel subsets 𝒳.
Exercise 13.3 a.
Show that there is a unique bounded continuous function v: X → R satisfying (1) and that v is strictly increasing and strictly concave.population change from period to period.
In such a case the invariant measure for the Markov process of interest describes the population every period as well as the experience of each individual averaged over time.
In this section we study an economy of this type in which currency is the only security held.
Consider an economy with a large number of households, each composed of one worker and one shopper.
In each period each worker produces y units of consumption goods.
However, a household cannot consume what it produces itself; rather, it must sell what it produces to other households and purchase what it consumes from other households.
Trading takes place as follows.
Each worker-shopper pair begins the period with some initial holdings of fiat money.
The shopper goes out and uses all or part of this money to buy goods from other households.
The worker stays at home and produces y units of output, which he or she sells to other households in exchange for fiat money.
Consumption occurs at the end of the period when the shopper returns.
Unspent currency plus receipts from the sale of goods determine the pair's initial cash balances at the beginning of the next day.
There is no technology for enforcing credit contracts; hence no household is willing to extend credit.
All households have identical preferences ex ante, but each period each pair experiences a stochastic shock to its preferences.
These shocks take values in a closed interval on the real line and will be denoted by z ∈ Z = [z, z].
The shocks are independent over time and across households.
Let ℬ be the Borel sets of Z, and let L be a probability measure on (Z, ℬ), describe the distribution of the shocks.
A pair's preferences are given by E[S u(c, z)], where 0 < δ < 1 and where U:R+ × Z → R is bounded and continuously differentiable.
Assume, in addition, that for each fixed z ∈ Z, U(·, z) is strictly increasing and strictly concave and that for each fixed c ∈ R+, U_z(c, ·) is strictly increasing in z.
That is, larger values of z are associated with higher marginal utilities at every level of consumption.
We require L to satisfy the same assumption we used in Section 13.3: for some α > 0, L((a, b]) = a(b − a), all (a, b] ⊂ Z.
Assume that the price level p is constant over time, and consider the decision problem facing a typical household.
Let M denote their beginning-of-period nominal money balances, and let m = M/p denote their real balances.
Then their decision problem can be written as (1) v(m, z) = max [u(c) + δ ∫_Z v(m', z') w(dz')] c,m' subject to m' ≤ m + y − c, and c ≤ m.
The first constraint is that real balances at the beginning of next period plus current consumption cannot exceed current real balances plus real income from the sale of goods.
(Note that both purchases and sales of goods have a real price of unity.) The second constraint is that the shopper's expenditures on the consumption good cannot exceed the pair's beginning-of-period cash balances.
This constraint reflects the fact that, under the given description of trading, it is impossible for the pair to use currency obtained from the sale of current-period goods for the purchase of current-period goods.
Current-period receipts can be used only for the purchase of goods in future periods.
The dynamic programming problem in (1) can be studied using the techniques developed in Chapter 9.
The next exercises establish the main facts about (1).
Exercise 13.5 a.
Show that there is a unique bounded continuous function v satisfying (1). b.
Show that for each z ∈ Z, v(·, z) is strictly increasing, strictly concave, and continuously differentiable in m. [Hint.
To establish differentiability at the point where the cash-in-advance constraint just binds, show that the left and right derivatives are equal.] c.
Show that there is a continuous function g(m, z) describing end-of-period real balances.
In order to study the evolution of a pair's real balances over time, we must characterize the policy function g more sharply.
Since c(m, z) = m + y − g(m, z), this argument will also characterize the optimal consumption policy.
Exercise 13.5. d.
Show that for each fixed z ∈ Z, there exists some m(z) > 0 such that g(·, z) = y on [0, m(z)], and g(·, z) is strictly increasing on [m(z), ∞). 1/3 4/2 9/2 Figure 13.1 e.
Show that for each fixed z ∈ Z, c(·, z) is strictly increasing on [0, ∞) and hence that m₁ > a implies 0 ≤ g(m₁, z) − g(m₂, z) ≤ m₁ − m₂. f.
Show that there exists m̄ > 0 such that g(m̄, z) = m̄. g.
Show that m(z) = y.
That is, g(·, z) = y on [0, y]. h.
Show that for each m > 0, g(m, ·) is weakly decreasing in z.
These exercises establish that the policy function g has the qualitative features displayed in Figure 13.1: the functions g(·, z) are ordered, as shown; each is constant on an interval [0, m(z)] and strictly increasing with a slope less than unity on [m(z), ∞); and each cuts the 45° line.
By Theorem 8.9, the function g and the measure L together define a transition function P on (R+, ℬ).
Evidently the ergodic sets of this process are contained in the set X = [y, m̄], so it is convenient to treat X with its Borel subsets 𝒜 as the state space of the process.
Exercise 13.5 i.
Show that the Markov process on (X, 𝒜) defined by P—that is, by g and L—satisfies the hypotheses of Theorem 12.12.
Let π* denote the unique stationary probability measure on (X, 𝒜).
The analysis thus far has dealt with consumption and real balances for a single household, with the price level p exogenously fixed and constant over time.
Next we will show how the equilibrium price level p is determined for a long-run stationary equilibrium.
Let M̄ be the (exogenously given) per capita supply of nominal money balances.
In market equilibrium in this economy the per capita demand for real cash balances, averaged over households, must equal per capita balances supplied M̄/p.
But in the long run the average per capita demand over households is given by the stationary probability measure π*.
Hence p must satisfy ∫_X m π*(dm) = M̄/p.
Exercise 13.5 j.
Show that (2) holds if and only if p satisfies ∫_X ∫_Z g(m, z) L(dz) π*(dm) = M̄ where g is the pair's optimal policy function.
Note that if the initial distribution of money balances across households is different from π*, then the price level will not be constant over time.
To study the evolution of the price level in this case, one would need to go back and re-solve the household's problem for situations where the price level is changing over time.
This would not be an easy exercise. 13.6 A Pure Currency Economy with Linear Utility The model of the last section has an intriguing structure when utility is linear, and in this case both the value function and the invariant measure can be calculated explicitly.
Let Z = [0, 1], and let U(c, z) = zc.
Note that because U is unbounded, this model is not quite a special case of the last one.
Hence we must analyze it from scratch.
The household's functional equation is now (1) v(m, z) = max [zc + δ ∫_Z v(m', z') w(dz')] c,m' subject to m' ≤ m + y − c, and c ≤ m.
Exercise 13.6 a.
Prove that for some ¢ ∈ (0, 1) and A > 0, v(m, z) =  { z m + A if z = ¢, { z m + A z if z < ¢ satisfies (1), and g(m, z) = { m + A if z = ¢, { y if z < ¢ is the associated policy function.
Characterize ¢ and A in terms of L and δ.
Let X = [y, ∞), with its Borel subsets 𝒜.
The policy function g and the measure L define a transition function on (X, 𝒜).
Exercise 13.6 b.
Prove that the ergodic set for this process consists of y and its integer multiples.
In view of (b), the invariant distribution is a discrete probability distribution {π_i}_{i=1}^∞, where π_i = Pr{m = y i}.
Exercise 13.6 c.
Calculate π_i, i = 1,2,.....(7) u(x,z;θ)=θ and g(x,z,θ)=0, all(x,z) ∈ X × Z.
Let θ be the smallest θ such that (7) holds.
Let Θ = (0, θ̲).
Show that for all θ ∈ Θ, v(·,·; θ) is such that (2a) and (2c) hold over some regions of the state space.] There are other conditions that might be employed in order to ensure uniqueness.
For example, there may be a few workers that enter or leave the work force for reasons other than current market conditions.
Exercise 13.8 e.
Modify the model so that each period a fraction γ of the workers currently on the island leave for idiosyncratic reasons such as health.
Establish that the invariant measure is unique in the model so modified.
In Exercise 13.8d we have obtained a complete characterization of the stationary equilibrium in the economy composed of one island and two continents, taking as given the value of the parameter θ.
We now return to the economy consisting of a continuum of islands, all with the same structure as the island just studied, with productivity shocks that are independent across islands.
To determine the equilibrium in this system, we reinterpret the parameter θ as the present value of earnings for a worker who migrates to the best available alternative island.
As in the analysis just completed, individual workers treat θ as given to them; for each worker, it plays the role of a competitive market price.
Thus, the analysis of the functional equation (4) and of the Markov process it gives rise to continue to apply, both conditional on θ.
But now we wish to determine θ endogenously, as the value that equates the average work force on an island to the exogenously given average population per island, N.
Let λθ denote the invariant measure found in Exercise 13.8d, where the notation emphasizes its dependence on θ.
We seek a value for θ such that D(θ) = ∫ ωr ∂λθ(∂x ∂z) = N.
To establish the existence of a value θ satisfying this equation, we first establish the following facts.
Exercise 13.8 f.
Show that D(θ) = x and that for some θ sufficiently large, θ = θ implies D(θ) = 0. g.
Show that D is continuous by verifying the hypotheses of Theorem 12.13.
We can establish that there is at most one positive equilibrium value for θ by showing that D(θ) is strictly decreasing for θ > 0.
Let Tθ be the Markov operator associated with Pθ, and let Tθ* be its adjoint.
We have shown, in Exercise 13.8c, that D(θ) = ∫ x ∂λθ(∂x ∂z) = lim { x (Tθ*μ0)(∂x ∂z), for any initial measure μ0 on X × X.
(Why?) Then it follows from Theorem 8.3 that D(θ) = lim ∫ (Tθ^n μ0)(∂x ∂z).
Exercise 13.8 h.
Use the definition of Tθ in terms of the policy function gθ(x, z) to show that D(θ) is nonincreasing.
How can this argument be strengthened to show that D(θ) is strictly decreasing when θ > 0? 13.9 Bibliographic Notes Scarf (1959) contains counterexamples to the conjecture that the stochastic linear inventory problem always has a solution of the (s, S) form.
That paper also provides conditions on the probability measure p for the shocks that are sufficient to ensure that an (s, S) policy is optimal.
Iglehart (1963) also provides sufficient conditions for the optimality of (s, S) policies.
Caplin (1985) analyzes a Markov chain arising from (s, S) policies in a formulation that is more general than the one in Section 13.1.
Section 13.2 is in the spirit of chapter 14 of Arrow, Karlin, and Scarf (1958), where characteristics of the stochastic processes for inventories are derived taking the parameters s and S as given.
Examples of explicit solutions for the invariant distributions of such processes are also provided.
The stochastic growth model in Section 13.3 is taken from Brock and Mirman (1972).
See also the other references in Section 10.13.
The proof of convergence used here, based on monotonicity, is from Razin and Yahav (1979).
Brock and Mirman provide an argument that also applies when f (0) = 0.
Majumdar and Radner (1983) study the existence of stationary equilibria in a much more general setting.
The model of industry investment under uncertainty in Section 13.4 is from Lucas and Prescott (1971).
The convergence argument here, based on monotonicity, is new.
Sargent (1980) studies a general equilibrium investment problem in which the nonnegativity constraint on gross investment is crucial.
The model of a pure currency economy in Section 13.5 is taken from Lucas (1980).
See also the earlier, similar model of Foley and Hellwig (1975).
Again, the convergence proof here is new.
The linear utility version in Section 13.6 is from Taub (1988a).
Taub (1988b) studies a credit economy similar to the one studied in Section 13.7.
The model of the search economy in Section 13.8 is based on Lucas and Prescott (1974), but the analysis here is quite different.
## 14 Laws of Large Numbers
In Chapters 11 and 12 we developed methods for characterizing the long-run behavior of a recursive system in terms of the sequence of probability measures on the state space in successive periods implied by the model.
As the applications in Chapter 13 showed, this type of analysis gives a good deal of insight into the outcomes such models generate.
By itself, however, it does not form a basis for systematic empirical work.
In this chapter we carry the analysis a little further and show how recursive models can be used as the bases for empirical studies.
Suppose that we are interested in whether a certain model is consistent with a set of data, where the data are simply time series for some observable function(s) of the state.
That is, the data are sequences of the form {f(sₙ)}, where sₙ is the state in period n, and where f: S → ℝ is a fixed, real-valued function.
Then we must decide what properties for such sequences are implied by the theoretical model.
To study this issue, we adopt the same framework we used in Chapters 11 and 12.
Let (S, Σ) be a measurable space; let A(S, Σ) be the space of probability measures on (S, Σ); let P be a transition function on (S, Σ); and let T* be the operator on probability measures associated with P (cf.
Section 8.1).
Given an arbitrary initial probability measure μ0, define the sequence {μₙ} recursively by μₙ₊₁ = T*μₙ, n = 0, 1,....
In Chapters 11 and 12 we developed conditions on (S, Σ) and P sufficient to ensure the strong and weak convergence of the sequence of averages {(1/N) Σₙ₌₁ᴺ μₙ} or the sequence {μₙ} itself to an invariant probability measure—a fixed point of T*.
Thus, Chapters 11 and 12 dealt with the convergence of sequences of probability measures, objects that are not directly observable.
Suppose that the sequence {(1/N) Σₙ₌₁ᴺ μₙ} converges weakly to a unique invariant probability measure μ*, for all μ₀.
Then for any continuous function f and any initial state s₀, it is natural to take the expected 414 value ∫ f dμ* as a prediction about the long-run average behavior of the observed values of f, that is, as a prediction about (1/N) Σₙ₌₁ᴺ f(sₙ) as N → ∞.
In this chapter we develop the language needed to make this statement more precise and provide conditions under which the desired conclusion holds.
To begin, we need several definitions.
Let (Ω, ℱ, μ) be a probability space, and let {fₙ}∞ₙ₌₁ and f be random variables (measurable, real-valued functions) on (Ω, ℱ).
Recall that we say that {fₙ} converges to f almost everywhere (a.e. or μ-a.e.) if there is a set A ∈ ℱ with μ(A) = 0 such that lim fₙ(ω) = f(ω), all ω ∈ A^c.
In probabilistic settings this is also referred to as convergence almost surely (a.s.).
In this chapter we will also make use of a weaker notion of convergence for such a sequence.
We say that {fₙ} converges to f in probability (in pr.) if lim μ({ω ∈ Ω : |fₙ(ω) - f(ω)| > ε}) = 0, all ε > 0.
This limiting property is also called convergence in measure.
Notice that both definitions require that we specify in advance a fixed probability measure μ on (Ω, ℱ); let E(·) denote integration with respect to this fixed measure.
If the sequence of random variables {f_n} is such that 1 N --- N⁻¹ Σ f_n → μ a.s. as N → ∞,      (1) n=1 we say that {f_n} satisfies a weak law of large numbers.
If the convergence in (1) is a.e., we say that {f_n} satisfies a strong law of large numbers.
Our objective in this chapter is to establish a strong law for Markov processes.
To do this, we must first decide how such a law is to be stated.
Let (S, 𝒮), P, and π₀ be given; let [S^ℕ, 𝒮^ℕ(s₀, ·)] = (Ω, ℱ, P^{s₀}) be the probability space of infinite sequences defined in Section 8.2; and for each ω = (s₀, s₁, s₂, ...) ∈ Ω, let X_n(ω) = s_n denote the nth component of ω.
Then for any function f: S → ℝ, define the sequence of functions f_n: Ω → ℝ by f_n(ω) = f[X_n(ω)] = f(s_n), n = 1, 2, ....
Now suppose that (S, 𝒮) and P are such that {(1/N) Σ_{n=1}^N 1_{A}(s_n)} converges weakly to a unique invariant probability measure π_A^*(s₀), for all A ∈ 𝒮.
Then in particular, that sequence converges if π₀ puts probability one on the point s₀.
Hence N lim_{N→∞} E^{s₀}[f_N] = lim_{N→∞} E^{s₀}[Σ_{n=1}^N f(s_n)]/N N→∞ = lim_{N→∞} ∫_S f(s) dπ_A^*(s₀)(s) = ∫_S f(s) dπ^*(s), where E(·) denotes integration with respect to P^{s₀}.
Since s₀ and f were arbitrary, (2) holds for all s₀ ∈ S and f ∈ C(S).
Hence we say that a Markov process satisfies a strong law of large numbers if it has the weak convergence property described above and if (3) lim_{N→∞} (1/N) Σ_{n=1}^N f(s_n) - ∫_S f(s) dπ^*(s) = 0 a.e., all f ∈ C(S), all π₀ ∈ 𝒫.
In this chapter we show that (3) holds if S is a compact set in a finite-dimensional Euclidean space and the transition function P has the Feller property.
In Section 14.1 we develop a series of laws of large numbers, dealing first with uncorrelated random variables and then with variables that display a certain type of correlation.
Then in Section 14.2 we apply the latter result to Markov processes.
Some of the arguments developed in this chapter are rather long and difficult, and none of them will be used elsewhere in the book.
Thus, skipping this chapter on first reading causes no loss in continuity. 14.1 Definitions and Preliminaries In this section we prove several laws of large numbers, culminating in a strong law of large numbers for a class of correlated random variables.
We begin with a series of preliminary results, Lemmas 14.1–14.3, that 14.1 Definitions and Preliminaries 417 provide alternative sufficient conditions for convergence a.e.
Then in Theorem 14.4 we use Chebyshev’s inequality to prove a weak law of large numbers for uncorrelated random variables, and in Theorem 14.5 we strengthen this result to obtain a strong law.
Finally, in Theorem 14.6 we provide a strong law for a class of correlated random variables, a result we draw on in the next section to prove a strong law for Markov processes.
Throughout this section, we take (Ω, ℱ, μ) to be a fixed probability space and let E(·) denote integration over Ω with respect to the measure μ.
That is, for any random variable f on (Ω, ℱ), E(f) = ∫_Ω f dμ.
We also adopt a shorthand notation, standard in probability theory, and use μ({f has property X}) to denote μ({ω ∈ Ω: f(ω) has property X}).
Our first result is an alternative characterization of convergence a.e.
### LEMMA 14.1
f_n → f a.e. if and only if (1) lim_{m→∞} μ({ sup_{n ≥ m} |f_n − f| = 0 }) = 1, all ε > 0.
**Proof.** Define the sets A = {ω: lim_{n→∞} f_n(ω) = f(ω)} and A_m(ε) = {|f_n − f| < ε, all n ≥ m}, all ε > 0, m = 1, 2, ....
Then to prove the lemma, it suffices to show that μ(A) = 1 if and only if lim_{m→∞} μ[A_m(ε)] = 1, all ε > 0.
First note that for any fixed ε > 0, {A_m(ε)} is a nested increasing sequence of sets.
Note, too, that if ω ∈ A, then ω ∈ A_m(ε) for all m sufficiently large.
Hence A ⊆ ∪_{m=1}^∞ A_m(ε).
Suppose that μ(A) = 1.
Then using Theorem 7.1, we find that 1 = lim_{m→∞} μ[A_m(ε)] = μ(∪_{m=1}^∞ A_m(ε)) ≥ μ(A) = 1, all ε > 0.
Conversely, suppose that lim_{m→∞} μ[A_m(ε)] = 1, all ε > 0.
Let A(ε) = ∪_{m=1}^∞ A_m(ε).
Then Theorem 7.1 implies that 1 = μ(∪_{m=1}^∞ A_m(ε)) = lim_{m→∞} μ(A_m(ε)) = 1, all ε > 0. m=1 m=1 Let {ε_k} be a decreasing sequence converging to zero.
Then {A(ε_k)} is a nested decreasing sequence of sets, and A = ∩_{k=1}^∞ A(ε_k).
Hence, applying Theorem 7.1 again, we obtain μ(A) = μ(∩_{k=1}^∞ A(ε_k)) = lim_{k→∞} μ(A(ε_k)) = 1.
Let {A_n} be any sequence of sets in ℱ.
Then we define the measurable set lim sup A_n by lim sup A_n = ∩_{m=1}^∞ ∪_{n=m}^∞ A_n.
Thus ω is an element of lim sup A_n if and only if it is contained in an infinite number of the sets A_n.
Stated a little differently, the event lim sup A_n occurs if and only if infinitely many of the events in the sequence {A_n} occur.
In this case we say that the events A_n occur infinitely often (i.o.).
Note that {∪_{n=m}^∞ A_n} is a nested, decreasing sequence of sets.
Hence (2) μ(A_n i.o.) = μ(lim sup A_n) = μ(∩_{m=1}^∞ ∪_{n=m}^∞ A_n) = lim_{m→∞} μ(∪_{n=m}^∞ A_n), where the last step uses Theorem 7.1.
The next lemma, a fairly immediate consequence of (2) and Lemma 14.1, provides a slightly different characterization of convergence a.e.
### LEMMA 14.2
f_n → f a.e. if and only if μ(|f_n − f| ≥ ε i.o.) = 0, all ε > 0. 14.1 Definitions and Preliminaries 419
**Proof.** Let A_n(ε) = {|f_n − f| ≥ ε}, n = 1, 2, ..., all ε > 0.
Then (2) implies that μ(|f_n − f| ≥ ε i.o.) = μ(A_n(ε) i.o.) = lim_{m→∞} μ(∪_{n=m}^∞ A_n(ε)), all ε > 0.
Hence by Lemma 14.1, it suffices to show that (1) holds if and only if lim_{m→∞} μ(∩_{n=m}^∞ A_n(ε)^c) = 0, all ε > 0.
This conclusion follows directly from the fact that {|f_n − f| < ε, all n ≥ m} = (∩_{n=m}^∞ A_n(ε)^c) = (∪_{n=m}^∞ A_n(ε))^c, m=1,2,..., all ε > 0.
The next result draws on this lemma to provide a sufficient condition for convergence a.e.
### LEMMA 14.3
If Σ_{n=1}^∞ μ(|f_n − f| > ε) < ∞, all ε > 0, n=1 then f_n → f a.e.
**Proof.** By Lemma 14.2, it suffices to show that for any sequence of sets {A_n} in ℱ, Σ_{n=1}^∞ μ(A_n) < ∞ implies μ(A_n i.o.) = 0. n=1 To establish the latter, note that for any sequence of sets {A_n} in ℱ, μ(∪_{n=m}^∞ A_n) ≤ Σ_{n=m}^∞ μ(A_n), m=1,2,.... 420 14 Laws of Large Numbers Moreover, Σ_{n=1}^∞ μ(A_n) < ∞ implies lim_{m→∞} Σ_{n=m}^∞ μ(A_n) = 0. n=1 Hence using (2), we have μ(A_n i.o.) = lim_{m→∞} μ(∪_{n=m}^∞ A_n) ≤ lim_{m→∞} Σ_{n=m}^∞ μ(A_n) = 0.
It follows directly from Lemma 14.1 that convergence almost everywhere implies convergence in probability; so a “strong law” is indeed stronger than a “weak law.” The converse, however, is not true.
Exercise 14.1 Let (Ω, ℱ, μ) be the unit interval [0, 1), with the Borel subsets and Borel measure.
For each n = 1, 2, ... and 1 ≤ i ≤ n, define 1 if ω ∈ [(i − 1)/n, i/n) f_{n,i}(ω) = {0 otherwise.
Consider the sequence of random variables (f_{1,1}, f_{2,1}, f_{2,2}, f_{3,1}, f_{3,2}, f_{3,3}, ...). a.
Show that this sequence does not converge at any point of Ω and, hence, does not converge a.e. b.
Show that this sequence converges in pr. to the random variable that is identically zero. c.
Identify a subsequence that converges a.e.
Exercise 14.2 Let (Ω, ℱ, μ) be a probability space and let {f_n} and f be random variables. a.
Let {ε_n} be a sequence of positive numbers converging to zero.
Show that if Σ_{n=1}^∞ μ(|f_n − f| > ε_n) < ∞, then f_n → f a.e. [Hint.
Adapt the proof of Lemma 14.3.] b.
Show that if f_n → f in pr., then there exists a subsequence {f_{n_k}} converging to f a.e. [Hint.
Let k > 1 satisfy μ(|f_{n_k} − f| > 1/k) ≤ 1/2^k.
Then define the sequence {n_k} inductively by n_k > n_{k-1} and μ(|f_{n_k} − f| > 1/k) ≤ 1/2^k, and apply the result in part (a).] 14.1 Definitions and Preliminaries 421 We turn next to three laws of large numbers.
Theorems 14.4 and 14.5 are weak and strong laws respectively for uncorrelated random variables.
These are presented to make clear the ideas behind the proof of Theorem 14.6, a strong law for a class of correlated random variables, which is the result we draw on in the next section.
The proof of Theorem 14.4 uses the fact that for any random variable h with E(h²) < ∞, E(h²) = ∫_{|h| ≥ ε} h² dμ + ∫_{|h| < ε} h² dμ ≥ ε² ∫_{|h| ≥ ε} dμ = ε² μ(|h| ≥ ε), all ε > 0, from which it follows that (3) μ(|h| ≥ ε) ≤ E(h²)/ε², all ε > 0.
This fact is called Chebyshev’s inequality.
We also need to recall the definition of uncorrelated random variables.Our next result draws upon Lemmas 14.11 and 14.12.
### LEMMA 14.13
(Norms Ergodic Lemma) Let X be a normed linear Space; let T: X — X be a linear operator with ||T|| = 1; and let the operators Fn be defined by (8).
Suppose that x € X is a fixed point of T and that x € X satisfies (9) lim (Hnx, w) = (x, w), all w © X*.
Then lim ||x − T^nx|| = 0.
**Proof.** Let X, T, and {Hn} be as specified, and let I: X 一 X be the identity map.
Note that (Hn − I) = (T^n − I) / (Σ_{k=0}^{n-1} T^k) / n, all n.
(Just carry out the multiplication on the right.) That is, (Hn − I)x ∈ (T − I)X, allx ∈ X, all n.
Let x be a fixed point of T, let x ∈ X satisfy (9), and let yn = (Hn − I)x n=1,2,....
Then (yn, w) = (Hn − T)x, (yn, w) = (Hnx, mw) − (x, gw), all n, all w © X*.
Taking the limit and using (9), we find that lim (yn, #) = 佳户 − (x, ow) = 保 − x gm), all w © X*.
Since yn ∈ (T − I)X, all n, it follows from Lemma 14.11 that (x 一切 ∈ (fT − 1X.
And since ||T|| = 1, it follows that 0 = lim ||, (x 一刘 | = lim ||Hnx − Hny|| = lim ||Hnx − 矶 ||, where the first equality uses Lemma 14.12 and the last uses the fact that, since x is a fixed point of T, it is also a fixed point of Hn, for all n. = Let S C R’ be a subset of a finite-dimensional Euclidean space, with its Borel subsets #, and let C(S) be the space of bounded continuous functions f: S— R.
Recall (see Exercise 3.4e) that C(S), with the sup norm, is a normed linear space.
In our application of Theorem 14.13, C(S) is the space of interest.
Let P be a transition function on (S, #), and let T be the Markov operator associated with P.
Assume that T has the Feller property (Assumption 14.2).
Exercise 14.4 Show that under Assumption 14.2, T: C(S)—> C(S) is a linear operator; that ||T||, = 1; and that every constant function is a fixed point of T.
To apply Theorem 14.13, we must also identify the dual space of C(S).
The next result states that ®(S, 8), the space of signed measures on (S, 8) introduced in Section 11.3, is the dual space of C(S).
Recall that signed measures must be finite.
### THEOREM 14.14
(Riesz Representation Theorem) Let S C R! be a compact Set, with its Borel subsets f ; let C(S) be the space of bounded continuous functions 与 8 一 Ri; and let ®(S, 9) be the space of signed measures on (S, f).
If T: C(S)— Ris a continuous linear functional on C(S), there exists a unique signed measure v © O(S, Ff) such that Tf = ∫ f dv, all f € C(S).
For a proof of this theorem, see Royden (1968, Theorem 8, pp. 310311).
We are now ready to establish our final result.
**Proof.** of Lemma 14.9.
Let (S, 8), T, and T* satisfy Assumptions 14.114.3, and let C(S) be the space of bounded continuous functions on s Under Assumption 14.1, C(S) isa normed linear space and, by Theoren 14.14, its dual is the space ®(S, ) of signed measures on (S, 8).
Unde Assumptions 14.1 and 14.2, it follows from Exercise 14.4 that T: C(5) 一 C(S) is a linear operator, with ||T|| = 1.
Define the linear operator: Hn: C(S), n = 1, 2,..., by (8).
By Assumption 14.3, there is a unique probability measure A# E A(S, 9) such that (10) lim [ (Hnf)(s) dd = ∫ f dμ*, all f © C(S), allA E ACS, P).
Let y € (S, F) be a signed measure on (S, 9).
Then there exist probability measures \,, Aa E A(S, 8) and constants al, a2 E Ry such that v(A) = alhl(4) 一 aaha(h), all A € 8.
Hence ∫ Hnf dv = a1 ∫ Hnf dμ1. - a2 ∫ Hnf dμ2, all-n, all f € C(S).
It then follows from (10) that lim ∫ Hnf dv = a1 lim ∫ Hnf dμ1 - a2 lim ∫ Hnf dμ2 = (a1 - a2) ∫ f dμ*, all f € C(S).
Now fix f € C(S), and let f denote the constant function with valut ∫ f dd*.
Then lim (Anf, v) = (a1 - a2)(f, X*) = (a1 - a)(f, A*) =(f,v), ally € OS, 9).
By Exercise 14.4, any constant function f is a fixed point of T.
Hence Lemma 14.13 implies that lim ||Hnf − f|| = 0.
This fact completes the proof of Lemma 14.9, and—in case the reader has lost sight of the point of all this—of Theorem 14.7. @ 14.3 Bibliographic Notes The strong law of large numbers proved in this chapter is due to Breiman (1960).
Our proof follows exactly that given in his paper.
We have drawn on Chung (1974, chaps. 4 and 5) in Section 14.1.
Our treatment of the Norms Ergodic Lemma in Section 14.2 is taken from Loéve (1977, sect. 35).
# PART IV
Competitive Equilibrium
## 15 Pareto Optima and
Competitive Equilibria Thus far we have been concerned with methods for studying a variety of dynamic optimization problems, both deterministic and stochastic.
In these problems a single decision-maker (a consumer, firm, or social planner) maximizes an objective function (utility, profits, or social welfare) subject to a set of constraints (technological or market opportunities or both).
If the decision-maker is a consumer or a firm, the solution to this optimization problem is sometimes the object of direct interest.
In other cases our ultimate interest is in the behavior of an economic system composed of two or more such agents trading on a specified set of markets.
In this chapter and the three that follow, we examine methods for analyzing the competitive equilibria of such systems.
Two approaches are developed.
The first draws upon the two fundamental theorems of welfare economics.
As we suggested in Chapter 2 and will show more formally below, there is a wide class of situations in which the “invisible hand” ensures that the sets of Pareto-optimal allocations and competitive equilibrium allocations coincide exactly.
In these situations we can interpret certain normative models of optimal decision-making (from the point of view of a hypothetical “benevolent social planner”) as positive models of equilibrium outcomes.
This approach is developed in the present chapter and the one that follows.
In situations where competitive equilibria are not Pareto-optimal, an entirely different approach is needed.
This second approach, which is based upon a direct analysis of the first-order conditions from individual agents’ optimization problems, is developed in Chapters 17 and 18.
In the rest of this chapter we study in more detail the device of exploiting the connection between competitive equilibria and Pareto optima.
To do this we develop the connections somewhat differently from the 441 way we did Chapter 2, where we simply checked that some first-order conditions matched.
That approach can, under suitable convexity assumptions, be made rigorous.
But we do not pursue it, because there are many situations in which Pareto-optimal and competitive equilibrium allocations coincide but in which this fact is difficult or impossible to verify by a comparison of first-order conditions.
Fortunately, much more powerful methods are available.
Our task in this chapter is to describe these methods and to see how they apply to the dynamic problems we are interested in.
The general plan can be illustrated diagrammatically.
Figure 15.1 displays indifference curves for a consumer whose utility U(J, c) depends on his leisure / and his goods consumption c.
He is endowed with one unit of leisure and has access to the production technology c = f(1 - J), so Y is the set of feasible (b c) pairs.
It is clear that the point (J°, c°) maximizes U over Y and hence is a Pareto-optimal allocation.
It is also a competitive equilibrium at the relative prices given by the slope of the straight line passing through (/°, c0).
One way to see this is to observe that an indifference curve is tangent to the production possibility frontier at this point, so the first-order condition for an optimum is satisfied.
Then note that the straight line to which these curves are mutually tangent is an equilibrium price, so (J°, c°) satisfies the first-order condif(1) 一 (4oco) 0 1 a Figure 15.1 , too.
If the functions U and f are concave and differentiable, this approach is perfectly respectable.
A somewhat different way of establishing the same thing is as follows.
To see that (2°, c°) is Pareto optimal, simply note that the set of allocations preferred to (/°, c°) consists of the interior of the set A.
Since none of these points is feasible—since Y and the interior of A do not intersect—(1°, c0) is a Pareto optimum.
To see that this allocation is also a competitive equilibrium, at the relative price p, refer to Figure 15.2.
We need to check two conditions.
The first is whether the allocation (1°, c0) is utility maximizing for the consumer over his budget set B.
The C A 十 (f%c°) B 0 D 1 C D f(1) (Pc?) Y 0 1 E Figure 15.2 argument that this is so is the same as the one above: B and the interior of A do not intersect.
The second is whether (1°, c0) is profit maximizing for the firm at the given prices and with the given technology.
The allocations that yield higher profit are simply those in the interior of the set D.
Since I and the interior of D do not intersect, none of these is feasible.
Note that the latter approach uses the fact that the sets A and Y are convex, with a shared point (/°, c0) and a line separating the two sets.
Since the convexity of A and Y is equivalent to the concavity of U and f— the assumptions used in the first approach—for this one-person, twogood economy there is little at stake in the choice between the two points of view (aside from the fact that the latter does not require differentiability).
The approach based on convex sets and separating lines (or planes, or hyperplanes) is much more powerful, however; and we need to exploit this extra power because the models discussed in Chapters 4 and 9 all involve infinite-dimensional commodity spaces.
There is no single idealization of a competitive economy that encompasses all the particular models one might ever run across, but the welfare theorems discussed in this chapter apply to such a wide range of models that it is useful to have as abstract a statement as possible.
Arrow (1951) provided the first modern treatment of this topic, idealizing the commodity allocations chosen by consumers and firms as points in a finite-dimensional Euclidean space.
Debreu (1954) extended this analysis to commodity spaces that are required only to be normed vector spaces.
It is clear from even the simple examples in Chapter 2 that to study models with an infinite time horizon or with random shocks that take on infinitely many values, we need this broader idea of a commodity space.
To discuss the competitive equilibria of economies in which the commodity space is an arbitrary normed vector space, we must first decide what is to be meant by a price system in such an economy.
For reasons that will become clear below, the most useful approach is to take price systems to be continuous linear functionals on the commodity space.
For a given commodity space, the set of possible price systems is then the dual space, the space of all continuous linear functionals.
Thus, we begin in Section 15.1 by discussing some of the main facts about the relationship between various normed vector spaces and their duals.
We also provide a statement of the Hahn-Banach Theorem, the infinite-dimensional version of the separation theorem for convex sets illustrated in Figure 15.1.
In Section 15.2 we draw on these results to review Debreu’s (1954) treatment of the relationship between Pareto optima and competitive equilibria, the two fundamental theorems of welfare economics, in a context where the commodity space is taken to be an arbitrary normed vector space.
Then in Section 15.3 we discuss the issues involved in deciding which particular normed vector spaces are suited for applications involving time and uncertainty.
Finally, in Section 15.4 we discuss conditions under which equilibrium price systems for such economies can be represented as inner products and hence be given a natural economic interpretation. 15.1 Dual Spaces To discuss competitive equilibrium, we need to decide what we mean by a price system.
If the commodity space is a finite-dimensional Euclidean space RX, the obvious way to do this is simply to take the price of each commodity, k = 1,...,K, to be a number p_k ∈ R.
A price system is then a vector p = (p1,...,pK) ∈ RK, and the value of any commodity point x is the inner product p · x = Σ_k p_k x_k.
Hence a price system in this case is a mapping from the commodity space RK into R; and since p · (αx + βy) = α(p · x) + β(p · y), for any α, β ∈ R and any x, y ∈ RK, the mapping is linear.
The generalization of this idea to a commodity space that is an arbitrary normed vector space is given in the following definition.
### DEFINITION A
linear functional on a normed vector space (S, ||·||_S) is a function φ: S → R satisfying φ(αx + βy) = αφ(x) + βφ(y), all x,y ∈ S, all α,β ∈ R.
The linear functional is continuous if ||x_n − x|| → 0 implies |φ(x_n) − φ(x)| → 0.
It is bounded if there exists a constant M such that |φ(x)| ≤ M||x||_S for all x ∈ S.
The norm of a bounded linear functional is then defined to be (1) ||φ|| = inf {M ∈ R: |φ(x)| ≤ M||x||_S, all x ∈ S} = sup_{||x|| ≤ 1} |φ(x)|.
When there is no possibility for confusion, we drop the subscripts on the norms and refer to S, rather than (S, ||·||_S), as a normed vector space.
The following theorem offers two useful ways of identifying continuous linear functionals.
### THEOREM 15.1
Let S be a normed vector space, and let φ be a linear functional on S.
Then a. if φ is continuous at any point in S, it is continuous on all of S; and b. φ is continuous if and only if it is bounded.
**Proof.** (a) Suppose that φ is continuous at s ∈ S, and let {x_n} be a sequence in S converging to x ∈ S.
Define the sequence {s_n} by s_n = s + x_n − x, n = 1,2,....
By the linearity of φ, φ(s_n) = φ(x) + φ(s_n) − φ(s), n = 1,2,....
Therefore, taking the limit and using the continuity of φ at s, we obtain lim φ(s_n) = φ(x) + lim (φ(s_n) − φ(s)) = φ(x).
(b) Suppose that φ is bounded, with ||φ|| = M.
Then for any sequence {x_n} converging to 0, we have lim |φ(x_n)| = lim M||x_n|| = 0, so φ is continuous at 0.
Hence by part (a) it is continuous on all of S.
Conversely, suppose that φ is continuous.
Then there exists some 0 < M < ∞ such that ||x|| = 1/M implies |φ(x)| < 1.
Then for any x ≠ 0, |φ(x)| = ||x||·φ(x/||x||) < M||x||.
Hence ||φ|| = M. = For any normed vector space S, the space S* of all continuous linear functionals on S is called the dual of S.
Addition and scalar multiplication on S* are defined in the obvious way, and since aφ + bψ ∈ S*, for all φ, ψ ∈ S*, and all a, b ∈ R, S* is a vector space.
With the norm defined in (1), (S*, ||·||_S*) is a normed vector space.
It is not too difficult to show that (S*, ||·||_S*) is also complete, even if S is not.
That is, every dual space is a Banach space.
Exercise 15.1 Let S be a normed vector space.
Show that the dual space S* is complete.
We turn next to some standard examples of normed vector spaces and their duals.
Example 1 Let S be the finite-dimensional Euclidean space R^n with the norm ||x|| = (Σ_i |x_i|^2)^{1/2}.
Clearly any y ∈ R^n defines a continuous linear functional on S through the inner product φ(x) = y · x = Σ_i y_i x_i.
The converse is true as well.
To see this, let φ be any continuous linear functional.
For i= 1,...,n, let e_i = (0,...,0,1,0,..., 0) be the vector with a one as the ith component and zeros elsewhere.
Define y ∈ R^n by y_i = φ(e_i).
Then the linearity of φ implies that φ(x) = Σ_i y_i x_i = y · x, all x ∈ R^n, and we say that the inner product y · x represents φ.
In this example there is a one-to-one correspondence between S* and R^n and we refer to either as the dual space.For each i, there exists x' ∈ X_i such that φ(x') < φ(x'').
Then [(x''), (y'')] ⊆ a competitive equilibrium.
**Proof.** It suffices to show that (E2) holds.
By hypothesis, for each i there exists x_i' ∈ X_i such that φ(x_i') < φ(x'').
Now suppose that x ∈ X_i and φ(x) = φ(x'').
Let x_θ = θx_i' + (1 - θ)x_i, all θ ∈ (0, 1).
By Assumption 15.1, x_θ ∈ X_i, all θ ∈ (0, 1); and by the linearity of φ, φ(x_θ) = θφ(x_i') + (1 - θ)φ(x_i) < φ(x''), all θ ∈ (0, 1).
Hence it follows by contraposition from (3) that u_i(x) < u_i(x''), all θ ∈ (0, 1).
Hence by Assumption 15.3, u_i(x_i) = lim_{θ→0} u_i(x_θ) = u_i(x''). □ Figure 15.3 illustrates a case where Theorem 15.4 holds but the Remark fails.
Consumer A’s consumption set is the closed, convex set X, and B’s is the entire positive orthant.
Consumer A’s indifference curves form right angles, and B’s are smooth and strictly convex, both as shown.
The allocation at E is clearly Pareto optimal but cannot be supported as a competitive equilibrium: the only price ratio at which E is utility maximizing for consumer B is the indicated ratio p; but at that price ratio, consumer A prefers the allocation x'. ### 15.3 Issues in the Choice of a Commodity Space The two welfare theorems of the last section establish that if Assumptions 15.1–15.5 are satisfied, then the set of competitive equilibrium allocations and the set of Pareto-optimal allocations coincide exactly.
Since the latter are simply solutions to the appropriate constrained optimization problems, with weighted sums of consumers' utilities as the objective, these optimization problems provide a very convenient way to study competitive equilibria.
In this section we look at particular issues that arise when optimization problems of the type studied in Chapters 7 and 8 are viewed in this way.
Specifically we look at the issues involved in ensuring that Assumptions 15.1–15.5 hold and that the continuous linear functional provided by Theorem 15.4 can be interpreted as a set of prices in the usual sense of the word.
In some cases this interpretation requires care in choosing the commodity space (S, ||·||).
The economic model itself generally determines the set S, but the choice of an appropriate norm can be more subtle.
Two considerations play a role in the decision.
The first is that the norm chosen determines whether any given function u_i is continuous and whether any given set Y has an interior point.
The norm on S must be chosen so that Assumptions 15.3 and 15.5 hold for the preferences and technologies of interest.
The second issue is that the choice of norm determines the class of continuous linear functionals on S; it is convenient if the norm can be chosen so that every continuous linear functional has an inner product representation, since Theorem 15.4 then guarantees the existence of a set of prices in the usual sense.
As we will see below, however, these two desiderata sometimes conflict.
In the rest of this section we look at three specific classes of models: a deterministic, one-period model; a deterministic, infinite-horizon model; and a stochastic, one-period model.
The first of these provides an example where both criteria are satisfied by any of a wide variety of norms.
The last two show how the two criteria can come into conflict.
In Section 15.4 we pursue the consequences of dropping the second.
There we look at situations where Theorem 15.4 applies but the continuous linear functional it provides may not have an inner product representation.
We show how, in these cases, additional assumptions on the preferences and technology can be imposed to guarantee the existence of a price system with an inner product representation.
In static models with no uncertainty, we generally take S = R^K, and x = (x_1, ..., x_K) ∈ S is interpreted as a list of quantities of K different goods.
Since this space is finite dimensional, we do not have to worry about the existence of an interior point for Y.
Moreover, all the norms on this space that one might reasonably think of—for example, ||x||_p = (Σ|x_k|^p)^{1/p}, p ≥ 1; ||x||_∞ = max_k |x_k|; and so forth—have the feature that a sequence {x_n} in R^K converges to x if and only if {x_{n,k}} converges to x_k for k = 1, ..., K.
Hence any function u_i that is continuous in one of these norms is continuous in all of them.
Finally, as was shown in Section 15.1, every linear functional on a finite-dimensional Euclidean space has an inner product representation, φ(x) = p · x, and conversely.
Dynamic models with a finite number of periods and stochastic models with a finite number of states-of-the-world have exactly the same mathematical properties, since the commodity space is still a finite-dimensional Euclidean space.
However, infinite-horizon dynamic models and stochastic models with an infinite number of states raise a new set of mathematical issues.
We turn to these now.
In the one-sector model of optimal growth, an allocation is an infinite sequence x = (x_0, x_1, ...).
As we saw in Section 15.1, all of the l_p spaces consist of such elements, so this family seems to offer many possibilities for commodity spaces.
However, working with any of the l_p spaces other than l_∞ causes serious difficulties.
In the first place, if 1 ≤ p < ∞, then x ∈ l_p only if the series Σ x_t^p converges, which requires lim_{t→∞} x_t = 0.
Although one has some flexibility in interpreting the zero point, this condition is obviously a severe restriction on the kind of dynamics that can be considered.
The next exercise illustrates a second difficulty: none of the l_p spaces with p finite can have a production set in the positive orthant with an interior point.
Among the l_p spaces, only l_∞ has a positive orthant with interior points.
Exercise 15.7 a.
Show that for 1 ≤ p < ∞, the positive orthant of l_p has no interior points. b.
Show that the positive orthant of l_∞ has a nonempty interior.
Within the l_p family, Theorem 15.4 can be applied only if l_∞ is chosen as the commodity space.
The following example shows that functionals on l_∞ that are not in l_1 can arise in models satisfying Assumptions 15.1–15.5.
Consider an infinite-horizon economy with one consumption good.
The commodity space S is l_∞, and x is interpreted as units of the single good available in period t.
The production set is Z = { y ∈ S : 0 ≤ y_t ≤ 1 + 1/t, all t }; the consumption set is X = { x ∈ S : x_t ≥ 0, all t } and preferences u: S → R are defined by (1) u(x) = inf_t x_t.
Exercise 15.8 Show that this economy satisfies Assumptions 15.1–15.5.
One Pareto-optimal allocation in this economy is x' = y' = 1 + 1/t, t = 1, 2, ....
By Theorem 15.4, then, there is a continuous linear functional φ: S → R, not identically zero on S, such that x', y', and φ together satisfy (2) x ∈ X and u(x) = u(x') implies φ(x) = φ(x'); (3) y ∈ Z implies φ(y) ≤ φ(y').
Suppose it were the case that this functional could be written (4) φ(x) = Σ p_t x_t, for some sequence {p_t}.
If p_t < 0 for any t, then (3) would be violated, since replacing y_t with 0 would yield a higher-profit element of Z.
Since not all of the p_t's can be zero, p_t > 0 for some t.
Now consider the sequence 1 = (1, 1, 1, ...).
Clearly 1 ∈ X; and for the preferences in (1), u(1) = u(x').
But if p_t > 0 for any t, then φ(1) = Σ p_t > Σ p_t(1 + 1/t) = φ(x'), so (2) is violated.
Thus φ(x) cannot take the form given in (4); rather, the equilibrium valuation must “put all of its weight at infinity.” As economists, we do not want to talk about “prices at infinity,” so this case poses a problem.
The solution must involve ruling out preferences, like those in (1), that put extreme emphasis on outcomes—in this case, consumption arbitrarily far in the future—that our economic instincts tell us actual consumers do not put much weight on.
But we want to do so in a way that is based on economic, not mathematical, considerations.this in a way that does not compromise the wide applicability of the theory.
As Exercise 15.8 shows, continuity in the sup norm does not rule out the preferences in (1).
The $L^p$ spaces with $1 < p < \infty$ are not useful alternatives for this problem, since none of them contains $Y$ as a subset.
What about the space of sequences $\{x_t\}$ with (5) $\|x\|_\delta = \sum_{t=0}^\infty \delta^t |x_t| < \infty$, where $\delta \in (0, 1)$?
Continuity in this norm rules out the preferences in (1); here the norm of the space itself expresses the idea that consumption in the distant future ought not to matter very much.
Exercise 15.9 Show that the preferences in (1) are not continuous if the norm in (5) is used.
But this line also fails: as shown in Exercise 15.6, the positive orthant then has no interior point, so Assumption 15.5 is violated.
These examples illustrate something of a theoretical bind.
We want to choose a commodity space for infinite-horizon problems to which we can apply Theorem 15.4.
To do this we require that the production set $Y$ have an interior, which dictates the use of $l^\infty$.
But a linear functional on $l^\infty$ need not have an inner product representation: it need not lie in $l^2$.
In other words, it may not have an economic interpretation as a price system.
The approach we use in the next section is to use $l^2$ as the commodity space but to impose stronger assumptions on the preferences and technology.
Under these stronger assumptions, we are able to construct from the functional $\phi$ of Theorem 15.4 a related, but possibly different, functional that is in $l^2$, and also serves as an equilibrium price system.
Exactly the same issues arise in stochastic models.
Let $(Z, \mathcal{F}, \mu)$ be a probability space, where $z \in Z$ describes the state-of-the-world.
If there are $K$ commodities in each state, then an allocation is a $\mathcal{F}$-measurable function $x: Z \to \mathbb{R}^K$, where $x(z)$ is a $K$-vector of contingent claims to goods to be delivered if the state $z \in Z$ occurs.
Hence we want the set $S$ to be the set of all such functions.
We then must choose a suitable norm for $S$ and use elements of the dual space as price systems.
For exactly the reasons already discussed, we want to take the commodity space to be the space $L_\infty(Z, \mathcal{F}, \mu)$ of essentially bounded equivalence classes of functions, with the ess sup norm defined in Section 15.1.
The difficulty then is that not every continuous linear functional on $L_\infty(Z, \mathcal{F}, \mu)$ can be represented as an inner product of the form $\phi(x) = \int p(z) \cdot x(z) d\mu$, where $p \in L_1(Z, \mathcal{F}, \mu)$.
To see this, note that the example above can be interpreted as a one-period model of uncertainty, where $t \in \{0, 1, ..., T\}$ indicates the state-of-the-world, and $\beta^t (1 - \beta)$ is the probability that the $t$th state occurs.
Using $l^\infty$ as the commodity space raises exactly the same set of difficulties as does using $L_\infty(Z, \mathcal{F}, \mu)$.
In the next section we show one way these difficulties can be dealt with. 15.4 Inner Product Representations of Prices We have seen that if the commodity space is $l^\infty$ or $L_\infty(Z, \mathcal{F}, \mu)$, the linear functional $\phi$ the existence of which is asserted in Theorem 15.4 need not have an inner product representation.
In this section we show that in these and similar cases we can, by imposing additional requirements on the preferences and technology, strengthen Theorem 15.4 to ensure the existence of prices, that is, of a linear functional that can be represented as an inner product.
We deal first with time and then with uncertainty, and then comment briefly on combining both.
Consider an infinite-horizon economy.
Let the normed vector space $(X, \|\cdot\|)$ be the one-period commodity space, which we take to be the same for each period.
Let $S = X \times X \times \ldots$ be the space of sequences $x = (x_0, x_1, \ldots) \in S$, with the norm $\|x\| = \sup_t \|x_t\|$.
For any $x = (x_0, x_1, \ldots) \in S$, let $x^T \in S$ denote the truncated sequence $x^T = (x_0, \ldots, x_T, 0, 0, \ldots)$.
In Lemma 15.5 these truncations are used to show that every continuous linear functional $\phi$ on $S$ can be decomposed into a “well-behaved” part, $\psi$, and a part that puts “weight at infinity,” the rest.
The lemma shows how to construct $\psi$ given $\phi$.
Then in Theorem 15.6 it is shown that with the preferences and technology suitably restricted, the functional $\psi$ is also an equilibrium price system.
### LEMMA 15.5
Let $\phi$ be a continuous linear functional on the normed vector space $(S, \|\cdot\|)$ defined above.
Then (1) $\psi(x) = \lim_{T\to\infty} \phi(x^T), \quad \text{all } x \in S$, defines a continuous linear functional on $S$, and can be written as (2) $\psi(x) = \sum_{t=0}^\infty \psi_t(x_t), \quad \text{all } x \in S$, where each $\psi_t$ is a continuous linear functional on $X$.
**Proof.** We must show that the limit in (1) exists for all $x \in S$ and that $\psi$ so defined is a continuous linear functional.
First note that since $\phi$ is continuous, it follows from Theorem 15.1 that $\|\phi\| < \infty$.
If $x = 0$, then clearly $\psi(x) = 0$.
Suppose $x \neq 0$.
For each $t=0,1,...$, let $x^t = (0,..., 0, x_t, 0,...)$; let $y^t = \begin{cases} x^t & \text{if } \phi(x^t) \geq 0 \\ 0 & \text{if } \phi(x^t) < 0 \end{cases}$, and let $y = (y^0, y^1, \ldots)$.
Then for all $T$, $\sum_{t=0}^T |\phi(y^t)| = \phi(y) \leq \|\phi\| \|y\| \leq \|\phi\| \|x\|$.
That is, the series $\sum_{t=0}^\infty |\phi(y^t)|$ is bounded above by $\|\phi\| \|x\|$, and hence converges.
It follows that the series $\sum_{t=0}^\infty \phi(x^t)$ also converges, so $\psi(x)$ is well defined.
Clearly $\psi$ is linear, and $\psi(x) < \|\phi\| \|x\|$, all $x \in S$; hence $\|\psi\| = \|\phi\| < \infty$, so $\psi$ is bounded.
It then follows from Theorem 15.1 that $\psi$ is continuous.
Finally, let $X^*$ be the dual of $X$, and define the continuous linear functionals $\psi_t \in X^*$, $t = 0, 1,...$, by $\psi_t(x_t) = \psi(x^t)$.
Then (2) follows immediately from (1). # If $X$ is the finite-dimensional Euclidean space $\mathbb{R}^K$, then, as shown in Section 15.1, each linear functional $\psi_t$ has an inner product representation: $\psi_t(x_t) = p_t \cdot x_t$, for some $p_t = (p_{1t}, ..., p_{Kt}) \in \mathbb{R}^K$.
Hence, for this case, the linear functional $\psi$ can be written as an inner product (3) $\psi(x) = \sum_{t=0}^\infty \psi_t(x_t) = \sum_{t=0}^\infty p_t \cdot x_t = \int_0^\infty p_t \cdot x_t$.
Next we show that under somewhat stronger assumptions on the preferences and technology, the linear functional $\phi$ given in Theorem 15.4 defines—by means of (1)—a functional that is a competitive equilibrium price system and does not put any “weight at infinity.” We need two additional assumptions.
The commodity space $S$ and the definitions of truncated sequences are as above.
Note that the $X_i$’s and $Y_j$’s are subsets of $S$, not of $X$.
ASSUMPTION 15.6 For each $i$, $x \in X_i$ implies $x^T \in X_i$ for all $T$ sufficiently large; and for each $j$, $y \in Y_j$ implies $y^T \in Y_j$ for all $T$ sufficiently large.
ASSUMPTION 15.7 For each $i$, if $x, x' \in X_i$ and $u_i(x) > u_i(x')$, then $u_i(x^T) > u_i(x'^T)$, for all $T$ sufficiently large.
Assumption 15.6 says that truncated feasible sequences are feasible for consumers and producers, if the truncation is sufficiently far in the future.
Assumption 15.7 is a continuity requirement on preferences to the effect that sufficiently distant consumption is “discounted” in a very weak sense.
Exercise 15.10 Let $C \subset X$ be a convex set with $0 \in C$, and let $X_i = C \times C \times \ldots$ a.
Show that $X_i$ satisfies Assumptions 15.1 and 15.6. b.
Let $U_i: C \to \mathbb{R}$ be a bounded function satisfying Assumptions 15.2 and 15.3, and let $\beta \in (0, 1)$.
Show that $u_i: X_i \to \mathbb{R}$ defined by $u_i(x) = \sum_{t=0}^\infty \beta^t U_i(x_t)$ satisfies Assumptions 15.2, 15.3, and 15.7. c.
Let $C = \mathbb{R}^K$, and let $W: C \times \mathbb{R}_+ \to \mathbb{R}_+$ be an aggregator function, as defined in Section 5.11.
Show that the fixed point $u_i$ of the operator $T_{u_i}$ defined there satisfies Assumptions 15.2, 15.3, and 15.7.
Exercise 15.11 Let $S = l^\infty$. a.
Show that the preferences $u(x) = \inf_t x_t$ do not satisfy Assumption 15.7. b.
Let $c_0 \subset l^\infty$ be the subspace consisting of all sequences converging to zero.
Then Assumption 15.6 requires that for each $i$, $x \in X_i$ implies that the tail of the sequence $\{x_t\}$ lies in $X_i \cap c_0$.
Show that Assumption 15.7 then holds if and only if $u_i(x) = \lim_{t\to\infty} u_i(x^t)$. , Our next theorem shows that under these two additional assumptions, if $[(x_i^*), (y_j^*), \phi]$ is a competitive equilibrium, then so is $[(x_i^*), (y_j^*), \psi]$,THEOREM 15.9 Let S be the normed vector space defined above; let Assumptions 15.1–15.7 and 15.8'–15.9' hold; let \((x^i), (y^j), \phi\) be a feasible allocation and a continuous linear functional such that (4) and (5) hold; and suppose that for each i, there exists \(z_i \in X_i\) such that \(u_i(z_i) > u_i(x^i)\).
Then there exists a continuous linear functional \(v\) on S such that (4) and (5) hold with \(v\) in place of \(\phi\) and such that \(v\) can be written as \[ (9) \quad v(x) = \sum_{i=1}^{\infty} \int_{Z'} p_i(z_i) x_i(z_i) \, du_i(z_i), \quad \text{all } x \in S, \] where \(p_i \in L_{\infty}(Z', \mathcal{F}, u_i)\) for all \(i\).
**Proof.** Let \(\phi\) be the continuous linear functional on S defined by (1); and let \(\phi_i\) be the continuous linear functionals on the spaces \(\{X_i\}\) such that (2) holds.
As noted above, minor modifications of Lemma 15.5 and Theorem 15.6 ensure that these are well defined and that (4) and (5) hold with \(\phi\) in place of \(v\).
That is, \[ (10) \quad \text{for each } i, x \in X_i \text{ and } u_i(x) = u_i(x^i) \text{ implies } w_i(x) = \phi_i(x) = \phi_i(x^i) = W(x^i); \] \[ (11) \quad \text{for each } j, y^j \in Y_j \text{ implies } w_j(y^j) = \sum_{i} \phi_i(y^j_i) \geq \sum_{i} \phi_i(0) = W(y^j). \] For each \(u_i\), it follows from Lemma 15.7 that there exists \(\lambda_i \geq 0\) and a continuous linear functional \(p_i\) such that \[ (12) \quad p_i(x) = \lim_{n \to \infty} w_i(x_n^i), \quad \text{all } x \in X_i. \] Define the continuous linear functional \(v\) on S by \[ v(x) = \sum_{i=1}^{\infty} \int_{Z'} p_i(z_i) x_i(z_i) \, du_i(z_i), \quad \text{all } x \in S. \] Next we will verify that \[ (13) \quad \text{for each } i, x \in X_i \text{ and } u_i(x) = u_i(x^i) \text{ implies } v(x) = \sum_{i} v_i(x_i) = \sum_{i} v_i(x_i^i) = V(x^i); \] \[ (14) \quad \text{for each } j, y^j \in Y_j \text{ implies } v(y^j) = \sum_{i} v(y^j_i) \geq \sum_{i} v(0) = V(y^j). \] Fix \(i\), and suppose that \(x \in X_i\) with \(u_i(x) = u_i(x^i)\).
By hypothesis, there exists \(z_i \in X_i\) such that \(u_i(z_i) > u_i(x^i)\).
Define \[ x^{\theta} = \theta z_i + (1 - \theta) x, \quad \text{all } \theta \in (0, 1). \] By Assumptions 15.1 and 15.2, \[ x^{\theta} \in X_i \quad \text{and} \quad u_i(x^{\theta}) > u_i(x^i), \quad \text{all } \theta \in (0, 1). \] Fix \(\theta \in (0, 1)\); then by Assumptions 15.6 and 15.7, for some \(T(\theta)\) sufficiently large, \[ x^{\theta} T \in X_i \quad \text{and} \quad u_i(x^{\theta} T) > u_i(x^i), \quad \text{all } T = T(\theta). \] For each \(u_i\), let \(\{A_n\}\) be the sequence used in defining \(p_i\) in (12).
For any function \(x \in S\), let \(x^n \in S\) denote the function that is truncated to zero in all components past the \(T\)th, and on the sets \(A_n\), for \(n = 0, 1, \dots, T\).
That is, \[ x^n = (x^n, \dots, x_T^n, 0, 0, \dots). \] Fix \(T = T(\theta)\); then it follows from repeated application of Assumptions 15.8' and 15.9' that for some \(N(T)\) sufficiently large, \[ x^{\theta} n \in X_i \quad \text{and} \quad u_i(x^{\theta} n) > u_i(x^i), \quad \text{all } n = N(T). \] Hence it follows from (10) and the definition of the \(v_i\)s that \[ \sum_{i=1}^{\infty} v_i(x^{\theta} n_i) = \sum_{i=1}^{\infty} \lim_{m \to \infty} w_i((x^{\theta} n_i)_m) = \lim_{m \to \infty} \sum_{i=1}^{\infty} v(x^{\theta} n), \quad \text{all } n = N(T). \] Since the right side converges as \(n \to \infty\), it follows that \[ \sum_{i=1}^{\infty} v_i(x^{\theta}_i) = \sum_{i=1}^{\infty} v_i(x^i), \quad \text{all } T = T(\theta). \] Then since the right side converges as \(T \to \infty\), it follows that \[ v(x^{\theta}) = \sum_{i=1}^{\infty} v_i(x^{\theta}_i) = \sum_{i=1}^{\infty} v_i(x^i) = v(x^i), \quad \text{all } \theta \in (0, 1). \] Then from the linearity of the \(v_i\)s, it follows that \[ \sum_{i=1}^{\infty} v(\theta z_i + (1 - \theta) x) = \theta \sum_{i=1}^{\infty} v(z_i) + (1 - \theta) \sum_{i=1}^{\infty} v(x_i), \quad \text{all } \theta \in (0, 1). \] Taking the limit as \(\theta \to 0\), we then find that \[ \sum_{i=1}^{\infty} v(x^i) = \sum_{i=1}^{\infty} v(z_i) \cdot 0 + \sum_{i=1}^{\infty} v(x_i) = v(x), \] which establishes (13).
Next let \(y \in Y_j\).
Then by Assumption 15.6, there exists some \(\gamma\) such that \(y^{\gamma} \in Y_j\), for all \(\gamma = \gamma\).
Fix \(\gamma = \gamma\); then by Assumption 15.8', there exists some \(N(\gamma)\) such that \(y^n \in Y_j\), for all \(n = N(\gamma)\).
It then follows from (11) and the definition of the \(v_i\)s that \[ \sum_{i} v(y^n_i) = \sum_{i} \lim_{m \to \infty} w_i((y^n_i)_m) = \lim_{m \to \infty} \sum_{i} v(y^n), \quad \text{all } n = N(\gamma). \] Taking the limit as \(n \to \infty\) and then as \(\gamma \to \infty\) establishes (14).
From (13) and (14), it can be established that \[ w(x^i) = v(x^i), \quad \text{all } i, \quad \text{and} \quad w_j(y^j) = v(y^j), \quad \text{all } j, \] the argument parallels exactly the one in the proof of Theorem 15.6.
It then follows from these equalities together with (13) and (14) that (4) and (5) hold with \(v\) in place of \(\phi\).
Finally, by Lemma 15.7, each \(p_i\) can be represented by a function \(p_i \in L_{\infty}(Z', \mathcal{F}, u_i)\); hence \(v\) can be written as shown in (9). \(\#\) 15.5 Bibliographic Notes Luenberger (1969, chap. 5) contains an excellent discussion of dual spaces, including many of the most common examples, and of the Hahn–Banach Theorem.
The two fundamental welfare theorems reviewed in Section 15.2 date from Arrow (1951), where a set-theoretic formulation of both theorems was given for the first time and where the separation theorem for convex sets was first used to prove the second theorem.
Theorems 15.3 and 15.4 and the Remark all appear in that paper, essentially as here except for the restriction to \(\mathbb{R}^n\).
The extension of these results to commodity spaces that are arbitrary normed vector spaces was first made in Debreu (1954), and our treatment follows his very closely.
The main difference is that we assume a continuous utility function rather than a preference ordering for each consumer.
Jones (1986) contains a set of examples illuminating the problems that can arise in infinite-dimensional commodity spaces.
These examples illustrate very nicely where certain norms (or more generally, certain topologies) cause difficulties.
As the examples in Section 15.3 show, many potentially interesting commodity spaces lack interior points.
Some recent work has been devoted to developing new arguments—arguments that do not involve the Hahn–Banach Theorem—for establishing the existence of supporting prices: see Mas-Colell (1986a,b) and Back (1988).
For the commodity space \(L^1\), Bewley (1972) first studied the existence of competitive equilibria supported by prices in \(L^{\infty}\).
In his treatment the role of Assumptions 15.6 and 15.7 is played by the assumption that preferences are continuous in the Mackey topology.
The appendix of that paper contains a proof that expected utility has this continuity property.
The treatment in Section 15.4 follows closely the one in Prescott and Lucas (1972).
Brown and Lewis (1981) showed that Mackey-continuity of preferences is equivalent to Assumptions 15.6 and 15.7, as well as to similar assumptions that treat the “tails” in different ways.
## 16 Applications of Equilibrium Theory
An immediate consequence of the theory reviewed in Chapter 15 is that the solutions to certain planning problems can be interpreted as competitive equilibria of economies with a large number of consumers who have identical preferences and identical endowments, and a large number of firms that have identical constant-returns-to-scale technologies.
The variables in such an economy are thought of as per capita magnitudes.
Since the consumers have identical preferences, solving the social planner’s problem is equivalent to finding the symmetric Pareto-optimal allocations.
The First Welfare Theorem then ensures that all symmetric competitive equilibria are symmetric Pareto optima and hence are solutions to the planning problem.
The Second Welfare Theorem ensures that all symmetric Pareto optima, and hence all solutions to the planning problem, are, for suitable prices, supportable as competitive equilibria.
The models in Sections 16.1–16.4 illustrate various ways in which this type of argument can be applied.
In Sections 16.5 and 16.6 we look at the issue of representing competitive equilibrium prices as inner products.
In Section 16.5 we consider a more general form of truncation than the one in Assumptions 15.6 and 15.7.
This generalization permits a strengthening of Theorem 15.6 that is useful in some applications.
In Section 16.6 we give a cautionary example that highlights a limitation on the applicability of Theorem 15.6.
In Section 16.7 we show that the Pareto-optimal allocations for a growth model with many heterogeneous consumers can be obtained by the methods of dynamic programming.
We also show that the theory of Chapter 15 can be applied to characterize equilibrium prices in this case, just as it can in economies with identical consumers. 16.1 A One-Sector Model of Growth under Certainty Consider the deterministic one-sector growth model that we studied in Sections 5.1 and 6.1.
There is one produced good, which can be consumed or used as capital, and one nonproduced good, which is in fixed supply each period and is used as a factor of production.
Here we interpret the latter resource as land.
In each period the representative household consumes goods, and the representative firm uses land and capital to produce goods.
Hence an allocation for this economy consists of a. a consumption sequence \( x = \{x_t\}_{t=0}^\infty \) for the representative consumer, where \( x_t \in \mathbb{R}_+ \) is consumption of goods in period \( t \) and b. a production sequence \( y = \{y_t\}_{t=0}^\infty \) for the representative firm, where \( y_t \geq 0 \) is the supply of consumption goods in period \( t \).
If the firm’s technology is bounded, it is appropriate to limit attention to bounded sequences; that is the case we consider here.
We can then take the commodity space to be \( \ell_\infty \).
The consumption set for the representative consumer is the positive orthant of \( \ell_\infty \), \( X = \ell_{\infty +} \).
His preferences over this set are given by \[ u(x) = \sum_{t=0}^\infty \beta^t U(x_t), \] where \( U: \mathbb{R} \to \mathbb{R} \).
Assume that \( U \) is bounded, continuous, strictly increasing, and strictly concave, and that \( \beta \in (0, 1) \).
Each firm has an initial endowment of one unit of land and \( k > 0 \) units of capital, both interpreted as the economy-wide stocks per capita.
Each firm also has access to the same constant-returns-to-scale production function \( F: \mathbb{R}_+^2 \to \mathbb{R}_+ \).
Since the supply of land is one unit per capita, it is convenient to define \( f: \mathbb{R}_+ \to \mathbb{R}_+ \) by \( f(k) = F(k, 1) + (1 - \delta) \) where \( \delta \in (0, 1] \) is the depreciation rate.
As noted above, we assume that \( f \) is bounded.
Then the production set \( Y \) is given by \[ Y = \{ y \in \ell_\infty : \text{there exists } k \in \ell_\infty \text{ such that } k_{t+1} = f(k_t) - y_t \text{ for all } t \}. \] ### 16.1 / One-Sector Growth 477 Assume that \( f \) is continuous, strictly increasing, and strictly concave, with \( f(0) = 0 \); note that since \( f \) is bounded, \( f(k) = k \) for some \( k > 0 \).
Assume \( f'(0) > 1 \), so capital accumulation is possible.
The maximization problem studied in Section 5.1 is, in this notation: choose \( x \in X \) to maximize \( u(x) \).
Clearly the solution is a symmetric Pareto-optimal allocation; we wish to show that it is also supportable as a competitive equilibrium. **Exercise 16.1** a.
Show that under the restrictions on \( \beta \), \( U \), and \( f \) stated above, this economy has exactly one symmetric Pareto-optimal allocation. [Hint.
Use the result of Exercise 5.1.] What does the First Welfare Theorem (Theorem 15.3) then imply about the number of symmetric competitive equilibrium allocations? b.
Show that under the restrictions on \( \beta \), \( U \), and \( f \) stated above, \( u \), \( X \), and \( Y \) satisfy Assumptions 15.1–15.5.
Make clear exactly how each of the restrictions is used.
What does the Second Welfare Theorem (Theorem 15.4) then imply about the existence of a symmetric competitive equilibrium? c.
Show that under the stated restrictions Assumptions 15.6 and 15.7 are also satisfied.
What does Theorem 15.6 then imply about the existence of equilibrium prices that are representable by \( p \in \ell_1 \)?
Let \( (x^0, y^0) \) be the unique symmetric Pareto-optimal allocation for this economy, and let \( p \in \ell_1 \) represent a continuous linear functional supporting it as a competitive equilibrium.
Then the consumer’s budget constraint can be written as \( p \cdot x = p \cdot x^0 \).
(Note that since \( p \cdot x^0 = p \cdot y^0 \) is the value of the firm’s revenue stream, the right side of the budget constraint can be interpreted as the value of the consumer's share holdings in the profits of the representative firm.) Alternatively, the sequence \( r = \{r_t\}_{t=0}^\infty \) of one-period real interest rates can be defined by \[ U'(x_{t+1}) = \beta (1 + r_t) U'(x_t), \quad t = 0, 1, \dots \] and the budget constraint can be written as \[ x_t + \sum_{s=t+1}^\infty \frac{y_s}{(1 + r_t) \cdots (1 + r_{s-1})} \leq \sum_{s=t}^\infty \frac{y_s^0}{(1 + r_t) \cdots (1 + r_{s-1})}. \] With a little more structure on preferences, we can use these interest **Exercise 16.1** d.
Assume that \( U \) and \( f \) are continuously differentiable, and let \( (x^0, y^0, p) \) and \( r \) be as specified above.
Express the sequence of equilibrium real interest rates \( \{r_t\} \) in terms of marginal rates of substitution and transformation.
Show that the sequence \( r \) is uniquely determined and hence that relative prices in equilibrium are uniquely determined.
The allocation and prices \( (x^0, y^0, p) \) can be interpreted as the competitive equilibrium of a market held in period 0, in which claims to infinite sequences of dated goods are exchanged.
Alternatively, suppose that agents trade in a sequence of spot markets and that each agent has rational expectations (perfect foresight) about future spot prices.
We show next that the allocation \( (x^0, y^0) \) is also a competitive equilibrium under the latter market structure.
The analysis here is carried out for a particularly simple structure of spot markets; many others are possible.
Recall that in period 0 each firm is endowed with one unit of land and \( k \) units of capital and each household owns one firm.
If \( (x^0, y^0) \) is to be the equilibrium allocation under sequential trading on spot markets, then it must be the case that all firms have equal capital : land ratios and that each household owns one firm in every subsequent period as well.
In this case the state of the system in any period \( t \) is fully described by the economy-wide capital : land ratio, \( k_t \), and all spot prices are functions of this state variable.
Suppose that in each period there are spot markets for claims to next period’s consumption good and for shares in firms, all priced in units of the current consumption good.
A competitive equilibrium then consists of functions describing prices for claims to future consumption and for shares in firms, the investment by each firm, and the consumption and savings of each household, all as functions of the current state of the economy.
Formally, an equilibrium consists of functions \( (g, q, w, A, v, s) \), where - \( g(k) \) is the economy-wide law of motion for the state variable; - \( q(k) \) is the price, when the state is \( k \), of a claim to one unit of next period’s consumption good; - \( w(k, z) \) is the market value before the current dividend has been paid, in terms of the current consumption good, when the state is \( k \), of a firm that owns one unit of land and \( z \) units of capital; - \( A(k, z) \) is the investment undertaken, when the state is \( k \), by a firm that owns one unit of land and \( z \) units of capital; - \( v(k, a) \) is the value, when the state is \( k \), of the maximized objective function for a household whose initial assets are \( a \); - \( s(k, a) \) is the savings undertaken, when the state is \( k \), by a household whose initial assets are \( a \).
In equilibrium the representative household has assets \( a = p(k, k) \) and the representative firm has \( z = k \) units of capital; but to determine equilibrium prices, it is essential to be able to evaluate the consequences of individual deviations from equilibrium behavior.
In each period, firms sell consumption goods to households at a price of unity, pay the receipts from those sales to shareholders as dividends, and retain all unsold output as capital.
The firm takes the price functions \( q \) and \( w \) as given, as well as the economy-wide law of motion \( g \) and the current value \( k \) of the economy-wide capital stock.
Its own current capital stock \( z \) is also given.
Hence the decision problem facing the firm is as follows: given \( k \) and \( z \), choose the quantity of capital to accumulate (and hence the quantity of consumption goods to sell) to maximize the return to current shareholders.
Formally, its problem is described by the functional equation \[ (1) \quad w(k, z) = \max_{0 \leq z' \leq f(z)} \left\{ f(z) - z' + q(k) w(g(k), z') \right\}. \] The representative household owns assets and in each period makes a consumption-savings decision.
(Since there is no uncertainty, all assets must pay the same one-period rate of return.) Households, like firms, take the functions \( g \), \( q \), and \( w \) as given.
A household thus faces the decision problem: given the current state \( k \) and its own asset holdings \( a \) (measured in units of the current consumption good), choose a level for current consumption and the quantity of assets to hold for next period.
Formally, its problem is described by the functional equation \[ (2) \quad v(k, a) = \max_{0 \leq a' \leq q(k) a} \left\{ U(a - q(k) a') + \beta v(g(k), a') \right\}. \] These considerations motivate the following definition of a recursivecompetitive equilibrium as a set of functions (g, f, Q, w) such that (R1) w satisfies the functional equation (1), and f is the associated optimal policy function; (R2) Q satisfies the functional equation (2), and w is the associated optimal policy function; (R3) f(k, k) = g(k), all k > 0; (R4) f[k, Y(k, k)] = g[k, g(k)], all k > 0.
Conditions (R1) and (R2) express maximizing behavior by firms and households.
Condition (R3) says that the function f leads to investment decisions by firms that are compatible with the law of motion g.
Condition (R4) says that, in state k, a household with beginning-of-period assets Y(k, k), the value of one representative firm, chooses for next period assets [g(k, k)], the value of the same firm.
Hence the market for shares clears.
By Walras’ Law the market for consumption goods also clears.
To see this note that the household simply consumes the dividend paid by the firm that it owns.
Formally, (1) implies g(k, k) = {W(k, k) – [β – g(k)]}/ vl g(k), g(k)], so consumption in (2) is c = a – q(k)a’ = y(k) – g(k) Wl g(k), g(k)] = f(k) – g(k).
To show that the allocation (x0, y°) is an equilibrium for the sequential trading structure, we proceed as follows.
Let g be the policy function for the dynamic programming problem (3) v(k) = max {U[f(k) – g(k)] + βv(g(k))}, 0 ≤ g(k) ≤ f(k) and define c(k) = f(k) – g(k), all k > 0.
In view of the two welfare theorems and the nature of this economy, it is a natural conjecture that the optimal policy function g for this planning problem is also the economy-wide law of motion for capital in a recursive competitive equilibrium.
We pursue this idea in the rest of this section.
The first-order and envelope conditions for (2) suggest that the equilibrium price of a claim to consumption goods one period hence must be (4) q(k) = βU’[c(g(k))]/U’[c(k)].
Exercise 16.1 e.
Show that, given the functions g and q defined by (3) and (4), there is a unique bounded continuous function v satisfying (1) and that the associated optimal policy function is a single-valued continuous function.
Show that there is a unique bounded continuous function Q satisfying (2) and that the associated optimal policy function is a single-valued continuous function. f.
Show that if all firms use the decision rule f and all households use the decision rule w, then conditions (R3) and (R4) in the definition of a recursive competitive equilibrium hold. g.
Explain why parts (e) and (f) of this exercise establish that (x°, y°) is the equilibrium allocation in the economy with sequential trading.
The equilibrium for the recursive economy with a series of spot markets is thus the same as the equilibrium for the corresponding economy in which infinite sequences are traded in one grand market meeting in period 0.
The recursive formulation suggests a very different market interpretation, however, one that seems much closer to ordinary experience. 16.2.
Many-Sector Stochastic Growth The solutions to the models of optimal growth under uncertainty studied in Sections 10.1-10.3 and again in Section 13.1 can also be given a market interpretation.
Here we use the more general setup of Section 10.3, specializing it when useful.
Recall that there are I capital goods and M consumption goods each period.
Let the measurable space (Z, ℰ), the transition function Q, the initial state z₀ ∈ Z, the product spaces (Zᵗ, ℰᵗ), the probability measures νᵗ, the set X ⊂ ℝᵏ, the correspondence Φ: X × Z → ℝ x X, and the function u be as described in Section 10.3, and let them satisfy the assumptions stated there.
Let S^M = {c = {cₜ}ₜ₌₀^∞ : for each t, cₜ: Z → ℝ is a ℰ-measurable, essentially bounded function, with ||c|| = sup {ess sup |cₜ(z)|} < ∞}.
The normed vector space S^M is the commodity space.
The consumption set C for the representative consumer in this economy is the positive orthant of S^M, and u: C → ℝ as described in Section 10.3 represents the consumer’s preferences.
Define S^I analogously to S^M.
Given the initial capital stock x₀ ∈ ℝᵏ, the production set Y ⊂ S^M for this economy is defined by Y = {c ∈ S^M; there exists a sequence x = {xₜ}ₜ₌₀^∞ ∈ S^I such that x₀ = x₀, and (cₜ, xₜ₊₁) ∈ Φ(xₜ, zₜ), all t, all z ∈ Z}.
Exercise 16.2 a.
Show that (C, u, Y) satisfy Assumptions 15.1–15.7 and 15.8’-15.9’. b.
Let y* ∈ S^M be as defined in Section 10.3.
Show that there exists a continuous linear functional v such that (y*, y*, v) is a competitive equilibrium and that v can be represented as v(c) = ∫∑ₜ₌₀^∞ βᵗ u(cₜ(zₜ)) ∏ᵢ₌₀^{t-1} Q(dz_{i+1}|z_i) dz₀, all c ∈ S^M.
With these facts established, it is not difficult to develop prices for arbitrary securities.
We use the recursive formulation of equilibrium introduced in Section 16.1, letting the representative consumer trade away from the equilibrium allocation by buying or selling the security whose price we wish to calculate.
Since the consumer is already in a complete market equilibrium, he never chooses to exercise this option.
This fact allows us to calculate the formula for the price of the security.
We consider one-period securities first.
For simplicity, we restrict attention to a single consumption good, M = 1.
Both the price and the returns from the security will be expressed in terms of this good.
(Alternatively, we could pick one of M consumer goods as the good being claimed, as in ordinary commodities futures markets.) Let f: Z → ℝ be a bounded measurable function.
Any such function defines a one-period security, where f(z’) is interpreted as the return per unit of the security if next period’s state is z’.
Let q(x, z) be the price of one unit of this security if it is purchased in state (x, z).
Let g be the policy function for the optimal growth model of Section 10.3, and let c be the associated consumption function: c(x, z) = argmax U(c) s.t. [c, g(x, z)] ∈ Φ(x, z). c ∈ ℝ, Let w(Λ, x, z) be the maximized present discounted utility, if the current state is (x, z), of a consumer who has a claim in perpetuity to c(x, z) units of consumption whenever state (x, z) occurs, and in addition a claim to Λ units of the current consumption good.
He can divide this claim between an increment δ (possibly negative) to his current consumption and a purchase at the price q(x, z) of b units of the security.
To ensure that maximization is over a compact set, we give the consumer a credit limit of –∞ < b < ∞.
This constraint does not bind in equilibrium.
Then w must satisfy (1) w(Λ, x, z) = max {U(c, z) + β] c,δ,b +β ∫ w{c(x, z) – b + f(z’), g(x, z), z’} Q(dz’|z) s.t. δ + g(x, z) = Λ, c(x, z) + δ = 0, b = b.
Exercise 16.2 c.
Show that there exists a unique bounded continuous function w satisfying (1). d.
Assume that U is differentiable.
Show that if c(x, z) > 0 for some fixed (x, z) ∈ X × Z, then w(·, x, z) is differentiable in its first argument and w₁(0, x, z) = U’[c(x, z)].
We maintain the assumption that U is differentiable in the rest of the problem.
The first-order condition for (1) is U’[c(x, z) + δ – q(x, z)b] q(x, z) = β ∫ U’ [c(g(x, z), z’)] f(z’) Q(dz’|z), and in equilibrium it must be the case that Λ = δ = 0.
Using this fact and combining the first-order and envelope conditions, we obtain (2) U’[c(x, z)] q(x, z) = β ∫ U’ (c[g(x, z), z’]) f(z’) Q(dz’|z).
Since the functions c and g have been solved for already, (2) characterizes the function q(x, z) that expresses the price, as a function of the current state, of the security with returns f(·).
This formula can easily be specialized to particular cases.
Exercise 16.2 e.
What is the price of a claim to one unit of consumption one period hence with certainty?
What is the price of a bond that pays one unit if the event E ∈ ℰ occurs and zero otherwise? f.
Lottery tickets (pure gambles) can also be priced with (2).
Supposenonnegative orthant of $L$.
Three additional requirements define $Y$: the beginning-of-period capital stock in each period $t$ is at least as great as the depreciated stock carried over from the previous period (so gross investment is nonnegative); production in each period $t$ is no greater than the firm's beginning-of-period capital stock; and gross investment in each period is sufficient to cover net additions to the capital stock.
The beginning-of-period capital stock in period 0, $k_0 = 0$, is given.
For $t = 0, 1, \ldots$, we use $h_{t+1}(z^t, \theta) \in L_+(Z^t, \theta, L_0)$ to denote its beginning-of-period capital stock in period $t+1$, as a function of the history of shocks through period $t$.
With this notation, the production set $Y$ can be defined as follows: (1) $Y = \{(q, I) \in L_s$: there exists $k = \{k_t\}_{t=0}^\infty$ such that: $$k_{t+1}(z^t) \ge a(z^t, F(z^t)), \quad t=0, 1, \ldots;$$ $$k_t = (1 - \delta)k_{t-1}, \quad g_t \ge 0; \quad k_t = h_t(k_{t-1});$$ $$k_{t+1}(z^t) = (1 - \delta)R(z^{t+1}), \quad t=1,2,\ldots, \text{ all } z^{t+1};$$ $$g_t(z^t) \le k_t(z^t), \quad t=1,2,\ldots, \text{ all } z^t;$$ $$T(z^t) = h_t(z^t)E[R_t | z^t, k_t(z^t)], \quad t=1,2,\ldots, \text{ all } z^t\}.$$ We define an industry equilibrium as an allocation $(q, I)$ together with a sequence of prices $p = \{p_t\}_{t=0}^\infty$, with $p_t \in L_\infty(Z^t, \theta, L_0)$, all $t$, such that $$\text{(I1) } (q, I) \in Y;$$ $$\text{(I2) } p_t = D(q_t, z^t), \quad \text{all } t, \text{ all } z^t;$$ $$\text{(I3) } E\left\{ \sum_{t=0}^\infty \beta^t [p_t q_t - r_t I_t] \right\} \ge E\left\{ \sum_{t=0}^\infty \beta^t [p_t q_t' - r_t I_t'] \right\}$$ $$\text{all } (q', I') \in Y.$$ That is, an equilibrium allocation must be feasible, it must be market clearing at equilibrium prices [remember that $D(q, z) = U_q(q, z) = \partial U(q, z)/\partial q$ is the market inverse demand function], and it must maximize the expected discounted value of profits at equilibrium prices.
As we did in Section 10.4, we define a surplus-maximizing allocation as an allocation $(q, I)$ such that condition (I1) holds and $$\text{(I4) } E\left\{ \sum_{t=0}^\infty \beta^t [U(q_t, z^t) - r_t I_t] \right\} \ge E\left\{ \sum_{t=0}^\infty \beta^t [U(q_t', z^t) - r_t I_t'] \right\}$$ $$\text{all } (q', I') \in Y.$$ That is, a surplus-maximizing allocation must be feasible and must maximize total (consumers' plus producers') surplus over all feasible allocations. **Exercise 16.4** a.
Reformulate the definitions of a surplus-maximizing allocation and of an industry equilibrium for the case when there are $J$ identical firms in the industry.
In Section 10.4 we showed that there is a unique surplus-maximizing allocation.
Here we want to establish that, at the prices given by condition (I2), this allocation is also the unique industry equilibrium.
One way to do this is to establish analogues to Theorems 15.3 and 15.4 by methods specific to this particular problem.
To this end we first establish the following result. **Exercise 16.4** b.
Show that if $(q, I, p)$ is an industry equilibrium, then $(q, I)$ is a surplus-maximizing allocation. [Hint.
Use the fact that the concavity of $U$ implies $$U(q_1, z) \le U(q_0, z) + U_q(q_0, z)(q_1 - q_0), \quad \text{all } (q_0, q_1, z)$$ to show that conditions (I2) and (I3) imply condition (I4).] Together with the results of Section 10.4, Exercise 16.4b implies that there is at most one industry equilibrium.
To show that there is exactly one industry equilibrium, we use this fact together with the next result. **Exercise 16.4** c.
Show that if $(q, I)$ is a surplus-maximizing allocation and $p$ is defined by condition (I2), then $(q, I, p)$ is an industry equilibrium. [Hint.
Let $(q, I)$ be a surplus-maximizing allocation, and for any $(q', I') \in Y$ define $f: [0, 1] \to \mathbb{R}$ by $$f(\epsilon) = E \left\{ \sum_{t=0}^\infty \beta^t \left[ U((1-\epsilon)q_t + \epsilon q_t', z^t) - r_t ((1-\epsilon)I_t + \epsilon I_t') \right] \right\}$$ $$ - \left[ (1-\epsilon) + \epsilon E \left\{ \sum_{t=0}^\infty \beta^t [p_t q_t' - r_t I_t'] \right\} \right].$$ Since $Y$ is convex, $f$ is well defined; and since $(q, I)$ is optimal, $\epsilon = 0$ maximizes $f$ over the interval $[0, 1]$.
Use the first-order condition for a maximum to complete the argument.] The result in Exercise 16.4c is the analogue, for this problem, to Theorem 15.4.
It is much easier to establish, however: since condition (I2) provides a candidate for the supporting prices, the Hahn-Banach Theorem is not needed.
Note that with differentiable, strictly concave preferences, we could have taken this same approach in Sections 16.1–16.3.
Alternatively, as we next show, we can apply Theorems 15.3 and 15.4 to the present problem.
The idea is to invent a synthetic consumer, whose marginal conditions are equivalent to condition (I2).
Let $X = L_+$. be the consumption set for this consumer.
Define his preferences on $X$ by $$u(x) = E \left\{ \sum_{t=0}^\infty \beta^t \left[ U(q_t(x), z^t) - r_t I_t(x) \right] \right\},$$ where the expectation is over the $z^t$'s given $z$. **Exercise 16.4** d.
Show that the pair $(X, u)$ satisfies Assumptions 15.1–15.3.
Show that $Y$ as defined in (1) satisfies Assumptions 15.4 and 15.5.
For the economy defined by $(X, u, Y)$, surplus-maximizing allocations as defined above are clearly Pareto optimal. **Exercise 16.4** e.
Apply Theorems 15.3–15.6 to prove the results in parts (b) and (c) of this exercise. **16.5 Truncation: A Generalization** In this problem we prove a generalization of Theorem 15.6 that is useful when the zero element $0$ is not an element of the consumption set of some or all consumers.
Recall that the main idea of Theorem 15.6 was that under Assumptions 15.6 and 15.7, if $x$ is in $X$, then for all $T$ sufficiently large the truncated allocation $x^T = (x_1, x_2, \ldots, x_T, 0, 0, \ldots)$ is also in $X$; and yields almost as much utility.
For one-period utility functions that are not well defined at zero, this approach fails.
But an analogous result can be obtained by truncating to a point other than zero.
For simplicity take $l_\infty$ to be the commodity space.
Let $\phi$ be a continuous linear functional on $l_\infty$, and let $W: l_\infty \to \mathbb{R}$ be defined by $$W(x) = \lim_{T \to \infty} \phi(x^T).$$ As shown in the first part of Lemma 15.5, this limit exists.
The following result plays the role of the second part of that lemma. **Exercise 16.5** a.
Show that for any $x, a \in l_\infty$, $$\lim_{T \to \infty} \phi(x_1, x_2, \ldots, x_T, a, a, \ldots) = \phi(x) - W(a) + W(a).$$ The idea behind this result is that each side of (2) expresses the "weight at infinity" that the linear functional $\phi$ assigns to the point $a \in l_\infty$.
In place of Assumptions 15.6 and 15.7, we need the following. **ASSUMPTION 16.1** There exists an allocation $[(a_i), (b_j)]$ such that a. for each $i$, if $x_i \in X_i$, then for all $T$ sufficiently large, $x^T = (x_{i1}, \ldots, x_{iT}, a_{i,T+1}, a_{i,T+2}, \ldots) \in X_i$; b. for each $j$, if $y_j \in Y_j$, then for all $T$ sufficiently large, $y^T = (y_{j1}, \ldots, y_{jT}, b_{j,T+1}, b_{j,T+2}, \ldots) \in Y_j$; c. $\sum_i a_i = \sum_j b_j$; d. for each $i$, if $x_i, \hat{x}_i \in X_i$ and $u_i(x_i) > u_i(\hat{x}_i)$, then for all $T$ sufficiently large, $u_i(x_{i1}, \ldots, x_{iT}, a_{i,T+1}, a_{i,T+2}, \ldots) > u_i(\hat{x}_{i1}, \ldots, \hat{x}_{iT}, a_{i,T+1}, a_{i,T+2}, \ldots)$.
Note that the allocation $[(a_i), (b_j)]$ need not be feasible.
However, it is useful to think of $a_i$ as a subsistence allocation for agent $i$.
Let Assumptions 15.1–15.5 and 16.1 hold; let $[(x^*_i), (y^*_j), \phi]$ be a feasible allocation and a continuous linear functional such that $$(3) \quad \text{for each } i, \text{ if } x_i \in X_i \text{ and } u_i(x_i) = u_i(x^*_i) \text{ then } \phi(x_i) = \phi(x^*_i);$$ $$(4) \quad \text{for each } j, \text{ if } y_j \in Y_j \text{ then } \phi(y_j) \le \phi(y^*_j);$$ and suppose that for each $i$ there exists $\hat{x}_i \in X_i$ such that $u_i(\hat{x}_i) > u_i(x^*_i)$.
Let $W$ be the continuous linear functional defined by (1). **Exercise 16.5** b.
Show that for each $i$, if $x_i \in X_i$ and $u_i(x_i) = u_i(x^*_i)$ implies $$W(x_i) + [\phi(a_i) - W(a_i)] = \phi(x^*_i);$$ and for each $j$, if $y_j \in Y_j$ implies $$W(y_j) + [\phi(b_j) - W(b_j)] \le \phi(y^*_j).$$ c.
Show that $$\phi(\sum_i x^*_i) - W(\sum_i x^*_i) = \sum_i [\phi(a_i) - W(a_i)]; \text{ and}$$ $$\phi(\sum_j y^*_j) - W(\sum_j y^*_j) = \sum_j [\phi(b_j) - W(b_j)].$$ d.
Show that $$\phi(x^*_i) = W(x^*_i) + [\phi(a_i) - W(a_i)], \quad \text{all } i; \text{ and}$$ $$\phi(y^*_j) = W(y^*_j) + [\phi(b_j) - W(b_j)], \quad \text{all } j.$$ e.
Show that (3) and (4) hold with $W$ in place of $\phi$. **16.6 A Peculiar Example** The following example illustrates what Theorem 15.4, the Remark following that theorem, and Theorem 15.6 do not say about supporting prices.
The example consists of a pure exchange economy with one household, so the unique Pareto-optimal allocation is for the household to consume the entire endowment.
Thus, the only interesting questions involve the existence and qualitative properties of prices supporting this allocation as a competitive equilibrium.
The commodity space is $l_\infty$ and the household's consumption set is $X = l_{\infty+}$, the positive orthant of $l_\infty$.
The household's preferences are represented by the utility function $u: X \to \mathbb{R}$ defined by $$u(x) = \sum_{t=1}^\infty \lambda_t \left[1 - \exp(-x_t^{0.9})\right].$$494 16 | Applications of Equilibrium Theory Note that \(x\) is bounded, continuous, strictly increasing, and strictly concave, with \[ \frac{du(x)}{dx_t} = \exp(-x_t^2) > 0, \] \[ \frac{d^2u(x)}{dx_t^2} = -2x_t \exp(-x_t^2) < 0, \quad \text{all } t. \] The aggregate production possibility set is \[ Y = \{y \in \ell_{\infty} : y \leq \sum_i x_i, \text{ all } i\}. \] Note that the production set includes the entire negative orthant.
Clearly, the unique Pareto-optimal allocation for this economy is given by \(x^* = y^* = (4, 4, 4, \ldots)\).
The question, then, is whether this allocation can be supported as a competitive equilibrium, and if so, what the supporting prices look like.
The following result is easy to establish.
Exercise 16.6 a.
Show that Assumptions 15.1–15.7 are satisfied.
It follows immediately that Theorems 15.4 and 15.6 hold.
Thus by Theorem 15.4 there exists a continuous linear functional \(\phi\) on \(\ell_{\infty}\), not identically zero, such that \[ (1) \; x \in X \text{ and } u(x) = u(x^*) \text{ implies } \phi(x) = \phi(x^*); \] \[ (2) \; y \in Y \text{ implies } \phi(y) = \phi(y^*). \] For any \(x \in \ell_{\infty}\), let \(x^T\) denote the truncated sequence \(x^T = (x_1, \ldots, x_T, 0, 0, \ldots)\).
Lemma 15.5 implies that \(w: \ell_{\infty} \to \mathbb{R}\) defined by \[ (3) \; v(x) = \lim_{T \to \infty} \phi(x^T), \quad \text{all } x \in \ell_{\infty}, \] is also a continuous linear functional, and Theorem 15.6 implies that (1) and (2) hold with \(w\) in place of \(\phi\).
Finally, since \(X\) is the entire positive orthant of \(\ell_{\infty}\), the Remark following Theorem 15.4 implies that if \(\phi(x^*) \neq 0\), then \((x^*, y^*, \phi)\) is a competitive equilibrium.
In the rest of this section we characterize in more detail the continuous linear functionals \(\phi\) and \(w\) satisfying (1) and (2), and determine whether any of them constitute competitive equilibrium prices.
An obvious candidate for a competitive equilibrium is to take \(\phi\) to be the continuous linear functional corresponding to the price vector \(p = (p_0, p_1, p_2, \ldots)\), where each price \(p_t\) is proportional to the marginal utility of consumption in period \(t\).
Since \[ \left. \frac{du(x)}{dx_t} \right|_{x=x^*} = \exp(-x_t^2) = \exp(-1), \quad \text{all } t, \] any price vector of the form \(p = (c, c, c, \ldots)\), for some \(c > 0\), would seem to be a natural candidate to support \(x^*\) as a competitive equilibrium.
Exercise 16.6 b.
Show that a price vector \(p\) of this form does not define a continuous linear functional on \(\ell_{\infty}\). [Hint: Use Theorem 15.1.] c.
Let \(\phi\) be any continuous linear functional satisfying (1) and (2), and let \(w\) be the continuous linear functional defined by (3).
Show that \(w(x) = 0\), all \(x \in \ell_{\infty}\). d.
Suppose that for this example we take the commodity space to be \(\ell_1\).
Show that in this case the production set \(Y\) has an empty interior.
Show that \((x^*, y^*, p)\) is a competitive equilibrium, where \(p \in \ell_1\) is any price vector of the form \(p = (c, c, \ldots)\), \(c > 0\). 16.7 An Economy with Many Consumers Although most of the dynamic applications of the theory of Chapter 15—including all of the applications so far in this chapter—deal with one-consumer economies, the theory can deal with any finite number of agents, with preferences differing among them.
In this section we treat a fairly general deterministic, recursive system with many agents, a generalization of the two-consumer exchange economy studied in Section 5.13.
The commodity space is \(\ell_{\infty}^J\), the set of sequences \(c = \{c_t\}_{t=0}^{\infty}\) such that \[ \|c\| = \sup_t \|c_t\| < \infty, \] where \(c_t \in \mathbb{R}^J\), all \(t\), and \(\|\cdot\|\) is the Euclidean norm on \(\mathbb{R}^J\).
There are \(i = 1, \ldots, J\) consumers, each with the consumption set \(C = \ell_{\infty}^+\).
Consumer \(i\) has preferences induced by an aggregator function \(W_i: \mathbb{R}_+^J \times \mathbb{R}_+ \to \mathbb{R}_+\), that is assumed to satisfy conditions (W1)–(W5) of Section 5.11.
In Exercise 5.11d we showed that any such aggregator function defines a utility function \(u_i: C \to \mathbb{R}_+\), the unique fixed point of the operator \(T_{W_i}\), defined there.
We also showed that \(u_i\) is bounded and continuous in the sup norm, is increasing and concave, and satisfies \[ |u_i(c) - u_i(c')| \leq \beta \|c - c'\|, \quad \text{all } c \in C, \] where \(c^T = (c_0, c_1, \ldots, c_T, 0, 0, \ldots)\) and where \(l = \sup_{c \in C} |u_i(c)|\).
Thus \(C\) and \(u_i\) satisfy Assumptions 15.1–15.3 and 15.6–15.7.
Next we construct the production set \(Y \subset \ell_{\infty}^J\); the method of construction ensures that the resulting technology is recursive.
Assume that the state of the system in any period is characterized by a vector \(k \in \mathbb{R}^K\) of capital goods.
Production during the period yields a vector \(y \in \mathbb{R}^J\) of current consumption goods and a vector \(k' \in \mathbb{R}^K\) of beginning-of-period capital stocks for the following period.
Feasible production within any period is thus characterized by a correspondence \(\Phi: \mathbb{R}^K \to \mathbb{R}^J \times \mathbb{R}^K\).
This correspondence is restricted as follows.
(T1) \(\Phi\) is continuous; (T2) for each \(k\), \(\Phi(k)\) is compact and convex; (T3) \((y, k') \in \Phi(k)\) and \(0 = (y', k') \leq (y, k')\) implies \((y', k') \in \Phi(k)\); (T4) \(k' \leq k\) implies \(\Phi(k') \subset \Phi(k)\); (T5) \((y, k') \in \Phi(k)\), \((y', k') \in \Phi(k')\), and \(\theta \in [0, 1]\) implies \[ [\theta y + (1 - \theta) y', \theta k + (1 - \theta) k'] \in \Phi[\theta k + (1 - \theta) k']; \] (T6) the set \(M = \{k \in \mathbb{R}^K: (0, k) \in \Phi(k)\}\) has a nonempty interior; (T7) if \(k\) is an interior point of \(M\), then \((y, k') \in \Phi(k)\) for some \(y \gg 0\).
Assumptions (T1)–(T3) restrict current-period production possibilities, given \(k\), and (T4) and (T5) restrict the way \(\Phi\) varies with \(k\).
As we will see shortly, Assumptions (T6) and (T7) ensure that the production set in the sense of Chapter 15 has a nonempty interior.
We use the production correspondence \(\Phi\) to define the production set \(Y\) for a given initial capital vector \(k\) exactly as we did in Sections 16.1 and 16.2: \[ Y(k) = \{c \in \ell_{\infty}^J: \text{there exists } k \in \ell_{\infty}^K \text{ with } k_0 = k, \text{ and} \] such that \((c_t, k_{t+1}) \in \Phi(k_t), \; t = 0, 1, 2, \ldots \}. \] Thus \(Y(k)\) is the set of consumption sequences that are feasible given the initial capital stock \(k\).
Exercise 16.7 a.
Show that for any \(k \in \mathbb{R}^K\), \(Y(k)\) is closed and convex and satisfies Assumption 15.6.
Show that if \(k\) is an interior point of the set \(M\) defined in Assumption (T6), then \(Y(k)\) has an interior point.
If preferences satisfy assumptions (W1)–(W5), if the technology satisfies assumptions (T1)–(T7), and if \(k\) is an interior point of \(M\), then the economy defined by \(C, u_1, \ldots, u_J\), and \(Y(k)\) satisfies Assumptions 15.1– 15.7.
Hence in this case the First and Second Welfare Theorems (Theorems 15.3 and 15.4) apply, as does Theorem 15.6.
The rest of this problem is concerned with the construction of this economy’s Paretooptimal allocations, which thus coincide with its competitive equilibrium allocations.
As we did in Chapter 15, we will use the notation \([(c_i), y]\) to denote an allocation.
We call an allocation feasible from \(k\) if \(c_i \in C\), all \(i\), \(y \in Y(k)\), and \(\sum_i c_i = y\).
We begin by defining this economy’s utility possibility set: \[ (1) \; U(k) = \{z \in \mathbb{R}^J: z_i = u_i(c_i), \text{ all } i, \text{ for some allocation} \] \[ [(c_i), y] \text{ that is feasible from } k\}. \] Next, let \(\Delta^J\) denote the unit simplex in \(\mathbb{R}^J\) and define the support function \(v: \mathbb{R}^K \times \Delta^J \to \mathbb{R}\), of \(U\) by \[ (2) \; v(k, \theta) = \sup_{z \in U(k)} \sum_{i=1}^J \theta_i z_i. \] From the definition of \(U\), it follows that we can also write \[ (3) \; v(k, \theta) = \sup_{c_i, y} \sum_{i=1}^J \theta_i u_i(c_i) \] \[ \text{s.t. } c_i \geq 0, \text{ all } i, \] \[ \sum_i c_i = y, \quad y \in Y(k). \] Exercise 16.7 b.
Prove that an allocation is Pareto optimal if and only if it attains the supremum in (3).
We next formulate a functional equation for the support function \(v\) and analyze it using the methods of Chapter 4.
The utility that consumer \(i\) receives from the allocation \(c_i\) is the utility he gets from the first term in the sequence, \(c_{i0}\), and from the remaining terms \((c_{i1}, c_{i2}, \ldots)\).
Evaluated in terms of the aggregator function \(W_i\), his utility from \(c_i\) is \[ u_i(c_i) = W_i(c_{i0}, u_i(c_{i1}, c_{i2}, \ldots)). \] The feasible \(J\)-vectors of utilities from next period on, \(u_i(c_{i1}, c_{i2}, \ldots)\), \(i = 1, 2, \ldots, J\), are the points \(z'\) in the set \(U(k')\), where \(k'\) is next period’s vector of capital stocks.
Hence (2) may be rewritten as \[ (4) \; v(k, \theta) = \sup_{y, k'} \sum_{i=1}^J \theta_i W_i(y_i, z_i') \] \[ \text{s.t. } z' \in U(k'), \] \[ (y, k') \in \Phi(k). \] Since \(U\) is defined by (1), (4) is a functional equation in the unknown function \(v\).
But the constraint that \(z'\) must lie in \(U(k')\) is equivalent to a statement about \(z'\) and the support function \(v(k', \cdot)\).
Exercise 16.7 c.
Prove that for any \(k \in \mathbb{R}^K\), \(z \in U(k)\) if and only if \(v(k, \theta) \geq \sum_i \theta_i z_i\), for all \(\theta \in \Delta^J\).Finally, fiat money, of which there is a fixed supply M, is the only store of value.
In each period, the young agents produce goods and sell them to the old in exchange for fiat money; this market is perfectly competitive.
This economy is competitive, but it does not satisfy the conditions of Chapter 15 under which competitive equilibrium allocations and Pareto-optimal allocations coincide.
(Why not?) Nevertheless, we can define a stationary competitive equilibrium for this economy and then study the existence, uniqueness, and properties of such equilibria by direct methods.
In this economy the technology shock x is the only state variable.
Let x be an element of a closed, bounded interval [a, b] = X ⊂ R₊; let 𝒷 be the Borel subsets of X; and let τ: X × 𝒷 → [0, 1] be a transition function.
Define a stationary competitive equilibrium in which money is valued to be a price function p: X → R₊, and a labor supply function n: X → [0, L) such that (1) n(x) ∈ argmax {−H(n) + β ∫ V[F(xn, x′)] τ(dx, x′)} for all x ∈ X; (2) xn(x) = M/p(x), for all x ∈ X.
The first condition is that given the price function p and the current state x, a young individual’s optimal labor supply is n(x).
The labor he supplies produces xn(x) units of output, which he sells for xn(x) p(x) units of money.
In his old age he uses all his money balances to buy goods, but since the price of goods next period is random, so is his consumption xn(x) p(x)/p(x′).
The second condition is that the supply and demand for goods, and hence, by Walras’s Law, for money are equal in every state.
In order to analyze this system, we need to place restrictions on the functions H and V.
The following assumption, although stronger than necessary, is very convenient.
ASSUMPTION 17.1 H: [0, L) → R₊ is twice continuously differentiable, strictly increasing, and strictly convex, with H(0) = 0 and lim_{n→L} H(n) = +∞, V: R₊ → R, is twice continuously differentiable, strictly increasing, and strictly concave.
(Note that labor supply is assumed to be bounded below by zero and above by L −.) Exercise 17.1 Show that under Assumption 17.1, given any measurable price function p: X → R₊ that is uniformly bounded away from zero, and any x ∈ X, the unique solution n(x) to the consumer’s problem (1) satisfies the first-order condition −H′(n) + β ∫ F₂(xn, x′) τ(dx, x′) = 0.
Show that the solution is always strictly positive: n(x) > 0 for all x.
Multiplying this first-order condition by n(x) and substituting from (2) to eliminate p(x) and p(x′), we obtain (3) n(x)H′[n(x)] = ∫ x′n(x′)V′[x′n(x′)] τ(dx, x′), for all x ∈ X.
Given any strictly positive, measurable function n satisfying (3), for the price function p(x) = M/xn(x) the pair (n, p) is a stationary competitive equilibrium.
Hence questions about the existence and uniqueness of a stationary equilibrium are essentially questions about the existence and uniqueness of a strictly positive function n satisfying (3).
Define φ: [0, L) → R₊ by φ(l) = lH′(l) and ψ: R₊ → R₊ by ψ(y) = yV′(y), so that (3) can be written as (4) E[ψ(x′n(x′))] = φ(n(x)), for all x ∈ X.
Equation (4) is a single equation in the unknown function n(x).
In some respects it appears simpler than the functional equations we studied in Chapters 4 and 9, since it does not involve a maximization operator.
It is not a special case of the equations we have examined earlier, however, so our concern in this chapter is with methods suitable for analyzing it and other equations of the same general type.
It is instructive to begin the analysis of (4) by considering first the special case of serially independent shocks.
In this case the right side of (4) does not depend on x, so a solution is simply a number n > 0 satisfying (5) φ(n) = ∫ ψ(x′n) τ(dx′).
We then have the following result.
(To distinguish the highly specific results we use as illustrations, we call them propositions.)
### PROPOSITION 1
Let X = [a, b] ⊂ R₊, with its Borel subsets 𝒷, and let τ be a probability measure on (X, 𝒷).
Let H and V satisfy Assumption 17.1, and define φ and ψ as above.
Then (5) has a unique solution n > 0.
**Proof.** Under Assumption 17.1, the function φ is once continuously differentiable, with φ′(l) = H′(l) + lH″(l).
Hence φ is strictly increasing, with φ(0) = 0; φ′(0) = 0; φ′(l) > 0, for all l ∈ (0, L); and lim_{l→L} φ(l) = +∞.
Moreover, the elasticity of φ is greater than one, ε_φ(l) = (lφ′(l))/φ(l) = 1 + (lH″(l))/H′(l) > 1, for all l ∈ (0, L), (6) with equality only at l = 0.
The function ψ is once continuously differentiable, with ψ′(y) = V′(y) + yV″(y).
Hence ψ may be either increasing or decreasing but is strictly increasing at zero, ψ′(0) = V′(0) > 0.
Moreover, its elasticity is less than one, ε_ψ(y) = (yψ′(y))/ψ(y) = 1 + (yV″(y))/V′(y) < 1, for all y > 0, (7) with equality only at y = 0.
There are two cases to consider, shown in Figure 17.1, where φ(l) and E[ψ(x′l)] = ∫ ψ(x′l) τ(dx′) are graphed as functions of l.
Note that their derivatives are φ′(l) and E[x′ψ′(x′l)] respectively.
If ψ′(0) > 0, then at l = 0 we have φ(0) = 0 < E[ψ(0)] = ψ(0), as shown in the top panel of Figure 17.1.
If ψ′(0) = 0, then at l = 0 we have φ(0) = 0 = E[ψ(0)] = ψ(0).
Since 0 < ψ′(0), however, it follows that φ′(0) = 0 < E[x′ψ′(0)] so that φ(l) < E[ψ(x′l)] in the neighborhood of l = 0, as shown in the bottom panel of Figure 17.1.
Since both functions are continuous, and since lim_{l→L} φ(l) = +∞ and E[ψ(x′L)] < +∞, the existence of a solution l > 0 follows immediately in either case.
To establish uniqueness, first note that for any l > 0, ψ(x′l) > 0, for all x′ ∈ X, and ∫ τ(dx′) = 1.
(4) E[ψ(x′l)] E[ψ(x′l)] 0 n L 4 Figure 17.1 Hence it follows from (6) and (7) that d/dl [E[ψ(x′l)]/φ(l)] = [E[x′ψ′(x′l)]φ(l) − E[ψ(x′l)]φ′(l)] / φ(l)² = [E[x′ψ′(x′l)]/E[ψ(x′l)]] * [E[ψ(x′l)]/φ(l)] − φ′(l)/φ(l) < 1 * [E[ψ(x′l)]/φ(l)] − 1, for all l > 0, where the second inequality uses the fact that the integral on the right is a convex combination of terms that are less than one.
Suppose n > 0 satisfies (5).
Then φ(n) = E[ψ(x′n)], and if we use this fact to cancel terms in the inequality above we find that φ′(n) > E[x′ψ′(x′n)].
Therefore, at any intersection the φ(l) curve crosses the E[ψ(x′l)] curve from below.
Hence the two curves cross only once, as shown in the figures, and there is only one strictly positive solution. □ For the case of independent shocks, then, the existence and uniqueness of the solution to (4) follows in a straightforward way from fairly standard assumptions on preferences.
To study the case when shocks are serially correlated, it is convenient to put (4) into a slightly different form.
Under Assumption 17.1, the function φ is continuous, strictly increasing, and onto.
Hence the inverse function φ⁻¹: R₊ → [0, L) is well defined, continuous, strictly increasing, and onto.
Therefore a bounded, continuous, strictly positive function n*: X → [0, L) satisfies (4) if and only if the bounded, continuous, strictly positive function f*: X → R₊ defined by f*(x) = φ[n*(x)] satisfies (8) f*(x) = ∫ ψ( f*(x′)/x′ * x′ ) τ(dx, x′), for all x ∈ X.
To study the existence of solutions to (8), we define the operator T on functions f: X → R₊ by (9) (Tf)(x) = ∫ ψ( f(x′) ) τ(dx, x′).
A function f* satisfies (8) if and only if it is a fixed point of T.
Hence the problem of finding equilibria of the overlapping-generations model has been converted into one of finding strictly positive functions f* that are fixed points of the operator T defined in (9).
In the next sections we pursue four different, mutually complementary strategies.
The first strategy, followed in Section 17.2, is to seek conditions sufficient to ensure that the operator T is a contraction mapping.
The required conditions are restrictions on preferences stronger than those stated in Assumption 17.1.
The second approach is to make the state space finite.
That is, let the state space be X = {x₁, ..., xₘ}, with transitions described by matrix π = [πᵢⱼ].Proof.
By Lemma 17.6, it suffices to show that the sequence of functions \(\{T^n f_0\}\) converges pointwise.
Suppose that \(f_0 \le T f_0\); then it follows by induction that the sequence \(\{T^n f_0\}\) is weakly increasing.
Since the set \(F\) is closed and bounded, it also follows that the limiting function \(f = \lim T^n f_0\) exists.
A similar argument applies if \(f_0 \ge T f_0\).
The following corollary illustrates how Theorem 17.7 can be used.
It shows that if \(T\) is monotone and if \(f_0\) and \(g_0\) are minimal and maximal elements of \(F\), then every fixed point \(h\) of \(T\) satisfies \[ \lim T^n f_0 \le h \le \lim T^n g_0. \]
### COROLLARY L
et \(X, F,\) and \(T\) satisfy the hypotheses of Theorem 17.7.
If \(f_0 \le h_0\) for all \(h_0 \in F\), then \(\lim T^n f_0 = f = h\) for all fixed points \(h\) of \(T\) in \(F\).
A similar conclusion holds with the inequalities reversed.
**Proof.** Suppose that \(f_0 \le h_0\), all \(h_0 \in F\).
Then \(f_0 \le T f_0\), and Theorem 17.7 implies that \(f = \lim T^n f_0 \in F\) exists and is a fixed point of \(T\).
Suppose that \(A\) is a fixed point of \(T\).
Since \(f_0 \le A\) and \(T\) is monotone, it follows that \(T f_0 \le T A = h\).
Hence by induction, \(f_0 \le T^n h = h, n = 1,2,...\), and taking the limit we find that \(f \le h\).
A similar argument holds with the inequalities reversed.
This corollary provides a useful computational check on the multiplicity of fixed points.
If \(f\) and \(g\) are the fixed points obtained by applying \(T\) to minimal and maximal elements of \(F\) respectively, and if it should turn out that \(f = g\), then this function is the unique fixed point of \(T\).
Now consider the assumptions that are needed to apply Theorem 17.7 and its corollary to functional equations of the type discussed in the earlier sections.
As before let \(X \subset \mathbb{R}^l\) be a bounded set, let \(T\) be a transition function on \((X, \mathscr{B})\), and let \(T\) satisfy Assumption 17.3.
Let \(D = [a, b] \subset \mathbb{R}\) be a nonempty, closed, bounded interval; and let \(F \subset C(X)\) be the family of functions \(f: X \to D\).
Let \(G: X \times X \times D \to D\) be a continuous function, and assume that \(G\) is uniformly continuous in its first and last arguments.
Consider the operator \(T\) on \(F\) defined by \[ (Tf)(x) = \int_X G(x, x', f(x')) d\mu(x'), \text{ all } x \in X. \] Under the stated conditions, \(F\) is closed and bounded, \(T\) maps \(F\) into itself, \(T(F)\) is equicontinuous (by Lemma 17.5), and \(T\) is a continuous operator (by Exercise 17.6).
Moreover, the functions \(f_0(x) = a\) and \(g_0(x) = b\), all \(x \in X\), satisfy \(f_0 \le h_0 \le g_0\), all \(h_0 \in F\).
Hence, to apply Theorem 17.7 it suffices to show that \(T\) is monotone.
Clearly this is so if \(G\) is weakly increasing in its third argument.
We conclude this section by applying Theorem 17.7 and its corollary to the overlapping-generations model discussed earlier.
The following additional assumption on preferences is required.
ASSUMPTION 17.4 \(-y V''(y)/V'(y) = 1\), all \(y \in \mathbb{R}_+\).
It is instructive to compare Assumptions 17.2 and 17.4.
Note that the monotonicity and concavity of \(V\) (Assumption 17.1) imply that \[ 0 < -y V''(y)/V'(y), \text{ all } y \in \mathbb{R}_+, \] and that Assumption 17.2 can be restated as a requirement that, for some \(\theta > 0\), \[ \theta < -y V''(y)/V'(y) \le 2 - \theta, \text{ all } y \in \mathbb{R}_+. \] Hence Assumption 17.4 involves dropping the uniformity requirement on the lower bound but strengthening the upper bound substantially.
In this particular example, the additional assumption on preferences needed to ensure monotonicity is stronger, almost, than the one needed to apply the Contraction Mapping Theorem.
### PROPOSITION 5
Let \((X, \mathscr{B})\) and \(T\) satisfy Assumption 17.3, with \(X = [a, b] \subset \mathbb{R}_+\).
Let \(H\) and \(V\) satisfy Assumptions 17.1 and 17.4, and define \(f\) and \(g\) as we did in Section 17.1.
Then the operator \(T\) on \(C(X)\) defined by \[ (Tf)(x) = \int_a^b e^{-r \phi [f(x')]} h(x, x') ds(x') \] has at least one fixed point.
Also, define \(\{e, \}, K,\) and \(B\) as we did in the proof of Proposition 4; and define the constant functions \(f_0(x) = e\) and \(g_0(x) = B\), all \(x \in X\).
Then the sequences \(\{T^n f_0\}\) and \(\{T^n g_0\}\) converge to fixed points of \(T\); and if \[ \lim T^n f_0 = f = g = \lim T^n g_0, \] then this function is the unique fixed point of \(T\).
**Proof.** Let \(F \subset C(X)\) be as specified in the proof of Proposition 4.
Clearly, \(F\) is closed and bounded, \(T: F \to F\) is continuous, and \(T(F)\) is equicontinuous.
Recall that \(\phi^{-1}\) is strictly increasing, and note that Assumption 17.4 implies that \(\phi\) is nondecreasing.
Hence the operator \(T\) is monotone, and the desired conclusions follow immediately from Theorem 17.7 and its corollary. 17.6 Partially Observed Shocks Other (more interesting) applications of monotonicity are discussed in Chapter 18. 17.6 Partially Observed Shocks To close this chapter, we show how the methods developed in the previous sections can be applied to a model in which the contemporaneous shock is only partially observed.
The example we consider is the “islands” model studied in Lucas (1972), which incorporates both real and monetary shocks.
First we show that the competitive equilibria of this system correspond to the fixed points of a certain operator on a space of bounded continuous functions.
We then show how the four fixed-point theorems described in the earlier sections—the Contraction Mapping Theorem, Brouwer’s Theorem, Schauder’s Theorem, and the monotonicity theorem—can be applied to this operator.
We begin with a description of the economy, which is a modification of the overlapping-generations example used in the earlier sections of the chapter.
As before, each individual lives for two periods.
When young, he works and sells the output he produces in exchange for money balances, which he carries over to the following period.
When old, he uses all of his money balances to buy goods, which he consumes.
As before, preferences over labor-consumption pairs have the form \(U(l, c) = -H(l) + V(c)\).
In contrast to the earlier example, there are no stochastic shocks to the production technology.
In each period labor can be used to produce output on a one-for-one basis: \(y = l\).
However, there are two sources of uncertainty in this economy that had no counterparts in the earlier model.
The first source of uncertainty is real and arises from the fact that the economy consists of two distinct “islands,” with no trade possible between them.
In each period the members of the young generation are assigned randomly to one of the two islands, with the proportion \(\theta/2\) going to one and \(1 - \theta/2\) to the other.
Members of the old generation are reassigned randomly to the two islands, with half going to each, in a way that equates the aggregate quantity of money in the two markets.
The second source of uncertainty is nominal and arises from the fact that in each period the government injects (or withdraws) money from the system by paying interest on (or taxing) money holdings of the old.
In particular, \(x m\) are the posttransfer money balances of an old individual who has accumulated balances \(m\) when young.
Thus, the nominal and real shocks to the system in any period are fully described by the exogenously determined pair \((x, \theta)\).
Let \(X \times \Theta\) denote the state space.
We assume that the pair \((x_t, \theta_t)\) is independently and identically distributed over time and that within each period the nominal and real components of the shock are independently drawn from distribution functions \(\mathcal{H}\) and \(G\) on \(X\) and \(\Theta\), respectively.
We use the following assumption on the shocks.
ASSUMPTION 17.5 \(x \in X = [x, \bar{x}]\), where \(0 < x < \bar{x} < \infty\); and \(\theta \in \Theta = (\underline{\theta}, \bar{\theta}]\), where \(0 < \underline{\theta} \le 2\).
The distribution functions \(\mathcal{H}\) and \(G\) have continuous densities, \(h\) and \(g\), respectively.
Assume that the contemporaneous shocks \((x, \theta)\) are not directly observed by any member of the young generation but are observed with a one-period lag.
Then the pretransfer money supply in period \(t-1\)—call it \(M_{t-1} = M_{t-1} \prod_{i=0}^\infty x_{t-i}\)—is known to all.
The money price of goods in period \(t\) will depend on the current state \((x_t, \theta_t)\) but will also depend—in a neutral way—on the pretransfer, perfectly observed money stock \(M_{t-1}\).
Thus, in any stationary equilibrium for this economy, the price level in any period \(t\) will be given by \(P_t = M_t p(x_t, \theta_t)\), where \(p(x, \theta)\) is a (real, not nominal) price function.‘As in the model analyzed earlier, we define a stationary equilibrium for this economy as a price function \(p: X \times \Theta \to \mathbb{R}\) and a labor supply function \(n: X \times \Theta \to [0,\infty)\).
For this economy, the equilibrium conditions are \[ (1) \quad n(x, \theta) \in \operatorname{arg\,max}_{l \in [0,L)} \; U(l) + V\left(\frac{x}{\theta} - p(x,\theta) l\right) \] \[ (2) \quad n(x, \theta) p(x, \theta) = \frac{x}{\theta}, \quad \text{all } (x, \theta) \in X \times \Theta. \] Condition (1) says that \(n(x, \theta)\) is the optimal labor supply for a young individual in state \((x, \theta)\), given the information available to him.
What information is this?
The agent cannot observe the current state \((x, \theta)\).
But he does observe the value of the price function \(p\) evaluated at the current state, and therefore he knows that the current state is in the subset of \(X \times \Theta\) where the price is equal to \(p(x, \theta)\).
Thus from his point of view the current state is a random variable, \((\tilde{x}, \theta)\), for which he knows the distribution but not the current realization.
Since the state is independently and identically distributed, next period’s state \((x', \theta')\) is also a random variable with a known distribution.
His optimal labor supply \(n(x, \theta)\) maximizes his conditional expected lifetime utility, given this information.
His choice entails producing \(n(x, \theta)\) units of output, which he sells at the known price \(p(x, \theta)M_t\), acquiring total revenues of \(n(x, \theta) p(x, \theta)M_t\).
Hence in the following period he has random posttransfer money balances of \(x' n(x, \theta) p(x, \theta)M_t\), which he uses to buy goods at the random price \(p(x', \theta')M_{t+1} = p(x', \theta')M_t\).
His random consumption of goods when old is thus \(x' n(x, \theta) p(x, \theta) / p(x', \theta')\).
Condition (2) is a market-clearing condition.
For the market with the fraction \(\theta\) of the young, it equates the real balances acquired by each young agent in payment for the labor he supplies to the average balances per young agent held by the old.
Notice that any two states \((x, \theta)\) and \((\hat{x}, \theta)\) that lead to the same price level are indistinguishable to the young agent.
Hence the set of utilitymaximizing values for labor supply in (1) is the same in both states.
Suppose that \(U\) and \(V\) satisfy Assumption 17.1, so that (1) is strictly concave in \(l\) and the maximizing value is unique.
Then \[ p(x, \theta) = p(\hat{x}, \theta) \text{ implies } n(x, \theta) = n(\hat{x}, \theta), \] and the market-clearing condition (2) then implies that \(x/\theta = \hat{x}/\theta\) for any such pair of states.
This equality implies that any equilibrium must be of the form \(p(x, \theta) = p(x/\theta)\) and \(n(x, \theta) = n(x/\theta)\).
If there is a solution of this form for which \(p\) is monotone, then the price reveals the ratio \(x/\theta\).
Thus, our strategy for establishing the existence of an equilibrium is as follows.
We will look for functions \((p, n)\) of the form above that satisfy (1) and (2) when the conditioning information in (1) is taken to be the ratio \(x/\theta\).
If such a pair can be found, and if \(p\) is monotone, then \((p, n)\) describes an equilibrium.
Define \(z = x/\theta\); under Assumption 17.5, \(Z = \mathcal{Z} = [\underline{z}, \bar{z}] = [\underline{x}/\bar{\theta}, \bar{x}/\underline{\theta}]\), where \(0 < \underline{z} < \bar{z}\).
The distribution function for \(z\) — call it \(\Pi\) — is then \[ \Pi(z) = \Pr\{z = \tilde{x}/\tilde{\theta} \leq z\} = \int_{\{\theta : x/\theta \leq z\}} g(x) \omega(\theta) \, dx \, d\theta = \int_{\theta} G(z\theta) \omega(\theta) \, d\theta, \] and \(\Pi\) has a continuous density: \[ \pi(z) = \Pi'(z) = \int_{\theta} g(z\theta) \theta \, \omega(\theta) \, d\theta. \] The following exercise shows that we can also derive the conditional distribution function \(G(\cdot | z)\) for \(\theta\) given \(z\), for any \(z \in Z\). **Exercise 17.8** a.
Derive the conditional distribution function \(G(\cdot | z) : \Theta \to [0, 1], z \in Z\).
Show that for each \(z \in \operatorname{int} Z\), \(G(\cdot | z)\) has a continuous density \(g(\cdot | z)\). b.
Show that if \(z_1 > z_2\), then \(G(\cdot | z_1)\) converges weakly to \(G(\cdot | z_2)\).
We can use the distribution functions \(\Pi\) and \(G(\cdot | z)\) to rewrite (1).
Substituting \(\eta\) for \(n\), \(\phi\) for \(p\), and \(z\) for \(x/\theta\), we can write (1) as \[ \eta(z) \in \operatorname{arg\,max}_{c} \left\{ U(\eta) + \int_{\Theta \times Z} V\left(\frac{z' \theta'}{\phi(z)} - c \theta'\right) g(d\theta' | z') \, \Pi(dz') \right\}. \] Under Assumption 17.1, the solution to this maximization problem is interior and hence must satisfy the first-order condition \[ (3) \quad \eta(z) H'[\eta(z)] = \int_{\Theta \times Z} V'\left(\frac{z' \theta'}{\phi(z)} - \eta(z) \theta'\right) \theta' \, g(d\theta' | z') \, \Pi(dz'), \] where (2) has been used to eliminate \(\phi\).
As we did in the earlier sections, define \(H(l) = U(l)\) and \(\psi(y) = y V'(y)\), and recall that under Assumption 17.1 \(\psi\) is invertible.
Then use (3) to define an operator \(T\) on \(C(Z)\) by \[ (4) \quad (Tf)(z) = \psi^{-1}\left[ \int_{\Theta \times Z} \frac{\psi(f(z')) \theta'}{z' \theta'} \, g(d\theta' | z') \, \Pi(dz') \right]. \] Clearly \(\eta\) satisfies (3) if and only if \(f(z) = \psi[\eta(z)]\) is a fixed point of \(T\).
A fixed point \(f\) corresponds to an equilibrium if the price function \(p\) associated with \(\phi = \psi^{-1}[f]\) is monotone.
Thus the problem of locating equilibria has been reduced to one of locating the fixed points of \(T\) in (4) and then verifying that the corresponding price function is invertible.
One approach to finding fixed points of \(T\) is to apply the Contraction Mapping Theorem as was done in Proposition 2.
Note that the restrictions on preferences needed here are exactly the ones used there. **PROPOSITION 6** Let \(U\) and \(V\) satisfy Assumptions 17.1 and 17.2; let \(X\), \(\Theta\), \(W\), and \(G\) satisfy Assumption 17.5; let \(Z = [\underline{x}/\bar{\theta}, \bar{x}/\underline{\theta}]\); and define \(\Pi\) and \(G (\cdot | z)\) as we did in Exercise 17.8.
Then the operator \(T\) defined in (4) has a unique fixed point in \(C(Z)\).
The proof of this result parallels the proof of Proposition 2, but it is not quite an application of Lemma 17.2 because the information structure of this economy is more complicated.
The main steps are 1.
Find a closed, convex set \(D \subset \mathbb{R}_{++}\) such that the operator \(T\) defined in (4) maps the space \(\mathcal{F}\) of bounded continuous functions \(f: Z \to D\) into itself.
Define \(\mathcal{F}\), \(D\), and \(\bar{\mathcal{F}}\) as we did in the proof of Proposition 2.
## 2. Apply the Mean Value Theorem as we did in the proof of Lemma
17.2, to show that \(T\) is a contraction with modulus \(\beta\).
We leave the details as an exercise. **Exercise 17.9** Complete the proof of Proposition 6.
An alternative to the approach taken in Proposition 6 is to apply Brouwer’s or Schauder’s Theorem.
This alternative approach allows us to dispense with Assumption 17.2, but it also means that we obtain no information about the uniqueness of an equilibrium of the desired form.
The application of Schauder’s Theorem is more difficult here than it was in Section 17.5, however, because—as the following exercise shows— Assumption 17.5 does not imply that the analogue to Assumption 17.3 holds. **Exercise 17.10** Let \(U\), \(V\), and \(G\) satisfy Assumption 17.5; and let \(Z\), \(\Pi\), and \(G(\cdot | z)\) be as specified in Exercise 17.8.
Show by example that if \(z_1 > z_2\), \(\{G(\cdot | z_1)\}\) may not converge to \(G(\cdot | z_2)\) in the total variation norm.
But Assumption 17.3 was simply a means to an end.
For the problem at hand, another line of argument is available for establishing equicontinuity.
To illustrate it, we consider the special case where \(x\) and \(\theta\) both have uniform distributions. **ASSUMPTION 17.6** \(G\) and \(\omega\) are uniform distributions. **PROPOSITION 7** Let \(U\) and \(V\) satisfy Assumption 17.1; and let \(X\), \(\Theta\), \(W\), and \(G\) satisfy Assumptions 17.5 and 17.6.
Then \(T\) has a fixed point in \(C(Z)\).
The proof of this result uses Schauder’s Theorem, so the steps in the argument parallel those in the proof of Proposition 4: 1.
Choose a nonempty, closed, bounded, convex set \(D \subset \mathbb{R}_{++}\), and let \(\mathcal{F} \subset C(Z)\) be the space of continuous functions \(f: Z \to D\). 2.
Show that \(T: \mathcal{F} \to \mathcal{F}\). 3.
Show that \(T\) is a continuous operator. 4.
Show that the family \(T(\mathcal{F})\) is equicontinuous. **Exercise 17.11** Carry out Steps 1-3.
Note that Assumption 17.6 does not simplify any of these three steps: they can as easily be carried out under Assumption 17.5 alone.
The proof that \(T(\mathcal{F})\) is equicontinuous (Step 4) is more difficult, and we write it out in some detail.
First we need to establish the following preliminary result. **Exercise 17.12** Let \(X\), \(\Theta\), \(W\), and \(G\) satisfy Assumptions 17.5 and 17.6.
Show that \(G(\cdot | z)\) is the uniform distribution on \([a(z), b(z)]\) where \[ (5) \quad a(z) = \max\{ \underline{x}/z, \underline{\theta} \} \quad \text{and} \quad b(z) = \min\{ \bar{x}/z, \bar{\theta} \}. \] Next, note that for any \(f \in \mathcal{F}\), we can define the function \(\phi_f : \Theta \to D\) by \[ \phi_f(\theta') = \psi^{-1} \left[ \frac{1}{b(z)-a(z)} \int_{a(z)}^{b(z)} f(z') \, dz' \right]. \] Then it follows immediately from (4) and Exercise 17.12 that \[ (6a) \quad (Tf)(z) = H\left[ \frac{1}{b(z)-a(z)} \int_{a(z)}^{b(z)} \frac{z' \phi_f(\theta')}{\theta'} \, dz' \right], \] \[ (6b) \quad \text{and } (Tf)(z') \text{ lies between } H\left[ \frac{a(z)}{\theta'} \right] \text{ and } H\left[ \frac{b(z)}{\theta'} \right]. \]competitive equilibrium allocations are not Pareto optimal and hence cannot be studied by analyzing an associated Pareto problem.
In this chapter we do not introduce any new fixed-point theorems; instead, we further illustrate how the theorems of Chapter 17 can be applied.
Recall that in the two specific economies studied in Chapter 17 the only state variables were exogenous shocks.
In the current chapter we show how similar arguments can be used in models with endogenous state variables.
In particular, we look at a growth model in which distorting taxes break the connection between Pareto-optimal and competitive equilibrium allocations.
(The economies considered in Chapter 17 were overlapping-generations models, and the ones to be considered below have identical, infinitely lived agents, but for our purposes this is not the critical distinction.
It is the presence of endogenous state variables that complicates the arguments in the present section.) Recall (cf.
Sections 5.1 and 16.1) that for the optimal growth model without taxes, dynamic programming techniques can be used to characterize competitive equilibria directly.
Since the competitive equilibrium allocation is Pareto optimal, the economy implicitly solves the problem of maximizing the representative consumer's utility.
Thus, an easy method for characterizing competitive equilibria in these situations is to solve this optimization problem explicitly.
In the presence of taxes, externalities, or other distortions, this type of attack fails.
Moreover, there is no single method of analysis that succeeds for all distorted economies.
Rather, there is an array of approaches, any one of which may or may not be useful in any specific application.
In the next three sections, we illustrate three alternative lines of argument that can be useful and discuss the strengths and weaknesses of each.
In Section 18.1 we describe in detail the growth model with distorting taxes that is used throughout the chapter, and we show that for certain kinds of taxes the competitive equilibrium of the distorted (taxed) economy solves the planning problem for a wholly fictional "pseudo-economy." In this case the methods of Chapter 4 can be used even though a tax wedge leads to a deviation between Pareto-optimal and competitive equilibrium allocations.
Unfortunately, the indirect pseudo-economy device of Section 18.1 has very limited applicability.
In Sections 18.2 and 18.3 we explore two other approaches for establishing the existence of a competitive equilibrium for a taxed economy, approaches that are useful when the pseudoeconomy method is not applicable.
Both of these approaches are based on a direct analysis of the first-order conditions for the representative consumer's dynamic optimization problem.
The first is a local analysis that makes use of the Contraction Mapping Theorem; the second is a global analysis that makes use of the Schauder Fixed-Point Theorem and the monotonicity result of Theorem 17.7. 18.1 An Indirect Approach Assume that there are many consumers, all with identical preferences described by the current-period utility function U and the discount factor β.
Let f denote the production function (gross of depreciated capital).
Then the functional equation for the optimally planned economy is (1) v(k) = max {U[f(k) - y + βv(y)}.
Let g be the optimal policy function corresponding to (1).
Then the total discounted utility of the representative consumer is maximized if all consumers adopt a policy of saving g(k) and consuming f(k) - g(k) per capita, whenever the capital stock per capita is equal to k.
That is, g describes a Pareto-optimal allocation in which all of the consumers are given equal weight.
As shown in Section 16.1, this allocation also describes the competitive equilibrium of an economy in which all consumers have equal initial holdings of capital.
That is, if all consumers have equal endowments of capital, then in the unique competitive equilibrium each saves g(k) and consumes f(k) - g(k) whenever the capital stock per capita is k.
To see this connection directly, note that each individual agent in this economy can be viewed as solving a dynamic programming problem.
Specifically, consider the problem faced by one agent, who anticipates that all other agents in the economy will use the savings rule described by the function g.
Suppose, too, that this particular agent begins with initial capital holdings of x, whereas all other agents in the economy begin with initial capital holdings of k.
This one agent must choose his current consumption c and end-of-period assets y such that their sum is less than the sum of his wage income, f(k) - kf'(k), and his earnings on capital, kx.
Hence the maximum present discounted value of his utility is described by the value function V(x, k; g) satisfying the functional equation (2) V(x, k; g) = max {U[f(k) - c + βV(y, f(k); g)}.
Call the policy function for this problem G(x, k; g), where the notation emphasizes that the individual's value and action depend both on the state (x, k) and on the way he expects others to behave, g.
As noted above, for this economy Pareto-optimal and competitive equilibrium allocations coincide.
Moreover, if all agents receive equal weight in the social welfare function or, in the competitive economy, if all begin with equal endowments of capital, then all agents have equal consumption and equal capital holdings in every subsequent period as well.
Therefore, given the unique value function v satisfying (1) and the associated policy function g, the unique value function V(., .; g) satisfying (2) and the associated policy function G(, ; g) satisfy V(k, k; g) = v(k) and G(k, k; g) = g(k), identically in k.
Exercise 18.1 Show that V(k, k; g) = v(k) and G(k, k; g) = g(k), all k.
In the rest of this section and in those that follow, we consider modifications to this model obtained by introducing flat-rate taxes and associ18.1 | An Indirect Approach 545 ated government spending programs.
To begin, consider the case where there is a flat-rate tax of θ ∈ (0, 1) on income from capital, the proceeds of which are returned to consumers in the form of a lump-sum subsidy. [The word income is being used here in a rather misleading way.
Since f(k) includes undepreciated capital, the tax is on both the oneperiod rental returns on capital and the undepreciated capital remaining at the end of the period.
Realistically, the latter is much larger, so it is probably more accurate to think of the tax we use here as a wealth tax.] Then the consumer's after-tax income, including his lump-sum subsidy is f(k) + (1 - θ)(x - k) f(k), and his functional equation is (3) W(x, k; g) = max {U[f(k) - c + (1 - θ)(x - k) f(k) - y + βW(y, f(k); g)}.
It is clear that the function V(., .; θ) does not satisfy (3) and hence that the consumer's policy function for the latter is not G(, ; θ), even if we restrict attention to the locus where x = k.
That is, the savings function g from the optimal growth model does not describe competitive equilibrium savings in the taxed economy.
Instead, an equilibrium for the taxed economy is an aggregate savings function A for the economy as a whole and an optimal policy function h(, k; h) for the individual such that h(k, k; h) = h(k), identically in k.
That is, in equilibrium it must be optimal for the representative agent to behave the way everyone else does.
To construct an equilibrium, we conjecture that the savings function of the representative consumer is a continuous function—call it h.
The optimization problem facing the typical agent in this economy is then given by (3), but with h in place of g.
The first-order and envelope conditions for this problem are then (4) U'[f(k) + (1 - θ)(x - k) f(k) - h(k)] = βW_k[h(k), f(k); h], (5) W_x(x, k; h)without further loss of generality—limit attention to functions that have a stationary point at k*.
In fact, we will confine attention to an even smaller set of functions.
Since Schauder’s Theorem says nothing about uniqueness, there is no particular virtue in working with a large space.
On the contrary, using a smaller space sharpens the characterization of the equilibrium.
Let C(K) be the set of continuous functions h: K → R.
Then define the following subset of C(K): F = {h ∈ C(K): h satisfies (2)—(6)}, where (2) ψ = h(k) ≤ w(k), all k ∈ K; (3) h and w — h are nondecreasing; (4) h(k) = k, all k < k*; (5) h(k*) = k*; (6) h(k) ≥ k, all k ≥ k*.
The restrictions on h implied by (2)-(6) are depicted in Figure 18.1.
Since ψ = f(k) − θkf'(k), it follows that ψ'(k) = (1 — θ) f'(k) — θkf''(k) ≤ (1 — θ) f'(k), all k ∈ K; so ψ is strictly increasing.
Moreover, since β(1 — θ) f'(k*) = 1 and f is strictly concave, it follows that ψ'(k) > 1/θ > 1, for k ≤ k*.
Finally, since ψ(0) = f(0) > 0 and since the derivative of ψ exceeds unity on [0, k*], it follows that ψ(k*) > k*.
Hence the functions ψ(k) and ψ(k) — [ψ(k*) − k*] are as shown in Figure 18.1.
The bounds in (2) and (4)—(6) imply that any function h ∈ F must lie in areas A and B−C.
In addition, since ψ−h must be nondecreasing, the slope of h is bounded above by the slope of ψ.
This fact in turn implies that h cannot lie in region C.
Thus functions in F must lie in regions A and B, with slopes bounded below by zero and above by the slope of ψ. ψ(k) ψ(k) − [ψ(k*) − k*] 0 k* k Figure 18.1 Our first objective is to use Schauder’s Theorem to show that there is a function g in F satisfying (1).
Note that the set K is bounded and that the family of functions F is nonempty, closed, bounded, and convex.
We can use the equilibrium condition (1) to define the following operator T on F: (7) β(1 — θ) f'(g(k)) U'(w(g(k)) = β(1 — θ) f'((Tg)(k)) U'(w((Tg)(k)) — θ(Tg)(k) f'((Tg)(k)).
Exercise 18.5 Prove that T is well defined and that T: F → F. [Hint.
Use Figure 18.2.] To apply Schauder’s Theorem, we only need to verify that T is continuous and that T(F) is an equicontinuous family.
To do this, we first prove that F is itself an equicontinuous family.
This result implies that β(1−θ)f'(k)U'(w(k) − θk f'(k)) βU'(w(k)) − βθf'(k)U'(w(k)) 0 k' Figure 18.2 T(F) is equicontinuous and is also useful in showing that T is a continuous operator.
### PROPOSITION 5
F is an equicontinuous family.
**Proof.** For all h ∈ F and all k, k' ∈ K with k' > k, (3) implies that 0 ≤ h(k') − h(k) ≤ ψ(k') − ψ(k).
The function ψ is continuously differentiable on the compact interval K; so by the Mean Value Theorem, |ψ(k') − ψ(k)| ≤ Ak' − k|, where A < ∞ is as specified in Assumption 18.2.
Combining these two facts gives the desired result.
With Proposition 5 established, the continuity of the operator T is also straightforward.
Exercise 18.6 Prove that T is continuous. [Hint.
First prove that if {g_n} and g are in F and g_n → g in the sup norm, then Tg_n → Tg pointwise.
Then use the fact that K is compact and F is equicontinuous to establish the desired result.] Proposition 5 and Exercise 18.6 complete the verification of the hypotheses of Schauder’s Theorem.
We have thus established that T has a fixed point in F.
In fact, much more can be said about the operator T.
Exercise 18.7 Prove that T is monotone; that is, if h, h' ∈ F and h ≤ h', then Th ≤ Th'.
(Hint.
Modify Figure 18.2.) The monotonicity of T is especially useful in this context, because F has both a smallest and a largest element.
Specifically, Figure 18.1 shows that the functions h_L(k) = { k, if k ≤ k*; ψ(k), if k > k*}, and h_M(k) = min {k, ψ(k) − [ψ(k*) − k*]} are minimal and maximal elements, respectively, of F.
Thus, Exercise 18.7 and Theorem 17.7 together imply that lim T^n h_L and lim T^n h_M are both fixed points of T.
Moreover, the corollary to Theorem 17.7 implies that if the two limits coincide, then that common limit g is the unique fixed point of T.
Finally, we discuss briefly how the analysis above can be modified to include exogenous shocks.
Specifically, assume that exogenous shocks affect the production technology.
Let Ξ = {ξ_1, ..., ξ_J} be a finite set, and let Π = [π_ij] be a J × J transition matrix.
The production technology is then described by a function f: R+ × Ξ → R+.
Parts (d) and (e) of Assumption 18.1 and the technology restriction in Assumption 18.2 can be modified in the obvious way to hold for each ξ_j.
Then define k̄ = max {k̄_1,..., k̄_J}, where k̄_j is the maximum capital stock maintainable out of after-tax income when the shock takes on the value ξ_j, as defined in the modification of part (e) of Assumption 18.1.
Let K = [0, k̄].
We retain the other features of the model above.
In particular we maintain the assumption that the only tax is a flat-rate tax of θ on income from capital and assume that the proceeds of this tax are thrown away.
Let w(k, ξ) = f(k, ξ) − θk f_k (k, ξ) be the function describing after-tax income.
By an argument exactly analogous to the one used in Section 18.1, we find that an equilibrium for this economy is described by a function g: K × Ξ → K satisfying (8) βU'(w(k, ξ) − g(k, ξ)) = β(1 − θ) Σ_{ξ'} π_{ξξ'} f_k(g(k, ξ), ξ') U'(w(g(k, ξ), ξ') − g(g(k, ξ), ξ')).
Equation (8) is the analogue of (1), modified to include the stochastic shocks.
Now consider the problem of establishing the existence of a function g satisfying (8).
Let C(K × Ξ) be the space of bounded continuous functions on K × Ξ, and consider the conditions in (2)—(6) used to define F in the deterministic case.
It is reasonable to suppose that the analogues to (2) and (3) are conditions that hold for each ξ_j ∈ Ξ.
However, there does not seem to be any reason to suppose that anything like (4)—(6) hold in the stochastic case, at least in the absence of further restrictions on the transition matrix Π and the technology f.
Thus, for the stochastic case, we take F ⊂ C(K × Ξ) to be the set of functions h: K × Ξ → K satisfying the analogues of (2) and (3).
Note that K × Ξ is a bounded subset of R^2 and that F is nonempty, closed, bounded, and convex.
Next, define the analogue to the operator T defined in (7): (9) βU'(w(k, ξ) − (Th)(k, ξ)) = β(1 − θ) Σ_{ξ'} π_{ξξ'} f'((Th)(k, ξ), ξ') × U'[(w((Th)(k, ξ), ξ') − θ(Th)(k, ξ) f'((Th)(k, ξ), ξ'))].
The following exercise then parallels Exercise 18.5.
Exercise 18.8 Show that the operator T in (9) is well defined and that T: F → F.
The proof that F is an equicontinuous family then parallels exactly the proof of Proposition 6, and the proof that T is continuous parallels the proof of Exercise 18.6.
That T has a fixed point in F then follows from Schauder’s Theorem.
Moreover, the proof that T is monotone parallels exactly the proof of Exercise 18.7, and minimal and maximal elements of F can be constructed as there.
Exercise 18.9 How must the assumptions or arguments, or both, above be modified if Ξ is a closed, bounded interval? 18.4 Bibliographic Notes For a more detailed description of the pseudo-economy approach described in Section 18.1, see R.
Becker (1985).
Lucas and Stokey (1987) use arguments similar to those in Section 18.3 to study monetary policy in a model without capital in which money holding is motivated by a cash-in-advance constraint that applies to one class of consumption goods.
Coleman (1987) uses a similar approach to study capital accumulation in a monetary model with a cash-in-advance constraint.
Bizer and Judd (1989) use arguments of this type to study capital accumulation in a model with a tax on income from capital and an investment tax credit, in which it is the tax rates themselves that are random.
Blume (1982) and Duffie et al.
(1988) contain results on the existenceof stationary equilibria for models of the type discussed in this chapter.
References Index of Theorems General Index References Abreu, Dilip, David Pearce, and Ennio Stacchetti. 1986.
Optimal cartel equilibria with imperfect monitoring.
Journal of Economic Theory 39:251-269.
Aghion, Philippe, Patrick Bolton, and Bruno Jullien. 1988.
Learning through price experimentation by a monopolist facing unknown demand.
Unpublished manuscript.
Massachusetts Institute of Technology, Cambridge, Mass.
Albrecht, James W., and Bo Axell. 1984.
An equilibrium model of search unemployment.
Journal of Political Economy 92:824—840.
Araujo, Aloisio, and José A.
Scheinkman. 1977.
Smoothness, comparative dynamics, and the turnpike property.
Econometrica 45:601-620.
Arrow, Kenneth J. 1951.
An extension of the basic theorems of classical welfare economics.
In Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability, ed.
J.
Neyman.
Berkeley: University of California Press, pp. 507-532.
Reprinted in Arrow (1983) 2:13-45. 1953.
Le rôle des valeurs boursières pour la répartition la meilleure des risques.
Econometrie.
Paris: Centre National de la Recherche Scientifique, pp. 41-48.
Translated as “The role of securities in the optimal allocation of risk bearing.” Review of Economic Studies 31(1963—64):91— 96.
Reprinted in Arrow (1983) 2:46-57. 1983.
Collected Papers of Kenneth J.
Arrow.
Vol. 2, General Equilibrium.
Cambridge, Mass.: Harvard University Press.
Arrow, Kenneth J., Samuel Karlin, and Herbert Scarf. 1958.
Studies in the Mathematical Theory of Inventory and Production.
Stanford, Calif.: Stanford University Press.
Arrow, Kenneth J., and Mordecai Kurz. 1970.
Public Investment, the Rate of Return, and Optimal Fiscal Policy.
Baltimore: Johns Hopkins University Press. 563 564 References Back, Kerry. 1988.
Structure of consumption sets and existence of equilibria in infinite-dimensional spaces.
Journal of Mathematical Economics 17:89-99.
Bartle, Robert G. 1966.
The Elements of Integration.
New York: Wiley.
Beals, Richard, and Tjalling C.
Koopmans. 1969.
Maximizing stationary utility in a constant technology.
SIAM Journal of Applied Mathematics 17:1009-15.
Becker, Gary S. 1962.
Investment in human capital: a theoretical analysis.
Journal of Political Economy 70:9-49.
Becker, Robert A. 1985.
Capital income taxation and perfect foresight.
Journal of Public Economics 26:147-167.
Behnke, Heinrich, et al.
(eds.). 1974.
Fundamentals of Mathematics, vol. 3.
Cambridge, Mass.: MIT Press.
Bellman, Richard. 1957.
Dynamic Programming.
Princeton, N.J.: Princeton University Press.
Ben-Porath, Yoram. 1967.
The production of human capital and the life cycle of earnings.
Journal of Political Economy 75:352-365.
Benveniste, Lawrence M., and José A.
Scheinkman. 1979.
On the differentiability of the value function in dynamic models of economics.
Econometrica 47:727-732.
Berge, Claude. 1963.
Topological Spaces.
New York: Macmillan.
Bertsekas, Dmitri P. 1976.
Dynamic Programming and Stochastic Control.
New York: Academic Press.
Bertsekas, Dmitri P., and Steven E.
Shreve. 1978.
Stochastic Optimal Control.
New York: Academic Press.
Bewley, Truman F. 1972.
Existence of equilibria in economies with infinitely many commodities.
Journal of Economic Theory 4:514—540.
Billingsley, Patrick. 1968.
Convergence of Probability Measures.
New York: Wiley. 1979.
Probability and Measure.
New York: Wiley.
Bizer, David, and Kenneth L.
Judd. 1989.
Taxation and uncertainty.
American Economic Review 79:331—336.
Blackwell, David. 1965.
Discounted dynamic programming.
Annals of Mathematical Statistics 36:226—235.
Blume, Lawrence. 1982.
New techniques for the study of stochastic equilibrium processes.
Journal of Mathematical Economics 9:61—70.
Blume, Lawrence, David Easley, and Maureen O’Hara. 1982.
Characterization of optimal plans for stochastic dynamic programs.
Journal of Economic Theory 28:221~234.
Boldrin, Michele, and Luigi Montrucchio. 1984.
The emergence of dynamic complexities in models of optimization over time: the role of impatience.
Unpublished manuscript.
University of Rochester, Rochester, N.Y. 1986.
On the indeterminacy of capital accumulation paths.
Journal of Economic Theory 40:26-39.
Border, Kim C. 1985.
Fixed-Point Theorems with Applications to Economics and Game Theory.
Cambridge: Cambridge University Press.
Boyer, Marcel. 1975.
An optimal growth model with stationary nonadditive utilities.
Canadian Journal of Economics 8:216—237.
Breeden, Douglas T. 1979.
An intertemporal asset pricing model with stochastic consumption and investment opportunities.
Journal of Financial Economics 7:265—296.
Breiman, Leo. 1960.
The strong law of large numbers for a class of Markov chains.
Annals of Mathematical Statistics 31:801-803. 1968.
Probability.
Reading, Mass.: Addison-Wesley.
Brock, William A. 1973.
Some results on the uniqueness of steady states in multisector models of economic growth when future utilities are discounted.
International Economic Review 14:535-559. 1982.
Asset prices in a production economy.
In The Economics of Information and Uncertainty, ed.
John J.
McCall.
Chicago: University of Chicago Press, pp. 1-43.
Brock, William A., and Edwin Burmeister. 1976.
Regular economies and conditions for uniqueness of steady states in optimal multi-sector economic models.
International Economic Review 17:105-120.
Brock, William A., and Leonard J.
Mirman. 1972.
Optimal economic growth and uncertainty: the discounted case.
Journal of Economic Theory 4:479-513. 1973.
Optimal economic growth and uncertainty: the no discounting case.
International Economic Review 14:497-—513.
Brock, William A., Michael Rothschild, and Joseph E.
Stiglitz. 1989.
Stochastic capital theory.
In Joan Robinson and Modern Economic Theory, ed.
George R.
Feiwel.
New York: New York University Press, pp. 591622.
Brock, William A., and José A.
Scheinkman. 1976.
Global asymptotic stability of optimal control systems with applications to the theory of economic growth.
Journal of Economic Theory 12:164-190.
Brown, Donald J., and Lucinda M.
Lewis. 1981.
Myopic economic agents.
Econometrica 49:359-368.
Burger, Ewald. 1963.
Introduction to the Theory of Games.
Trans.
John E.
Freund.
Englewood Cliffs, N.J.: Prentice-Hall.
Burmeister, Edwin. 1980.
Capital Theory and Dynamics.
Cambridge: Cambridge University Press. 566 References Burmeister, Edwin, and A.
Rodney Dobell. 1970.
Mathematical Theories of Economic Growth.
New York: Macmillan.
Caplin, Andrew S. 1985.
The variability of aggregate demand with (S, s) inventory policies.
Econometrica 53:1395—1409.
Cass, David. 1965.
Optimum growth in an aggregative model of capital accumulation.
Review of Economic Studies 32:233-240.
Cass, David, and Karl Shell. 1976.
The structure and stability of competitive dynamical systems.
Journal of Economic Theory 12:31—70. 1983.
Do sunspots matter?
Journal of Political Economy 91:193-227.
Chung, Kai Lai. 1967.
Markov Chains, Second Edition.
New York: SpringerVerlag. 1974.
A Course in Probability Theory, Second Edition.
New York: Academic Press.
Clarke, Frank H., Masako N.
Darrough, and John M.
Heineke. 1982.
Optimal pricing policy in the presence of experience effects.
Journal of Business 53:51-67.
Coddington, Earl A., and Norman Levinson. 1955.
Theory of Ordinary Differential Equations.
New York: McGraw-Hill.
Coleman, Wilbur John II. 1987.
Money, interest, and capital.
Doctoral dissertation, University of Chicago, Chicago, Ill.
Cox, John C., Jonathon E.
Ingersoll, and Stephen A.
Ross. 1985.
An intertemporal general equilibrium model of asset prices.
Econometrica 53:363-384.
Dana, Rose-Anne, and Cuong Le Van. 1988.
On the structure of Paretooptima in an infinite horizon economy where agents have recur-sive preferences.
Unpublished manuscript.
University of Paris VI, Paris.
Danthine, Jean-Pierre. 1977.
Martingale, market efficiency and commodity prices.
European Economic Review 10:1–17.
Danthine, Jean-Pierre, and John B.
Donaldson. 1981.
Stochastic properties of fast vs. slow growing economies.
Econometrica 49:1007–33.
Debreu, Gerard. 1954.
Valuation equilibrium and Pareto optimum.
Proceedings of the National Academy of Sciences 40:588–592.
Reprinted in Debreu (1983), pp. 98–104. 1959.
The Theory of Value.
New Haven, Conn.: Yale University Press. 1983.
Mathematical Economics: Twenty Papers of Gerard Debreu.
Cambridge: Cambridge University Press.
Denardo, Eric V. 1967.
Contraction mappings in the theory underlying dynamic programming.
SIAM Review 9:165–177.
Donaldson, John B., and Rajnish Mehra. 1983.
Stochastic growth with correlated production shocks.
Journal of Economic Theory 29:282–312.
References 567 Doob, J.
L. 1953.
Stochastic Processes.
New York: Wiley.
Duffie, Darrell, John Geanakoplos, Andreu Mas-Colell, and Andrew McLennan. 1988.
Stationary Markov equilibria.
Unpublished manuscript.
Stanford University, Stanford, Calif.
Dynkin, E.
B. 1965.
Markov Processes, vol. 1.
Berlin: Springer-Verlag.
Dynkin, E.
B., and A.
A.
Yushkevich. 1979.
Controlled Markov Processes.
New York: Springer-Verlag.
Easley, David, and Daniel F.
Spulber. 1981.
Stochastic equilibrium and optimality with rolling plans.
International Economic Review 22:79–103.
Eisner, Robert, and Robert Strotz. 1963.
Determinants of business investment.
Commission on Money and Credit.
Impacts of Monetary Policy.
Englewood Cliffs, N.J.: Prentice-Hall.
Ekeland, Ivar, and José A.
Scheinkman. 1986.
Transversality conditions for some infinite horizon discrete time optimization problems.
Mathematics of Operations Research 11:216–229.
Epstein, Larry G. 1987.
A simple dynamic general equilibrium model.
Journal of Economic Theory 41:68–95.
Fama, Eugene F. 1965.
The behavior of stock market prices.
Journal of Business 38:34–105.
Feller, William. 1971.
An Introduction to Probability Theory and Its Applications, vol. 2, Second Edition.
New York: Wiley.
Foley, Duncan, and Martin Hellwig. 1975.
Asset management with trading uncertainty.
Review of Economic Studies 42:327–396.
Futia, Carl A. 1982.
Invariant distributions and the limiting behavior of Markovian economic models.
Econometrica 50:377–408.
Gihman, I.
I., and A.
V.
Skorohod. 1974.
The Theory of Stochastic Processes I.
Trans.
Samuel Kotz.
New York: Springer-Verlag. 1979.
Controlled Stochastic Processes.
Trans.
Samuel Kotz.
New York: Springer-Verlag.
Gilles, Christian, John M.
Marshall, and Jon Sonstelie. 1987.
An infinity of Arrow exceptional cases.
Unpublished manuscript.
University of California, Santa Barbara, Calif.
Gould, John P. 1968.
Adjustment costs in the theory of investment of the firm.
Review of Economic Studies 35:47–55.
Green, Edward J. 1976.
An introduction to Markov processes.
Unpublished manuscript.
Carnegie-Mellon University, Pittsburgh, Penn.
Hall, Robert E. 1978.
Stochastic implications of the life cycle-permanent income hypothesis: theory and evidence.
Journal of Political Economy 86:971–988.
Halmos, Paul R. 1974.
Measure Theory.
New York: Springer-Verlag. 568 References Hansen, Lars P. 1985.
Results on existence, convergence, and stability for the quadratic control problem.
Unpublished manuscript.
University of Chicago, Chicago, Ill.
Hansen, Lars P., and Kenneth J.
Singleton. 1983.
Stochastic consumption, risk aversion, and the temporal behavior of asset returns.
Journal of Political Economy 91:249–265.
Harris, Milton. 1987.
Dynamic Economic Analysis.
New York: Oxford University Press.
Hildenbrand, Werner. 1974.
Core and Equilibria of a Large Economy.
Princeton, N.J.: Princeton University Press.
Hirshleifer, Jack. 1966.
Investment decision under uncertainty: applications of the state-preference approach.
Quarterly Journal of Economics 80:252–277.
Hopenhayn, Hugo A., and Edward C.
Prescott. 1987.
Invariant distributions for monotone Markov processes.
Federal Reserve Bank of Minneapolis Working Paper No. 299, Minneapolis, Minn.
Hotelling, Harold. 1931.
The economics of exhaustible resources.
Journal of Political Economy 39:137–175.
Hutson, V., and J.
S.
Pym. 1980.
Applications of Functional Analysis and Operator Theory.
London: Academic Press.
Iglehart, Donald S. 1963.
Optimality of (s, S) policies in the infinite horizon dynamic inventory problem.
Management Science 9:257–267.
Istratescu, Vasile I. 1981.
Fixed Point Theory: An Introduction.
Dordrecht-Boston: D.
Reidel Publishing Corp.
Iwai, Katsuhito. 1972.
Optimal economic growth and stationary ordinal utility.
Journal of Economic Theory 5:121–151.
Jones, Larry E. 1984.
A competitive model of commodity differentiation.
Econometrica 52:507–530. 1986.
Special problems arising in the study of economies with infinitely many commodities.
In Models of Economic Dynamics, ed.
Hugo F.
Sonnenschein.
Berlin: Springer-Verlag, pp. 184–205.
Jones, Larry E., and Rodolfo E.
Manuelli. 1987.
A model of optimal equilibrium growth.
Unpublished manuscript.
Northwestern University, Evanston, Ill.
Jorgenson, Dale W. 1963.
Capital theory and investment behavior.
American Economic Review 53:247–259.
Jovanovic, Boyan. 1979.
Job matching and the theory of turnover.
Journal of Political Economy 87:972–990.
Kamien, Morton I., and Nancy L.
Schwartz. 1981.
Dynamic Optimization.
New York: North Holland.
Karlin, Samuel. 1955.
The structure of dynamic programming models.
Naval Research Logistics Quarterly 2:285–294.
References 569 Kehoe, Timothy J., and David K.
Levine. 1985.
Comparative statics and perfect foresight.
Econometrica 53:433–454.
Kemeny, John G., and J.
Laurie Snell. 1960.
Finite Markov Chains.
Princeton, N.J.: D.
Van Nostrand.
Kemeny, John G., J.
Laurie Snell, and Anthony W.
Knapp. 1976.
Denumerable Markov Chains, Second Edition.
New York: Springer-Verlag.
Kolmogorov, A.
N., and S.
V.
Fomin. 1970.
Introductory Real Analysis.
Trans.
Richard A.
Silverman.
Englewood Cliffs, N.J.: Prentice-Hall.
Koopmans, Tjalling C. 1960.
Stationary ordinal utility and impatience.
Econometrica 28:287–309. 1965.
On the concept of optimal growth.
The Econometric Approach to Development Planning.
Chicago: Rand McNally.
Koopmans, Tjalling C., Peter A.
Diamond, and Richard E.
Williamson. 1964.
Stationary utility and time perspective.
Econometrica 32:82–100.
Kurz, Mordecai. 1968.
The general instability of a class of competitive growth processes.
Review of Economic Studies 35:155–174.
Kydland, Finn, and Edward C.
Prescott. 1982.
Time to build and aggregate fluctuations.
Econometrica 50:1345–70.
Labadie, Pamela. 1984.
A test of risk premia behavior in an overlapping generations model.
Unpublished manuscript.
Columbia University, New York.
Lang, Serge. 1983.
Real Analysis, Second Edition.
Reading, Mass.: Addison-Wesley.
LeRoy, Stephen F. 1973.
Risk aversion and the martingale property of stock prices.
International Economic Review 14:436–446.
Levhari, David, and Nissan Liviatan. 1972.
On stability in the saddle-point sense.
Journal of Economic Theory 4:88–93.
Lippman, Steven A., and John J.
McCall. 1976a.
The economics of job search: a survey: part I.
Economic Inquiry 14:155–189. 1976b.
The economics of job search: a survey.
Economic Inquiry 14:347–368.
Loéve, Michel. 1977.
Probability Theory I and II, Fourth Edition.
New York: Springer-Verlag.
Long, John B., Jr., and Charles I.
Plosser. 1983.
Real business cycles.
Journal of Political Economy 91:39–69.
Lucas, Robert E., Jr. 1967a.
Optimal investment policy and the flexible accelerator.
International Economic Review 8:78–85. 1967b.
Adjustment costs and the theory of supply.
Journal of Political Economy 75:321–334. 1972.
Expectations and the neutrality of money.
Journal of Economic Theory 4:103–124. 570 References——— 1978.
Asset prices in an exchange economy.
Econometrica 46:1429-45. ——— 1980.
Equilibrium in a pure currency economy.
Economic Inquiry 18:203-220. —— 1988.
On the mechanics of economic development.
Journal of Monetary Economics 22:3-42.
Lucas, Robert E., Jr., and Edward C.
Prescott. 1971.
Investment under uncertainty.
Econometrica 39:659-681. 1974.
Equilibrium search and unemployment.
Journal of Economic Theory 7:188-209.
Lucas, Robert E., Jr., and Nancy L.
Stokey. 1984.
Optimal growth with many consumers.
Journal of Economic Theory 32:139-171. 1987.
Money and interest in a cash-in-advance economy.
Econometrica 55:491-513.
Luenberger, David G. 1969.
Optimization by Vector Space Methods.
New York: Wiley.
Majumdar, Mukul, and Roy Radner. 1983.
Stationary optimal policies with discounting in a stochastic activity analysis model.
Econometrica 51:1821-37.
Manuelli, Rodolfo E. 1985.
A note on the behavior of the solutions to dynamic stochastic models.
Unpublished manuscript.
Stanford University, Stanford, Calif.
Manuelli, Rodolfo E., and Thomas J.
Sargent. 1987.
Exercises in Dynamic Macroeconomic Theory.
Cambridge, Mass.: Harvard University Press.
Mas-Colell, Andreu. 1975.
A model of equilibrium with differentiated commodities.
Journal of Mathematical Economics 2:263-295. 1986a.
The price equilibrium existence problem in topological vector lattices.
Econometrica 54:1039-53. 1986b.
Valuation equilibrium and Pareto optimum revisited.
In Contributions to Mathematical Economics, ed.
Werner Hildenbrand and Andreu Mas-Colell.
Amsterdam: North-Holland, pp. 317-331.
McCall, John J. 1970.
Economics of information and job search.
Quarterly Journal of Economics 84:113-126.
McCallum, Bennett T. 1989.
Real business cycle models.
In Modern Business Cycle Theory, ed.
Robert J.
Barro.
Cambridge, Mass.: Harvard University Press, pp. 16-50.
McKenzie, Lionel W. 1987.
Turnpike theory.
In The New Palgrave: A Dictionary of Economics, Vol. 4. ed.
John Eatwell, Murray Milgate, and Peter Newman.
New York: Stockton Press, pp. 712-720.
Mehra, Rajnish, and Edward C.
Prescott. 1985.
The equity premium: a puzzle.
Journal of Monetary Economics 15:145-162.
References 571 Milnor, John W. 1965.
Topology from the Differentiable Viewpoint.
Charlottesville: University Press of Virginia.
Mirman, Leonard J., and Itzhak Zilcha. 1975.
On optimal growth under uncertainty.
Journal of Economic Theory 11:329-339.
Modigliani, Franco, and Merton H.
Miller. 1958.
The cost of capital, corporation finance and the theory of investment.
American Economic Review 48:261-297.
Mortensen, Dale T. 1970.
A theory of wage and employment dynamics.
In Edmund S.
Phelps et al.
Microeconomic Foundations of Employment and Inflation Theory.
New York: Norton, pp. 167-211. 1973.
Generalized costs of adjustment and dynamic factor demand theory.
Econometrica 41:657-665.
Muller, Walter J., and Michael Woodford. 1988.
Determinacy of equilibrium in stationary economies.
Journal of Economic Theory 46:255-290.
Muth, John F. 1961.
Rational expectations and the theory of price movements.
Econometrica 29:315-335.
Neveu, Jacques. 1965.
Mathematical Foundations of the Calculus of Probability.
Trans.
Amiel Feinstein.
San Francisco: Holden-Day.
Onicescu, Octav. 1969.
Calcolo delle Probabilità ed Applicazioni.
Rome: Veschi Editori.
Peleg, Bezalel, and Harl E.
Ryder. 1972.
On optimal consumption plans in a multi-sector economy.
Review of Economic Studies 39:159-170.
Pontryagin, L.
S. 1962.
Ordinary Differential Equations.
Trans.
Leonas Kacinskas and Walter B.
Counts.
Reading, Mass.: AddisonWesley.
Pontryagin, L.
S., et al. 1962.
The Mathematical Theory of Optimal Processes.
Trans.
K.
N.
Trirogoff; ed.
L.
W.
Neustadt.
New York: WileyInterscience.
Prescott, Edward C. 1975.
Notes on dynamic programming with unbounded loss.
Unpublished manuscript.
Carnegie-Mellon University, Pittsburgh, Penn.
Prescott, Edward C., and Robert E.
Lucas, Jr. 1972.
Price systems in infinite dimensional space.
International Economic Review 13:416-422.
Prescott, Edward C., and Rajnish Mehra. 1980.
Recursive competitive equilibrium: the case of homogeneous households.
Econometrica 48:1365-79.
Prescott, Edward C., and José V.
Rios-Rull. 1988.
Classical competitive analysis in a growth economy with search.
Federal Reserve Bank of Minneapolis Working Paper 329, Minneapolis, Minn.
Radner, Roy. 1961.
Paths of economic growth that are optimal with regard only to final states.
Review of Economic Studies 28:98-104. 572 References 1972.
Existence of equilibrium of plans, prices, and price expectations in a sequence of markets.
Econometrica 40:289-303.
Ramsey, Frank P. 1928.
A mathematical theory of saving.
Economic Journal 38:543-559.
Razin, Assaf, and Joseph A.
Yahav. 1979.
On stochastic models of economic growth.
International Economic Review 20:599-604.
Rebelo, Sergio. 1987.
Long run policy analysis and long run growth.
Unpublished manuscript.
University of Rochester, Rochester, N.Y.
Rockafellar, R.
Tyrrell. 1970.
Convex Analysis.
Princeton, N.J.: Princeton University Press. 1976.
Saddle points of Hamiltonian systems in convex Lagrange problems having a nonzero discount rate.
Journal of Economic Theory 12:71-113.
Rosen, Sherwin. 1976.
A theory of life earnings.
Journal of Political Economy 84:545-567.
Rosenblatt, Murray. 1971.
Markov Processes: Structure and Asymptotic Behavior.
New York: Springer-Verlag.
Royden, H.
L. 1968.
Real Analysis.
New York: Macmillan.
Samuelson, Paul A. 1965.
Proof that properly anticipated prices fluctuate randomly.
Industrial Management Review 6:41-49.
Sargent, Thomas J. 1979.
Macroeconomic Theory.
New York: Academic Press. 1980. “Tobin’s q” and the rate of investment in general equilibrium.
Carnegie-Rochester Conference Series on Public Policy 12:107-154. 1987.
Dynamic Macroeconomic Theory.
Cambridge, Mass.: Harvard University Press.
Scarf, Herbert E. 1959.
The optimality of (S, s) policies in the dynamic inventory problem.
In Mathematical methods in the Social Sciences, ed.
K.
Arrow, S.
Karlin, and P.
Suppes.
Stanford, Calif.: Stanford University Press.
Scheinkman, José A. 1973.
On optimal steady states of n-sector growth models when utility is discounted.
Doctoral dissertation, University of Rochester, Rochester, N.Y. 1976.
On optimal steady states of n-sector growth models when utility is discounted.
Journal of Economic Theory 12:11-30.
Scheinkman, José A., and Jack Schechtman. 1983.
A simple competitive model with production and storage.
Review of Economic Studies 50:427-441.
Shiryayev, A.
N. 1984.
Probability.
Trans.
R.
P.
Boas.
New York: SpringerVerlag.
Solow, Robert M. 1956.
A contribution to the theory of economic growth.
Quarterly Journal of Economics 70:65-94.
References 573 Song, Byung Ho. 1986.
Dynamic programming with constant-returnsto-scale return functions.
Unpublished manuscript.
University of Chicago, Chicago, Ill.
Stigler, George J. 1961.
The economics of information.
Journal of Political Economy 69:213-225.
Stokey, Nancy L. 1986.
The dynamics of industrywide learning.
In Equilibrium Analysis: Essays in Honor of Kenneth J.
Arrow, vol. 2, ed.
Walter P.
Heller, Ross M.
Starr, and David Starrett.
Cambridge: Cambridge University Press, pp. 81-104.
Strauch, Ralph E. 1966.
Negative dynamic programming.
Annals of Mathematical Statistics 37:871-890.
Sutherland, W.
R.
S. 1970.
On optimal development in a multi-sectorial economy.
Review of Economic Studies 37:585-589.
Swan, Trevor W. 1956.
Economic growth and capital accumulation.
Economic Record 32:334-361.
Taub, Bart. 1988a.
Efficiency in a pure currency economy with inflation.
Economic Inquiry 26:567-583. 1988b.
The equivalence of optimal lending and monetary equilibria under asymmetric information.
Unpublished manuscript.
Virginia Polytechnic Institute, Blacksburg, Va.Torres, Ricard. 1988.
Stochastic dominance ordering in metric spaces.
Unpublished manuscript.
Northwestern University, Evanston, Ill.
Treadway, Arthur B. 1969.
On rational entrepreneurial behavior and the demand for investment.
Review of Economic Studies 36:227–239.
Tweedie, Richard L. 1975.
Sufficient conditions for ergodicity and recurrence of Markov chains in a general state space.
Stochastic Processes and Their Applications 3:385–403.
Uzawa, Hirofumi. 1964.
Optimal growth in a two-sector model of capital accumulation.
Review of Economic Studies 31:1–25. 1965.
Optimum technical change in an aggregative model of economic growth.
International Economic Review 6:18–31. 1968.
Time preference, the consumption function, and optimum asset holdings.
In Value, Capital, and Growth: Papers in Honour of Sir John Hicks, ed.
J.
N.
Wolfe.
Chicago: Aldine.
Weitzman, Martin. 1973.
Duality theory for infinite horizon convex models.
Management Science 19:783–789.
Yosida, Kosaku, and Edwin Hewitt. 1952.
Finitely additive measures.
Transactions of the American Mathematical Society 72:46–66.
Zeidler, Eberhard. 1986.
Nonlinear Functional Analysis and Its Applications.
New York: Springer-Verlag.
Index of Theorems Theorem 3.1 Space of bounded continuous functions is complete 47 Theorem 3.2 Contraction Mapping Theorem 50 Theorem 3.3 Blackwell's sufficient conditions for a contraction 54 Theorem 3.4 Sufficient conditions for u-h.c. 60 Theorem 3.5 Sufficient conditions for Lh.c. 61 Theorem 3.6 Theorem of the Maximum 62 Lemma 3.7 Approximation of the maximizing value of a concave function 63 Theorem 3.8 Convergence of functions defined as maximizing values 64 Lemma 4.1 Total discounted returns can be expressed recursively 71 Theorem 4.2 The supremum function satisfies the functional equation 71 Theorem 4.3 A solution to the functional equation is the supremum function 72 Theorem 4.4 An optimal sequence attains the supremum in the functional equation 75 Theorem 4.5 Plans generated by the policy correspondence are optimal 76 Theorem 4.6 Existence and characterization results for dynamic programs with bounded returns 79 Theorem 4.7 Monotonicity of the value function 80 Theorem 4.8 Concavity of the value function; single-valued policy function 81 Theorem 4.9 Convergence of the approximate policy functions 82 Theorem 4.10 Differentiability result of Benveniste and Scheinkman 84 Theorem 4.11 Differentiability of the value function 85 Theorem 4.12 Contraction result for the space of functions that are homogeneous of degree one 90 Theorem 4.13 Existence and characterization results for dynamic programs with constant returns to scale 90 Theorem 4.14 Existence result for dynamic programs with unbounded returns 92 Theorem 4.15 Sufficiency of Euler equations and transversality conditions 98 Theorem 6.1 Theorem of Boldrin and Montrucchio 138 Lemma 6.2 Liapounov’s method for global stability of nonlinear systems 140 Theorem 6.3 Global stability of linear systems 146 Theorem 6.4 Dimension of stable manifold for linear systems 146 Theorem 6.5 Local stability of nonlinear systems 147 Theorem 6.6 Dimension of stable manifold for nonlinear systems 147 Lemma 6.7 Characteristic roots of Euler equations come in almost-reciprocal pairs 150 Theorem 6.8 Global stability of linear Euler equations 151 Theorem 6.9 Local stability of nonlinear Euler equations 153 Theorem 7.1 Measure of the limit of an increasing or decreasing sequence of sets 172 Theorem 7.2 Caratheodory Extension Theorem 175, 177 Theorem 7.3 Hahn Extension Theorem 175 Theorem 7.4 Pointwise convergence preserves measurability 179 Theorem 7.5 Approximation of measurable functions by simple functions 180 Theorem 7.6 Measurable Selection Theorem 184 Lemma 7.7 Construction of measures from simple functions 186 Theorem 7.8 Monotone Convergence Theorem 187 Lemma 7.9 Fatou’s Lemma 190 Theorem 7.10 Lebesgue Dominated Convergence Theorem 192 Theorem 7.11 Radon-Nikodym Theorem 194 Lemma 7.12 Decomposition of measures 195 Theorem 7.13 Construction of measures on product spaces 196 Theorem 7.14 Measurability of sections of sets and functions 198 Lemma 7.15 Monotone Class Lemma 200 Theorem 7.16 Existence of conditional expectation 205 Theorem 8.1 Characterization of Markov operators on measurable functions 213 Theorem 8.2 Characterization of Markov operators on probability measures 215 Theorem 8.3 Relationship between Markov operators on functions and those on measures 216 Theorems 8.4–8.6 Parallels for stochastic kernels of Theorems 8.1–8.3 226–229 Theorem 8.7 Extension of Theorem 8.6 to integrable functions 231 Theorem 8.8 Representation of expected values as iterated integrals 232 Theorem 8.9 Construction of transition functions from stochastic difference equations 234 Lemma 9.1 Existence of feasible plans for stochastic sequence problems 243 Theorem 9.2 A solution to the functional equation is the supremum function; any plan generated by the policy correspondence attains the supremum 246 Index of Theorems Lemma 9.3 Total discounted returns can be expressed recursively 249 Theorem 9.4 Any plan that attains the supremum is generated a.e. by the policy correspondence 251 Lemma 9.5 Integration preserves continuity, monotonicity, concavity 261 Theorem 9.6 Existence and characterization results for stochastic dynamic programs with bounded returns 263 Theorem 9.7 Monotonicity of the value function in the endogenous state variables 264 Theorem 9.8 Concavity of the value function in the endogenous state variables; single-valued policy function 265 Theorem 9.9 Convergence of the approximate policy functions 265 Theorem 9.10 Differentiability of the value function with respect to the endogenous state variables 266 Theorem 9.11 Monotonicity of the value function in the exogenous shocks 267 Theorem 9.12 Existence result for stochastic dynamic programs with unbounded returns 274 Theorem 9.13 Use of the policy function to construct a transition function 284 Theorem 9.14 Sufficient conditions for a transition function to have the Feller property 285 Theorem 11.1 Existence and convergence results for finite Markov chains 326 Theorem 11.2 Uniqueness of the ergodic set for finite Markov chains 330 Lemma 11.3 Sufficient condition for a transition matrix to define a contraction mapping 332 Theorem 11.4 Convergence at a uniform rate to a unique invariant distribution for finite Markov chains 332 Lemma 11.5 Characterization of the total variation between two measures 339 Theorem 11.6 Characterization of norm convergence in terms of measures of sets 340 Theorem 11.7 Characterization of norm convergence in terms of integrals of functions 341 Lemma 11.8 Space of probability measures with the total variation norm is complete 343 Theorem 11.9 Existence and convergence results based on Doeblin’s condition 347 Theorem 11.10 Uniqueness of the ergodic set 348 Lemma 11.11 Contraction result based on Condition M 349 Theorem 11.12 Convergence at a uniform rate to a unique invariant measure for Markov processes 350 Lemma 12.1 Approximation of closed sets by continuous functions 355 Lemma 12.2 Approximation of integrals of functions by measures of sets 356 Theorem 12.3 Characterization of weak convergence 358 Theorem 12.4 Sufficient condition for weak convergence in terms of measures of sets 360 Theorem 12.5 Application of Theorem 12.4 to ℝⁿ 361 Theorem 12.6A probability measure is determined by its values on closed sets 363 Characterization of distribution functions 365 Characterization of weak convergence in terms of distribution functions 369 Helly's Theorem 372 Existence of an invariant measure for a Markov process 376 Bounds on expected values for transition functions satisfying a mixing condition 382 Uniqueness and convergence result based on monotonicity and mixing 382 Continuity in a parameter vector of invariant measures 384 Version of Lemma 9.5 that does not require compactness 386 Characterizations of convergence a.e. 417-419 Weak law of large numbers for uncorrelated random variables 421 Strong law for uncorrelated random variables 422 Strong law for correlated random variables 424 Strong law for Markov processes 425 Results needed to prove Theorem 14.7 427 Minimum Norm Duality 432 Results needed to prove Norms Ergodic Lemma 432-433 Norms Ergodic Lemma 434 Riesz Representation Theorem 435 Characterization of continuous linear functionals 446 Hahn-Banach Theorem 450 First Welfare Theorem 453 Second Welfare Theorem 455 Preliminary lemma for models with infinite time horizon 463 Existence of inner product prices for infinite-horizon models 466 Preliminary lemma for stochastic models 468 Existence of inner product prices for stochastic models 469 Existence of inner product prices for stochastic, infinite-horizon models 470 Contraction result for operators defined by expected values 509 Contraction result for operators defined by logarithms of expected values 511 578 Theorem 17.3 Theorem 17.4 Lemma 17.5 Lemma 17.6 Theorem 17.7 Index of Theorems Brouwer Fixed-Point Theorem 517 Schauder Fixed-Point Theorem 520 ity of functions defined as expected values 521 Fixed-point result for pointwise limits of monotone Existence of fixed points of monotone operators General Index Abreu, D., 500 Absolute continuity, 193 Additivity, countable, 170 Adjoint, 213-219 Adjustment costs, 112-114, 158-159, 292-297, 315, 395-396, 413 Aggregator function, 115.
See also Recursive preferences Aghion, P., 130 Albrecht, J.
W., 315 Algebra, 173 Borel, 169-170 Almost everywhere (a.e.), 171 Almost surely (a.s.), 171 Araujo, A., 84 Arrow, K.
J., 3, 6, 29, 35, 102, 130, 412, 473, 444 Arrow-Debreu prices, 6, 29 Asset prices, 300-304, 315, 482-485, 500 Axell, B., 315 Back, K., 474 Baire function, 182 Banach space, 47 Bang-bang solution, 129 Bartle, R.
G., 167, 194, 209 Beals, R., 130 Becker, G.
S., 129 Becker, R.
A., 560 Behnke, H., 253 Bellman, R., 3, 7, 67, 101 Ben-Porath, Y., 129 Benveniste, L.
M., 84 Benveniste and Scheinkman, Theorem of, 84 Berge, C., 65 Bertsekas, D.
P., 101, 287 Bewley, T.
F., 474 Billingsley, P., 388 Bizer, D., 560 Blackwell, D., 3, 54, 65, 90, 101, 246, 253, 287 conditions for a contraction, 54-55 example of a nonmeasurable value function, 253-254 Blume, L., 101, 287, 560 Boldrin, M., 138, 161 Boldrin and Montrucchio, Theorem of, 138 Bolton, P., 130 Border, K.
C., 541 Borel algebra, 169-170, 175-176 set, 169-170, 175-176 measure, 175-177 measurability of a function, 178 measurability of a composite function, 182-183 Boundary, 358 Bounded returns, 77-87, 259-270 Boyer, M., 130 Breeden, D.
T., 315 Breiman, L., 209, 437 Brock, W.
A., 35, 129, 161, 315, 412, 500 579 588 Value function (continued) with constant returns to scale, 87-92, 270-273 with unbounded returns, 92-97, 273-280 nonmeasurable example of, 253-254 Value loss, 142, 161 Vector space, 43-44 normed, 45-46 complete normed, 47 Weak convergence of probability measures, 337, 353-364, 388 of distribution functions, 369-375, 388 Univerzita Karlova
## 4 ERGE
1 21 Praha | Politickych věznd 7 V Praze General Index of a monotone Markov process, 375-383, 388 Weak law of large numbers, 415 for uncorrelated random variables, 421-422 Weitzman, M., 102 Welfare Theorems, 451-458, 473-474 Werning, P., 101 Williamson, R.
E., 130 Woodford, M., 541 Yahav, J.
A., 388, 412 Yosida, K., 468 Yushkevich, A.
A., 287 Zeidler, E., 541 Zilcha, I., 35, 315 586 General Index Radner, R., 35, 161, 413 Radon-Nikodym Theorem, 194 Ramsey, F.
P., 3, 5, 6, 34, 129, 315 Random variable, 177 expectation of, 191 σ-algebra generated by, 208 Rational expectations, 35 Razin, A., 388, 412 Rebelo, S., 130, 500 Rectangle, measurable, 195, 197 finite, 221 Recurrent state, 326 Recursive competitive equilibrium, 30, 479-480, 499-500, 541 Recursive preferences, 114-118, 130, 160-161, 495-500 Relatively open, 354 Reservation wage, 307 Riemann integral, 184-185 Riesz Representation Theorem, 435 Rios-Rull, J.
V., 500 Rockafellar, R.
T., 161 Rosen, S., 129 Rosenblatt, M., 351 Ross, S.
A., 315 Rothschild, M., 129 Royden, H.
L., 65, 167, 178, 194, 209, 361, 435 Ryder, H., 102 Sample path, 223 Samuelson, P.
A., 500 Sargent, T.
J., 101, 287, 413 Savings.
See Consumer theory; Growth Scarf, H.
E., 130, 412 Schauder Fixed-Point Theorem, 520, 541 application to OG model, 522-525, 535-539 application to tax model, 551, 556-558 Schechtman, J., 315 Scheinkman, J.
A., 84, 102, 147-148, 161, 162, 315 Schwartz, N.
L., 102 Search, 304-311, 315, 404-413, 501 Second Welfare Theorem, 27-28, 455-456, 473-474 Remark on, 456-458 Section, 198 Securities prices, 300-304, 315, 484-485, 500 Separation Theorem, 450-451 Sequence problem (SP), 66 Set measurable, 169 Borel, 169-170, 176 Lebesgue, 176 section of, 198 Setwise convergence, 335 Shell, K., 161, 541 Shiryayev, A.
N., 209, 222, 238 Shreve, S.
E., 287 σ-algebra, 168 generated by a family of sets, 169 Borel, 169-170 completion of, 176 generated by a random variable, 208 σ-finite measure, 175 σ-measurable function.
See Measurable function Signed measure, 339 Simple function, 179 Singleton, K.
J., 315 Singular measure, 193 Skorohod, A.
V., 238, 287, 351 Snell, J.
L., 351 Solow, R.
M., 35, 129 Song, B.
H., 101 Sonstelie, J., 500 Space vector, 43 metric, 44 normed vector, 45 Banach, 47 measurable, 169 measure, 171 probability, 171 complete measurable, 176 product, 196 of signed measures, 339 dual, 446-447, 473 Lp, 447-448, 459-462, 474 L∞, 449-450, 462 Speed of convergence, 147, 153 Spulber, D.
F., 101 (5, 8) inventory model, 118-123, 130, 389-391, 412 General Index 587 Stability.
See Difference equations Stable manifold, 147-148 Stacchetti, E., 500 Standard representation, 179 State, 17 State space, 68, 241 Stationary point, 15, 134-135, 137 stochastic process, 223 transitions, 224 Markov process, 224 plan, 243 distribution.
See Invariant distribution Stigler, G.
J., 315 Stiglitz, J.
E., 129 Stochastic process, 223, 238 kernel, 226, 238 Euler equations, 280-283, 287 matrix, 320 dominance, 378 growth.
See Growth Stochastic difference equation, 19 transition function defined by, 234-237 Stock market, 300-304, 315 Stokey, N.
L., 129, 130, 500, 560 Strauch, R.
E., 101, 102 Strong convergence of probability measures, 337-344 of a Markov process, 344-351 Strong law of large numbers, 415 for uncorrelated random variables, 422-423 for correlated random variables, 424 for Markov processes, 425-437 Strotz, R., 129 Subgradient, 84 Successive approximations, method of, 40-42 Support of a distribution, 372 function, 497 Supremum function, 70, 245, 257 nonmeasurable example of, 253254 continuity of, 255 Sutherland, R.
S., 161 Swan, T.
W., 35 Taub, B., 413 Taxes, 541, 542-560 Technical progress, 105-107, 129, 485-487, 500 Theorem of the Maximum, 62, 65 Theorems.
See Index of Theorems Theory of the consumer, 126-128 with recursive preferences, 116-117, 130 Tonelli's Theorem, 234 Torres, R., 388 Total variation norm, 339 Transient state, 322 Transition function, 20, 212, 238 operators associated with, 213-219 iterates of, 219 monotone, 220 stable, 220 stationary, 224 defined by a stochastic difference equation, 234-237 defined by a policy function, 283-286 Transversality condition, 98, 102, 281 Treadway, A.
B., 129 Tree cutting, 107, 129Jones, L.
E., 130, 474, 500 Jordan matrix, 144 Jorgenson, D.
W., 129 Jovanovic, B., 315 Judd, K.
L., 560 Jullien, B., 130 Kamien, M.
I., 102 Karlin, 5, 101, 130, 412 Kehoe, T.
J., 541 Kemeny, J.
G., 351 Kernel, stochastic, 226 Knapp, A.
W., 351 Kolmogorov, A.
N., 65 Koopmans, T.
C., 35, 129, 130, 161 Kurz, M., 102, 161 Kydland, F., 130, 500 Labadie, P., 541 Lang, S., 281 Law of large numbers, 21, 319, 415 for uncorrelated random variables, 421–423 for correlated random variables, 424 for Markov processes, 425–437 Law of the iterated expectation, 208 Learning by doing, 107–109, 129 Lebesgue sets, 176 measure, 176 measurability of composite functions, 182–183 integral, 185 Lebesgue Dominated Convergence Theorem, 192–193 LeRoy, S.
F., 315 Le Van, C., 500 Levhari, D., 162 Levine, D.
K., 541 Levinson, N., 162 Lewis, L M., 474 Liapounov function, 139–143 Linear approximations, 147–148, 153–156 Linear functional, 445–450 inner product representation of, 447, 458–473 Linear operator, 431 Linear-quadratic model, 95–97, 148–153, 277–280, 282–283, 287 Linear space.
See Vector space Linear utility in a growth model, 105, 129 in a currency economy, 401–402, 413 in a credit economy, 402–403, 413 580 General Index Brouwer Fixed-Point Theorem, 517, 541 application to OG model, 518–519, 535 Brown, D.
J., 474 Burger, E., 541 Burmeister, E., 129, 161 “Cake-eating” problem, 105 Caplin, A.
S., 412 Caratheodory Extension Theorem, 175, 177 Cash-in-advance model, 397–402, 413, 560.
See also Overlappinggenerations model Cass, D., 35, 129, 161, 541 Cauchy sequence, 46–47 Chaos, 132, 139 Characteristic function.
See Indicator function Characteristic roots, 145–148 for Euler equations, 148–156 for linear-quadratic model, 149–153 Chebyshev’s inequality, 421 Chung, K.
L., 209, 351, 437 Clarke, F.
H., 129 Closure, 353 relative, 354 Coddington, E.
A., 162 Coleman, W.
J., 560 Commodity space, choice of, 458–462, 474 Competitive equilibrium, 441–445, 452–453, 541 Complete metric space, 47 Completion, 176 of Borel measure, 176 Composition of functions, measurability of, 182 Concavity of the value function, 80–81, 264–265, 270 Conditional expectation, 205 Conditional probability, 202, 206–207 Condition D, 345, 351 Condition M, 348, 351 Cone, 88 Consequent set, 326, 346 Constant returns to scale, 87–92, 101, 270–273 investment with, 113–114, 130, 159–160 Consumer theory, 126–128 with recursive preferences, 116–117, 130, 160–161 Contingency plan, 17, 242, 255 Continuation of a plan, 248, 258 Continuity of a correspondence, 56–61 Contraction mapping, 50, 65 Blackwell’s conditions for, 54–55 Contraction Mapping Theorem, 50–52 corollaries to, 52–53 application to differential equations, 53–54 application to dynamic programs, 79, 89–91, 263–264, 269, 271–272 application to recursive utility, 115–116 application to Markov chains, 331–333 application to Markov processes, 348–351 application to operators defined by integrals, 508–513 application to OG model, 513–516, 535 application to tax model, 552–554 Convergence, 46 uniform, 49 speed of, 147 almost everywhere (a.e.), 171 almost sure (a.s.), 171 of approximate policy functions, 265–266 of distribution functions, 369–375, 388 in measure, 415 in probability (in pr.), 415 Convergence-determining class, 362 Convergence of a Markov process strong, 344–351 weak, 375–383, 388 Convergence of probability measures, 317–318, 334–338 setwise, 335 General Index 581 Convergence of probability measures (continued) strong, 337–344 weak, 337, 353–364 in the total variation norm, 343 Convex cone, 88 Correlated random variables, law of large numbers for, 424 Correspondence, 55 lower hemi-continuous (l.h.c.), 56–61, 65 upper hemi-continuous (u.h.c.), 56–58, 60–61, 65 continuous, 57–60, 65 graph of, 60 measurable selection from, 183 See also Policy correspondence Countable additivity, 170 Countable partition, 203 Cox, J.
C., 315 Credit economy, 402–404 Currency economy, 397–402, 413, 501.
See also Overlapping-generations model Cycles, 132, 139, 157–158, 323 Cyclically moving subsets, 323 Dana, R.-A., 500 Danthine, J.-P., 315 Darrough, M.
N., 129 Debreu, G., 3, 6, 29, 35, 444–445, 452, 474 Decomposition of measures, 195 Denardo, E.
V., 101, 130 Diamond, P.
A., 130 Difference equations, 132–133 economic examples of, 133–138 arising from dynamic programs, 138–139 global stability of, 139–143 linear, 143–148 arising from Euler equations, 148–156 Differentiability of the value function, 85, 101, 266–267, 270, 287 of the policy function, 101, 287 Distorting taxes, 541, 542–560 Distortion, 501, 542 Distribution functions, 364–369, 388 weak convergence of, 369–375, 388 monotone sequence of, 374 Dobell, A.
R., 129 Doeblin’s Condition, 345, 351 Dominance relation for probability measures, 378–380, 388 Dominated Convergence Theorem, 192–193 Donaldson, J.
B., 315 Doob, J.
L., 238, 348, 351 Dual space, 446–447, 473 examples of, 447–450 Duffie, D., 560 Dynkin, E.
B., 287, 351 Easley, D., 101, 287 Eisner, R., 129 Ekeland, I., 102 Envelope condition, 14, 100, 281 Epstein, L.
G., 130 Equicontinuity, 520–522 Equivalence class of functions, 449–450 Ergodic set, 321, 346 Essential supremum (ess sup) norm, 449 Euler equations, 97–100, 102, 148–156 stochastic, 280–283, 287 equilibrium existence argument based on, 547–554 Event, 171 Exchange economy with recursive preferences, 117–118, 130 asset prices in, 300–304, 315 with many consumers, 495–499, 500 Expectation, 165–168, 177, 184–185, 191 conditional, 205 iterated, 208 Extension of a measure, 175, 177 on a product space, 196–197 Extraneous solution to value function, 74–75 in policy correspondence, 76–77

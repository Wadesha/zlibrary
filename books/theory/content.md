# Dynamic Asset Pricing Theory

> hy3忠实校订

# THIRD EDITION

Darrell Duffie

Princeton University Press Princeton and Oxford

--

HG

Library of Congress Cataloging-in-Publication Data

Duffie, Darrell.

British Library Cataloging-in-Publication Data is available

10 9 8 7 6 5 4 3 2 1

--

# Preface

--

PART I: DISCRETE-TIME MODELS

1 Introduction to State Pricing

# 1.A Arbitrage and State Prices
# 1.B Risk-Neutral Probabilities
# 1.C Optimality and Asset Pricing
# 1.D Efficiency and Complete Markets
# 1.E Optimality and Representative Agents
# 1.F State-Price Beta Models
# Exercises

2 The Basic Multiperiod Model

# 2.A Uncertainty 2.2... ee ee ee eee
# 2.B Security Markets... ee eee
# 2.C Arbitrage, State Prices, and Martingales
# 2.D Individual Agent Optimality
# 2.E Equilibrium and Pareto Optimality
# 2.F Equilibrium Asset Pricing
# 2.G Arbitrage and Martingale Measures
# 2.H Valuation of Redundant Securities
# 2.I American Exercise Policies and Valuation
# 2.J Is Early Exercise Optimal
# Exercises 2 2 ee ee
# Notes

--

3 The Bellman Approach # 3.A First-Order Bellman Conditions # 3.B Markov Uncertainty

4 Markov Asset Pricing # 4.A Security Pricing by Markov Control # 4.B Markov Arbitrage-Free Valuation # 4.C Early Exercise and Optimal Stopping

5 The Infinite-Horizon Setting # 5.A Markov Dynamic Programming # 5.B Dynamic Programming and Equilibrium # 5.C Arbitrage and State Prices 0 0 ee # 5.D Optimality and State Prices # 5.E Method-of-Moments Estimation

--

PART II: CONTINUOUS-TIME MODELS

6 The Black-Scholes Model # 6.A Trading Gains for Brownian Prices # 6.B Martingale Trading Gains # 6.C Ito Prices and Gains, 2... ee ee

# 6.D The Black-Scholes Option-Pricing Formula
# 6.E Black-Scholes Formula: First Try
# 6.F The PDE for Arbitrage-Free Prices
# 6.G The Feynman-Kac Solution
# 6.H The Multidimensional Case

7 State Prices and Equivalent Martingale Measures

# 7.A Numeraire Invariance
# 7.B State Prices and Doubling Strategies
# 7.C Expected Rates of Return
# 7.D Equivalent Martingale Measures
# 7.E State Prices and Martingale Measures
# 7.F Girsanov and Market Prices of Risk 2... .0..00.0,., tll
# 7.G Black-Scholes Again
# 7.H Complete Markets
# 7.I Redundant Security Pricing
# 7.J Martingale Measures from No Arbitrage
# 7.K Arbitrage Pricing with Dividends
# 7.L Lumpy Dividends and Term Structures
# 7.M Martingale Measures, Infinite Horizon
# Exercises
# Notes

8 Term-Structure Models # 8.A The Term Structure # 8.B One-Factor Term-Structure Models # 8.C The Gaussian Single-Factor Models # 8.D The Cox-Ingersoll-Ross Model # 8.E The Affine Single-Factor Models
# 8.F Term-Structure Derivatives
# 8.G The Fundamental Solution
# 8.H Multifactor Models
# 8.I Affine Term-Structure Models
# 8.J The HJM Model of Forward Rates
# 8.K Markovian Yield Curves and SPDEs
# Exercises
# Notes

9 Derivative Pricing # 9.A Martingale Measures in a Black Box # 9.B Forward Prices # 9.C Futures and Continuous Resettlement # 9.D Arbitrage-Free Futures Prices # 9.E Stochastic Volatility
# 9.F Option Valuation by Transform Analysis
# 9.G American Security Valuation
# 9.H American Exercise Boundaries
# 9.I Lookback Options
# Exercises
# Notes

10 Portfolio and Consumption Choice ....-...-.--.-.-.-++ # 10.A Stochastic Control # 10.B Merton’s Problem # 10.C Solution to Merton’s Problem # 10.D The Infinite-Horizon Case # 10.E The Martingale Formulation
# 10.F Martingale Solution
# 10.G A Generalization
# 10.H The Utility-Gradient Approach
# Exercises
# Notes

11 Equilibrium # 11.A The Primitives # 11.B Security-Spot Market Equilibrium # 11.C Arrow-Debreu Equilibrium # 11.D Implementing Arrow-Debreu Equilibrium # 11.E Real Security Prices
# 11.F Optimality with Additive Utility
# 11.G Equilibrium with Additive Utility
# 11.H The Consumption-Based CAPM
# 11.I The CIR Term Structure
# 11.J The CCAPM in Incomplete Markets
# Exercises
# Notes

12 Corporate Securities # 12.A The Black-Scholes-Merton Model # 12.B Endogenous Default Timing # 12.C Example: Brownian Dividend Growth # 12.D Taxes and Bankruptcy Costs # 12.E Endogenous Capital Structure
# 12.F Technology Choice
# 12.G Other Market Imperfections
# 12.H Intensity-Based Modeling of Default
# 12.I Risk-Neutral Intensity Process .....22222 0s
# 12.J Zero-Recovery Bond Pricing
# 12.K Pricing with Recovery at Default
# 12.L Default-Adjusted Short Rate
# Exercises
# Notes

13 Numerical Methods

# 13.A Central Limit Theorems ........--..--+
# 13.B Binomial to Black-Scholes
# 13.C Binomial Convergence for Unbounded Derivative Payoffs
# 13.D Discretization of Asset Price Processes
# 13.E Monte Carlo Simulation
# 13.F Efficient SDE Simulation
# 13.G Applying Feynman-Kac
# 13.H Finite-Difference Methods
# 13.I Term-Structure Example
13.J Finite-Difference Algorithms with Early Exercise Options # 13.K The Numerical Solution of State Prices
# 13.L Numerical Solution of the Pricing Semi-Group
# 13.M Fitting the Initial Term Structure
# Exercises

# A Finite-State Probabilities
# A.1 Separating Hyperplanes and Optimality
# A.2 Probability

# B Stochastic Integration

# C SDE, PDE, and Feynman-Kac
# C.1 Ito's Formula with Jumps

# D Utility Gradients
D.1 Ito’s Formula for Complex Functions ............64:

# E Counting Processes

# F Finite-Difference Code

# Bibliography
# Symbol Glossary
# Author Index
# Subject Index

--

# Preface

THIS BOOK IS an introduction to the theory of portfolio choice and asset pricing in multiperiod settings under uncertainty. An alternate title might be Arbitrage, Optimality, and Equilibrium, because the book is built around the three basic constraints on asset prices: absence of arbitrage, single-agent optimality, and market equilibrium. The most important unifying principle is that any of these three conditions implies that there are “state prices,” meaning positive discount factors, one for each state and date, such that the price of any security is merely the state-price weighted sum of its future payoffs. This idea can be traced to the invention by Arrow (1953)
of the general equilibrium model of security markets. Identifying the state prices is the major task at hand. Technicalities are given relatively little emphasis so as to simplify these concepts and to make plain the similarities between discrete- and continuous-time models.

To someone who came out of graduate school in the mid-eighties, the decade spanning roughly 1969-79 seems like a golden age of dynamic asset pricing theory. Robert Merton started continuous-time financial modeling with his explicit dynamic programming solution for optimal portfolio and consumption policies. This set the stage for his 1973 general equilibrium model of security prices, another milestone. His next major contribution was his arbitrage-based proof of the option pricing formula introduced by Fisher Black and Myron Scholes in 1973, and his continual development of that approach to derivative pricing. The Black-Scholes model now seems to be, by far, the most important single breakthrough of this
“golden decade,” and ranks alone with the Modigliani and Miller (1958)
Theorem and the Capital Asset Pricing Model (CAPM) of Sharpe (1964)
and Lintner (1965) in its overall importance for financial theory and practice. A tremendously influential simplification of the Black-Scholes model appeared in the “binomial” option pricing model of Cox, Ross, and
Rubinstein (1979), who drew on an insight of Bill Sharpe.

Working with discrete-time models, LeRoy (1973), Rubinstein (1976), and Lucas (1978) developed multiperiod extensions of the CAPM. The
“Lucas model” is the “vanilla flavor” of equilibrium asset pricing models.
The simplest multiperiod representation of the CAPM finally appeared in
Doug Breeden’s continuous-time consumption-based CAPM, published in
1979. Although not published until 1985, the Cox-Ingersoll-Ross model of the term structure of interest rates appeared in the mid-seventies and is still the premier textbook example of a continuous-time general equilibrium asset pricing model with practical applications. It also ranks as one of the key breakthroughs of that decade. Finally, extending the ideas of
Cox and Ross (1976) and Ross (1978), Harrison and Kreps (1979) gave an almost definitive conceptual structure to the whole theory of dynamic security prices.

Theoretical developments in the period since 1979, with relatively few exceptions, have been a mopping-up operation. Assumptions have been weakened, there have been noteworthy extensions and illustrative models, and the various problems have become much more unified under the umbrella of the Harrison-Kreps model of equivalent martingale measures.
For example, the standard approach to optimal portfolio and consumption choice in continuous-time settings has become the martingale method of Cox and Huang (1989). An essentially final version of the relationship between the absence of arbitrage and the existence of equivalent martingale measures was finally obtained by Delbaen and Schachermayer (1999).

On the applied side, markets have experienced an explosion of new valuation techniques, hedging applications, and security innovation, much of this based on the Black-Scholes and related arbitrage models.
No major investment bank, for example, lacks the experts or computer technology required to implement advanced mathematical models of the term structure. Because of the wealth of new applications, there has been a significant development of special models to treat stochastic volatility, jump behavior including default, and the term structure of interest rates, along with many econometric advances designed to take advantage of the resulting improvements in richness and tractability.

Although it is difficult to predict where the theory will go next, in order to promote faster progress by people coming into the field it seems wise to have some of the basics condensed into a textbook. This book is designed to be a streamlined course text, not a research monograph.
Much generality is sacrificed for expositional reasons, and there is relatively little emphasis on mathematical rigor or on the existence of general equilibrium. As its title indicates, I am treating only the theoretical side

of the story. Although it might be useful to tie the theory to the empirical side of asset pricing, we have excellent treatments of the econometric modeling of financial data, such as Campbell, Lo, and MacKinlay (1997)
and Gourieroux and Jasiak (2000). I also leave out some important aspects of functioning security markets, such as asymmetric information and transactions costs. I have chosen to develop only some of the essential ideas of dynamic asset pricing, and even these are more than enough to put into one book or into a one-semester course.

Other books whose treatments overlap with some of the topics treated here include Avellanedo and Laurence (2000), Björk (1998), Dana and
Jeanblanc (1998), Demange and Rochet (1992), Dewynne and Wilmott
(1994), Dixit and Pindyck (1993), Dothan (1990), Duffie (1988b), Harris
(1987), Huang and Litzenberger (1988), Ingersoll (1987), Jarrow (1988),
Karatzas (1997), Karatzas and Shreve (1998), Lamberton and Lapeyre
(1997), Magill and Quinzii (1994), Merton (1990), Musiela and Rutkowski
(1997), Neftci (2000), Stokey and Lucas (1989), Wilmott, Dewynne, and
Howison (1993), and Wilmott, Howison, and Dewynne (1995). Each has its own aims and themes. I hope that readers will find some advantage in having yet another perspective.

A reasonable way to teach a shorter course on continuous-time asset pricing out of this book is to begin with Chapter 1 or 2 as an introduction to the basic notion of state prices and then to go directly to Chapters 5 through 11. Chapter 12, on numerical methods, could be skipped at some cost to the student’s ability to implement the results. There is no direct dependence of any results in Chapters 5 through 12 on the first four chapters.

For mathematical preparation, little beyond undergraduate analysis, as in Bartle (1976), and linear algebra is assumed. Some familiarity with
Royden (1968) or a similar text on functional analysis and measure theory, would also be useful. Some background in microeconomics would be useful, say Kreps (1990) or Luenberger (1995). Familiarity with probability theory at the level of Jacod and Protter (2000), for example, would also speed things along, although measure theory is not used heavily. In any case, a series of appendices supplies all of the required concepts and definitions from probability theory and stochastic calculus. Additional useful references in this regard are Brémaud (1981), Karatzas and Shreve (1988), Revuz and Yor (1991), and Protter (1990).

Students seem to learn best by doing problem exercises. Each chapter has exercises and notes to the literature. I have tried to be thorough in giving sources for results whenever possible and plead that any cases

in which I have mistaken or missed sources be brought to my attention for correction. The notation and terminology throughout is fairly standard. I use R to denote the real line and R = R ∪ {−∞, +∞} for the extended real line. For any set Z and positive integer n, I use Z^n for the set of n-tuples of the form (z₁ … zₙ) with zᵢ in Z for all i. An example is Rⁿ.Chien, Seongman Cho, Fai Tong Chung, Chin-Shan Chuan, Howie Corb,
Qiang Dai, Eugene Demler, Shijic Deng, Michelle Dick, Phil Dolan, Rod
Duncan, Wedad Elmaghraby, Kian Esteghamat, Mark Ferguson, Christian Riis Flor, Prashant Fuloria, John Fuqua, Nicolae Garleanu, Mark
Garmaise, Filippo Ginanni, Michel Grueneberg, Bing Han, Philippe
Henrotte, Ayman Hindy, Yael Hochberg, Toshiki Honda, Taiichi Hoshino,

Jiangping Hu, Ming Huang, Cristobal Hunceus, Don Iglchart, Michael

Intriligator, Farshid Jamshidian, Ping Jiang, Shinsuke Kambe, Rui Kan,
Ron Karidi, Don Kim, Felix Kubler, Allan Kulig, Yoichi Kuwana, Piero
La Mura, Yingcong Lan, Joe Langsam, Jackie Lec, André Levy, Shujing
Li, Wenzhi Li, Tiong Wee Lim, Jun Liu, Leonid Litvak, Hanno Lustig,
Rob McMillan, Rajnish Mehra, Sergei Morozov, Christophe Mueller,
Ravi Myneni, Lee Bath Nelson, Yigal Newman, Angela Ng, Kazuhiko
Ohashi, Hui Ou-Yang, John Overdeck, Hideo Owen, Caglar Ozden, Mikko
Packalen, Jun Pan, Lasse Pedersen, Albert Perez, Monika Piazzesi, Jorge
Picazo, Heracles Polemarchakis, Marius Rabus, Rohit Rahi, Shikhar
Ranjan, Michael Rierson, Amir Sadr, Yuliy Sannikoy, Marco Scarsini,
Martin Schneider, Christine Shannon, Yong-Seok Shin, Mark Shivers,
Hersir Sigurgeirsson, Marciano Siniscalchi, Ravi Singh, Ronnie Sircar,
Viktor Spivakovsky, Lucie Tepla, Sergiy Terentyev, Rajat Tewari, Sverrir
Thorvaldsson, Alex Tolstykh, Tunay Tunca, John Uglum, Len Umantsevy,
Stijn Van Nieuwerburgh, Laura Veldkamp, Mary Vyas, Muhamet Yildiz,
Nese Yildiz, Ke Wang, Neng Wang, Chao Wei, Wei Wei, Pierre-Olivier
Weill, Steven Weinberg, Seth Weingram, Guojun Wu, Pinghua Young, Assaf
Zeevi, and Alexandre Ziegler, with apologies to those whose assistance was forgotten. I am especially grateful to the expert team of Japanese translators of the second edition, Toshiki Honda, Kazuhiko Ohashi, Yoichi
Kuwana, and Akira Yamazaki, all of whom are personal friends as well.

For the reader’s convenience, the original preface has been revised for this third edition. Significant improvements have been made in most chapters. Chapter 11, “Corporate Securities,” has been added for this edition.
Errors are my own responsibility, and I hope to hear of them and any other comments from readers.

Darrell Duffie

# Discrete-Time Models

This first part of the book takes place in a discrete-time setting with a discrete set of states. This should ease the development of intuition for the models to be found in Part II. The three pillars of the theory, arbitrage, optimality, and equilibrium, are developed repeatedly in different settings.
Chapter 1 is the basic single-period model. Chapter 2 extends the results of Chapter 1 to many periods. Chapter 3 specializes Chapter 2 to a Markov setting and illustrates dynamic programming as an alternate solution technique. The Ho-and-Lee and Black-Derman-Toy term-structure models are included as exercises. Chapter 4 is an infinite-horizon counterpart to
Chapter 3 that has become known as the Lucas model.

The focus of the theory is the notion of state prices, which specify the price of any security as the state-price weighted sum or expectation of the security’s state-contingent dividends. In a finite-dimensional setting, there exist state prices if and only if there is no arbitrage. The same fact is true in infinite-dimensional settings under mild technical regularity conditions.
Given an agent’s optimal portfolio choice, a state-price vector is given by that agent’s utility gradient. In an equilibrium with Pareto optimality, a state-price vector is likewise given by a representative agent’s utility gradient at the economy’s aggregate consumption process.

Introduction to State Pricing

THIS CHAPTER INTRODUCES the basic ideas in a finite-state one-period setting. In many basic senses, each subsequent chapter merely repeats this one from a new perspective. The objective is a characterization of security prices in terms of “state prices,” one for each state of the world. The price of a given security is simply the state-price weighted sum of its payoffs in the different states. One can treat a state price as the “shadow price,” or
Lagrange multiplier, for wealth contingent on a given state of the world.
We obtain a characterization of state prices, first based on the absence of arbitrage, then based on the first-order conditions for optimal portfolio choice of a given agent, and finally from the first-order conditions for
Pareto optimality in an equilibrium with complete markets. State prices are connected with the “beta” model for excess expected returns, a special case of which is the Capital Asset Pricing Model (CAPM). Many readers will find this chapter to be a review of standard results. In most cases, here and throughout, technical conditions are imposed that give up much generality so as to simplify the exposition.

# A. Arbitrage and State Prices

Uncertainty is represented here by a finite set {1,…, S} of states, one of which will be revealed as true. The N securities are given by an N × S matrix D, with D_{ij} denoting the number of units of account paid by security i in state j. The security prices are given by some q in R^N. A portfolio θ ∈ R^N has market value q·θ and payoff D^T θ in R^S. An arbitrage is a portfolio θ in R^N with q·θ < 0 and D^T θ ≥ 0, or q·θ ≤ 0 and D^T θ > 0. An arbitrage is therefore, in effect, a portfolio offering “something for nothing.” Not surprisingly, it will later be shown that an arbitrage is naturally ruled out, and this gives a characterization of security prices as follows. A

Figure 1.1. Separating a Cone from a Linear Subspace

state-price vector is a vector ψ in R^S with q = Dψ. We can think of ψ as the marginal cost of obtaining an additional unit of account in state j.

Theorem. There is no arbitrage if and only if there is a state-price vector.

Proof: The proof is an application of the Separating Hyperplane
Theorem. Let L = R × R^S and M = {(-q·θ, D^T θ) : θ ∈ R^N}, a linear subspace of L. Let K = R_+ × R^S, which is a cone (meaning that if x is in K, then λx is in K for each strictly positive scalar λ). Both K and M are closed and convex subsets of L. There is no arbitrage if and only if K and M intersect precisely at 0, as pictured in Figure 1.1.

Suppose K ∩ M = {0}. The Separating Hyperplane Theorem (in a version for closed cones that is found in Appendix B) implies the existence of a nonzero linear functional F : L → R such that F(z) < F(x) for all z in M and nonzero x in K. Since M is a linear space, this implies that
F(z) = 0 for all z in M and that F(x) > 0 for all nonzero x in K. The latter fact implies that there is some α > 0 in R and ψ ≥ 0 in R^S such that F(v,c) = α v + ψ·c, for any (v,c) ∈ L. This in turn implies that
−α q·θ + ψ·(D^T θ) = 0 for all θ in R^N. The vector (1/α)ψ is therefore a state-price vector.

Conversely, if a state-price vector exists, then for any θ, we have q·θ = ψ·(D^T θ). Thus, when D^T θ > 0, we have q·θ > 0, and when D^T θ ≥ 0, we have q·θ ≥ 0, so there is no arbitrage. |

# B. Risk-Neutral Probabilities

We can view any ψ in R^S with ψ_1 + … + ψ_S = 1 as a vector of probabilities of the corresponding states. Given a state-price vector ψ for the dividendprice pair (D, q), let W = ψ_1 + … + ψ_S and, for any state j, let π_j = ψ_j/W.

We now have a vector (π_1, …, π_S) of probabilities and can write, for an arbitrary security i,

q_i/W = E(D_i) = Σ_{j=1}^S π_j D_{ij},

viewing the normalized price of the security as its expected payoff under specially chosen “risk-neutral” probabilities. If there exists a portfolio θ with D^T θ = (1,1,…,1), then W = θ·q is the discount on riskless borrowing and, for any security i, q_i = W E(D_i), showing any security’s price to be its discounted expected payoff in this sense of artificially constructed probabilities.

C. Optimality and Asset PricingSuppose the dividend-price pair (D, q) is given. An agent is defined by a strictly increasing utility function \( U : \mathbb{R}^S \rightarrow \mathbb{R} \) and an endowment \( e \) in \( \mathbb{R}^S \). This leaves the budget-feasible set \[
X(q,e) = \{ e + D' \theta \in \mathbb{R}^S : \theta \in \mathbb{R}^N, q \cdot \theta \leq 0 \}, \] and the problem \[ \sup_{c \in X(q,e)} U(c). \tag{1}
\]
We will suppose for this section that there is some portfolio \( \theta^0 \) with payoff \( D' \theta^0 > 0 \). Because \( U \) is strictly increasing, the wealth constraint \( q \cdot \theta \leq 0 \) is then binding at an optimum. That is, if \( c^* = e + D' \theta^* \) solves (1), then \( q \cdot \theta^* = 0 \).

**Proposition.** If there is a solution to (1), then there is no arbitrage. If \( U \) is continuous and there is no arbitrage, then there is a solution to (1).

*Proof is left as an exercise.*

**Theorem.** Suppose that \( c^* \) is a strictly positive solution to (1), that \( U \) is continuously differentiable at \( c^* \), and that the vector \( dU(c^*) \) of partial derivatives of \( U \) at \( c^* \) is strictly positive. Then there is some scalar \( \lambda > 0 \) such that \( \lambda dU(c^*) \) is a state-price vector.

**Proof:** The first-order condition for optimality is that for any \( \theta \) with \( q \cdot \theta = 0 \), the marginal utility for buying the portfolio \( \theta \) is zero. This is expressed more precisely in the following way. The strict positivity of \( c^* \) implies that for any portfolio \( \theta \), there is some scalar \( k > 0 \) such that \( c^* + \alpha D' \theta > 0 \) for all \( \alpha \) in \( [-k, k] \). Let \( g(\alpha) : [-k, k] \rightarrow \mathbb{R} \) be defined by
\[ g(\alpha) = U(c^* + \alpha D' \theta).
\]
Suppose \( q \cdot \theta = 0 \). The optimality of \( c^* \) implies that \( g \) is maximized at \( \alpha = 0 \). The first-order condition for this is that \( g'(0) = dU(c^*) \cdot D' \theta = 0 \). We can conclude that, for any \( \theta \) in \( \mathbb{R}^N \), if \( q \cdot \theta = 0 \), then \( dU(c^*) \cdot D' \theta = 0 \). From this, there is some scalar \( \lambda \) such that \( dU(c^*) = \lambda D^{-1} q \).

By assumption, there is some portfolio \( \theta^0 \) with \( D' \theta^0 > 0 \). From the existence of a solution to (1), there is no arbitrage, implying that \( q \cdot \theta^0 > 0 \). We have
\[ q \cdot \theta^0 = \lambda dU(c^*) \cdot D' \theta^0 > 0.
\]
Thus \( \lambda > 0 \). We let \( \lambda = 1/\mu \), obtaining \[ q = \mu dU(c^*), \tag{2}
\] implying that \( \mu dU(c^*) \) is a state-price vector. \(\square\)

Although we have assumed that \( U \) is strictly increasing, this does not necessarily mean that \( dU(c^*) > 0 \). If \( U \) is concave and strictly increasing, however, it is always true that \( dU(c^*) > 0 \).

**Corollary.** Suppose \( U \) is concave and differentiable at some \( c^* = e + D' \theta^* > 0 \), with \( q \cdot \theta^* = 0 \). Then \( c^* \) is optimal if and only if \( \lambda dU(c^*) \) is a state-price vector for some scalar \( \lambda > 0 \).

This follows from the sufficiency of the first-order optimality conditions for concave objective functions. The idea is illustrated in Figure 1.2. In that figure, there are only two states, and a state-price vector is a suitably normalized nonzero positive vector orthogonal to the set \( B = \{ D' \theta : q \cdot \theta = 0 \} \) of budget-neutral consumption adjustments. The first-order condition for optimality of \( c^* \) is that movement in any feasible direction away from \( c^* \) has negative or zero marginal utility, which is equivalent to the statement that the budget-neutral set is tangent at \( c^* \) to the preferred set \( \{ c \in \mathbb{R}^S : U(c) \geq U(c^*) \} \), as shown in the figure. This is equivalent to the statement that \( dU(c^*) \) is orthogonal to \( B \), consistent with the last corollary. Figure 1.3 illustrates a strictly suboptimal consumption choice \( c \), at which the derivative vector \( dU(c) \) is not co-linear with the state-price vector \( q \).

**C. Optimality and Asset Pricing** 7

**Figure 1.2. First-Order Conditions for Optimal Consumption Choice**

We consider the special case of an expected utility function \( U \), defined by a given vector \( p \) of probabilities and by some \( u : \mathbb{R}_+ \rightarrow \mathbb{R} \) according to \[
U(c) = \mathbb{E}[u(c)] = \sum_{j=1}^S p_j u(c_j). \tag{3}
\]
For \( c > 0 \), if \( u \) is differentiable, then \( dU(c)_j = p_j u'(c_j) \). For this expected utility function, (2) therefore applies if and only if \[ q = \lambda \mathbb{E}[D u'(c^*)], \tag{4}
\] with the obvious notational convention. As we saw in Section B, one can also write (2) or (4), with the "risk-neutral" probability \( \tilde{p}_j = u'(c_j^*) p_j / \mathbb{E}[u'(c^*)] \), in the form
\[ q = \sum_{j=1}^S \tilde{p}_j D_j, \quad 1 \leq i \leq n. \tag{5}
\]

**Figure 1.3. A Strictly Suboptimal Consumption Choice**

**8** 1. Introduction to State Pricing

**D. Efficiency and Complete Markets**

Suppose there are \( m \) agents, defined as in Section C by strictly increasing utility functions \( U_1, \dots, U_m \) and by endowments \( e^1, \dots, e^m \). An equilibrium for the economy \( [(U_i, e^i), D] \) is a collection \( (\theta^1, \dots, \theta^m, q) \) such that, given the security-price vector \( q \), for each agent \( i \), \( \theta^i \) solves \( \sup_{\theta} U_i(e^i + D' \theta) \) subject to \( q \cdot \theta \leq 0 \), and such that \( \sum_{i=1}^m \theta^i = 0 \). The existence of equilibrium is treated in the exercises and in sources cited in the Notes.

With \( \text{span}(D) = \{ D' \theta : \theta \in \mathbb{R}^N \} \) denoting the set of possible portfolio payoffs, markets are complete if \( \text{span}(D) = \mathbb{R}^S \), and are otherwise incomplete.

Let \( e = e^1 + \dots + e^m \) denote the aggregate endowment. A consumption allocation \( (c^1, \dots, c^m) \) in \( (\mathbb{R}^S)^m \) is feasible if \( c^1 + \dots + c^m = e \). A feasible allocation \( (c^1, \dots, c^m) \) is Pareto optimal if there is no feasible allocation \( (\tilde{c}^1, \dots, \tilde{c}^m) \) with \( U_i(\tilde{c}^i) \geq U_i(c^i) \) for all \( i \) and with \( U_i(\tilde{c}^i) > U_i(c^i) \) for some \( i \).

Complete markets and the Pareto optimality of equilibrium allocations are almost equivalent properties of any economy.

**Proposition.** Suppose markets are complete and \( (\theta^1, \dots, \theta^m, q) \) is an equilibrium. Then the associated equilibrium allocation is Pareto optimal.

This is sometimes known as The First Welfare Theorem. The proof, requiring only the strict monotonicity of utilities, is left as an exercise. We have established the sufficiency of complete markets for Pareto optimality. The necessity of complete markets for the Pareto optimality of equilibrium allocations does not always follow. For example, if the initial endowment allocation \( (e^1, \dots, e^m) \) happens by chance to be Pareto optimal, then any equilibrium allocation is also Pareto optimal, regardless of the span of securities. It would be unusual, however, for the initial endowment to be Pareto optimal. Although beyond the scope of this book, it can be shown that with incomplete markets and under natural assumptions on utility, for almost every endowment, the equilibrium allocation is not Pareto optimal.

**E. Optimality and Representative Agents**

Aside from its allocational implications, Pareto optimality is also a convenient property for the purpose of security pricing. In order to see this, consider, for each vector \( \lambda \in \mathbb{R}^m \) of "agent weights," the utility function \( U_\lambda : \mathbb{R}^S \rightarrow \mathbb{R} \) defined by \[
U_\lambda(x) = \sup_{(c^1,\dots,c^m)} \sum_{j=1}^m \lambda_j U_j(c^j) \quad \text{subject to} \quad c^1 + \dots + c^m = x. \tag{6}
\]

**9** E. Optimality and Representative Agents

**Lemma.** Suppose that, for all \( i \), \( U_i \) is concave. An allocation \( (c^1, \dots, c^m) \) that is feasible is Pareto optimal if and only if there is some nonzero \( \lambda \in \mathbb{R}^m \) such that \( (c^1, \dots, c^m) \) solves (6) at \( x = e = e^1 + \dots + e^m \).

*Proof:* Suppose that \( (c^1, \dots, c^m) \) is Pareto optimal. For any allocation \( x \), let \( U(x) = (U_1(x^1), \dots, U_m(x^m)) \). Next, let
\[
\mathcal{U} = \{ U(x) - U(c) - z : x \in \mathcal{M}, z \in \mathbb{R}_+^m \} \subset \mathbb{R}^m,
\] where \( \mathcal{M} \) is the set of feasible allocations. Let \( \mathcal{J} = \{ y \in \mathbb{R}^m : y \neq 0 \} \). Since \( \mathcal{U} \) is convex (by the concavity of utility functions) and \( \mathcal{U} \cap \mathcal{J} \) is empty (by Pareto optimality), the Separating Hyperplane Theorem (Appendix B) implies that there is a nonzero vector \( \lambda \) in \( \mathbb{R}^m \) such that \( \lambda \cdot y \leq \lambda \cdot z \) for each \( y \) in \( \mathcal{U} \) and each \( z \) in \( \mathcal{J} \). Since \( 0 \in \mathcal{U} \), we know that \( \lambda > 0 \), proving the first part of the result. The second part is easy to show as an exercise. \(\square\)

**Proposition.** Suppose that for all \( i \), \( U_i \) is concave. Suppose that markets are complete and that \( (\theta^1, \dots, \theta^m, q) \) is an equilibrium. Then there exists some nonzero \( \lambda \in \mathbb{R}^m \) such that \( (\theta, q) \) is a (no-trade) equilibrium for the single-agent economy \( [(U_\lambda, e), D] \) defined by (6). Moreover, the equilibrium consumption allocation \( (c^1, \dots, c^m) \) solves the allocation problem (6) at the aggregate endowment. That is, \( U_\lambda(e) = \sum_{i=1}^m \lambda_i U_i(c^i) \).

**Proof:** Since there is an equilibrium, there is no arbitrage, and therefore there is a state-price vector \( \psi \). Since markets are complete, this implies that the problem of any agent \( i \) can be reduced to
\[
\sup_{c \in \mathbb{R}^S} U_i(c) \quad \text{subject to} \quad \psi \cdot c = \psi \cdot e^i.
\]We can assume that ε is not zero, for otherwise c = 0 and agent i can be eliminated from the problem without loss of generality. By the Saddle
Point Theorem of Appendix B, there is a Lagrange multiplier α_i > 0 such that c_i solves the problem

sup ∇U_i(c_i - α_i(p - c_i - p·e_i))

c_i ∈ R^S
(The Slater condition is satisfied since ε is not zero and > 0.) Since
U_i is strictly increasing, α_i > 0. Let A_i = 1/α_i. For any feasible allocation (x^1, ..., x^m), we have

m                          m
∑ A_i U_i(c_i) = ∑ [A_i U_i(c_i) - A_i α_i(p·c_i - p·e_i)] i=1                       i=1

>   ∑ A_i U_i(c_i)
i=1

>   ∑ A_i U_i(x^i).
i=1

This shows that (c^1, ..., c^m) solves the allocation problem (6). We must also show that no trade is optimal for the single agent with utility function U_i and endowment e. If not, there is some x in R^S such that
U_i(x) > U_i(e) and x - x < e - e. By the definition of U_i, this would imply the existence of an allocation (x^1, ..., x^m), not necessarily feasible, such that ∑ A_i U_i(x^i) > ∑ A_i U_i(c^i) and

Var Σ x^i = b - x^s  ... = Σ A_i α_i ... c Putting these two inequalities together, we have
∑ [A_i U_i(x^i) - A_i α_i(p·(x^i - e^i))] > ∑ [A_i U_i(c^i) - A_i α_i(p·(c^i - e^i))] i=1                                     i=1

which contradicts the fact that, for each agent i, (c^i, α_i) is a saddle point for that agent’s problem. ∎

Corollary 1. If, moreover, e >> 0 and D is continuously differentiable at e, then
A can be chosen so that ∇U_i(e) is a state-price vector, meaning

λ = ∇U_i(e). (7)
The differentiability of U_i at e is implied by the differentiability, for some agent i, of U_i at c (See Exercise 10(C).)

Corollary 2. Suppose there is a fixed vector p of state probabilities such that, for all i, U_i(c) = E[u_i(c)] = Σ_j p_j u_i(c_j), for some u_i(·). Then U_i(c) = E[u_i(c)], where, for each y in R^S,

u(y) = max Σ A_i u_i(x^i) subject to x^1 + ... + x^m = y.

In this case, (7) is equivalent to λ = E[∇u_i(e)].

Extensions of this representative-agent asset pricing formula will crop up frequently in later chapters.

# F. State-Price Beta Models

We fix a vector p > 0 in R^S of probabilities for this section, and for any x in R^S we write E(x) = Σ_j p_j x_j. For any x and τ in R^S, we take x ⊗ τ to be the vector (x_1 τ_1, ..., x_S τ_S). The following version of the Riesz
Representation Theorem can be shown as an exercise.

Lemma. Suppose F : R^S → R is linear. Then there is a unique τ in R^S such that, for all x in R^S, we have F(x) = E(x ⊗ τ). Moreover, F is strictly increasing if and only if τ > 0.

Corollary. A dividend-price pair (D, q) admits no arbitrage if and only if there is some τ >> 0 in R^S such that q = E(D ⊗ τ).

Proof: Given a state-price vector γ, let τ = γ / p. Conversely, if τ has the assumed property, then γ = p ⊗ τ defines a state-price vector γ. ∎

Given (D, q), we refer to any vector τ given by this result as a state-price deflator. (The terms state-price density and state-price kernel are often used synonymously with state-price deflator.) For example, the representativeagent pricing model of Corollary 2 of Section E shows that we can take τ = ∇u_i(e_i).

For any x and y in R^S, the covariance cov(x, y) = E(xy) − E(x)E(y) is a measure of covariation between x and y that is useful in asset pricing applications. For any such x and y with var(y) = cov(y, y) ≠ 0, we can always represent x in the form x = a + B y + ε, where B = cov(y, x)/var(y), where cov(y, ε) = E(ε) = 0, and where a is a scalar. This linear regression of x on y is uniquely defined. The coefficient B is called the associated regression coefficient.

Suppose (D, q) admits no arbitrage. For any portfolio θ with q·θ ≠ 0, the return on θ is the vector R^θ in R^S defined by R^θ = (D^T θ) / (q·θ). Fixing a state-price deflator τ, for any such portfolio θ, we have E(τ R^θ) = 1.
Suppose there is a riskless portfolio, meaning some portfolio θ with constant return R^θ. We then call R^θ the riskless return. A bit of algebra shows that for any portfolio θ with a return, we have

cov(R^θ, τ)

E(R^θ) − R^θ = − E(τ)

Thus, covariation with τ has a negative effect on expected return, as one might expect from the interpretation of state prices as shadow prices for wealth.

The correlation between any x and y in R^S is zero if either has zero variance, and is otherwise defined by cov(x, y)

corr(x, y) = √var(x) var(y)

There is always a portfolio θ* solving the problem

sup corr(D^T θ ⊗ τ). (8)
θ

If there is such a portfolio θ* with a return R* having nonzero variance, then it can be shown as an exercise that, for any return R^θ ≠ 0,

E(R^θ) − R^θ = B_θ[E(R*) − R^θ], (9)
where cov(R*, R^θ)
B_θ = ———— var(R*)
If markets are complete, then R* is of course perfectly correlated with the state-price deflator.

Formula (9) is a state-price beta model, showing excess expected returns on portfolios to be proportional to the excess return on a portfolio having maximal correlation with a state-price deflator, where the constant of proportionality is the associated regression coefficient. The formula can be extended to the case in which there is no riskless return.

Another exercise carries this idea, under additional assumptions, to the Capital Asset Pricing Model, or CAPM.

# Exercises

1.1 The dividend-price pair (D, q) of Section A is defined to be weakly arbitrage-free if q·θ > 0 whenever D^T θ > 0. Show that (D, q) is weakly arbitrage-free if and only if there exist (“weak” state prices) γ ∈ R^S such that q = D^T γ. This fact is known as
Farkas’s Lemma.

1.2 Prove the assertion in Section A that (D, q) is arbitrage-free if and only if there exists some τ ∈ R^S, such that q = D^T τ. Instead of following the proof given in Section A, use the following result, sometimes known as the Theorem of the
Alternative.

Stiemke’s Lemma. Suppose A is an m × n matrix. Then one and only one of the following

(a) There exists x in R^n, with Ax = 0.
(b) There exists y in R^m with y^T A > 0.

1.3 Show, for U(c) = E[u(c)] as defined by (3), that (2) is equivalent to (4).

1.4 Prove the existence of an equilibrium as defined in Section D under these assumptions: There exists some portfolio θ with payoff D^T θ > 0 and, for all i, e^i > 0 and U_i is continuous, strictly concave, and strictly increasing. This is a demanding exercise, and calls for the following general result.

Kakutani’s Fixed Point Theorem. Suppose Z is a nonempty convex compact subset of R^n, and for each x in Z, P(x) is a nonempty convex compact subset of Z. Suppose also that
{(x, y) ∈ Z × Z: x ∈ p(y)} is closed. Then there exists x* in Z such that x* ∈ p(x*).

1.5 Prove Proposition D. Hint: The maintained assumption of strict monotonicity of U_i(·) should be used.

1.6 Suppose that the endowment allocation (e^1, ..., e^m) is Pareto optimal.

(A) Show, as claimed in Section D, that any equilibrium allocation is Pareto optimal.

(B) Suppose that there is some portfolio θ with D^T θ > 0 and, for all i, that D is concave and e^i >> 0. Show that (e^1, ..., e^m) is itself an equilibrium allocation.

1.7 Prove Proposition C. Hint: A continuous real-valued function on a compact set has a maximum.

1.8 Prove Corollary 1 of Proposition E.
1.9 Prove Corollary 2 of Proposition E.

1.10 Suppose, in addition to the assumptions of Proposition E, that

(a) e = e^1 + ... + e^m is in R^S;
(b) for all i, U_i is concave and twice continuously differentiable in R^S;
(c) for all i, c^i is in R^S and the Hessian matrix ∇²U_i(c^i), which is negative semi-definite by concavity, is in fact negative definite.

Property (c) can be replaced with the assumption of regular preferences, as defined in a source cited in the Notes.

(A) Show that the assumption that U_i is continuously differentiable at e is justified and, moreover, that for each i there is a scalar γ_i > 0 such that ∇U_i(e) = γ_i ∇U_i(c^i).
(This co-linearity is known as “equal marginal rates of substitution,” a property of any Pareto optimal allocation.) Hint: Use the following:

Implicit Function Theorem. Suppose for given m and n that f : R^m × R^n → R^k is C^1(k times continuously differentiable) for some k > 1. Suppose also that the n x n matrix
∂f(x, y) of partial derivatives of f with respect to its second argument is nonsingular at some (x, y). If f(x, y) = 0, then there exist scalars ε > 0 and δ > 0 and a Cᵏ function
Z: Rⁿ → Rⁿ such that if ||x − x₀|| < ε, then f[x, Z(x)] = 0 and ||Z(x) − y₀|| < δ.

(B) Show that the negative-definite part of condition (c) is satisfied if β >> 0 and, for all i, Uᵢ is an expected utility function of the form Uᵢ(c) = E[uᵢ(c)], where uᵢ is strictly concave with an unbounded derivative on (0, ∞).

(C) Obtain the result of part (A) without assuming the existence of second derivatives of the utilities. (You would therefore not exploit the Hessian matrix or
Implicit Function Theorem.) As the first (and main) step, show the following.
Given a concave function f : Rⁿ → R, the superdifferential of f at some x in Rⁿ is

∂f(x) = {z ∈ Rⁿ: f(y) ≤ f(x) + z·(y − x), ∀ y ∈ Rⁿ}.

For any feasible allocation (c¹, …, cᵐ) and λ ∈ Rₘ satisfying Uᵢ(c) = 0; λᵢUᵢ(cⁱ),

∑ᵢ₌₁ᵐ λᵢ dUᵢ(cⁱ) = ∑ᵢ₌₁ᵐ λᵢ ∇Uᵢ(cⁱ).

1.11 (Binomial Option Pricing). As an application of the results in Section A, consider the following two-state (S = 2) option-pricing problem. There are N = 3 securities:

(a) a stock, with initial price qₛ > 0 and dividend Dₛ₁ = Gqₛ in state 1 and dividend Dₛ₂ = Bqₛ in state 2, where G > B > 0 are the “good” and “bad”
gross returns, respectively;

(b) a riskless bond, with initial price q_b > 0 and dividend D_{b1} = D_{b2} = Rq_b in both states (that is, R is the riskless return and R⁻¹ is the discount);

(c) a call option on the stock, with initial price q_c = C and dividend D_{cj} =
(D_{sj} − K)⁺ = max(D_{sj} − K, 0) for both states j = 1 and j = 2, where
K > 0 is the exercise price of the option. (The call option gives its holder the right, but not the obligation, to pay K for the stock, with dividend, after the state is revealed.)

(A) Show necessary and sufficient conditions on G, B, and R for the absence of arbitrage involving only the stock and bond.

(B) Assuming no arbitrage for the three securities, calculate the call-option price
C explicitly in terms of qₛ, G, R, B, and K. Find the state-price probabilities π₁ and π₂ referred to in Section B in terms of G, B, and R, and show that C = R⁻¹E[D_c], where E denotes expectation with respect to (π₁, π₂).

1.12 (CAPM). In the setting of Section D, suppose (c¹, …, cᵐ) is a strictly positive equilibrium consumption allocation. For any agent i, suppose utility is of the expected-utility form Uᵢ(c) = E[uᵢ(c)]. For any agent i, suppose there are fixed positive constants α and βᵢ such that, for any state j, we have x̄ − α ≤ x and uᵢ(x) = x − βᵢx² for all x ≤ x̄.

(A) In the context of Corollary 2 of Section E, show that uᵢ(e) = k − Ke for some positive constants k and K. From this, derive the CAPM

q = A E[D] − B cov(D, e), (10)

for positive constants A and B, where cov(D, e) ∈ Rⁿ is the vector of covariances between the security dividends and the aggregate endowment.
Suppose for a given portfolio θ that each of the following is well defined:

• the return R_θ = D'θ/q_θ > 0;

• the return R_M on a portfolio M with payoff D'M = e;

• the return R₀ on a portfolio θ⁰ with cov(D'θ⁰, e) = 0;
• β = cov(R_θ, R_M)/var(R_M).

The return R_M is sometimes called the market return. The return R₀ is called the zero-beta return and is the return on a riskless bond if one exists. Prove the “beta”
form of the CAPM

E(R_θ − R₀) = β E(R_M − R₀). (11)

(B) Part (A) relies on the completeness of markets. Without any such assumption, but assuming that the equilibrium allocation (c¹, …, cᵐ) is strictly positive, show that the same beta form (11) applies, provided we extend the definition of the market return R_M to be the return on any portfolio solving

sup corr(R_θ, e). (12)
θ∈ℝⁿ

For complete markets, corr(R_M, e) = 1, so the result of part (A) is a special case.

(C) The CAPM applies essentially as stated without the quadratic expected-utility assumption provided that each agent i is strictly variance-averse, in that Uᵢ(x) > Uᵢ(y)
whenever E(x) = E(y) and var(x) < var(y). Formalize this statement by providing a reasonable set of supporting technical conditions.

We remark that a common alternative formulation of the CAPM allows security portfolios in initial endowments ωⁱ₁, …, ωⁱₙ with ∑ⱼ ωⁱⱼ = 1 for all j. In this case, with the total endowment e redefined by e = ∑ᵢ (D'ωⁱ + eⁱ), the same CAPM (11)
applies. If eⁱ = 0 for all i, then even in incomplete markets, corr(R_M, e) = 1, since
(12) is solved by θ = (1, 1, …, 1). The Notes provide references.

1.13 An Arrow-Debreu equilibrium for [(Uⁱ, eⁱ), D] is a nonzero vector p in Rⁿ and a feasible consumption allocation (c¹, …, cᵐ) such that for each i, cⁱ solves sup_c Uⁱ(c) subject to p · c ≤ p · eⁱ. Suppose that markets are complete, in that span(D) = Rⁿ. Show that (c¹, …, cᵐ) is an Arrow-Debreu consumption allocation if and only if it is an equilibrium consumption allocation in the sense of Section D.

1.14 Suppose (D, q) admits no arbitrage. Show that there is a unique state-price vector if and only if markets are complete.

1.15 (Aggregation). For the “representative-agent” problem (6), suppose for all i that Uᵢ(c) = E[u(c)], where u(c) = cᵞ/γ for some nonzero scalar γ < 1.

(A) Show, for any nonzero agent weight vector λ ∈ Rₘ, that U(c) = E[kcᵞ/γ] for some scalar k > 0 and that (6) is solved by cⁱ = h x for some scalar h > 0 that is nonzero if and only if λᵢ is nonzero.

(B) With this special utility assumption, show that there exists an equilibrium with a Pareto efficient allocation, without the assumption that markets are complete, but with the assumption that eⁱ ∈ span(D) for all i. Calculate the associated equilibrium allocation.

1.16 (State-Price Beta Model). This exercise is to prove and extend the state-price beta model (9) of Section F.

(A) Show problem (8) is solved by any portfolio θ such that T = D'θ + ε, where cov(ε, Dⱼ) = 0 for any security j, where Dⱼ ∈ ℝⁿ is the payoff of security j.

(B) Given a solution θ to (8) such that R_θ is well defined with nonzero variance, prove (9).

(C) Reformulate (9) for the case in which there is no riskless return by redefining
R₀ to be the expected return on any portfolio θ such that R_θ is well defined and cov(R_θ, e) = 0, assuming such a portfolio exists.

1.17 Prove the Riesz representation lemma of Section F. The following hint is perhaps unnecessary in this simple setting but allows the result to be extended to a broad variety of spaces called Hilbert spaces. Given a vector space L, a function
(· | ·): L × L → ℝ is called an inner product for L if, for any x, y, and z in L and any scalar α, we have the five properties:

(a) (x | y) = (y | x)

(b) (x + y | z) = (x | z) + (y | z)

(c) (αx | y) = α(x | y)

(d) (x | x) > 0

(e) (x | x) = 0 if and only if x = 0.

Suppose a finite-dimensional vector space L has an inner product (· | ·). (This defines a special case of a Hilbert space.) Two vectors x and y are defined to be orthogonal if (x | y) = 0. For any linear subspace H of L and any x in L, it can be shown that there is a unique y in H such that (x − y | z) = 0 for all z in H. This vector y is the orthogonal projection in L of x onto H, and solves the problem min_{y∈H} ||x − y||. Let L = ℝⁿ. For any x and y in L, let (x | y) = E[xy]. We must show that given a linear functional F, there is a unique τ with F(x) = (τ | x) for all x.
Let J = {x : F(x) = 0}. If J = L, then F is the zero functional, and the unique representation is τ = 0. If not, there is some z such that F(z) = 1 and (z | x) = 0 for all x in J. Show this using the idea of orthogonal projection. Then show that τ = 2z/(z | z) represents F, using the fact that for any x, we have x − F(x)z ∈ J.

1.18 Suppose there are m = 2 consumers, A and B, with identical utilities for consumption c₁ and c₂ in states 1 and 2 given by U(c₁, c₂) = 0.2√c₁ + 0.5 log c₂.There is a total endowment of e = 25 units of consumption in state 1.

(A) Suppose that markets are complete and that, in a given equilibrium, consumer
A’s consumption is 9 units in state 1 and 10 units in state 2. What is the total endowment in state 2?

(B) Continuing under the assumptions of part (A), suppose there are two securities. The first is a riskless bond paying 10 units of consumption in each state. The second is a risky asset paying 5 units of consumption in state 1 and 10 units in state 2. In equilibrium, what is the ratio of the price of the bond to that of the risky asset?

1.19 There are two states of the world, labeled 1 and 2, two agents, and two securities, both paying units of the consumption numeraire good. The risky security pays a total of 1 unit in state 1 and pays 3 units in state 2. The riskless security pays
1 unit in each state. Each agent is initially endowed with half of the total supply of the risky security. There are no other endowments. (The riskless security is in zero net supply.) The two agents assign equal probabilities to the two states. One of the agents is risk-neutral, with utility function E(c) for state-contingent consumption c, and can consume negatively or positively in both states. The other, risk-averse, agent has utility E(√c) for nonnegative state-contingent consumption. Solve for the equilibrium allocation of the two securities in a competitive equilibrium.

1.20 Consider a setting with two assets A and B, only, both paying off the same random variable X, whose value is nonnegative in every state and nonzero with strictly positive probability. Asset A has price p, while asset B has price q. An arbitrage is then a portfolio (α, β) ∈ ℝ² of the two assets whose total payoff αX + βX is nonnegative and whose initial price αp + βq is strictly negative, or whose total payoff is nonzero with strictly positive probability and always nonnegative, and whose initial price is negative or zero.

(A) Assuming no restrictions on portfolios, and no transactions costs or frictions, state the set of arbitrage-free prices (p, q). (State precisely the appropriate subset of ℝ².)

(B) Assuming no short sales (α ≥ 0 and β ≥ 0), state the set of arbitrage-free prices (p, q).

(C) Now suppose that A and B can be short sold, but that asset A can be short sold only by paying an extra fee of γ > 0 per unit sold short. There are no other

fees of any kind. Provide the obvious new definition of “no arbitrage” in precise mathematical terms, and state the set of arbitrage-free prices.

# Notes

The basic approach of this chapter follows Arrow (1953), taking a general equilibrium perspective originating with Walras (1877). Black (1995) offers a perspective on the general equilibrium approach and a critique of other approaches.

(A) The state-pricing implications of no arbitrage found in Section A originate with Ross (1978).

(B) The idea of “risk-neutral probabilities” apparently originates with Arrow
(1970), a revision of Arrow (1953), and appears as well in Dréze (1971).

(C) This material is standard.

(D) Proposition D is the First Welfare Theorem of Arrow (1951) and Debreu
(1954). The generic inoptimality of incomplete-markets equilibrium allocations can be gleaned from sources cited by Geanakoplos (1990). Indeed, Geanakoplos and Polemarchakis (1986) show that even a reasonable notion of constrained optimality generically fails in certain incomplete-markets settings. See, however,
Kajii (1994) and references cited in the Notes of Chapter 2 for mitigating results.
Mas-Colell (1987) and Werner (1991) also treat constrained optimality.

(E) The “representative-agent” approach goes back, at least, to Negishi (1960).
The existence of a representative agent is no more than an illustrative simplification in this setting, and should not be confused with the more demanding notion of aggregation of Gorman (1953) found in Exercise 15. In Chapter 10, the existence of a representative agent with smooth utility, based on Exercise 1.11, is important for technical reasons.

(F) The “beta model” for pricing goes back, in the case of mean-variance preferences, to the capital asset pricing model, or CAPM, of Sharpe (1964) and
Lintner (1965). The version without a riskless asset is due to Black (1972). Allingham (1991), Berk (1992), Nielsen (1990a), and Nielsen (1990b) address the existence of equilibrium in the CAPM. Characterization of the mean-variance model and two-fund separation is provided by Bottazzi, Hens, and Löffler (1994), Nielsen
(1993b), and Nielsen (1993a). Löffler (1996) provides sufficient conditions for variance aversion in terms of mean-variance preferences.

Additional Topics: Ross (1976) introduced the arbitrage pricing theory, a multifactor model of asset returns that, in terms of expected returns, can be thought of as an extension of the CAPM. In this regard, see also Bray (1994a), Bray (1994b), and Gilles and LeRoy (1991). Balasko and Cass (1986) and Balasko, Cass, and
Siconolfi (1990) treat equilibrium with constrained participation in security trading. See also Hara (1994).

Debreu (1972) provides a notion of regular preferences that substitutes for the existence of a negative-definite Hessian matrix of each agent’s utility function at the equilibrium allocation. For more on regular preferences and the differential approach to general equilibrium, see Mas-Colell (1985) and Balasko (1989).
Kreps (1988) reviews the theory of choice and utility representations of preferences. For Farkas’s and Stiemke’s Lemmas, and other forms of the Theorem of the Alternative, see Gale (1960).

Arrow and Debreu (1954) and, in a slightly different model, McKenzie
(1954) are responsible for a proof of the existence of complete-markets equilibria.
Debreu (1982) surveys the existence problem. Standard introductory treatments of general equilibrium theory are given by Debreu (1959) and Hildenbrand and Kirman (1989). In this setting, with incomplete markets, Polemarchakis and
Siconolfi (1993) address the failure of existence unless one has a portfolio θ with payoff Dθ > 0. Geanakoplos (1990) surveys other literature on the existence of equilibria in incomplete markets, some of which takes the alternative of defining security payoffs in nominal units of account, while allowing consumption

of multiple commodities. Most of the literature allows for an initial period of consumption before the realization of the uncertain state. For a survey, see Magill and Shafer (1991). Additional results on incomplete-markets equilibrium include those of Araujo and Monteiro (1989), Berk (1997), Boyle and Wang (1999), and Weil (1992).

For related results in multiperiod settings, references are cited in the Notes of Chapter 2.

The superdifferentiability result of Exercise 10(C) is due to Skiadas (1995).

Hellwig (1996), Mas-Colell and Monteiro (1996), and Monteiro (1996) have recently shown existence of equilibrium with a continuum of states. Geanakoplos and Polemarchakis (1986) and Chae (1988) show existence in a model closely related to that studied in this chapter. Grodal and Vind (1988) and Yamazaki
(1991) show existence with alternative formulations. With multiple commodities or multiple periods, existence is not guaranteed under any natural conditions, as shown by Hart (1975), who gives a counterexample. For these more delicate cases, the literature on generic existence is cited in the Notes of Chapter 2.

The binomial option-pricing formula of Exercise 1.11 is from an early edition of Sharpe (1985), and is extended in Chapter 2 to a multiperiod setting.
The hint given for the demonstration of the Riesz representation exercise is condensed from the proof given by Luenberger (1969) of the Riesz-Frechet Theorem: For any Hilbert space H with inner product ⟨·|·⟩, any continuous linear functionalF: H → R has a unique T in H such that F(x) = (7 |x), x ∈ H. The Fixed Point Theorem of Exercise 1.4 is from Kakutani (1941).

On the role of default and collateralization, see Geanakoplos and Zame
(1999) and Sabarwal (1999). Gottardi and Kajii (1999) study the role and existence of sunspot equilibria. Pietra (1992) treats indeterminacy. Lobo, Fazel,
Boyd (1999) address portfolio choice with fixed transactions costs.

The Basic Multiperiod Model

THIS CHAPTER EXTENDS the results of Chapter 1 on arbitrage, optimality, and equilibrium to a multiperiod setting. A connection is drawn between state prices and martingales for the purpose of representing security prices. The exercises include the consumption-based capital asset pricing model and the multiperiod “binomial” option pricing model.

A. Uncertainty

As in Chapter 1, there is some finite set, say Ω, of states. In order to handle multiperiod issues, however, we will treat uncertainty a bit more formally as a probability space (Ω, F, P), with 3 denoting the tribe of subsets of Ω that are events (and can therefore be assigned a probability), and with P a probability measure assigning to any event B in 3 its probability
P(B). Those not familiar with the definition of a probability space can consult Appendix A. The terms “σ-algebra” and “σ-field,” among others, are often used in place of the word “tribe.”

There are T + 1 dates: 0,1,..., T. At each of these, a tribe F_t ⊂ F denotes the set of events corresponding to the information available at time t. In effect, an event B in F_t is known at time t to be true or false. (A definition of tribes in terms of “partitions” of Ω is given in Exercise 2.11.)
We adopt the usual convention that F_t ⊂ F_s whenever t < s, meaning that events are never “forgotten.” For simplicity, we also take it that every event in F_0 has probability 0 or 1, meaning roughly that there is no information at time t = 0. Taken altogether, the filtration F = {F_0,..., F_T} represents how information is revealed through time. For any random variable Y, we let E_t(Y) = E(Y |F_t) denote the conditional expectation of Y given F_t.
(Appendix A provides definitions of random variables and of conditional expectation.) An adapted process is a sequence X = {X_0,..., X_T} such that

for each t, X_t is a random variable with respect to (Ω, F_t). Informally, this means that X_t is observable at time t. An adapted process X is a martingale if, for any times t and s > t, we have E_t(X_s) = X_t. As we shall see, martingales are useful in the characterization of security prices. In order to simplify things, for any two random variables Y and Z, we always write “Y = Z” if the probability that Y ≠ Z is zero.

B. Security Markets

A security is a claim to an adapted dividend process, say δ, with δ_t denoting the dividend paid by the security at time t. Each security has an adapted security-price process S, so that S_t is the price of the security, ex dividend, at time t. That is, at each time t the security pays its dividend δ_t and is then available for trade at the price S_t. This convention implies that δ_t plays no role in determining ex-dividend prices. The cum-dividend security price at time t is S_t + δ_t.

Suppose there are N securities defined by the R^N-valued adapted dividend process δ = (δ_1,..., δ_N). These securities have some adapted price process S = (S_1,..., S_N). A trading strategy is an adapted process θ in R^N. Here, θ_t = (θ_1,..., θ_N)_t represents the portfolio held after trading at time t. The dividend process δ^θ generated by a trading strategy θ is defined by

δ_t^θ = δ_t + (S_t + δ_t) · θ_t - S_{t-1} · θ_{t-1}, (1)

with “S_{-1}” taken to be zero by convention.

C. Arbitrage, State Prices, and Martingales

Given a dividend-price pair (δ, S) for N securities, a trading strategy θ is an arbitrage if δ^θ > 0. (The reader should become convinced that this is the same notion of arbitrage defined in Chapter 1.) Let Θ denote the space of trading strategies. For any θ and φ in Θ and scalars α and β we have αδ^θ + βδ^φ = δ^{αθ+βφ}. Thus the marketed subspace M = {δ^θ : θ ∈ Θ} of dividend processes generated by trading strategies is a linear subspace of the space L of adapted processes.

Proposition. There is no arbitrage if and only if there is a strictly increasing linear function F : L → R such that F(δ^θ) = 0 for any trading strategy θ.

Proof: The proof is almost identical to that of Theorem 1A. Let L, =
{x ∈ L : x > 0}. There is no arbitrage if and only if the cone L_+ and

a

the marketed subspace M intersect precisely at zero. Suppose there is no arbitrage. The Separating Hyperplane Theorem, in a form given in
Appendix B for cones, implies the existence of a nonzero linear functional
F such that F(x) < F(y) for each x in M and each nonzero y in L_+. Since
M is a linear subspace, this implies that F(x) = 0 for each x in M, and thus that F(y) > 0 for each nonzero y in L_+. This implies that F is strictly increasing. The converse is immediate. ∎

The following result gives a convenient Riesz representation of a linear function on the space of adapted processes. Proof is left as an exercise, extending the single-period Riesz representation lemma of Section 1F.

Lemma. For each linear function F : L → R, there is a unique γ in L_+ called the Riesz representation of F, such that

F(x) = E(∑_{t=0}^T γ_t x_t), x ∈ L.

If F is strictly increasing, then γ is strictly positive.

For convenience, we call any strictly positive adapted process a deflator.
A deflator γ is a state-price deflator if, for all t,

S_t = E_t(∑_{j=t+1}^T γ_j δ_j / γ_t) (2)

A state-price deflator is variously known in the literature as a state-price density, a pricing kernel, and a marginal-rate-of- substitution process.

For t = T, the right-hand side of (2) is zero, so S_T = 0 whenever there is a state-price deflator. The notion here of a state-price deflator is a natural extension of that of Chapter 1. It can be shown as an exercise that a deflator γ is a state-price deflator if and only if, for any trading strategy θ,

δ_t - S_t = E_t(∑_{j=t+1}^T γ_j δ_j^θ / γ_t), t < T, (3)

meaning roughly that the market value of a trading strategy is, at any time, the state-price discounted expected future dividends generated by the strategy. The cum-dividend value process V^θ of a trading strategy θ is defined by V_t = S_t + δ_t + θ_t · δ_t. If γ is a state-price deflator, we have

V_t = γ_t^{-1} E_t(∑_{j=t}^T γ_j δ_j^θ).

The gain process G for (δ, S) is defined by G_t = S_t + ∑_{j=1}^t δ_j, the price plus accumulated dividend. Given a deflator γ, the deflated gain process G^γ is defined by G_t^γ = γ_t S_t + ∑_{j=1}^t γ_j δ_j. We can think of deflation as a change of numeraire.

Theorem. The dividend-price pair (δ, S) admits no arbitrage if and only if there is a state-price deflator. A deflator γ is a state-price deflator if and only if S_T = 0 and the state-price-deflated gain process G^γ is a martingale.

Proof: It can be shown as an easy exercise that a deflator γ is a state-price deflator if and only if S_T = 0 and the state-price-deflated gain process G^γ is a martingale.

Suppose there is no arbitrage. Then S_T = 0, for otherwise the strategy θ is an arbitrage when defined by θ_t = 0, t < T, θ_T = -S_T. The previous proposition implies that there is some strictly increasing linear function
F : L → R such that F(δ^θ) = 0 for any strategy θ. By the previous lemma, there is some deflator γ such that F(x) = E(∑_t γ_t x_t) for all x in L. This implies that E(∑_t γ_t δ_t^θ) = 0 for any strategy θ.

We must prove (2), or equivalently, that G^γ is a martingale. From
Appendix A, an adapted process X is a martingale if and only if E_s(X_t) =
X_s for any stopping time s < t. Consider, for an arbitrary security n and an arbitrary stopping time s < T, the trading strategy θ defined by θ_k^n = 0 for k ≠ n and θ_k^n = 1, k < s, with θ_k^n = 0, k ≥ s. Since E(∑_t γ_t δ_t^θ) = 0, we have

0 = E(∑_{t=1}^T γ_t δ_t^θ) = E[∑_{t=1}^s γ_t δ_t + γ_s (S_s + δ_s) - γ_{s-1} S_{s-1}], t=1P. For this, we define a new probability measure Q to be equivalent to
P if Q and P assign zero probabilities to the same events. An equivalent probability measure Q is an equivalent martingale measure if

$$E^Q\left[ \frac{S_T}{R_T} \middle| \mathcal{F}_t \right] = \frac{S_t}{R_t}, \quad t < T,$$

where $E^Q$ denotes expectation under $Q$, and likewise $E^Q(x) = E^Q(x|\mathcal{F}_t)$ for any random variable $x$. An equivalent martingale measure is often called a risk-neutral measure.

It is easy to show that $Q$ is an equivalent martingale measure if and only if, for any trading strategy $\theta$,

$$\theta_t' S_t = E^Q\left( \sum_{j=t+1}^T \theta_j' D_j \middle| \mathcal{F}_t \right), \quad t < T. \tag{10}$$

If interest rates are deterministic, (10) is merely the total discounted expected dividends, after substituting $Q$ for the original measure $P$. We will show that the absence of arbitrage is equivalent to the existence of an equivalent martingale measure.

The deflator $\gamma$ defined by $\gamma_t = R_t^{-1}$ defines the discounted gain process $G^{\gamma \prime}$. The word “martingale” in the term “equivalent martingale measure” comes from the following equivalence.

**Lemma.** A probability measure $Q$ equivalent to $P$ is an equivalent martingale measure for $(S, D)$ if and only if $S_t/R_t = 0$ and the discounted gain process $G^{\gamma \prime}$ is a martingale with respect to $Q$.

We already know from Theorem C that the absence of arbitrage is equivalent to the existence of a state-price deflator $\gamma$. As explained in Appendix A, a probability measure $Q$ equivalent to $P$ can be defined in terms of a Radon-Nikodym derivative, a strictly positive random variable $\xi$ with $E(\xi) = 1$, via the definition of expectation with respect to $Q$ given by $E^Q(Z) = E(\xi Z)$, for any random variable $Z$. We will choose a particular equivalent probability measure $Q$ by the Radon-Nikodym derivative $\xi = \xi_T$, where

$$\xi_t = \frac{\gamma_t}{\gamma_0}.$$

(Indeed, one can check that $\xi$ is strictly positive and of expectation 1.) The density process $\xi$ for $Q$ is defined by $\xi_t = E(\xi | \mathcal{F}_t)$. Relation (A.2) of Appendix A implies that for any times $s$ and $t > s$, and any $\mathcal{F}_t$-measurable random variable $Z$,

$$E^Q(Z | \mathcal{F}_s) = \frac{1}{\xi_s} E(\xi Z | \mathcal{F}_s). \tag{11}$$

Fixing some time $t < T$, consider a trading strategy $\theta$ that invests one unit of account at time $t$ and repeatedly rolls the value over in short-term riskless borrowing until time $T$, with final value $R_T$. That is, $\theta_t' S_t = 1$ and $\theta_j = 0$, $j \neq t$. Relation (3) then implies that

$$E^Q\left( \frac{R_T}{R_T} \middle| \mathcal{F}_t \right) = E\left( \xi_T \frac{1}{R_t} \middle| \mathcal{F}_t \right) = \frac{\xi_t}{R_t}$$

so

$$\xi_t = R_t E^Q\left( \frac{R_T}{R_T} \middle| \mathcal{F}_t \right) = R_t.$$

From (11), (12), and the definition of a state-price deflator, (10) is satisfied, so $Q$ is indeed an equivalent martingale measure. We have shown the following result.

**Theorem.** There is no arbitrage if and only if there exists an equivalent martingale measure. Moreover, $\gamma$ is a state-price deflator if and only if an equivalent martingale measure $Q$ has the density process $\xi$ defined by $\xi_t = R_t \gamma_t / \gamma_0$.

**Proposition.** Suppose that $\mathcal{F}_0 = \mathcal{F}$ and there is no arbitrage. Then markets are complete if and only if there is a unique equivalent martingale measure.

*Proof.* Suppose that markets are complete and let $Q_1$ and $Q_2$ be two equivalent martingale measures. We must show that $Q_1 = Q_2$. Let $A$ be any event. Since markets are complete, there is a trading strategy $\theta$ with dividend process $D^\theta$ such that $\theta_t' S_t = \mathbf{1}_A$, and $D^\theta = 0$, $0 < t < T$. By (10), we have $\theta_t' S_t = Q_1(A) = Q_2(A)$. Since $A$ is arbitrary, $Q_1 = Q_2$.

Exercise 2.18 outlines a proof of the converse part of the result.

This martingale approach simplifies many asset pricing problems that might otherwise appear to be quite complex. This approach also applies much more generally than indicated here. For example, the assumption of short-term borrowing is merely a convenience. More generally, as elaborated in Chapter 6, one can typically obtain an equivalent martingale measure after normalizing prices and dividends by the price of some particular security (or trading strategy).

**H. Valuation of Redundant Securities**

Suppose that the given dividend-price pair $(D, S)$ is arbitrage-free, with an associated state-price deflator $\gamma$. Now consider the introduction of a new security with dividend process $D^*$ and price process $S^*$. We say that $D^*$ is redundant given $(D, S)$ if there exists a trading strategy $\theta$, with respect to only the original security dividend-price process $(D, S)$, that replicates $D^*$, in the sense that $\theta_t' D_t = D^*_t$, $t > 1$. In this case, the absence of arbitrage for the

**I. American Exercise Policies and Valuation**

“augmented” dividend-price process $[(D, S), (D^*, S^*)]$ implies that $S_t^* = V_t$, where

$$V_t = \sum_{j=t+1}^T E^Q\left( \frac{D^*_j}{R_j} \middle| \mathcal{F}_t \right), \quad t < T.$$

If this were not the case, there would be an arbitrage, as follows. For example, suppose that for some stopping time $\tau$, we have $S^*_\tau > V_\tau$, and that $\tau < T$ with strictly positive probability. We can then define the strategy:

(a) Sell the redundant security $D^*$ at time $\tau$ for $S^*_\tau$, and hold this position until $T$.
(b) Invest $S^*_\tau$ at time $\tau$ in the replicating strategy $\theta$, and follow this strategy until $T$.

Since the dividends generated by this combined strategy (a)-(b) after $\tau$ are zero, the only dividend is at $\tau$ for the amount $S^*_\tau - V_\tau > 0$, which means that this is an arbitrage. Likewise, if $S^*_\tau < V_\tau$ for some nontrivial stopping time $\tau$, the opposite strategy is an arbitrage. We have shown the following.

**Proposition.** Suppose $(D, S)$ is arbitrage-free with state-price deflator $\gamma$. Let $D^*$ be a redundant dividend process with price process $S^*$. Then the augmented dividend-price pair $[(D, S), (D^*, S^*)]$ is arbitrage-free if and only if it has $\gamma$ as a state-price deflator.

In applications, it is often assumed that $(D, S)$ generates complete markets, in which case any additional security is redundant. Exercise 2.1 gives a classical example in which the redundant security is an option on one of the original securities.

**I. American Exercise Policies and Valuation**

We now extend our pricing framework to include a family of securities, called “American,” for which there is discretion regarding the timing of cash flows.

Given an adapted process $X$, each finite-valued stopping time $\tau$ generates a dividend process $D^{\tau:*}$ defined by $D^{\tau:*} = 0$, $t \neq \tau$, and $D^{\tau:*}_\tau = X_\tau$. In this context, a finite-valued stopping time is an exercise policy, determining the time at which to accept payment. Any exercise policy $\tau$ is constrained by $\tau \leq T$ for some expiration time $T \leq T$. (In what follows, we might take $\tau$ to be a stopping time, which is useful for the case of certain knockout options, as shown for example in Exercise 2.1.) We say that $(X, \tau)$ defines an American security. The exercise policy is selected by the holder of the security. Once exercised, the security has no remaining cash flows. A standard example is an American put option on a security with price process $S$. The American put gives the holder of the option the right, but not the obligation, to sell the underlying security for a fixed exercise price at any time before a given expiration time $\tau$. If the option has an exercise price $K$ and expiration time $\tau < T$, then $X_t = (K - S_t)_+$, $t < \tau$, and $X_t = 0$, $t > \tau$.

We will suppose that, in addition to an American security $(X, \tau)$, there are securities with an arbitrage-free dividend-price process $(D, S)$ that generates complete markets. The assumption of complete markets will dramatically simplify our analysis since it implies, for any exercise policy $\tau$, that the dividend process $D^{\tau:*}$ is redundant given $(D, S)$. For notational convenience, we assume that $\tau < T$.

Let $\gamma$ be a state-price deflator associated with $(D, S)$. From Proposition H, given any exercise policy $\tau$, the American security’s dividend process $D^{\tau:*}$ has an associated cum-dividend price process, say $V'$, which, in the absence of arbitrage, satisfies

$$V_t = \sum_{s=t}^\tau E^Q\left( \frac{X_s}{R_s} \middle| \mathcal{F}_t \right), \quad t < \tau.$$

This value does not depend on which state-price deflator is chosen because, with complete markets, state-price deflators are all equal up to a positive rescaling, as one can see from the theorem and proposition of Section G.

We consider the optimal stopping problem

$$V_0 = \max_{\tau} V_0^\tau, \tag{13}$$where, for any time \( t < \tau \), we let \( \mathcal{T}(t) \) denote the set of stopping times bounded below by \( t \) and above by \( \tau \). A solution to (13) is called a rational exercise policy for the American security \( X \), in the sense that it maximizes the initial arbitrage-free value of the resulting claim.

We claim that in the absence of arbitrage, the actual initial price \( V_0 \)
for the American security must be the “rational value” \( V^*_0 \). In order to see this, suppose first that \( V_0 > V^*_0 \). Then one could buy the American security, adopt for it a rational exercise policy \( \tau \), and also undertake a trading strategy replicating \( X_{\tau^*} \). Since \( V^*_0 = E(\pi_0 X_{\tau^*}) \), this replication involves an initial payoff of \( V^*_0 \), and the net effect is a total initial dividend of \( V_0 - V^*_0 > 0 \) and zero dividends after time 0, which defines an arbitrage.

Thus the absence of arbitrage easily leads to the conclusion that \( V_0 \leq V^*_0 \).
It remains to show that the absence of arbitrage also implies the opposite inequality \( V_0 \geq V^*_0 \).

Suppose that \( V_0 > V^*_0 \). One could sell the American security at time 0 for \( V_0 \). We will show that for an initial investment of \( V^*_0 \), one can “super replicate” the payoff at exercise demanded by the holder of the American security, regardless of the exercise policy used. Specifically, a super-replicating trading strategy for \( (X, \tau, 6, S) \) is a trading strategy \( \theta \) involving only the securities with dividend-price process \( (6, S) \) that has the properties:

(a) \( \theta^6 = 0 \) for \( 0 < t < \tau \), and (b) \( V_t \geq X_t \), for all \( t < \tau \),

where, we recall, \( V_t \) is the cum-dividend value of \( \theta \) at time \( t \). Regardless of the exercise policy \( \tau \) used by the holder of the security, the payment of \( X_\tau \) demanded at time \( \tau \) is dominated by the market value \( V \) of a super-replicating strategy \( \theta \). (In effect, one modifies \( \theta \) by liquidating the portfolio \( \theta_t \) at time \( \tau \), so that the actual trading strategy \( \theta \) associated with the arbitrage is defined by \( \theta_t = 0 \), for \( t < \tau \) and \( \theta_t = 0 \) for \( t > \tau \).) Now, suppose \( \theta \) is super-replicating, with \( V_0 = V^*_0 \). If, indeed, \( V_0 > V^*_0 \), then the strategy of selling the American security and adopting a super-replicating strategy, liquidating at exercise, effectively defines an arbitrage.

This notion of arbitrage for American securities, an extension of the notion of arbitrage used earlier in the chapter, is reasonable because a super-replicating strategy does not depend on the exercise policy adopted by the holder (or sequence of holders over time) of the American security.
It would be unreasonable to call a strategy involving a short position in the American security an “arbitrage” if, in carrying it out, one requires knowledge of the exercise policy for the American security that will be adopted by other agents that hold the security over time, who may after all act “irrationally.”

Proposition. Given \( (X, \tau, 6, S) \), suppose \( (6, S) \) is arbitrage-free and generates complete markets. Then there is a super-replicating trading strategy \( \theta \) for \( (X, \tau, 6, S) \)
with the initial value \( V_0 = V^*_0 \).

In order to construct a super-replicating strategy, we will make a short excursion into the theory of optimal stopping. For any process \( Y \) in \( L \), the Snell envelope \( W \) of \( Y \) is defined by

\[ W = \max_{T \in \mathcal{T}(t)} E_t(Y_\tau)
\]

It can be shown as an exercise that for any \( t < \tau \), \( W_t = \max[Y_t,
E_t(W_{t+1})] \). Thus \( W_t \geq E_t(W_{t+1}) \), implying that \( W \) is a supermartingale. As explained in Appendix A, this implies that we can decompose \( W \) in the form \( W = Z - A \), for some martingale \( Z \) and some increasing adapted process \( A \) with \( A_0 = 0 \). This decomposition is illustrated in Figure 2.1 for the case in which \( Y \) is a deterministic process, which implies that \( W, Z \), and \( A \) are also deterministic.

In order to prove Proposition I, we define \( Y \) by \( Y_t = X_t 1_{\tau=t} \), and let
\( W, Z, \), and \( A \) be defined as above. By the definition of complete markets, there is a trading strategy \( \theta \) with the property that

(a) \( \theta^6_t = 0 \) for \( 0 < t < \tau \);
(b) \( \theta^s_t = Z_t / \pi_t \);
(c) \( \theta^6_\tau = 0 \) for \( t > \tau \).

Property (a) of a super-replicating strategy is satisfied by this strategy \( \theta \).
From the fact that \( Z \) is a martingale and the definition of a state-price deflator, the cum-dividend value \( V \) of the trading strategy \( \theta \) satisfies

\[
\pi_t V_t = E_t(\pi_t V_\tau) = E_t(Z_\tau) = Z_t, \quad t \leq \tau. \quad (14)
\]

From (14) and the fact that \( A_0 = 0 \), we know that \( V_0 = W_0 \) because \( Z_0 =
W_0 = \pi_0 V^*_0 \). Since \( Z_t - A_t = W_t \geq Y_t \) for all \( t \), from (14) we also know that

\[
\pi_t V_t - A_t = \pi_t W_t \geq \pi_t Y_t = \pi_t X_t 1_{\tau=t}, \]

so \( V_t \geq X_t 1_{\tau=t} \), and since \( A_t \geq 0 \) for all \( t \), we have \( V_t \geq X_t \) for all \( t < \tau \). Thus the dominance property (b) is also satisfied, and \( \theta \) is indeed a superreplicating strategy with \( V_0 = V^*_0 \). This proves the proposition and implies that unless there is an arbitrage, the initial price \( V_0 \) of the American security is equal to the market value \( V^*_0 \) associated with a rational exercise policy.

The Snell envelope \( W \) is also the key to finding a rational exercise policy. As for the deterministic case illustrated in Figure 2.1, a rational exercise policy is given by \( \tau^0 = \min\{t : W_t = Y_t\} \). We now show the optimality of \( \tau^0 \). First, we know that if \( \tau \) is a rational exercise policy, then
\( W_\tau = Y_\tau \). (This can be seen from the fact that \( W_t \geq Y_t \), and if \( W_t > Y_t \), then \( \tau \) cannot be rational.) From this fact, any rational exercise policy \( \tau \)
has the property that \( \tau \geq \tau^0 \). For any such \( \tau \), we have

\[ E_0[W(\tau)] \leq W(\tau^0) = Y(\tau^0), \]

and the law of iterated expectations implies that \( E[Y(\tau)] = E[Y(\tau^0)] \), so \( \tau^0 \) is rational.

We have shown the following.

Theorem. Given \( (X, \tau, 6, S) \), suppose \( (6, S) \) generates complete markets. Suppose there is a state-price deflator \( \pi \) for \( (6, S) \), and let \( W \) be the Snell envelope of \( Y \)
up to the expiration time \( \tau \). Then a rational exercise policy for \( (X, \tau, 6, S) \) is given by \( \tau^0 = \min\{t : W_t = Y_t\} \). The unique initial cum-dividend arbitrage-free price of the American security is

\[ V_0 = \pi_0^{-1} W_0.
\]

J. Is Early Exercise Optimal?

With the equivalent martingale measure \( Q \) defined in Section G, we can also write the optimal stopping problem (13) in the form

\[
V_0 = \max_{\tau \in \mathcal{T}(0)} E^Q[ X_\tau ]. \quad (15)
\]

This representation of the rational exercise problem is sometimes convenient. For example, let us consider the case of an American call option on a security with price process \( p \). We have \( X_t = (p_t - K)^+ \) for some exercise price \( K \). Suppose the underlying security has no dividends before or at the expiration time \( \tau \). We suppose positive interest rates, meaning that
\( R_{t,s} > 1 \) for all \( t \) and \( s > t \). With these assumptions, we will show that it is never optimal to exercise the call option before its expiration date \( \tau \).

This property is sometimes called “no early exercise,” or “better alive than dead.”

We define the “discounted price process” \( p^* \) by \( p^*_t = p_t / R_{0,t} \). The fact that the underlying security pays dividends only after the expiration time \( \tau \) implies, by Lemma G, that \( p^* \) is a \( Q \)-martingale at least up to the expiration time \( \tau \). That is, for \( t < s < \tau \), we have \( E^Q(p^*_s) = p^*_t \).

Jensen’s Inequality can be used to show the following fact about convex functions of martingales, which we will use to obtain conditions for the no-early-exercise result.

Lemma. Suppose \( f : R \times R \to R \) is convex with respect to its first argument, \( Y \)
is a martingale, \( \tau(1) \) and \( \tau(2) \) are two stopping times with \( \tau(2) > \tau(1) \), and \( Z \)
is an adapted process. Then \( f(Y_{\tau(1)}, Z_{\tau(1)}) \leq E^Q[f(Y_{\tau(2)}, Z_{\tau(2)})] \). Moreover, the law of iterated expectations implies that \( E^Q[f(Y_{\tau(2)}, Z_{\tau(2)})] \leq E^Q[f(Y_{\tau}, Z_{\tau})] \).

With the benefit of this lemma and positive interest rates, we have, for any stopping time \( \tau < \tau \),

\[
E^Q[ (p_\tau - K)^+ ] \geq (E^Q[ p_\tau ] - K)^+ = (p_0 - K)^+.
\]

It follows that \( \tau \) is a rational exercise policy. In typical cases, \( \tau \) is the unique rational exercise policy.

If the underlying security pays dividends before expiration, then earlyeliminated). This process of paying or collecting any changes in the futures price, period by period, is called marking to market, and serves in practice to reduce the likelihood or magnitude of potential defaults. Formally, all of this means simply that the dividend process Δ of the futures contract is defined by Δ = Φ − Φ_{t-1}, t > 0.

For our purposes, it is natural to assume that the delivery value Φ is contractually equated with W. (In a more detailed model, we could equate Φ and W by the absence of delivery arbitrage.)

(B) Suppose Q is an equivalent martingale measure and show that for all t < T,
Φ_t = E_Q(Φ_T). It follows from parts (A) and (B) that with deterministic interest rates and the absence of arbitrage, futures and forward prices coincide.

(C) We now suppose that W_t is the market value S_t of a security with dividend process Δ. Suppose that Δ and the discount process d = {d_0,...,d_T} on riskless borrowing are both deterministic. Calculate the futures and forward prices, Φ_t and F_t, explicitly in terms of S_t, d, and Δ.

2.18 Provide details fleshing out the following outline of a proof of the converse part of Proposition G.

Let J = {(x_0,...,x_T): x ∈ ℳ} and H = {(η_0,...,η_T): η ∈ Θ}. Markets are complete if and only if J = H. By Theorem G, there is a unique equivalent martingale measure if and only if there is a unique state-price deflator γ such that γ_0 = 1. Suppose H ≠ J. Since H is a linear subspace of J, there is some nonzero η in J “orthogonal” to H, in the sense that E(η_0 x_0 + ... + η_T x_T) = 0 for all x in H. Let γ ∈ L be defined by γ_0 = 1 and γ_t = γ_{t-1} + α η_t, t > 1, where α > 0 is a scalar small enough that γ > 0. Then γ is a distinct state-price deflator with γ_0 = 1. This shows that if there is a unique state-price deflator γ with γ_0 = 1, then markets must be complete. Hint: Let

γ_t x_t = Σ_{s=t}^T E_t(η_s x_s), h = η define an inner product ( · | · ) for H in the sense of Exercise 1.17.

2.19 It is asserted in Section I that if W is the Snell envelope of Y, then W_t = max[Y_t, E_t(W_{t+1})]. Prove this natural property.

2.20 Prove Lemma J.

2.21 Consider the “tree” of prices for securities A and B shown in Figure 2.2. At each node in the tree, a pair (p_A, p_B) of prices is shown, the first of which is the price of A at that node, the second of which is the price of B.

(A) Construct a probability space (Ω, ℱ, P), a filtration of tribes, {ℱ_0, ℱ_1, ℱ_2}, and a vector security price process V, that formally encode the information in the figure. Please be explicit. Take the security price process to be cum dividend, so that V_2 is both the price and the dividend payoff vector of the securities at time 2.
There are no dividend payments in periods 0 and 1.

(B) Suppose there is no arbitrage. Find the price at time 0 of an American put option on asset B, with an exercise price of 95 and expiring at time 2. (Remember, this is an option to sell B for 95 at any of times 0, 1, or 2.)

(100, 150)

(98, 100)

(100, 75)

(95, 85)
(100, 80)

(100, 90)

(100, 100)
t=0 t=1 t=2

Figure 2.2. An Event Tree With Prices

(C) Suppose the price at time 0 in the market of this put option is in fact 10 percent lower than the arbitrage-free price you arrived at in part B. Show explicitly how to create a riskless profit of 1 million dollars at time 0, with no cash flow after time 0.

(D) Suppose the price in the market of this put option is in fact 10 percent higher than the arbitrage-free price you arrived at in part B. Show explicitly how to create a riskless profit of 1 million dollars at time 0, with nonnegative cash flow after time
0. Hint: If you decide to sell the option, you should not assume that the person to whom you sold it will exercise it in any particular fashion.

2.22 Let T=1, and suppose there are three equally likely states of world, ω_1, ω_2, and ω_3, one of which is revealed as true at time 1. A particular agent has utility function U and has equilibrium consumption choices c_0 = 25 and

c_1(ω_1) = 9, c_1(ω_2) = 16, c_1(ω_3) = 4.

In each case below, compute the price of a security that pays 3 in state ω_1, 6 in state ω_2, and 5 in state ω_3. Show your work.

(A) Expected, but not time-additive, utility U(c_0, c_1) = E[u(c_0, c_1)], with u(x, y) = xy.

(B) Nonexpected utility U(c_0, c_1) = v(c_0) + Σ_{i=1}^3 π_i u(c_1(ω_i)).

2.23 For concreteness, the length of one period is one year. There are two basic types of investments. The first is riskless borrowing or lending. The equilibrium

one-year short rate is 25 percent (simple interest per year), each year. (So one can invest 1 at time zero and collect 1.25 at the end of the first year, or invest 1 at the end of the first year and collect 1.25 at the end of the second year.) At the end of each year, a fair coin is flipped. A risky security has zero initial market value.
Its market value goes up by one unit at the end of each year if the outcome of the coin flip for that year is heads. Its market value goes down by one unit at the end of each year if the outcome of the coin flip for that year is tails. For example, the price of the risky security at the end of the second year is −2, 0, or +2, with respective probabilities 0.25, 0.50, and 0.25.

There is also a European option to purchase the risky security above at the end of the second year (only) at an exercise price of 1 unit of account.

(A) Suppose there is no arbitrage. State the initial market price q of the option.
(Show your reasoning.)

(B) Now suppose the option is actually selling for q/2. Construct a trading strategy that generates a net initial positive cash flow of 1000 units of account and no subsequent cash flows. (State a precise recipe for the quantities of each security to buy or sell, at each time, in each contingency.)

2.24 Prove Corollary F.

2.25 (Numeraire Invariance). Consider a dividend-price pair (Δ, S) ∈ L_+ × L_+, and a deflator γ. Let Δ̂ = Δγ and Ŝ = Sγ denote the deflated price and dividend processes. Let θ be any given trading strategy. Show that the dividend process Δ^θ generated by θ given (Δ, S) and the dividend process Δ̂^θ generated by θ under
(Δ̂, Ŝ) are related by Δ̂^θ = γ Δ^θ. Show that θ is an arbitrage with respect to (Δ, S) if and only if θ is an arbitrage with respect to (Δ̂, Ŝ). If γ is a state-price deflator for
(Δ, S), compute a state-price deflator γ̂ for (Δ̂, Ŝ) in terms of γ and Δ.

# Notes

Radner (1967, 1972) originated the sort of dynamic equilibrium model treated in this chapter. The monograph by Magill and Quinzii (1996b) is a comprehensive survey of the theory of general equilibrium in incomplete markets.

(A-B) The model of uncertainty and information is standard. The model of uncertainty is equivalent to that originated in the general equilibrium model of
Debreu (1953), which appears in Chapter 7 of Debreu (1959). For more details in a finance setting, see Dothan (1990).

(C-D) The connection between arbitrage and martingales given in Sections C and G is from the more general model of Harrison and Kreps (1979). Girotto and Ortu (1996) present general results, in this finite-dimensional setting, on the equivalence between no arbitrage and the existence of an equivalent martingale measure. The spirit of the results on optimality and state prices is also from Harrison and Kreps (1979). Girotto and Ortu (1994, 1997a, 1997b) fully explore this equivalence in finite-dimensional multiperiod economies.

(E) The spirit of this section is from Kreps (1982) and Duffie and Huang (1985).

(F) The representative-agent state-pricing model for this setting was shown by
Constantinides (1982). An extension of this notion to incomplete markets, where one cannot generally exploit Pareto optimality, is given by Cuoco and He (1992a).

(G-H) These sections are based on the ideas of Harrison and Kreps (1979).

(I) The modeling of American security valuation given here is similar to the continuous-time treatments of Bensoussan (1984) and Karatzas (1988), who donot formally connect the valuation of American securities with the absence of arbitrage, but rather deal with the similar notion of “fair price.” Merton (1973b) was the first to attack American option valuation systematically using arbitrage-based methods and to point out the suboptimality of early exercise of certain American options in a Black-Scholes style setting. American option valuation is reconsidered in Chapters 3 and 8, whose literature notes cite many additional references.

(J) These results were developed in a continuous-time setting by Merton (1973b).

Additional Topics: The habit-formation utility model was developed by Dunn and Singleton (1986) and in continuous time by Ryder and Heal (1973). An application of habit formation to state-pricing in this setting appears in Chapman (1998b). The recursive-utility model, in various forms, is due to Selden
(1978), Kreps and Porteus (1978), and Epstein and Zin (1989), and is surveyed by Epstein (1992). Koopmans (1960) presented an early precursor. The recursiveutility model allows for preference for earlier or later resolution of uncertainty
(which have no impact on additive utility). This is relevant, for example, in the context of the remarks by Ross (1989), as shown by Skiadas (1998), and Duffie,
Schroder, and Skiadas (1997). See Grant, Kajii, and Polak (2000) for more on preference for resolution of information. For a more general form of recursive utility than that appearing in Exercise 2.9, the von Neumann-Morgenstern function h can be replaced with a function of the conditional distribution of next-period utility. Examples are the local-expected-utility model of Machina (1982) and the betweenness certainty equivalent model of Chew (1983, 1989), Dekel (1989), and Gul and Lantto (1990). The equilibrium state-price associated with recursive utility is computed in a Markovian version of this setting by Kan (1995). For further justification and properties of recursive utility, see Chew and Epstein (1991), Skiadas
(1998), and Skiadas (1997). For further implications for asset pricing, see Epstein
(1988), Epstein (1992), Epstein and Zin (1999), and Giovannini and Weil (1989).
Kan (1993) explored the utility gradient representation of recursive utility in this setting.

The basic approach to existence given in Exercise 2.11 is suggested by Kreps
(1982), and is shown to work for “generic” dividends and endowments, under technical regularity conditions, in McManus (1984), Repullo (1986), and Magill and Shafer (1990), provided the number of securities is at least as large as the spanning number of the filtration F (as suggested in Exercise 2.11). This literature is reviewed in depth by Geanakoplos (1990). See Duffie and Huang (1985) for

the definition of spanning number in more general settings and for a continuoustime version of a similar result. Duffie and Shafer (1985, 1986b) show generic existence of equilibrium in incomplete markets; Hart (1975) gives a counterexample. Bottazzi (1995) has a somewhat more advanced version of this result in its single-period multiple-commodity version. See also Won (1996a, 1996b). Related existence topics are studied by Bottazzi and Hens (1996), Hens (1991), and Zhou
(1997b). Dispersed expectations, in a temporary-equilibrium variant of the model, is shown to lead to existence by Henrotte (1994) and by Honda (1992). Alternative proofs of existence of equilibrium are given in the two-period version of the model by Geanakoplos and Shafer (1990), Hirsch, Magill, and Mas-Colell (1990), and
Husseini, Lasry, and Magill (1990); and in a T-period version by Florenzano and
Gourdel (1994). If one defines security dividends in nominal terms, rather than in units of consumption, then equilibria always exist under standard technical conditions on preferences and endowments, as shown by Cass (1984), Werner (1985),
Duffie (1987), and Gottardi and Hens (1996), although equilibrium may be indeterminate, as shown by Cass (1989) and Geanakoplos and Mas-Colell (1989). On this point, see also Kydland and Prescott (1991), Mas-Colell (1991), and Cass
(1991). Likewise, one obtains existence in a one-period version of the model provided securities have payoffs in a single commodity (the framework of most of this book), as shown by Chae (1988) and Geanakoplos and Polemarchakis (1986). Surveys of general-equilibrium models in an incomplete-markets setting are given by
Cass (1991), Duffie (1992), Geanakoplos (1990), Magill and Quinzii (1996b), and
Magill and Shafer (1991). In the presence of price-dependent options, existence can be more problematic, as shown by Polemarchakis and Ku (1990), but variants of the formulation will suffice for existence in many cases, as shown by Huang and
Wu (1994) and Krasa and Werner (1991). Detemple and Selden (1991) examine the implications of options for asset pricing in a general equilibrium model with incomplete markets. Bajeux-Besnainou and Rochet (1996) explore the dynamic spanning implications of options. The importance of the timing of information in this setting is described by Berk and Uhlig (1993). Hindy and Huang (1993b)
show the implications of linear collateral constraints on security valuation. Hara
(1993) treats the role of “redundant” securities in the presence of transactions costs.

Hahn (1994, 1999) raises some philosophical issues regarding the possibility of complete markets and efficiency. The Pareto inefficiency of incomplete-markets equilibrium consumption allocations, and notions of constrained efficiency, are discussed by Hart (1975), Kreps (1979) (and references therein), Citanna, Kaji, and Villanacci (1994), Citanna and Villanacci (1993), and Pan (1993, 1995).

The optimality of individual portfolio and consumption choices in incomplete markets in this setting is given a dual interpretation by He and Pagés (1993).
(Girotto and Ortu (1994) offer related remarks.) Methods for computation of equilibrium with incomplete markets are developed by Brown, DeMarzo, and
Eaves (1996a), Brown, DeMarzo, and Eaves (1996b), and DeMarzo and Eaves (1996). See also the notes of Chapter 12.

Kraus and Litzenberger (1975) and Stapleton and Subrahmanyam (1978)
present parametric examples of equilibrium. Hansen and Richard (1987)
explore the state-price beta model in a much more general multiperiod setting.

Ross (1987) and Prisman (1985) show the impact of taxes and transactions costs on the state-pricing model. Hara (1993) discusses the role of redundant securities in the presence of transactions costs. The consumption-based CAPM of
Exercise 2.6 is found, in a different form, in Rubinstein (1976). The aggregation result of Exercise 2.15 is based on Rubinstein (1974a). Rubinstein (1974b) has a detailed treatment of asset pricing results in the setting of this chapter. Rubinstein
(1987) is a useful expository treatment of derivative asset pricing in this setting.

Cox, Ross, and Rubinstein (1979) developed the multiperiod binomial option pricing model analyzed in Exercise 2.1, and further analyzed in terms of convergence to the Black-Scholes formula in Chapter 12.

The role of production is considered by Duffie and Shafer (1986a) and
Naik (1994). The Modigliani-Miller Theorems are reconsidered in this setting by
DeMarzo (1988), Duffie and Shafer (1986a), and Gottardi (1995).

The Dynamic Programming Approach

THIS CHAPTER PRESENTS portfolio choice and asset pricing in the framework of dynamic programming, a technique for solving dynamic optimization problems with a recursive structure. The asset pricing implications go little beyond those of the previous chapter, but there are computational advantages. After introducing the idea of dynamic programming in a deterministic setting, we review the basics of a finite-state Markov chain.
The Bellman equation is shown to characterize optimality in a Markovsetting. The first-order condition for the Bellman equation, often called the “stochastic Euler equation,” is then shown to characterize equilibrium security prices. This is done with additive utility in the main body of the chapter, and extended to more general recursive forms of utility in the exercises. The last sections of the chapter show the computation of arbitrage-free derivative security values in a Markov setting, including an application of Bellman’s equation for optimal stopping to the valuation of American securities such as the American put option. An exercise presents algorithms for the numerical solution of term-structure derivative securities in a simple “binomial” setting.

# A. The Bellman Approach

To get the basic idea, we start in the T-period setting of the previous chapter, with no securities except those permitting short-term riskless borrowing at any time t at the discount dt > 0. The endowment process of a given agent is e. Given a consumption process c, it is convenient to define the agent’s wealth process W° by W0 = 0 and

Wt = Wt-1 + θt-1 · (Sqt - Sqt-1) + dt-1(Wt-1 + et-1 - ct-1). (1)

50 i 3. The Dynamic Programming Approach

Given a utility function U:L→R on the set L of nonnegative adapted processes, the agent’s problem can be rewritten as

sup U(c)

c∈L

subject to (1) and ct = Wt + et. (2)

Dynamic programming is only convenient with special types of utility functions. One example is an additive utility function U, defined by

U(c) = Σ t=0T βt ut(ct), (3)

where βt ∈ [0,1]. In order to keep things simple at first, we take the case in which there is no uncertainty, meaning that Ft = {O, Ω} for all t. The maximum remaining utility at time t is then written, for each w in R, as

Vt(w) = sup Σ τ=tT βτ ut(cτ), c∈L, s.t.
subject to Wt = w, the wealth dynamic (1), and cτ = Wτ + eτ. If there is no budget-feasible consumption choice (because w is excessively negative), we write Vt(w) = −∞.

Clearly Vt(w) = −∞ if w < et, and it is shown as an exercise that Vt(w) = sup (βt ut(w + et) + Vt+1(w + et - ct))
c∈R w ≥ et. The Bellman equation. For each t < T and each w for which there is a solution to (4), let Ct(w) denote a solution, and let Ct(w) be also left as an exercise to show that an optimal consumption policy c is defined inductively by ct = Ct(Wt). From (4), the value function Vt+1 thus summarizes all information regarding the “future” of the problem that is required for choice at time t.

# B. First-Order Bellman Conditions

Throughout this section, we take the additive model (3) and assume in addition that for each t, ut is strictly concave and is differentiable on
(0, ∞). From Exercise 2.2, there exists a unique c* > 0 maximizing ut(c) + βt Vt+1(w + et - c) over c. We assume that c* is strictly positive and associate with w* by (1).

Lemma. For any t, Vt is strictly concave and continuously differentiable at wt, with Vt'(wt) = βt ut'(ct).
Proof is left as Exercise 3.4, which gives a broad hint. The first-order conditions for the Bellman equation (4) then imply, for any t < T, that the one-period discount is

dt = βt ut'(ct) / ut'(ct+1). (5)

The same equation is easily derived from the general characterization of equilibrium security prices given by equation (2.9). More generally, the price λt at time t of a unit riskless bond maturing at any time τ > t is

λt = βtτ ut'(cτ) / ut'(ct), (6)

which, naturally, is the marginal rate of substitution of consumption between the two dates.
The price of any security, in this deterministic setting, can be calculated in terms of the prices {λtu} of zero-coupon bonds.

Πt = dt dt+1 … dt+n-1.

# C. Markov Uncertainty

We take the easiest kind of Markov uncertainty, a time-homogeneous
Markov chain. Let the elements of a fixed set Z = {1,…,k} be known as shocks. For any shocks i and j, let qij ∈ [0,1] be thought of as the probability, for any t that shock j occurs in period t +1 given that shock i occurs in period t. Of course, for each i, qi1 + … + qik = 1. The k x k transition matrix q is thus a complete characterization of transition probabilities. This idea is formalized with the following construction of a probability space and filtration of tribes. It is enough to consider a state of the world as some particular sequence (z0, …, zT) of shocks that might occur. We therefore let Ω = ZT+1 and let F be the set of all subsets of Ω. For each t let Xt : Ω → Z (the random shock at time t) be the random variable defined by Xt(z0, …, zT) = zt. Finally, for each possible initial state i in Z, let Pi be the probability measure on (Ω, F) uniquely defined by the two conditions:

Pi(X0 = i) =1 (7)
and, for all t < T,

Pi(Xt+1 = j | X0, X1, X2, …, Xt) = qij where it = Xt. (8)

52 3. The Dynamic Programming Approach

Relations (7) and (8) mean that under probability measure Pi, X starts at i with probability 1 and has the transition probabilities previously described informally. In particular, (8) means that X = {X0,…,XT} is a Markov process: the conditional distribution of Xt+s given X0, …, Xt depends only on Xt. To complete the formal picture, for each t, we let Ft be the tribe generated by [X0, …, Xt], meaning that the information available at time t is that obtained by observing the shock process X until time t. The following lemma gives the complete flavor of the Markov property.

Lemma. For any time t, let f : ZT-t+1 → R be arbitrary. Then there exists a fixed function g : Z → R such that for any i in Z,

Ei[f(Xt, …, XT) | Ft] = g(Xt),

where Ei denotes expectation under Pi.

# D. Markov Asset Pricing

Taking the particular Markov source of uncertainty described in Section C, we now consider the prices of securities in a single- or representative-agent setting with additive utility of the form (3), where, for all t, ut has a strictly positive continuous derivative on (0, ∞). Suppose, moreover, that for each t, there are functions ft: Z → R+ and gt: Z → R+ such that the dividend is δt = ft(Xt) and the endowment is et = gt(Xt). Then Lemma 3C and the general gradient solution (2.9) for equilibrium security prices imply the following characterization of the equilibrium security price process S.
For each t there is a function St : Z → R+ such that St = St(Xt). In particular, for any initial shock i and any time t < T,

St(i) = Ei [ Σ τ=tT βτ δτ(Xτ) | Xt=i ] / Σ τ=tT βτ uτ'(gτ(Xτ)) / ut'(gt(Xt)), (9)

where T is the state-price deflator given by τ,t = uτ'[gτ(Xτ)] / ut'[gt(Xt)]. This has been called the stochastic Euler equation for security prices.

# E. Security Pricing by Markov Control

We will demonstrate (9) once again, under stronger conditions, using instead Markov dynamic programming methods. Suppose that X is the shock process already described. For notational simplicity, in this section we suppose that the transition matrix q is strictly positive and that,

for all t,

• ut is continuous, strictly concave, increasing, and differentiable on (0, ∞);

• et = gt(Xt) for some gt: Z → R+; and

• δt = ft(Xt) for some ft: Z → R+.

We assume, naturally, that Yt : Z → R+ for t < T, and that there is no arbitrage. We let Θ denote the space of trading strategies and L the space of nonnegative adapted processes (for consumption). For each t < T, consider the value function Vt : Z × R → R defined by

Vt(i, w) = sup Et [ Σ τ=tT βτ uτ(cτ)]
(c,θ)∈L×Θ | i s.t. Wi = w, (10)
subject to

Wi = Wi-1 + ([Y(Xi) + F(Xi)] · θi-1), i = t, …, T, w = z0, (11)

and

cj + δj · P(Xj) < Wj + e(Xj), t ≤ j ≤ T.
One may think of Vt(Xt, ·) as an indirect utility function for wealth at time t, given the current state Xt. The conditional expectation in (10) does not depend on the initial state X0 according to Lemma 3C, so we abuse the notation by simply ignoring the initial state in this sort of expression. For sufficiently negative w, there is no (c, θ) that is feasible for (10), in which case we take Vt(i, w) = −∞. For initial wealth w = 0 and time t = 0, (10)
is equivalent to problem (2.4) with Sj = Yj(Xj) for any time j.

We now define a sequence Vt, …, VT of functions on Z × R intoR that will eventually be shown to coincide with the value functions V_t. We first define V_T = 0. For t < T, we recursively define F_t by the Bellman equation

F_t(i, ω) = sup G_t(δ, ω) subject to c + δ - A(i) ≤ ω g(i), (12)
c, δ ∈ ℝ₊ × ℝ, where

G_t(i, ω) = u(c) + E[ F_{t+1}(X_{t+1}, c - [f_o(X_{t+1}) + f_1(X_{t+1})]) | X_t = i ].

The following technical conditions extend those of Lemma 3B, and have essentially the same proof.

--

**54 3. The Dynamic Programming Approach**

Proposition. For any i in Z and t < T, the function F_t(i, ·): ℝ → ℝ, restricted to its domain of finiteness {ω : F_t(i, ω) > -∞} is strictly concave and increasing.
If (c, δ) solves (12) and c > 0, then F_t(i, ·) is continuously differentiable at ω with derivative F_{t,ω}(i, ω) = u'(c).

It can be shown as an exercise that unless the constraint of (12) is infeasible, a solution to (12) always exists. In this case, for any i, t, and ω, let [C_t(i, ω), D_t(i, ω)] denote a solution. We can then define the associated wealth process W* recursively, for any initial condition ω, by W_T = ω and

W_t = D_t(X_t, W_{t+1}) [ c_t = C_t(X_t, W_{t+1}) + D_t(X_t, W_{t+1}) f_o(X_{t+1}) ].

Let (c*, δ*) be defined, at each t, by c*_t = C_t(X_t, W*_{t+1}) and δ*_t = D_t(X_t, W*_{t+1}).
The fact that (c*, δ*) solves (10) for t = 0 can be shown as follows:
Let (c, δ) be an arbitrary feasible policy. For each t, from the Bellman equation (12),

F_t(X_t, w_t) ≥ u_t(c_t) + E[F_{t+1}(X_{t+1}, c_t - [f_o(X_{t+1}) + f_1(X_{t+1})]) | X_t]
Rearranging this inequality and applying the law of iterated expectations,
E[F_t(X_t, w_t)] - E[F_{t+1}(X_{t+1}, w_{t+1})] ≥ E[u_t(c_t)]. (13)

Adding (13) from t = 0 to t = T shows that V_0(X_0, w_0) = U(c).
Repeating the same calculations for the special policy (c, δ) = (c*, δ*)
allows us to replace the inequality in (13) with an equality, leaving
V_0(X_0, w_0) = U(c*). This shows that U(c*) > U(c) for any feasible (c, δ), meaning that (c*, δ*) indeed solves (10) for t = 0. An optimal policy can thus be captured in feedback-policy form in terms of the functions C_t and D_t, t < T. We also see that for all t < T, F_t = V_t, so V_t inherits the properties of F_t given by the last proposition.

We can now recover the stochastic Euler equation (9) directly from the first-order conditions to (12), rather than from the more general first-order conditions developed in chapter 2 based on the gradient of U.

Theorem. Suppose c* is a strictly positive consumption process and δ* is a trading strategy such that c_t = w_t + e_t - δ_t - s_t. Then (c*, δ*) solves (10) for t = 0 if and only if, for all t < T,

u'(c_t) = E_t [ (δ_{t+1} / S_t) u'(c_{t+1}) ].

**F. Markov Arbitrage-Free Valuation 55**

The theorem follows from the necessity and sufficiency of the first-order conditions for (12), relying on the last proposition for the fact that

F_{t,ω}(X_t, W_{t+1}) = u'(c_t). (14)

In a single-agent model, we define a sequence {S_0, ..., S_T} of securityprice functions to be a single-agent equilibrium if (c, δ) = (e, 0) (no trade) solves (10) for t = 0, w = 0, and any initial shock i.

Corollary. {S_0, ..., S_T} is a single-agent equilibrium if and only if S_0 = 0 and, for all t < T, the stochastic Euler equation (9) is satisfied taking c* = e.

**F. Markov Arbitrage-Free Valuation**

Taking the setting of Markov uncertainty described in Section C, but assuming no particular optimality properties or equilibrium, suppose that security prices and dividends are given, at each t, by functions S_t and h_t on Z into ℝ^k. We also suppose that a state-price deflator π is given by π_t = ψ_t(X_t) for some ψ : Z → (0, ∞). With this, we have, for 0 ≤ t ≤ T,

π_t S_t(X_t) = E_t [ π_{t+1} (h_{t+1}(X_{t+1}) + S_{t+1}(X_{t+1})) ]. (15)

In the special setting of Section E, for example, (9) tells us that we can take ψ(i) = w[g(i)].

Since Z = {1, ..., k} for some integer k, we can abuse the notation by treating any function such as ψ : Z → ℝ interchangeably as a vector in ℝ^k denoted ψ, with ith element ψ(i). Likewise, S_t can be treated as a k × N matrix, and so on. In this sense, (15) can also be written

S_t = Π_t (h_{t+1} + S_{t+1}), (16)

where Π_t is the k × k matrix with (i, j)-element π_{t+1}(j) ψ(i) / π_t(i). For each t and s ≥ t, we let Π_{t,s} = Π_t Π_{t+1} … Π_{s-1}. Then (16) is equivalent to, for any t and τ ≥ t

S_t = Π_{t,τ} S_τ + Σ_{s=t}^{τ-1} Π_{t,s} h_s. (17)

As an example, consider the “binomial” model of Exercise 2.1. We can let Z = {0,1,..., T}, with shock i having the interpretation: “There have

so far occurred i ‘up’ returns on the stock,” as illustrated in Figure 3.1 for the case T = 6.

--

**56 3. The Dynamic Programming Approach**

![A Binomial Tree](image_placeholder)
Figure 3.1. A Binomial Tree

From the calculations in Exercise 2.1, it is apparent that for any t, we may choose Π_t = P, where

P = [ p_ij ] with p_{i,i+1} = p, p_{i,i-1} = 1 - p, = 0, otherwise,

where p = (R - D)/(U - D), for constant coefficients R, U, and D, with
0 < D < R < U. For a given initial stock price x and any i ∈ Z, the stockprice process S of Exercise 2.1 can indeed be represented at each time t by S_t : Z → ℝ, where S_t(i) = x U^i D^{t-i}.

We can recover the “binomial” option-pricing formula (2.16) by noting that the European call option with strike price K and expiration time
T may be treated as a security with dividends only at time T given by the function g : Z → ℝ, with g(i) = [S_T(i) - K]^+. From (17), the arbitragefree value of the option at time t is C_t = Π_{t,T} g, where Π_{t,T} denotes the matrix product. This same valuation formula applies to an arbitrary security paying a dividend at time τ defined by some payoff function g : Z → ℝ.

**G. Early Exercise and Optimal Stopping**

In the general Markov setting of Section F, consider an “American” security, defined by some payoff functions g_t : Z → ℝ, t ∈ {0,..., T}. As explained in Section 2I, the security is a claim to the dividend g_t(X_t)
at any stopping time τ selected by the owner. Expiration of the security at some time τ is handled by defining g_t to be zero for t > τ. Given a

**G. Early Exercise and Optimal Stopping 57**

state-price deflator π defined by π = ψ_t(X_t), as outlined in the previous section, the rational exercise problem (2.13) for the American security, with initial shock i is given by

J_0(i) = max_{τ ∈ J} E_0[ ψ_τ(X_τ) g_τ(X_τ) ], (18)

where J is the set of stopping times bounded by T. As explained in
Section 2I, if the American security is redundant and there is no arbitrage, then J_0(i) is its cum-dividend value at time 0 with initial shock i. The Bellman equation for (18) is

J_t(X_t) = max { g_t(X_t), E_t[ π_{t+1} J_{t+1}(X_{t+1}) / π_t(X_t) ] }. (19)

It is left as an exercise to show that J_t is indeed determined inductively, backward in time from T, by (19) and J_T = g_T. Moreover, as demonstrated in Section 2I, problem (18) is solved by the stopping time

τ = min { t : J_t(X_t) = g_t(X_t) }. (20)

In our alternate notation that treats J_t as a vector in ℝ^k, we can rewrite the Bellman equation (19) in the form

J_t = max ( g_t, Π_t J_{t+1} ), (21)

where, for any x and y in ℝ^k, max(x, y) denotes the vector in ℝ^k that has max(x_i, y_i) as its i-th element.

The Bellman equation (21) leads to a simple recursive solution algorithm for the American put valuation problem of Exercise 2.1. Given an expiration time τ < T and exercise price K, we have J_τ = 0 and

J_t = max [ (K - S_t)^+, Π_t J_{t+1} ], t < τ. (22)

More explicitly: For any t and i ∈ Z

J_t(i) = max [ (K - x U^i D^{t-i})^+, p J_{t+1}(i+1) + (1-p) J_{t+1}(i-1) ], (23)

where S_t(i) = x U^i D^{t-i} and p = (R - D)/(U - D), for constant coefficients R, U, and D, with 0 < D < R < U.

More generally, consider an American security defined by dividend functions h_0, …, h_T and exercise payoff functions g_0, …, g_T. For a given expiration time τ, we have h_t = g_t = 0, t > τ. The owner of the security

--

**58 3. The Dynamic Programming Approach**

chooses a stopping time τ at which to exercise, generating the dividend process d^τ defined by

d^τ_t = h_t(X_t), t < τ, = g_t(X_t), t = τ, = 0, t > τ.

Assuming that d^τ is redundant for any exercise policy τ, the security’s arbitrage-free cum-dividend value is defined recursively by J_τ = 0 and the extension of (21):

J_t = max ( g_t, h_t + Π_t J_{t+1} ). (24)

**Exercises**

3.1 Consider the classical “binomial” model of a price process S developed inwhere A and B are scalars and \(\epsilon_1, \epsilon_2, \dots\) is an i.i.d. sequence of normally distributed random variables with \(E(\epsilon_t) = 0\) and \(\text{var}(\epsilon_t) = \sigma^2\).

(b) \(G(x, \alpha) = \alpha\) for some \(\gamma \in (0, 1)\).

(c) \(J(q, w) = \log(q) + \rho \log(w^{1/\alpha})\) for some \(\alpha \in (0, 1)\).

(d) \(A(v) = e^{\gamma v}\) for \(\gamma > 0\).

Hint: You may wish to conjecture a solution to the value function of the form
\(V_t(x, k) = \Lambda_k(t) \log(k) + \Lambda_x(t) x + \Lambda(t)\), for time-dependent coefficients \(\Lambda_k, \Lambda_x\), and \(\Lambda\). This example is unlikely to satisfy the regularity conditions that you imposed in part (C).

(E) (Term Structure). For the consumption endowment process \(e\) defined by the solution to part (D), return to the setting of part (B), and calculate the price \(A_{t,s}\) at time \(t\) of a pure discount bond paying one unit of consumption at time \(s > t\). Note that \(\alpha\) is a measure of risk tolerance that can be studied independently of the effects of intertemporal substitution in this model, since, for deterministic consumption processes, utility is independent of \(\alpha\), with \(J[q, h(v)] = \log(q) + \rho \log(v)\).

3.10 Show equation (5) directly from equation (2.9).

3.11 (Binomial Term-Structure Algorithms). This exercise asks for a series of numerical solutions of term-structure valuation problems in a setting with binomial changes in short-term interest rates. In the setting of Section F, under the absence of arbitrage, suppose that short-term riskless borrowing is possible at any time \(t\) at the discount \(d_t\). The one-period interest rate at time \(t\) is denoted \(r_t\), and is given by its definition:

\[ 1 = d_t \cdot (1 + r_t)^{-1}.
\]

The underlying shock process \(X\) has the property that either \(X_{t+1} = X_t + 1\) or \(X_{t+1} = X_t\). That is, in each period, the new shock is the old shock plus a 0–1 binomial trial. An example is the binomial stock-option pricing model of Exercise 2.1, which is reconsidered in Section F. As opposed to that example, we do not necessarily assume here that interest rates are constant. Rather, we allow, at each time \(t\), a function \(\rho_t : \mathbb{Z} \rightarrow \mathbb{R}\) such that \(r_t = \rho_t(X_t)\). For simplicity, however, we take it that at any time \(t\) the pricing matrix \(\Pi_t\) defined in Section F is of the form

\[ \pi_{i,j} = \begin{cases}
\frac{p}{1 + r_t} & \text{if } j = i+1, \\ \frac{1-p}{1 + r_t} & \text{if } j = i, \\ 0 & \text{otherwise}, \end{cases}
\]

where \(p \in (0,1)\) is the “risk-neutral” probability that \(X_{t+1} - X_t = 1\). Literally, we suppose that there is an equivalent martingale measure \(Q\), in the sense of chapter 2, under which, for all \(t\) we have

\[ Q[X_{t+1} - X_t = 1 \mid X_0, \dots, X_t] = p.
\]

It may help to imagine the calculation of security prices at the nodes of the “tree” illustrated in Figure 3.1. The horizontal axis indicates the time periods; the vertical axis corresponds to the possible levels of the shock, assuming that \(X_0 = 0\). At each time \(t\) and at each shock level \(i\), the price of a given security at the \((i, t)\)-node of the tree is given by a weighted sum of its value at the two successor nodes \((i+1, t+1)\) and \((i, t+1)\). Specifically,

\[
H(i, t) = \pi_{i,i+1} H(i+1, t+1) + \pi_{i,i} H(i, t+1).
\]

Two typical models for the short rate are obtained by taking \(p = 1/2\) and either

(a) the Ho–Lee model: For each \(t < T\), \(\rho_t(i) = a_t + b_t i\) for some constants \(a_t\), and \(b_t\); or

(b) the Black–Derman–Toy model: For each \(t\), \(\rho_t(i) = a_t \exp(b_t i)\) for some constants \(a_t\), and \(b_t\).

(A) For case (b), the Black–Derman–Toy model, prepare computer code to calculate the arbitrage-free price \(A_{0,t}\) of a zero-coupon bond of any given maturity \(t\), given the coefficients \(a_t\) and \(b_t\) for each \(t\). Prepare an example taking \(b_t = 0.01\) for all \(t\) and \(a_1, a_2, \dots, a_{50}\) such that \(E^Q(r_t) = 0.01\) for all \(t\). (These parameters are of a typical order of magnitude for monthly periods.) Solve for the price \(A_{0,t}\) of a unit zero-coupon riskless bond maturing at time \(t\), for all \(t\) in \(\{1, \dots, 50\}\).

(B) Consider, for any \(i\) and \(t\) the price \(y_t(i)\) at time 0 of a security that pays one unit of account at time \(t\) if and only if \(X_t = i\). Show that \(y\) can be calculated recursively by the “forward” difference equation

\[ y_{t+1}(i) = \frac{1}{2[1 + \rho_t(i)]} \left[ y_t(i) + y_t(i-1) \right], \]

for \(i \geq 1\), and

\[ y_{t+1}(0) = \frac{1}{1 + \rho_t(0)} y_t(0), \]

for \(i = 0\). The initial condition is \(y_0(0) = 1\) and \(y_0(i) = 0\) for \(i > 0\). Knowledge of this “shock-price” function \(y\) is useful. For example, the arbitrage-free price at time 0 of a security that pays the dividend \(f(X_t)\) at time \(t\) (and nothing otherwise) is given by \(\sum_{i=0}^{\infty} y_t(i) f(i)\).

(C) In practice, the coefficients \(a_t\) and \(b_t\) are often fitted to match the initial term structure \(A_{0,1}, \dots, A_{0,T}\), given the “volatility” coefficients \(b_1, \dots, b_T\). The following algorithm has been suggested for this purpose, using the fact that \(A_{0,t} = y_t(0)\).

(a) Let \(y_0(0) = 1\) and let \(t = 1\).

(b) Fixing \(y_{t-1}(\cdot)\) and \(b_t\), let \(A_{0,t}(a_{t-1}) = y_t(0)\), where \(y_t\) is given by the forward difference equation (28). Only the dependence of the \(t\)-maturity zero-coupon bond price \(A_{0,t}(a_{t-1})\) on \(a_{t-1}\) is notationally explicit. Since \(A_{0,t}(a_{t-1})\) is strictly monotone in \(a_{t-1}\), we can solve numerically for that coefficient \(a_{t-1}\) such that \(A_{0,t} = A_{0,t}(a_{t-1})\). (A Newton–Raphson search will suffice.)

(c) Let \(t\) be increased by 1. Return to step (b) if \(t < T\). Otherwise, stop.

Prepare computer code for this algorithm (a)–(b)–(c). Given \(b_t = 0.01\) for all \(t\), solve for \(a_t\) for all \(t\), using the Black–Derman–Toy model, given an initial term structure that is given by \(A_{0,t} = \alpha^t\), where \(\alpha = 0.99\).

(D) Extend your code as necessary to give the price of American call options on coupon bonds of any given maturity. For the coefficients \(a_0, \dots, a_{T-1}\) that you determined from part (C), calculate the initial price of an American option on a bond that pays coupons of 0.013 each period until its maturity at time 20, at which time it pays 1 unit of account in addition to its coupon. The option has an exercise price of 1.00, ex dividend, and expiration at time 10. Do this for the Black–Derman–Toy model only.

**Notes**

(A–B) Bellman’s principle of optimality is due to Bellman (1957). The proof for Lemma 3B that is sketched in Exercise 3.3, on the differentiability of the value function, is from Benveniste and Scheinkman (1979), and easily extends to general state spaces; see, for example, Duffie (1988c) and Stokey and Lucas (1989).

(C) Freedman (1983) covers the theory of Markov chains. For general treatments of dynamic programming in a discrete-time Markov setting, see Bertsekas (1976) and Bertsekas and Shreve (1978).

(D–F) This is a simple finite-horizon version of the Markov asset-pricing models of LeRoy (1973) and Lucas (1978) that are reviewed in Chapter 4. The semi-group pricing approach implicit in (17) is from Duffie and Garman (1991). The “binomial” option pricing model of Section F was developed by William Sharpe and by Cox, Ross, and Rubinstein (1979), and is further explored in Exercise 2.1 and in Chapter 12.

Additional Topics: Exercise 3.9, treating asset pricing with the recursive utility of Exercise 2.9, is extended to the infinite-horizon setting of Epstein and Zin (1989) in Exercise 4.12. See the Notes of Chapter 2 for additional references on recursive utility, and Streufert (1991a, 1991b, 1996) for more on dynamic programming with a recursive-utility function. For additional work on recursive utility and asset pricing in a discrete-time Markov setting, see Kan (1993, 1995) and Ma (1993b, 1994).

The extensive exercise on binomial term-structure models is based almost entirely on Jamshidian (1991c), who emphasizes the connection between the solution \(y\) of the difference equation (28) and state pricing of contingent claims. This connection is reconsidered in Chapters 7 and 12 for continuous-time applications. The two particular term-structure models appearing in this exercise are based, respectively, on Ho and Lee (1986) and Black, Derman, and Toy (1990). The parametric form shown here for the Ho–Lee model is slightly more general than the form actually appearing in Ho and Lee (1986). Most authors take the convention that \(X_{t+1}\) is \(X_t+1\) or \(X_t-1\), which generates a slightly different form for thearbitrary feasible control. For any time \(t\) by the Bellman equation (7)–(9),

\[
F(X_t, W_t) \geq u(c_t) + p E_t[F(X_{t+1}, W_{t+1}) \mid X_t].
\]

Multiplying through by \(p^t\) and rearranging,

\[ p^t F(X_t, W_t) - p^t E_t[F(X_{t+1}, W_{t+1}) \mid X_t] \geq p^t u(c_t). \tag{10}
\]

Taking expectations on each side, and using the law of iterated expectations,

\[
E_t[p^t F(X_t, W_t)] - E_t[p^t E_t[F(X_{t+1}, W_{t+1}) \mid X_t]] = E_t[p^t u(c_t)].
\]

Calculating the sum of this expression from \(t = 0\) to \(t = T\), for any time \(T > 0\), causes telescopic cancellation on the left-hand side, leaving only

\[
E_t[F(X_0, W_0)] - E_t[p^T F(X_T, W_T)] \geq E_t\left[\sum_{t=0}^{T} p^t u(c_t)\right].
\]

Since \(F\) is a bounded function and \(p \in (0,1)\), the limit of the left-hand side as \(T \to \infty\) is \(F(i,w)\). By the Dominated Convergence Theorem (Appendix C), the limit of the right-hand side is \(U(c)\). Thus \(F(i,w) \geq U(c)\). All of the above calculations apply for the given optimal feedback control \((c^*, \theta^*)\), for which we can replace the inequality in (10) with an equality, using the definition of \(C\) and \(\Phi\). This leaves \(F(i,w) = U(c^*)\). It follows, since \((i,w)\) is arbitrary, that \(F\) is indeed the value function and that \((c^*, \theta^*)\) is optimal, in that it solves (2)–(6), proving the result.

# B. Dynamic Programming and Equilibrium

Section A shows the existence of optimal control in feedback form, given by policy functions \(C\) and \(\Phi\) that specify optimal consumption and portfolio choices in terms of the current shock-wealth pair \((i,w)\). In order to characterize an equilibrium by the same approach, we adopt stronger utility conditions for this section. In addition to our standing assumption that \(u\) is strictly increasing, bounded, concave, and continuous, we add the following regularity condition.

Assumption A. The function \(u\) is strictly concave and differentiable on \((0,\infty)\).

We define \(s\) to be a single-agent Markov equilibrium if associated optimal feedback policy functions \(C\) and \(\Phi\) can be chosen so that for any shock \(i\), \(C(i,0) = g(i)\) and \(\Phi(i,0) = 0\). With this, the consumption and security markets always clear if the agent is originally endowed with no wealth beyond that of his or her private endowment. The short-sales restriction on portfolios is superfluous in equilibrium since this short-sales constraint is not binding at the solution \((\underline{\theta},0)\), and since the equilibrium shown (which is the unique equilibrium) does not depend on the particular lower bound \(\underline{\theta}\) chosen. (It is an exercise to verify this fact.) Our main objective is to demonstrate the following characterization of equilibrium.

Proposition. \(s\) is a Markov equilibrium if and only if, for all \(i\),

\[ V_w(i,w) = 1 \quad \text{if } w = w_0, \]
\[
V_w(i,w) = \frac{u'(g(i))}{p E_i[V_w(i', w')]}, \quad \text{if } w > w_0. \tag{11}
\]

The law of iterated expectations implies the following equivalent form of (11), sometimes called the stochastic Euler equation.

Corollary. \(s\) is a Markov equilibrium if and only if, for any time \(t\) and any initial shock \(i\),

\[
V_w(X_t) = E_t\left(p u'[g(X_{t+1})] U_w(X_{t+1}) + f(X_{t+1}) \mid X_t\right). \tag{12}
\]

We will demonstrate these results by exploiting the following two properties of the value function \(V\).

Fact 1. For each \(i\), \(V(i,\cdot) : [w_0,\infty) \to \mathbb{R}\) is increasing and strictly concave.

Fact 2. Fixing \(s\) arbitrarily, let \((C,\Phi)\) be optimal feedback policy functions, as above. Suppose, at a given \(i\) and \(w > w_0\), that \(c = C(i,\Phi) > 0\). Then \(V(i,\cdot)\) is continuously differentiable at \(w\) with derivative \(V_w(i,w) = u'(c)\).

These two facts, proved in a manner similar to their analogues in Chapter 3, imply, from the first-order conditions of the Bellman equation (7) and the fact that \(V\) solves the Bellman equation, that \(C\) and \(\Phi\) can be chosen with \(C(i,0) = g(i)\) and \(\Phi(i,0) = 0\) for all \(i\) if and only if

\[
V_w(i) = \frac{1}{w} E\left(p u'[e(X')] U_w(X') + f(X')\right), \quad \text{if } w > w_0. \tag{13}
\]

Then (13) is equivalent to (11) and (12), proving the proposition and corollary.

# C. Arbitrage and State Prices

We turn away from the special case of Markov uncertainty in order to investigate the implications of lack of arbitrage and of optimality for security prices in an abstract infinite-horizon setting. Suppose \(\Omega\) is a set, \(\mathcal{F}\) is a tribe on \(\Omega\), and, for each nonnegative integer \(t\), \(\mathcal{F}_t\) is a finite subtribe with \(\mathcal{F}_s \subseteq \mathcal{F}_t\) for \(s \geq t\). We also fix a probability measure \(P\) on \((\Omega, \mathcal{F})\). As usual, we assume that \(\mathcal{F}_0\) includes only events of probability 0 or 1. We again denote by \(\mathcal{L}\) the space of bounded adapted processes. There are \(N\) securities; security \(n\) is defined by a dividend process \((\delta_t^n)\) in \(\mathcal{L}\) and has a price process \(S^n\) in \(\mathcal{L}\). A trading strategy is some \(\theta = (\theta^1,\dots,\theta^N) \in \mathcal{L}^N\).

An arbitrage is a trading strategy \(\theta\) with \(\theta_t \geq 0\). If there is no arbitrage, then for any \(T\), there is no \(T\)-period arbitrage, meaning an arbitrage \(\theta\) with \(\theta_t = 0\) for \(t > T\). Fixing \(T\) momentarily, if there is no \(T\)-period arbitrage, then the results of Chapter 2 imply that there is a \(T\)-period state-price deflator, a strictly positive process \(\eta\) in \(\mathcal{L}\) with \(\eta_0 = 1\) such that for any trading strategy \(\theta\) with \(\theta_t = 0\) for \(t > T\), we have \(E(\sum_{t=0}^T \eta_t \theta_t \delta_t) = 0\). Likewise, there is a \((T+1)\)-period state-price deflator \(\eta^{T+1}\). It can be checked that the process \(\eta\) defined by \(\eta_t = \eta_t^T\), \(t < T\), and \(\eta_T = \eta_T^{T+1}\), \(t \geq T\), is also a \((T+1)\)-period state-price deflator. By induction in \(T\), this means that there is a strictly positive adapted process \(\eta\) such that, for any trading strategy \(\theta\) with \(\theta_t = 0\) for all \(t\) larger than some \(T\), we have \(E(\sum_{t=0}^T \eta_t \theta_t \delta_t) = 0\). In particular, \(\eta\) has the property that for any times \(t\) and \(\tau > t\), we have the now-familiar state-pricing relationship

\[
S_t = E_t\left( \sum_{k=0}^{\tau-t-1} \eta_{t+k} \delta_{t+k} + \eta_{\tau-t} S_\tau \right). \tag{14}
\]

Equation (14) even holds when \(\tau\) is a bounded stopping time. Unfortunately, there is no reason (yet) to believe that there is a state-price deflator, a strictly positive adapted process \(\eta\) such that (14) holds for \(\tau\) an unbounded stopping time, or that for any \(t\),

\[
S_t = E_t\left( \sum_{k=0}^\infty \eta_{t+k} \delta_{t+k} \right). \tag{15}
\]

Indeed, the right-hand side of (15) may not even be well defined. We need some restriction on \(\eta\).

We call an adapted process \(x\) mean-summable if \(E(\sum_{t=0}^\infty |x_t|) < \infty\), and let \(\mathcal{L}^*\) denote the space of mean-summable processes. If \(\eta \in \mathcal{L}^*\) and \(c \in \mathcal{L}\), then the Dominated Convergence Theorem (Appendix C) implies that \(E(\sum_{t=0}^\infty c_t)\) is well defined and finite, so \(\mathcal{L}^*\) may be a natural space of candidate state-price deflators if (15) is to work.

# D. Optimality and State Prices

An agent is defined by an endowment process \(e\) in the space \(\mathcal{L}_+\) of nonnegative processes in \(\mathcal{L}\), and by a strictly increasing utility function \(U : \mathcal{L}_+ \to \mathbb{R}\). Given the dividend-price pair \((\delta, S) \in \mathcal{L}^N \times \mathcal{L}^N\), the agent faces the problem

\[
\sup_{\theta} U(e + \theta \cdot \delta). \tag{16}
\]

We say that the utility function \(U\) is \(\mathcal{L}^*\)-smooth at \(c\) if the gradient \(\nabla U(c)\) exists and moreover has a unique Riesz representation \(\tau\) in \(\mathcal{L}^*\) defined by

\[
\nabla U(c; x) = E\left( \sum_{t=0}^\infty \tau_t x_t \right), \]

for any feasible direction \(x\) in \(\mathcal{L}\). (See Appendix B for the definition of the gradient and feasible directions.) For example, suppose that \(U\) is defined by

\[
U(c) = E\left[ \sum_{t=0}^\infty \beta^t u(c_t) \right], \]

where \(u : \mathbb{R}_+ \to \mathbb{R}\) is strictly increasing and continuously differentiable on \((0,\infty)\), and where \(\beta \in (0,1)\). Then, for any \(c\) in \(\mathcal{L}\) that is bounded away from zero, \(U\) is \(\mathcal{L}^*\)-smooth at \(c\), any \(x\) in \(\mathcal{L}\) is a feasible direction at \(c\), and

\[
\nabla U(c; x) = \sum_{t=0}^\infty \beta^t u'(c_t) x_t, \]

implying that the Riesz representation of the utility gradient is in this case the process \(\tau\) defined by \(\tau_t = \beta^t u'(c_t)\).

More generally, we have the following characterization of state-price deflators.

Proposition. Suppose \(c^*\) solves (16), \(c^*\) is bounded away from zero, and \(U\) is \(\mathcal{L}^*\)-smooth at \(c^*\). Then the Riesz representation \(\tau\) of \(\nabla U(c^*)\) is a state-price deflator.

Corollary. Suppose, moreover, that \(U\) is defined by

\[
U(c) = E\left[ \sum_{t=0}^\infty \beta^t u(c_t) \right], \]

where \(\beta \in (0,1)\) and \(u\) has a strictly positive derivative on \((0,\infty)\). Then \(\tau\) defined by \(\tau_t = \beta^t u'(c_t^*)\) is a state-price deflator and, for any time \(t\) and stopping time \(T > t\),

\[
S_t = E_t\left[ \sum_{k=0}^{T-t-1} \beta^k u'(c_{t+k}^*) S_{t+k+1} + \beta^{T-t} u'(c_T^*) S_T \right].
\]

This corollary gives a necessary condition for optimality that, when specialized to the case of equilibrium, recovers the stochastic Euler equation.tion (12) as a necessary condition on equilibrium without relying on
Markov uncertainty or dynamic programming. For sufficiency, we should give conditions under which the stochastic Euler equation implies that S is an equilibrium. For this, we define S to be a single-agent equilibrium if θ = 0 solves (16) given S.

Theorem. Suppose that U is strictly increasing, concave, and L*-smooth at the endowment process e. Suppose that the endowment process e is bounded away from zero. Let T ∈ L^∞ be the Riesz representation of VU(e). It is necessary and sufficient for S to be a single-agent equilibrium that T is a state-price deflator.

The assumption that e is bounded away from zero is automatically satisfied in the Markovian example of Section A. Proof of the theorem is assigned as an exercise.

# E. Method-of-Moments Estimation

Although it is not our main purpose to delve into econometrics, it seems worthwhile to illustrate here why the infinite-horizon setting is useful for empirical modeling.

Suppose, for some integer m > 1, that B ⊂ R^m is a set of parameters. Each b in B corresponds to a different Markov economy with the same state space Z. In particular, the transition matrix q(b) of the Markov process X may vary with b. For instance, we could take a single agent with utility given by a discount factor ρ ∈ (0,1) and a reward function u(x) = x^α/α for α < 1 (with x₀(x) = log x). We could then take m = 2 and b = (ρ, α) ∈ B = (0, ∞) × (−∞, 1). In this example, the transition matrix q(·) does not depend on b.

We fix some b₀ in B, to be thought of as the “true” parameter vector governing the economy. Our goal is to estimate the unknown parameter vector b₀.

For simplicity, we will assume that the transition matrix q(b₀) of X is strictly positive. With this, a result known as the Frobenius-Perron Theorem implies that there is a unique vector π ∈ Δ whose elements sum to 1 with the property that q(b₀)'π = π. Letting q(b₀)^t denote the t-fold product of q(b₀), we see that P(X_t = j | X_0 = i) = [q(b₀)^t]_{ij}, so that q(b₀)^t is the t-period transition matrix. It can be shown that π is given by any row of lim_{t→∞} q(b₀)^t.
Thus, regardless of the initial shock i, lim_{t→∞} P_i(X_t = j) = π_j. Indeed, the convergence to the “steady-state” probability vector π is exponentially fast, in the sense that there is a constant B > 1 such that for any i and t

B^t |π_j − P_i(X_t = j)| > 0. (18)

From this, it follows immediately that for any H : Z → ℝ and any initial condition i ∈ Z, we have E_i[H(X_t)] → ∑_j π_j H(j), and again convergence is exponentially fast. The empirical distribution vector  hat{p}  of X at time T is defined by

hat{p}_i = #{t ≤ T : X_t = i} / T,

where A denotes the number of elements in a finite set A. That is, hat{p}_i is the average fraction of time, up to T, spent in state i. From the law of large numbers for i.i.d. sequences of random variables, it is not hard to show that hat{p}_i converges almost surely to the steady-state distribution vector π_i. Proof of this fact is assigned as Exercise 4.14, which includes a broad

hint. From this, we have the following form of the law of large numbers for Markov chains.

The Strong Law of Large Numbers for Markov Chains. For any H : Z → ℝ, the empirical average (1/T) ∑_{t=1}^T H(X_t) converges almost surely to the steady-state mean ∑_{i∈Z} π_i H(i).

Proof: Since (1/T) ∑_{t=1}^T H(X_t) = ∑_i hat{p}_i H(i), the result follows from the fact that hat{p}_i → π_i almost surely. □

Suppose that there is some integer ℓ ≥ 0 such that for each time t, the econometrician observes at time t + ℓ the data h(Y_t), where Y_t =
(X_t, X_{t+1}, ..., X_{t+ℓ}) and h : Z^{ℓ+1} → ℝ^n. For example, the data could be in the form of security prices, dividends, endowments, or functions of these.
It is easy to check that the strong law of large numbers would apply even if q(b₀) were not strictly positive, provided the t-period transition matrix q(b₀)^t is strictly positive for some t. From this fact, Z also satisfies the strong law of large numbers, since Y can be treated as a Markov process whose
(ℓ+1)-period transition matrix is strictly positive. In particular, for any G :
Z^{ℓ+1} → ℝ the empirical average (1/T) ∑_{t=1}^T G(Y_t) converges almost surely to the corresponding steady-state mean, which is also equal to lim_{t→∞} E^∞[G(Y_t)], a quantity that is independent of the initial shock i.

We now specify some test moment function K : ℝ^n × B → ℝ^M, for some integer M, with the property that for all b, E^∞[K(A(Y_t), b₀)] = 0. For a simple example, we could take the single-agent Markov equilibrium described by the stochastic Euler equation (13), where the utility function is specified as above by the unknown parameter vector b₀ = (ρ₀, α₀). For this example, we can let Y_t = (X_t, X_{t+1}) and let A(Y_t) = (R_{t+1}, e_{t+1}, e_t), where e_t = g(X_t) is the current endowment and R_{t+1} is the ℝ^N-valued return vector defined by

R_{t+1} = [g(X_{t+1}) + ρ X_{t+1}] / [g(X_t) + ρ X_t], for i ∈ {1,...,N}.

With M = N and b = (ρ, α), we can let
K(A(Y_t), b) = ρ R_{t+1} − [e_{t+1}/e_t]^{α−1}. (19)

From (13), we confirm that E^∞[K(Y_t, b₀)] = 0.

We know from the strong law of large numbers that, for each b in B, the empirical average K_T(b) = (1/T) ∑_{t=1}^T K(Y_t, b) converges almost surely to its stationary mean, denoted K_∞(b). By the law of iterated expectations, for any initial state i,

E_i[K(Y_t, b₀)] = E_i[E^∞[K(Y_t, b₀)]] = 0.

From this, we know that K_∞(b₀) = 0 almost surely. A natural estimator of b₀ at time T is then given by a solution hat{b}_T to the problem

min_{b∈B} ||K_T(b)||^2. (20)

Any such sequence {hat{b}_T} of solutions to (20) is called a generalized-method-ofmoments, or GMM, estimator of b₀. Under conditions, one can show that a GMM estimator is consistent, in the sense that hat{b}_T → b₀ almost surely. A sufficient set of technical conditions is as follows.

GMM Regularity Conditions. The parameter set B is compact. For any b in B other than b₀, K_∞(b) ≠ 0. The function K is Lipschitz with respect to b, in the sense that there is a constant k such that, for any y in Z^{ℓ+1} and any b₁ and b₂ in B, we have

‖K(y, b₁) − K(y, b₂)‖ ≤ k ‖b₁ − b₂‖.

Theorem. Under the GMM regularity conditions, a GMM estimator exists and any GMM estimator is consistent.

The proof follows immediately from the following proposition.
Uniform Strong Law of Large Numbers. Under the GMM regularity conditions,

sup_{b∈B} |K_T(b) − K_∞(b)| → 0 — almost surely.

Proof: The following proof is adapted from a source indicated in the
Notes. Without loss of generality for the following arguments, we can take
M = 1. Since B is a compact set and K is Lipschitz with respect to b, for each ε ∈ (0, ∞) there is a finite set B_ε ⊂ B with the following property:
For any b in B, there is some b^0 and b^1 in B_ε satisfying, for all y,

K(y, b^0) ≤ K(y, b) ≤ K(y, b^1), |K(y, b) − K(y, b^0)| < ε. (21)

As is customary, for any sequence {x_n} of numbers, we let

lim_{n→∞} x_n = sup_{n} inf_{m≥n} x_m.

For a given ε > 0, lim_{T→∞} inf [K_T(b) − K_∞(b)] = lim_{T→∞} inf [K_T(b^0) − K_∞(b)]
+ inf [K_∞(b^0) − K_∞(b)]

≥ lim_{T→∞} inf [K_T(b^0) − K_∞(b^0)]

− ε almost surely,

by the strong law of large numbers, (21), and the fact that B_ε is finite. Let
A_ε ⊂ Ω be the event of probability 1 on which this inequality holds, and let A = ∩_ε A_ε. Then A also has probability 1, and on A we have

lim_{T→∞} inf [K_T(b) − K_∞(b)] ≥ 0. (22)
Likewise, by using b in place of b, and −K in place of K, we have

lim_{T→∞} inf [−K_T(b) + K_∞(b)] = 0 almost surely. (23)
□)

The claim follows from (22) and (23). □

The Notes cite sources that prove the consistency of GMM estimators under weaker conditions and analyze the theoretical properties of this estimator. Included in these are technical conditions implying the normality of the limit of the distribution of √T(hat{b}_T − b₀) as well as the form of covariance matrix Ω of this asymptotic distribution. As shown in these references, the efficiency properties of the GMM estimator, in terms of this asymptotic covariance matrix Ω, can be improved by replacing thecriterion function β + || K_t(d) || in (20) with the criterion function β K_t(β) W_t K_t(β), for a particular adapted sequence {W_t} of positive semi-definite “weighting” matrices. Other papers cited in the Notes apply GMM estimators in a financial setting.

# Exercises
4.1 Prove Fact 4A.
4.2 Prove Lemma 4A.

4.8 Prove Proposition 4A.

4.4 Prove Fact 1 of Section B.

4.5 Prove Fact 2 of Section B.

4.6 Show that (13) is necessary and sufficient for optimality of C(i, 0) = g(i) and (i, 0) = 0, that is, for equilibrium.

4.7 Show that (11), (12), and (13) are equivalent.

4.8 Show that the constraint (9), placing a lower bound on portfolios, is not binding in a Markov equilibrium.

4.9 Suppose there is a single security with price process S_t = 1 and with dividend process d satisfying d_t > -1 for all t. The utility function U is defined by (1), where u(x) = x^α / α for α < 1 and α ≠ 0. The endowment process e is given by e_0 = 0, e_t > 1 for t > 1, and e_t = w > 0. Let 𝒫 denote the space of nonnegative adapted processes.
With a nonnegative wealth constraint and no other bounding restrictions, the agent’s problem is modified to

sup U(c)

coh,

subject to W_t > 0, t>0, (24)

where W_0 = w and W_t = (W_{t-1} - e_{t-1})(1 + δ_t), t>1.

(A) Suppose δ_t = ε for all t where ε > -1 is a constant. Provide regularity conditions on α, ρ, and ε under which there exists a solution to (24). Solve for the value function and the optimal consumption control. Hint: Use dynamic programming and conjecture that the value function is of the form V(w) = kw^α / α for some constant k. Solve the Bellman equation explicitly for V, and then show that the
Bellman equation characterizes optimality by showing that V(w) ≥ U(c) for any feasible c, and that V(w) = U(c*), where c* is your candidate control. Note thatA related issue of speculative bubbles is addressed by Gilles and
(1992a, 1992b, 1998), Magill and Quinzii (1996a), and Santos and Woodford
(1995). Kurz (1993, 1997, 1998), Kurz and Beltratti (1996), and Kurz and Motolese
(1999) develop the implications of stationarity and rationality in this setting, proposing a rational-beliefs model that allows individual probability assessments of agents to be restricted only by absence of conflict with long-run empirical data (Ke and Shannon, 1996 gives conditions for determinacy. Hansen and Sargent
(1990) have worked out extensive examples for equilibrium in this setting with quadratic utilities and linear dynamics.

A spate of literature has addressed the issue of asset pricing with heterogeneous agents and incomplete markets, partly spurred by the equity-premium puzzle pointed out by Mehra and Prescott (1985), showing the difference in expected returns between equity and riskless bonds to be far in excess of what one would find from a typical representative-agent model. Bewley (1982)

and Mankiw (1986) have seminal examples of the effects of incomplete markets. The more recent literature includes Acharya and Madan (1993), Aiyagari and Gertler (1991), Calvet (1999), Constantinides and Duffie (1996), Duffie
(1992), Haan (1996), Heaton and Lucas (1996), Judd (1997), Levine and Zame
(1999), Lucas (1994), Marcet and Singleton (1999), Mehrling (1990, 1998),
Sandroni (1995), Scheinkman (1989), Scheinkman and Weiss (1986), Svensson and Werner (1993), Telmer (1993), and Weil (1992). Others have attempted to resolve the perceived equity-premium puzzle by turning to more general utility functions, such as the habit-formation model (see, for example,
Constantinides (1990) and Hansen and Jagannathan (1990)) or the recursive model (see Epstein and Zin (1989, 1991)). For the effect of first-order risk aversion or Knightian uncertainty, see Epstein and Wang (1994). Judd, Kubler, and
Schmedders (1997) and Santos and Vigo (1998) treat the computation of equilibria in this setting. For more on computation of equilibria, see the Notes of Chapters 1, 2, and 12.

Dumas and Luciano (1989) treat optimal portfolio selection with transactions costs in this setting. Cover and Ordentlich (1996) is a recent example of the literature on optimal long-run returns, sometimes called log-optimal growth-rate models.

Barberis, Huang, and Santos (1999) proposed a limited-rationality asset pricing model that stressed the role of investors’ aversion to negative asset returns.

# Continuous-Time Models

Part II is a continuous-time counterpart to Part I. The results are somewhat richer and more delicate than those in Part I, with a greater dependence on mathematical technicalities. It is wiser to focus on the parallels than on these technicalities. Once again, the three basic forces behind the theory are arbitrage, optimality, and equilibrium.

Chapter 5 introduces the continuous-trading model and develops the
Black-Scholes partial differential equation (PDE) for arbitrage-free prices of derivative securities. The Harrison-Kreps model of equivalent martingale measures is presented in Chapter 6 in parallel with the theory of state prices in continuous time. Chapter 7 presents models of the term structure of interest rates, including the Black-Derman-Toy, Vasicek, Cox-IngersollRoss, and Heath-Jarrow-Morton models, as well as extensions. Chapter 8 presents specific classes of derivative securities, such as futures, forwards,
American options, and lookback options. Chapter 8 also introduces models of option pricing with stochastic volatility. Chapter 9 is a summary of optimal continuous-time portfolio choice, using both dynamic programming and an approach involving equivalent martingale measures or state prices.
Chapter 10 is a summary of security pricing in an equilibrium setting.
Included are such well-known models as Breeden’s consumption-based capital asset pricing model and the general equilibrium version of the
Cox-Ingersoll-Ross model of the term structure of interest rates. Chapter
11 treats the valuation of equities and corporate bonds, beginning with
“structural models,” based on the capital structure of the firm and incentives of equity and debt holders, then turning to “reduced-form” models, based on an assumed stochastic arrival intensity of the stopping time defining default. Chapter 12 reviews numerical methods for calculating derivative security prices in a continuous-time setting, including Monte Carlo simulation of a discrete-time approximation of security prices, and finitedifference solution of the associated PDE.

The Black-Scholes Model

THIS CHAPTER PRESENTS the basic Black-Scholes model of arbitrage pricing in continuous time, as well as extensions to a nonparametric multivariate Markov setting. We first introduce the Brownian model of uncertainty and continuous security trading, and then derive partial differential equations for the arbitrage-free prices of derivative securities. The classic example is the Black-Scholes option-pricing formula.
Chapter 6 extends to a non-Markovian setting using more general techniques.

# A. Trading Gains for Brownian Prices

We fix a probability space (Ω, ℱ, P). A process is a measurable function on Ω × [0, ∞) into ℝ. (For a definition of measurability with respect to a product space of this variety, see Appendix C.) The value of a process X at time t is the random variable variously written as X_ω, X(t), or
X(·, t): Ω → ℝ. A standard Brownian motion is a process B defined by the properties:

(a) B₀ = 0 almost surely;

(b) for any times t and s > t, B_s − B_t is normally distributed with mean zero and variance s − t;

(c) for any times t₁, ..., tₙ such that 0 < t₁ < t₂ < ... < tₙ < ∞, the random variables B(t₁), B(t₂) − B(t₁), ..., B(tₙ) − B(tₙ₋₁) are independently distributed; and

(d) for each ω in Ω, the sample path t ↦ B(ω, t) is continuous.

It is a nontrivial fact, whose proof has a colorful history, that the probability space (Ω, ℱ, P) can be constructed so that there exist standard

Brownian motions. By 1900, in perhaps the first scientific work involving
Brownian motion, Louis Bachelier proposed Brownian motion as a model of stock prices. We will follow his lead for the time being and suppose that a given standard Brownian motion B is the price process of a security.
Later we consider more general classes of price processes.

The σ-algebra ℱₜ generated by {B_s: 0 ≤ s ≤ t} is, on intuitive grounds, a reasonable model of the information available at time t for trading the security, since ℱₜ includes every event based on the history of the price process B up to that time. For technical reasons, however, one must be able to assign probabilities to the null sets of Ω, the subsets of events of zero probability. For this reason, we will fix instead the standard filtration
ℱₜ = {ℱₜ: t ≥ 0} of B, with ℱₜ defined as the σ-algebra generated by the union of ℱₜ and the null sets. The probability measure P is also extended by letting P(A) = 0 for any null set A. This completion of the probability space is defined in more detail in Appendix C.

A trading strategy is an adapted process θ specifying at each state ω and time t the number θₜ(ω) of units of the security to hold. If a strategy θ is a constant, say θ, between two dates t and s > t, then the total gain between those two dates is θ(B_s − B_t), the quantity held multiplied by the price change. So long as the strategy is piecewise constant, we would have no difficulty in defining the total gain between any two times. In order to make for a general model of trading gains, a trading strategy θ is required to satisfy ∫_0^T θ_t^2 dt < ∞ almost surely for each T. Let L² denote the space of adapted processes satisfying this integrability restriction. For each θ in L²,there is an adapted process with continuous sample paths, denoted θ dB, that is called the stochastic integral of θ with respect to B. The definition of
∫ θ dB is outlined in Appendix D. The value of the process ∫ θ dB at time
T is usually denoted ∫_0^T θ dB, and represents the total gain generated up to time T by trading the security with price process B according to the trading strategy θ.

An interpretation of ∫_0^T θ dB can be drawn from the discrete-time analogue ∑_{i=0}^{n-1} θ_i Δ_i B, where Δ_i B = B_{i+1} - B_i, that is, the sum (over i)
of the shares held at i multiplied by the change in price between i and i+1. More generally, let Δ^n_i B = B_{i/n} - B_{(i-1)/n}. In a sense that we shall not make precise, ∫_0^T θ dB can be thought of as the limit of ∑_{i=0}^{nT-1} θ_{i/n} Δ^n_i B, as the number n of trading intervals per unit of time goes to infinity. This statement is literally true, for example, if θ has continuous sample paths, taking “limit” to mean limit in probability. The definition of ∫_0^T θ dB as a limit in probability of the discrete-time analogue extends to a larger class

of θ, but not large enough to capture some of the applications in later chapters. The definition of ∫ θ dB given in Appendix D therefore admits any θ in L^2.

The stochastic integral has some of the properties that one would expect from the fact that it is a good model of trading gains. For example, suppose a trading strategy θ is piecewise constant on [0, T] in that, for some stopping times T_0, ..., T_N with 0 = T_0 < T_1 < ... < T_N = T, and for any n, we have θ(t) = θ(T_{n-1}) for all t ∈ [T_{n-1}, T_n). Then

∫_0^T θ dB = ∑_{n=1}^N θ(T_{n-1}) [B(T_n) - B(T_{n-1})]

A second natural property of stochastic integration as a model for trading gains is linearity: For any θ and φ in L^2 and any scalars a and b, the process aθ + bφ is also in L^2, and, for any time T > 0,

∫_0^T (aθ + bφ) dB = a ∫_0^T θ dB + b ∫_0^T φ dB.

# B. Martingale Trading Gains

The properties of standard Brownian motion imply that B is a martingale.
(This follows basically from the property that its increments are independent and of zero expectation.) A process θ is bounded if there is a fixed constant K such that |θ(ω, t)| < K for all (ω, t). For any bounded θ in L^2, the law of iterated expectations and the “martingality” of B imply, for any integer times s and t > s, that E_s(θ_{s+1} Δ^s_t B) = 0. This means that the discrete-time gain process X, defined by X_0 = 0 and X_n = ∑_{i=0}^{n-1} θ_i Δ_i B, is itself a martingale with respect to the discrete-time filtration {F_0, F_1, ...}, an exercise for the reader. The same is also true in continuous time: For any bounded θ in L^2, ∫ θ dB is a martingale. This is natural; it should be impossible to generate an expected profit by trading a security that never experiences an expected price change. If one places no bound or other restriction on θ, however, the expectation of ∫_0^T θ dB may not even exist.
Even if, for each T, ∫_0^T θ dB and its expectation exist, ∫ θ dB need not be a martingale. Indeed, we may not have a reasonable model of trading gains without some restriction on θ, as shown by example in Chapter 6. The following Proposition assists in determining whether the expectation or the

variance of ∫_0^T θ dB is finite, and whether ∫ θ dB is indeed a martingale.
Consider the spaces

L^1 = {θ ∈ L^2: E[∫_0^T |θ| dt] < ∞, T > 0}
L^2 = {θ ∈ L^2: E[∫_0^T θ^2 dt] < ∞, T > 0}.

Of course, L^1 is contained by L^2.

Proposition. If θ is in L^1, then ∫ θ dB is a martingale. If ∫ θ dB is a martingale, then var( ∫_0^T θ dB) = E[ ∫_0^T θ^2 dt]. (1)

A proof of the proposition is cited in the Notes.

C. Ito Prices and Gains

As a model of security-price processes, standard Brownian motion is too restrictive for most purposes. Consider, instead, a process of the form

S_t = x + ∫_0^t μ_s ds + ∫_0^t σ_s dB_s, t > 0, (2)

where x is a real number, σ is in L^2, and μ is in L^1, meaning that μ is an adapted process such that ∫_0^t |μ_s| ds < ∞ almost surely for all t. We call a process S of this form (2) an Ito process. It is common to write (2) in the informal “differential” form

dS_t = μ_t dt + σ_t dB_t; S_0 = x.

One often thinks intuitively of dS_t as the “increment” of S at time t, made up of two parts, the “dt” part and the “dB_t” part. In order to further interpret this differential representation of an Ito process, suppose that μ and σ have continuous sample paths and are in L^2. It is then literally the case that for any time t

lim_{h↓0} E_t[S_{t+h} - S_t] / h = μ_t almost surely (3)

and

lim_{h↓0} var_t[S_{t+h} - S_t] / h = σ_t^2 almost surely, (4)

where the derivatives are taken from the right, and where, for any random variable X with finite variance, var_t(X) = E_t(X^2) - [E_t(X)]^2 is the F_tconditional variance of X. In this sense of (3) and (4), we can interpret μ as the rate of change of the expectation of S_t conditional on information available at time t and likewise interpret σ^2 as the rate of change of the conditional variance of S at time t. One sometimes reads the associated abuses of notation “E_t(dS_t) = μ_t dt” and “var_t(dS_t) = σ_t^2 dt.” Of course, dS_t is not even a random variable, so this sort of characterization is not rigorously justified and is used purely for its intuitive content. We will refer to μ and σ as the drift and diffusion processes of S, respectively. Many authors reserve the term “diffusion” for σ^2 or other related quantities.

For an Ito process S of the form (2), let L(S) denote the space consisting of any adapted process θ with {θ_t μ_t : t > 0} in L^1 and {θ_t σ_t : t > 0} in L^2. For θ in L(S), we define the stochastic integral ∫ θ dS as the Ito process given by

∫_0^T θ dS = ∫_0^T (θ_t μ_t) dt + ∫_0^T (θ_t σ_t) dB_t. (5)

We also refer to ∫ θ dS as the gain process generated by θ, given the price process S. If θ is in L(S) is such that {θ_t σ_t : t > 0} is in L^2 and E[∫_0^T θ_t^2 σ_t^2 dt] <
∞, then we write that θ is in L^2(S). By Proposition 5B, if θ is in L^2(S), then ∫ θ dS is a finite-variance process.

We will have occasion to refer to adapted processes θ and φ that are equal almost everywhere, by which we mean that E(∫_0^∞ |θ_t - φ_t| dt) = 0. In fact, we shall write “θ = φ“ whenever θ = φ almost everywhere. This is a natural convention, for suppose that X and Y are Ito processes with
X_0 = Y_0, and with dX_t = a_t dt + σ_t dB_t and dY_t = b_t dt + ρ_t dB_t. Since stochastic integrals are defined for our purposes as continuous-samplepath processes, it turns out that X_t = Y_t for all t almost surely if and only if a = b almost everywhere and σ = ρ almost everywhere. We call this the unique decomposition property of Ito processes.

D. Ito’s Formula
More than any other result, Ito’s Formula is the basis for explicit solutions

to asset-pricing problems in a continuous-time setting.

Ito's Formula. Suppose X is an Ito process with dX_t = μ_t dt + σ_t dB_t and f:
R^2 → R is twice continuously differentiable. Then the process Y, defined by

Y_t = f(X_t, t), is an Ito process with

dY_t = [ f_t(X_t, t) + μ_t f_x(X_t, t) + \frac{1}{2} σ_t^2 f_{xx}(X_t, t) ] dt + f_x(X_t, t) σ_t dB_t. (6)

A generalization of Ito’s Formula (6) appears later in the chapter.

E. The Black-Scholes Option-Pricing Formula

Consider a security, to be called a stock, with price process S_t = x exp(αt + σ B_t), t > 0, (7)

where x > 0, α, and σ are constants. Such a process, called a geometric
Brownian motion, is often called log-normal because, for any t, log(S_t) = log (x) + αt + σ B_t is normally distributed. Moreover, since X_t = αt + σ B_t =
∫_0^t α ds + ∫_0^t σ dB_s defines an Ito process X with constant drift α and diffusion σ, Ito’s Formula implies that S is an Ito process and that

dS_t = μ_t S_t dt + σ S_t dB_t; S_0 = x,

where μ = α + σ^2 / 2. From (3) and (4), at any time t the rate of change of the conditional mean of S_t is μ S_t, and the rate of change of the conditional variance is σ^2 S_t^2, so that, per dollar invested in this security at time t, one may think of μ as the “instantaneous” expected rate of return, and σ as the “instantaneous” standard deviation of the rate of return. Thissort of characterization abounds in the literature, and one often reads the associated abuses of notation “E(dS_t/S_t) = dt” and “var(dS_t/S_t) = σ² dt.”
The coefficient σ is also known as the volatility of S. In any case, a geometric
Brownian motion is a natural two-parameter model of a security-price process because of these simple interpretations of μ and σ.

Consider a second security, to be called a bond, with the price process B defined by

B = B₀e^{rt}, t > 0, (8)

for some constants B₀ > 0 and r. We have the obvious interpretation of r as the continually compounding interest rate, that is, the exponential rate at which riskless deposits accumulate with interest. Throughout, we will also refer to r as the short rate. Since {r_t : t > 0} is trivially an Itô process, B is also an Itô process with

dB_t = r B_t dt. (9)

We can also view (9) as an ordinary differential equation with initial condition B₀ and solution (8).

We allow any trading strategies a in R^2(S) for the stock and b in R^2(B)
for the bond. Such a trading strategy (a, b) is said to be self-financing if it generates no dividends (either positive or negative), meaning that for all t

a_t S_t + b_t B_t = a_0 S_0 + b_0 B_0 + ∫_0^t a_u dS_u + ∫_0^t b_u dB_u. (10)

The self-financing condition (10) is merely a statement that the current portfolio value (on the left-hand side) is precisely the initial investment plus any trading gains, and therefore that no dividend “inflow” or “outflow” is generated.

Now consider a third security, an option. We begin with the case of a
European call option on the stock, giving its owner the right, but not the obligation, to buy the stock at a given exercise price K on a given exercise date T. The option’s price process Y is as yet unknown except for the fact that Y_T = (S_T — K)^+ = max(S_T — K, 0), which follows from the fact that the option is rationally exercised if and only if S_T > K. (See Exercise 2.1 for a discrete-time analogue.)

Suppose there exists a self-financing trading strategy (a, b) in the stock and bond with a_t S_t + b_t B_t = Y_t for all t. If a_0 S_0 + b_0 B_0 < Y_0, then one could sell the option for Y_0, make an initial investment of a_0 S_0 + b_0 B_0 in the trading strategy (a,b), and at time T liquidate the entire portfolio (−1, a_T, b_T)
of option, stock, and bond with payoff −Y_T + a_T S_T + b_T B_T = 0. The initial profit Y_0 − a_0 S_0 − b_0 B_0 > 0 is thus riskless, so the trading strategy
(−1,a,b) would be an arbitrage. Likewise, if a_0 S_0 + b_0 B_0 > Y_0, the
Strategy (1, −a, −b) is an arbitrage. Thus, if there is no arbitrage, Y_0 = a_0 S_0 + b_0 B_0. The same arguments applied at each date t imply that, in the absence of arbitrage, Y_t = a_t S_t + b_t B_t. A full definition of continuoustime arbitrage is given in Chapter 6, but for now we can proceed without

much ambiguity at this informal level. Our objective now is to show the following.

The Black-Scholes Formula. If there is no arbitrage, then, for all t < T, Y_t = C(S_t, t), where

C(x, t) = x Φ(z) − K e^{−r(T−t)} Φ(z − σ√(T − t)), (11)

with

z = [ log(x/K) + (r + σ²/2)(T − t) ] / [σ√(T − t)], (12)

where Φ is the cumulative standard normal distribution function.

F. Black-Scholes Formula: First Try

We will eventually see many different ways to arrive at the Black-Scholes formula (11). Although not the shortest argument, the following is perhaps the most obvious and constructive. We start by assuming that
Y_t = C(S_t, t), t < T, without knowledge of the function C aside from the assumption that it is twice continuously differentiable on (0, ∞) × [0, T)
(allowing an application of Itô’s Formula). This will lead us to deduce
(11), justifying the assumption and proving the result at the same time.
Based on our assumption that Y_t = C(S_t, t) and Itô’s Formula,

dY_t = C_t(S_t, t) dt + C_x(S_t, t)σS_t dB_t, t < T, (13)
where

C_t(S_t, t) = C_t(S_t, t) + μ S_t C_x(S_t, t) + ½ σ² S_t² C_{xx}(S_t, t).

Now suppose there is a self-financing trading strategy (a, b) with

a_t S_t + b_t B_t = Y_t, t ∈ [0, T], (14)

as outlined in Section E. This assumption will also be justified shortly.
Equations (10) and (14), along with the linearity of stochastic integration, imply that

dY_t = a_t dS_t + b_t dB_t = (a_t μ S_t + b_t r B_t) dt + a_t σ S_t dB_t. (15)

One way to choose the trading strategy (a, b) so that both (13) and (15)
are satisfied is to “match coefficients separately in both dB_t and dt.” In fact, the unique decomposition property of Itô processes explained at the end of Section C implies that this is the only way to ensure that (13) and
(15) are consistent. Specifically, we choose a_t so that the diffusion terms match: a_t σ S_t = C_x(S_t, t) σ S_t. For this, we let a_t = C_x(S_t, t). From (14) and Y_t = C(S_t, t), we then have
C_x(S_t, t) S_t + b_t B_t = C(S_t, t), or b_t = [C(S_t, t) − C_x(S_t, t) S_t] / B_t. (16)

Finally, “matching coefficients in dt” from (13) and (15) leaves, for t < T,

C_t(S_t, t) + μ S_t C_x(S_t, t) + ½ σ² S_t² C_{xx}(S_t, t) = a_t μ S_t + b_t r B_t = 0. (17)

In order for (17) to hold, it is enough that C satisfies the partial differential equation (PDE)

−r C(x, t) + C_t(x, t) + r x C_x(x, t) + ½ σ² x² C_{xx}(x, t) = 0, (18)

for (x, t) ∈ (0, ∞) × [0, T). The fact that Y_T = C(S_T, T) = (S_T — K)^+ supplies the boundary condition:

C(x, T) = (x — K)^+, x ∈ (0, ∞). (19)
By direct calculation of derivatives, one can show as an exercise that (11)
is a solution to (18)–(19). All of this seems to confirm that C(S₀, 0), with
C defined by the Black-Scholes formula (11), is a good candidate for the initial price of the option. In order to make this solid, suppose that Y₀ >
C(S₀, 0), where C is defined by (11). Consider the strategy (−1, a, b) in the option, stock, and bond, with a_t = C_x(S_t, t) and b_t given by (16) for t < T.
We can choose a_0 and b_0 arbitrarily so that (14) is satisfied; this does not affect the self-financing condition (10) because the value of the trading strategy at a single point in time has no effect on the stochastic integral.
(For this, see the implications of equality “almost everywhere” at the end of Section C.) The result is that (a, b) is self-financing by construction and that a_T S_T + b_T B_T = Y_T = (S_T — K)^+. This strategy therefore nets an initial riskless profit of

Y_0 − a_0 S_0 − b_0 B_0 = Y_0 − C(S₀, 0) > 0,

which defines an arbitrage. Likewise, if Y₀ < C(S₀, 0), the trading strategy
(+1, −a, −b) is an arbitrage. Thus, it is indeed a necessary condition for the absence of arbitrage that Y₀ = C(S₀, 0). Sufficiency is a more delicate matter. We will see in Chapter 6 that under mild technical conditions on trading strategies, the Black-Scholes formula for the option price is also sufficient for the absence of arbitrage. One last piece of business is to show that the “option-hedging” strategy (a, b) is such that a is in R^2(S)
and b is in R^2(B). This is true, and is left to show as an exercise.
Transactions costs play havoc with the sort of reasoning just applied.
For example, if brokerage fees are any positive fixed fraction of the market value of stock trades, the stock-trading strategy a constructed above would call for infinite total brokerage fees, since, in effect, the number of shares traded is infinite! This fact and the literature on transactions costs in this setting are reviewed in the Notes of Chapters 6 and 9.

# G. The PDE for Arbitrage-Free Prices

The expression dS_t = μ S_t dt + σ S_t dB_t for the log-normal stock-price process S of Section E is a special case of a stochastic differential equation (SDE) of the form

dS_t = μ(S_t, t) dt + σ(S_t, t) dB_t, S₀ = x, (20)

where μ : R × [0, ∞) → R and σ : R × [0, ∞) → R are given functions.
Under regularity conditions on μ and σ reviewed in Appendix E, there is a unique Itô process S solving (20) for each starting point x in R.
Assuming that such a solution S defines a stock-price process, consider the price process B defined by

B_t = B₀ exp[ ∫_0^t r(S_u, u) du ], (21)

where r : R × [0, ∞) → R is well enough behaved for the existence of the integral in (21). We may view B_t as the market value at time t ofan investment account that is continuously reinvested at the short rate r(S_t, t). This is consistent with a trivial application of Ito’s Formula, which implies that

dB_t = B_t r(S_t, t) dt; B_0 > 0. (22)

Rather than restricting attention to the option payoff Y_T = (S_T - K)^+, consider a derivative security defined by the payoff g = g(S_T) at time T, for some continuous g: R → R. Arguments like those in Section F lead one to formulate the arbitrage-free price process Y of the derivative security as Y_t = C(S_t, t), t ∈ [0, T], where C solves the PDE

- r(x, t)C(x, t) + C_t(x, t) + r(x, t)xC_x(x, t) + ½ σ^2(x, t)^2 C_{xx}(x, t) = 0, (23)
for (x, t) ∈ R × [0, T), with the boundary condition C(x, T) = g(x), x ∈ R. (24)

In order to tie things together, suppose that C solves (23)-(24). If
Y_0 ≠ C(S_0, 0), then an obvious extension of our earlier arguments implies

that there is an arbitrage. (This extension is left as an exercise.) This is true even if C is not twice continuously differentiable, but merely
C^{2,1}(R × [0, T)), meaning that the derivatives C_x, C_t, and C_{xx} exist and are continuous in R × (0, T), and extend continuously to R × [0, T). (Ito’s
Formula also applies to any function in this class.)

This PDE characterization of the arbitrage-free price of derivative securities is useful if there are convenient methods for solving PDEs of the form (23)-(24). Numerical solution techniques are discussed in Chapter 12. One of these techniques is based on a probabilistic representation of solutions given in the next section.

# H. The Feynman-Kac Solution

A potential simplification of the PDE problem (23)-(24) is obtained as follows. For each (x, t) in R × [0, T], let Z^{x,t} be the Ito process defined by Z^{x,t}_t = x, s < t, and

dZ^{x,t}_s = r(Z^{x,t}_s, s) Z^{x,t}_s ds + σ(Z^{x,t}_s, s) Z^{x,t}_s dB_s, s > t (25)

That is, Z^{x,t} starts at x at time t and continues from there by following the SDE (25).

Condition FK. The functions σ, r, and g satisfy one of the technical sufficient conditions given in Appendix E for Feynman-Kac solutions.

The FK (for “Feynman-Kac”) condition is indeed only technical, and limits how quickly the functions σ, r, and g can grow or change. Referring to Appendix E, we have the following solution to the PDE (23)-(24) as an expectation of the discounted payoff of the derivative security, modified by replacing the original price process S with a pseudo-price process Z^{x,t} whose expected rate of return is the riskless interest rate. This is sometimes known as risk-neutral valuation. This is not to say that agents are risk-neutral, but rather that risk-neutrality is (in this setting) without loss of generality for purposes of pricing derivative securities.

The Feynman-Kac Solution. Under Condition FK, if there is no arbitrage, then the derivative security defined by the payoff g(S_T) at time T has the price process Y with Y_t = C(S_t, t), where C is the solution to (23)-(24) given by

C(x, t) = E[exp(- ∫_t^T r(Z^{x,t}_s, s) ds) g(Z^{x,t}_T)], (x, t) ∈ R × [0, T]. (26)

It can be checked as an exercise that (26) recovers the Black-Scholes option-pricing formula (11). Calculating this expectation directly is a simpler way to solve the corresponding PDE (18)-(19) than is the method originally used to discover the Black-Scholes formula. Chapter 12 presents numerical methods for solving (23)-(24), one of which involves Monte
Carlo simulation of the Feynman-Kac solution (26), which bears a close resemblance to the discrete-time equivalent-martingale-measure arbitragefree price representation of Chapter 2. This is more than a coincidence, as we shall see in Chapter 6.

# I. The Multidimensional Case

Suppose that B^1, ..., B^d are d independent standard Brownian motions on a probability space (Ω, F, P). The process B = (B^1, ..., B^d) is known as a standard Brownian motion in R^d. The standard filtration F = {F_t : t ≥ O} of B is defined just as in the one-dimensional case. Given F, the subsets
S^1, S^2, R^1, and R^2 of adapted processes are also as defined in Sections A and B.

In this setting, X is an Ito process if, for some x in R, some μ in S^1, and some σ^1, ..., σ^d in R^2,

X_t = x + ∫_0^t μ_s ds + ∫_0^t Σ_{i=1}^d σ^i_s dB^i_s, t>0. (27)
For convenience, (27) is also written
X_t = x + ∫_0^t μ_s ds + ∫_0^t σ_s dB_s, t > 0, (28)
or in the convenient stochastic differential form dX_t = μ_t dt + σ_t dB_t; X_0 = x. (29)

If X^1, ..., X^N are Ito processes, then we call X = (X^1, ..., X^N) an Ito process in R^N, which can be written

X_t = x + ∫_0^t μ_s ds + ∫_0^t Σ_{j=1}^d σ_{sj} dB^j_s, t>0, (30)

or

dX_t = μ_t dt + σ_t dB_t; X_0 = x ∈ R^N (31)

where μ and σ are valued in R^N and R^{N×d}, respectively. (Here, R^{N×d} denotes the space of real matrices with N rows and d columns.) Ito’s Formula extends as follows.

Ito’s Formula. Suppose X is the Ito process in R^N given by (30) and f is in
C^{2,1}(R^N × [0, ∞)). Then { f(X_t, t) : t ≥ 0} is an Ito process and, for any time t,

df(X_t, t) = (∂_t f + D_μ f)(X_t, t) dt + Σ_{j=1}^d (D_σ f^j)(X_t, t) dB^j_t, where
D_μ f(x) = (∇f)^T μ(x) + ½ tr[σ(x) σ(x)^T ∇^2 f(x)].

Here, ∇f, ∇^2 f, and f_t denote the obvious partial derivatives of f valued in
R^N, R^{N×N}, and R, respectively, and tr(A) denotes the trace of a square matrix A (the sum of its diagonal elements).

If X and Y are real-valued Ito processes with dX_t = μ_X(t) dt + σ_X(t) dB_t and dY_t = μ_Y(t) dt + σ_Y(t) dB_t, then Ito’s Formula (for N = 2)
implies that the product Z = XY is an Ito process, with drift μ_Z given by

μ_Z(t) = X_t μ_Y(t) + Y_t μ_X(t) + σ_X(t) · σ_Y(t). (32)

If μ_X, μ_Y, σ_X, and σ_Y are all in R^2 and have continuous sample paths, then an application of Fubini’s Theorem (Appendix C) implies that d dt Cov_t(X_t, Y_t) = Cov_t(μ_X(t), Y_t) + Cov_t(X_t, μ_Y(t)) + σ_X(t) σ_Y(t)^T almost surely, (33)
where Cov_t(X_t, Y_t) = E_t(X_t Y_t) - E_t(X_t) E_t(Y_t) and where the derivative is taken from the right, extending the intuition developed with (3) and (4).

If X is an Ito process in R^N with dX_t = μ_t dt + σ_t dB_t and θ =
(θ^1, ..., θ^d) is a vector of adapted processes such that θ^j is in S^1 and, for each i, θ^j σ_{ij} is in R^1, then we say that θ is in L^2(X), which implies that

∫_0^T θ_t · dX_t = ∫_0^T θ_t^T μ_t dt + ∫_0^T θ_t^T σ_t dB_t, T>0, 0 0 0

is well defined as an Ito process. If E[(∫_0^T |θ_t^T σ_t|^2 dt)^2] < ∞ and, for each j, θ^j is also in R^1, then we say that θ is in L^2_2(X), which implies that ∫ θ_t · dX_t is a finite-variance process.

Suppose that S = (S^1, ..., S^N) is an Ito process in R^N specifying the prices of N given securities, and that S satisfies the stochastic differential equation

dS_t = μ(S_t, t) dt + σ(S_t, t) dB_t; S_0 = x ∈ R^N, (34)

where μ: R^N × [0, ∞) → R^N and σ: R^N × [0, ∞) → R^{N×d} satisfy enough regularity (conditions are given in Appendix E) for existence and uniqueness of a solution to (34). Let

B_t = B_0 exp[ ∫_0^t r(S_u, u) du], B_0 > 0, (35)

define the price process of a bond, where r: R^N × [0, ∞) → R defines a continuously compounding short rate, sufficiently well behaved that (35)
is a well-defined Ito process. We can also use Ito’s Formula to write

dB_t = B_t r(S_t, t) dt, B_0 > 0. (36)

Finally, let some continuous g: R^N → R define the payoff g(S_T) at time
T of a derivative security whose price at time zero is to be determined.

Once again, the arguments of Section F can be extended to show that, under technical regularity conditions and in the absence of arbitrage, the price process Y of the derivative security is given by Y_t = C(S_t, t), where C solves the PDE:

∂_t C(x, t) - r(x, t)C(x, t) + D_μ C(x, t) = 0, (x, t) ∈ R^N × [0, T), (37)
with boundary condition C(x, T) = g(x), x ∈ R^N, (38)
where D_μ C(x, t) = C_x(x, t)^T r(x, t)x + C_t(x, t)
+ ½ tr[σ(x, t) σ(x, t)^T C_{xx}(x, t)]. (39)

We exploit once again the technical condition FK on (r, σ, g) reviewed in
Appendix E for existence of a probabilistic representation of solutions to the PDE (37)-(38).

The Feynman-Kac Solution. Under Condition FK, if there is no arbitrage, then the derivative security with payoff g(S_T) at time T has the price process Y given by Y_t = C(S_t, t), where C is the solution to the PDE (37)-(38) given, at each (x, t) ∈ R^N × [0, T], by x,t x,t

C(x, t) = E[exp(- ∫_t^T r(Z^{x,t}_s, s) ds) g(Z^{x,t}_T)]; (40)

where Z^{x,t} is the Ito process defined by Z^{x,t}_t = x, s < t, and(A) What replicating strategy would you recommend?

(B) If the options are sold at a 10 percent profit markup, give an explicit formula for the option price Gold in Sacks should charge its customers.

(C) Suppose borrowing in U.S. funds is too clumsy, since the other two parts of the strategy (dollar and haggis trading) are done at Gold in Sacks’s Edinburgh office. If the British pound borrowing rate is \( r_p \), a constant, is it possible, under some conditions, to answer parts (A) and (B), using British pound borrowing (and lending) rather than U.S. dollar borrowing (and lending)? If so, provide the conditions. If not, say why not. If you find it useful, you may use any arbitrage conditions relating the various coefficients (\( \rho \), \( \sigma \), \( T \), \( r \)), if indeed there are any such coefficients precluding arbitrage.

--

**100 5. The Black-Scholes Model**

--

5.12 Show, in the setting of Section E, that (26) recovers the Black-Scholes formula (11).

5.13 Show that the Black-Scholes option-hedging strategy (\( a \), \( b \)) of Section F is such that \( a \in \mathcal{E}^2(S) \) and \( b \in \mathcal{E}^2(B) \), as assumed.

--

**Notes**

(A) The Brownian model was introduced to the study of option pricing by Bachelier (1900).

(B-D) Karatzas and Shreve (1988) is a standard source for stochastic calculus for Brownian motion. Proposition 5B can be found, for example, in Protter (1990).

(E-I) The Black and Scholes (1973) formula was extended by Merton (1973b, 1977) and subsequently given literally hundreds of further extensions and applications. The line of exposition here is based on Gabay (1982) and Duffie (1988a). Andreasen, Jensen, and Poulsen (1998) provide numerous alternative methods of deriving the Black-Scholes formula. The basic approach of using continuous-time self-financing strategies as the basis for making arbitrage arguments is due to Merton (1977) and Harrison and Kreps (1979). The basic idea of risk-neutral valuation, via adjustment of the underlying stock-price process, is due to Cox and Ross (1976). This is extended to the notion of equivalent martingale measures, found in Chapter 6, by Harrison and Kreps (1979).

Additional Topics: Cox and Rubinstein (1985) is a standard reference on options, while Hull (2000) has further applications and references. The impact of variations in the "volatility" on the Black-Scholes option-pricing formula is shown, in two different senses, by El Karoui, Jeanblanc, and Shreve (1998), Bergman, Grundy, and Wiener (1996a), Johnson and Shanno (1987), and Reisman (1986). For "stochastic volatility" models, see Section E and references cited in the Notes to Chapter 8.

Alternative approaches to the standard methods of stochastic calculus have been developed by Cutland, Kopp, and Willinger (1991, 1993a,b), who apply nonstandard analysis; by Bick and Willinger (1994) and Willinger and Taqu (1989), who use a pathwise integral established by Föllmer (1981); and by Kunitomo (1993) and Cutland, Kopp, and Willinger (1991, 1993a), who exploit fractional Brownian motion. See Rogers (1998) for a discussion of the use of fractional Brownian motion in this setting. Lacoste (1995) proposes a Wiener-Chaos version of derivative calculations.

Part (C) of Exercise 5.10 was related to the author by Bruce Grundy. For the case of transactions costs and other market "imperfections," see the Notes of Chapter 6.

--

**6 State Prices and Equivalent Martingale Measures**

THIS CHAPTER SUMMARIZES arbitrage-free security pricing theory in the continuous-time setting introduced in Chapter 5. The main idea is the equivalence between no arbitrage, the existence of prices, and the existence of an equivalent martingale measure, paralleling the discrete-state theory of Chapter 2. This extends the Markovian results of Chapter 5, which are based on PDE methods. For those interested mainly in applications, the first sections of Chapters 7 and 8 summarize the major conclusions of this chapter as a "black box," making it possible to skip this chapter on a first reading.

The existence of a state-price deflator is shown to imply the absence of arbitrage. Then a state-price "beta" model of expected returns is derived. Turning to equivalent martingale measures, we begin with the sufficiency of an equivalent martingale measure for the absence of arbitrage. Girsanov’s Theorem (Appendix D) gives conditions under which there exists an equivalent martingale measure. This approach generates another proof of the Black-Scholes formula. State prices are then connected with equivalent martingale measures; the two concepts are more or less the same. They are literally equivalent in the analogous finite-state model of Chapter 2, and we will see that the distinction here is purely technical.

--

**A. Arbitrage**

We fix a standard Brownian motion \( B = (B^1, \dots, B^d) \) in \( \mathbb{R}^d \), restricted to some time interval \( [0, T] \), on a given probability space \( (\Omega, \mathcal{F}, P) \). We also fix the standard filtration \( \mathcal{F} = \{ \mathcal{F}_t : t \in [0, T] \} \) of \( B \), as defined in Section 5I. For simplicity, we take \( \mathcal{F} \) to be \( \mathcal{F}_T \). Suppose the price processes of \( N \) given securities form an Itô process \( X = (X^1, \dots, X^N) \) in \( \mathbb{R}^N \). We suppose that each security price process is in the space \( \mathcal{E}^2 \) containing any Itô process \( Y \) with \( dY_t = a(t) \, dt + \sigma(t) \, dB(t) \) for which \[
\mathbb{E} \left[ \int_0^T |a(t)|^2 \, dt \right] < \infty \quad \text{and} \quad \mathbb{E} \left[ \int_0^T \|\sigma(t)\|^2 \, dt \right] < \infty.
\]

Until later in the chapter, we will suppose that the securities pay no dividends during the time interval \( [0, T) \), and that \( X_T \) is the vector of cum-dividend security prices at time \( T \).

A trading strategy \( \theta \), as we recall from Chapter 5, is an \( \mathbb{R}^N \)-valued process \( \theta \) in \( \mathcal{E}^2(X) \), as defined in Section 5L. This means simply that the stochastic integral \( \int \theta \cdot dX \) defining trading gains is well defined. A trading strategy \( \theta \) is self-financing if \[
\theta_t \cdot X_t = \theta_0 \cdot X_0 + \int_0^t \theta_s \cdot dX_s, \quad t \in [0, T]. \tag{1}
\]

If there is some process \( r \) with the property that \( \int_0^T |r_t| \, dt \) is finite almost surely and, for some security with strictly positive price process \( B \), we have \[
B_t = B_0 \exp \left( \int_0^t r_s \, ds \right), \quad t \in [0, T], \tag{2}
\] then we call \( r \) the short-rate process. In this case, \( dB_t = r_t B_t \, dt \), allowing us to view \( r_t \) as the riskless short-term continuously compounding rate of interest, in an instantaneous sense, and to view \( B \) as the market value of an account that is continually reinvested at the short-term interest rate \( r \).

A self-financing strategy \( \theta \) is an arbitrage if \( \theta_0 \cdot X_0 < 0 \) and \( \theta_T \cdot X_T \ge 0 \), or \( \theta_0 \cdot X_0 = 0 \) and \( \theta_T \cdot X_T > 0 \). (Recall, "\( \theta_T \cdot X_T > 0 \)" means that \( \theta_T \cdot X_T \) is non-negative and is non-zero with positive probability.) Our main goal in this chapter is to characterize the properties of a price process \( X \) that admits no arbitrage, at least after placing some reasonable restrictions on trading strategies.

--

**B. Numeraire Invariance**

It is often convenient to renormalize all security prices, sometimes relative to a particular price process. This section shows that such a renormalization has essentially no economic effects. A deflator is a strictly positive Itô process. We can deflate the previously given security price process \( X \) by a deflator \( Y \) to get the new price process \( X^Y \) defined by \( X^Y_t = X_t / Y_t \).

**Numeraire Invariance Theorem.** Suppose \( Y \) is a deflator. Then a trading strategy \( \theta \) is self-financing with respect to \( X \) if and only if \( \theta \) is self-financing with respect to \( X^Y \).

**Proof.** Let \( W_t = \theta_0 \cdot X_0 + \int_0^t \theta_s \cdot dX_s \), \( t \in [0, T] \). Let \( W^Y \) be the process defined by \( W^Y_t = W_t Y_t^{-1} \). Because \( W \) and \( Y \) are Itô processes, Itô’s Formula implies, letting \( \sigma_X \), \( \sigma_W \), and \( \sigma_Y \) denote the respective diffusions of \( X \), \( W \), and \( Y \), that
\[ dW^Y_t = Y_t^{-1} \, dW_t + W_t \, d(Y_t^{-1}) + \sigma_W(t) \cdot \sigma_{Y^{-1}}(t) \, dt \]
\[
= Y_t^{-1} \theta_t \cdot dX_t + (\theta_t \cdot X_t) \, d(Y_t^{-1}) + [\sigma_W(t) \cdot \sigma_{Y^{-1}}(t)] \, dt \]
\[
= \theta_t \cdot [Y_t^{-1} \, dX_t + X_t \, d(Y_t^{-1}) + \sigma_X(t) \cdot \sigma_{Y^{-1}}(t) \, dt]
\]
\[ = \theta_t \cdot dX^Y_t.
\]
Thus, \( \theta_t \cdot X^Y_t = \theta_0 \cdot X^Y_0 + \int_0^t \theta_s \cdot dX^Y_s \) if and only if \( \theta_t \cdot X_t = \theta_0 \cdot X_0 + \int_0^t \theta_s \cdot dX_s \), completing the proof. \( \blacksquare \)

We have the following corollary, which is immediate from the Numeraire Invariance Theorem, the strict positivity of \( Y \), and the definition of an arbitrage.

--

**102 6. State Prices and Equivalent Martingale Measures**

--

**C. State Prices and Doubling Strategies** 103Model — 7, = ——9,(t) - 0, (2). (7)
7,
We will now see that (7) leads to a “beta model” for expected returns, analogous to that of Chapter 2. We can always find adapted processes p and e valued in R^N and R respectively, such that

σ_X(t) = σ_X(t) g + e and σ_X(e) = 0,  t ∈ [0, T],

where σ_X is the R^N×N-valued diffusion of the price process X. For each
(ω, t) in Ω × [0, T], the vector σ_X(ω, t) g(ω, t) is the orthogonal projection in R^N of σ_X(ω, t) onto the span of the rows of the matrix σ_X(ω, t).
Suppose θ = (θ^0, …, θ^N) is a self-financing trading strategy with σ_θ = θ^T σ_X. (For example, if X^0(t) = exp (∫_0^t r_s ds) for a short-rate process r, we can construct θ by letting θ^0 = -g^0, θ^j > 1, and by choosing θ^0 so that the self-financing condition is met.) The market-value process W^θ of θ is an Ito process because θ is self-financing. We suppose that the initial portfolio can be chosen so that W^θ is also strictly positive, implying that the associated return process R^θ = dW^θ/W^θ is well defined. Because the diffusion of W^θ is σ_θ, the diffusion of R^θ is σ_θ = σ_θ p/W^θ. For an arbitrary Ito return process R, (6) implies that

σ_R(ω) — β = —σ_X(ω)^T φ - ε(ω)

= — σ_X(ω) g(ω) - σ_X(ω)^T ε, + α

= ——σ_X(ω)^T g(ω) - σ_X(ω)^T ε

using the fact that σ_X(ω, t) is (in each state ω) a linear combination of the rows of σ_X(ω, t). This in turn implies that σ_X(ω) - ε, = 0. In particular, for the return process R*, we have

σ_R* — β = σ_X g^T

where p* is the drift (expected rate of return) of R*. Substituting back into (6) the resulting expression for W^θ/7, leaves the state-price beta model of returns given by

β_R*(t) — r = β(σ)(u - r), (8)
where β(σ)(t) = σ_X g / σ_R*

In the “instantaneous sense” in which σ_R*^2 d⟨R^*⟩ stands for the conditional variance of dR* and σ_X σ_R* d⟨X, R^*⟩ stands for the conditional covariance between dX and dR*, we can view (8) as the continuous-time analogue to the state-price beta models of Section 1F and Exercise 2.6(C). Likewise, we can loosely think of R* as a return process whose increments have maximal conditional correlation with the increments of the state-price deflator 7. Chapter 10 develops a special case, the consumption-based capital asset pricing model.

# E. Equivalent Martingale Measures

A probability measure Q on (Ω, F) is said to be equivalent to P provided, for any event A, we have Q(A) > 0 if and only if P(A) > 0. An equivalent probability measure Q is an equivalent martingale measure for the price process X of N given securities if X is a martingale with respect to Q, and if the Radon-Nikodym derivative ξ (defined in Appendix C) has finite variance. The finite-variance condition is a technical convenience that is not uniformly adopted in the literature cited in the Notes on equivalent martingale measures. An equivalent martingale measure is sometimes referred to as a “risk-neutral” measure.

In the finite-state setting of Chapter 2, it was shown that the existence of a state-price deflator is equivalent to the existence of an equivalent martingale measure (after some deflation). Later in this chapter, we will see technical conditions sustaining that equivalence in this continuous-time setting. Aside from offering a conceptual simplification of some asset pricing and investment problems, the use of equivalent martingale measures is justified by the large body of useful properties of martingales that can be applied to simplify reasoning and calculations.

First, we establish the sufficiency of an equivalent martingale measure for the absence of arbitrage. We later show that a technical strengthening

of the no-arbitrage condition of the following theorem implies the existence of an equivalent martingale measure. Aside from technical issues, the arguments are the same as those used to show this equivalence in
Chapter 2. As in Section C, we need to apply an integrability condition or a credit constraint to trading strategies.

Theorem. If the price process X admits an equivalent martingale measure, then there is no arbitrage in H*(X) or in Q(X).

Proof: The proof is quite similar to that of Proposition C. Let Q be an equivalent martingale measure. Let θ be any self-financing trading strategy.

The idea of the proof is based on the case in which θ is bounded, which we assume for the moment. The fact that X is a martingale under Q implies that E_Q( ∫_0^t θ_s dX_s ) = 0. The self-financing condition (1) therefore implies that

0 = X_0 + ∫_0^t θ_s dX_s = X_0 + E_Q(∫_0^t θ_s dX_s).

Thus, if X_T - X_0 > 0, then θ_T - X_T > 0. Likewise, if θ_T - X_T > 0, then θ_0 · X_0 > 0. An arbitrage is therefore impossible using bounded trading strategies.

For the case of any self-financing trading strategy θ ∈ H*(X), additional technical arguments are needed to show that E_Q( ∫_0^t θ_s dX_s ) = 0.
As X is an Ito process, we can write dX_t = μ dt + σ_t dB_t for appropriate μ and σ. By the Diffusion Invariance Principle (Appendix D), there is a standard Brownian motion B^Q in R^m under Q such that dX_t = σ_t dB_t^Q.
Let Z = ∫_0^T |θ_s σ_s|^2 dt. Because θ is in H*(X), Y has finite expectation under P. The product of two random variables of finite variance is of finite expectation, so ξ Y is also of finite expectation under P. Thus,
E_Q(√Z) < ∞. Proposition 5B then implies that ∫_0^t θ_s dX_s is a Q-martingale, so E_Q( ∫_0^t θ_s dX_s ) = 0. The remainder of the proof for this case is covered by the arguments used for bounded θ.

For the case of θ ∈ Q(X), the arguments used in the proof of
Proposition C imply that the wealth process W, defined by W_t = θ_t · X_t, is a supermartingale under Q, so that E_Q(θ_T · X_T) ≤ θ_0 · X_0, implying that θ cannot be an arbitrage.

In most cases, the theorem is applied along the lines of the following

Corollary, a consequence of the corollary to the Numeraire Invariance Theorem of Section B.

Corollary. If there is a deflator Y such that the deflated price process X^Y admits an equivalent martingale measure, then there is no arbitrage in H*(X^Y) or in Q(X^Y).

If there is a short-rate process r, it is typical in applications to take the deflator Y defined by Y_t = exp(— ∫_0^t r_s ds). If r is bounded, then we have
H*(X^Y) = H*(X) and Q(X^Y) = Q(X), so the previous result can be stated in a more natural form.

# F. State Prices and Martingale Measures

We now investigate the relationship between equivalent martingale measures and state-price deflators. They turn out to be effectively the same concept. We take as given the setup of Section A, including a price process X for N securities.
For a probability measure Q equivalent to P, the density process ξ for Q is the martingale defined by dξ_t

ξ_t = E_P(dQ|F_t), t ∈ [0, T], (9)

where 4 is the Radon-Nikodym derivative of Q with respect to P. As stated in Appendix C, for any times t and s > t, and any F_t-measurable

random variable W such that E_P(|W|) < ∞, E_Q(ξ_t W) = ξ_t E_P(W), t ∈ [0, T]. (10)

Proposition. Suppose there is a short-rate process r and let Y be defined by Y_t = exp(— ∫_0^t r_s ds). Suppose, after deflation by Y, that there is an equivalent martingale measure with density process ξ. Then a state-price deflator T is defined by

T = ξ Y, provided var(T_t) < ∞ for all t. Conversely, suppose T is a state-price deflator and let ξ be defined by

ξ_t = E_P(dQ/dP|F_t), t ∈ [0, T]. (11)

Then, provided var(ξ_t) is finite, ξ is the density process for an equivalent martingale measure.

Proof: Suppose, after deflation by Y, that there is an equivalent martingale measure Q with density process ξ. Let T = ξ Y. Then, for any times t and s > t, using (10),

E_t(ξ_s X_s^Y) = E_Q(ξ_s X_s^Y) = ξ_t E_Q(X_s^Y) = ξ_t X_t^Y = T_t X_t^Y. (12).

G. Girsanov and Market Prices of Risk 111

(These expectations exist because both X_s^Y and T_s have finite variances.)
This shows that X^Y is a martingale, so T is indeed a state-price deflator.
Conversely, suppose T is a state-price deflator, and let ξ be definedimal rank d, however, there can be at most one solution n(ω, t) to (13).
This maximal-rank condition is equivalent to the condition that the span of the rows of σ(ω, t) is all of R^d, which is reminiscent of the uniqueness condition for equivalent martingale measures found in Chapter 2.

Proposition. If rank σ = d almost everywhere, then there is at most one market price of risk and at most one equivalent martingale measure. If there is a unique market-price-of-risk process, then rank σ = d almost everywhere.

# H. Black-Scholes Again

Suppose the given security-price process is X = (X^0, X^1, ..., X^{N-1}) = (B, S^1, ..., S^{N-1}), where, for S = (S^1, ..., S^{N-1}), B), we have

dS_t = μ_t dt + σ_t dB_t, and

dB_t = r_t B_t dt, B_0 > 0,

where μ, σ, and r are adapted processes (valued in R^{N-1}, R^{(N-1)×d}, and R, respectively). We also suppose for technical convenience that the short-rate process r is bounded. Then Y = B^{-1} is a convenient numeraire deflator, and we let Z = SY. By Ito’s Formula,

dZ_t = (-r Z_t + μ_t) dt + σ_t dB_t.

In order to apply Theorem G to the deflated price process X^Y = (Z, 1) it would be enough to know that Z has an L^2-reducible market price of risk. Given this, there would be an equivalent martingale measure Q and no arbitrage in X^Y(X) or @(X). Suppose, for the moment, that this is the case. By the Diffusion Invariance result of Appendix D there is a standard Brownian motion B^Q in R^d under Q such that

dZ_t = σ_t dB^Q_t.

Because S = BZ, another application of Ito’s Formula yields

dS_t = r_t S_t dt + σ_t dB^Q_t. (14)

This equation is an important intermediate result for arbitrage-free asset pricing: it gives an explicit expression for security prices under a probability Q under which B^Q is a martingale. For the property that the “discounted” price process is a martingale, Black-Scholes follows. For example, this leads to an easy recovery of the Black-Scholes formula, as follows.

Suppose that one of the securities with price processes S^0, ..., S^{N-1} is an option on another. For convenience, we denote the price process of the option by U and the price process of the underlying security by V, so that U_t = (V_t - K)^+, for expiration at time T with some

given exercise price K. Because U/B is by assumption a martingale under Q, we have

E^Q [ (U_T/B_T) | F_t ] = U_t/B_t = exp(-∫_t^T r_s ds) E^Q [ (V_T - K)^+ | F_t ]. (15)

The reader is asked to verify as an exercise that this is the Black-Scholes formula for the case of d = 1, N = 3, V^0 = B, and with constants r and nonzero σ such that, for all t, r_t = r and dV_t = V_t μ(t) dt + V_t σ dB_t, where μ is a bounded adapted process. Indeed, in this case, Z has an L^2-reducible market-price-of-risk process, so the assumption of an equivalent martingale measure is justified. To be more precise, it is sufficient for the absence of arbitrage that the option-price process is given by (15). Necessity of the Black-Scholes formula for the absence of arbitrage in X(X) or @(X) is formally addressed in Section J. We can already see, however, that the expectation in (15) defining the Black-Scholes formula does not depend on which equivalent martingale measure Q one chooses, so one should expect that the Black-Scholes formula (15) is also necessary for the absence of arbitrage. If (15) is not satisfied, for instance, there cannot be an equivalent martingale measure for S/B. Unfortunately, and for purely technical reasons, this is not enough to imply directly the necessity of (15) for the absence of well-behaved arbitrage, because we do not have a precise equivalence between the absence of arbitrage and the existence of equivalent martingale measures. Section J shows that other methods can be used to show necessity.

In the Black-Scholes setting, we have at most one equivalent martingale measure because σ is nonzero, implying that σ is of maximal rank d = 1 almost everywhere. Thus, from Proposition G, there is exactly one equivalent martingale measure.

The detailed calculations of Girsanov’s Theorem appear nowhere in the actual solution (14) for the “risk-neutral behavior” of arbitrage-free security prices, which can be given by inspection in terms of r and μ only. The results extend to the case of an infinite horizon, as discussed in Section N.

# I. Complete Markets

We say that a random variable W can be replicated by a self-financing trading strategy θ if it is obtained as the terminal value W = θ_T ⋅ X_T. Our basic objective in this section is to give a simple spanning condition on the diffusion σ of the price process X under which, up to technical integrability

conditions, any random variable can be replicated (without resorting to “doubling strategies”).

Proposition. Suppose Y is a numeraire deflator and Q is an equivalent martingale measure for the deflated price process X^Y. Suppose the diffusion σ^Y of X^Y is of rank d almost everywhere. Let W be any random variable with E^Q(|WY|) < ∞. Then there is a self-financing trading strategy θ that replicates W and whose deflated market-value process {θ_t ⋅ X^Y_t : 0 ≤ t ≤ T} is a Q-martingale.

Proof: We can suppose that, without loss of generality, the numeraire is the last of the N securities and write X^Y = (Z, 1). Let B^Q be the standard Brownian motion in R^d under Q obtained by Girsanov’s Theorem.

Because B^Q has the martingale representation property under Q, there is some p such that

E^Q[WY_T | F_t] = E^Q[WY_t] + ∫_t^T p_s ⋅ dB^Q_s, t ∈ [0, T]. (16)

By the rank assumption on σ^Y and the fact that σ^Y = (σ, 0), there are adapted processes φ^1, ..., φ^{N-1} solving

∑_{j=1}^{N-1} φ^j_t σ^{j,k}_t = p^k_t, k = 1,..., d, t ∈ [0,T]. (17)

Let θ be defined by

θ^j_t = φ^j_t(WY_t/Z_t) + θ^0_t(1/Z_t), for j = 1,..., N-1, θ^0_t = E^Q[WY_t | F_t] - ∑_{j=1}^{N-1} θ^j_t Z_t, t ∈ [0, T]. (18)

Then θ = (θ^0, ..., θ^{N-1}) is self-financing and θ_T ⋅ X^Y_T = WY_T. By the numeraire invariance theorem, θ is also self-financing with respect to X and θ_T ⋅ X_T = W. As ∫_t^T p_s ⋅ dB^Q_s is by construction a Q-martingale, (16)-(18) imply that {θ_t ⋅ X^Y_t : 0 ≤ t ≤ T} is a Q-martingale. □

In order to further explore the dynamic spanning properties of the price process X, we let @(X) denote the space of self-financing trading strategies in X. The marketed space of X is

M(X) = {θ ⋅ X_t : θ ∈ @(X)}.

Note that M(X) is a subset of L^2(P), the space of all random variables with finite second moment (and therefore finite expectation), because every θ ∈ @(X) is in @*(X). We say that markets are complete if the marketed space M(X) is actually equal to the space L^2(P). Our objective now is to

extend Proposition I with necessary and sufficient conditions for complete markets.

To say that M(X) is closed means that if W_n, n ∈ ℕ, is a sequence in M(X), and if W is some random variable such that E[(W - W_n)^2] → 0, then W is also in M(X). (This would mean that W is also replicated by some trading strategy in @.) For technical reasons, this closedness property is useful. The following result is from a source cited in the Notes.

Lemma. Suppose that Y is a numeraire deflator and that there is a bounded market-price-of-risk process for X^Y. Then M(X^Y) is closed.

We can now exploit the previous lemma to obtain a simple condition for complete markets.

Theorem. Let Y_t = exp( -∫_0^t r_s ds) for a bounded short-rate process r. For dX_t = μ_t dt + σ_t dB_t, suppose there is a bounded market-price-of-risk process for X^Y. Then markets are complete if and only if rank(σ) = d almost everywhere.

Proof: Let π be a bounded market-price-of-risk process for X^Y and Q be the associated equivalent martingale measure. We can take X^Y = (Z, 1), for an R^{N-1}-valued Ito process Z. Let B^Q be the standard Brownian motion in R^d under Q defined by dB^Q_t = dB_t + π_t dt. Let W be a bounded random variable.

By Ito’s Formula, the diffusion σ^Y of X^Y has the same span as σ(ω,t) by (ω,t), and is therefore of rank d almost everywhere. By Proposition I, there is a self-financing trading strategy θ such that θ_T ⋅ X^Y_T = W, and whose deflated market-value process V is a Q-martingale. Because W is bounded and dV_t = p_t ⋅ dB^Q_t, where p is given by (16), Proposition 5Bimplies that b = σ is essentially bounded. (That is, there is a constant h such that, letting ζₜ = 1 whenever |γₜ| > h and zero otherwise, we have E( ∫ ζₜ dt) = 0.) By the definition of a market-price-of-risk process, b = σγ. By assumption, γ is bounded, so b is essentially bounded, and therefore θ is in H₂(X). This proves that any bounded W can be replicated by some θ in H₂(X).

Now suppose that W is in L₂(P). For each positive integer n, we approximate W with the bounded random variable Wₙ, defined by Wₙ(ω) = W(ω) whenever |W(ω)| ≤ n and Wₙ(ω) = 0 otherwise. As Wₙ is in the marketed space for all n, and because E[(W - Wₙ)²] → 0, we have W in M(X) by the previous lemma. Thus M(X) = L₂(P).

Conversely, suppose that it is not true that rank(σ) = d almost everywhere. We will show that markets are not complete. By the rank assumption on σ and the fact that the diffusion σᵃ of Xᵃ and the diffusion σ of X have the same span for all (ω, t), there is some bounded adapted process g such that there is no solution θ₀, ..., θ_{d-1} to (17). Then there is no trading strategy θ in H₂(X) that is self-financing with respect to (Z, 1) such that θₜ · d(Zₜ, 1) = ∫ gₜ · dXₜ. By the Numeraire Invariance Theorem, there is no θ in H₂(X) with θₜ · Xₜ = W, where W = exp(∫ γₜ dXₜ) ∫ gₜ dBₜ. Because γ, σ, and g are bounded, W is in L₂(P).

# J. Redundant Security Pricing

We return to the Black-Scholes example of Section H. We recall that the underlying Brownian motion B is one-dimensional, and that there are two primitive securities with price processes V and B, where V is a geometric Brownian motion and Bₜ = e^{rt} for a constant interest rate r. For a market with these two securities alone, there is a bounded market-price-of-risk process. It follows that markets are complete, that there is an equivalent martingale measure Q after deflating by B, and that there is no arbitrage in H₂(X).

Now, consider an option at strike price K, paying (V_T - K)⁺ at time T. We would like to conclude that the Black-Scholes formula applies, meaning that the option has the price process U defined by U_t = E_Q[ e^{-r(T-t)} (V_T - K)⁺ ].
In Section H, we showed that this pricing formula is sufficient for the absence of a well-behaved arbitrage with respect to (B, V, U). Now we show that this is the unique arbitrage-free price process for the option with that property. (This was already shown, in effect, in Chapter 5, but the following argument leads to a more general theorem.)

We proceed as follows. As V_T has finite variance, so does the option payoff (V_T - K)⁺. Suppose, to set up a contradiction, that the actual option price process U is not U. For any constant ε > 0, let A_ε⁺ denote the event that U_t - U_t > ε for some t in [0, T]. Let A_ε⁻ denote the event that U_t - U_t > ε for some t in [0, T]. Because U and U are assumed to be different processes, there is some ε > 0 such that at least one of the events A_ε⁺ or A_ε⁻ has strictly positive probability. Without loss of generality, suppose that P(A_ε⁺) > 0, and let τ = inf{t : U_t - U_t > ε}, a stopping time that is valued in [0, T] with strictly positive probability.

By construction, there is a self-financing trading strategy θ = (θ₀, θ₁) in H₂(B, V) that replicates (V_T - K)⁺. From the fact that θ is self-financing, numeraire invariance, and the fact that Q is an equivalent martingale measure for (1, V/B), we have θ₀ₜ Bₜ + θ₁ₜ Vₜ = E_Q[ e^{-r(T-t)} (V_T - K)⁺ ] = U_t.

Let ψ be the R³-valued trading strategy defining investments at the short rate, in the underlying asset, and in the option defined by ψ = (0, 0, 0) for t < τ, and ψₜ = (0, 0, e^{r(τ-t)} 1_{[τ,T]}(t)) + (θ₀ₜ, θ₁ₜ, 0) 1_{[τ,T]}(t), where (θ₀, θ₁) is the option-replicating strategy described above. It can be checked that ψ is self-financing and that ψₜ · d(Bₜ, Vₜ, Uₜ) ≥ 0, implying that ψ is an arbitrage that is in H₂(B, V, U).

More broadly, given some general price process X for the N “primitive” securities, we say that a security with price process U is redundant if its final value U_T can be replicated by a trading strategy θ in H₂(X). Complete markets implies that any security (with finite-variance price process) is redundant.

**Theorem.** Suppose X admits an equivalent martingale measure Q. Given X, consider a redundant security with price process U in H₂. Then (X, U) = (X₁, ..., X_N, U) admits no arbitrage in H₂(X, U) if and only if U is a Q-martingale.

*Proof:* If U is a Q-martingale, then Q is an equivalent martingale measure for (X, U), implying no arbitrage in H₂(X, U) by Theorem E. Conversely, suppose U is not a Q-martingale. The arguments used for the preceding Black-Scholes case extend directly to this setting so as to imply the existence of an arbitrage in H₂(X, U). ∎

One would typically apply this result after deflation. In the definition of a redundant security, one could have as easily substituted the credit-constrained class H₂(X, U) of trading strategies for W₂(X, U), allowing a like condition on U in the statement of the theorem.

# K. Martingale Measures from No Arbitrage

So far, we have exploited the existence of an equivalent martingale measure as a sufficient condition for the absence of well-behaved arbitrage. Now we turn to the converse issue: Does the absence of well-behaved arbitrages imply the existence of an equivalent martingale measure? In the finite-dimensional setting of Chapter 2, we know that the answer is always: “After a change of numeraire, yes.” Only technicalities stand between this finite-dimensional equivalence and the infinite-dimensional case we face here. Because of these technicalities, this section can be skipped on a first reading.

Given a price process X for the N securities, suppose there is no arbitrage in H₂(X). Then, for each W in M(X) (that is, each W = θ_T · X_T for some θ in H₂(X)), let Ψ(W) = θ₀ · X₀ denote the unique initial investment required to obtain the payoff W. We know that this function Ψ: M(X) → R is uniquely well defined because, if there are two trading strategies θ and ρ in H₂(X) with θ_T · X_T = ρ_T · X_T and θ₀ · X₀ > ρ₀ · X₀, then θ - ρ is an arbitrage. The function Ψ is linear because stochastic integration is linear. Finally, again from the absence of arbitrage, Ψ is strictly increasing, meaning that Ψ(W) > Ψ(Z) whenever W > Z. The marketed space M(X) is a linear subspace of L₂(P) because, whenever Z = θ_T · X_T and W = ρ_T · X_T are in M(X), then aZ + bW is also in M(X) for any constants a and b. (This follows from the fact that aθ + bρ is a self-financing strategy, using the linearity of stochastic integration.)

Because of technicalities, the existence of an equivalent martingale measure does not follow from the absence of arbitrage in H₂(X), alone. Indeed, some sources cited in the Notes provide counterexamples. We can resort, however, to a slightly stronger condition. An approximate arbitrage is a sequence {Zₙ} in M(X) with Ψ(Zₙ) < 0 for all n, such that there exists some sequence {Zₙ'} in L₂(P) with Zₙ ≤ Zₙ' for all n, and with E[(Zₙ' - Z')²] → 0 for some Z' > 0. The idea is that no Zₙ has positive market value, yet Zₙ is larger than Zₙ', which in turns converges to a positive, nonzero, random value. For example, suppose θ is an arbitrage in H₂(X) with θ_T · X_T ≥ 0. Then the (trivial) sequence {Zₙ} defined by Zₙ = θ_T · X_T for all n is an approximate arbitrage. (Just take Zₙ' = θ_T · X_T + X₁, for all n.) Provided there is a bounded short-rate process, or under other weak assumptions, the absence of approximate arbitrage is indeed a stronger assumption than the absence of arbitrage in H₂(X), and the difference is only important (for technical reasons) in this infinite-dimensional setting. If we strengthen the assumption of no arbitrage in H₂(X) to the assumption of no approximate arbitrage, we can recover the existence of an equivalent martingale measure. Variants of the following result are cited in the Notes.Each of the above implications of the absence of arbitrage for security prices has a natural extension to this case of “lumpy” dividends. In particular, (20) applies as stated, with \(\int dD\) defined by \(\int f dZ + \int f dV - \int f dW\) whenever all three integrals are well defined, the first as a stochastic integral and the latter two as Stieltjes integrals. A reader unfamiliar with the Stieltjes integral may consult sources given in the Notes. Happily, the stochastic integral and the Stieltjes integral coincide whenever both are well defined. In this book, we only consider applications that involve the following two trivial examples of the Stieltjes integral \(\int f dV\).

(a) For the first example of a Stieltjes integral, we let \(V_t = \int_0^t \gamma_s ds\) for some \(\gamma\) in \(\mathcal{L}^1\), in which case \(\int_a^b f dV = \int_a^b f \gamma ds\).

(b) In the second case, for some stopping time \(T\), we have \(V_t = 0\), \(t \le T\), and \(V_t = v\), \(t > T\), where \(v = \Delta V_T\) is the jump of \(V\) at time \(T\). For this second case, we have \(\int_a^T f dV = 0\), \(a \le T\), and \(\int_T^b f dV = f_T v\), \(b > T\), which is natural for our purposes.

We continue to take \((D, X)\) to be a dividend-price pair if \(X + D\) is an Itô process. Because of the possibility of jumps in dividends, it is now necessary to take an explicit stance, however, on whether security prices will be measured ex dividend or cum dividend. We opt for the former convention, which means that for a dividend-price pair \((D, X)\), a trading strategy \(\theta\) is self-financing if

\[
\theta_t \cdot (X_t + \Delta D_t) = \theta_0 \cdot X_0 + \int_0^t \theta_s dG_s, \quad t \in [0,T], \]

where \(G = X + D\). With this, an arbitrage is defined as a self-financing trading strategy \(\theta\) with \(\theta_0 \cdot X_0 < 0\) and \(\theta_t \cdot (X_t + \Delta D_t) > 0\), or with \(\theta_0 \cdot X_0 > 0\) and \(\theta_t \cdot (X_t + \Delta D_t) < 0\).

Extending our earlier definition to allow for lumpy dividends, a trading strategy \(\theta\) finances a dividend process \(D^\theta\) if \(D^\theta\) is a right continuous process whose left limit \(D^\theta_{t-}\) exists for each \(t\) satisfying

\[
\theta_t \cdot (X_t + \Delta D^\theta_t) = \theta_0 \cdot X_0 + \int_0^t \theta_s dG_s - D^\theta_t, \quad t \in [0,T], \]

with \(\Delta D^\theta_T = \theta_T \cdot (X_T + \Delta D^\theta_T)\).

With these new definitions in place, the term structure can be characterized from (20) as follows. Given a bounded short-rate process \(r\), suppose that \(Q\) is an equivalent martingale measure after deflation by \(Y\), where \(Y_t = \exp(-\int_0^t r_s ds)\). A unit zero-coupon riskless bond maturing at time \(T\) is defined by the cumulative-dividend process \(H\) with \(H_s = 0\), \(s < T\) and \(H_s = 1\), \(s \ge T\). Because \(dH_s = 0\) for \(s \neq T\), and because \(\Delta H_T = 1\), we know from case (b) of the Stieltjes integral that

\[
\int_s^T \exp(-\int_s^u r_v dv) dH_u = \exp(-\int_s^T r_v dv).
\]

Then (20) implies that the price at time \(t\) of a unit zero-coupon riskless bond maturing at time \(T > t\) is given by

\[
B(t,T) = \mathbb{E}^Q \left[ \exp\left(-\int_t^T r_u du\right) \bigg| \mathcal{F}_t \right]. \tag{21}
\]

The solution for the term structure given by (21) is based on the implicit assumption that the price of a bond after its maturity date is zero. This is also consistent with our earlier analysis of option prices, where we have implicitly equated the terminal cum-dividend price of an option with its terminal dividend payment. For example, with an option expiring at \(T\) on a price process \(S\) with exercise price \(K\), we set the terminal option price at its expiration value \((S_T - K)^+\). This seems innocuous. Had we actually allowed for the possibility that the terminal cum-dividend option price might be something other than \((S_T - K)^+\), however, we would have needed a more complicated model and further analysis to conclude from the absence of arbitrage that \((S_T - K)^+\) is indeed the cum-dividend expiration value. This issue of terminal security prices is further pursued in a source cited in the Notes.

**N. Martingale Measures, Infinite Horizon**

There are some applications for which we will want a version of Girsanov’s Theorem for the case of an infinite time horizon. Care must be taken. For example, on a given probability space \((\Omega, \mathcal{F}, P)\), let \(\{\mathcal{F}_t : t \ge 0\}\) be the standard filtration of a standard Brownian motion \(B\), and suppose that there is a constant short rate \(r\). The only other security has a geometric Brownian price process \(S\) given by

\[ dS_t = \mu S_t dt + \sigma S_t dB_t, \]

for constants \(\mu\) and \(\sigma\). The security pays dividends at the rate \(\delta S_t\) at time \(t\), for some constant \(\delta\). This setup is completely standard.

We are naturally led to define

\[ \tilde{B}_t = B_t + \nu t, \]

where \(\nu = (\mu + \delta - r)/\sigma\), and re-express \(dS\) in the form

\[ dS_t = S_t(r - \delta) dt + \sigma S_t d\tilde{B}_t.
\]

While \(\tilde{B}\) is a standard Brownian motion under a measure \(Q\) equivalent to \(P\), there may exist a probability measure \(Q\) under which, as required for risk-neutral pricing, \(\tilde{B}\) is a standard Brownian motion under \(Q\). However, the measure \(Q\) and \(P\) cannot be equivalent!

We can, however, rely on the fact, cited in the Notes, that a probability space \((\Omega, \mathcal{F}, P)\) on which there is a standard Brownian motion \(B\) in \(\mathbb{R}^d\) can be constructed with the following properties:

For any adapted process \(\nu\) in \(\mathbb{R}^d\) such that \(\int_0^t \|\nu_s\|^2 ds < \infty\) for all \(t\), and such that the local martingale \(Z\) defined by

\[
Z_t = \exp\left( -\int_0^t \nu_s dB_s - \frac{1}{2} \int_0^t \|\nu_s\|^2 ds \right)
\]

satisfies \(E[Z_t] = 1\) for all \(t\), there exists a probability measure \(Q\) on \((\Omega, \mathcal{F})\) such that:

- For any time \(t\), \(P\) and \(Q\) assign zero probability to the same events in \(\mathcal{F}_t\). That is, the restrictions of these two probability measures to \(\mathcal{F}_t\) are equivalent.

- Restricted to \((\Omega, \mathcal{F}_t)\), we have \(dQ = Z_t dP\).

- A standard Brownian motion \(B^Q\) in \(\mathbb{R}^d\) for \((\Omega, \mathcal{F}, Q)\) and \(\{\mathcal{F}_t : t \ge 0\}\) is defined by

\[ B^Q_t = B_t + \int_0^t \nu_s ds.
\]

- Under \(Q\), \(B^Q\) has the martingale representation property. That is, for any process \(M\) that is a local martingale under \(Q\), there exists an adapted \(\mathbb{R}^d\)-valued process \(\theta\) such that \(\int_0^t \|\theta_s\|^2 ds < \infty\) almost surely and such that

\[
M_t = M_0 + \int_0^t \theta_s dB^Q_s, \quad t \ge 0.
\]

Somewhat more on this issue, including a sense in which \(Q\) is uniquely defined, can be found in sources cited in the Notes.

**Exercises**

6.1 Provide the details left out of the proof provided for Lemma G.

6.2 Verify relation (14).

6.3 In the setting of this chapter, suppose \(d = 1\), and there is a bounded short rate process \(r\). Suppose the price process \(V\) of an underlying asset is \(V\), where

\[ dV_t = V_t \mu_t dt + V_t \sigma_t dB_t, \]

where \(\mu\) and \(\sigma\) are bounded, and \(\sigma\) is bounded away from zero.

(A) Let \(Y\) be the numeraire deflator defined by \(Y_t = \exp(-\int_0^t r_s ds)\). Show that there is an equivalent martingale measure \(Q\) for \((V^Y, 1)\). Compute \(dV^Y\) and provide the drift of \(V^Y\) under \(Q\).

(B) Consider a European call option on the underlying asset, with expiration at \(T\) and strike \(K\). Provide an expression for the price process \(U\) of the option in the absence of arbitrage in \(\mathcal{M}(V, 1/Y, U)\). Hint: Construct an arbitrage that would apply if your proposed price process were not equal to the actual price process \(U\).

(C) For the price process \(U\) that you found in part (B), show that

\[
U_t = c_1 V_t \mathbb{Q}_1(A) - c_2 K Y_t \mathbb{Q}_2(A), \]

where \(A\) is the event that the option expires in the money, \(\mathbb{Q}_1\) and \(\mathbb{Q}_2\) are probability measures equivalent to \(P\), and \(c_1\), \(c_2\) are constants. All of \(c_1, c_2, \mathbb{Q}_1\), and \(\mathbb{Q}_2\) do not depend on the strike price \(K\). For each \(i\), provide \(\mathbb{Q}_i\) and the constant \(c_i\) and explain how \(c_i\) can be obtained from market data without calculation.

(D) Show that the solution \(U_t\) for the option price given in part (C) corresponds to the Black-Scholes option-pricing formula in the case of constant \(r\) and \(\sigma\). Hint: For each \(i\), use Girsanov’s formula for the distribution of \(\log V_T\) under \(\mathbb{Q}_i\).

(E) Provide an explicit solution \(U_t\) for the option price given in part (C), for the case in which \(r\) and \(\sigma\) are deterministic (but not necessarily constant), expressing the solution in terms of the Black-Scholes formula with an adjusted interest rate parameter and volatility parameter.

6.4 Prove Theorem J.

6.5 Suppose that the return process \(R^\theta\) for a self-financing trading strategy \(\theta\) is well defined as an Itô process, as at the end of Section D. Show, as claimed there, that \(R\) satisfies the state-price restriction (6).

6.6 Extend the arguments of Section E to the case of intermediate dividends, as follows. First, consider a particular security with a dividend-rate process \(\delta\) in \(\mathcal{L}^2\).The cumulative-dividend process H is thus defined by H = ∫₀ᵗ Yₛ dSₛ, t ∈ [0, T].
Suppose that the security's price process V satisfies V_Y = 0. Suppose that Q is an equivalent martingale measure with density ξ. Let T be defined by T₀ = 1 and (11). The fact that H^Y + V^P is a Q-martingale is equivalent to

Vₜ = (1/T) E^Q[ ∫ₜᵀ ξₛ Yₛ dSₛ ], t ∈ [0, T].

Based on the definition of ξ, Fubini’s Theorem, the law of iterated expectations, and the fact that ξ is a martingale, show each of the equalities

Vₜ = (1/T) E^P[ ∫ₜᵀ ξₛ Yₛ dSₛ ]
= (1/T) E^P[ ∫ₜᵀ E^P[ξₛ | Fₜ] Yₛ dSₛ ]
= ∫ₜᵀ E^P[ξₛ Yₛ] dSₛ = ∫ₜᵀ E^P[ξₛ Yₛ] dSₛ
= (1/T) ∫ₜᵀ E^P[ξₛ Yₛ] dSₛ = (1/T) ∫ₜᵀ E^P[ξₛ Yₛ] dSₛ.

This calculation shows that H^P + V^P is a martingale, consistent with the definition of T as a state-price deflator. Reversing the calculations shows that if T is a state-price deflator and var(T) < ∞, then H^Y + V^P is a Q-martingale, where Q is the probability measure defined by its density process ξ from (11).

(B) Extend to the case of V_Y not necessarily zero. That is, suppose Q is an equivalent probability measure whose density process is of finite variance. Show that
V_Y + Y is a Q-martingale if and only if V^P + H^P is a P-martingale.

(C) Extend to the case of a cumulative-dividend process H that is a bounded Ito process. (Although beyond our scope here, an extension of Ito’s Formula applying to general dividend processes that are not necessarily Ito processes shows that one need not assume that H is an Ito process.)

6.7 (State-Price Beta Again). Recall that the cumulative-dividend process DV generated by a trading strategy θ is defined by AD^θ, = W^θ, and W^θ, = W^θ, + ∫₀ᵗ θₛ dGₛ —
D^θ_, where W^θ, = 0, - (X, + AD,) and G is the gain process of the given securities. Let G^θ denote the gain process generated by θ, defined by G^θ, = W^θ + D^θ.
Assuming that an Ito return process R^θ for θ is well defined by dR^θ = (W^θ)* dG^θ,

show that R^θ satisfies the return restriction (6).

6.8 Extend the proof of Proposition K to allow for general dividend processes.
Add technical conditions as necessary.

6.9 In the setting of Section A, a probability measure Q equivalent to P is called a local martingale measure for X if X is a local martingale under Q. Show that if there is a local martingale measure for the deflated price process XY^Y, for some deflator
Y, then there is no arbitrage θ for X whose market-value process {θ_t·X_t: t ≥ 0} is nonnegative, a slightly stronger credit constraint than that of C(X).

6.10 Suppose, for some numeraire deflator Y, that XY has a market-price-of-risk process π such that ∫₀ᵀ πₜ dt < ∞. Prove that there is no arbitrage for X whose

market-value process is nonnegative. Add no regularity conditions.

6.11 Prove numeraire invariance with dividends, in the form of Lemma L.

# Notes

The basic approach of this chapter is from Harrison and Kreps (1979) and
Harrison and Pliska (1981), who coined most of the terms and developed most of the techniques and basic results. Huang (1985b,c) generalized the basic theory.
The development here differs in some minor ways. Most of the results in this chapter extend to an abstract filtration, not necessarily generated by Brownian motion.

(A-B) The notion of a self-financing trading strategy is from Harrison and Kreps
(1979). On numeraire invariance in more general settings, see Huang (1985b)
and Protter (1999), and on the role of numeraire, see Geman, El Karoui, and Rochet (1995).

(C) The idea of a doubling strategy, as described here in terms of coin tosses, appears in Harrison and Kreps (1979). The actual continuous-time “doubling”
strategy (3)-(4), and proof that the associated stopping time τ is valued in
(0, T), is from Karatzas (1993), as is a version of Lemma G. The relevance of the credit-constrained class C(X) of trading strategies and related results such as
Proposition C originate with Dybvig and Huang (1988). Hindy (1995) explores further the implications of a nonnegative wealth constraint.

(D) The beta version of the state-pricing results may be original.

(E) Equivalent martingale measures were developed in Harrison and Kreps
(1979), who also developed the equivalence, up to technical issues, of the absence of arbitrage and the existence of equivalent martingale measures. This section presents only one direction of that result.

(F) The relationship between state prices and equivalent martingale measures is standard.

(G-H) Girsanov’s Theorem was brought into this application by Harrison and
Kreps (1979). Huang and Pagés (1992) give an extension to the case of an infinitetime horizon. Choulli, Krawczyk, and Stricker (1998) address the role of martingales that are stochastic exponentials (such as a density process) in financial applications. Loewenstein and Willard (1998, 1999) treat the implications of local martingale versions of a “density process” for what would, as a martingale, define an equivalent martingale measure.

(D) The relationship between complete markets and the uniqueness of an equivalent martingale measure was initiated by Harrison and Kreps (1979) and Harrison and Pliska (1981). More on this can be found in Artzner and Heath (1990, 1995),
Brown and Madan (1991), Miller (1985), Protter (1999), and Stricker (1984).
Stichnoth, Schachermayer, Schweizer, and Stricker (1994) and Monat and
Stricker (1994, 1995) provide conditions for L²-closedness of the marketed space of contingent claims, a property used in the last section and in the proof of
Proposition I. Rydberg (1997) discusses uniqueness in a Markovian setting. On

preserving market completeness under a change of measure with abstract filtrations, see Duffie (1985).

(K) The main technical result used in Section K, on the extension of positive linear functionals, is inspired by Kreps (1981) and can be found specifically in
Clark (1993). The notion of an approximate arbitrage is a slight variation on the notion of a free lunch, introduced by Kreps (1981). Related results leading to technical conditions for the existence of an equivalent martingale measure are based on Harrison and Kreps (1979) and Harrison and Pliska (1981). The result applies without technical qualification in discrete-time settings, as shown by Dalang, Morton, and Willinger (1990). For a simpler proof, see Kabanov and Stricker (2000). Delbaen and Schachermayer (1999) offer a definitive result in continuous-time settings, based on the notion of a free lunch with vanishing risk, which is closely related to that of an approximate arbitrage. They show the equivalence, after deflation by a numeraire deflator, between no free lunch with vanishing risk and the existence of a local martingale measure. For previous and related results, see Ansel and Stricker (1992, 1994b), Back and
Pliska (1987), Cassese (1996) Delbaen (1992), Delbaen and Schachermayer
(1994a, b, 1995a, b,c, 1996a,b, 1998), Duffie and Huang (1986), El Karoui and
Quenez (1995), Frittelli and Lakner (1995), Jacod and Shiryaev (1998), Kabanov
(1996), Kabanov and Kramkov (1994, 1995), Kusuoka (1992a), Lakner (1993a,b),
Levental and Skorohod (1995), Rogers (1994), Schachermayer (1992, 1994, 1998), Schweizer (1992), and Stricker (1990).

For various notions of counterexamples to the existence of an equivalent martingale measure in the absence of arbitrage, see Stricker (1990), Back and
Pliska (1991), Delbaen and Schachermayer (1994b), Schachermayer (1993), and Levental and Skorohod (1995).

(L-M) The extensions to handle dividends and jumps is routine. The Stieltjes integral, mentioned in Section M, can be found in an analysis text such as Royden
(1968). In order to see a sense in which the absence of arbitrage implies that terminal ex-dividend prices are zero, see Ohashi (1991). This issue is especially delicate in non-Brownian information settings, since the event that X_t ≠ 0, insome informational sense not explored here, can be suddenly revealed at time T, and therefore be impossible to exploit with a simultaneous trade. For further discussion of the terminal arbitrage issue, see Ohashi (1991).

(N) The motivation here is from Huang and Pagès (1992). The results extending
Girsanov’s Theorem are based on Revuz and Yor (1991), Section VI.1.

Additional Topics: Banz and Miller (1978) and Breeden and Litzenberger
(1978) deduce state prices from the valuation of derivative securities.

Amendinger (1999) treats martingale representation for enlarged filtrations.
Imkeller, Pontier, and Weisz (1999) address the existence of arbitrage after enlarging the filtration to include some “advanced” information.

Dritschel and Protter (1998) apply martingale representation in a financial setting involving Azema’s martingale.

Babbs and Selby (1996), Bühlmann, Delbaen, Embrechts, and Shiryaev
(1998), and Föllmer and Schweizer (1990) suggest some criteria or parameterization for the selection of an equivalent martingale measure in incomplete markets. In particular, Artzner (1995), Bajeux-Besnainou and Portait (1997),
Dijkstra (1996), Johnson (1994), and Long (1990) address the numeraire portfolio, also called growth-optimal portfolio, as a device for selecting a state-price deflator.

Carr and Jarrow (1990) show a connection between local time and the BlackScholes model. See also Bick (1995).

Analogues to some of the results in Chapter 5 or in this chapter for the case of market imperfections such as portfolio constraints or transactions costs are provided by Ahn, Dayal, Grannan, and Swindle (1995), Avellaneda and
Parès (1994a), Bergman (1995), Boyle and Vorst (1992), Carassus and Jouini
(1998), Chen (1994), Clewlow and Hodges (1996), Constantinides (1993),
Constantinides and Zariphopoulou (1999), Cvitanić and Karatzas (1993), Davis and Clark (1993), Davis and Panas (1991), Davis, Panas, and Zariphopoulou
(1993), Edirisinghe, Naik, and Uppal (1993), Grannan and Swindle (1996),
Henrotte (1991), Jouini and Kallal (1993a, 1995), Karatzas and Kou (1998),
Korn (1995), Kusuoka (1992b, 1993), Leland (1985), Levental and Skorohod
(1997), Luttmer (1996), Munk (1997), Soner, Shreve, and Cvitanić (1994), Taleb
(1997), and Whalley and Wilmott (1997). Many of these results are asymptotic, for “small” proportional transactions costs, based on the approach of Leland
(1985). Additional implications of transactions costs and portfolio constraints for optimal portfolio and consumption choice are cited in the Notes of Chapter 9.
(1986). Application to international markets is given by Delbaen and Shirakawa.

General treatments of some of the issues covered in this chapter can be found in Babbs and Selby (1996), Back and Pliska (1991), Christensen (1987,
1991), Conze and Viswanathan (1991b), Dothan (1990), El Karoui and Quenez
(1991), El Karoui and Quenez (1995), Jarrow and Madan (1999), Jouini and Kallal
(1995), Karatzas (1993), Miller (1985), Protter (1999), and Rady (1993).

# Term-Structure Models

THIS CHAPTER REVIEWS models of the term structure of interest rates that are used for the pricing and hedging of fixed-income securities, those whose future payoffs are contingent on future interest rates. Termstructure modeling is one of the most active and sophisticated areas of application of financial theory to everyday business problems, ranging from managing the risk of a bond portfolio to the design and pricing of collateralized mortgage obligations.

Included in this chapter are such standard examples as the Merton,
Ho-Lee, Dothan, Brennan-Schwartz, Vasicek, Black-Derman-Toy, BlackKarasinski, and Cox-Ingersoll-Ross models, and variations of these “singlefactor” term-structure models, so named because they treat the entire term structure of interest rates at any time as a function of a single state variable, the short rate of interest. We will also review multifactor models, including multifactor affine models, extending the Cox-Ingersoll-Ross and Vasicek models.

All of the named single-factor and multifactor models can be viewed in terms of marginal forward rates rather than directly in terms of interest rates, within the Heath-Jarrow-Morton (HJM) term-structure framework.
The HJM framework allows, under technical conditions, any initial term structure of forward interest rates and any process for the conditional volatilities and correlations of these forward rates.

Numerical tractability is essential for practical applications. The “calibration” of model parameters and the pricing of term-structure derivatives are typically done by such numerical methods as “binomial trees”
(Chapter 3), Fourier transform methods (Chapter 8), Monte Carlo simulation (Chapter 12), and finite-difference solution of PDEs (Chapter 12).

This chapter makes little direct use of the pricing theory developed in Chapter 6 beyond the basic idea of an equivalent martingale measure,

which can therefore be treated as a “black box.” One need only remember that, with probabilities assigned by an equivalent martingale measure, the expected rate of return on any security is the short rate of interest. Since the existence of an equivalent martingale measure is, except for purely technical conditions, equivalent to the absence of arbitrage, we find it safe and convenient to work almost from the outset under an assumed equivalent martingale measure. Sufficient conditions for an equivalent martingale measure are reviewed in Chapter 6. An equilibrium example is given in Chapter 10. In empirical applications, it is often convenient to specify the probabilistic properties of a term-structure model under an equivalent martingale measure and also under a probability measure reflecting actual data generation.

# A. The Term Structure

We fix a standard Brownian motion B = (B₁,..., B_d) in R^d, for some dimension d > 1, restricted to some time interval [0, T], on a given probability space (Ω, F, P). We also fix the standard filtration F = {F_t: 0 < t < T} of B, as defined in Section 5.1.

We take as given an adapted short-rate process r with E ∫_0^T |r_t| dt < ∞.
Conceptually, r is the continually compounding rate of interest on riskless securities at time t. This is formalized by supposing that, for any time t, one can invest one unit of account and achieve a market value at any future time s of exp(∫_t^s r_u du). This may be viewed as the proceeds of continual reinvestment at the short rate r.

Consider a zero-coupon bond maturing at some future time s > t. By definition, the bond pays no dividends before time s, and offers a fixed lump-sum payment at time s that we can take without loss of generality to be 1 unit of account. Although it is not always essential to do so, we assume throughout the chapter that such a bond exists for each maturity date s. One of our main objectives is to characterize the price P(t, s), at time t, of the s-maturity bond, and its behavior over time.

In the absence of arbitrage, purely technical conditions reviewed in
Chapter 6 are required for the existence of an equivalent martingale measure. Such a probability measure Q has the property that any security whose dividend is in the form of a lump-sum payment of Z at some time s has a price, at any time t < s, of

E^Q [ exp( -∫_t^s r_u du ) Z | F_t ], (1)

where E^Q denotes F_t-conditional expectation under Q. Here, Z would be F_s-measurable, and such that the expectation (1) is well defined. A review of Theorem 2.6 justifies the easy finite-dimensional version of (1).
In particular, taking Z = 1 in (1), the price at time t of the zero-coupon

bond maturing at s is P(t, s) = E^Q [ exp( -∫_t^s r_u du ) | F_t ]. (2)

The doubly indexed process P is sometimes known as the discount function, or more loosely as the term structure of interest rates. The term structure is often expressed in terms of the yield curve. The continuouslycompounding yield \( y_{t,T} \) on a zero-coupon bond maturing at time \( T \) is defined by

\[ y_{t,T} = -\frac{\log(A_{t,T})}{T-t}.
\]

The term structure can also be represented in terms of forward interest rates, as explained in Section J.

In most of this chapter, we review conventional models of the behavior of the short rate \( r \) under a fixed equivalent martingale measure \( \mathbb{Q} \). In each case, \( r \) is modeled in terms of the standard Brownian motion \( B^{\mathbb{Q}} \) in \( \mathbb{R}^d \) under \( \mathbb{Q} \) that is obtained from \( B \) via Girsanov’s Theorem (Appendix D). The Notes cite more general models. We will characterize the term structure and the pricing of term-structure derivatives, securities whose payoffs depend on the term structure.

# B. One-Factor Term-Structure Models

We begin with one-factor term-structure models, by which we mean models of the short rate \( r \) given by an SDE of the form

\[ dr_t = \mu(r_t, t) \, dt + \sigma(r_t, t) \, dB^{\mathbb{Q}}_t, \tag{3}
\]

where \( \mu : \mathbb{R} \times [0,T] \rightarrow \mathbb{R} \) and \( \sigma : \mathbb{R} \times [0,T] \rightarrow \mathbb{R}_+ \) satisfy technical conditions guaranteeing the existence of a solution to (3) such that for all \( t \) and \( s > t \), the price \( A_{t,s} \) of the zero-coupon bond maturing at \( s \) is finite and well defined by (2). For simplicity, we can take \( d = 1 \).

The one-factor models are so named because the Markov property (under \( \mathbb{Q} \)) of the solution \( r \) to (3) implies from (2) that the short rate is the only state variable, or “factor,” on which the current yield curve

--

Table 7.1. Common Single-Factor Model Parameters

Model \( \kappa_0 \) \( \kappa_1 \) \( \kappa_2 \) \( H_0 \) \( H_1 \) \( \gamma \)
Cox-Ingersoll-Ross \( \varepsilon \) \( \varepsilon \) \( \varepsilon \) 0 0.5
Pearson-Sun \( \varepsilon \) \( \varepsilon \) \( \varepsilon \) \( \varepsilon \) 0.5 Dothan \( \varepsilon \) \( \varepsilon \) 1.0
Brennan-Schwartz \( \varepsilon \) \( \varepsilon \) \( \varepsilon \) 1.0 Merton (Ho-Lee) D \( \varepsilon \) 1.0 Vasicek D D D 1.0
Black-Karasinski D \( \varepsilon \) \( \varepsilon \) 1.0 Constantinides-Ingersoll \( \varepsilon \) 0.615

depends. That is, for all \( t \) and \( s > t \), we can write \( A_{t,s} = F(t,s,r_t) \), for some fixed \( F : [0,T] \times [0,T] \times \mathbb{R} \rightarrow \mathbb{R} \).

Table 7.1 shows many of the parametric examples of one-factor models appearing in the literature, with their conventional names. Each of these models is a special case of the SDE

\[ dr_t = [\kappa_0(t) + \kappa_1(r_t - e^{\kappa_2(t)})] \, dt + [H_0(t) + H_1(t)r_t]^{\gamma} \, dB^{\mathbb{Q}}_t, \]

for continuous functions \( \kappa_0, \kappa_1, \kappa_2, H_0 \), and \( H_1 \) on \( [0,T] \) into \( \mathbb{R} \), and for some exponent \( \gamma \in [0.5, 1.5] \). Coefficient restrictions, and restrictions on the space of possible short rates, are needed for the existence and uniqueness of solutions. For each model, Table 7.1 shows the associated exponent \( \gamma \), and uses the symbol “\( \varepsilon \)” to indicate those coefficients that appear in nonzero form. We can view a negative coefficient function \( \kappa_1 \) as a mean-reversion parameter, in that a higher short rate generates a lower drift, and vice versa. Empirically speaking, mean reversion is widely believed to be a useful attribute to include in single-factor short-rate models.

In most cases, the original versions of these models had constant coefficients, and were only later extended to allow \( \kappa_i(t) \) and \( H_i(t) \) to depend on \( t \) for practical reasons, such as calibration of the model to a given set of bond and option prices, as described in Section 12M. For example, with time-varying coefficients, the Merton model of the term structure is often called the Ho-Lee model. A popular special case of the Black-Karasinski model is the Black-Derman-Toy model, defined in Exercise 7.1. References to the literature are given in the Notes.

Each of these single-factor models has its own desirable properties, some of which will be reviewed below. It tends to depend on the application which of these, if any, is used in practice. The Notes cite some

of the empirical evidence regarding these single-factor models, in some cases strongly pointing toward multifactor extensions, to which we will turn later in this chapter.

For essentially any single-factor model, the term structure can be computed (numerically, if not explicitly) by taking advantage of the Feynman-Kac relationship between PDEs and SDEs given in Appendix E. Fixing for convenience the maturity date \( s \), the Feynman-Kac approach implies from (2), under technical conditions on \( \mu \) and \( \sigma \), that for all \( t \),

\[ A_{t,s} = f(r_t, t), \tag{4}
\]

where \( f \in C^{2,1}(\mathbb{R} \times [0,T)) \) solves the PDE

\[ f_t(x,t) + \mu(x,t) f_x(x,t) + \frac{1}{2}\sigma(x,t)^2 f_{xx}(x,t) - x f(x,t) = 0, \quad (x,t) \in \mathbb{R} \times [0,s), \tag{5}
\]

with boundary condition

\[ f(x,s) = 1, \quad x \in \mathbb{R}, \tag{6}
\]

where

\[
D f(x,t) = f_t(x,t) + \mu(x,t) f_x(x,t) + \frac{1}{2}\sigma(x,t)^2 f_{xx}(x,t).
\]

According to the results in Appendix E, in order for (4)–(6) to be consistent, it is enough that \( \mu \) and \( \sigma \) are nonnegative and that \( \mu \) and \( \sigma \) satisfy Lipschitz conditions in \( x \) and have derivatives \( \mu_x \) and \( \sigma_x \) that are continuous and satisfy growth conditions in \( x \). These conditions are not necessary and can be weakened. We note that the Lipschitz condition is violated for several of the examples considered in Table 7.1, such as the Cox-Ingersoll-Ross model, which must be treated on a case-by-case basis.

The PDE (5)–(6) can be quickly solved using numerical algorithms described in Chapter 12. If \( \mu \) and \( \sigma \) do not depend on \( t \), then, for any calendar time \( t \) and any time \( u < s \) remaining to maturity, we can also view the solution \( f \) to (5)–(6) as determining the price \( f(r_t, s-u) = A_{t, t+u} \) at time \( t \) of the zero-coupon bond maturing at \( t + u \), so that a single function \( f \) describes the entire term structure at any time.

# C. The Gaussian Single-Factor Models

A subset of the models considered in Table 7.1, those with \( \kappa_2 = H_1 = 0 \), are Gaussian, in that the short rates \( \{r(t_1), \dots, r(t_n)\} \) at any finite set \( \{t_1, \dots, t_n\} \) of times have a joint normal distribution under \( \mathbb{Q} \). This follows

--

from the properties of linear stochastic differential equations reviewed in Appendix E. Special cases are the Merton (often called “Ho-Lee”) and Vasicek models.

For the Gaussian model, we can show that bond-price processes are log-normal (under \( \mathbb{Q} \)) by defining a new process \( y \) satisfying \( dy_t = -r_t \, dt \), and noting that \( (r, y) \) is the solution of a two-dimensional linear stochastic differential equation, in the sense of Appendix E. Thus, for any \( t \) and \( s > t \), the random variable \( y_s - y_t = -\int_t^s r_u \, du \) is normally distributed. Under \( \mathbb{Q} \), the mean \( m(t,s) \) and variance \( v(t,s) \) of \( -\int_t^s r_u \, du \), conditional on \( \mathcal{F}_t \), are easily computed in terms of \( r_t, \kappa_0, \kappa_1, \) and \( H_0 \). From the results for linear SDEs in Appendix E, the conditional variance \( v(t,s) \) is deterministic and the conditional mean \( m(t,s) \) is of the form \( \alpha(t,s) + \beta(t,s)r_t \), for coefficients \( \alpha(t,s) \) and \( \beta(t,s) \) whose calculation is left as an exercise. It follows that

\[
A_{t,s} = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^s r_u \, du} \mid \mathcal{F}_t]
= \exp\left(m(t,s) + \frac{1}{2}v(t,s)\right)
= \exp\left(\alpha(t,s) + \beta(t,s)r_t\right), \tag{7}
\]

where \( \alpha(t,s) = \alpha(t,s) + v(t,s)/2 \). Because \( r \) is normally distributed under \( \mathbb{Q} \), this means that any zero-coupon bond price is log-normally distributed under \( \mathbb{Q} \). Using this property, a further exercise requests explicit computation of bond-option prices in this setting, along the lines of the original Black-Scholes formula. Aside from the simplicity of the Gaussian model, this explicit computation is one of its main advantages in applications.

An undesirable feature of the Gaussian model is that it implies (for \( H_1 \) everywhere nonzero) that the short rate and yields on bonds of any maturity are negative with positive probability at any future date. While negative interest rates are sometimes plausible when expressed in “real” (consumption numeraire) terms, it is common in practice to express term structures in nominal terms, relative to the price of money. In nominal terms, negative bond yields imply a kind of arbitrage. In order to describe this arbitrage, we can formally view money as a security with no dividends whose price process is identically equal to 1. If a particular zero-coupon bond were to offer a negative yield, consider a short position in the bond (that is, borrowing) and a long position of an equal number of units of money, both held to the maturity of the bond. With a negative bond yield,

the initial bond price is larger than 1, implying that this position is an arbitrage. Of course, the proposed alternative of everywhere positive interestrates, along with money, implies that the opposite strategy is an arbitrage if money can be freely shorted. One normally assumes that money is a special kind of security that cannot be shorted. (Indeed, the fact that money has a strictly positive price despite having no dividends means that shorting money is itself a kind of arbitrage.) To address properly the role of money in supporting nonnegative interest rates would therefore require a rather wide detour into monetary theory and the institutional features of money markets. It may suffice for our purposes to point out that money conveys certain special advantages, for example the ability to undertake certain types of transactions immediately, or with reduced transactions costs, which would imply a fee in equilibrium for the shorting of money.
Let us merely leave this issue with the sense that allowing negative interest rates is not necessarily “wrong,” but is somewhat undesirable. Gaussian short-rate models are nevertheless useful, and frequently used, because they are relatively tractable and in light of the low likelihood that they would assign to negative interest rates within a reasonably short time, with reasonable choices for the coefficient functions.

# D. The Cox-Ingersoll-Ross Model

One of the best-known single-factor term-structure models is the CoxIngersoll-Ross (CIR) model indicated in Table 7.1. For constant coefficient functions $K_y$, $K_x$, and $H_y$, the CIR drift and diffusion functions, $\mu$ and $\sigma$, may be written in the form

$\mu(x, t) = K(X - x)$; $\sigma(x, t) = C \sqrt{x}$, $x > 0$, (8)

for constants $k$, $x$ and $C$. Provided $k$ and $x$ are positive, there is a nonnegative solution to the SDE (3), based on a source cited in the Notes.
(Obviously, nonnegativity is important, if only for the fact of the square root in the diffusion.) Of course, we assume that $\gamma > 0$, and treat (5)
(6) as applying only to a short rate $x$ in $[0, \infty)$. Given $\gamma$, under $Q$, $r$ has a noncentral $\chi^2$ distribution with parameters that are known explicitly.
The drift $k(x - r)$ indicates reversion of $r$ toward a stationary risk-neutral mean $x$ at a rate $k$, in the sense that

$E_Q(r_s) = x + e^{-k(s-t)} (r_t - x)$,

which tends to $x$ as $s$ goes to $+\infty$. Additional properties of this model are discussed later in this chapter and in Section 10.1, where the coefficients

--

**Page 81**

$K$, $x$, and $C$ are calculated in a general-equilibrium setting in terms of the utility function and endowment of a representative agent. For the CIR model, it can be verified by direct computation of the derivatives that the solution for the term-structure PDE (5)-(6) is given by

$f(x, t) = e^{A(t,s)} e^{B(t,s)x}$, (9)

where

$A(t, s) = \frac{K}{\gamma^2} \left[ \log(2\gamma e^{\frac{\gamma^2(t-s)}{2}}) - \log((\gamma + K)(e^{\gamma(s-t)} - 1) + 2\gamma) \right]$, (10)

$B(t, s) = \frac{2(1 - e^{\gamma(s-t)})}{(\gamma + K)(e^{\gamma(s-t)} - 1) + 2\gamma}$, (11)

for $\gamma = (K^2 + 2C^2)^{1/2}$. We will later consider multifactor versions of the CIR model.

# E. The Affine Single-Factor Models

The Gaussian and Cox-Ingersoll-Ross models are special cases of singlefactor models with the property that the solution $f$ of the term-structure
PDE (5)-(6) is given in the exponential-affine form (9) for some coefficients $A(t,s)$ and $B(t, s)$ that are continuously differentiable in $s$. For all $t$ the yield $-\log[ f(x, t)]/(s - t)$ obtained from (9) is affine in $x$. We therefore call any such model an affine term-structure model. (A function
$g: \mathbb{R}^* \to \mathbb{R}$, for some $\ell$, is affine if there are constants $Q$ and $S$ in $\mathbb{R}$ such that for all $x$, $g(x) = Q + S \cdot x$.)

We can use the PDE (5) to characterize the drift and diffusion functions, $\mu$ and $\sigma^2$, underlying any affine model. Specifically, substituting (9)
into (5) and simplifying leaves, for each $(x, t) \in \mathbb{R} \times [0, s)$,

$B(t, s) \mu(x, t) = [1 - B_s(t, s)]x - A_s(t, s)$, (12)

where subscripts indicate partial derivatives. We will use (12) to deduce how $\mu(x, t)$ and $\sigma(x, t)$ depend on $x$. Suppose, for simplicity, that $\mu(x, t)$ and $\sigma(x, t)$ do not depend on $t$. Applying (12) at two possible maturity dates, say $s_1$ and $s_2$, we have the two linear equations in the two unknowns $\mu(x)$ and $\sigma^2(x)$:

$\mu(x) = \frac{A_s(t, s_1) + [1 - B_s(t, s_1)]x}{B(t, s_1)}$

$\mu(x) = \frac{A_s(t, s_2) + [1 - B_s(t, s_2)]x}{B(t, s_2)}$ (13)

--

**Page 82**

where

$\Delta(s_1, s_2) = \frac{B(t, s_1) B_s(t, s_2) - B(t, s_2) B_s(t, s_1)}{B(t, s_1) B(t, s_2)}$

Except at maturity dates $s_1$ and $s_2$ chosen so that $\Delta(s_1, s_2)$ is singular, we can conclude from (13) that $\mu(x)$ and $\sigma^2(x)$ must themselves be affine in $x$.

Going the other way, suppose that $\mu$ and $\sigma^2$ are affine in $x$, in that

$\mu(x, t) = K_0(t) + K_1(t)x$; $\sigma^2(x, t) = A_0(t) + A_1(t)x$.

Then we can recover an affine term-structure model by showing that the solution to (5)—(6) is of the affine form (9). Such a solution applies if there exists $(A, B)$ solving (12). The terms proportional to $x$ in (12) must sum to zero, for otherwise we could vary $x$ and contradict (12). This supplies us with an ordinary differential equation (ODE) for $B$:

$B_s(t, s) = 1 - K_1(t) B(t, s) - S A_1(t) B(t, s)^2$; $B(s, s) = 0$, (14)

whose boundary condition $B(s,s) = 0$ is dictated by (6) and (9). The ODE
(14) is a form of what is known as a Riccati equation. Solutions are finite given technical conditions on $K_1$ and $A_1$.

Likewise, the “intercept” term in (12), the term that is not dependent on $x$, must also be zero. Having solved for $B$ from (14), this gives us

$A(t, s) = -\int_t^s [K_0(u) B(u, s) + S A_0(u) B(u, s)^2] du$.

Again, the boundary condition $A(s, s) = 0$ is from (6) and (9). Thus, by integrating $A_s(u, s)$ with respect to $u$, we have

$a(t, s) = -\int_t^s [K_0(u) B(u, s) + S A_0(u) B(u, s)^2] du$, (15)

and technicalities aside, $\mu$ and $\sigma^2$ are affine in $x$ if and only if the term structure is itself affine in $x$. Sources cited in the Notes strengthen by allowing for time-inhomogeneity. Numerical solutions of the ODE (14), for example by discretization methods such as Runge-Kutta, are straightforward.

Then (15) can be solved by numerical integration. The special cases associated with the Gaussian model and the CIR model have explicit solutions for $A$ and $B$.

--

**Page 83**

We have shown, basically, that affine term-structure models are easily classified and solved. This idea is further pursued in a multifactor setting later in this chapter and in sources cited in the Notes.

From the above characterization, we know that the “affine class” of term-structure models includes those shown in Table 7.1 with $K_x = 0$ and $\gamma = 0.5$, including

(a) The Vasicek model, for which $H_y = 0$.
(b) The Cox-Ingersoll-Ross model, for which $H_y = 0$.
(c) The Merton (Ho-Lee) model, for which $K_x = H_y = 0$.
(d) The Pearson-Sun model.

For affine models with $H_y \neq 0$, existence of a solution to the SDE (3)
requires coefficients $(\kappa, K)$ with

$\frac{A_0(t)}{K_1(t)} \geq -\frac{H_0(t)}{H_1(t)} \quad \text{for all } t$. (16)

$K_1(t) = K_y(t) \Delta > 0$.

This condition guarantees the existence of a solution $r$ to the SDE (3)
with $r(t) > -H_0(t)/H_1(t)$ for all $t$.

# F. Term-Structure Derivatives

We return to the general one-factor model (3) and consider one of its most important applications, the pricing of derivative securities. Suppose a derivative has a payoff at some given time $s$ defined by $g(r)$. By the definition of an equivalent martingale measure, the price at time $t$ for such a security is

$F(r, t) = E_Q \left[ e^{-\int_t^s r_u du} g(r_s) \right]$.

The Feynman-Kac PDE results of Appendix E give technical conditions on
$\mu$, $\sigma$, and $g$ under which $F$ solves the PDE, for $(x, t) \in \mathbb{R} \times [0, s)$,

$F_t(x, t) + F_x(x, t) \mu(x, t) + \frac{1}{2} F_{xx}(x, t) \sigma^2(x, t) - x F(x, t) = 0$, (17)
with boundary condition $F(x, s) = g(x)$, $x \in \mathbb{R}$. (18)

Some examples follow, abstracting from many institutional details.

--

**Page 84**

(a)
(b)
(c)
(d)
(e)

A European option expiring at time $s$ on a zero-coupon bond maturing at some later time $u$, with strike price $p$, is a claim to $(f(s, u) - p)^+$ at $s$. The valuation of the option is given, in a one-factor setting, by the solution $F$ to (17)-(18), with $g(x) =
[f(x, s) - p]^+$, where $f(x, s)$ is the price at time $s$ of a zero-coupon bond maturing at $u$.

A forward-rate agreement (FRA) calls for a net payment by the fixedrate payer of $c^* - c(s)$ at time $s$, where $c^*$ is a fixed payment and
$c(s)$ is a floating-rate payment for a time-to-maturity $\delta$, in arrears,meaning that \( c(s) = A \delta s \). Here, 1 is the simple interest rate applying at time \( s - \delta \) for loans maturing at time \( s \). In practice, we usually have a time to maturity \( \delta \) of one-quarter or one-half year. When originally sold, the fixed-rate payment \( c^* \) is usually set so that the FRA is at market, meaning of zero market value.

An interest-rate swap is a portfolio of FRAs maturing at a given increasing sequence \( t(1), t(2), \ldots, t(m) \) of coupon dates. The intercoupon interval \( t(i) - t(i-1) \) is usually 3 months or 6 months. The associated FRA for date \( t(i) \) calls for a net payment by the fixed-rate payer of \( c^* - c(t(i)) \), where the floating-rate payment received is \( c(t(i)) = A n_i \delta_i - 1 \), and the fixed-rate payment \( c^* \) is the same for all coupon dates. At initiation, the swap is usually at market, meaning that the fixed rate \( c^* \) is chosen so that the swap is of zero market value. Ignoring default risk and market imperfections, this would imply, as can be shown as an exercise, that the fixed-rate coupon \( c^* \) is the par coupon rate. That is, the at-market swap rate \( c^* \) is set at the origination date \( t \) of the swap so that

\[
\sum_{i=1}^m c^* \delta(t_i) P(t, t_i) + P(t, t_m) = 1, \]

meaning that \( c^* \) is the coupon rate on a par bond, one whose face value and initial market value are the same.

A cap can be viewed as a portfolio of “caplet” payments of the form \( (c(t(i)) - c^*)^+ \), for a sequence of payment dates \( t(1), t(2), \ldots, t(m) \) and floating rates \( c(t(i)) \) that are defined as for a swap. The fixed rate \( c^* \) is set with the terms of the cap contract. Exercise 7.13 explores the valuation of caps.

A floor is defined symmetrically with a cap, replacing \( (c(t(i)) - c^*)^+ \) with \( (c^* - c(t(i)))^+ \).

(f) A swaption is an option to enter into a swap at a given strike rate \( c^* \) at some exercise time. If the future time is fixed, the swaption is European. An important variant, the Bermudan swaption, allows exercise at any of a given set of successive coupon dates.

Path-dependent derivative securities, such as mortgage-backed securities, sometimes call for additional state variables. Some interest-rate derivative securities are based on the yields of bonds that are subject to some risk of default, in which case the approach must be modified by accounting for default risk, as illustrated in Chapter 11.

There are relatively few cases of practical interest for which the PDE (17)-(18) can be solved explicitly. Chapters 8 and 12 review some numerical solution techniques.

# G. The Fundamental Solution

Based on the results of Appendix E, under technical conditions we can also express the solution \( F \) of the PDE (17)-(18) for the value of a derivative term-structure security in the form

\[
F(x, t) = \int_{-\infty}^{\infty} G(x, t, y, s) g(y) \, dy, \tag{19}
\]

where \( G \) is the fundamental solution of the PDE (17). Some have called \( G \) the Green’s function associated with (17), although that terminology is not rigorously justified. From (19), for any time \( s > t \) and any interval \( [y(1), y(2)] \),

\[ \int_{y(1)}^{y(2)} G(x, t, y, s) \, dy \]

is the price at time \( t \) of a security that pays one unit of account at time \( s \) in the event that \( r_s \) is in \( [y(1), y(2)] \). For example, the current price \( P(t, s) \) of the zero-coupon bond maturing at \( s \) is given by \( \int_{-\infty}^{\infty} G(x, t, y, s) \, dy \).

One can compute the fundamental solution \( G \) by solving a PDE that is “dual” to (5)-(6), in the following sense. As explained in Appendix E, under technical conditions, for each \( (x, t) \) in \( \mathbb{R} \times [0, T) \), a function \( \psi(y, s) \) in \( C^{2,1}(\mathbb{R} \times (t, T]) \) is defined by \( \psi(y, s) = G(x, t, y, s) \), and solves the forward Kolmogorov equation (also known as the Fokker-Planck equation):

\[
\frac{\partial}{\partial s} \psi(y, s) = \mathcal{L}^* \psi(y, s) = 0, \tag{20}
\]

where

\[
\mathcal{L}^* = \frac{1}{2} \frac{\partial^2}{\partial y^2} [a^2(y, s)] - \frac{\partial}{\partial y} [h(y, s)].
\]

The “intuitive” boundary condition for (20) is obtained from the role of \( G \) in pricing securities. Imagine that the current short rate at time \( t \) is \( x \), and consider an instrument that pays one unit of account immediately, if and only if the current short rate is some number \( y \). Presumably this contingent claim is valued at 1 unit of account if \( x = y \), and otherwise has no value. From continuity in \( s \), one can thus think of \( \psi(\cdot, s) \) as the density at time \( s \) of a measure on \( \mathbb{R} \) that converges as \( s \downarrow t \) to a probability measure \( \nu \) with \( \nu(\{x\}) = 1 \), sometimes called the Dirac measure at \( x \). Although this initial boundary condition on \( \psi \) can be made more precise, we leave that to sources cited in Appendix E. An implementation of this boundary condition for a numerical solution of (20) is spelled out in Chapter 12. A discrete-time analogue is found in Chapter 3, where we provided an algorithm for computing the fundamental solutions for the Black-Derman-Toy and Ho-Lee models.

Given the fundamental solution \( G \), the derivative asset price function \( F \) is more easily computed by numerically integrating (19) than from a direct numerical attack on the PDE (17)-(18). Thus, given a sufficient number of derivative securities whose prices must be computed, it may be worth the effort to compute \( G \). Some numerical methods for calculating \( F \) and \( G \) are indicated in Chapter 12.

A lengthy argument given by a source cited in the Notes shows that the fundamental solution \( G \) of the Cox-Ingersoll-Ross model (8) is given explicitly in terms of the parameters \( k, \kappa \), and \( C \) by

\[
G(x, t, y, s) = \frac{P(s)}{C^2} \left( \frac{y}{x} \right)^{\nu/2} e^{-(y + x e^{-k(s-t)})/C^2} I_\nu \left( \frac{2 \sqrt{x y e^{-k(s-t)}}}{C^2} \right), \]

where \( \nu = (2\kappa/C^2) - 1 \), \( n = (k - \nu \kappa)/C^2 \), and \( I_\nu(\cdot) \) is the modified Bessel function of the first kind of order \( \nu \). The same source gives explicit solutions for the fundamental solutions of other models. For time-independent \( L \) and \( a \), as with the CIR model, we have, for all \( t \) and \( s > t \), \( G(x, t, y, s) = G(x, 0, y, s - t) \).

# H. Multifactor Models

The one-factor model (3) for the short rate is limiting. Even a casual review of the empirical properties of the term structure, some of which can be found in papers cited in the Notes, shows the significant potential improvements in fit offered by a multifactor term-structure model. While terminology varies from place to place, by a “multifactor” model, we mean a model in which the short rate is of the form \( r_t = R(X_t, t) \), \( t \geq 0 \), where \( X \) is an Itô process in some subset \( D \) of \( \mathbb{R}^k \) solving a stochastic differential equation of the form

\[ dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dB_t, \tag{21}
\]

where the given functions \( R, \mu \), and \( \sigma \) on \( D \times [0, \infty) \) into \( \mathbb{R}, \mathbb{R}^k \), and \( \mathbb{R}^{k \times m} \), respectively, satisfy enough technical regularity to guarantee that (21) has a unique solution and that the term structure (2) is well defined. (Sufficient conditions are given in Appendix E.) In empirical applications, one often supposes that the state process \( X \) also satisfies a stochastic differential equation under the probability measure \( P \), in order to exploit the time-series behavior of observed prices and price-determining variables in estimating the model. Examples are indicated in the Notes.

An interpretation of the role of the “state variables” is left open for the time being. For example, in an equilibrium model such as that considered in Chapter 10, some elements of the state vector \( X \) are sometimes latent, that is, unobservable to the modeler, except insofar as they can be inferred from prices that depend on the levels of \( X \). This latent-variable approach has been popular in much of the empirical literature on term-structure modeling. Another approach is to take some or all of the state variables to be directly observable variables, such as macroeconomic determinants of the business cycle and inflation, that are thought to play a role in determining the term structure. This approach has also been explored in the empirical literature. In many examples, one of the component processes \( X_1, \ldots, X_k \) is singled out as the short-rate process \( r \), whose drift and diffusion are allowed to depend on the levels of the other component processes.

A derivative security, in this setting, can often be represented in terms of some real-valued terminal payment function \( g \) on \( \mathbb{R}^k \), for some maturitydate s < T. By the definition of an equivalent martingale measure, the associated derivative security price is given from (1) by

\[
F(X_t, t) = \mathbb{E} \left[ \exp\left( - \int_t^s R(X_u, u) \, du \right) g(X_s) \right].
\]

Extending (17)—(18), under technical conditions given in Appendix E, we have the PDE characterization

\[
\mathcal{B}F(x, t) - R(x, t)F(x, t) = 0, \quad (x, t) \in D \times [0, s), \tag{22}
\]

with boundary condition

\[ F(x, s) = g(x), \quad x \in D, \tag{23}
\]

where

\[
\mathcal{B}F(x, t) = F_t(x, t) + F_x(x, t) w(x, t) + \frac{1}{2} \operatorname{tr} \left[ \sigma(x, t) \sigma(x, t)'' F_{xx}(x, t) \right].
\]

The case of a zero-coupon bond is \( g(x) = 1 \). Under technical conditions, we can also express the solution \( F \), as in (19), in terms of the fundamental solution \( G \) of the PDE (22), as discussed in Appendix E.

# I. Affine Term-Structure Models

A rich and tractable subclass of multifactor models are the affine term-structure models, for which the state process is an affine diffusion, defined by

\[ w(x, t) = \kappa_0(t) + \kappa_1(t) x, \tag{24}
\]

for \( \kappa_0(t) \in \mathbb{R}^k \) and \( \kappa_1(t) \in \mathbb{R}^{k \times k} \), and by taking, for each \( i \) and \( j \) in \( \{1, \ldots, k\} \),

\[
\left[ \sigma(x, t) \sigma(x, t)'' \right]_{ij} = H_{ij}(t) + \sum_{l=1}^k H_{ijl}(t) x_l, \tag{25}
\]

for \( H_{ij}(t) \in \mathbb{R} \) and \( H_{ijl}(t) \in \mathbb{R} \). One can also allow the coefficient functions \( \kappa_0 = (\kappa_{00}, \kappa_{01}) \) and \( \kappa_1 = (\kappa_{10}, \kappa_{11}) \) to depend on \( t \); we ignore that for notational simplicity. Given affine coefficients \( (H, \kappa) \), a natural state space \( D \subset \mathbb{R}^k \) for this process is set by the obvious requirement that \( \left[ \sigma(x, t) \sigma(x, t)'' \right]_{ii} > 0 \) for all \( x \) in \( D \). Thus, given \( H \), we choose the state space

\[
D = \left\{ x \in \mathbb{R}^k : H_i + \sum_{j=1}^k H_{ij} x_j > 0, \; i \in \{1, \ldots, k\} \right\}. \tag{26}
\]

Conditions cited in the Notes on the coefficients \( (H, \kappa) \) that ensure existence of a unique solution \( X \) to (21) that is valued in \( D \) also ensure existence of the affine process.

An example is the “multifactor CIR” model, defined by

\[ dX_t = \kappa(\bar{X} - X_t) dt + C \sqrt{X_t} \, dB_t^Q, \quad X_{t0} > 0, \tag{27}
\]

where \( \kappa > 0 \), \( \bar{X} > 0 \), and \( C > 0 \) are positive constants playing the same respective roles as \( \kappa \), \( \bar{X} \), and \( C \) in the one-factor CIR model (8). Given the independence under \( Q \) of \( B_t^{Q,1}, \ldots, B_t^{Q,k} \), if we let \( R(x, t) = x_1 + \cdots + x_k \), then the multifactor CIR model generates the zero-coupon bond price \( f(x, t) \) for maturity date \( s \) given by

\[ f(x, t) = \exp\left[ \alpha(t, s) + \beta_1(t, s) x_1 + \cdots + \beta_k(t, s) x_k \right], \tag{28}
\]

where \( \alpha(t, s) = \alpha_1(t,s) + \cdots + \alpha_k(t,s) \), and where \( \alpha_i(t,s) \) and \( \beta_i(t, s) \) are the solution coefficients of the univariate CIR model with coefficients \( \kappa, \bar{X}, C \). More generally, we suppose that

\[ R(x, t) = \rho_0(t) + \rho_1(t)' x, \tag{29}
\]

for coefficients \( \rho_0(t) \in \mathbb{R} \) and \( \rho_1(t) \in \mathbb{R}^k \). For a fixed maturity date \( s \), we expect a solution \( f(X_t, t) \) for the price at time \( t \) of a zero-coupon bond maturing at time \( s \) to be of the exponential-affine form

\[ f(t) = \exp\left[ \alpha(t) + \beta(t)' x \right], \tag{30}
\]

for deterministic \( \alpha(t) \) and \( \beta(t) \). For notational simplicity, we suppress the maturity date \( s \) from the notation for \( \alpha \) and \( \beta \), and we let \( \beta(t)'' H(t) \beta(t) \) denote the vector in \( \mathbb{R}^k \) whose \( l \)-th element is \( \sum_{i,j} \beta_i(t) H_{ijl}(t) \beta_j(t) \). After substituting the candidate solution (30) into the PDE (22), extending from the single-factor case, we conjecture that \( f \) satisfies the \( k \)-dimensional ordinary differential equation, analogous to (14), given by

\[
\beta'(t) = \rho_1 - \kappa_1' \beta(t) - \frac{1}{2} \beta(t)'' H(t) \beta(t), \tag{31}
\]

with the boundary condition \( \beta(s) = 0 \) determined by (30) and the requirement that \( f(x,s) = 1 \). We have repeatedly used a separation-of-variables argument: If \( a + b'x = 0 \) for all \( x \) in some open subset of \( \mathbb{R}^k \), then \( a \) and \( b \) must be zero.

The ODE (31) is, as with the single-factor affine models, a Riccati equation. Solutions are finite given technical conditions on \( \kappa \) and \( H \). In some cases, an explicit solution is possible. One can alternatively apply a numerical ODE solution method, such as Runge-Kutta.

Likewise, we find that

\[
\alpha'(t) = \rho_0(t) + \kappa_0(t)' \beta(t) - \frac{1}{2} \beta(t)'' H_0(t) \beta(t), \tag{32}
\]

with the boundary condition \( \alpha(s) = 0 \). One integrates (32) to get

\[
\alpha(t) = \int_t^s \left[ \rho_0(u) + \kappa_0(u)' \beta(u) - \frac{1}{2} \beta(u)'' H_0(u) \beta(u) \right] du. \tag{33}
\]

Numerical integration is an easy and fast method for treating (33) when explicit solutions are not at hand.

This affine class of term-structure models extends to allow for time-dependent coefficients \( (\kappa, H, \rho) \) and to cases with jumps in the state process \( X \), as cited in the Notes. As we shall see in Chapter 8, one can also analytically solve for the transition distribution of an affine state-variable process, and for the associated prices of options on zero-coupon bonds and other securities, using Fourier-transform methods. Affine models, moreover, are used extensively in the analysis of default timing and the related valuation of defaultable bonds, as explained in Chapter 11.

# J. The HJM Model of Forward Rates

In modeling the term structure, we have so far taken as the primitive a model of the short-rate process of the form \( r_t = R(X_t, t) \), where (under some equivalent martingale measure) \( X \) solves a given stochastic differential equation. (In the one-factor case, one usually takes \( r_t = X_t \).) This approach has the advantage of a finite-dimensional state space. For example, with this state-space approach one can compute certain derivative prices by solving PDEs. This approach is also amenable to standard econometric methods for the estimation of coefficients from time-series data, as indicated in the Notes.

An alternative approach is to directly model the stochastic behavior of the entire term structure of interest rates. This is the essence of the Heath–Jarrow–Morton (HJM) model. The remainder of this section is a summary of the basic elements of the HJM model. The following section, the exercises, and sources cited in the Notes provide many extensions and details.

The forward price at time \( t \) of a zero-coupon bond for delivery at time \( \tau > t \) with maturity at time \( s > \tau \) is (in the absence of arbitrage) given by \( A_{t,s} / A_{t,\tau} \), the ratio of zero-coupon bond prices at maturity and delivery, respectively. Proof of this is left as an exercise. The associated forward rate is defined by

\[ f(t, \tau, s) = - \frac{\log(A_{t,s}) - \log(A_{t,\tau})}{s - \tau}. \tag{34}
\]

which can be viewed as the continuously compounding yield of the bond bought forward. The instantaneous forward rate, when it exists, is defined for each time \( t \) and forward delivery date \( \tau > t \) by

\[ f(t, \tau) = \lim_{s \downarrow \tau} f(t, \tau, s). \tag{35}
\]

Thus, the instantaneous forward-rate process \( f \) exists (and is an adapted process) if and only if, for all \( t \), the discount \( A_{t,s} \) is differentiable with respect to \( s \).

From (34) and (35), we arrive at the ordinary differential equation

\[
\frac{\partial}{\partial s} \log A(t,s) = - f(t,s), \]

with the boundary condition \( A(t, t) = 1 \), with the solution

\[
A(t,s) = \exp\left( - \int_t^s f(t,u) \, du \right). \tag{36}
\]

The term structure can thus be recovered from the instantaneous forward rates, and vice versa.

Given a stochastic model \( f \) of forward rates, we will assume that the short-rate process \( r \) is defined by \( r_t = f(t, t) \), the limit of bond yields as maturity goes to zero. Justification of this assumption can be given under technical conditions cited in the Notes.

We first fix a maturity date \( s \) and model the one-dimensional forward-rate process \( \{f(t,s) : 0 < t < s\} \). We suppose that \( f(\cdot, s) \) is an Itô process, meaning that

\[ df(t,s) = \mu(t,s) \, dt + \sigma(t,s) \, dB_t, \quad 0 < t < s, \tag{37}
\]

where \( \mu(\cdot, s) = \{\mu(t,s) : 0 < t < s\} \) and \( \sigma(\cdot, s) = \{\sigma(t,s) : 0 \leq t \leq s\} \) are adapted processes valued in \( \mathbb{R} \) and \( \mathbb{R}^d \), respectively, such that, almost surely, \( \int_0^s |\mu(t, s)| \, dt < \infty \) and \( \int_0^s \|\sigma(t, s)\|^2 \, dt < \infty \).

There is an important consistency relationship between \( \mu \) and \( \sigma \). Under purely technical conditions, it must be the case that

\[
\mu(t, s) = \sigma(t, s) \cdot \int_t^s \sigma(t, u) \, du. \tag{38}
\]

This risk-neutral drift restriction on forward rates will be shown at the end of this section. For now, let us point out that knowledge of the initial forward rates \( \{ f(0, s) : 0 < s < T \} \) and the forward-rate “volatility” process \( \sigma \) is enough to determine all bond and interest-rate derivative price processes. That is, given (38), we can use the definition \( r_t = f(t, t) \) of the short rate to obtain

\[ r_t = f(0, t) + \int_0^t \sigma(v,t) \cdot \int_v^t \sigma(v, u) \, du \, dv + \int_0^t \sigma(v, t) \cdot dB_v, \tag{39}
\]

assuming that this process exists and is adapted. We can see that if \( \sigma \)(B) Suppose, for arbitrary \( t \) and \( s \), the price at time \( t \) of a zero-coupon bond maturing at time \( s \) is of the form \( P e^{A(i,t,s)+B(i,t,s)r(t)} \), for deterministic coefficients \( A(i,t,s) \) and \( B(i,t,s) \). Can you guess some form, under technical conditions, of an associated equivalent martingale measure \( Q \), after some convenient deflation, that provides this type of term structure? What is the most general consistent form that you can guess?

7.13 (Cap Pricing). Show that a claim to the caplet payoff \( (c(t_i) - c^*)^+ \) at time \( t_i \) as defined in Section F, may be viewed as a European put option, exercisable at time \( t_{i-1} \), on a zero-coupon bond maturing at time \( t_i \). Now, in the Vasicek setting, provide a formula for the price at time 0 of a cap, which is the portfolio of caplets defined in Section F.

7.14 (The Market Model and Cap Pricing). In the setting of Section A, let \( \{A_{t,s}\} \) be a given model of the term structure of discounts, and let \( s \rightarrow A_{t,s}/A_{t,T} \) define the associated forward bond prices, as in Section J. For each given date \( s \), using as a numeraire the bond maturing at date \( s \), we know that the absence of arbitrage is tantamount to the existence of an equivalent martingale measure \( Q_s \), after deflation by \( A_{t,s} \). That is, for each \( x > s \), the bond-price process \( \{A_{t,x}/A_{t,s} : 0 \leq t < s\} \) is a \( Q_s \)-martingale. We recall that \( Q_s \) is called the forward measure for maturity \( s \).

(A) Suppose, for each \( s < T \), that such a forward measure \( Q_s \) exists. Fixing \( s \), show, under technical integrability conditions that you will supply, that for each given maturity date \( u > s \),

\[
\frac{d}{dt} \log A_{t,u} = \gamma_u(t,s,u) dW_t^{s}, \]

for some adapted \( \mathbb{R}^d \)-valued process \( \{\gamma(t,s,u) : 0 < t < s\} \) such that the stochastic integral is well defined, where \( W^s \) is a particular standard Brownian motion in \( \mathbb{R}^d \) under \( Q_s \).

(B) Given the model (61) for forward bond-price processes, consider, for each fixed date \( s \) and tenor \( \delta \), the \( \delta \)-tenor forward rate \( L(t,s) \) defined by

\[
1 + L(t,s)\delta = \frac{A_{t,s}}{A_{t,s+\delta}}, \]

which is the convention by which discrete-tenor forward rates are quoted in practice. In practice, \( \delta \) is typically 3 months, 6 months, or 1 year. The rate \( L(s,s) \) is the spot \( \delta \)-tenor rate for maturity at \( s + \delta \), sometimes called the LIBOR rate, because of the quotation method used for the London Inter-Bank Offering Rate. Calculate a process \( \Lambda(\cdot, s) = \{\Lambda(t,s) : 0 < t < s\} \) for which

\[ dL(t,s) = L(t,s)\Lambda(t,s) dW_t^{s}.
\]

(C) Suppose that \( \Lambda(\cdot, s) \) is deterministic, and that \( L(0,s) \) is strictly positive. Calculate explicitly the price at time \( t \) of a caplet paying \( \delta(L(s,s) - L)^* \) at the settlement date \( s + \delta \), for some strike rate \( L \). (This is the common payment convention in current market practice, as explained in Section F.)

# Notes

General treatments of term-structure modeling and related derivative pricing issues are offered by Garbade (1996), Moreleda (1997), DeMunnik (1992), Musiela and Rutkowski (1997), and Sundaresan (1997). Van Horne (1993) describes the general institutional features of fixed-income security markets.

(B-C) The Gaussian short-rate model appears in Merton (1974), who originated much of the approach taken in this chapter. Pye (1966) has an early precursor of modern term-structure modeling. Ho and Lee (1986) extended the model and developed the idea of calibration of the model to the current yield curve. Option evaluation and other applications of the Gaussian model are provided by Carverhill (1988), Jamshidian (1989a,b,d, 1991a, 1993b), and El Karoui and Rochet (1989). Jamshidian (1989b) developed the forward-measure approach for this purpose. See also Davis (1998), El Karoui and Rochet (1989), Elliott and der Hoek (1999), and Schroder (1999). The calibration idea, reviewed in Section 12M, has been further developed by Black, Derman, and Toy (1990), Hull and White (1990a, 1993), and Black and Karasinski (1991), among others. The Black-Derman-Toy model was shown in a discrete-time version in Exercise 3.12.

Exercise 12.6 shows convergence of the discrete-time Black-Derman-Toy model, with appropriate parameters, to the continuous-time “log-normal” model shown in Exercise 7.1. Other models include that of Courtadon (1982).

(D) The CIR term-structure model of Cox, Ingersoll, and Ross (1985b) was developed in a general-equilibrium setting, as explained in Chapter 10. It was also later developed as a primitive arbitrage-based term-structure model by Richard (1978). One can see that the associated CIR short-rate process exists from the results of Yamada and Watanabe (1971) reviewed in Appendix E. In order to apply their results, we can let \( a(x) = 0 \) for \( x < 0 \). The nonnegativity of solutions is then implied by the fact that zero is a natural boundary, in the sense of Dynkin and Skorohod (1972). Feller (1951) solved for the Laplace transform of the distribution of the CIR interest rate \( r_t \). The associated density was calculated by Yang (1990), according to a footnote of Richard (1978). Further characterization is given in Cox, Ingersoll, and Ross (1985b), Cherubini (1993), Cherubini and Esposito (1992), Deelstra and Delbaen (1994, 1995), Delbaen (1993), Gibbons and Sun (1986), Jamshidian (1995), Nelson and Ramaswamy (1989), and Rogers (1993).

Sun (1992) provides a discrete-time model that converges with shrinking period length to the CIR model. For additional results in a CIR setting, including analytic treatment of time-varying coefficients, see Maghsoodi (1996a, b, 1997a, b).

(E) The idea that an affine term-structure model is typically associated with affine drift and squared diffusion is foreshadowed in Cox, Ingersoll, and Ross (1985b) and Hull and White (1990a), and is explicit in Brown and Schaefer (1994a).

Filipović (1999a) provides a definitive result for affine term-structure models in a one-dimensional state space, based in part on the characterization of continuous-branching processes with immigration by Kawazu and Watanabe (1971).

Examples of the one-dimensional affine class include those of Carverhill (1988), Chen (1996), Cox, Ingersoll, and Ross (1985b), Dybvig (1988), Frachot (1996), Jamshidian (1989a,b,d, 1991a), Pearson and Sun (1994), Selby and Strickland (1993), and Vasicek (1977). Pearson and Sun (1994) refer to their model as the translated CIR model, for obvious reasons.

(F) Applied general treatments of term-structure derivatives include those of Garbade (1996), Moreleda (1997), DeMunnik (1992), Musiela and Rutkowski (1997), and Sundaresan (1997). Swap markets are analyzed by Brace and Musiela (1994b), Carr (1993b), Duffie and Huang (1996), El Karoui and Geman (1994), and Sundaresan (1997). For institutional and general economic features of the swap markets, see Lang, Litzenberger, and Liu (1996) and Litzenberger (1992). For the valuation of caps, see, for example, Chen and Scott (1995), Clewlow, Pang, and Strickland (1997), Miltersen, Sandmann, and Sondermann (1997), and Scott (1996b). Jamshidian (1999) and Rutkowski (1996, 1998) offer general treatments of LIBOR (London Interbank Offering Rate) derivative modeling.

On the valuation of other specific forms of term-structure derivatives, see Artzner and Roger (1993), Bajeux-Besnainou and Portait (1998), Brace and Musiela (1994b), Chacko and Das (1998), Chen and Scott (1992b, 1993b), Cherubini and Esposito (1995), Chesney, Elliott, and Gibson (1993), Cohen (1995), Daher, Romano, and Zacklad (1992), Décamps and Rochet (1997), El Karoui, Lepage, Myneni, Roseau, and Viswanathan (1991a,b), Turnbull (1993), Fleming and Whaley (1994) (wildcard options), Ingersoll (1977) (convertible bonds), Jamshidian (1993a, 1994) (diff swaps and quantos), Jarrow and Turnbull (1994), Longstaff (1990) (yield options), and Turnbull (1994).

On the valuation of American bond options, see Andersen and Andreasen (1999), Büttler (1995), Battler and Waldvogel (1996), Gatarek and Musiela (1995), Grosen and Jorgensen (1995), Jamshidian (1989a, c), Jorgensen (1996), Longstaff (1990).and Schwartz (1998), Pedersen (1999), and Tanudjaja (1995).

Cox, Ingersoll, and Ross (1981b), Duffie and Stanton (1988), and Grinblatt and Jegadeesh (1996) consider the relative pricing of futures and forwards.
Apelfeld and Conze (1990) study the term structure under imperfect information using filtering theory, extending the work of Dothan and Feldman (1986).
Additional fixed-income derivative pricing issues are considered in Chapter 8.
Derivative hedging issues are also considered by Jarrow and Turnbull (1997a), and Jaschke (1997).

(G) Applications to term-structure modeling of the fundamental solution, sometimes erroneously called the Green’s function, are illustrated by Btittler and
Waldvogel (1996), Dash (1989), Beaglehole (1990), Beaglehole and Tenney
(1991), Dai (1994), and Jamshidian (1991c). The fundamental solution for the
Dothan (log-normal) short-rate model can be deduced from the form of the solution by Hogan (1993a) of what he calls the “conditional discounting function.” Chen (1996) provides the fundamental solution for his three-factor affine model. Steenkiste and Foresi (1999) provide a general treatment of fundamental solutions of the PDE for affine models. The summary here is standard. For more on technical details and references, see, for example, Karatzas and Shreve (1988).

(H-I) Duffie and Kan (1996) provide a characterization of multifactor affine term-structure models. Affine multifactor term-structure models include those of
Balduzzi, Das, and Foresi (1998), Balduzzi, Das, Foresi, and Sundaram (1996),
Berardi and Esposito (1999), Chen (1996), Cox, Ingersoll, and Ross (1985b), Dai and Singleton (2000), Heston (1988b), Langetieg (1980), Longstaff and Schwartz
(1992, 1993), Pang and Hodges (1995), and Selby and Strickland (1993).
Filipovié (1999a) offers an example in a multidimensional setting of a termstructure model in which yields are affine in diffusion state variables that do not solve an affine stochastic differential equation.

The valuation of discount bond options and caps in an affine setting, using
Fourier-transform methods, is pursued by Chen and Scott (1995), Duffie, Pan, and Singleton (2000), Nunes, Clewlow, and Hodges (1999), and Scaillet (1996).
The valuation of path-dependent derivatives in an affine setting is considered by Leblanc and Scaillet (1998). Steenkiste and Foresi (1999) provide a general treatment of fundamental solutions of the PDE for affine models. For a RungeKutta method of numerically solving an ODE such as (31), see Press, Flannery,
Teukolsky, and Vetterling (1993). For additional general discussion of affine termstructure models, see Dai and Singleton (2000), Duffee (1999b), Duffie, Pan, and
Singleton (2000), Pedersen (1997), and Steenkiste and Foresi (1999).

Empirical estimation of various forms of affine term-structure models is pursued by Brown and Schaefer (1994b), Chan, Karolyi, Longstaff, and Saunders
(1992), Chen and Scott (1992a, 1993a), Dai (1995, 1996), Dai and Singleton
(2000), Duan and Simonato (1993), Duffee (1999b), Duffie and Singleton (1997),
Gibbons and Ramaswamy (1993), Heston (1989), DeMunnik (1992), Lesne
(1995), Longstaff and Schwartz (1993), Pearson and Sun (1994), Pennacchi
(1991), Rogers and Stummer (1994), Singh (1995), Stambaugh (1988), and
Vasicek (1995). Further analysis of the affine model with regard to transform methods for option valuation and other applications is provided in Chapter 8 and by Duffie, Pan, and Singleton (2000), Liu, Pan, and Pedersen (1999), and Singleton (1999).

(J) El Karoui, Myneni, and Viswanathan (1995), Constantinides (1992),
(1993), Myneni, and Viswanathan (1992), Jamshidian (1996a), and Rogers
(1993) characterize a model in which the short rate is a linear-quadratic form multivariate Markov Gaussian process. This model clearly overlaps with the general affine model, under a change of variables, although the extent to which a model can be developed that fully nests both affine and quadratic Gaussian

models remains to be seen. Piazzesi (1999) offers extensions that include both quadratic-Gaussian and affine-non-Gaussian features.

The consol-rate multifactor model of Brennan and Schwartz (1979, 1980c,
1982) is further analyzed by Nelson and Schaefer (1983), Schaefer and Schwartz
(1984), Hogan (1993b), and Duffie, Ma, and Yong (1995).

Other multifactor models include those of Black, Derman, and Kani (1992),
Chan (1992), Kraus and Smith (1993), and Platten (1994).

(J) The idea of using the instantaneous forward-rate process appears in Richard
(1978). The forward-rate model of Heath, Jarrow, and Morton (1992a) has been extensively treated in the case of Gaussian instantaneous forward rates Jamshidian
(1989a,b,d, 1991a), El Karoui and Rochet (1989), El Karoui, Lepage, Myneni,
Roseau, and Viswanathan (1991a,b), El Karoui and Lacoste (1992), Frachot
(1995), Frachot, Janci, and Lacoste (1993), Frachot and Lesne (1993a,b,c),
Miltersen (1994), and DeMunnik (1992). The illustration of the basic HJM drift restriction (38) is based on Rogers (1993). A quicker alternative derivation, based on an assumption that bond-price diffusions are differentiable with respect to maturity, is given by Hull (2000). The original derivation of (38) by Heath, Jarrow, and Morton (1992a) is based on the approach in Exercise 7.12. This exercise is useful as a means of establishing the relationship between the behavior of forward rates under the original measure P and under the equivalent martingale measure Q. Technical conditions justifying the calculations leading to (38) and the relationship r_t = f(t, t) between the short rate and forward rates are found in Carverhill (1995), Heath, Jarrow, and Morton (1992a), and Miltersen (1994).

Exercise 7.6, on bond-option pricing in a Gaussian forward-rate setting, is from several of the above papers on the HJM model. Heath, Jarrow, and Morton
(1992a) provide a model for forward rates in the form

df(t,s) = α(t,s)dt + σ(t,s)∫_t^s σ(t,u) du dt + σ(t,s) dB_t, (64)

for 0 <t <s, where α : [0, T] x [0, T] x R → R and σ: [0, T] x [0, T] x R → R* are bounded and Lipschitz continuous. Under additional regularity, the solution for the forward-rate process is nonnegative. The HJM model has been extended by
Miltersen (1994). For related work, derivative pricing, and computational methods in the HJM setting, see Babbs (1991), Brace and Musiela (1995b), Baxter (1996),
Carverhill and Pang (1995), Heath, Jarrow, and Morton (1990, 1992b), Jeffrey
(1995a, b), Miltersen and Persson (1997), and Rutkowski (1995, 1996).

Markovian versions of the HJM model are presented by Au and Thurston
(1993), Bhar and Chiarella (1995), Brace and Musiela (1994a), Cheyette (1995),
Jeffrey (1995c), Musiela (1994b), Ritchken and Sankarasubramanian (1992), and Ritchken and Trevor (1993).

(K) Musiela (1994b) developed a version of the HJM model in which the forwardrate curve is a Markov process. For related work in this setting, sometimes called a string, random field, or SPDE model of the term structure, see Cont (1998), Jong and Santa-Clara (1999), Goldstein (1997, 2000), Goldys and Musiela (1996), Hamza and Klebaner (1995), Kennedy (1994), Kusuoka (2000), Musiela and Sondermann
(1994), Pang (1996), Santa-Clara and Sornette (1997), and Sornette (1998).

Additional Topics: Cox, Ingersoll, and Ross (1981a) and Cheng (1991) give examples of what can go wrong if one begins with a model for the stochastic behavior of bond prices without first verifying conditions for the absence of arbitrage. See also Campbell (1986b). Amin and Morton (1994a) show how to estimate implied volatilities of interest rates from term-structure models. Theoretical arbitrage problems with the calibration approach, as often applied in practice, are explained by Backus, Foresi, and Zin (1998).

There is a growing literature on the econometric estimation of term-structuremodels. In addition to papers mentioned above, this includes the work of Ait-Sahalia (1996a, b, c), Ball and Torous (1994), Broze, Scaillet, and Zakoian (1993), Buhler, Uhrig-Homburg, Walter, and Weber (1995), Buono, Gregory-Allen, and Yaari (1992), Chan, Karolyi, Longstaff, and Saunders (1992), Danesi, Garcia, Genon-Catalot, and Laurent (1993), Das (1998a, b), Duffee (1999b), Fournié and Talay (1991), Gourieroux and Laurent (1994), Gourieroux and Scaillet (1994), Grinblatt and Jegadeesh (1996), Jegadeesh (1993), Koedijk, Nissen, Schotman, and Wolff (1994), Litterman and Scheinkman (1988), and DeMunnik (1992). For estimation in the HJM setting, see Frachot (1995), Frachot, Janci, and Lacoste (1993), Frachot and Lesne (1993a, b, c), Flesaker (1993), Jeffrey (1995b), Miltersen (1993), and Stanton (1995a).

On log-normal interest rates and on the “market model” of interest rates of Miltersen, Sandmann, and Sondermann (1997) used in Exercise 7.14, see Andersen and Andreasen (1998), Brace and Musiela (1995c), Dothan (1978), Goldberg (1998), Goldys, Musiela, and Sondermann (1994), Hansen and Jorgensen (1998), Hogan (1993a), Jamshidian (1996b, 1997b, 1999), Miltersen, Sandmann, and Sondermann (1997), Sandmann and Sondermann (1997), Musiela (1994a), and Vargiolu (1999). A related log-normal futures-price term-structure model is due to Heath (1998).

The role of jumps in term-structure modeling is examined by Baz and Das (1996), Bjork, Kabanov, and Runggaldier (1995), Bjork, DiMasi, Kabanov, and Runggaldier (1997), Das (1993c, 1995, 1997, 1998), Das and Foresi (1996), Duffie and Kan (1996), Eberlein and Raible (1999), Glasserman and Kou (1999), and Naik and Lee (1994).

Dybvig, Ingersoll, and Ross (1996) show that the asymptote of long-term interest rates, as maturity goes to infinity, defines a process that is nondecreasing in calendar time. Related work can be found in Carverhill (1996) and El Karoui, Frachot, and Geman (1997).

Numerical methods for solving term-structure models and the pricing of derivative securities are described in Chapter 12.

The pricing of mortgage-backed securities based on term-structure models (1996) is discussed by Boudoukh, Richardson, Stanton, and Whitelaw (1995), Cheyette (1996), and Stanton (1995b), and Stanton and Wallace (1995, 1998). For term-structure models with jumps in the foreign exchange setting, see Nielsen and Saa-Requejo (1993). The exercise on pricing foreign bonds in the foreign exchange setting is based on Amin and Jarrow (1993) and Amin and Jarrow (1994). The explicit form of the drift restriction on the foreign forward rate appearing as a solution in this exercise seems to have appeared both here and in Musiela and Rutkowski (1997). Restrictions implied by monetary integration are explored by Lund (1999).

We have taken the zero-coupon yield curve throughout as though it can be directly observed in the marketplace. In fact, it is normal practice in the finance industry to estimate the current zero-coupon yield curve (or forward rates) from the prices of both zero-coupon and coupon bonds. Such curve-fitting methods as nonlinear least squares or splines of several varieties are used for this purpose. See, for example, Adams and Van Deventer (1994), Coleman, Fisher, and Ibbotson (1992), Diament (1993), Fisher, Nychka, and Zervos (1994), Jaschke (1996), Konno and Takase (1995, 1996), and Svensson and Dahlquist (1993). Consistency of the curve-fitting method with an underlying term-structure model is examined by Bjork and Christensen (1999), Bjork and Gombani (1999), and Filipović (1999b).

On modeling the term structure of real interest rates, see Brown and Schaefer (1996) and Pennacchi (1991). On central-bank policy effects and term-structure models, see Babbs and Webber (1994), Balduzzi, Bertola, Foresi, and Klapper (1998), and Piazzesi (1997, 1999).

On the relative yields of taxable and nontaxable bonds, see Jordan (1995) and Rumsey (1996).

The expectations hypothesis is addressed in a term-structure setting by Fisher and Gilles (1998a).

The implications of special repo rates for term-structure modeling are explored by Barone and Risa (1994), Duffie (1996), and Fisher and Gilles (1996). Grinblatt (1994) pursues a related swap-spread model.

Further general reading on arbitrage-free models of the term structure is found in Artzner and Delbaen (1990b), Babbs and Webber (1994), Back (1996), Balduzzi (1994), Bjork (1996), Bossaerts (1990), Campbell (1995), Carverhill (1990, 1991), Heston (1988a, 1989), Hull and White (1993), Marsh (1994), DeMunnik (1992), Musiela and Rutkowski (1997), Pedersen and Shiu (1993), Pedersen, Shiu, and Thorlacius (1989), Rogers (1993), and Webber (1990, 1992).

Alternative approaches to modeling the term structure of interest rates are given by Backus, Foresi, and Zin (1998), Brace and Musiela (1995a), Goldstein (1995), Jin and Classerman (1998), Kim (1992, 1993, 1994), Tice and Webber (1997), and Zheng (1994).

On term-structure modeling of forward commodity prices, see references cited in Chapter 8.

Derivative Pricing

THIS CHAPTER APPLIES arbitrage-free pricing techniques from Chapters 6 and 7 to derivative securities that are not always easily treated by the direct PDE approach of Chapter 5. A derivative security is one whose cash flows are contingent on the prices of other securities, or on related indices. After summarizing the essential results from Chapter 6 for this purpose, we study the valuation of forwards, futures, European and American options, and certain exotic options. Option pricing with stochastic volatility is addressed with Fourier-transform methods.

A. Martingale Measures in a Black Box

Skipping over the foundational theory developed in Chapter 6, this section reviews the properties of an equivalent martingale measure, a convenient “black-box” approach to derivative asset pricing in the absence of arbitrage. Once again, we fix a standard Brownian motion B = (B¹, ..., Bᵈ) in ℝᵈ restricted to some time interval [0, T], on a given probability space (Ω, 𝓕, P). The standard filtration 𝓕 = {𝓕ₜ : 0 < t < T} of B is as defined in Section 5.1.

We take as given an adapted short-rate process r, with ∫₀ᵀ |rₜ| dt < ∞ almost surely, and an Itô security-price process S in ℝᴺ with

dSₜ = μₜ dt + σₜ dBₜ,

for appropriate μ and σ. It was shown in Chapter 6 that, aside from technical conditions, the absence of arbitrage is equivalent to the existence of an equivalent probability measure Q with special “risk-neutral” properties, called the equivalent martingale measure. For this chapter, we will use a narrow definition of equivalent martingale measures under which all expected rates of return are equivalent to the riskless rate r; a broader definition is given in Chapter 6. This means that, under Q, there is a standard Brownian motion B^Q in ℝᵈ such that, if the given securities pay no dividends before T, then

dSₜ = r_t Sₜ dt + σₜ dB^Qₜ, (1)

which repeats (6.14). After substituting this “risk-neutral” measure Q for P, one can thus treat every security as though its “instantaneous expected rate of return” is the short rate r.

More generally, suppose the securities with price process S are claims to a cumulative-dividend process D. (That is, Dₜ is the vector of cumulative dividends paid by the N securities up through time t.) In this case, we have

Sₜ = E_t [ ∫ₜᵀ e^{-(∫ₜˢ rᵤ du)} dDₛ + e^{-(∫ₜᵀ rᵤ du)} S_T ], (2)

which repeats (6.20). For example, suppose that Dₜ = ∫₀ᵗ δₛ ds for some dividend-rate process δ. Then (2) implies that

dSₜ = (r_t Sₜ − δₜ) dt + σₜ dB^Qₜ, (3)

generalizing (1). For another example, consider a unit discount riskless bond maturing at some time s. The cumulative-dividend process, say H, of this security is characterized by Hₜ = 0 for t < s and Hₜ = 1 for u ≥ s. The price of this bond at any time t < s is therefore determined by (2) as

P(t, s) = E_t [ exp(−∫ₜˢ rᵤ du) ].This doubly indexed process A is sometimes known as the discount function, or more loosely as a term-structure model. Details are given in Chapter 7.

By the definition of an equivalent martingale measure given in Chapter 6, any random variable Z that has finite variance with respect to P has finite expectation with respect to Q, and

B_t(z) = + B(E_t,z), (4)

where E_t denotes F_t-conditional expectation under Q and

吊 =e】【P〈_还]【17工(翼Z【叟工一皇互′7′】^7】JZ谚薯),

and where γ is a market-price-of-risk process, that is, an adapted process in R^d solving the family of linear equations

ON = by — 1S; te [0, T].

The remainder of this chapter applies these concepts to the calculation of derivative asset prices, going beyond the simple cases treated in Chapter 5.

# B. Forward Prices

Sections B through D address the pricing of forward and futures contracts, an important class of derivatives. A discrete-time primer on this topic is given in Exercise 2.17. The forward contract is the simpler of these two closely related securities. Let W be an F_t-measurable finite-variance random variable underlying the claim payable to a holder of the forward contract at its delivery date T. For example, with a forward contract for delivery of a foreign currency at time T, the random variable W is the market value at time T of the foreign currency. The forward-price process F is an Itô process defined by the fact that one forward contract at time t is a commitment to pay the net amount F_t — W at time T, with no other cash flows at any time. In particular, the true price of a forward contract, at the contract date, is zero.

We fix a bounded short-rate process r and an equivalent martingale measure Q. The dividend process H defined by the forward contract made at time t is given by H_s = 0, s < T, and H_T = W — F_t. Because the true price of the forward contract at t is zero, (2) implies that

0 - Fe 恤〈一还『r, as)w - 峭〕Solving for the forward price, E_Q [exp(- ∫_t^T r_s ds)W]
E_Q [exp(- ∫_t^T r_s ds)]

If we assume that there exists at time t a zero-coupon riskless bond maturing at time T, then

F_t = E_Q [exp(- ∫_t^T r_s ds)W]. (5)

From this, we see that the forward-price process F is indeed an Itô process.

If r and W are statistically independent with respect to Q, we have the simplified expression F_t = E_Q(W), implying that the forward price is a Q-martingale. This would be true, for instance, if the short-rate process r is deterministic.

As an example, suppose that the forward contract is for delivery at time T of one unit of a particular security with price process S and dividend process D. In particular, W = S_T. We can obtain a more concrete representation of the forward price than (5), as follows. From (5) and (2),

If the short-rate process r is deterministic, we can simplify further to

F_t = E_Q [S_T exp(- ∫_t^T r_s ds)] (7)

which is known as the cost-of-carry formula for forward prices.

For deterministic r and D, the cost-of-carry formula (7) can be recovered from a direct and simple arbitrage argument. As an alternative to buying a forward contract at time t, one could instead buy the underlying security at t and borrow the required cost S_t by selling riskless zero-coupon bonds maturing at T. If one lends out the dividends as they are received by buying riskless bonds maturing at T, the net payoff to this strategy at time T is the value S_T of the underlying security, less the maturity value S_t/A_{t,T} of the bonds sold at t, plus the total maturity value ∫_t^T A_{s,T} dD_s of all of the bonds purchased with the dividends received between t and T. The total is S_T — S_t/A_{t,T} + ∫_t^T A_{s,T} dD_s. The payoff of the forward contract is S_T — F_t. Since these two strategies have no payoffs except at T, and since both F_t and S_t/A_{t,T} — ∫_t^T A_{s,T} dD_s are known at time t, there would be an arbitrage unless F_t and S_t/A_{t,T} — ∫_t^T A_{s,T} dD_s are equal, consistent with (7).

We have put aside the issue of calculating the equivalent martingale measure Q. The simplest case is that in which the forward contract is redundant, for in this case, the equivalent martingale measure does not depend on the forward price. The forward contract is automatically redundant if the underlying asset is a security with deterministic dividends between the contract date t and the delivery date T, provided there is a zero-coupon bond maturing at T. In that case, the forward contract can be replicated by a strategy similar to that used to verify the cost-of-carry formula directly. Construction of the strategy is assigned as an exercise.

# C. Futures and Continuous Resettlement

As with a forward contract, a futures contract with delivery date T is keyed to some delivery value W, which we take to be an F_t-measurable random variable with finite variance. The contract is completely defined by a futures-price process Φ with the property that Φ_T = W. As we shall see, the contract is literally a security whose price process is zero and whose cumulative-dividend process is Φ. In other words, changes in the futures price are credited to the holder of the contract as they occur. See Exercise 2.17 for an explanation in discrete time.

This definition is an abstraction of the traditional notion of a futures contract, which calls for the holder of +1 contract at the delivery time T to accept delivery of some asset (whose spot market value at T is represented here by W) in return for simultaneous payment of the current futures price Φ_T. Likewise, the holder of —1 contract, also known as a short position of 1 contract, is traditionally obliged to make delivery of the same underlying asset in exchange for the current futures price Φ_T. This informally justifies the property Φ_T = W of the futures-price process Φ given in the definition above. Roughly speaking, if Φ_T is not equal to W (and if we continue to neglect transactions costs and other details), there is a delivery arbitrage. We will not explicitly define a delivery arbitrage since it only complicates the following analysis of futures prices. Informally, however, in the event that W > Φ_T one could buy at time T the deliverable asset for W, simultaneously sell one futures contract, and make immediate delivery for a profit of W — Φ_T. Thus the potential of delivery arbitrage will naturally equate Φ_T with the delivery value W. This is sometimes known as the principle of convergence.

Many modern futures contracts have streamlined procedures that avoid the delivery process. For these, the only link that exists with the notion of delivery is that the terminal futures price Φ_T is contractually equated to some such variable W, which could be the price of some commodity or security, or even some abstract variable of general economic interest such as a price deflator. This procedure, finessing the actual delivery of some asset, is known as cash settlement. In any case, whether based on cash settlement or the absence of delivery arbitrage, we shall always take it by definition that the delivery futures price Φ_T is equal to the given delivery value W.

The institutional feature of futures markets that is central to our analysis of futures prices is resettlement, the process that generates daily or even more frequent payments to and from the holders of futures contracts based on changes in the futures price. As with the expression "forward

price," the term "futures price" can be misleading in that the futures price Φ_t at time t is not at all the price of the contract. Instead, at each resettlement time t an investor who has held δ futures contracts since the last resettlement time, say s, receives the resettlement payment δ(Φ_t — Φ_s), following the simplest resettlement recipe. More complicated resettlement arrangements often apply in practice. The continuous-time abstraction is to take the futures-price process Φ to be an Itô process and a futures posi-tion process to be some θ ∈ Φ(ℝ) generating the settlement gain f_6 db as a cumulative-dividend process. In particular, as we have already stated in its definition, the futures-price process Φ is itself, formally speaking, the cumulative dividend process associated with the contract. The true price process is zero, since (again ignoring some of the detailed institutional procedures) there is no payment against the contract due at the time a contract is bought or sold.

# D. Arbitrage-Free Futures Prices

The futures-price process Φ can now be characterized as follows. We suppose that the short-rate process r is bounded. For all t, let Y_t = exp( − ∫₀ᵗ r_s ds). Because Φ is strictly speaking the cumulative-dividend process associated with the futures contract, and since the true-price process of the contract is zero, from (2) we see that

0 = E_Q([ Y_T Φ_T | ℱ_t ), t<T,

from which it follows that the stochastic integral { Φ dΦ } is a Q-martingale.
Because r is bounded, there are constants k > 0 and k_r such that Y_t ≤ k_r for all t. The process Φ dΦ is therefore a Q-martingale if and only if Φ is also a Q-martingale. (This seems obvious; proof is assigned as an exercise.) Since Φ_T = W_T, we have deduced a convenient representation for the futures-price process:

Φ_t = E_Q( W_T | ℱ_t ), t ∈ [0,T]. (8)

If r and W are statistically independent under Q, the futures-price process Φ given by (8) and the forward-price process F given by (5)
are thus identical. In particular, if r is deterministic, the cost-of-carry formula (7) applies as well to futures prices.

As for how to calculate an equivalent martingale measure Q, it is most convenient if the futures contract is redundant, for then a suitable Q can be calculated directly from the other available securities. We shall work on

this approach, originating with an article cited in the Notes, and fix for the remainder of the section such an equivalent martingale measure Q. Aside from the case of complete markets, it is not obvious how to establish the redundancy of a futures contract since the futures-price process Φ is itself the cumulative-dividend process of the contract, so any argument might seem circular. Suppose, however, that there is a self-financing strategy (in securities other than the futures contract) whose value at the delivery date

T is Z_T = E_Q( W_T ).

We will give an example of such a strategy shortly. From the definition of
Q, the market value of this strategy at time t is Z_t = E_Q(W_T | ℱ_t). We claim that if Φ_t is not equal to Z_t, then there is an arbitrage. In order to show this, we will construct a trading strategy, involving only the futures contract and borrowing or lending at the short rate, such that the strategy pays off exactly Z_T at time T and requires the investment of Φ_t at time t. It will be clear from this that the absence of arbitrage equates Φ_t and Z_t. The strategy is constructed as follows. Let θ be the (bounded) futures position process defined by θ_s = 0, s < t and θ_s = exp(∫ₜˢ r_u du), s > t. Let V_s be the amount invested at the short rate at time s, determined as follows.
Let V_s = 0, s < t, and V_t = Φ_t. After t, let all dividends generated by the futures position be invested at the short rate and "rolled over." That is, let

dV_s = r_s V_s ds + θ_s dΦ_s, s ∈ [t,T].

The total market value at any time s > t of this self-financing strategy in futures and investment at the short rate is the amount V_s invested at the short rate, since the true price of the futures contract is zero. We can calculate by Itô’s Formula that

V_T = Φ_t exp( ∫ₜᵀ r_s ds ) = Z_T, (9)
t

which verifies the claim that the futures contract is redundant.

Summarizing, the futures-price process is uniquely defined by (8) provided there is a self-financing strategy with value Z_T = W_T exp( ∫ₜᵀ r_s ds ) at the delivery date T. It remains to look for examples in which Z_T is indeed the value at time T of some self-financing strategy. That is the case, for instance, if the futures contract delivers a security that pays no dividends

before T and if the short-rate process is deterministic. With this, the purchase of exp( ∫ₜᵀ r_s ds ) units of the underlying security at time t would suffice. More general examples can easily be constructed.

There is one loose end to tidy up. The assumption that the futuresprice process Φ is an Itô process played a role in our analysis, yet we have not confirmed that the solution (8) for Φ is actually an Itô process. This can be shown as an application of Girsanov’s Theorem (Appendix D).

# E. Stochastic Volatility

The Black-Scholes option-pricing formula, as we recall from Chapter 5, is of the form C(x, p, r, t, σ), for C : ℝ₊ × ℝ₊ × ℝ × [0,T] × ℝ₊ → ℝ₊, where x is the current underlying asset price, p is the exercise price, r is the short interest rate, t is the time to expiration, and σ is the volatility coefficient for the underlying asset. For each fixed (x, p, r, t) with nonzero x and t, the map from σ to C(x, p, r, t, σ) is strictly increasing, and its range is unbounded. We may therefore invert and obtain the volatility from the option price. That is, we can define an implied volatility function I: ℝ₊ × ℝ₊ × ℝ × [0,T] × ℝ₊ → ℝ₊ by

c = C(x, p, r, t, I(x, p, r, t, σ)), (10)

for all sufficiently large c ∈ ℝ₊.

If c₁ is the Black-Scholes price of an option on a given asset at strike p₁ and expiration t₁, and c₂ is the Black-Scholes price of an option on the same asset at strike p₂ and expiration t₂, then the associated implied volatilities I(x, p₁, r, t₁, c₁) and I(x, p₂, r, t₂, c₂) must be identical, if indeed the assumptions underlying the Black-Scholes formula apply literally, and in particular if the underlying price process has the constant volatility of a geometric Brownian motion. It has been widely noted, however, that actual market prices for European options on the same underlying asset have associated Black-Scholes implied volatilities that vary with both exercise price and expiration date. For example, in certain markets at certain times, implied volatilities of options with a given exercise date depend on strike prices in a manner that is often termed a smile curve. Figure 8.1, for example, illustrates the dependence of Black-Scholes implied volatilities on moneyness (the ratio of strike price to futures price), for various
S&P 500 index options on November 2, 1993. Other forms of systematic deviation away from constant implied volatilities have been noted, both over time and across various derivatives at a point in time.

Three major lines of modeling address these systematic deviations from the assumptions underlying the Black-Scholes model. In all of these,

0.24 —

0.22 —

0.2

Black-Scholes Implied Vol (%)

0.08 —

0.06 7 5 4 5 5 06 07 0.8 0.9 1 1.1 1.2

Moneyness = Strike/Futures

Figure 8.1. “Smile Curves” Implied by S&P 500 Index Options of Six Different Times to Expiration, from Market Data for November 2, 1993

the underlying log-normal price process is generalized by replacing the constant-volatility parameter σ of the Black-Scholes model with a volatility process, an adapted nonnegative process V with ∫₀ᵀ V_t dt < ∞ such that the underlying asset price process S satisfies

dS_t = μ_t S_t dt + S_t √V_t dW_t, (11)

where dW = γ dB, B is a standard Brownian motion under Q obtained from any γ in ℝ² with unit norm.
In the first class of models, V_t = v(S_t, t), for some function v : ℝ₊ × [0,T] → ℝ₊ satisfying technical regularity conditions. In practical applications, the function v, or its discrete-time, discrete-state analogue, is often “calibrated” to the available option prices. This approach, sometimes referred to as the implied-tree model, is explored in literature cited in the Notes of this chapter and of Chapter 3.
For a second class of models, called generalized autoregressive conditional heteroscedastic or GARCH, the volatility depends on the path of squaredrns. The model was originally formulated in a discrete-time setting by

constructing the volatility \( V \) at time \( t \) of the return \( r_{t+1} = \log S_{t+1} - \log S_t \) according to the recursive formula

\( V_t = a + bV_{t-1} + cZ_t^2 \), (12)

for fixed coefficients \( a \), \( b \), and \( c \) satisfying regularity conditions. By taking a time period of length \( h \), normalizing in a natural way, and taking limits, a natural continuous-time limiting behavior for volatility is simply a deterministic mean-reverting process \( V \) satisfying the ordinary differential equation

\( dV(t) = \alpha ( \bar{V} - V(t) ) \, dt \). (13)

(Discussion of the nature of the continuous-time limit can be found in sources cited in the Notes.)

In a third approach, the increments of the volatility process \( V \) depend on Brownian motions (or more general random processes) that are not perfectly correlated with \( \epsilon^S \). For example, in a simple “one-factor” setting the volatility process \( V \) satisfies a stochastic differential equation of the form

\( dV_t = \mu(V_t) \, dt + \sigma(V_t) \, d\epsilon_t^V \), (14)

where \( \epsilon^V = c_V \cdot B_2 \) is a standard Brownian motion under \( Q \), for some constant vector \( c_V \) of unit norm. As we shall see, the correlation parameter \( \rho_{SV} = c_S^{\top} c_V \) has an important influence on option prices.

The Feynman-Kac approach illustrated in Chapter 5 leads, under technical conditions, to a partial differential equation to be solved for a function \( f: \mathbb{R}_+ \times \mathbb{R}_+ \times [0,t] \to \mathbb{R} \) that determines the price at time \( s \) of a European option at exercise price \( p \) and expiration at time \( t \) as

\( f(S_s, V_s, s) = E_Q[ e^{-\int_s^t r_u \, du} (S_t - p)_+ ] \).

Methods for solving such a PDE by discretization are cited in Chapter 12.

A special case of the stochastic-volatility model that has sometimes been applied takes the correlation parameter \( \rho_{SV} \) to be zero. This implies that the volatility process \( V \) is independently distributed (under \( Q \)) with the return-driving Brownian motion \( \epsilon^S \). One can then more easily calculate the value of an option (or another derivative) on the underlying asset by noting that, conditional on the volatility process \( V \), the underlying asset price process is log-normal under \( Q \). That is, the distribution under \( Q \) of

\( \log S_1 \) conditional on the entire volatility process \( \{V_s : s \in [0,t]\} \) is normal with standard deviation \( \sigma(V) \sqrt{t} \), where

\( \sigma(V) = \left( \frac{1}{t} \int_0^t \sigma^2(V_u) \, du \right)^{1/2} \),

and with mean \( \mu t - \sigma(V)^2 t / 2 \). By the law of iterated expectations, the initial European call-option price, with expiration date \( t \) and strike \( p \), is given by

\( f(S_0, V_0, t) = E_Q[ e^{-r t} (S_t - p)_+ ] \)
\( = E_Q[ E_Q[ e^{-r t} (S_t - p)_+ \mid \{V_s : s \in [0,t]\} ] ] \)
\( = E_Q[ C(S_0, p, r, t, \sigma(V)) ] \), (18)

where \( C() \) as usual denotes the Black-Scholes formula. Given a particular stochastic model for \( V \), one could evaluate the option price (15) by several numerical methods mentioned in the Notes. One finds that the implied smile curve is indeed “smile-shaped,” although it is difficult to reconcile this special case with the empirical behavior of many types of options. In particular, in many settings, a pronounced skew to the smile, as in Figure 8.1, indicates an important potential role for correlation between the increments of the return-driving and volatility-driving Brownian motions, \( \epsilon^S \) and \( \epsilon^V \). This role is borne out directly by the correlation apparent from time-series data on implied volatilities and returns for certain important asset classes, as indicated in sources cited in the Notes.

A tractable model that allows for the skew effects of correlation is the Heston model, the special case of (14) for which

\( dV_t = \kappa (\theta - V_t) \, dt + \sigma_V \sqrt{V_t} \, d\epsilon_t^V \), (16)

for positive coefficients \( \kappa \), \( \theta \), and \( \sigma_V \) that play the same respective roles for \( V \) as for a Cox-Ingersoll-Ross interest-rate model. (Indeed, (16) is sometimes called a “CIR model” for volatility.) In the original Heston model, the short rate was assumed to be a constant, say \( r \), and option prices can be computed analytically, using transform methods explained in the next Section, in terms of the parameters \( (r, \rho_{SV}, \kappa, \theta, \sigma_V) \) of the Heston model, as well as the initial volatility \( V_0 \), the initial underlying price \( S_0 \), the strike price, and the expiration time. Figure 8.2 shows the “smile curves” for the options illustrated in Figure 8.1, for parameters, including \( V_0 \), chosen to minimize the sum of squared differences between actual and theoretical

option prices. Notably, the distinctly downward slopes, often called skews, are captured with a negative correlation coefficient \( \rho_{SV} \). Taking the short rate \( r = 0.0319 \), the remaining coefficients of the Heston model are calibrated as \( \rho_{SV} = -0.66 \), \( \kappa = 19.66 \), \( \theta = 0.017 \), \( \sigma_V = 1.516 \), and \( V_0 = 0.094 \). The Notes cite literature that uses time-series data on both options and underlying prices to fit the parameters, indicating evidence that the Heston model is overly restrictive for these data. This transform approach, however, also accommodates stochastic interest rates, jumps, and more general volatility models.

# F. Option Valuation by Transform Analysis

This section is devoted to the calculation of option prices with stochastic volatility, in a setting with affine state dynamics of the type introduced for term-structure modeling in Chapter 7. We use transform analysis, allowing for relatively rich and tractable specifications of stochastic interest rates and volatility, and, eventually, for jumps. Repeating from Chapter 7, a state process \( X \) in state space \( D \subset \mathbb{R}^k \) is affine (under \( Q \)) if

\( dX_t = \mu(X_t) \, dt + \sigma(X_t) \, dB_t \), (17)

where \( \mu(x) = K_0 + K_1 x \) for some \( K_0 \in \mathbb{R}^k \) and \( K_1 \in \mathbb{R}^{k \times k} \) and, for each \( i \) and \( j \) in \( \{1,...,k\} \),

\( (\sigma(x) \sigma(x)^{\top})_{ij} = A_{ij} + B_{ij}^{\top} x \), (18)

for some \( A_{ij} \in \mathbb{R} \) and \( B_{ij} \in \mathbb{R}^k \), for the state space

\( D = \{ x : A_{ij} + B_{ij}^{\top} x > 0, 1 \leq i \leq n \} \). (19)

The Notes cite technical conditions on the coefficients \( (K_0, K_1) \) ensuring the existence of a unique solution \( X \) to (17). For time-series empirical studies, it is often convenient to suppose that the state process \( X \) is also affine under the original data-generating probability measure \( P \), albeit with a different set \( K^P = (K_0^P, K_1^P) \) of drift-related coefficients in place of \( K \). Conditions for this, and extensions to time-dependent coefficients, are explored in exercises.

In this setting, the short-rate process \( r \) is assumed to be of the affine form \( r = \rho_0 + \rho_1^{\top} X_t \), for coefficients \( \rho_0 \in \mathbb{R} \) and \( \rho_1 \in \mathbb{R}^k \). Finally, we suppose that the price process \( S \) underlying the options in question is of the exponential-affine form \( S = \exp(a_t + b_t^{\top} X_t) \), for potentially time-dependent coefficients \( a_t \in \mathbb{R} \) and \( b_t \in \mathbb{R}^k \). An example would be the price of an equity, a foreign currency, or, as shown in Chapter 7, the price of a zero-coupon bond.

The Heston model (16) is a special case of an affine process \( X = (X^{(1)}, X^{(2)}) \), with \( X^{(1)} = Y = \log(S_t) \), and \( X^{(2)} = V_t \). The short rate is assumed constant \( r = \rho_0 \). From Ito’s Formula,

\( dY_t = (r - \frac{1}{2} V_t) \, dt + \sqrt{V_t} \, d\epsilon_t^S \), (20)

which indeed makes the state vector \( X_t = (Y_t, V_t) \) an affine process, whose state space is \( D = \mathbb{R} \times [0, \infty) \), and whose coefficients \( (A, B) \) can be chosen in terms of the parameters \( (r, \rho_{SV}, \kappa, \theta, \sigma_V) \) of the Heston model. The underlying asset price is of the desired exponential-affine form because \( a_t = 0 \) and \( b_t = (1, 0) \). We will return to the Heston model shortly with some explicit results on option valuation.

For the general affine case, suppose we are interested in valuing a European call option on the underlying security, with strike price \( p \) and exercise date \( t \). We have the initial option price

\( U = E_Q[ e^{-\int_0^t r_u \, du} (S_t - p)_+ ] \).

Letting \( A \) denote the event \( \{ \omega : S(\omega, t) > p \} \) that the option is in themoney at expiration, we have the option price

$$v = E\left[ \exp\left( -\int_0^T r_s \, ds \right) (S_T - p)^+ \right].$$ Because $S(t) = e^{\sigma X_t} S_0$, we have
$$v = e^{\sigma G}(-\log p + a(t); t, b(t), -b(t)) - p G(-\log p + a(t); t, 0, -b(t)), \tag{21}$$

where, for any $\theta \in \mathbb{R}$ and for any coefficient vectors $d$ and $\delta$ in $\mathbb{R}^d$,

$$G(z; t, d, \delta) = E\left[ \exp\left( -\int_0^t r_s \, ds \right) e^{z X_t + d \cdot X_0 + \delta \cdot \int_0^t \sigma_s \, ds} \right]. \tag{22}$$

So, if we can compute the function $G$, we can obtain the prices of options of any strike and exercise date. Likewise, the prices of European puts, interest-rate caps, chooser options, and many other derivatives can be derived in terms of $G$, as shown in exercises and sources cited in the Notes.

We note, for fixed $(t, d, \delta)$, assuming $E[\exp(\int_0^t r_s \, ds)] < \infty$, that $G(\cdot; t, d, \delta)$ is a bounded increasing function. For any such function $g: \mathbb{R} \to [0, \infty)$, an associated transform $\tilde{g}: \mathbb{R} \to \mathbb{C}$, where $\mathbb{C}$ is the set of complex numbers, is defined by

$$\tilde{g}(z) = \int_{-\infty}^{\infty} e^{i z y} g(y) \, dy, \tag{23}$$

where $i$ is the usual imaginary number, often denoted $\sqrt{-1}$. (Appendix H summarizes a few minimal elements of complex arithmetic.) Depending on one’s conventions, one may refer to $\tilde{g}$ as the Fourier transform of $g$. Under the technical condition that $\int_{-\infty}^{\infty} |g(z)| \, dz < \infty$, we have the Lévy Inversion Formula

$$g(y) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-i z y} \, \text{Im}[\tilde{g}(z)] \, dz, \tag{24}$$

where $\text{Im}(c)$ denotes the imaginary part of a complex number $c$.

For the case $g(\cdot) = G(\cdot; t, d, \delta)$, with transform $\tilde{G}(z; t, d, \delta)$, we can compute $G(y; t, d, \delta)$ from (24), typically by computing the integral in (24) numerically, and thereby obtain option prices from (21). Our final objective is therefore to compute the transform $\tilde{G}$. Fixing $z$, an application of Fubini’s Theorem to (23) implies that $\tilde{G}(z; t, d, \delta) = f(X_0, 0)$, where $f: D \times [0, t] \to \mathbb{C}$ is defined by

$$f(x, s) = E\left[ \exp\left( -\int_s^t r_u \, du \right) e^{z X_t + d \cdot x + \delta \cdot \int_s^t \sigma_u \, du} \,\Big|\, X_s = x \right]. \tag{25}$$

From (25), the same separation-of-variables arguments used in Chapter 7 imply, under technical regularity conditions, that

$$f(x, s) = e^{\alpha(s) + B(s) \cdot x}, \tag{26}$$

where $B$ solves the Riccati ordinary differential equation (ODE)

$$\frac{dB}{ds}(s) = \rho - \gamma B(s) - \frac{1}{2} B(s)^H B(s), \tag{27}$$

with the boundary condition $$B(t) = d + i z \delta, \tag{28}$$ and where
$$\alpha(s) = \int_s^t \left[ \rho_u + B(u)^H \mu(u) + \frac{1}{2} B(u)^H \sigma(u) \right] du. \tag{29}$$

The ODE (27) is identical to that arising in the affine term-structure calculations of Chapter 7, but the solutions for $\alpha(s)$ and $B(s)$ are complex numbers, in light of the complex boundary condition (28) for $B(t)$. One must keep track of both the real and imaginary parts of $\alpha(s)$ and $B(s)$, following the usual rules of complex arithmetic outlined in Appendix H.

Thus, under technical conditions, we have our transform $\tilde{G}(z; t, d, \delta)$, evaluated at a particular $z$. We then have the option-pricing formula (21), where $G(y; t, d, \delta)$ is obtained from the inversion formula (24) applied to the transforms $\tilde{G}(-; t, b(t), -b(t))$ and $\tilde{G}(-; t, 0, -b(t))$, obtained by solving the Riccati equation (27) with the respective boundary conditions $B(t) = i z b(t)$ and $-i z b(t)$. For cases in which the ODE (27) cannot be solved explicitly, its numerical computation, followed by numerical integration to obtain (24), is somewhat burdensome. Direct PDE or Monte Carlo numerical methods would typically, however, be even more computationally intensive.

For option pricing with the Heston model, we require only the transform $\tilde{G}(z) = e^{-\alpha(t,z)} E[e^{z V_t}]$, for some particular choices of $z \in \mathbb{C}$.
Solving (27) for this case, we have

$$\tilde{G}(z) = \exp\left\{ \alpha(t, z) + B(t, z) V(0) \right\},$$

where, letting $b = u \sigma$, $\kappa$, $a = u(1-u)$, and $\gamma = \sqrt{b^2 + a \theta}$, we find that

$$B(t, z) = \frac{a}{b^2} \left( \frac{2\gamma (1 - e^{-\gamma t})}{2\gamma - (\gamma + \kappa)(1 - e^{-\gamma t})} \right)$$ and
$$\alpha(t, z) = \frac{\kappa \theta}{\sigma^2} \left[ \kappa t - 2 \log\left( \frac{2\gamma - (\gamma + \kappa)(1 - e^{-\gamma t})}{2\gamma} \right) \right].$$

Other special cases for which one can compute explicit solutions are cited in the Notes, or treated in exercises.

# G. American Security Valuation

This section addresses the valuation of American securities, those whose cash flows are determined by the stopping time at which the owner of the American security decides to exercise. As our setup for primitive securities, we take a bounded short-rate process $r$ and suppose that the price process $S$ of the other securities satisfies (1), where $B$ is a standard Brownian motion under a probability measure $Q$ equivalent to $P$. We also suppose for this section that $\text{rank}(\sigma) = d$ almost everywhere, so that any random payoff with finite risk-neutral expectation can be replicated without resorting to “doubling strategies,” as shown by Proposition 6.1. As indicated in Chapter 2, some sort of dynamic-spanning property of this type is important for the valuation of American securities.

An American security, defined by an adapted process $U$ and an expiration time $T$, is a claim to the payoff $U_\tau$ at a stopping time $\tau \leq T$ chosen by the holder of the security. Such a stopping time is an exercise policy. As with the discrete-time treatment in Chapter 2, our objective is to calculate the price process $V$ of the American security and to characterize rational exercise policies. The classic example is the case of a put option on a stock in the Black-Scholes setting of constant-volatility stock prices and constant short rates. In that case, we have $U_t = (p - S_t)^+$, where $p$ is the exercise price and $S$ is the underlying asset price process. More generally, we will rely on the following technical condition.

American Regularity Condition. $U$ is an adapted continuous process, bounded below, with $E[\sup_{t \in [0, T]} U_t] < \infty$.

This regularity is certainly satisfied for an American put option in standard settings for which the underlying price process is an Itô process.

Given some particular exercise policy $\tau$, Proposition 6.1 implies that the claim to $U_\tau \exp(-\int_0^\tau r_s \, ds)$ at $T$ can be replicated by a self-financing trading strategy $\theta$ whose market-value process $\pi$ is given by

$$V_\tau = E_Q(\xi_{\tau, T} U_\tau),$$

where $\xi_{s,t} = \exp(-\int_s^t r_u \, du)$. This implies that the payoff of $U_\tau$ at time $\tau$ is replicated by the trading strategy $\theta^\tau$ that is $\theta$ until time $\tau$, and zero afterward, generating a lump-sum payment of $U_\tau$ at $\tau$.

Following the approach taken in Section 2.1, we therefore define a rational exercise policy as a solution to the optimal-stopping problem

$$V_t^* = \sup_{\tau \in \mathcal{T}(t)} V_\tau, \tag{30}$$

where $\mathcal{T}(t)$ denotes the set of stopping times valued in $[t, T]$. This is the problem of maximizing the initial cost of replication. We will show that there is in fact a stopping time $\tau^*$ solving (30), and that the absence of “nonpathological” arbitrages implies that the American security must sell initially for $V_0^*$.

If $V_0^* < V_0$, then purchase of the American security for $V_0$, adoption of a rational exercise policy $\tau^*$ and replication of the payoff $-U(\tau^*)$ at $\tau^*$ at an initial payoff of $V_0^*$, together generate a net initial profit of $V_0^* - V_0 > 0$ and no further cash flow. This is an arbitrage.

In order to rule out the other possibility, that $V_0^* > V_0$, we will exploit the notion of a super-replicating trading strategy, a self-financing trading strategy whose market-value process $Y$ dominates the exercise-value process $U$, in that $Y_t \geq U_t$ for all $t$ in $[0, T]$. We will show the existence of a super-replicating trading strategy with initial market value $Y_0 = V_0^*$. If $V_0^* > V_0$, then sale of the American security and adoption of a super-replicating strategy implies an initial profit of $V_0^* - V_0 > 0$ and the ability to cover the payment $U_\tau$ demanded by the holder of the American security at exercise with the market value $Y_\tau$ of the super-replicating strategy, regardless of the exercise policy $\tau$ used by the holder of the American security. This constitutes an arbitrage. Indeed, then, the unique arbitrage-free American security price would be given by (30). (We have implicitly extended the definition of an arbitrage slightly in order to handle American securities.)

Let $U^*$ be the deflated exercise-value process, defined by

$$U^*_t = \exp\left( -\int_0^t r_s \, ds \right) U_t.$$

Let $W$ be the Snell envelope of $U^*$ under $Q$, meaning that

$$W_t = \operatorname{ess\,sup}_{\tau \in \mathcal{T}(t)} E_Q(U^*_\tau), \tag{31}$$

where $\operatorname{ess\,sup}$ denotes essential supremum. [In other words, for all $\tau \in \mathcal{T}(t)$,P(W, > E[Φ(0)]) = 1, and if U is any other Y,-measurable random variable satisfying P(W, > E[Φ(0)]) = 1 for all t in F(t), then P(W, < W,) = 1.]
We recall from Chapter 6 that a trading strategy whose market-value process is bounded below cannot take advantage of certain “pathological”
varieties of arbitrage, such as doubling strategies.

Proposition. There is a super-replicating trading strategy b“ whose market-value process Y is bounded below, with initial market value Y₀ = V₀. A rational exercise policy is given by τ° = inf {t : Y, = U,}.

Proof: Under the American Regularity Conditions, a source cited in the
Notes shows that the Snell envelope W of Φ is a continuous supermartingale under Q, and can therefore be decomposed in the form
W = Z − A, where Z is a Q-martingale and A is an increasing adapted process with A₀ = 0. By Proposition 6.1 and numeraire invariance, there is a self-financing trading strategy whose market-value process Y has the final market value y = Z_T exp(∫₀ᵀ r, dt) and satisfies

Y, = Y₀ exp(∫₀ᵗ r, ds).

A Q-martingale V is thus defined by V, = Y, exp(−∫₀ᵗ r, ds). Because Z is also a Q-martingale, for t < T we have

V, = E_Q [ exp(−∫ₜᵀ r, ds) Y_T | F_t ]
= exp(∫₀ᵗ r, ds) E_Q [ exp(−∫ₜᵀ r, ds) Z_T | F_t ]
= exp(∫₀ᵗ r, ds) Z, = exp(∫₀ᵗ r, ds)(W, + A,). (32)

Taking t = 0 in (32), we have V₀ = W₀ = V₀, as asserted. From (32),

Y, > exp(∫₀ᵗ r, ds) W, > U,, (33)

using the fact that A, is nonnegative, the definition of W, and the fact that
W, > U,. Thus the underlying trading strategy is super-replicating. Because
U is bounded below, (33) implies that the replicating market-value process
Y is bounded below. Moreover, τ° is a rational exercise policy because

V_{τ°} = Y_{τ°} = E_Q [exp(−∫_{τ°}^{T} r, ds) Φ(τ°)] = V₀",

from noting that V is a Q-martingale and that Φ(τ°) = U(τ°). ■

Putting the various pieces of the story together, the “arbitrage-pricing”
result is summarized as follows. If the initial price V₀ of the American security (Φ, T) is strictly larger than

V* = sup_{τ∈𝒯(0)} E_Q [exp(−∫₀ᵀ r(s) ds) U_τ] , (34)

then an arbitrage consists of sale of the option and adoption of the superreplicating trading strategy b* until whatever exercise time τ chosen by the option holder. Conversely, if V₀ < V*, then an arbitrage is made by purchase of the option at time 0, exercise of the option at the rational time τ°, and adoption of the trading strategy −b* until liquidation at τ.
Neither of these arbitrage strategies are “doubling strategies” of the type discussed in Chapter 6; the implied pricing is indeed consistent with the given equivalent martingale measure Q.

All of our assumptions are satisfied in the case of an American put in the “Black-Scholes” setting, with a constant short rate r, and an underlying price process S solving

dS, = r S, dt + σ S, dξ; S₀ = x, (35)

where ξ is a standard Brownian motion under Q. Thus, an American put with exercise price p and expiration at time T has the initial arbitrage-free price

V₀ = max E_Q [e^{−rT} (p − S_T)⁺]. (36)

In Chapter 12 we review some numerical recipes for approximating this value. There need not in fact be complete markets for our results to apply even in this simple setting, for even if the underlying Brownian motion is of dimension a > 1, the super-replicating strategy of Proposition 8.G can be constructed in terms of the underlying security with price process S and funds invested at the short rate r, and has a market-value process Y

that dominates the exercise value (p − S_τ)⁺ at any stopping time τ, even a stopping time τ that is determined by information not generated by the Brownian motion ξ of the underlying price process S.

By extending our arguments, we can handle an American security that promises a cumulative-dividend process H until exercised at a stopping time τ < T for a final payoff of U_τ. The same arguments applied previously lead to an initial price of the American security (H, U, T) given, under similar technical regularity, by

V₀ = sup_{τ∈𝒯(0)} E_Q [∫₀^τ e^{−∫₀^t r(s) ds} dH, + e^{−∫₀^T r(s) ds} U_T].

# H. American Exercise Boundaries

We take the case of an American security (Φ, T) with U, = g(X, t), where g: R* × [0, T] → R is continuous and X is a state process in R* satisfying the SDE

dX, = a(X,) dt + b(X,) dξ, (37)

for continuous functions a and b satisfying Lipschitz conditions. For simplicity, we take the interest-rate process r to be zero, and later show that, aside from technicalities, this is without loss of generality. We adopt the American regularity conditions and again assume redundancy of the
American security for any exercise policy. Starting at time t with initial condition X, = x for (37), the arbitrage-free value is given by

h(x, t) = sup_{τ∈𝒯(t)} E_Q [g(X, τ)]. (38)

By inspection, h > g. From Proposition G, an optimal exercise policy is given by

τ° = inf{t ∈ [0, T]: h(X, t) = g(X, t)}. (39)

By (39), h(X, t) > g(X, t) for all t < τ°. Letting
𝒞 = {(x, t) ∈ R* × [0, T]: h(x, t) = g(x, t)} (40)

we can write τ° = inf{t : (X, t) ∈ 𝒞}, and safely call 𝒞 the exercise region, and its complement

𝒥 = {(x, t) ∈ R* × [0, T) : h(x, t) > g(x, t)}

the continuation region. In order to solve the optimal exercise problem, it is enough to break R* × [0, T] into these two sets. An optimal policy is then to exercise whenever (X, t) is in 𝒞, and otherwise to wait. Typically, solving for the exercise region 𝒞 is a formidable problem.

For a characterization of the solution in terms of the solution of a partial differential equation, suppose that h is sufficiently smooth for an application of Ito’s Formula. Then

h(X, t) = h(X, 0) + ∫₀ᵗ 𝒟h(X, s) ds + ∫₀ᵗ h, (X, s) b(X,) dξ, where

𝒟h(x, t) = h, (x, t) + h, (x, t) a(x) + ½ tr[h,, (x, t) b(x) b(x)"].

For any initial conditions (x, t) and any stopping time τ > t, we know from the definition of h that E_Q [h(X, τ)] < h(x, t). From this, it is natural to conjecture that 𝒟h(x, t) ≤ 0 for all (x, t). Moreover, we can see that
𝒟h(x, t) = 0 for all (x, t) in 𝒥. We summarize these conjectured necessary conditions on h, suppressing the arguments (x, t) everywhere for brevity.
On R × [0, T),

h ≥ g, 𝒟h ≤ 0, 𝒟(h − g) = 0. (41)

The last of these three conditions means that 𝒟h = 0 wherever h > g and conversely that h = g wherever 𝒟h < 0. Intuitively, this is a Bellman condition prescribing a policy of not exercising so long as the expected rate of change of the value function is not strictly negative. We also have the boundary condition

h(x, T) = g(x, T), x ∈ R*. (42)

Under strong technical assumptions that can be found in sources cited in the Notes, it turns out that these necessary conditions (41)-(42) are also sufficient for h to be the value function. This characterization (41)-(42) of the value function lends itself to a finite-difference algorithm for numerical solution of the value function h.

In order to incorporate nonzero interest rates, suppose that the shortrate process r can be written in the form r, = R(X,) for some bounded
R(·). By similar arguments, the variational inequality (41)-(42) for the value function h can then be written exactly as before, with the exception that h(x, t) is replaced everywhere by 𝒟h(x, t) − R(x)h(x, t).

Figure 8.3. Optimal Exercise Boundary for American Put

For the special case of the American put with a constant short rate and the constant-volatility underlying process S given by (35), a series of advances cited in the Notes has led to the following characterization of the solution, taking the state process X to be the underlying price process S. Because S is nonnegative, the continuation region 𝒥 can be treated as a subset of R₊ × [0, T). It turns out that there is an increasing continuously differentiable function s : [0, T) → R, called the optimaldefinition of T given by f(X_t, t, s) = E_t(τ_s)/τ_s. Extending the ideas in Section 7, conjecture the ordinary differential equation (ODE) solved by some a : [0, s] → R and b : [0, s] → R* such that f(x, t, s) = exp[a(s − t) + b(s − t) − x]. Do not forget to provide boundary conditions. This sort of ordinary differential equation (which we shall see again below) is easy to solve numerically, provided a solution exists
(which we assume). Perform a verification of your candidate solution for f under technical integrability conditions provided by you. Hint: If an Ito process is a martingale, its drift process must be zero.

(C) Suppose there are n ≥ 0 such zero-coupon bonds available for trade, with maturity dates T₁, T₂,..., Tₙ. Provide a spanning condition under which, in principle, an additional security with payoff at some time T given by a bounded ℱ_Tmeasurable random variable Z is redundant, given the opportunity to trade the n bonds and to borrow or lend continuously at the short rate r. Develop notation as you need it.

(D) We are now interested in pricing a zero-coupon bond option that provides the opportunity, but not the obligation, to sell at time T for a given price p > 0 the zero-coupon bond maturing at a given time s > T (paying one unit of account at maturity). The option is in the money at expiration if and only if exp[a(s − T) − b(s − T) − X_T] < p, which is the event A that b(s − T) · X_T < log p − a(s − T). It can be seen under integrability conditions that the price of the option at time 0 is therefore of the form c₁Q₁(A) − c₂Q₂(A), for some coefficients c₁ and c₂ and
Probability measures Q₁ and Q₂ equivalent to P. Provide the integrability conditions, the Radon-Nikodym derivatives of Q₁ and Q₂ with respect to P, and the definitions of c₁ and c₂. Explain how to obtain these coefficients c₁ and c₂ from market data.

(E) For each i ∈ {1, 2}, the density process ξ_i of Q_i can be shown (under technical integrability conditions) to be of the form ξ_i(t) = exp[α_i(t) + β_i(t) · X_t], for α_i and β_i solving ordinary differential equations. Provide these ordinary differential equations, their boundary conditions, and technical integrability conditions needed, justifying this solution.

--

(F) Under Q_i, for each i ∈ {1, 2}, provide a new stochastic differential equation for the state-vector process X driven by a standard Brownian motion B^{Q_i} in Rⁿ under Q_i. Define B^{Q_i}.

(G) By virtue of the previous steps, you have shown that the bond option price can be easily computed if one can compute any probability of the form Q_i(Y | X_T < y), for any Y ∈ Rⁿ and any y. One can compute P(Z < z), for a given random variable
Z and number z, if one knows the characteristic function φ : R → C of Z, defined by φ(u) = E[exp(iuZ)], where i = √−1 is the usual imaginary number. Thus, option pricing in this setting can be reduced to the calculation of the characteristic function (sometimes called the Fourier transform—the Fourier transform and the characteristic function are identical up to a scalar multiple) of Z = u · X_T under
Q₁ and Q₂. Based on the results of Section F, we conjecture that, fixing x and u, and defining Φ(X_t, t) = E_t[exp(iu · X_t)], we have

Φ(x, t) = exp[A(t) + B(t) · x],

where A and B are complex-valued coefficient functions that solve ordinary differential equations (ODEs). Taking as given the time-dependent coefficients
(K(t), H(t)) for X appropriate to the probability measure at hand, your task is now to provide these ODEs for A and B, with their boundary conditions, and to confirm the conjecture under integrability conditions provided by you that will arise as you verify your solution with Ito’s Formula. Hint: Remember that Φ(X_t, t)
is a complex number, and apply Ito’s Formula to get the drift (both the real and imaginary parts). You will see a restriction on the drift that will give you the desired ODEs. Express the ODEs as tidily as possible. Note: In practice, at this point, you would compute the solutions of the differential equation for each u, separately (there are tricks that can speed this up), and from the resulting characteristic function, numerically compute the needed numbers c₁, c₂, Q₁(A), and Q₂(A).

# Notes

General reviews of options, futures, or other derivative markets include those of
Avellaneda and Laurence (2000), Cox and Rubinstein (1985), Daigler (1993),
Duffie (1989), Hull (2000), Jarrow and Rudd (1983), Jarrow and Turnbull
(1999), Lamberton and Lapeyre (1997), Musiela and Rutkowski (1997), Prisman
(2000), Rubinstein (1999), Siegel and Siegel (1990), and Stoll and Whaley
(1993). For computational issues, see Chapter 12, Tavella and Randall (2000), and
Wilmott, Dewynne, and Howison (1993). Dixit and Pindyck (1993) is a thorough treatment, with references, of the modeling of real options, which arise in the theory of production planning and capital budgeting under uncertainty.

(B-D) The relationship between forwards and futures in Sections B, C, and D was developed by Cox, Ingersoll, and Ross (1981b). The derivation given here for the martingale property (8) of futures prices is original, although the formula itself is due to Cox, Ingersoll, and Ross (1981b), as is the subsequent replication strategy:
For additional work in this vein, see Bick (1994), Dezhbakhsh (1994), Duffie and

Stanton (1988), and Myneni (1992b). An explicit Gaussian example is given by
Jamshidian (1993b) and Jamshidian and Fein (1990). Grinblatt and Jegadeesh
(1996) derived the futures prices for bonds in the setting of a Cox-Ingersoll-Ross model of the term structure. Carr (1989) provides option-valuation models for assets with stochastic dividends, in terms of the stochastic model for forward prices on the underlying asset.

Bick (1997), Carr (1993b), Carr and Chen (1993), and Hemler (1990) value the option to deliver various grades of the underlying asset against the futures contract, sometimes called the cheapest-to-deliver option or quality option, and the associated problem of determining the futures price. This problem is related to that of valuing compound options, and options on the maximum or minimum of several assets, which was solved (in the Black-Scholes setting) by Geske (1979),
Johnson (1987), Margrabe (1978), Selby and Hodges (1987), and Stulz (1982).
For the related wildcard option, see Fleming and Whaley (1994).

Black (1976) showed how to extend the Black-Scholes option-pricing formula to the case of futures options. See also Bick (1988).

On put-call parity and symmetry, see Carr (1993a). The forward and futures prices for bonds in the Cox-Ingersoll-Ross model, addressed in Exercise 8.8, are found in Grinblatt (1994). A related problem, examined by Carr (1989), is the valuation of options when carrying costs are unknown.

(E-F) Beckers (1981) developed and promoted the idea of using implied volatility as a measure of the market volatility implicit in options prices. A generalized version of implied volatility is discussed by Bick and Reisman (1993). Cherian and
Jarrow (1998) explore a related “rationality” issue.

Derman and Kani (1994), Dupire (1994a,b), Jackwerth (1997, 2000),
Jackwerth and Rubinstein (1996a,b,c), Rubinstein (1994, 1995) and Toft and
Brown (1996) treat implied-tree models for option pricing, calibrating to a given family of smile curves or “risk-neutral” probability distributions. Andersen and
Brotherton-Ratcliffe (1995) take an “implied finite-difference” approach to the analysis of smiles. A general calibration approach is pursued by Lagnado and Osher (1996).

Breeden and Litzenberger (1978) described how one can invert for the state price deflator, in certain settings, from the prices of options at each exercise price.
This topic is further pursued by Ait-Sahalia and Lo (1998, 2000), Rady (1995), Rosenberg and Engle (1999).

Option pricing with stochastic volatility was proposed as an answer to the
“smile curve,” and analyzed, by Hull and White (1987), Scott (1987, 1992), andWiggins (1987), and since has been addressed by Amin (1993b), Amin and Ng
(1998), Amin and Morton (1994b), Ball and Roma (1994), Barles, Romano, and
Touzi (1993), Duan (1995), Heston (1993), Hofmann, Platen, and Schweizer see Lu and Yu (1993), Madan and Chang (1996), Platen and Schweizer
(1994), Renault, Pastorello, and Touzi (2000), Renault and Touzi (1992), and Touzi (1993, 1995).
Amin and Jarrow (1993) treat the problem of option valuation with stochastic interest rates, in a Heath-Jarrow-Morton setting. Melino and Turnbull (1990) illustrate an application to foreign-exchange option pricing. Heynen and Kat (1993)
and Heynen, Kemna, and Vorst (1994) provide formulas for prediction of volatility in a Markovian setting. Nelson (1990, 1991, 1992) treat the convergence of ARCH,
GARCH, and EGARCH models to stochastic-volatility models of the style considered in Section E, as well as related issues. Corradi (2000), however, shows that a more natural notion of convergence leaves a limiting volatility process defined by
(13) that is degenerate. Bollerslev, Chou, and Kroner (1992) and Taylor (1994)
survey applications in finance for ARCH and ARCH-related models, originated by Engle (1982). Heston and Nandi (1997) offered an option-pricing model in a
GARCH setting. Harvey, Ruiz, and Shephard (1994), Harvey and Shephard (1993), and Lamoureux and Lastrapes (1993) present related econometric techniques and results. Hobson and Rogers (1993) describe a model for endogenous stochastic volatility, while Hobson and Rogers (1998) show how markets can be complete with stochastic volatility. This is further pursued by Romano and Touzi (1997), who also provide for monotonicity of option prices with respect to the stochasticvolatility state variable.

Proposition E can be deduced from results in Karatzas and Shreve (1988).

Based on early work by Clark (1973), Geman, Madan and Yor (1999), Ghysels,
Gourieroux, and Jasiak (1995), Maghsoodi (1998), Redekop (1995), and Redekop and Fisher (1995) treat stochastic volatility through the effects of a random time change, sometimes called “market time.” Bergman, Grundy, and Wiener (1996b),
El Karoui, Jeanblanc, and Shreve (1998), Frey and Sin (1997), and Romano and
Touzi (1997) characterize the dependence of the option price on the underlying price and on the coefficients of the model, including volatility. Some of these results give conditions for convexity of the option price with respect to the underlying asset, using the method of stochastic flows.

Attempts have also been made to extend the econometric modeling in a timeseries setting to include observations on option prices in the data set used to estimate the parameters of the stochastic volatility process, as in Ait-Sahalia, Wang, and Yared (1998), Benzoni (1998), Chernov and Ghysels (2000), Guo (1998),
Pan (1999), Poteshman (1998), and Renault and Touzi (1992). Exploiting options data improves the econometric efficiency of the estimation, given the one-to-one relationship between V, and a given option price at time t. Other econometric approaches built around stochastic volatility include those of Papanicolaou, and Sircar (1999a, b,c).

Figure 8.1 is reproduced from Duffie, Pan, and Singleton (2000). The options data used to plot this figure are from the home page of Professor Yacine Ait-Sahalia of Princeton University. The figure represents a total of 87 options with maturities
(times to exercise date) ranging from 17 days to 318 days, and strike prices ranging from 0.74 to 1.17 times the underlying futures price.

The transform approach of Section F was originated by Stein and Stein
(1991). The first explicit results along these lines were by Heston (1993). Transform results for general affine models of Duffie, Pan, and Singleton (2000)
extend those of Bakshi, Cao, and Chen (1997), Bakshi and Madan (1997), Bates
(1996), Bates (1997), and Scott (1997). Option pricing by fast Fourier transform is illustrated by Carr and Madan (1999).

Option pricing in a jump-diffusion setting was originated by Merton (1976), and more recently treated by Amin (1993a), Andersen and Andreasen (1999),
Ball and Torous (1985), Bates (1997), Carr and Madan (1999), Eberlein and
Jacod (1997), Eberlein and Keller (1995), Eberlein, Keller, and Prause (1998),
Jorion (1988), Kou (1999), Lando (1995), Madan and Milne (1991), Madan,
Milne, and Shefrin (1989), Pappalardo (1996), Scott (1997), and Zhang (1994).
Pan (1999), Barndorff-Nielsen (1997), and Eraker, Johannes, and Polson (1999)
offer econometric evidence on jump behavior.

(G-H) McKean (1965), Merton (1973b), Harrison and Kreps (1979), and
Bensoussan (1984) did important early work on American option pricing.
Proposition G is from Karatzas (1988), although his technical conditions are slightly different. Karatzas defines the fair price of an American security, which turns out to be equal to the arbitrage-free price when both exist, and also extends
Merton’s analysis of perpetual options, those with no expiration. Jaillet, Lamberton, and Lapeyre (1988, 1990) review the treatment of the optimal-stopping valuation problem as a variational inequality, which can be written in the form (41). A decomposition of the American option in terms of an early exercise premium was proposed in a collection of papers by Jamshidian (1989c), Jacka (1991), Kim
(1990), and Carr, Jarrow, and Myneni (1992), working from the formulation by
McKean (1965) of the free-boundary problem, sometimes called a Stefan problem. Van Moerbeke (1976) was the first to demonstrate, among other results, that the optimal stopping boundary S* is continuously differentiable. In this regard, see also Ait-Sahalia (1995). Jorgensen (1994) and Myneni (1992a) survey this and other literature on American put option pricing in the Black-Scholes setting.
Numerical or approximate solutions to the American option price or the optimal exercise boundary are given by Ait-Sahalia and Lai (1997a, b, 1998), Allegretto,
Barles, Burdeau, Romano, and Samsoen (1995), Barone-Adesi, and Elliott (1993),
Barone-Adesi and Elliott (1991), Broadie and Detemple (1996), Carr (1994),
Carr and Faguet (1996), Geske and Johnson (1984), Huang, Subrahmanyam, and Yu (1996), and Longstaff and Schwartz (1998). See, also, the Notes of Chapter
12. The behavior of the optimal exercise boundary near expiration is treated by Ait-Sahalia (1995), Barles, Burdeau, Romano, and Samsoen (1993), Lamberton
(1998), and Charretour, Elliott, Myneni, and Viswanathan (1992). Buckdahn and
Hu (1995), Gukhal (1995a,b), Pham (1995), and Zhang (1993) treat American options with jumps in the underlying. Additional general work on optimal stopping in the setting of American options is offered by Beibel and Lerche (1995, 1997) and Kusuoka (1996).
de Matos (1993) gives a simulated-method-of-moments estimation technique for American options. Yu (1993) provides additional results on American option valuation. Broadie and Detemple (1995, 1997) provide pricing for American capped call options, and for options on multiple assets. Haug (1999) treats lookback barrier options.
Brennan and Schwartz (1977), McConnell and Schwartz (1986), and Pikovsky and Shreve
(1996) analyze the valuation of securities for which both the buyer and the seller hold American options, such as callable convertible debt.

(H) The sell-at-the-max and buy-at-the-min lookback option valuation is from
Boyle, Emanuel, and McPherson (1979). The particular representation of the sellat-the-max put formula is copied from Conze and Viswanathan (1991a). The distribution of the maximum of a Brownian motion path between two dates, and related results on the distribution of first passage times, can be found in Chuang,
(1994), Dassios (1994), Harrison (1985), and Ricciardi and Sato (1998). For other lookback option valuation results, see Conze and Viswanathan (1991a), Davydovand Linetsky (1999a, b), Duffie and Harrison (1993), Hobson (1998), Ju (1997b), and Shepp and Shiryaev (1993).

The Asian option, based on an arithmetic average of the underlying price process, is analyzed by Décamps and Koehl (1994), Geman and Yor (1993), Oliveira
(1994), Rogers and Shi (1995), and Yor (1991). Akahari (1993) and Yor (1993)
treat the related problem of median-price options. Bakshi and Madan (2000), He and Takahashi (1995), and Ju (1997a) consider average-rate options.

The hedging of Asian and lookback options is analyzed by Kat (1993). For hedging under leverage constraints, see Naik and Uppal (1994). For hedging with a “minimax” criterion, see Howe and Rustem (1994a, b).

Forms of barrier options, which are variously known as knock-outs, knock-ins, down-and-outs, up-and-ins, limited-risk options, and lock-in options, are covered by Carr
(1995), Carr and Ellis (1994), Conze and Viswanathan (1991a), Haug (1999), Merton (1973b), Sbuelz (1998), and Yu (1993).

Nahum (1998) treats options dependent on a maximum over a discrete set of times.

Andersen, Andreasen, and Brotherton-Ratcliffe (1998) and Delbaen and Yor (1999) consider passport options.

For additional methods for the analysis of path-dependent options, see Kind,
Lipster, and Runggaldier (1991), Zhou (1997a), and Zou and Derman (1996).

Chesney, Jeanblanc, and Yor (1997) and Schröder (1999a, b, c, d) use advanced transform methods to analyze path-dependent options, such as Asian, barrier, and “Parisian options,” a form of barrier option. Jamshidian (1997a)
provides methods for the valuation of double-barrier options.

Additional Topics: Term-structure models such as those applied in Chapter 7 have been applied to commodity option valuation by Grauer and Litzenberger
(1979), Jamshidian (1991b, 1993b), Miltersen and Schwartz (1998), and in other sources cited in Chapter 7. Grabbe (1983) developed a foreign-exchange version of the Black-Scholes model. Nielsen and Sad-Requejo (1992) further treat foreignexchange option valuation.

The hedging coefficients, “delta,”“gamma,” and so on, associated with derivative securities are studied by Carr (1991).

On option pricing with transactions costs and constraints, see Barles and Soner (1998), Bergman (1985a), Frey (1996), Ma and Cvitanić (1996),
Subramanian (1997), and references cited in the Notes of Chapter 6. Johnson and Shanno (1987) and Rich (1993) deal with the impact of default risk on the
Black-Scholes approach, a topic revisited in Chapter 11. Brennan and Schwartz
(1980b) present a model for the valuation of convertible bonds.

The definition and pricing result for the market-timing option is from
Ordentlich (1996). Gerber and Shiu (1994) describe a computational approach to option pricing based on the Esscher transform. Heston (1997) considers option pricing with infinitely divisible distributions for the underlying.

Andersen (1995) considers bivariate binary options. Davydov and Linetsky
(1998) and Linetsky (1999) treat step options and double-step options. Flesaker
(1991) considers cases in which the underlying is unobservable at expiration.

Frey and Stremme (1997) consider feedback effects, allowing for hedging activity to influence the price of the option.

Based on early work by Jamshidian (1989b) for bond option pricing under the forward measure, Geman, El Karoui, and Rochet (1995) and Schröder (1999)
treat changes of numeraire in the valuation of futures, forwards, and options.

Portfolio and Consumption Choice

THIS CHAPTER PRESENTS basic results on optimal portfolio and consumption choice, first using dynamic programming, then using general martingale and utility-gradient methods. We begin with a review of the
Hamilton-Jacobi-Bellman equation for stochastic control, and then apply it to Merton’s problem of optimal consumption and portfolio choice in finite- and infinite-horizon settings. Then, exploiting the properties of equivalent martingale measures from Chapter 6, Merton’s problem is solved once again in a non-Markovian setting. Finally, we turn to the general utility-gradient approach from Chapter 2, and show that it coincides with the approach of equivalent martingale measures.

# A. Stochastic Control

Dynamic programming in continuous time is often called stochastic control and uses the same basic ideas applied in the discrete-time setting of
Chapter 3. The existence of well-behaved solutions in a continuous-time setting is a delicate matter, however, and we shall focus mainly on necessary conditions. This helps us to conjecture a solution that, if correct, can often be validated.

Given is a standard Brownian motion B = (B^1,..., B^K) in R^K on a probability space (Ω, ℱ, P). We fix the standard filtration F = {ℱ_t : t ≥ 0} of B and begin with the time horizon [0, T] for some finite T > 0. The primitive objects of a stochastic-control problem are

* a set A ⊂ R^m of actions, for some integer m ≥ 1.
* a set Y ⊂ R^K of states, for some integer K ≥ 1.
* a set 𝒞 of A-valued adapted processes, called controls.
* a controlled drift function g: A × Y → R^K.
* a controlled diffusion function h: A × Y → R^{K×d}.
* a running reward function f: A × Y × [0, T] → R.
* a terminal reward function F: Y → R.

The state space Y is not to be confused with the underlying set Ω of
“states of the world.” A control c in 𝒞 is admissible given an initial state y in Y if there is a unique Itô process Y^c valued in Y with

dY^c_t = g(c_t, Y^c_t) dt + h(c_t, Y^c_t) dB_t; \quad Y^c_0 = y. \tag{1}

For admissibility, technical conditions are required of c, g, and h.

Let 𝒞_t(y) denote the set of admissible controls given initial state y. We assume that the primitives (A, Y, 𝒞, g, h, f, F) are such that, given any initial state y ∈ Y, the utility of any admissible control c is well defined as

V^c(y) = E\left[ \int_0^T e^{-\rho s} f(c_s, Y^c_s, s) ds + e^{-\rho T} F(Y^c_T) \right],

which we allow to take the values −∞ or +∞. The value of an initial state y in Y is then

V(y) = sup_{c ∈ 𝒞_t(y)} V^c(y), \tag{2}

with V(y) = −∞ if there is no admissible control given initial state y.

If V^{c*}(y) = V(y), then c* is an optimal control at y. (One may note that this formulation allows for the possibility that an optimal control achieves infinite utility.)

One usually proceeds by conjecturing that V(y) = J(y, 0) for some J in C^{1,2}(Y × [0, T)) that solves the Bellman equation:

sup_{a ∈ A} { BJ(y,t) + f(a,y,t) } = 0, \quad (y,t) ∈ Y × [0,T), \tag{3}

where
BJ(y,t) = J_t(y,t) + L^a J(y,t) + ½ Tr[ h(a,y) h(a,y)^T J_{yy}(y,t) ], with the boundary condition J(y, T) = F(y), \quad y ∈ Y. \tag{4}

An intuitive justification of (3) is obtained from an analogous discrete-time, discrete-state, discrete-action setting, in which the Bellman equation would be something like

J(y_n, t_n) = max_{a} { f(a, y_n, t_n) + E[ J(Y_{t_{n+1}}, t_{n+1}) | Y_{t_n} = y_n, c_{t_n} = a ] },

where f(a, y, t) is the running reward per unit of time. (The reader is invited to apply imagination liberally here. A complete development and rigorous justification of this analogy goes well beyond the goal of illustrating the idea. Sources that give such a justification are cited in the Notes.)
For any given control process c, this discrete-time Bellman equation of Chapter 3 implies that

E[ J(Y_{t+Δt}, t+Δt) - J(Y_t, t) ] + f(c_t, Y_t, t) Δt ≤ 0,

which, for a model with intervals of length Δt, may be rewritten
E[ J(Y_{t+Δt}, t+Δt) - J(Y_t, t) ] + f(c_t, Y_t, t) Δt ≤ 0.

Now, returning to the continuous-time setting, dividing the last equation by Δt, and taking limits as Δt → 0 leaves, under technical conditions described in Chapter 5,

BJ(y,t) + f(a,y,t) ≤ 0,

with equality if c attains the supremum in the discrete version of the
Bellman equation. This leads, again only by this incomplete heuristic argument, to the Bellman equation (3).

The continuous-time Bellman equation (3) is often called the
Hamilton-Jacobi-Bellman (HJB) equation. One may think of J(y,t) as the optimal utility remaining at time t in state y. Given a solution J to (3)-(4), suppose that a measurable function c* : Y × [0, T] → A is defined so that,dimensional setting of Chapter 2.) We would next like to see how to deduce an optimal choice \( c^* \) from this first-order condition (57). We may have a significant amount of structure with which to determine \( c^* \) on this basis. First, from Chapter 6, we know that a state-price deflator \( \pi \) is given, under regularity, by

\[
\pi_t = \pi_0 \exp\left( - \int_0^t \theta_s^\top dB_s \right), \tag{58}
\]

where \( \zeta \) is the density process for some equivalent martingale measure, which implies that \( d\zeta_t = -\zeta_t \theta_t^\top dB_t \) for a market-price-of-risk process \( \theta \) for the assets. Second, \( U \) may be one of the popular utility functions for which we can calculate the gradient \( \nabla U(c) \) at any \( c \). Finally, we can attempt to invert for an optimal \( c^* \) by matching the Riesz representation of \( \nabla U(c^*) \) to one of the state-price deflators that we can calculate from (58).

In the case of additive utility, for example, if \( c^* \) is optimal, then a state price deflator \( \pi \) can be chosen, for some scalar \( k > 0 \), by \( k\pi_t = u_c(c^*_t, t) \), so that \( c^*_t = I(k\pi_t, t) \), where \( I(\cdot, t) \) inverts \( u_c(\cdot, t) \). Finally, we need to choose
\( k \) so that \( c^* \) is budget-feasible. For the case of complete markets, it suffices, by the same numeraire invariance argument made earlier, that

\[ c^*_0 = B\left( \int_0^T I(k\pi_t, t) \pi_t \, dt \right).
\tag{59}
\]

Provided \( I(\cdot, t) \) has range \( (0, \infty) \) for all \( t \), the arguments used in Section F can be applied for the existence of some scalar \( k > 0 \) satisfying (59). It is enough, for instance, that a market-price-of-risk process \( \theta \) can be chosen to be bounded, and that \( J \) satisfies a uniform growth condition in its first argument. The Notes cite examples of a nonadditive utility function
\( U \) with the property that for each deflator \( \pi \) in a suitably general class, one can recover a unique consumption process \( c^* \) with the property that
\( \nabla U (c^*) \) has \( \pi \) as its Riesz representation. Subject to regularity conditions, the habit-formation and recursive-utility functions have this property.

For the case of incomplete markets (for which it is not true that
\( \text{rank}(a) = d \) almost everywhere), all of the above steps can be carried out in the absence of arbitrage, except that there need not be a trading strategy \( \theta^* \) that finances the candidate solution \( c^* \). Papers cited in the Notes have taken the following approach. With incomplete markets, there is a family of different market-price-of-risk processes. The objective is to choose a market-price-of-risk process \( \pi^* \) with the property that, when matching the Riesz representation of the utility gradient to \( k\pi^* \), we can

224 9. Portfolio and Consumption Choice

choose \( k \) so that \( c^* \) can be financed. This can be done under technical regularity conditions.

# Exercises

9.1 For the candidate optimal portfolio control \( g^t = \theta \) given by the right-hand side of (22), verify that (28) is indeed a martingale as asserted.

9.2 Solve Merton’s problem in the following cases. Add any regularity conditions that you feel are appropriate.

(A) Let \( T \) be finite, \( F = 0 \), and \( u(c, t) = e^{Pt} c^\alpha/\alpha \), \( \alpha \in (0, 1) \).

(B) Let \( T \) be finite, \( F = 0 \), and \( u(c, t) = \log c \).

(C) Let \( T = +\infty \) and \( u(c, t) = e^{Pt} c^\alpha/\alpha \), \( \alpha \in (0, 1) \). Verify the solution given by
\( c_t = \gamma W_t \) and \( \rho = (\alpha''')^{-1} A/(1 - \alpha) \), where \( \gamma \) is given by (32). Verify the so-called transversality condition (31) with \( \gamma > 0 \).

9.3 Extend the example in Section D, with \( v(\xi, w) = w^\alpha/\alpha \), to the case without a riskless security. Add regularity conditions as appropriate.

9.4 The rate of growth of capital stock in a given production technology is determined by a “random shock” process \( Y \) solving the stochastic differential equation

\[ dY_t = (b - \kappa Y_t) \, dt + \sigma \sqrt{Y_t} \, dB_t; \quad Y_0 = y \in \mathbb{R}_+, \quad t \geq 0, \]

where \( b \), \( \sigma \), and \( \kappa \) are strictly positive scalars with \( 2b > \sigma^2 \), and where \( B \) is a standard Brownian motion. Let \( \mathcal{C} \) be the space of nonnegative adapted consumption processes satisfying \( \int_0^T c_t \, dt < \infty \) almost surely for all \( T > 0 \). For each \( c \) in \( \mathcal{C} \), a capital stock process \( K^c \) is defined by

\[ dK^c_t = \big( K^c_t h Y_t - c_t \big) \, dt + K^c_t \epsilon \sqrt{Y_t} \, dB_t; \quad K^c_0 = x > 0, \]

where \( h \) and \( \epsilon \) are strictly positive scalars with \( h > \epsilon^2 \). Consider the control problem

\[
V(x, y) = \sup_{c \in \mathcal{C}} \mathbb{E} \left[ \int_0^T e^{-\rho t} \log(c_t) \, dt \right]
\]

subject to \( K^c_t > 0 \) for all \( t \) in \( [0, T] \).
(A) Let \( C: \mathbb{R}_+ \times [0, T] \rightarrow \mathbb{R}_+ \) be defined by
\( C(x, t) = \) and let \( K \) be the solution of the SDE

\[ dK_t = \big[ K_t h Y_t - C(K_t, t) \big] \, dt + K_t \epsilon \sqrt{Y_t} \, dB_t; \quad K_0 = x > 0.
\]

Finally, let \( c^* \) be the consumption process defined by \( c^*_t = C(K_t, t) \). Show that \( c^* \)
is the unique optimal-consumption control. Hint: Verify that \( V(x, y) = J(x, y, 0) \), where \( J \) is of the form

\[
J(x, y, t) = A_1(t) \log(x) + A_2(t) y + A_3(t), \quad (x, y, t) \in \mathbb{R}_+ \times \mathbb{R}_+ \times [0, T), \]

where \( A_1 \), \( A_2 \), and \( A_3 \) are (deterministic) real-valued functions of time. State the function \( A_1 \), and differential equations for \( A_2 \) and \( A_3 \).

(B) State the value function and the optimal consumption for the infinite-horizon case. Add regularity conditions as appropriate.

9.5 An agent has the objective of maximizing \( \mathbb{E}[u(W_T)] \), where \( W_T \) denotes wealth at some future time \( T \) and \( u: \mathbb{R} \rightarrow \mathbb{R} \) is increasing and strictly concave.
The wealth \( W_T \) is the sum of the market value of a fixed portfolio of assets and the terminal value of the margin account of a futures trading strategy, as elaborated below. This problem is one of characterizing optimal futures hedging. The first component of wealth is the spot market value of a fixed portfolio \( \rho \in \mathbb{R}^M \) of \( M \)
different assets whose price processes \( S^{(1)}_t, \ldots, S^{(M)}_t \) satisfy the respective stochastic differential equations

\[ dS^{(m)}_t = \rho_m(t) \, dt + \sigma_m(t) \, dB_t; \quad t \in [0, T], \quad S^{(m)}_0 = 1, \quad m = 1, \ldots, M, \]

where, for each \( m \), \( \rho_m : [0, T] \rightarrow \mathbb{R} \) and \( \sigma_m : [0, T] \rightarrow \mathbb{R}^d \) are continuous. There are futures contracts for \( K \) assets with delivery at some date \( T' > T \), having futuresprice processes \( F^{(1)}_t, \ldots, F^{(K)}_t \) satisfying the stochastic differential equations

\[ dF^{(k)}_t = m_k(t) \, dt + v_k(t) \, dB_t; \quad t \in [0, T], \quad 1 \leq k \leq K, \]

where \( m_k \) and \( v_k \) are continuous on \( [0, T] \) into \( \mathbb{R} \) and \( \mathbb{R}^d \), respectively. For simplicity, we assume that there is a constant short rate \( r \) for borrowing or lending. One takes a futures position merely by committing oneself to mark a margin account to market. Conceptually, that is, if one holds a long (positive) position of, say, ten futures contracts on a particular asset and the price of the futures contract goes up by a dollar, then one receives ten dollars from the short side of the contract.
(In practice, the contracts are largely insured against default by the opposite side, and it is normal to treat the contracts as default-free for modeling purposes.) The margin account earns interest at the riskless rate (or, if the margin account balance is negative, one loses interest at the riskless rate). We ignore margin calls or borrowing limits. Formally, as described in Section 8C, the futures-price process is actually the cumulative-dividend process of a futures contract; the true price process is zero. Given any bounded adapted process \( \delta = (\delta_t^{(1)}, \ldots, \delta_t^{(K)}) \) for the agent’s futures-position process, the agent’s wealth at time \( T \) is \( \rho^\top S_T + e^{rT} X_T \), where
\( X \) is the Itô process for the agent’s margin account value, defined by \( X_0 = 0 \) and
\( dX_t = r X_t \, dt + \sum_k \delta_t^{(k)} dF_t^{(k)} \).

(A) Set up the agent’s dynamic hedging problem for choice of futures-position process \( \delta \) in the framework of continuous-time stochastic control. State the Bellman equation and first-order conditions. Derive an explicit expression for the

226 9. Portfolio and Consumption Choice

optimal futures position \( \delta^* \), involving the (unknown) value function. Make regularity assumptions such as differentiability and nonsingularity. Hint: Let \( W_t = \)
\( \rho^\top S_t + e^{-r t} X_t \), \( t \in [0, T] \).

(B) Solve for the optimal policy \( \delta \) in the case \( m = 0 \), meaning no expected futuresprice changes. Add any regularity conditions needed to prove optimality.

(C) Solve the problem explicitly for the case \( u(w) = -e^{-\alpha w} \), where \( \alpha > 0 \) is a scalar risk-aversion coefficient. Prove optimality.

9.6 In the setting of Section B, consider the special case of the utility function

\[
U(c) = \mathbb{E} \left[ \int_0^T \log(c_t) \, dt + \log(W_T) \right], \]

obtain a closed-form solution for Merton’s problem (13). Hint: The mixture of logarithm and power function in the utility makes this a situation in which themartingale approach has an advantage over the Bellman approach, from which it might be difficult to conjecture a value function. Once the optimal-consumption policy is found, do not forget to calculate the optimal portfolio trading strategy.

9.7 (Utility-Gradient Example). Suppose B is a standard Brownian motion and there are two securities with price processes S and B given by

dS_t = μ_t S_t dt + σ_t S_t dB_t, S_t > 0, dB_t = r_t B_t dt, B_t > 0,

where μ, σ, and r are bounded adapted processes with μ_t > r_t for all t. We take the infinite-horizon case, with utility function U defined by

U(c) = E[∫_0^∞ e^{-ρt} u(c_t) dt],

where α ∈ (0, 1) and ρ ∈ (0, ∞). Taking the utility-gradient approach of Section H, c* is, in principle, an optimal choice if and only if

∫_0^∞ m_t c_t dt = u,

where VU(c) has Riesz representation η, and S^η and B^η are martingales. Assuming that the solution c* is an Ito process with

dc_t = c^*_μ dt + c^*_σ dB_t,

we can write

dη_t = η_b(t) dt + η_σ(t) dB_t,

for processes η_b and η_σ that can be solved explicitly in terms of c^* and σ^* from
Ito’s Formula and the fact that η_t = α e^{-ρt} u(c_t)^{α-1}. Assuming that S^η and B^η are indeed martingales, solve for η_b and η_σ explicitly.

9.8 Verify that, as defined by (35) and (36), Q is indeed an equivalent martingale measure, including the property that var(Q) < ∞.

9.9 (Constrained Investment Behavior). Security markets are characterized by price processes S = (S_0, …, S_d) and B, with

dB_t = r_t B_t dt, B_t > 0,

for a bounded adapted process r, and with

dS_t = S_t μ_t dt + S_t σ_t dB_t,

where, for each i, μ_i and σ_i are bounded adapted processes in R and R^d, respectively. We also assume that I_t = (σ_t σ_t')^{-1} is well defined and bounded. With a trading strategy specified in terms of a bounded adapted process θ valued in
R^d with ∫_0^T |θ_t|^2 dt < ∞, and with a nonnegative consumption process c, the wealth process W^{θ,c} of an investor is defined by

dW_t^{θ,c} = [W_t^{θ,c} (r_t + (μ_t - r_t)θ_t) - c_t] dt + W_t^{θ,c} σ_t θ_t dB_t, W_0^{θ,c} = w,

where μ_t = (μ_1, …, μ_d)' and where w > 0 is a given constant. The investmentconsumption strategy (θ, c) is admissible if W_t^{θ,c} > 0 for all t. Consider an investor with the utility criterion

U(c) = E[∫_0^T e^{-ρt} u(c_t) dt],

where ρ > 0 is a constant, and c is chosen from the set of nonnegative adapted processes such that U(c) is well defined.

(A) (Unconstrained Case). Let G*(r, w, a) denote the set of solutions to the investor’s optimization problem,

sup U(c), (θ,c) ∈ G(w),

where G(w) is the set of admissible strategies. Calculate G*(r, w, a).

(B) (Leverage Constraints). Let G(w, ε) = {(θ,c) ∈ G(w) : |θ| ≤ ε}, where ε is a nonnegative bounded adapted process that sets an upper bound on the leverage of the investment strategy. The investor’s problem is now

sup U(c).
(θ,c) ∈ G(w, ε)

Solve this leverage-constrained problem. Hint: Reduce the problem to that of the unconstrained case by an adjustment of the interest rate r, to reflect the shadow

Price of the leverage constraint, so that the problem may be effectively solved unconstrained.

228 9. Portfolio and Consumption Choice

(C) (Leverage and Short-Sales Constraints). Let G(w, ε, b) = {(θ,c) ∈ G(w, ε) : θ_i ≥ -b_i},

where ε is as above and b = (b_1, …, b_d), where b_i is for each i a nonnegative bounded adapted process that places, in addition to a leverage constraint, a bound on short sales as a fraction of portfolio value. Now, solve:

sup U(c).
(θ,c) ∈ G(w, ε, b)

Hint: Again, reduce to the unconstrained case, this time by suitable adjustment of all of the return coefficients (r, μ, σ) to reflect the shadow prices of the constraints.

9.10 (Investment and Price Behavior with Jumps). The objective of this exercise is to extend the basic results for consumption-investment models and asset pricing to an economy in which the volatilities and expected rates of return of the available securities may change suddenly, and depend on a “regime” state process defined by a two-state Markov chain Z, as defined in Appendix F. When a regime switch occurs, the price may jump as well, for example to reflect the sudden change in the distribution of returns on equilibrium asset values.

We fix a probability space on which is defined a standard Brownian motion B in R^d and the two-state continuous-time Markov chain Z, as defined in Appendix F, with states 0 and 1, and transition intensities λ(0) and λ(1). We let M denote the compensated version of Z.

Suppose X = (X^0, X^1, …, X^N) is an adapted process in R^{N+1} for the prices of N +1 securities. For each i > 0, we assume that

dX^i = μ_i(Z_t) X^i dt + X^i σ_i(Z_t) dB_t + X^i β_i(Z_t) dM_t, X^i_0 > 0,

where, for each j ∈ {0, 1},

σ_i(j) is the i-th row of a constant matrix σ(j) in R^{N×d},

μ_i(j) is a constant.

β_i(j) is a constant strictly less than 1 in absolute value.

This implies, in particular, that within a “regime,” each process X^i behaves as a geometric Brownian motion of the sort used in the Black-Scholes model of option pricing. When the regime changes, the price process jumps and its drift and diffusion parameters change. When the regime changes from 0 to 1, for example, the price of risky security i jumps by a multiplicative factor of i(0).
When the regime changes from 1 to zero, the price of risky security i jumps by a multiplicative factor of η_i(1).

Given a short-rate process {R(Z_t) : t > 0}, for given constants R(0) and R(1)
the market value of an investment rolled over at the short rate defines a value process X^0 by

dX^0 = R(Z_t) X^0 dt; X^0_0 > 0.

The filtration of tribes generated by (B, Z), and augmented with null sets as above, defines the information available to investors. A trading strategy is a predictable R^{N+1}-valued process θ such that the stochastic integral ∫ θ dX exists
(Note the informational restriction to predictable trading strategies, as defined in
Appendix F. With merely the requirement of adapted trading strategies, a position could be taken at a jump time τ based on information associated with the outcome of the jump.) A trading strategy θ is self-financing if

θ_t' X_t = θ_0' X_0 + ∫_0^t θ_s' dX_s, 0 < t < T.

(A) (Complete Markets and Equivalent Martingale Measure). Find conditions on the primitive functions (μ, σ, r, λ, β) defining asset returns that are sufficient for the existence of a unique equivalent martingale measure Q for the deflated price process X/X^0. (Do not assume that λ or β are trivial.) Show, under these conditions, for any bounded F_T-measurable random variable Y, there is a selffinancing trading strategy θ with bounded market value θ_T · X_T, with θ_T · X_T = Y,

θ_0 · X_0 = E^Q[Y exp(∫_0^T r_s ds) I_{τ > T} Z_1(τ) f(τ)]?

Also, given the existence of an equivalent martingale measure, show that any selffinancing trading strategy θ satisfying θ_t · X_t > 0 for all t cannot be an arbitrage.
Hint: For a given equivalent probability measure Q, let

ξ_t = dQ/dP|_{F_t}, t < T.

Because ξ is a martingale, it has a martingale representation in the form

dξ_t = ξ_t φ(t) dB_t + ξ_t ψ(t) dM_t,(c, 0) is admissible if \( c \in \mathcal{L} \), and if \( \pi \in \mathcal{L}(X) \) is a trading strategy satisfying \[
X_t^{\pi,c} = w + \int_0^t \left( r X_s^{\pi,c} + \pi_s (b - r\sigma) - c_s \right) ds + \int_0^t \pi_s \sigma dB_s, \quad t \in [0,T],
\] where \( w > 0 \) is a given constant and \( c, \pi \) are nonnegative. We now have the problem, for each initial wealth \( w \) and each initial regime \( i \in \{0,1\} \), \[
J(i,w) = \sup_{(c,\pi) \in \mathcal{A}(w)} \mathbb{E}[U(c)]. \tag{60}
\]
Using the martingale approach, compute the optimal-consumption process up to a missing scalar Lagrange multiplier. Justify your answer, making technical assumptions as needed.

(C) (Parametric Example). We change the formulation in part (B) by letting \( T = +\infty \) and by considering the special case \( u(c) = \frac{c^\alpha}{\alpha} \), for some \( \alpha \in (0,1) \). A consumption process \( c \) is nonnegative and adapted, with \( \int_0^t c_s ds < \infty \) for each \( t > 0 \). We also simplify the problem by assuming that \( \delta_i = 0 \) for all \( i \), meaning that a regime shift causes no jump in asset prices, but may cause a change in expected rates of returns, volatilities, and correlations. State the solution to (60), proving its optimality by reducing the supremum value function \( J \) defined by (60) to two unknown coefficients, \( k_0 \) and \( k_1 \), one for each initial regime. Using your extension of the Hamilton–Jacobi–Bellman equation for optimal control in this setting, obtain two nonlinear restrictions on these two unknown coefficients. Assume existence of a solution to this system of equations for \( k_0 \) and \( k_1 \). Compute the candidate optimal-consumption and portfolio fraction policies as explicitly as possible. Verify your candidate solution, under additional explicit regularity conditions on the primitive parameters as well as \( k_0 \) and \( k_1 \). Please be extremely careful to provide a complete proof of optimality, given \( k_0 \) and \( k_1 \).

(D) (Robinson Crusoe). Let \( d = 1 \) (one-dimensional Brownian motion). Robinson must consume at each time \( t \) from a physical stock \( K_t \) of consumption commodity, satisfying the production equation
\[ dK_t = \left[ n(Z_t) K_t - a \right] dt + K_t \sigma(Z_t) dB_t + K_t \delta(Z_t) dZ_t, \tag{61}
\] where \( n, \sigma, \) and \( \delta \) are real-valued functions on \( \{0, 1\} \) and \( c \) is a nonnegative adapted consumption process to be chosen by Robinson. We assume that \( |\delta| < 1 \). Robinson’s utility for consumption is defined by \[
U(c) = \mathbb{E} \left[ \int_0^\infty e^{-\rho t} u(c_t) dt \right],
\] for a given \( \rho \in (0, 1) \). Robinson’s problem is \[ \sup_{c \in \mathcal{A}} U(c), \tag{62}
\] where \( \mathcal{A} \) is the space containing any consumption process \( c \) such that the stock \( K_t \) of commodity solving (61) remains nonnegative for all \( t \). Solve (62). Hint: Conjecture the form of the value function. Now, for each initial state \( i \in \{0, 1\} \), consider the stopping time \( \tau \) of first transition to the other state. Begin your calculation of the unknown coefficients of the solution by conditioning on this stopping time \( \tau \).

(E) (Incomplete Information and Filtering). We now consider the special case of a single risky asset (\( N = 1 \)) for which, with each change in regime, there is no jump in the risky asset price (that is, \( \delta = 0 \)), no change in the interest rate (that is, \( R(1) = R(0) = r \) for some constant \( r \)), and no jumps in the volatility (that is, \( \sigma(1) = \sigma(2) = \sigma \) for some constant \( \sigma \)). With a change in regime, however, there is a change in the mean-rate-of-return coefficient. That is, \( \mu(1) \neq \mu(0) \). For simplicity, we will assume that \( \lambda(0) = \lambda(1) = \lambda \), for some constant \( \lambda > 0 \), so that the arrival intensity of a change in regime is the same in both regimes.

Suppose, however, that the investor is not able to observe the regime state process \( Z \), but can only observe the risky asset’s price process \( S = X^0 \). This means that, for the investor, the relevant filtration of tribes describing the available information is \( \mathcal{F}_t^S = \sigma(\{S_s : 0 \leq s \leq t\}) \).

Now solve the optimal portfolio investment strategy for an investor with the utility criterion \[
U(c) = \mathbb{E} \left[ \int_0^\infty e^{-\rho t} \log c_t dt \right],
\] where \( \rho > 0 \) is a constant, and \( c \) is chosen from the set of nonnegative adapted processes such that \( U(c) \) is well defined. Hint: It may assist you to work with a stochastic differential model for asset price behavior given the limited information available. For this, let \( p_t = \mathbb{P}(Z_t = 1 | \mathcal{F}_t^S) \) denote the conditional probability at time \( t \) that \( Z_t = 1 \), given the observed asset prices to that time. By adding and subtracting the same thing from the stochastic differential expression for \( S \), we have \[ dS_t = S_t m(p_t) dt + S_t \sigma dB_t,
\] where \[ dB_t = [\mu(Z_t) - m(p_t)] dt + d\tilde{B}_t,
\] and where, for any \( a \in [0, 1] \), \[ m(a) = a \mu(1) + (1 - a) \mu(0)
\] defines the conditional expectation of the mean rate of return on the risky asset given probability \( a \) that the unknown regime is 1. It can be shown, for the probability space \( (\Omega, \mathcal{F}, \mathbb{P}) \) and the limited filtration \( \{ \mathcal{F}_t^S : t > 0 \} \) available to the investor, that \( B \) is a standard Brownian motion. It turns out, moreover, that
\[ dp_t = \lambda (1 - 2p_t) dt + \sigma p_t (1 - p_t) d\tilde{B}_t,
\] where \( k = [\mu(1) - \mu(0)] / \sigma \). The initial condition \( p_0 \) is the investor’s prior probability assessment that \( Z(0) = 1 \). We have therefore effectively reduced the original investment problem to one of complete observation, with a stochastic mean rate of return \( m(p_t) \) determined by a separate Markov process \( p \) satisfying its own stochastic differential equation.

# Notes

A comprehensive treatment of the topic is provided by Karatzas and Shreve (1998). Other surveys include those of Quenez (1992) and Karatzas (1989).

Standard treatments of stochastic control in this setting are given by
Bensoussan and Rishel (1975), Krylov (1980), Bensoussan (1983), Lions (1981, 1983), and Fleming and Soner (1993). The book of Fleming and Soner (1993) treats viscosity solutions of the Hamilton–Jacobi–Bellman (HJB) equation. Among other advantages of this approach, it allows one to characterize the continuous-time stochastic-control problem as the limit of discrete Markov control problems of the sort considered in Chapter 3. Other work using viscosity methods includes that of Benth, Karlsen, and Reikvam (1999).

(B–D) Merton (1969, 1971), in perhaps the first successful application of stochastic control methods in an economics application, formulated and solved the problem described in Section B. (Another early example is Mirrlees [1974].) Extensions and improvements of Merton’s result have been developed by Aase (1988),
Fleming and Zariphopoulou (1991), Karatzas, Lehoczky, Sethi, and Shreve (1991),
Lehoczky, Sethi, and Shreve (1983, 1985), Sethi and Taksar (1988), and
Fleming (1991), Richard (1975), Jacka (1984), Ocone and Karatzas (1991)
(who apply the Malliavin calculus), and Merton (1990).

(E–G) The martingale approach to optimal investment described in Section F has been developed in a series of papers. Principal among these are Cox and
Huang (1989) and, subsequently, Karatzas, Lehoczky, and Shreve (1991).
This literature includes Cox (1983), Pliska (1986), Cox and Huang (1989),
Back (1986), Back and Pliska (1987), Huang and Pagés (1992), Tao (1989),
Slud (1991), Pagés (1987), Jeanblanc and Pontier (1990), Richardson (1989), and Xu and Shreve (1992a, b). For applications of duality techniques and other methods to multiperiod investment with constraints in incomplete complete markets, see Broadie, Cvitanić, and Soner (1998), Cuoco (1997). Cvitanić
(1995, 1997, 1999), Cvitanić and Karatzas (1992, 1993, 1995, 1996a, b), He,
Karatzas, and Soner (1998), Derviz (1996), He and Pages (1993), He and Pearson
(1991a, b), Karatzas, Lehoczky, Shreve, and Xu (1991), El Karoui and Quenez (1991), Ruegg (1996), and Tepla (1996).

For additional results with incomplete markets, see Adler and Detemple
(1988), Cuoco (1994), Cvitanić and Karatzas (1992, 1995), Cvitanić, Schachermayer, and Wang (1999), Duffie, Fleming, Soner, and Zariphopoulou (1997),
Duffie and Zariphopoulou (1993), Dybvig (1989), El Karoui and Jeanblanc
(1998), He and Pagés (1993), Koo (1998, 1999), Munk (2000b), Pagés (1987),
Scheinkman and Weiss (1986), and Svensson and Werner (1993).

For the case of shortsales constraints and other forms of portfolio restrictions, see Back and Pliska (1986), Brennan, Schwartz, and Lagnado (1997),Cuoco (1994), Cvitanić and Karatzas (1992, 1995), Dybvig (1995), Fleming and
Zariphopoulou (1991), He and Pagès (1993), Hindy (1995), Shirakawa (1994),
Vila and Zariphopoulou (1997), Xu and Shreve (1992a, b), and Zariphopoulou (1992, 1994).

(H) The utility-gradient approach to optimal investment of Section H is based on work by Harrison and Kreps (1979), Kreps (1981), Huang (1985c), Foldes (1978a, b, 1990, 1991a, b, 1992, 1996), Back (1991), and Duffie and Skiadas (1994), and is extended in these sources to an abstract setting with more general information and utility functions. Appendix G provides some additional information on the existence and calculation of utility gradients.

Additional Topics: For problems with mean-variance criteria in a continuoustime setting, see Ansel and Stricker (1994a), Bajeux-Besnainou and Portait (1993),
Bossaerts and Hillion (1997), Bouleau and Lamberton (1989), Duffie and Jackson
(1990), Duffie and Richardson (1991), Föllmer and Schweizer (1990), Föllmer and
Sondermann (1986), Gourieroux, Laurent, and Pham (1998), Lakner (1994a),
Lioui (1995), Schweizer (1994a, b, c, d), and Sekine (1998).

For optimality under various habit-formation utilities, see Chapman (1997),
Constantinides (1990), Detemple and Zapatero (1992), Ingersoll (1992), Ryder and Heal (1973), Schroder and Skiadas (1999), and Sundaresan (1989).

A model involving local substitution for consumption was developed by Hindy and Huang (1992, 1993a), and Hindy, Huang, and Kreps (1992). See also Bank and Riedel (1999) and Hindy, Huang, and Zhu (1997).

Ekern (1993) is an example of a model of irreversible investment. Dixit and
Pindyck (1993) review many other models of optimal production under uncertainty using stochastic-control methods. See, also, Chapter 11 and its Notes.

For a development of recursive utility in continuous-time settings, called
Stochastic differential utility, see Duffie and Epstein (1992b) (with Skiadas), and for related work including portfolio and consumption choice, see Ahn
(1993), Bergman (1985b), Duffie and Epstein (1992a), Duffie and Lions (1990),
Duffie and Skiadas (1994), Duffie, Schroder, and Skiadas (1997), El Karoui,
Peng, and Quenez (1997), Fisher and Gilles (1998b), Lazrak and Quenez
(1999), Ma (1991, 1993a, b), Schroder and Skiadas (1999), Svensson (1989), and Uzawa (1968). For the related problem of backward stochastic differential equations (BSDE), see Pardoux and Peng (1990) and Peng (1993b) for their seminal work, and for subsequent developments, see Alvarez and Tourin
(1996), Bally (1995), Barles, Buckdahn, and Pardoux (1997), Barles and Lesigne
(1997), Buckdahn (1995a, b), Cvitanić, Karatzas, and Soner (1998), Darling
(1995), El Karoui (1997), El Karoui and Huang (1997), El Karoui, Kapoudjian,

234 9. Portfolio and Consumption Choice

Pardoux, Peng, and Quenez (1997), El Karoui, Peng, and Quenez (1997), GegoutPetit and Pardoux (1996), Pardoux and Peng (1994), Pardoux (1997), Peng
(1993a), Pontier (1997), and Quenez (1997). For developments and applications of forward-backward stochastic differential equations (FBSDE), see Antonelli
(1993), Cvitanić and Ma (1996), Duffie, Geoffard, and Skiadas (1994), Ma,
Protter, and Yong (1994), and Ma and Yong (1995, 1999).

For an elegant extension of Merton’s problem that allows for proportional transactions costs, see Davis and Norman (1990). Other work on optimal investment problems in the case of transactions costs includes that of Akian,
Menaldi, and Sulem (1996), Akian, Sulem, and Taksar (1999), Alvarez (1991),
Arntzen (1994), Avellaneda and Paras (1994b), Balduzzi and Lynch (1997, 1999),
Cadenillas and Pliska (1999), Chang (1993), Clewlow and Hodges (1996),
Constantinides (1986), Cuoco and Liu (2000), Davis and Panas (1991), Duffie and
Sun (1990), Dumas and Luciano (1989), Edirisinghe, Naik, and Uppal (1993),
Fleming, Grossman, Vila, and Zariphopoulou (1989), Huang (1999), Jouini and
Kallal (1993a, b), Lynch and Balduzzi (1998), Pliska and Selby (1994), Schroder
(1993), Shreve and Soner (1994), Shreve, Soner, and Xu (1991), Taksar, Klass, and
Assaf (1988), Vayanos and Vila (1999), Weerasinghe (1998), and Zariphopoulou
(1992). See also the references cited in the Notes of Chapter 6.

On the existence of additive or other particular forms of utility consistent with given asset prices, sometimes called “integrability,” or an “inverse problem,”
see Bick (1986), Cuoco and Zapatero (2000), He and Huang (1994), He and
Leland (1993), Hodges and Carverhill (1992), and Wang (1993b). On turnpike problems, see Cox and Huang (1991, 1992), Dybvig, Rogers, and Back (1999), and Huang and Zariphopoulou (1999). For problems in settings with incomplete information, usually requiring filtering of the state, see Detemple (1986,
1991), Detemple and Murthy (1994a), Dothan and Feldman (1986), Gennotte
(1986), Duffie, Schroder, and Skiadas (1997), Föllmer and Schweizer (1990),
Honda (1997c), Karatzas (1991), Karatzas and Xue (1990), Kuwana (1994,
1995), Lakner (1994b, 1995), Ocone and Karatzas (1991), Pikovsky and Karatzas
(1996), and Schweizer (1994d). Exercise 9.10 is based on Honda (1997b, c). For more on portfolio choice with regime switching, see Honda (1996, 1997b). For the results on filtering used in Exercise 9.10, see Lipster and Shiryaev (1977).

For optimal investment with “advance information” (that is, based on enlargement of filtrations), see Amendinger, Imkeller, and Schweizer (1998) and Pikovsky and Karatzas (1996).

On portfolio and consumption choice with stochastic return distributions, see Liu (1999) and Schroder and Skiadas (1999).

Exercise 9.4 is from Cox, Ingersoll, and Ross (1985b). Exercise 9.9 is based in part on Cvitanić and Karatzas (1992, 1995) and Tepla (2000).

For optimal behavior of a “large investor,” that is, one who considers the impact of trading on prices, see Cuoco and Cvitanić (1998) and Sircar (1996).

On portfolio insurance, see Grossman and Zhou (1996). On optimal portfolio choice with logarithmic additive utility, there is a long history. A recent general treatment is given by Goll and Kallsen (1999). On the related growth-optimal policies, see Iyengar and Cover (1997) and work cited therein.

On policies allowing for a payoff with bankruptcy, see Sethi and Taksar (1992)
and Sethi, Taksar, and Prisman (1992).

# Equilibrium

THIS CHAPTER REVIEWS security market equilibrium in a continuous-time setting and derives several implications for security prices and expected returns. These include Breeden’s consumption-based capital asset pricing model (in both complete- and incomplete-market settings) as well as the Cox-Ingersoll-Ross model of the term structure.

# A. The Primitives

As usual, we let \( B = (B^1,\dots, B^d) \) denote a standard Brownian motion in
\(\mathbb{R}^d\) on a probability space \((\Omega, \mathcal{F}, P)\), and let \(\mathcal{F} = \{\mathcal{F}_t : t \geq 0\}\) denote the standard filtration of \(B\). The consumption space is the set \(\mathcal{L}\) of adapted processes satisfying \( \mathbb{E}\left( \int_0^T c_t^2 \, dt \right) < \infty \) for some fixed time horizon \(T > 0\).

There are \(m\) agents. Agent \(i\) is defined by a nonzero consumption endowment process \(e^i\) in the set \(\mathcal{L}\), nonnegative processes in \(\mathcal{L}\), and by a strictly increasing utility function \( U_i : \mathbb{R}_+ \rightarrow \mathbb{R} \).

As in Section 6L, a cumulative-dividend process is a finite-variance process of the form \( C = Z + V - W \), where \( Z = \int_0^\cdot \theta_s \, dB_s \) for some \(\theta \in \mathcal{V}(B)\), and where \(V\) and \(W\) are increasing adapted right-continuous processes.
For any time \(t\), the jump \( \Delta C_t = C_t - C_{t-} \) represents the lump-sum payment at time \(t\). For example, if the security is a unit zero-coupon bond that matures at time \(T\), then \( C_t = 0 \), \(t < T\), and \( C_t = 1 \), \(t > T\). By convention, any dividend process \(C\) satisfies \( C_{0-} = C_0 = 0 \). For example, a dividendrate process \(\delta\) in \(\mathcal{L}\) defines the cumulative-dividend process \( C = V - W \)
with \( V_t = \int_0^t \max(\delta_s, 0) \, ds \) and \( W_t = \int_0^t \max(-\delta_s, 0) \, ds \). There are \(N + 1\)
securities, numbered 0 through \(N\), defined by a cumulative-dividend process \( D = (D^0, D^1, \dots, D^N) \).As can be seen by taking expectations through (18) and using the fact that
E[∫_0^T 6_t dG_t] = 0. Thus (c_0) solves agent is problem (4).

Let θ be chosen in this fashion for each agent i > 1, and let θ^{(1)} = Σ_{i=2}^{m} θ^{(i)}. It can be checked from the linearity of stochastic integration that θ^{(1)} finances c^{(1)} – e^{(1)}, so (c^{(1)}, θ^{(1)}) is a solution to problem (4) for agent 1.
By construction, 7 f = 0. By the feasibility of (c^{(1)}, …, c^{(m)}), we conclude that {(c^{(i)}, θ^{(i)}), 1 < i < m} is an equilibrium. □

# E. Real Security Prices

The equilibrium {X; p; (c^{(i)}, θ^{(i)}), 1 < i < m} shown in the last theorem has a nominal security-price process X that is “risk-neutral,” in the sense of
(13). Relative to the price of the consumption commodity, or in real terms, security prices are not generally risk-neutral. For example, consider a particular security paying the nominal cumulative-dividend process C defined by C_t = ∫_0^t 8_s ds, for some nonnegative dividend-rate process 8 in L. We let Z denote the nominal price process of this security. By (13), Z =
E[∫_t^T 8_s ds]. The real price process S, defined by S_t = Z_t/p_t, and the real dividend-rate process δ, defined by δ_t = 8_t / p_t, are therefore related by

S_t = E[∫_t^T δ_s ds], t ∈ [0, T]. (19)

We can consider a more general cumulative-dividend process C that is increasing and right-continuous, allowing for the payment of lump-sum amounts at points in time, as for a coupon bond. Since the real dividend process δ corresponding to C is given by δ_t = ∫_0^t dC, the real price process S for a security promising the real cumulative-dividend process C is given from (13) by

S_t = E[∫_t^T p_s dC_s], t ∈ [0, T). (20)

A simple example is a real zero-coupon unit bond maturing at some time τ in (0, T], for which we have C_t = 0, t < τ, and C_t = 1, t ≥ τ. The real bond-price process is then given from (20) by

A_t = E[p_τ], t < τ, (21)

with A_t = 0, t > τ. This defines the term structure of interest rates.
Although we will have no need for it, the extension of (20) for a cumulative-dividend process C that is an Itô process may be calculated from the general formula given in Chapter 6 for the deflation of Itô dividend processes.

The central issue, to which we now turn, is a characterization of the consumption-price process p. For example, we will give sufficient conditions for p to be an Itô process. After the above normalization to real prices, this will imply that p is a state-price deflator in the sense of Chapter 6.

# G. Optimality with Additive Utility
For most of the remainder of the chapter, we will be exploiting the properties of smooth-additive utility functions, defined as follows.

Definition. A utility function U : R_+ → R is smooth-additive (u) if

U(c) = ∫_0^T u(c_t, t) dt,

where u : R_+ × [0, T] → R is smooth on (0, ∞) × [0, T] and, for each t in
(0, T], u(·, t) : R_+ → R is increasing, strictly concave, with an unbounded derivative u_c(·, t) on (0, ∞).

(c, t) ∈ dom U (22)

For the purposes of this definition, we call a function “smooth” if it can be extended to an open set with continuous derivatives of any order.
(In our applications, the order required will sometimes be as high as three). A special case of a utility function U that is smooth-additive (u) is that given by u(c, t) = e^{-αt}c^{α}/α, with α < 1 and α ≠ 0. If the consumptionprice process p is bounded, the Inada condition of unbounded u_c guarantees that consumption will be strictly positive.

Consider the choice problem in an Arrow-Debreu equilibrium with smooth-additive utility:

sup ∫_0^T u(c_t, t) dt subject to ∫_0^T p_t c_t dt ≤ w, (23)
c∈L_y

where p is the Riesz representation of the equilibrium price function Π and w > 0 is the market value Π(e) of the agent’s endowment e. Given the strict monotonicity and concavity of utility, the Saddle Point Theorem implies that a necessary and sufficient condition for c* to solve (23)
is the existence of a Lagrange multiplier γ > 0 such that c* solves the unconstrained problem

sup ∫_0^T [u(c_t, t) – γ p_t c_t] dt, (24)
c∈L_y

along with the complementary slackness condition E[∫_0^T p_t c_t dt] = w.
Naturally, one can do no better than to maximize u(c_t, t) – γ p_t c_t separately for each t and each state of the world. Since u_c(·, t) is unbounded, this implies, for optimal c*, that c* > 0 and that

u_c(c_t^*, t) = γ p_t, t ∈ [0, T]. (25)

In fact, this leads directly to a method for solving (23) that is described in
Section 9G, but that is not needed here. Relation (25) gives us our first characterization of the state-price deflator p in the security-spot market equilibrium studied in Sections D and E. We know, for some γ > 0, that

p_t = (1/γ) u_c(c_t^*, t), t ∈ [0, T], (26)

assuming that one of the agents has the optimal consumption process c^* and a utility function that is smooth-additive (u). The fact that the
Lagrange multiplier γ is unknown is of no consequence, since {γ p_t : t ∈
[0, T]} is also a state-price deflator for any constant γ > 0. This characterization of the state-price deflator is in terms of an individual agent’s

consumption process. Now we work toward a like characterization of p in terms of aggregate consumption, which is arguably more easily studied from empirical data.

# G. Equilibrium with Additive Utility

This section further characterizes state-price deflators under the assumption of smooth-additive utility. A proof of the following theorem is cited in the Notes.

Theorem. Suppose that the aggregate endowment process e is bounded away from zero and that, for each i, U_i is smooth-additive (u_i). Then there is an Arrow-Debreu equilibrium [Π, (c^{(1)},..., c^{(m)})] for which Π has a bounded Riesz representation p, and such that for all i, c^{(i)} is bounded away from zero.

Coupling this result with Theorem D, we have conditions for the existence of a security-spot market equilibrium under smooth-additive utility.

Corollary. Suppose, in addition, that the cumulative-dividend process D satisfies the dynamic spanning condition. Let X be given by (13). Then there are trading strategies (θ^{(1)},..., θ^{(m)}) such that [X; p; (c^{(i)}, θ^{(i)}), 1 < i < m] is a security-spot market equilibrium.

We fix the equilibrium consumption allocation (c^{(1)},..., c^{(m)}) and consumption-price process p of this result for the remainder of this section and the next. By Theorem C, (c^{(1)}, ..., c^{(m)}) is a Pareto optimal allocation. By Proposition C, there exists a nonzero “weight” vector Λ ∈ R^m such that (c^{(1)},..., c^{(m)}) solves the problem

sup ∑_{i=1}^m λ_i ∫_0^T u_i(c_t^{(i)}, t) dt subject to ∑_{i=1}^m c_t^{(i)} ≤ e_t. (27)

Because of the additive nature of utility, one can solve this problem separately for each time t in [0, T] and state ω in Ω. In order to see this, let u_y : R_+ × [0, T] → R be defined by

u_y(y, t) = sup ∑_{i=1}^m λ_i u_i(x_i, t) subject to x_1 + ... + x_m ≤ y. (28)
x∈R_+^m

Since (c^{(1)}, ..., c^{(m)}) solves (27), it follows that [c^{(1)}(ω, t),..., c^{(m)}(ω, t)] solves
Problem (28) for y = e(ω, t), except perhaps for (ω, t) in a null subset. (A set A ⊂ Ω × [0, T] is null if E[∫_0^T 1_A(ω, t) dt] = 0, where 1_A(t) is the random variable whose outcome is 1 if (ω, t) is in A, and is zero otherwise.) This is

244 10, Equilibrium

shown as follows. Suppose not, and let (b^{(1)},..., b^{(m)}) be a feasible allocation and A be a nonnull subset of Ω × [0, T] such that, for all (ω, t) in A,

∑_{i=1}^m λ_i u_i[b^{(i)}(ω, t), t] > ∑_{i=1}^m λ_i u_i[c^{(i)}(ω, t), t] (29)
i=1 i=1

Let (a^{(1)},..., a^{(m)}) be the feasible allocation defined by

a^{(i)}(ω,t) = b^{(i)}(ω, t), if (ω, t) ∈ A, = c^{(i)}(ω,t), otherwise.

Then
∑_{i=1}^m λ_i U_i(a^{(i)}) > ∑_{i=1}^m λ_i U_i(c^{(i)}), i=1 i=1 contradicting the fact that (c^{(1)},..., c^{(m)}) solves (27).

An exercise in applying the Implicit Function Theorem shows that the utility function U_y : R_+ → R, defined by

T U_y(e) = ∫_0^T u_y(e_t, t) dt (30)

is smooth-additive (u_y). With γ > 0, the first-order conditions for optimality of x^* in (28) imply that

λ_i u_{i,c}(x_i^*, t) = u_{y,c}(y, t), t ∈ [0, T], (31)

where the subscript “c” indicates a derivative in the customary way. This implies that, almost everywhere and for all i,

λ_i u_{i,c}(c_t^{(i)}) = u_{y,c}(e_t). (32)derivative) of the current capital stock. Include a boundary condition.

10.5 Consider the following continuous-time analogue to the Markov single-agent asset pricing model of Chapter 4. Let X be the Ito process in \( \mathbb{R}^N \) solving the stochastic differential equation

\[ dX_t = \nu(X_t) dt + \sigma(X_t) dB_t; \quad X_0 = x \in \mathbb{R}^N, \tag{54} \]

where \( \nu : \mathbb{R}^N \to \mathbb{R}^N \) and \( \sigma : \mathbb{R}^N \to \mathbb{R}^{N \times N} \) are sufficiently well behaved for existence.
There are \( N \) securities in total supply of one each, paying dividends according to a bounded measurable function \( f : \mathbb{R}^N \to \mathbb{R}^N \). That is, security \( n \) pays dividends at the rate \( f_n(X_t) \) at time \( t \). The security-price process is an Ito process
\( S \) in \( \mathbb{R}^N \). The single agent chooses a nonnegative real-valued bounded adapted consumption process \( c \) and a bounded trading strategy \( \theta = (\theta^1, \dots, \theta^N) \). The wealth process \( W \) of an agent initially endowed with all of the securities and adopting the consumption-portfolio strategy \( (c, \theta) \) is thus given by

\[ W_t = 1 + \int_0^t [W_s r_s - c_s + f_s \cdot \mathbf{1} + \theta_s \cdot (dS_s - r_s S_s ds)], \quad t > 0, \]

where \( \mathbf{1} = (1, 1, \dots, 1)' \in \mathbb{R}^N \). The agent's utility function \( U \) is defined by

\[ U(c) = \mathbb{E} \left[ \int_0^\infty e^{-\rho t} u(c_t) dt \right], \]

where \( \rho \in (0, \infty) \) and \( u : \mathbb{R}_+ \to \mathbb{R} \) is increasing and strictly concave. An equilibrium for this economy is a security-price process \( S \) such that the problem \( \sup_{c, \theta} U(c) \)
has a solution \( (c, \theta) \) with \( c_t = 1 + f(X_t) \cdot \mathbf{1} \) and \( \theta_t = \mathbf{1} \) for all \( t \in [0, \infty) \).

(A) Suppose the security-price process \( S \) is given by \( S_t = \Psi(X_t) \) for all \( t \), for some twice continuously differentiable function \( \Psi : \mathbb{R}^N \to \mathbb{R}^N \). Provide the Bellman equation for the agent's stochastic control problem. A verification argument is not required.

(B) Based on your understanding of this model, give an expression for the term structure of interest rates. That is, provide a conjecture for the market value at time \( t \) of a \( T \)-period pure discount bond, which is a zero-net-supply contract to pay one unit of the consumption numeraire at time \( t + T \). No verification argument is required here. The expression should involve only the primitives of the model,
\( r, h, v, \mu, \sigma, u, \rho \), the initial state \( x \in \mathbb{R}^N \), and future states, \( X_s, s > t \).

(C) Provide a PDE for the market value of any security as a necessary condition for an equilibrium, under stated regularity conditions, using the following infinitehorizon version of the Feynman-Kac formula. (We drop the argument \( x \in \mathbb{R}^N \)
from all functions for simplicity.) We do not supply the "strong regularity conditions"
referred to in the result; there is a range of possible assumptions that are cumbersome and mainly of mathematical interest.

A version of the Feynman-Kac Formula. Suppose \( F : \mathbb{R}^N \to \mathbb{R} \) and \( h: \mathbb{R}^N \to \mathbb{R} \) are measurable functions, and the Itô process \( X \) in \( (\nu, \sigma, h, \mathbb{R}^N) \) satisfies the "strong regularity conditions." Suppose
\( F \) satisfies a growth condition. Then \( F \) satisfies the partial differential equation if and only if \( F \) solves the partial differential equation

\[ F(x) = \mathbb{E}^x \left[ \int_0^\infty e^{-\int_0^t R(X_s) ds} h(X_t) dt \right], \quad x \in \mathbb{R}^N, \]

where \( DF = F_\nu + h \operatorname{tr}(\sigma^T F_\sigma) \).

--

# Page

(D) Solve for the term structure of interest rates in the special case of \( N = 1 \) and
\[ u(c) = \frac{c^{1-\gamma}}{1-\gamma}, \quad \gamma \in (0, 1), \]
\[ \nu(x) = \lambda x, \quad \lambda \in \mathbb{R}, \]
\[ \sigma(x) = D, \quad D \in \mathbb{R}, \]
\[ f(x) = e^{\delta x}, \quad \delta \in \mathbb{R}. \]

Also, solve for the current equilibrium short-rate process \( r \) in this economy.

(E) For this last part, a further extension of the Black-Scholes model, we do not take the parametric assumptions of part (D). Suppose the short-rate process is given by \( r_t = R(X_t) \) for all \( t \) where \( R : \mathbb{R}^N \to \mathbb{R} \), and that the security-price process is given by \( S_t = \Psi(X_t) \) for all \( t \), for some twice continuously differentiable function
\( \Psi : \mathbb{R}^N \to \mathbb{R}^N \). Give a PDE for the arbitrage-free value of an additional security defined by a dividend process \( \{h(X_t) : t \geq 0\} \), where \( h : \mathbb{R}^N \to \mathbb{R} \) is bounded and measurable. In particular, state regularity conditions implying redundancy of this additional security. Finally, give a solution to the PDE you suggest, in the form of an expectation, and provide the corresponding regularity conditions.

10.6 This exercise is to verify that the CIR model of the term structure given in Section I can be embedded in a stock-market equilibrium with decentralized production decisions. The objective is to construct an equilibrium \( [(S, r), 5, (c, \theta)] \)
of the following form:

(a) \( \theta \) is the optimal real output rate process of a firm controlling the capitalstock production process and maximizing its share price;

(b) \( r \) is a state-price deflator;

(c) \( S \) is the real stock-price process of the firm that is taken as given by the agent, and is equal to the share-price process generated as the market value of the firm's solution to the problem of maximizing its real market value, given the state-price deflator \( r \);

(d) \( (c_t, \theta_t) = (5_t, 1) \) solves the agent's optimal-consumption and trading strategy problem, given \( (S, 5) \) as the price process and real dividend-rate process of the firm. (Note that, as opposed to the pure-exchange economy studied in the body of the chapter, for which securities are held in zero net supply, the total supply of the firm's shares is 1. The market clearing condition is thus that the agent optimally holds one share in equilibrium.)

(A) Formally define a stochastic equilibrium consistent with the loose description just given. In particular, state precisely the agent's problem and the firm's problem.

(B) In the setting of Exercise 9.4, show that the (real) stock-price process \( S = K \), the capital-stock process of (41), and the dividend rate \( 5 \) given by (42) are consistent with equilibrium. Add any technical regularity conditions that you find appropriate. Hint: Be careful about real versus nominal values.

10.7 Given the Markov shock process \( X \) of (54) and an equilibrium characterized by Theorem G and its corollary, suppose that the aggregate endowment process
\( \epsilon \) is defined by \( \epsilon_t = g(X_t, t) \), where \( g \in C^{2,1}(\mathbb{R}^N \times [0, T]) \). Express a state-price deflator \( \rho \) and the short rate \( r \) in the form \( \rho_t = \rho(X_t, t) \) and \( r_t = R(X_t, t) \), for measurable functions \( \rho \) and \( R \) on \( \mathbb{R}^N \times [0, T] \). Under technical conditions, the density process \( \xi \) of an equivalent martingale measure \( Q \) for real security prices is defined by \( \xi_t = \exp(-\int_0^t r_s ds) \rho_t \). Show that \( d\xi_t = -\xi_t \theta(X_t, t) dB_t \) for some \( \mathbb{R}^N \)-valued function \( \theta \) on \( \mathbb{R}^N \times [0, T] \). Show that there is a standard Brownian motion \( B \) in
\( \mathbb{R}^N \) under \( Q \) such that \( X \) solves an SDE of the form

\[ dX_t = a(X_t, t) dt + \sigma(X_t, t) dB_t, \]

and state the function \( a \). Show that, under technical regularity conditions, the price of a security promising a real dividend-rate process of the form \( \{h(X_t, t) :
t \in [0, T]\} \) is given as the solution to a PDE of the Cauchy type examined in Appendix E. State the PDE.

# Notes

The basic framework of this chapter is standard. The seminal continuous-time equilibrium asset pricing model is due to Merton (1973a).

(C) Section C is standard in general-equilibrium theory. Existence of ArrowDebreu equilibria in infinite-dimensional settings similar to the one treated in this chapter was first shown by Bewley (1972). The first result that applies directly to the case of square-integrable functions, treated here, is due to Mas-Colell
(1986a). Developments in general-equilibrium modeling in infinite-dimensional spaces are surveyed by Mas-Colell and Zame (1992). Theorem G is from Duffie and Zame (1989). Other proofs of essentially the same result are given by Araujo and Monteiro (1989), Karatzas, Lakner, Lehoczky, and Shreve (1991), Dana and
Pontier (1990), and Dana (1993a, b), who studies the uniqueness of equilibria.
Dana and Le Van (1996) pursue duality-based equilibrium results. An extension showing existence with recursive utility is given in Duffie, Geoffard, Skiadas
(1994). (A sense in which this formulation is restrictive is given in Araujo and
Monteiro [1987] and Monteiro [1994].) Dumas, Uppal, and Wang (2000) provide a characterization of efficient allocations with recursive utility, and applications to asset pricing.

For Pareto optimality in infinite-dimensional economies, see Mas-Colell
(1986b). Colell and He (1992b) provide a notion of "local" agent weights.
--- Page 140 --

Corporate Bond (Face Value L)

Sa

一一 L Asset Level

Figure 11.1. Corporate Bond as a Derivative on the Firm’s Assets geometric Brownian motion, satisfying dA_t = μA_t dt + σA_t dB_t,

for constants μ and σ > 0, and where we have taken d = 1 as the dimension of the underlying Brownian motion B. One sometimes refers to A_t as the assets of the firm. We will suppose for simplicity that the firm produces no cash flows before a given time T. In order to justify this valuation of the firm, we could assume that there is some other security (or self-financing trading strategy) whose market value at any time t is A_t.

We take it that the original owners of the firm have chosen a capital structure consisting of pure equity and of debt in the form of a single zerocoupon bond maturing at time T, of face value L. In the event that the total value A_T of the firm at maturity is less than the contractual payment
L due on the debt, the firm defaults, giving its future cash flows, worth A_T, to debtholders. That is, debtholders receive min(L, A_T) at T, as depicted in Figure 11.1. Equityholders receive the residual max(A_T − L, 0). We suppose for simplicity that there are no other distributions (such as dividends) to debt or equity. We will shortly confirm the natural conjecture that the market value of equity is given by the Black-Scholes option-pricing formula, treating the firm’s asset value as the price of the underlying security.

Bond and equity investors have already paid the original owners of the firm for their respective securities. The absence of well-behaved arbitrage implies that at any time t < T, the total of the market values S_t of equity and Y_t of debt must be the market value A_t of the assets. (The result seems obvious; an exercise asks for proof.)

Markets are complete, in the sense of Chapter 6, given riskless borrowing or lending at a constant rate r and access to a self-financing trading strategy whose value process is A. This implies that there is at most one equivalent martingale measure.

Letting B^Q_t = B_t + πt, where π = (μ − r)/σ, we have

dA_t = rA_t dt + σA_t d B^Q_t.

By Girsanov’s Theorem, B^Q defines a standard Brownian motion under the equivalent probability measure Q defined by

dP/dQ = exp{−π B_t − (π^2/2) t}.

By Itô’s Formula, {e^{-rt} A_t : t ∈ [0, T]} is a Q-martingale. It follows that, after deflation by e^{-rt}, Q is the equivalent martingale measure. As Q is unique in this regard, we have the unique price process S of equity in the absence of well-behaved arbitrage, as explained in Chapter 6, given by

S_t = E_t^Q [e^{-r(T-t)} max(A_T − L, 0)].

Thus, the equity price S_t is computed by the Black-Scholes option-pricing formula, treating A_t as the underlying asset price, σ as the volatility coefficient, the face value L of debt as the strike price, and T − t as the time remaining to exercise. The market value of debt at time t is the residual, A_t − S_t.

When the original owners of the firm sold the debt with face value L and the equity, they realized a total initial market value of S_0 + Y_0 = A_0, which does not depend on the chosen face value L of debt. This is one aspect of the Modigliani-Miller Theorem. The same irrelevance of capital structure for the total valuation of the firm applies much more generally, and has nothing to do with geometric Brownian motion, nor with the specific nature of debt and equity. Once we consider market imperfections, however, the design of the capital structure can be important in this regard.

Fixing the current value A_t of the assets, the market value S_t of equity is increasing in the asset volatility parameter σ, due to the usual Jensen effect in the Black-Scholes formula. Thus, equity owners, were they to be given the opportunity to make a switch to a “riskier technology,” one with a larger asset volatility parameter, would increase their market valuation by doing so, at the expense of bondholders, provided the total initial market value of the firm is not reduced too much by the switch. This is a simple example of what is sometimes called “asset substitution.”

Given the time value of the option embedded in equity, bondholders would prefer to advance the maturity date of the debt; equityholders would prefer to extend it.

Equityholders (or managers acting as their agents) typically hold the power to make decisions on behalf of the firm, subject to legal and contractual restrictions such as debt covenants. This is natural in light of equity’s position as the residual claim on the firm’s cash flows. Later, in both the body of the chapter and in the exercises, we consider the opportunity that equityholders may have to issue additional debt, to call debt, or to make changes in production technologies. We will also consider certain rights of debtholders.

# B. Endogenous Default Timing

We shift now to a slightly more elaborate setting for the valuation of debt and equity, and consider the endogenous timing of default. We take as given a martingale measure Q, in the infinite-horizon sense of Section 6N, after deflation by e^{-rt}.

The resources of a given firm are assumed to consist of cash flows at the rate δ_t, for each time t. We suppose that δ is an adapted process with
∫_0^t |δ_s| ds < ∞ almost surely for all t. The market value of the assets of the firm at time t is defined as the market value A_t of the future cash flows.
That is,

A_t = E_t^Q [∫_t^∞ e^{-r(s-t)} δ_s ds]. (1)

We assume that A_t is well defined and finite for all t. The martingalerepresentation part of Girsanov’s Theorem then implies that

dA_t = (rA_t − δ_t) dt + σ_t d B^Q_t, (2)

where σ is an adapted R^d-valued process such that ∫_0^T σ_t^2 dt < ∞ for all
T ∈ (0, ∞), and where B^Q is the standard Brownian motion in R^d under Q obtained from B and Girsanov’s Theorem.

We suppose that the original owners of the firm chose its capital structure to consist of a single bond as its debt, and pure equity, defined in detail below. The bond and equity investors have already paid the original owners for these securities. Before we consider the effects of market imperfections, the total of the market values of equity and debt must be the market value A of the assets, which is a given process, so the design of the capital structure is again irrelevant from the viewpoint of maximizing the total value received by the original owners of the firm.

For simplicity, we suppose that the bond promises to pay coupons at a constant total rate c, continually in time, until default. This sort of bond is sometimes called a consol. Equityholders receive the residual cash flow in the form of dividends at the rate δ_t − c at time t, until default. At default, the firm’s future cash flows are assigned to debtholders.

The equityholders’ dividend rate, δ_t − c, may have negative outcomes.
It is commonly stipulated, however, that equity claimants have limited liability, meaning that they should not experience negative cash flows. One can arrange for limited liability by dilution of equity. That is, so long as the market value of equity remains strictly positive, newly issued equity can be sold into the market so as to continually finance the negative portion (c − δ_t)^+ of the residual cash flow. (Alternatively, the firm could issue debt, or other forms of securities, to finance itself, which we pursue in exercises.) When the price of equity reaches zero, and the financing of the firm through equity dilution is no longer possible, the firm is in any case in default, as we shall see. While dilution increases the quantity of shares outstanding, it does not alter the total market value of all shares, and so is a relatively simple modeling device. Moreover, dilution is irrelevant to individual shareholders, who would in any case be in a position to avoid negative cash flows by selling their own shares as necessary tofinance the negative portion of their dividends, with the same effect as if the firm had diluted their shares for this purpose. We are ignoring here any frictional costs of equity issuance or trading. This is another aspect of the Modigliani-Miller theory, that part of it dealing with the irrelevance of dividend policy.

Equityholders are assumed to have the contractual right to declare default at any stopping time τ, at which time equityholders give up to debtholders the rights to all future cash flows, a contractual arrangement termed strict priority, or sometimes absolute priority. We assume that equityholders are not permitted to delay liquidation after the value A of the firm reaches 0, so we ignore the possibility that A_t < 0. Only later do we consider the option of equityholders to change the firm’s production technology, or to call in the debt for some price.

The bond contract conveys to debtholders, under a protective covenant, the right to force liquidation at any stopping time τ at which the asset value A_t is as low or lower than some stipulated level, which we take for now to be the face value L of the debt. Debtholders would receive A_τ at such a time τ; equityholders would receive nothing. We later treat other covenants.

Assuming that A_0 > L, we first consider the total coupon payment rate c that would be chosen at time 0 in order that the initial market value of the bond is its face value L. Such a bond is said to be “at par,” and the corresponding coupon rate per unit of face value, c/L, is the par yield.
If bondholders rationally enforce their protective covenant, we claim that the par yield must be the riskless rate r. We also claim that, until default, the bond paying coupons at the total rate c = rL is always priced at its face value , and that equity is always priced at the residual value, A_t − L.
Finally, equityholders have no strict preference to declare default on a par-coupon bond before τ(L) = inf{t : A_t < L}, which is the first time allowed for in the protective covenant, and bondholders rationally force liquidation at τ(L).

If the total coupon rate c is strictly less than the par rate rL, then equityholders never gain by exercising the right to declare default (or, if they have it, the right to call the debt at its face value) at any stopping time τ with A_t > L, because the market value at time τ of the future cash flows to the bond is strictly less than L if liquidation occurs at a stopping time U > τ with A_U < L. Avoiding liquidation at τ would therefore leave a market value for equity that is strictly greater than A_τ − L. With c < rL, bondholders would liquidate at the first time τ(L) allowed for in their protective covenant, for by doing so they receive L at τ(L) for a bond that, if left alive, would be worth less than L. In summary, with c < rL, the bond is liquidated at τ(L), and trades at a “discount” price at any time t before liquidation, given by

P(t) = E_t[ L / e^{∫_t^{τ(L)} r ds } ] (3)

c/r + E_t[ ∫_t^{τ(L)} e^{-r(s-t)} c/r ds ] < L. (4)

C. Example: Brownian Dividend Growth

As an example, suppose the cash-flow rate process δ is a geometric Brownian motion under Q, in that

dδ_t = μ δ_t dt + θ δ_t dB_t,

for constants μ and θ, where B is a standard Brownian motion under
Q. We assume throughout that μ < r so that, from (1), A is finite and

dA_t = μ A_t dt + θ A_t dB_t.

We calculate that δ_t = (r − μ) A_t.

For any given constant K ∈ (0, A_0), the market value of a security that claims one unit of account at the hitting time τ(K) = inf{t: A_t < K} is, at any time t < τ(K),

E_t[ e^{-r(τ(K)−t)} ] = (A_t / K)^{γ}, (5)
where

γ = [ -μ + sqrt(μ^2 + 2r θ^2) ] / θ^2 , (6)
and where m = μ − θ^2/2. An exercise provides guidance on the verification of (5), a pricing formula that will prove useful in what follows.

Let us consider for simplicity the case in which bondholders have no protective covenant. Then equityholders declare default at a stopping time that solves the maximum-equity-valuation problem

V(A_0) = sup_{τ ∈ T} E_Q[ ∫_0^τ e^{-r t} (δ_t − c) dt ], (7)
where T is the set of stopping times.

We naturally conjecture that the maximization problem (7) is solved by a hitting time of the form τ(A_d) = inf{t : A_t < A_d}, for some defaulttriggering level A_d of assets, to be determined. Given this conjecture, we further conjecture from Ito’s Formula that the function w : (0, ∞) → [0, ∞) defined by (7) solves the ODE

Dw(x) − r w(x) + (r − μ)x − c = 0, x > A_d, (8)
where D w(x) = w'(x) μ x + ½ w''(x) θ^2 x^2, (9)
with the absolute-priority boundary condition w(x) = 0, x ≤ A_d. (10)
Finally, we conjecture the smooth-pasting condition w'(A_d) = 0, (11)

based on (10) and continuity of the first derivative w′(.) at A_d. Although not an obvious requirement for optimality, the smooth-pasting condition,

sometimes called the high-order-contact condition, has proven to be a fruitful method by which to conjecture solutions, as follows.

If we are correct in conjecturing that the optimal default time is of the form τ(A_d) = inf{t: A_t < A_d}, then, given an initial asset level A_0 = x > A_d, the value of equity must be

w(x) = x − L − (A_d / K)^{γ} − c/r. (12)

This conjectured value of equity is merely the market value x of the total future cash flows of the firm, less a deduction equal to the market value of the debtholders’ claim to A at the default time τ(A_d) using (5), less another deduction equal to the market value of coupon payments to bondholders before default. The market value of those coupon payments is easily computed as the present value c/r of coupons paid at the rate c from time 0 to time +∞, less the present value of coupons paid at the rate c from the default time τ(A_d) until +∞, again using (5). In order to complete our conjecture, we apply the smooth-pasting condition w’(A_d) = 0 to this functional form (12), and by calculation obtain the conjectured default-triggering asset level as

A_d = B_c, (13)
where B_c = L c / (r − μ). (14)

We are ready to state and verify the result.

Proposition. The default-timing problem (7) is solved by inf{t : A_t < B_c}. The associated initial market value w(A_0) of equity is W(A_0, c), where

W(x,c) = 0, x ≤ B_c, (15)

and

W(x,c) = x − L − (B_c / x)^{γ} − c/r, x > B_c. (16)

The initial value of debt is A_0 − W(A_0, c).

Proof: First, it may be checked by calculation that W(·,c) satisfies the differential equation (8) and the smooth-pasting condition (11). Ito’s

Formula applies to C^2 (twice continuously differentiable) functions. In our case, although W(·,c) need not be C^2, it is convex, is C^1, and is C^2 except at B_c, where W_x(B_c, c) = 0. Under these conditions, we obtain the result, as though from a standard application of Ito’s Formula, that

W(A_t,c) = W(A_0,c) + ∫_0^t D W(A_s,c) ds + ∫_0^t W_x(A_s,c) θ A_s dB_s, (17)
where

D W(x, c) = W(x, c) μ x + ½ W_{xx}(x, c) θ^2 x^2, (18)

except at x = B_c, where we may replace “W_{xx}(B_c, c)” with zero. This slight extension of Ito’s Formula is based on sources cited in the Notes.
For each time t let

q_t = W(A_t, c) + ∫_0^t e^{-r s} (r − μ) A_s − c ds.
From Ito’s Formula, dq_t = e^{-r t} f(A_t) dt + e^{-r t} W_x(A_t, c) θ A_t dB_t, (19)
where

f(x) = D W(x, c) − r W(x, c) + (r − μ) x − c.

Because W_x is bounded, the last term of (19) defines a Q-martingale, by
Proposition 5B. For x ≤ B_c, we have both W(x, c) = 0 and (r − μ) x − c ≤
0, So f(x) ≤ 0. For x > B_c, we have (8), and therefore f(x) = 0. The drift of q is therefore never positive, and for any stopping time τ we have V(A_0) ≥ E_Q(q_τ), or equivalently,

V(A_0) ≥ E_Q[ W(A_τ,c) + ∫_0^τ e^{-r t} (δ_t − c) dt ]. (20)

For the particular stopping time τ(B_c), we have

W(A_0,c) = E_Q[ ∫_0^{τ(B_c)} e^{-r t} (δ_t − c) dt ], (21)

using the boundary condition (15) and the fact that f(x) = 0 for x > B_c.
So, for any stopping time τ,

V(A_0) ≥ E_Q[ ∫_0^{τ(B_c)} e^{-r t} (δ_t − c) dt ]
≥ E_Q[ ∫_0^{τ} e^{-r t} (δ_t − c) dt ] (22)
= W(A_τ,c) + E_Q[ ∫_0^{τ} e^{-r t} (δ_t − c) dt ],

using the nonnegativity of W for the last inequality. This implies the optimal default time is τ(B_c), and the value of equity is W(A_0,c).an investment of g(1, 2) = J > 0. The optimal switch time is of the form inf{t : X_t > x}, for some trigger level x. Once having made the investment to become active, there is no reason for an all-equity firm to stop producing, unless there is a “salvage value,” that is, unless p(2, 1) < 0.
An exercise calls for a solution of this investment problem, and for the associated valuations of equity and debt. The presence of debt may generate an inefficiency, in that the timing of activation may be delayed (debt overhang) and the timing of abandonment for the salvage value may (“
“asset substitution”) be inefficient, generating a lower total value than that of an all-equity firm, absent tax shields. The Notes cite sources with many variants of this real-option problem.

# G. Other Market Imperfections

A “perfect” debt covenant forces equity owners to follow the investment and financing strategy that maximizes the total market value of the firm, including the initial sale value of debt. Such a covenant, while theoretically maximizing the initial owners’ total market value, may in practice be prohibitively costly to formulate, monitor, and enforce. This section offers

an informal discussion of the monitoring and renegotiation of debt, and a brief list of potential extensions of our modeling approach.

An inability of bondholders to perfectly monitor the firm implies that, with some probability, equityholders, unless otherwise prohibited, may have a valuable option to violate the covenant, for example to continue to operate the firm after the asset value drops below protective levels set in the covenant. If monitoring by bondholders can be improved at some cost, then bondholders might restore some of the value that would have been “expropriated” by equityholders. The total of the market values of debt and equity is lowered, however, by the market value of future monitoring costs. It may be fruitful for the initial owner of the firm, before issuance of debt, to put in place a low-cost monitoring system, so as to raise the total initial market value of the firm. After the debt has been issued, however, it may in some cases be to the advantage of equityholders to take actions that increase the cost of monitoring.

Another common market imperfection is an inability to enforce strict priority. While equityholders may be contractually entitled to nothing in the event of their failure to meet the bond covenants or to make timely payments on the debt contracts, they may attempt to renegotiate this absolute priority. For example, equityholders may be in a position to influence the level of financial distress costs, or to delay giving up the firm to debtholders. In order to entice equityholders to make efforts to arrange for low financial distress costs, bondholders may negotiate to convey some portion of the remaining value of the firm to equityholders. If any action by equityholders can only reduce financial distress costs, then, under reasonable conditions, this ability to negotiate a deviation from absolute priority presumably raises the pre-default market values of both debt and equity above the values that would prevail if strict priority were always enforced. If, however, equityholders can, by actions that they are entitled to make, increase financial distress costs (that is, “destroy” value), then the opportunity to renegotiate can raise the market value of equity at the expense of bondholders, relative to the values that would apply with strict priority.

One may extend the models that we have seen so as to treat bonds of finite maturity, or with discrete coupons. One can also allow for multiple classes of debtholders, each with its own contractual cash flows and rights, by generalizing the definition of an equilibrium in a relatively straightforward way. For example, bonds are conventionally classified by priority, so that, at liquidation, senior bondholders are contractually entitled to cash flows resulting from liquidation up to the total face value of senior

debt (in proportion to the face values of the respective senior bonds, and normally without regard to maturity dates). If the most senior class of debtholders can be paid off in full, the next most senior class is assigned liquidation cash flows, and so on, to the lowest subordination class. Some bonds may be secured by certain identified assets, or collateralized, in effect giving them seniority over the liquidation value resulting from those cash flows, before any unsecured bonds may be paid according to the seniority of unsecured claims. In practice, the overall priority structure may be rather complicated. Some implications of seniority and of relative maturity for bond valuation are explored in exercises.

Corporate bonds are often callable, within certain time restrictions.
Not infrequently, corporate bonds may be converted to equity at prearranged conversion ratios (number of shares for a given face value) at the timing option of bondholders. Such convertible bonds present a challenging set of valuation issues, some reviewed in sources cited in the Notes.
Occasionally, corporate bonds are puttable, that is, may be sold back to the issuer at a prearranged price at the option of bondholders.

One can also allow for adjustments in capital structure, normally instigated by equityholders, that result in the issuing and retiring of securities, subject to legal restrictions, some of which may be embedded in debt contracts.

# H. Intensity-Based Modeling of Default

This section introduces a model for a default time as a stopping time τ with a given intensity process λ, as defined below. From the joint behavior of λ, the short-rate process r, the promised payment of the security, and the model of recovery at default, as well as risk premia, one can characterize the stochastic behavior of the term structure of yields on defaultable bonds.

In applications, default intensities are allowed to depend on observable variables that are linked with the likelihood of default, such as debt-to-equity ratios, asset volatility measures, other accounting measures of indebtedness, market equity prices, bond yield spreads, industry performance measures, and macroeconomic variables related to the business cycle. This dependence could, but in practice does not usually, arise endogenously from a model of the ability or incentives of the firm to make payments on its debt. Because the approach presented here does not depend on the specific setting of a firm, it has also been applied to the valuation of defaultable sovereign debt, as indicated in the Notes.

We fix a complete probability space (Ω, F, P) and a filtration {G_t :
t ≥ 0} satisfying the usual conditions, which are listed in Appendix I.
This will be our first extensive use, for reasons that will become clear, of continuous-time filtrations that are not purely Brownian. As we depart from the case of purely Brownian information, it is important to make a distinction between an adapted process and a predictable process. As defined in Appendix I, a predictable process is, intuitively speaking, one whose value at any time s depends only on the information in the underlying filtration that is available up to, but not including, time s.

As defined in Appendix I, a nonexplosive counting process K (for example, a Poisson process) has an intensity λ if λ is a predictable nonnegative process satisfying ∫_0^t λ_s ds < ∞ almost surely for all t, with the property that a local martingale M, the compensated counting process, is given by

M_t = K_t - ∫_0^t λ_s ds. (26)

The compensated counting process M is a martingale if, for all t, we have E[∫_0^t λ_s ds] < ∞, as elaborated in Appendix I.

We will say that a stopping time τ has an intensity λ if τ is the first jump time of a nonexplosive counting process whose intensity process is λ. Theaccompanying intuition is that, at any time t and state ω with t < τ(ω), the 𝒢 -conditional probability that τ < t + Δ is approximately Λ(t)Δ, for small Δ. This intuition is justified in the sense of derivatives if Λ is bounded and continuous, and under weaker conditions.

A stopping time τ is nontrivial if P(τ ∈ (0, ∞)) > 0. If a stopping time τ is nontrivial and if the filtration {𝒢_t : t ≥ 0} is the standard filtration of some Brownian motion B in R^d, then τ could not have an intensity. We know this from the fact that, if {𝒢_t : t ≥ 0} is the standard filtration of B, then the associated compensated counting process M of (26) (indeed, any local martingale) could be represented as a stochastic integral with respect to B, and therefore cannot jump, but M must jump at τ. In order to have an intensity, a stopping time must be totally inaccessible, a property whose definition, cited in the Notes, suggests arrival as a “sudden surprise,” but there are no such surprises on a Brownian filtration!

As an illustration, we could imagine that the firm’s equityholders or managers are equipped with some Brownian filtration for purposes of determining their optimal default time τ, as in Section C, but that bondholders have imperfect monitoring, and may view τ as having an intensity with respect to the bondholders’ own filtration {𝒢_t : t ≥ 0}, which contains less information than the Brownian filtration. Such a situation arises in a model cited in the Notes.

We say that τ is doubly stochastic with intensity Λ if the underlying counting process whose first jump time is τ is doubly stochastic with intensity
Λ, as defined in Appendix I. The doubly stochastic property implies that
P(τ > s | 𝒢) = E_t [exp(− ∫_t^s Λ_u du)], t < min(τ, s), (27)
where E_t denotes 𝒢-conditional expectation. This property (27) is convenient for calculations, as evaluating the expectation in (27) is computationally equivalent to the pricing of a default-free zero-coupon bond, treating Λ as a short rate and “E” as risk-neutral. Indeed, this analogy is also quite helpful for intuition.

It would be sufficient for (27) that Λ_t = Λ(X_t, t) for some measurable
Λ: R^d × [0, ∞) → [0, ∞), where X in R^d solves a stochastic differential equation of the form dX_t = μ(X_t, t) dt + σ(X_t, t) dB_t, (28)
for some (𝒢_t)-standard Brownian motion B in R^d.

More generally, (27) follows from assuming that the doubly stochastic counting process K whose first jump time is τ is driven by some filtration
{ℱ_t : t ≥ 0}, a concept defined in Appendix I. (Included in the definition is the condition that ℱ_t ⊂ 𝒢_t, and that {ℱ_t : t ≥ 0} satisfies the usual conditions.) The idea of the doubly stochastic assumption is that the intensity
Λ is (ℱ_t)-predictable and that, conditional on Λ, K is a Poisson process with (conditionally deterministic) time-varying intensity {Λ_t : t ≥ 0}. In particular, for any time s > t conditional on the tribe 𝒢_t ∨ ℱ_t generated by the events in 𝒢_t ∪ ℱ_t, the number K_s − K_t of arrivals between t and s is distributed as a Poisson random variable with parameter ∫_t^s Λ_u du. (A random variable q has the Poisson distribution with parameter β if P(q = k) = e^{−β} β^k / k! for any nonnegative integer k.) Thus, letting A be the event that
K_s − K_t = 0, the law of iterated expectations implies that, for t < τ, P(τ > s | 𝒢_t) = E(1_A | 𝒢_t)
= E[E(1_A | 𝒢_t ∨ ℱ_t) | 𝒢_t]   (29)
= E[P(K_s − K_t = 0 | 𝒢_t ∨ ℱ_t) | 𝒢_t]
= E[ exp(− ∫_t^s Λ_u du) | 𝒢_t], consistent with (27). This is only a sketch of the idea; sources cited in the
Notes offer a proper development of the theory. Appendix I connects the intensity to the probability density and hazard rate of the underlying stopping time.

As we proceed, we will repeatedly use the following natural result. We have not defined here a stochastic integral with respect to a martingale in the case of our general filtration, but that is done in sources cited in the Notes.
Lemma. Suppose M is a martingale and H is a bounded predictable process. Then the stochastic integral ∫ H dM is well defined and is a martingale.

I. Risk-Neutral Intensity Process

For purposes of the market valuation of bonds and other securities whose cash flows are sensitive to default timing, we would want to have an equivalent martingale measure Q and a risk-neutral intensity process, that is, an intensity process Λ^Q for the default time τ that is associated with (Q, ℱ, Q)
and the given filtration {𝒢_t : t ≥ 0}. In this case, we call Λ^Q the Q-intensity of τ. (As usual, there may be more than one equivalent martingale measure.) As we shall see later in this section, the ratio Λ^Q / Λ (for Λ strictly positive) is in some sense a multiplicative risk premium for the uncertainty associated with the timing of default. The Notes cite the following convenient result.
Proposition. Suppose a nonexplosive counting process K has a P-intensity process
Λ and Q is any probability measure equivalent to P. Then K has a Q-intensity process.

A version of Girsanov’s Theorem provides conditions suitable for calculating the change of probability measure associated with a change of intensity, by analogy with the “change in drift” of a Brownian motion.
Suppose K is a nonexplosive counting process with intensity Λ, and that ψ is a strictly positive predictable process such that, for some fixed time horizon T, ∫_0^T ψ_s Λ_s ds is finite almost surely. A local martingale is then well defined by ε_t = exp( ∫_0^t (1 − ψ_s) dM_s − ∫_0^t (1 − ψ_s) Λ_s ds ), t ≤ T.
Girsanov’s Theorem. Suppose the local martingale ε is in fact a martingale. Then an equivalent probability measure Q is defined by dQ = ε(T) dP. Restricted to the time interval [0, T], the counting process K has Q-intensity ψΛ.

Care must be taken with assumptions, for the convenient doubly stochastic property need not be preserved with a change to an equivalent probability measure. Illustrative counterexamples are cited in the Notes.
A proof of Girsanov’s Theorem is cited in Appendix I, which also gives sufficient conditions for the martingale property of ε, and for K to be doubly stochastic under both P and Q.

Under certain conditions on the filtration {𝒢_t : t ≥ 0} that are outlined in Appendix I, the martingale representation property applies, and for any equivalent probability measure Q, one can obtain the associated
Q-intensity of K from the martingale representation of the associated density process.

# J. Zero-Recovery Bond Pricing

We fix a short-rate process r and an equivalent martingale measure Q after deflation by exp(− ∫_0^t r_s ds). We consider the valuation of a security that pays F at a given time s > 0, where F is a 𝒢_s-measurable bounded random variable. As 1_{τ>s} is the random variable that is 1 in the event of no default by s and zero otherwise, we may view F as the contractually promised payment of the security at time s, with default by s leading to no payment. The case of a defaultable zero-coupon bond is treated by letting
F = 1. In the next section, we will consider recovery at default.

From the definition of Q as an equivalent martingale measure, the price S_t of this security at any time t < s is given by
S_t = E_Q [ exp(− ∫_t^s r_u du) F 1_{τ > s} | 𝒢_t ] (30)
where E_Q denotes 𝒢_t-conditional expectation under Q. From (30) and the fact that τ is a stopping time, S_t must be zero for all t > τ.

Under Q, the default time τ is assumed to have an intensity process Λ^Q.
Theorem. Suppose that F, r, and Λ^Q are bounded and that τ is doubly stochastic under Q driven by a filtration {ℱ_t : t ≥ 0} such that r is (ℱ_t)-adapted and F is
ℱ_s-measurable. Fix any t < s. Then, for t > τ, we have S_t = 0, and for t < τ,
S_t = E_Q [ exp(− ∫_t^s (r_u + Λ^Q_u) du) F | 𝒢_t ] (31)
The idea of this representation (31) of the pre-default price is that discounting for default that occurs at an intensity is analogous to discounting at the short rate r.Proof: From (30), the law of iterated expectations, and the assumption that τ is (F_t)-adapted and F is F_s-measurable,

S_t = E_Q [e^{-∫_t^τ r_u du} F 1_{τ > s} | F_t] = E_Q [e^{-∫_t^τ r_u du} F | F_t, τ > s] P(τ > s | F_t).

The result then follows from the implication of double stochasticity that Q(τ > s | F_t) = exp(-∫_t^s A_u du). □

As a special case, suppose the filtration {F_t : t ≥ 0} is generated by B_Q, a (F_t)-standard Brownian motion in R^d under Q. Consider a “state” process X valued in some subset D of R^d and solving a stochastic differential equation of the form

dX_t = μ(X_t) dt + σ(X_t) dB_Q. (32)

It is natural to allow dependence of A_t, r_t, and F on the state process X in the sense that

A_t = λ(X_t), r_t = r(X_t), F = f(X_s), (33)

where λ, r, and f are real-valued measurable functions on D.

Relation (31) then states that for t < τ, we have S_t = g(X_t, t), for a function g : D × [0, s] → R that, under the Feynman-Kac technical conditions (Appendix E), solves the PDE

g_t(x, t) + [μ(x) + λ(x)] ∇g(x, t) = 0, (34)

for (x,t) ∈ D × [0,s), with the boundary condition

g(x, T) = f(x), (35)

where

g_t(x, t) = ∂g/∂t + r(x)g(x, t) + λ(x) f(x) + ½ tr[σ(x)σ(x)′ ∇²g(x, t)].

For computationally tractable examples, suppose that the functions r, λ, p, and log f(·) are affine. (For a zero-coupon defaultable bond, we take f(x) = 1.) In this “affine” setting, as shown in Chapter 7, we can readily compute a solution to (34)-(35) of the form g(x, t) = e^{a(t) + B(t)'x}, for deterministic coefficients a(t) and B(t) that are explicitly known or easily computed in practice.

# K. Pricing with Recovery at Default

The next step is to consider the recovery of some random payoff W at the default time τ, if default occurs before the maturity date s of the security.
We adopt the assumptions of Theorem J, and add the assumption that
W = w_τ, where w is a bounded predictable process that is also adapted to the filtration {F_t : t ≥ 0} that appears in the theorem statement.

The market value at any time t < min(s, τ) of any default recovery is, by definition of the equivalent martingale measure Q, given by

P(t, u) = E_Q [e^{-∫_t^u (r_v + A_v) dv} w_u 1_{τ > t} | F_t] (36)

The doubly stochastic assumption implies that τ has a probability density under Q, at any time u in [t, s], conditional on τ > t and on the event that τ > t, of

q(t, u) = exp(-∫_t^u A_v dv).

Thus, using the same iterated-expectations argument of the proof of Theorem J, we have, on the event that τ > t, S_t = E_Q [e^{-∫_t^τ r_v dv} W 1_{τ ≤ s} | F_t]
= E_Q [E_Q [e^{-∫_t^τ r_v dv} w_τ 1_{τ ≤ s} | F_t, τ] | F_t]
= E_Q [∫_t^s e^{-∫_t^u r_v dv} w_u q(t, u) du | F_t]
= ∫_t^s E_Q [e^{-∫_t^u r_v dv} w_u | F_t] q(t, u) du,

using Fubini’s Theorem, where

P(t, u) = E_Q [e^{-∫_t^u (r_v + A_v) dv} w_u | F_t]. (37)
t
We summarize the main defaultable valuation result as follows.

Theorem. Consider a security that pays F at s if τ > s, and otherwise pays w_τ at τ. Suppose that w, F, λ, and τ are bounded. Suppose that τ is doubly stochastic under Q driven by a filtration {F_t : t ≥ 0} with the property that r and w are
(F_t)-adapted and F is F_s-measurable. Then, for t > τ, we have S_t = 0, and for t<τ,

S_t = E_Q [e^{-∫_t^τ (r_v + A_v) dv} F | F_t] + ∫_t^s P(t, u) du. (38)

In the affine state-space setting described at the end of the previous section, P(t, u) can be computed by our usual “affine” methods, provided that w is of form w_t = e^{α(t) + β(t)'X_t} for deterministic α(t) and β(t). In this case, it is an exercise to show that, under technical regularity,

P(t, u) = e^{α(t) + β(t)'X_t} [C(t, u) + C(t, u)' X_t + D(t, u)], (39)

for readily computed deterministic coefficients α, β, C, and D. This still leaves the task of numerical computation of the integral ∫_t^s P(t, u) du.

For the price of a typical defaultable bond promising periodic coupons followed by its principal at maturity, one may sum the prices of the coupons and of the principal, treating each of these payments as though it were a separate zero-coupon bond. An often-used assumption, although one that need not apply in practice, is that there is no default recovery for coupons, and that bonds of different maturities have the same recovery of principal. In any case, convenient parametric assumptions, based for example on an affine driving process X, lead to straightforward computation of a term structure of defaultable bond yields that may be applied in practical situations, such as the valuation of credit derivatives, a class of derivative securities designed to transfer credit risk that is treated in sources cited in the Notes.

For the case of defaultable bonds with embedded American options, the most typical cases being callable or convertible bonds, the usual resort is valuation by some numerical implementation of the associated dynamic programming problems.

# L. Default-Adjusted Short Rate

In the setting of Theorem K, a particularly simple pricing representation can be based on the definition of a predictable process L for the fractional loss in market value at default, defined by

(1 — L_τ)(S_{τ-}) = w_τ. (40)

Manipulation that is left as an exercise shows that, under the conditions of Theorem K, for t < min(τ, s),

S_t = E_Q [e^{-∫_t^{τ ∧ s} (r_v + λ_v L_v) dv} F | F_t]. (41)

This valuation model (41) is particularly convenient if we take L as an exogenously given fractional loss process, as it allows for the application

of standard valuation methods, treating the payoff F as default-free, but accounting for the intensity and severity of default losses through the
“default-adjusted” short-rate process r + λL. The adjustment λL is in fact the risk-neutral mean rate of proportional loss in market value due to default.

Notably, the dependence of the bond price on the intensity λ and fractional loss L at default is only through the product λL. Thus, for any bounded strictly positive predictable process θ, the bond price is invariant to a substitution for L and λ of θL and λ/θ, respectively. For example, doubling λ and halving L has no effect on the bond-price process before default.

Suppose, for example, that τ is doubly stochastic driven by X, and we take r + λL = R(X_t) and F = f(X_s), for a state process X satisfying
(32). Then, under Feynman-Kac regularity conditions, we obtain at each time t before default the bond price S_t = g(X_t, t), for a solution g of the PDE

Dg (x, t) — R(x)g(x, t) = 0, (x,t) ∈ D × [0, s), (42)

with boundary condition g(x, s) = f(x). Sources cited in the Notes, as well as exercises, provide examples. As a special case, if the driving process X is affine, if f(x) = e^{c'x} for some c ∈ R^d, and if R(x) = a + d'x for some a ∈R and d in R^d, then we have g(x, t) = e^{a(t) + B(t)'x} for deterministic and readily computed coefficients a(t) and B(t).

There are also interesting cases, some cited in the Notes, in which λ or L (or both) are naturally dependent on the pre-default bond price itself. In a Markovian setting, the PDE (42) would be generalized to one of the nonlinear form

Dg(x, t) — R(x, g(x, t))g(x, t) = 0. (43)

# Exercises

11.1 In the setting of Section A, suppose “equity” and “debt” are defined by an arbitrary sharing rule, subject only to the feasibility condition S_t + D_t = A_t.
Suppose there is a stopping time τ such that P(τ < T) > 0 and A_τ ≠ D_τ + E_τ.
Show that there is an arbitrage whose market value is bounded below.

11.2 Show that (2) is implied by (1).

11.3 In the setting of Section B, an asset-valuation process A is fixed, and we consider the contractual right of debtholders to force liquidation at any stopping

time τ at which A_τ < K, where K < L is a constant. We assume for simplicity that
A_t ≥ L. We also suppose that equityholders have the right to call the debt at par, meaning that, at a stopping time selected by equityholders, the obligation to pay coupons can be extinguished in return for a payment of L to bondholders.

(A) Show that the bond is always liquidated by τ(K), assuming that equityholders and bondholders optimally time their covenant exercise, default, and call decisions and that each knows the other’s policy.(C) Now, fixing the initial level x of assets, suppose that Zinc’s equity owners can substitute the current technology with an alternative technology that has the same mean-growth parameter m, but has a higher volatility parameter σ > . The same
Brownian motion B drives asset growth. Would Zinc’s equity owners choose to do so in all cases? Please bear in mind that, while the all-equity firm Zinc remains as described above, there may not be another firm that uses the riskier technology characterized by (m, σ). Please justify your answer theoretically. Please be precise, by giving a proof or counterexample.

11.7 (Floating-Rate Notes). Fix a probability space and a filtration. Consider an arbitrage-free market in which, for each t and s > t, there is available for purchase or sale a unit zero-coupon default-free bond maturing at s with a bounded price at t of A_{t,s}, with outcomes in (0, 1). A floating-rate note, with a given maturity T, a face value of 1, and a spread K_F, is defined as a claim to payment of the face value 1 at the maturity date T, and payment at each integer date i ∈ {1,..., T} of

the spread K_F plus the one-period default-free floating rate L_{i-1}, established at the previous integer date. The one-period default-free floating rate L_{i-1}, established at date i−1 is A_{i-1,i} − 1, the simple interest rate on one-period default-free loans.
(In practice, the calendar length of the interpayment time interval associated with a given note may vary from case to case. You may assume for concreteness that one unit of time is one calendar year, and that bounded positions in zero-coupon bonds and floating-rate notes are permitted. All prices and trading strategies are adapted.)

(A) A par floating-rate note is a floating-rate note whose market value at the issue date is equal to its face value. Prove, without the benefit of assuming the existence of a state-price deflator, short-rate process, or equivalent martingale measure, that for any integer maturity T, the unique arbitrage-free default-free par floating-rate spread K_F is zero. (You may assume that the issue date is 0.)

(B) Now, suppose there is a complete probability space (Ω, F, P), and a filtration {F_t} satisfying the usual conditions. There is an adapted nonnegative short-rate process r_t, and an equivalent martingale measure Q after deflation by exp(−∫_0^t r_u du). A corporation, Zank, defaults at a stopping time τ that, under Q, is doubly stochastic with an intensity process λ^Q_t.

For simplicity, we suppose that any floating-rate note issued by Zank has no cash flows at or after default. This is sometimes called a “zero-recovery” assumption. One can price a defaultable floating-rate note of maturity T at any given spread K_F by pricing each of the promised payments at times 1 through T, and then adding up the prices. For an “explicit” model, we now suppose that there is an R^n-valued process X that is “affine” under Q, in the sense that, for any c = (α, β, a, b) ∈ R × R × R^n × R^n,

and for any times t and s > t, there exist a scalar a(t, s, c) and some b(t, s, c) in R^n such that

E_Q[exp(∫_t^s (a + b·X_u) du) | X_t] = exp(a(t, s, c) + b(t, s, c)·X_t).

These coefficients a(t, s, c) and b(t, s, c) are typically computable in applications from certain ordinary differential equations, and in certain cases are explicit. You may take these coefficients as given in terms of any (t, s, c).

Assume that r_t = α + β·X(t) and that λ^Q_t = α_Q + δ_Q·X(t), for given scalars α and α_Q, and given β and δ_Q in R^n. Assuming the pricing rule (31) applies, price the coupon payment L_{i-1} + K_F promised at date i. Finally, give a formula for the par spread K_F.

11.8 (Valuation of Options with Bankruptcy). We fix a complete probability space (Ω, F, P) and a filtration {G_t : t ≥ 0} satisfying the usual conditions. Suppose, in a given economy, that there is a constant short rate r. Consider a firm whose equity price process is a geometric Brownian motion X, until bankruptcy.

We assume that there is an equivalent martingale measure Q (after deflation by exp(−r t)) such that, for given real parameters m and σ, we have

X_t = X_0 exp(m t + σ B_t^Q),

where B^Q is a standard Brownian motion under Q. Bankruptcy occurs with constant Q-intensity λ. Specifically, bankruptcy occurs at the stopping time τ = inf {t :
N_t = 1}, where, under Q, N is a Poisson process, independent of B^Q, with constant intensity λ. When bankruptcy occurs, the price of the equity jumps to zero.

(A) Compute the price of a European call option on the equity for expiration at time T and for strike price x > 0. Hint: The point of the exercise is that the firm may go bankrupt before expiration. The option pays off if the firm does not go bankrupt, and if the price of the equity is above the strike.

(B) Compute the price of a European put option on the equity for expiration at time T and for strike price x > 0, without using put-call parity. Now show that put-call parity holds.

11.9 Fixing a probability space and a filtration satisfying the usual conditions, consider a market in which there exists a short-rate process r and an equivalent martingale measure Q after deflation by exp(∫_0^t r_s ds), with dr_t = a(t) dt + b(t)·dB_t^Q, for continuous functions a and b of time alone, where B^Q is a standard
Brownian motion in R^d under Q, and b is therefore valued in R^d.

(A) For a given maturity T, show that the price process U of a zero-coupon bond maturing at T, satisfies dU_t = r_t U_t dt + U(t) v(t)·dB_t^Q, t < T, and provide a formula for v(t) in terms of a and b. Hint: Use the fact that ∫_t^T r_s ds is normally distributed under Q. Alternatively, use the fact that this is an affine term-structure model.

(B) Consider a firm whose total market-value process A satisfies dA_t = r_t A_t dt +
A_t σ_A·dB_t^Q, A_0 > 0, where σ_A ∈ R^d. There are no dividends, and the drift, r_t A_t, is therefore dictated by the definition of an equivalent martingale measure. The firm has issued L bonds maturing at T, each promising to pay 1 unit of account at maturity unless the value A_T of the firm is not large enough to cover the debt, in which case the bonds share the value of the firm on a pro rata basis, meaning a default payment of A_T/L to each bondholder. Letting Z denote the price of a bond at time zero, compute explicitly the default risk premium U_0 − Z_0, showing it to be of the form of a Black-Scholes put option price with explicitly stated coefficients. Hint: Take U as a deflator.

11.10 Suppose that τ is a stopping time with intensity λ, in the sense of Section
H, and let N_t = 1_{τ ≤ t}. Show that N is a nonexplosive counting process with intensity {λ_t 1_{t < τ} : t > 0}. Hint: Use the local martingale characterization of intensity.

11.11 Under the conditions of Theorem K and the assumption that w_t = (1 − ζ_t)(S_{t-}), obtain the representation (41) of defaultable bond prices based on the

default-adjusted short rate. The following exercise asks for a bit more, taking ζ as a primitive rather than w.

11.12 Suppose that ζ is a given predictable process valued in [0, 1], to be treated as a fractional loss in market value at default. Suppose, in the setting of Section I, that the promised payoff F, the short-rate process r, and the intensity λ of the default time τ are bounded, and let

P = E[exp(−∫_t^s (r_u + ζ_u λ_u) du), t < s]. (44)

Suppose that F does not jump at τ, almost surely. (Conditions for this are analogous to those of Theorem I.) Show that there is a unique bounded adapted process S with the property that S is the price process for a security that pays
(1 − ζ_τ) S_{τ-} at τ if τ < s and pays F at s if τ > s. Show, moreover, that for t < τ, we have S_t = F, and that for t > τ, we have S_t = 0.

11.13 Certain credit derivatives are based on the first to default, meaning that they are based on the first min(τ_1, ..., τ_n) of n default (stopping) times τ_1, ..., τ_n.
In the setting of Section H, suppose that, for each i, the stopping time τ_i hasintensity A and that there is no simultaneous default, meaning that for any i and j ≠ i, we have P(τᵢ = τⱼ) = 0. Show that min(τ₁, ... , τₙ) has intensity A₁ + ... + Aₙ.

11.14 On a given complete probability space (Ω, ℱ, P), let N be a Poisson process with constant intensity γ. Let W be a random variable, independent of N, with outcomes 1 and 0, with respective probabilities p and 1 − p. Let K = NW, and let ℱₜ be the completion of the tribe generated by {(Kₛ, Nₛ): 0 < s < t}. Let τ be the first jump time of K. Show that K is a nonexplosive counting process, and calculate its intensity process λ. Calculate, for an arbitrary given time s, the survival probability P(τ > s), and show that the convenient formula (27) does not apply. In particular, K is not doubly stochastic.

11.15 Derive the formula (39), under an affine model for X under Q, and affine dependence of λ and r on X. You may assume that (37) applies, and adopt integrability conditions as needed.

# Notes

(A) This model of debt and equity pricing is based on Black and Scholes (1973)
and Merton (1970, 1973b, 1974). Pitts and Selby (1983) further characterize the implied shape of the term structure of credit spreads. Modigliani and
Miller (1958) is the classic treatment of irrelevance of capital structure in perfect capital markets. Geske (1977) uses compound option modeling so as to extend to debt at various maturities.

(B-E) These sections are based on the model proposed by Fisher, Heinkel, and Zechner (1989), and explicitly solved by Leland (1994) for optimal default timing and for the valuation of equity and debt with taxes and bankruptcy distress costs. The model was further elaborated to treat coupon debt of finite maturity in Leland and Toft (1996), endogenous calling of debt and recapitalization in
Leland (1998) and Uhrig-Homburg (1998), incomplete observation by bond investors, with default intensity, in Duffie and Lando (1998), and alternative approaches to default recovery in Anderson and Sundaresan (1996), Anderson,
Pan, and Sundaresan (1995), Fan and Sundaresan (1997), Mella-Barral (1999), and Mella-Barral and Perraudin (1997).

The optimality verification proof of Section C is adapted from Duffie and
Lando (1998). For this proof, we use a version of Itô’s Formula that can be applied to a real-valued function that is C¹ and is C² except at a point, as, for example, in Karatzas and Shreve (1988), page 219.

Cvitanić and Karatzas (1996b) and Kifer (2000) treat stopping games that might be adapted to some of the games considered in this chapter.

Black and Cox (1976) developed the idea of first-passage-based default timing, but used an exogenous default boundary. Longstaff and Schwartz (1995a)
developed a similar first-passage defaultable bond pricing model with stochastic default-free interest rates. (See also Nielsen, Sad-Requejo, and Santa-Clara (1993)
and Collin-Dufresne and Goldstein (1999).) Zhou (2000) bases pricing on first passage of a jump-diffusion.

(F) Examples based on the switching approach here have been developed and solved repeatedly in the literature. A standard model that fits literally into the setting of this section is that of Dixit (1989). Further sources to the literature are cited by Dixit and Pindyck (1994), who summarize a significant amount of modeling in this topic area, which is sometimes called real options. Boyarchenko and Levendorskii (2000a,b) and Marcozzi (2000) offer some related results on perpetual options.

(G) On renegotiation and pricing, see Anderson and Sundaresan (1996),
Anderson, Pan, and Sundaresan (1995), Décamps and Faure-Grimaud (1998,
1999), Fan and Sundaresan (1997), Mella-Barral (1999), and Mella-Barral and Perraudin (1997).

Huang, Subrahmanyam, and Sundaram (1999) address the valuation of corporate debt with costly refinancing.

Acharya and Carpenter (1999) treat callable defaultable bonds. On convertible bond valuation, see Brennan and Schwartz (1980a), Davis and Lischka (1999),
Loshak (1996), Nyborg (1996), and Tsiveriotis and Fernandes (1998). On the timing of call and conversion options on convertible bonds, see Ederington, Caton, and Campbell (1997).

On credit derivatives, see Chen and Sopranzetti (1999), Cooper and
Martin (1996), Davis and Mavroidis (1997), Duffie (1998b), Longstaff and Schwartz (1995b), and Pierides (1997).

(H-I) A standard reference on counting processes is Brémaud (1981). Additional sources include Daley and Vere-Jones (1988) and Karr (1991). Meyer (1966)
defines totally inaccessible stopping times. Appendix I contains a summary of some of the key results on counting processes that we use here. Lemma H

and the definition of a stochastic integral with respect to a martingale can be found in Protter (1990), among other sources. Proposition I is from Artzner and
Delbaen (1995). Theorem I is simplified from Brémaud (1981), as summarized in Appendix I. Duffie and Lando (1998) show how default intensity can arise in the model of Section C with incomplete information. Elliott, Jeanblanc, and
Yor (1999) give a new proof of this intensity result, which is generalized by
Song (1998) to the multidimensional case. Kusuoka (1999b) provides an example of this intensity result that is based on unobservable drift of assets.

Kusuoka (1999b) also gives examples in which the doubly stochastic property is not preserved under a change of measure.

(J) The use of intensity-based defaultable bond pricing models was instigated by Artzner and Delbaen (1990a, 1992, 1995), Lando (1994, 1998), and Jarrow and Turnbull (1995). Theorem J is based on results from Duffie, Schroder, and
Skiadas (1996) and Lando (1998). Additional work in this vein is by Bielecki and Rutkowski (1999a,b, 2000), Cooper and Mello (1991, 1992), Das and
Sundaram (2000), Das and Tufano (1995), Davydov, Linetsky, and Lotz (1999),
Duffie (1998a), Duffie and Huang (1996), Duffie and Singleton (1999), Elliott,
Jeanblanc, and Yor (1999), Hull and White (1992, 1995), Jarrow and Yu (1999),
Jarrow, Lando, and Yu (1999), Jeanblanc and Rutkowski (1999), Madan and Unal (1998), and Nielsen and Ronn (1995).

Intensity-based debt pricing models based on stochastic transition among credit ratings were developed by Arvantis, Gregory, and Laurent (1999), Jarrow,
Lando, and Turnbull (1997), Kijima and Komoribayashi (1998), Kijima (1998), and Lando (1998).

(K) These results are based on Duffie, Schroder, and Skiadas (1996) and
Lando (1994, 1998). Schönbucher (1998) extends to treat the case of recovery W which is not of the form w, for some predictable process w, but rather allows the recovery to be revealed just at the default time τ.

(L) Debt pricing models based on a default-adjusted short-rate process were developed by Duffie and Singleton (1999), based on precursors due to Pye (1974)
and Litterman and Iben (1991). For empirical work on default-adjusted short rates, see Duffee (1999a) for an application to corporate bonds, and Duffee,
Pedersen, and Singleton (2000) and Pagés (2000) for work on sovereign debt.
For more on sovereign debt valuation, see Gibson and Sundaresan (1999) and Merrick (1999).

Applications of price-dependent default-adjusted short rates determined by the nonlinear PDE (43) include the case of defaultable swaps, as addressed by Duffie and Huang (1996). For more on the valuation of defaultable swaps, see Abken (1993), Artzner and Delbaen (1990a), Cooper and Mello (1991),
Jarrow and Turnbull (1997b), Li (1995), Huge and Lando (1999), and Sorenson and Bollier (1995). For institutional background on defaultable swaps, see
Litzenberger (1992). On the impact of credit risk on derivative pricing, see Martin (1997).

Additional Topics: The exercise on corporate bond pricing under Gaussian interest rates is based on Décamps and Rochet (1997) and Shimko, Tejima, and
Van Deventer (1993). On the impact of illiquidity on defaultable debt prices,see Ericsson and Renault (1999). Models of default correlation and collateralized debt obligations include those of Davis and Lo (1999, 2000), Duffie and Garleanu (1999), and Finger (2000).

Bensoussan, Crouhy, and Galai (1995a,b) analyze compound options and complex options, examples of which include options on an equity, which in turn can be viewed as an option on the underlying assets of the firm. Galai and Schneller (1978) and Schwartz (1997) treat warrant valuation.

Numerical Methods

This chapter reviews three numerical approaches to pricing securities in a continuous-time setting: “binomial” approximation, Monte Carlo simulation, and finite-difference solution of the associated partial differential equation.

A. Central Limit Theorems

It is well known that a normal random variable can be represented as the limit of normalized sums of Bernoulli trials, that is, i.i.d. binomial random variables. This idea, a version of the Central Limit Theorem, leads to the characterization given in this section of the Black-Scholes option-pricing formula (equation [5.11]) as the limit of the binomial option-pricing formula (equation [2.16]), letting the number of trading periods per unit of time go to infinity. Aside from making an interesting connection between the discrete- and continuous-time settings, this also suggests a numerical recipe for calculating continuous-time arbitrage-free derivative security prices.

A sequence \(X_n\) of random variables converges in distribution to a random variable \(X\), denoted \(X_n \Rightarrow X\), if, for any bounded continuous function \(f: \mathbb{R} \to \mathbb{R}\), we have \(E[f(X_n)] \to E[f(X)]\). We could allow \(X\) and each of \(X_n, X_{n_1}, \ldots\) to be defined on different probability spaces. A standard version of the Central Limit Theorem reads along the following lines. A random variable is standard normal if it has the standard normal cumulative distribution function.

Central Limit Theorem. Suppose \(Y_1, Y_2, \ldots\) is a sequence of independent and identically distributed random variables on a probability space, each with expected

value \(\mu\) and finite variance \(\sigma^2 > 0\). For each \(n\), let \(Z_n = Y_1 + \cdots + Y_n\). Then, for any standard normal random variable \(X\),

\[
\frac{Z_n - n\mu}{\sigma \sqrt{n}} \xrightarrow{d} X.
\]

Proofs are cited in the Notes. This version of the Central Limit Theorem is not general enough to handle convergence of the binomial option-pricing formula of Exercise 2.1 to the Black-Scholes formula. In order to set up the required extension, we say that a collection

\[
Y = \{Y_{ni} : i = 1, \ldots, k(n), n = 1, 2, \ldots \}
\]

with \(k(n) \to \infty\) as \(n \to \infty\) is a triangular array if, for each \(n\), the random variables \(Y_{ni}, i = 1, \ldots, k(n)\) are independently distributed random variables on some probability space. The following version of the Central Limit Theorem is sufficient for our purposes here, and can be proved as an easy corollary of the Lindeberg-Feller Central Limit Theorem given in Appendix C.

Proposition. Suppose \(Y\) is a triangular array of random variables such that

the \(Y_{ni}\) are bounded in absolute value by a constant \(\delta_n\), with \(\delta_n \to 0\). Let \(Z_n = \sum_{i=1}^{k(n)} Y_{ni}\). If \(E(Z_n) \to \mu\) and \(\text{var}(Z_n) \to \sigma^2 > 0\), then \(Z_n\) converges in distribution to a normally distributed random variable with mean \(\mu\) and variance \(\sigma^2\).

# B. Binomial to Black-Scholes

Recall the setup from Section 5E of the Black-Scholes model for pricing a European put option:
a probability space \((\Omega, \mathcal{F}, \mathbb{P})\) on which there is a standard Brownian motion \(B_t\); a stock-price process \(S\) defined by \(S_t = x \exp(\alpha t + \sigma B_t)\) and a bond-price process \(B\) defined by \(B_t = e^{rt}\), for constants \(\alpha, \sigma,\) and \(r\); the put-option payoff \((K - S_T)^+\), defined by the expiration time \(T\) and exercise price \(K\).

The solution of the “arbitrage-free” put price, in the sense of Chapter 6, is

\[ p = e^{-rT} \mathbb{E}^{\mathbb{Q}} \left[ (K - x e^{X_T})^+ \right], \tag{1}
\]

where \(X_t = (r - \sigma^2/2)t + \sigma B_t^{\mathbb{Q}}\) for any \(t < T\), where \(B^{\mathbb{Q}}\) is a standard Brownian motion under the equivalent martingale measure \(\mathbb{Q}\).

In the binomial setting of Exercise 2.1, the stock has a binomial return in each period with outcomes \(D\) and \(U > D\), while a riskless bond has a constant return given by some \(R > D, U\). The risk-neutralized probabilistic representation of the put price is given, as with the call-price formula of Chapter 2, by

\[ e^{-rT} \mathbb{E}^{\mathbb{Q}} \left[ (K - x e^{Y_n})^+ \right], \tag{2}
\]

where \(Y_n = Y_{n1} + \cdots + Y_{nn}\), and where \(Y_{n1}, \ldots, Y_{nn}\) are, under \(\mathbb{Q}\), i.i.d. binomial random variables (called Bernoulli trials) having outcomes \(u = \log(U)\) and \(d = \log(D)\) with respective “risk-neutral” probabilities \(p = (R - D)/(U - D)\) and \(1 - p\). We can calibrate the binomial stock returns \(U\) and \(D\), as well as the bond return \(R\), to our model of the continuous-time stock- and bond-price processes as follows. Obviously, we set the bond return at \(R = e^r\). The stock returns \(U\) and \(D\) require more thought. To maintain some probabilistic similarity between the continuous-time and binomial models, we will explicitly model an exogenously given probability \(q\) of an up-return \(U\), and choose \(U\) and \(D\) so that the “actual” (under \(\mathbb{P}\)) mean and standard deviation of the continuously compounding stock returns are the same in the two settings. The probability \(q\) should not be confused with the “risk-neutralized” probability \(p\) constructed from the returns. Let us arbitrarily choose \(q = 0.50\), and then select \(u = \alpha + \sigma\) and \(d = \alpha - \sigma\). With this, the continuously compounding stock returns in both the discrete- and continuous-time models have, under \(\mathbb{P}\), mean \(\alpha\) and variance \(\sigma^2\) per unit of time. Many other combinations of \(q, u,\) and \(d\) would work.

Let “Model \(n\)” refer to the binomial model with \(n\) trading periods per unit of time and with returns \(U_n\), \(D_n\), and \(R_n\) per trading period. We will allow \(n\) to approach infinity, always calibrating, as above, the binomial returns to the continuous-time returns. In order to maintain the mean and variance (under \(\mathbb{P}\)) of total returns per unit of time at the continuously compounding levels \(\alpha\) and \(\sigma^2\) respectively, we reset the per-trading-period continuously compounding returns \(u_n = \log(U_n)\) and \(d_n = \log(D_n)\) to
\(u_n = \alpha/n + \sigma/\sqrt{n}\) and \(d_n = \alpha/n - \sigma/\sqrt{n}\). We leave \(q_n\) fixed at 0.50. With i.i.d. returns, the per-unit-of-time risk-neutral mean and variance of the continuously compounding returns are then, respectively,

\[ n[q_n u_n + (1 - q_n)d_n] = \alpha \] and \[ n q_n(1 - q_n)(u_n - d_n)^2 = \sigma^2, \]

precisely as required. The per-trading-period return on the bond is \(R_n = e^{r/n}\). The number of trading periods required for passage of \(T\) units of calendar time is \(nT\). We can therefore rewrite the put-price formula (2) for Model \(n\) as

\[ p_n = e^{-rT} \mathbb{E}^{\mathbb{Q}} \left[ (K - x e^{Y_n})^+ \right], \tag{3}
\]

where \(Y_n = Y_{n1} + \cdots + Y_{nn}\) and where \(Y_{n1}, \ldots, Y_{nn}\) are i.i.d. binomial with outcomes \(u_n\) and \(d_n\) at respective risk-neutralized (\(\mathbb{Q}\)) probabilities \(p_n\) and \(1 - p_n\), where

\[ p_n = \frac{R_n - D_n}{U_n - D_n} = \frac{e^{r/n} - e^{d_n}}{e^{u_n} - e^{d_n}}. \tag{4}
\]

The per-unit-of-time risk-neutralized mean and variance of returns are, respectively,

\[ M_n = n[p_n u_n + (1 - p_n)d_n]
\] and \[ V_n = n p_n(1 - p_n)(u_n - d_n)^2.
\]

An exercise shows that \(M_n \to r - \sigma^2/2\) and \(V_n \to \sigma^2\). Thus, \(\mathbb{E}^{\mathbb{Q}}[Y_n] \to (r - \sigma^2/2)T\) and \(\text{var}^{\mathbb{Q}}[Y_n] \to \sigma^2 T\), where \(\text{var}^{\mathbb{Q}}\) denotes variance under \(\mathbb{Q}\). Because \(u_n\) and \(d_n\) each converge to zero, the version of the Central Limit Theorem given by Proposition A implies that \(Y_n \Rightarrow X_T\). Because the function \(h: \mathbb{R} \to \mathbb{R}\) defined by \(h(y) = (K - x e^y)^+\) is bounded and continuous, the binomial put price \(p_n\) of (3) converges to the Black-Scholes put price \(p\) given in (1) as the number \(n\) of trading intervals per unit of time goes to infinity.

The only properties of the put payoff function \(h\) used above are its continuity and its boundedness. The same arguments therefore allow one to conclude that, for any bounded continuous \(g\), the arbitrage-free price of a claim to \(g(S_T)\) in the binomial setting with \(n\) trading periods per unit of time converges to the corresponding continuous-time “arbitrage-free” price \(\mathbb{E}^{\mathbb{Q}}[e^{-rT}g(Z_T)]\) obtained from the Feynman-Kac formula, where \(Z_T = x \exp[(r - \sigma^2/2)T + \sigma B_T^{\mathbb{Q}}]\).

By put-call parity, the binomial call-pricing formula converges to the Black-Scholes call-pricing formula in the same sense. That is, put-call parity holds in the limit.this computing budget grows to infinity, the approximation error
\(\hat{a}_n - a\) has an asymptotically normal distribution provided \(k_n\) grows with \(n\)

like \(n^{2p}\). If \(k_n\) does not grow at this rate, then the asymptotic distribution is “infinite,” meaning a loss in efficiency. For instance, with the Euler scheme (\(p = 1\)), the number of simulations should quadruple (at least asymptotically) with each doubling of the number of time intervals. With a second-order scheme such as (8), the number of simulations should be on the order of the number of time intervals to the fourth power, and so on. Sharper results concerning the asymptotic distribution can be found with the original source for this result, cited in the Notes.

Theorem 1. Suppose Condition A holds.
(A) If \(k_n/n^{2p} \to +\infty\) or if \(k_n/n^{2p} \to 0\) as \(n k_n \to 00\), then
\((k_n n)^{1/2} (\hat{a}_n - a) \Rightarrow +\infty\). (10)

(B) If \(k_n/n^{2p}\) converges to a nonzero constant \(c\) as \(n k_n \to \infty\) then

\(b/(1+2p)^{-1}\)

\((cn)^{1/2} (\hat{a}_n - a) \Rightarrow \mathcal{L}\)

\(W + BC?,\) (11)

where \(C = C(\mu + 2p)\), \(W\) is standard normal, and \(\sigma^2 = \text{var}(Z)\).

Proof: Note that

\(\frac{1}{k_n} \sum_{i=1}^{k_n} (Z_i(n) - a) = \hat{a}_n - a\)

Let \(Z_i(n) = Z_i(n) - a(n)\). Then,

\(= \frac{1}{k_n} \sum_{i=1}^{k_n} Z_i(n) + (a(n) - a)\)

. Parts (i) and (ii) of Condition A allow an application of the
Lindeberg-Feller Central Limit Theorem (Appendix C). Thus, as \(n \to \infty\),

\((k_n n)^{1/2} (\hat{a}_n - a) \Rightarrow \sigma W\),

where \(W\) is standard normal and \(\sigma^2 = \text{var}(Z)\). Applying part (iii) of
Condition A and some algebra completes the proof. \(\blacksquare\)

# G. Applying Feynman-Kac
Consider the solution given by (5.40) for the price \(C(x, 0)\) of a derivative asset paying \(g(S_T)\) at time \(T\), where \(S\) is defined by (5.34) and where the short rate at time \(t\) is given by \(r(S_t, t)\). To repeat, we have

\(C(x, 0) = E[\Psi_T g(Z_T)]\), (12)
where \(\Psi_t = \exp[-\int_0^t r(Z_s, s) ds]\) and where
\(dZ_t = \mu(Z_t, t) Z_t dt + \sigma(Z_t, t) dB_t\); \(Z_0 = x\).

Since \(d\Psi_t = -r(Z_t, t) \Psi_t dt\), the \(\mathbb{R}^{1+1}\)-valued process \(X\) defined by \(X_t = (\Psi_t, Z_t)\) solves an SDE of the same form as (6). We assume that the associated coefficient functions \(a\) and \(b\) satisfy the technical regularity conditions imposed with (6) of Section D. This calls for \(r\) to be bounded with bounded derivatives of every order and for \(\mu\) to have bounded derivatives of every order. The Feynman-Kac solution (12) can be written in the form \(E[f(X_T)]\), where \(f : \mathbb{R}^{1+1} \to \mathbb{R}\) is defined by \(f(z_0, z_1) = g(z_b, z_1)\). If \(g\) has bounded derivatives of every order, then the derivative asset price \(C(x,0)\) can be approximated as suggested in the previous section. (Weaker conditions will suffice.)

The case of options requires special handling. The payoff function
\(g\) of a call, defined by \(g(x) = (x - K)^+\), is not even once differentiable.
The “kink” at \(K\) is the only issue to overcome. The function \(g\) can be satisfactorily approximated by \(g_\alpha\), where, for any \(\alpha > 0\),

\(g_\alpha(x) = \frac{(x - K + \alpha)}{2} + \frac{\sqrt{(x - K)^2 + \alpha^2}}{2}\) (13)

Indeed, \(g_\alpha\) has continuous derivatives of any order, satisfies a growth condition, and converges uniformly and monotonically from above to \(g\)
as \(\alpha \to 0\). The Dominated Convergence Theorem therefore implies that the associated Feynman-Kac solution also converges to \(C(x, 0)\) as \(\alpha \to 0\).

# H. Finite-Difference Methods

This section reviews a simple finite-difference method for the PDE associated with asset prices. After reviewing the basic idea, we will work out an example based on the Cox-Ingersoll-Ross model of the term structure.

We will treat the Cauchy problem: Given real-valued functions \(r\), \(\mu\), \(h\),
\(L\) and \(\sigma\) on \(\mathbb{R} \times [0, T]\), find a function \(f\) in \(C^{2,1}(\mathbb{R} \times [0, T))\) solving

\(Df (x, t) - r(x, t) f(x, t) + L(x, t) = 0,\) \((x,t) \in \mathbb{R} \times [0, T),\) (14)

with boundary condition

\(f(x, T) = g(x, T),\) \(x \in \mathbb{R},\) (15)

where

\(Df (x, t) = f_t (x, t) + \mu(x, t) x f_x (x, t) + \frac{1}{2} \sigma^2(x, t) x^2 f_{xx} (x, t)\).

As we have seen in Chapter 5, we can interpret the solution \(f\) to (14)-(15)
as the arbitrage-free market value of a security that promises the dividend rate \(h(x, t)\) at time \(t\) when the state is \(x\), assuming that the security has a terminal value of \(g(x, T)\) at time \(T\) when the state is \(x\). The short rate is \(r(x, t)\)
at time \(t\) when the state is \(x\), and the “primitive” securities have prices and dividends determining the functions \(L\) and \(\sigma\) in the manner described in Chapter 5. Alternatively, \(L\) and \(\sigma\) could be determined directly from the equilibrium approach shown in Chapter 10 (see Exercise 10.7). Regularity conditions that ensure the existence and uniqueness of solutions are treated in Appendix E, where probabilistic Feynman-Kac solutions are also treated.

The basic idea of the finite-difference method for solving (14)-(15)
is to choose a grid

\(\{(x_i, t_j) : x_i \in \{1,..., N\}, t_j \in \{1,..., M\}\} \subset \mathbb{R} \times [0, T),\)

and to find an approximate solution of (14)-(15) in the form of an
\(N \times M\) matrix \(F\) whose \((i, j)\)-element \(F_{ij}\) is to be an approximation of
\(f(x_i, t_j)\). We always take \(t_1 = 0\) and \(t_M = T\). We take constants \(\Delta x\) and \(\Delta t\)
to define the mesh sizes of the grid, so that \(x_i - x_{i-1} = \Delta x\) for all \(i > 1\)
and \(t_j - t_{j-1} = \Delta t\) for all \(j > 1\), as depicted in Figure 12.1. In principle, increasing the number \(N\) of space points or the number \(M = T/\Delta t\) of time points increases the accuracy of the approximation, although the convergence and stability properties of finite-difference methods can be a delicate issue. Various finite-difference methods could be suitable for the Cauchy problem, depending on the properties of \((\mu, r, h, g)\). We will merely describe one of these, sometimes known as the Crank-Nicholson method, which has reasonable properties. We leave a characterization of

the accuracy and stability of this and other finite-difference schemes to Sources cited in the Notes.

12. Numerical Methods

— \(N\) 一一万一万国 A 一十一上 — + 广1
一 - 一一一 [ 屋 hy  Finag+t 皇 , Try VRon iz。T Tras Taya - 3 | ( - 2十 _l_ 1 [ 一 T | “ 9 1 2 3 7 at M T=MΔt

Figure 12.1. Finite-Difference Grid

The basis of the Crank-Nicholson method is the following approximation of the derivatives of \(f\) given \(F\):

\(\frac{\partial f}{\partial t} (x_i, t_j) \sim \frac{F_{ij} - F_{i,j-1}}{\Delta t}\)

\(f_x (x_i, t_j) \sim \frac{F_{i+1,j} - F_{i-1,j}}{2\Delta x}\)

\(f_{xx} (x_i, t_j) \sim \frac{F_{i+1,j} - 2F_{ij} + F_{i-1,j}}{(\Delta x)^2}\)

It may be seen that the Crank-Nicholson method actually takes \((F_{ij} +\)
\(F_{i,j-1})/2\) as our approximation of \(f (x_i, t_j)\). Accordingly, as we substitute these approximations of the derivatives of \(f\) into (14), we obtain at \((x_i, t_j)\),

\(1 \leq i \leq N\), the expression

\(A_{ij} F_{i-1,j} + B_{ij} F_{ij} + C_{ij} F_{i+1,j} = D_{ij} F_{i-1,j-1} + E_{ij} F_{i,j-1} + G_{ij} F_{i+1,j-1}\) (16)

where
\(A_{ij} = -\frac{\mu(x_i, t_j) x_i}{4\Delta x} + \frac{\sigma^2(x_i, t_j) x_i^2}{4(\Delta x)^2}\),
\(B_{ij} = -r(x_i, t_j) \frac{\Delta t}{2} + \frac{1}{2} - \frac{\sigma^2(x_i, t_j) x_i^2}{2(\Delta x)^2}\),
\(C_{ij} = \frac{\mu(x_i, t_j) x_i}{4\Delta x} + \frac{\sigma^2(x_i, t_j) x_i^2}{4(\Delta x)^2}\),
\(D_{ij} = \frac{\mu(x_i, t_j) x_i}{4\Delta x} - \frac{\sigma^2(x_i, t_j) x_i^2}{4(\Delta x)^2}\),
\(E_{ij} = r(x_i, t_j) \frac{\Delta t}{2} + \frac{1}{2} + \frac{\sigma^2(x_i, t_j) x_i^2}{2(\Delta x)^2}\),
\(G_{ij} = -\frac{\mu(x_i, t_j) x_i}{4\Delta x} - \frac{\sigma^2(x_i, t_j) x_i^2}{4(\Delta x)^2}\), \(H_{ij} = \frac{L(x_i, t_j) \Delta t}{2}\).

Of course, (16) is not defined at \(i = 1\) or \(i = N\), for which we substitute with equations of the form

\(a_{1j} F_{1,j} + b_{1j} F_{2,j} = d_{1j}\); \(a_{Nj} F_{N-1,j} + b_{Nj} F_{N,j} = d_{Nj}\), (17)

for suitable coefficients \(a_{1j}, b_{1j}, d_{1j}, a_{Nj}, b_{Nj}, d_{Nj}\) that may depend on the particular problem at hand.

We can combine (16) and (17) to obtain a backward difference equation for the columns \(F_{\cdot, M}, F_{\cdot, M-1}, \dots, F_{\cdot, 1}\) of \(F\), given by

\(A_j F_j = d_j\), (18)
with terminal boundary condition
\(F_M = g(x_i, T),\) \(i \in \{1,\dots, N\}\), (19)

where \(A_j\) is the tridiagonal matrix given by

\(A_j = \begin{bmatrix} b_{1j} & c_{1j} & 0 & 0 & 0 & 0 \\ a_{2j} & b_{2j} & c_{2j} & 0 & 0 & 0 \\ 0 & a_{3j} & b_{3j} & c_{3j} & 0 & 0 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & a_{N-1,j} & b_{N-1,j} & c_{N-1,j} \\ 0 & 0 & 0 & 0 & a_{Nj} & b_{Nj}
\end{bmatrix}\) (20)

and where \(d_j \in \mathbb{R}^N\) is the vector with \(i\)-th element

\(d_{ij} = D_{ij} F_{i-1,j-1} + E_{ij} F_{i,j-1} + G_{ij} F_{i+1,j-1} - H_{ij}\). (21)
Standard “staircase” algorithms for solving linear equations of the tridiagonal form (18) can be found in off-the-shelf software packages. (Code is provided in Appendix J.) Such algorithms exploit the special structure of
\(A_j\), avoiding a “brute-force” calculation of its inverse.

To summarize, the basic finite-difference algorithm (18)—(19) begins by fixing \(F_M\) according to the terminal boundary condition (19). Then
\(d_{M-1}\) is computed from \(F_M\) by (21). Then \(F_{M-1}\) is computed by solving the tridiagonal equation (18) with \(j = M - 1\). Next, \(d_{M-2}\) is computed from
\(F_{M-1}\), (18) is solved for \(F_{M-2}\), and so on, until \(F_1\) is solved. If the functionssame functions f, g, and h. Only the functions f and g differ from security to security. In this case, given a grid {(x_i, t_j)} defined by mesh sizes Δx and Δt, it makes sense to find an approximation Ψ_{ij} of the market value at time 0 of a security that pays 1/Δx units of account at time t_j in the event that the state is between x_i + Δx/2 and x_i - Δx/2. With this, it is reasonable to approximate the market value at time 0 of the security with payoff functions h for dividend rate and g for terminal value by

V(h, g) = ΔtΔx Σ_{i=1}^N Σ_{j=1}^M ψ_{ij} h(x_i, t_j) + Ψ_{iM} g(x_i, T).  (30)

We will show how the same finite-difference approach used to calculate F in Section J can be modified to calculate the "approximate state prices" specified by Ψ. This is based on the fundamental solution of the PDE (14), reviewed in Appendix E. Under technical conditions, for each initial state x* in ℝ, there is a function ψ ∈ C^{2,1}(ℝ × (0, T]) with the following (almost equivalent) properties:

(a) ψ satisfies
∂ψ/∂t + r(x, t)ψ + ∇ψ·[μ(x, t) - r(x, t)x] + ½ Tr[σ(x, t)σ(x, t)^T ∇^2ψ] = 0, (x, t) ∈ ℝ × (0, T], (31)

with an initial boundary condition requiring essentially that ψ(·, t) is the density of a measure that converges as t ↓ 0 to a probability measure ν with ν({x*}) = 1; and

(b) for any (g, h) satisfying technical conditions, the solution f of the PDE (14)-(15) satisfies

f(x*, 0) = ∫_0^T ∫_ℝ h(x, t)ψ(x, t) dx dt + ∫_ℝ g(x, T)ψ(x, T) dx, (32)

which is the integral analogous to the sum given by (30).

The PDE (31) is sometimes called the Fokker-Planck equation, or the forward Kolmogorov equation, to distinguish it from the backward Kolmogorov equation (14). For the case r = 0, one can literally treat ψ(·, t) as the probability density of X_t, where X solves the underlying stochastic differential equation dX_t = μ(X_t, t) dt + σ(X_t, t) dB_t, with X_0 = x*. Much more can be said on this point, as indicated in sources cited in the Notes. The initial boundary condition for (31) stated above corresponds naturally to this interpretation of ψ. An explicit solution for ψ for the Cox-Ingersoll-Ross model (28) is given in Section 7G.

Now, given (32) and the equivalence between (a) and (b), in order to solve for f(x*, 0) we would like to approximate ψ with a finite-difference solution Ψ of the PDE (31). The same Crank-Nicholson approach can be applied, generating the forward difference equation for the columns Ψ_1, ..., Ψ_M of Ψ given by

Ψ_j = Ψ_{j-1} + A_j Ψ_j Δt, (33)

with boundary condition for a given initial state X_0 = x* of

Ψ_1 = e_1 / Δx, (34)

where the tridiagonal matrix A_j and the vector Ψ_1 can be calculated for each j in the same manner as for the backward difference equation, using the Crank-Nicholson approximations for the derivatives of ψ in terms of Ψ. Specifically, for μ twice continuously differentiable with respect to x and A continuously differentiable with respect to x, we have

d_j = Φ_j Ψ_{j-1} + Θ_j Ψ_j, (35)

and

Φ_j = I + ½ Δt B_j, Θ_j = I - ½ Δt B_j, (36)

where

a_{ij} = (Δt / 2 Δx) [μ_i + (σ_i^2)/Δx], b_{ij} = - (Δt / 2) [ (2 σ_i^2)/(Δx)^2 + r_i + (μ_i - r_i x_i)/Δx ], c_{ij} = (Δt / 2 Δx) [ (σ_i^2)/Δx - (μ_i - r_i x_i) ].

The cases of i = 1 and i = N again require special consideration.

One begins with the initial condition (34) for Ψ, and then propagates the solution forward, calculating Ψ_j at each stage by (33), given d_j in terms of Ψ_{j-1}. (In fact, in application, stability of solutions may be more easily achieved by initial conditions that are not so "concentrated" at the initial condition as suggested by (34), but rather by an initial condition at t_1 later in time that is, for example, a low-variance Gaussian density suggested by the parameters. There is in any case a certain "art" to obtaining reasonable approximate solutions.)

Given Ψ, the approximate value of any security with dividend rate h and terminal value g is given by (30). If there is but a single security to value, (30) involves an extra set of computations that is not required with the backward approach. With many securities to value, however, the "forward approach" can involve significant savings in computations.

The astute reader will notice that we could have avoided the scaling factors Δx and 1/Δx in (30) and (34), respectively, in which case Ψ would not be an approximation for ψ, but rather for ψΔx.

L. Numerical Solution of the Pricing Semi-Group

In the tridiagonal system (33)-(35), we have d_j = C_j Ψ_{j-1} for the tridiagonal matrix

C_j = I - ½ Δt B_j.

Thus (33) can be re-expressed in the recursive form

Ψ_j = Π_j Ψ_0, (37)

where Π_j = (Θ_j)^{-1} Φ_j. It follows that, for any j and k > j,

Π_{k,j} = Π_k ... Π_{j+1}, (38)

where Π_j denotes the identity matrix. The collection Π = {Π_{k,j} : 1 ≤ j < k ≤ M} of N x N matrices is a semi-group since it has the property: Whenever j < k < m, we have Π_{m,j} = Π_{m,k} Π_{k,j}. We will describe some of the useful properties of the semi-group Π.

First, for any initial state x_i in the grid, the associated approximate state-price matrix Ψ is given by

Ψ = Π e_1, (40)

where e_1 is given by (34). This means that, given the semi-group Π, the state prices associated with any given initial state can be obtained without repeated solution of the tridiagonal equations (37).

Second, given any payoff functions h and g, the N x M matrix F* approximating the solution f to (14)-(15) is easily characterized as follows. For any j and k > j, we have

f(x_i, t_j) ≈ Σ_{m=j+1}^k h(x_i, t_m) ψ_{im} Δt + Ψ_{ik} g(x_i, t_k), (41)

where H_m is the vector in ℝ^N with h(x_i, t_m)Δt as its i-th element. In particular, (41) applies with k = M and the boundary condition F_{iM} = g(x_i, T).

Although solving for the semi-group Π can be computationally intensive, there are obvious compensations. For the case in which μ, σ, and r do not depend on t the matrices A_j and C_j do not depend on j, so there is but a single matrix Π to compute, with Π_{j+1,j} = Π for all j.

The close parallel between (41) and the Markov chain valuation equation (3.17) is not an accident. One can indeed approximate the solution X to the SDE dX_t = μ(X_t, t) dt + σ(X_t, t) dB_t with that of an N-state Markov chain having transition matrix q^j at period j ∈ {1,..., M} given by

q_{ik}^j = ν_i P(X_{t_j} ∈ [x_k - Δx/2, x_k + Δx/2] | X_{t_{j-1}} = x_i). (42)

A source given in the Notes gives the sense of this approximation and further details on this connection between continuous and discrete pricing.

The parallel with the discrete-time case extends to the pricing of American securities. Using the semi-group approach, one can replace the backward difference equation (29) for the American security described in Section J with the backward equation

V_i = max( Π_{j+1,j} (V_{j+1} + H_{j+1}), G_i ), (43)

where the maximum is taken element-wise and where G_i is the vector in ℝ^N whose i-th element is g(x_i, t_j). Equation (3.21) gives the exact discrete-time version of this American valuation algorithm.

# M. Fitting the Initial Term Structure

In the context of the term-structure model (22), there are many practical applications in which the initial term structure is given from market data in the form of a vector p in ℝ^M, with p_j denoting the price at time 0 of a unit pure discount bond maturing at t_j. (In practice, p is often obtained from the prices of coupon bonds by spline methods cited in the Notes of Chapter 7.) Since a model rarely coincides with reality, the functions μ and σ determining the risk-neutral behavior of the short rate will not, in general, generate a term structure consistent with the market data p.Suppose, however, that for each t, the functions y(·, t) and o(·, t) depend on a free parameter A(t). One can imagine choosing the function A in order to match the solution of the term structure to that given by p. For example, one could extend the CIR model (28) by replacing the constant x with A(t), and then choose A(t₁), A(t₂), ..., A(t_M) so that the solution given in Section I for the term structure is consistent with p.

One can imagine a number of different numerical approaches to this term-structure matching procedure. One that has been suggested by a source cited in the Notes is based on the numerical solution p for state prices. Using the fact that Σ_{i} W_i approximates p, the proposed algorithm for A is given by the following steps.

(a) Let j = 2.
(b) Search for that number A(t_j) such, given p_{j-1}, we have

p(A(t_j), W_j) = P_j(44)

where p(A(t_j), W_j) = P_j is notation indicating the dependence of the solution p of (33) on W_{j-1} and A(t_j) given by (35)
and (36). This one-dimensional search could be conducted by a Newton-Raphson iterative method.

(c) Let j be increased by 1, and return to step (b) if j < M. Otherwise, stop.

In order for the numerical search for A(t_j) in step (44) to succeed, and for the solution to be uniquely defined, the model should be such that p(A(t_j)) is a strictly monotonic continuous function with range (0, 1).
This is true for the CIR example given above, in which x is replaced in (28) with A(t).

One could match additional parameters to market data on the prices of derivative securities, such as options. The idea is to obtain better "calibration" with the market in order, in principle, to obtain higher accuracy in the pricing of derivative securities. For example, one can extend by taking A to be an R²-valued function specifying two free parameters, to be matched against the initial term structure of bond prices as well as the ini

tial "volatility structure" implicit in bond-option prices, an approach taken in papers cited in the Notes.

Of course, with the passage of time, the "matched" model will fall out of calibration, implying that the free parameter vector A was in fact inappropriate. In typical practice, a new set of free parameters is chosen, and valuation proceeds again. This process of routine reparameterization is theoretically inconsistent (and, to the author's knowledge, has been applied with relatively little econometric sophistication), but seems to some degree unavoidable. The "name of the game" is apparently to specify an accurate term-structure model that is both tractable and relatively stable over time.

# Exercises

12.1 Prove Proposition A, using the Lindeberg-Feller Central Limit Theorem given in Appendix C.

12.2 Show, as claimed in Section B, that the perunitoftime risk-neutralized mean M and variance V_t converge to r − σ²/2 and σ², respectively.

12.3 Show that the sequence { [X_{nt0} − K]^+ } of "binomial" call-option payoffs constructed in Section C is uniformly integrable. Hint: Use the converse part of Theorem C.

12.4 Show how the Lindeberg-Feller Central Limit Theorem is invoked in order to obtain the limiting normal distribution asserted in the proof of Theorem F.

12.5 Verify the Crank-Nicholson equation (16) from (14) and the CrankNicholson derivative approximations.

12.6 (Binomial Approximation of the Black-Derman-Toy Term-Structure Model).
The continuous-time version of the Black-Derman-Toy model shown in Exercise 7.1 has the short-rate process r given by

r_t = U(t) exp[B(t) B(d)], where d is a standard Brownian motion under an equivalent martingale measure
Q, and where U : [0, ∞) → R₊ and B : [0, ∞) → R₊ are continuously differentiable. The discrete-time version of the Black-Derman-Toy model given in Exercise
3.11 has the short-rate process r given by r_t = a_t exp(b_t X_t), where, for each time t ∈ {0,1,...}, a_t and b_t are strictly positive constants, and X_t is a shock process with the property that, for all t,

Q(X_{t+1} − X_t = 1 | X_0,...,X_t) = Q(X_{t+1} − X_t = 0 | X_0,...,X_t) = ½.

This exercise calls for the construction, at each t of sequences {a_t^n} and {b_t^n} of coefficients for the discrete-time Black-Derman-Toy model with the property that, for each t ∈ {1,2,...},

r_t = a_t^n exp(b_t^n X_{nt}) → r_t

or convergence in distribution of the discrete-time model with n time periods per unit of calendar time to the continuous-time model. Hint: Use the Continuous
Mapping Theorem, and the fact that z → U(t) exp(B(t)z) defines a continuous function on R into R. We can write

r_t = U(t) exp[B(t) Z_t]

where Z_t = (1/√n) Σ_{i=1}^{nt} Y_i and Y_i are i.i.d. with mean zero and variance t.
Show that it is therefore enough to choose {a_t^n} and {b_t^n} so that

X_{nt} = √n (b_t^n)⁻¹ (log Z_t − log U(t)) → Z,

where Z is normally distributed with mean zero and variance t. Make use of the
Central Limit Theorem to design {a_t^n} and {b_t^n} accordingly.

# Notes

(A) Standard references on probability theory include Chung (1974), Chow and
Teicher (1978), Billingsley (1986), and Durrett (1991), all of which include the law of large numbers and the Central Limit Theorem.

(B-C) The convergence of the binomial model of option pricing to the BlackScholes model is due to Cox, Ross, and Rubinstein (1979). Extensions of this approach can be found in Amin (1991, 1993b), Bertsimas, Kogan, and Lo (1998),
Clewlow and Carverhill (1995), Cutland, Kopp, and Willinger (1991, 1993a),
Diener and Diener (1999), Duffie (1988c), Duffie and Protter (1988), He (1990,
1991), Heston and Zhou (1997), Hubalek and Schachermayer (1998), Lamberton and Pagés (1990), Lamberton (1997), Lesne, Prigent, and Scaillet (2000), Lee
(1991), Madan, Milne, and Shefrin (1989), Nelson and Ramaswamy (1989),
Prigent (1995), Rogers and Stapleton (1998), Willinger and Taqqu (1991), and Eberlein (1991), among many other papers.

For other numerical procedures, see Gerber and Shiu (1994) and Levy,
Avellaneda, and Paras (1994). Broadie, Glasserman, and Kou (1997, 1999) treat discretization errors for path-dependent options and barrier options. Curran
(1996) and Glasserman, Heidelberger, and Shahabuddin (1999) discuss importance sampling for path-dependent option valuation. Fournié and Lasry (1996)
and Fournié, Lasry, and Touzi (1996) also treat importance sampling with pricing applications. On approximation methods for Asian options, see Chalasani,
Jha, and Varikooty (1998), Fu, Madan, and Wang (1999), and Zvan, Forsyth, and Vetzal (1998).

(D-E) This section is based on Talay and Tubaro (1990). Milshtein (1974,
1978) introduced second-order discretization schemes such as (8). Bally and
Talay (1996), and Talay (1984, 1986, 1990) provide more advanced second-order schemes for discretization of stochastic differential equations in Rⁿ. See also
Bernard, Talay, and Tubaro (1994), Kusuoka (1999a), Newton (1990), and Török
(1993) in this regard. On discretization of backward SDEs, see Chevance (1995, 1996) and Douglas, Ma, and Protter (1996).

(F) This section is based on Duffie and Glynn (1995), where additional details may be found. The first edition of this book took a different approach to the trade-off between number of simulations and number of time steps, based on the
Large Deviations Theorem, which is described by Durrett (1991).

(G) Boyle, Broadie, and Glasserman (1997) offer a general survey of pricing by Monte Carlo simulation. The smooth approximation g_ε in Section G of the call payoff function appears in Duffie (1988c), and was related to the author by Stephen Smale. Various applications of the Monte Carlo estimation of derivative asset prices and hedging are given by Andersen (1996), Avellaneda,
Buff, Friedman, Grandchamp, Kruk, and Newman (1999), Barraquand (1993),
Boyle (1977, 1988, 1990), Boyle, Evnine, and Gibbs (1989), Glasserman and
Zhao (1999), Fournié (1993), Jones and Jacobs (1986), and Schoenmakers and
Heemink (1996). For the simulation of hedging coefficients, or "deltas" andother derivatives, see Clewlow and Carverhill (1992) and Broadie and Glasserman
(1996). For "quasi-Monte Carlo" simulation methods, with finance applications, see Caflisch and Morokoff (1995, 1996), Caflisch, Morokoff, and Owen (1997),
Chidambaran and Figlewski (1995), Joy, Boyle, and Tan (1996), Morokoff and
Caflisch (1993, 1994, 1995), and Moskowitz and Caflisch (1994).

Owen (1996, 1997) and Owen and Tavella (1996) apply scrambled-net methods to pricing and risk calculations.

(H) Tavella and Randall (2000) review the solution of derivative pricing by finitedifference methods. Mitchell and Griffiths (1980), Smith (1985), and Strikwerda
(1989) are basic treatments of the finite-difference solution of PDEs. Computer code for the solution of tridiagonal systems of equations such as (18) is given by
Press, Flannery, Teukolsky, and Vetterling (1993). An example of a more advanced finite-difference approach is given by Lawson and Morris (1978). Schwartz (1977)
introduced the use of finite-difference methods to the solution of asset pricing in finance. Andreasen (1998) applies finite-difference methods to lookback options.
For more examples of finite-difference methods with financial applications, see
Clewlow (1990) and Druskin, Knizhnerman, Tamarchenko, and Kostek (1997).

(I) The term-structure example of Section I is based on Courtadon (1982)
and Stanton (1995b). Jamshidian (1991c) gives an alternate change of variables under which the diffusion is a constant. The literature in finance is reviewed and summarized by Clewlow (1990). The Crank-Nicholson approximation is known as an implicit method. Hull and White (1990b) show how the range of the simpler explicit methods can be extended. Hull and White (1993) review some of the simpler implicit and explicit methods. Dewynne and Wilmott (1994) provide example

applications to exotic options. Barles, Daher, and Romano (1992) examine the general issue of convergence of finite-difference schemes in finance applications.
Nelson and Ramaswamy (1989) treat finite-difference methods that are based on replacing the underlying stochastic differential equation with a Markov chain that has binomial transitions, extending the range of application of the binomial approach. Kishimoto (1989), Stanton (1990), and Stanton and Wallace
(1995) numerically solve path-dependent security prices, such as mortgage-backed securities. Willard (1996) treats path-dependent valuation in a multifactor setting.

Dengler and Jarrow (1996) examine the implications of variable time steps in numerical option-pricing solutions.

(J) Justification of the valuation algorithm (29) for securities with early exercise options is a delicate issue that is treated by Jaillet, Lamberton, and Lapeyre (1988,
1990). An early variation of this algorithm for the Black-Scholes (log-normal)
put option problem is found in Brennan and Schwartz (1977). The methods of
Chernoff and Petkau (1984) also give a practical accurate numerical approximation to the American put value. For further results on the numerical valuation of American-style securities, see Ait-Sahlia and Lai (1996), Amin (1991), Amin and Khanna (1994), Andreasen and Gruenewald (1996), Barraquand and Pudet
(1996), Barraquand and Martineau (1995), Bjerksund and Stensland (1993),
Broadie and Detemple (1994), Broadie and Glasserman (1996, 1997, 1998),
Bunch and Johnson (1993), Büttler (1995), Büttler and Waldvogel (1996), Carr
(1994, 1998), Carr and Faguet (1994), Clarke and Parrott (1996), Dempster
(1994), Dempster and Hutton (1997), Gandhi, Kooros, and Salkin (1993), Gao,
Huang, and Subrahmanyam (1996), Ibanez and Zapatero (1999), Lamberton
(1997), Lee (1990), Longstaff and Schwartz (1998), Wu (1996), and Zhang (1993).

(K-L) The valuation of securities in terms of the fundamental solution also appears in the literature under such labels as path integrals, as in Dash (1989), or
Green's function, as in Beaglehole (1990) who calculates the fundamental solution G explicitly for the Cox-Ingersoll-Ross model (28), or Jamshidian (1991c).
The idea of using pricing semi-groups goes back at least to Garman (1985). See also Huang (1985a).

(M) The issue of matching parameters to the initial term structure apparently originated with Ho and Lee (1986) in their "binomial" model of the term structure. Subsequent work in this vein can be found in Black, Derman, and Toy (1990),
Dybvig (1988), Hull and White (1990a, 1994), and Jamshidian (1991c). Further references are given in the Notes to Chapter 7. The Newton-Raphson search, and other numerical optimization techniques, can be found in Luenberger (1984) and
Press, Flannery, Teukolsky, and Vetterling (1993).

Additional Topics: On numerical methods for valuation of interest-rate options, in addition to sources cited in Chapter 7, see Clewlow and Strickland (1996),
Clewlow, Pang, and Strickland (1997), Kunitomo and Takahashi (1996), Li,
Ritchken, and Sankarasubramanian (1995), Nielsen and Sandmann (1996), Scott

(1996a), and Topper (1997). For numerical methods for HJM models in particular, see Brace (1996), Chiarella and Hassan (1997), Heath, Jarrow, and Morton (1990, 1992a, b), and Ritchken and Trevor (1999).

On the numerical valuation of convertible debt, see Pikovsky and Shreve (1996a) and Zhu and Sun (1999).

An important topic that we have not treated is numerical solution of dynamic programming problems. Examples in the literature include Judd (1989), Tauchen and Hussey (1991), and Gagnon and Taylor (1990), who treat discrete-time models, and Fitzpatrick and Fleming (1991), Fleming and Soner (1993), Munk
(2000a), and Prigent (1994). A free-boundary problem that arises with investment under durability is treated by Hindy, Huang, and Zhu (1993, 1997).

Numerical computation of equilibria is treated by Kubler and Schmedders
(1997), Marcet (1993), and Marcet and Marshall (1994).

Fourier transform methods for derivative pricing are discussed in Chapter 8.
See also Carr and Madan (1998) and Rebonato and Cooper (1996). Applications of Malliavin calculus to asset pricing and hedging are addressed by Fournié, Lasry, Lebuchoux, Lions, and Touzi (1999).

Eydeland (1994a,b) provides alternative numerical methods for some of the derivative valuation problems addressed here. Bouleau and Lépingle (1994) is a general treatment of numerical methods for stochastic problems.

Appendixes

A

Finite-State Probability

Suppose Ω is a finite set. A tribe on Ω is a collection ℱ of subsets of Ω that includes the empty set ∅ and that satisfies the following two conditions:

(a) if B is in ℱ, then its complement {ω ∈ Ω : ω ∉ B} is also in ℱ;
(b) if A and B are in ℱ, their union A ∪ B is in ℱ.

A tribe ℱ is also known as an algebra or field, among other terms. When Ω is to be thought of as the states of the world, the elements of ℱ are called events. Conditions (a) and (b) allow for simple logical rules regarding the probabilities of events. Specifically, a probability measure is a function
P: ℱ → [0,1] satisfying P(∅) = 0, P(Ω) = 1, and, for any disjoint events A and B,

P(A ∪ B) = P(A) + P(B).

Under P, an event B has probability P(B). A pair (Ω, ℱ) consisting of a finite set Ω and a tribe ℱ on Ω is called a measurable space. With the addition of a probability measure P on ℱ, the triple (Ω, ℱ, P) is a called a probability space.

Fixing a measurable space (Ω, ℱ), a random variable is a function X :
Ω → ℝ with the following property: For any x ∈ ℝ, the set {ω ∈ Ω :
X(ω) = x} is in ℱ. Intuitively, X is a random variable if, for any possible outcome x, we will know whether X has this outcome from knowing the outcomes (true or false) of the events in ℱ. If X is a random variable with respect to (Ω, ℱ), we also say that X is ℱ-measurable.

Since Ω is finite, for any random variable X there are events
B₁,...,Bₖ and some a in ℝ such that X = a₁1_{B₁} + … + a_k1_{B_k}, wherethe indicator function 1_B for an event B is defined by 1_B(ω) = 1 for ω in B,

and 1_B(ω) = 0 otherwise. Given a probability measure P, the expectation of X is then defined by

E(X) = a₁ P(B₁) + … + aₙ P(Bₙ), (A.1)

merely the probability-weighted average of the outcomes.

For a probability space (Ω, ℱ, P) with Ω finite, if 𝒢 is a tribe on Ω that is contained by ℱ, then 𝒢 represents in some sense “less information,”
and is known as a subtribe of ℱ. For any ℱ-measurable random variable X, the conditional expectation of X given a subtribe 𝒢 of ℱ is defined as any
𝒢-measurable random variable Y, satisfying the property that E(XZ) =
E(YZ) for any 𝒢-measurable random variable Z. We let E(X | 𝒢) denote this conditional expectation. The law of iterated expectations, also called the tower property, states that if 𝒢 is a subtribe of another subtribe ℋ, then for any random variable X, E[E(X | ℋ) | 𝒢] = E(X | 𝒢).

If Z is a nonnegative random variable with E(Z) = 1, then we can create a new probability measure Q from the old probability measure P by defining Q(B) = E(1_B Z) for any event B. In this case, we write dQ/dP, and call Z the Radon-Nikodym derivative of Q with respect to P. It also follows that, for any random variable X,

E^Q(X) = E^P(ZX),

where E^Q denotes expectation under Q, and likewise for E^P. If Q(B) > 0 whenever P(B) > 0, and vice versa, then P and Q are said to be equivalent measures, they have the same events of probability zero.

If 𝒢 is a subtribe of ℱ and Q is equivalent to P, then

E^Q(Z | 𝒢) = E^P(Z dQ/dP | 𝒢), (A.2)

where dQ/dP = Z.

The tribe generated by a set 𝒵 of random variables is the smallest subtribe, often denoted σ(𝒵), with respect to which each random variable in
𝒵 is measurable. It is enough to think of σ(𝒵) as the set of events that can be ascertained as true or false by observing the outcomes of all of the random variables in 𝒵.

Suppose there are multiple periods given by a set 𝒥 of times such as
{0,1,…, T} or {0,1,…}. A filtration 𝔽 = (ℱ_t : t ∈ 𝒥) of subtribes of ℱ is usually given, as described in Section 2A. We always assume that ℱ_s ⊂ ℱ_t whenever s < t. Given 𝔽, a stopping time is a random variable τ taking values in 𝒥 ∪ {+∞} such that, for any time t in 𝒥, the event {ω ∈ Ω : τ(ω) ≤ t} is in ℱ_t. The event τ = +∞ is allowed for convenience. For example, if two processes X and Y are not the same, then the stopping time τ = inf{t : X_t ≠ Y_t} has a strictly positive probability of being finite valued, but may also have a strictly positive probability of being +∞. (We follow the usual convention that the infimum of the empty set is +∞.) A stopping time τ is nontrivial if P(τ = +∞) < 1. A martingale can be defined as in
Section 2A, or alternatively as any 𝔽-adapted process X such that, for any bounded stopping time τ, we have E(X_τ) = E(X_0).

The tribe ℱ_τ of events known at a finite-valued stopping time τ allows us to define the conditional expectation E_τ(·) = E(· | ℱ_τ). We define ℱ_τ to include any event A with the property that, for any time t, the event A ∩ {ω : τ(ω) ≤ t} is in ℱ_t.

A supermartingale is an adapted process X with the property that X_t ≥
E_t(X_s) for all t and s > t. It is known that a supermartingale X can be decomposed as the sum X = M − A, where M is a martingale and A is an increasing process with A_0 = 0, and such that, for each t < T, A_{t+1} is
ℱ_t-measurable. Likewise, a submartingale is an adapted process X such that −X is a supermartingale.

--

B

Separating Hyperplanes and Optimality

THIS APPENDIX REVIEWS some applications of the following result. Basic references are Rockafeller (1973) and Luenberger (1984).

Separating Hyperplane Theorem. Suppose that A and B are convex disjoint subsets of ℝⁿ. There is some nonzero linear functional F such that F(x) < F(y) for each x in A and y in B. Moreover, if x is in the interior of A or y is in the interior of B, then F(x) < F(y). Furthermore, if A is closed and B is compact, then F can be chosen so that F(x) < F(y) for all x in A and y in B.

Our first application of the Separating Hyperplane Theorem is a special case for separation of cones that is applied in Theorem 1A.

Linear Separation of Cones. Suppose M and K are closed convex cones in ℝⁿ that intersect precisely at zero. If K does not contain a linear subspace other than {0}, then there is a nonzero linear functional F such that F(x) < F(y) for each x in M and each nonzero y in K.

Proof: We can assume without loss of generality that K ≠ {0}. Let C be the convex hull (that is, the set of all convex combinations) of {y ∈ K : ‖y‖ = 1}.

As C is a compact subset of K, and K contains no lines, we know that
C and M are disjoint. By the Separating Hyperplane Theorem, there is a nonzero linear functional F such that F(x) < F(y) for all x in M and y in
C. As 0 is in M, we have F(y) > 0 for all y in C. For any nonzero element z of K, we have z = λy for some y in C and some strictly positive scalar λ.
The result follows. □

‘This proof, due to Lasse Pedersen, is simpler than that of the second edition.

--

Our next application of the Separating Hyperplane Theorem is the
Saddle Point Theorem for optimality. A concave program is a triple (U, X, g)
of the form

sup U(x) subject to g(x) ≤ 0, (B.1)
x∈X

where X is a convex subset of some vector space, U : X → ℝ is concave, and g : X → ℝᵐ is convex for some integer m. The Lagrangian for
(U, X, g) is the function L : X × ℝᵐ → ℝ defined by L(x, λ) = U(x) − λ⁺ g(x). A pair (x₀, λ₀) in X × ℝᵐ is a saddle point of L if, for all (x, λ)
in X × ℝᵐ, we have L(x, λ₀) ≤ L(x₀, λ₀) ≤ L(x₀, λ). If (x₀, λ₀) is a saddle point, we often term λ₀ a Lagrange multiplier for problem (B.1). The following version of the conditions for optimality is proved with the Separating Hyperplane Theorem. The existence of some x in X with g(x) < 0 is known as the Slater condition.

Saddle Point Theorem. Let (U, X, g) be a concave program.

I. (Necessity) Suppose the Slater condition is satisfied. If x₀ solves (B.1), then there exists λ₀ ∈ ℝᵐ such that (x₀, λ₀) is a saddle point of the Lagrangian
L. Moreover, λ₀⁺ g(x₀) = 0, which is called the complementary slackness condition.

II. (Sufficiency) If (x₀, λ₀) is a saddle point of L, then x₀ solves (B.1).

Proof: For the first part of the result, let L = ℝ × ℝᵐ, let C(r,z) = {x ∈ X : r ≤ U(x), z ≥ λ⁺ g(x)}, and let
A = {(r,z) : C(r,z) ≠ ∅} and B = {(r,z) : r > U(x), z < 0}.

Both A and B are convex. By the fact that x₀ solves (B.1), the sets A and
B are disjoint. By the Separating Hyperplane Theorem, there is a linear functional F : L → ℝ such that F(v) < F(w) for each v in A and w in
B. It follows, for any v in A and w in the closure of B, that F(v) ≤ F(w).
There is some scalar a and λ in ℝᵐ such that, for any (r,z) in L, we have F(r,z) = ar + λ⁺ z. Using the Slater condition, we can check that a > 0 and λ ≤ 0. Let λ₀ = −λ/a. It follows, using the fact that [U(x₀), 0]

is in both A and the closure of B, that (x₀, λ₀) is a saddle point, and that complementary slackness holds.
The second part of the result is easy to show. □

Now we turn to first-order conditions for optimality. Consider

sup U(x), (B.2)
x∈X

where X is a convex subset of a vector space L and U : X → ℝ is some function. We are interested in necessary and sufficient conditions for x* to solve (B.2). For x ∈ X, let

Y(x, y) = sup{α ∈ [0,1) : x+αy ∈ X, α ∈ [0,1]

and

F(x) = {y ∈ L : Y(x, y) > 0},

the set of feasible directions from x. The derivative of U at some x in X in the direction y ∈ F(x), if it exists, is defined as the limit

U(x + αy) − U(x)

∂U(x; y) = lim  (B.3)
α↓0            α

This is sometimes known as the directional or Gateaux derivative. If y ↦
∂U(x; y) defines a linear function on F(x), this function is called the gradient of U at x, and is denoted ∇U(x). In that case, we write ∇U(x; y) =∂U (x; y) for the value of ∇U(x) at y. If U: ℝⁿ → ℝ is a continuously differentiable function, then the gradient ∇U(x) exists at any x and ∇U(x; y) = ∇U(x) ⋅ y, where ∇U(x) is the vector of partial derivatives of U at x.

Suppose x* solves (B.2) and ∇U(x*) exists. Then ∇U(x*; y) < 0 for all y in F(x*), for if not, there is some feasible direction y with ∇U(x*; y) > 0, in which case there is some α > 0 with U(x* + αy) − U(x*) > 0, which contradicts the optimality of x*. If F(x*) is the entire vector space L, it follows that ∇U(x*) = 0 is necessary for the optimality of x*, for if ∇U(x*; y) < 0, then −y is a feasible direction of strict improvement.

If U is concave, ∇U(x*) exists, and F(x*) = L, then it is both necessary and sufficient for the optimality of x* that ∇U(x*) = 0. Necessity has been shown. For sufficiency, concavity of U implies that for any x and y ∈ F,

U(y) − U(x) ≤ ∇U(x; y). (B.4)

Taking x = x*, we have U(y) < U(x*) for all y. There are extensions of these results to the case of nondifferentiable U.

C

# Probability

THIS APPENDIX EXTENDS the definitions of Appendix A to handle probability spaces with possibly infinitely many distinct events. We also add some useful general results, such as the Dominated Convergence Theorem, the Central Limit Theorem, and Fubini’s Theorem. A standard reference is Billingsley (1986).

Given a set Ω of states, a tribe on Ω is a collection ℱ of subsets of Ω that includes the empty set ∅ and that satisfies the following two conditions:

(a) if B is in ℱ, then its complement {ω ∈ Ω : ω ∉ B} is also in ℱ;
(b) for any sequence {B₁, B₂,...} in ℱ, the union B₁ ∪ B₂ ∪ … is in ℱ.

A tribe is also known in this general context as a σ-algebra or σ-field. For any collection 𝒮 of subsets of Ω, the tribe generated by 𝒮 is the intersection of all tribes containing 𝒮. An important example is to take Ω = ℝⁿ and to let ℱ be the tribe generated by the open sets of ℝⁿ. In this case, ℱ is known as the Borel tribe on ℝⁿ, and is denoted ℬ(ℝⁿ).

Suppose Ω is a set with tribe ℱ. A random variable is a function X : Ω → ℝ with the following property: For any set A in the Borel tribe ℬ(ℝ), the set {ω ∈ Ω : X(ω) ∈ A} is in ℱ. A probability measure is a function P : ℱ → [0, 1] satisfying P(∅) = 0, P(Ω) = 1, and, for any sequence B₁, B₂,... of disjoint events,

P(B₁ ∪ B₂ ∪ ⋯) = Σₙ₌₁ P(Bₙ).

The triple (Ω, ℱ, P) is a probability space.
An event B is said to be almost sure if P(B) = 1. For example, “X = Y almost surely” means, in formal notation, that P({ω ∈ Ω : X(ω) = Y(ω)}) = 1. We sometimes write instead, more informally, that “P(X = Y) = 1.”

330 Appendix C

It is our practice throughout to take “X = Y” to mean merely that X = Y almost surely, but the phrase “almost surely” is sometimes added for emphasis.

Given a probability space (Ω, ℱ, P), a null set is a subset of an event of zero probability. In order to assign zero probability to null sets, the probability space can be completed, which means that we can replace ℱ with the tribe ℱ⁻ generated by the union of ℱ and the set of all null sets. The probability measure P then extends uniquely to a probability measure P⁻ on (Ω, ℱ⁻) with the property that P⁻(A) = P(A) for all A in ℱ and P⁻(A) = 0 for any null set A. The space (Ω, ℱ⁻, P⁻) is called the completion of (Ω, ℱ, P).

Suppose X is a random variable that can be written as a linear combination, X = a₁I_{B₁} + ⋯ + aₙI_{Bₙ}, of indicator functions. In this case, X is called simple. As in the finite-state case, the expectation of X given a probability measure P on (Ω, ℱ) is defined by

E(X) = a₁ P(B₁) + ⋯ + aₙP(Bₙ),

merely the probability-weighted average of the outcomes. If X is not necessarily simple, but is a nonnegative random variable, then the expectation of X is defined as

E(X) = sup { E(Y) subject to Y ≤ X }, (C.1)
Y∈ℱ

where ℱ is the set of simple random variables. More generally, any random variable X may be written as X = X⁺ − X⁻, where X⁺ = max(X, 0) and X⁻ = max(−X, 0); that is, X is the difference between its positive and negative parts. If both E(X⁺) and E(X⁻) are finite, then X is said to be integrable, and its expectation is defined by

E(X) = E(X⁺) − E(X⁻), (C.2)

which coincides with the definition for simple random variables when X is itself simple. If X⁺ is integrable and X⁻ is not, we define E(X) = −∞, and symmetrically define E(X) = +∞ when X⁻ is integrable and X⁺ is not.

Fixing a probability space (Ω, ℱ, P), a sequence {Xₙ} of random variables converges in distribution to a random variable X if, for any bounded continuous f : ℝ → ℝ, we have E[f(Xₙ)] → E[f(X)]. The sequence {Xₙ} converges in probability to X if, for all ε > 0, P(|Xₙ − X| ≥ ε) → 0. The sequence {Xₙ} converges almost surely to X if there is an event B of

probability 1 such that Xₙ(ω) → X(ω) for all ω in B. The definition of convergence in distribution extends as given to the case of Xₙ, defined on a (possibly different) probability space (Ωₙ, ℱₙ, Pₙ) for each n.

Dominated Convergence Theorem. Suppose {Xₙ} is a sequence of random variables on a probability space with |Xₙ| ≤ Y for all n, where Y is a random variable with E(|Y|) < ∞. Suppose, almost surely, or in probability, or in distribution, that Xₙ converges to X. Then E(Xₙ) → E(X).

Convergence almost surely implies convergence in probability, which in turn implies convergence in distribution, so we could have stated the Dominated Convergence Theorem just for convergence in distribution and had the same result.

A sequence {Xₙ} of random variables on a given probability space is independently distributed if, for any finite subset {X_{n₁}, ... , X_{n_k}} and any bounded measurable functions f_j : ℝ → ℝ, 1 ≤ j ≤ k, we have

E[∏ⱼ₌₁ᵏ f_j(X_{nⱼ})] = ∏ⱼ₌₁ᵏ E[f_j(X_{nⱼ})].

A sequence {Xₙ} of random variables on a given probability space is uniformly integrable if

lim sup E(Y_{n,a}) = 0, a→∞ n

where Y_{n,a}(ω) = |Xₙ(ω)| if |Xₙ(ω)| > a and otherwise Y_{n,a}(ω) = 0.
We next describe a version of the Central Limit Theorem. For this, we define

Yₙₖ = 1/√n Zₙₖ, k = 1, ..., k(n),

with k(n) → ∞, to be a triangular array if, for each n, Y_{n1}, ..., Y_{n k(n)} are independently distributed random variables on some probability space.
For any constant ε > 0, let Uₙ(ε) denote the “ε-truncated” triangular array defined by Uₙₖ(ε) = 0 for |Yₙₖ| < ε and Uₙₖ(ε) = Yₙₖ for |Yₙₖ| ≥ ε. The array {Yₙₖ} satisfies the Lindeberg-Feller condition if, for any ε > 0,

lim var[Σₖ Uₙₖ(ε)] = 0.
n→∞

The Lindeberg-Feller Central Limit Theorem. Suppose {Yₙₖ} is a triangular array of random variables, all with zero expectations, satisfying the Lindeberg-Feller condition. For each n, let Zₙ = Y_{n1} + ⋯ + Y_{n k(n)} and let sₙ² = var(Zₙ). If sₙ² → σ² > 0,

then Zₙ converges in distribution to a normal random variable with mean zero and variance σ².

332 Appendix C

For any integrable random variable X, the conditional expectation of X given a subtribe 𝒢 of ℱ is denoted E(X | 𝒢), and is defined as any 𝒢-measurable random variable Z with the property E(XZ) = E(YZ) for any 𝒢-measurable random variable Z such that XZ is integrable. The existence of this conditional expectation is assured, but we do not show that here. The law of iterated expectations applies as in the finite-state case.

As in the finite-state setting, Q and P are equivalent probability measures on (Ω, ℱ) if, for any event A, P(A) = 0 if and only if Q(A) = 0. In this case, there is always a strictly positive random variable ξ called the Radon-Nikodym derivative of Q with respect to P, with the following property: If Z is such that E_P(|Z|) < ∞, then E_Q(Z) = E_P(ξZ). Under the same assumptions, if 𝒢 is a subtribe of ℱ, then

E_Q(Z | 𝒢) = E_P(ξZ | 𝒢). (C.3)

It is common to denote ξ by dQ/dP.

If there are multiple periods, we fix a set of times denoted J, usually with J = {0, 1, ..., T}, or J = {0, 1, ...}, or J = [0, T], or J = [0, ∞). A filtration ℱ = {ℱₜ : t ∈ J} of subtribes of ℱ is usually given, as in theProposition. Assume θ satisfies Novikov's condition, then a martingale ε^θ is defined by $$
\varepsilon^{\theta}_t = \exp\left( \int_0^t \theta_s dB_s - \frac{1}{2} \int_0^t \theta_s^2 ds \right), \quad t \in [0, T].
$$
Suppose θ satisfies Novikov’s condition. Because ε^θ is a martingale and $$ \varepsilon^{\theta}_0 = 1,
$$ we know that \( E(\varepsilon^{\theta}) = 1 \). Since ε^θ is strictly positive, we saw in
Appendix C that an equivalent probability measure \( Q(\theta) \) can be defined by $$ \frac{dQ(\theta)}{dP} = \varepsilon^{\theta}.
$$
It is sometimes useful to exploit Itô's Lemma and write \( d\varepsilon^{\theta} = \varepsilon^{\theta} \theta \cdot dB \).

For any local martingales \( Y \) and \( Z \), there is a unique continuous adapted process, denoted \( \langle Y, Z \rangle \), such that \( \langle Y, Z \rangle_0 = 0 \) and \( YZ - \langle Y, Z \rangle \)
is a local martingale. One sometimes calls \( \langle X,Y \rangle \) the sharp-brackets process. Evidently, by the Martingale Representation Theorem and Itô’s Formula, for some \( \mathbb{R}^d \)-valued adapted processes \( \sigma^Y \) and \( \sigma^Z \), we have \( dY_t = \sigma^Y(t) dB_t \), \( dZ_t = \sigma^Z(t) dB_t \), and \( d\langle Y, Z \rangle_t = \sigma^Y(t) \cdot \sigma^Z(t) dt \).

Next, we state Lévy’s characterization of Brownian motion. The result actually applies for any filtration \( (\mathcal{F}_t) \) satisfying the usual conditions, stated in Appendix F, as stated in Revuz and Yor (1991).

**Lévy’s Characterization Theorem.** Suppose \( X \) is an \( \mathbb{R}^d \)-valued adapted process.
Then \( X \) is a standard Brownian motion in \( \mathbb{R}^d \) if and only if \( X_0 = 0 \) and \( X \) is a continuous local martingale in \( \mathbb{R}^d \) with \( \langle X^i, X^j \rangle_t = \delta_{ij} t \), where \( \delta_{ii} = 1 \) and, for distinct \( i \) and \( j \), \( \delta_{ij} = 0 \).

**Girsanov’s Theorem.** Given \( \theta \in (\mathcal{H})^d \), suppose that \( \varepsilon^{\theta} \) is a martingale.
(Novikov’s condition suffices.) Then a standard Brownian motion \( B^{\theta} \) that is a martingale under \( Q(\theta) \) is defined by $$
B^{\theta}_t = B_t - \int_0^t \theta_s ds, \quad 0 < t < T. \quad \text{(D.4)}
$$

Moreover, \( B^{\theta} \) has the martingale representation property under \( Q(\theta) \). That is, for any local \( Q(\theta) \)-martingale \( M \), there is some \( \phi \) in \( (\mathcal{H})^d \) such that $$
M_t = M_0 + \int_0^t \phi_s \cdot dB^{\theta}_s, \quad t < T.
$$
The martingale representation aspect of Girsanov’s Theorem is not usually emphasized, but is particularly useful in finance applications. By direct calculation, Girsanov’s Theorem has the following useful corollary.

**Corollary.** Let \( X \) be an Itô process in \( \mathbb{R}^d \) of the form
$$ dX_t = \mu_t dt + \sigma_t dB_t, \quad 0 < t < T.
$$
Suppose \( v = (v^1, \dots, v^d) \) is a vector of processes in \( \mathcal{H} \) such that there exists some \( \theta \) in \( (\mathcal{H})^d \) satisfying $$
\theta_t = \frac{\mu_t}{\sigma_t} - v_t, \quad 0 < t < T.
$$
If \( \varepsilon^{\theta} \) is a martingale (Novikov’s condition suffices), then \( X \) is also an Itô process with respect to \( (\Omega, \mathcal{F}, F, Q(\theta)) \), and
$$ dX_t = v_t dt + \sigma_t dB^{\theta}_t, \quad 0 < t < T.
$$
In short, Girsanov’s Theorem gives us a way to adjust probability assessments so that a given Itô process can be rewritten as an Itô process with almost arbitrary drift.

For any probability measure \( Q \) equivalent to \( P \), we can define a martingale \( M \) by $$ M_t = \frac{dQ}{dP} \bigg|_{\mathcal{F}_t}.
$$
The Martingale Representation Theorem implies that there is some \( \phi \) in
\( (\mathcal{H})^d \) such that \( dM_t = \phi_t \cdot dB_t \). In particular, \( M \) is a continuous process.
Since \( Q \) is equivalent to \( P \), it can be shown that \( M \) is a strictly positive process, and we can define \( \theta \) in \( (\mathcal{H})^d \) by \( \theta_t = -\phi_t / M_t \). It follows that \( M = \varepsilon^{\theta} \), and that \( Q = Q(\theta) \). Given the unique decomposition property of Itô processes, this implies the following convenient result, showing that the diffusion of an Itô process does not change with a change to an equivalent probability measure. (The drift process can of course change, as we have just seen.)

**Diffusion Invariance Principle.** Let \( Q \) be a probability measure equivalent to \( P \).
There is a standard Brownian motion \( B^Q \) in \( \mathbb{R}^d \) under \( Q \) with the martingale representation property under \( Q \). Let \( X \) be an Itô process (under \( P \)) with \( dX_t = \mu_t dt + \sigma_t dB_t \). Then \( X \) is also an Itô process under \( Q \), and \( dX_t = \tilde{\mu}(t) dt + \sigma_t dB^Q_t \), where \( \tilde{\mu} \) is the drift of \( X \) under \( Q \).

Finally, we review a version of Fubini’s Theorem for stochastic integrals that was used in deriving the Heath-Jarrow-Morton model for forward rates. Suppose \( X \) is an Itô process and, for some bounded real interval
\( [a, b] \), \( H : [a, b] \times \Omega \times [0, T] \to \mathbb{R} \) is jointly measurable and, for each \( u \) in
\( [a, b] \), \( H^u = H(u, \cdot, \cdot) \) defines an adapted process such that the stochastic integral \( \int H^u \cdot dX \) exists. Let \( h(a, t) = \left[ \int_a^b H^u(u, \cdot, t) du \right]^{1/2} \), and suppose that the stochastic integral \( \int h \cdot dX \) exists. Letting \( g(w, t) = \int_a^b H^u(w, t) du \), we get a result analogous to Fubini’s Theorem in its classical form of
Appendix C, namely that, for each time \( T \), \( \int_0^T \int_a^b H^u \cdot dX_t du = \int_0^T g_t \cdot dX_t \).
This follows from Theorem 46, page 160, of Protter (1990).

--
**E**
**SDE, PDE, and Feynman-Kac**

THIS APPENDIX TREATS the existence of solutions to stochastic differential equations (SDEs) and shows how SDEs can be used to represent solutions to partial differential equations (PDEs) of the parabolic type. Standard references include Karatzas and Shreve (1988).

As usual, a standard Brownian motion \( B \) in \( \mathbb{R}^d \) is given on some probability space \( (\Omega, \mathcal{F}, P) \), along with the standard filtration \( \mathcal{F} \) of \( B \), as defined in Appendix D. An SDE is an expression of the form
$$ dX_t = \mu(X_t, t) dt + \sigma(X_t, t) dB_t \quad \text{(E.1)}
$$ where \( \mu: \mathbb{R}^d \times [0, \infty) \to \mathbb{R}^d \) and \( \sigma: \mathbb{R}^d \times [0, \infty) \to \mathbb{R}^{d \times d} \) are given functions. We are interested in conditions on \( \mu \) and \( \sigma \) under which, for each \( x \)
in \( \mathbb{R}^d \), there is a unique Itô process \( X \) satisfying (E.1) with \( X_0 = x \). In this case, we say that \( X \) solves (E.1) with initial condition \( x \). A process such as
\( X \) is often called a diffusion, although there is no generally accepted definition for “diffusion.” By saying “unique,” we mean as usual that any other
Itô process with the same properties is equal to \( X \) almost everywhere. A unique solution in this sense is sometimes called a strong solution. We will have no need for what is known as a weak solution.

Sufficient conditions for a solution to (E.1) are Lipschitz and growth conditions on \( \mu \) and \( \sigma \). In order to explain these, we first define a norm on matrices by letting \( \| A \| = [\text{tr}(AA^T)]^{1/2} \) for any matrix \( A \), where “tr(·)”
denotes trace. (This coincides with the usual Euclidean norm when \( A \) has one row or column.) We then say that \( \sigma \) satisfies a Lipschitz condition in
\( x \) if there is a constant \( k \) such that, for any \( x \) and \( y \) in \( \mathbb{R}^d \) and any time \( t \), $$
\| \sigma(x, t) - \sigma(y, t) \| \leq k \| x - y \|. \quad \text{(E.2)}
$$
Similarly, \( \sigma \) satisfies a growth condition in \( x \) if there is a constant \( k \) such that, for any \( x \) in \( \mathbb{R}^d \) and any time \( t \), $$
\| \sigma(x, t) \| \leq k(1 + \| x \|). \quad \text{(E.3)}
$$
Note that these conditions apply uniformly in \( t \), in that the constants apply for all \( t \) simultaneously. The same conditions (E.2) and (E.3), substituting
\( \mu \) for \( \sigma \), define Lipschitz and growth conditions, respectively, on \( \mu \).

**SDE Proposition.** Suppose \( \mu \) and \( \sigma \) are measurable and satisfy Lipschitz and growth conditions in \( x \). Then, for each \( x \) in \( \mathbb{R}^d \), there is a unique Itô process \( X \)
in \( \mathbb{R}^d \) satisfying the SDE (E.1) with initial condition \( x \). Moreover, \( X \) is a Markov process, and for each time \( t \) there is a constant \( C \) such that $$
E(\| X_t \|^p) \leq C e^{Ct} + \int_0^t E(\| X_s \|^p) ds.
$$
The conclusion that \( X \) is a Markov process can be strengthened to the conclusion that \( X \) is a strong Markov process, a property that we do not define here. One can weaken somewhat the Lipschitz conditions for solutions to (E.1). We say that \( \sigma \) is locally Lipschitz in \( x \) if, for each positive constant \( K \), there is a constant \( k \) such that (E.2) is satisfied for all \( t \) and for all \( x \) and \( y \) bounded in norm by \( K \).

**SDE Theorem.** Suppose \( \mu \) and \( \sigma \) are measurable, satisfy growth conditions in \( x \), and are locally Lipschitz in \( x \). Then, for each \( x \) in \( \mathbb{R}^d \), there is a unique Itô process \( X \) in \( \mathbb{R}^d \) satisfying the SDE (E.1) with initial condition \( x \). Moreover, \( X \) is a Markov process. If, in addition, \( \mu \) and \( \sigma \) are continuous functions, then \( X \) is a finite-variance process.

Even these weaker conditions do not cover the case of “square root”
diffusions of the type used in the Cox-Ingersoll-Ross model, and more general “affine” processes of the type appearing in Chapters 7 and 8. For these special cases, we can rely on the following result for the one-dimensional case ( \( N = d = 1 \) ), reported in Karatzas and Shreve (1988), page 291. It is enough that \( \mu \) is continuous and satisfies a Lipschitz condition in \( x \), and that \( \sigma \) is continuous with the property that $$ | \sigma(x) - \sigma(y) | \leq \rho | x - y |,
$$for all \(x\) and \(y\) and all \(t\), where \(p: [0, \infty) \rightarrow [0,\infty)\) is a strictly increasing function with \(p(0) = 0\) such that for any \(\varepsilon > 0\),

\[ \int_{(0,\varepsilon)} p^2(x) \, dx = +\infty.
\]

342 Appendix E

It is enough to take \(p(x) = \sqrt{x}\), which covers the CIR model (taking \(\mu(x) = 0\) for \(x < 0\)). While even these weak conditions can be further weakened, it should be noted that there are counterexamples to the uniqueness of solutions for the case \(a(x) = |x|^\alpha\) for \(\alpha < 1/2\).

These SDE existence results can be gleaned from such sources as Ikeda and Watanabe (1981) or Karatzas and Shreve (1988). The conditions of these results also imply that for any given time \(T\) and any \(x\) in \(\mathbb{R}^N\), there is a unique Itô process \(X\) satisfying (E.1) for \(t \geq T\) with \(X_T = x\). In this case, we say that \(X\) solves (E.1) with initial condition \(x\) at time \(T\).

An important special case of the SDE is the linear stochastic differential equation

\[ dX_t = [a(t)X_t + b(t)] \, dt + c(t) \, dB_t, \qquad (E.4)
\]

where \(a: [0,\infty) \rightarrow \mathbb{R}^{N \times N}\), \(b: [0,\infty) \rightarrow \mathbb{R}^N\), and \(c: [0,\infty) \rightarrow \mathbb{R}^{N \times M}\) are continuous. We can express the solution to a linear SDE quite explicitly. First, let \(\Phi\) denote the solution of the ordinary differential equation

\[
\frac{d\Phi(t)}{dt} = a(t)\Phi(t), \quad \Phi(0) = I_N.
\]

It can be shown that for all \(t\), the matrix \(\Phi(t)\) is nonsingular, and the solution of (E.4) is

\[
X_t = \Phi(t) \left( x + \int_0^t \Phi^{-1}(s)b(s) \, ds + \int_0^t \Phi^{-1}(s)c(s) \, dB_s \right), \quad t \geq 0.
\]

In particular, \(X\) is Gaussian, meaning that for any finite times \(t_1 < \ldots < t_k\), \(\{X(t_1), \ldots, X(t_k)\}\) has a joint normal distribution. For any \(t\), the mean vector \(m(t)\) and covariance matrix \(V(t)\) for \(X_t\) are given as solutions to the ordinary differential equations

\[ \begin{aligned}
\frac{dm(t)}{dt} &= a(t)m(t) + b(t), \quad m(0) = X_0, \\
\frac{dV(t)}{dt} &= a(t)V(t) + V(t)a(t)^\top + c(t)c(t)^\top, \quad V(0) = 0.
\end{aligned}
\]

Further details, and generalizations, can be found in Karatzas and Shreve (1988).

We next consider the Cauchy problem, for given \(T > 0\): Find \(f \in C^{2,1}(\mathbb{R}^N \times [0, T))\) solving

\[
\frac{\partial f}{\partial t}(x, t) + Lf(x, t) + h(x, t) = 0, \quad (x, t) \in \mathbb{R}^N \times [0, T), \tag{E.5}
\]

with the boundary condition

\[ f(x, T) = g(x), \quad x \in \mathbb{R}^N, \tag{E.6}
\]

where

\[
Lf(x, t) = \sum_{i=1}^N \mu_i(x, t) \frac{\partial f}{\partial x_i}(x, t) + \frac{1}{2} \sum_{i,j=1}^N [\sigma\sigma^\top]_{ij}(x, t) \frac{\partial^2 f}{\partial x_i \partial x_j}(x, t), \tag{E.7}
\]

and where \(\mu: \mathbb{R}^N \times [0, T] \rightarrow \mathbb{R}^N\), \(h: \mathbb{R}^N \times [0, T] \rightarrow \mathbb{R}\), \(g: \mathbb{R}^N \rightarrow \mathbb{R}\), and \(\sigma: \mathbb{R}^N \times [0, T] \rightarrow \mathbb{R}^{N \times M}\).
The Feynman-Kac solution to (E.5)—(E.6), should it exist, is given by

\[ f(x, t) = \mathbb{E}_t \left[ \int_t^T h(X_s, s) \, ds + g(X_T) \right], \tag{E.8}
\]

where

\[
\mathbb{E}_t[\cdot] \text{ denotes expectation conditional on } X_t = x, \]

and where \(\mathbb{E}_{t,x}\) indicates that \(X\) is assumed to solve the SDE (E.1) with initial condition \(x\) at time \(t\). The term “Feynman-Kac” is widely considered a misnomer in that it originally referred to the probabilistic representation of the solution to a narrower class of parabolic equations than the Cauchy problem. Typically, (E.8) would be called a probabilistic solution of the PDE (E.5)-(E.6).

Momentarily putting aside the delicate issue of existence of solutions to the Cauchy problem, the Feynman-Kac representation of a given solution is itself not difficult to verify under technical assumptions. In order to see this, suppose that \(X\) solves (E.1) and that \(f\) is a solution to the Cauchy problem. For an arbitrary \((x, t)\) in \(\mathbb{R}^N \times [0, T]\), let \(Y\) be the Itô process defined by \(Y_s = f(X_s, s)\) for \(s \in [t, T]\) and

\[ Y_s = f(x, t), \quad s \leq t, \]

where \(X\) solves (E.1) with initial condition \(x\) at time \(t\). By Itô’s Formula,

\[ \begin{aligned}
Y_T &= Y_t + \int_t^T \left( \frac{\partial f}{\partial s}(X_s, s) + Lf(X_s, s) \right) ds \\
&\quad + \int_t^T \nabla f(X_s, s) \sigma(X_s, s) \, dB_s.
\end{aligned}
\]

344 Appendix E

Taking expectations through each side, rearranging, and assuming enough technical conditions for integrability and (from Proposition 5.8) for the integral with respect to \(B\) to be a martingale, we have

\[ f(x, t) = \mathbb{E}_{t,x} \left[ g(X_T) - \int_t^T \left( Lf(X_s, s) - \frac{\partial f}{\partial s}(X_s, s) \right) ds \right], \]

from which (E.8) follows with substitution of (E.5) and (E.6). Sufficient technical conditions are

(a) all of \(\mu, \sigma, g, h\), and \(f\) are continuous;
(b) the solution \(f\) satisfies a polynomial growth condition in \(x\), meaning that for some positive constants \(M\) and \(D\),

\[
|f(x, t)| \leq M(1 + |x|), \quad (x, t) \in \mathbb{R}^N \times [0, T];
\]

(c) \(g\) and \(h\) are each either nonnegative or satisfy a polynomial growth condition in \(x\);

(d) \(r\) is nonnegative; and

(e) \(\mu\) and \(\sigma\) satisfy Lipschitz and growth conditions in \(x\).

We state this more formally.

**Proposition.** Suppose conditions (a)—(e) above are satisfied and that \(f\) solves (E.5)-(E.6). Then (E.5)—(E.6) is solved by (E.8). There is no other solution to (E.5)-(E.6) that satisfies a polynomial growth condition.

A proof is found in Karatzas and Shreve (1988), page 366. Reducing the PDE solution to an expectation in this fashion can sometimes ease the computation of the solution, as is the case for the Black-Scholes formula. The expectation can also be used as the basis for a numerical solution by Monte Carlo methods, a topic considered in Chapter 12. The Feynman-Kac approach can also be applied to other types of parabolic and elliptic PDEs.

The previous proposition does not resolve whether or not a solution to the PDE actually exists. For this, stronger technical conditions are typically imposed. Different sets of conditions are available in the literature; we will give some of these from different sources. A function \(F: \mathbb{R}^N \rightarrow \mathbb{R}^N\) is Hölder continuous if there is some \(\alpha \in (0, 1]\) such that

\[
\sup_{x \neq y} \frac{\|F(x) - F(y)\|}{\|x - y\|^\alpha} < \infty.
\]

A function has a property (such as Hölder continuity) locally if it has the property when restricted to any compact subset of its domain.

**Condition 1.** The functions \(\mu, \sigma, g, h\), and \(r\) are all continuous and

(a) \(\mu\) and \(\sigma\) are bounded and locally Lipschitz in \((x, t)\);

(b) \(\sigma\) is Hölder continuous in \(x\), uniformly in \(t\);

(c) \(r\) is bounded and, locally, \(r\) is Hölder continuous in \(x\), uniformly in \(t\);

(d) \(h\) is Hölder continuous in \(x\), uniformly in \(t\), and satisfies a polynomial growth condition in \(x\);

(e) \(a = \sigma\sigma^\top\) is uniformly parabolic, in that there is some scalar \(E > 0\) such that the eigenvalues of \(a(x, t)\) are larger than \(E\) for all \((x, t) \in \mathbb{R}^N \times [0, T]\); and

(f) \(g\) satisfies a polynomial growth condition.

We can substitute strong smoothness conditions for some of the stringent bounding and uniform ellipticity properties of Condition 1.

**Condition 2.** All of \(\mu, \sigma, g, r\), and \(h\) satisfy a Lipschitz condition in \(x\), and \(r\) is nonnegative. All of \(\frac{\partial \mu}{\partial t}, \frac{\partial \sigma}{\partial t}, \frac{\partial r}{\partial t}, \frac{\partial h}{\partial t}, \frac{\partial^2 \mu}{\partial x_i \partial x_j}, \frac{\partial^2 \sigma}{\partial x_i \partial x_j}, \frac{\partial^2 r}{\partial x_i \partial x_j}, \frac{\partial^2 h}{\partial x_i \partial x_j}\) exist, are continuous, and satisfy a growth condition in \(x\).

**Theorem.** Under Condition 1 or Condition 2, there is a unique solution of (E.5)-(E.6) that satisfies a polynomial growth condition in \(x\), and this solution is given by (E.8).

Condition 1 is from Friedman (1975), while Condition 2 is a special case from Krylov (1980). Kuwano (1994) offers improvements on Krylov’s result. Unfortunately, neither Condition 1 nor Condition 2 includes the exact case of the Black-Scholes option-pricing formula, simply because the option payoff is not differentiable in the stock price.

Under technical conditions on \(\mu, \sigma\), and \(r\), there is a function \(G: \mathbb{R}^N \times [0, T] \times \mathbb{R}^N \times [0, T] \rightarrow \mathbb{R}\), called the fundamental solution of (E.5)-(E.6), or sometimes the Green’s function, that has the following useful properties:

(a) For any \((x_0, t_0) \in \mathbb{R}^N \times [0, T)\), the function \(v\) defined by \(v(x, t) = G(x_0, t_0, x, t)\) is in \(C^{2,1}(\mathbb{R}^N \times (t_0, T])\) and solves the PDE

\[
\frac{\partial v}{\partial t}(x, t) - Lv(x, t) = 0, \quad (x,t) \in \mathbb{R}^N \times (t_0, T], \tag{E.9}
\]

where

\[
Lv(x, t) = \frac{1}{2} \sum_{i,j=1}^N [\sigma\sigma^\top]_{ij}(x, t) \frac{\partial^2 v}{\partial x_i \partial x_j}(x, t) + \sum_{i=1}^N \mu_i(x, t) \frac{\partial v}{\partial x_i}(x, t) - r(x, t)v(x, t).
\]

346 Appendix E

where \(a(x, t) = \sigma(x, t)\sigma(x, t)^\top\). The PDE (E.9) is sometimes called the Fokker-Planck equation, or the forward Kolmogorov equation, distinguishing it from the backward Kolmogorov equation (E.5)-(E.6).

(b) Under technical conditions on \(g\) and \(h\), the solution to (E.5)-(E.6) is given by

\[ f(x_0, t_0) = \int_{t_0}^T \int_{\mathbb{R}^N} G(x_0, t_0, x, t) h(x, t) \, dx \, dt \\
+ \int_{\mathbb{R}^N} G(x_0, t_0, x, T) g(x) \, dx. \tag{E.10}
\]

A sufficient set of technical conditions, as well as boundary conditions for (E.9), are given by Friedman (1964) and Friedman (1975). Knowledge of the fundamental solution \(G\) is valuable since particular solutions of the PDE (E.5)-(E.6) can be computed from (E.10) for each of a number of different cases for \(g\) and \(h\). In the case of \(N = 1\), numerical solution of \(G\)is briefly discussed in Chapter 12.

Further work on probabilistic solutions of PDEs has been done by Freidlin (1985).

F

Itô’s Formula with Jumps

THIS APPENDIX DEVELOPS Itô’s Formula in somewhat more generality, allowing for certain simple settings with jumps. A standard source, with further generality, is Protter (1990).

We first establish some preliminary definitions. We fix a complete probability space (Ω, F, P) and a filtration {F_t : t ≥ 0} satisfying the usual conditions.

* For all t, F_t contains all of the null sets of F.
* For all t, ∩_{s>t} F_s = F_t, a property called right-continuity.

A function Z : [0, ∞) → ℝ is left-continuous if, for all t, we have Z_t = lim_{s↑t} Z_s; the process has left limits if Z_{t-} = lim_{s↑t} Z_s exists; and finally the process is right-continuous if Z_t = lim_{s↓t} Z_s. The jump ΔZ of Z at time t is ΔZ_t = Z_t - Z_{t-}.

Under the usual conditions, we can without loss of generality for our applications assume that a martingale has sample paths that are almost surely right-continuous with left limits. See, for example, Protter (1990), page 8. This is sometimes taken as a defining property of martingales, for example by Jacod and Shiryaev (1987).

Lemma 1. Suppose Q is equivalent to P, with density process Y. Then an adapted process Y that is right-continuous with left limits is a Q-martingale if and only if EY is a P-martingale.

The proof is immediate from the calculation shown in Appendix C for E[X_{T+1} | G_t].

A process X is a finite-variation process if X = U — V, where U and
V are right-continuous increasing adapted processes with left limits. For

348 Appendix F

example, X is finite-variation if X_t = ∫_0^t δ_s ds, where δ is an adapted process such that the integral exists. The next lemma is a variant of Itô’s Formula.

Lemma 2. Suppose X is a finite-variation process and f : ℝ → ℝ is continuously differentiable. Then

f(X_t) = f(X_0) + ∫_0^t f'(X_{s-}) dX_s + ∑_{0<s≤t} [f(X_s) - f(X_{s-}) - f'(X_{s-}) ΔX_s].

This can be found, for example, in Protter (1990), page 71.

We now record a version of Itô’s Formula that is only occasionally used in this book. For proofs and extensions, see Protter (1990). A semimartingale is a process of the form V + M, where V is a finite-variation process and M is a local martingale.

Lemma 3. Suppose X and Y are semimartingales and at least one of them is a finite-variation process. Let Z = XY. Then Z is a semimartingale and

dZ_t = X_{t-} dY_t + Y_{t-} dX_t + ΔX_t ΔY_t. (F.1)

We now extend the last two lemmas. From this point, B denotes a standard Brownian motion in ℝ^d.

Lemma 4. Suppose X = M + A, where A is a finite-variation process and M_t =
∫_0^t σ_s dB_s, where σ is an adapted process in ℝ^d with ∫_0^t σ_s^2 ds < ∞ almost surely for all t. Suppose f : ℝ → ℝ is twice continuously differentiable. Then

f(X_t) = f(X_0) + ∫_0^t f'(X_{s-}) dX_s + ∑_{0<s≤t} [f(X_s) - f(X_{s-}) - f'(X_{s-}) ΔX_s]
+ 1/2 ∫_0^t f''(X_s) σ_s^2 ds.

Lemma 5. Suppose dX_t = dA_t + σ_t dB_t and dY_t = dC_t + ν_t dB_t, where A and
C are finite-variation processes, and σ and ν are adapted processes in ℝ^d such that ∫_0^t σ_s^2 ds and ∫_0^t ν_s^2 ds are finite almost surely for all t. Let Z = X Y.
Then Z is a semimartingale and

dZ_t = X_{t-} dY_t + Y_{t-} dX_t + ΔX_t ΔY_t + σ_t ν_t dt. (F2)

One can easily define a stochastic integral with respect to a Poisson process N, or any counting process, as defined in Appendix I. For any adapted process θ, we can let

∫_0^t θ_s dN_s = Σ_{0<s≤t} θ_{s-} ΔN_s. (F3)

Itô’s Formula with Jumps 349

Based on the notion of a Poisson process, we can define a continuoustime Markov chain. We will look only at the case of such a process Z with two possible states, say 0 and 1. When in state 0, the process Z moves to state 1 after a time whose probability distribution is exponential with parameter λ(0). When in state 1, the process moves to state 0 after a time whose probability distribution is exponential with parameter λ(1). More precisely, Z solves the stochastic differential equation

ΔZ_t = γ_0(Z(t-)) dN^{(0)}_t + γ_1(Z(t-)) dN^{(1)}_t, (F4)

where N^{(0)} and N^{(1)} are independent Poisson processes with intensity parameters λ(0) and λ(1), respectively, and where

γ(0) = —γ(1) = 1; γ(1) = γ(0) = 0.

The initial condition, Z_0, is either 0 or 1. This is easily generalized to the n-state case.

One can see that the “compensated” process M, defined by dM_t = —λ(Z_t) dt + dZ_t,

is a martingale. Moreover, as above, (B, M) has the martingale representation property, as defined in Appendix I, for the filtration generated by them. We remark that, because Z has a countable number of jumps (almost surely), it makes no difference, for any f whether we write ∫ f(Z_t) dt or
∫ f(Z_{t-}) dt, as f(Z_t) and f(Z_{t-}) differ at most at a countable set of points.
This remark applies similarly below for all integrals with respect to t.

We now develop some simple applications of Itô’s Formula. Here, Z is either a Poisson process with parameter λ, or Z is the continuous-time
Markov chain described above. Suppose that S and U are processes with

dS_t = s(t) dt + σ_s(t) dB_t + β_s(t) dZ_t, dU_t = u(t) dt + σ_u(t) dB_t + β_u(t) dZ_t,

where s, u, σ_s, σ_u, β_s, and β_u are adapted processes such that these integrals exist, with β_s and β_u left-continuous.

Let f : ℝ × [0, T] → ℝ be twice continuously differentiable and let U_t = f(S_t, t). Lemma 4 implies that

dU_t = g(t) dt + f_s(S_t, t) σ_s(t) dB_t + [f(S_t, t) - f(S_{t-}, t)],

where g(t) = f_t(S_{t-}, t) + f_s(S_{t-}, t) s(t) + 1/2 f_{ss}(S_{t-}, t) σ_s(t)^2.

One may note that g is not generally the rate of change of the expectation of U, for the “jump” term f(S_t, t) - f(S_{t-}, t) in (F5) produces another source of expected change. Indeed, provided f satisfies a growth condition in its first (S) argument, we have

dU_t = g(t) dt + dY_t,

where Y is a local martingale and, for the case in which Z is a Poisson process with arrival intensity λ, g(t) = g(t) + λ[Z f(S_{t-} + β_s(t), t) - f(S_{t-}, t)]. (F.6)

The last term in (F.6) represents the expected rate of arrival of jumps multiplied by the size of a jump at time t, assuming that a jump occurs at time t. If Z is instead the continuous-time Markov chain (F.4), then

g(t) = g(t) + [γ_1(Z_{t-})λ(1)(Z_{t-}) + γ_0(Z_{t-})λ(0)(Z_{t-})] × [f(S_{t-} + β_s(t), t) - f(S_{t-}, t)]. (F7)

More generally, let f : {0,1} × ℝ × [0, T] → ℝ be twice continuously differentiable with respect to its last two arguments, and let U_t = f(Z_t, S_t, t). We let f_S and f_{SS} denote partials with respect to the second (S) argument. Then

dU_t = g(t) dt + f_S(Z_{t-}, S_{t-}, t) σ_s(t) dB_t + [f(Z_t, S_t, t) - f(Z_{t-}, S_{t-}, t)], (F8)
where g(t) = f_t(Z_{t-}, S_{t-}, t) + f_S(Z_{t-}, S_{t-}, t) s(t) + 1/2 f_{SS}(Z_{t-}, S_{t-}, t) σ_s(t)^2.
Moreover, dU_t = g(t) dt + dY_t, for Y a local martingale, and g(t) = g(t) + Δ(Z_{t-}, S_{t-}, t), where Δ(z, S, t) = f(z, S + β_s(t), t) - f(z, S, t)
is the size of a jump at time t given that a jump occurs.

G

Utility Gradients

THIS APPENDIX GIVES some examples of the calculation of utility gradients in a continuous-time setting. Further examples are found in Duffie and Skiadas (1994). For further work in this direction, see Schroder and Skiadas (1997, 1999, 2000).

First recall the Mean Value Theorem: If f : [a,b] → ℝ is continuous on the interval [a,b] and has a derivative on (a, b), then there is some c ∈ (a, b) such that f(b) — f(a) = f’(c)(b— a).

We fix a probability space and the time interval [0, T]. A process c: Ω × [0, T] → ℝ is square-integrable if E[∫ c^2 dt] < ∞. Let L denote the space of square-integrable processes and L_+ the space of nonnegative processes in L. We recall from Appendix B that the gradient of a function
U: L_+ → ℝ, when well defined at c ∈ L_+, is given by

VU (c; h) = lim_{α↓0} [F(c+αh) - F(c)]/α,

where F(c) is the set of feasible directions at c.
Consider first the additive-utility function U defined by

U(c) = ∫_0^T u(c(t), t) dt,

where w is continuous and, for each t, u(., t) is continuously differentiable on (0, ∞) with a derivative u_y(., t) satisfying a growth condition |u_y(y, t)| < k + ky, for some constant k independent of t. Let c ∈ L_+ and h ∈ F(c).
Let {α_n} be any sequence of strictly positive scalars smaller than 1 and converging to zero. For each n, α_n, and t, let τ(t) be chosen, by theMean Value Theorem, so that

U(t, c_t + αh_t) - U(t, c_t) = ∫_0^α (U_s(t, c_t + sh_t), h_t) ds.

352 Appendix G

In fact, this can be done so that c + sh is a process in L^∞. It follows that for all n,

U(t, c + αh_n) - U(t, c) = ∫_0^α (U_s(t, c + s h_n), h_n) ds

≤ ∫_0^α (k + h|U_s(t, c + s h_n)|) |h_n| ds

≤ ∫_0^α (k + h|U_s(t, c)|) |h| ds

Moreover, E( ∫_0^T |h_n| dt) < ∞ by the Cauchy-Schwarz inequality since both c and h are in L^2. The Dominated Convergence Theorem implies that

lim_{n→∞} [U(t, c + αh_n) - U(t, c)] / α = lim_{n→∞} (1/α) ∫_0^α (U_s(t, c + s h_n), h_n) ds

= (1/α) ∫_0^α lim_{n→∞} (U_s(t, c + s h_n), h_n) ds

= (1/α) ∫_0^α (U_s(t, c), h) ds

since (U_s(t, c + s h_n), h_n) converges with n to (U_s(t, c), h) for all (ω, t). Thus, for any h ∈ H(c),

VU(c; h) = (1/α) ∫_0^α (U_s(t), h) ds,

where T = u(t, c_t). This implies that the gradient of U at c exists and has the Riesz representation T.

Suppose, for any ε > 0, that u_s satisfies the growth condition given above restricted to (ε, ∞) × [0, T], but not necessarily on the whole domain [0, ∞) × [0, T]. This is important, for example, in dealing with
Inada conditions, as in the example u(x, t) = ex*. In that case, the above calculations extend to obtain the same solution for utility gradients so long as the given consumption process c is bounded away from zero.
That is, suppose for some ε > 0 that c_t > ε for all t. In order to be a feasible direction, c + αh > 0 for some α ∈ (0,1), so c + αh must be bounded away from zero for all α ∈ (0, δ/2), and all of the above calculations carry through to this case. This situation covers the equilibrium described by
Theorem 10G, in which the consumption process c of an arbitrary agent i is indeed bounded away from zero.

We now extend this approach to calculating utility gradients to continuous-time versions of recursive and habit-forming utilities. For these, we fix a filtration F = {F_t : t ∈ [0, T]} of tribes satisfying the usual conditions, which are given in Appendix F. We let f : Ω × [0, T] ×
R^n × R → R be a jointly measurable function satisfying the following

Utility Gradients 353

conditions:

(a) For each fixed (z, v), f(·,·,z, v) is an adapted process.

(b) Uniform Lipschitz condition in utility: For all (ω, t, z, u, v)
there exists a constant K such that | f(ω, t, z, u) − f(ω, t, z, v) | K|u − v|.

(c) Uniform growth condition: There exists a constant K such that for all (ω, t, z), we have | f(ω, t, z, 0)| < K(1 + ||z||).

The function f is a “felicity” function. Its first and second generic arguments, “ω” and “t,” allow dependence of felicity on state and time. The third “z” argument allows dependence on current or past consumption through n different variables. The final argument, “v,” allows dependence of the felicity on utility itself. The additive model has felicity f(ω, t, z, ) = u(t, z), where z stands for current consumption. Fixing a given consumption process c in L^∞, we wish to define a utility process V, an Itô process whose current level V_t corresponds to current utility for remaining consumption. For example, with the additive model, we have V_t =
∫_t^T e^{-ρ(s-t)} u(c_s) ds. In general, we will define the utility for c with felicity f

We use the following existence result of Duffie and Epstein (1992b).

Given any z = (z1, …, zn) in L^∞, there is a unique process V such that

V_t = E_t [ ∫_t^T f(s, z_s, V_s) ds], t ∈ [0,T].

(In the expression “f(s, z_s, V_s),” we have suppressed ω from the notation.

For the continuous-time case of recursive utility, called stochastic differential utility as developed in Duffie and Epstein (1990), this result is applied to the consumption process. For the continuoustime (1973) and habit-formation model, developed by Ryder and Heal
(1973), Duffie and Epstein (1992a), and applied by Constantinides (1990) and
Campbell and Cochrane (1995), Campbell, Ingersoll, and Ross (1991), and
Heaton and Zapatero (1991, 1992), we take n = 2 and let

z1 = c z2 = L_t = ∫_0^t H(c_s, z_s) ds, t ∈ [0,T],

for some measurable H : R^2 → R that is uniformly Lipschitz in its second argument and satisfies a growth condition in its first argument. (See
Duffie and Epstein (1992a) on the question of monotonicity.) It is not difficult to extend this example to cases in which H is state and time dependent. We

354 Appendix G

can compute the Riesz representation of the gradients of the new utilities just defined. For this, we assume that f is continuously differentiable with respect to (z, v), and that there exists a constant K such that

|f_v(ω, t, z, v)| < K(1 + |z|), (ω, t, z, v) ∈ [0, T] × Ω × R^n × R,

where, here and below, subscripts denote partial derivatives with respect to the indicated arguments. For the habit-formation case, we also assume that H is continuously differentiable, that its partial derivative H_z with respect to consumption satisfies a uniform growth condition, and that H_c is bounded. That is, there is a constant K such that |H_c(c, z)| < K(1 + |c|)
for all (c, z).

With these new utilities, and under the stated assumptions, for any strictly positive consumption process c we again have a utility gradient of the form

VU(c; h) = (1/α) ∫_0^α (m_s, h_s) ds,

for a Riesz representation m that is given for stochastic differential utility by

m_t = β_t f_z(t, z_t, V_t),

where β_t = exp(∫_0^t f_v(s, z_s, V_s) ds), and for habit-formation utility by

m_t = β_t [ H_z( c_t, L_t ) exp( ∫_0^t (f_v + H_v) ds) + ∫_t^T f_z ds ],

where the obvious arguments have been omitted. Proofs of these gradient representations, and extensions to more general models, can be found in Duffie and Skiadas (1994).

Another formulation of habit formation is suggested by Hindy and
Huang (1992), extending the work of Hindy, Huang, and Kreps (1992).
Their model is incorporated into this setting by taking n = 1 and Z_t =
∫_0^t k_s dC_s, where k is a bounded adapted process and C is an increasing right-continuous adapted process defining cumulative consumption. For the case of absolutely continuous cumulative consumption, we have C_t =
∫_0^t c_s ds for some c ∈ L^2. In general, consumption may occur with “lumps.”
A gradient calculation for this case is given by Duffie and Skiadas (1994).

H

Itô’s Formula for Complex Functions

THIS APPENDIX GIVES some minimal rules necessary for applying Itô’s Formula to the types of complex-valued functions that arise in the transform calculations of Chapter 8.

With an imaginary number traditionally denoted i = √-1, a complex number is an object of the form z = a + bi, for some real numbers a and b. The real part of z is a; the imaginary part of z is ib. The set of complex numbers, denoted C, is a vector space by pairwise calculations, in that
(a + bi) + (c + di) = (a+c) + (b+d)i and k(a + bi) = ka + kbi for any real scalar k. Complex multiplication is given by

(a + bi) × (c + di) = ac + adi + bci + bdi² = (ac − bd) + (ad + bc)i.

We have the definition e^{iθ} = cos(θ) + i sin(θ) (which can be justified by deeper axioms). For a complex number x = a + bi, one treats e^x as the complex number e^{a+bi} = e^a e^{bi}. One can check that, for two complex numbers z and w, we have e^{z+w} = e^z e^w and e^z / e^w = e^{z-w}.

The norm of a complex number a + bi is defined by |a + bi| =
√(a² + b²). The square root y = √(a+bi) is defined by y = |y|^{1/2} exp(i arg(y)/2), where y² = a+ bi and, for any z ∈ C, arg(z) is defined such that z = |z| exp(i arg(z)), with -π ≤ arg(z) ≤ π. For any z ∈ C, ln(z) = ln |z| + i arg(z), as defined on the “principal branch.”

There are certain definitions and rules for differentiation of an appropriate class of complex-valued functions called analytic. Of these, we will need only the facts:

(a) e^z is analytic with e^z' = e^z.
(b) For integer n ≥ 1, z^n is analytic with (z^n)' = nz^{n-1}.

356 Appendix H

(c) The chain rule f(g(z))' = f'(g(z))g'(z) applies whenever f and g are analytic.

If an Itô process Y is complex valued (that is, Y = Y_R + i Y_I, for realvalued Itô processes Y_R and Y_I), then we can apply Itô’s Formula to see that g(Y_t) is a complex-valued Itô process for any analytic g. The only such g that we need consider here are of the exponential and polynomial forms
(a) and (b), above. In particular, we will be interested in characterizingof Financial Studies 9: 37-68.
Options and Futures Contracts Review
Andersen, J. (1998). “Fast and Accurate Pricing of Path Dependent Options: A Finite Difference Approach.” Journal of Computational Finance 2 (Fall).
Andersen, J., and B. Gruenewald. (1996). “American Option Pricing in the Jump-Diffusion Model.” Working Paper, Aarhus University, Denmark.
Andersen, J., R. Jensen, and R. Poulsen. (1998). “Eight Valuation Methods in Financial Mathematics: A Comparison of the Black-Scholes Formula as an Example.” Mathematical Scientists.
Ansel, J., and C. Stricker. (1992). “Quelques Remarques sur un Théorème de Shurème de N Working Paper, Université de Franche-Comté.
Ansel, J., and C. Stricker. (1994a). ‘Couverture des Actifs Contingents et Prix Maximum.” Annales de l'Institut Henri Poincaré Probabilités et Statistiques 30: 303-315.
Ansel, J., and C. Stricker. (1994). “Lois de Martingale, Densités et Décomposition de Continuity.” 6llmer Schweizer. Working Paper, Université de Franche-Comté.
Cannelli, F. (1993). “Backward-Forward Stochastic Differential Equations.” Annals of Applied Probability 8: 777-98.
Pfleiderer, P., and A. Conze. (1990). “The Term Structure of Interest Rates: The Case of Imperfect Information.” Working Paper, Department of Economics, University of Chicago.

Araujo, A., and P. Monteiro. (1987). “Generic Non-Existence of Equilibria in Finance Models.” Journal of Mathematical Economics 20: 489-501.

Araujo, A., and P. Monteiro. (1989). “Equilibrium Without Uniform Conditions.” Journal of Economic Theory 48: 416-427.

Araujo, A., P. Monteiro, and M. Pascoa. (1996). “Infinite Horizon Incomplete Markets with a Continuum of States.” Mathematical Finance 6: 119-132.

Arntzen, H. (1994). “Solution to a Class of Stochastic Investment Problems Involving Finite Variation Controls.” Working Paper, Mathematics Institute, University of Oslo.

Arrow, K. (1951). “An Extension of the Basic Theorems of Classical Welfare Economics.” In J. Neyman (Ed.), Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability, pp.07-532. Berkeley: University of California Press.

Arrow, K. (1953). “Le Rôle des Valeurs Boursières pour la Répartition la Meilleure des Risques.” Économétrie. Colloq. Internat. Centre National de la Recherche Scientifique 40 (Paris 1952), pp.1-47; discussion, pp.7-48, C.N.R.S. (Paris 1953). English Translation in Review of Economic Studies 31 (1964): 91-96.

Arrow, K. (1970). Essays in the Theory of Risk Bearing. London: North-Holland.

Arrow, K., and G. Debreu. (1954). “Existence of an Equilibrium for a Competitive Economy.” Econometrica 22: 265-290.

Artzner, P. (1995). “References for the Numeraire Portfolio.” Working Paper, Institut de Recherche Mathématique Avancée Université Louis Pasteur et CNRS, et Laboratoire de Recherche en Gestion.

Artzner, P., and F. Delbaen. (1990a). “‘Finem Lauda’ or the Risk of Swaps.” Insurance: Mathematics and Economics 9: 295-303.

Artzner, P., and F. Delbaen. (1990b). “Term Structure of Interest Rates: The Martingale Approach.” Advances in Applied Mathematics 10: 95-129.

Artzner, P., and F. Delbaen. (1992). “Credit Risk and Prepayment Option.” ASTIN Bulletin 22: 81-96.

Artzner, P., and F. Delbaen. (1995). “Default Risk and Incomplete Insurance Markets.” Mathematical Finance 5: 187-195.

Artzner, P., and D. Heath. (1990). “Completeness and Non-Unique Pricing.” Working Paper, Department of Operations Research, Cornell University.

Artzner, P., and D. Heath. (1995). “Approximate Completeness with Multiple Martingale Measures.” Mathematical Finance 5: 1-11.

Artzner, P., and P. Roger. (1993). “Definition and Valuation of Optional Coupon Reinvestment Bonds.” Finance 14: 7-22.

Avramis, A., J. Gregory, and J.-P. Laurent. (1999). “Building Models for Credit Spreads.” Journal of Derivatives 6 (3): 27-43.

Au, K., and D. Thurston. (1993). “Markovian Term Structure Movements.” Working Paper, School of Banking and Finance, University of New South Wales.

Avellaneda, M., R. Buff, C. Friedman, N. Grandchamp, L. Kruk, and J. Newman. (1999). “Weighted Monte Carlo: A New Technique for Calibrating Asset-Pricing Models.” Working Paper, Courant Institute of Mathematical Sciences.

Avellaneda, M., and A. Paras. (1994). “Dynamic Hedging Strategies for Derivative Securities in the Presence of Large Transaction Costs.” Applied Mathematical Finance 1: 165-194.

Avellaneda, M., and P. Laurence. (2000). Financial Models and Derivative Securities. Forthcoming.

Babbs, S. (1991). “A Family of Ito Process Models for the Term Structure of Interest Rates.” Working Paper, Financial Options Research Centre, University of Warwick.
Babbs, S., and M. Selby. (1996). “Pricing by Arbitrage in Incomplete Mathematical Finance 8: 163-168.
Babbs, S., and N. Webber. (1994). “A Theory of the Term Structure with an Official Short Rate.” Working Paper, Midland Global Markets and University of Warwick.
Bachelier, L. (1900). “Théorie de la Spéculation.” Annales Scientifiques de L'École Normale Supérieure 3d ser., 17: 21-88. Translation in The Random Character of Stock Market Prices, ed. Paul Cootner, pp.7-79. Cambridge, MA: MIT Press, 1964.
Back, K. (1986). “Securities Market Equilibrium without Bankruptcy: Contingent Claim Valuation and the Martingale Property.” Working Paper, Center for Mathematical Studies in Economics and Management Science, Northwestern University.
Back, K. (1994). “Option Pricing for General Processes.” Journal of Mathematical Economics 20: 396.
Back, K. (1996). “Yield Curve Models: A Mathematical Review.” Working Paper, Olin School of Business, Washington University in St. Louis, St. Louis.
Back, K., H. Cao, and G. Willard. (2000). “Imperfect Competition among Informed Traders.” Journal of Finance 55: 2117-2155.
Back, K., and S. Pliska. (1986). “Discrete versus Continuous Trading in Securities Markets with Net Worth Constraints.” Working Paper, Center for Mathematical Studies in Economics and Management Science, Northwestern University.
Back, K., and S. Pliska. (1987). “The Shadow Price of Information in Continuous Time Decision Problems.” Stochastics 22: 151-186.
Back, K., and S. Pliska. (1991). “On the Fundamental Theorem of Asset Pricing with an Infinite State Space.” Journal of Mathematical Economics 20: 1-18.

Backus, D., S. Foresi, and S. Zin. (1998). “Arbitrage Opportunities in Arbitrage-Free Models of Bond Pricing.” Journal of Business and Economic Statistics 16: 13-26.
Bajeux-Besnainou, I., and R. Portait. (1993). “Dynamic Asset Allocation in a Mean-Variance Framework.” Working Paper, ESSEC and Laboratoire d’Économétrie de L'École Polytechnique.
Bajeux-Besnainou, I., and R. Portait. (1997). “The Numeraire Portfolio: A New Methodology for Financial Theory.” European Journal of Finance 3: 291-309.
Bajeux-Besnainou, I., and R. Portait. (1998). “Pricing Derivative Securities with a Multi-Factor Gaussian Model.” Applied Mathematical Finance 5: 1-19.
Bajeux-Besnainou, I., and J.-C. Rochet. (1996). “Dynamic Spanning: Are Options an Appropriate Instrument?” Mathematical Finance 6: 1-16.
Bakshi, G., C. Cao, and Z. Chen. (1997). “Empirical Performance of Alternative Option Pricing Models.” Journal of Finance 52: 2003-2049.
Bakshi, G., and D. Madan. (1997). “Pricing Average-Rate Contingent Claims.” Working Paper, Department of Finance, College of Business and Management, University of.
Bakshi, G., and D. Madan. (2000). “Spanning and Derivative Security Valuation.” Journal of.
Balasko, Y. (1989). Foundations of the Theory of General Equilibrium. New York: Academic Press.
Balasko, Y., and D. Cass. (1986). “The Structure of Financial Equilibrium with Exogenous Yields: The Case of Incomplete Markets.” Econometrica 57: 135-162.Balasko, Y., D. Cass, and P. Siconolfi. (1990). “The Structure of Financial Equilibrium with
Exogenous Yields: The Case of Restricted Participation.” *Journal of Mathematical Economics* 19: 195-216.

Balduzzi, P. (1994). “A Second Factor in Bond Yields.” Working Paper, Department of
Finance, Stern School of Business, New York University.

Balduzzi, P., G. Bertola, S. Foresi, and L. Klapper. (1998). “Interest Rate Targeting and the
Dynamics of Short-Term Interest Rates.” *Journal of Money, Credit, and Banking* 30: 26-50.

Balduzzi, P., S. Das, and S. Foresi. (1998). “The Central Tendency: A Second Factor in Bond
Yields.” *Review of Economics and Statistics* 80: 62-72.

Balduzzi, P., S. Das, S. Foresi, and R. Sundaram. (1996). “A Simple Approach to Three Factor
Affine Term Structure Models.” *Journal of Fixed Income* 6 (December): 43-53.

Balduzzi, P., and A. Lynch. (1997). “Samuelson’s Irrelevance Result Reconsidered: The Case of Transaction Costs.” Working Paper, New York University.

Balduzzi, P., and A. Lynch. (1999). “Transaction Costs and Predictability: Some Utility Cost
Calculations.” *Journal of Financial Economics* 52: 47-78.

Ball, C., and A. Roma. (1994). “Stochastic Volatility Option Pricing.” *Journal of Financial and Quantitative Analysis* 29: 589-607.

Ball, C., and W. Torous. (1985). “On Jumps in Common Stock Prices and their Impact on
Call Option Pricing.” *Journal of Finance* 40: 155-173.

Ball, C., and W. Torous. (1994). “Regime Shifts in Short-Term Interest Rate Dynamics.”
Working Paper, Owen Graduate School of Management, Vanderbilt University.

Bally, V. (1995). “An Approximation Scheme for BSDE's and Applications to Control and
Nonlinear PDE’s.” Working Paper, Laboratoire De Statistique et Processus, Universités du Maine et D’Angers.

Bally, V., and D. Talay. (1996). “The Law of the Euler Scheme for Stochastic Differential
Equations: II. Convergence Rate of the Density.” *Monte Carlo Methods and Applications* 2: 93-128.

Bank, P. and F. Riedel. (1999). “Optimal Consumption Choice under Uncertainty with Intertemporal Substitution.” Working Paper, Mathematics Department, Humboldt-University of Berlin.

Banz, R., and M. Miller. (1978). “Prices for State-Contingent Claims: Some Evidence and Applications.” *Journal of Business* 51: 653-672.

Barberis, N., M. Huang, and T. Santos. (2001). “Prospect Theory and Asset Prices.” *Quarterly Journal of Economics*, 116: 1-53.

Barles, G., R. Buckdahn, and E. Pardoux. (1997). “Backward Stochastic Differential Equations and Integral-Partial Differential Equations.” *Stochastics and Stochastics Reports* 60: 57-83.

Barles, G., J. Burdeau, M. Romano, and N. Samsoen. (1993). “Estimation de la Frontiére
Libre des Options Américaines au Voisinage de l’Echéance.” *Comptes Rendus de l’Académie des Sciences de Paris* 316-I: 171-174.

Barles, G., J. Burdeau, M. Romano, and N. Samsoen. (1995). “Critical Stock Price Near Expiration.” *Mathematical Finance* 2: 77-96.

Barles, G., C. Daher, and M. Romano. (1992). “Convergence of Numerical Schemes for
Parabolic Equations Arising in Finance Theory.” Working Paper, Cahier 9244, CEREMADE, Université de Paris.

Barles, G., and E. Lesigne. (1997). “SDE, BSDE and PDE.” In N. El Karoui and L. Mazliak
(Eds.), *Backward Stochastic Differential Equations*, pp.7-80. Essex: Addison Wesley Longman Ltd.

Barles, G., M. Romano, and N. Touzi. (1993). “Contingent Claims and Market Completeness in a Stochastic Volatility Model.” Working Paper, Département de Mathématiques, Université de Tours, France.

Barles, G., and M. Soner. (1998). “Option Pricing with Transaction Costs and a Nonlinear
Black-Scholes Equation.” *Finance and Stochastics* 2: 369-397.

Barndorff-Nielsen, O. (1997). “Normal Inverse Gaussian Distributions and Stochastic Volatility Modelling.” *Scandinavian Journal of Statistics* 24: 1-13.

Barone, E., and S. Risa. (1994). “Valuation of Floaters and Options on Floaters under Special
Repo Rates.” Working Paper, Instituto Mobiliare Italiano, Rome.

Barone-Adesi, G., and R. Elliott. (1991). “Approximations for the Values of American
Options.” *Stochastic Analysis and Applications* 9: 115-131.

Barraquand, J. (1993). “Numerical Valuation of High Dimensional Multivariate European
Securities.” Working Paper, Digital Research Laboratory, Paris.

Barraquand, J., and D. Martineau. (1995). “Numerical Valuation of High Dimensional Multivariate American Securities.” *Journal of Financial and Quantitative Analysis* 30: 383-405.

Barraquand, J., and T. Pudet. (1996). “Pricing of American Path-Dependent Contingent Claims.” *Mathematical Finance* 6: 17-51.

Bartle, R. (1976). *The Elements of Real Analysis* (2nd ed.). New York: Wiley.

Basak, S. (1995). “A General Equilibrium Model of Portfolio Insurance.” *Review of Financial Studies* 8: 1059-1090.

Basak, S. (1997). “Consumption Choice and Asset Pricing with a Non-Price-Taking Agent.”
*Economic Theory* 10: 437-462.

Basak, S., and D. Cuoco. (1999). “An Equilibrium Model with Restricted Stock Market Participation.” *Review of Financial Studies* 11: 309-341.

Bates, D. (1996). “Jumps and Stochastic Volatility: Exchange Rate Processes Implicit in
Deutsche Mark Option.” *Review of Financial Studies* 9: 69-107.

Bates, D. (1997). “Post-87’ Crash Fears in Sand-P 500 Futures Options.” Working Paper,
Finance Department, Wharton School, University of Pennsylvania.

Baxter, M. (1996). “General Interest-Rate Models and the Universality of HJM.” Working
Paper, Statistical Laboratory, University of Cambridge, Cambridge.

Baz, J., and S. Das. (1996). “Analytical Approximations of the Term Structure for JumpDiffusion Processes: A Numerical Analysis.” *Journal of Fixed Income* 6 (1): 78-86.

Beaglehole, D. (1990). “Tax Clientele and Stochastic Processes in the Gilt Market.” Working
Paper, Graduate School of Business, University of Chicago.

Beaglehole, D., and M. Tenney. (1991). “General Solutions of Some Interest Rate Contingent
Claim Pricing Equations.” *Journal of Fixed Income* 1: 69-84.

Becker, R., and J. Boyd. (1993). “Recursive Utility: Discrete Time Theory.” *Hitotsubashi Journal of Economics* 34: 49-98.

Beckers, S. (1981). “Standard Deviations Implied in Option Process as Predictors of Future
Stock Price Variability.” *Journal of Banking and Finance* 5: 363-382.

Beibel, M., and H. Lerche. (1995). “A New Look at Warrant Pricing and Related Optimal
Stopping Problems.” Working Paper, Institut für Mathematische Stochastik, University of Bonn.

Beibel, M., and H. Lerche. (1997). “A New Look at Optimal Stopping Problems Related to
Mathematical Finance.” *Statistica Sinica* 7: 93-108.
Bellman, R. (1957). *Dynamic Programming*. Princeton, NJ.: Princeton University Press.
Bensoussan, A. (1983). “Lectures on Stochastic Control.” In S. Mitter and A. Moro (Eds.),
*Nonlinear Filtering and Stochastic Control*, Lecture Notes in Mathematics 972, pp.-62. New York: Springer-Verlag.
Bensoussan, A. (1984). “On the Theory of Option Pricing.” *Acta Applicandae Mathematicae* 2: 139-158.
Bensoussan, A., M. Crouhy, and D. Galai. (1995a). “Black-Scholes Approximation of Complex Option Values: The Cases of European Compound Call Options and Equity
Warrants.” Working Paper, Université Paris Dauphine and INRIA, France.
Bensoussan, A., M. Crouhy, and D. Galai. (1995b). “Stochastic Equity Volatility Related to the
Leverage Effect II: Valuation of European Equity Options and Warrants.” *Applied Mathematical Finance* 2: 43-59.
Benth, R., K. Karlsen, and K. Reikvam. (1999). “Optimal Portfolio Selection with Consumption and Nonlinear Integro-Differential Equations with Gradient Constraint: A
Viscosity Solution Approach.” Working Paper, Centre for Mathematical Physics and Stochastics.
Benveniste, L., and J. Scheinkman. (1979). “On the Differentiability of the Value Function in Dynamic Models of Economics.” *Econometrica* 47: 727-732.
Benzoni, L. (1998). “Pricing Options under Stochastic Volatility: An Econometric Analy-sis.” Working Paper, J.L. Kellog Graduate School of Management, Northwestern University.
Berardi, A., and M. Esposito. (1999). “A Base Model for Multifactor Specifications of the Term Structure.” Economic Notes 28: 145-170.
Bergman, Y. (1985b). “Time Preference and Capital Asset Pricing Models.” Journal of Financial Economics 14: 145-159.
Bergman, Y. (1995). “Option Pricing with Differential Interest Rates.” Review of Financial Studies 8: 475-500.
Bergman, Y., B. Grundy, and Z. Wiener. (1996). “Generalized Theory of Rational Option Pricing.” Journal of Finance 51: 1573-1610.
Berk, J. (1992). “The Necessary and Sufficient Conditions that Imply the CAPM.” Working
Paper, Faculty of Commerce, University of British Columbia, Canada.
Berk, J. (1997). “Necessary Conditions for the CAPM.” Journal of Economic Theory 73: 245-257.
Berk, J., and H. Uhlig. (1993). “The Timing of Information in a General Equilibrium Framework.” Journal of Economic Theory 59: 275-287.
Bernard, P., D. Talay, and L. Tubaro. (1994). “Rate of Convergence of a Stochastic Particle
Method for the Kolmogorov Equation with Variable Coefficients.” Mathematics of Computation 63: 555-587.
Bertsekas, D. (1976). Dynamic Programming and Stochastic Control. New York: Academic Press.
Bertsekas, D., and S. Shreve. (1978). Stochastic Optimal Control: The Discrete Time Case.
New York: Academic Press.
Bertsimas, D., L. Kogan, and A. Lo. (1998). “When is Time Continuous?” Working Paper,
MIT Sloan School of Management. Forthcoming in Journal of Financial Economics.
Bewley, T. (1972). “Existence of Equilibria in Economies with Infinitely Many Commodities.”
Journal of Economic Theory 4: 514-540.

Bewley, T. (1982). “Thoughts on Volatility Tests of the Intertemporal Asset Pricing Model.”
Working Paper, Department of Economics, Northwestern University.

Bhar, R., and C. Chiarella. (1995). “Transformation of Heath-Jarrow-Morton Models to
Markovian Systems.” Working Paper, School of Finance and Economics, University of Technology, Sydney.

Bick, A. (1986). “On Viable Diffusion Price Processes.” Journal of Finance 45: 673-689.

Bick, A. (1988). “Producing Derivative Assets with Forward Contracts.” Journal of Financial and Quantitative Analysis 2: 153-160.

Bick, A. (1994). “Futures Pricing via Futures Strategies.” Working Paper, Faculty of Business
Administration, Simon Fraser University, Vancouver, Canada.

Bick, A. (1995). “Quadratic Variation Based Dynamic Strategies.” Management Science 41: 722-732.

Bick, A. (1997). “Two Closed-Form Formulas for the Futures Price in the Presence of a
Quality Option.” European Finance Review 1: 81-104.

Bick, A., and H. Reisman. (1993). “Generalized Implied Volatility.” Working Paper, Faculty of Business Administration, Simon Fraser University, Vancouver, Canada.

Bick, A., and W. Willinger. (1994). “Dynamic Spanning without Probabilities.” Stochastic Processes and Their Applications 50: 349-374.

Bielecki, T., and M. Rutkowski. (1999a). “Credit Risk Modelling: A Multiple Ratings Case.”
Working Paper, Northeastern Illinois University and Technical University of Warsaw.

Bielecki, T., and M. Rutkowski. (1999b). “Modelling of the Defaultable Term Structure: Conditionally Markov Approach.” Working Paper, Northeastern Illinois University and Technical University of Warsaw.

Bielecki, T., and M. Rutkowski. (2000). “Credit Risk Modelling: Intensity Based Approach.”
Working Paper, Department of Mathematics, Northeastern Illinois University.

Billingsley, P. (1986). Probability and Measure (2d ed.). New York: Wiley.

Bjerksund, P., and G. Stensland. (1993). “Closed-Form Approximation of American Options.”
Scandinavian Journal of Management 9: S87-S99.

Bjork, T. (1996). “Interest Rate Theory.” Working Paper, Department of Finance, Stockholm School of Economics.

Bjork, T. (1998). Arbitrage Theory in Continuous Time. New York: Oxford University Press.

Bjork, T., and B. Christensen. (1999). “Interest Rate Dynamics and Consistent Forward Rate Curves.” Mathematical Finance 22: 17-23.

Bjork, T., G. DiMasi, Y. Kabanov, and W. Runggaldier. (1997). “Towards a General Theory of
Bond Markets.” Finance and Stochastics 1: 141-174.

Bjork, T., and A. Gombani. (1999). “Minimal Realizations of Interest Rate Models.” Finance and Stochastics 3: 413-432.

Bjork, T., Y. Kabanov, and W. Runggaldier. (1995). “Bond Markets where Prices are Driven by a General Marked Point Process.” Working Paper, Optimization and Systems
Theory, Department of Mathematics, Royal Institute of Technology, Stockholm.

Black, F. (1972). “Capital Market Equilibrium with Restricted Borrowing.” Journal of Business 45: 444-454.

Black, F. (1976). “The Pricing of Commodity Contracts.” Journal of Financial Economics 3: 167-179.

Black, F. (1990). “Mean Reversion and Consumption Smoothing.” Review of Financial Studies 3: 107-114.

Black, F. (1995). Exploring General Equilibrium. Cambridge, MA: MIT Press.

Black, F., and J. Cox. (1976). “Valuing Corporate Securities: Liabilities: Some Effects of Bond
Indenture Provisions.” Journal of Finance 31: 351-367.

Black, F., E. Derman, and I. Kani. (1992). “A Two-Factor Model of Interest Rates.” Working Paper, Goldman, Sachs and Company, New York.

Black, F., E. Derman, and W. Toy. (1990). “A One-Factor Model of Interest Rates and
Its Application to Treasury Bond Options.” Financial Analysts Journal JanuaryFebruary: 33-39.

Black, F., and P. Karasinski. (1991). “Bond and Option Pricing when Short Rates are Lognormal.” Financial Analysts Journal (July-August): 52-59.

Black, F., and M. Scholes. (1973). “The Pricing of Options and Corporate Liabilities.” Journal of Political Economy 81: 637-654.

Blackwell, D. (1965). “Discounted Dynamic Programming.” Annals of Mathematical Statistics 36: 226-235.

Blume, L., D. Easley, and M. O’Hara. (1982). “Characterization of Optimal Plans for Stochastic Dynamic Programs.” Journal of Economic Theory 28: 221-234.

Bollerslev, T., R. Chou, and K. Kroner. (1992). “ARCH Modeling in Finance: A Review of the Theory and Empirical Evidence.” Journal of Econometrics 52: 5-59.

Bonomo, M., and R. Garcia. (1993). “Disappointment Aversion as a Solution to the Equity
Premium and the Risk-Free Rate Puzzles.” Working Paper, CRDE 2793, Université de Montréal.

Bossaerts, P. (1990). “Modern Term Structure Theory.” Working Paper, California Institute of Technology, Pasadena.

Bossaerts, P., E. Ghysels, and C. Gouriéroux. (1996). “Arbitrage-Based Pricing when Volatility is Stochastic.” Working Paper, California Institute of Technology, Pasadena.

Bossaerts, P., and P. Hillion. (1997). “Local Parametric Analysis of Hedging in Discrete Time.”
Journal of Econometrics 81: 243-272.

Bottazzi, J.-M., T. Hens, and A. Léffler. (1994). “Market Demand Functions in the CAPM.”
Working Paper, Delta, Université de Paris.

Bottazzi, J.-M. (1995). “Existence of Equilibria with Incomplete Markets: The Case of Smooth
Returns.” Journal of Mathematical Economics 24: 59-72.

Bottazzi, J.-M., and T. Hens. (1996). “Excess Demand Functions and Incomplete Markets.”
Journal of Economic Theory 68: 49-63.

Boudoukh, J., M. Richardson, R. Stanton, and R. Whitelaw. (1995). “Pricing Mortgage-Backed
Securities in a Multifactor Interest Rate Environment: A Multivariate Density Estimation Approach.” Working Paper, Institute of Business and Economic Research, University of California at Berkeley.

Bouleau, N., and D. Lamberton. (1989). “Residual Risks and Hedging Strategies in Markovian Markets.” Stochastic Processes and Their Applications 33: 131-150.

Bouleau, N., and D. Lépingle. (1994). Numerical Methods for Stochastic Processes. New York: Wiley.

Boyarchenko, S., and S. Levendorskii. (2000a). “Pricing of the Perpetual American Call
Under Lévy Processes.” Working Paper, Department of Mathematics, University of Pennsylvania.

Boyarchenko, S., and S. Levendorskii. (2000b). “Pricing of the Perpetual American PutUnder Lévy Processes.” Working Paper, Department of Mathematics, University of Pennsylvania.

Boyle, P (1977). “Options: A Monte Carlo Approach.” Journal of Financial Economics 4: 323-338.

Boyle, P. (1988). “A Lattice Framework for Option Pricing with Two State Variables.” Journal of Financial and Quantitative Analysis 23: 1-12.

Boyle, P. (1990). “Valuation of Derivative Securities Involving Several Assets using Discrete
Time Methods.” Working Paper, Accounting Group, University of Waterloo, Waterloo, Canada.

Boyle, P., M. Broadie, and P. Glasserman. (1997). “Monte Carlo Methods for Security Pricing.” Journal of Economic Dynamics and Control 21: 1267-1321.

Boyle, P., J. Evnine, and S. Gibbs. (1989). “Numerical Evaluation of Multivariate Contingent Claims.” Review of Financial Studies 2: 241-250.

Boyle, P., and T. Vorst. (1992). “Options Replication in Discrete Time with Transaction Costs.” Journal of Finance 47: 271-293.

Boyle, P., and T. Wang. (1999). “Valuation of New Securities in an Incomplete Market: The
Catch of Derivative Pricing.” Working Paper, School of Accountancy, University of Waterloo.

Brace, A. (1996). “Non-Bushy Trees for Gaussian HJM and Lognormal Forward Models.”
Working Paper, School of Mathematics, University of New South Wales, Australia.

Brace, A., and M. Musiela. (1994a). “A Multifactor Gauss Markov Implementation of Heath,
Jarrow, and Morton.” Mathematical Finance 4: 259-284.

Brace, A., and M. Musiela. (1994b). “Swap Derivatives in a Gaussian HJM Framework.” Working Paper, Treasury Group, Citibank, Sydney, Australia.

Brace, A., and M. Musiela. (1995a). “Duration, Convexity and Wiener Chaos.” Working Paper, Treasury Group, Citibank, Sydney, Australia.

Brace, A., and M. Musiela. (1995b). “Hedging, Duration, Bucketing and Convexity in a
Gaussian Heath Jarrow Morton Framework.” Working Paper, Treasury Group, Citibank, Sydney, Australia.

Brace, A., and M. Musiela. (1995c). “The Market Model of Interest Rate Dynamics.” Mathematical Finance 7: 127-155.

Bray, M. (1994a). “The Arbitrage Pricing Theory is Not Robust 1: Variance Matrices and
Portfolio Theory in Pictures.” Working Paper, London School of Economics.

Bray, M. (1994b). “The Arbitrage Pricing Theory is Not Robust 2: Factor Structure and Factor
Pricing.” Working Paper, London School of Economics.

Breeden, D. (1979). “An Intertemporal Asset Pricing Model with Stochastic Consumption and Investment Opportunities.” Journal of Financial Economics 7: 265-296.

Breeden, D. (1986). “Consumption, Production, Inflation and Interest Rates.” Journal of Financial Economics 16: 3-39.

Breeden, D., M. Gibbons, and R. Livenberger. (1989). “Empirical Tests of the Consumption Oriented CAPM.” Journal of Finance 44: 231-262.

Breeden, D., and R. Livenberger. (1978). “Prices of State-Contingent Claims Implicit in Option Prices.” Journal of Business 51: 621-651.

Brémaud, P. (1981). Point Processes and Queues: Martingale Dynamics. New York: Springer.

Brennan, M., and E. Schwartz. (1977). “The Valuation of American Put Options.” Journal of Finance 32: 449-462.

Brennan, M., and E. Schwartz. (1979). “A Continuous Time Approach to the Pricing of
Bonds.” Journal of Banking and Finance 3: 133-155.

Brennan, M., and E. Schwartz. (1980a). “Analysing Convertible Bonds.” Journal of Financial and Quantitative Analysis 15: 907-929.

Brennan, M., and E. Schwartz. (1980c). “Conditional Predictions of Bond Prices and Returns.” Journal of Finance 35: 405-419.

Brennan, M., and E. Schwartz. (1982). “An Equilibrium Model of Bond Pricing and a Test of Market Efficiency.” Journal of Financial and Quantitative Analysis 17: 301-329.

Brennan, M., E. Schwartz, and R. Lagnado. (1997). “Strategic Asset Allocation.” Journal of Economic Dynamics and Control 21: 1377-1403.

Broadie, M., J. Cvitanić, and M. Soner. (1998). “Optimal Replication of Contingent Claims
Under Portfolio Constraints.” Review of Financial Studies 11: 59-79.

Broadie, M., and J. Detemple. (1995). “American Capped Call Options on Dividend-Paying Assets.” Review of Financial Studies 8: 161-191.

Broadie, M., and J. Detemple. (1996). “American Option Valuation: New Bounds, Approximations and a Comparison of Existing Methods.” Review of Financial Studies 9: 1211-1250.

Broadie, M., and J. Detemple. (1997). “The Valuation of American Options on Multiple Assets.” Mathematical Finance 7: 241-285.

Broadie, M., and P. Glasserman. (1996). “Estimating Security Price Derivatives Using Simulation.” Management Science 42: 269-285.

Broadie, M., and P. Glasserman. (1997). “Pricing American Style Securities Using Simulation.” Journal of Economic Dynamics and Control 21: 1323-1353.

Broadie, M., and P. Glasserman. (1998). “A Stochastic Mesh Method for Pricing High
Dimensional American Options.” Working Paper, Graduate School of Business, Columbia University, New York, NY.

Broadie, M., P. Glasserman, and S. Kou. (1997). “A Continuity Correction for Discrete Barrier Options.” Mathematical Finance 7: 325-349.

Broadie, M., P. Glasserman, and S. Kou. (1999). “Connecting Discrete and Continuous PathDependent Options.” Finance and Stochastics 3: 55-82.

Brock, W. (1979). “An Integration of Stochastic Growth Theory and the Theory of Finance,
Part J: The Growth Model.” In J. Green and J. Scheinkman (Eds.), General Equilibrium, Growth, and Trade, pp.65-192. New York: Academic Press.

Brock, W. (1982). “Asset Prices in a Production Economy.” In J. McCall (Ed.), The Economics of Information and Uncertainty, pp.-46. Chicago: University of Chicago Press.

Brown, D., P. DeMarzo, and C. Eaves. (1996a). “Computing Equilibria when Asset Markets are Incomplete.” Econometrica 64: 1-27.

Brown, D., P. DeMarzo, and C. Eaves. (1996b). “Computing Zeros of Sections Vector Bundles Using Homotopies and Relocalization.” Mathematics of Operations Research 21: 26-43.

Brown, D., and M. Gibbons. (1985). “A Simple Econometric Approach for Utility-Based Asset Pricing Models.” Journal of Finance 40: 359-381.

Brown, R., and S. Schaefer. (1994a). “Interest Rate Volatility and the Shape of the Term
Structure.” Philosophical Transactions of the Royal Society: Physical Sciences and Engineering 347: 449-598.

Brown, R., and S. Schaefer. (1994b). “The Term Structure of Real Interest Rates and the
Cox, Ingersoll, and Ross Model.” Journal of Financial Economics 35: 3-42.

Brown, R., and S. Schaefer. (1996). “Ten Years of the Real Term Structure: 1984-1994.”
Journal of Fixed Income 6 (March): 6-22.

Broze, L., O. Scaillet, and J.-M. Zakoian. (1993). “Testing for Continuous-Time Models of the
Short-Term Interest Rate.” Working Paper, CORE, Louvain-la-Neuve, Belgium.

Buckdahn, R. (1995a). “Backward Stochastic Differential Equations Driven by a Martingale.”
Working Paper, FB Mathematik der Humboldt-Universität zu Berlin, Berlin.

Buckdahn, R. (1995b). “BSDE with Non-Square Integrable Terminal Value—FBSDE with
Delay.” Working Paper, Faculté des Sciences, Département de Mathématiques,
Université de Bretagne Occidentale, Brest, France.

Buckdahn, R., and Y. Hu. (1995). “Pricing of American Contingent Claims with Jump Stock
Price and Constrained Portfolios.” Working Paper, Département de Mathématiques, Université de Bretagne Occidentale.

Bühler, W., M. Uhrig-Homburg, U. Walter, and T. Weber. (1995). “An Empirical Comparison of Alternative Models for Valuing Interest Rate Options.” Working Paper,
Lehrstuhl für Finanzwirtschaft, Universität Mannheim.

Bühlmann, H., F. Delbaen, P. Embrechts, and A. Shiryaev. (1998). “On Esscher Transforms in Discrete Finance Models.” ASTIN Bulletin 28: 171-186.

Bunch, D., and H. Johnson. (1993). “A Simple and Numerically Efficient Valuation Method for American Puts Using a Modified Roll-Geske-Johnson Approach.” Journal of Finance 47: 809-816.

Buono, M., R. Gregory-Allen, and U. Yaari. (1992). “The Efficacy of Term Structure Estima-tion Techniques: A Monte Carlo Study.” Journal of Fixed Income 2: 52-63.

Battler, H. (1995). “Evaluation of Callable Bonds: Finite Difference Methods, Stability and Accuracy.” Economic Journal 105: 374-384.

Battler, H., and J. Waldvogel. (1996). “Pricing Callable Bonds by Means of Green's Function.” Mathematical Finance 6: 53-88.

Cadenillas, A., and S. Pliska. (1999). “Optimal Trading of a Security when there are Taxes and Transaction Costs.” Finance and Stochastics 3: 137-165.

Caflisch, R., and W. Morokoff. (1995). “Quasi-Monte Carlo Computation of a Finance Problem.” Working Paper, Department of Mathematics, University of California, Los Angeles.

Caflisch, R., and W. Morokoff. (1996). “Valuation of Mortgage Backed Securities using the Quasi-Monte Carlo Method.” Working Paper, Department of Mathematics, University of California, Los Angeles.

Caflisch, R., W. Morokoff, and A. Owen. (1997). “Valuation of Mortgage Backed Securities Using Brownian Bridges to Reduce Effective Dimension.” Journal of Computational Finance 1 (Fall).

Calvet, L. (1999). “Incomplete Markets and Volatility.” Working Paper, Department of Economics, Littauer Center, Cambridge, MA.

Campbell, J. (1986a). “Bond and Stock Returns in a Simple Exchange Model.” Quarterly Journal of Economics 101: 785-803.

Campbell, J. (1986b). “A Defense of Traditional Hypotheses about the Term Structure of Interest Rates.” Journal of Finance 41: 183-193.

Campbell, J. (1993). “Intertemporal Asset Pricing without Consumption.” American Economic Review 83: 487-512.

Campbell, J. (1995). “Some Lessons from the Yield Curve.” Journal of Economic Perspectives 9: 129-152.

Campbell, J., A. Lo, and C. MacKinlay. (1997). The Econometrics of Financial Markets. Princeton University Press.

Carassus, L., and E. Jouini. (1998). “Investment and Arbitrage Opportunities with Shorts ale Constraints.” Mathematical Finance 8: 169-178.

Carr, P. (1989). “European Option Valuation when Carrying Costs are Unknown.” Working Paper, Johnson Graduate School of Management, Cornell University.

Carr, P. (1991). “Deriving Derivatives of Derivative Securities.” Working Paper, Johnson Graduate School of Management, Cornell University. Forthcoming in Journal of Computational Finance.

Carr, P. (1992a). “European Put Call Symmetry.” Working Paper, Johnson Graduate School of Management, Cornell University.

Carr, P. (1993b). “Valuing Bond Futures and the Quality Option.” Working Paper, Johnson Graduate School of Management, Cornell University.

Carr, P. (1994). “On Approximations for the Values of American Options.” Working Paper, Johnson Graduate School of Management, Cornell University.

Carr, P. (1995). “Two Extensions to Barrier Option Valuation.” Applied Mathematical Finance 2: 173-209.

Carr, P. (1998). “Randomization and the American Put.” Review of Financial Studies 11: 598-626.

Carr, P., and R-R. Chen. (1993). “Valuing Bond Futures and the Quality Option.” Working Paper, Johnson Graduate School of Management, Cornell University.

Carr, P., and K. Ellis. (1994). “Non-Standard Valuation of Barrier Options.” Working Paper, Johnson Graduate School of Management, Cornell University.

Carr, P., and D. Faguet. (1994). “Fast Accurate Valuation of American Options.” Working Paper, Johnson Graduate School of Management, Cornell University.

Carr, P., and D. Faguet. (1996). “Valuing Finite-Lived Options as Perpetual.” Working Paper, Johnson School of Management, Cornell University.

Carr, P., and R. Jarrow. (1990). “The Stop-Loss Start-Gain Paradox and Option Valuation: A New Decomposition into Intrinsic and Time Value.” Review of Financial Studies 3: 469-492.

Carr, P., R. Jarrow, and R. Myneni. (1992). “Alternative Characterizations of American Put Options.” Mathematical Finance 2: 87-106.

Carr, P., and D. Madan. (1998). “Option Valuation Using the Fast Fourier Transform.” Journal of Computational Finance 2 (Summer).

Carr, P., and D. Madan. (1999). “Option Valuation using the Fast Fourier Transform.” Journal of Computational Finance 2: 61-74.

Carverhill, A. (1988). “The Ho and Lee Term Structure Theory: A Continuous Time Version.” Working Paper, Financial Options Research Centre, University of Warwick.

Carverhill, A. (1990). “A Survey of Elementary Techniques for Pricing Options on Bonds and Interest Rates.” Working Paper, Financial Options Research Centre, University of Warwick.

Carverhill, A. (1991). “The Term Structure of Interest Rates and Associated Options: Equilibrium versus Evolutionary Models.” Working Paper, Financial Options Research Centre, University of Warwick.

Carverhill, A. (1995). “A Simplified Exposition of the Heath, Jarrow, and Morton Model.” Stochastics 53: 227-240.

Carverhill, A. (1996). “Arbitrage, the Term Structure of Volatility, and the Long Forward Rate.” Working Paper, Department of Finance, University of Science and Technology, Hong Kong.

Carverhill, A., and K. Pang. (1995). “Efficient and Flexible Bond Option Valuation in the Heath, Jarrow, and Morton Framework.” Journal of Fixed Income 5 (September): 70-77.

Cass, D. (1984). “Competitive Equilibria in Incomplete Financial Markets.” Working Paper, Center for Analytic Research in Economics and the Social Sciences, University of Pennsylvania.

Cass, D. (1989). “Sunspots and Incomplete Financial Markets: The Leading Example.” In G. Feiwel (Ed.), The Economics of Imperfect Competition and Employment: Joan Robinson and Beyond, pp.77-693. London: Macmillan.

Cass, D. (1991). “Incomplete Financial Markets and Indeterminacy of Financial Equilibrium.” In J.J. Laffont (Ed.), Advances in Economic Theory, pp.63-288. Cambridge: Cambridge University Press.

Cassese, G. (1996). “An Elementary Remark on Martingale Equivalence and the Fundamental Theorem of Asset Pricing.” Working Paper, Istituto di Economia Politica, Universita Commerciale “Luigi Bocconi,” Milan.

Chacko, G., and S. Das. (1998). “Pricing Average Interest Rate Options: A General Approach.” Working Paper, Harvard Business School.

Chae, S. (1988). “Existence of Equilibria in Incomplete Markets.” Journal of Economic Theory 44: 9-18.

Chalasani, P., S. Jha, and A. Varikooty. (1998). “Accurate Approximations for European Asian Options.” Journal of Computational Finance 1 (Summer).

Chamberlain, G. (1988). “Asset Pricing in Multiperiod Securities Markets.” Econometrica 56: 1283-1300.

Chan, K-C., A. Karolyi, F. Longstaff, and A. Saunders. (1992). “An Empirical Comparison of Alternative Models of the Short-Term Interest Rate.” Journal of Finance 47: 1209-1227.

Chan, Y.-K. (1992). “Term Structure as a Second Order Dynamical System, and Pricing of Derivative Securities.” Working Paper, Bear Stearns and Company, New York.

Chang, F-R. (1993). “Adjustment Costs, Optimal Investment and Uncertainty.” Working Paper, Department of Economics, Indiana University.

Chapman, D. (1998). “Habit Formation, Consumption, and State-Prices.” Econometrica 66: 1223-1230.

Charretour, F., R. Elliott, R. Myneni, and R. Viswanathan. (1992). “American Option Valuation Notes.” Working Paper, Oberwolfach Institute, Oberwolfach, Germany.

Chen, L. (1996). Stochastic Mean and Stochastic Volatility: A Three-Factor Model of the Term Structure of Interest Rates and Its Application to the Pricing of Interest Rate Derivatives: Part I. Oxford: Blackwell Publishers.

Chen, R-R., and L. Scott. (1992a). “Maximum Likelihood Estimation for a Multi-Factor Equilibrium Model of the Term Structure of Interest Rates.” Working Paper, Department of Finance, Rutgers University.

Chen, R-R., and L. Scott. (1992b). “Pricing Interest Rate Options in a Two-Factor Cox-Ingersoll-Ross Model of the Term Structure.” Review of Financial Studies 5: 613-636.

Chen, R-R., and L. Scott. (1993a). “Multi-Factor Cox-Ingersoll-Ross Models of the Term Structure: Estimates and Tests from a State-Space Model using a Kalman Filter.” Working Paper, Department of Finance, Rutgers University.-R., and L. Scott. (1993b). “Pricing Interest Rate Futures Options with Futures-Style Margining.” Journal of Futures Markets 13: 15-22.

Chen, R.

Chen, R.

Chen, R-R., and L. Scott. (1995). “Interest Rate Options in Multifactor Cox-Ingersoll-Ross Models of the Term Structure.” Journal of Derivatives 3: 53-72.

Chen, R-R., and B. Sopranzetti. (1999). “The Valuation of Default-Triggered Credit Derivatives.” Working Paper, Rutgers Business School, Department of Finance and Economics.

Chen, Z., and L. Epstein. (1999). “Ambiguity, Risk and Asset Returns in Continuous Time.” Working Paper, Department of Mathematics, Shandong University.

Chen, Z.-W. (1994). “Viable Costs and Equilibrium Prices in Frictional Securities Markets.” Working Paper, Graduate School of Business, University of Wisconsin.

Cheng, S. (1991). “On the Feasibility of Arbitrage-Based Option Pricing when Stochastic Bond Price Processes are Involved.” Journal of Economic Theory 53: 185-198.

Cherian, J., and R. Jarrow. (1998). “Options Markets, Self-Fulfilling Prophecies, and Implied Volatilities.” Review of Derivatives Research 2: 5-37.

Cherif, T., N. El Karoui, R. Myneni, and R. Viswanathan. (1995). “Arbitrage Pricing and Hedging of Quanto Options and Interest Rate Claims with Quadratic Gaussian State Variables.” Working Paper, Laboratoire de Probabilités, Université de Paris, VI.

Chernoff, H., and A. Petkau. (1984). “Numerical Methods for Bayes Sequential Decisions Problems.” Working Paper, Technical Report 34, Statistics Center, Massachusetts Institute of Technology.

Chernov, M., and E. Ghysels. (2000). “A Study towards a Unified Approach to the Joint Estimation of Objective and Risk Neutral Measures for the Purpose of Options Valuation.” Journal of Financial Economics 56: 407-458.

Cherubini, U. (1993). “The Orthogonal Polynomial Approach to Contingent Claim Pricing.” Working Paper, Banco Commerciale Italiana, Ufficio Studi, Milan.

Cherubini, U., and M. Esposito. (1992). “Using Pearson’s System to Characterize Diffusion Processes: A Note.” Working Paper, Banco Commerciale Italiana, Ufficio Studi, Milan.

Cherubini, U., and M. Esposito. (1995). “Options in and on Interest Rate Futures Contracts: Results from Martingale Pricing Theory.” Applied Mathematical Finance 2: 1-15.

Chesney, M., R. Elliott, and R. Gibson. (1993). “Analytical Solution for the Pricing of American Bond and Yield Options.” Mathematical Finance 3: 277-294.

Chesney, M., M. Jeanblanc, and M. Yor. (1997). “Brownian Excursions and Barrier Options.” Advances in Applied Probability 29: 165-184.

Chevance, D. (1995). “Discrétisation des Equations Différentielles Stochastiques Rétrogrades.” Working Paper, I.N.R.LA.

Chevance, D. (1996). “Discretization of Pardoux-Peng’s Backward Stochastic Differential Equations.” Working Paper, Université de Provence.

Chew, S.-H. (1983). “A Generalization of the Quasilinear Mean with Applications to the Measurement of Income Inequality and Decision Theory Resolving the Allais Paradox.” Econometrica 51: 1065-1092.

Chew, S.-H. (1989). “Axiomatic Utility Theories with the Betweenness Property.” Annals of Operations Research 19: 273-298.

Chew, S-H., and L. Epstein. (1991). “Recursive Utility under Uncertainty.” In A. Khan and N. Yannelis (Eds.), Equilibrium Theory with an Infinite Number of Commodities, pp.53-369. New York: Springer-Verlag.

Cheyette, O. (1995). “Markov Representation of the Heath-Jarrow-Morton Model.” Working Paper, BARRA Inc., Berkeley, California.

Cheyette, O. (1996). “Implied Prepayments.” Working Paper, BARRA Inc., Berkeley, California.

Chiarella, C., and N. E. Hassan. (1997). “Evaluation of Derivative Security Prices in the Heath-Jarrow-Morton Framework as Path Integrals.” Journal of Financial Engineering 6: 121-147.

Chidambaran, N., and S. Figlewski. (1995). “Streamlining Monte-Carlo Simulation with the Quasi-Analytic Method: An Analysis of a Path-Dependent Option Strategy.” Journal of Derivatives 3: 29-51.

Choulli, T., L. Krawczyk, and C. Stricker. (1998). “€-Martingales and Their Applications in Mathematical Finance.” Annals of Probability 26: 853-876.

Chow, Y., and H. Teicher. (1978). Probability Theory: Independence Interchangeability Martingales. New York: Springer-Verlag.

Christensen, B. J. (1991). “Statistics for Arbitrage-Free Asset Pricing.” Working Paper, Department of Finance, New York University.

Christensen, P. (1987). “An Intuitive Approach to the Harrison and Kreps Concept of Arbitrage Pricing for Continuous Time Diffusions.” Working Paper, Department of Management, Odense University, Denmark.

Christensen, P., S. Graversen, and K. Miltersen. (1996). “Dynamic Spanning in the Consumption-Based Capital Asset Pricing Model.” Working Paper, Department of Management, Odense University, Denmark.

Chuang, C. (1994). “Joint Distribution of Brownian Motion and Its Maximum, with a Generalization to Correlated BM and Applications to Barrier Options.” Working Paper, Department of Statistics, Stanford University.

Chung, K. (1982). Lectures from Markov Processes to Brownian Motion. New York: Springer-Verlag.

Chung, K-L. (1974). A Course in Probability Theory (2d ed.). New York: Academic Press.

Chung, K-L., and R. Williams. (1990). An Introduction to Stochastic Integration (2d ed.). Boston: Birkhauser.

Citanna, A., A. Kajii, and A. Villanacci. (1994). “Constrained Suboptimality in Incomplete Markets: A General Approach and Two Applications.” Economic Theory 11: 495-521.

Citanna, A., and A. Villanacci. (1993). “On Generic Pareto ImprovementBibliography 391

Constantinides, G. (1986). “Capital Market Equilibrium with Transaction Costs.” Journal of Political Economy 94: 842-862.

Constantinides, G. (1990). “Habit Formation: A Resolution of the Equity Premium Puzzle.”
Journal of Political Economy 98: 519-543.

Constantinides, G. (1992). “A Theory of the Nominal Term Structure of Interest Rates.”
Review of Financial Studies 5: 531-552.

Constantinides, G. (1993). “Option Pricing Bounds with Transactions Costs.” Working Paper,
Graduate School of Business, University of Chicago.

Constantinides, G., and D. Duffie. (1996). “Asset Pricing with Heterogeneous Consumers.”
Journal of Political Economy 104: 219-240.

Constantinides, G., and T. Zariphopoulou. (1999). “Bounds on Prices of Contingent Claims in an Intertemporal Economy with Proportional Transaction Costs and General Preferences.” Finance and Stochastics 3: 345-369.

Cont, R. (1998). “Modeling Term Structure Dynamics: An Infinite Dimensional Approach.”
Working Paper, Centre de Mathématiques Appliquées, Ecole Polytechnique, Palaiseau, France.

Conze, A., and R. Viswanathan. (1991a). “Path Dependent Options: The Case of Lookback Options.” Journal of Finance 5: 1893-1907.

Conze, A., and R. Viswanathan. (1991b). “Probability Measures and Numeraires.” Working Paper, CEREMADE, Université de Paris.

Cooper, I., and M. Martin. (1996). “Default Risk and Derivative Products.” Applied Mathematical Finance 3: 53-74.

Cooper, I., and A. Mello. (1991). “The Default Risk of Swaps.” Journal of Finance 46: 597-620.

Cooper, I., and A. Mello. (1992). “Pricing and Optimal Use of Forward Contracts with
Default Risk.” Working Paper, Department of Finance, London Business School, University of London.

Cornell, B. (1981). “The Consumption Based Asset Pricing Model.” Journal of Financial Economics 9: 103-108.

Corradi, V. (2000). “Degenerate Continuous Time Limits of GARCH and GARCH-type Processes.” Journal of Econometrics 96: 145-153.

Courtadon, G. (1982). “The Pricing of Options on Default-Free Bonds.” Journal of Financial and Quantitative Analysis 17: 75-100.

Cover, T., and E. Ordentlich. (1996). “Universal Portfolios with Side Information.” IEEE Transactions on Information Theory 42: 348-363.

Cox, J. (1983). “Optimal Consumption and Portfolio Rules when Assets Follow a Diffusion
Process.” Working Paper, Graduate School of Business, Stanford University.

Cox, J., and C.-F. Huang. (1989). “Optimal Consumption and Portfolio Policies when Asset
Prices Follow a Diffusion Process.” Journal of Economic Theory 49: 33-83.

Cox, J., and C.-F. Huang. (1991). “A Variational Problem Arising in Financial Economics with an Application to a Portfolio Turnpike Theorem.” Journal of Mathematical Economics 20: 465-488.

Cox, J., and C.-F. Huang. (1992). “A Continuous-Time Portfolio Turnpike Theorem.” Journal of Economic Dynamics and Control 16: 491-508.

Cox, J., J. Ingersoll, and S. Ross. (1981a). “A Re-examination of Traditional Hypotheses about the Term Structure of Interest Rates.” Journal of Finance 36: 769-799.

Cox, J., J. Ingersoll, and S. Ross. (1981b). “The Relation between Forward Prices and Futures
Prices.” Journal of Financial Economics 9: 321-346.

Cox, J., J. Ingersoll, and S. Ross. (1985a). “An Intertemporal General Equilibrium Model of Asset Prices.” Econometrica 53: 363-384.

Cox, J., J. Ingersoll, and S. Ross. (1985b). “A Theory of the Term Structure of Interest Rates.”
Econometrica 53: 385-408.

Cox, J., and S. Ross. (1976). “The Valuation of Options for Alternative Stochastic Processes.”
Journal of Financial Economics 3: 145-166.

Cox, J., S. Ross, and M. Rubinstein. (1979). “Option Pricing: A Simplified Approach.” Journal of Financial Economics 7: 229-263.

Cox, J., and M. Rubinstein. (1985). Options Markets. Englewood Cliffs, NJ: Prentice-Hall.

Cuoco, D. (1997). “Optimal Consumption and Equilibrium Prices with Portfolio Constraints and Stochastic Income.” Journal of Economic Theory 72: 33-73.

Cuoco, D., and J. Cvitanić. (1998). “Optimal Consumption Choices for a ‘Large’ Investor.”
Journal of Economic Dynamics and Control 22: 401-436.

Cuoco, D., and H. He. (1992a). “Dynamic Aggregation and Computation of Equilibria in Finite-Dimensional Economies with Incomplete Financial Markets.” Working
Paper, Haas School of Business, University of California, Berkeley.

Cuoco, D., and H. He. (1992b). “Dynamic Equilibrium in Infinite-Dimensional Economies with Incomplete Financial Markets.” Working Paper, Wharton School, University of Pennsylvania.

Cuoco, D., and H. Liu. (2000). “Optimal Consumption of a Divisible Durable Good.” Journal of Economic Dynamics and Control 24: 561-613.

Cuoco, D., and F. Zapatero. (2000). “On the Recoverability of Preferences and Beliefs in
Financial Models.” Review of Financial Studies 13: 417-431.

Curran, M. (1996). “Adaptive Importance Sampling for Pricing Path Dependent Options.”
Working Paper, Banque Paribas, London.

Cutland, N., P. Kopp, and W. Willinger. (1991). “A Nonstandard Approach to Option Pricing.” Mathematical Finance 1: 1-38.

Cutland, N., P. Kopp, and W. Willinger. (1993a). “From Discrete to Continuous Financial
Models: New Convergence Results for Options Pricing.” Mathematical Finance 3: 101-124.

Cutland, N., P. Kopp, and W. Willinger. (1993b). “Stock Price Returns and the Joseph Effect:
Fractional Version of the Black-Scholes Model.” Working Paper, School of Mathematics, University of Hull, England.

Cvitanić, J. (1995). “Nonlinear Financial Markets: Hedging and Portfolio Optimization.” In
Mathematics of Derivative Securities, pp.27-254. Cambridge: Cambridge University Press.

Cvitanić, J. (1997). Optimal Trading under Constraints. Lecture Notes in Mathematics 1656.
New York: Springer-Verlag.

Cvitanić, J. (1999). “Methods of Partial Hedging.” Asia-Pacific Financial Markets 6: 7-35.

Cvitanić, J., and I. Karatzas. (1992). “Convex Duality in Constrained Portfolio Optimization.”
Annals of Applied Probability 2: 767-818.

Cvitanić, J., and I. Karatzas. (1993). “Hedging Contingent Claims with Constrained Portfolios.” Annals of Applied Probability 3: 652-681.

Cvitanić, J., and I. Karatzas. (1995). “On Portfolio Optimization under ‘Drawdown’ Constraints.” IMA Volumes in Mathematics and its Applications 65: 35-46.

Cvitanić, J., and I. Karatzas. (1996a). “Backward Stochastic Differential Equations with Reflection and Dynkin Games.” Annals of Probability 24: 2024-2056.

Cvitanić, J., and I. Karatzas. (1996b). “Hedging and Portfolio Optimization under Transaction Costs: A Martingale Approach.” Mathematical Finance 6: 133-165.

Cvitanić, J., I. Karatzas and M. Soner. (1998). “Backward Stochastic Differential Equations with Constraints on the Gains-Process.” Annals of Probability 26: 1522-1551.

Cvitanić, J., and J. Ma. (1996). “Hedging Options for a Large Investor and Forward-Backward SDEs.” Annals of Applied Probability 6: 370-398.

Cvitanić, J., W. Schachermayer, and H. Wang. (1999). “Utility Maximization in Incomplete
Markets with Random Endowment.” Working Paper, Department of Mathematics, University of Southern California. Forthcoming in Finance and Stochastics.

Daher, C., M. Romano, and G. Zacklad. (1992). “Determination du Prix de Produits Optionnels Obligatoires à Partir d’un Modèle Multi-Facteurs de la Courbe des Taux.”
Working Paper, Caisse Autonome de Refinancement, Paris.

Dai, Q. (1994). “Implied Green’s Function in a No-Arbitrage Markov Model of the Instantaneous Short Rate.” Working Paper, Graduate School of Business, Stanford University.

Dai, Q. (1995). “Understanding the Interest Rate Yield Curve Dynamics with the Correlated Three-Factor Vasicek Model.” Working Paper, Graduate School of Business, Stanford University.

Dai, Q. (1996). “Technical Notes on CIR Model.” Working Paper, Graduate School of Business, Stanford University.

Dai, Q. (2000). “From Equity Premium Puzzle to Expectations Puzzle: A General Equilibrium
Production Economy with Stochastic Habit Formation.” Working Paper, Stern
School, New York University.Dai, Q., and K. Singleton. (2000). “Specification Analysis of Affine Term Structure Models.”
Journal of Finance 55: 1943-1978.

Daigler, R. (1993). Financial Futures Markets. New York: Harper Collins.

Dalang, R., A. Morton, and W. Willinger. (1990). “Equivalent Martingale Measures and NoArbitrage in Stochastic Securities Market Models.” Stochastics and Stochastic Reports 29: 185-201.

Daley, D., and D. VereJones. (1988). An Introduction to the Theory of Point Processes. New York: Springer-Verlag.

Dana, R., and M. Jeanblanc. (1998). Marchés Financiers en Temps Continu (2d ed.). Paris: Economica.

Dana, R.-A. (1993a). “Existence and Uniqueness of Equilibria when Preferences are Additively Separable.” Econometrica 61: 953-958.

Dana, R.-A. (1993b). “Existence, Uniqueness and Determinacy of Arrow-Debreu Equilibria in Finance Models.” Journal of Mathematical Economics 22: 563-580.

Dana, R.-A., and C. Le Van. (1996). “Asset Equilibria in L² Spaces with Complete Markets:
A Duality Approach.” Journal of Mathematical Economics 25: 263-280.

Dana, R.-A., and M. Pontier. (1990). “On the Existence of a Stochastic Equilibrium.” Working Paper, Université de Paris VI, Paris.

Danesi, V., J.-P. Garcia, V. Genon-Catalot, and J.-P. Laurent. (1993). “Parameter Estimation for
Yield Curve Models using Contrast Methods.” Working Paper, Université MarneLa-Vallée, Noisy-Le-Grand, France.

Darling, R. (1995). “Constructing Gamma-Martingales with Prescribed Limit, Using Backward SDE.” Annals of Probability 3: 431-454.

Das, S. (1993a). “Jump-Diffusion Processes and the Bond Markets.” Working Paper, Department of Finance, Harvard Business School.

Das, S. (1993b). “Jump-Hunting Interest Rates.” Working Paper, Department of Finance, New York University.

Das, S. (1993c). “Mean Rate Shifts and Alternative Models of the Interest Rate: Theory and
Evidence.” Working Paper, Department of Finance, New York University.

Das, S. (1995). “Pricing Interest Rate Derivatives with Arbitrary Skewness and Kurtosis: A Simple Approach to Jump-Diffusion Bond Option Pricing.” Working Paper, Division of Research, Harvard Business School.

Das, S. (1997). “Discrete-Time Bond and Option Pricing for Jump-Diffusion Processes.”
Review of Derivatives Research 1: 211-243.

Das, S. (1998). “Poisson-Gaussian Processes and the Bond Markets.” Working Paper, Department of Finance, Harvard Business School.

Das, S., and S. Foresi. (1996). “Exact Solutions for Bond and Option Prices with Systematic
Jump Risk.” Review of Derivatives Research 1: 7-24.

Das, S., and R. K. Sundaram. (2000). “A Discrete-Time Approach to Arbitrage-Free Pricing of Credit Derivatives.” Management Science 46: 46-62.

Das, S., and P. Tufano. (1995). “Pricing Credit Sensitive Debt when Interest Rates, Credit
Ratings and Credit Spreads are Stochastic.” Journal of Financial Engineering 5(2): 161-198.

Dash, J. (1989). “Path Integrals and Options—I.” Working Paper, Financial Strategies Group, Merrill Lynch Capital Markets, New York.

Dassios, A. (1994). “The Distribution of the Quantiles of a Brownian Motion with Drift and the Pricing of Related Path-Dependent Options.” Working Paper, Department of Statistics, London School of Economics.

Davis, M. (1998). “A Note on the Forward Measure.” Finance and Stochastics 2: 19-28.

Davis, M., and M. Clark. (1993). “Analysis of Financial Models including Transactions Costs.”
Working Paper, Imperial College, University of London.

Davis, M., and F. Lischka. (1999). “Convertible Bonds with Market Risk and Credit Risk.”
Working Paper, Tokyo-Mitsubishi International plc.

Davis, M., and V. Lo. (1999). “Infectious Defaults.” Working Paper, Tokyo-Mitsubishi International plc.

Davis, M., and V. Lo. (2000). “Modelling Default Correlation in Bond Portfolios.” Working Paper, Tokyo-Mitsubishi International plc.

Davis, M., and T. Mavroidis. (1997). “Valuation and Potential Exposure of Default
Swaps.” Working Paper, Research and Product Development, Tokyo-Mitsubishi International plc.

Davis, M., and A. Norman. (1990). “Portfolio Selection with Transaction Costs.” Mathematics of Operations Research 15: 676-713.

Davis, M., and V. Panas. (1991). “European Option Pricing with Transaction Costs.” Proceedings of the Thirtieth IEEE Conference on Decision and Control, Brighton, December, pp.299-1304.

Davis, M., A. Panas, and T. Zariphopoulou. (1993). “European Option Pricing with Transaction Costs.” SIAM Journal of Control and Optimization 31: 470-493.

Davydov, D., and V. Linetsky. (1998). “Double Step Options.” Working Paper, University of
Michigan. Forthcoming in Journal of Computational Finance.

Davydov, D., and V. Linetsky. (1999a). “Pricing Options on One-Dimensional Diffusions: A
Sturm-Liouville Approach.” Working Paper, University of Michigan.

Davydov, D., and V. Linetsky. (1999b). “The Valuation and Hedging of Barrier and Lookback Options for Alternative Stochastic Processes.” Working Paper, University of Michigan.

Davydov, D., V. Linetsky, and C. Lotz. (1999). “The Hazard-Rate Approach to Pricing Risky
Debt: Two Analytically Tractable Examples.” Working Paper, Department of Economics, University of Michigan.

Debreu, G. (1953). “Une Economie de l'Incertain.” Working Paper, Electricité de France.

Debreu, G. (1954). “Valuation Equilibrium and Pareto Optimum.” Proceedings of the National Academy of Sciences 40: 588-592.

Debreu, G. (1959). Theory of Value. Cowles Foundation Monograph 17. New Haven, CT: Yale University Press.

Debreu, G. (1972). “Smooth Preferences.” Econometrica 40: 603-615; Corrigendum 44 (1976): 831-832.

Debreu, G. (1982). “Existence of Competitive Equilibrium.” In K. Arrow and M. Intriligator
(Eds.), Handbook of Mathematical Economics, Volume II, pp.97-743. Amsterdam: North-Holland.

Décamps, J.-P., and A. Faure-Grimaud. (1998). “Pricing the Gamble for Resurrection and the
Consequences of Renegotiation and Debt Design.” Working Paper, University of Toulouse.

Décamps, J.-P., and A. Faure-Grimaud. (1999). “Should I Stay or Should I Go? Excessive
Continuation and Dynamic Agency Costs of Debt.” Working Paper, University of Toulouse.

Décamps, J.-P., and P. Koehl. (1994). “Pricing and Hedging Asian Options: A PDE Approach.”
Working Paper, GREMAQ, Université des Sciences Sociales.

Décamps, J.-P., and J.-C. Rochet. (1997). “A Variational Approach for Pricing Options and Corporate Bonds.” Economic Theory 9: 557-569.

Deelstra, G., and F. Delbaen. (1994). “Existence of Solutions of Stochastic Differential Equations Related to the Bessel Process.” Working Paper, Department of Mathematics, Vrije Universiteit Brussel.

Deelstra, G., and F. Delbaen. (1995). “Long-Term Returns in Stochastic Interest Rate Models.” Insurance: Mathematics and Economics 17: 163-169.

Dekel, E. (1989). “Asset Demands without the Independence Axiom.” Econometrica 57: 163-169.

Delbaen, F. (1992). “Representing Martingale Measures when Asset Prices are Continuous and Bounded.” Mathematical Finance 2: 107-130.

Delbaen, F. (1993). “Consols in the CIR Model.” Mathematical Finance 3: 125-134.

Delbaen, F., P. Monat, W. Schachermayer, M. Schweizer, and C. Stricker. (1994). “Inégalités de Normes avec Poids et Fermeture d’un Espace d’Intégrales Stochastiques.”
Comptes Rendus de l’Académie des Sciences de Paris 319: 1079-1081.

Delbaen, F., and W. Schachermayer. (1994a). “Arbitrage and Free Lunch with Bounded Risk for Unbounded Continuous Processes.” Mathematical Finance 4: 343-348.

Delbaen, F., and W. Schachermayer. (1994b). “A General Version of the Fundamental Theorem of Asset Pricing.” Mathematische Annalen 300: 463-520.

Delbaen, F., and W. Schachermayer. (1995a). “Arbitrage Possibilities in Bessel Processes and
Their Relations to Local Martingales.” Probability Theory and Related Fields 102: 357-366.

Delbaen, F., and W. Schachermayer. (1995b). “The Existence of Absolutely Continuous LocalUniversity Press.

Duffie, D. (1996). “Special Repo Rates.” Journal of Finance 51: 493-526.

Duffie, D. (1998a). “Defaultable Term Structures with Fractional Recovery of Par.” Working
Paper, Graduate School of Business, Stanford University.

Duffie, D. (1998b). “First to Default Valuation.” Working Paper, Graduate School of Business, Stanford University.

Duffie, D., and L. Epstein. (1992a). “Asset Pricing with Stochastic Differential Utility.” Review of Financial Studies 5: 411-436.

Duffie, D., and L. Epstein. (1992b). “Stochastic Differential Utility.” Econometrica 60: 353-394;
Appendix with C. Skiadas.

Duffie, D., W. Fleming, M. Soner, and T. Zariphopoulou. (1997). “Hedging in Incomplete
Markets with HARA Utility.” Journal of Economic Dynamics and Control 21: 753-782.

Duffie, D., and N. Garleanu. (2001). “Risk and Valuation of Collateralized Debt Valuation.”
Financial Analysts Journal, 57: 41-62.

Duffie, D., and M. Garman. (1991). “Intertemporal Arbitrage and the Markov Valuation of
Securities.” Cuadernos economicos de ICE 49: 37-60.

Duffie, D., J. Geanakoplos, A. Mas-Colell, and A. McLennan. (1994). “Stationary Markov Equilibria.” Econometrica 62: 745-781.

Duffie, D., P-Y. Geoffard, and C. Skiadas. (1994). “Efficient and Equilibrium Allocations with
Stochastic Differential Utility.” Journal of Mathematical Economics 23: 133-146.

Duffie, D., and P. Glynn. (1995). “Efficient Monte Carlo Estimation of Security Prices.” Annals of Applied Probability 5: 897-905.

Duffie, D., and M. Harrison. (1993). “Arbitrage Pricing of Russian Options and Perpetual
Lookback Options.” Annals of Applied Probability 3: 641-651.

Duffie, D., and C.-F. Huang. (1985). “Implementing Arrow-Debreu Equilibria by Continuous
Trading of Few Long-Lived Securities.” Econometrica 53: 1337-1356.

Duffie, D., and C.-F. Huang. (1986). “Multiperiod Security Markets with Differential Information: Martingales and Resolution Times.” Journal of Mathematical Economics 15: 283-303.

Duffie, D., and M. Huang. (1996). “Swap Rates and Credit Quality.” Journal of Finance 51: 921-949.

Duffie, D., and M. Jackson. (1990). “Optimal Hedging and Equilibrium in a Dynamic Futures
Market.” Journal of Economic Dynamics and Control 14: 21-33.

Duffie, D., and R. Kan. (1996). “A Yield-Factor Model of Interest Rates.” Mathematical Finance
6: 379-406; reprinted in Options Markets, edited by G. Constantinides and A.
Malliaris, London: Edward Elgar, 2000.

Duffie, D., and D. Lando. (1998). “Term Structures of Credit Spreads with Incomplete
Accounting Information.” Working Paper, Graduate School of Business, Stanford University. Forthcoming in Econometrica.

Duffie, D., and P-L. Lions. (1990). “PDE Solutions of Stochastic Differential Utility.” Journal of Mathematical Economics 21: 577-606.

Duffie, D., J. Ma, and J. Yong. (1995). “Black’s Consol Rate Conjecture.” Annals of Applied Probability 5: 356-382.

Duffie, D., J. Pan, and K. Singleton. (2000). “Transform Analysis and Asset Pricing for Affine Jump-Diffusions.” Econometrica 68: 1343-1376.

Duffie, D., L. Pedersen, and K. Singleton. (2000). “Modeling Sovereign Yield Spreads: A Case

Study of Russian Debt.” Working Paper, Graduate School of Business, Stanford University.

Duffie, D., and P. Protter. (1988). “From Discrete to Continuous Time Finance: Weak Convergence of the Financial Gain Process.” Mathematical Finance 2: 1-16.

Duffie, D., and H. Richardson. (1991). “Mean-Variance Hedging in Continuous Time.”
Annals of Applied Probability 1: 1-15.

Duffie, D., M. Schroder, and C. Skiadas. (1996). “Recursive Valuation of Defaultable Securities and the Timing of the Resolution of Uncertainty.” Annals of Applied Probability 6: 1075-1090.

Duffie, D., M. Schroder, and C. Skiadas. (1997). “A Term Structure Model with Preferences for the Timing of Resolution of Uncertainty.” Economic Theory 9: 3-22.

Duffie, D., and W. Shafer. (1985). “Equilibrium in Incomplete Markets I: A Basic Model of
Generic Existence.” Journal of Mathematical Economics 14: 285-300.

Duffie, D., and W. Shafer. (1986a). “Equilibrium and the Role of the Firm in Incomplete
Markets.” Working Paper, Graduate School of Business, Stanford University.

Duffie, D., and W. Shafer. (1986b). “Equilibrium in Incomplete Markets II: Generic Existence in Stochastic Economies.” Journal of Mathematical Economics 15: 199-216.

Duffie, D., and K. Singleton. (1993). “Simulated Moments Estimation of Markov Models of Asset Prices.” Econometrica 61: 929-952.

Duffie, D., and K. Singleton. (1997). “An Econometric Model of the Term Structure of
Interest Rate Swap Yields.” Journal of Finance 52: 1287-1321; reprinted in Options
Markets, edited by G. Constantinides and A. Malliaris, London: Edward Elgar, 2001.

Duffie, D., and K. Singleton. (1999). “Modeling Term Structures of Defaultable Bonds.”
Review of Financial Studies 12: 687-720.

Duffie, D., and C. Skiadas. (1994). “Continuous-Time Security Pricing: A Utility Gradient
Approach.” Journal of Mathematical Economics 23: 107-132.

Duffie, D., and R. Stanton. (1988). “Pricing Continuously Resettled Contingent Claims.”
Journal of Economic Dynamics and Control 16: 561-574.

Duffie, D., and T.-S. Sun. (1990). “Transactions Costs and Portfolio Choice in a DiscreteContinuous Time Setting.” Journal of Economic Dynamics and Control 14: 35-51.

Duffie, D., and W. Zame. (1989).“ The Consumption-Based Capital Asset Pricing Model.”
Econometrica 57: 1279-1297.

Duffie, D., and T. Zariphopoulou. (1993). “Optimal Investment with Undiversifiable Income Risk.” Mathematical Finance 3: 135-148.

Dumas, B. (1989). “Two-Person Dynamic Equilibrium in the Capital Market.” Review of Financial Studies 2: 157-188.

Dumas, B., and E. Luciano. (1989). “An Exact Solution to a Dynamic Portfolio Choice Problem under Transactions Costs.” Journal of Finance 46: 577-595.

Dumas, B., R. Uppal, and T. Wang. (2000). “Efficient Intertemporal Allocations with Recursive Utility.” Journal of Economic Theory 93: 240-259.

Dunn, K., and K. Singleton. (1986). “Modeling the Term Structure of Interest Rates under
Nonseparable Utility and Durability of Goods.” Journal of Financial Economics 17: 27-55.

Dupire, B. (1994b). “Pricing with a Smile.” Risk January: 18-20.

Durrett, R. (1991). Probability: Theory and Examples, Belmont, CA: Wadsworth Publishing Co.

Dybvig, P. (1988). “Bond and Bond Option Pricing Based on the Current Term Structure.”
Working Paper, School of Business, Washington University, St. Louis.

Dybvig, P. (1989). “Hedging Nontraded Wealth.” Working Paper, School of Business, Washington University, St. Louis.

Dybvig, P. (1995). “Duesenberry’s Ratcheting of Consumption: Optimal Dynamic Consumption and Investment Given Intolerance for Any Decline in Standard of Living.”
Review of Economic Studies 62: 287-313.

Dybvig, P., and C.-F. Huang. (1988). “Nonnegative Wealth, Absence of Arbitrage, and Feasible
Consumption Plans.” Review of Financial Studies 1: 377-401.

Dybvig, P., J. Ingersoll, and S. Ross. (1996). “Long Forward and Zero-Coupon Rates Can Never Fall.” Journal of Business 69: 1-25.

Dybvig, P., C. Rogers, and K. Back. (1999). “Portfolio Turnpikes.” Review of Financial Studies

12: 165-195.
Dynkin, E., and A. Yushkevich. (1979). Controlled Markov Processes. Berlin, New York: SpringerVerlag.

Eberlein,cesses.” Mathematical Finance 9: 31-53.

Ederington, L., G. Caton, and C. Campbell. (1997). “To Call or Not to Call Convertible Debt.” Financial Management 26: 22-31.

Edirisinghe, C., V. Naik, and R. Uppal. (1993). “Optimal Replication of Options with Transactions Costs.” Journal of Financial and Quantitative Analysis 28: 117-138.

Ekern, S. (1993). “Entry and Exit Decisions with Restricted Reversibility.” Working Paper, Norwegian School of Economics, Bergen.

El Karoui, N. (1997). “Backward Stochastic Differential Equations: A General Introduction.”
In N. El Karoui and L. Mazliak (Eds.), Backward Stochastic Differential Equations, pp.-26. Essex: Addison Wesley Longman Ltd.

El Karoui, N., A. Frachot, and H. Geman. (1997). “On the Behavior of Long Zero Coupon
Rates in a No Arbitrage Framework.” Review of Derivatives Research 1: 351-369.

El Karoui, N., and H. Geman. (1994). “A Probabilistic Approach to the Valuation of General
Floating-Rate Notes with an Application to Interest Rate Swaps.” Advances in Futures and Options Research 7: 47-63.

El Karoui, N., and S.J. Huang. (1997). “A General Result of Existence and Uniqueness of Backward Stochastic Differential Equations.” In N. El Karoui and L. Mazliak
(Eds.), Backward Stochastic Differential Equations, pp.7-36. Essex: Addison Wesley Longman Ltd.

El Karoui, N., and M. Jeanblanc. (1998). “Optimization of Consumption with Labor Income.”
Finance and Stochastics 2: 409-440.

El Karoui, N., M. Jeanblanc, and S. Shreve. (1998). “Robustness of the Black-Scholes Formula.” Mathematical Finance 8: 93-126.

El Karoui, N., C. Kapoudjian, E. Pardoux, S. Peng, and M. Quenez. (1997). “Reflected Solutions of Backward SDE’s, and Related Obstacle Problems for PDE’s.” Annals of Probability 2: 702-737.

El Karoui, N., and V. Lacoste. (1992). “Multifactor Models of the Term Structure of Interest
Rates.” Working Paper, Laboratoire de Probabilités, Université de Paris VI.

El Karoui, N., C. Lepage, R. Myneni, N. Roseau, and X Viswanathan. (1991a).“The Pricing and Hedging of Interest Rate Claims: Applications.” Working Paper, Laboratoire de Probabilités, Université de Paris VI.

El Karoui, N., C. Lepage, R. Myneni, N. Roseau, and R. Viswanathan. (1991b). “The Valuation and Hedging of Contingent Claims with Gaussian Markov Interest Rates.”
Working Paper, Laboratoire de Probabilités, Université de Paris VI.

El Karoui, N., R. Myneni, and R. Viswanathan. (1992). “Arbitrage Pricing and Hedging of
Interest Rate Claims with State Variables I: Theory.” Working Paper, Laboratoire de Probabilités, Université de Paris VI.

El Karoui, N., S. Peng, and M. Quenez. (1997). “Backward Stochastic Differential Equations in Finance.” Mathematical Finance 1: 1-71.

El Karoui, N., and M. Quenez. (1991). “Programmation Dynamique et Evaluation des Actifs
Contingents en Marché Incomplet.” Comtes Rendus de l’Academie de Science de Paris 3131: 851-854.

El Karoui, N., and M. Quenez. (1995). “Dynamic Programming and Pricing of Contingent
Claims in an Incomplete Market.” SIAM Journal of Control and Optimzation 33: 29-66.

El Karoui, N., and J.-C. Rochet. (1989). “A Pricing Formula for Options on Coupon Bonds.”
Working Paper, October, Laboratoire de Probabilités, Université de Paris VI.

Elliot, R., and J. Van der Hoek. (1999). “Stochastic Flows and the Forward Measure.” Working Paper, Department of Mathematical Sciences, University of Alberta, Canada.
Forthcoming, in Finance and Stochastics.

Elliott, R., M. Jeanblanc, and M. Yor. (1999). “Some Models on Default Risk.” Working Paper,
Department of Mathematics, University of Alberta. Forthcoming in Mathematical Finance.

Engle, R.(1982). “Autoregressive Conditional Heteroskedasticity with Estimates of the Variance of United Kingdom Inflation.” Econometrica 50: 987-1008.

Epstein, L. (1988). “Risk Aversion and Asset Prices.” Journal of Monetary Economics 22: 179-192.

Epstein, L. (1992). “Behavior under Risk: Recent Developments in Theory and Application.”
In J. Laffont (Ed.), Advances in Economic Theory, pp.-63. Cambridge: Cambridge University Press.

Epstein, L., and A. Melino. (1995). “A Revealed Preference Analysis of Asset Pricing under
Recursive Utility.” Review of Economic Studies 62: 597-618.

Epstein, L., and T. Wang. (1994). “Intertemporal Asset Pricing under Knightian Uncertainty.”
Econometrica 62: 283-322.

Epstein, L., and S. Zin. (1989). “Substitution, Risk Aversion and the Temporal Behavior of
Consumption and Asset Returns I: A Theoretical Framework.” Econometrica 57: 937-969.

Epstein, L., and S. Zin. (1999). “Substitution, Risk Aversion and the Temporal Behavior of Consumption and Asset Returns: An Empirical Analysis.” Journal of Political Economy 99: 263-286.

Eraker, B., M. Johannes, and N. Polson. (1999). “Asset Return Dynamics with Jumps, Stochastic Volatility and Jumps to Volatility.” Working Paper, Norwegian School of Economics and University of Chicago.

Ericsson, J., and O. Renault. (1999). “Credit and Liquidity Risk.” Working Paper, Faculty of Management, McGill University.

Ethier, S., and T. Kurtz. (1986). Markov Processes: Characterization and Convergence. New York: Wiley.

Eydeland, A. (1994a). “A Fast Algorithm for Computing Integrals in Function Spaces: Financial Applications.” Working Paper, Fuji Capital Markets Corporation, New York.

Eydeland, A. (1994b). “A Spectral Algorithm for Pricing Interest Rate Options.” Working
Paper, Department of Mathematics, University of Massachusetts.

Fan, H., and S. Sundaresan. (1997). “Debt Valuation, Strategic Debt Service and Optimal
Dividend Policy.” Working Paper, Columbia University.

Feller, W. (1951). “Two Singular Diffusion Problems.” Annals of Mathematics 54: 173-182.

Filipovic, D. (1999a). “A General Characterization of Affine Term Structure Models.” Working Paper, ETH, Zurich. Forthcoming in Finance and Stochastics.

Filipovic, D. (1999b). “A Note on the Nelson-Siegel Family.” Mathematical Finance 9: 349-359.

Finger, C. (2000). “A Comparison of Stochastic Default Rate Models.” Working Paper, The Risk Metrics Group.

Fisher, E., R. Heinkel, and J. Zechner. (1989). “Dynamic Capital Structure Choice: Theory and Tests.” Journal of Finance 44: 19-40.

Fisher, M., and C. Gilles. (1996). “The Term Structure of Repo Spreads.” Working Paper,
Research and Statistics, Board of Governors of the Federal Reserve System.

Fisher, M., and C. Gilles. (1997). “The Equity Premium and the Term Structure of Interest
Rates with Recursive Preferences.” Working Paper, Research and Statistics, Board of Governors of the Federal Reserve System.

Fisher, M., and C. Gilles. (1998a). “Around and Around: The Expectations Hypothesis.”
Journal of Finance 53: 365-383.

Fisher, M., and C. Gilles. (1998b). “Consumption and Asset Prices with Recursive Preferences.” Working Paper, Board of Governors of the Federal Reserve System.

Fisher, M., D. Nychka, and D. Zervos. (1994). “Fitting the Term Structure of Interest Rates with Smoothing Splines.” Working Paper, Board of Governors of the Federal Reserve Board, Washington D.C.

Fitzpatrick, B., and W. Fleming. (1991). “Numerical Methods for Optimal Investment—
Consumption Models.” Mathematics of Operations Research 16: 823-841.

Fleming, J., and R. Whaley. (1994). “The Value of Wildcard Options.” Journal of Finance 1: 215-236.

Fleming, W., S. Grossman, J.-L. Vila, and T. Zariphopoulou. (1989). “Optimal Portfolio Rebalancing with Transaction Costs.” Working Paper, Department of Applied Mathematics, Brown University.

Fleming, W., and R. Rishel. (1975). Deterministic and Stochastic Optimal Control. Berlin: Springer-Verlag.

Fleming, W., and M. Soner. (1993). Controlled Markov Processes and Viscosity Solutions. New York: Springer-Verlag.

Fleming, W., and T. Zariphopoulou. (1991). “An Optimal Investment/Consumption Model with Borrowing Constraints.” Mathematics of Operations Research 16: 802-822.Flesaker, B. (1991). “Valuing European Options when the Terminal Value of the Underlying Asset is Unobservable.” Working Paper, Department of Finance, University of Illinois at Urbana-Champaign.

Flesaker, B. (1993). “Testing the Heath-Jarrow-Morton/Ho-Lee Model of Interest Rate Contingent Claims Pricing.” Journal of Financial and Quantitative Analysis 28: 483-495.

Florenzano, M., and P. Gourdel. (1993). “Incomplete Markets in Infinite Horizon: Debt Constraints versus Node Prices.” Mathematical Finance 6: 167-196.

Florenzano, M., and P. Gourdel. (1994). “T-Period Economies with Incomplete Markets.” Economics Letters 44: 91-97.

Foldes, L. (1978a). “Martingale Conditions for Optimal Saving—Discrete Time.” Journal of Mathematical Economics 5: 83-96.

Foldes, L. (1978b). “Optimal Saving and Risk in Continuous Time.” Review of Economic Studies 45: 39-65.

Foldes, L. (1990). “Conditions for Optimality in the Infinite-Horizon Portfolio-Cum-Saving Problem with Semimartingale Investments.” Stochastics and Stochastics Reports 29: 133-170.

Foldes, L. (1991a). “Certainty Equivalence in the Continuous-Time Portfolio-Cum-Saving Model.” In Applied Stochastic Analysis. London: Gordon and Breach.

Foldes, L. (1991b). “Optimal Sure Portfolio Plans.” Mathematical Finance 1: 15-55.

Foldes, L. (1992). “Existence and Uniqueness of an Optimum in the Infinite-Horizon Portfolio-Cum-Saving Model with Semimartingale Investments.” Stochastic and Stochastic Reports 41: 241-267.

Foldes, L. (1996). “The Optimal Consumption Function in a Brownian Model of Accumulation, Part A: The Consumption Function as Solution of a Boundary Value Problem.” Working Paper, London School of Economics and Political Science.

Föllmer, H. (1981). “Calcul d’Ito Sans Probabilities.” In J. Azéma and M. Yor (Eds.), Séminaire de Probabilités XV. Lecture Notes in Mathematics, pp.43-150. Berlin: Springer-Verlag.

Föllmer, H. (1993). “A Microeconomic Approach to Diffusion Models for Stock Prices.” Mathematical Finance 3: 1-23.

Föllmer, H., and M. Schweizer. (1990). “Hedging of Contingent Claims under Incomplete Information.” In M. Davis and R. Elliott (Eds.), Applied Stochastic Analysis, pp.89-414. London: Gordon and Breach.

Föllmer, H., and D. Sondermann. (1986). “Hedging of Non-Redundant Contingent Claims.” In W. Hildenbrand and A. Mas-Colell (Eds.), Contributions to Mathematical Economics, pp.05-224. Amsterdam: North-Holland.

Fournié, E. (1993). “Statistiques des Diffusions Ergodiques avec Applications en Finance.” Working Paper, Université de Nice-Sophia Antipolis.

Fournié, E., and J.-M. Lasry. (1996). “Some Nonlinear Methods to Study Far-from-the-Money Contingent Claims.” Working Paper, Caisse Autonome de Refinancement, Paris.

Fournié, E., J.-M. Lasry, J. Lebuchoux, P.-L. Lions, and N. Touzi. (1999). “Applications of Malliavin Calculus to Monte Carlo Methods in Finance.” Finance and Stochastics 3: 391-412.

Fournié, E., J.-M. Lasry, and N. Touzi. (1996). “Méthode de Monte Carlo pour les Modèles de Volatilité Stochastique.” Working Paper, Caisse Autonome de Refinancement, Paris.

Fournié, E., and D. Talay. (1991). “Application de la Statistique des Diffusions à un Modèle de Taux d’Intérêt.” Finances 12: 79-111.
Frachot, A. (1995). “Factor Models of Domestic and Foreign Interest Rates with Stochastic Volatilities.” Mathematical Finance 5: 167-185.
Frachot, A. (1996). “A Reexamination of the Uncovered Interest Rate Parity Hypothesis.” Journal of International Money and Finance 15: 419-437.
Frachot, A., D. Janci, and V Lacoste. (1993). “Factor Analysis of the Term Structure: A Probabilistic Approach.” Working Paper, Banque de France, Paris.
Frachot, A., and J.-P. Lesne. (1993a). “Econometrics of Linear Factor Models of Interest Rates.” Working Paper, Banque de France, Paris.
Frachot, A., and J.-P. Lesne. (1993b). “Expectations Hypotheses and Stochastic Volatilities.” Working Paper, Banque de France, Paris.
Frachot, A., and J.-P. Lesne. (1993c). “Factor Models of Interest Rates with Stochastic Volatilities.” Working Paper, Banque de France, Paris.
Freedman, D. (1983). Markov Chains. New York: Springer-Verlag.
Freidlin, M. (1985). Functional Integration and Partial Differential Equations. Princeton, NJ.: Princeton University Press.
Frey, R. (1996). “The Pricing and Hedging of Options in Finitely Elastic Markets.” Working Paper, Department of Statistics, Faculty of Economics, University of Bonn.
Frey, R., and C. Sin. (1997). “Bounds on European Option Prices under Stochastic Volatility.” Working Paper, Department Mathematik, ETH Zentrum, Zurich.
Frey, R., and A. Stremme. (1997). “Market Volatility and Feedback Effects from Dynamic Hedging.” Mathematical Finance 7: 351-374.
Friedman, A. (1964). Partial Differential Equations of the Parabolic Type. Englewood Cliffs, N.J.: Prentice-Hall.
Friedman, A. (1975). Stochastic Differential Equations and Applications, Vol. I. New York: Academic Press.
Frittelli, M., and P. Lakner. (1995). “Arbitrage and Free Lunch in a General Financial Market Model; The Fundamental Theorem of Asset Pricing.” Mathematical Finance 5: 237-261.
Fu, M., D. Madan, and T. Wang. (1999). “Pricing Continuous-Time Asian Options: A Comparison of Monte Carlo and Laplace Transform Methods.” Journal of Computational Finance 2 (Winter): 49-74.
Gabay, D. (1982). “Stochastic Processes in Models of Financial Markets.” Proceedings of the IFIP Conference on Control of Distributed Systems, Toulouse. Toulouse, France: Pergamon Press.
Gagnon, J., and J. Taylor. (1990). “Solving Stochastic Equilibrium Models with the Extended Path Method.” Economic Modelling 7: 251-257.
Galai, D., and M. Schneller. (1978). “Pricing of Warrants and the Value of the Firm.” Journal of Finance 33: 1333-1342.
Gale, D. (1960). The Theory of Linear Economic Models. New York: McGraw-Hill.
Gallant, R., and H. White. (1988). A Unified Theory of Estimation and Inference for Nonlinear Dynamic Models. New York: Basil Blackwell.
Gandhi, S., A. Kooros, and G. Salkin. (1993). “An Improved Analytic Approximation for American Option Pricing.” Working Paper, Imperial College, University of London.

Gao, B., J.-Z. Huang, and M. Subrahmanyam. (1996). “An Analytical Approach to the Valuation of American Path-Dependent Options.” Working Paper, Kenan-Flagler Business School, University of North Carolina. Forthcoming in Journal of Economic Dynamics and Control.

Garbade, K. (1996). Fixed Income Analytics. Cambridge, MA: MIT Press.

Garman, M. (1985). “Towards a Semigroup Pricing Theory.” Journal of Finance 40: 847-861.

Gatarek, D., and M. Musiela. (1995). “Pricing of American Receiver Swaptions as Optimal Stopping of an Ornstein-Uhlenbeck Process.” Working Paper, School of Mathematics, University of New South Wales, Sydney.

Geanakoplos, J. (1990). “An Introduction to General Equilibrium with Incomplete Asset Markets.” Journal of Mathematical Economics 19: 1-38.

Geanakoplos, J., and A. Mas-Colell. (1989). “Real Indeterminacy with Financial Assets.” Journal of Economic Theory 47: 22-38.

Geanakoplos, J., and H. Polemarchakis. (1986). “Existence, Regularity, and Constrained Suboptimality of Competitive Allocations when the Asset Market is Incomplete.” In W. Heller and D. Starrett (Eds.), Essays in Honor of Kenneth J. Arrow, Volume III, pp.5-96. Cambridge: Cambridge University Press.

Geanakoplos, J., and W. Shafer. (1990). “Solving Systems of Simultaneous Equations in Economics.” Journal of Mathematical Economics 19: 69-94.

Geanakoplos, J., and W. Zame. (1999). “Collateral, Default, and Market Crashes.” Working Paper, Cowles Foundation Working Paper, Yale University.

Géguout-Petit, A., and E. Pardoux. (1996). “Equations Différentielles Stochastiques Rétrogrades Réfléchies dans un Convexe.” Stochastics and Stochastics Reports 57: 111-128.

Geman, H., N. El Karoui, and J. Rochet. (1995). “Changes of Numéraire, Changes of Probability Measure.”Geman, H., D. Madan, and M. Yor. (1999). “Time Changes for Lévy Processes. Working Paper, Université Paris IX Dauphine and ESSEC.

Geman, H., and M. Yor. (1993). “Bessel Processes, Asian Options and Perpetuities.” Mathematical Finance 3: 349-375.

Gennotte, G. (1986). “Continuous-Time Production Economies under Incomplete Information I: A Separation Theorem.” Journal of Finance 41: 733-746.

Gerber, H., and E. Shiu. (1994). “Option Pricing by Esscher Transforms.” Transactions of the Society of Actuaries 46: 51-92.

Geske, R. (1977). “The Valuation of Corporate Liabilities as Compound Options.” Journal of Financial Economics 7: 63-81.

Geske, R. (1979). “The Valuation of Compound Options.” Journal of Financial Economics 7: 63-81.

Geske, R., and H. Johnson. (1984). “The American Put Option Valued Analytically.” Journal of Finance 39: 1511-1524.

Ghysels, E. (1986). “Asset Prices in an Economy with Latent Technological Shocks—
Econometric Implications of a Discrete Time General Equilibrium Model.” Working Paper, Department of Economics and Centre de Recherche et Développement en Economique, Université de Montréal.

Ghysels, E., C. Gourieroux, and J. Jasiak. (1995). “Market Time and Asset Price Movements
Theory and Estimation.” Working Paper, C.R.D.E., Université de Montreal.

Gibbons, M., and K. Ramaswamy. (1993). “A Test of the Cox-Ingersoll-Ross Model of the
Term Structure of Interest Rates.” Review of Financial Studies 6: 619-658.

Gibbons, M., and T. Sun. (1986). “The Term Structure of Interest Rates: A Simple Exposition of the Cox, Ingersoll, and Ross Model.” Working Paper, Graduate School of Business, Stanford University.

Gibson, R., and S. Sundaresan. (1999). “A Model of Sovereign Borrowing and Sovereign
Yield Spreads.” Working Paper, School of HEC, University of Lausanne.

Gihman, I., and A. Skorohod. (1972). Stochastic Differential Equations. Berlin: Springer-Verlag.
Gilles, C., and S. LeRoy. (1991). “On the Arbitrage Pricing Theory.” Economic Theory 1: 213-230.

Gilles, C., and S. LeRoy. (1992a). “Bubbles and Charges.” International Economic Review 33: 323-339.

Gilles, C., and S. LeRoy. (1992b). “Stochastic Bubbles in Markov Economies.” Working Paper,
Board of Governors of The Federal Reserve System, Washington, D.C.

Gilles, C., and S. LeRoy. (1998). “Arbitrage, Martingales, and Bubbles.” Economics Letters 60: 357-362.

Giovannini, A., and P. Weil. (1989). “Risk Aversion and Intertemporal Substitution in the
Capital Asset Pricing Model.” Working Paper, National Bureau of Economic Research, Cambridge, Massachusetts.

Girotto, B., and F. Ortu. (1994). “Consumption and Portfolio Policies with Incomplete Markets and Short-Sale Contraints in the Finite-Dimensional Case: Some Remarks.”
Mathematical Finance 4: 69-73.

Girotto, B., and F. Ortu. (1996). “Existence of Equivalent Martingale Measures in Finite
Dimensional Securities Markets.” Journal of Economic Theory 69: 262-277.

Girotto, B., and F. Ortu. (1997a). “Generic Existence and Robust Non-Existence of
Numeraires in Finite Dimensional Securities Markets.” Working Paper, Dipartimento di Matematica Applicata “B. de Finetti,” Universita di Trieste, Trieste.

Girotto, B., and F. Ortu. (1997b). “Numeraires, Equivalent Martingale Measures and Completeness in Finite Dimensional Securities Markets.” Journal of Mathematical Economics 27: 283-294.

Glasserman, P., P. Heidelberger, and P Shahabuddin. (1999). “Asymptotically Optimal Importance Sampling and Stratification for Pricing Path-Dependent Options.” Mathematical Finance 9: 117-152.

Glasserman, P., and Y. Jin. (1999). “Comparing Stochastic Discount Factors through their
Implied Measures.” Working Paper, Columbia University.

Glasserman, P., and S. Kou. (1999). “The Term Structure of Simple Forward Rates with Jump Risk.” Working Paper, Columbia University.

Glasserman, P., and X. Zhao. (1999). “Fast Greeks by Simulation in Forward LIBOR Models.”
Journal of Computational Finance 3 (Fall): 5-40.

Goldberg, L. (1998). “Volatility of the Short Rate in the Rational Lognormal Model.” Finance and Stochastics 2: 199-211.

Goldman, B., H. Sosin, and M. Gatto. (1979). “Path Dependent Options: ‘Buy at the Low,
Sell at the High’.” Journal of Finance 34: 1111-1127.

Goldstein, R. (1995). “On the Term Structure of Interest Rates in the Presence of Reflecting and Absorbing Boundaries.” Working Paper, Walter A. Haas School of Business, University of California at Berkeley.

Goldstein, R. (1997). “Beyond HJM: Fitting the Current Term Structure While Maintaining a Markovian System.” Working Paper, Fisher College of Business, The Ohio State University.

Goldstein, R. (2000). “The Term Structure of Interest Rates as a Random Field.” Review of Financial Studies 13: 365-384.

Goldstein, R., and F. Zapatero. (1996). “General Equilibrium with Constant Relative Risk
Aversion and Vasicek Interest Rates.” Mathematical Finance 6: 331-340.

Goldys, B., and M. Musiela. (1996). “On Partial Differential Equations Related to Term
Structure Models.” Working Paper, School of Mathematics, University of New South Wales, Sydney.

Goldys, B., M. Musiela, and D. Sondermann. (1994). “Lognormality of Rates and Term
Structure Models.” Working Paper, School of Mathematics, University of New South Wales.

Goll, T., and J. Kallsen. (1999). “Optimal Portfolios for Logarithmic Utility.” Working Paper, University of Freiburg.

Gorman, W. (1953). “Community Preference Fields.” Econometrica 21: 63-80.

Gottardi, P. (1995). “An Analysis of the Conditions for the Validity of the Modigliani-Miller
Theorem with Incomplete Markets.” Economic Theory 5: 191-208.

Gottardi, P., and T. Hens. (1996). “The Survival Assumption and Existence of Competitive
Equilibria when Asset Markets are Incomplete.” Journal of Economic Theory 71: 313-323,

Gottardi, P., and A. Kajii. (1999). “The Structure of Sunspot Equilibria: The Role of Multiplicity.” Review of Economic Studies 66: 713-732.

Gourieroux, C., and J. Jasiak. (2000). Financial Econometrics. Princeton, N.J.: Princeton University Press.

Gourieroux, C., and J.-P. Laurent. (1994). “Estimation of a Dynamic Hedging.” Working Paper, CREST and CEPREMAP, Paris.

Gourieroux, C., J.-P. Laurent, and H. Pham. (1998). “Mean-Variance Hedging and Numeraire.” Mathematical Finance 3: 179-200.

Gourieroux, C., and O. Scaillet. (1994). “Estimation of the Term Structure from Bond Data.”
Working Paper, CREST and CEPREMAP, Paris.

Grabbe, J. (1983). “The Pricing of Call and Put Options on Foreign Exchange.” Journal of International Money and Finance 2: 239-253.

Grandell, J. (1976). Doubly Stochastic Poisson Processes. Lecture Notes in Mathematics, Number 529. New York: Springer-Verlag.

Grannan, E., and G. Swindle. (1996). “Minimizing Transaction Costs of Option Hedging Strategies.” Mathematical Finance 6: 341-364.

Grant, S., A. Kaji and B. Polak. (2000). “Temporal Resolution of Uncertainty and Recursive
Non-Expected Utility Models.” Econometrica 68: 425-434.

Grauer, F., and R. Litzenberger. (1979). “The Pricing of Commodity Futures Contracts, Nominal Bonds, and Other Risky Assets under Commodity Price Uncertainty.” Journal of Finance 44: 69-84.

Grinblatt, M. (1994). “An Analytic Solution for Interest Rate Swap Spreads.” Working
Paper, Anderson Graduate School of Management, University of California, Los Angeles.

Grinblatt, M., and N. Jegadeesh. (1996). “The Relative Pricing of Eurodollar Futures and
Forward Contracts.” Journal of Finance 51: 1499-1522.

Grodal, B., and K. Vind. (1988). “Equilibrium with Arbitrary Market Structure.” Working
Paper, Department of Economics, University of Copenhagen.

Grosen, A., and P. Jorgensen. (1995). “The Valuation of Interest Rate Guarantees: An Application of American Option Pricing Theory.” Working Paper, Department ofBanking and Finance, Aarhus School of Business.

Grossman, S., and G. Laroque. (1990). “Asset Pricing and Optimal Portfolio Choice in the Presence of Illiquid Durable Consumption Goods.” Econometrica 58: 25-51.

Grossman, S., and R. Shiller. (1982). “Consumption Correlatedness and Risk Measurement in Economies with Non-Traded Assets and Heterogeneous Information.” Journal of Financial Economics 10: 195-210.

Grossman, S., and Z. Zhou. (1996). “Equilibrium Analysis of Portfolio Insurance.” Journal of Finance 51: 1379-1403.

Gukhal, C. (1995a). “American Call Options on Stocks with Discrete Dividends.” Working Paper, Graduate School of Business, Columbia University, New York.

Gukhal, C. (1995b). “The Analytic Valuation of American Options on Jump-Diffusion Processes.” Working Paper, Graduate School of Business, Columbia University, New York.

Gul, F., and O. Lantto. (1990). “Betweenness Satisfying Preferences and Dynamic Choice.” Journal of Economic Theory 52: 162-177.

Guo, D. (1998). “The Risk Premium of Volatility Implicit in Currency Options.” Journal of Business and Economics Statistics 16: 498-507.

Haan, W. D. (1996). “Heterogeneity, Aggregate Uncertainty, and the Short-Term Interest Rate.” Journal of Business and Economic Statistics 14: 399-411.

Hahn, F. (1994). “On Economies with Arrow Securities.” Working Paper, Department of Economics, Cambridge University.

Hahn, F. (1999). “A Remark on Incomplete Markets Equilibrium.” In G. Chichilnisky (Ed.), Markets, Information and Uncertainty, pp.7-71. New York: Cambridge University Press.

Hakansson, N. (1970). “Optimal Investment and Consumption Strategies under Risk for a Class of Utility Functions.” Econometrica 38: 587-607.

Hakansson, N. (1974). “Convergence to Isoelastic Utility and Policy in Multiperiod Portfolio Choice.” Journal of Financial Economics 1: 201-224.

Hamza, K., and F. Klebaner. (1995). “A Stochastic Partial Differential Equation for Term Structure of Interest Rates.” Working Paper, Department of Statistics, University of Melbourne.

Hansen, A., and P. Jorgensen. (1998). “Exact Analytical Valuation of Bonds when Spot Interest Rates are Log-Normal.” Working Paper, Centre for Analytical Finance, University of Aarhus, Aarhus School of Business.

Hansen, L. (1982). “Large Sample Properties of Generalized Method of Moments Estimators.” Econometrica 50: 1029-1054.

Hansen, L., and R. Jaganathan. (1990). “Implications of Security Market Data for Models of Dynamic Economies.” Journal of Political Economy 99: 225-262.

Hansen, L., and S. Richard. (1987). “The Role of Conditioning Information in Deducing Testable Restrictions Implied by Dynamic Asset Pricing Models.” Econometrica 55: 587-614.

Hansen, L., and T. Sargent. (1990). “Recursive Linear Models of Dynamic Economies.” Working Paper, Department of Economics, University of Chicago.

Hansen, L., and K. Singleton. (1982). “Generalized Instrumental Variables Estimation of Nonlinear Rational Expectations Models.” Econometrica 50: 1269-1286.

Hansen, L., and K. Singleton. (1983). “Stochastic Consumption, Risk Aversion, and the Temporal Behavior of Asset Returns.” Journal of Political Economy 91: 249-265.

Hansen, L., and K. Singleton. (1996). “Efficient Estimation of Linear Asset-Pricing Models with Moving Average Errors.” Journal of Business and Economic Statistics 14: 53-68.

Hara, C. (1993). “A Role of Redundant Assets in the Presence of Transaction Costs.” Working Paper, Sloan School of Management, Massachusetts Institute of Technology.

Hara, C. (1994). “Marginal Rates of Substitution for Uninsurable Risks with Constraint-Efficient Asset Structures.” Working Paper, Center for Operations Research and Econometrics, Université Catholique de Louvain.

Harris, M. (1987). Dynamic Economic Analysis. New York: Oxford University Press.

Harrison, M. (1985). Brownian Motion and Stochastic Flow Systems. New York: Wiley.

Harrison, M., and D. Kreps. (1979). “Martingales and Arbitrage in Multiperiod Securities Markets.” Journal of Economic Theory 20: 381-408.

Harrison, M., and S. Pliska. (1981). “Martingales and Stochastic Integrals in the Theory of Continuous Trading.” Stochastic Processes and Their Applications 11: 215-260.

Hart, O. (1975). “On the Optimality of Equilibrium when the Market Structure is Incomplete.” Journal of Economic Theory 11: 418-430.

Harvey, A., E. Ruiz, and N. Shephard. (1994). “Multivariate Stochastic Variance Models.” Review of Economic Studies 61: 247-264.

Harvey, A., and N. Shephard. (1993). “The Econometrics of Stochastic Volatility.” Working Paper, Department of Statistical and Mathematical Sciences, London School of Economics.

Haug, E. (1999). “Closed Form Valuation of American Barrier Options.” Working Paper, Derivatives Research, Tempus Financial Engineering, Norway.

He, H. (1990). “Convergence from Discrete- to Continuous-Time Contingent Claims Prices.” Review of Financial Studies 3: 523-546.

He, H. (1991). “Optimal Consumption-Portfolio Policies: A Convergence from Discrete to Continuous Time Models.” Journal of Economic Theory 55: 340-363.

He, H., and C. Huang. (1994). “Consumption-Portfolio Policies: An Inverse Optimal Problem.” Journal of Economic Theory 62: 294-320.

He, H., and H. Leland. (1993). “On Equilibrium Asset Price Processes.” Review of Financial Studies 6: 593-617.

He, H., and D. Modest. (1995). “Market Frictions and Consumption-Based Asset Pricing.” Journal of Political Economy 103: 94-117.

He, H., and H. Pagés. (1993). “Labor Income, Borrowing Constraints, and Equilibrium Asset Prices.” Economic Theory 3: 663-696.

He, H., and N. Pearson. (1991a). “Consumption and Portfolio Policies with Incomplete Markets: The Finite-Dimensional Case.” Mathematical Finance 1: 1-10.

He, H., and N. Pearson. (1991b). “Consumption and Portfolio Policies with Incomplete Markets: The Infinite-Dimensional Case.” Journal of Economic Theory 54: 259-305.

He, H., and A. Takahashi. (1995). “A Variable Separation Technique for Pricing Average-Rate Options.” Working Paper, Salomon Brothers Asia Limited, Derivatives Analysis.

Heath, D. (1998). “Some New Term Structure Models.” Working Paper, Department of Mathematical Sciences, Carnegie Mellon University.

Heath, D., R. Jarrow, and A. Morton. (1990). “Bond Pricing and the Term Structure of Interest Rates: A Discrete Time Approximation.” Journal of Financial and Quantitative Analysis 25: 419-440.

Heath, D., R. Jarrow, and A. Morton. (1992a). “Bond Pricing and the Term Structure of Interest Rates: A New Methodology for Contingent Claims Valuation.” Econometrica 60: 77-106.

Heath, D., R. Jarrow, and A. Morton. (1992b). “Contingent Claim Valuation with a Random Evolution of Interest Rates.” Working Paper, Operations Research Department, Cornell University.

Heaton, J. (1993). “The Interaction between Time-Nonseparable Preferences and Time Aggregation.” Econometrica 61: 353-386.

Heaton, J., and D. Lucas. (1996). “Evaluating the Effects of Incomplete Markets on Risk Sharing and Asset Pricing.” Journal of Political Economy 104: 668-712.

Hellwig, M. (1996). “Rational Expectations Equilibria in Sequence Economies with Symmetric Information: The Two Period Case.” Journal of Mathematical Economics 26: 9-49.

Hemler, M. (1990). “The Quality Delivery Option in Treasury Bond Futures Contracts.” Journal of Finance 45: 1565-1586.

Henrotte, P. (1991). “Transactions Costs and Duplication Strategies.” Working Paper, Graduate School of Business, Stanford University.

Henrotte, P. (1994). “Multiperiod Equilibrium with Endogenous Price Uncertainty.” Working Paper, Groupe HEC, Département de Finance et Economie, Jouy en Josas, France.

Hens, T. (1991). “Structure of General Equilibrium Models with Incomplete Markets.” Working Paper, Department of Economics, University of Bonn.

Hernandez, A., and M. Santos. (1996). “Competitive Equilibria for Infinite-HorizonEconomies with Incomplete Markets.” Journal of Economic Theory 71: 102-130.

Heston, S. (1988a). “Generalized Interest Rate Processes for the Goldman, Sachs, and Company Mortgage Valuation Model.” Working Paper, Graduate School of Industrial Administration, Carnegie Mellon University.

Heston, S. (1988b). “Testing Continuous Time Models of the Term Structure of Interest Rates.” Working Paper, Graduate School of Industrial Administration, Carnegie Mellon University.

Heston, S. (1989). “Discrete Time Versions of Continuous Time Interest Rate Models.” Working Paper, Graduate School of Industrial Administration, Carnegie Mellon University.

Heston, S. (1990). “Sticky Consumption, Optimal Investment, and Equilibrium Asset Prices.” Working Paper, School of Organization and Management, Yale University.

Heston, S. (1993). “A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options.” Review of Financial Studies 6: 327-344.

Heston, S. (1997). “Option Pricing with Infinitely Divisible Distributions.” Working Paper, John M. Olin School of Business, Washington University, St. Louis.

Heston, S., and S. Nandi. (1997). “A Closed-Form GARCH Option Pricing Model.” Working Paper, Federal Reserve Bank of Atlanta.

Heston, S., and G. Zhou. (1997). “On Rate of Convergence of Discrete Time Contingent Claims.” Working Paper, Washington University, St. Louis.

Heynen, R., and H. Kat. (1993). “Volatility Prediction: A Comparison of the Stochastic Volatility, GARCH(1,1) and EGARCH(1,1) Models.” Working Paper, Department of Operations Research, Erasmus University, Rotterdam.

Heynen, R., A. Kemna, and T. Vorst. (1994). “Analysis of the Term Structure of Implied Volatilities.” Journal of Financial and Quantitative Analysis 1: 31-57.

Hildenbrand, W., and P. Kirman. (1989). Introduction to Equilibrium Analysis (2nd ed.). Amsterdam: North-Holland Elsevier.

Hindy, A. (1995). “Viable Prices in Financial Markets with Solvency Constraints.” Journal of Mathematical Economics 24: 105-136.

Hindy, A., and C.-F. Huang. (1992). “Intertemporal Preferences for Uncertain Consumption: A Continuous Time Approach.” Econometrica 60: 781-802.

Hindy, A., and C.-F. Huang. (1993). “Optimal Consumption and Portfolio Rules with Local Substitution.” Econometrica 61: 85-122.

Hindy, A., C.-F. Huang, and D. Kreps. (1992). “On Intertemporal Preferences in Continuous Time: The Case of Certainty.” Journal of Mathematical Economics 21: 401-440.

Hindy, A., C.-F. Huang, and H. Zhu. (1993). “Numerical Analysis of a Free Boundary Singular Control Problem in Financial Economics.” Working Paper, Graduate School of Business, Stanford University.

Hindy, A., C.-F. Huang, and H. Zhu. (1997). “Optimal Consumption and Portfolio Rules with Durability and Habit Formation.” Journal of Economic Dynamics and Control 21: 525-550.

Hindy, A., and M. Huang. (1993b). “Asset Pricing with Linear Collateral Constraints.” Working Paper, Graduate School of Business, Stanford University.

Hirsch, M., M. Magill, and A. Mas-Colell. (1990). “A Geometric Approach to a Class of Equilibrium Existence Theorems.” Journal of Mathematical Economics 19: 95-106.

Ho, T., and S. Lee. (1986). “Term Structure Movements and Pricing Interest Rate Contingent Claims.” Journal of Finance 41: 1011-1029.

Hobson, D. (1998). “Bounds on the Lookback.” Finance and Stochastics 2: 250-263.
Hobson, D., and C. Rogers. (1993). “Models of Endogenous Stochastic Volatility.” Working Paper, Judge Institute of Management Studies, Cambridge University.

Hobson, D., and L. Rogers. (1998). “Complete Models with Stochastic Volatility.” Mathematical Finance 8: 27-48.

Hodges, S., and A. Carverhill. (1992). “The Characterization of Economic Equilibria which Support Black-Scholes Options Pricing.” Working Paper, Financial Options Research Centre, University of Warwick.

Hodges, S., and M. Selby. (1996). “The Risk Premium in Trading Equilibria Which Support Black-Scholes Option Pricing.” In M. A. H. Dempster and S. R. Pliska (Eds.), Mathematics of Derivative Securities, pp.1-52. Cambridge: Cambridge University Press.

Hofmann, N., E. Platen, and M. Schweizer. (1992). “Option Pricing Under Incompleteness and Stochastic Volatility.” Mathematical Finance 2: 153-187.

Hogan, M. (1993a). “The Lognormal Interest Rate Model and Eurodollar Futures.” Working Paper, Citibank, New York.

Hogan, M. (1993b). “Problems in Certain Two-Factor Term Structure Models.” Annals of Applied Probability 3: 576-581.

Honda, T. (1992). “Equilibrium in Incomplete Real Asset Markets with Dispersed Forecast Functions.” Working Paper, Engineering-Economic Systems Department, Stanford University.

Honda, T. (1996). “On the Consumption/Investment Problem with Stochastic ‘Regime Switching’ Parameters.” Working Paper, Engineering-Economic Systems Department, Stanford University.

Honda, T. (1997a). “Equilibrium Asset Pricing with Unobservable Regime-Switching Mean Earnings Growth.” Working Paper, Department of Engineering-Economic Systems and Operations Research, Stanford University.

Honda, T. (1997b). “Optimal Portfolio Choice and Equilibrium Valuation with Regime-Switching Mean Returns.” Working Paper, Department of Engineering-Economic Systems and Operations Research, Stanford University.

Honda, T. (1997c). “Optimal Portfolio Choice for Unobservable and Regime-Switching Mean Returns.” Working Paper, Department of Engineering-Economic Systems and Operations Research, Stanford University.

Hong, C., and L. Epstein. (1989). “Non-Expected Utility Preferences in a Temporal Framework with an Application to Consumption-Savings Behavior.” Journal of Economic Theory 50: 54-81.

Howe, M., and B. Rustem. (1994a). “Minimax Hedging Strategy.” Working Paper, Financial Options Research Centre, University of Warwick.

Howe, M., and B. Rustem. (1994b). “Multi-Period Minimax Hedging Strategies.” Working Paper, Financial Options Research Centre, University of Warwick.

Huang, C.-F. (1985a). “Discussion on ‘Towards a Semigroup Pricing Theory’.” Proceedings of the Journal of Finance 40: 861-862.

Huang, C.-F. (1985b). “Information Structures and Equilibrium Asset Prices.” Journal of Economic Theory 31: 33-71.

Huang, C.-F. (1985c). “Information Structures and Viable Price Systems.” Journal of Mathematical Economics 14: 215-240.

Huang, C.-F. (1987). “An Intertemporal General Equilibrium Asset Pricing Model: The Case of Diffusion Information.” Econometrica 55: 117-142.

Huang, C.-F., and R. Litzenberger. (1988). Foundations for Financial Economics. Amsterdam: North-Holland.

Huang, C.-F., and H. Pagès. (1992). “Optimal Consumption and Portfolio Policies with an Infinite Horizon: Existence and Convergence.” Annals of Applied Probability 2: 36-64.

Huang, C.-F., and T. Zariphopoulou. (1999). “Turnpike Behavior of Long-Term Investments.” Finance and Stochastics 3: 15-34.

Huang, J., M. Subrahmanyam, and R. Sundaram. (1999). “Costly Financing, Optimal Payout Policies and the Valuation of Corporate Debt.” Working Paper, Department of Finance, Smeal School of Business, Penn State University.

Huang, J., M. Subrahmanyam, and G. Yu. (1996). “Pricing and Hedging American Options: A Recursive Integration Method.” Review of Financial Studies 9: 277-300.

Huang, M. (1999). “Liquidity Shocks and Equilibrium Liquidity Premia.” Working Paper, Graduate School of Business, Stanford University.

Huang, P., and H. Wu. (1994). “Competitive Equilibrium of Incomplete Markets for Securities with Smooth Payoffs.” Journal of Mathematical Economics 23: 219-234.

Hubalek, F., and W. Schachermayer. (1998). “When Does Convergence of Asset Price Processes Imply Convergence of Option Prices?” Mathematical Finance 8: 215-233.

Huge, B., and D. Lando. (1999). “Swap Pricing with Two-Sided Default Risk in a Rating-Based Model.” European Finance Review 3: 239-268.Working Paper, Cornell University.

Jaschke, S. (1996). “Arbitrage Bounds for the Term Structure of Interest Rates.” Finance and Stochastics 2: 29-40.

Jaschke, S. (1997). “Super-Hedging and Arbitrage Pricing of Bonds and Interest Rate Derivatives.” Working Paper, Institut für Mathematik, Humboldt-Universität zu Berlin.

Jeanblanc, M., and M. Pontier. (1990). “Optimal Portfolio for a Small Investor in a Market Model with Discontinuous Prices.” Applied Mathematics and Optimization 22: 287-310.

Jeanblanc, M., and M. Rutkowski. (1999). “Modelling of Default Risk: An Overview.” Working Paper, University of Evry Val d'Essonne and Technical University of Warsaw.

Jeffrey, A. (1995a). “A Class of Non-Markovian Single Factor Heath-Jarrow-Morton Term Structure Models.” Working Paper, School of Banking and Finance, University of New South Wales, Sydney.

Jeffrey, A. (1995b). “An Empirical Test of Single Factor Heath-Jarrow-Morton Term Structure Models,” Working Paper, School of Banking and Finance, University of New South Wales, Sydney.

Jeffrey, A. (1995c). “Single Factor Heath-Jarrow-Morton Term Structure Models Based on Markov Spot Interest Rate.” Journal of Financial and Quantitative Analysis 30: 619-643.

Jegadeesh, N. (1993). “An Empirical Analysis of the Pricing of Interest Rate Caps.” Working Paper, College of Commerce and Business Administration, University of Illinois at Urbana-Champaign.

Jin, Y., and P. Glasserman. (1998). “Equilibrium Positive Interest Rates: A Unified View.” Working Paper, Columbia Business School, New York.

Johnson, B. (1994). “Dynamic Asset Pricing Theory: The Search for Implementable Results.” Working Paper, Engineering-Economic Systems Department, Stanford University.

Johnson, H. (1987). “Options on the Maximum or the Minimum of Several Assets.” Journal of Financial and Quantitative Analysis 22: 277-283.

Johnson, H., and D. Shanno. (1987). “The Pricing of Options when the Variance is Changing.” Journal of Financial and Quantitative Analysis 22: 143-151.

Jones, R., and R. Jacobs. (1986). “History Dependent Financial Claims: Monte Carlo Valuation.” Working Paper, Department of Finance, Simon Fraser University, Vancouver, Canada.

Jong, F. de, and P. Santa-Clara. (1999). “The Dynamics of the Forward Interest Rate Curve: A Formulation with State Variables.” Journal of Financial and Quantitative Analysis 34: 131-157.

Jordan, B. (1995). “On the Relative Yields of Taxable and Municipal Bonds: A Theory of the Tax Structure of Interest Rates.” Working Paper, Department of Finance, College of Business and Public Administration, University of Missouri-Columbia.

Jorgensen, P. (1994). “American Option Pricing.” Working Paper, School of Business, Institute of Management, University of Aarhus, Denmark.

Jorgensen, P. (1996). “American Bond Option Pricing in One-Factor Spot Interest Rate Models.” Review of Derivatives Research 1: 245-267.

Jorion, P. (1988). “On Jump Processes in the Foreign Exchange and Stock Markets.” Review of Financial Studies 1: 427-445.

Jouini, E., and H. Kallal. (1993a). “Efficient Trading Strategies in the Presence of Market Frictions.” Working Paper, CREST-ENSAE, Paris.

Jouini, E., and H. Kallal. (1993b). “Portfolio Choice and Market Frictions.” Working Paper, ENSAE, and Laboratoire d’Économétrie de l’École Polytechnique, Paris, France.

Jouini, E., and H. Kallal. (1995). “Martingales, Arbitrage, and Equilibrium in Security Markets with Transactions Costs.” Journal of Economic Theory 66: 178-197.

Jouini, E., P. Koehl, and N. Touzi. (1995). “Incomplete Markets, Transaction Costs and Liquidity Effects.” Working Paper, Crest-Ensae, Université de Paris I.

Joy, C., P. Boyle, and K. Tan. (1996). “Quasi-Monte Carlo Methods in Numerical Finance.” Management Science 42: 926-938.

Ju, N. (1997). “Fourier Transformation, Martingale, and the Pricing of Average-Rate Derivatives.” Working Paper, Haas School of Business, University of California at Berkeley.

Ju, N. (1997b). “Pricing American Perpetual Lookback Options.” Working Paper, Haas School of Business, University of California at Berkeley.

Judd, K. (1989). “Minimum Weighted Residual Methods for Solving Dynamic Economic Models.” Working Paper, Hoover Institution, Stanford University.

Judd, K. (1997). “Incomplete Asset Markets with Heterogeneous Tastes and Idiosyncratic Income.” Working Paper, Hoover Institution, Stanford University.

Judd, K., R. Kubler, and K. Schmedders. (1997). “Computing Equilibria in Infinite Horizon Finance Economies—The Case of One Asset.” Working Paper, Hoover Institution, Stanford University.

Kabanov, Y. (1996). “On the FTAP of Kreps-Delbaen-Schachermayer.” Working Paper, Laboratoire de Mathématiques, Université de Franche-Comté.

Kabanov, Y., and D. Kramkov. (1994). “Non-Arbitrage and Equivalent Martingale Measures: A New Proof of the Harrison-Pliska Theorem.” Theory of Probability and its Applications 39: 523-527.

Kabanov, Y., and D. Kramkov. (1995). “Large Financial Markets: Asymptotic Arbitrage and Contiguity.” Theory of Probability and its Applications 39: 182-187.

Kabanov, Y., and C. Stricker. (2000). “A Teacher’s Note in No-Arbitrage Criteria.” Working Paper, Laboratoire de Mathématiques, Université de Franche-Comté.

Kajii, A. (1994). “Anonymity and Optimality of Competitive Equilibrium when Markets are Incomplete.” Journal of Economic Theory 64: 115-129.

Kakutani, S. (1941). “A Generalization of Brouwer’s Fixed-Point Theorem.” Duke Mathematical Journal 8: 451-459.

Kan, R. (1993). “Gradient of the Representative Agent Utility When Agents Have Stochastic Recursive Preferences.” Working Paper, Graduate School of Business, Stanford University.

Kan, R. (1995). “Structure of Pareto Optima when Agents Have Stochastic Recursive Preferences.” Journal of Economic Theory 66: 626-631.

Kandori, M. (1988). “Equivalent Equilibria.” International Economic Review 29: 401-417.

Karatzas, I. (1988). “On the Pricing of American Options.” Applied Mathematics and Optimization 17: 37-60.

Karatzas, I. (1989). “Optimization Problems in the Theory of Continuous Trading.” SIAM Journal of Control and Optimization 27: 1221-1259.

Karatzas, I. (1991). “A Note on Utility Maximization under Partial Observations.” Mathematical Finance 1: 57-70.

Karatzas, I. (1993). “IMA Tutorial Lectures 1-3: Minneapolis.” Working Paper, Department of Statistics, Columbia University.

Karatzas, I. (1997). Lectures on the Mathematics of Finance, Providence: American Mathematical Society.

Karatzas, I., and S.-G. Kou. (1998). “Hedging American Contingent Claims with Constrained Portfolios.” Finance and Stochastics 2: 215-258.

Karatzas, I., P. Lakner, J. Lehoczky, and S. Shreve. (1991). “Equilibrium in a Simplified Dynamic, Stochastic Economy with Heterogeneous Agents.” In E. Mayer-Wolf, A. Schwartz, and O. Zeitouni (Eds.), Stochastic Analysis: Liber Amicorum for Moshe Zakai, pp.45-272. New York: Academic Press.

Karatzas, I., J. Lehoczky, S. Sethi, and S. Shreve. (1986). “Explicit Solution of a General Consumption/Investment Problem.” Mathematics of Operations Research 11: 261-294.

Karatzas, I., J. Lehoczky, and S. Shreve. (1987). “Optimal Portfolio and Consumption Decisions for a ‘Small Investor’ on a Finite Horizon.” SIAM Journal of Control and Optimization 25: 1157-1186.

Karatzas, I., J. Lehoczky, and S. Shreve. (1990). “Existence and Uniqueness of Multi-Agent Equilibrium in a Stochastic Dynamic Consumption/Investment Model.” Mathematics of Operations Research 15: 80-128.

Karatzas, I., J. Lehoczky, and S. Shreve. (1991). “Equilibrium Models with Singular Asset Prices.” Mathematical Finance 1: 11-30.

Karatzas, I., J. Lehoczky, S. Shreve, and G.-L. Xu. (1991). “Martingale and Duality Methods for Utility Maximization in Incomplete Markets.” SIAM Journal of Control and Optimization 29: 702-730.

418 BibliographyKaratzas, I., and S. Shreve. (1988). Brownian Motion and Stochastic Calculus. New York: Springer-Verlag.

Karatzas, I., and S. Shreve. (1998). Methods of Mathematical Finance. New York: Springer-Verlag.

Karatzas, I., and X.-X. Xue. (1990). “Utility Maximization in a Financial Market with Partial Observations.” Working Paper, Department of Mathematics, Rutgers University.

Karr, A. F. (1991). Point Processes and Their Statistical Inference, (2d ed.). New York: Marcel Dekker, Inc.

Kat, H. (1993). “Hedging Lookback and Asian Options.” Working Paper, Derivatives Department, MeesPierson N.V., Amsterdam.

Kawazu, K., and S. Watanabe. (1971). “Branching Processes with Immigration and Related Limit Theorems.” Theory of Probability and its Applications 16: 36-54.

Kehoe, T., and D. K. Levine. (1993). “Debt-Constrained Asset Markets.” Review of Economic Studies 60: 865-888.

Kennedy, D. (1994). “The Term Structure of Interest Rates as a Gaussian Random Field.” Mathematical Finance 4: 247-258.

Kifer, Y. (2000). “Game Options.” Finance and Stochastics 4: 443-463.

Kijima, M. (1998). “Monotonicities in a Markov Chain Model for Valuing Corporate Bonds Subject to Credit Risk.” Mathematical Finance 8: 229-247.

Kijima, M., and K. Komoribayashi. (1998). “A Markov Chain Model for Valuing Credit Risk Derivatives.” Journal of Derivatives 6 (Fall): 97-108.

Kim, I. (1990). “The Analytic Valuation of American Options.” Review of Financial Studies 3: 547-572.

Kim, J. (1992). “A Martingale Analysis of the Term Structure of Interest Rates.” Working Paper, Graduate School of Industrial Administration, Carnegie-Mellon University.

Kim, J. (1993). “A Discrete-Time Approximation of a One-Factor Markov Model of the Term Structure of Interest Rates.” Working Paper, Graduate School of Industrial Administration, Carnegie-Mellon University.

Kim, J. (1994). “A Model of the Term Structure of Interest Rates with the Time-Variant Market Price of Risk.” Working Paper, Graduate School of Industrial Administration, Carnegie-Mellon University.

Kind, P., R. Liptser, and W. Runggaldier. (1991). “Diffusion Approximation in Past Dependent Models and Applications to Option Pricing.” Annals of Applied Probability 1: 379-405.

Kishimoto, N. (1989). “A Simplified Approach to Pricing Path Dependent Securities.” Working Paper, Fuqua School of Business, Duke University.

Kocherlakota, N. (1990). “On the Discount Factor in Growth Economies.” Journal of Monetary Economics 25: 43-47.

Koedijk, K., F. Nissen, R. Schotman, and C. Wolff. (1994). “The Dynamics of Short-Term Interest Rate Volatility Reconsidered.” Working Paper, Limburg Institute of Financial Economics, University of Limburg.

Konno, H., and T. Takase. (1995). “A Constrained Least Square Approach to the Estimation of the Term Structure of Interest Rates.” Financial Engineering and the Japanese Markets 2: 169-179.

Konno, H., and T. Takase. (1996). “On the De-Facto Convex Structure of a Least Square Problem for Estimating the Term Structure of Interest Rates.” Financial Engineering and the Japanese Market 3: 77-85.

Koo, H.-K. (1998). “Consumption and Portfolio Selection with Labor Income: A Continuous-Time Approach.” Mathematical Finance 8: 49-65.

Koo, H.-K. (1999). “Consumption and Portfolio Selection with Labor Income: A Discrete-Time Approach.” Mathematical Methods of Operations Research 50: 219-243.

Koopmans, T. (1960). “Stationary Utility and Impatience.” Econometrica 28: 287-309.

Korn, R. (1995). “Contingent Claim Valuation in a Market with Different Interest Rates.” Mathematical Methods of Operations Research 42: 255-274.

Kou, S. (1999). “A Jump Diffusion Model for Option Pricing with Three Properties: Leptokurtic Feature, Volatility Smile, and Analytical Tractability.” Working Paper, Department of IEOR, Columbia University.

Krasa, S., and J. Werner. (1991). “Equilibria with Options: Existence and Indeterminacy.” Journal of Economic Theory 54: 305-320.

Kraus, A., and R. Litzenberger. (1975). “Market Equilibrium in a Multiperiod State Preference Model with Logarithmic Utility.” Journal of Finance 30: 1213-1227.

Kraus, A., and M. Smith. (1993). “A Simple Multifactor Term Structure Model.” Journal of Fixed Income 3: 19-23.

Kreps, D. (1979). “Three Essays on Capital Markets.” Working Paper, Institute for Mathematical Studies in the Social Sciences, Stanford University.

Kreps, D. (1981). “Arbitrage and Equilibrium in Economies with Infinitely Many Commodities.” Journal of Mathematical Economics 8: 15-35.

Kreps, D. (1982). “Multiperiod Securities and the Efficient Allocation of Risk: A Comment on the Black-Scholes Option Pricing Model.” In J. McCall (Ed.), The Economics of Uncertainty and Information, pp.03-232. Chicago: University of Chicago Press.

Kreps, D. (1988). Notes on the Theory of Choice. Boulder, CO, and London: Westview Press.

Kreps, D. (1990). A Course in Microeconomics. Princeton, NJ: Princeton University Press.

Kreps, D., and E. Porteus. (1978). “Temporal Resolution of Uncertainty and Dynamic Choice.” Econometrica 46: 185-200.

Krylov, N. (1980). Controlled Diffusion Processes. New York: Springer-Verlag.

Kubler, F., and K. Schmedders. (1997). “Computing Equilibria in Stochastic Finance Economies.” Working Paper, Department of Economics, Yale University. Forthcoming in Computational Economics.

Kunitomo, N. (1993). “Long-Term Memory and Fractional Brownian Motion in Financial Markets.” Working Paper, Faculty of Economics, University of Tokyo.

Kunitomo, N., and A. Takahashi. (1996). “The Asymptotic Expansion Approach to the Valuation of Interest Rates Contingent Claims.” Working Paper, Faculty of Economics, University of Tokyo.

Kurz, M. (1993). “General Equilibrium with Endogenous Uncertainty.” Working Paper, Department of Economics, Stanford University.

Kurz, M. (1997). “Asset Prices with Rational Beliefs.” In M. Kurz (Ed.), Endogenous Economic Fluctuations: Studies in the Theory of Rational Beliefs. New York: Springer Verlag.

Kurz, M. (1998). “Social States of Belief and the Determinants of the Equity Risk Premium in a Rational Belief Equilibrium.” In E. A. Y. A. Abramovich and N. Yannelis (Eds.), Functional Analysis and Economic Theory, pp.71-220. New York: Springer Verlag.

Kurz, M., and A. Beltratti. (1996). “The Equity Premium is No Puzzle.” Working Paper, Department of Economics, Stanford University.

Kurz, M., and M. Motolese. (1999). “Endogenous Uncertainty and Market Volatility.” Working Paper, Stanford University.

Kusuoka, S. (1992a). “Arbitrage and Martingale Measure.” Working Paper, Research Institute for Mathematical Sciences, Kyoto University.

Kusuoka, S. (1992b). “Consistent Price System when Transaction Costs Exist.” Working Paper, Research Institute for Mathematical Sciences, Kyoto University.

Kusuoka, S. (1993). “Limit Theorem on Option Replication Cost with Transaction Costs.” Working Paper, Department of Mathematics, University of Tokyo.

Kusuoka, S. (1996). “A Remark on American Securities.” Working Paper, Graduate School of Mathematical Sciences, University of Tokyo.

Kusuoka, S. (1999a). “Approximation of Expectation of Diffusion Process and Mathematical Finance.” Working Paper, Graduate School of Mathematical Sciences, University of Tokyo. Forthcoming in Advanced Studies in Pure Mathematics, Proceedings of Final Taniguchi Symposium, Nara 1998, ed. T. Sunada.

Kusuoka, S. (1999b). “A Remark on Default Risk Models.” Advances in Mathematical Economics 1: 69-82.

Kusuoka, S. (2000). “Term Structure and SPDE.” Advances in Mathematical Economics 2: 67-85.

Kuwana, Y. (1994). Ph.D. Dissertation, Statistics Department, Stanford University.

Kuwana, Y. (1995). “Certainty Equivalence and Logarithmic Utilities in Consumption/Investment Problems.” Mathematical Finance 5: 297-309.

Kydland, F. E., and E. Prescott. (1991). “Indeterminacy in Incomplete Market Economies.” Economic Theory 1: 45-62.Lobo, M., M. Fazel, and S. Boyd. (1999). “Portfolio Optimization with Linear and Fixed
Transaction Costs and Bounds on Risk.” Working Paper, Information Systems Laboratory, Stanford University.

Loewenstein, M., and G. Willard. (1998). “Rational Equilibrium Asset-Pricing Bubbles in Continuous Trading Models.” Working Paper, Olin School of Business, Washington University in St. Louis.

Loewenstein, M., and G. Willard. (1999). “Local Martingales, Arbitrage, and Viability: Free
Snacks and Cheap Thrills.” Working Paper, Olin School of Business, Washington University in St. Louis.

Léffler, A. (1996). “Variance Aversion Implies A-σ^2-Criterion” Journal of Economic Theory 69: 532-539.

Long, J. (1990). “The Numeraire Portfolio.” Journal of Financial Economics 26: 29-69.

Longstaff, F. (1990). “The Valuation of Options on Yields.” Journal of Financial Economics 26: 97-121.

Longstaff, F., and E. Schwartz. (1992). “Interest Rate Volatility and the Term Structure: A
Two-Factor General Equilibrium Model.” Journal of Finance 47: 1259-1282.

Longstaff, F., and E. Schwartz. (1993). “Implementing of the Longstaff-Schwartz Interest Rate
Model.” Working Paper, Anderson Graduate School of Management, University of California, Los Angeles.

Longstaff, F., and E. Schwartz. (1995a). “A Simple Approach to Valuing Risky Fixed and
Floating Rate Debt.” Journal of Finance 50: 789-819.

Longstaff, F., and E. Schwartz. (1995b). “Valuing Credit Derivatives.” Journal of Fixed Income 5 (June): 6-12.

Longstaff, F., and E. Schwartz. (1998). “Valuing American Options By Simulation: A Simple
Least-Squares Approach.” Working Paper, Anderson Graduate School of Management, University of California, Los Angeles.

Loshkay, B. (1996). “The Valuation of Defaultable Convertible Bonds under Stochastic Interest Rate.” Working Paper, Krannert Graduate School of Management, Purdue University, West Lafayette.

Lu, S., and G. Yu. (1993). “Valuation of Options under Stochastic Volatility: The Garch
Diffusion Approach.” Working Paper, Department of Mathematics, University of Michigan.

Lucas, D. (1994). “Asset Pricing with Undiversifiable Income Risk and Short Sales Constraints: Deepening the Equity Premium Puzzle.” Journal of Monetary Economics 34: 325-341.

Lucas, D. (1995). “Market Fractions, Savings Behavior and Portfolio Choice.” Working Paper,
Kellogg School of Management, Northwestern University.

Lucas, R. (1978). “Asset Prices in an Exchange Economy.” Econometrica 46: 1429-1445.

Luenberger, D. (1969). Optimization by Vector Space Methods. New York: Wiley.

Luenberger, D. (1984). Introduction to Linear and Nonlinear Programming (2d ed.). Reading, MA: Addison-Wesley.

Luenberger, D. (1995). Microeconomic Theory. New York: McGraw-Hill.

Lund, J. (1999). “A Model for Studying the Effect of EMU on European Yield Curves.”
European Finance Review, Journal of the European Finance Association 2: 321-363.

Luttman, E. (1996). “Asset Pricing in Economies with Frictions.” Econometrica 64: 1439-1467.

Lynch, A., and P. Balduzzi. (1998). “Predictability and Transaction Costs: The Impact on
Rebalancing Rules and Behavior.” Working Paper, New York University.

Ma, C.-H. (1991). “Valuation of Derivative Securities with Mixed Poisson-Brownian Information and with Recursive Utility.” Working Paper, Department of Economics, University of Toronto.

Ma, C.-H. (1993a). “Intertemporal Recursive Utility in the Presence of Mixed PoissonBrownian Uncertainty.” Working Paper, Department of Economics, McGill University.

Ma, C.-H. (1993b). “Market Equilibrium with Heterogeneous Recursive-Utility-Maximizing
Agents.” Economic Theory 3: 243-266; Corrigendum 6 (1995): 567-570.

Ma, C.-H. (1994). “Discrete-Time Model of Asset Pricing in Incomplete Market: GE
Approach with Recursive Utility.” Working Paper, Department of Economics, McGill University.

Ma, C.-H. (1996). “Attitudes Toward the Timing of Resolution of Uncertainty and the Existence of Recursive Utility.” Working Paper, Department of Economics, McGill University, Montreal.

Ma, J., and J. Cvitanić. (1996). “Hedging Options for a Large Investor and Forward Backward SDEs.” Annals of Applied Probability 6: 370-398.

Ma, J., P. Protter, and J. Yong. (1994). “Solving Forward-Backward Stochastic Differential
Equations Explicitly—A Four Step Scheme.” Probability Theory and Related Fields 98: 339-359.

Ma, J., and J. Yong. (1995). “Solvability of Forward-Backward SDEs and the Nodal Set of
Hamilton-Jacobi-Bellman Equations.” Chinese Annals of Mathematics. Series B 16: 279-298.

Ma, J., and J. Yong. (1999). Forward-Backward Stochastic Differential Equations and their Applications. New York: Springer-Verlag.

Machina, M. (1982). “‘Expected Utility’ Analysis without the Independence Axiom.” Econometrica 50: 277-323.

Madan, D. (1988). “Risk Measurement in Semimartingale Models with Multiple Consumption Goods.” Journal of Economic Theory 44: 398-412.

Madan, D., and E. Chang. (1996). “Volatility Smiles, Skewness Premia and Risk Metrics:
Applications of a Four Parameter Closed Form Generalization of Geometric
Brownian Motion to the Pricing of Options.” Working Paper, University of Maryland.

Madan, D., and F. Milne. (1991). “Option Pricing with V.G. Martingale Components.” Mathematical Finance 1: 39-55.

Madan, D., F. Milne, and H. Shefrin. (1989). “The Multinomial Option Pricing Model and
Its Brownian and Poisson Limits.” Review of Financial Studies 2: 251-266.

Madan, D., and H. Unal. (1998). “Pricing the Risks of Default.” Review of Derivatives Research 2: 121-160.

Maghsoodi, Y. (1996a). “Market’s Change in Time, Time Change and Time Structured Term
Structures.” Working Paper, SCINANCE, UK, Southampton and University of Southampton.

Maghsoodi, Y. (1996b). “Solution of the Extended CIR Term Structure and Bond Option Valuation.” Mathematical Finance 6: 89-109.

Maghsoodi, Y. (1997a). “Term Structure, Solutions and Option Valuation Under Marked
Point Process Square-Root Interest Rates.” Working Paper, Department of Mathematics, University of Southampton, U.K.

Maghsoodi, Y. (1997b). “Two-Country Term Structure under Marked Point Process Diffusion Interest and Exchange Rates.” Working Paper, Department of Mathematics, University of Southampton, U.K.

Maghsoodi, Y. (1998). “A Closed-Form Analytical Formula for Options with a Non-Linear
Stochastic Volatility.” Working Paper, University of Southampton, UK.

Magill, M., and M. Quinzii. (1994). “Infinite Horizon Incomplete Markets.” Econometrica 62: 853-880.

Magill, M., and M. Quinzii. (1996a). “Incomplete Markets over an Infinite Horizon: LongLived Securities and Speculative Bubbles.” Journal of Mathematical Economics 26: 133-170.

Magill, M., and M. Quinzii. (1996b). Theory of Incomplete Markets. Cambridge, MA: MIT Press.

Magill, M., and W. Shafer. (1990). “Characterization of Generically Complete Real Asset
Structures.” Journal of Mathematical Economics 19: 167-194.

Magill, M., and W. Shafer. (1991). “Incomplete Markets.” In Handbook of Mathematical Economics, Volume 4, pp.523-1614. Amsterdam: North-Holland.

Mankiw, G. (1986). “The Equity Premium and the Concentration of Aggregate Shocks.”
Journal of Financial Economics 17: 211-219.

Marcet, A. (1993). “Simulation Analysis of Dynamic Stochastic Models: Applications to Theory and Estimation.” Working Paper, Department of Economics, Universitat Pompeu Fabra, Barcelona.

Marcet, A., and D. Marshall. (1994). “Solving Nonlinear Rational Expectations Models by Parameterized Expectations: Convergence to Stationary Solutions.” Working
Paper, Universitat Pompeu Fabra, Department of Economics, Barcelona.

Marcet, A., and K. Singleton. (1999). “Equilibrium Asset Prices and Savings of Heterogeneous Agents in the Presence of Portfolio Constraints.” Macroeconomic Dynamics 3: 243-277.

Marcozzi, M. (2000). “On the Approximation of Optimal Stopping Problems with Appli-cation to Financial Mathematics.” Working Paper, Department of Mathematical Sciences, University of Nevada, Las Vegas.

Margrabe, W. (1978). “The Value of an Option to Exchange One Asset for Another.” Journal of Finance 33: 177-186.

Marsh, T. (1994). “Term Structure of Interest Rates and the Pricing of Fixed Income Claims and Bonds.” Working Paper, Haas School of Business, University of California, Berkeley.

Marshall, D. (1999). “Can Cost of Consumption Adjustment Explain Asset Pricing Puzzles?”
Journal of Finance 54: 623-654.

Martin, M. (1997). “Credit Risk in Derivative Products.” Working Paper, University of London, London Business School.

Mas-Colell, A. (1985). The Theory of General Economic Equilibrium—A Differentiable Approach.
Cambridge: Cambridge University Press.

Mas-Colell, A. (1986a). “The Price Equilibrium Existence Problem in Topological Vector Lattices.” Econometrica 54: 1039-1054.

Mas-Colell, A. (1986b). “Valuation Equilibrium and Pareto Optimum Revisited.” In W
Hildenbrand and A. Mas-Colell (Eds.), Contributions to Mathematical Economics, pp.17-332. Amsterdam: North-Holland.

Mas-Colell, A. (1987). “An Observation on Geanakoplos and Polemarchakis.” Working Paper, Department of Economics, Harvard University.

Mas-Colell, A. (1991). “Indeterminacy in Incomplete Market Economies.” Economic Theory 1: 45-62.

Mas-Colell, A., and P. Monteiro. (1996). “Self-Fulfilling Equilibria: An Existence Theorem for a General State Space.” Journal of Mathematical Economics 26; 51-62.

Mas-Colell, A., and W. Zame. (1992). “Equilibrium Theory in Infinite Dimensional Spaces.”
In W. Hildenbrand and H. Sonnenschein (Eds.), Handbook of Mathematical
Economics, Volume 4, pp.835-1898. Amsterdam: North-Holland.

McConnell, J., and E. Schwartz. (1986). “LYON Taming.” Journal of Finance 41: 561-576.

McFadden, D. (1989). “A Method of Simulated Moments for Estimation of Discrete Response
Models without Numerical Integration.” Econometrica 57: 995-1026.

McKean, H. (1965). “Appendix: Free Boundary Problem for the Heat Equation Arising from a Problem in Mathematical Economics.” Industrial Management Review 6: 32-39.

McKenzie, L. (1954). “On Equilibrium in Graham’s Model of World Trade and Other Competitive Systems.” Econometrica 22: 147-161.

McManus, D. (1984). “Incomplete Markets: Generic Existence of Equilibrium and Optimality
Properties in an Economy with Futures Markets.” Working Paper, Department of Economics, University of Pennsylvania.

Mehra, R. (1988). “On the Existence and Representation of Equilibrium in an Economy with Growth and Nonstationary Consumption.” International Economic Review 29: 131-135.

Mehra, R., and E. Prescott. (1985). “The Equity Premium: A Puzzle.” Journal of Monetary Economics 15: 145-161.

Mehrling, P. (1990). “Heterogeneity, Incomplete Markets, and the Equity Premium.” Working Paper, Department of Economics, Barnard College and Columbia University.

Mehrling, P. (1998). “Idiosyncratic Risk, Borrowing Constraints and Asset Prices.” Metroeconomica 49: 261-283.

Melino, A., and S. Turnbull. (1990). “Pricing Foreign Currency Options with Stochastic Volatility.” Journal of Econometrics 45: 239-265.

Mella-Barral, P. (1999). “Dynamics of Default and Debt Reorganization.” Review of Financial Studies 12: 535-578.

Mella-Barral, P., and W. Perraudin. (1997). “Strategic Debt Service.” Journal of Finance 52: 531-556.

Merrick, J. (1999). “Crisis Dynamics of Russian Eurobond Implied Default Recovery Ratios.”
Working Paper, Stern School of Business, New York University.

Merton, R. (1969). “Lifetime Portfolio Selection under Uncertainty: The Continuous Time
Case.” Review of Economics and Statistics 51: 247-257.

Merton, R. (1970). “A Dynamic General Equilibrium Model of the Asset Market and its
Application to the Pricing of the Capital Structure of the Firm.” Working Paper,
Sloan School of Management, Massachusetts Institute of Technology.

Merton, R. (1971). “Optimum Consumption and Portfolio Rules in a Continuous Time
Model.” Journal of Economic Theory 3: 373-413; Erratum 6 (1973): 213-214.

Merton, R. (1973a). “An Intertemporal Capital Asset Pricing Model.” Econometrica 41: 867-888.

Merton, R. (1973b). “The Theory of Rational Option Pricing.” Bell Journal of Economics and Management Science 4: 141-183.

Merton, R. (1974). “On the Pricing of Corporate Debt: The Risk Structure of Interest Rates.”
Journal of Finance 29: 449-470.

Merton, R. (1976). “Option Pricing when the Underlying Stock Returns are Discontinuous.”
Journal of Financial Economics 5: 125-144.

Merton, R. (1977). “On the Pricing of Contingent Claims and the Modigliani-Miller Theorem.” Journal of Financial Economics 5: 241-250.

Merton, R. (1990). Continuous-Time Finance. Oxford: Basil Blackwell.

Meyer, P.-A. (1966). Probability and Potentials. Waltham, MA: Blaisdell Publishing Company.

Milshtein, G. (1974). “Approximate Integration of Stochastic Differential Equations.” Theory of Probability and Its Applications 3: 557-562.

Milshtein, G. (1978). “A Method of Second-Order Accuracy Integration of Stochastic Differential Equations.” Theory of Probability and Its Applications 23: 396-401.

Miltersen, K. (1993). “Pricing of Interest Rate Contingent Claims: Implementing the Simulation Approach.” Working Paper, Department of Management, Odense University.

Miltersen, K. (1994). “An Arbitrage Theory of the Term Structure of Interest Rates.” Annals of Applied Probability 4: 953-967.

Miltersen, K., and S.-A. Persson. (1997). “Pricing Rate of Return Guarantees in a HeathJarrow-Morton Framework.” Insurance: Mathematics and Economics 25: 307-325.

Miltersen, K., K. Sandmann, and D. Sondermann. (1997). “Closed Form Solutions for Term
Structure Derivatives with Log-Normal Interest Rates.” Journal of Finance 52: 409-430.

Miltersen, K., and E. Schwartz. (1998). “Pricing of Options on Commodity Futures with
Stochastic Term Structures of Convenience Yields and Interest Rates.” Journal of Financial and Quantitative Analysis 33: 33-59.

Mirrlees, J. (1974). “Optimal Accumulation under Uncertainty: The Case of Stationary
Returns to Investment.” In J. Dréze (Ed.), Allocation under Uncertainty: Equilibrium and Optimality, pp.6-50. New York: Wiley.

Mitchell, A., and D. Griffiths. (1980). The Finite Difference Method in Partial Differential Equations. New York: John Wiley.

Modigliani, F., and M. Miller. (1958). “The Cost of Capital, Corporation Finance, and the
Theory of Investment.” American Economic Review 48: 261-297.

Monat, P., and C. Stricker. (1994). “Décomposition de Föllmer-Schweizer et Fermeture de
G,(@).” Comptes Rendus de l'Académie des Sciences Paris 318I: 573-576.

Monat, P., and C. Stricker. (1995). “Follmer-Schweizer Decomposition and Closedness of G,(®).” Annals of Probability 23: 605-628.

Monteiro, P. (1994). “Inada’s Condition Imply Equilibrium Existence is Rare.” Economics Letters 44: 99-102.

Monteiro, P. (1996). “A New Proof of the Existence of Equilibrium in Incomplete Markets
Economies.” Journal of Mathematical Economics 26: 85-101.

Moreleda, J. (1997). On The Pricing of Interest Rate Options. Tinbergen Institute Research
Series., Rotterdam, The Netherlands: Erasmus University.

Morokoff, W., and R. Caflisch. (1993). “A Quasi-Monte Carlo Approach to Particle Simulation of the Heat Equation.” SIAM Journal of Numerical Analysis 30: 1558-1573.

Morokoff, W., and R. Caflisch. (1994). “Quasi-Random Sequences and Their Discrepancies.”
SIAM Journal of Scientific Computing 15: 1251-1279.

Morokoff, W., and R. Caflisch. (1995). “Quasi-Monte Carlo Integration.” Journal of Computational Physics 122: 218-230.

Moskowitz, B., and R. Caflisch. (1994). “Smoothness and Dimension Reduction in QuasiMonte Carlo Methods.” Working Paper, Department of Mathematics, University of California, Los Angeles.Miller, S. (1985). Arbitrage Pricing of Contingent Claims. Lecture Notes in Economics and
Mathematical Systems, vol.54. New York: Springer-Verlag.

Munk, C. (1997). “No-Arbitrage Bounds on Contingent Claims Prices with Convex Constraints on the Dollar Investments of the Hedge Portfolio.” Working Paper,
Department of Management, Odense University, Denmark.

Munk, C. (2000b). “Optimal Consumption/Portfolio Policies with Undiversifiable Income
Risk and Liquidity Constraints.” Journal of Economic Dynamics and Control 24: 1315-1343.

Musiela, M. (1994a). “Nominal Annual Rates and Lognormal Volatility Structure.” Working
Paper, Department of Mathematics, University of New South Wales, Sydney.

Musiela, M. (1994b). “Stochastic PDEs and Term Structure Models.” Working Paper, Department of Mathematics, University of New South Wales, Sydney.

Musiela, M., and M. Rutkowski. (1997). Martingale Methods in Financial Modeling. New York: Springer.

Musiela, M., and D. Sondermann. (1994). “Different Dynamical Specifications of the Term
Structure of Interest Rates and their Implications.” Working Paper, Department of Mathematics, University of New South Wales, Sydney.

Myneni, R. (1992a). “Continuous-Time Relationships between Futures and Forward Prices.”
Working Paper, Graduate School of Business, Stanford University.

Myneni, R. (1992b). “The Pricing of the American Option.” Annals of Applied Probability 2: 1-23.

Nahum, E. (1998). “The Pricing of Options Depending on a Discrete Maximum.” Working
Paper, Department of Statistics, University of California, Berkeley.

Naik, V. (1994). “Asset Prices in Dynamic Production Economies with Time Varying Risk.”
Review of Financial Studies 7: 781-801.

Naik, V., and M. Lee. (1994). “The Yield Curve and Bond Option Prices with Discrete Shifts in Economic Regimes.” Working Paper, University of British Columbia.

Naik, V., and R. Uppal. (1994). “Leverage Constraints and the Optimal Hedging of Stock and Bond Options.” Journal of Financial and Quantitative Analysis 29: 199-222.

Nakagawa, H. (1999). “A Remark on Spot Rate Models Induced by an Equilibrium Model.”
University of Tokyo Journal of Mathematical Sciences 6: 453-475.

Neftci, S. (2000). An Introduction to the Mathematics of Financial Derivatives. New York: Academic Press.

Negishi, T. (1960). “Welfare Economics and Existence of an Equilibrium for a Competitive Economy.” Metroeconometrica 12: 92-97.

Nelson, D. (1990). “ARCH Models as Diffusion Approximations.” Journal of Econometrics 45: 7-38.

Nelson, D. (1991). “Conditional Heteroskedasticity in Asset Returns: A New Approach.”
Econometrica 59: 347-370.

Nelson, D. (1992). “Filtering and Forecasting with Misspecified ARCH Models I.” Journal of Econometrics 52: 61-90.

Nelson, D., and K. Ramaswamy. (1989). “Simple Binomial Processes as Diffusion Approximations in Financial Models.” Review of Financial Studies 3: 393-430.

Nelson, J., and S. Schaefer. (1983). “Innovations in Bond Portfolio Management: Duration
Analysis and Immunization.” In The Dynamic of the Term Structure and Alternative
Portfolio Immunization Strategies. Greenwich: JAI Press.

Newton, N. (1990). “Asymptotically Efficient Runge-Kutta Methods for a Class of Ito and
Stratonovich Equations.” Working Paper, Department of Electrical Engineering, University of Essex.

Nielsen, J., and K. Sandmann. (1996). “The Pricing of Asian Options Under Stochastic Interest Rates.” Applied Mathematical Finance 3: 209-236.

Nielsen, L. (1990a). “Equilibrium in CAPM without a Riskless Asset.” Review of Economic Studies 57: 315-324.

Nielsen, L. (1990b). “Existence of Equilibrium in CAPM.” Journal of Economic Theory 52: 223-231.

Nielsen, L. (1993a). “Robustness of the Market Model.” Economic Theory 3: 365-370.

Nielsen, L. (1993b). “Two-Fund Separation and Equilibrium.” Working Paper, INSEAD, Fontainebleau, France.

Nielsen, L. T., and J. Sad-Requejo. (1992). “Exchange Rate and Term Structure Dynamics and the Pricing of Derivative Securities.” Working Paper, INSEAD, Fontainebleau, France.

Nielsen, L. T., J. Sad-Requejo, and P Santa-Clara. (1993). “Default Risk and Interest Rate Risk:
The Term Structure of Credit Spreads.” Working Paper, INSEAD, Fontainebleau, France.

Nielsen, S., and E. Ronn. (1995). “The Valuation of Default Risk in Corporate Bonds and
Interest Rate Swaps.” Working Paper, Department of Management Science and
Information Systems, University of Texas at Austin.

Nunes, J., L. Clewlow, and S. Hodges. (1999). “Interest Rate Derivatives in a Duffie and Kan
Model with Stochastic Volatility: An Arrow-Debreu Pricing Approach.” Review of Derivatives Research 3: 5-66.

Nyborg, K. (1996). “The Use and Pricing of Convertible Bonds.” Applied Mathematical Finance 3: 167-190.

Ocone, D., and I. Karatzas. (1991). “A Generalized Clark Representation Formula, with
Application to Optimal Portfolios.” Stochastics and Stochastics Reports 34: 187-220.

Ohashi, K. (1991). “A Note on the Terminal Date Security Prices in a Continuous Time
Trading Model with Dividends.” Journal of Mathematical Economics 20: 219-224.

Oliveira, D. (1994). “Arbitrage Pricing of Integral Options.” Working Paper, Instituto de Matematica Pura e Applicada, Rio de Janeiro.

Ordentlich, E. (1996). Ph.D. Dissertation, Department of Electrical Engineering, Stanford University.

Owen, A. (1996). “Monte Carlo Variance of Scrambled Net Quadrature.” Working Paper,
Department of Statistics, Stanford University. Forthcoming in SIAM Journal.

Owen, A. (1997). “Scrambled Net Variance for Integrals of Smooth Functions.” Annals of Statistics 25: 1541-1562.

Owen, A., and D. Tavella. (1996). “Scrambled Nets for Value at Risk Calculations.” Working
Paper, Statistics Department, Stanford University.

Pagés, H. (1987). “Optimal Consumption and Portfolio Policies when Markets are Incomplete.” Working Paper, Department of Economics, Massachusetts Institute of Technology.

Pagés, H. (2000). “Estimating Brazilian Sovereign Risk from Brady Bond Prices.” Working Paper, Bank of France.

Pakes, A., and D. Pollard. (1989). “Simulation and the Asymptotics of Optimization Estimators.” Econometrica 57: 1027-1057.

Pan, J. (1999). “Integrated Time-Series Analysis of Spot and Options Prices.” Working Paper, Graduate School of Business, Stanford University.

Pan, W.-H. (1993). “Constrained Efficient Allocations in Incomplete Markets: Characterization and Implementation.” Working Paper, Department of Economics, University of Rochester.

Pan, W.-H. (1995). “A Second Welfare Theorem for Constrained Efficient Allocations in
Incomplete Markets.” Journal of Mathematical Economics 24: 577-599.

Pang, K. (1996). “Multi-Factor Gaussian HJM Approximation to Kennedy and Calibration to
Caps and Swaptions Prices.” Working Paper, Financial Options Research Center, Warwick Business School, University of Warwick.

Pang, K., and S. Hodges. (1995). “Non-Negative Affine Yield Models of the Term Structure.”
Working Paper, Financial Options Research Center, Warwick Business School, University of Warwick.

Pappalardo, L. (1996). “Option Pricing and Smile Effect when Underlying Stock Prices are
Driven by a Jump Process.” Working Paper, Financial Options Research Centre, University of Warwick.

Pardoux, E. (1997). “Generalized Discontinuous Backward Stochastic Differential Equations.” In N. El Karoui and L. Mazliak (Eds.), Backward Stochastic Differential Equations, pp.07-220. Essex: Addison Wesley Longman Ltd.

Pardoux, E., and S. Peng. (1990). “Adapted Solution of a Backward Stochastic Differential Equation.” Systems and Control Letters 14: 55-61.

Pardoux, E., and S. Peng. (1994). “Some Backward Stochastic Differential Equations with
Non-Lipschitz Coefficients.” Working Paper, Department of Mathematics, Université de Provence.

Pearson, N., and T-S. Sun. (1994). “An Empirical Examination of the Cox, Ingersoll, andRoss Model of the Term Structure of Interest Rates using the Method of Maximum Likelihood.” Journal of Finance 54: 929-959.

Pedersen, H., and E. Shiu. (1993). “Pricing of Options on Bonds by Binomial Lattices and by Diffusion Processes.” Working Paper, Investment Policy Department, Great-West Life Assurance Company.

Pedersen, H., E. Shiu, and A. Thorlacius. (1989). “Arbitrage-Free Pricing of Interest Rate Contingent Claims.” Transactions of the Society of Actuaries 41: 231-265.

Pedersen, L. (1997). “Affine Multifactor Term Structure Models—Theory and Inference.” Working Paper, University of Copenhagen.

Pedersen, M. (1999). “Bermudan Swaptions in the LIBOR Market Model.” Working Paper, Financial Research Department, SimCorp A/S.

Peng, S. (1993a). “Adapted Solution of Backward Stochastic Equations and Related Partial Differential Equations.” Working Paper, Department of Mathematics, Shandong University.

Peng, S. (1993b). “Backward Stochastic Differential Equations and Applications to Optimal Control.” Applied Mathematics and Optimization 27: 125-144.

Pennacchi, G. (1991). “Identifying the Dynamics of Real Interest Rates and Inflation: Evidence Using Survey Data.” Review of Financial Studies 4: 53-86.

Pham, H. (1995). “Optimal Stopping, Free Boundary and American Option in a Jump Diffusion Model.” Working Paper, CEREMADE, Université de Paris IX Dauphine. Forthcoming in Applied Mathematics and Optimization.

Pham, H., and N. Touzi. (1993). “Intertemporal Equilibrium Risk Premia in a Stochastic Volatility Model.” Working Paper, CREST, Paris.

Piazzesi, M. (1997). “An Affine Model of the Term Structure of Interest Rates with Macroeconomic Factors.” Working Paper, Stanford University.

Piazzesi, M. (1999). “A Linear-Quadratic Jump-Diffusion Model with Scheduled and Unscheduled Announcements.” Working Paper, Stanford University.

Pierides, Y. (1997). “The Pricing of Credit Risk Derivatives.” Journal of Economic Dynamics and Control 21: 1579-1611.

Pietra, T. (1992). “Indeterminacy in General Equilibrium Economies with Incomplete Financial Markets—Mixed Asset Returns.” Journal of Mathematical Economics 21: 155-172.

Pikovsky, I., and I. Karatzas. (1996). “Anticipative Portfolio Optimization.” Advances in Applied Probability 28: 1095-1122.

Pikovsky, I., and I. Karatzas. (1998). “Stochastic Equilibrium with Differential Information.” Working Paper, Department of Mathematics, Columbia University.

Pikovsky, I., and S. Shreve. (1996a). “Callable Convertible Bonds.” Working Paper, Department of Mathematics, Courant Institute, New York.

Pikovsky, I., and S. Shreve. (1996b). “Perpetual Convertible Debt.” Working Paper, Department of Mathematics, Courant Institute, New York.

Pitts, C., and M. Selby. (1983). “The Pricing of Corporate Debt: A Further Note.” Journal of Finance 38: 1311-1313.

Platen, E., and M. Schweizer. (1994). “On Smile and Skewness.” Working Paper, School of Mathematical Sciences, Centre for Mathematics and Its Applications, The Australian National University, Canberra.

Platen, I. (1994). “Non-linear General Equilibrium Models of the Term Structure: Comments and Two-Factor Generalization.” Finance 15: 63-78.

Pliska, S. (1986). “A Stochastic Calculus Model of Continuous Trading: Optimal Portfolios.” Mathematics of Operations Research 11: 371-382.

Pliska, S., and M. Selby. (1994). “On a Free Boundary Problem that Arises in Portfolio Management.” Philosophical Transactions of the Royal Society of London. Series A.47: 555-561.

Polemarchakis, H., and B. Ku. (1990). “Options and Equilibrium.” Journal of Mathematical Economics 19: 107-112.

Polemarchakis, H., and P. Siconolfi. (1993). “Competitive Equilibria without Free Disposal or Nonsatiation.” Journal of Mathematical Economics 22: 85-99.

Pollard, D. (1984). Convergence of Stochastic Processes. New York: Springer-Verlag.

Pontier, M. (1997). “Solutions of Forward-Backward Stochastic Differential Equations.” In N. El Karoui and L. Mazliak (Eds.), Backward Stochastic Differential Equations, pp.9-46. Essex: Addison Wesley Longman Ltd.

Poteshman, A. M. (1998). “Estimating a General Stochastic Variance Model from Options Prices.” Working Paper, Graduate School of Business, University of Chicago.

Pouque, J., G. Papanicolaou, and K. Sircar. (1999a). “Financial Modeling in a Fast Mean-Reverting Stochastic Volatility Environment.” Asia-Pacific Financial Markets 6: 37-48.

Pouque, J., G. Papanicolaou, and K. Sircar. (1999b). “Mean-Reverting Stochastic Volatility.” Working Paper, Department of Mathematics, North Carolina State University.

Pouque, J., G. Papanicolaou, and K. Sircar. (1999c). “Stochastic Volatility Correction to Black-Scholes.” Working Paper, Department of Mathematics, North Carolina State University.

Prescott, E., and R. Mehra. (1980). “Recursive Competitive Equilibrium: The Case of Homogeneous Households.” Econometrica 48: 1365-1379.

Press, W., B. Flannery, S. Teukolsky, and W. Vetterling. (1993). Numerical Recipes in C: The Art of Scientific Computing (2d ed.). Cambridge: Cambridge University Press.

Prigent, J.-L. (1994). “From Discrete to Continuous Time Finance: Weak Convergence of the Optimal Financial Trading Strategies.” Working Paper, Institute of Mathematical Research of Rennes, University of Rennes.

Prigent, J.-L. (1995). “Incomplete Markets: Convergence of Options Values under the Minimal Martingale Measure.” Working Paper, THEMA, Université de Cergy-Pontoise, Cergy-Pontoise.

Prisman, E. (1985). “Valuation of Risky Assets in Arbitrage Free Economies with Frictions.” Working Paper, Department of Finance, University of Arizona.

Prisman, E. (2000). Pricing Derivative Securities. San Diego: Academic Press.

Protter, P. (1990). Stochastic Integration and Differential Equations. New York: Springer-Verlag.

Protter, P. (1999). “A Partial Introduction to Finance.” Working Paper, Purdue University. Forthcoming in Stochastic Processes and Their Applications.

Pye, G. (1966). “A Markov Model of the Term Structure.” Quarterly Journal of Economics 81: 61-72.

Pye, G. (1974). “Gauging the Default Premium.” Financial Analysts Journal (January-February): 49-52.

Quenez, M.-C. (1992). “Méthodes de Controle Stochastique en Finance.” Working Paper, Ph.D. diss., Laboratoires de Probabilités, Université de Paris VI.

Quenez, M.-C. (1997). “Stochastic Control and BSDEs.” In N. El Karoui and L. Mazliak (Eds.), Backward Stochastic Differential Equations, pp.3-100. Essex: Addison Wesley Longman Ltd.

Radner, R. (1967). “Equilibre des Marchés a Terme et au Comptant en Cas d’Incertitude.” Cahiers d'Econométrie 4: 35-52.

Radner, R. (1972). “Existence of Equilibrium of Plans, Prices, and Price Expectations in a Sequence of Markets.” Econometrica 40: 289-303.

Rady, S. (1993). “State Prices Implicit in Valuation Formula for Derivative Securities: A Martingale Approach.” Working Paper, London School of Economics.

Rady, S. (1995). “Option Pricing with a Quadratic Diffusion Term.” Working Paper, Financial Markets Group, London School of Economics.

Rebonato, R., and I. Cooper. (1996). “Coupling Backward Induction with Monte Carlo Simulations: A Fast Fourier Transform (FFT) Approach.” Working Paper, Institute of Finance and Accounting, London Business School.

Redekop, J. (1995). “Extreme-value Distributions for Generalizations of Brownian Motion.” Working Paper, Departments of Economics and Statistics and Actuarial Science.

Redekop, J., and R. Fisher. (1995). “Extreme-Value Diagnostic Statistics for Some Stochastic Volatility Models.” Working Paper, Department of Economics, University of Waterloo.

Reisman, H. (1986). “Option Pricing for Stocks with a Generalized Log-Normal Price Distribution.” Working Paper, Department of Finance, University of Minnesota.

Renault, E., S. Pastorello, and N. Touzi. (2000). “Statistical Inference for Random VarianceOption Pricing.” Journal of Business and Economic Statistics 18: 358-317.

Renault, E., and N. Touzi. (1992). “Stochastic Volatility Models: Statistical Inference from
Implied Volatilities.” Working Paper, GREMAQ IDEI, Toulouse, and CREST, Paris, France.

Repullo, R. (1986). “On the Generic Existence of Radner Equilibria when there are as Many
Securities as States of Nature.” Economics Letters 21: 101-105.

Revuz, D. (1975). Markov Chains. Amsterdam: North-Holland.

Revuz, D., and M. Yor. (1991). Continuous Martingales and Brownian Motion. New York: Springer.

Ricciardi, L., and S. Sato. (1988). “First-Passage-Time Density and Moments of the OrnsteinUhlenbeck Process.” Journal of Applied Probability 25: 43-57.

Rich, D. (1993). “The Valuation of Black-Scholes Options Subject to Intertemporal Default
Risk.” Working Paper, Department of Finance, Virginia Polytechnic Institute.

Richard, S. (1975). “Optimal Consumption, Portfolio, and Life Insurance Rules for an Uncertain Lived Individual in a Continuous Time Model.” Journal of Financial Economics 2: 187-203.

Richard, S. (1978). “An Arbitrage Model of the Term Structure of Interest Rates.” Journal of Financial Economics 6: 33-57.

Richardson, H. (1989). “A Minimum Variance Result in Continuous Trading Portfolio Optimization.” Management Science 35: 1045-1055.

Ritchken, P., and L. Sankarasubramaniam. (1992). “Valuing Claims when Interest Rates have Stochastic Volatility.” Working Paper, Department of Finance, University of Southern California.

Ritchken, P., and R. Trevor. (1993). “On Finite State Markovian Representations of the
Term Structure.” Working Paper, Department of Finance, University of Southern California.

Ritchken, P., and R. Trevor. (1999). “Option Pricing Options under GARCH and Stochastic Volatility.” Journal of Finance 54: 377-402.

Rockafellar, T. (1973). Convex Analysis. Princeton, NJ: Princeton University Press.

Rogers, C. (1993). “Which Model for Term-Structure of Interest Rates Should One Use?”
Working Paper, Department of Mathematics, Queen Mary and Westfield College, University of London.

Rogers, C. (1994). “Equivalent Martingale Measures and No-Arbitrage.” Stochastics and Stochastic Reports 51: 1-9.

Rogers, C. (1998). “Arbitrage with Fractional Brownian Motion.” Working Paper, University of Bath.

Rogers, C., and Z. Shi. (1995). “The Value of an Asian Option.” Journal of Applied Probability 32: 1077-1088.

Rogers, C., and W. Stummer. (1994). “How Well Do One-Factor Models Fit Bond Prices?”
Working Paper, School of Mathematical Sciences, University of Bath.

Rogers, L., and E. Stapleton. (1998). “Fast Accurate Binomial Pricing.” Finance and Stochastics 2: 3-17.

Romano, M., and N. Touzi. (1997). “Contingent Claims and Market Completeness in a
Stochastic Volatility Model.” Mathematical Finance 7: 399-412.

Rosenberg, J., and R. Engle. (1999). “Empirical Pricing Kernels.” Working Paper, Stern School of Business, New York University.

Ross, S. (1976). “The Arbitrage Theory of Capital Asset Pricing.” Journal of Economic Theory 13: 341-360.

Ross, S. (1978). “A Simple Approach to the Valuation of Risky Streams.” Journal of Business 51: 453-475.

Ross, S. (1987). “Arbitrage and Martingales with Taxation.” Journal of Political Economy 95: 371-393.

Ross, S. (1989). “Information and Volatility: The Non-Arbitrage Martingale Approach to
Timing and Resolution Irrelevancy.” Journal of Finance 64: 1-17.

Royden, H. (1968). Real Analysis (2d ed.). New York: Macmillan.

Rubinstein, M. (1974a). “An Aggregation Theorem for Securities Markets.” Journal of Financial Economics 1: 225-244.

Rubinstein, M. (1974b). “A Discrete-Time Synthesis of Financial Theory.” Working Paper,
Haas School of Business, University of California, Berkeley.

Rubinstein, M. (1976). “The Valuation of Uncertain Income Streams and the Pricing of Options.” Bell Journal of Economics 7: 407-425.

Rubinstein, M. (1987). “Derivative Assets Analysis.” Economics Perspectives 1: 73-93.

Rubinstein, M. (1994). “Implied Binomial Trees.” Journal of Finance 49: 771-818.

Rubinstein, M. (1995). “As Simple as One, Two, Three.” Risk 8 (January): 44-47.

Rubinstein, M. (1999). Derivatives: A Power-Plus Picture Book. Corte Madera, CA: In-The-Money.

Ruegg, M. (1996). “Optimal Consumption and Portfolio Choice with Borrowing Constraints.”
Working Paper, Department of Mathematics, ETH Zurich.

Rumsey, J. (1996). “Comparison of Tax Rates Inferred from Zero-Coupon Yield Curves.”
Journal of Fixed Income 6 (March): 75-81.

Rutkowski, M. (1995). “Pricing and Hedging of Contingent Claims in the HJM Model with
Deterministic Volatilities.” Working Paper, Institute of Mathematics, Politechnika Warszawska, Warszawa.

Rutkowski, M. (1996). “Valuation and Hedging of Contingent Claims in the HJM Model with
Deterministic Volatilities.” Applied Mathematical Finance 3: 237-267.

Rutkowski, M. (1998). “Dynamics of Spot, Forward, and Futures Libor Rates.” International
Journal of Theoretical and Applied Finance 1: 425-445.

Rydberg, T. (1997). “Existence of Unique Equivalent Martingale Measures in a Markovian Setting.” Finance and Stochastics 1: 251-257.

Ryder, H., and G. Heal. (1973). “Optimal Growth with Intertemporally Dependent Preferences.” Review of Economic Studies 40: 1-31.

Saa-Requejo, J. (1993). “The Dynamics of the Term Structure of Risk Premia in Foreign
Exchange Markets.” Working Paper, INSEAD, Fontainebleau, France.

Sabarwal, T. (1999). “Default and Bankruptcy in General Equilibrium.” Working Paper,
Department of Economics, University of California, Berkeley.

Saito, M. (1998). “Incomplete Insurance and Non-expected Utility.” Japanese Economic Review 49: 271-83.

Samuelson, P. (1969). “Lifetime Portfolio Selection by Dynamic Stochastic Programming.”
Review of Economics and Statistics 51: 239-246.

Sandmann, K., and D. Sondermann. (1997). “On the Stability of Lognormal Interest Rate Models.” Mathematical Finance 7: 119-125.

Sandroni, A. (1995). “The Risk Premium and the Interest Rate Puzzles: The Role of Heterogeneous Agents.” Working Paper, University of Pennsylvania.

Santa-Clara, P., and D. Sornette. (1997). “The Dynamics of the Forward Interest Rate
Curve with Stochastic String Shocks.” Working Paper, University of California, Los Angeles.

Santos, M. (1991). “Smoothness of the Policy Function in Discrete Time Economic Models.”
Econometrica 59: 1365-1382.

Santos, M. (1994). “Smooth Dynamics and Computation in Models of Economic Growth.”
Journal of Economic Dynamics and Control 18: 879-895.

Santos, M., and J. Vigo. (1998). “Numerical Dynamic Programming Algorithm Applied to Economic Models.” Econometrica 66: 409-426.

Santos, M., and M. Woodford. (1995). “Rational Asset Pricing Bubbles.” Econometrica 65: 19-58.

Sbuelz, A. (1998). “A General Treatment of Barrier Options.” Working Paper, London Business School.

Scaillet, O. (1996). “Compound and Exchange Options in the Affine Term Structure Model.”
Applied Mathematical Finance 3: 75-92.

Schachermayer, W. (1992). “A Hilbert-Space Proof of the Fundamental Theorem of Asset
Pricing.” Insurance Mathematics and Economics 11: 249-257.

Schachermayer, W. (1993). “A Counterexample to Several Problems in the Theory of Asset Pricing.” Mathematical Finance 3: 217-230.

Schachermayer, W. (1994). “Martingale Measures for Discrete-Time Processes with Infinite Horizon.” Mathematical Finance 4: 25-56.

Schachermayer, W. (1998). “Some Remarks on a Paper of David Kreps.” Working Paper, Institut für Statistik der Universität Wien.

Schaefer, S., and E. Schwartz. (1984). “A Two-Factor Model of the Term Structure: An
Approximate Analytical Solution.” Journal of Financial and Quantitative Analysis 19: 413-423.

Scheinkman, J. (1989). “Market Incompleteness and the Equilibrium Valuation of Assets.”
In S. Bhattacharya and G. Constantinides (Eds.), Theory of Valuation, pp.5-51.
Totowa, NJ: Rowman and Littlefield.Scheinkman, J., and L. Weiss. (1986). “Borrowing Constraints and Aggregate Economic Activity.” Econometrica 54: 23-45.

Schoenmakers, J., and A. Heemink. (1996). “Fast Valuation of Financial Derivatives.” Working Paper, Delft University of Technology, The Netherlands.

Schönbucher, P. (1998). “Term Structure Modelling of Defaultable Bonds.” Review of Derivatives Research 2: 161-192.

Schroder, M. (1993). “Optimal Portfolio Selection with Transactions Costs.” Working Paper, Finance Department, Northwestern University.

Schroder, M. (1999). “Changes of Numeraire of Pricing Futures, Forwards and Options.” Review of Financial Studies 12: 143-164.

Schroder, M. (1999a). “On the Valuation of Arithmetic-Average Asian Options: Explicit Formulas.” Working Paper, Fakultät für Mathematik und Informatik der Universität Mannheim.

Schroder, M. (1999b). “On the Valuation of Double-Barrier Options.” Working Paper, Fakultät für Mathematik und Informatik der Universität Mannheim.

Schroder, M. (1999c). “On the Valuation of Paris Options: Foundational Results.” Working Paper, Lehrstuhl Mathematik III Universität Mannheim.

Schroder, M. (1999d). “On the Valuation of Paris Options: The First Standard Case.” Working Paper, Lehrstuhl Mathematik III Universität Mannheim.

Schroder, M., and C. Skiadas. (1997). “Optimal Consumption and Portfolio Selection with Temporally Dependent Preferences.” Working Paper, School of Management, SUNY at Buffalo, NY.

Schroder, M., and C. Skiadas. (1999). “Optimal Consumption and Portfolio Selection with Stochastic Differential Utility.” Journal of Economic Theory 89: 68-126.

Schroder, M., and C. Skiadas. (2000). “An Isomorphism between Asset Pricing Models (with and without Linear Habit Formation).” Working Paper, Eli Broad Graduate School of Management, Michigan State University.

Schwartz, E. (1977). “The Valuation of Warrants: Implementing a New Approach.” Journal of Financial Economics 4: 79-94.

Schwartz, E. (1997). “Presidential Address: The Stochastic Behavior of Commodity Prices: Implications for Valuation and Hedging.” Journal of Finance 52: 923-973.

Schweizer, M. (1992). “Martingale Densities for General Asset Prices.” Journal of Mathematical Economics 21: 363-378.

Schweizer, M. (1994a). “Approximating Random Variables by Stochastic Integrals.” Annals of Probability 22: 1536-1575.

Schweizer, M. (1994b). “Hedging and the CAPM.” Working Paper, Department of Mathematics, University of Bonn.

Schweizer, M. (1994c). “A Projection Result for Semimartingales.” Stochastics and Stochastics Reports 50: 175-183.

Schweizer, M. (1994d). “Risk-Minimizing Hedging Strategies under Restricted Information.” Mathematical Finance 4: 327-342.

Scott, L. (1987). “Option Pricing when the Variance Changes Randomly: Theory, Estimation, and Application.” Journal of Financial and Quantitative Analysis 4: 419-438.

Scott, L. (1992). “Stock Market Volatility and the Pricing of Index Options: An Analysis of Implied Volatilities and the Volatility Risk Premium in a Model with Stochastic Interest Rates and Volatility.” Working Paper, Department of Finance, University of Georgia.

Scott, L. (1996a). “Simulating a Multi-Factor Term Structure Model over Relatively Long Discrete Time Periods.” Working Paper, Department of Banking and Finance, University of Georgia, Athens.

Scott, L. (1996b). “The Valuation of Interest Rate Derivatives in a Multi-Factor Cox-Ingersoll-Ross Model that Matches the Initial Term Structure.” Working Paper, Department of Banking and Finance, University of Georgia, Athens.

Scott, L. (1997). “Pricing Stock Options in a Jump-Diffusion Model with Stochastic Volatility and Interest Rates: Applications of Fourier Inversion Methods.” Mathematical Finance 7: 413-426.

Sekine, J. (1998). “Mean-Variance Hedging in Continuous-Time with Stochastic Interest Rate.” Working Paper, MTP Investment Technology Institute, Tokyo.

Selby, M., and S. Hodges. (1987). “On the Evaluation of Compound Options.” Management Science 33: 118-124.

Senbet, L., and T. Sargent. (1995). “Computing the Fong and Vasicek Pure Discount Bond Pricing Formula.” Working Paper, FORC Preprint 93/42, October 1993, University of Warwick.

Selden, L. (1978). “A New Representation of Preference over ‘Certain x Uncertain’ Consumption Pairs: The ‘Ordinal Certainty Equivalent’ Hypothesis.” Econometrica 46: 1045-1060.

Serrat, A. (1995). “An Equilibrium Analysis of Liquidity Constraints.” Working Paper, Sloan School of Management, Massachusetts Institute of Technology.

Serrat, A. (2000). “Exchange Rate Dynamics in a Multilateral Target Zone.” Review of Economic Studies 67: 193-211.

Sethi, S., and M. Taksar. (1988). “A Note on Merton’s ‘Optimum Consumption and Portfolio Rules in a Continuous-Time Model’.” Journal of Economic Theory 46: 395-401.

Sethi, S., and M. Taksar. (1992). “Infinite-Horizon Investment Consumption Model with a Nonterminal Bankruptcy.” Journal of Optimization Theory and Applications 74: 333-346.

Sethi, S., M. Taksar, and E. Prisman. (1992). “Explicit Solution of a General Consumption/Portfolio Problem with Subsistence Consumption and Bankruptcy.” Journal of Economic Dynamics and Control 16: 747-768.

Shannon, C. (1996). “Determinacy of Competitive Equilibria in Economies with Many Commodities.” Working Paper, Department of Economics, University of California, Berkeley. Forthcoming in Economic Theory.

Sharpe, W. (1964). “Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk.” Journal of Finance 19: 425-442.

Sharpe, W. (1985). Investments (3d ed.). Englewood Cliffs, NJ: Prentice-Hall.

Shepp, L., and A. N. Shiryaev. (1993). “The Russian Option: Reduced Regret.” Annals of Applied Probability 3: 631-640.

Shimko, D., N. Tejima, and D. van Deventer. (1993). “The Pricing of Risky Debt when Interest Rates are Stochastic.” Journal of Fixed Income 3 (September): 58-65.

Shirakawa, H. (1994). “Optimal Consumption and Portfolio Selection with Incomplete Markets and Upper and Lower Bound Constraints.” Mathematical Finance 4: 1-24.

Shreve, S., and M. Soner. (1994). “Optimal Investment and Consumption with Transaction Costs.” Annals of Applied Probability 4: 609-692.

Shreve, S., M. Soner, and G.-L. Xu. (1991). “Optimal Investment and Consumption with Two Bonds and Transaction Costs.” Mathematical Finance 1: 53-84.

Shrikhande, M. (1995). “Nonaddictive Habit-Formation and the Equity Premium Puzzle.” Working Paper, School of Management, Georgia Institute of Technology, Atlanta.

Siegel, D., and D. Siegel. (1990). Futures Markets. Orlando: The Dryden Press.

Singh, M. (1995). “Estimation of Multifactor Cox, Ingersoll, and Ross Term Structure Model: Evidence on Volatility Structure and Parameter Stability.” Journal of Fixed Income 5 (September): 8-28.

Singleton, K. (1999). “Estimation of Affine Asset Pricing Models using the Empirical Characteristic Function.” Working Paper, Stanford University and NBER. Forthcoming in Journal of Econometrics.

Sircar, R. (1996). “Feedback Effects in Option Pricing.” Working Paper, SC-CM Program, Stanford University.

Skiadas, C. (1995). “On the (Super) Differentiability of the Utility of a Representative Agent at a Pareto Optimal Allocation.” Working Paper, Private Written Communication, Kellogg School of Management, Northwestern University.

Skiadas, C. (1997). “Conditioning and Aggregation of Preferences.” Econometrica 65: 347-367.

Skiadas, C. (1998). “Recursive Utility and Preferences for Information.” Economic Theory 12: 293-312.

Smith, G. (1985). Numerical Solution of Partial Differential Equations: Finite Difference Methods (3d ed.). Oxford: Clarendon Press.

Soner, M., S. Shreve, and J. Cvitanic. (1994). “There is No Nontrivial Hedging Portfolio for Option Pricing with Transaction Costs.” Annals of Applied Probability 5: 327-355.

Song, S. (1998). “A Remark on a Result of Duffie and Lando.” Working Paper, Department.of Mathematics, Université d’Evry, France.

Sorenson, E., and T. Bollier. (1995). “Pricing Default Risk: The Interest-Rate Swap Example.” In Derivative Credit Risk. London: Risk Publications.

Sornette, D. (1998). “String Formulation of the Dynamics of the Forward Interest Rate Curve.” Working Paper, Université des Sciences, Parc Valrose, France, and Institute of Geophysics and Planetary Physics, University of California, Los Angeles.

Stambaugh, R. (1988). “The Information in Forward Rates: Implications for Models of the Term Structure.” Journal of Financial Economics 21: 41-70.

Stanton, R. (1995a). “A Nonparametric Model of Term Structure Dynamics and the Market Price of Interest Rate Risk.” Journal of Finance 52: 1973-2002.

Stanton, R. (1995b). “Rational Prepayment and the Valuation of Mortgage-Backed Securities.” Review of Financial Studies 8: 677-708.

Stanton, R., and N. Wallace. (1995). “ARM Wrestling: Valuing Adjustable Rate Mortgages IndexedVargiolu, T. (1999). “Invariant Measures for the Musiela Equation with Deterministic Diffusion Term.” Finance and Stochastics 3: 483-492.

Vasicek, O. (1977). “An Equilibrium Characterization of the Term Structure.” Journal of Financial Economics 5: 177-188.

Vasicek, O. (1995). “The Finite Factor Model of Bond Prices.” Working Paper, KMV Corporation, San Francisco.

Vayanos, D. (1998). “Transaction Costs and Asset Prices: A Dynamic Equilibrium Model.” Review of Financial Studies 11: 1-58.

Vayanos, D., and J.-L. Vila. (1999). “Equilibrium Interest Rate and Liquidity Premium with Transaction Costs.” Economic Theory 13: 509-539.

Vila, J.-L., and T. Zariphopoulou. (1997). “Optimal Consumption and Portfolio Choice with Borrowing Constraints.” Journal of Economic Theory 77: 402-431.

Walras, L. (1874-1877). Eléments d'Economie Politique Pure (4th ed.). Lausanne: L. Corbaz,
English translation of the definitive edition by W. Jaffé, Elements of Pure Economics.
London: Allen and Unwin, (1954).

Wang, J. (1993a). “A Model of Intertemporal Asset Prices under Asymmetric Information.”
Review of Economic Studies 60: 249-282.

Wang, J. (1996). “The Term Structure of Interest Rates in a Pure Exchange Economy with
Heterogeneous Investors.” Journal of Financial Economics 41: 75-110.

Wang, S. (1993b). “The Integrability Problem of Asset Prices.” Journal of Economic Theory 59: 199-213.

Wang, S. (1993c). “Is Kreps-Porteus Utility Distinguishable from Intertemporal Expected Utility?” Economic Theory 3: 119-127.

Wang, S. (1993d). “The Local Recoverability of Risk Aversion and Intertemporal Substitution.”
Journal of Economic Theory 59: 333-363.

Webber, N. (1990). “The Term Structure of Spot Rate Volatility and the Behavior of Interest
Rate Processes.” Working Paper, Financial Options Research Centre, University of Warwick.

Webber, N. (1992). “The Consistency of Term Structure Models: The Short Rate, the Long
Rate, and Volatility.” Working Paper, Financial Options Research Centre, University of Warwick.

Weerasinghe, A. (1998). “Singular Optimal Strategies for Investment with Transaction Costs.”
Annals of Applied Probability 8: 1312-1330.

Weil, P. (1992). “Equilibrium Asset Prices with Undiversifiable Labor Income Risk.” Journal of Economic Dynamics and Control 16: 769-790.

Werner, J. (1985). “Equilibrium in Economies with Incomplete Financial Markets.” Journal of Economic Theory 36: 110-119.

Werner, J. (1991). “On Constrained Optimal Allocations with Incomplete Markets.” Economic Theory 1: 205-209.

Whalley, A. E., and P. Wilmott. (1997). “An Asymptotic Analysis of an Optimal Hedging
Model for Options with Transaction Costs.” Mathematical Finance 7: 307-324.

Wiggins, J. (1987). “Option Values under Stochastic Volatility: Theory and Empirical Estimates.” Journal of Financial Economics 19: 351-372.

Willard, G. (1996). “Calculating Prices and Sensitivities for Path-Independent Derivative
Securities in Multifactor Models.” Working Paper, Washington University in St. Louis.

Willinger, W., and M. Taqqu. (1989). “Pathwise Stochastic Integration and Application to the Theory of Continuous Trading.” Stochastic Processes and Their Applications 32: 253-280.

Willinger, W., and M. Taqqu. (1991). “Toward a Convergence Theory for Continuous Stochastic Securities Market Models.” Mathematical Finance 1: 55-100.

Wilmott, P., J. Dewynne, and S. Howison. (1993). Option Pricing: Mathematical Models and Computation. Oxford: Oxford Financial Press.

Wilmott, P., S. Howison, and J. Dewynne. (1995). The Mathematics of Financial Derivatives.
Cambridge: Cambridge University Press.

Won, D. (1996a). “Generic Existence of Equilibrium in Incomplete Markets: The Case of
Differential Participation.” Working Paper, Korea Economic Research Institute, Seoul.

Won, D. (19Jf 9dB, 84, 335 f 0dS, 87

# Symbol Glossary

fax, 95 corr(-), 12 tr(A), 95 max(x, y), 57 VU (x), 328 VU (x*; y) < 0, 328 VU (c*), 222
VU (c*; c), 25 aU(c*), 5 U(c!), 13 σ-algebra, 21, 329 σ-field, 21, 329 σ(Z), 324

d(F, G) = 0, 67 9 95

H', 86, 94 32(5), 87 H^2(X), 95 L(S), 87 ¥(X), 95

, 86, 94

3 84, 94

Aase, 232, 257 Abel, 79 Abken, 290 Acharya, 80, 289
Adams, 166 Adler, 233 Ahn, 133, 233 Ait-Sahalia, 165, 197
Ait-Sahalia, 199, 319 Aiyagari, 80 Akahari, 200 Akian, 234
Aliprantis, 255 Allegretto, 199 Allingham, 18 Alvarez, 233, 234 Amaro de Matos, 199 Amendinger, 132, 234
Amin, 165, 197, 198, 317, 319 Andersen, 162, 165, 197, 198, 200, 201, 318
Anderson, 289 Andreasen, 100, 162, 165, 198, 200, 318, Ansel, 132, 233 Antonelli, 234
Apelfeld, 162 Araujo, 19, 79, 255 Arntzen, 234 Arrow, 17, 18
Artzner, 131, 133, 162, 166, 290 Arvantis, 290 Assaf, 234 Au, 164
Avellaneda, 133, 196, 234, 317, 318 Babbs, 133, 164, 166
Back, 132, 133, 166, 232, 233, 234, 256, 257 Backus, 165, 166

# Author Index

Bajeux-Besnainou, 47, 162, 233, 257 Bakshi, 198, 200 Balasko, 18 Balduzzi, 163, 166, 234
Ball, 165, 197, 199 Bally, 233, 318 Bank, 233 Banz, 132
Barberis, 80 Barles, 197, 199, 200, 233, 319 Barndorff-Nielsen, 199 Barone, 166
Barone-Adesi, 199 Barraquand, 318, 319 Basak, 257 Bates, 198, 199
Baxter, 164 Baz, 165 Beaglehole, 163, 319 Becker, 78
Beckers, 197 Beibel, 199 Bellman, 63 Beltratti, 79
Bensoussan, 46, 199, 232, 291 Benth, 232 Benveniste, 63, 78 Benzoni, 198
Berardi, 163 Bergman, 133, 198, 200, 233 Berk, 18, 19, 47 Bernard, 318
Bertola, 166 Bertsekas, 63, 78 Bertsimas, 317 Bewley, 79, 255 Bhar, 164

Bick, 100, 133, 196, 197, 234, 257, 336 Bielecki, 290 Billingsley, 317 Bjerksund, 319
Bjork, 165, 166 Black, 17, 18, 64, 100, 161, 164, 197, 256, 288, 289, 319 Blackwell, 78
Blume, 79 Bodurtha, 165 Bollerslev, 198 Bonomo, 257
Bossaerts, 64, 166, 233 Bottazzi, 18, 47 Boudoukh, 165 Bouleau, 233, 320 Boyarchenko, 289 Boyd, 19, 78
Boyle, 19, 133, 318 Brace, 162, 164, 165, 166, 320 Bray, 18 Breeden, 132, 256
Bremaud, 289 Brennan, 164, 200, 233, 289, 319 Broadie, 199, 232, 317, 318, 319 Brock, 78
Brotherton-Ratcliffe, 197, 200 Brown, 47, 79, 162, 163, 197 Broze, 165 Buckdahn, 199, 233 Buff, 318 Buhler, 165 Buhlmann, 133 Bunch, 319
Buono, 165 Burdeau, 199 Burkinshaw, 255 Butler, 162, 163, 319
Cadenillas, 234 Caflisch, 318 Calvet, 80 Campbell, 79, 165, 166, 257, 289 Cao, 198, 257 Carassus, 133
Carpenter, 289 Carr, 133, 162, 197, 198, 199, 200, 319, 320
Carverhill, 161, 162, 164, 165, 166, 234, 257, 317, 318 Cass, 18, 47 Cassese, 132 Caton, 289

# Author Index

Chacko, 162 Chae, 19, 47 Chalasani, 317 Chamberlain, 257
Chan, 163, 164, 165 Chang, 197, 234 Chapman, 46, 233, 256, 353 Charretour, 199
Chen, 133, 162, 163, 197, 198, 256, 289 Cheng, 165 Cherian, 197 Cherif, 163
Chernoff, 319 Chernov, 198 Cherubini, 161, 162 Chesney, 162, 200
Chevance, 318 Chew, 46 Cheyette, 164, 165 Chiarella, 164, 320 Chidambaran, 318 Chou, 198 Choulli, 131 Chow, 317
Christensen, 133, 166, 256 Chuang, 200 Chung, 317, 334 Citanna, 47 Clark, 132, 133, 198 Clarke, 319
Clewlow, 133, 162, 163, 234, 317, 318, 319 Cohen, 162 Colell, 255 Coleman, 166
Constantinides, 46, 80, 133, 163, 233, 234, Cont, 164 Conze, 133, 162, 199 Cooper, 289, 290 Cornell, 256 Courtadon, 161, 318
Cover, 80, 234 Cox, 100, 161, 162, 163, 165, 196, 232, 234, 256, 257, 289, 317 Crouhy, 291 Cuoco, 46, 232, 233, 234, 257 Curran, 317
Cutand, 100, 317 Cvitanié, 133, 200, 232, 233, 234, 289

# Author Index

Daher, 162, 319 Dahlquist, 166 Dai, 163 Daigler, 196 Daley, 289 Dana, 255 Danesi, 165 Darling, 233
Das, 162, 163, 165, 290 Dash, 163, 319 Dassios, 200 Davis, 133, 161, 234, 289, 291
Davydov, 200, 201, 290 Dayal, 133 Debreu, 18, 45 Décamps, 162, 200, 289, 291 Deelstra, 161 Dekel, 46
Delbaen, 131, 132, 133, 161, 166, 290 Delgado, 256 DeMarzo, 47, 48 Dempster, 319
DeMunnik, 161, 162, 163, 164, 165, 166 Dengler, 319 der Hoek, 161 Derman, 64, 161, 164, 197, 200, 319 Derviz, 232
Detemple, 47, 199, 233, 234, 256, 257, 319, Dewynne, 196, 318 Dezhbakhsh, 196 Diament, 166
Diener, 317 Dijkstra, 133 DiMasi, 165 Dixit, 196, 233, 289
Donaldson, 79 Dothan, 45, 133, 162, 163, 165, 234, Douglas, 318 Dritschel, 132
Druskin, 318 Dreze, 17 Duan, 163, 197 Duffee, 163, 165
Duffie, 46, 47, 48, 63, 78, 79, 80, 100, 132, 162, 163, 164, 166, 196, 197, 198, 200,
233, 234, 255, 256, 257, 290, 291, 317, Dumas, 79, 80, 234, 255, 256, 257 Dunn, 46 Dupire, 64, 197

Durrett, 317, 318 Dybvig, 131, 162, 165, 233, 234, 319 Dynkin, 78

Easley, 79 Eaves, 47 Eberlein, 165, 199, 317 Ederington, 289 Edirisinghe, 133, 234 Ekern, 233
El Karoui, 100, 131, 132, 133, 161, 162, 163, 164, 165, 198, 232, 233, 234 Elliot, 161 Elliott, 162, 199, 290 Ellis, 200 Embrechts, 133
Engle, 198 Epstein, 46, 64, 78, 80, 233, 256, 257, Eraker, 199 Ericsson, 291 Esposito, 161, 162, 163 Evnine, 318 Eydeland, 320

Faguet, 199, 319 Fan, 289 Faure-Grimaud, 289 Fazel, 19Trevor, 164, 320

Tsiveriotis, 289

Tubaro, 318

Tufano, 290

Turnbull, 162, 196, 197, 290

Uhlig, 47

Uhrig-Homburg, 165, 289 Unal, 290

Uppal, 133, 200, 234, 255, 256 Uzawa, 233

Van Deventer, 166, 291 Van Horne, 161

Van Moerbeke, 199 Vargiolu, 165

Varikooty, 317

Vasicek, 162, 163 Vayanos, 234, 256 Vere-Jones, 289 Vetterling, 163, 318, 319 Vetzal, 317

Vigo, 80

Vila, 233, 234 Villanacci, 47

Vind, 19

Viswanathan, 133, 162, 163, 164, 199 Vorst, 133, 198

Waldvogel, 162, 163, 319

Wallace, 165, 319

Walras, 17

Walter, 165

Wang, 19, 78, 80, 233, 234, 255, 256, 257,

Watanabe, 161, 162, 342

Webber, 166

Weber, 165

Weerasinghe, 234

Weil, 19, 46, 80

Weiss, 80, 233

Weisz, 132

Werner, 18, 47, 80, 233

Whaley, 162, 196, 197

Whalley, 133

White, 79, 161, 166, 197, 290, 318,

Whitelaw, 165

Wiener, 100, 198

Wiggins, 197

Willard, 131, 257, 319 Williams, 334 Willinger, 100, 317, 336 Wilmott, 133, 196, 318 Wolff, 165

Won, 47

Woodford, 78, 79

Wu, 47, 319

Xu, 232, 233, 234 Xue, 234

Yaari, 165 Yamada, 161 Yamazaki, 19 Yao, 161

Yong, 164, 234 Yor, 200, 290, 334

# Author Index

Yu, 78, 197, 199, 200, 290 Yushkevich, 78

Zacklad, 162

Zakoian, 165

Zame, 19, 79, 80, 255, 256, 257 Zapatero, 233, 234, 256, 257, 319, 353 Zariphopoulou, 133, 232, 233, 234 Zechner, 288

Zervos, 166

Zhang, 199, 319

Zhao, 318

Zheng, 166

Zhou, 47, 200, 234, 317

Zhu, 233, 320

Zin, 46, 64, 78, 80, 165, 166

Zou, 200

Zuasti, 257

Zvan, 317

absence of arbitrage, 108

absolute priority, 263

actions, 203

adapted, 332

adapted process, 21

additive utility, 25, 60

admissible controls, 204

affine, 142, 179, 180

affine diffusion, 149

affine, intensity, 279

affine model, empirical estimation, 163

affine term-structure model, 142, 149, 162

affine volatility process, 179

after-tax, 268

agent, 5

aggregate endowment, 8

aggregation, 15, 18, 41

algebra, 323

allocation, 8

almost everywhere, 87

almost surely, 329

ambiguity aversion, 257

American barrier options, 199

American call, 36

American call, with dividends, 36

American option, early exercise premium,

American option, free boundary problem,

American option price, 46, 199

American option price, numerical solution,

American option, Stefan problem, 199

American options with jumps, 199

American put, 32, 36, 188, 309

American securities, using the semi-group approach to, 314

American security, 32, 46, 57, 182

# Subject Index

analytic, 355

antithetic sampling, 299

approximate arbitrage, 121, 132

arbitrage, 1, 22, 70, 89, 102, 123, 126

arbitrage pricing theory, 18

ARCH, 198

arrears, 145

Arrow-Debreu equilibria in infinite-dimensional settings, 255

Arrow-Debreu equilibrium, 15, 40, 237

Arrow-Pratt measure, 245

Asian option, 190, 200, 317

asset pricing formula, 10

asset pricing, nonadditive utility, 256

asset substitution, 261, 271

assets, 260

asymmetric information, 257

asymptotic distribution, 76

at market, 145

augmented filtration of a process, 359

average-rate options, 200

Azema’s martingale, 132

Bachelier, 84

backward difference equation, 305

backward Kolmogorov equation, 346

backward SDEs, 318

backward stochastic differential equations,

Banach lattice, 255

bankruptcy, 234

barrier option, 38, 200, 317

basic HJM drift restriction, 164

Bellman condition, 187

Bellman equation, 50, 53, 57, 68, 204

Bellman’s principle of optimality, 63

Bermudan swaption, 146

Bernoulli trials, 295

Bessel function, 147

beta, 15, 107

betweenness certainty equivalent, 46

binary options, 201

Binomial Approximation of the Black-Derman-Toy, 316

Binomial Option Pricing, 14, 21, 37

binomial option pricing, limit, 293

binomial stock returns, 295

binomial term-structure models, 61, 64

bivariate binary options, 201

Black-Derman-Toy model, 64, 138, 147, 155,

Black-Karasinski model, 138

Black-Scholes, 100, 133, 174, 294

Black-Scholes, convergence to, 294

Black-Scholes formula, 48, 90, 294

Black-Scholes implied volatilities, 174

Black-Scholes option pricing formula, in equilibrium, 257

Black-Scholes-Merton model, 259

Blackwell’s Theorem, 78

bond, 88

bond options, American, 162

bond-option pricing in a Gaussian setting,

Borel, 329

boundary condition, 91

bounded, 85

bounded adapted processes, 66

Brownian motion, geometric, 88

Brownian motion, martingale, 97

budget-feasible consumption set, 5, 24

buy-at-the-min, 190

calibration, 161, 165, 175, 197, 295 call option, 14

callable bonds, 281

callable convertible debt, 199 cancellable call option, 58

cap pricing, 145, 160, 162

Capital Asset Pricing Model, 12, 18, 257 capital structure, 261

capital-stock process, 246

caplet, 145, 161

CAPM, 12, 14, 15, 18

CAPM, two factor, 257

carrying costs, 197

cash settlement, 171

Cauchy problem, 302, 342

CBI processes, 162

# Subject Index

CCAPM, 249

Central Limit Theorem, 293, 294, 296, 317,

changes of numeraire, 201

cheapest-to-deliver option, 197

CIR, density function, 161

CIR, discrete-time model, 161, 256

CIR, empirical estimation, 162

CIR, empirical results, 256

CIR, Laplace transform, 161

CIR model, 141, 142, 161, 248, 254, 315,

CIR model, calibration, 315

CIR, nonnegativity of interest rate, 161

closed, 118

collateral, 274

collateral constraints, 47, 257, 274

collateralized debt obligations, 291

commodity prices, 166

commodity, term-structure models, 200

compact metric space, 78

compensated counting process, 275

complement, 323, 329

complementary slackness condition, 327

complete, 8, 26, 117

complete markets, 8, 27, 117

completed, 330

completion, 84, 330

complex options, 291

compound options, 291

computation of equilibrium, 47

concave program, 327

conditional expectation, 324, 332

conditional expected rate of return, 106

cone, 4

consistency of GMM estimators, 76

consistent, 75

consol, 252, 263

consol rate, 164

constrained participation, 18

constraints, 200

consumption, 207

consumption process, 24, 39, 48, 66, 256

consumption-based CAPM, 108, 246, 256

consumption-based CAPM, incomplete markets, 249

consumption CAPM, transaction costs, 256

continually compounding interest rate, 88

continuation region, 187

continuous, 25

Continuous Mapping Theorem, 297, 317

# Subject Index

continuous-branching processes, 162

continuously compounding yield, 137

control problem, 67

controlled diffusion function, 204

controlled drift function, 203

controls, 203

convergence, 171

convergence of the binomial model, 294,

converges in distribution, 293, 330

converges in probability, 330

convertible bond, 200, 274, 281, 289, 320

convexity, 198

corporate debt, 259

correlation, 12

cost-of-carry formula, 170

counting process, 357

covariance, 11

Cox-Ingersoll-Ross, 141, 147, 177, 197, 246, 341, 363

Cox-Ingersoll-Ross, fundamental solution,

Crank-Nicholson approach, 303, 311, 318

credit derivatives, 281

credit-constrained, 131

cum-dividend, 22, 23, 102, 126, 127, 308

cum-dividend value, 57

cumulative dividend, 123

cumulative dividend process, 97, 235

cumulative-return process, 106

currency convergence, 166

currency options, 158, 200

curve-fitting, 166

debt overhang, 272

decentralized production decisions, 254 default correlation, 291

default risk premium, 287

defaultable swaps, 290

default-adjusted short rate, 288

deflated cumulative-dividend process, 124 deflated gain process, 24, 124

deflator, 23, 102

delivery arbitrage, 43, 171

delivery date, 42

density process, 29, 110

derivative asset pricing, 48

derivative security, 92

derivatives, credit risk, 290 determinacy, 79

diff swaps, 162

differential approach, 18

diffusion, 87, 340

Diffusion Invariance Principle, 339 Dirac measure, 147

directional, 328

disappointment aversion, 257 discount, 5, 28

discount function, 137, 168

discount rate, 213

discretization errors, 317

dispersed expectations, 47

distance, 67

dividend process, 22

dividend yield, 98dividend-price pair, 5, 22, 123 dividend-rate process, 123, 235
Dominated Convergence Theorem, 331 double-barrier, 200

double-step, 201

double-step options, 201

doubling strategies, 184

doubling strategy, 131

doubly stochastic, 276, 290, 359 doubly stochastic, counter-example, 288 down-and-outs, 200

drift, 87

driven by some filtration, 276

duality and optimality, 47

duality techniques, 232

Dudley's Theorem, 336

dynamic programming, 50, 63, 78, 320 dynamic programming, recursive-utility, 64 dynamic spanning condition, 256

early exercise, 36, 309

econometric estimation of term-structure models, 165

econometrics, 73

economy, 8

efficient allocation, 237

EGARCH, 198

elliptic, 344

empirical average, 74

empirical distribution vector, 73

endowment, 5, 24, 235

enlargement of filtrations, 132, 234

equilibrium, 1, 8, 26, 237

equilibrium, indeterminacy, 47

equilibrium, recursive utility, 256

equity, 259

equity-premium puzzle, 79

equivalent, 28, 108

equivalent martingale measure, 28, 41, 43, 45, 100, 108, 132, 167

equivalent martingale measure, constraints,

equivalent martingale measure, counterexample, 132

equivalent martingale measure, infinite-horizon case, 131

equivalent martingale measure, transactions costs, 133

equivalent measures, 324

error coefficient, 298

Escher transform, 200

essential supremum, 184

essentially bounded, 118

Euclidean norm, 340

Euler approximation, 298

European call option, 37, 89

European put option, 294

events, 21, 323

ex dividend, 22, 126, 236, 308

exercise, American calls, 36

exercise boundary, 199

exercise policy, 31, 182

exercise price, 14, 32, 37

exercise region, 186

existence with recursive utility, 255

exotic options, 191, 319

expectation, 324, 330

expectations hypothesis, 166

expected utility, 7

expiration time, 31, 32, 37

explicit methods, 318

exponential-affine, 179

fair price, 199

Farkas's Lemma, 12, 18

fast Fourier transform, 198

FBSDE, 234

feasible, 8, 237

feasible allocation, 8

feasible directions, 328

feedback, 54, 69, 205

Feynman-Kac solution, 94, 253, 343 field, 323

filtering, 162, 234, 257

filtration, 21, 324

filtration, right-continuous, 347 filtration, usual conditions, 347 finances a consumption process, 98, 236 finite-difference, 197, 302, 318 finite-difference, binomial method, 319

# Subject Index

finite-variation process, 347

first to default, 288

first-order risk aversion, 80

first-order scheme, 298

fixed point, 68

Fixed Point Theorem, 19

fixed-income securities, 135

fixed-point, 78

floating-rate note, 286

floating-rate notes, 285

floor, 145

Fokker-Planck equation, 146, 311, 346

Fokker-Planck equation, 163

foreign bond options, 158

foreign exchange rates, 257

foreign term-structure models, 165

foreign-currency, 158

foreign-exchange option, 200

forward contract, 42

forward curves, commodities, 166

forward difference equation, 311

forward Kolmogorov equation, 146, 311,

forward measure, 201

forward price, 42, 151

forward-backward stochastic differential equations, 234

forward-measure approach, 161

forward-rate model, 164

forwards and futures, 196

Fourier transform, 180, 198

Fourier transform methods, 320

fractional Brownian motion, 100

free boundary problem, 319

free lunch, 132

free lunch with vanishing risk, 132

free-boundary problem, 199, 320

Frobenius-Perron Theorem, 73

Fubini's Theorem, 333

Fubini's Theorem for stochastic integrals,

fundamental solution, 146, 163, 310, 319,

fundamental solution, CIR model, 147

futures and forwards, 162

futures contract, 42

futures, hedging, 225

futures, interest rate, 162

futures position process, 172

futures price, 42

Futures-Forward Price Equivalence, 42

futures-price process, 171

# Subject Index

gain process, 24, 87, 97, 123, 236

GARCH, 175, 198

GARCH, option pricing, 198

Gateaux, 328

Gaussian, 342

Gaussian forward-rate model, 156

Gaussian short-rate model, 161

general equilibrium, 45

generalized autoregressive conditional heteroscedastic, 175

generalized method of moments, 75, 79

generated, 22, 124

generic, 78

generic existence of equilibrium, 47

geometric Brownian motion, 88

Girsanov's Theorem, 111, 117, 337

gradient, 39, 328, 351

gradient, utility, 233

Green's function, 146, 163, 319, 345

Green's function, numerical solution, 310

grid, 303, 307

growth, 340

growth condition, 341

growth-optimal policies, 133, 234

habit-formation, 26, 40, 46, 80, 223, 233, 256, 353

Hahn-Banach Theorem, 122

Hamilton Jacobi-Bellman (HJB), 205, 232

HARA, 210

hazard function, 361

hazard rate, 361

Heath-Jarrow-Morton, 151, 155, 197

Heath-Jarrow-Morton model, 339

hedging under leverage constraints, 200

Hessian matrix, 13

Heston, 182, 193, 194

Heston model, 177, 179

heterogeneous agents and incomplete markets, 79

heterogeneous beliefs, 257

high-ordercontact 266

Hilbert space, 16, 255

HJM drift restriction, 164

HJM, estimation, 165

HJM model, 164, 320

HJM, model Markov variation, 164

HJM, numerical methods, 220

Hölder continuous, 344

Ho-Lee, 62, 64, 138, 140, 147

hyperbolic absolute risk averse (HARA),

hyperbolic SPDEs, 155

illiquidity, 291

imperfect information, 162 implicit, 318

Implicit Function Theorem, 13, 244 implied volatility, 64, 197 irreversible investment, 233

Ito process, 86

Ito's Formula, 87

Ito's Lemma, 87

jointly measurable, 332 jump, 125, 347 jump-diffusion, 198

Kakutani's Fixed Point Theorem, 13
Knightian uncertainty, 80, 257 knock-ins, 190, 200

knock-outs, 31, 190, 200 Kreps-Porteus, 40

Kreps-Yan Theorem, 122

Lévy Inversion Formula, 180

Lévy's characterization of Brownian motion,

Lagrange multiplier, 9, 327

Lagrangian, 327

Large Deviations Theorem, 318

large investor, 234

latent, 148

law of iterated expectations, 324, 332

law of large numbers, 73, 299, 317

law of large numbers for Markov chains, 73

left limits, 347

left-continuous, 347

leverage constraints, 200

LIBOR, 161, 162

limit in probability, 84

limited liability, 263

limited-rationality, 80

limited-risk options, 200

Lindeberg-Feller Central Limit Theorem, 294, 331

linear equations of the tridiagonal form,

linear regression, 11

linear stochastic differential equation, 342

linear subspace, 4, 121

linearity of stochastic integrals, 123

Lipschitz, 340

local martingale, 212

local martingale measure, 130

local substitution for consumption, 233 local time, 133

local-expected-utility, 46

locally, 344

locally Lipschitz, 341

lock-in options, 200

logarithmic additive utility, 234 log-normal, 88

log-optimal, 80

long-term interest rates, 165 lookback options, 189, 190, 200, 318 Lucas model, 1

lump-sum dividend, 125

Malliavin calculus, 221, 232, 320

marginal rates of substitution, 103

marginal utility, 5

marginal utility of a representative agent,

marginal-rate-of-substitution process, 23

market completeness under a change of measure, 132

market imperfections, 133, 261

market model, 165

market model, cap pricing, 160

market return, 15

market risk aversion, 250

market time, 198

marketed space, 22, 117

marketed space, L*-closedness, 131

marketprice-of-risk process, 112

market-value process, 106

marking to market, 42

Markov, 51, 52, 78, 96

Markov chain, 63, 65, 78

Markov chain, continuous-time, 349

Markov dynamic programming, 52

Markov equilibrium, 69

Markov single-agent asset pricing model,

Markovian versions of the HJM model, 164

martingale, 22, 24, 85, 97, 325, 332

martingale approach to optimal investment,

martingale generator, 238

martingale representation property, 117, 338, 339, 359

martingale representation theorem, 336,

maturity goes to infinity, 165

# Subject Index

Mean Value Theorem, 351

mean-reversion, 138, 248

mean-summable, 71

mean-variance criteria in a continuous-time setting, 233

measurable, 323

median-price options, 200

Merton, 140

Merton model, 138

mesh sizes, 303transversality condition, 213

triangular array, 294, 331

tribe, 21, 323, 329

tribe generated, 324, 329

tridiagonal matrix, 305, 306, 311, 318 turnpike, 79, 234

two-fund separation, 18

uniform strong law of large numbers, 79

uniformly in t, 341

uniformly integrable, 297, 316, 331

uniformly parabolic, 345

unique decomposition property of Ito processes, 87, 90

uniqueness of equilibria, 255

uniqueness of equivalent martingale measures, 114

unit zero-coupon riskless bond, 126

up-and-ins, 200

usual conditions, 347

utility function, 5

utility gradients, 233, 351

utility process, 40

utility representations, 18

value, 67, 204

value function, 50, 78

value function, differentiability, 59, 63 value iteration, 67

variance reduction techniques, 299
Vasicek term-structure model, 140, 160, 256 viscosity solutions, 232

volatility, 88

volatility, CIR process, 177

volatility, GARCH limit, 176

volatility, Heston model, 177

volatility process, 175

volatility, stochastic, 177

von Neumann-Morgenstern, 46

weak solution, 340 weakly arbitrage-free, 12 wealth process, 49 weighting matrices, 76 Wiener-Chaos, 100 wildcard option, 197

yield, 142 yield options, 162 yield-spread option, 159

zero-beta return, 15 zero-coupon bond, 136, 166, 238

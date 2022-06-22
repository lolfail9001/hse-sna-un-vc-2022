# Problem statement

We are interested in, being given a weighted graph $G(V,E)$ expressing correlation between voting records of various countries, to design a partition of $V$ into $k$ separate blocs. Since the sample size of our problem as is not particularly sufficient for supervised algorithms, we propose to use the information we have to optimize some functional that maps a partition of $V$ to a number. Albeit, this is a problem from combinatorial optimization and is *a priori* bound to not have a polynomial time solution. As such, we propose to approximate solving this problem by replacing original function by a functional that maps distributions $p_{v}$, assigned to each node $v \in V$, to a number.

# Choice of a functional

We want a functional that is convex to enable appropriate optimizatino algorithms, and that straightforwardly models our problem. Albeit, this ended up in a failure to find appropriate function to optimize, so We made a different choice: the functional we will optimize models which nodes may not be a part of the voting bloc. To that end, we may propose different choices of a main function, but the one We chose is the following:

$$
\mathcal F = \sigma \ln \left[\frac{1}{|V|}\sum_{u\in V} E(u,v) e^{p_u \cdot p_v}\right]
$$

Where $\forall u\in V$ it holds that $\sum_i p_u(i) = 1$ and $E(u,v)$ reflects covariance between voting records accurately, namely the greater it is, the more correlated voting records are. Using the covariance itself works fine in this context.

# Optimization

We don't have particularly many choices when it comes to optimization of non-linear functions over a set of equality and boundary constraints, but the algorithm chosen was SciPy's implementation of interior point algorithm described in  [1]. Empirically, the important implementation detail here is that gradient jumps we provide must be big enough, otherwise we will fall into local minimum of the Lagrangian function of equiprobable distribution of everything.

# Post-processing

The result of optimizing functional above will be a vector of size $k|V|$ which contains discrete values for each distribution. As a matter of fact, it is easy to see that when it works properly, every distribution will be focused around one of the points, thus partitioning $|V|$ into $k$ blocs. Albeit, unlike partition we seek, the property of this partition is that countries within 1 bloc are most likely to not be a part of voting bloc. We shall use this information to remove related edges from the initial voting graph, and study the effect of it on normal graph analysis metrics used in the past.













# References

[1] -- Byrd, Richard H., Mary E. Hribar, and Jorge Nocedal. 1999. An interior point algorithm for large-scale nonlinear programming. SIAM Journal on Optimization 9.4: 877-900.

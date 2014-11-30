#13. Commutability and compatibility

A state may be simultaneously an eigenstate of two observables.
If the state corresponds to the ket vector $\ket{A}$ and the observables are
$\xi$ and $\eta$, we should then have the equations
$$\xi\ket{A} = \xi'\ket{A}$$
$$\eta\ket{A} = \eta'\ket{A}$$

Where $\xi'$ and $\eta'$ are eigenvalues of $\xi$ and $\eta$ respectively. We can now deduce
$$\xi\eta\ket{A} = \xi\eta'\ket{A} = \xi'\eta'\ket{A} = \eta\xi'\ket{A} = \eta\xi\ket{A},$$
or
$$\left(\xi\eta - \eta\xi\right)\ket{A} = 0.$$

This suggests that the chances for the existence of a simultaneous eigenstate are most favourable if $\xi\eta - \eta\xi = 0$ and the two observables commute. If they do not commute a simultaneous eigenstate is not impossible, but is rather exceptional. On the other hand, *if they do commute there exist so many simultaneous eigenstates that they form a complete set*, as will now be proved.

Let $\xi$ and $\eta$ be two commuting observables. Take an eigenket of $\eta$, $\ket{\eta'}$ say, belonging to the eigenvalue $\eta'$, and expand it in terms of eigenkets of f in the form of the right-hand side of (25), thus
\begin{equation}
\ket{\eta'} = \int \ket{\xi' \eta' c} \operatorname{d}\xi' + \sum_r \ket{\xi^r \eta' d}.
\end{equation}

The eigenkets of $\xi$ on the right-hand side here have $\eta'$ inserted in them as an extra label, in order to remind us that they come ﬁom the expansion of a special ket vector, namely $\eta'$, and not a general one as in equation (25). We can now show that each of these eigenkets of $\xi$ is also an eigenket of $\eta$ belonging to the eigenvalue $\eta'$. We have
\begin{align}
0 = \left(\eta -\eta'\right)\ket{\eta'} = \int \left(\eta -\eta'\right)\ket{\xi'\eta'c}\operatorname{d}\xi' + \sum_r \left(\eta - \eta'\right)\ket{\xi^r\eta'd}.
\end{align}

Now the ket $\left(\eta-\eta'\right)\ket{\xi^r\eta'd}$ satisfies
\begin{aligned}
\xi\left(\eta-\eta'\right)\ket{\xi^r\eta'd} = \left(\eta-\eta'\right)\xi\ket{\xi^r\eta'd} &= \left(\eta -\eta'\right) \xi^r\ket{\xi^r\eta'd} \\\\
            &= \xi^r\left(\eta - \eta'\right)\ket{\xi^r\eta'd},
\end{aligned}
showing that it is an eigenket of $\xi$ belonging to the eigenvalue $\xi^r$, and similarly the ket $\left(\eta - \eta'\right)\ket{\xi'\eta'c}$ is an eigenket of $\xi$ belonging to the eigenvalue $\xi'$. Equation (48) thus gives an integral plus a sum of eigenkets of $\xi$ equal to zero, which, as we have seen with equation (31), is impossible unless the integrand and every term in the sum
vanishes. Hence
$$\left(\eta -\eta'\right)\ket{\xi'\eta'c} = 0, \, \left(\eta - \eta'\right)\ket{\xi^r\eta'd} = 0,$$
so that all the kets appearing on the right-hand side of (47) are
eigenkets of $\eta$ as well as of $\xi$. Equation (47) now gives $\ket{\eta'}$ expanded in terms of simultaneous eigenkets of $\xi$ and $\eta$. Since any ket can be expanded in terms of eigenkets $\ket{\eta'}$ of $\eta$, it .follows that any ket can be expanded in terms of simultaneous eigenkets of $\xi$ and $\eta$, and thus the simultaneous eigenstates form a complete set.

The above simultaneous eigenkets of $\xi$ and $\eta$, $\ket{\xi'\eta'c}$ and $\ket{\xi^r\eta'd}$, are labelled by the eigenvalues $\xi'$ and $\eta'$, or $\xi^r$ and $\eta'$, to which they belong, together with the labels $c$ and $d$ which may also be necessary. The procedure of using eigenvalues as labels for simultaneous eigenvectors will be generally followed in the future, just as it has been followed in the past for eigenvectors of single observables.

The converse to the above theorem says that, *if $\xi$ and $\eta$ are two observables such that their simultaneous eigenstates form a complete set, then $\xi$ and $\eta$ commute*. To prove this, we note that, if $\ket{\xi'\eta'}$ is a simultaneous eigenket belonging to the eigenvalues $\xi'$ and $\eta'$,
\begin{equation}
\left(\xi\eta-\eta\xi\right)\ket{\xi'\eta'} = \left(\xi'\eta'-\eta'\xi'\right)\ket{\xi'\eta'} = 0.
\end{equation}
Since the simultaneous eigenstates form a complete set, an arbitrary ket $\ket{P}$ can be expanded in terms of simultaneous eigenkets $\ket{\xi'\eta'}$, for each of which (49) holds, and hence
$$\left(\xi\eta-\eta\xi\right)\ket{P} = 0$$
and so
$$\xi\eta-\eta\xi = 0$$

The idea of simultaneous eigenstates may be extended to more than two observables and the above theorem and its converse still hold, i.e. if any set of observables commute, each with all the others, their simultaneous eigenstates form a complete set, and conversely. The same arguments used for the proof with two observables are adequate for the general case; e.g., if we have three commuting observables $\xi$, $\eta$, $\zeta$, we can expand any simultaneous eigenket of $\xi$ and $\eta$ in terms of eigenkets of $\zeta$ and then show that each of these eigenkets of $\zeta$ is also an eigenket of $\xi$ and of $\eta$. Thus the simultaneous eigenket of $\xi$ and $\eta$ is expanded in terms of simultaneous eigenkets of $\xi$, $\eta$, and $\zeta$, and since any ket can be expanded in terms of simultaneous eigenkets of $\xi$ and $\eta$, it can also be expanded in terms of simultaneous eigenkets of $\xi$, $\eta$, and $\zeta$.

The orthogonality theorem applied to simultaneous eigenkets tells us that two simultaneous eigenvectors of a set of commuting observables are orthogonal if the sets of eigenvalues to which they belong differ in any way.

Owing to the simultaneous eigenstates of two or more commuting observables forming a complete set, we can set up a theory of functions of two or more commuting observables on the same lines as the theory of functions of a single observable given in § 11. If $\xi$, $\eta$, $\zeta$, $\ldots$ are commuting observables, we define a general function $f$ of them to be that linear operator $f(\xi,\eta,\zeta,\ldots)$ which satisfies
\begin{equation}
f(\xi,\eta,\zeta,\ldots)\ket{\xi'\eta'\zeta'\ldots} = f(\xi',\eta',\zeta',\ldots)\ket{\xi'\eta'\zeta'\ldots},
\end{equation}
where $\ket{\xi'\eta'\zeta'\ldots}$ is any simultaneous eigenket of $\xi$, $\eta$, $\zeta$, $\ldots$ belonging to the eigenvalues $\xi'$, $\eta'$, $\zeta'$, $\ldots$. Here $f$ is any function such that $f(a,b,c,\ldots)$ is deﬁned for all values of $a,b,c,\ldots$ which are eigenvalues of $\xi, \eta, \zeta, \ldots$ respectively. As with a function of a single observable defined by (34), we can show that $f(\xi,\eta,\zeta,\ldots)$ is completely determined by (50), that
$$\overline{f(\xi,\eta,\zeta,\ldots)} = \bar{f}(\xi,\eta,\zeta,\ldots),$$
corresponding to (37), and that if $f(a, b, c,\ldots)$ is a real function, $f(\xi,\eta,\zeta,\ldots)$ is real and is an observable.

We can now proceed to generalize the results (45) and (46). Given a set of commuting observables $\xi,\eta,\zeta,\ldots$ we may form that function of them which is equal to unity when $\xi=a,\eta=b\zeta=c,\ldots, a,b,c,\ldots$ being real numbers, and is equal to zero when any of these conditions is not fulfilled. This function may be written $\delta\_{\xi a}\delta\_{\eta b}\delta\_{\zeta c}$ and is in fact just the product in any order of the factors $\delta\_{\xi a},\delta\_{\eta b},\delta\_{\zeta c}$ defined as functions of single observables, as may be seen by substituting this product for $f(\xi,\eta,\zeta,\ldots)$ in the left-hand side of (50). The average value of this function for any state is the probability, $P\_{abc\ldots}$ say, of $\xi,\eta,\zeta,\ldots$ having the values $a, b, c,\ldots$ respectively for that state. Thus if the state corresponds to the normalized ket vector $\ket{x}$, we get from our general assumption for physical interpretation
\begin{equation}
P\_{abc\ldots} = \bra{x}\delta\_{\xi a}\delta\_{\eta b}\delta\_{\zeta c}\ldots\ket{x}.
\end{equation}

$P\_{abc\ldots}$ is zero unless each of the numbers $a,b,c,\ldots$ is an eigenvalue of the corresponding observable. If any of the numbers $a,b,c,\ldots$ is an eigenvalue in a range of eigenvalues of the corresponding observable, $P\_{abc\ldots}$ will usually again be zero, but in this case we ought to replace the requirement that this observable shall have exactly one value by the requirement that it shall have a value lying within a small range, which involves replacing one of the $\delta$ factors in (51) by a factor like the $\chi(\xi)$ of equation (46). On carrying out such a replacement for each of the observables $\xi,\eta,\zeta,\ldots$ whose corresponding numerical value $a, b, c,\ldots$ lies in a range of eigenvalues, we shall get a probability which does not in general vanish.

If certain observables commute, there exist states for which they all have particular values, in the sense explained at the bottom of p. 46, namely the simultaneous eigenstates. Thus *one can give a meaning to several commuting observables having values at the same time*. Further, we see from (51) that for any state *one can give a meaning to the probability of particular results being obtained for simultaneous measurements of several commuting observables*. This conclusion is an important new development. In general one cannot make an observation on a system in a deﬁnite state without disturbing that state and spoiling it for the purposes of a second observation. One cannot then give any meaning to the two observations being made simultaneously. The above conclusion tells us, though, that in the special case when the two observables commute, the observations are to be considered as non-interfering or *compatible*, in such a xvay that one can give a meaning to the two observations being made simultaneously and can discuss the probability of any particular results being obtained. The two observations may, in fact, be considered as a single observation of a more complicated type, the result of which is expressible by two numbers instead of a single number. *Front the point of view of general theory, any two or more commuting observables may be counted as a single observable, the result of a measurement of which consists of two or more numbers*. The states for which this measurement is certain to lead to one particular result arefthe simultaneous eigenstates.

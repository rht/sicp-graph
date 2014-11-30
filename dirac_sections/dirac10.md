#10. Observables

We have made a number of assumptions about the way in which states and dynamical variables are to be represented mathematically in the theory. These assumptions are not, by themselves, laws of nature, but become laws of nature when we make some further assumptions that provide a physical interpretation of the theory. Such further assumptions must take the form of establishing connexions between the results of observations, on one hand, and the equations of the mathematical formalism on the other.

When we make an observation we measure some dynamical variable. It is obvious physically that the result of such a measurement must always be a real number, so we should expect that any dynamical variable that we can measure must be a real dynamical variable. One might think one could measure a complex dynamical variable by measuring separately its real and pure imaginary parts. But this would involve two measurements or two observations, which would be all right in classical mechanics, but would not do in quantum mechanics, where two observations in general interfere with one another--it is not in general permissible to consider that two observations can be made exactly simultaneously, and if they are made in quick succession the first will usually disturb the state of the system and introduce an indeterminacy that will affect the second. We therefore have to restrict the dynamical variables that we can measure to be real, the condition for this in quantum mechanics being as given in §8. Not every real dynamical variable can be measured, however. A further restriction is needed, as we shall see later.

We now make some assumptions for the physical interpretation of the theory. *If the dynamical system is in an eigenstate of a real dynamical variable $\xi$, belonging to the eigenvalue $\xi'$, then a measurement of $\xi$ will certainly give as result the number $\xi'$*. Conversely, *if the system
is in a state such that a measurement of a real dynamical variable $\xi$ is
certain to give one particular result* (instead of giving one or other of
several possible results according to a probability law, as is in general
the case), *then the state is an eigenstate of $\xi$ and the result of the measurement is the eigenvalue of $\xi$ to which this eigenstate belongs*. These assumptions are reasonable on account of the eigenvalues of real linear operators being always real numbers.

Some of the immediate consequences of the assumptions will be noted. If we have two or more eigenstates of a real dynamical variable $\xi$ belonging to the same eigenvalue $\xi'$, then any state formed by superposition of them will also be an eigenstate of $\xi$ belonging to the eigenvalue $\xi'$. We can infer that if we have two or more states for which a measurement of $\xi$ is certain to give the result $\xi'$, then for any state formed by superposition of them a measurement of $\xi$ will still be certain to give the result $\xi'$. This gives us some insight into the physical significance of superposition of states. Again, two eigenstates of $\xi$ belonging to djﬁerent eigenvalues are orthogonal. We can infer that two states for which a measurement of $\xi$ is certain to give two different results are orthogonal. This gives us some insight into the physical significance of orthogonal states.

When we measure a real dynamical variable $\xi$, the disturbance involved in the act of measurement causes a jump in the state of the dynamical system. ‘From physical continuity, if we make a second measurement of the same dynamical variable $\xi$ immediately after the first, the result of the second measurement must be the same as that of the first. Thus after the first measurement has been made, there is no indeterminacy in the result of the second. Hence, after the first measurement has been made, the system is in an eigenstate of the dynamical variable $\xi$, the eigenvalue it belongs to being equal to the result of the first measurement. This conclusion must still hold if the second measurement is not actually made. In this way we see that a measurement always causes the system to jump into an eigenstate of the dynamical variable that is being measured, the eigenvalue this eigenstate belongs to being equal to the result of the measurement.

We can infer that, with the dynamical system in any state, *any result of a measurement of a real dynamical variable is one of its eigenvalues*. Conversely, *every eigenvalue is a possible result of a measure ment of the dynamical variable for some state of the system*, since it is certainly the result if the state is an eigenstate belonging to this eigenvalue. This gives us the physical significance of eigenvalues. The set of eigenvalues of a real dynamical variable are just the possible results of measurements of that dynamical variable and the calculation of eigenvalues is for this reason an important problem.

Another assumption we make connected with the physical interpretation of the theory is that, *if a certain real dynamical variable $\xi$ is measured with the system in a particular state, the states 'into which the system may jump 0n account of the measurement are such that the original state is dependent on them*. Now these states into which the system may jump are all eigenstates of $\xi$, and hence the original state is dependent on eigenstates of $\xi$. But the original state may be any state, so we can conclude that any state is dependent on eigenstates of $\xi$. If we define a complete set of states to be a set such that any state is dependent on them, then our conclusion can be formulated--the eigenstates of $\xi$ form a complete set.

Not every real dynamical variable has sufﬁcient eigenstates to form a complete set. Those Whose eigenstates do not form complete sets are not quantities that can be measured. We obtain in this way a further condition that a dynamical variable has to satisfy in order that it shall be susceptible t0 measurement, in addition t0 the condition that it shall be real. We call a real dynamical variable whose eigenstates form a complete set an observable. Thus any quantity that can be measured is an observable.

The question now presents itself--Can every observable be measured? The answer theoretically is yes. In practice it may he very awkward, or perhaps even beyond the ingenuity of the experimenter, to devise an apparatus which could measure some particular observable, but the theory always allows one to imagine that the measurement can be made.

Let us examine mathematically the condition for a real dynamical variable $\xi$ to be an observable. Its eigenvalues may consist of a (finite or infinite) discrete set of numbers, or alternatively, they may consist of all numbers in a certain range, such as all numbers lying between $a$ and $b$. In the former case, the condition that any state is dependent on eigenstates of $\xi$ is that any ket can be expressed as a sum of eigenkets of $\xi$. In the latter case the condition needs modiﬁcation, since one may have an integral instead
of a sum, i.e. a ket $\ket{P}$ may be expressible as an integral of eigenkets of $\xi$,
\begin{equation}
\ket{P} = \int \ket{\xi'} \operatorname{d}\xi',
\end{equation}
$\ket{\xi'}$ being an eigenket of $\xi$ belonging to the eigenvalue $\xi'$ and the
range of integration being the range of eigenvalues, as such a ket is
dependent on eigenkets of $\xi$. Not every ket dependent on eigenkets
of $\xi$ can be expressed in the form of the right-hand side of (24), since
one of the eigenkets itself cannot, and more generally any sum of
eigenkets cannot. The condition for the eigenstates of $\xi$ to form a
complete set must thus be formulated, that any ket $\ket{P}$ can be
expressed as an integral plus a sum of eigenkets of $\xi$, i.e.
\begin{equation}
\ket{P} = \int \ket{\xi'c}\operatorname{d}\xi' + \sum_r\ket{\xi^rd},
\end{equation}
where the $\ket{\xi'c}$, $\ket{\xi^rd}$ are all eigenkets of $\xi$, the labels $c$ and $d$ being inserted to distinguish them when the eigenvalues $\xi'$ and $\xi^r$ are equal, and where the integral is taken over the whole range of eigenvalues and the sum is taken over any selection of them. If this condition is satisfied in the case when the eigenvalues of $\xi$ consist of a range of numbers, then $\xi$ is an observable.

There is a more general case that sometimes occurs, namely the eigenvalues of $\xi$ may consist of a range of numbers together with a discrete set of numbers lying outside the range. In this case the condition that $\xi$ shall be an observable is still that any ket shall be expressible in the form of the right-hand side of (25), but the sum over $r$ is now a sum over the discrete set of eigenvalues as well as a selection of those in the range.

It is often very diffﬁcult to decide mathematically whether a particular real dynamical variable satisfies the condition for being an observable or not, because the whole problem of ﬁnding eigenvalues and eigenvectors is in general very difﬁcult. However, we may have good reason on experimental grounds for believingth at the dynamical variable can be measured and then we may reasonably assume that it is an observable even though the mathematical proof is missing. This is a thing we shall frequently do during the course of development of the theory, eg. we shall assume the energy of any dynamical system to be always an observable, even though it is beyond the power of presenti-day mathematical analysis to prove it so except in simple cases.

In the special case when the real dynamical variable is a number, every state is an eigenstate and the dynamical variable is obviously an observable. Any measurement of it always gives the same result, so it is just a physical constant, like the charge on an electron. A physical constant in quantum mechanics may thus be looked upon either as an observable with a single eigenvalue or as a mere number appearing in the equations, the two points of view being equivalent.

If the real dynamical variable satisfies an algebraic equation, then the result ($\beta$) of the preceding section shows that the dynamical variable is an observable. Such an observable has a ﬁnite number of eigenvalues. Conversely, any observable with a ﬁnite number of eigenvalues satisfies an algebraic equation, since if the observable $\xi$ has as its eigenvalues $\xi',\xi'',\ldots,\xi^n$, then
$$\left(\xi-\xi'\right) \left(\xi-\xi''\right) \ldots \left(\xi-\xi^n\right) \ket{P} = 0$$
holds for $\ket{P}$ any eigenkets of $\xi$, and thus it holds for any $ket{P}$ whatever, because any ket can be expressed as a sum of eigenkets of $\xi$ on account of $\xi$ being an observable. Hence
\begin{equation}
\left(\xi-\xi'\right) \left(\xi-\xi''\right) \ldots \left(\xi-\xi^n\right) = 0
\end{equation}

As an example we may consider the linear operator $\ket{A}\bra{A}$, where $\ket{A}$ is a normalized ket. This linear operator is real according to (7), and its square is
\begin{equation}
\\{\ket{A}\bra{A}\\}^2 = \ket{A}\braket{A}{A}\bra{A} = \ket{A}\bra{A}
\end{equation}
since $\braket{A}{A} = 1$. Thus its square equals itself and so it satisfies an algebraic equation and is an observable. Its eigenvalues are 1 and 0, with $\ket{A}$ as the eigenket belonging to the eigenvalue 1 and all kets orthogonal to $\ket{A}$ as eigenkets belonging to the eigenvalue 0. A measurement of the observable thus certainly gives the result 1 if the dynamical system is in the state corresponding to $\ket{A}$ and the result 0 if the system is in any orthogonal state, so the observable may be described as the quantity which determines whether the system is in the state $\ket{A}$ or not.

Before concluding this section we should examine the conditions for an integral such as occurs in (24) to be significant. Suppose $\ket{X}$ and $\ket{Y}$ are two kets which can be expressed as integrals of eigenkets of the observable $\xi$,
$$\ket{X} = \int\ket{\xi'x}\operatorname{d}\xi', \ket{Y} = \int \ket{\xi''y}\operatorname{d}\xi''$$
$x$ and $y$ being used as labels to distinguish the two integrands. Then we have, taking the conjugate imaginary of the first equation and multiplying by the second
\begin{equation}
\braket{X}{Y} = \int\int \braket{\xi'x}{\xi''y}\operatorname{d}\xi'\operatorname{d}\xi''.
\end{equation}

Consider now the single integral
\begin{equation}
\int\braket{\xi'x}{\xi''y}\operatorname{d}\xi''.
\end{equation}

From the orthogonality theorem, the integrand here must vanish over the whole range of integration except the one point $\xi'' = \xi'$. If the integrand is finite at this point, the integral (29) vanishes, and if this holds for all $\xi'$, we get from (28) that $\braket{X}{Y}$ vanishes. Now
in general $\braket{X}{Y}$ does not vanish, so in general $\braket{\xi'x}{\xi'y}$ must be infinitely great in such a way as to make (29) non-vanishing and finite. The form of infinity required for this will be discussed in § 15.

In our work up to the present it has been implied that our bra and ket vectors are of finite length and their scalar products are finite. We see now the need for relaxing this condition when we are dealing with eigenvectors of an observable whose eigenvalues form a range. If we did not relax it, the phenomenon of ranges of eigenvalues could not occur and our theory would be too weak for most practical problems.

Taking $\ket{Y} = \ket{X}$ above, we get the result that in general $\braket{\xi'x}{\xi'x}$ is infinitely great. We shall assume that if $\ket{\xi'x} \ne 0$
\begin{equation}
\int \braket{\xi'x}{\xi''x}\operatorname{d}\xi'' \gt 0,
\end{equation}
as the axiom corresponding to (8) of §6 for vectors of infinite length.

The space of bra or ket vectors when the vectors are restricted to be of finite length and to have finite scalar products is called by mathematicians a *Hilbert space*. The bra and ket vectors that we now use form a more general space than a Hilbert space.

We can now see that the expansion of a ket $ket{P}$ in the form of the right-hand side of (25) is unique, provided there are not two or more terms in the sum referring to the same eigenvalue. To prove this result, let us suppose that two different expansions of $ket{P}$ are possible. Then by subtracting one from the other, we get an equation of the form
\begin{equation}
0 = \int\ket{\xi'a}\operatorname{d}\xi' + \sum_s \ket{\xi^sb},
\end{equation}
$a$ and $b$ being used as new labels for the eigenvectors, and the sum over $s$ including all terms left after the subtraction of one sum from the other. If there is a term in the sum in (31) referring to an eigenvalue $\xi'$ not in the range, we get, by multiplying (31) on the left by $\bra{\xi'b}$ and using the orthogonality theorem,
$$0 = \braket{\xi'b}{\xi'b},$$

which contradicts (8) of § 6. Again, if the integrand in (31) does not
vanish for some eigenvalue $\xi''$ not equal to any $\xi^s$ occurring in the
sum, we get, by multiplying (31) on the left by $\bra{\xi''a}$ and using the
orthogonality theorem,
$$0 = \int \braket{\xi''a}{\xi'a}\operatorname{d}\xi',$$
which contradicts (30). Finally, if there is a term in the sum in (31)
referring to an eigenvalue $\xi'$ in the range, we get, multiplying (31) on
the left by $\bra{\xi'b}$,
\begin{equation}
0 = \int \braket{\xi'b}{\xi'a}\operatorname{d}\xi' + \braket{\xi'b}{\xi'b}
\end{equation}
and multiplying (31) on the left by $\bra{\xi'a}$
\begin{equation}
0 = \int \braket{\xi'a}{\xi'a}\operatorname{d}\xi' + \braket{\xi'a}{\xi'b}.
\end{equation}

Now the integral in (33) is finite, so $\braket{\xi'a}{\xi'b}$ is finite and $\braket{\xi'b}{\xi'a}$ is ﬁnite. The integral in (32) must then be zero, so $\braket{\xi'b}{\xi'b}$ is zero and we again have a contradiction. Thus every term in (31) must vanish and the expansion of a ket $\ket{P}$ in the form of the right-hand side of (25) must be unique.

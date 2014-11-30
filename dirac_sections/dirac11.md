#11. Functions of observables

Let $\xi$ be an observable. We can multiply it by any real number $k$ and get another observable $k\xi$. In order that our theory may be self-consistent it is necessary that, when the system is in a state such that a measurement of the observable $\xi$ certainly gives the result $\xi$, a measurement of the observable k5 shall certainly give the result $k\xi'$. It is easily verified that this condition is fulfilled. The ket corresponding to a state for which a measurement of E certainly gives the result $\xi'$ is an eigenket of $\xi$, $\ket{\xi'}$ say, satisfying
$$\xi\ket{\xi'} = \xi'\ket{\xi'}$$
This equation leads to
$$k\xi\ket{\xi'} = k\xi'\ket{\xi'}$$
showing that $\ket{\xi'}$ is an eigenket of $k\xi$ belonging to the eigenvalue $k\xi'$, and thus that a measurement of $k\xi$ will certainly give the result $k\xi'$.

More generally, we may take any real function of $\xi$, $f\left(\xi\right)$ say, and consider it as a new observable wzvhich is automatically measured
whenever $\xi$ is measured, since an experimental determination of the value of $\xi$ also provides the value of $f\left(\xi\right)$. We need not restrict $f\left(\xi\right)$ to be real, and then its real and pure imaginary parts are two observables which are automatically measured when $\xi$ is measured. For the theory to be consistent it is necessary that, when the system is in a state such that a measurement of $\xi$ certainly gives the result $\xi'$, a measurement of the real and pure imaginary parts of $f\left(\xi\right)$ shall certainly give for results the real and pure imaginary parts of $f\left(\xi'\right)$. In the case when $f\left(\xi\right)$ is expressible as a power series
$$f\left(\xi\right) = c_0 + c_1\xi + c_2\xi^2 + c_3\xi^3 + \ldots,$$
the c's being numbers, this condition can again be verified by elementary algebra. In the case of more general functions $f$ it may not be possible to verify the condition. The condition may then be used to define $f\left(\xi\right)$, which we have not yet defined mathematically. In this way me can get a more general definition of a function of an observable than is provided by power series.

We define $f\left(\xi\right)$ in general to be that linear operator which satisfies
\begin{equation}
f\left(\xi\right)\ket{\xi'} = f\left(\xi'\right)\ket{\xi'}
\end{equation}
for every eigenket $\ket{\xi'}$ of $\xi$, $f\left(\xi'\right)$ being a number for each eigenvalue $\xi'$. It is easily seen that this deﬁnition is self-consistent when applied to eigenkets $\ket{\xi'}$ that are not independent. If we have an eigenket $\ket{\xi'A}$ dependent on other eigenkets of $\xi$, these other eigenkets must all belong to the same eigenvalue $\xi'$, otherwise we should have an equation of the type (31), which we have seen is impossible. On multiplying the equation which expresses $\ket{\xi'A}$ linearly in terms of the other eigenkets of $\xi$ by $f\left(\xi\right)$ on the left, me merely multiply each term in it by the number $f\left(\xi'\right)$, so we obviously get a consistent equation. Further, equation (34) is sufficient to define the linear operator $f\left(\xi'\right)$ completely, since to get the result of $f\left(\xi\right)$ multiplied into an arbitrary ket $ket{P}$, we have only to expand $\ket{P}$ in the form of the right-hand side of (25) and take
\begin{equation}
f(\xi)\ket{P} = \int f(\xi')\ket{\xi'c}\operatorname{d}\xi' + \sum_r f(\xi^4)\ket{\xi^rd}.
\end{equation}
The conjugate complex $\overline{f(\xi)}$ of $f(\xi)$ is defined by the conjugate imaginary equation to (34), namely
$$\bra{\xi'}\overline{f(\xi)} = \bar{f}(\xi')\bra{\xi'},$$
holding for any eigenbra $\bra{\xi'}$, $\bar{f}(\xi')$ being the conjugate complex function to $f(\xi')$. Let us replace $\xi'$ here by $\xi''$ and multiply the equation on the right by the arbitrary ket $\ket{P}$. Then we get, using
the expansion (25) for $\ket{P}$,
\begin{equation}
\begin{aligned}
\bra{\xi''}\overline{f(\xi)}\ket{P} & = \bar{f}(\xi'')\braket{\xi''}{P} \\\\
                                    & = \int \bar{f}(\xi'')\braket{\xi''}{\xi'c}\operatorname{d}\xi' + \sum_r \bar{f}(\xi'')\braket{\xi''}{\xi^r d} \\\\
                                    & = \int \bar{f}(\xi'')\braket{\xi''}{\xi'c}\operatorname{d}\xi' + \bar{f}(\xi'')\braket{\xi''}{\xi'' d} \\\\
\end{aligned}
\end{equation}
with the help of the orthogonality theorem, $\braket{\xi''}{\xi''d}$ being understood to be zero if $\xi''$ is not one of the eigenvalues to which the terms
in the sum in (25) refer. Again, putting the conjugate complex function $\bar{f}(\xi')$ for $f(\xi')$ in (35) and multiplying on the left by $\bra{\xi''}$, we get
$$\bra{\xi''}\bar{f}(\xi)\ket{P} = \int \bar{f}(\xi')\braket{\xi'}{\xi'c}\operatorname{d}\xi' + \bar{f}(\xi'')\braket{\xi''}{\xi''d}.$$
The right-hand side here equals that of (36), since the integrands
vanish for $\xi' \ne \xi''$, and hence
$$\bra{\xi''}\overline{f(\xi)}\ket{P} = \bra{\xi''}\bar{f}(\xi)\ket{P}.$$
This holds for $\bra{\xi''}$ any eigenbra and $\ket{P}$ any ket, so
\begin{equation}
\overline{f(\xi)} = \bar{f}(\xi).
\end{equation}

Thus the conjugate complex of the linear operator $f(\xi)$ is the conjugate complex function $\bar{f}$ of $\xi$.

It follows as a corollary that if $f(\xi')$ is a real function of $\xi'$, $f(\xi)$ is a real linear operator. $f(\xi)$ is then also an observable, since its eigenstates form a complete set, every eigenstate of $\xi$ being also an eigenstate of $f(\xi)$.

With the above definition we are able to give a meaning to any function $f$ of an observable, provided only that the domain of existence of the function of a real variable $f(x)$ includes all the eigenvalues of the observable. If the domain of existence contains other points besides these eigenvalues, then the values of $f(x)$ for these other points will not affect the function of the observable. The function need not be analytic or continuous. The eigenvalues of a function f of an observable are just the function f of the eigenvalues of the observable.

It is important to observe that the possibility of defining a function $f$ of an observable requires the existence of a unique number $f(x)$ for each value of X which is an eigenvalue of the observable. Thus the function $f(x)$ must be single-valued. This may be illustrated by considering the question: When we have an observable $f(A)$ which is a real function of the observable $A$, is the observable $A$ a function of the observable $f(A)$)? The answer to this is yes, if different eigenvalues $A'$ of $A$ always lead to different values of $f(A')$. If, however, there exist two different eigenvalues of $A$, $A'$ and $A'$' say, such that $f(A') = f(A'')$, then, corresponding to the eigenvalue $f(A')$ of the observable $f(A)$, there will not be a unique eigenvalue of the observable A and the latter will not be a function of the observable $f(A)$.

It may easily be verified mathematically, from the definition, that the sum or product of two functions of an observable is a function of that observable and that a function of a function of an observable is a function of that observable. Also it is easily seen that the whole theory of functions of an observable is symmetrical between bras and kets and that we could equally well work from the equation
\begin{equation}
\bra{\xi'}f(\xi) = f(\xi')\bra{\xi'}
\end{equation}
instead of from (34).

We shall conclude this section with a discussion of two examples which are of great practical importance, namely the reciprocal and the square root. The reciprocal of an observable exists if the observable does not have the eigenvalue zero. If the observable $\alpha$ does not have the eigenvalue zero, the reciprocal observable, which we call $\alpha^{-1}$ or $1/\alpha$, will satisfy
\begin{equation}
\alpha^{-1}\ket{\alpha'} = \alpha'^{-1}\ket{\alpha'}
\end{equation}

where $\ket{\alpha'}$ is an eigenket of $\alpha$ belonging to the eigenvalue $\alpha'$. Hence
$$\alpha\alpha^{-1}\ket{\alpha'} = \alpha\alpha'^{-1}\ket{\alpha'} = \ket{\alpha'}$$
Since this holds for any eigenket $\ket{\alpha'}$, we must have
\begin{equation}
\alpha\alpha^{-1} = 1
\end{equation}
Similarly,
\begin{equation}
\alpha^{-1}\alpha = 1
\end{equation}

Either of these equations is sufficient to determine $\alpha^{-1}$ completely, provided $\alpha$ does not have the eigenvalue zero. To prove this in the case of (40), let $x$ be any linear operator satisfying the equation
$$\alpha x = 1$$
and multiply both sides on the left by the $\alpha^{-1}$ defined by (39). The result is
$$\alpha^{-1}\alpha x = \alpha^{-1}$$
and hence from (41)
$$ x = \alpha^{-1}$$

Equations (40) and (41) can be used to define the reciprocal, when it exists, of a general linear operator $\alpha$, which need not even be real. One of these equations by itself is then not necessarily sufficient. If any two linear operators $\alpha$ and $\beta$ have reciprocals, their product $\alpha\beta$ has the reciprocal
\begin{equation}
\left(\alpha\beta\right)^{-1} = \beta^{-1}\alpha^{-1}
\end{equation}
obtained by taking the reciprocal of each factor and reversing their order. We verify (42) by noting that its right-hand side gives unity when multiplied by a5, either on the right or on the left. This reciprocal law for products can be immediately extended to more than two factors, i.e.,
$$\left(\alpha\beta\gamma\ldots\right)^{-1} = \ldots\gamma^{-1}\beta^{-1}\alpha^{-1}.$$

The square root of an observable on always exists, and is real if $\alpha$ has no negative eigenvnlues. We write it $\sqrt{\alpha}$ or $\alpha^{\frac12}$. It satisfies
\begin{equation}
\sqrt{\alpha}\ket{\alpha'} = \pm \sqrt{\alpha'}\ket{\alpha'},
\end{equation}

$\ket{\alpha'}$ being an eigenket of $\alpha$ belonging to the eigenvalue $\alpha$. Hence
$$\sqrt{\alpha}\sqrt{\alpha}\ket{\alpha'} = \sqrt{\alpha'}\sqrt{\alpha'}\ket{\alpha'} = \alpha'\ket{\alpha'} = \alpha\ket{\alpha'},$$
and since this holds for any eigenket $\ket{\alpha'}$ we must have
\begin{equation}
\sqrt{\alpha}\sqrt{\alpha} = \alpha
\end{equation}

On account of the ambiguity of sign in (43) there will be several square roots. To fix one of them me must specify a particular sign in (43) for each eigenvalue. This sign may vary irregularly from one eigenvalue to the next and equation (43) will always define a linear operator $\sqrt{\alpha}$ satisfying (44) and forming a square-root function of $\alpha$. If there is an eigenvalue of o: with two or more independent eigenkets belonging to it, then we must, according to our definition of a function, have the same sign in (43) for each of these eigenkets. If we took different signs,however, equation (44)would still hold, and hence equation (44) by itself is not sufficient to define $\sqrt{\alpha}$, except in the special case when there is only one independent eigenket of $\alpha$. belonging to any eigenvalue.

The number of different square roots of an observable is $2^n$, where $n$ is the total number of eigenvalues not zero. In practice the square-root function is used only for observables without negative eigenvalues and the particular square root that is useful is the one for which the positive sign is always taken in (43). This one will be called the *positive square root*.

#8. Conjugate relations

Our linear operators are complex quantities, since one can multiply
them by complex numbers and get other quantities of the same nature.
Hence they must correspond in general to complex dynamical variables, i.e. to complex functions of the coordinates, velocities, etc. We
need some further development of the theory to see What kind of
Linear operator corresponds to a real dynamical variable.

Consider the Bet which is the conjugate imaginary of $\bra{P}\alpha$. This
ket depends antilinearly on $\bra{P}$ and thus depends linearly on $\ket{P}$.
It may therefore be considered as the result of some linear operator
operating on $\ket{P}$. This linear operator is called the *adjoint* of $\alpha$ and we shall denote it by $\bar{\alpha}$. With this notation, the conjugate imaginary of $\bra{P}\alpha$ is $\bar{\alpha}\ket{P}$.

In formula (7) of Chapter I put $\bra{P}\alpha$ for $\bra{A}$ and its conjugate imaginary $\bar{\alpha}\ket{P}$ for $\ket{A}$. The result is
\begin{equation}
\bra{B}\bar{\alpha}\ket{P} = \overline{\bra{P}\alpha\ket{B}}.
\end{equation}

This is a general formula holding for any ket vectors $\ket{B}$, $\ket{P}$ and
any linear operator $\alpha$, and it expresses one of the most frequently
used properties of the adjoint.

Putting $\bar{\alpha}$ for $\alpha$ in (4), we get

$$\bra{B}\bar{\bar{\alpha}}\ket{P} = \overline{\bra{P}\bar{\alpha}\ket{B}} = \bra{B}\alpha\ket{P},$$

by using (4) again With $\ket{P}$ and $\ket{B}$ interchanged. This holds for
any ket $\ket{P}$, so We can infer from (4) of Chapter I,
$$\bra{B}\bar{\bar{\alpha}} = \bra{B}\alpha,$$
and since this holds for any bra vector $\bra{B}$, we can infer
$$\bar{\bar{\alpha}} = \alpha$$

Thus *the adjoint of the adjoint of a linear operator is the original linear operator*. This property of the adjoint makes it like the conjugate complex of a number, and it is easily verified that in the special case When the linear operator is a number, the adjoint linear operator is the conjugate complex number. Thus it is reasonable to assume that *the adjoint of a linear operator corresponds to the conjugate complex of a dynamical variable*. With this physical significance for the adjoint of a linear operator, We may call the adjoint alternatively the conjugate complex linear operator, Which conforms With onr notation $\bar{\alpha}$.

A linear operator may equal its adjoint, and is then called *self-adjoint*. It corresponds to a real dynamical variable, so it may be called alternatively a *real linear operator*. Any linear operator may be split up into a real part and a pure imaginary part. For this reason the Words 'conjugate complex' are applicable to linear operators and not the words 'conjugate imaginary'.

The conjugate complex of the sum of two linear operators is obviously the sum of their conjugate complexes. To get the conjugate complex of the product of two linear operators $\alpha$ and $\beta$, We apply formula (7) of Chapter I With
$$\bra{A} = \bra{P}\alpha, \bra{B} = \bra{Q}\bar{\beta}$$
$$\mathrm{so that} \ket{A} = \bar{\alpha}\ket{P}, \ket{B} = \beta\ket{Q}.$$
The result is
$$\bra{Q}\bar{\beta}\bar{\alpha}\ket{P} = \overline{\bra{P}\alpha\beta\ket{Q}} = \bra{Q}\overline{\alpha\beta}\ket{P}$$
from (4). Since this holds for any $\ket{P}$ and $\bra{Q}$, we can infer that
\begin{equation}
\bar{\beta}\bar{\alpha} = \overline{\alpha\beta}
\end{equation}
Thus *the conjugate complex of the product of two linear operators equals the product of the conjugate complexes of the factors in the reverse order*.
As simple examples of this result, it should be noted that, if $\xi$ and
$\eta$ are real, in general $\xi\eta$ is not real. This is an important difference from classical mechanics. However, $\xi\eta + \eta\xi$ is real, and so is $i\left(\xi\eta-\eta\xi\right)$. Only when $\xi$ and $\eta$ commute is $\xi\eta$ itself also real. Further, if $\xi$ is real, then so is $\xi^2$ and, more generally, $\xi^n$ with $n$ any positive integer.
We may get the conjugate complex of the product of three linear operators by successive applications of the rule (5) for the conjugate complex of the product of two of them. We have
\begin{equation}
\alpha\beta\gamma = \alpha\left(\beta\gamma\right) = \beta\gamma\bar{\alpha} =\bar{\gamma}\bar{\beta}\bar{\alpha},
\end{equation}
so the conjugate complex of the product of three linear operators equals the product of the conjugate complexes of the factors in the reverse order. The rule may easily be extended to the product of any number of linear operators.

In the preceding section we saw that the product $\ket{A}\bra{B}$ is a linear operator. We may get its conjugate complex by referring directly to the definition of the adjoint. Multiplying $\ket{A}\bra{B}$ into a general bra $\bra{P}$ we get $\braket{P}{A}\bra{B}$, whose conjugate imaginary ket is
$$\overline{\braket{A}{A}}\ket{B} = \braket{A}{P}\ket{B} = \ket{B}\braket{A}{P} $$
Hence
\begin{equation}\overline{\ket{A}\bra{A}} = \ket{B}\bra{A}.\end{equation}

We now have several rules concerning conjugate complexes and conjugate imaginaries of products, namely equation (7 ) of Chapter I, equations (4), (5), (6), (7) of this chapter, and the rule that the conjugate imaginary of $\bra{P}\alpha$ is $\bar{\alpha}\ket{P}$. These rules can all be summed up in a single comprehensive rule, *the conjugate complex or conjugate imaginary of any product of hra vectors, ket vectors, and linear operators is obtained by taking the conjugate complex or conjugate imaginary of each factor and reversing the order of all the factors*. The rule is easily verified to hold quite generally, also for the cases not explicitly given, above.

THEOREM. *If $\xi$ is a real linear operator and*
\begin{equation}\xi^m\ket{P}\end{equation}
*for a particular ket $\ket{P}$, m heing a positive integer, then*
$$\xi\ket{P} = 0$$

To prove the theorem, take first the case when m = 2. Equation
(8) then gives
$$\bra{P}\xi^2\ket{P} = 0$$
showing that the ket $\xi\ket{P}$ multiplied by the conjugate imaginary bra $\bra{P}\xi$ is zero. From the assumption (8) of Chapter I with $\xi\ket{P}$ for $\ket{A}$,

we see that $\xi\ket{P}$ must be zero. Thus the theorem is proved for $m = 2$.
Now take $m > 2$ and put
$$\xi^{m-2}\ket{P} = \ket{Q}$$
Equation (8) now gives
$$\xi^2\ket{Q} = 0$$
Applying the theorem for m = 2, we get
$$\xi\ket{Q} = 0$$
\begin{equation}
\mathrm{or} \xi^{m-1}\ket{P} = 0.
\end{equation}

By repeating the process by which equation (9) is obtained from
(8), we obtain successively
$$\xi^{m-2}\ket{P} = 0, \xi^{m-3}\ket{P} = 0, \ldots, \xi^2\ket{P} = 0, \xi\ket{P} = 0,$$

and so the theorem is proved generally.

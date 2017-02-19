#9. Eigenvalues and eigenvectors

We must make a further development of the theory of linear operators, consisting in studying the equation
\begin{equation}
\alpha\ket{P} = a\ket{P},
\end{equation}
where $\alpha$ is a linear operator and $a$ is a number. This equation usually presents itself in the form that $\alpha$ is a known linear operator and the number $a$ and the ket $\ket{P}$ are unknowns, which we have to try to choose so as to satisfy (10), ignoring the trivial solution $\ket{P} = 0$.

Equation (10) means that the linear operator a applied to the ket $\ket{P}$ just multiplies this ket by a numerical factor without changing its direction, or else multiplies it by the factor zero, so that it ceases to have a direction. This same $\alpha$ applied to other kets will, of course, in general change both their lengths and their directions. It should be noticed that only the direction of $\ket{P}$ is of importance in equation (10). If one multiplies $\ket{P}$ by any number not zero, it will not affect the question of whether ( 10) is satisfied or not.

Together with equation (10), we should consider also the conjugate imaginary form of equation
\begin{equation}
\bra{Q}\alpha = b\bra{Q},
\end{equation}
where $b$ is a number. Here the unknowns are the number $b$ and the non-zero bra $\bra{Q}$. Equations (10) and (11) are of such fundamental importance in the theory that it is desirable to have some special words to describe the relationships between the quantities involved.
If (10) is satisfied, We shall call $a$ an *eigenvalue* $\dagger$ of the linear operator $\alpha$, or of the corresponding dynamical variable, and We shall call $\ket{P}$ an *eigenket* of the linear operator or dynamical variable. Further, we shall say that the eigenket $\ket{P}$ belongs to the eigenvalue $a$. Similarly, if (11) is satisfied, We shall call $b$ an eigenvalue of $\alpha$ and $\bra{Q}$ an eigenbra belonging to this eigenvalue. The words eigenvalue, eigenket, eigenbra have a meaning, of course, *only with reference to a linear operator or dynamical variable.*

Using this terminology, We can assert that, if an eigenket of $\alpha$ is multiplied by any number not zero, the resulting ket is also an eigenket and belongs to the same eigenvalue as the original one. It is possible to have two or more independent eigenkets of a linear operator belonging to the same eigenvalue of that linear operator, e.g. equation (10) may have several solutions, $\ket{P_1}, \ket{P_2}, \ket{P_3}, \ldots$ say, all holding for the same value of a, with the various eigenkets $\ket{P_1}, \ket{P_2}, \ket{P_3}, \ldots$ independent. In this case it is evident that any linear combination of the eigenltets is another eigenket belonging to the same eigenvalue of the linear operator, e.g.
$$c_1\ket{P_1} + c_2\ket{P_2} + c_3\ket{P_3} + \ldots$$
is another solution of (10), where $c_1, c_2, c_3, \ldots$ are any numbers.

In the special case when the Linear operator a of equations (10) and
(11) is a number, $k$ say, it is obvious that any ket $\ket{P}$ and bra $\bra{Q}$ will satisfy these equations provided $a$ and $b$ equal $k$. Thus a number considered as a linear operator has just one eigenvalue, and any ket is an eigenliet and any bra is an eigenbra, belonging to this eigenvalue.

The theory of eigenvalues and eigenvectors of a linear operator $\alpha$ which is not real is not of much use for quantum mechanics. We shall therefore confine ourselves to real linear operators for the further development of the theory. Putting for $\alpha$ the real linear operator $\xi$,
We have instead of equations (10) and (11)
\begin{equation}
\xi\ket{P} = a \ket{P},
\end{equation}
\begin{equation}
\bra{Q}\xi = b\bra{Q}.
\end{equation}
$\dagger$ The word 'proper' is sometimes used instead of 'eigein', but this is not satisfactory as the words 'proper' and 'improper' are often used with other meanings. For example, in §§ 15 and 46 the words 'improper function' and 'proper-energy' are used.

Three important results can now be readily deduced.
*(i) The eigenvalues are all real numbers*. To prove that a satisfying
(12) is real, we multiply (12) by the bra $\bra{Q}$ on the left, obtaining
$\bra{P}\xi\ket{P} = a\braket{P}{P}$
Now from equation (4) with $\bra{B}$ replaced by $\bra{P}$ and $\alpha$ replaced by the real linear operator $\xi$, we see that the number $\bra{P}\xi\ket{P}$ must be real, and from (8) of § 6, $\braket{P}{P}$ must be real and not zero. Hence $a$ is real. Similarly, by multiplying (13) by $\ket{Q}$ on the right, we can prove that $b$ is real.

Suppose we have a solution of (12) and we form the conjugate
imaginary equation, which will read
$$\bra{P}\xi = a\bra{P}$$
in view of the reality of $\xi$ and $a$. This conjugate imaginary equation
now provides a solution of (13), with $\bra{Q} = \bra{P}$ and $b = a$. Thus we can infer

(ii) *The eigenvalues associated with eigenkets are the same as the eigenvalues associated with eigenbras*.

(iii) *The conjugate imaginary of any eigenket is a n eigenbra belonging to the same eigenvalue, and conversely*. This last result makes it reasonable to call the state correspondingto any eigenket or to the conjugate imaginary eigenbra an eigenstate of the real dynamical variable $\xi$.

Eigenvalues and eigenvectors of various real dynamical variables are used very extensively in quantum mechanics, so it is desirable to have some systematic notation for labelling them. The following is suitable for most purposes. If $\xi$ is a real dynamical variable, we call its eigenvalues $\xi'.\xi'',\xi^r$, etc. Thus we have a letter by itself denoting a *real dynamical variable* or a *real linear operator*, and the same letter with primes or an index attached denoting a *number*, namely an eigenvalue of what the letter by itself denotes. An eigenvector may now be labelled by the'eigenvalue to which it belongs.
Thus $\ket{\xi'}$ denotes an eigenket belonging to the eigenvalue $\xi'$ of the dynamical variable $\xi$. If in a piece of work we deal with more than one eigenket belonging to the same eigenvalue of a dynamical variable, we may distinguish them one from another by means of a further label, or possibly of more than one further labels. Thus, if we are dealing with two eigenkets belonging to the same eigenvalue of $\xi'$, we may call them $\ket{\xi_1'}$ and $\ket{\xi_2'}$.

THEOREM. *Two eigenvectors of a real dynamical variable belonging to different eigenvalues are orthogonal.*

To prove the theorem, let $\ket{\xi'}$ and $\ket{\xi''}$ be two eigenkets of the real dynamical variable $\xi$, belonging to the eigenvalues $\xi'$ and $\xi''$ respectively. THen we ahve the equations

\begin{equation}
\xi\ket{\xi'} = \xi'\ket{\xi'}
\end{equation}

\begin{equation}
\xi\ket{\xi''} = \xi''\ket{\xi''}
\end{equation}
Taking the conjugate imaginary of (14), we get
$$\bra{\xi'}\xi = \xi'\bra{\xi'}.$$
Multiplying this by $\ket{\xi''}$ on the right gives
$$\bra{\xi'}\xi\ket{\xi''} = \xi'\braket{\xi'}{\xi''}$$
and multiplying (15) by $\bra{\xi'}$ on the left gives
$$\bra{\xi'}\xi\ket{\xi''} = \xi''\braket{\xi'}{\xi''}.$$
\begin{equation}
\mathrm{Hence, subtracting,} \left(\xi'-\xi''\right)\braket{\xi'}{\xi''} = 0,
\end{equation}
showing that, if $\xi'\ne\xi'', \braket{\xi'}{\xi''} = 0$ and the two eigenvectors $\ket{\xi'}$ and $\ket{\xi''}$ are orthogonal. This theorem will be referred to as the *orthogonality theorem*.

We have been discussing properties of the eigenvalues and eigenvectors of a real linear operator, but have not yet considered the question of whether, for a given real linear operator, any eigenvalues and eigenvectors exist, and if so, how to find them. This question is in general very difficult to answer. There is one useful special case, however, which is quite tractable, namely when the real linear operator, $\xi$ say, satisfies an algebraic equation
\begin{equation}
\phi\left(\xi\right) \equiv \xi^n + a_1\xi^{n-1} + a_2\xi^{n-2} + \ldots + a_n =0,
\end{equation}
the coefficients $a$ being numbers. This equation means, of course, that the linear operator $\phi\left(\xi\right)$ produces the result zero when applied to any ket vector or to any bra vector.

Let (17) be the simplest algebraic equation that $\xi$ satisfies. Then it will be shown that

($\alpha$) The number of eigenvalues of $\xi$ is n.

($\beta$) There are so many eigenkets of$\xi$ that any ket whatever can be expressed as a sum of such eigenkets.

The algebraic form $\phi\left(\xi\right)$ can be factorized into $n$ linear factors, the result being
\begin{equation}
\phi\left(\xi\right) \equiv \left(\xi - c_1\right) \left(\xi - c_2\right) \left(\xi - c_3\right) \ldots \left(\xi - c_n\right)
\end{equation}
say, the c's being numbers, not assumed to be all different. This factorization can be performed with $\xi$ a linear operator just as well as with $\xi$ an ordinary algebraic varaible, since there is nothing occurring in (18) that does not commute with $\xi$. Let the quotient when $\phi\left(\xi\right)$ is divided by $\left(\xi-c_r\right)$ be $\chi_r\left(\xi\right)$, so that
$$\phi\left(\xi\right) \equiv \left(\xi-c_r\right)\chi_r\left(\xi\right) \left(r = 1,2,3,\ldots,n\right).$$
Then, for any ket $\ket{P}$,
\begin{equation}
\left(\xi-c_r\right)\chi_r\left(\xi\right)\ket{P} = \phi\left(\xi\right)\ket{P} = 0
\end{equation}

Now $\chi_r\left(\xi\right)\ket{P}$ cannot vanish for every ket $\ket{P}$, as otherwise $\chi_r\left(\xi\right)$ itself would vanish and we should have $\xi$ satisfying an algebraic equation of degree $n-1$, which would contradict the assumption that (17) is the simplest equation that $\xi$ satisfies. If we choose $\ket{P}$ so that $\chi_r\left(\xi\right)\ket{P}$ does not vanish, then equation (19) shows that $\chi_r\left(\xi\right)\ket{P}$ is an eigenket of $|xi$, belonging to the eigenvalue $c_r$. The arguments holds for each value of $r$ from 1 to n, and hence each of the c's is an eigenvalue of $\xi$. No other number can be an eigenvalue of $\xi$, since if $\xi'$ is any eigenvalue, belonging to an eigenket $\ket{\xi'}$,
$$\xi\ket{\xi'} = \xi'\ket{\xi'}$$
and we can deduce $\phi\left(\xi\right)\ket{\xi'} = \phi\left(\xi'\right)\ket{\xi'},$

and since the left-hand side vanishes we must have $\phi\left(\xi'\right) = 0$.

To complete the proof of ($\alpha$) we must verify that the c's are all different. Suppose the c's are not all different and $c_s$ occurs m times say with $m>1$. Then $\phi\left(\xi\right)$ is of the form
$$\phi\left(\xi\right) \equiv \left(\xi - c_s\right)^m\theta\left(\xi\right),$$
with $\theta\left(\xi\right)$ a rational integral function of $\xi$. Equation (17) now gives us
\begin{equation}
\left(\xi - c_s\right)^m\theta\left(\xi\right)\ket{a} = 0
\end{equation}
for any ket $\ket{A}$. Since $c_s$ is an eigenvalue of $\xi$ it must be real, so that $\xi-c_s$ is a real linear operator. Equation (20) is now of the same form as equation (8) with $\xi-c_s$ for $\xi$ and $\theta\left(\xi\right)\ket{A}$ for $\ket{P}$. From the theorem connected with equation (8) we can infer that
$$\left(\xi-c_s\right)\theta\left(\xi\right)\ket{A} = 0.$$
Since the ket $\ket{A}$ is arbitrary,
$$\left(\xi - c_s\right)^m\theta\left(\xi\right) = 0,$$
which contradicts the assumption that (17) is the simplest equaiton that $\xi$ satisfies. Henc ethe c's are all different and ($\alpha$) is proved.

Let $\chi_r\left(c_r\right)$ be the number obtained when $c_r$ is substituted for $\xi$ in the algebraic expression $\chi_r\left(\xi\right)$. Since the c's are all diﬁereilt, $\chi_r\left(c_r\right)$ cannot vanish. Consider now the expression
\begin{equation}
\sum_r \frac{\chi_r\left(\xi\right)}{\chi_r\left(c_r\right)} - 1
\end{equation}

If $c_s$, is substituted for $\xi$ here, every term in the sum vanishes except
the one for which $r = s$, since $\chi_r\left(\xi\right)$ contains $\left(\xi-c_s\right)$ as a factor when $r \ne s$, and the term for which $r = s$ is unity, so the whole expression vanishes. Thus the expression (21) vanishes when $\xi$ is put equal to any of the $n$ numbers $c_1,c_2,\ldots,c_n$. Since, however, the expression is only of degree $n-1$ in $\xi$, it must vanish identically. If we now apply the linear operator (21) to an arbitrary ket $\ket{P}$ and equate the result to zero, me get
\begin{equation}
\ket{P} = \sum_r \frac{1}{\chi_r\left(c_r\right)}\chi_r\left(\xi\right)\ket{P}.
\end{equation}
Each term in the sum on the right here is, according to (19), an eigenket of $\xi$, if it does not vanish. Equation (22) thus expresses the arbitrary ket $\ket{P}$ as a sum of eigenkets of $\xi$, and thus ($\beta$) is proved.

As a simple example we may consider a real linear operator $\sigma$ that
satisfies the equation
\begin{equation}
\sigma^2 = 1.
\end{equation}

Then $\sigma$ has the two eigenvalues 1 and -1. Any ket $\ket{P}$ can be
expressed as
$$\ket{P} = \frac12\left(1 + \sigma\right)\ket{P} + \frac12\left(1-\sigma\right)\ket{P}.$$

It is easily verified that the two terms on the right here are eigenkets of $\sigma$, belonging to the eigenvalues 1 and -1 respectively, when they do not vanish.

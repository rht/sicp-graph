#14. Basic vectors

IN the preceding chapters We set up an algebraic scheme involving certain abstract quantities of three kinds, namely bra vectors, ket vectors, and linear operators, and we expressed some of the fundamental laws of quantum mechanics in terms of them. It would be possible to continue to devslop the theory in terms of these abstract quantities and to use them for applications to particular problems. However, for some purposes it is more convenient to replace the abstract quantities by sets of numbers with analogous mathematical properties and to work in terms of these sets of numbers. The procedure is similar to using coordinates in geometry, and has the advantage of giving one greater mathematical power for the solving of particular problems.

The way in which the abstract quantities are to be replaced by numbers is not unique, there being many possible ways corresponding to the many systems of coordinates one can have in geometry. Each of these ways is called a representation and the set of numbers that replace an abstract quantity is called the representative of that abstract quantity in the representation. Thus the representative of an abstract quantity corresponds to the coordinates of a geometrical object. When one has a particular problem to work out in quantum mechanics, one can minimize the labour by using a representation in which the representatives of the more important abstract quantities occurring in that problem are as simple as possible.

To set up a representation in a general way, we take a complete set of bra vectors, i.e. a set such that any bra can be expressed linearly in terms of them (as a sum or an integral or possibly an integral plus a sum). These bras we call the basic bras of the representation. They are sufﬁcient, as We shall see, to ﬁx the representation completely.

Take any ket $\ket{a}$ and form its scalar product with each of the basic
bras. The numbers so obtained constitute the representative of $\ket{a}$. They are sufficientto determine the ket $\ket{a}$ completely, since if there
is a second ket, $\ket{a\_1}$ say, for which these numbers are the same, the difference $\ket{a}-\ket{a\_1}$ will have its scalar product with any basic bra vanishing, and hence its scalar product with any bra whatever will
vanish and. $\ket{a}-\ket{a\_1}$ itself will vanish.

We may suppose the basic bras to be labelled by one or more parameters, $\lambda\_1,\lambda\_2,\ldots,\lambda\_u$ each of which may take on certain numerical values. The basic bras will then be written $\bra{\lambda\_1,\lambda\_2,\ldots,\lambda\_u}$ and the representative of $\ket{a}$ will be written $\braket{\lambda\_1,\lambda\_2,\ldots,\lambda\_u}{a}$. This representative will now consist of a set of numbers, one for each set, of values that $\lambda\_1,\lambda\_2,\ldots,\lambda\_u$ may have in their respectve domains. Such a set of numbers just forms a *function* of the variables $\lambda\_1,\lambda\_2,\ldots,\lambda\_u$. Thus the representative of a ket may be looked upon either as a set of numbers or as a function of the variables used to label the basic bras.

If the number of independent states of our dynamical system is finite, equal to $n$. say, it is sufficient to take $n$ basic bras, which may be labelled by a single parameter $\lambda$ taking on the values $1, 2, 3,..., n$.
The representative of any ket $\ket{a}$ now consists of the set of $n$ numbers $\braket{1}{a}, \braket{2}{a}, \braket{3}{a}, \ldots, \braket{n}{a}$, which are precisely the coordinates of the vector $\ket{a}$ referred to a system of coordinates in the usual way. The idea of the representative of a ket vector is just a generalization of the idea of the coordinates of an ordinary vector and reduces to the latter when the number of dimensions of the space of the ket vectors is finite.

In a general representation there is no need for the basic bras to be all independent. In most representations used in practice, however, they are all independent, and also satisfy the more stringent condition that any two of them are orthogonal. The representation is then called an orthogonal representation.

Take an orthogonal representation with basic bras $\bra{\lambda\_1,\lambda\_2\ldots\lambda\_u}$, labelled by parameters $\lambda\_1,\lambda\_2,\ldots,\lambda\_u$ whose domains are all real. Take a ket $\ket{a}$ and form its representative $\braket{\lambda\_1\lambda\_2\ldots\lambda\_u}{a}$. Now form the numbers $\lambda\_1\braket{\lambda\_1\lambda\_2\ldots\lambda\_u}{a}$ and consider them as the representative of a new ket $\ket{b}$. This is permissible since the numbers forming the representative of a ket are independent, on account of the basic bras being independent. The ket $\ket{b}$ is defined by the equation
$$\braket{\lambda\_1\lambda\_2\ldots\lambda\_2}{b} = \lambda\_1\braket{\lambda\_1\lambda\_2\ldots\lambda\_u}{a}$$
The ket $\ket{b}$ is evidently a linear function of the ket $\ket{a}$, so it may be considered as the result of a linear operator applied to $\ket{a}$. Calling this linear operator $L_1$, we have
$$\ket{b} = L_1 \ket{a}$$
and hence $\bra{\lambda\_1\lambda\_2\ldots\lambda\_u}L_1\ket{a} = \lambda\_1\braket{\lambda\_1\lambda\_2\ldots\lambda\_u}{a}$.
This equation holds for any ket $\ket{a}$, so we get
\begin{equation}
\bra{\lambda\_1\lambda\_2\ldots\lambda\_u}L_1 = \lambda\_1\bra{\lambda\_1\lambda\_2\ldots\lambda\_u}.
\end{equation}

Equation (1) may be looked upon as the deﬁnition of the linear operator $L\_1$. It shows that each basic bra is an eigenbra of $L_1$, *the
value of the parameter $\lambda\_1$, being the eigenvalue belonging to it*.

From the condition that the basic bras are orthogonal we can deduce that $L_1$ is real and is en observable. Let $\lambda\_1',\lambda\_2',\ldots,\lambda\_u'$ and $\lambda\_1',\lambda\_2'',\ldots,\lambda\_u''$ be two sets of values for the parameters $\lambda\_1,\lambda\_2,\ldots,\lambda\_u$. We have, putting $\lambda'$'s for the $\lambda$'s in (1) and multiplying on the right by $\ket{\lambda\_1''\lambda\_2''\ldots\lambda\_u''}$, the conjugate imaginary of the basic bra $\bra{\lambda\_1''\lambda\_2''\ldots\lambda\_u''}$,
$$\bra{\lambda\_1'\lambda\_2'\ldots\lambda\_u'}L_1\ket{\lambda\_1''\lambda\_2''\ldots\lambda\_u''} = \lambda\_1'\braket{\lambda\_1'\lambda\_2'\ldots\lambda\_u'}{\lambda\_1''\lambda\_2''\ldots\lambda\_u''}.$$
Interchanging  $\lambda'$'s and $\lambda''$'s,
$$\bra{\lambda\_1''\lambda\_2''\ldots\lambda\_u''}L_1\ket{\lambda\_1'\lambda\_2'\ldots\lambda\_u'} = \lambda\_1'\braket{\lambda\_1'\lambda\_2'\ldots\lambda\_u'}{\lambda\_1''\lambda\_2''\ldots\lambda\_u''}.$$

On account of the basic bras being orthogonal, the right-hand sides here vanish unless $\lambda\_r'' = \lambda\_r'$ for all $r$ from 1 to $u$, in which case the right-hand sides are equal, and they are also real, $\lambda\_1'$ being real. Thus, whether the $\lambda''$'s are equal to the $\lambda'$'s or not,

\begin{aligned}
\bra{\lambda\_1'\lambda\_2'\ldots\lambda\_u'}L_1\ket{\lambda\_1''\lambda\_2''\ldots\lambda\_u''} & = \overline{\bra{\lambda\_1''\lambda\_2''\ldots\lambda\_u''}L_1\ket{\lambda\_1'\lambda\_2'\ldots\lambda\_u'}} \\\\
& = \bra{\lambda\_1'\lambda\_2'\ldots\lambda\_u'}\bar{L}\_1\ket{\lambda\_1''\lambda\_2''\ldots\lambda\_u''}
\end{aligned}
from equation (4) of § 8. Since the $\bra{\lambda\_1'\lambda\_2'\ldots\lambda\_u'}$'s form a complete set of bras and the $\lambda_1''\lambda_2''\ldots\lambda_u''$'s form a complete set of kets, we can infer that $L_1 = \bar{L}\_1$. The further condition required for $L_1$ to be an observable, namely that its eigenstates shall form a complete set, is obviously satisﬁed since it has as eigenbras the basic bras, which form a complete set.

We can similarly introduce linear operators $L_2, L_3,\ldots,L_u$ by multiplying $\braket{\lambda_1\lambda_2\ldots\lambda_u}{a}$ by the factors $\lambda_2,\lambda_3,\ldots,\lambda_u$ in turn and considering the resulting sets of numbers as representatives of kets. Each of these $L$'s can be shown in the same way to have the basic bras as eigenbras and to be real and an observable. The basic bras are simultaneous eigenbras of all the L's. Since these simultaneous eigenbras form a complete set, it follows from a theorem of § 13 that any two of the $L$'s commute.

It will now be shown that, if $\xi_1,\xi_2,\ldots,\xi_u$ are *any set of commuting observables, vve can set up an orthogonal representation i n which the basic bras are simultaneous eigenbras of $\xi_1,\xi_2,\ldots,\xi_u$*. Let us suppose first that there is only one independent simultaneous eigenbra of $\xi_1,\xi_u,\ldots,\xi_u$ belonging to any set of eigenvalues $\xi_1',\xi_u',\ldots,\xi_u'$. Then we may take these simultaneous eigenbras, with arbitrary numerical coefﬁcients,as our basic bras. They are all orthogonal on account of the orthogonality theorem (any two of them will have at least one eigenvalue different, which is sufficient to make them orthogonal) and there are sufficient of them to form a complete set, from a result of § 13. They may conveniently be labelled by the eigenvalues $\xi_1',\xi_2',\ldots,\xi_u'$ to which they belong, so that one of them is written $\bra{\xi_1'\xi_2'\ldots\xi_u'}$.

Passing now to the general case when there are several independent simultaneous eigenbras of $\xi_1',\xi_2',\ldots,\xi_u'$ belonging to some sets of eigenvalues, we must pick out from all the simultaneous eigenbras belonging to a set of eigenvalues $\xi_1',\xi_2',\ldots,\xi_u'$ a complete subset, the members of which are all orthogonal to one another. (The condition of completeness here means that any simultaneous eigenbra belonging to the eigenvalues $\xi_1',\xi_2',\ldots,\xi_u'$ can be expressed linearly in terms of the members of the subset.) We must do this for each set of eigenvalues $\xi_1',\xi_2',\ldots,\xi_u'$ and then put all the members of all the subsets together and take them as the basic bras of the representation. These bras are all orthogonal, two of them being orthogonal from the orthogonality theorem if they belong to different sets of eigenvalues and from the special way in which they were chosen if they belong to the same set of eigenvalues, and they form altogether a complete set of bras, as any bra can be expressed linearly in terms of simultaneous eigenbras and each simultaneous eigenbra can then be expressed linearly in terms of the n1embers of a subset. There are infinitely many ways of choosing the subsets, and each way provides one orthogonal representation.

For labelling the basic bras in this general case, we may use the eigenvalues $\xi_1',\xi_2',\ldots,\xi_u'$ to which they belong, together with certain
additional real variables $\lambda_1,\lambda_2,\ldots,\lambda_v$ say, which must be introduced to distinguish basic vectors belonging to the same set of eigenvalues from one another. A basic bra is then written $\bra{\xi_1'\xi_2'\ldots\xi_u'\lambda_1\lambda_2\ldots\lambda_v}$. Corresponding to the variables $\lambda_1,\lambda_2,\ldots,\lambda_v$ we can deﬁne linear operators $L_1, L_2, \ldots, L_v$ by equations like (1) and can show that these
linear operators have the basic bras as eigenbras, and that they are
real and observables, and that they commute with one another and
with the $\xi$'s. The basic bras are now simultaneous eigenbras of all
the commuting observables $\xi_1,\xi_2,\ldots,\xi_u, L_1, L_2, \ldots, L_v$.

Let us define a *complete set of commuting observables* to be a set of observables Which all commute With one another and for which there is only one simultaneous eigenstate belonging to any set of eigenvalues. Then the observables $\xi_1,\xi_2,\ldots,\xi_u, L_1, L_2, \ldots, L_v$ form a complete set of commuting observables, there being only one independent simultaneous eigenbra belonging to the eigenvalues $\xi_1',\xi_2',\ldots,\xi_u',\lambda_1,\lambda_2,\ldots,\lambda_v$ namely the corresponding basic bra. Similarly the observables $L_1,L_2,\ldots,L_u$, defined by equation (1) and the following Work form a complete set of commuting observables. With the help of this definition the main results of the present section can be concisely formulated thus:

(i) The basic bras of an orthogonal representation are simul-
taneous eigenbras of a complete set of commuting observ-
able.

(ii) Given a complete set of commuting observables, We can set
up an orthogonal representation in Which the basic bras are
simultaneous eigenbras of this complete set.

(iii) Any set of commuting observables can be made into a com-
plete commuting set by adding certain observables to it.

(iv) A convenient Way of labelling the basic bras of an orthogonal
representation is by means of the eigenvalues of the complete
set of commuting observables of Which the basic bras are
simultaneous eigenbras.

The conjugate imaginaries of the basic bras of a representation We
call the *basic kets* of the representation. Thus, if the basic bras are
denoted by $\bra{\lambda_1\lambda_2\ldots\lambda_u}$, the basic kets will be denoted by $\ket{\lambda_1\lambda_2\ldots\lambda_u}$.
The representative of a bra $\bra{b}$ is given by its scalar product With
each of the basic kets, i.e. by $\braket{b}{\lambda_1\lambda_2\ldots\lambda_u}$. It may, like the representative of a ket, be looked upon either as a set of numbers or as a function of the variables $\lambda_1,\lambda_2,\ldots,\lambda_u$. We have
$$\braket{b}{\lambda_1\lambda_2\ldots\lambda_u} = \overline{\braket{\lambda_1\lambda_2\ldots\lambda_u}{b}},$$
showing that *the representative of a bra is the conjugate complex of the representative of the conjugate imaginary ket*. In an orthogonal representation, Where the basic bras are simultaneous eigenbras of a complete set of commuting observables, $\xi_1,\xi_2,\ldots,\xi_u$ say, the basic kets will be simultaneous eigenkets of $\xi_1,\xi_2,\ldots,\xi_u$.

We have not yet considered the lengths of the basic vectors. With an orthogonal representation, the natural thing to do is to normalize the basic vectors, rather than leave their lengths arbitrary, and so introduce a further stage of simpliﬁcation into the representation. However, it is possible to normalize them only if the parameters which label them all take on discrete values. If any of these parameters are continuous variables that can take on all values in a range, the basic vectors are eigenvectors of some observable belonging to eigenvalues in a range and are of infinite length, from the discussion in §10 (see p. 39 and top of p. 40). Some other procedure is then
needed to ﬁx the numerical factors by which the basic vectors may be multiplied. To get a convenient method of handling this question a new mathematical notation is required, which will be given in the next section.

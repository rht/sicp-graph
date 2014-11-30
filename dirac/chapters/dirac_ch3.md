#III REPRESENTATIONS

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

#15. The $\delta$ function
Our work in § 10 led us to consider quantities involving a certain kind of inﬁnity. To get a precise notation for dealing with these infinities, we introduce a quantity $\delta(x)$ depending on a parameter $x$ satisfying the conditions
\begin{equation}
\begin{aligned}
    \int_{-\infty}^\infty \delta(x)\operatorname{d}x &= 1 \\\\
        \delta(x) &= 0 \, \mathrm{for}\, x \ne 0.
\end{aligned}
\end{equation}
To get a picture of $\delta(x)$, take a function of the real variable $x$ which vanishes everywhere except inside a small domain, of length $\epsilon$ say,
surrounding the origin $x = 0$, and which is so large inside this domain that its integral over this domain is unity. The exact shape of the function inside this domain does not matter, provided there are no unnecessarily wild variations (for example provided the function is always of order $\epsilon^{-1}$). Then in the limit $\epsilon \rightarrow 0$ this function will go
over into $\delta(x)$.

$\delta(x)$ is not a function of $x$ according to the usual mathematical definition of a function, which requires a function to have a deﬁnite value for each point in its domain, but is something more general, which we may call an ‘improper function’ to show up its difference from a function deﬁned by the usual deﬁnition. Thus $\delta(x)$ is not a quantity which can be generally used in mathematical analysis like an ordinary function, but its use must be conﬁned to certain simple types of expression for which it is obvious that no inconsistency can arise.

The most important property of $\delta(x)$ is exempliﬁed by the following equation,
\begin{equation}
\int\_{-\infty}^{\infty} f(x)\delta(x)\operatorname{d}x = f(0),
\end{equation}
Where $f(x)$ is any continuous function of $x$. We can easily see the validity of this equation from the above picture of $\delta(x)$. The left-hand side of (3 ) can depend only on the values of $f(x)$ very close to the origin, so that we may replace $f(x)$ by its value at the origin, $f(0)$, without essential error. Equation (3) then follows from the first of equations (2). By making a change of origin in (3), we can deduce the formula
\begin{equation}
\int\_{-\infty}^{\infty}f(x)\delta(x-a)\operatorname{d}x = f(a),
\end{equation}

where $a$ is any real number. Thus *the process of multiplying a function
of x by $\delta(x-a)$ and integrating over all x is equivalent to the process of substituting a for x*. This general result holds also if the function of $x$ is not a numerical one, but is a vector or linear operator depending on $x$.

The range of integration in (3) and (4) need not be from $-\infty$ to $\infty$, but may be over any domain surrounding the critical point at which the $\delta$ function does not vanish. In future the limits of integration will usually be omitted in such equations, it being understood that the domain of integration is a suitable one.

Equations (3) and (4) show that, although an improper function does not itself have a well-defined value, when it occurs as a factor in an integrand the integral has a well-defined value. In quantum theory, Whenever an improper function appears, it will be something which is to be used ultimately in an integrand. Therefore it should be possible to rewrite the theory in a form in which the improper functions appear all through only in integrands. One could then eliminate the improper functions altogether. The use of improper functions thus does not involve any lack of rigour in the theory, but is merely a convenient notation, enabling us to express in a concise form certain relations which we could, if necessary, rewrite in a form not involving improper functions, but only in a cumbersome way which would tend to obscure the argument.

An alternative way of defining the $\delta$ function is as the diﬁerential
coefficient $\epsilon'(x)$ of the function $\epsilon(x)$ given by
\begin{equation}
\begin{aligned}
    \epsilon(x) &= 0 \, (x \lt 0) \\\\
                &= 1 \, (x \gt 0).
\end{aligned}
\end{equation}


We may verify that this is equivalent to the previous deﬁnition by
substituting e'(x) for 3(:c) in the left-hand side of (3)and integrating
by parts. We ﬁnd, for g1 and g2 two positive numbers,

fhmewx) dz = Manx) e,- mwrc-gx) dw

""02 a "U:
= fa.»- f ma») dx
0

in agreement with (3) . The 8 function appears whenever one differen-
tiates a discontinuous function.

There are a number of elementary equations which one can write
down about 3 functions. These equations are essentially rules of
manipulation for algebraic work involving S functions. The meaning
of any of these equations is that its two sides give equivalent results
as factors in an integrand.

Examples of such equations are

5(—$) = 50B) " (6)

112M113) = O, (7)

3(ax) = a"'18(ac) (a > O), (8)

5(a:2--a2) = 1§a*1{8(a:--a)+3(x—|—a)} (a > 0), (9)

J‘ Nib-CU) da: 8(as-—-b) = act-gas), (10)
f(x)5(=v-@) = f(@)3(w—@)- (11)

Equation (6), which merely states that 3(:c) is an even function of its
variable x is trivial. To verify ( 7) take any continuous function of

x, f(as). Then
.|‘_f(o:)x3(:c) dx = 0,

from (3). Thus m8(:r:) as a factor in an integrand is equivalent to
zero, which is just the meaning of (7). (8)and (9) may be verified
by similar elementary arguments. To verify (1 0)take any continuous
function of a,f (a) . Then

Jifw) da I 5(a—a:) 01a: 3(x--b) = I 5(a:--b) da: ff(a) da Mal-x)
= f 8(:c--b)da:f(as) = f f(a)da8(a,--b).

Thus the two sides of (10) are equivalent as factors in an integrand
with a as variable of integration. It may be shown in the same way

§15 THE s FUNCTION 61

that they are equivalent also as factors in an integrand with b as
variable of integration, so that equation (10) is justified from either
of these points of view. Equation (11) is also easily justified, with
the help of (4), from two points of view.

Equation (10) would be given by an application of (4) with
f(x) = 8(:c—b). We have here an illustration of the fact that we may
often use an improper function as though it were an ordinary con-
tinuous function, without getting a wrong result.

Equation (7) shows that, whenever one divides both sides of an
equation by a variable X which can take on the value zero, one
should add on to one side an arbitrary multiple of 3(5):), i.e. from an

equation A I B (12)
one cannot infer A/x = B/x,
but only A/x = B/x-l-cﬁar), (13)

where c is unknown. _
As an illustration of work with the 6 function, we may consider the
differentiation of log X. The usual formula

é-i-ér-logx = é (14)
requires examination for the neighbourhood of X = 0. In order to
make the reciprocal function l/x well defined in the neighbourhood
of X = 0 (in the sense of an improper function) ‘we must impose on
it an eXtra condition, such as that its integral from —-e to e vanishes.
With this eXtra condition, the integral of the right-hand side of (14)
from —e to e vanishes, while that of the left-hand side of (l4) equals
log ( — l), so that (l4)is not a correct equation. To correct it, we must
remember that, taking principal values, logX has a pure imaginary
term in for negative values of X. As a: passes through the value zero
this pure imaginary term vanishes discontinuously. The differen-
tiation of this pure imaginary term gives us the result --—iw8(a:), so
that (14) should read

gglogx = %—iw8(x). (15)

The particular combination of reciprocal function and 8 function
appearing in (15) plays an important part in the quantum theory of
collision processes (see§ 50).

 

62 REPRESENTATIONS §15

#16. Properties of the basic vectors

Using the notation of the 6 function, we can proceed with the theory
of representations. Let us suppose ﬁrst that we have a single observ-
able 5 forming by itself a complete commuting set, the condition for
this being that there is only one eigenstate of 5 belonging to any
eigenvalue f’, and let us set up an orthogonal representation in which
the basic vectors are eigenvectors of E and are written (SI, 1E’).

In the case when the eigenvalues of i are discrete, we can normalize
the basic vectors, and we then have

<€’|§”> = 0 (€’ #15’),

<€'|€'> = 1-
These equations can be combined into the single equation
<§'|§"> = 5.5%», (15)

where the symbol 6 with two suﬁxes, which we shall often use in the
future, has the meaning

8,8 = O when r 7i s } (17)
= 1 when 1" = s.

In the case when the eigenvalues of 4f are continuous we cannot
normalize the basic vectors. If we now consider the quantity Of’ If’)
with 5' ﬁxed and f’ varying, we see from the work connected with
expression (29) of § 10 that this quantity vanishes for i" # E’ and
that its integral over a range of 5” extending through the value 4f’
is finite, equal to c say. Thus

<s'|s"> = v5(€’—-£”)-
From (30) of § 10, c is a positive number. It may vary with E’, so
we should write it 0(8) or c’ for brevity, and thus we have
<s'|s"> = v mea"). <18)
Alternatively, we have
<s'|§"> = <="8<s'-§">. <19)
where o” is short for c(f”), the right-hand sides of (18) and (19) being
equal on account of (11).
Let us pass to another representation whose basic vectors are
eigenvectors of 5, the new basic vectors being numerical multiples of

the previous oneis. Calling the new basic vectors (f’* ], 15*), with the
additional label to distinguish them from the previous ones, we have

<s'*1 = kwaw. |s'*> = Fm

§15 PROPERTIES OF THE BASIC VECTORS 63
where h’ is short for lc(§') and is a number depending on E’. We get
<§r4<l€m|¢> i krg<érlén> ____ fcfFc-i’ 

with the help of (l8). This may be written
<€'*|§”*> = k’F@'5(€'—§")

from (l l). By choosing k’ so that its modulus is c"'i', which is possible
since c’ is positive, we arrange to have

<€'*l€”*> = 5(§'-€")- (20)
The lengths of the new basic vectors are now fixed so as to make the
representation as simple as possible. The way these lengths were
fixed is in some respects analogous to the normalizing of the basic
vectors in the case of discrete ‘f’, equation (20) being of the form of
(l6) with the 6 function 8(§’--§”) replacing the 6 symbol 5&- of

equation (l6). We shall continue to work with the new representation
and shall drop the f‘ labels in it to save writing. Thus (20) will now

‘w Writ“ <§’1§"> = ace-at» <21)

We can develop the theory on closely parallel lines for the discrete
and continuous cases. For the discrete case we have, using (16),

g l§'><§'IE"> =  |§'>3ga§' = If”),

the sum being taken over all eigenvalues. This equation holds for
any basic ket 1E") and hence, since the basic kets form a complete set,

g |€'><E'| = 1- (22)

This is a useful equation expressing an important property of the
basic vectors, namely, if l5’) is multiplied on the right by (Fl the
resulting linear operator, summed for all 5', equals the unit operator.
Equations (16)a.11d (22)give the fundamental properties of the basic
vectors for the discrete case.
Similarly, for the continuous case we have, using (21),

f |§-">d6’ <».='|s"> == f :§’>de'8<s'-s"> = |s"> <23)

from (4) applied with a ket vector for f(a:), the range of integration
being the range of eigenvalues. This holds for any basic ket |f")

and hence
f 1:» are <6: = 1. <24)

e4 REPRESENTATIONS § 16

This is of the same form as (22) with an integral replacing the sum.
Equations (21) and (24) give the fundamental properties of the basic
vectors for the continuous case.

Equations (22) and (24) enable one to expand any bra or ket in
terms of the basic vectors. For example, we get for the ket |P> in the
discrete case, by multiplying (22) on the right by {P}, a

l?) =  |€'><5'|P>= (25)

which gives IP) expanded in terms of the ]§')’s and shows that the
coefficients in the expansion are (§'|P which are just the numbers
forming the representative of IP). Similarly, in the continuous case,

|P> = f 15> as <§'sP>. <26)

giving |P> as an integral over the I§’>’s, with the coefﬁcient in the
integrand again just the representative <5’ |P) of fP). The conjugate
imaginary equations to (25) and (26) would give the bra vector (P I
expanded in terms of the basic bras.

011:: present mathematical methods enable us in the continuous
case to expand any ket as an integral of eigenkets of E. If we do not
use the 6 function notation, the expansion 011a. general ket will consist
of an integral plus a sum, as in equation (25) of $ 1 0 , but the 6 function
enables us to replace the sum by an integral in which the integrand
consists of terms each containing a 5 function as a factor. For
example, the eigenket IE”) may be replaced by an integral of eigen-
kets, as is shown by the second of equations (23).

If (Q! is any bra and |P> any ket we get, by further applications

for discrete E’ and

<Q|P> z f <Qlé'> d? <s’|P> <28)

for continuous f’. These equations express the scalar product of (Q1
and IP) in terms of their representatives (Q|§’> and (FIP). Equa-
tion (27) is just the usual formula for the scalar product of two
vectors in terms of the coordinates of the vectors, and (28) is the
natural modification of this formula for the case of continuous f’,
with an integral instead of a sum.

The generalization of the foregoing work to the case when E has
both discrete and continuous eigenvalues is quite straightforward.

§16 PROPERTIES OF THE BASIC VECTORS 65

Using ‘f’ and E“ t0 denote discrete eigenvalues and 5’ and f" t0 denote
continuous eigenvalues, We have the set of equations

<s'|a~>=B,,=',-. <s=~|s'>=o. <s*|s"> =B<s'-s"> <29)

as the generalization of (16) or (21). These equations express that
the basic vectors are all orthogonal, that those belonging to discrete
eigenvalues are normalized and those belonging to continuous eigen-
values have their lengths ﬁxed by the same rule as led to (20). From
(29) v)? can derive, as the generalization of (22) or (24),

gl~f'><f’l+ f 16d? <51 = 1. <30)

the range of integration being the range of continuous eigenvalues.
With the help of (30), We get immediately

|P> =  lE"><é’lP>+ f |s'> dz’ <s'|P> <31)
as the generalization of (25) or (26), and
<QIP> = g <cnsr><araP>+ f <QI€’> ds’ <s'|P> 432)

as the generalization of (27) or (28).

Let us noW pass to the general case When We have several commuting
observables E1, $2,“, i.“ forming a complete commuting set and set up
an orthogonal representation in Which the basic vectors are simul-
taneous eigenvectors of all of them, and are Written <§'1...§,f,|, Iﬂufi).
Let us suppose E1,§2,...,§,, (v ~<\_ u) have discrete eigenvalues and
§v+1,...,§u have continuous eigenvalues.

Consider the quantity (£1.45; E;,+1..§.I,]§1..§§, §f,+,_..§;>. From the
orthogonality theorem, it must vanish ‘unless each é; = f; for
s --= v+l,..,u. By extending the Work connected With expression
(29) of §l0 to simultaneous eigenvectors of several commuting
observables and extending also the axiom (30), We ﬁnd that the
(u-vyfold integral of this quantity with respect to each é; over
a, range extending through the value g; is a. ﬁnite positive number.
Calling this number c', the ’ denoting that it is a function of
ﬁr.’ 5;, §§,+1,.., 5.1,, We can express our results by the equation

(514;§L+1--§L|€i--§L€Z+1--€Z> = <1’5(§L+1-€Z+1)--3(EL—§Z), (33)

With one 6 factor on the right-hand side for each value of s from
v+l to u. We noW change the lengths of our basic vectors so as to

66 REPRESEXTATIONS §16

make c' unity, by a procedure similar t0 that which led t0 (20). By
a further use of the orthogonality theorem, we get ﬁnally

<E1---6l.l§§---€i'.> = 5§1§1--5§;§:3(§L+1~EZ+1)~-3(§Z.-EL'Z), (34)

with a two-suffix 8 synfbﬁ on the right-friend side for each 5 with
discrete eigenvalues and a 5 function for each § with continuous
eigenvalues. This is the generalization of (16) or (21) to the case when
there are several commuting observables in the complete set.

From (34) we can derive, as the generalization of (22) or (24)

,2, H I€1---é;>d§;+1--dé;<E1---§;.l = 1. <35)
61-5.

the integral being a (u~—-v)-fo1d one over all the §"s with continuous
eigenvalues and the summation being over all the §”s with discrete
eigenvalues. Equations (34) and (35) give the fundamental properties
of the basic vectors in the present case. From (35) we can imme-
diately write down the generalization of (2 5)or (2 6)and of (27) or (28).

The case we have just considered can be further generalized by
allowing some of the Es to have both discrete and continuous eigen-
values. The modiﬁcations required in the equations are quite straight-
forward, but will not be given here as they are rather cumbersome to
write down in general form.

There are some problems in which it is convenient not to make the
c' of equation (33) equal unity, but to make it equal to some definite
function of the §”s instead. Calling this function of the §”s p’"1 we
then have, instead of (34)

<€1---€Ll€§---§Z1> == P"15§1§:--5§;§;5(€L+r~ Z+1)-~5(€Z.-—§ZZ), (36)
and instead of (35) we get

ll

z, [H] 1§1~~§;>p' ds;.+1~ds; ei-grr 1. , <37)

ér-Ev
p’ is called the weight function of the representation, p’d§;,+1..d§._f,
being the ‘Weight’ attached to a small volume element of the space
of the variables §§,+1,.., 5;.

The representations we considered previously all had the weight
function unity. The introduction of a weight function not unity is
entirely a matter of convenience and does not add anything to the
mathematical power of the representation. The basic bras <.§;...§;,*|
of a representation with the weight function p‘ are connected with

§16 PROPERTIES OF THE BASIC VECTORS 67

the basic bras (Eimﬂl of the corresponding representation with the
weight function unity by

<s;.--.§;.*| = p'—*-<§;~.s;.1. <38)
as is easily verified. An example of a useful representation with
non-unit weight function occurs when one has two 8s which are
the polar and azimuthal angles I9 and g6 giving a direction in three-
dimensionalspace and one takes p‘ = sin 9’. One then has the element
of solid angle sin t9’d6’dg!>' occurring in (37).

#17. The representation of linear operators

In § 14 me saw how to represent ket and bra vectors by sets of
numbers. We now have to do the same for linear operators, in order
to have a complete scheme for representing all our abstract quantities
by sets of numbers. The same basic vectors that we had in§ 14 can
be used again for this purpose.

Let us suppose the basic vectors are simultaneous eigenvectors of
a complete set of commuting observables §1,§2,...,§,,. If or. is any
linear operator, we take a general basic bra (§;...§;,| and a general
basic ket Iffnﬁﬂ) and form the numbers

<€1---€ltl@¢l§i'---€{i>- (39)
These numbers are sufficient to determine a completely, since in the
first place they determine the ket altfiiuﬁﬂ) (as they provide the
representative of this ket), and the value of this ket for all the basic
kets l§1'...§.§;) determines a. The numbers (39) are called the repre-
sentative of the linear operator a or of the dynamical variable a. They
are more complicated than the representative of a ket or bra vector
in that they involve the parameters that label two basic vectors
instead of one.

Let us examine the form of these numbers in simple cases. Take
ﬁrst the case when there is only one f, forming a complete commuting
set by itself, and suppose that it has discrete eigenvalues §'. The
representative of a is then the discrete set of numbers <§'|a]§">. If
one had to write out these numbers explicitly, the natural way of
arranging them would be as a two-dimensional array, thus:

l<€1l¢==I€1> <§1|¢>¢IE2> <€1IQ¢IE3>
$210451) <§2|<1|§2> <E2IO¢I§3> - .
<§3l<>¢l§1> <€3I<>==IEZ> <§3l<>=l€3> . . (49)

6s REPRESENTATIONS §1'?

Where §1,§2,§3,.. are all the eigenvalues of £1. Such an array is called
a matrix and the numbers are called the elements of the matrix. We
make the convention that the elements must always be arranged s0
that those in the same row refer t0 the same basic bra vector and
those in the same column refer to the same basic ket vector.

An element (flail?) referring to two basic vectors With the same
label is called a diagonal element of the matrix, as all such elements
lie on a diagonal. If We put a: equal to unity, We have from (16) all
the diagonal elements equal to unity and all the other elements equal
to zero. The matrix is then called the ttnit matrix.

If a: is real, We have

<€'|@=l€”> = <€"|¢r|§'>- (41)

The effect of these conditions on the matrix (40) is to make the

diagonal elements ‘all real and each of the other elements equal the

conjugate complex of its mirror reﬂectionin the diagonal. The matrix
is then called a Hermitian matrix.

If We put a: equal to E, We get for a general element of the matrix

(FEW) = 5’<€’l€"> == 5755p (42)
Thus all the elements not on the diagonal are zero. The matrix is
then called a diagonal matrix. Its diagonal elements are just equal
to the eigenvalues of 5. More generally, if me put a: equal to f(§), a
function of 5, We get
<§'|f(§)|E”> = f(§') 335-» (43)
and the matrix is again a diagonal matrix.
Let us determine the representative of a product oaﬁ of two linear

operators a: and i5’ in terms of the representatives of the factors.
From equation (22) With 5"” substituted for i’ We obtain

<§'|<1B|€"> = (He; |€'”><E”’|J5|§”>
1g <grioﬁlgm><ézrrlﬁlén>, 

Which gives us the required result. Equation (44) shows that the
matrix formed by the elements (§'|aB|§") equals the product of the
matrices formed by the elements (E104?) and (FIBIF) respectively,
according to the usual mathematical rule for multiplying matrices.
This rule gives for the element in the rth row and sth column of the
product matrix the sum of the product of each element in the rth
row of the first factor matrix urith the corresponding element in the sth

§l7 THE REPRESENTATION OF LINEAR OI'EH.ATORS B9

column 0f the second factor matrix. The multiplication of matrices
is non-commutative, like the multiplication of linear operators.

We can summarize our results for the case when there is only one
5 and it has discrete eigenvalues as follows:

(i) A n y linear operator is represented by a matrix.
(ii) The unit operator is represented by the unit matrix.

(iii) A real linear operator is represented by a Hermitian matrix.

(iv) 1f and functions of E are represented by diagonal matrices.

(v) The matrix representing the product of two linear operators is the
product of the matrices representing the two factors.

Let us now consider the case when there is only one 5 and it has
continuous eigenvalues. The representative of o: is now (51048), a
function of two variables f’ and i" which can vary continuously. It
is convenient to call such a function a ‘matrix’, using this word in
a generalized sense, in order that we may be able to use the same
terminology for the discrete and continuous cases. One of these
generalized matrices cannot, of course, be written out as a two-
dimensional array like an ordinary matrix, since the number of its
rows and columns is an infinity equal to the number of points on a
line, and the number of its elements is an infinity equal to the
number of points in an area.

We arrange our definitions concerning these generalized matrices
so that the rules (i)-(v) which we had above for the discrete case
hold also for the continuous ‘case. The unit operator is represented
by 8(§'—-§") and the generalized matrix formed by these elements
we define to be the unit matrix. We still have equation (41) as the
condition for a to be real and we define the generalized matrix formed
by the elements (§’[a|f"> to be Hermitian when it satisfies this
condition. f is represented by

<e|§ic> = 4' 8<§'~s") <45)
$115176 b)’ <§'|f(€)|§”> = f(E’)3(§’~—€")= (45)
and the generalized matrices formed by these elements we define to be
diagonal matrices. From (11), we could equally well have ﬁ” and f(§")
as the coefﬁcients of 3(E’—§”) on the right-hand sides of (45)and (46)
respectively. Corresponding to equation (44) we now have, from (24)

when?» = f <s'|a|c'> dz" <§’”IBI€">, w)

with an integral instead of a sum, and we define the generalized

matrix formed by the elements on the right-hand side here to be the
—_i3~5_95,57 F

70 REPRESENTATIONS § 17

product of the matrices formed by <§'|a]§"> and (§'|,B[§”>. With
these deﬁnitions we secure complete parallelism between the discrete
and continuous cases and we have the rules (i)-(v) holding for both.

The question arises how a general diagonal matrix is to be deﬁned
in the continuous case, as so far we have only deﬁned the right-hand
sides of (45) and (46) to be examples of diagonal matrices. One
mightftae inclined to deﬁne as diagonal any matrix whose (§',§”)
elements all vanish except when 5' differs inﬁnitely little from i",
but this would not be satisfactory, because an important property
of diagonal matrices in the discrete case is that they always commute
with one another and we want this property to hold also in the
continuous case. In order that the matrix formed by the elements
(§’|w]2§"> in the continuous case may commute with that formed by
the elements on the right-hand side of (45)we must have, using the
multiplication rule (4:7),

J‘ <€r|w|grrr> d5!!! §rr!8(§rrr__§rr) z J‘ 5" 8(§'___€nr) dgm <§rlr|w]§:r>.
With the help of formula (4), this reduces to

<£’|wl€”>E” = §'<s'|w|§"> <48)
or (€’--§”)<§’|w|§"> = 0-
This gives, according to the rule by which (l3) follows from (12),
<§'|wl€”> = ¢'5(§'—§")

where c’ is a number that may depend on .5’. Thus <5’ [w I5”) is of the
form of the right-hand side of (46). For this reason we deﬁne only
matrices whose demerits are 0f the form 0f the right-hand side 0f (46) t0
be diagonal matrices. It is easily veriﬁed that these matrices all
commute with one another. One can form other matrices whose
(f, E”) elements all vanish when f’ differs appreciably from E" and
have a different form of singularity when 5’ equals if” [we shall later
introduce the derivative 81x) of the 6 function and 8’(§’--§") will
then be an example, see § 22 equation (19)], but these other matrices
are not diagonal according to the deﬁnition.

Let us now pass on to the case when there is only one f and it has
both discrete and continuous eigenvalues. Using 5’, £8 to denote

discrete eigenvalues and 5’, f” to denote continuous eigenvalues, we
now have the representative of on consisting of four kinds of quanti-

ties, (8104.58), <§"|@i|§’>, (§’|a|§">, (('la l5”). These quantities can all

§l7 THE REPRESENTATION OF LINEAR OPERATORS 71

be put together and considered to form a more general kind of matrix
having some discrete rows and columns and also a continuous range
of rows and columns. We deﬁne unit matrix, Hermitian matrix,
diagonal matrix, and the product of two matrices also for this more
general kind of matrix so as to make the rules (i)-(v) still hold. The
details are a straightforward generalization of what has gone before
and need not be given explicitly.

Let us now go back to the general case of several §’s,§1,§2,...,.§,,.
The representative of oz, expression (39), may still be looked upon as
forming a matrix, with rows corresponding to different values of
§1,...,E.1,, and columns corresponding to different values of §1',...,§{1.
Unless all the §’s have discrete eigenvalues, this matrix will be of the
generalized kind wvith continuous ranges of rows and columns. We
again arrange our definitions so that the rules (i)-(v) hold, with rule
(iv) generalized to:

(iv') Each 5m (m= 1,2,...,u) and any function of them is repre-
sented by a diagonal matrix.

A diagonal matrix is now defined as one whose general element

<§1...§;,\wlﬂ...§,’f,> is of the form
<€1-~-§§ilwl§i-~-§l1> = c’3&1§I--3§;§;3(€L+1~€Z+1)--5(€li"—E{l) (49)

in the case when $1,“, 5,, have discrete eigenvalues and 5,, 4,1,", 5,, have
continuous eigenvalues, c’ being any function of the 5%. This defini-
tion is the generalization of what we had with one 5 and makes
diagonal matrices always commute with one another. The other
definitions are straightforward and need not be given explicitly.

We now have a linear operator always represented by a matrix.
The sum of two linear operators is represented by the sum of the
matrices representing the operators and this, together with rule (v),
means that the matrices are subject t0 the same algebraic relations as
the linear operators. If any algebraic equation holds between certain
linear operators, the same equation must hold between the matrices
representing those operators.

The scheme of matrices can be extended to bring in the repre-
sentatives of ket and bra vectors. The matrices representing linear
operators areiall square matrices with the same number of rows and
columns, and with, in fact, a one-one correspondence between their
rows and columns. We may look upon the representative of a ket
{P} as a matrix with a single column by setting all the numbers

72 REPRESENTATIONS § 17

<§Q...§.:,|P) which form this representative one below the other. The
number of rows in this matrix tvill be the same as the number of
rows or columns in the square matrices representing linear operators.
Such a single-column matrix can be multiplied on the left by a square
matrix <§;j--~<f-;JCB|§;...§;> representing a linear operator, by a rule
similar tojahat for the multiplication of two square matrices. The
product is another single-column matrix with elements given by

,2, H <s;-.-s;.|@|§;ms;;> ds;..1_»ds;; <£i'---£ILIP>-
grin

From (35) this is just equal to (<§i...§;,]a|P), the.representative of
O¢|P>. Similarly we may look upon the representative of a bra <Q[
as a natrix with a Single row by setting all the numbers <Q|§i...§;>
side by side. Such a single-row matrix may be multiplied on the
right by a square matrix (§;...§;,_|oc |§{...§.ﬂ>, the product being another
single-row matrix, which is just the representative of <Q|0c. The
single-row matrix representing (QI may be multiplied on the right
by the single-column matrix representing |P), the product being a
matrix with just a single element, which is equal to (QIP). Finally,
the single-row matrix representing (Ql may be multiplied on the left
by the single-column matrix representing |P), the product being a
square matrix, which is just the representative of ]P><Q|. In.this
way all our abstract symbols, Linear operators, bra vectors, and ket
vectors, can be represented by matrices, which are subject to the
same algebraic relations as the abstract symbols themselves.

#18. Probability amplitudes

Representations are of great importance in the physical interpreta-
tion of quantum mechanics as they provide a convenient method for
obtaining the probabilities of observables having given values. In
$12 we obtained the probability of an observable having any speci-
f1ed value for a given state and in § l3 we generalized this result
and obtained the probability of a set of commuting observables
simultaneously having speciﬁed values for a given state. Let us now
apply this result to a complete set of commuting observables, say the
set of §’s which we have been dealing with already. According to
formula (51) of § l3, the probability of each 5,. having the value E;
for the state corresponding -to the normalized ket vector {m} is

P-.s;...§;. = <xlsalsa5szsa---5e..s;.lx>— (50)

§13 PROBABILITY AMPLITUDES 73

If the 51s all have discrete eigenvalues, We can use (35) With 12 = u
and no integrals, and get

Peas; 1%, <xi8§1€l 3hr;--5§..s;.|§i-~~5il><§i-iii"?
l...

i8

I g ($1352513:25;.---3g;§;.1§i-~-§;><§i-.-{Z1110

£1’... u
= <$l§§_---§lt><51---§ltlx>
= |<€i-~-€ltl$>l2- (51)

We thus get the simple result that the probability 0f the $39 having the
values g?’ is just the square 0f the modulus 0f the appropriate coordinate
of the normalized ket vector corresponding to the state concerned.

If the §’s do not all have discrete eigenvalues, but if, say, €1:"!§v
have discrete eigenvalues and 5,, +1,” 5,, have continuous eigenvalues,,
then to get something physically signiﬁcant We must obtain the
probability of each 5,. (r = 1 ,.., v) having a speciﬁed value 5,’. and each
f8 (s = o+1,..,U) lying in a speciﬁed small range E; to ﬁ-l-drf} For
this purpose We must replace each factor 8,5,5; in (50) by a factor x3,
Which is that function of the observable f8 Which is equal to unity
for E3 Within the range 5f, to 534g; and zero otherwise. Proceeding
as before with the help of (35), We obtain for this probability

1351...§;dEL+1~-d§;= I<rfi---éltl=v>lgdéi+l--d§it~ (52)

Thus in every case the probability distribution of values for the $8 is
given by the square of the modulate of the representative of the norma-
lized ket vector corresponding to the state concerned.

The numbers Which form the representative of a normalized ket
(or bra) may for this reason be called probability amplitudes. The
square of the modulus of a probability amplitude is an ordinary
probability, or a probability per unit range for those variables that
have continuous ranges of values.

We may be interested in a state Whose corresponding ket Irv) cannot
be normalized. This occurs, for example, if the state is an eigenstadie
of some observable belonging to an eigenvalue lying in a range of
eigenvalues. The forznula (51) or (52) can then still be used to give
the relative probability of the Ks having speciﬁed values or having
values lying in speciﬁed small ranges, i.e. it Will give correctly the
ratios of the probabilities for different §”s. The numbers (éi-uéjdiv)
may then be called relative probability amplitudes.

74 REPRESEXTATIONS § 18

The representation for Which the above results hold is characterized
by the basic vectors being simultaneous eigenvectors of all the §’s.
It may also be characterized by the requirement that each of the Es
shall be represented by a diagonal matrix, this condition being easily
seen to be equivalent to the previous one. The latter characterization
is usually the more convenient one. For brevity, We shall formulate
it as each of the Es ‘being diagonal in the representation’.

Provided the Es form a complete set of commuting observables,
the representation is completely determined by the characterization,
apart from arbitrary phase factors in the basic vectors. Each basic bra
<§1...§.L,f may be Inultiplied by ail’, Where y’ is any real function of
the variables $1,“, 5;, Without changing any of the conditions Which
the representation has to satisfy, i.e. the condition that the §’s are
diagonal or that the basic vectors are simultaneous eigenvectors of
the Ks, and the fundamental properties of the basic vectors (34) and
(35). With the basic bras changed in this Way, the representative
(QUJEQIP) of a ket |P> gets multiplied by e15", the representative
(Q|§1...§;,> of a bra (Q! gets multiplied by e"'*"?" and the representa-
tive <§1...§.‘,'_,|@]§{...§{1> of a linear operator o: gets multiplied by e'*7(>""°’").
The probabilities or relative probabilities (51), (52) are, of course,
unaltered.

The probabilities that one calculates in practical problems in
quantum mechanics are nearly alWays obtained from the squares
of the moduli of probability amplitudes or relative probability ampli-
tudes. Even When one is interested only in the probability of an
incomplete set of commuting observables having speciﬁed values, it
is usually necessary first to make the set a complete one by the
introduction of some extra commuting observables and to obtain
the probability of the complete set having speciﬁed values (as the
square of the modulus of a probability amplitude), and then to sum
or integrate over all possible wralues of the extra observables. A
Inore direct application of formula (51) of § l3 is usually not
practicable.

To introduce a representation in practice

(i) We look for observables Which we Would like to have diagonal,
either because we are interested in their probabilities or for
reasons of mathematical simplicity;

(ii) We must see that they all commute—a necessary condition
since diagonal matrices alWays commute;

§18 PROBABILITY AMPLITUDES 75

(iii) We then see that they form a complete commuting set, atld
if not we add some more commuting observables to them to
make them into a complete commuting set;

(iv) We set up an orthogonal representation with this complete
commuting set diagonal.

The representation is then completely determined except for the
arbitrary phase factors. For most purposes the arbitrary phase
factors are unimportant and trivial, so that we may count the
representation as being completely determined by the observables
that are diagonal in it. This fact is already implied in our notation,
since the only indication in a representative of the representation to
which it belongs are the letters denoting the observables that are
diagonal.

It may be that me are interested in two representations for the
same dynainical system. Suppose that in one of them the complete
set of commuting observables §1,...,§,, are diagonal and the basic
bras are (53.5; and in the other the complete set of commuting
observables 171,...,v7,,, are diagonal and the basic bras are <v;;’,_...17§,,|.
A ket {P> will now have the turo representatives <§;...§.j,lP) and
(q1...17§,,]P>. If $1,", 5,, have discrete eigenvalues and §,,H,..,§,, have
continuous eigenvalues and if 7713;.’ 1b, have discrete eigenvalues and
17x w“, 17w have continuous eigenvalues, we get from (35)

<ﬂi---*YZDIP> =25, H <v1---'0{@l51---€£.-.> déiMr-dﬁt <§1--.§;.|P>. <53)

 

and interchanging §’s and afs
<€1---§Z.~.IP> =12", <§1~--§;lni---12Zv> device-elite <12i---*2MP>- (54)

These are the transformation equations which give one representative
of 1P) in terms of the other. They showv that either representative
is expressible linearly in terms of the other, with the quantities

<121---'0I..-I€i---€;>, <€i~~éitlwi~~vlv> (55)

as coefficients. These quantities are called the transformation func-
tions. Similar equations ‘may be written dowh to connect the two
representatives of a bra vector or of a linear operator. The trans-
formation functions (55) are in every case the means wvhioh enable
one to pass from one representative to the other. Each of the

76 REPRESENTATIONS §18

transformation functions is the conjugate complex of the other, and
they satisfy the conditions

f; H <n1~--w:.|s;_~.s;.> dgaa-r-déiz. <5§.-~-§Z.-.lﬂ'1'--~W’§L>
hi’ 2-‘- 517iqI"81]§,-1);8(7l:17+1_ng7+1)"5(?l;.v*“77:v) 

and the corresponding conditions with §’s and 175s interchanged, as
may be verified from (35) and (34) and the corresponding equations
for the vfs.

Transformation functions are examples of probability amplitudes
or relative probability amplitudes. Let us take the case when all the
<f’s and all the q's have discrete eigenvalues. Then the basic ket
{v;;...17§,,> is normalized, so that its representative in the {lrepresenta-
tion, (§1...§.§,-|~q_i,...-q;,>, is a probability amplitude for each set of values
for the §”s. The state to which these probability amplitudes refer,
namely the state corresponding to |171...17;,,>, iS characterized by the
condition that a simultaneous measurement of q1,..., 17w is certain to
lead to the results q1,...,17.10. Thus |<§i...§§,]1;_§_...17;,>|2 is the proba-
bility of the ﬁ-"s having the values ﬁnf; for the state for which the
q's certainly have the values 171...v;§,,. Since

I<€i---€LI17i-~-WZQ>I2 = |<ﬂi---17Zvl§i--~§L>l2,

we have the theorem of reciprocity —the probability cf the 53s having
the values $'for the state for which the vfs certainly have the values n’
is equal to the probability cf the vfs having the values w)’ for the state for
which the fie certainly have the values 5’. l

If all the vfs have discrete eigenvalues and some of the §’s have
continuous eigenvalues, ]<.;'-'1...§;,[1q’1...17;,>|2 still gives the probability
distribution of values for the 5s for the state for which the vfs cer-
tainly have the values 1;’. If some of the vfs have continuous eigen-
values, Ivqiunqiv) is not normalized and |<§1...§.',,|17;_...v;§,,>|2 then gives
only the relative probability distribution of values for the $3 for the
state for which the vfs certainly have the values n’.

#19. Theorems about functions of observables

We shall illustrate the mathematical value of representations by
using them to prove some theorems.

THEOREM 1. A linear operator that commutes with an observable 5
commutes also with any function cf f.

The theorem is obviously true when the function is expressible as

§l9 THEOREMS ABOUT FUNCTIONS 01*‘ OBSERVABLEG 77

a power series. To prove it generally, let w be the linear operator,
so that we have the equation

gw-wg = 0. (57)

Let us introduce a representation in which E is diagonal. If 5 by
itself does not form a complete commuting set of observables, we must
make itinto a complete commuting set by adding certain observables,
5 say, to it, and then take the representation in which {f and the 18%.
are diagonal. (The case when {I does form a complete commuting set
by itself can be looked upon as a special case of the preceding one
with the number of ﬁ variables zero.) In this representation equation

(57) becomes <g,ﬁ.-lgw_wglgn)8i,> = 0’
which reduces to
él<élﬁf|(uigffﬂfl>__<gfﬁfltulgﬂﬁrf>gﬂ i 
In the case when the eigenvalues of E are discrete, this equation
shows that all the matrix elements <§’B’|w]§",8"> of w vanish except

those for which 5’ = 5". In the case when the eigenvalues o ff are
continuous it shows, like equation (48), that <§',8'lw|§" ”> is of the

m“ <é’ﬁ'lwlé”ﬁ”> = c8<§*-s">.

where c is some function of E’ and the ,8”s and ﬁms. In either case
we may say that the matrix representing w ‘is diagonal with respect
to 5’. If f(§) denotes any function o ff in accordance with the general
theory of $1 1,which requiresf(§"’) to be defined for 5”’ any eigenvalue
of f, we can deduce in either case

f(§’)<<§’23'|<vl§”5">"—<§'l5'lwl§"5">f(§") = 0-
This gives <§’B'If(§)w—wf(§)]§”;8"> = 0,
so that f(§)w—wf(§) = 0

and the theorem is proved.

As a special case of the theorem, we have the result that any
observable that commutes with an observable § also commutes with
any function of 5. This result appears as a physical necessity when
we identify, as in §13, the condition of commutability of two
observables with the condition of compatibility of the correspond-
ing observations. Any observation that is compatible with the
measurement of an observable f must also be compatible with the
measurement of f(§), since any measurement of 5 includes in itself
a measurement of f(§).

7s REPRESEXTATIONS §19

THEOREM 2. A. linear operator that commutes with each of a complete
set cf commuting observables is a function cf those observables.

Let w be the linear operator and §1,§2,...,§,, the complete set of
commuting observables, and set up a representation with these
observables diagonal. Since w commutes with each of the Ks, the
matrix representing it is diagonal with respect to each of the §’s,
by the argument we had above. This matrix is therefore a diagonal
matrix and is of the form (49), involving a number c’ which is a
function of the ”s. It thus represents the function of the §’s that
c' is of the §”s, and hence w equals this function of the §’s.

THEOREM 3. Ifan observable E and a linear operator g are such that
any linear operator that commutes with 5 also commutes with g, then g
is a function cf 5.

This is the converse of Theorem 1. To prove it, we use the same
representation with f diagonal as we had for Theorem 1. In the first
place, we see that g must commute with 5 itself, and hence the
representative of g must be diagonal with respect to 5, i.e. it must
be of the form

<grﬁrlglgrtﬁrw> i “(grﬁrﬁnugérglr Or a(£1B:Brr)8(€r__ga-L
according to whether .5 has discrete or continuous eigenvalues. Now
let w be any linear operator that commutes with 5, so that its
representative is of the form
<gfﬁl’cuigffﬁlf> i b(gfﬁfﬁfl)séié'  b(gfﬁfﬁff)s(ffﬂﬂgif).
By hypothesis w must also commute with g, so that
<§'ﬁ'1gw-wg|§"s"> = 0» <58)
If we suppose for definiteness that the B’s have discrete eigenvalues,
(58)leads, with the help of the law of matrix multiplication, to
B2{a(grﬁrﬁlrr)b(grﬁrrlﬁrr)_b(giﬁlﬁiﬂ)a(grﬁlllﬁrl)} Z 0, 
the left-hand side of (58) being equal to the left-hand side of (59)

multiplied by 55,5» or 8(§’-§”). Equation (59) must hold for all
functions b(§',8’[3”). We can deduce that

w(£’B'B")= 0 for 5' #13”.
v axgrﬁrﬁ!) Z (“£1505”).
The first of these results shows that the matrix representing g is

diagonal and the second shows that a(§’{3’ﬁ”) is a function of 5' only.
We can now infer that g is that function off "which a(§’B',B') is off’,

$19 THEOREMS ABOUT FUNCTIONS OF OBSERVABLES 79

so the theorem is proved. The proof is analogous if some of t h e ' s
have continuous eigenvalues.

Theorems 1 and 3 are still valid if we replace the observable E by
any set of commuting observables §1,§2,..,§,., only formal changes
being needed in the proofs.

#20. Developments in notation

The theory of representations that we have developed provides a
general system for labelling kets and bras. Ina representation in which
the complete set of commuting observables $1,“, 5,, are diagonal any
ket |P) mill have a representative <§1...§;,|P), or <$'|P> for brevity.
This representative is a deﬁnite function of the variables 5’, say M5’).
The function d: then determines the ket IP) completely, so it may be
used to label this ket, to replace the arbitrary label P. In symbols,
if <s'|P> = m’) } cw
W6 put |P> = M5».
We must put IP) equal to |<,!1(§)> and not ]¢(§’)>, since it does not
depend on a particular set of eigenvalues for the Fs, but only on the
form of the function 5b.

With f(§) any function of the observables §,_,...,§u, f(§)|P> will
have as its representative

<E’|f(€)lP> =f(€’)¢(§’)-
Thus according to (60) we put

f(€)iP> = lf(€)¢(€)>-
With the help of the second of equations (60) we now get

f (€)I¢(E)> = If(€)¢(€)>- (51)

This is a general result holding for any functions f and 1b of the §’s,
and it shows that the vertical line l is not necessary with the new
notation for a ket—either side of (61) may be written simply as
_f(§):,b(§)>. Thus the rule for the new notation becomes:—

if <e1P> = m’) } (6,)
W6 Put IP> = $05))
We may further shorten 511(5)) to $>, leaving the variables 5 under-
stood, if no ambiguity arises thereby.

The ket #5)) may be considered as the product of the linear

operator 3M5) with a lazet which is denoted simply by ) without a
label. We call the ket ) the standard ket. Any ket whatever can be

80 REPRESENTATIONS § 20

expressed as a function 0f the §’s multiplied into the standard ket.
For example, taking (P)in (62) t0 be the basic ket I5”), we ﬁnd

I56 = 8£1g;."8§l?£;8(€1?+1~m§$+1)"8(§1£h_§3)> (63)
in the case when $1,", 5,, have discrete eigenvalues and §.,,+1,.., 5,, have
continuous eigenvalues. The standard ket is characterized by the
condition that its representative (£1) is unity over the whole domain
of the variable g’, as may be seen by putting gb =~ l in (62).

A further contraction may be made in the notation, namely to
leave the symbol ) for the standard ket understood. A ket is then
written simply as 1/45), a function of the observables i. A function
of the §’s used in this way to denote a ket is called a wave functionj"
The system of notation provided by wave functions is the one usually
used by most authors for calculations in quantum mechanics. In
using it one should remember that each wave function is understood
to have the standard ket multiplied into it on the right, which
prevents one from multiplying the wave function by any operator
on the right. Wave functions can be multiplied by operators only on
the left. This distinguishes them from ordinary functions of the §’s,
which are operators and can be multiplied by operators on either the
left or the right. A wave function is just the representative of a ket
expressed as a function of the observables f, instead of eigenvalues 5'
for those observables. The square of its modulus gives the proba-
bility (or the relative probability, if it is not normalized) of the ES
having specified values, or lying in specified small ranges, for the
corresponding state.

The new notation for bras may be developed in the same way as
for kets. A bra (Q! whose representative (Ql?) is q5(§’) we write
<<ﬁ(§)[. With this notation the conjugate imaginary to Ic/dﬁ) is
{#5)}. Thus the rule that we have used hitherto, that a ket and
its conjugate imaginary bra are both specified by the same label,
must be extended to read-if the labels of a het involve complex

numbers or complex functions, the labels of the conjugate inmgimry
bra involve the conjugate complex numbers or functions. As in the

case of kets we can show that <q5(-§)ff(§) and <q5(§)f(-f)| are the same,
so that the vertical line can be omitted. We can consider (#5) as
the product of the linear operator q5(§) into the standard bra (, which

1' The reason for this name is that in the early days 0f quantum mechanics all the

examples 0f these functions were 0f the form 0f waves. The name is not a descriptive
one from the point of View of the modern general theory.

§2O DEVELOPMENTS IN NOTATION 81

is the conjugate imaginary of the standard lret  We may leave
the standard bra understood, so that a general bra is written as ME),
the conjugate complex of a wave function. The conjugate complex
of a wave function can be multiplied by any linear operator on the
right, but cannot be multiplied by a linear operator on the left. We
can construct triple products of the form <f(§)>. Such a triple product
is a number, equal to _f(§) summed or integrated over the whole
domain of eigenvalues for the §’s,

<f<s>> - 2, f~~ff<s')de;+1_.ds;. <64)
£11.. v

in the case when $1,", 5,, have discrete eigenvalues and 501.1,“, f.“ have
continuous eigenvalues.

The standard ket and bra are defined with respect to a representa-
tion. If me carried through the above work with a different repre-
sentation in which the complete set of commuting observables 1] are
diagonal, or if we merely changed the phase factors in the representa-
tion with the §’s diagonal, we should get a different standard ket and
bra. In a piece of work in which more than one standard ket or bra
appears one must, of course, distinguish them by giving them labels.

A further development of the notation which is of great importance
for dealing with complicated dynamical systems will now be discussed.
Suppose we have a dynamical system describable in terms of dynami-
cal variables which can all be divided into two sets, set A and set B
say, such that any member of set A commutes with any member of
set B. A general dynamical variable must be expressible as a function
of the A-variables and B-variables together. We may consider
another dynamical system in which the dynamical variables are the
A-variables only —let us call it the A-system. Similarly we may
consider a third dynamical system in which the dynamical variables
are the B-variables only—the B-system. The original system can
then be looked upon as a combination of the A-system and the
B-system in accordance with the mathematical scheme given below.

Let us take any ket (a) for the A-system and any ket |b> for the
B-system. We assume that they have a product |a)[b) for which
the commutative and distributive axioms of multiplication hold, 1,9,

la>lb> = |b>la>,
ic1lai>+czla2>llb> = 471la1>lb>+62iaz>lb>,
|a>{(31lb1>+c2|b2>} = clia>ibl>+c2ia>ib2>v

s2 REPRESENTATIONS §20

the c's being numbers. We can give a meaning to any A-variable
operating on the product la>|b> by assuming that it operates only
on the |a> factor and commutes with the |b> factor, and similarly
we can give a meaning to any B-variable operating on this product
by assuming that it operates only on the |b> factor and commutes
with the $\ket{a}$ factor. (This makes every A-variable commute with
every B-variable.) Thus any dynamical variable of the original
system can operate on the product $\ket{a}$|b>, so this product can be
looked upon as a ket for the original system, and may then be
written lab), the two labels a and b being sufficient to specify it.
In this way we get the fundamental equations

la>lb> = lb>la> = lab) (65)

The multiplication here is of quite a different kind from any that
occurs earlier in the theory. The ket vectors $\ket{a}$ and $\ket{b}$ are in two
different vector spaces and their product is in a third vector space,
which may be called the product of the two previous vector spaces.
The number of dimensions of the product space is equal to the
product of the number of dimensions of each of the factor spaces.
A general ket vector of the product space is not of the form (65), but
is a sum or integral of kets of this form.

Let us take a representation for the A-system in which a complete
set of commuting observables Q4 of the A-system are diagonal. We
shall then have the basic-bras (ﬁll for the A-system. Similarly,taking
a representation for the B-system with the observables 5B diagonal,
we shall have the basic bras (5 "31 for the B-system. The products

E <é;l<§;;-i = eras: <66)
will then provide the basic bras for a representation for the original
system, in which representation the {ifs and the §B’s will be diagonal.

The {ifs and §B’s will together form a complete set of commuting
observables for the original system. From (65) and (66) we get

<EQI<I><FBII>> = (5.2. éélabk (67)
showing that the representative of lab) equals the product of the
representatives of $\ket{a}$ and of $\ket{b}$ in their respective representations.

We can introduce the standard ket, >A say, for the A-system,
with respect to the representation with the fie, diagonal, and also
the standard ket >3 for the B-system, with respect to the repre-
sentation with the §B’s diagonal. Their product )A )5 is then the

§20 DEVELOPMENTS IN NOTATION 83

standard ket for the original system, wvith respect t0 the representa-
tion with the gs and §B’s diagonal. Any ket for the original system

may be expressed as (Mid awn >13“ (68)

It may be that in a certain calculation we wish to use a particular
representation for the B-system, say the above representation with
the §B’s diagonal, but do not wish to introduce any particular
representation for the A-system. It mould then be convenient to
use the standard ket >3 for the R-system and no standard ket for
the A-system. Under these circumstances we could write any ket

for the original system as I§B>>B) (69)

in which |§B> is a ket for the A-system and is also a function of the
g-"B’s, i.e. it is a ket for the A-system for each set of values for the

tO's —in fact (69) equals (68)if we take
|§B> = ‘Mir 53b4-

We 1ney leave the standard ket >3 in (69) understood, and then we
have the general ket for the original system appearing as EB), a ket
for the A-system and a Wave function in the variables 5B of the
B-system. An example of this notation will be used in $66.

The above Work can be immediately extended to a dynamical
system describable in terms of dynamical variables which can be
divided into three or more sets A, B, (l... such that any member of
one set commutes with any member of another. Equation (6.5) gets

generalized to lanwlc)" = Jam")!

the factors on the left being kets for the component systems and
the ket on the right being a Bet for the original system. Equations
(66), (67), and (68) get generalized to many factors in a similar may.

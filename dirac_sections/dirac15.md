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

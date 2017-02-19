<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-11.html)</span><span>,
[next](book-Z-H-13.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[1.5  The Euler-Lagrange Equations](book-Z-H-4.html#%_toc_%_sec_1.5)
--------------------------------------------------------------------

The principle of stationary action characterizes the realizable paths of
systems in configuration space as those for which the action has a
stationary value. In elementary calculus, we learn that the critical
points of a function are the points where the derivative vanishes. In an
analogous way, the paths along which the action is stationary are
solutions of a system of differential equations. This system, called the
*Euler-Lagrange equations* or just the *Lagrange equations*, is the link
that permits us to use the principle of stationary action to compute the
motions of mechanical systems, and to relate the variational and
Newtonian formulations of mechanics.[^48^](#footnote_Temp_66)

#### [Lagrange equations](book-Z-H-4.html#%_toc_%_sec_Temp_67)

We will find that if *L* is a Lagrangian for a system that depends on
time, coordinates, and velocities, and if *q* is a coordinate path for
which the action *S*[*q*](*t*~1~, *t*~2~) is stationary (with respect to
any variation in the path that keeps the endpoints of the path fixed),
then

<div align="left">

![](chap1-Z-G-33.gif)

</div>

Here *L* is a real-valued function of a local tuple;
![](front-Z-G-D-2.gif)~1~ *L* and ![](front-Z-G-D-2.gif)~2~ *L* denote
the partial derivatives of *L* with respect to its generalized position
and generalized velocity arguments.[^49^](#footnote_Temp_68) The
function ![](front-Z-G-D-2.gif)~2~ *L* maps a local tuple to a structure
whose components are the derivatives of *L* with respect to each
component of the generalized velocity. The function
![](chap1-Z-G-D-9.gif)[*q*] maps time to the local tuple:
![](chap1-Z-G-D-9.gif)[*q*](*t*) = ( *t*, *q*(*t*), *Dq*(*t*), `...` ).
Thus the compositions ![](front-Z-G-D-2.gif)~1~ *L* o
![](chap1-Z-G-D-9.gif)[*q*] and ![](front-Z-G-D-2.gif)~2~ *L* o
![](chap1-Z-G-D-9.gif)[*q*] are functions of one argument, time. The
Lagrange equations assert that the derivative of
![](front-Z-G-D-2.gif)~2~ *L* o ![](chap1-Z-G-D-9.gif)[*q*] is equal to
![](front-Z-G-D-2.gif)~1~ *L* o ![](chap1-Z-G-D-9.gif)[*q*], at any
time. Given a Lagrangian, the Lagrange equations form a system of
ordinary differential equations that must be satisfied by realizable
paths.[^50^](#footnote_Temp_69)

### [1.5.1  Derivation of the Lagrange Equations](book-Z-H-4.html#%_toc_%_sec_1.5.1)

We will show that principle of stationary action implies that realizable
paths satisfy a set of ordinary differential equations. First we will
develop tools for investigating how path-dependent functions vary as the
paths are varied. We will then apply these tools to the action, to
derive the Lagrange equations.

#### [Varying a path](book-Z-H-4.html#%_toc_%_sec_Temp_70)

Suppose that we have a function *f*[*q*] that depends on a path *q*. How
does the function vary as the path is varied? Let *q* be a coordinate
path and *q* + ![](chap1-Z-G-D-12.gif) ![](chap1-Z-G-D-13.gif) be a
varied path, where the function ![](chap1-Z-G-D-13.gif) is a path-like
function that can be added to the path *q*, and the factor
![](chap1-Z-G-D-12.gif) is a scale factor. We define the *variation*
![](chap1-Z-G-D-17.gif)~![](chap1-Z-G-D-13.gif)~ *f*[*q*] of the
function *f* on the path *q* by[^51^](#footnote_Temp_71)

<div align="left">

![](chap1-Z-G-36.gif)

</div>

The variation of *f* is a linear approximation to the change in the
function *f* for small variations in the path. The variation of *f*
depends on ![](chap1-Z-G-D-13.gif).

A simple example is the variation of the identity path function:
*I*[*q*] = *q*. Applying the definition, we find

<div align="left">

![](chap1-Z-G-37.gif)

</div>

It is traditional to write
![](chap1-Z-G-D-17.gif)~![](chap1-Z-G-D-13.gif)~ *I*[*q*] simply as
![](chap1-Z-G-D-17.gif) *q*. Another example is the variation of the
path function that returns the derivative of the path. We have

<div align="left">

![](chap1-Z-G-38.gif)

</div>

It is traditional to write
![](chap1-Z-G-D-17.gif)~![](chap1-Z-G-D-13.gif)~ *g*[*q*] as
![](chap1-Z-G-D-17.gif) *Dq*.

The variation may be represented in terms of a derivative. Let
*g*(![](chap1-Z-G-D-12.gif)) = *f*[*q* + ![](chap1-Z-G-D-12.gif)
![](chap1-Z-G-D-13.gif)]; then

<div align="left">

![](chap1-Z-G-39.gif)

</div>

Variations have the following derivative-like properties. For
path-dependent functions *f* and *g* and constant *c*:

<div align="left">

![](chap1-Z-G-40.gif)

</div>

Let *F* be a path-independent function and *g* be a path-dependent
function; then

<div align="left">

![](chap1-Z-G-41.gif)

</div>

The operators *D* (differentiation) and ![](chap1-Z-G-D-17.gif)
(variation) commute in the following sense:

<div align="left">

![](chap1-Z-G-42.gif)

</div>

Variations also commute with integration in a similar sense.

If a path-dependent function *f* is stationary for a particular path *q*
with respect to small changes in that path, then it must be stationary
for a subset of those variations that results from adding small
multiples of a particular function ![](chap1-Z-G-D-13.gif) to *q*. So
the statement ![](chap1-Z-G-D-17.gif)~![](chap1-Z-G-D-13.gif)~ *f*[*q*]
= 0 for arbitrary ![](chap1-Z-G-D-13.gif) implies the function *f* is
stationary for small variations of the path around *q*.

**Exercise 1.7.**  **Properties of ![](chap1-Z-G-D-17.gif)**\
 Show that ![](chap1-Z-G-D-17.gif) has the
properties [1.23](#EQUATION_1.23)-[1.27](#EQUATION_1.27).

**Exercise 1.8.**  **Implementation of ![](chap1-Z-G-D-17.gif)**\

\
**a**.  Suppose we have a procedure `f` that implements a path-dependent
function: for path `q` and time `t` it has the value `((f q) t)`. The
procedure `delta` computes the variation
(![](chap1-Z-G-D-17.gif)~![](chap1-Z-G-D-13.gif)~ *f*)[*q*](*t*) as the
value of the expression `((((delta eta) f) q) t)`. Complete the
definition of `delta`:

`(define (((delta eta) f) q)   ...`  )\

**b**.  Use your `delta` procedure to verify the properties of
![](chap1-Z-G-D-17.gif) listed in exercise [1.7](#%_thm_1.7) for simple
functions such as implemented by the procedure `f`:

`(define (f q)   (compose      (literal-function 'F (-> (UP Real Real Real) Real))     (Gamma q))) `

This implements a one-degree-of-freedom path-dependent function that
depends on the local tuple of the path at each moment. You should
compute both sides of the equalities and compare the results.

#### [Varying the action](book-Z-H-4.html#%_toc_%_sec_Temp_74)

The action is the integral of the Lagrangian along a path:

<div align="left">

![](chap1-Z-G-43.gif)

</div>

For a realizable path *q* the variation of the action with respect to
any variation ![](chap1-Z-G-D-13.gif) that preserves the endpoints,
![](chap1-Z-G-D-13.gif)(*t*~1~) = ![](chap1-Z-G-D-13.gif)(*t*~2~) = 0,
is zero:

<div align="left">

![](chap1-Z-G-44.gif)

</div>

Variation commutes with integration, so the variation of the action is

<div align="left">

![](chap1-Z-G-45.gif)

</div>

Using the fact that

<div align="left">

![](chap1-Z-G-46.gif)

</div>

which follows from equations ([1.20](#EQUATION_1.20)) and
([1.21](#EQUATION_1.21)), and using the chain rule for
variations ([1.26](#EQUATION_1.26)), we get[^52^](#footnote_Temp_75)

<div align="left">

![](chap1-Z-G-48.gif)

</div>

Integrating the last term of equation ([1.32](#EQUATION_1.32)) by parts
gives

<div align="left">

![](chap1-Z-G-49.gif)

</div>

For our variation ![](chap1-Z-G-D-13.gif) we have
![](chap1-Z-G-D-13.gif)(*t*~1~) = ![](chap1-Z-G-D-13.gif)(*t*~2~) = 0,
so the first term vanishes.

Thus the variation of the action is zero if and only if

<div align="left">

![](chap1-Z-G-50.gif)

</div>

The variation of the action is zero because, by assumption, *q* is a
realizable path. Thus ([1.34](#EQUATION_1.34)) must be true for *any*
function ![](chap1-Z-G-D-13.gif) that is zero at the endpoints.

We retain enough freedom in the choice of the variation that the factor
in the integrand multiplying ![](chap1-Z-G-D-13.gif) is forced to be
zero at each point along the path. We argue by contradiction: Suppose
this factor were nonzero at some particular time. Then it would have to
be nonzero in at least one of its components. But if we choose our
![](chap1-Z-G-D-13.gif) to be a bump that is nonzero only in that
component in a neighborhood of that time, and zero everywhere else, then
the integral will be nonzero. So we may conclude that the factor in
curly brackets is identically zero:[^53^](#footnote_Temp_76)

<div align="left">

![](chap1-Z-G-51.gif)

</div>

This is just what we set out to obtain, the Lagrange equations.

A path satisfying Lagrange's equations is one for which the action is
stationary, and the fact that the action is stationary depends only on
the values of *L* at each point of the path (and at each point on nearby
paths), not on the coordinate system we use to compute these values. So
if the system's path satisfies Lagrange's equations in some particular
coordinate system, it must satisfy Lagrange's equations in *any*
coordinate system. Thus the equations of variational mechanics are
derived the same way in any configuration space and any coordinate
system.

#### [Harmonic oscillator](book-Z-H-4.html#%_toc_%_sec_Temp_77)

For an example, consider the harmonic oscillator. A Lagrangian is

<div align="left">

![](chap1-Z-G-52.gif)

</div>

Then

<div align="left">

![](chap1-Z-G-53.gif)

</div>

The Lagrangian is applied to a tuple of the time, a coordinate, and a
velocity. The symbols *t*, *x*, and *v* are arbitrary; they are used to
specify formal parameters of the Lagrangian.

Now suppose we have a configuration path *y*, which gives the coordinate
of the oscillator *y*(*t*) for each time *t*. The initial segment of the
corresponding local tuple at time *t* is

<div align="left">

![](chap1-Z-G-54.gif)

</div>

So

<div align="left">

![](chap1-Z-G-55.gif)

</div>

and

<div align="left">

![](chap1-Z-G-56.gif)

</div>

so the Lagrange equation is

<div align="left">

![](chap1-Z-G-57.gif)

</div>

which is the equation of motion of the harmonic oscillator.

#### [Orbital motion](book-Z-H-4.html#%_toc_%_sec_Temp_78)

As another example, consider the two-dimensional motion of a particle of
mass *m* with gravitational potential energy `-` µ/*r*, where *r* is the
distance to the center of attraction. A Lagrangian
is[^54^](#footnote_Temp_79)

<div align="left">

![](chap1-Z-G-58.gif)

</div>

where ![](chap1-Z-G-D-18.gif) and ![](chap1-Z-G-D-13.gif) are formal
parameters for rectangular coordinates of the particle, and
*v*~![](chap1-Z-G-D-18.gif)~ and *v*~![](chap1-Z-G-D-13.gif)~ are formal
parameters for corresponding rectangular velocity components.
Then[^55^](#footnote_Temp_80)

<div align="left">

![](chap1-Z-G-59.gif)

</div>

Similarly,

<div align="left">

![](chap1-Z-G-60.gif)

</div>

Now suppose we have a configuration path *q* = ( *x*, *y* ), so that the
coordinate tuple at time *t* is *q*(*t*) = ( *x*(*t*), *y*(*t*) ). The
initial segment of the local tuple at time *t* is

<div align="left">

![](chap1-Z-G-61.gif)

</div>

So

<div align="left">

![](chap1-Z-G-62.gif)

</div>

and

<div align="left">

![](chap1-Z-G-63.gif)

</div>

The component Lagrange equations at time *t* are

<div align="left">

![](chap1-Z-G-64.gif)

</div>

**Exercise 1.9.**  **Lagrange's equations**\
 Derive the Lagrange equations for the following systems, showing all of
the intermediate steps as in the harmonic oscillator and orbital motion
examples.

**a**.  A particle of mass *m* moves in a two-dimensional potential
*V*(*x*, *y*) = (*x*^2^ + *y*^2^)/2 + *x*^2^ *y* `-` *y*^3^/3, where *x*
and *y* are rectangular coordinates of the particle. A Lagrangian is
*L*(*t*; *x*, *y*; *v*~*x*~, *v*~*y*~) = (1/2) *m* (*v*~*x*~^2^ +
*v*~*y*~^2^) `-` *V*(*x*, *y*).

**b**.  An ideal planar pendulum consists of a bob of mass *m* connected
to a pivot by a massless rod of length *l* subject to uniform
gravitational acceleration *g*. A Lagrangian is *L*(*t*,
![](chap1-Z-G-D-19.gif), ![](chap1-Z-G-D-20.gif)) = (1/2) *m* *l*^2^
![](chap1-Z-G-D-20.gif)^2^ + *m* *g* *l* cos ![](chap1-Z-G-D-19.gif).
The formal parameters of *L* are *t*, ![](chap1-Z-G-D-19.gif), and
![](chap1-Z-G-D-20.gif); ![](chap1-Z-G-D-19.gif) measures the angle of
the pendulum rod to a plumb line and ![](chap1-Z-G-D-20.gif) is the
angular velocity of the rod.[^56^](#footnote_Temp_82)

**c**.  A Lagrangian for a particle of mass *m* constrained to move on a
sphere of radius *R* is *L*(*t*; ![](chap1-Z-G-D-19.gif),
![](chap1-Z-G-D-16.gif); ![](chap1-Z-G-D-21.gif), *ß*) = (1/2) *m*
*R*^2^ (![](chap1-Z-G-D-21.gif)^2^ + (*ß* sin
![](chap1-Z-G-D-19.gif))^2^). The angle ![](chap1-Z-G-D-19.gif) is the
colatitude of the particle and ![](chap1-Z-G-D-16.gif) is the longitude;
the rate of change of the colatitude is ![](chap1-Z-G-D-21.gif) and the
rate of change of the longitude is *ß*.

**Exercise 1.10.**  **Higher-derivative Lagrangians**\
 Derive Lagrange's equations for Lagrangians that depend on
accelerations. In particular, show that the Lagrange equations for
Lagrangians of the form *L*(*t*, *q*, ![](front-Z-G-D-1.gif),
![](chap1-Z-G-D-22.gif)) with ![](chap1-Z-G-D-22.gif) terms
are[^57^](#footnote_Temp_84)

<div align="left">

![](chap1-Z-G-66.gif)

</div>

In general, these equations, first derived by Poisson, will involve the
fourth derivative of *q*. Note that the derivation is completely
analogous to the derivation of the Lagrange equations without
accelerations; it is just longer. What restrictions must we place on the
variations so that the critical path satisfies a differential equation?

### [1.5.2  Computing Lagrange's Equations](book-Z-H-4.html#%_toc_%_sec_1.5.2)

The procedure for computing Lagrange's equations mirrors the functional
expression ([1.18](#EQUATION_1.18)), where the procedure `Gamma`
implements ![](chap1-Z-G-D-9.gif):[^58^](#footnote_Temp_85)

`(define ((Lagrange-equations Lagrangian) q)   (- (D (compose ((partial 2) Lagrangian) (Gamma q)))      (compose ((partial 1) Lagrangian) (Gamma q)))) `

The argument of `Lagrange-equations` is a procedure that computes a
Lagrangian. It returns a procedure that when applied to a path `q`
returns a procedure of one argument (time) that computes the left-hand
side of the Lagrange equations ([1.18](#EQUATION_1.18)). These residual
values are zero if `q` is a path for which the Lagrangian action is
stationary.

Observe that the `Lagrange-equations` procedure, like the Lagrange
equations themselves, is valid for *any* generalized coordinate system.
When we write programs to investigate particular systems, the procedures
that implement the Lagrangian function and the path *q* will reflect the
actual coordinates chosen to represent the system, but we use the same
`Lagrange-equations` procedure in each case. This abstraction reflects
the important fact that the method of derivation of Lagrange's equations
from a Lagrangian is always the same; it is independent of the number of
degrees of freedom, the topology of the configuration space, and the
coordinate system used to describe points in the configuration space.

#### [The free particle](book-Z-H-4.html#%_toc_%_sec_Temp_86)

Consider again the case of a free particle. The Lagrangian is
implemented by the procedure `L-free-particle`. Rather than numerically
integrating and minimizing the action, as we did in
section [1.4](book-Z-H-11.html#%_sec_1.4), we can check Lagrange's
equations for an arbitrary straight-line path *t*
![](chap1-Z-G-D-11.gif) ( *at* + *a*~0~, *bt* + *b*~0~, *ct* + *c*~0~ ):

`(define (test-path t)   (up (+ (* 'a t) 'a0)       (+ (* 'b t) 'b0)       (+ (* 'c t) 'c0))) (print-expression  (((Lagrange-equations (L-free-particle 'm))    test-path)   't)) (down 0 0 0) `

That the residuals are zero indicates that the test path satisfies the
Lagrange equations.[^59^](#footnote_Temp_87)

We can also apply the `Lagrange-equations` procedure to an arbitrary
function:[^60^](#footnote_Temp_88)

`(show-expression  (((Lagrange-equations (L-free-particle 'm))    (literal-function 'x))   't)) (* (((expt D 2) x) t) m) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-67.gif)

</div>

------------------------------------------------------------------------

The result is an expression containing the arbitrary time *t* and mass
*m*, so it is zero precisely when *D*^2^ *x* = 0, which is the expected
equation for a free particle.

#### [The harmonic oscillator](book-Z-H-4.html#%_toc_%_sec_Temp_89)

Consider the harmonic oscillator again, with
Lagrangian ([1.16](book-Z-H-11.html#EQUATION_1.16)). We know that the
motion of a harmonic oscillator is a sinusoid with a given amplitude,
frequency, and phase:

<div align="left">

![](chap1-Z-G-68.gif)

</div>

Suppose we have forgotten how the constants in the solution relate to
the physical parameters of the oscillator. Let's plug in the proposed
solution and look at the residual:

`(define (proposed-solution t)   (* 'a (cos (+ (* 'omega t) 'phi))))  (show-expression  (((Lagrange-equations (L-harmonic 'm 'k))    proposed-solution)   't)) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-69.gif)

</div>

------------------------------------------------------------------------

The residual here shows that for nonzero amplitude, the only solutions
allowed are ones where ( *k* `-` *m* ![](chap1-Z-G-D-23.gif)^2^ ) = 0 or
![](chap1-Z-G-D-23.gif) = (*k*/*m*)^1/2^.

**Exercise 1.11.**  ****\
 Compute Lagrange's equations for the Lagrangians in
exercise [1.9](#%_thm_1.9) using the `Lagrange-equations` procedure.
Additionally, use the computer to perform each of the steps in the
`Lagrange-equations` procedure and show the intermediate results. Relate
these steps to the ones you showed in the hand derivation of
exercise [1.9](#%_thm_1.9).

**Exercise 1.12.**  ****\
\
**a**.  Write a procedure to compute the Lagrange equations for
Lagrangians that depend upon acceleration, as in
exercise [1.10](#%_thm_1.10). Note that `Gamma` can take an optional
argument giving the length of the initial segment of the local tuple
needed. The default length is 3, giving components of the local tuple up
to and including the velocities.

**b**.  Use your procedure to compute the Lagrange equations for the
Lagrangian

<div align="left">

![](chap1-Z-G-70.gif)

</div>

Do you recognize the resulting equation of motion?

**c**.  For more fun, write the general Lagrange equation procedure that
takes a Lagrangian of any order, and the order, to produce the required
equations of motion.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^48^](#call_footnote_Temp_66) This result was initially discovered by
Euler and later rederived by Lagrange.

[^49^](#call_footnote_Temp_68) The derivative or partial derivative of a
function that takes structured arguments is a new function that takes
the same number and type of arguments. The range of this new function is
itself a structure with the same number of components as the argument
with respect to which the function is differentiated.

[^50^](#call_footnote_Temp_69) Lagrange's equations are traditionally
written in the form

<div align="left">

![](chap1-Z-G-34.gif)

</div>

or, if we write a separate equation for each component of *q*, as

<div align="left">

![](chap1-Z-G-35.gif)

</div>

In this way of writing Lagrange's equations the notation does not
distinguish between *L*, which is a real-valued function of three
variables (*t*, *q*, ![](front-Z-G-D-1.gif)), and *L* o
![](chap1-Z-G-D-9.gif)[*q*], which is a real-valued function of one real
variable *t*. If we do not realize this notational pun, the equations
don't make sense as written -- ![](front-Z-G-D-2.gif)
*L*/![](front-Z-G-D-2.gif) ![](front-Z-G-D-1.gif) is a function of three
variables, so we must regard the arguments *q*, ![](front-Z-G-D-1.gif)
as functions of *t* before taking *d*/*dt* of the expression. Similarly,
![](front-Z-G-D-2.gif) *L*/![](front-Z-G-D-2.gif) *q* is a function of
three variables, which we must view as a function of *t* before setting
it equal to *d*/*dt*(![](front-Z-G-D-2.gif) *L*/![](front-Z-G-D-2.gif)
![](front-Z-G-D-1.gif)). These implicit applications of the chain rule
pose no problem in performing hand computations -- once you understand
what the equations represent.

[^51^](#call_footnote_Temp_71) The variation operator
![](chap1-Z-G-D-17.gif)~![](chap1-Z-G-D-13.gif)~ is like the derivative
operator in that it acts on the immediately following function:
![](chap1-Z-G-D-17.gif)~![](chap1-Z-G-D-13.gif)~ *f*[*q*] =
(![](chap1-Z-G-D-17.gif)~![](chap1-Z-G-D-13.gif)~ *f*)[*q*].

[^52^](#call_footnote_Temp_75) A function of multiple arguments is
considered a function of a tuple of its arguments. Thus, the derivative
of a function of multiple arguments is a tuple of the partial
derivatives of that function with respect to each of the arguments. So
in the case of a Lagrangian *L*,

<div align="left">

![](chap1-Z-G-47.gif)

</div>

[^53^](#call_footnote_Temp_76) To make this argument more precise
requires careful analysis.

[^54^](#call_footnote_Temp_79) When we write a definition that names the
components of the local tuple, we indicate that these are grouped into
time, position, and velocity components by separating the groups with
semicolons.

[^55^](#call_footnote_Temp_80) The derivative with respect to a tuple is
a tuple of the partial derivatives with respect to each component of the
tuple (see the appendix on notation).

[^56^](#call_footnote_Temp_82) The symbol ![](chap1-Z-G-D-20.gif) is
just a mnemonic symbol; the dot over the ![](chap1-Z-G-D-19.gif) does
not indicate differentiation. To define *L* we could have just as well
have written: *L*(*a*, *b*, *c*) = (1/2) *m* *l*^2^ *c*^2^ + *m* *g* *l*
cos *b*. However, we use a dotted symbol to remind us that the argument
matching a formal parameter, such as ![](chap1-Z-G-D-20.gif), is a rate
of change of an angle, such as ![](chap1-Z-G-D-19.gif).

[^57^](#call_footnote_Temp_84) In traditional notation these equations
read

<div align="left">

![](chap1-Z-G-65.gif)

</div>

[^58^](#call_footnote_Temp_85) The `Lagrange-equations` procedure uses
the operations `(partial 1)` and `(partial 2)`, which implement the
partial derivative operators with respect to the second and third
argument positions (those with indices 1 and 2).

[^59^](#call_footnote_Temp_87) There is a Lagrange equation for every
degree of freedom. The residuals of all the equations are zero if the
path is realizable. The residuals are arranged in a `down` tuple because
they result from derivatives of the Lagrangian with respect to argument
slots that take `up` tuples. See the appendix on notation.

[^60^](#call_footnote_Temp_88) Observe that the second derivative is
indicated as the square of the derivative operator `(expt D 2)`.
Arithmetic operations in Scmutils extend over operators as well as
functions.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-11.html)</span><span>,
[next](book-Z-H-13.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


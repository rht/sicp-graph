<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-60.html)</span><span>,
[next](book-Z-H-62.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[5.4  Extended Phase Space](book-Z-H-4.html#%_toc_%_sec_5.4)
------------------------------------------------------------

In this section we show that we can treat time as just another
coordinate if we wish. Systems described by a time-dependent Hamiltonian
may be recast in terms of a time-independent Hamiltonian with an extra
degree of freedom. An advantage of this view is that what was a
time-dependent canonical transformation can be treated as a
time-independent transformation, where there are no additional
conditions for adjusting the Hamiltonian.

Suppose that we have some system characterized by a time-dependent
Hamiltonian, for example, a periodically driven pendulum. We may imagine
that there is some extremely massive oscillator, unperturbed by the
motion of the relatively massless pendulum, that produces the drive.
Indeed, we may think of time itself as the coordinate of an infinitely
massive particle moving uniformly and driving everything else. We often
consider the rotation of the Earth as exactly such a stable time
reference when performing short-time experiments in the laboratory.

More formally, consider a dynamical system with *n* degrees of freedom,
whose behavior is described by a possibly time-dependent Lagrangian *L*
with corresponding Hamiltonian *H*. We make a new dynamical system with
*n* + 1 degrees of freedom by extending the generalized coordinates to
include time and introducing a new independent variable. We also extend
the generalized velocities to include a velocity for the time
coordinate. In this new *extended state space* the coordinates are
redundant, so there is a constraint relating the time coordinate to the
new independent variable.

We relate the original dynamical system to the extended dynamical system
as follows: Let *q* be a coordinate path. Let *q*~*e*~,*t* :
![](chap2-Z-G-D-22.gif) ![](chap1-Z-G-D-11.gif)
*q*~*e*~(![](chap2-Z-G-D-22.gif)),*t*(![](chap2-Z-G-D-22.gif)) be a
coordinate path in the extended system where ![](chap2-Z-G-D-22.gif) is
the new independent variable. Then *q*~*e*~ = *q* o *t*, or
*q*~*e*~(![](chap2-Z-G-D-22.gif)) = *q*(*t*(![](chap2-Z-G-D-22.gif))).
Consequently, if *v* = *Dq* is the velocity along a path then
*v*~*e*~(![](chap2-Z-G-D-22.gif)) = *D*
*q*~*e*~(![](chap2-Z-G-D-22.gif)) = *Dq*(*t*(![](chap2-Z-G-D-22.gif))) ·
*Dt*(![](chap2-Z-G-D-22.gif)) = *v*(*t*(![](chap2-Z-G-D-22.gif))) ·
*v*~*t*~(![](chap2-Z-G-D-22.gif)).

We can find a Lagrangian for the extended system by requiring that the
value of the action be unchanged. Introduce the extended Lagrangian
action

<div align="left">

![](chap5-Z-G-91.gif)

</div>

with

<div align="left">

![](chap5-Z-G-92.gif)

</div>

We have

<div align="left">

![](chap5-Z-G-93.gif)

</div>

The extended system is subject to a constraint that relates the time to
the new independent variable. We assume the constraint is of the form
![](chap1-Z-G-D-16.gif)(![](chap2-Z-G-D-22.gif); *q*~*e*~, *q*~*t*~;
*v*~*e*~, *v*~*t*~) = *q*~*t*~ `-` *f*(![](chap2-Z-G-D-22.gif)) = 0. The
constraint is a holonomic constraint involving the coordinates and time,
so we can incorporate this constraint by augmenting the
Lagrangian:[^12^](#footnote_Temp_356)

<div align="left">

![](chap5-Z-G-94.gif)

</div>

The Lagrange equations of *L*'~*e*~ for *q*~*e*~ are satisfied for the
paths *q* o *t* where *q* is any path that satisfies the original
Lagrange equations of *L*.

The momenta conjugate to the coordinates are

<div align="left">

![](chap5-Z-G-95.gif)

</div>

So the extended momenta have the same values as the original momenta at
the corresponding states. The momentum conjugate to the time coordinate
is the negation of the energy plus *v*~![](chap1-Z-G-D-40.gif)~. The
momentum conjugate to ![](chap1-Z-G-D-40.gif) is the constraint, which
must be zero.

Next we carry out the transformation to the corresponding Hamiltonian
formulation. First, note that the Lagrangian *L*~*e*~ is a homogeneous
form of degree one in the velocities. Thus, by Euler's theorem,

<div align="left">

![](chap5-Z-G-96.gif)

</div>

The *p*![](front-Z-G-D-1.gif)-part of the Legendre transform of
*L*~*e*~' is

<div align="left">

![](chap5-Z-G-97.gif)

</div>

So the Hamiltonian *H*'~*e*~ corresponding to *L*'~*e*~ is

<div align="left">

![](chap5-Z-G-98.gif)

</div>

We have used the fact that that at corresponding states the momenta have
the same values, so on paths *p*~*e*~ = *p* o *t*, and

<div align="left">

![](chap5-Z-G-99.gif)

</div>

The Hamiltonian *H*'~*e*~ does not depend on ![](chap1-Z-G-D-40.gif) so
we deduce that *p*~![](chap1-Z-G-D-40.gif)~ is constant. In fact,
*p*~![](chap1-Z-G-D-40.gif)~ must be given the value zero, because it is
the constraint. When there is a cyclic coordinate we can form a reduced
Hamiltonian for the remaining degrees of freedom by substituting the
constant value of conserved momentum conjugate to the cyclic coordinate
into the Hamiltonian. The resulting Hamiltonian is

<div align="left">

![](chap5-Z-G-100.gif)

</div>

This extended Hamiltonian governs the evolution of the extended system,
for arbitrary *f*.[^13^](#footnote_Temp_357)

Hamilton's equations reduce to

<div align="left">

![](chap5-Z-G-101.gif)

</div>

The second equation gives the required relation between *t*
and ![](chap2-Z-G-D-22.gif). The first and third equations are
equivalent to Hamilton's equations in the original coordinates, as we
can see by using *q*~*e*~ = *q* o *t* to rewrite them:

<div align="left">

![](chap5-Z-G-102.gif)

</div>

Using *Dt*(![](chap2-Z-G-D-22.gif)) = *Df*(![](chap2-Z-G-D-22.gif)) and
dividing these factors out, we recover Hamilton's
equations.[^14^](#footnote_Temp_358)

Now consider the special case for which the time is the same as the
independent variable: *f*(![](chap2-Z-G-D-22.gif)) =
![](chap2-Z-G-D-22.gif), *Df*(![](chap2-Z-G-D-22.gif)) = 1. In this case
*q* = *q*~*e*~ and *p* = *p*~*e*~. The extended Hamiltonian becomes

<div align="left">

![](chap5-Z-G-103.gif)

</div>

Hamilton's equation for *t* becomes *Dt*(![](chap2-Z-G-D-22.gif)) = 1,
restating the constraint. The Hamilton's equations for *Dq*~*e*~ and
*Dp*~*e*~ are directly Hamilton's equations:

<div align="left">

![](chap5-Z-G-104.gif)

</div>

The extended Hamiltonian ([5.103](#EQUATION_5.103)) does not depend on
the independent variable, so it is a conserved quantity. Thus, up to an
additive constant *p*~*t*~ is equal to minus the energy. The Hamilton's
equation for *Dp*~*t*~ relates the change of the energy to
![](front-Z-G-D-2.gif)~0~ *H*. Note that in the more general case, the
momentum conjugate to the time is not the negation of the energy. This
choice, *t*(![](chap2-Z-G-D-22.gif)) = ![](chap2-Z-G-D-22.gif), is
useful for a number of applications.

Note that the extension transformation is canonical in the sense that
the two sets of equations of motion describe equivalent dynamics.
However, the transformation is not symplectic; in fact, it does not even
have the same number of input and output variables.

**Exercise 5.10.**  **Homogeneous extended Lagrangian**\
 Verify that *L*~*e*~ is homogeneous of degree one in the velocities.

**Exercise 5.11.**  **Lagrange equations**\
\
**a**.  Verify the claim that the Lagrange equations for *q*~*e*~ are
satisfied for exactly the same trajectories that satisfy the original
Lagrange equations for *q*.

**b**.  Verify the claim that the Lagrange equation for *t* relates the
rate of change of energy to ![](front-Z-G-D-2.gif)~0~ *L*.

**Exercise 5.12.**  **Lorentz transformations**\
 Investigate Lorentz transformations as point transformations in the
extended phase space.

#### [Restricted three-body problem](book-Z-H-4.html#%_toc_%_sec_Temp_362)

An example that shows the utility of reformulating a problem in the
extended phase space is the restricted three-body problem: the motion of
a low-mass particle subject to the gravitational attraction of two other
massive bodies that move in some fixed orbit. The problem is an
idealization of the situation where a body with very small mass moves in
the presence of two bodies with much larger masses. Any effects of the
smaller body on the larger bodies are neglected. In the simplest
version, the motion of all three bodies is assumed to be in the same
plane, and the orbit of the two massive bodies is circular.

The motion of the bodies with larger masses is not influenced by the
small mass, so we model this situation as the small body moving in a
time-varying field of the larger bodies undergoing a prescribed motion.
This situation can be captured as a time-dependent Hamiltonian:

<div align="left">

![](chap5-Z-G-105.gif)

</div>

where *r*~1~ and *r*~2~ are the distances of the small body to the
larger bodies, *m* is the mass of the small body, and *m*~1~ and *m*~2~
are the masses of the larger bodies. Note that *r*~1~ and *r*~2~ are
quantities that depend both on the position of the small particle and
the time varying position of the massive particles.

The massive bodies are in circular orbits and maintain constant distance
from the center of mass. Let *a*~1~ and *a*~2~ be the distances to the
center of mass; then the distances satisfy *m*~1~ *a*~1~ = *m*~2~
*a*~2~. The angular frequency is ![](chap1-Z-G-D-57.gif) = (*G*(*m*~1~ +
*m*~2~)/*a*^3^)^1/2^ where *a* is the distance between the masses.

In polar coordinates, with the center of mass of the subsystem of
massive particles at the origin and with *r* and ![](chap1-Z-G-D-19.gif)
describing the position of the low-mass particle, the positions of the
two massive bodies are *a*~2~ = *m*~1~ *a* / (*m*~1~ + *m*~2~) with
![](chap1-Z-G-D-19.gif)~2~ = ![](chap1-Z-G-D-57.gif) *t* , *a*~1~ =
*m*~2~ *a* / (*m*~1~ + *m*~2~) with ![](chap1-Z-G-D-19.gif)~1~ =
![](chap1-Z-G-D-57.gif) *t* + ![](chap1-Z-G-D-15.gif) . The distances to
the point masses are

<div align="left">

![](chap5-Z-G-106.gif)

</div>

So, in polar coordinates, the Hamiltonian is

<div align="left">

![](chap5-Z-G-107.gif)

</div>

We see therefore that the Hamiltonian can be written in terms of some
function *f* such that

<div align="left">

![](chap5-Z-G-108.gif)

</div>

The essential feature is that ![](chap1-Z-G-D-19.gif) and *t* appear in
the Hamiltonian only in the combination ![](chap1-Z-G-D-19.gif) `-`
![](chap1-Z-G-D-57.gif) *t*.

One way to get rid of the time dependence is to choose a new set of
variables with one coordinate equal to this combination
![](chap1-Z-G-D-19.gif) `-` ![](chap1-Z-G-D-57.gif) *t*, by making a
point transformation to a rotating coordinate system. We have shown that

<div align="left">

![](chap5-Z-G-109.gif)

</div>

with

<div align="left">

![](chap5-Z-G-110.gif)

</div>

is a canonical transformation. The new Hamiltonian, which is not the
energy, is conserved because there is no explicit time dependence. It is
a useful integral of motion -- the Jacobi
constant.[^15^](#footnote_Temp_363)

We can also eliminate the dependence on the independent time-like
variable from the Hamiltonian for the restricted problem by going to the
extended phase space, choosing *t* = ![](chap2-Z-G-D-22.gif). The
Hamiltonian

<div align="left">

![](chap5-Z-G-111.gif)

</div>

is autonomous and is consequently an integral of the motion. Again, we
see that ![](chap1-Z-G-D-19.gif) and *t* occur only in the combination
![](chap1-Z-G-D-19.gif) `-` ![](chap1-Z-G-D-57.gif) *t*, which suggests
a point transformation to a new coordinate ![](chap1-Z-G-D-19.gif)' =
![](chap1-Z-G-D-19.gif) `-` ![](chap1-Z-G-D-57.gif) *t*. This point
transformation is independent of the new independent variable
![](chap2-Z-G-D-22.gif). The transformation is specified in
equations ([5.109](#EQUATION_5.109)-[5.112](#EQUATION_5.109)), augmented
by relations specifying how the time coordinate and its conjugate
momentum are handled:

<div align="left">

![](chap5-Z-G-112.gif)

</div>

The new Hamiltonian is obtained by composing the old Hamiltonian with
the transformation:

<div align="left">

![](chap5-Z-G-113.gif)

</div>

We recognize that the new Hamiltonian in the extended phase space, which
has the same value as the original Hamiltonian in the extended phase
space, is just the Jacobi constant plus *p*'~*t*~. The new Hamiltonian
does not depend on *t*', so *p*'~*t*~ is a constant of the motion. In
fact, its value is irrelevant to the rest of the dynamical evolution, so
we may set the value of *p*'~*t*~ to zero if we like. Thus, we have
found that the Hamiltonian in the extended phase space, which is
conserved, is just the Jacobi constant plus an additive arbitrary
constant. We have two routes to the Jacobi constant: (1) transform the
original system to a rotating coordinate system to eliminate the time
dependence, but in the process add extra terms to the Hamiltonian, and
(2) go to the extended phase space and immediately get an integral, and
by going to rotating coordinates recognize that this Hamiltonian is the
same as the Jacobi constant. So sometimes the Hamiltonian in the
extended phase space is a useful integral.

**Exercise 5.13.**  **Transformations in the extended phase space**\
 In section [5.2.3](book-Z-H-59.html#%_sec_5.2.3) we found that
time-dependent transformations for which the derivative of the
coordinate-momentum part is symplectic are canonical only if the
Hamiltonian is modified by adding a function *K* subject to certain
constraints (equation [5.54](book-Z-H-59.html#EQUATION_5.54)). Show that
the constraints on *K* follow from the symplectic condition in the
extended phase space, using the choice *t* = ![](chap2-Z-G-D-22.gif).

### [5.4.1  Poincaré-Cartan Integral Invariant](book-Z-H-4.html#%_toc_%_sec_5.4.1)

A time-dependent transformation is canonical if in the extended phase
space the Hamiltonians transform by composition and the extended
phase-space transformation is symplectic. In
section [5.3](book-Z-H-60.html#%_sec_5.3) we showed that if the
derivative of the transformation is symplectic then the sum of the areas
of the projections of any two-dimensional region of phase space onto the
canonical *q*^*i*^, *p*~*i*~ planes is preserved. This invariance is
also true of symplectic transformations in the extended phase space. Let
*R* and *R*' be corresponding regions of extended phase-space
coordinates. Let *A*~*i*~ be the area of the projection of the region
*R* onto the canonical *q*^*i*^, *p*~*i*~ plane, and *A*'~*i*~ be the
area of the projection of the corresponding region *R*' onto the
canonical *q*'^*i*^, *p*'~*i*~ plane. In the extended phase space, we
also have a projection onto the *t*, *p*~*t*~ canonical plane. Let
*A*~*n*~ be the area of the projection onto the *t*, *p*~*t*~ plane. We
have then

<div align="left">

![](chap5-Z-G-114.gif)

</div>

In terms of integrals this is

<div align="left">

![](chap5-Z-G-115.gif)

</div>

This equality for the sum of area integrals can be rewritten in terms of
line integrals by Stokes's theorem:

<div align="left">

![](chap5-Z-G-116.gif)

</div>

where the order of the integration and summation can be reversed because
the boundary of *R* projects to the boundary on the canonical planes.

For the special choice of *t* = ![](chap2-Z-G-D-22.gif) this result can
be rephrased in an interesting way. Let *E* be the value of the
Hamiltonian in the original unextended phase space. Using *q*^*n*^ = *t*
and *p*~*n*~ = *p*~*t*~ = `-` *E*, we can write

<div align="left">

![](chap5-Z-G-117.gif)

</div>

and

<div align="left">

![](chap5-Z-G-118.gif)

</div>

The relations ([5.121](#EQUATION_5.121)) and ([5.122](#EQUATION_5.122))
are two formulations of the *Poincaré-Cartan integral invariant*.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^12^](#call_footnote_Temp_356) We augment the Lagrangian with the total
time derivative of the constraint so that the Legendre transform will be
well defined.

[^13^](#call_footnote_Temp_357) Once we have made this reduction, taking
*p*~![](chap1-Z-G-D-40.gif)~ to be zero, we can no longer perform a
Legendre transform back to the extended Lagrangian system; we cannot
solve for *p*~*t*~ in terms of *v*~*t*~. However, the Legendre transform
in the extended system from *H*'~*e*~ to *L*'~*e*~, with associated
state variables, is well defined.

[^14^](#call_footnote_Temp_358) If *f* is strictly increasing then *Df*
is never zero.

[^15^](#call_footnote_Temp_363) Actually, the traditional Jacobi
constant is *C* = `-` 2 *H*'.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-60.html)</span><span>,
[next](book-Z-H-62.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


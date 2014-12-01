<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-14.html)</span><span>,
[next](book-Z-H-16.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[1.8  Conserved Quantities](book-Z-H-4.html#%_toc_%_sec_1.8)
------------------------------------------------------------

A function of the state of the system that is constant along a solution
path is called a *conserved quantity* or a *constant of motion*. If *C*
is a conserved quantity, then

<div align="left">

![](chap1-Z-G-169.gif)

</div>

for solution paths *q*. Following historical practice we also refer to
constants of the motion as *integrals* of the
motion.[^79^](#footnote_Temp_136) In this section, we will investigate
systems with symmetry and find that symmetries are associated with
conserved quantities. For instance, linear momentum is conserved in a
system with translational symmetry, angular momentum is conserved if
there is rotational symmetry, energy is conserved if the system does not
depend on the origin of time. We first consider systems for which a
coordinate system can be chosen that expresses the symmetry naturally,
and later discuss systems for which no coordinate system can be chosen
that simultaneously expresses all symmetries.

### [1.8.1  Conserved Momenta](book-Z-H-4.html#%_toc_%_sec_1.8.1)

If a Lagrangian *L*(*t*, *q*, *v*) does not depend on some particular
coordinate *q*^*i*^, then

<div align="left">

![](chap1-Z-G-170.gif)

</div>

and the corresponding *i*th component of the Lagrange equations is

<div align="left">

![](chap1-Z-G-171.gif)

</div>

This is the same as[^80^](#footnote_Temp_137)

<div align="left">

![](chap1-Z-G-172.gif)

</div>

So we see that

<div align="left">

![](chap1-Z-G-173.gif)

</div>

is a conserved quantity. The function ![](chap1-Z-G-D-44.gif) is called
the *momentum state function*. The value of the momentum state function
is the *generalized momentum*. We refer to the *i*th component of the
generalized momentum as the momentum *conjugate* to the *i*th
coordinate.[^81^](#footnote_Temp_138) A generalized coordinate component
that does not appear explicitly in the Lagrangian is called a *cyclic
coordinate*. The generalized momentum component conjugate to any cyclic
coordinate is a constant of the motion. Its value is constant along
realizable paths; it may have different values on different paths. As we
will see, momentum is an important quantity even when it is not
conserved.

Given the coordinate path *q* and the Lagrangian *L*, the momentum path
*p* is

<div align="left">

![](chap1-Z-G-174.gif)

</div>

with components

<div align="left">

![](chap1-Z-G-175.gif)

</div>

The momentum path is well defined for any path *q*. If the path is
realizable and the Lagrangian does not depend on *q*^*i*^, then *p*~*i*~
is a constant function

<div align="left">

![](chap1-Z-G-176.gif)

</div>

The constant value of *p*~*i*~ may be different for different
trajectories.

#### [Examples of conserved momenta](book-Z-H-4.html#%_toc_%_sec_Temp_139)

The free-particle Lagrangian *L*(*t*, *x*, *v*) = (1/2) *mv*^2^ is
independent of *x*. So the momentum state function,
![](chap1-Z-G-D-44.gif)(*t*, *q*, *v*) = *mv*, is conserved along
realizable paths. The momentum path *p* for the coordinate path *q* is
*p*(*t*) = ![](chap1-Z-G-D-44.gif) o ![](chap1-Z-G-D-9.gif)[*q*](*t*) =
*m* *Dq*(*t*). For a realizable path *Dp*(*t*) = 0. For the free
particle the usual linear momentum is conserved for realizable paths.

For a particle in a central force field
(section [1.6](book-Z-H-13.html#%_sec_1.6)), the Lagrangian

<div align="left">

![](chap1-Z-G-177.gif)

</div>

depends on *r* but is independent of ![](chap1-Z-G-D-16.gif). The
momentum state function is

<div align="left">

![](chap1-Z-G-178.gif)

</div>

It has two components. The first component, the \`\`radial momentum,''
is not conserved. The second component, the \`\`angular momentum,'' is
conserved along any solution trajectory.

If the central-potential problem had been expressed in rectangular
coordinates, then all of the coordinates would have appeared in the
Lagrangian. In that case there would not be any obvious conserved
quantities. Nevertheless, the motion of the system does not depend on
the choice of coordinates, so the angular momentum is still conserved.

We see that there is great advantage in making a judicious choice for
the coordinate system. If we can choose the coordinates so that a
symmetry of the system is reflected in the Lagrangian by the absence of
some coordinate component, then the existence of a corresponding
conserved quantity will be automatic.[^82^](#footnote_Temp_140)

### [1.8.2  Energy Conservation](book-Z-H-4.html#%_toc_%_sec_1.8.2)

Momenta are conserved by the motion if the Lagrangian does not depend on
the corresponding coordinate. There is another constant of the motion,
the energy, if the Lagrangian *L*(*t*, *q*, ![](front-Z-G-D-1.gif)) does
not depend explicitly on the time: ![](front-Z-G-D-2.gif)~0~ *L* = 0.

Consider the time derivative of the Lagrangian along a solution path
*q*:

<div align="left">

![](chap1-Z-G-179.gif)

</div>

Using Lagrange's equations to rewrite the second term yields

<div align="left">

![](chap1-Z-G-180.gif)

</div>

Isolating ![](front-Z-G-D-2.gif)~0~ *L* and combining the first two
terms on the right side gives

<div align="left">

![](chap1-Z-G-181.gif)

</div>

where, as before, ![](chap1-Z-G-D-42.gif) selects the velocity from the
state. So we see that if ![](front-Z-G-D-2.gif)~0~ *L* = 0 then

<div align="left">

![](chap1-Z-G-182.gif)

</div>

is conserved along realizable paths. The function
![](chap1-Z-G-D-45.gif) is called the *energy state
function*.[^83^](#footnote_Temp_141) Let *E* = ![](chap1-Z-G-D-45.gif) o
![](chap1-Z-G-D-9.gif)[*q*] denote the energy function on the path *q*.
The energy function has a constant value along any realizable trajectory
if the Lagrangian has no explicit time dependence; the energy *E* may
have a different value for different trajectories. A system that has no
explicit time dependence is called *autonomous*.

Given a Lagrangian procedure `L`, we may compute the energy:

`(define (Lagrangian->energy L)   (let ((P ((partial 2) L)))     (- (* P velocity) L))) `

#### [Energy in terms of kinetic and potential energies](book-Z-H-4.html#%_toc_%_sec_Temp_142)

In some cases the energy can be written as the sum of kinetic and
potential energies. Suppose the system is composed of particles with
rectangular coordinates **x**~![](chap1-Z-G-D-21.gif)~, the movement of
which may be subject to constraints, and that these rectangular
coordinates are some functions of the generalized coordinates *q* and
possibly time *t*: **x**~![](chap1-Z-G-D-21.gif)~ =
*f*~![](chap1-Z-G-D-21.gif)~(*t*, *q*). We form the Lagrangian as *L* =
*T* `-` *V* and compute the kinetic energy in terms of *q* by writing
the rectangular velocities in terms of the generalized velocities:

<div align="left">

![](chap1-Z-G-183.gif)

</div>

The kinetic energy is

<div align="left">

![](chap1-Z-G-184.gif)

</div>

where *v*~![](chap1-Z-G-D-21.gif)~ is the magnitude of
**v**~![](chap1-Z-G-D-21.gif)~.

If the *f*~![](chap1-Z-G-D-21.gif)~ functions do not depend explicitly
on time (![](front-Z-G-D-2.gif)~0~ *f*~![](chap1-Z-G-D-21.gif)~ = 0),
then the rectangular velocities are homogeneous functions of the
generalized velocities of degree 1, and *T* is a homogeneous function of
the generalized velocities of degree 2, because it is formed by summing
the square of homogeneous functions of degree 1. If *T* is a homogeneous
function of degree 2 in the generalized velocities then

<div align="left">

![](chap1-Z-G-185.gif)

</div>

where the second equality follows from Euler's theorem on homogeneous
functions.[^84^](#footnote_Temp_143) The energy state function is

<div align="left">

![](chap1-Z-G-186.gif)

</div>

So if *f*~![](chap1-Z-G-D-21.gif)~ is independent of time, the energy
function can be rewritten

<div align="left">

![](chap1-Z-G-187.gif)

</div>

Notice that if *V* depends on time the energy is still the sum of the
kinetic energy and potential energy, but the energy is not conserved.

The energy state function is always a well defined function, whether or
not it can be written in the form *T* + *V*, and whether or not it is
conserved along realizable paths.

**Exercise 1.28.**  ****\
 An analogous result holds when the *f*~![](chap1-Z-G-D-21.gif)~ depend
explicitly on time.

**a**.   Show that in this case the kinetic energy contains terms that
are linear in the generalized velocities.

**b**.   Show that, by adding a total time derivative, the Lagrangian
can be written in the form *L* = *A* `-` *B*, where *A* is a homogeneous
quadratic form in the generalized velocities and *B* is independent of
velocity.

**c**.   Show, using Euler's theorem, that the energy function is
![](chap1-Z-G-D-45.gif) = *A* + *B*.

An example in which terms that were linear in the velocity were removed
from the Lagrangian by adding a total time derivative has already been
given: the driven pendulum.

**Exercise 1.29.**  ****\
 A particle of mass *m* slides off a horizontal cylinder of radius *R*
in a uniform gravitational field with acceleration *g*. If the particle
starts close to the top of the cylinder with zero initial speed, with
what angular velocity does it leave the cylinder?

### [1.8.3  Central Forces in Three Dimensions](book-Z-H-4.html#%_toc_%_sec_1.8.3)

One important physical system is the motion of a particle in a central
field in three dimensions, with an arbitrary potential energy *V*(*r*)
depending only on the radius. We will describe this system in spherical
coordinates *r*, ![](chap1-Z-G-D-19.gif), and ![](chap1-Z-G-D-16.gif),
where ![](chap1-Z-G-D-19.gif) is the colatitude and
![](chap1-Z-G-D-16.gif) is the longitude. The kinetic energy has three
terms:

<div align="left">

![](chap1-Z-G-188.gif)

</div>

As a procedure:

`(define ((T3-spherical m) state)   (let ((q (coordinate state))         (qdot (velocity state)))     (let ((r (ref q 0))           (theta (ref q 1))           (rdot (ref qdot 0))           (thetadot (ref qdot 1))           (phidot (ref qdot 2)))       (* 1/2 m          (+ (square rdot)             (square (* r thetadot))             (square (* r (sin theta) phidot))))))) `

The Lagrangian is then formed by subtracting the potential energy:

`(define (L3-central m Vr)   (define (Vs state)     (let ((r (ref (coordinate state) 0)))       (Vr r)))   (- (T3-spherical m) Vs)) `

Let's first look at the generalized forces (the derivatives of the
Lagrangian with respect to the generalized coordinates). We compute
these with a partial derivative with respect to the coordinate argument
of the Lagrangian:

`(show-expression  (((partial 1) (L3-central 'm (literal-function 'V)))   (up 't       (up 'r 'theta 'phi)       (up 'rdot 'thetadot 'phidot)))) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-189.gif)

</div>

------------------------------------------------------------------------

The ![](chap1-Z-G-D-16.gif) component of the force is zero because
![](chap1-Z-G-D-16.gif) does not appear in the Lagrangian (it is a
cyclic variable). The corresponding momentum component is conserved.
Compute the momenta:

`(show-expression  (((partial 2) (L3-central 'm (literal-function 'V)))   (up 't        (up 'r 'theta 'phi)       (up 'rdot 'thetadot 'phidot)))) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-190.gif)

</div>

------------------------------------------------------------------------

The momentum conjugate to ![](chap1-Z-G-D-16.gif) is conserved. This is
the *z* component of the angular momentum ![](chap1-Z-G-D-46.gif) × (*m*
![](chap1-Z-G-D-10.gif)), for vector position ![](chap1-Z-G-D-46.gif)
and linear momentum *m* ![](chap1-Z-G-D-10.gif). We can show this by
writing the *z* component of the angular momentum in spherical
coordinates:

`(define ((ang-mom-z m) state)   (let ((q (coordinate state))         (v (velocity state)))      (ref (cross-product q (* m v)) 2))) (define (s->r state)   (let ((q (coordinate state)))     (let ((r (ref q 0))           (theta (ref q 1))           (phi (ref q 2)))       (let ((x (* r (sin theta) (cos phi)))             (y (* r (sin theta) (sin phi)))             (z (* r (cos theta))))         (up x y z))))) (show-expression   ((compose (ang-mom-z 'm) (F->C s->r))    (up 't         (up 'r 'theta 'phi)        (up 'rdot 'thetadot 'phidot)))) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-191.gif)

</div>

------------------------------------------------------------------------

The choice of the *z*-axis is arbitrary, so the conservation of any
component of the angular momentum implies the conservation of all
components. Thus the total angular momentum is conserved. We can choose
the *z*-axis so all of the angular momentum is in the *z* component. The
angular momentum must be perpendicular to both the radius vector and the
linear momentum vector. Thus the motion is planar,
![](chap1-Z-G-D-19.gif) = ![](chap1-Z-G-D-15.gif)/2, and
![](chap1-Z-G-D-20.gif) = 0. Planar motion in a central-force field was
discussed in section [1.6](book-Z-H-13.html#%_sec_1.6).

We can also see that the energy state function computed from the
Lagrangian for a central field is in fact *T* + *V*:

`(show-expression  ((Lagrangian->energy (L3-central 'm (literal-function 'V)))   (up 't       (up 'r 'theta 'phi)       (up 'rdot 'thetadot 'phidot)))) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-192.gif)

</div>

------------------------------------------------------------------------

The energy is conserved because the Lagrangian has no explicit time
dependence.

**Exercise 1.30.**  **Driven spherical pendulum**\
 A spherical pendulum is a massive bob, subject to uniform gravity, that
may swing in three dimensions, but remains at a given distance from the
pivot. Formulate a Lagrangian for a spherical pendulum, driven by
vertical motion of the pivot. What symmetry(ies) can you find? Find
coordinates that express the symmetry. What is conserved? Give analytic
expression(s) for the conserved quantity(ies).

### [1.8.4  Noether's Theorem](book-Z-H-4.html#%_toc_%_sec_1.8.4)

We have seen that if a system has a symmetry and if a coordinate system
can be chosen so that the Lagrangian does not depend on the coordinate
associated with the symmetry, then there is a conserved quantity
associated with the symmetry. However, there are more general symmetries
that no coordinate system can fully express. For example, motion in a
central potential is spherically symmetric (the dynamical system is
invariant under rotations about any axis), but the expression of the
Lagrangian for the system in spherical coordinates exhibits symmetry
around only one axis. More generally, a Lagrangian has a symmetry if
there is a coordinate transformation that leaves the Lagrangian
unchanged. A continuous symmetry is a parametric family of symmetries.
Noether proved that for any continuous symmetry there is a conserved
quantity.

Consider a parametric coordinate transformation ![](chap1-Z-G-D-47.gif)
with parameter *s*:

<div align="left">

![](chap1-Z-G-193.gif)

</div>

To this parametric coordinate transformation there corresponds a
parametric state transformation ![](chap1-Z-G-D-48.gif):

<div align="left">

![](chap1-Z-G-194.gif)

</div>

We require that the transformation ![](chap1-Z-G-D-47.gif)(0) be the
identity coordinate transformation *x*' =
![](chap1-Z-G-D-47.gif)(0)(*t*, *x*'), and as a consequence
![](chap1-Z-G-D-48.gif)(0) is the identity state transformation ( *t*,
*x*', *v*' ) = ![](chap1-Z-G-D-48.gif)(0)(*t*, *x*', *v*'). The
Lagrangian *L* has a continuous symmetry corresponding to
![](chap1-Z-G-D-47.gif) if it is invariant under the transformations

<div align="left">

![](chap1-Z-G-195.gif)

</div>

for any *s*. The Lagrangian *L* is the same function as the transformed
Lagrangian ![](chap1-Z-G-D-49.gif)(*s*).

That ![](chap1-Z-G-D-49.gif)(*s*) = *L* for any *s* implies
*D*![](chap1-Z-G-D-49.gif)(*s*) = 0. Explicitly,
![](chap1-Z-G-D-49.gif)(*s*) is

<div align="left">

![](chap1-Z-G-196.gif)

</div>

where we have rewritten the velocity component of
![](chap1-Z-G-D-48.gif)(*s*) in terms of the total time derivative. The
derivative of ![](chap1-Z-G-D-49.gif) is zero:

<div align="left">

![](chap1-Z-G-197.gif)

</div>

where we have used the fact that[^85^](#footnote_Temp_147)

<div align="left">

![](chap1-Z-G-198.gif)

</div>

On a realizable path *q* we can use the Lagrange equations to rewrite
the first term:

<div align="left">

![](chap1-Z-G-199.gif)

</div>

For *s* = 0 the paths *q* and *q*' are the same, because
![](chap1-Z-G-D-47.gif)(0) is the identity, so
![](chap1-Z-G-D-9.gif)[*q*] = ![](chap1-Z-G-D-9.gif)[*q*'] and this
equation becomes

<div align="left">

![](chap1-Z-G-200.gif)

</div>

Thus the state function ![](chap1-Z-G-D-50.gif),

<div align="left">

![](chap1-Z-G-201.gif)

</div>

is conserved along solution trajectories. This is Noether's integral.
The integral is the product of the momentum and a vector associated with
the symmetry.

#### [Illustration: motion in a central potential](book-Z-H-4.html#%_toc_%_sec_Temp_148)

For example, consider the central potential Lagrangian in rectangular
coordinates:

<div align="left">

![](chap1-Z-G-202.gif)

</div>

and a parametric rotation *R*~*z*~(*s*) about the *z* axis

<div align="left">

![](chap1-Z-G-203.gif)

</div>

The rotation is an orthogonal transformation so

<div align="left">

![](chap1-Z-G-204.gif)

</div>

Differentiating along a path, we get

<div align="left">

![](chap1-Z-G-205.gif)

</div>

so the velocities also transform by an orthogonal transformation, and
*v*~*x*~^2^ + *v*~*y*~^2^ + *v*~*z*~^2^ = (*v*~*x*~')^2^ +
(*v*~*y*~')^2^ + (*v*~*z*~')^2^ . Thus

<div align="left">

![](chap1-Z-G-206.gif)

</div>

and we see that *L*' is precisely the same function as *L*.

The momenta are

<div align="left">

![](chap1-Z-G-207.gif)

</div>

and

<div align="left">

![](chap1-Z-G-208.gif)

</div>

So the Noether integral is

<div align="left">

![](chap1-Z-G-209.gif)

</div>

which we recognize as minus the *z* component of the angular momentum:
![](chap1-Z-G-D-26.gif) × (*m* ![](chap1-Z-G-D-10.gif)). Since the
Lagrangian is preserved by any continuous rotational symmetry, all
components of the vector angular momenta are conserved for the
central-potential problem.

The procedure calls `((Rx angle-x) q)`, `((Ry angle-y) q)`, and
`((Rz angle-z) q)` rotate the rectangular tuple `q` about the indicated
axis by the indicated angle.[^86^](#footnote_Temp_149) We use these to
make a parametric coordinate transformation `F-tilde`:

`(define (F-tilde angle-x angle-y angle-z)   (compose (Rx angle-x) (Ry angle-y) (Rz angle-z) coordinate)) `

A Lagrangian for motion in a central potential is

`(define ((L-central-rectangular m U) state)   (let ((q (coordinate state))         (v (velocity state)))     (- (* 1/2 m (square v)) (U (sqrt (square q)))))) `

The Noether integral is then

`(define Noether-integral   (let ((L (L-central-rectangular              'm (literal-function 'U))))     (* ((partial 2) L) ((D F-tilde) 0 0 0))))  (print-expression   (Noether-integral      (up 't         (up 'x 'y 'z)         (up 'vx 'vy 'vz)))) (down (+ (* m vy z) (* -1 m vz y))       (+ (* m vz x) (* -1 m vx z))       (+ (* m vx y) (* -1 m vy x))) `

We get all three components of the angular momentum.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^79^](#call_footnote_Temp_136) In older literature conserved quantities
are sometimes called *first integrals*.

[^80^](#call_footnote_Temp_137) The derivative of a component is equal
to the component of the derivative.

[^81^](#call_footnote_Temp_138) Observe that we indicate a component of
the generalized momentum with a subscript, and a component of the
generalized coordinates with a superscript. These conventions are
consistent with those commonly used in tensor algebra, which is
sometimes helpful in working out complex problems.

[^82^](#call_footnote_Temp_140) In general, conserved quantities in a
physical system are associated with continuous symmetries, whether or
not one can find a coordinate system in which the symmetry is apparent.
This powerful notion was formalized and a theorem linking conservation
laws with symmetries was proved by Noether early in the 20th century.
See section [1.8.4](#%_sec_1.8.4) on Noether's theorem.

[^83^](#call_footnote_Temp_141) The sign of the energy state function is
a matter of convention.

[^84^](#call_footnote_Temp_143) A function *f* is homogenous of degree
*n* if and only if *f*(*ax*) = *a*^*n*^*f*(*x*). Euler's theorem says
that if *f* is a homogeneous function of degree *n*, then *Df*(*x*)*x* =
*nf*(*x*). The proof is as follows: Let *g*~*x*~(*a*) = *f*(*ax*). Then
*Dg*~*x*~(*a*) = *Df*(*ax*)*x*. But *g*~*x*~(*a*) = *a*^*n*^*f*(*x*) by
the definition of homogeneity. Therefore *Dg*~*x*~(*a*) =
*na*^*n*`-`1^*f*(*x*). Equating these, we find *Df*(*ax*)*x* =
*na*^*n*`-`1^*f*(*x*). Specializing to *a* = 1 we obtain *Df*(*x*)*x* =
*nf*(*x*) as required.

[^85^](#call_footnote_Temp_147) The total time derivative is like a
derivative with respect to a real-number argument in that it does not
generate structure, so it can commute with derivatives that generate
structure. Be careful, though: it may not commute with some derivatives
for other reasons. For example, *D*~*t*~ ![](front-Z-G-D-2.gif)~1~
(![](chap1-Z-G-D-47.gif)(*s*)) is the same as ![](front-Z-G-D-2.gif)~1~
*D*~*t*~ (![](chap1-Z-G-D-47.gif)(*s*)), but *D*~*t*~
![](front-Z-G-D-2.gif)~2~ (![](chap1-Z-G-D-47.gif)(*s*)) is not the same
as ![](front-Z-G-D-2.gif)~2~ *D*~*t*~ (![](chap1-Z-G-D-47.gif)(*s*)).
The reason is that ![](chap1-Z-G-D-47.gif)(*s*) does not depend on the
velocity, but *D*~*t*~ (![](chap1-Z-G-D-47.gif)(*s*)) does.

[^86^](#call_footnote_Temp_149) The definition of the procedure `Rx` is

`(define ((Rx angle) q)   (let ((ca (cos angle)) (sa (sin angle)))     (let ((x (ref q 0)) (y (ref q 1)) (z (ref q 2)))       (up x           (- (* ca y) (* sa z))           (+ (* sa y) (* ca z)))))) `

The definitions of `Ry` and `Rz` are similar.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-14.html)</span><span>,
[next](book-Z-H-16.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


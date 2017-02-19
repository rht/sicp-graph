<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-12.html)</span><span>,
[next](book-Z-H-14.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[1.6  How to Find Lagrangians](book-Z-H-4.html#%_toc_%_sec_1.6)
---------------------------------------------------------------

Lagrange's equations are a system of second-order differential
equations. In order to use them to compute the evolution of a mechanical
system, we must find a suitable Lagrangian for the system. There is no
general way to construct a Lagrangian for every system, but there is an
important class of systems for which we can identify Lagrangians in a
straightforward way in terms of kinetic and potential energy. The key
idea is to construct a Lagrangian *L* such that Lagrange's equations are
Newton's equations ![](chap1-Z-G-D-24.gif) = *m*![](chap1-Z-G-D-25.gif).

Suppose our system consists of *N* particles indexed by
![](chap1-Z-G-D-21.gif), with mass *m*~![](chap1-Z-G-D-21.gif)~ and
vector position ![](chap1-Z-G-D-26.gif)~![](chap1-Z-G-D-21.gif)~(*t*).
Suppose further that the forces acting on the particles can be written
in terms of a gradient of a potential energy ![](chap1-Z-G-D-27.gif)
that is a function of the positions of the particles and possibly time,
but does not depend on the velocities. In other words, the force on
particle ![](chap1-Z-G-D-21.gif) is
![](chap1-Z-G-D-24.gif)~![](chap1-Z-G-D-21.gif)~ = `-`
![](chap1-Z-G-D-28.gif)~![](chap1-Z-G-D-26.gif)~![](chap1-Z-G-D-21.gif)~~
![](chap1-Z-G-D-27.gif), where
![](chap1-Z-G-D-28.gif)~![](chap1-Z-G-D-26.gif)~![](chap1-Z-G-D-21.gif)~~
![](chap1-Z-G-D-27.gif) is the gradient of ![](chap1-Z-G-D-27.gif) with
respect to the position of the particle with index
![](chap1-Z-G-D-21.gif). We can write Newton's equations as

<div align="left">

![](chap1-Z-G-71.gif)

</div>

Vectors can be represented as tuples of components of the vectors on a
rectangular basis. So ![](chap1-Z-G-D-26.gif)~1~(*t*) is represented as
the tuple **x**~1~(*t*). Let *V* be the potential energy function
expressed in terms of components:

<div align="left">

![](chap1-Z-G-72.gif)

</div>

Newton's equations are

<div align="left">

![](chap1-Z-G-73.gif)

</div>

where ![](front-Z-G-D-2.gif)~1,\\ ![](chap1-Z-G-D-21.gif)~ *V* is the
partial derivative of *V* with respect to the
**x**~![](chap1-Z-G-D-21.gif)~(*t*) argument slot.

To form the Lagrange equations we collect all the position components of
all the particles into one tuple *x*(*t*), so *x*(*t*) = (**x**~0~(*t*),
`...`, **x**~*N*`-`1~(*t*)). The Lagrange equations for the coordinate
path *x* are

<div align="left">

![](chap1-Z-G-74.gif)

</div>

Observe that Newton's equations ([1.51](#EQUATION_1.51)) are just the
components of the Lagrange equations ([1.54](#EQUATION_1.54)) if we
choose *L* to have the properties

<div align="left">

![](chap1-Z-G-75.gif)

</div>

here *V*(*t*, *x*(*t*)) = *V*(*t*; **x**~0~(*t*), `...`,
**x**~*N*`-`1~(*t*)) and
![](front-Z-G-D-2.gif)~1,![](chap1-Z-G-D-21.gif)~ *V*(*t*, *x*(*t*)) is
the tuple of the components of the derivative of *V* with respect to the
coordinates of the particle with index ![](chap1-Z-G-D-21.gif),
evaluated at time *t* and coordinates *x*(*t*). These conditions are
satisfied if for every **a**~![](chap1-Z-G-D-21.gif)~
and **b**~![](chap1-Z-G-D-21.gif)~

<div align="left">

![](chap1-Z-G-76.gif)

</div>

and

<div align="left">

![](chap1-Z-G-77.gif)

</div>

where *a* = (**a**~0~, `...` , **a**~*N*`-`1~). We use the symbols *a*
and *b* to emphasize that these are just formal parameters of the
Lagrangian. One choice for *L* that has the required
properties ([1.56](#EQUATION_1.56)-[1.57](#EQUATION_1.57)) is

<div align="left">

![](chap1-Z-G-78.gif)

</div>

where *v*~![](chap1-Z-G-D-21.gif)~^2^ is the sum of the squares of the
components of **v**~![](chap1-Z-G-D-21.gif)~.[^61^](#footnote_Temp_92)

The first term is the kinetic energy, conventionally denoted *T*. So
this choice for the Lagrangian is *L*(*t*, *x*, *v*) = *T*(*t*, *x*,
*v*) `-` *V*(*t*, *x*), the difference of the kinetic and potential
energy. We will often extend the arguments of the potential energy
function to include the velocities so that we can write *L* = *T* `-`
*V*.[^62^](#footnote_Temp_93)

#### [Hamilton's principle](book-Z-H-4.html#%_toc_%_sec_Temp_94)

Given a system of point particles for which we can identify the force as
the (negative) derivative of a potential energy *V* that is independent
of velocity, we have shown that the system evolves along a path that
satisfies Lagrange's equations with *L* = *T* `-` *V*. Having identified
a Lagrangian for this class of systems, we can restate the principle of
stationary action in terms of energies. This statement is known as
*Hamilton's principle*: A point-particle system for which the force is
derived from a velocity-independent potential energy evolves along a
path *q* for which the action

<div align="left">

![](chap1-Z-G-79.gif)

</div>

is stationary with respect to variations of the path *q* that leave the
endpoints fixed, where *L* = *T* `-` *V* is the difference between
kinetic and potential energy.[^63^](#footnote_Temp_95)

It might seem that we have reduced Lagrange's equations to nothing more
than ![](chap1-Z-G-D-24.gif) = *m* ![](chap1-Z-G-D-25.gif), and indeed,
the principle is motivated by comparing the two equations for this
special class of systems. However, the Lagrangian formulation of the
equations of motion has an important advantage over
![](chap1-Z-G-D-24.gif) = *m* ![](chap1-Z-G-D-25.gif). Our derivation
used the rectangular components **x**~![](chap1-Z-G-D-21.gif)~ of the
positions of the constituent particles for the generalized coordinates,
but if the system's path satisfies Lagrange's equations in some
particular coordinate system, it must satisfy the equations in *any*
coordinate system. Thus we see that *L* = *T* `-` *V* is suitable as a
Lagrangian with *any* set of generalized coordinates. The equations of
variational mechanics are derived the same way in any configuration
space and any coordinate system. In contrast, the Newtonian formulation
is based on elementary geometry: In order for
*D*^2^![](chap1-Z-G-D-26.gif)(*t*) to be meaningful as an acceleration,
![](chap1-Z-G-D-26.gif)(*t*) must be a vector in physical space.
Lagrange's equations have no such restriction on the meaning of the
coordinate *q*. The generalized coordinates can be any parameters that
conveniently describe the configurations of the system.

#### [Constant acceleration](book-Z-H-4.html#%_toc_%_sec_Temp_96)

Consider a particle of mass *m* in a uniform gravitational field with
acceleration *g*. The potential energy is *m* *g* *h* where *h* is the
height of the particle. The kinetic energy is just (1/2) *mv*^2^. A
Lagrangian for the system is the difference of the kinetic and potential
energies. In rectangular coordinates, with *y* measuring the vertical
position and *x* measuring the horizontal position, the Lagrangian is
*L*(*t*; *x*, *y*; *v*~*x*~, *v*~*y*~) = (1/2) *m* ( *v*~*x*~^2^ +
*v*~*y*~^2^ ) `-` *m* *g* *y*. We have[^64^](#footnote_Temp_97)

`(define ((L-uniform-acceleration m g) local)   (let ((q (coordinate local))         (v (velocity local)))     (let ((y (ref q 1)))       (- (* 1/2 m (square v)) (* m g y))))) (show-expression  (((Lagrange-equations     (L-uniform-acceleration 'm 'g))    (up (literal-function 'x)         (literal-function 'y)))   't)) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-80.gif)

</div>

------------------------------------------------------------------------

This equation describes unaccelerated motion in the horizontal direction
(*mD*^2^ *x*(*t*) = 0) and constant acceleration in the vertical
direction (*mD*^2^ *y*(*t*) = `-` *g* *m*).

#### [Central force field](book-Z-H-4.html#%_toc_%_sec_Temp_98)

Consider planar motion of a particle of mass *m* in a central force
field, with an arbitrary potential energy *U*(*r*) depending only upon
the distance *r* to the center of attraction. We will derive the
Lagrange equations for this system in both rectangular coordinates and
polar coordinates.

In rectangular coordinates (*x*, *y*), with origin at the center of
attraction, the potential energy is *V*(*t*; *x*, *y*) = *U*((*x*^2^ +
*y*^2^)^1/2^) and the kinetic energy is *T*(*t*; *x*, *y*; *v*~*x*~,
*v*~*y*~) = (1/2) *m* (*v*~*x*~^2^ + *v*~*y*~^2^). A Lagrangian for the
system is *L* = *T* `-` *V*:

<div align="left">

![](chap1-Z-G-81.gif)

</div>

As a procedure:

`(define ((L-central-rectangular m U) local)   (let ((q (coordinate local))         (v (velocity local)))     (- (* 1/2 m (square v))        (U (sqrt (square q)))))) `

The Lagrange equations are

`(show-expression  (((Lagrange-equations      (L-central-rectangular 'm (literal-function 'U)))    (up (literal-function 'x)         (literal-function 'y)))   't)) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-82.gif)

</div>

------------------------------------------------------------------------

We can rewrite these Lagrange equations as:

<div align="left">

![](chap1-Z-G-83.gif)

</div>

where *r*(*t*) = ((*x*(*t*))^2^ + (*y*(*t*))^2^)^1/2^. We can interpret
these as follows. The particle is subject to a radially directed force
with magnitude `-` *DU*(*r*). Newton's equations equate the force with
the product of the mass and the acceleration. The two Lagrange equations
are just the rectangular components of Newton's equations.

We can describe the same system in polar coordinates. The relationship
between rectangular coordinates (*x*, *y*) and polar coordinates (*r*,
![](chap1-Z-G-D-16.gif)) is

<div align="left">

![](chap1-Z-G-84.gif)

</div>

The relationship of the generalized velocities is derived from the
coordinate transformation. Consider a configuration path that is
represented in both rectangular and polar coordinates. Let
![](chap1-Z-G-D-29.gif) and ![](chap1-Z-G-D-30.gif) be components of the
rectangular coordinate path, and let ![](chap1-Z-G-D-31.gif) and
![](chap1-Z-G-D-32.gif) be components of the corresponding polar
coordinate path. The rectangular components at time *t* are
(![](chap1-Z-G-D-29.gif)(*t*), ![](chap1-Z-G-D-30.gif)(*t*)) and the
polar coordinates at time *t* are (![](chap1-Z-G-D-31.gif)(*t*),
![](chap1-Z-G-D-32.gif)(*t*)). They are related
by ([1.62](#EQUATION_1.62)):

<div align="left">

![](chap1-Z-G-85.gif)

</div>

The rectangular velocity at time *t* is
(*D*![](chap1-Z-G-D-29.gif)(*t*), *D*![](chap1-Z-G-D-30.gif)(*t*)).
Differentiating ([1.63](#EQUATION_1.63)) gives the relationship among
the velocities

<div align="left">

![](chap1-Z-G-86.gif)

</div>

These relations are valid for any configuration path at any moment, so
we can abstract them to relations among coordinate representations of an
arbitrary velocity. Let *v*~*x*~ and *v*~*y*~ be the rectangular
components of the velocity and ![](chap1-Z-G-D-33.gif) and
![](chap1-Z-G-D-34.gif) be the rate of change of *r* and
![](chap1-Z-G-D-16.gif). Then

<div align="left">

![](chap1-Z-G-87.gif)

</div>

The kinetic energy is (1/2) *m*(*v*~*x*~^2^ + *v*~*y*~^2^):

<div align="left">

![](chap1-Z-G-88.gif)

</div>

and the Lagrangian is

<div align="left">

![](chap1-Z-G-89.gif)

</div>

We express this Lagrangian as follows:

`(define ((L-central-polar m U) local)   (let ((q (coordinate local))         (qdot (velocity local)))     (let ((r (ref q 0)) (phi (ref q 1))           (rdot (ref qdot 0)) (phidot (ref qdot 1)))       (- (* 1/2 m            (+ (square rdot)               (square (* r phidot))) )          (U r))))) `

Lagrange's equations are

`(show-expression  (((Lagrange-equations      (L-central-polar 'm (literal-function 'U)))    (up (literal-function 'r)         (literal-function 'phi)))   't)) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-90.gif)

</div>

------------------------------------------------------------------------

We can interpret the first equation as saying that the product of the
mass and the radial acceleration is the sum of the force due to the
potential and the centrifugal force. The second equation can be
interpreted as saying that the derivative of the angular momentum
*mr*^2^*D* ![](chap1-Z-G-D-16.gif) is zero, so angular momentum is
conserved.

Note that we used the same `Lagrange-equations` procedure for the
derivation in both coordinate systems. Coordinate representations of the
Lagrangian are different for different coordinate systems, and the
Lagrange equations in different coordinate systems look different. Yet
the same method is used to derive the Lagrange equations in any
coordinate system.

**Exercise 1.13.**  ****\

Check that the Lagrange equations for central force motion in polar
coordinates and in rectangular coordinates are equivalent. Determine the
relationship among the second derivatives by substituting paths into the
transformation equations and computing derivatives, then substitute
these relations into the equations of motion.

### [1.6.1  Coordinate Transformations](book-Z-H-4.html#%_toc_%_sec_1.6.1)

The motion of a system is independent of the coordinates we use to
describe it. This coordinate-free nature of the motion is apparent in
the action principle. The action depends only on the value of the
Lagrangian along the path and not on the particular coordinates used in
the representation of the Lagrangian. We can use this property to find a
Lagrangian in one coordinate system in terms of a Lagrangian in another
coordinate system.

Suppose we have a mechanical system whose motion is described by a
Lagrangian *L* that depends on time, coordinates, and velocities. And
suppose we have a coordinate transformation *F* such that *x* = *F*(*t*,
*x*'). The Lagrangian *L* is expressed in terms of the unprimed
coordinates. We want to find a Lagrangian *L*' expressed in the primed
coordinates that describes the same system. One way to do this is to
require that the value of the Lagrangian along any configuration path be
independent of the coordinate system. If *q* is a path in the unprimed
coordinates and *q*' is the corresponding path in primed coordinates,
then the Lagrangians must satisfy:

<div align="left">

![](chap1-Z-G-91.gif)

</div>

We have seen that the transformation from rectangular to polar
coordinates implies that the generalized velocities transform in a
certain way. The velocity transformation can be deduced from the
requirement that a path in polar coordinates and a corresponding path in
rectangular coordinates are consistent with the coordinate
transformation. In general, the requirement that paths in two different
coordinate systems be consistent with the coordinate transformation can
be used to deduce how all of the components of the local tuple
transform. Given a coordinate transformation *F*, let *C* be the
corresponding function that maps local tuples in the primed coordinate
system to corresponding local tuples in the unprimed coordinate system:

<div align="left">

![](chap1-Z-G-92.gif)

</div>

We will deduce the general form of *C* below.

Given such a local-tuple transformation *C*, a Lagrangian *L*' that
satisfies equation ([1.68](#EQUATION_1.68)) is

<div align="left">

![](chap1-Z-G-93.gif)

</div>

We can see this by substituting for *L*' in
equation ([1.68](#EQUATION_1.68)):

<div align="left">

![](chap1-Z-G-94.gif)

</div>

To find the local-tuple transformation *C* given a coordinate
transformation *F*, we deduce how each component of the local tuple
transforms. Of course, the coordinate transformation specifies how the
coordinate component of the local tuple transforms. The
generalized-velocity component of the local-tuple transformation can be
deduced as follows. Let *q* and *q*' be the same configuration path
expressed in the two coordinate systems. Substituting these paths into
the coordinate transformation and computing the derivative, we find

<div align="left">

![](chap1-Z-G-95.gif)

</div>

Through any point there is always a path of any given velocity, so we
may generalize and conclude that along corresponding coordinate paths
the generalized velocities satisfy

<div align="left">

![](chap1-Z-G-96.gif)

</div>

If needed, rules for higher-derivative components of the local tuple can
be determined in a similar fashion. The local-tuple transformation that
takes a local tuple in the primed system to a local tuple in the
unprimed system is constructed from the component transformations:

<div align="left">

![](chap1-Z-G-97.gif)

</div>

So if we take the Lagrangian *L*' to be

<div align="left">

![](chap1-Z-G-98.gif)

</div>

then the action has a value that is independent of the coordinate system
used to compute it. The configuration path of stationary action does not
depend on which coordinate system is used to describe the path. The
Lagrange equations derived from these Lagrangians will in general look
very different from one another, but they must be equivalent.

**Exercise 1.14.**  ****\
 Show by direct calculation that the Lagrange equations for *L*' are
satisfied if the Lagrange equations for *L* are satisfied.

Given a coordinate transformation *F*, we can use
([1.74](#EQUATION_1.74)) to find the function *C* that transforms local
tuples. The procedure `F->C` implements this:[^65^](#footnote_Temp_101)

`(define ((F->C F) local)   (->local (time local)            (F local)            (+ (((partial 0) F) local)               (* (((partial 1) F) local)                   (velocity local))))) `

As an illustration, consider the transformation from polar to
rectangular coordinates, *x* = *r* cos ![](chap1-Z-G-D-16.gif) and *y* =
*r* sin ![](chap1-Z-G-D-16.gif), with the following implementation:

`(define (p->r local)   (let ((polar-tuple (coordinate local)))     (let ((r (ref polar-tuple 0))            (phi (ref polar-tuple 1)))       (let ((x (* r (cos phi)))              (y (* r (sin phi))))         (up x y))))) `

In terms of the polar coordinates and the rates of change of the polar
coordinates, the rates of change of the rectangular components are

`(show-expression   (velocity   ((F->C p->r)    (->local 't (up 'r 'phi) (up 'rdot 'phidot))))) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-99.gif)

</div>

------------------------------------------------------------------------

We can use `F->C` to find the Lagrangian for central force motion in
polar coordinates from the Lagrangian in rectangular components, using
equation ([1.70](#EQUATION_1.70)):

`(define (L-central-polar m U)   (compose (L-central-rectangular m U) (F->C p->r)))  (show-expression   ((L-central-polar 'm (literal-function 'U))    (->local 't (up 'r 'phi) (up 'rdot 'phidot)))) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-100.gif)

</div>

------------------------------------------------------------------------

The result is the same as Lagrangian ([1.67](#EQUATION_1.67)).

**Exercise 1.15.**  **Central force motion**\
 Find Lagrangians for central force motion in three dimensions in
rectangular coordinates and in spherical coordinates. First, find the
Lagrangians analytically, then check the results with the computer by
generalizing the programs that we have presented.

### [1.6.2  Systems with Rigid Constraints](book-Z-H-4.html#%_toc_%_sec_1.6.2)

We have found that *L* = *T* `-` *V* is a suitable Lagrangian for a
system of point particles subject to forces derived from a potential.
Extended bodies can sometimes be conveniently idealized as a system of
point particles connected by rigid constraints. We will find that *L* =
*T* `-` *V*, expressed in irredundant coordinates, is a suitable
Lagrangian for modeling systems of point particles with rigid
constraints. We will first illustrate the method and then provide a
justification.

#### [Lagrangians for rigidly constrained systems](book-Z-H-4.html#%_toc_%_sec_Temp_103)

The system is presumed to be made of *N* point masses, indexed
by ![](chap1-Z-G-D-21.gif), in ordinary three-dimensional space. The
first step is to choose a convenient set of irredundant generalized
coordinates *q* and redescribe the system in terms of these. In terms of
the generalized coordinates the rectangular coordinates of particle
![](chap1-Z-G-D-21.gif) are

<div align="left">

![](chap1-Z-G-101.gif)

</div>

For irredundant coordinates *q* all the coordinate constraints are built
into the functions *f*~![](chap1-Z-G-D-21.gif)~. We deduce the
relationship of the generalized velocities *v* to the velocities of the
constituent particles **v**~![](chap1-Z-G-D-21.gif)~ by inserting path
functions into equation ([1.76](#EQUATION_1.76)), differentiating, and
abstracting to arbitrary velocities.[^66^](#footnote_Temp_104) We find

<div align="left">

![](chap1-Z-G-102.gif)

</div>

We use equations ([1.76](#EQUATION_1.76)) and ([1.77](#EQUATION_1.77))
to express the kinetic energy in terms of the generalized coordinates
and velocities. Let ![](chap1-Z-G-D-35.gif) be the kinetic energy as a
function of the rectangular coordinates and velocities:

<div align="left">

![](chap1-Z-G-103.gif)

</div>

where **v**^2^~![](chap1-Z-G-D-21.gif)~ is the squared magnitude of
**v**~![](chap1-Z-G-D-21.gif)~. As a function of the generalized
coordinate tuple *q* and the generalized velocity tuple *v*, the kinetic
energy is

<div align="left">

![](chap1-Z-G-104.gif)

</div>

Similarly, we use equation ([1.76](#EQUATION_1.76)) to reexpress the
potential energy in terms of the generalized coordinates. Let
![](chap1-Z-G-D-36.gif)(*t*, *x*) be the potential energy at time *t* in
the configuration specified by the tuple of rectangular coordinates *x*.
Expressed in generalized coordinates the potential energy is

<div align="left">

![](chap1-Z-G-105.gif)

</div>

We take the Lagrangian to be the difference of the kinetic energy and
the potential energy: *L* = *T* `-` *V*.

#### [A pendulum driven at the pivot](book-Z-H-4.html#%_toc_%_sec_Temp_105)

Consider a pendulum (see figure [1.2](#FIGURE_1.2)) of length *l* and
mass *m*, modeled as a point mass, supported by a pivot that is driven
in the vertical direction by a given function of time *y*~*s*~.

<div align="left">

![](chap1-Z-G-106.gif)

</div>

The dimension of the configuration space for this system is one; we
choose ![](chap1-Z-G-D-19.gif), shown in figure [1.2](#FIGURE_1.2), as
the generalized coordinate.

The position of the bob is given, in rectangular coordinates, by

<div align="left">

![](chap1-Z-G-107.gif)

</div>

The velocities are

<div align="left">

![](chap1-Z-G-108.gif)

</div>

obtained by differentiating along a path and abstracting to velocities
at the moment.

The kinetic energy is ![](chap1-Z-G-D-35.gif)(*t*; *x*, *y*; *v*~*x*~,
*v*~*y*~) = (1/2) *m* (*v*~*x*~^2^ + *v*~*y*~^2^). Expressed in
generalized coordinates the kinetic energy is

<div align="left">

![](chap1-Z-G-109.gif)

</div>

The potential energy is ![](chap1-Z-G-D-36.gif)(*t*; *x*, *y*) = *mgy*.
Expressed in generalized coordinates the potential energy is

<div align="left">

![](chap1-Z-G-110.gif)

</div>

A Lagrangian is *L* = *T* `-` *V*.

The Lagrangian is expressed as

`(define ((T-pend m l g ys) local)   (let ((t (time local))         (theta (coordinate local))         (thetadot (velocity local)))     (let ((vys (D ys)))       (* 1/2 m          (+ (square (* l thetadot))             (square (vys t))             (* 2 l (vys t) thetadot (sin theta))))))) (define ((V-pend m l g ys) local)   (let ((t (time local))         (theta (coordinate local)))     (* m g (- (ys t) (* l (cos theta))))))  (define L-pend (- T-pend V-pend)) `

Lagrange's equation for this system is[^67^](#footnote_Temp_106)

`(show-expression  (((Lagrange-equations      (L-pend 'm 'l 'g (literal-function 'y_s)))    (literal-function 'theta))   't)) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-111.gif)

</div>

------------------------------------------------------------------------

**Exercise 1.16.**  ****\
 Derive the Lagrangians in exercise [1.9](book-Z-H-12.html#%_thm_1.9).

**Exercise 1.17.**  **Bead on a helical wire**\
 A bead of mass *m* is constrained to move on a frictionless helical
wire. The helix is oriented so that its axis is horizontal. The diameter
of the helix is *d* and its pitch (turns per unit length) is *h*. The
system is in a uniform gravitational field with vertical acceleration
*g*. Formulate a Lagrangian that describes the system and find the
Lagrange equations of motion.

**Exercise 1.18.**  **Bead on a triaxial surface**\
 A bead of mass *m* moves without friction on a triaxial ellipsoidal
surface. In rectangular coordinates the surface satisfies

<div align="left">

![](chap1-Z-G-112.gif)

</div>

for some constants *a*, *b*, and *c*. Identify suitable generalized
coordinates, formulate a Lagrangian, and find Lagrange's equations.

**Exercise 1.19.**  **A two-bar linkage**\
 The two-bar linkage shown in figure [1.3](#FIGURE_1.3) is constrained
to move in the plane. It is composed of three small massive bodies
interconnected by two massless rigid rods in a uniform gravitational
field with vertical acceleration *g*. The rods are pinned to the central
body by a hinge that allows the linkage to fold. The system is arranged
so that the hinge is completely free: the members can go through all
configurations without collision. Formulate a Lagrangian that describes
the system and find the Lagrange equations of motion. Use the computer
to do this, because the equations are rather big.

<div align="left">

![](chap1-Z-G-113.gif)

</div>

**Exercise 1.20.**  **Sliding pendulum**\
 Consider a pendulum of length *l* attached to a support that is free to
move horizontally, as shown in figure [1.4](#FIGURE_1.4). Let the mass
of the support be *m*~1~ and the mass of the pendulum be *m*~2~.
Formulate a Lagrangian and derive Lagrange's equations for this system.

<div align="left">

![](chap1-Z-G-114.gif)

</div>

#### [Why it works](book-Z-H-4.html#%_toc_%_sec_Temp_112)

In this section we show that *L* = *T* `-` *V* is in fact a suitable
Lagrangian for rigidly constrained systems. We do this by requiring that
the Lagrange equations be equivalent to the Newtonian vectorial dynamics
with vector constraint forces.[^68^](#footnote_Temp_113)

We consider a system of particles. The particle with index
![](chap1-Z-G-D-21.gif) has mass *m*~![](chap1-Z-G-D-21.gif)~ and
position ![](chap1-Z-G-D-26.gif)~![](chap1-Z-G-D-21.gif)~(*t*) at time
*t*. There may be a very large number of these particles, or just a few.
Some of the positions may also be specified functions of time, such as
the position of the pivot of a driven pendulum. There are rigid position
constraints among some of the particles. We assume that all of these
constraints are of the form

<div align="left">

![](chap1-Z-G-115.gif)

</div>

that is, the distance between particles ![](chap1-Z-G-D-21.gif) and *ß*
is *l*~![](chap1-Z-G-D-21.gif)*ß*~.

The Newtonian equation of motion for particle ![](chap1-Z-G-D-21.gif)
says that the mass times the acceleration of particle
![](chap1-Z-G-D-21.gif) is equal to the sum of the potential forces and
the constraint forces. The potential forces are derived as the negative
gradient of the potential energy, and may depend on the positions of the
other particles and the time. The constraint forces
![](chap1-Z-G-D-24.gif)~![](chap1-Z-G-D-21.gif)*ß*~ are the vector
constraint forces associated with the rigid constraint between particle
![](chap1-Z-G-D-21.gif) and particle *ß*. So

<div align="left">

![](chap1-Z-G-116.gif)

</div>

where in the summation *ß* ranges over only those particle indices for
which there are rigid constraints with the particle indexed
by ![](chap1-Z-G-D-21.gif); we use the notation *ß* \<--\>
![](chap1-Z-G-D-21.gif) for the relation that there is a rigid
constraint between the indicated particles.

The force of constraint is directed along the line between the
particles, so we may write

<div align="left">

![](chap1-Z-G-117.gif)

</div>

where *F*~![](chap1-Z-G-D-21.gif)*ß*~(*t*) is the scalar magnitude of
the tension in the constraint at time *t*. Note that
![](chap1-Z-G-D-24.gif)~![](chap1-Z-G-D-21.gif)*ß*~ = `-`
![](chap1-Z-G-D-24.gif)~*ß*![](chap1-Z-G-D-21.gif)~. In general, the
scalar constraint forces change as the system evolves.

Formally, we can reproduce Newton's equations with the
Lagrangian[^69^](#footnote_Temp_114)

<div align="left">

![](chap1-Z-G-118.gif)

</div>

where the constraint forces are being treated as additional generalized
coordinates. Here *x* is a structure composed of all the rectangular
components **x**~![](chap1-Z-G-D-21.gif)~ of all the
![](chap1-Z-G-D-26.gif)~![](chap1-Z-G-D-21.gif)~,
![](chap1-Z-G-D-37.gif) is a structure composed of all the rectangular
components ![](chap1-Z-G-D-38.gif)~![](chap1-Z-G-D-21.gif)~ of all the
velocity vectors ![](chap1-Z-G-D-10.gif)~![](chap1-Z-G-D-21.gif)~, and
*F* is a structure composed of all the *F*~![](chap1-Z-G-D-21.gif)*ß*~.
The velocity of *F* does not appear in the Lagrangian, and *F* itself
appears only linearly. So the Lagrange equations associated with *F* are

<div align="left">

![](chap1-Z-G-119.gif)

</div>

but this is just a restatement of the constraints. The Lagrange
equations for the coordinates of the particles are Newton's
equations ([1.87](#EQUATION_1.87))

<div align="left">

![](chap1-Z-G-120.gif)

</div>

Now that we have a suitable Lagrangian, we can use the fact that
Lagrangians can be reexpressed in any generalized coordinates to find a
simpler Lagrangian. The strategy is to choose a new set of coordinates
for which many of the coordinates are constants and the remaining
coordinates are irredundant.

Let *q* be a tuple of generalized coordinates that specify the degrees
of freedom of the system without redundancy. Let *c* be a tuple of other
generalized coordinates that specify the distances between particles for
which constraints are specified. The *c* coordinates will have constant
values. The combination of *q* and *c* replaces the redundant
rectangular coordinates *x*.[^70^](#footnote_Temp_115) In addition, we
still have the *F* coordinates, which are the scalar constraint forces.
Our new coordinates are the components of *q*, *c*, and *F*.

There exist functions *f*~![](chap1-Z-G-D-21.gif)~ that give the
rectangular coordinates of the constituent particles in terms of *q* and
*c*:

<div align="left">

![](chap1-Z-G-121.gif)

</div>

To reexpress the Lagrangian in terms of *q*, *c*, and *F*, we need to
find **v**~![](chap1-Z-G-D-21.gif)~ in terms of the generalized
velocities ![](front-Z-G-D-1.gif) and ![](chap1-Z-G-D-39.gif): we do
this by differentiating *f*~![](chap1-Z-G-D-21.gif)~ along a path and
abstracting to arbitrary velocities (see section [1.6.1](#%_sec_1.6.1)):

<div align="left">

![](chap1-Z-G-122.gif)

</div>

Substituting these into Lagrangian ([1.89](#EQUATION_1.89)), and using

<div align="left">

![](chap1-Z-G-123.gif)

</div>

we find

<div align="left">

![](chap1-Z-G-124.gif)

</div>

The Lagrange equations are derived by the usual procedure. Rather than
write out all the gory details, let's think about how it will go.

The Lagrange equations associated with *F* just restate the constraints:

<div align="left">

![](chap1-Z-G-125.gif)

</div>

and consequently we know that along a solution path, *c*(*t*) = *l* and
*Dc*(*t*) = *D*^2^*c*(*t*) = 0. We can use this result to simplify the
Lagrange equations associated with *q* and *c*.

The Lagrange equations associated with *q* are the same as if they were
derived from the Lagrangian[^71^](#footnote_Temp_116)

<div align="left">

![](chap1-Z-G-126.gif)

</div>

but this is exactly *T* `-` *V* where *T* and *V* are computed from the
generalized coordinates *q*, with fixed constraints. Notice that the
constraint forces do not appear in the Lagrange equations for *q*
because in the Lagrange equations they are multiplied by a term that is
identically zero on the solution paths. So the Lagrange equations for
*T* `-` *V* with irredundant generalized coordinates *q* and fixed
constraints are equivalent to Newton's equations with vector constraint
forces.

The Lagrange equations for *c* can be used to find the constraint
forces. The Lagrange equations are a big mess so we will not show them
explicitly, but in general they are equations in *D*^2^*c*, *Dc*, and
*c* that will depend upon *q*, *Dq*, and *F*. The dependence on *F* is
linear, so we can solve for *F* in terms of the solution path *q* and
*Dq*, with *c* = *l* and *Dc* = *D*^2^*c* = 0.

If we are not interested in the constraint forces, we can abandon the
full Lagrangian ([1.95](#EQUATION_1.95)) in favor of
Lagrangian ([1.97](#EQUATION_1.97)), which is equivalent as far as the
evolution of the generalized coordinates *q* is concerned.

The same derivation goes through even if the lengths
*l*~![](chap1-Z-G-D-21.gif)*ß*~ specified in the interparticle distance
constraints are a function of time. It can also be generalized to allow
distance constraints to time-dependent positions, by making some of the
positions of particles ![](chap1-Z-G-D-26.gif)~*ß*~ be specified
functions of time.

#### [More generally](book-Z-H-4.html#%_toc_%_sec_Temp_117)

Consider a constraint of the form

<div align="left">

![](chap1-Z-G-127.gif)

</div>

where *x*(*t*) is the structure of all the rectangular components
***x***~![](chap1-Z-G-D-21.gif)~(*t*) at time *t*. In
section [1.10](book-Z-H-17.html#%_sec_1.10) we will show, using the
variational principle, that an appropriate Lagrangian for this system is

<div align="left">

![](chap1-Z-G-128.gif)

</div>

where ![](chap1-Z-G-D-40.gif) is an additional coordinate and
![](chap1-Z-G-D-41.gif) is the corresponding generalized velocity. The
Lagrange equations associated with ![](chap1-Z-G-D-40.gif) are just a
restatement of the constraints: ![](chap1-Z-G-D-16.gif)(*t*, *x*(*t*)) =
0 . The Lagrange equations for the particle coordinates are

<div align="left">

![](chap1-Z-G-129.gif)

</div>

Such a constraint can also be modeled by including appropriate
constraint forces in Newton's equations:

<div align="left">

![](chap1-Z-G-130.gif)

</div>

For equations ([1.100](#EQUATION_1.100)) to be the same as
equations ([1.101](#EQUATION_1.101)) we must identify
![](chap1-Z-G-D-40.gif)(*t*)
![](front-Z-G-D-2.gif)~1,![](chap1-Z-G-D-21.gif)~
![](chap1-Z-G-D-16.gif)(*t*, *x*(*t*)) with the forces of constraint on
particle ![](chap1-Z-G-D-21.gif). Notice that these forces of constraint
are proportional to the normal to the constraint surface at each instant
and thus do no work for motions that obey the constraint.
Lagrangian ([1.89](#EQUATION_1.89)), which we developed above to include
Newtonian forces of constraint for position constraints, is of exactly
this form. We can identify

<div align="left">

![](chap1-Z-G-131.gif)

</div>

The forces of constraint satisfy

<div align="left">

![](chap1-Z-G-132.gif)

</div>

Accepting Lagrangian ([1.99](#EQUATION_1.99)) as describing systems with
constraints of the form ([1.98](#EQUATION_1.98)), we can make a
coordinate transformation from the redundant coordinates *x* to
irredundant generalized coordinates *q* and constraint coordinates *c* =
![](chap1-Z-G-D-16.gif)(*t*,*x*), as above. The coordinate
![](chap1-Z-G-D-40.gif) will not appear in the Lagrange equations for
*q* because on solution paths they will be multiplied by a factor that
is identically zero. If we are interested only in the evolution of the
generalized coordinates, we can assume the constraints are identically
satisfied and take the Lagrangian to be the difference of the kinetic
and potential energies expressed in terms of the generalized
coordinates.

<div align="left">

![](chap1-Z-G-133.gif)

</div>

**Exercise 1.21.**  **The dumbbell**\
 In this exercise we will recapitulate the derivation of the Lagrangian
for constrained systems for a particular simple system.

Consider two massive particles in the plane constrained by a massless
rigid rod to remain a distance *l* apart, as in
figure [1.5](#FIGURE_1.5). There are apparently four degrees of freedom
for two massive particles in the plane, but the rigid rod reduces this
number to three.

We can uniquely specify the configuration with the redundant coordinates
of the particles, say *x*~0~(*t*), *y*~0~(*t*) and *x*~1~(*t*),
*y*~1~(*t*). The constraint (*x*~1~(*t*) `-` *x*~0~(*t*))^2^ +
(*y*~1~(*t*) `-` *y*~0~(*t*))^2^ = *l*^2^ eliminates one degree of
freedom.

**a**.  Write Newton's equations for the balance of forces for the four
rectangular coordinates of the two particles, given that the scalar
tension in the rod is *F*.

**b**.  Write the formal Lagrangian

<div align="left">

![](chap1-Z-G-134.gif)

</div>

such that Lagrange's equations will yield the Newton's equations you
derived in part **a**.

**c**.  Make a change of coordinates to a coordinate system with center
of mass coordinates *x*~*cm*~, *y*~*cm*~, angle ![](chap1-Z-G-D-19.gif),
distance between the particles *c*, and tension force *F*. Write the
Lagrangian in these coordinates, and write the Lagrange equations.

**d**.  You may deduce from one of these equations that *c*(*t*) = *l*.
From this fact we get that *Dc* = 0 and *D*^2^*c* = 0. Substitute these
into the Lagrange equations you just computed to get the equation of
motion for *x*~*cm*~, *y*~*cm*~, ![](chap1-Z-G-D-19.gif).

**e**.  Make a Lagrangian ( = *T* `-` *V*) for the system described with
the irredundant generalized coordinates *x*~*cm*~, *y*~*cm*~,
![](chap1-Z-G-D-19.gif) and compute the Lagrange equations from this
Lagrangian. They should be the same equations as you derived for the
same coordinates in part **d**.

**Exercise 1.22.**  **Driven pendulum**\
 Show that the Lagrangian ([1.89](#EQUATION_1.89)) can be used to
describe the driven pendulum, where the position of the pivot is a
specified function of time: Derive the equations of motion using the
Newtonian constraint force prescription, and show that they are the same
as the Lagrange equations. Be sure to examine the equations for the
constraint forces as well as the position of the pendulum bob.

**Exercise 1.23.**  **Fill in the details**\
 Show that the Lagrange equations for
Lagrangian ([1.97](#EQUATION_1.97)) are the same as the Lagrange
equations for Lagrangian ([1.95](#EQUATION_1.95)) with the substitution
*c*(*t*) = *l*, *Dc*(*t*) = *D*^2^*c*(*t*) = 0.

**Exercise 1.24.**  **Constraint forces**\
 Find the tension in an undriven planar pendulum.

### [1.6.3  Constraints as Coordinate Transformations](book-Z-H-4.html#%_toc_%_sec_1.6.3)

The derivation of a Lagrangian for a constrained system involves steps
that are analogous to those in the derivation of a coordinate
transformation.

For a constrained system we specify the rectangular coordinates of the
constituent particles in terms of generalized coordinates that
incorporate the constraints. We then determine the rectangular
velocities of the constituent particles as functions of the generalized
coordinates and the generalized velocities. The Lagrangian that we know
how to express in rectangular coordinates and velocities of the
constituent particles can then be reexpressed in terms of the
generalized coordinates and velocities.

To carry out a coordinate transformation one specifies how the
configuration of a system expressed in one set of generalized
coordinates can be reexpressed in terms of another set of generalized
coordinates. We then determine the transformation of generalized
velocities implied by the transformation of generalized coordinates. A
Lagrangian that is expressed in terms of one of the sets of generalized
coordinates can then be reexpressed in terms of the other set of
generalized coordinates.

These are really two applications of the same process, so we can make
Lagrangians for constrained systems by composing a Lagrangian for
unconstrained particles with a coordinate transformation that
incorporates the constraint. Our deduction that *L* = *T* `-` *V* is a
suitable Lagrangian for a constrained systems was in fact based on a
coordinate transformation from a set of coordinates subject to
constraints to a set of irredundant coordinates plus constraint
coordinates that are constant.

Let ***x***~![](chap1-Z-G-D-21.gif)~ be the tuple of rectangular
components of the constituent particle with index
![](chap1-Z-G-D-21.gif), and let ***v***~![](chap1-Z-G-D-21.gif)~ be its
velocity. The Lagrangian

<div align="left">

![](chap1-Z-G-135.gif)

</div>

is the difference of kinetic and potential energies of the constituent
particles. This is a suitable Lagrangian for a set of unconstrained free
particles with potential energy *V*.

Let *q* be a tuple of irredundant generalized coordinates and *v* be the
corresponding generalized velocity tuple. The coordinates *q* are
related to ***x***~![](chap1-Z-G-D-21.gif)~, the coordinates of the
constituent particles, by ***x***~![](chap1-Z-G-D-21.gif)~ =
*f*~![](chap1-Z-G-D-21.gif)~(*t*, *q*), as before. The constraints among
the constituent particles are taken into account in the definition of
the *f*~![](chap1-Z-G-D-21.gif)~. Here we view this as a coordinate
transformation. What is unusual about this as a coordinate
transformation is that the dimension of *x* is not the same as the
dimension of *q*. From this coordinate transformation we can find the
local-tuple transformation function (see section [1.6.1](#%_sec_1.6.1))

<div align="left">

![](chap1-Z-G-136.gif)

</div>

A Lagrangian for the constrained system can be obtained from the
Lagrangian for the unconstrained system by composing it with the
local-tuple transformation function from constrained coordinates to
unconstrained coordinates:

<div align="left">

![](chap1-Z-G-137.gif)

</div>

The constraints enter only in the transformation.

To illustrate this we will find a Lagrangian for the driven pendulum
introduced in section [1.6.2](#%_sec_1.6.2). The *T* `-` *V* Lagrangian
for a free particle of mass *m* in a vertical plane subject to a
gravitational potential with acceleration *g* is

<div align="left">

![](chap1-Z-G-138.gif)

</div>

where *y* measures the vertical height of the point mass. A program that
computes this Lagrangian is

`(define ((L-uniform-acceleration m g) local)   (let ((q (coordinate local))         (v (velocity local)))     (let ((y (ref q 1)))       (- (* 1/2 m (square v)) (* m g y))))) `

The coordinate transformation from generalized coordinate
![](chap1-Z-G-D-19.gif) to rectangular coordinates is *x* = *l* sin
![](chap1-Z-G-D-19.gif), *y* = *y*~*s*~(*t*) `-` *l* cos
![](chap1-Z-G-D-19.gif), where *l* is the length of the pendulum and
*y*~*s*~ gives the height of the support as a function of time. It is
interesting that the drive enters only through the specification of the
constraints. A program implementing this coordinate transformation is

`(define ((dp-coordinates l y_s) local)   (let ((t (time local))         (theta (coordinate local)))     (let ((x (* l (sin theta)))           (y (- (y_s t) (* l (cos theta)))))       (up x y)))) `

Using `F->C` we can deduce the local-tuple transformation and define the
Lagrangian for the driven pendulum by composition:

`(define (L-pend m l g y_s)   (compose (L-uniform-acceleration m g)             (F->C (dp-coordinates l y_s)))) `

The Lagrangian is

`(show-expression  ((L-pend 'm 'l 'g (literal-function 'y_s))   (->local 't 'theta 'thetadot))) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-139.gif)

</div>

------------------------------------------------------------------------

This is the same as the Lagrangian found in
section [1.6.2](#%_sec_1.6.2).

We have found a very interesting decomposition of the Lagrangian for
constrained systems. One part consists of the difference of the kinetic
and potential energy of the constituents. The other part describes the
constraints that are specific to the configuration of a particular
system.

### [1.6.4  The Lagrangian Is Not Unique](book-Z-H-4.html#%_toc_%_sec_1.6.4)

Lagrangians are not in a one-to-one relationship with physical
systems -- many Lagrangians can be used to describe the same physical
system. In this section we will demonstrate this by showing that the
addition to the Lagrangian of a \`\`total time derivative'' of a
function of the coordinates and time does not change the paths of
stationary action or the equations of motion deduced from the action
principle.

#### [Total time derivatives](book-Z-H-4.html#%_toc_%_sec_Temp_122)

Let's first explain what we mean by a \`\`total time derivative.'' Let
*F* be a function of time and coordinates. Then the time derivative of
*F* along a path *q* is

<div align="left">

![](chap1-Z-G-140.gif)

</div>

Because *F* depends only on time and coordinates, we have

<div align="left">

![](chap1-Z-G-141.gif)

</div>

So we only need the first two components of
*D*![](chap1-Z-G-D-9.gif)[*q*],

<div align="left">

![](chap1-Z-G-142.gif)

</div>

to form the product

<div align="left">

![](chap1-Z-G-143.gif)

</div>

where ![](chap1-Z-G-D-42.gif) = *I*~2~ is a selector
function:[^72^](#footnote_Temp_123) *c* = ![](chap1-Z-G-D-42.gif)(*a*,
*b*, *c*), so *Dq* = ![](chap1-Z-G-D-42.gif) o
![](chap1-Z-G-D-9.gif)[*q*]. The function

<div align="left">

![](chap1-Z-G-144.gif)

</div>

is called the total time derivative of *F*; it is a function of three
arguments: the time, the generalized coordinates, and the generalized
velocities.

In general, the *total time derivative* of a local-tuple function *F* is
that function *D*~*t*~ *F* that when composed with a local-tuple path is
the time derivative of the composition of the function *F* with the same
local-tuple path:

<div align="left">

![](chap1-Z-G-145.gif)

</div>

The total time derivative *D*~*t*~ *F* is explicitly given by

<div align="left">

![](chap1-Z-G-146.gif)

</div>

where we take as many terms as needed to exhaust the arguments of *F*.

**Exercise 1.25.**  **Properties of *D*~*t*~**\
 The total time derivative *D*~*t*~ *F* is not the derivative of the
function *F*. Nevertheless, the total time derivative shares many
properties with the derivative. Demonstrate that *D*~*t*~ has the
following properties for local-tuple functions *F* and *G*, number *c*,
and a function *H* with domain containing the range of *G*.

**a**.  *D*~*t*~ (*F* + *G*) = *D*~*t*~ *F* + *D*~*t*~ *G*

**b**.  *D*~*t*~ (*cF*) = *c* *D*~*t*~ *F*

**c**.  *D*~*t*~ (*F* *G*) = *F* *D*~*t*~ *G* + (*D*~*t*~ *F*) *G*

**d**.  *D*~*t*~ (*H* o *G*) = (*D* *H* o *G* ) *D*~*t*~ *G*

#### [Adding total time derivatives to Lagrangians](book-Z-H-4.html#%_toc_%_sec_Temp_125)

Consider two Lagrangians *L* and *L*' that differ by the addition of a
total time derivative of a function *F* that depends only on the time
and the coordinates

<div align="left">

![](chap1-Z-G-147.gif)

</div>

The corresponding action integral is

<div align="left">

![](chap1-Z-G-148.gif)

</div>

The variational principle states that the action integral along a
realizable trajectory is stationary with respect to variations of the
trajectory that leave the configuration at the endpoints fixed. The
action integrals *S*[*q*](*t*~1~, *t*~2~) and *S*^/^[*q*](*t*~1~,
*t*~2~) differ by a term

<div align="left">

![](chap1-Z-G-149.gif)

</div>

that depends only on the coordinates and time at the endpoints and these
are not allowed to vary. Thus, if *S*[*q*](*t*~1~, *t*~2~) is stationary
for a path, then *S*^/^[*q*](*t*~1~, *t*~2~) will also be stationary. So
either Lagrangian can be used to distinguish the realizable paths.

The addition of a total time derivative to a Lagrangian does not affect
whether the action is critical for a given path. So if we have two
Lagrangians that differ by a total time derivative, the corresponding
Lagrange equations are equivalent in that the same paths satisfy each.
Moreover, the additional terms introduced into the action by the total
time derivative appear only in the endpoint condition and thus do not
affect the Lagrange equations derived from the variation of the action,
so the Lagrange equations are the same. So the Lagrange equations are
not changed by the addition of a total time derivative to a Lagrangian.

**Exercise 1.26.**  **Lagrange equations for total time derivatives**\
 Let *F*(*t*, *q*) be a function of *t* and *q* only, with total time
derivative

<div align="left">

![](chap1-Z-G-150.gif)

</div>

Show explicitly that the Lagrange equations for *D*~*t*~ *F* are
identically zero, and thus that the addition of *D*~*t*~ *F* to a
Lagrangian does not affect the Lagrange equations.

The driven pendulum provides a nice illustration of adding total time
derivatives to Lagrangians. The equation of motion for the driven
pendulum (see section [1.6.2](#%_sec_1.6.2)),

<div align="left">

![](chap1-Z-G-151.gif)

</div>

has an interesting and suggestive interpretation: it is the same as the
equation of motion of an undriven pendulum, except that the acceleration
of gravity *g* is augmented by the acceleration of the pivot *D*^2^
*y*~*s*~. This intuitive interpretation was not apparent in the
Lagrangian derived as the difference of the kinetic and potential
energies in section [1.6.2](#%_sec_1.6.2). However, we can write an
alternate Lagrangian with the same equation of motion that is as easy to
interpret as the equation of motion:

<div align="left">

![](chap1-Z-G-152.gif)

</div>

With this Lagrangian it is apparent that the effect of the accelerating
pivot is to modify the acceleration of gravity. Note, however, that it
is not the difference of the kinetic and potential energies. Let's
compare the two Lagrangians for the driven pendulum. The difference
![](chap1-Z-G-D-43.gif) *L* = *L* `-` *L*^/^ is

<div align="left">

![](chap1-Z-G-153.gif)

</div>

The two terms in ![](chap1-Z-G-D-43.gif) *L* that depend on neither
![](chap1-Z-G-D-19.gif) nor ![](chap1-Z-G-D-20.gif) do not affect the
equations of motion. The remaining two terms are the total time
derivative of the function *F*(*t*, ![](chap1-Z-G-D-19.gif)) = `-` *m*
*l* *Dy*~*s*~(*t*) cos ![](chap1-Z-G-D-19.gif), which does not depend on
![](chap1-Z-G-D-20.gif). The addition of such terms to a Lagrangian does
not affect the equations of motion.

#### [Identification of total time derivatives](book-Z-H-4.html#%_toc_%_sec_Temp_127)

If the local-tuple function *G*, with arguments (*t*, *q*, *v*), is the
total time derivative of a function *F*, with arguments (*t*, *q*), then
*G* must have certain properties.

From equation ([1.112](#EQUATION_1.112)), we see that *G* must be linear
in the generalized velocities

<div align="left">

![](chap1-Z-G-154.gif)

</div>

where neither *G*~1~ nor *G*~0~ depend on the generalized velocities:
![](front-Z-G-D-2.gif)~2~ *G*~1~ = ![](front-Z-G-D-2.gif)~2~ *G*~0~ = 0.

If *G* is the total time derivative of *F* then *G*~1~ =
![](front-Z-G-D-2.gif)~1~ *F* and *G*~0~ = ![](front-Z-G-D-2.gif)~0~
*F*, so

<div align="left">

![](chap1-Z-G-155.gif)

</div>

The partial derivative with respect to the time argument does not have
structure, so ![](front-Z-G-D-2.gif)~0~ ![](front-Z-G-D-2.gif)~1~ *F* =
![](front-Z-G-D-2.gif)~1~ ![](front-Z-G-D-2.gif)~0~ *F*. So if *G* is
the total time derivative of *F* then

<div align="left">

![](chap1-Z-G-156.gif)

</div>

Furthermore, *G*~1~ = ![](front-Z-G-D-2.gif)~1~ *F*, so

<div align="left">

![](chap1-Z-G-157.gif)

</div>

If there is more than one degree of freedom these partials are actually
structures of partial derivatives with respect to each coordinate. The
partial derivatives with respect to two different coordinates must be
the same independent of the order of the differentiation. So
![](front-Z-G-D-2.gif)~1~ *G*~1~ must be symmetric.

Note that we have not shown that these conditions are sufficient for
determining that a function is a total time derivative, only that they
are necessary.

**Exercise 1.27.**  **Identifying total time derivatives**\

For each of the following functions, either show that it is not a total
time derivative or produce a function from which it can be derived.

**a**.  *G*(*t*, *x*, *v*~*x*~) = *m* *v*~*x*~

**b**.  *G*(*t*, *x*, *v*~*x*~) = *m* *v*~*x*~ cos *t*

**c**.  *G*(*t*, *x*, *v*~*x*~) = *v*~*x*~ cos *t* `-` *x* sin *t*

**d**.  *G*(*t*, *x*, *v*~*x*~) = *v*~*x*~ cos *t* + *x* sin *t*

**e**.  *G*(*t*; *x*, *y*; *v*~*x*~, *v*~*y*~) = 2 (*x* *v*~*x*~ + *y*
*v*~*y*~) cos *t* `-` (*x*^2^ + *y*^2^) sin *t*

**f**.  *G*(*t*; *x*, *y*; *v*~*x*~, *v*~*y*~) = 2 (*x* *v*~*x*~ + *y*
*v*~*y*~) cos *t* `-` (*x*^2^ + *y*^2^) sin *t* + *y*^3^ *v*~*x*~ + *x*
*v*~*y*~

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^61^](#call_footnote_Temp_92) Remember that *x* and *v* are just formal
parameters of the Lagrangian. This *x* is not the path *x* used earlier
in the derivation, though it could be the value of that path at a
particular time.

[^62^](#call_footnote_Temp_93) We can always give a function extra
arguments that are not used so that it can be algebraically combined
with other functions of the same shape.

[^63^](#call_footnote_Temp_95) Hamilton formulated the fundamental
variational principle for time-independent systems in 1834-1835. Jacobi
gave this principle the name \`\`Hamilton's principle.'' For systems
subject to generic, nonstationary constraints Hamilton's principle was
investigated in 1848 by Ostrogradsky, and in the Russian literature
Hamilton's principle is often called the Hamilton-Ostrogradsky
principle.

William Rowan Hamilton (1805-1865) was a brilliant mathematician. His
early work on geometric optics (based on Fermat's principle) was so
impressive that he was elected to the post of Professor of Astronomy at
Trinity College and Royal Astronomer of Ireland while he was still an
undergraduate. He produced two monumental works of mathematics. His
discovery of quaternions revitalized abstract algebra and sparked the
development of vector techniques in physics. His 1835 memoir \`\`On a
General Method in Dynamics'' put variational mechanics on a firm
footing, finally giving substance to Maupertuis's vaguely stated
Principle of Least Action of 100 years before. Hamilton also wrote
poetry and carried on an extensive correspondence with Wordsworth, who
advised him to put his energy into writing mathematics rather than
poetry.

In addition to the formulation of the fundamental variational principle,
Hamilton also emphasized the analogy between geometric optics and
mechanics, and stressed the importance of the momentum variables (which
were earlier introduced by Lagrange and Cauchy), leading to the
\`\`canonical'' form of mechanics discussed in
chapter [3](book-Z-H-36.html#%_chap_3).

[^64^](#call_footnote_Temp_97) When applied to a tuple, `square` means
the the sum of the squares of the components of the tuple.

[^65^](#call_footnote_Temp_101) As described in
footnote [28](book-Z-H-11.html#footnote_Temp_41) above, the procedure
`->local` constructs a local tuple from an initial segment of time,
coordinates, and velocities.

[^66^](#call_footnote_Temp_104) See section [1.6.1](#%_sec_1.6.1).

[^67^](#call_footnote_Temp_106) We hope you appreciate the TEX magic
here. A symbol with an underline character is converted by
`show-expression` to a subscript. Symbols with carets, the names of
Greek letters, and those terminating in the characters \`\`dot'' are
similarly mistreated.

[^68^](#call_footnote_Temp_113) We will simply accept the Newtonian
procedure for systems with rigid constraints and find Lagrangians that
are equivalent. Of course, actual bodies are never truly rigid, so we
may wonder what detailed approximations have to be made to treat them as
if they were truly rigid. For instance, a more satisfying approach would
be to replace the rigid distance constraints by very stiff springs. We
could then immediately write the Lagrangian as *L* = *T* `-` *V*, and we
should be able to *derive* the Newtonian procedure for systems with
rigid constraints as an approximation. However, this is too complicated
to do at this stage, so we accept the Newtonian idealization.

[^69^](#call_footnote_Temp_114) This Lagrangian is purely formal and
does not represent a model of the constraint forces. In particular, note
that the constraint terms do not add up to a potential energy with a
minimum when the constraints are exactly satisfied. Rather, the
constraint terms in the Lagrangian are zero when the constraint is
satisfied, and can be either positive or negative depending on whether
the distance between the particles is larger or smaller than the
constraint distance.

[^70^](#call_footnote_Temp_115) Typically the number of components of
*x* is equal to the sum of the number of components of *q* and *c*;
adding a strut removes a degree of freedom and adds a distance
constraint. However, there are singular cases in which the addition of
single strut can remove more than a single degree of freedom. We do not
consider the singular cases here.

[^71^](#call_footnote_Temp_116) Consider a function *g* of, say, three
arguments, and let *g*~0~ be a function of two arguments satisfying
*g*~0~(*x*, *y*) = *g*(*x*, *y*, 0). Then (![](front-Z-G-D-2.gif)~0~
*g*~0~)(*x*, *y*) = (![](front-Z-G-D-2.gif)~0~ *g*)(*x*, *y*, 0). The
substitution of a value in an argument commutes with the taking of the
partial derivative with respect to a different argument. In deriving the
Lagrange equations for *q* we can set *c* = *l* and
![](chap1-Z-G-D-39.gif) = 0 in the Lagrangian, but we cannot do this in
deriving the Lagrange equations associated with *c*, because we have to
take derivatives with respect to those arguments.

[^72^](#call_footnote_Temp_123) Components of a tuple structure, such as
the value of ![](chap1-Z-G-D-9.gif)[*q*](*t*), can be selected with
selector functions: *I*~*i*~ gets the element with index *i* from the
tuple.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-12.html)</span><span>,
[next](book-Z-H-14.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


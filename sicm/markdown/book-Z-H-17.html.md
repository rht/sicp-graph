<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-16.html)</span><span>,
[next](book-Z-H-18.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[1.10  Constrained Motion](book-Z-H-4.html#%_toc_%_sec_1.10)
------------------------------------------------------------

An advantage of the Lagrangian approach is that coordinates can often be
chosen that exactly describe the freedom of the system, automatically
incorporating any constraints. We may also use coordinates that have
more freedom than the system actually has and consider explicit
constraints among the coordinates. For example, the planar pendulum has
a one-dimensional configuration space. We have formulated this problem
using the angle from the vertical as the configuration coordinate.
Alternatively, we may choose to represent the pendulum as a body moving
in the plane, constrained to be on the circle of the correct radius
around the pivot. We would like to have valid descriptions for both
choices and show they are equivalent. In this section we develop tools
to handle problems with explicit constraints. The constraints considered
here are more general than those used in the demonstration that the
Lagrangian for systems with rigid constraints can be written as the
difference of kinetic and potential energies (see
section [1.6.2](book-Z-H-13.html#%_sec_1.6.2)).

Suppose the configuration of a system with *n* degrees of freedom is
specified by *n* + 1 coordinates and that configuration paths *q* are
constrained to satisfy some relation of the form

<div align="left">

![](chap1-Z-G-223.gif)

</div>

How do we formulate the equations of motion? One approach would be to
use the constraint equation to eliminate one of the coordinates in favor
of the rest; then the evolution of the reduced set of generalized
coordinates would be described by the usual Lagrange equations. The
equations governing the evolution of coordinates that are not fully
independent should be equivalent.

We can address the problem of formulating equations of motion for
systems with redundant coordinates by returning to the action principle.
Realizable paths are distinguished from other paths by having stationary
action. Stationary refers to the fact that the action does not change
with certain small variations of the path. What variations should be
considered? We have seen that velocity-independent rigid constraints can
be used to eliminate redundant coordinates. In the irredundant
coordinates we distinguished realizable paths by using variations that
by construction satisfy the constraints. Thus in the case where
constraints can be used to eliminate redundant coordinates we can
restrict the variations in the path to those that are consistent with
the constraints.

So how does the restriction of the possible variations affect the
argument that led to Lagrange's equations (refer to
section [1.5](book-Z-H-12.html#%_sec_1.5))? Actually most of the
calculation is unaffected. The condition that the action is stationary
still reduces to the condition ([1.34](book-Z-H-12.html#EQUATION_1.34)):

<div align="left">

![](chap1-Z-G-224.gif)

</div>

At this point we argued that because the variations
![](chap1-Z-G-D-13.gif) are arbitrary (except for conditions at the
endpoints), the only way for the integral to be zero is for the
integrand to be zero. Furthermore, the freedom in our choice of
![](chap1-Z-G-D-13.gif) allowed us to deduce that the factor multiplying
![](chap1-Z-G-D-13.gif) in the integrand must be identically zero,
thereby deriving Lagrange's equations.

Now the choice of ![](chap1-Z-G-D-13.gif) is not completely free. We can
still deduce from the arbitrariness of ![](chap1-Z-G-D-13.gif) that the
integrand must be zero,[^88^](#footnote_Temp_155) but we can no longer
deduce that the factor multiplying ![](chap1-Z-G-D-13.gif) is zero (only
that the projection of this factor onto acceptable variations is zero).
So we have

<div align="left">

![](chap1-Z-G-225.gif)

</div>

with ![](chap1-Z-G-D-13.gif) subject to the constraints.

A path *q* satisfies the constraint if ![](chap1-Z-G-D-54.gif)[*q*] =
![](chap1-Z-G-D-16.gif) o ![](chap1-Z-G-D-9.gif)[*q*] = 0. The
constraint must be satisfied even for the varied path, so we allow only
variations ![](chap1-Z-G-D-13.gif) for which the variation of the
constraint is zero:

<div align="left">

![](chap1-Z-G-226.gif)

</div>

We can say that the variation must be \`\`tangent'' to the constraint
surface. Expanding this with the chain rule, a variation
![](chap1-Z-G-D-13.gif) is tangent to the constraint surface
![](chap1-Z-G-D-16.gif) if

<div align="left">

![](chap1-Z-G-227.gif)

</div>

Note that these are functions of time; the variation at a given time is
tangent to the constraint at that time.

### [1.10.1  Coordinate Constraints](book-Z-H-4.html#%_toc_%_sec_1.10.1)

Consider constraints that do not depend on velocities:

<div align="left">

![](chap1-Z-G-228.gif)

</div>

In this case the variation is tangent to the constraint surface if

<div align="left">

![](chap1-Z-G-229.gif)

</div>

Together, equations ([1.177](#EQUATION_1.177)) and
([1.180](#EQUATION_1.180)) should determine the motion, but how do we
eliminate ![](chap1-Z-G-D-13.gif)? The residual of the Lagrange
equations is orthogonal[^89^](#footnote_Temp_156) to any
![](chap1-Z-G-D-13.gif) that is orthogonal to the normal to the
constraint surface. A vector that is orthogonal to all vectors
orthogonal to a given vector is parallel to the given vector. Thus, the
residual of Lagrange's equations is parallel to the normal to the
constraint surface; the two must be proportional:

<div align="left">

![](chap1-Z-G-230.gif)

</div>

That the two vectors are parallel everywhere along the path does not
guarantee that the proportionality factor is the same at each moment
along the path, so the proportionality factor ![](chap1-Z-G-D-40.gif) is
some function of time, which may depend on the path under consideration.
These equations, with the constraint equation ![](chap1-Z-G-D-16.gif) o
![](chap1-Z-G-D-9.gif)[*q*] = 0, are the governing equations. These
equations are sufficient to determine the path *q* and to eliminate the
unknown function ![](chap1-Z-G-D-40.gif).

#### [Now watch this](book-Z-H-4.html#%_toc_%_sec_Temp_157)

Suppose we form an augmented Lagrangian treating ![](chap1-Z-G-D-40.gif)
as one of the coordinates:

<div align="left">

![](chap1-Z-G-231.gif)

</div>

The Lagrange equations associated with the coordinates *q* are just the
modified Lagrange equations ([1.181](#EQUATION_1.181)), and the Lagrange
equation associated with ![](chap1-Z-G-D-40.gif) is just the constraint
equation. (Note that ![](chap1-Z-G-D-41.gif) does not appear in the
augmented Lagrangian.) So the Lagrange equations for this augmented
Lagrangian fully encapsulate the modification to the Lagrange equations
that is imposed by the addition of an explicit coordinate constraint, at
the expense of introducing extra degrees of freedom. Notice that this
Lagrangian is of the same form as the Lagrangian
(equation [1.89](book-Z-H-13.html#EQUATION_1.89)) that we used in the
derivation of *L* = *T* `-` *V* for rigid systems
(section [1.6.2](book-Z-H-13.html#%_sec_1.6.2)).

#### [Alternatively](book-Z-H-4.html#%_toc_%_sec_Temp_158)

How do we know that we have enough information to eliminate the unknown
function ![](chap1-Z-G-D-40.gif) from
equations ([1.181](#EQUATION_1.181)), or that the extra degree of
freedom introduced in Lagrangian ([1.182](#EQUATION_1.182)) is purely
formal?

If ![](chap1-Z-G-D-40.gif) could be written as a function of the
solution state path, then it would be clear that it is determined by the
state and can thus be eliminated. Suppose ![](chap1-Z-G-D-40.gif) can be
written as a composition of a state-dependent function with the path:
![](chap1-Z-G-D-40.gif) = ![](chap1-Z-G-D-55.gif) o
![](chap1-Z-G-D-9.gif)[*q*]. Consider the Lagrangian

<div align="left">

![](chap1-Z-G-232.gif)

</div>

This new Lagrangian has no extra degrees of freedom. The Lagrange
equations for *L*'' are the Lagrange equations for *L* with additional
terms arising from the product of ![](chap1-Z-G-D-55.gif)
![](chap1-Z-G-D-16.gif). Applying the Euler-Lagrange operator *E* (see
section [1.9](book-Z-H-16.html#%_sec_1.9)) to this Lagrangian
gives[^90^](#footnote_Temp_159)

<div align="left">

![](chap1-Z-G-234.gif)

</div>

Composition of *E*[*L*''] with ![](chap1-Z-G-D-9.gif)[*q*] gives the
Lagrange equations for the path *q*. Using the fact that the constraint
is satisfied on the path ![](chap1-Z-G-D-16.gif) o
![](chap1-Z-G-D-9.gif)[*q*] = 0 and consequently *D*~*t*~
![](chap1-Z-G-D-16.gif) o ![](chap1-Z-G-D-9.gif)[*q*] = 0, we have

<div align="left">

![](chap1-Z-G-235.gif)

</div>

where we have used ![](chap1-Z-G-D-40.gif) = ![](chap1-Z-G-D-55.gif) o
![](chap1-Z-G-D-9.gif)[*q*]. If we now use the fact that we are dealing
only with coordinate constraints, ![](front-Z-G-D-2.gif)~2~
![](chap1-Z-G-D-16.gif) = 0, then

<div align="left">

![](chap1-Z-G-236.gif)

</div>

The Lagrange equations are the same as those derived from the augmented
Lagrangian *L*'. The difference is that now we see that
![](chap1-Z-G-D-40.gif) = ![](chap1-Z-G-D-55.gif) o
![](chap1-Z-G-D-9.gif)[*q*] is determined by the unaugmented state. This
is the same as saying that ![](chap1-Z-G-D-40.gif) can be eliminated.

Considering only the formal validity of the Lagrange equations for the
augmented Lagrangian, we could not deduce that ![](chap1-Z-G-D-40.gif)
could be written as the composition of a state-dependent function
![](chap1-Z-G-D-55.gif) with ![](chap1-Z-G-D-9.gif)[*q*]. The explicit
Lagrange equations derived from the augmented Lagrangian depend on the
accelerations *D*^2^*q* as well as ![](chap1-Z-G-D-40.gif), so we cannot
deduce separately that either is the composition of a state-dependent
function and ![](chap1-Z-G-D-9.gif)[*q*]. However, now we see that
![](chap1-Z-G-D-40.gif) is such a composition. This allows us to deduce
that *D*^2^*q* is also a state-dependent function composed with the
path. The evolution of the system is determined from the dynamical
state.

<div align="left">

![](chap1-Z-G-237.gif)

</div>

#### [The pendulum using constraints](book-Z-H-4.html#%_toc_%_sec_Temp_160)

The pendulum can be formulated as the motion of a massive particle in a
vertical plane subject to the constraint that the distance to the pivot
is constant (see figure [1.8](#FIGURE_1.8)).

In this formulation, the kinetic and potential energies in the
Lagrangian are those of an unconstrained particle in a uniform
gravitational acceleration. A Lagrangian for the unconstrained particle
is

<div align="left">

![](chap1-Z-G-238.gif)

</div>

The constraint that the pendulum moves in a circle of radius *l* about
the pivot is[^91^](#footnote_Temp_161)

<div align="left">

![](chap1-Z-G-239.gif)

</div>

The augmented Lagrangian is

<div align="left">

![](chap1-Z-G-240.gif)

</div>

The Lagrange equations for the augmented Lagrangian are

<div align="left">

![](chap1-Z-G-241.gif)

</div>

These equations are sufficient to solve for the motion of the pendulum.

It should not be surprising that these equations simplify if we switch
to \`\`polar'' coordinates

<div align="left">

![](chap1-Z-G-242.gif)

</div>

Substituting this into the constraint equation, we determine that *r* =
*l*, a constant. Forming the derivatives and substituting into the other
two equations, we find

<div align="left">

![](chap1-Z-G-243.gif)

</div>

Multiplying the first by cos ![](chap1-Z-G-D-19.gif) and the second by
sin ![](chap1-Z-G-D-19.gif) and adding, we find

<div align="left">

![](chap1-Z-G-244.gif)

</div>

which we recognize as the correct equation for the pendulum. This is the
same as the Lagrange equation for the pendulum using the unconstrained
generalized coordinate ![](chap1-Z-G-D-19.gif). For completeness, we can
find ![](chap1-Z-G-D-40.gif) in terms of the other variables:

<div align="left">

![](chap1-Z-G-245.gif)

</div>

This confirms that ![](chap1-Z-G-D-40.gif) is really the composition of
a function of the state with the state path. Notice that 2 *l*
![](chap1-Z-G-D-40.gif) is a force -- it is the sum of the outward
component of the gravitational force and the centrifugal force. Using
this interpretation in the two coordinate equations of motion, we see
that the terms involving ![](chap1-Z-G-D-40.gif) are the forces that
must be applied to the unconstrained particle to make it move on the
circle required by the constraints. Equivalently, we may think of 2 *l*
![](chap1-Z-G-D-40.gif) as the tension in the pendulum rod that holds
the mass.[^92^](#footnote_Temp_162)

#### [Building systems from parts](book-Z-H-4.html#%_toc_%_sec_Temp_163)

The method of using augmented Lagrangians to enforce constraints on
dynamical systems provides a way to analyze a compound system by
combining the results of the analysis of the parts of the system and the
coupling between them.

Consider the compound spring-mass system shown at the top of
figure [1.9](#FIGURE_1.9). We could analyze this as a monolithic system
with two configuration coordinates *x*~1~ and *x*~2~, representing the
extensions of the springs from their equilibrium lengths *X*~1~ and
*X*~2~.

An alternative procedure is to break the system into several parts. In
our spring-mass system we can choose two parts: one is a spring and mass
attached to the wall, and the other is a spring and mass with its
attachment point at an additional configuration coordinate
![](chap1-Z-G-D-18.gif). We can formulate a Lagrangian for each part
separately. We can then choose a Lagrangian for the composite system as
the sum of the two component Lagrangians with a constraint
![](chap1-Z-G-D-18.gif) = *X*~1~ + *x*~1~ to accomplish the coupling.

<div align="left">

![](chap1-Z-G-246.gif)

</div>

Let's see how this works. The Lagrangian for the subsystem attached to
the wall is

<div align="left">

![](chap1-Z-G-247.gif)

</div>

and the Lagrangian for the subsystem that attaches to it is

<div align="left">

![](chap1-Z-G-248.gif)

</div>

We construct a Lagrangian for the system composed from these parts as a
sum of the Lagrangians for each of the separate parts, with a coupling
term to enforce the constraint:

<div align="left">

![](chap1-Z-G-249.gif)

</div>

Thus we can write Lagrange's equations for the four configuration
coordinates, in order, as follows:

<div align="left">

![](chap1-Z-G-250.gif)

</div>

Notice that in this system ![](chap1-Z-G-D-40.gif) is the force of
constraint holding the system together. We can now eliminate the
\`\`glue'' coordinates ![](chap1-Z-G-D-18.gif) and
![](chap1-Z-G-D-40.gif) to obtain the equations of motion in the
coordinates *x*~1~ and *x*~2~:

<div align="left">

![](chap1-Z-G-251.gif)

</div>

This strategy can be generalized. We can make a library of primitive
components. Each component may be characterized by a Lagrangian with
additional degrees of freedom for the *terminals* where that component
may be attached to others. We then can construct composite Lagrangians
by combining components, using constraints to glue together the
terminals.

**Exercise 1.34.**  **Combining Lagrangians**\
\
**a**.  Make another primitive component, compatible with the
spring-mass structures described in this section. For example, make a
pendulum that can attach to the spring-mass system. Build a combination
and derive the equations of motion. Be careful, the algebra is horrible
if you choose bad coordinates.

**b**.  For a nice little project, construct a family of compatible
mechanical parts, characterized by appropriate Lagrangians, that can be
combined in a variety of ways to make interesting mechanisms. Remember
that in a good language the result of combining pieces should be a piece
of the same kind that can be further combined with other pieces.

**Exercise 1.35.**  **Bead on a triaxial surface**\
 Consider again the motion of a bead constrained to move on a triaxial
surface (exercise [1.18](book-Z-H-13.html#%_thm_1.18)). Reformulate this
using rectangular coordinates as the generalized coordinates with an
explicit constraint that the bead stay on the surface. Find a Lagrangian
and show that the Lagrange equations are equivalent to those found in
exercise [1.18](book-Z-H-13.html#%_thm_1.18).

**Exercise 1.36.**  **Motion of a tiny golf ball**\
 Consider the motion of a golf ball idealized as a point mass
constrained to a frictionless smooth surface of varying height *h*(*x*,
*y*) in a uniform gravitational field with acceleration *g*.

**a**.  Find an augmented Lagrangian for this system, and derive the
equations governing the motion of the point mass in *x* and *y*.

**b**.  Under what conditions is this approximated by a potential
function *V*(*x*, *y*) = *mgh*(*x*, *y*)?

**c**.  Assume that *h*(*x*, *y*) is axisymmetric about *x* = *y* = 0.
Can you find such an *h* that yields motions with closed orbits?

### [1.10.2  Derivative Constraints](book-Z-H-4.html#%_toc_%_sec_1.10.2)

Here we investigate velocity-dependent constraints that are \`\`total
time derivatives'' of velocity-independent constraints. The methods
presented so far do not apply because the constraint is
velocity-dependent.

Consider a velocity-dependent constraint ![](chap1-Z-G-D-56.gif) = 0.
That ![](chap1-Z-G-D-56.gif) is a total time derivative means that there
exists a velocity-independent function ![](chap1-Z-G-D-16.gif) such that

<div align="left">

![](chap1-Z-G-252.gif)

</div>

That ![](chap1-Z-G-D-16.gif) is velocity-independent means
![](front-Z-G-D-2.gif)~2~ ![](chap1-Z-G-D-16.gif) = 0. As state
functions the relationship between ![](chap1-Z-G-D-56.gif) and
![](chap1-Z-G-D-16.gif) is

<div align="left">

![](chap1-Z-G-253.gif)

</div>

Given a ![](chap1-Z-G-D-56.gif) we can find ![](chap1-Z-G-D-16.gif) by
solving this linear partial differential equation. The solution is
determined up to a constant, so ![](chap1-Z-G-D-56.gif) = 0 implies
![](chap1-Z-G-D-16.gif) = *K* for some constant *K*. On the other hand,
if we knew ![](chap1-Z-G-D-16.gif) = *K* then ![](chap1-Z-G-D-56.gif) =
0 follows. Thus the velocity-dependent constraint
![](chap1-Z-G-D-56.gif) = 0 is equivalent to the velocity-independent
constraint ![](chap1-Z-G-D-16.gif) = *K*, and we know how to find
Lagrange equations for such systems.

If *L* is a Lagrangian for the unconstrained problem, the Lagrange
equations with the constraint ![](chap1-Z-G-D-16.gif) = *K* are

<div align="left">

![](chap1-Z-G-254.gif)

</div>

where ![](chap1-Z-G-D-40.gif) is a function of time that will be
eliminated during the solution process. The constant *K* does not affect
the Lagrange equations. The function ![](chap1-Z-G-D-16.gif) is
independent of velocity, ![](front-Z-G-D-2.gif)~2~
![](chap1-Z-G-D-16.gif) = 0, so the Lagrange equations become

<div align="left">

![](chap1-Z-G-255.gif)

</div>

From equation ([1.208](#EQUATION_1.208)) we see that

<div align="left">

![](chap1-Z-G-256.gif)

</div>

so the Lagrange equations with the constraint ![](chap1-Z-G-D-56.gif) =
0 are

<div align="left">

![](chap1-Z-G-257.gif)

</div>

The important feature is that we can write the Lagrange equations
directly in terms of ![](chap1-Z-G-D-56.gif) without having to produce
the integral ![](chap1-Z-G-D-16.gif). But the validity of these Lagrange
equations depends on the existence of the integral
![](chap1-Z-G-D-16.gif).

It turns out that the augmented Lagrangian trick also works here. These
Lagrange equations are given if we augment the Lagrangian with the
constraint ![](chap1-Z-G-D-56.gif) multiplied by a function of
time ![](chap1-Z-G-D-40.gif)':

<div align="left">

![](chap1-Z-G-258.gif)

</div>

The Lagrange equations for *L*' turn out to be

<div align="left">

![](chap1-Z-G-259.gif)

</div>

which, with the identification ![](chap1-Z-G-D-40.gif) = `-`
*D*![](chap1-Z-G-D-40.gif)', are the same as Lagrange
equations ([1.212](#EQUATION_1.212)).

Sometimes a problem can be naturally formulated in terms of
velocity-dependent constraints. The formalism we have developed will
handle any velocity-dependent constraint that can be written in terms of
the derivative of a coordinate constraint. Such a constraint is called
an *integrable constraint*. Any system for which the constraints can be
put in the form of a coordinate constraint, or are already in that form,
is called a *holonomic system*.

**Exercise 1.37.**  ****\
 Show that the augmented Lagrangian ([1.213](#EQUATION_1.213)) does lead
to the Lagrange equations ([1.214](#EQUATION_1.214)), taking into
account the fact that ![](chap1-Z-G-D-56.gif) is a total time derivative
of ![](chap1-Z-G-D-16.gif).

#### [Goldstein's hoop](book-Z-H-4.html#%_toc_%_sec_Temp_168)

Here we consider a problem for which the constraint can be represented
as a time derivative of a coordinate constraint: a hoop of mass *M*
rolling, without slipping, down a (one-dimensional) inclined plane (see
figure [1.10](#FIGURE_1.10)).[^93^](#footnote_Temp_169)

<div align="left">

![](chap1-Z-G-260.gif)

</div>

We will formulate this problem in terms of the two
coordinates ![](chap1-Z-G-D-19.gif), the rotation of an arbitrary point
on the hoop from an arbitrary reference direction, and *x*, the linear
progress down the inclined plane. The constraint is that the hoop does
not slip. Thus a change in ![](chap1-Z-G-D-19.gif) is exactly reflected
in a change in *x*; the constraint function is

<div align="left">

![](chap1-Z-G-261.gif)

</div>

This constraint is phrased as a relation among generalized velocities,
but it could be integrated to get *x* = *R* ![](chap1-Z-G-D-19.gif) +
*c*. We may form our augmented Lagrangian with either the integrated
constraint or its derivative.

The kinetic energy has two parts, the energy of rotation of the hoop and
the energy of the motion of its center of
mass.[^94^](#footnote_Temp_170) The potential energy of the hoop
decreases as the height decreases. Thus we may write the augmented
Lagrangian:

<div align="left">

![](chap1-Z-G-262.gif)

</div>

Lagrange's equations are

<div align="left">

![](chap1-Z-G-263.gif)

</div>

And by differentiation of the third Lagrange equation we obtain

<div align="left">

![](chap1-Z-G-264.gif)

</div>

By combining these equations we can solve for the dynamical quantities
of interest. For this case of a rolling hoop the linear acceleration

<div align="left">

![](chap1-Z-G-265.gif)

</div>

is just half of what it would have been if the mass had just slid down a
frictionless plane without rotating. Note that for this hoop *D*^2^*x*
is independent of both *M* and *R*. We see from the Lagrange equations
that *D*![](chap1-Z-G-D-40.gif) can be interpreted as the friction force
involved in enforcing the constraint. The frictional force of constraint
is

<div align="left">

![](chap1-Z-G-266.gif)

</div>

and the angular acceleration is

<div align="left">

![](chap1-Z-G-267.gif)

</div>

### [1.10.3  Nonholonomic Systems](book-Z-H-4.html#%_toc_%_sec_1.10.3)

Systems with constraints that are not integrable are termed
*nonholonomic systems*. A constraint is not integrable if it cannot be
written in terms of an equivalent coordinate constraint. An example of a
nonholonomic system is a ball rolling without slipping in a bowl. As the
ball rolls it must turn so that its surface does not move relative to
the bowl at the point of contact. This looks as if it might establish a
relation between the location of the ball in the bowl and the
orientation of the ball, but it doesn't. The ball may return to the same
place in the bowl with different orientations depending on the
intervening path it has taken. As a consequence, the constraints cannot
be used to eliminate any coordinates.

What are the equations of motion governing nonholonomic systems? For the
restricted set of systems with nonholonomic constraints that are linear
in the velocities, it is widely reported[^95^](#footnote_Temp_171) that
the equations of motion are as follows. Let ![](chap1-Z-G-D-56.gif) have
the form

<div align="left">

![](chap1-Z-G-268.gif)

</div>

a state function that is linear in the velocities. We assume
![](chap1-Z-G-D-56.gif) is not a total time derivative. If *L* is a
Lagrangian for the unconstrained system, then the equations of motion
are asserted to be

<div align="left">

![](chap1-Z-G-269.gif)

</div>

With the constraint ![](chap1-Z-G-D-56.gif) = 0, the system is closed
and the evolution of the system is determined. Note that these equations
are identical to the Lagrange equations ([1.212](#EQUATION_1.212)) for
the case that ![](chap1-Z-G-D-56.gif) is a total time derivative, but
here the derivation of those equations is no longer valid.

An essential step in the derivation of the Lagrange equations for
coordinate constraints ![](chap1-Z-G-D-16.gif) = 0 with
![](front-Z-G-D-2.gif)~2~ ![](chap1-Z-G-D-16.gif) = 0 was to note that
two conditions must be satisfied:

<div align="left">

![](chap1-Z-G-270.gif)

</div>

and

<div align="left">

![](chap1-Z-G-271.gif)

</div>

Because *E* [*L*] o ![](chap1-Z-G-D-9.gif)[*q*] is orthogonal to
![](chap1-Z-G-D-13.gif) and ![](chap1-Z-G-D-13.gif) is constrained to be
orthogonal to ![](front-Z-G-D-2.gif)~1~ ![](chap1-Z-G-D-16.gif) o
![](chap1-Z-G-D-9.gif)[*q*] , the two must be parallel at each moment:

<div align="left">

![](chap1-Z-G-272.gif)

</div>

The Lagrange equations for derivative constraints were derived from
this.

This derivation does not go through if the constraint function depends
on velocity. In this case, for a variation ![](chap1-Z-G-D-13.gif) to be
consistent with the velocity-dependent constraint function
![](chap1-Z-G-D-56.gif) it must satisfy (see equation [1.179](#1.179))

<div align="left">

![](chap1-Z-G-273.gif)

</div>

We may no longer eliminate ![](chap1-Z-G-D-13.gif) by the same argument,
because ![](chap1-Z-G-D-13.gif) is no longer orthogonal to
![](front-Z-G-D-2.gif)~1~ ![](chap1-Z-G-D-56.gif) o
![](chap1-Z-G-D-9.gif)[*q*], and we cannot rewrite the constraint as a
coordinate constraint because ![](chap1-Z-G-D-56.gif) is, by assumption,
not integrable.

The following is the derivation of the nonholonomic equations from
Arnold et al. [[6](book-Z-H-80.html#cite{Arnold88})], translated into
our notation. Define a \`\`virtual velocity'' ![](chap1-Z-G-D-18.gif) to
be any velocity satisfying

<div align="left">

![](chap1-Z-G-274.gif)

</div>

The \`\`principle of d'Alembert-Lagrange,'' according to Arnold, states
that

<div align="left">

![](chap1-Z-G-275.gif)

</div>

for any virtual velocity ![](chap1-Z-G-D-18.gif). Because
![](chap1-Z-G-D-18.gif) is arbitrary except that it is required to be
orthogonal to ![](front-Z-G-D-2.gif)~2~ ![](chap1-Z-G-D-56.gif) o
![](chap1-Z-G-D-9.gif)[*q*] and any such ![](chap1-Z-G-D-18.gif) is
orthogonal to *E* [*L*] o ![](chap1-Z-G-D-9.gif)[*q*], then
![](front-Z-G-D-2.gif)~2~ ![](chap1-Z-G-D-56.gif) o
![](chap1-Z-G-D-9.gif)[*q*] must be parallel to *E* [*L*] o
![](chap1-Z-G-D-9.gif)[*q*]. So

<div align="left">

![](chap1-Z-G-276.gif)

</div>

which are the nonholonomic equations.

To convert the stationary action equations to the equations of Arnold we
must do the following. To get from equation ([1.226](#EQUATION_1.226))
to equation ([1.231](#EQUATION_1.231)), we must replace
![](chap1-Z-G-D-13.gif) by ![](chap1-Z-G-D-18.gif). However, to get from
equation ([1.229](#EQUATION_1.229)) to
equation ([1.230](#EQUATION_1.230)), we must set ![](chap1-Z-G-D-13.gif)
= 0 and replace *D*![](chap1-Z-G-D-13.gif) by ![](chap1-Z-G-D-18.gif).
All \`\`derivations'' of the nonholonomic equations have similar
identifications. It comes down to this: the nonholonomic equations do
not follow from the action principle. They are something else. Whether
they are correct or not depends on whether or not they agree with
experiment.

For systems with either coordinate constraints or derivative
constraints, we have found that the Lagrange equations can be derived
from a Lagrangian that is augmented with the constraint. However, if the
constraints are not integrable the Lagrange equations for the augmented
Lagrangian are not the same as the nonholonomic
system (equations [1.225](#EQUATION_1.225)).[^96^](#footnote_Temp_172)
Let *L*' be an augmented Lagrangian with non-integrable constraint
![](chap1-Z-G-D-56.gif):

<div align="left">

![](chap1-Z-G-277.gif)

</div>

then the Lagrange equations associated with the coordinates are

<div align="left">

![](chap1-Z-G-278.gif)

</div>

The Lagrange equation associated with ![](chap1-Z-G-D-40.gif) is just
the constraint equation

<div align="left">

![](chap1-Z-G-279.gif)

</div>

An interesting feature of these equations is that they involve both
![](chap1-Z-G-D-40.gif) and *D*![](chap1-Z-G-D-40.gif). Thus the usual
state variables *q* and *Dq*, with the constraint, are not sufficient to
determine a full set of initial conditions for the derived Lagrange
equations; we need to specify an initial value for
![](chap1-Z-G-D-40.gif) as well.

In general, for any particular physical system,
equations ([1.225](#EQUATION_1.225)) and ([1.234](#EQUATION_1.234)) are
not the same, and in fact they have different solutions. It is not
apparent that either set of equations accurately models the physical
system. The first approach to nonholonomic systems is not justified by
extension of the arguments for the holonomic case and the other is not
fully determined. Perhaps this indicates that the models are inadequate,
that more details of how the constraints are maintained need to be
specified.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^88^](#call_footnote_Temp_155) Given any acceptable variation, we may
make another acceptable variation by multiplying the given one by a bump
function that emphasizes any particular time interval.

[^89^](#call_footnote_Temp_156) We take two tuple-valued functions of
time to be orthogonal if at each instant the dot product of the tuples
is zero. Similarly, tuple-valued functions are considered parallel if at
each moment one of the tuples is a scalar multiple of the other. The
scalar multiplier is in general a function of time.

[^90^](#call_footnote_Temp_159) Recall that the Euler-Lagrange operator
*E* has the property

<div align="left">

![](chap1-Z-G-233.gif)

</div>

[^91^](#call_footnote_Temp_161) This constraint has the same form as
those used in the demonstration that *L* = *T* `-` *V* can be used for
rigid systems. Here it is a particular example of a more general set of
constraints.

[^92^](#call_footnote_Temp_162) Indeed, if we had scaled the constraint
equations as we did in the discussion of Newtonian constraint forces, we
could have identified ![](chap1-Z-G-D-40.gif) with the the magnitude of
the constraint force *F*. However, though ![](chap1-Z-G-D-40.gif) will
in general be related to the constraint forces it will not be one of
them. We chose to leave the scaling as it naturally appeared rather than
make things turn out artificially pretty.

[^93^](#call_footnote_Temp_169) This example appears in
[[20](book-Z-H-80.html#cite{Goldstein})], pp. 49-51,

[^94^](#call_footnote_Temp_170) We will see in
chapter [2](book-Z-H-20.html#%_chap_2) how to compute the kinetic energy
of rotation, but for now the answer is (1/2) *M* *R*^2^
![](chap1-Z-G-D-20.gif)^2^.

[^95^](#call_footnote_Temp_171) For some treatments of nonholonomic
systems see, for example,
Whittaker [[46](book-Z-H-80.html#cite{Whittaker})],
Goldstein [[20](book-Z-H-80.html#cite{Goldstein})],
Gantmakher [[19](book-Z-H-80.html#cite{Gantmakher})], or Arnold et
al. [[6](book-Z-H-80.html#cite{Arnold88})].

[^96^](#call_footnote_Temp_172) Arnold et
al. [[6](book-Z-H-80.html#cite{Arnold88})] call the variational
mechanics with the constraints added to the Lagrangian *Vakonomic
mechanics*.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-16.html)</span><span>,
[next](book-Z-H-18.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


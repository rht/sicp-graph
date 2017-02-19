<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-43.html)</span><span>,
[next](book-Z-H-45.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[3.8  Liouville's Theorem](book-Z-H-4.html#%_toc_%_sec_3.8)
-----------------------------------------------------------

If an ensemble of states occupies a particular volume of phase space at
one moment, then the subsequent evolution of that volume by the flow
described by Hamilton's equations may distort the ensemble but does not
change the volume the ensemble occupies. The fact that phase-space
volume is preserved by the phase flow is called *Liouville's theorem*.

We will first illustrate the preservation of phase-space volume with a
simple example and then prove it in general.

#### [The phase flow for the pendulum](book-Z-H-4.html#%_toc_%_sec_Temp_277)

Consider an undriven pendulum described by the Hamiltonian:

<div align="left">

![](chap3-Z-G-165.gif)

</div>

In figure [3.25](#FIGURE_3.25) we see the evolution of an elliptic
region around a point on the ![](chap1-Z-G-D-19.gif)-axis, in the
oscillation region of the pendulum. Three later positions of the region
are shown. The region is stretched and sheared by the flow, but the area
is preserved. After many cycles, the starting region will be stretched
to be a thin layer distributed in the phase angle of the pendulum.

<div align="left">

![](chap3-Z-G-166.gif)

</div>

Figure [3.26](#FIGURE_3.26) shows a similar evolution (for smaller time
intervals) of a region straddling the
separatrix[^31^](#footnote_Temp_278) near the unstable equilibrium
point. The phase-space region rapidly stretches along the separatrix,
while preserving the area. The initial conditions that start in the
oscillation region (inside of the separatrix) will continue to spread
into a thin ring-shaped region, while the initial conditions that start
outside of the separatrix will spread into a thin region of rotation on
the outside of the separatrix.

<div align="left">

![](chap3-Z-G-167.gif)

</div>

#### [Proof of Liouville's theorem](book-Z-H-4.html#%_toc_%_sec_Temp_279)

Consider a set of ordinary differential equations of the form

<div align="left">

![](chap3-Z-G-168.gif)

</div>

where *z* is a tuple of *N* state variables. Let *R*(*t*~1~) be a region
of the state space at time *t*~1~. Each element of this region is an
initial condition at time *t*~1~ for the system, and evolves to an
element at time *t*~2~ according to the differential equations. The set
of these elements at time *t*~2~ is the region *R*(*t*~2~). Regions
evolve to regions.

The evolution of the system for a time interval ![](chap1-Z-G-D-43.gif)
*t* defines a map *g*~*t*,\\ ![](chap1-Z-G-D-43.gif)\\ *t*~ from the
state space to itself:

<div align="left">

![](chap3-Z-G-169.gif)

</div>

Regions map to regions by mapping each element in the region:

<div align="left">

![](chap3-Z-G-170.gif)

</div>

The volume *V*(*t*) of a region *R*(*t*) is
![](chap1-Z-G-D-2.gif)~*R*(*t*)~ ![](chap3-Z-G-D-8.gif), where
![](chap3-Z-G-D-8.gif) is the function whose value is one for every
input. The volume of the evolved region *R*(*t* +
![](chap1-Z-G-D-43.gif) *t*) is

<div align="left">

![](chap3-Z-G-171.gif)

</div>

where Jac(*g*~*t*,\\ ![](chap1-Z-G-D-43.gif)\\ *t*~) is the Jacobian of
the mapping *g*~*t*,\\ ![](chap1-Z-G-D-43.gif)\\ *t*~. The Jacobian is
the determinant of the derivative of the mapping.

For small ![](chap1-Z-G-D-43.gif) *t*

<div align="left">

![](chap3-Z-G-172.gif)

</div>

and thus

<div align="left">

![](chap3-Z-G-173.gif)

</div>

where *I* is the identity function, so *DI*(*z*(*t*)) is a unit
multiplier. We can use the fact that if ***A*** is an *N* × *N* square
matrix then

<div align="left">

![](chap3-Z-G-174.gif)

</div>

to show that

<div align="left">

![](chap3-Z-G-175.gif)

</div>

where

<div align="left">

![](chap3-Z-G-176.gif)

</div>

Thus

<div align="left">

![](chap3-Z-G-177.gif)

</div>

So the rate of change of the volume at time *t* is

<div align="left">

![](chap3-Z-G-178.gif)

</div>

Now we compute *G*~*t*~ for a system described by a Hamiltonian *H*. The
components of *z* are the components of the coordinates and the momenta:
*z*^*k*^ = *q*^*k*^, *z*^*k*+*n*^ = *p*~*k*~ for *k* = 0, `...`, *n* `-`
1. The components of *F* are

<div align="left">

![](chap3-Z-G-179.gif)

</div>

for *k* = 0, `...`, *n* `-` 1. The diagonal components of the derivative
![](front-Z-G-D-2.gif)~1~ *F* are

<div align="left">

![](chap3-Z-G-180.gif)

</div>

The component partial derivatives commute, so the diagonal components
with index *k* and index *k* + *n* are equal and opposite. We see that
the trace, which is the sum of these diagonal components, is zero. Thus
the integral of *G*~*t*~ over the region *R*(*t*) is zero, so the
derivative of the volume at time *t* is zero. Because *t* is arbitrary,
the volume does not change. This proves *Liouville's theorem*: the
phase-space flow conserves phase-space volume.

Notice that the proof of Liouville's theorem does not depend upon
whether or not the Hamiltonian has explicit time dependence. Liouville's
theorem holds for systems with time-dependent Hamiltonians.

We may think of the ensemble of all possible states as a fluid flowing
around under the control of the dynamics. Liouville's theorem says that
this fluid is incompressible for Hamiltonian systems.

**Exercise 3.11.**  **Determinants and traces**\
 Show that equation ([3.152](#EQUATION_3.152)) is correct.

#### [Area preservation of stroboscopic surfaces of section](book-Z-H-4.html#%_toc_%_sec_Temp_281)

Surfaces of section for periodically driven Hamiltonian systems are area
preserving if the section coordinates are the phase-space coordinate and
momentum. This is an important feature of surfaces of section. It is a
consequence of Liouville's theorem for one-degree-of-freedom problems.

It is also the case that surfaces of section such as those we have used
for the Hénon-Heiles problem are area preserving, but we are not ready
to prove this yet!

#### [Poincaré recurrence](book-Z-H-4.html#%_toc_%_sec_Temp_282)

The *Poincaré recurrence theorem* is a remarkable theorem that is a
trivial consequence of Liouville's theorem. Loosely, the theorem states
that almost all trajectories eventually return arbitrarily close to
where they started. This is true regardless of whether the trajectories
are chaotic or regular.

More precisely, consider a Hamiltonian dynamical system for which the
phase space is a bounded domain *D*. We identify some initial point in
the phase space, say *z*~0~. Then, for any finite neighborhood *U* of
*z*~0~ we choose, there are trajectories that emanate from initial
points in that neighborhood and eventually return to the neighborhood.

We can prove this by considering the successive images of *U* under the
time evolution. For simplicity, we restrict consideration to time
evolution for a time interval ![](chap1-Z-G-D-43.gif). The map of the
phase space onto itself generated by time evolution for an interval
![](chap1-Z-G-D-43.gif) we call *C*. Subsequent applications of the map
generate a discrete time evolution. Sets of points in phase space
transform by evolving all the points in the set; the image of the set
*U* is denoted *C*(*U*). Now consider the trajectory of the set *U*,
that is, the sets *C*^*n*^(*U*) where *C*^*n*^ indicates the *n*-times
composition of *C*. Now there are two possibilities: either the
successive images *C*^*i*^(*U*) intersect or they do not. If they do not
intersect, then with each iteration, a volume of *D* equal to the volume
of *U* gets \`\`used up'' and cannot belong to the further image. But
the volume of *D* is finite, so we cannot fit an infinite number of
non-intersecting finite volumes into it. Therefore, after some number of
iterations the images intersect. Suppose *C*^*i*^(*U*) intersects with
*C*^*j*^(*U*), with *j*\<*i*, for definiteness. Then the pre-image of
each must also intersect, since the pre-image of a point in the
intersection belongs to both sets. Thus *C*^*i*`-`1^(*U*) intersects
*C*^*j*`-`1^(*U*). This can be continued until finally we have that
*C*^*i*`-`*j*^(*U*) intersects *U*. So we have proven that after *i* `-`
*j* iterations of the map *C* there are a set of points initially in *U*
that return to the neighborhood *U*.

So for every neighborhood of every point in the phase space there is a
subneighborhood such that the trajectories emanating from all of the
points in that subneighborhood return to that subneighborhood. Thus
almost every trajectory returns arbitrarily close to where it started.

#### [The gas in the corner of the room](book-Z-H-4.html#%_toc_%_sec_Temp_283)

Suppose we have a collection of *N* classical atoms in a perfectly
sealed room. The phase-space dimension of this system is 6*N*. A point
in this phase space is denoted *z*. Suppose initially all the atoms are,
say, within one centimeter of one corner, with arbitrarily chosen finite
velocities. This corresponds to some initial point *z*~0~ in the phase
space. The phase space of the system is limited in space by the room and
in momentum by energy conservation; the phase space is bounded. The
recurrence theorem then says that in the neighborhood of *z*~0~ there is
an initial condition of the system that returns to the neighborhood of
*z*~0~ after some time. For the individual atoms this means that after
some time all of the atoms will be found in the corner of the room
again, and again, and again. Makes one wonder about the second law of
thermodynamics, doesn't it?[^32^](#footnote_Temp_284)

#### [Nonexistence of attractors in Hamiltonian systems](book-Z-H-4.html#%_toc_%_sec_Temp_285)

Some systems have attractors. An *attractor* is a region of phase space
that gobbles volumes of trajectories. For an attractor there is some
larger region, the basin of attraction, such that sets of trajectories
with nonzero volume eventually end up in the attractor and never leave
it. The recurrence theorem shows that Hamiltonian systems with bounded
phase space do not have attractors. Consider some candidate volume in
the proposed basin of attraction. The recurrence theorem guarantees that
some trajectories in the candidate volume return to the volume
repeatedly. Therefore, the volume is not in a basin of attraction.
Attractors do not exist in Hamiltonian systems with bounded phase space.

This does not mean that every trajectory always returns. A simple
example is the pendulum. Suppose we take a blob of trajectories that
spans the separatrix, the trajectory that asymptotically approaches the
unstable equilibrium with the pendulum pointed up. Trajectories with
more energy than the separatrix make a full loop around and return to
their initial point; trajectories with lower energy than the separatrix
oscillate once across and back to their initial position; but the
separatrix trajectory itself leaves the initial region permanently, and
continually approaches the unstable point.

#### [Conservation of phase volume in a dissipative system](book-Z-H-4.html#%_toc_%_sec_Temp_286)

The definition of a dissipative system is not so clear. For some,
\`\`dissipative'' implies that phase-space volume is not conserved,
which is the same as saying the evolution of the system is not governed
by Hamilton's equations. For others, \`\`dissipative'' implies that
friction is present, representing loss of energy to unmodeled degrees of
freedom. Here is a curious example. The damped harmonic oscillator is
the paradigm of a dissipative system. Here we show that the damped
harmonic oscillator can be described by Hamilton's equations and that
phase-space volume is conserved.

The damped harmonic oscillator is governed by the ordinary differential
equation

<div align="left">

![](chap3-Z-G-181.gif)

</div>

where ![](chap1-Z-G-D-21.gif) is a coefficient of damping. We can
formulate this system with the Lagrangian[^33^](#footnote_Temp_287)

<div align="left">

![](chap3-Z-G-182.gif)

</div>

The Lagrange equation for this Lagrangian is

<div align="left">

![](chap3-Z-G-183.gif)

</div>

Since the exponential is never zero this equation has the same
trajectories as equation ([3.159](#EQUATION_3.159)) above.

The momentum conjugate to *x* is

<div align="left">

![](chap3-Z-G-184.gif)

</div>

and the Hamiltonian is

<div align="left">

![](chap3-Z-G-185.gif)

</div>

For this system, the Hamiltonian is not the sum of the kinetic energy of
the motion of the mass and the potential energy stored in the spring.
The value of the Hamiltonian is not conserved (![](front-Z-G-D-2.gif)~0~
*H* ne 0). Hamilton's equations are

<div align="left">

![](chap3-Z-G-186.gif)

</div>

Let's consider a numerical case. Let *m* = 5, *k* = 1/4,
![](chap1-Z-G-D-21.gif) = 3. Here the characteristic roots of the linear
constant-coefficient ordinary differential
equation ([3.159](#EQUATION_3.159)) are *s* = `-` 1/10, `-` 1/2. Thus
the solutions are

<div align="left">

![](chap3-Z-G-187.gif)

</div>

for *A*~1~ and *A*~2~ determined by the initial conditions

<div align="left">

![](chap3-Z-G-188.gif)

</div>

Thus we can form the transformation from the initial state to the final
state:

<div align="left">

![](chap3-Z-G-189.gif)

</div>

The transformation is linear, so the area is transformed by the
determinant, which is 1 in this case. Thus, contrary to intuition, the
phase-space volume is conserved. So why is this not a contradiction with
the statement that there are no attractors in Hamiltonian systems? The
answer is that the Poincaré recurrence argument is true only for bounded
phase spaces. Here, the momentum expands exponentially with time (as the
coordinate contracts), so it is unbounded.

We shouldn't really be too surprised by the way the theory protects
itself from an apparent paradox -- that the phase volume is conserved
even though all trajectories decay to zero velocity and coordinates. The
proof of Liouville's theorem allows time-dependent Hamiltonians. In this
case we are able to model the dissipation by just such a time-dependent
Hamiltonian.

**Exercise 3.12.**  **Time-dependent systems**\
 To make the fact that Liouville's theorem holds for time-dependent
systems even more concrete, extend the results of
section [3.8](#%_sec_3.8) to show how a swarm of initial points
outlining an area in the phase space of the *driven* pendulum deforms as
it evolves. Construct pictures analogous to figures [3.25](#FIGURE_3.25)
and [3.26](#FIGURE_3.26) for one of the interesting cases where we have
surfaces of section. Does the distortion look different in different
parts of the phase space? How?

#### [Distribution functions](book-Z-H-4.html#%_toc_%_sec_Temp_289)

We know the state of a system only approximately. It is reasonable to
model our state of knowledge by a probability density function on the
set of possible states. Given such incomplete knowledge, what are the
probable consequences? As the system evolves, the density function also
evolves. Liouville's theorem gives us a handle on this kind of problem.

Let *f*(*t*, *q*, *p*) be a probability density function on the phase
space at time *t*. For this to be a good probability density function we
require that the integral of *f* over all coordinates and momenta be
1 -- it is certain that the system is somewhere.

There is a set of trajectories that pass through any particular region
of phase space at a particular time. These trajectories are neither
created nor destroyed, and they proceed as a bundle to another region of
phase space at a later time. Liouville's theorem tells us that the
volume of the source region is the same as the volume of the target
region, so the density must remain constant. Thus
*D*(*f*o![](chap3-Z-G-D-5.gif)) = 0. If we have a system described by
the Hamiltonian *H* then

<div align="left">

![](chap3-Z-G-190.gif)

</div>

so we may conclude that

<div align="left">

![](chap3-Z-G-191.gif)

</div>

or

<div align="left">

![](chap3-Z-G-192.gif)

</div>

Since this must be true at each moment and since there is a solution
trajectory that emanates from every point in phase space, we may
abstract from solution paths and deduce a constraint on *f*:

<div align="left">

![](chap3-Z-G-193.gif)

</div>

This linear partial differential equation governs the evolution of the
density function, and thus shows how our state of knowledge evolves.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^31^](#call_footnote_Temp_278) The separatrix is the curve that
separates the oscillating motion from the circulating motion. It is made
up of several trajectories that are asymptotic to the unstable
equilibrium.

[^32^](#call_footnote_Temp_284) It is reported that when Boltzmann was
confronted with this problem he responded, \`\`You should wait that
long!''

[^33^](#call_footnote_Temp_287) This is just the product of the
Lagrangian for the undamped harmonic oscillator with an increasing
exponential of time.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-43.html)</span><span>,
[next](book-Z-H-45.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


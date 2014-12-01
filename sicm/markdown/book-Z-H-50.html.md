<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-49.html)</span><span>,
[next](book-Z-H-51.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[4.2  Linear Stability](book-Z-H-4.html#%_toc_%_sec_4.2)
--------------------------------------------------------

Qualitative changes are associated with fixed points of the surface of
section. As the drive is turned on, chaotic zones appear at fixed points
on separatrices of the undriven system, and we observe the appearance of
new fixed points and periodic points associated with resonance islands.
Here we investigate the behavior of systems near fixed points. We can
distinguish two types of fixed points on a surface of section: there are
fixed points that correspond to equilibria of the system and there are
fixed points that correspond to periodic orbits of the system. We first
consider the stability of equilibria of systems governed by differential
equations, then discuss the stability of fixed points of maps.

### [4.2.1  Equilibria of Differential Equations](book-Z-H-4.html#%_toc_%_sec_4.2.1)

Consider first the case of an equilibrium of a system of differential
equations. If a system is initially at an equilibrium point, the system
remains there. What can we say about the evolution of the system for
points near such an equilibrium point? This is actually a very difficult
question, which has not been completely answered. We can, however,
understand quite a lot about the motion of systems near equilibrium. The
first step is to investigate the evolution of a linear approximation to
the differential equations near the equilibrium. This part is easy, and
is the subject of linear stability analysis. Later, we will address what
the linear analysis implies for the actual problem.

Consider a system of ordinary differential equations

<div align="left">

![](chap4-Z-G-4.gif)

</div>

with components

<div align="left">

![](chap4-Z-G-5.gif)

</div>

where *n* is the dimension of the state space. An equilibrium point of
this system of equations is a point *z*~*e*~ for which the state
derivative is zero:

<div align="left">

![](chap4-Z-G-6.gif)

</div>

That this is zero at all moments for the equilibrium solution implies
![](front-Z-G-D-2.gif)~0~ *F*(*t*, *z*~*e*~) = 0.

Next consider a state path *z*' that passes near the equilibrium point.
The path displacement ![](chap2-Z-G-D-10.gif) is defined so that at time
*t*

<div align="left">

![](chap4-Z-G-7.gif)

</div>

We have

<div align="left">

![](chap4-Z-G-8.gif)

</div>

If ![](chap2-Z-G-D-10.gif) is small we can write the right-hand side as
a Taylor series in ![](chap2-Z-G-D-10.gif):

<div align="left">

![](chap4-Z-G-9.gif)

</div>

but the first term is zero because *z*~*e*~ is an equilibrium point, so

<div align="left">

![](chap4-Z-G-10.gif)

</div>

If ![](chap2-Z-G-D-10.gif) is small the evolution is approximated by the
linear terms. Linear stability analysis investigates the evolution of
the approximate equation

<div align="left">

![](chap4-Z-G-11.gif)

</div>

These are the variational
equations ([3.144](book-Z-H-40.html#EQUATION_3.144)) with the
equilibrium solution substituted for the reference trajectory. The
relationship of the solutions of this linearized system to the full
system is a difficult mathematical problem, which has not been fully
resolved.

If we restrict attention to autonomous systems
(![](front-Z-G-D-2.gif)~0~ *F* = 0), then the variational equations at
an equilibrium are a linear system of ordinary differential equations
with constant coefficients.[^2^](#footnote_Temp_298) Such systems can be
solved analytically. To simplify the notation, let *M* =
![](front-Z-G-D-2.gif)~1~ *F*(*t*, *z*~*e*~), so

<div align="left">

![](chap4-Z-G-12.gif)

</div>

We seek a solution of the form

<div align="left">

![](chap4-Z-G-13.gif)

</div>

where ![](chap1-Z-G-D-21.gif) is a structured constant with the same
number of components as ![](chap2-Z-G-D-10.gif), and
![](chap1-Z-G-D-40.gif) is a complex number called a *characteristic
exponent*. Substituting, we find

<div align="left">

![](chap4-Z-G-14.gif)

</div>

The exponential factor is not zero, so we find

<div align="left">

![](chap4-Z-G-15.gif)

</div>

which is an equation for the eigenvalue ![](chap1-Z-G-D-40.gif) and
(normalized) eigenvector ![](chap1-Z-G-D-21.gif). In general, there are
*n* eigenvalues and *n* eigenvectors, so we must add a subscript to both
![](chap1-Z-G-D-21.gif) and ![](chap1-Z-G-D-40.gif) indicating the
particular solution. The general solution is an arbitrary linear
combination of these individual solutions. The eigenvalues are solutions
of the characteristic equation

<div align="left">

![](chap4-Z-G-16.gif)

</div>

where ***M*** is the matrix representation of *M*, and ***I*** is the
identity matrix of the same dimension. The elements of ***M*** are real,
so we know that the eigenvalues ![](chap1-Z-G-D-40.gif) either are real
or come in complex-conjugate pairs. We assume the eigenvalues are all
distinct.[^3^](#footnote_Temp_299)

If the eigenvalue is real then the solution is exponential, as assumed.
If the eigenvalue ![](chap1-Z-G-D-40.gif) \> 0 then the solution expands
exponentially along the direction ![](chap1-Z-G-D-21.gif); if
![](chap1-Z-G-D-40.gif) \< 0 then the solution contracts exponentially
along the direction ![](chap1-Z-G-D-21.gif).

If the eigenvalue is complex we can form real solutions by combining the
two solutions for the complex-conjugate pair of eigenvalues. Let
![](chap1-Z-G-D-40.gif) = *a* + *i* *b*, with real *a* and *b*, be one
such complex eigenvalue. Let ![](chap1-Z-G-D-21.gif) = *u* + *i* *v*,
where *u* and *v* are real, be the eigenvector corresponding to it. So
there is a complex solution of the form

<div align="left">

![](chap4-Z-G-17.gif)

</div>

The complex conjugate of this solution is also a solution, because the
ordinary differential equation is linear with real linear coefficients.
This complex-conjugate solution is associated with the eigenvalue that
is the complex conjugate of the original complex eigenvalue. So the real
and imaginary parts of ![](chap2-Z-G-D-10.gif)~*c*~ are real solutions:

<div align="left">

![](chap4-Z-G-18.gif)

</div>

These two solutions reside in the plane containing the vectors *u* and
*v*. If *a* is positive both solutions spiral outwards exponentially,
and if *a* is negative they both spiral inwards. If *a* is zero, both
solutions trace the same ellipse, but with different phases.

Again, the general solution is an arbitrary linear combination of the
particular real solutions corresponding to the various eigenvalues. So
if we denote the *k*th real eigensolution
![](chap2-Z-G-D-10.gif)~*k*~(*t*), then the general solution is

<div align="left">

![](chap4-Z-G-19.gif)

</div>

where *A*~*k*~ may be determined by the initial conditions (the state at
a given time).

**Exercise 4.1.**  **Pendulum**\

Carry out the details of finding the eigensolutions for the two
equilibria of the pendulum (![](chap1-Z-G-D-19.gif) = 0 and
![](chap1-Z-G-D-19.gif) = ![](chap1-Z-G-D-15.gif), both with
*p*~![](chap1-Z-G-D-19.gif)~ = 0). How is the small-amplitude
oscillation frequency related to the eigenvalues? How are the
eigendirections related to the contours of the Hamiltonian?

### [4.2.2  Fixed Points of Maps](book-Z-H-4.html#%_toc_%_sec_4.2.2)

Fixed points on a surface of section correspond either to equilibrium
points of the system or to a periodic motion of the system. Linear
stability analysis of fixed points is similar to the linear stability
analysis for equilibrium points.

Let *T* be a map of the state space onto itself, as might be generated
by a surface of section. A trajectory sequence is generated by
successive iteration of the map *T*. Let *x*(*n*) be the *n*th point of
the sequence. The map carries one point of the trajectory sequence to
the next: *x*(*n* + 1) = *T*(*x*(*n*)). We can represent successive
iterations of the map by a superscript, so that *T*^*i*^ indicates *T*
composed *i* times. For example, *T*^2^(*x*) = *T*(*T*(*x*)). Thus
*x*(*n*) = *T*^*n*^(*x*(0)).[^4^](#footnote_Temp_301)

A *fixed point* *x*~0~ of the map *T* satisfies

<div align="left">

![](chap4-Z-G-20.gif)

</div>

A *periodic point* of the map *T* is a point that is visited every *k*
iterations of *T*. Thus it is a fixed point of the map *T*^*k*^. So the
behavior near a periodic point can be ascertained by looking at the
behavior near an associated fixed point of *T*^*k*^.

Let *x* be some trajectory initially near the fixed point *x*~0~ of *T*,
and ![](chap1-Z-G-D-18.gif) be the deviation from *x*~0~: *x*(*n*) =
*x*~0~ + ![](chap1-Z-G-D-18.gif)(*n*). The trajectory satisfies

<div align="left">

![](chap4-Z-G-21.gif)

</div>

Expanding the right-hand side as a Taylor series, we obtain

<div align="left">

![](chap4-Z-G-22.gif)

</div>

but *x*~0~ = *T*(*x*~0~) so

<div align="left">

![](chap4-Z-G-23.gif)

</div>

Linear stability analysis considers the evolution of the system
truncated to the linear terms

<div align="left">

![](chap4-Z-G-24.gif)

</div>

This is a system of linear difference equations, with constant
coefficients *DT*(*x*~0~).

We assume there are solutions of the form

<div align="left">

![](chap4-Z-G-25.gif)

</div>

where ![](chap4-Z-G-D-1.gif) is some (complex) number, called a
*characteristic multiplier*.[^5^](#footnote_Temp_302) Substituting this
solution into the linearized evolution equation, we find

<div align="left">

![](chap4-Z-G-26.gif)

</div>

or

<div align="left">

![](chap4-Z-G-27.gif)

</div>

where *I* is the identity function. We see that ![](chap4-Z-G-D-1.gif)
is an eigenvalue of the linear transformation *DT*(*x*~0~) and
![](chap1-Z-G-D-21.gif) is the associated (normalized) eigenvector. Let
*M* = *DT*(*x*~0~), and ***M*** be its matrix representation. The
eigenvalues are determined by

<div align="left">

![](chap4-Z-G-28.gif)

</div>

The elements of ***M*** are real, so the eigenvalues
![](chap4-Z-G-D-1.gif) are either real or come in complex-conjugate
pairs.[^6^](#footnote_Temp_303)

For the real eigenvalues the solutions are just exponential expansion or
contraction along the associated eigenvector ![](chap1-Z-G-D-21.gif):

<div align="left">

![](chap4-Z-G-29.gif)

</div>

The solution is expanding if || ![](chap4-Z-G-D-1.gif) || \> 1 and
contracting if || ![](chap4-Z-G-D-1.gif) || \< 1. If the eigenvalues are
complex, then the solution is complex, but the complex solutions
corresponding to the complex-conjugate pair of eigenvalues can be
combined to form two real solutions, as was done for the equilibrium
solutions. Let ![](chap4-Z-G-D-1.gif) = exp(*A* + *i* *B*) with real *A*
and *B*, and ![](chap1-Z-G-D-18.gif) = *u* + *i* *v*. A calculation
similar to that for the equilibrium case show that there are two real
solutions

<div align="left">

![](chap4-Z-G-30.gif)

</div>

We see that if *A*\>0 then the solution exponentially expands, and if
*A*\<0 the solution exponentially contracts. Exponential expansion,
*A*\>0, corresponds to || ![](chap4-Z-G-D-1.gif) || \> 1; exponential
contraction, *A*\<0, corresponds to || ![](chap4-Z-G-D-1.gif) || \< 1.
If *A* = 0 then the two real solutions trace an ellipse and any linear
combination of them traces an ellipse.

The general solution is an arbitrary linear combination of each of the
eigensolutions. Let ![](chap1-Z-G-D-18.gif)~*k*~ be the *k*th real
eigensolution. The general solution is

<div align="left">

![](chap4-Z-G-31.gif)

</div>

where *A*~*k*~ may be determined by the initial conditions.

**Exercise 4.2.**  **Elliptical oscillation**\

Show that the arbitrary linear combination of
![](chap1-Z-G-D-18.gif)~*a*~ and ![](chap1-Z-G-D-18.gif)~*b*~ traces an
ellipse for *A* = 0.

**Exercise 4.3.**  **Standard map**\

The standard map (see section [3.9](book-Z-H-45.html#%_sec_3.9)) has
fixed points at *I* = 0 for ![](chap1-Z-G-D-19.gif) = 0 and
![](chap1-Z-G-D-19.gif) = ![](chap1-Z-G-D-15.gif). Find the full
eigensolutions for these two fixed points. For what ranges of the
parameter *K* are the fixed points linearly stable or unstable?

### [4.2.3  Relations Among Exponents](book-Z-H-4.html#%_toc_%_sec_4.2.3)

For maps that are generated by stroboscopic sampling of the evolution of
a system of autonomous differential equations, equilibrium points are
fixed points of the map. The eigensolutions of the equilibrium of the
flow and the eigensolutions of the map at the fixed point are then
related. Let ![](chap2-Z-G-D-22.gif) be the sampling period. Then
![](chap4-Z-G-D-1.gif)~*i*~ =
*e*^![](chap1-Z-G-D-40.gif)~*i*~\\ ![](chap2-Z-G-D-22.gif)^ .

The Lyapunov exponent is a measure of the rate of exponential divergence
of nearby trajectories from a reference trajectory. If the reference
trajectory is an equilibrium of a flow, then the Lyapunov exponents are
the real parts of the linearized characteristic exponents
![](chap1-Z-G-D-40.gif)~*i*~. If the reference trajectory is fixed point
of a map generated by a flow (either a periodic orbit or an
equilibrium), then the Lyapunov exponents are real parts of the
logarithm of the characteristic multipliers, divided by the period of
the map. So if the characteristic multiplier is ![](chap4-Z-G-D-1.gif) =
*e*^*A*+*iB*^ and the period of the map is ![](chap2-Z-G-D-22.gif), then
the Lyapunov exponent is *A*/![](chap2-Z-G-D-22.gif). A positive
Lyapunov exponent of a fixed point indicates linear instability of the
fixed point.

The Lyapunov exponent has less information than the characteristic
multipliers or exponents because the imaginary part is lost. However,
the Lyapunov exponent is more generally applicable in that it is well
defined even for reference trajectories that are not periodic.

In the linear analysis of the fixed point, each characteristic exponent
corresponds to a subspace of possible linear solutions. For instance,
for a real characteristic multiplier there is a corresponding
eigendirection, and for any initial displacement along this direction
successive iterates are also along this direction. Complex-conjugate
pairs of multipliers correspond to a plane of solutions. For a
displacement initially on this plane, successive iterates are also on
this plane.

It turns out that something like this is also the case for the
linearized solutions near a reference trajectory that is not at a fixed
point. For each nonzero Lyapunov exponent there is a twisting subspace,
so that for an initial displacement in this subspace successive iterates
also belong to the subspace. At different points along the reference
trajectory the unit displacement vector that characterizes the direction
of this subspace is different.

#### [Hamiltonian specialization](book-Z-H-4.html#%_toc_%_sec_Temp_306)

For Hamiltonian systems there are additional constraints among the
eigenvalues.

Consider first the case of two-dimensional surfaces of section. We have
seen that Hamiltonian surfaces of section preserve area. As we saw in
the proof of Liouville's theorem, area preservation implies that the
determinant of the derivative of the transformation is 1. At a fixed
point *x*~0~ the linearized map is ![](chap1-Z-G-D-18.gif)(*n* + 1) =
*DT*(*x*~0~) ![](chap1-Z-G-D-18.gif)(*n*). So *M* = *DT*(*x*~0~) has
unit determinant. Now the determinant is the product of the eigenvalues,
so for a fixed point on a Hamiltonian surface of section the two
eigenvalues must be inverses of each other. We also have the constraint
that if an eigenvalue is complex then the complex conjugate of the
eigenvalue is also an eigenvalue. These two conditions imply that the
eigenvalues must either be real and inverses, or be complex-conjugate
pairs on the unit circle (see figure [4.4](#FIGURE_4.4)).

<div align="left">

![](chap4-Z-G-32.gif)

</div>

Fixed points for which the characteristic multipliers all lie on the
unit circle are called *elliptic* fixed points. The solutions of the
linearized variational equations trace ellipses around the fixed point.
Elliptic fixed points are linearly stable.

Fixed points with positive real characteristic multipliers are called
*hyperbolic* fixed points. For two-dimensional maps, there is an
exponentially expanding subspace and an exponentially contracting
subspace. The general solution is a linear combination of these. Fixed
points for which the characteristic multipliers are negative are called
*hyperbolic with reflection*.

The edge case of two degenerate characteristic multipliers is called
*parabolic*. For two degenerate eigenvalues the general solution grows
linearly. This happens at points of bifurcation where elliptic points
become hyperbolic points or vice versa.

For two-dimensional Hamiltonian maps these are the only possibilities.
For higher-dimensional Hamiltonian maps, we can get combinations of
these: some characteristic multipliers can be real and others
complex-conjugate pairs. We might imagine that in addition there would
be many other types of fixed points that occur in higher dimensions. In
fact, there is only one additional type, shown in
figure [4.5](#FIGURE_4.5). For Hamiltonian systems of arbitrary
dimensions it is still the case that for each eigenvalue the complex
conjugate and the inverse are also eigenvalues. We can prove this
starting from a result in chapter [5](book-Z-H-57.html#%_chap_5).
Consider the map of the phase space onto itself that is generated by
time evolution of a Hamiltonian system. Let *z* = (*q*, *p*); then the
map *T*~*ß*~ satisfies *z*(*t* + *ß*) = *T*~*ß*~(*z*(*t*)) for solutions
*z* of Hamilton's equations. We will show in
chapter [5](book-Z-H-57.html#%_chap_5) that the derivative of the map
*T*~*ß*~ is symplectic, whether or not the starting point is at a fixed
point. A 2*n*×2*n* matrix ***M*** is *symplectic* if it satisfies

<div align="left">

![](chap4-Z-G-33.gif)

</div>

where ***J*** is the 2*n*-dimensional symplectic unit:

<div align="left">

![](chap4-Z-G-34.gif)

</div>

with the *n*× *n* unit matrix **1**~*n*\\ ×\\ *n*~ and the *n* × *n*
zero matrix **0**~*n*\\ ×\\ *n*~.

<div align="left">

![](chap4-Z-G-35.gif)

</div>

Using the symplectic property, we can show that in general for each
eigenvalue its inverse is also an eigenvalue. Assume
![](chap4-Z-G-D-1.gif) is an eigenvalue, so that ![](chap4-Z-G-D-1.gif)
satisfies det(***M*** `-` ![](chap4-Z-G-D-1.gif) ***I***) = 0. This
equation is unchanged if ***M*** is replaced by its transpose, so
![](chap4-Z-G-D-1.gif) is also an eigenvalue of ***M***^`T`^:

<div align="left">

![](chap4-Z-G-36.gif)

</div>

From this we can see that

<div align="left">

![](chap4-Z-G-37.gif)

</div>

Now, from the symplectic property we have

<div align="left">

![](chap4-Z-G-38.gif)

</div>

So

<div align="left">

![](chap4-Z-G-39.gif)

</div>

and we can conclude that 1/![](chap4-Z-G-D-1.gif) is an eigenvalue of
***M*** with the eigenvector ***J*** ![](chap1-Z-G-D-21.gif)'. From the
fact that for every eigenvalue its inverse is also an eigenvalue we
deduce that the determinant of the transformation ***M***, which is the
product of the eigenvalues, is one.

The constraints that the eigenvalues must be associated with inverses
and complex conjugates yields exactly one new pattern of eigenvalues in
higher dimensions. Figure [4.5](#FIGURE_4.5) shows the only new pattern
that is possible.

We have seen that the Lyapunov exponents for fixed points are related to
the characteristic multipliers for the fixed points, so the Hamiltonian
constraints on the multipliers correspond to Hamiltonian constraints for
Lyapunov exponents at fixed points. For each characteristic multiplier,
the inverse is also a characteristic multiplier. This means that at
fixed points, for each positive Lyapunov exponent there is a
corresponding negative Lyapunov exponent with the same magnitude. It
turns out that this is also true if the reference trajectory is not at a
fixed point. For Hamiltonian systems, for each positive Lyapunov
exponent there is a corresponding negative exponent of equal magnitude.

**Exercise 4.4.**  **Quartet**\

Describe (perhaps by drawing cross sections) the orbits that are
possible with quartets.

#### [Linear and nonlinear stability](book-Z-H-4.html#%_toc_%_sec_Temp_308)

A fixed point that is linearly unstable indicates that the full system
is unstable at that point. This means that trajectories starting near
the fixed point diverge from the fixed point. On the other hand, linear
stability of a fixed point does not generally guarantee that the full
system is stable at that point. For a two-degree-of-freedom Hamiltonian
system, the Kolmogorov-Arnold-Moser theorem proves under certain
conditions that linear stability implies nonlinear stability. In higher
dimensions, though, it is not known whether linear stability implies
nonlinear stability.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^2^](#call_footnote_Temp_298) Actually, all we need is
![](front-Z-G-D-2.gif)~0~ ![](front-Z-G-D-2.gif)~1~ *F*(*t*, *z*~*e*~) =
0.

[^3^](#call_footnote_Temp_299) If the eigenvalues are not unique then
the form of the solution is modified.

[^4^](#call_footnote_Temp_301) The map *T* is being used as an operator:
multiplication is interpreted as composition.

[^5^](#call_footnote_Temp_302) A characteristic multiplier is also
sometimes called a Floquet multiplier.

[^6^](#call_footnote_Temp_303) We assume for now that the eigenvalues
are distinct.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-49.html)</span><span>,
[next](book-Z-H-51.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


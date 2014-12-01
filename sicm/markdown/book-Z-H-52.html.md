<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-51.html)</span><span>,
[next](book-Z-H-53.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[4.4  Integrable Systems](book-Z-H-4.html#%_toc_%_sec_4.4)
----------------------------------------------------------

Islands appear near commensurabilities, and commensurabilities are
present even in integrable systems. In integrable systems an infinite
number of periodic orbits are associated with each commensurability, but
upon perturbation only a finite number of periodic orbits survive. How
does this happen? First we have to learn more about integrable systems.

If an *n*-degree-of-freedom system has *n* independent conserved
quantities then the solution of the problem can be reduced to
quadratures. Such a system is called *integrable*. Typically, the phase
space of integrable systems is divided into regions of qualitatively
different behavior. For example, the motion of a pendulum is reducible
to quadratures and has three distinct types of solutions: the
oscillating solutions and the clockwise and counterclockwise circulating
solutions. The different regions of the pendulum phase space are
separated by the trajectories that are asymptotic to the unstable
equilibrium. It turns out that for any system that is reducible to
quadratures, a set of phase-space coordinates can be chosen for each
region of the phase space so that the Hamiltonian describing the motion
in that region depends only on the momenta. Furthermore, if the phase
space is bounded then the generalized coordinates can be chosen to be
angles (that are 2![](chap1-Z-G-D-15.gif)-periodic). The configuration
space described by *n* angles is an *n*-torus. The momenta conjugate to
these angles are called *actions*. Such phase-space coordinates are
called *action-angle* coordinates. We will see later how to reformulate
systems in this way. Here we explore the consequences of such a
formulation; this formulation is especially useful for finding out what
happens as additional effects are added to integrable problems.

#### [Orbit types in integrable systems](book-Z-H-4.html#%_toc_%_sec_Temp_312)

Suppose we have a time-independent *n*-degree-of-freedom system that is
reducible to quadratures. For each region of phase space there is a
local formulation of the system so that the evolution of the system is
described by a time-independent Hamiltonian that depends only on the
momenta. Suppose further that the coordinates are all angles. Let
![](chap1-Z-G-D-19.gif) be the tuple of angles and *J* be the tuple of
conjugate momenta. The Hamiltonian is

<div align="left">

![](chap4-Z-G-44.gif)

</div>

Hamilton's equations are simply

<div align="left">

![](chap4-Z-G-45.gif)

</div>

where ![](chap1-Z-G-D-23.gif)(*J*) = *D* *f*(*J*) is a tuple of
frequencies with a component for each degree of freedom. The momenta are
all constant because the Hamiltonian does not depend on any of the
coordinates. The motion of the coordinate angles is uniform; the rates
of change of the angles are the frequencies ![](chap1-Z-G-D-23.gif),
which depend only on the constant momenta. Given initial values
![](chap1-Z-G-D-19.gif)(*t*~0~) and *J*(*t*~0~) at time *t*~0~, the
solutions are simple:

<div align="left">

![](chap4-Z-G-46.gif)

</div>

Though the solutions are simple, there are a number of distinct orbit
types: equilibrium solutions, periodic orbits, and quasiperiodic orbits,
depending on the frequency ratios.

If ![](chap1-Z-G-D-23.gif)(*J*) is zero for some *J* then
![](chap1-Z-G-D-19.gif) and *J* are both constant, for any
![](chap1-Z-G-D-19.gif). The system is at an equilibrium point.

A solution is *periodic* if all the coordinates (and momenta) of the
system return to their initial values at some later time. Each
coordinate ![](chap1-Z-G-D-19.gif)^*i*^ with nonzero frequency
![](chap1-Z-G-D-23.gif)^*i*^(*J*(*t*~0~)) is periodic with a period
![](chap2-Z-G-D-22.gif)~*i*~ =
2![](chap1-Z-G-D-15.gif)/![](chap1-Z-G-D-23.gif)^*i*^(*J*(*t*~0~)). The
period of the system must therefore be an integer multiple *k*~*i*~ of
each of the individual coordinate periods ![](chap2-Z-G-D-22.gif)~*i*~.
If the system is periodic with some set of integer multiples, then it is
also periodic with any common factors divided out. Thus the period of
the system is ![](chap2-Z-G-D-22.gif) = (*k*~*i*~/*d*)
![](chap2-Z-G-D-22.gif)~*i*~ where *d* is the greatest common divisor of
the integers *k*~*i*~.

For a system with two degrees of freedom, a solution is periodic if
there exists a pair of relatively prime integers *k* and *j* such that
*k* ![](chap1-Z-G-D-23.gif)^0^(*J*(*t*~0~)) = *j*
![](chap1-Z-G-D-23.gif)^1^(*J*(*t*~0~)). The period of the system is
![](chap2-Z-G-D-22.gif) = 2 ![](chap1-Z-G-D-15.gif) *j* /
![](chap1-Z-G-D-23.gif)^0^(*J*(*t*~0~)) = 2 ![](chap1-Z-G-D-15.gif) *k*
/ ![](chap1-Z-G-D-23.gif)^1^(*J*(*t*~0~)); the frequency is
![](chap1-Z-G-D-23.gif)^0^(*J*(*t*~0~)) / *j* =
![](chap1-Z-G-D-23.gif)^1^(*J*(*t*~0~)) / *k*. A periodic motion on the
2-torus is illustrated in figure [4.10](#FIGURE_4.10).

<div align="left">

![](chap4-Z-G-47.gif)

</div>

If the frequencies ![](chap1-Z-G-D-23.gif)^*i*^(*J*(*t*~0~)) satisfy an
integer-coefficient relation sum~*i*~ *n*~*i*~
![](chap1-Z-G-D-23.gif)^*i*^(*J*(*t*~0~)) = 0, we say that the
frequencies satisfy a commensurability. If there is no commensurability
for any nonzero integer coefficients, we say that the frequencies are
linearly independent (with respect to the integers) and the solution is
*quasiperiodic*. One can prove that for *n* incommensurate frequencies
all solutions come arbitrarily close to every point in the configuration
space.[^8^](#footnote_Temp_313)

For a system with two degrees of freedom the solutions in a region
described by a particular set of action-angle variables are either
equilibrium solutions, periodic solutions, or quasiperiodic
solutions.[^9^](#footnote_Temp_314) For systems with more than two
degrees of freedom there are trajectories that are neither periodic nor
quasiperiodic with *n* frequencies. These are quasiperiodic with fewer
frequencies and dense over a corresponding lower-dimensional torus.

#### [Surfaces of section for integrable systems](book-Z-H-4.html#%_toc_%_sec_Temp_315)

As we have seen, in action-angle coordinates the angles move with
constant angular frequencies, and the momenta are constant. Thus
surfaces of section in action-angle coordinates are particularly simple.
We can make surfaces of section for time-independent
two-degree-of-freedom systems or one-degree-of-freedom systems with
periodic drive. In the latter case, one of the angles in the
action-angle system is the phase of the drive. We make surfaces of
section by accumulating points in one pair of canonical coordinates as
the other coordinate goes through some particular value, such as zero.
If we plot the section points with the angle coordinate on the abscissa
and the conjugate momentum on the ordinate then the section points for
all trajectories lie on horizontal lines, as illustrated in
figure [4.11](#FIGURE_4.11).

<div align="left">

![](chap4-Z-G-48.gif)

</div>

For definiteness, let the plane of the surface of section be the
(![](chap1-Z-G-D-19.gif)^0^, *J*~0~) plane, and the section condition be
![](chap1-Z-G-D-19.gif)^1^ = 0. The other momentum *J*~1~ is chosen so
that all the trajectories have the same energy. The momenta are all
constant, so for a given trajectory all points that are generated are
constrained to a line of constant *J*~0~.

The time between section points is the period of
![](chap1-Z-G-D-19.gif)^1^: ![](chap1-Z-G-D-43.gif) *t* =
2![](chap1-Z-G-D-15.gif) / ![](chap1-Z-G-D-23.gif)^1^(*J*(*t*~0~))
because a section point is generated for every cycle of
![](chap1-Z-G-D-19.gif)^1^. The angle between successive points on the
section is ![](chap1-Z-G-D-23.gif)^0^(*J*(*t*~0~))
![](chap1-Z-G-D-43.gif) *t* = ![](chap1-Z-G-D-23.gif)^0^(*J*(*t*~0~)) 2
![](chap1-Z-G-D-15.gif) / ![](chap1-Z-G-D-23.gif)^1^(*J*(*t*~0~)) = 2
![](chap1-Z-G-D-15.gif) ![](chap1-Z-G-D-14.gif)(*J*(*t*~0~)), where
![](chap1-Z-G-D-14.gif)(*J*) = ![](chap1-Z-G-D-23.gif)^0^(*J*) /
![](chap1-Z-G-D-23.gif)^1^(*J*) is called the *rotation number* of the
trajectory. Let ![](chap4-Z-G-D-2.gif)(*i*) and
![](chap4-Z-G-D-3.gif)(*i*) be the *i*th point (*i* is an integer) in a
sequence of points on the surface of section generated by a solution
trajectory:

<div align="left">

![](chap4-Z-G-49.gif)

</div>

where the system is assumed to be on the section at *t* = *t*~0~. Along
a trajectory, the map from one section point (
![](chap4-Z-G-D-2.gif)(*i*), ![](chap4-Z-G-D-3.gif)(*i*) ) to the next (
![](chap4-Z-G-D-2.gif)(*i* + 1), ![](chap4-Z-G-D-3.gif)(*i* + 1) ) is of
the form:[^10^](#footnote_Temp_316)

<div align="left">

![](chap4-Z-G-50.gif)

</div>

As a function of the action on the section, the rotation number is
![](chap4-Z-G-D-4.gif)(![](chap4-Z-G-D-3.gif)(0)) =
![](chap1-Z-G-D-14.gif)(![](chap4-Z-G-D-3.gif)(0), *J*~1~(*t*~0~)),
where *J*~1~(*t*~0~) has the value required to be on the section, as for
example by giving the correct energy. If the rotation number function
![](chap4-Z-G-D-4.gif) is strictly monotonic in the action coordinate on
the section then the map is called a *twist
map*.[^11^](#footnote_Temp_317)

On a surface of section the different types of orbits generate different
patterns. If the orbit is an equilibrium solution then the initial point
on the surface of section is a fixed point. The system just stays there.

If the two frequencies are commensurate, then the trajectory is periodic
and only a finite number of points are generated on the surface of
section. Both of the periodic solutions illustrated in
figure [4.10](#FIGURE_4.10) generate two points on the surface of
section defined by ![](chap1-Z-G-D-19.gif)^1^ = 0. If the frequencies
are commensurate they satisfy a relation of the form *k*
![](chap1-Z-G-D-23.gif)^0^(*J*(*t*~0~)) = *j*
![](chap1-Z-G-D-23.gif)^1^(*J*(*t*~0~)), where *J*(*t*~0~) =
(![](chap4-Z-G-D-3.gif)(0), *J*~1~(*t*~0~)) is the initial and constant
value of the momentum tuple. The motion is periodic with frequency
![](chap1-Z-G-D-23.gif)^0^(*J*(*t*~0~))/*j* =
![](chap1-Z-G-D-23.gif)^1^(*J*(*t*~0~))/*k*, so the period is
2![](chap1-Z-G-D-15.gif) *j*/ ![](chap1-Z-G-D-23.gif)^0^(*J*(*t*~0~)) =
2![](chap1-Z-G-D-15.gif) *k*/ ![](chap1-Z-G-D-23.gif)^1^(*J*(*t*~0~)).
Thus this periodic orbit generates *k* points on this surface of
section. For trajectories with commensurate frequencies the rotation
number is rational: ![](chap4-Z-G-D-4.gif)(![](chap4-Z-G-D-3.gif)(0)) =
![](chap1-Z-G-D-14.gif)(![](chap4-Z-G-D-3.gif)(0), *J*~1~(*t*~0~)) =
*j*/*k*. The coordinate ![](chap1-Z-G-D-19.gif)^1^ makes *k* cycles
while the coordinate ![](chap1-Z-G-D-19.gif)^0^ makes *j* cycles
(figure [4.10](#FIGURE_4.10) shows a system with a rotation number of
2/3). The frequencies depend on the momenta but not on the coordinates,
so the motion is periodic with the same period and rotation number for
all initial angles given these momenta. Thus there is a continuous
family of periodic orbits with different initial angles.

If the two frequencies are incommensurate, then the 2-torus is filled
densely. Thus the line on which the section points are generated is
filled densely. Again, this is the case for any initial coordinates,
because the frequencies depend only on the momenta. There are infinitely
many such orbits that are distinct for a given set of
frequencies.[^12^](#footnote_Temp_318)

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^8^](#call_footnote_Temp_313) Motion with *n* incommensurate
frequencies is dense on the *n*-torus. Furthermore, such motion is
*ergodic* on the *n*-torus. This means that time averages of
time-independent phase-space functions computed along trajectories are
equal to the phase-space average of the same function over the torus.

[^9^](#call_footnote_Temp_314) For time-independent systems with two
degrees of freedom the boundary between regions described by different
action-angle coordinates has asymptotic solutions and unstable periodic
orbits or equilibrium points. The solutions on the boundary are not
described by the action-angle Hamiltonian.

[^10^](#call_footnote_Temp_316) The coordinate
![](chap4-Z-G-D-2.gif)(*i*) is an angle. It can be brought to a standard
interval such as 0 to 2![](chap1-Z-G-D-15.gif).

[^11^](#call_footnote_Temp_317) Actually, for a map to be a twist map we
require | *D*![](chap1-Z-G-D-14.gif)(*J*) | \> *K* \> 0 over some
interval of *J*.

[^12^](#call_footnote_Temp_318) The section points for any particular
orbit are countable and dense, but they have zero measure on the line.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-51.html)</span><span>,
[next](book-Z-H-53.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-30.html)</span><span>,
[next](book-Z-H-32.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[2.11  Spin-Orbit Coupling](book-Z-H-4.html#%_toc_%_sec_2.11)
-------------------------------------------------------------

The rotation of planets and natural satellites is affected by the
gravitational forces from other celestial bodies. As an extended
application of the Lagrangian method for forced rigid bodies, we
consider the rotation of celestial objects subject to gravitational
forces.

We first develop the form of the potential energy for the gravitational
interaction of an extended body with an external point mass. With this
potential energy and the usual rigid-body kinetic energy we can form
Lagrangians that model a number of systems. We will take an initial look
at the rotation of the Moon and Mercury; later, after we have developed
more tools, we will return to study these systems.

### [2.11.1  Development of the Potential Energy](book-Z-H-4.html#%_toc_%_sec_2.11.1)

The first task is to develop convenient expressions for the
gravitational potential energy of the interaction of a rigid body with a
distant mass point. A rigid body can be thought of as made of a large
number of mass elements, subject to rigid coordinate constraints. We
have seen that the kinetic energy of a rigid body is conveniently
expressed in terms of the moments of inertia of the body and the angular
velocity vector, which in turn can be represented in terms of a suitable
set of generalized coordinates. The potential energy can be developed in
a similar manner. We first represent the potential energy in terms of
moments of the mass distribution and later introduce generalized
coordinates as particular parameters of the potential energy.

The gravitational potential energy of a mass point and a rigid body (see
figure [2.9](#FIGURE_2.9)) is the sum of the potential energy of the
mass point with each mass element of the body:

<div align="left">

![](chap2-Z-G-80.gif)

</div>

where *M*' is the mass of the external point mass,
*r*~![](chap1-Z-G-D-21.gif)~ is the distance between the point mass and
the constituent mass element with index ![](chap1-Z-G-D-21.gif),
*m*~![](chap1-Z-G-D-21.gif)~ is the mass of this constituent element,
and *G* is the gravitational constant. Let *R* be the distance of the
center of mass of the rigid body from the point mass; *R* is the
magnitude of the vector ![](chap1-Z-G-D-26.gif) `-`
![](chap2-Z-G-D-2.gif), where the external mass point has position
![](chap1-Z-G-D-26.gif) and the center of mass of the rigid body has
position ![](chap2-Z-G-D-2.gif). The vector from the center of mass to
the constituent with index ![](chap1-Z-G-D-21.gif) is
![](chap2-Z-G-D-3.gif)~![](chap1-Z-G-D-21.gif)~ and has magnitude
![](chap1-Z-G-D-18.gif)~![](chap1-Z-G-D-21.gif)~. The distance
*r*~![](chap1-Z-G-D-21.gif)~ is then given by the law of cosines as
*r*~![](chap1-Z-G-D-21.gif)~^2^ = *R*^2^ +
![](chap1-Z-G-D-18.gif)~![](chap1-Z-G-D-21.gif)~^2^ `-` 2
![](chap1-Z-G-D-18.gif)~![](chap1-Z-G-D-21.gif)~ *R* cos
![](chap1-Z-G-D-19.gif)~![](chap1-Z-G-D-21.gif)~, where
![](chap1-Z-G-D-19.gif)~![](chap1-Z-G-D-21.gif)~ is the angle between
![](chap1-Z-G-D-26.gif) `-` ![](chap2-Z-G-D-2.gif) and
![](chap2-Z-G-D-3.gif)~![](chap1-Z-G-D-21.gif)~. The potential energy is
then

<div align="left">

![](chap2-Z-G-81.gif)

</div>

This is complete, but we need to find a representation that does not
mention each constituent.

<div align="left">

![](chap2-Z-G-82.gif)

</div>

Typically, the size of celestial bodies is small compared to the
distance between them. We can make use of this to find a more compact
representation of the potential energy. If we expand the potential
energy in the small ratio
![](chap1-Z-G-D-18.gif)~![](chap1-Z-G-D-21.gif)~/*R* we find

<div align="left">

![](chap2-Z-G-83.gif)

</div>

where *P*~*l*~ is the *l*th Legendre
polynomial.[^15^](#footnote_Temp_204) Interchanging the order of the
summations yields:

<div align="left">

![](chap2-Z-G-85.gif)

</div>

Successive terms in this expansion of the potential energy typically
decrease very rapidly because celestial bodies are small compared to the
distance between them. We can compute an upper bound to the size of
these terms by replacing each factor in the sum over
![](chap1-Z-G-D-21.gif) by an upper bound. The Legendre polynomials all
have magnitudes less than one for arguments in the range `-` 1 to 1. The
distances ![](chap1-Z-G-D-18.gif)~![](chap1-Z-G-D-21.gif)~ are all less
than some maximum extent of the body ![](chap1-Z-G-D-18.gif)~max~. The
sum over *m*~![](chap1-Z-G-D-21.gif)~ times these upper bounds is just
the total mass *M* times the upper bounds. Thus

<div align="left">

![](chap2-Z-G-86.gif)

</div>

We see that the upper bound on successive terms decreases by a factor
![](chap1-Z-G-D-18.gif)~max~ / *R*. Successive terms may be smaller
still. For large bodies the gravitational force is strong enough to
overcome the internal material strength of the body, so the body, over
time, becomes nearly spherical. Successive terms in the expansion of the
potential are measures of the deviation of the mass distribution from a
spherical mass distribution. Thus for large bodies the higher-order
terms are small because the bodies are nearly spherical.

Consider the first few terms in *l*. For *l* = 0 the sum over
![](chap1-Z-G-D-21.gif) just gives the total mass *M* of the rigid body.
For *l* = 1 the sum over ![](chap1-Z-G-D-21.gif) is zero, as a
consequence of choosing the origin of the
![](chap2-Z-G-D-3.gif)~![](chap1-Z-G-D-21.gif)~ to be the center of
mass. For *l* = 2 we have to do a little more work. The sum involves
second moments of the mass distribution, and can be written in terms of
moments of inertia of the rigid body:

<div align="left">

![](chap2-Z-G-87.gif)

</div>

where *A*, *B*, and *C* are the principal moments of inertia, and *I* is
the moment of inertia of the rigid body about the line between the
center of mass of the body to the external point mass. The moment *I*
depends on the orientation of the rigid body relative to the line
between the bodies. The contributions to the potential energy up to *l*
= 2 are then[^16^](#footnote_Temp_205)

<div align="left">

![](chap2-Z-G-88.gif)

</div>

Let ![](chap1-Z-G-D-21.gif) = cos ![](chap1-Z-G-D-19.gif)~*a*~, *ß* =
cos ![](chap1-Z-G-D-19.gif)~*b*~, and ![](chap1-Z-G-D-1.gif) = cos
![](chap1-Z-G-D-19.gif)~*c*~ be the direction cosines of the angles
![](chap1-Z-G-D-19.gif)~*a*~, ![](chap1-Z-G-D-19.gif)~*b*~ and
![](chap1-Z-G-D-19.gif)~*c*~ between the principal axes hata,
![](chap2-Z-G-D-13.gif), and ![](chap2-Z-G-D-14.gif) and the line
between the center of mass and the point mass.[^17^](#footnote_Temp_206)
A little algebra shows that *I* = ![](chap1-Z-G-D-21.gif)^2^ *A* +
*ß*^2^ *B* + ![](chap1-Z-G-D-1.gif)^2^ *C*. The potential energy is then

<div align="left">

![](chap2-Z-G-89.gif)

</div>

This is a good first approximation to the potential energy of
interaction for most situations in the solar system; if we intended to
land on the Moon we probably would want to take into account
higher-order terms in the expansion.

**Exercise 2.14.**  ****\

\
**a**.  Fill in the details that show that the sum over constituents in
equation ([2.72](#EQUATION_2.72)) can be expressed as written in terms
of moments of inertia. In particular, show that

<div align="left">

![](chap2-Z-G-90.gif)

</div>

<div align="left">

![](chap2-Z-G-91.gif)

</div>

and that

<div align="left">

![](chap2-Z-G-92.gif)

</div>

**b**.  Show that if the principal moments of inertia of a rigid body
are *A*, *B*, and *C*, then the moment of inertia about an axis that
goes through the center of mass of the body with direction cosines
![](chap1-Z-G-D-21.gif), *ß*, and ![](chap1-Z-G-D-1.gif) relative to the
principal axes is

<div align="left">

![](chap2-Z-G-93.gif)

</div>

### [2.11.2  Rotation of the Moon and Hyperion](book-Z-H-4.html#%_toc_%_sec_2.11.2)

The approximation to the potential energy that we have derived can be
used for a number of different problems. It can be used to investigate
the effect of oblateness on the evolution of an artificial satellite
about the Earth, or to incorporate the effect of planetary oblateness on
the evolution of the orbits of natural satellites, such as the Moon or
the Galilean satellites of Jupiter. However, as the principal
application here, we will use it to investigate the rotational dynamics
of natural satellites and planets.

The potential energy depends on the position of the point mass relative
to the rigid body and on the orientation of the rigid body. Thus the
changing orientation is coupled to the orbital evolution; each affects
the other. However, in many situations the effect of the orientation of
the body on the evolution of the orbit may be ignored. One way to see
this is to look at the relative magnitudes of the two terms in the
potential energy ([2.74](#EQUATION_2.74)). We already know that the
second term is guaranteed to be smaller than the first by a factor of
(![](chap1-Z-G-D-18.gif)~max~ / *R*)^2^, but often it is much smaller
still because the body involved is nearly spherical. For example, the
radius of the Moon is about a third the radius of the Earth and the
distance to the Moon is about 60 Earth-radii. So the second term is
smaller than the first by a factor of order 10^`-`4^ due to the size
factors. In addition, the Moon is roughly spherical and for any
orientation the combination *A* + *B* + *C* `-` 3*I* is of order
10^`-`4^*C*. Now *C* is itself of order (2/5)*MR*^2^, because the
density of the Moon does not vary strongly with radius. So for the Moon
the second term is of order 10^`-`8^ relative to the first. Even radical
changes in the orientation of the Moon would have little dynamical
effect on its orbit.

We can learn some important qualitative aspects of the orientation
dynamics by studying a simplified model problem. First, we assume that
the body is rotating about its largest moment of inertia. This is a
natural assumption. Remember that for a free rigid body the loss of
energy while conserving angular momentum leads to rotation about the
largest moment of inertia. This is observed for most bodies in the solar
system. Next, we assume that the spin axis is perpendicular to the
orbital motion. This is a good approximation for the rotation of natural
satellites, and is a natural consequence of tidal friction --
dissipative solid-body tides raised on the satellite by the
gravitational interaction with the planet. Finally, for simplicity we
take the rigid body to be moving on a fixed elliptic orbit. This may
approximate the motion of some physical systems, provided the time scale
of the evolution of the orbit is large compared to any time scale
associated with the rotational dynamics we are investigating. So we have
a nice toy problem, one that has been used to investigate the rotational
dynamics of Mercury, the Moon, and other natural satellites. It makes
specific predictions concerning the rotation of Phobos, a satellite of
Mars, that can be compared with observations. It provides a basic
explanation of the fact that Mercury rotates precisely three times for
every two orbits it completes, and is the starting point for
understanding the chaotic tumbling of Saturn's satellite Hyperion.

<div align="left">

![](chap2-Z-G-94.gif)

</div>

We are assuming that the orbit does not change or precess. The orbit is
an ellipse with the point mass at a focus of the ellipse. The angle *f*
(see figure [2.10](#FIGURE_2.10)) measures the position of the rigid
body in its orbit relative to the point in the orbit at which the two
bodies are closest.[^18^](#footnote_Temp_208) We assume the orbit is a
fixed ellipse, so the angle *f* and the distance *R* are periodic
functions of time, with period equal to the orbit period. With the spin
axis constrained to be perpendicular to the orbit plane, the orientation
of the rigid body is specified by a single degree of freedom: the
orientation of the body about the spin axis. We specify this orientation
by the generalized coordinate ![](chap1-Z-G-D-19.gif) that measures the
angle to the hata principal axis from the same line from which we
measure *f*, the line through the point of closest approach.

Having specified the coordinate system, we can work out the details of
the kinetic and potential energies, and thus find the Lagrangian. The
kinetic energy is

<div align="left">

![](chap2-Z-G-95.gif)

</div>

where *C* is the moment of inertia about the spin axis and the angular
velocity of the body about the ![](chap2-Z-G-D-14.gif) axis is
![](chap1-Z-G-D-20.gif). There is no component of angular velocity on
the other principal axes.

To get an explicit expression for the potential energy we must write the
direction cosines in terms of ![](chap1-Z-G-D-19.gif) and *f*:
![](chap1-Z-G-D-21.gif) = cos ![](chap1-Z-G-D-19.gif)~*a*~ = `-` cos
(![](chap1-Z-G-D-19.gif) `-` *f*), *ß* = cos
![](chap1-Z-G-D-19.gif)~*b*~ = sin (![](chap1-Z-G-D-19.gif) `-` *f*),
and ![](chap1-Z-G-D-1.gif) = cos ![](chap1-Z-G-D-19.gif)~*c*~ = 0
because the ![](chap2-Z-G-D-14.gif) axis is perpendicular to the orbit
plane. The potential energy is then

<div align="left">

![](chap2-Z-G-96.gif)

</div>

Since we are assuming that the orbit is given, we need keep only terms
that depend on ![](chap1-Z-G-D-19.gif). Expanding the squares of the
cosine and the sine in terms of the double angles and dropping all the
terms that do not depend on ![](chap1-Z-G-D-19.gif), we find the
potential energy for the orientation[^19^](#footnote_Temp_209)

<div align="left">

![](chap2-Z-G-97.gif)

</div>

A Lagrangian for the model spin-orbit coupling problem is then *L* = *T*
`-` *V*:

<div align="left">

![](chap2-Z-G-98.gif)

</div>

We introduce the dimensionless \`\`out-of-roundness'' parameter

<div align="left">

![](chap2-Z-G-99.gif)

</div>

and use the fact that the orbit frequency *n* satisfies Kepler's third
law *n*^2^ *a*^3^ = *G*(*M* + *M*'), which is approximately *n*^2^
*a*^3^ = *GM*' for a small body in orbit around a much more massive one
(*M* \<\< *M*'). In terms of ![](chap1-Z-G-D-12.gif) and *n* the
spin-orbit Lagrangian is

<div align="left">

![](chap2-Z-G-100.gif)

</div>

This is a problem with one degree of freedom with terms that vary
periodically with time.

The Lagrange equations are derived in the usual manner:

<div align="left">

![](chap2-Z-G-101.gif)

</div>

The equation of motion is very similar to that of the periodically
driven pendulum. The main difference here is that not only is the
strength of the acceleration changing periodically, but in the
spin-orbit problem the center of attraction is also varying
periodically.

We can give a physical interpretation of this equation of motion. It
states that the rate of change of the angular momentum is equal to the
applied torque. The torque on the body arises because the body is out of
round and the gravitational force varies as the inverse square of the
distance. Thus the force per unit mass on the near side of the body is a
little more than the acceleration of the body as a whole, and the force
per unit mass on the far side of the body is a little less than the
acceleration of the body as a whole. Thus, relative to the acceleration
of the body as a whole, the far side is forced outward while the inner
part of the body is forced inward. The net effect is a torque on the
body that tries to align the long axis of the body with the line to the
external point mass. If ![](chap1-Z-G-D-19.gif) is a bit larger than *f*
then there is a negative torque, and if ![](chap1-Z-G-D-19.gif) is a bit
smaller than *f* then there is a positive torque, both of which would
align the long axis with the planet if given a fair chance. The torque
arises because of the difference of the inverse *R*^2^ force across the
body, so the torque is proportional to *R*^`-`3^. There is a torque only
if the body is out of round, for otherwise there is no handle to pull
on. This is reflected in the factor *B* `-` *A* in the expression for
the torque. The potential depends only on the moment of inertia, and
thus the body has the same dynamics if it is rotated by 180^o^. The
factor of 2 in the argument of sine reflects this symmetry. This torque
is called the \`\`gravity gradient torque.''

<div align="left">

![](chap2-Z-G-102.gif)

</div>

To compute the evolution requires a lot of detailed preparation similar
to what has been done for other problems. There are many interesting
phenomena to explore. We can take parameters appropriate for the Moon
and find that Mr. Moon does not constantly point the same face to the
Earth, but instead constantly shakes his head in dismay at what goes on
here. If we nudge the Moon a bit, say by hitting it with an asteroid, we
find that the long axis oscillates back and forth with respect to the
direction that points to the Earth. For the Moon, the orbital
eccentricity is currently about 0.05, and the out-of-roundness parameter
is about ![](chap1-Z-G-D-12.gif) = 0.026. Figure [2.11](#FIGURE_2.11)
shows the angle ![](chap1-Z-G-D-19.gif) `-` *f* as a function of time
for two different values of the \`\`lunar'' eccentricity. The plot spans
50 lunar orbits, or a little under four years. This Moon has been kicked
by a large asteroid and has initial rotational angular velocity
![](chap1-Z-G-D-20.gif) equal to 1.01 times the orbit frequency. The
initial orientation is ![](chap1-Z-G-D-19.gif) = 0. The smooth trace
shows the evolution if the orbital eccentricity is set to zero. We see
an oscillation with a period of about 40 lunar orbits or about three
years. The more wiggly trace shows the evolution of
![](chap1-Z-G-D-19.gif) `-` *f* with an orbital eccentricity of 0.05,
near the current lunar eccentricity. The lunar eccentricity superimposes
an apparent shaking of the face of the Moon back and forth with the
period of the lunar orbit. Though the Moon does slightly change its rate
of rotation during the course of its orbit, most of this shaking is due
to the nonuniform motion of the Moon in its elliptical orbit. This
oscillation, called the \`\`optical libration of the Moon,'' allows us
to see a bit more than half of the Moon's surface. The longer-period
oscillation induced by the kick is called the \`\`free libration of the
Moon.'' It is \`\`free'' because we are free to excite it by choosing
appropriate initial conditions. The mismatch of the orientation of the
Moon caused by the optical libration actually produces a periodic torque
on the Moon, which slightly speeds it up and slows it down during every
orbit. The resulting oscillation is called the \`\`forced libration of
the Moon,'' but it is too small to see in this plot.

The oscillation period of the free libration is easily calculated. We
see that the eccentricity of the orbit does not substantially affect the
period, so we consider the special case of zero eccentricity. In this
case *R* = *a*, a constant, and *f*(*t*) = *n* *t*, where *n* is the
orbital frequency (traditionally called the *mean motion*). The equation
of motion becomes

<div align="left">

![](chap2-Z-G-103.gif)

</div>

Let ![](chap1-Z-G-D-16.gif)(*t*) = ![](chap1-Z-G-D-19.gif)(*t*) `-` *n*
*t*, and consequently *D*![](chap1-Z-G-D-16.gif)(*t*) =
*D*![](chap1-Z-G-D-19.gif)(*t*) `-` *n*, and
*D*^2^![](chap1-Z-G-D-16.gif) = *D*^2^![](chap1-Z-G-D-19.gif).
Substituting these, the equation governing the evolution of
![](chap1-Z-G-D-16.gif) is

<div align="left">

![](chap2-Z-G-104.gif)

</div>

For small deviations from synchronous rotation (small
![](chap1-Z-G-D-16.gif)) this is

<div align="left">

![](chap2-Z-G-105.gif)

</div>

so we see that the small-amplitude oscillation frequency of
![](chap1-Z-G-D-16.gif) is *n*![](chap1-Z-G-D-12.gif). For the Moon,
![](chap1-Z-G-D-12.gif) is about 0.026, so the period is about 1/0.026
orbit periods or about 40 lunar orbit periods, which is what we
observed.

<div align="left">

![](chap2-Z-G-106.gif)

</div>

It is perhaps more fun to see what happens if the out-of-roundness
parameter is large. After our experience with the driven pendulum it is
no surprise that we find abundant chaos in the spin-orbit problem when
the system is strongly driven by having large ![](chap1-Z-G-D-12.gif)
and significant *e*. There is indeed one body in the solar system that
exhibits chaotic rotation -- Hyperion, a small satellite of Saturn.
Though our toy model is not adequate for a complete account of Hyperion,
we can show that it exhibits chaotic behavior for parameters appropriate
for Hyperion. We take ![](chap1-Z-G-D-12.gif) = 0.89 and *e* = 0.1.
Figure [2.12](#FIGURE_2.12) shows ![](chap1-Z-G-D-19.gif) `-` *f* for 50
orbits, starting with ![](chap1-Z-G-D-19.gif) = 0 and
![](chap1-Z-G-D-20.gif) = 1.05. We see that sometimes one face of the
body oscillates facing the planet, sometimes the other face oscillates
facing the planet, and sometimes the body rotates relative to the planet
in either direction.

If we relax our restriction that the spin axis be fixed perpendicular to
the orbit, then we find that the Moon maintains this orientation of the
spin axis even if nudged a bit, but for Hyperion the spin axis almost
immediately falls away from this configuration. The state in which
Hyperion on average points one face to Saturn is dynamically unstable to
chaotic tumbling. Observations of Hyperion have confirmed that it is
chaotically tumbling.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^15^](#call_footnote_Temp_204) The Legendre polynomials *P*~*l*~ may be
obtained by expanding the expression (1 + *y*^2^ `-` 2 *y* *x*)^`-`1/2^
as a power series in *y*. The coefficient of *y*^*l*^ is *P*~*l*~(*x*).
The first few Legendre polynomials are: *P*~0~(*x*) = 1, *P*~1~(*x*) =
*x*, *P*~2~(*x*) = (3/2) *x*^2^ `-` (1/2), and so on. The rest satisfy
the recurrence relation

<div align="left">

![](chap2-Z-G-84.gif)

</div>

[^16^](#call_footnote_Temp_205) This approximate representation of the
potential energy is sometimes called MacCullagh's formula.

[^17^](#call_footnote_Temp_206) Watch out, we just reused
![](chap1-Z-G-D-21.gif). It was also used as the constituent index.

[^18^](#call_footnote_Temp_208) Traditionally, the point in the orbit at
which the two bodies are closest is called the *pericenter* and the
angle *f* is called the *true anomaly*.

[^19^](#call_footnote_Temp_209) The given potential energy differs from
the actual potential energy in that non-constant terms that do not
depend on ![](chap1-Z-G-D-19.gif) and consequently do not affect the
evolution of ![](chap1-Z-G-D-19.gif) have been dropped.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-30.html)</span><span>,
[next](book-Z-H-32.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


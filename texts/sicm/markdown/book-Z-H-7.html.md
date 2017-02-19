<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-6.html)</span><span>, [next](book-Z-H-8.html)</span>
page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

 {.chapter}

<div class="chapterheading">

[Chapter 1](book-Z-H-4.html#%_toc_%_chap_1)

</div>

\
 [Lagrangian Mechanics](book-Z-H-4.html#%_toc_%_chap_1)

<div align="right">

+--------------------------------------------------------------------------+
| <span class="epigraph"> </span>                                          |
| The purpose of mechanics is to describe how bodies change their position |
| in space with \`\`time.'' I should load my conscience with grave sins    |
| against the sacred spirit of lucidity were I to formulate the aims of    |
| mechanics in this way, without serious reflection and detailed           |
| explanations. Let us proceed to disclose these sins.                     |
|                                                                          |
| Albert Einstein, *Relativity, the Special and General Theory*            |
| [[16](book-Z-H-80.html#cite{Einstein})], p. 9                            |
+--------------------------------------------------------------------------+

</div>

The subject of this book is motion and the mathematical tools used to
describe it.

Centuries of careful observations of the motions of the planets revealed
regularities in those motions, allowing accurate predictions of
phenomena such as eclipses and conjunctions. The effort to formulate
these regularities and ultimately to understand them led to the
development of mathematics and to the discovery that mathematics could
be effectively used to describe aspects of the physical world. That
mathematics can be used to describe natural phenomena is a remarkable
fact.

A pin thrown by a juggler takes a rather predictable path and rotates in
a rather predictable way. In fact, the skill of juggling depends
crucially on this predictability. It is also a remarkable discovery that
the same mathematical tools used to describe the motions of the planets
can be used to describe the motion of the juggling pin.

Classical mechanics describes the motion of a system of particles,
subject to forces describing their interactions. Complex physical
objects, such as juggling pins, can be modeled as myriad particles with
fixed spatial relationships maintained by stiff forces of interaction.

There are many conceivable ways a system could move that never occur. We
can imagine that the juggling pin might pause in midair or go fourteen
times around the head of the juggler before being caught, but these
motions do not happen. How can we distinguish motions of a system that
can actually occur from other conceivable motions? Perhaps we can invent
some mathematical function that allows us to distinguish realizable
motions from among all conceivable motions.

The motion of a system can be described by giving the position of every
piece of the system at each moment. Such a description of the motion of
the system is called a *configuration path*; the configuration path
specifies the configuration as a function of time. The juggling pin
rotates as it flies through the air; the configuration of the juggling
pin is specified by giving the position and orientation of the pin. The
motion of the juggling pin is specified by giving the position and
orientation of the pin as a function of time.

The function that we seek takes a configuration path as an input and
produces some output. We want this function to have some characteristic
behavior when the input is a realizable path. For example, the output
could be a number, and we could try to arrange that this number be zero
only on realizable paths. Newton's equations of motion are of this form;
at each moment Newton's differential equations must be satisfied.

However, there is an alternate strategy that provides more insight and
power: we could look for a path-distinguishing function that has a
minimum on the realizable paths -- on nearby unrealizable paths the
value of the function is higher than it is on the realizable path. This
is the *variational strategy*: for each physical system we invent a
path-distinguishing function that distinguishes realizable motions of
the system by having a stationary point for each realizable
path.[^1^](#footnote_Temp_8) For a great variety of systems realizable
motions of the system can be formulated in terms of a variational
principle.[^2^](#footnote_Temp_9)

Mechanics, as invented by Newton and others of his era, describes the
motion of a system in terms of the positions, velocities, and
accelerations of each of the particles in the system. In contrast to the
Newtonian formulation of mechanics, the variational formulation of
mechanics describes the motion of a system in terms of aggregate
quantities that are associated with the motion of the system as a whole.

In the Newtonian formulation the forces can often be written as
derivatives of the potential energy of the system. The motion of the
system is determined by considering how the individual component
particles respond to these forces. The Newtonian formulation of the
equations of motion is intrinsically a particle-by-particle description.

In the variational formulation the equations of motion are formulated in
terms of the difference of the kinetic energy and the potential energy.
The potential energy is a number that is characteristic of the
arrangement of the particles in the system; the kinetic energy is a
number that is determined by the velocities of the particles in the
system. Neither the potential energy nor the kinetic energy depends on
how those positions and velocities are specified. The difference is
characteristic of the system as a whole and does not depend on the
details of how the system is specified. So we are free to choose ways of
describing the system that are easy to work with; we are liberated from
the particle-by-particle description inherent in the Newtonian
formulation.

The variational formulation has numerous advantages over the Newtonian
formulation. The equations of motion for those parameters that describe
the state of the system are derived in the same way regardless of the
choice of those parameters: the method of formulation does not depend on
the choice of coordinate system. If there are positional constraints
among the particles of a system the Newtonian formulation requires that
we consider the forces maintaining these constraints, whereas in the
variational formulation the constraints can be built into the
coordinates. The variational formulation reveals the association of
conservation laws with symmetries. The variational formulation provides
a framework for placing any particular motion of a system in the context
of all possible motions of the system. We pursue the variational
formulation because of these advantages.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^1^](#call_footnote_Temp_8) A *stationary point* of a function is a
point where the function's value does not vary as the input is varied.
Local maxima or minima are stationary points.

[^2^](#call_footnote_Temp_9) The variational formulation successfully
describes all of the Newtonian mechanics of particles and rigid bodies.
The variational formulation has also been usefully applied in the
description of many other systems such as classical electrodynamics, the
dynamics of inviscid fluids, and the design of mechanisms such as
four-bar linkages. In addition, modern formulations of quantum mechanics
and quantum field theory build on many of the same concepts. However, it
appears that not all dynamical systems have a variational formulation.
For example, there is no simple prescription to apply the variational
apparatus to systems with dissipation, though in special cases
variational methods can still be used.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-6.html)</span><span>, [next](book-Z-H-8.html)</span>
page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


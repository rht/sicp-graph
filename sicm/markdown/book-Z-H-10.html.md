<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-9.html)</span><span>,
[next](book-Z-H-11.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[1.3  Generalized Coordinates](book-Z-H-4.html#%_toc_%_sec_1.3)
---------------------------------------------------------------

In order to be able to talk about specific configurations we need to
have a set of parameters that label the configurations. The parameters
used to specify the configuration of the system are called the
*generalized coordinates*. Consider an unconstrained free particle. The
configuration of the particle is specified by giving its position. This
requires three parameters. The unconstrained particle has three degrees
of freedom. One way to specify the position of a particle is to specify
its rectangular coordinates relative to some chosen coordinate axes. The
rectangular components of the position are generalized coordinates for
an unconstrained particle. Or consider an ideal planar double pendulum:
a point mass constrained to be a given distance from a fixed point by a
rigid rod, with a second mass constrained to be at a given distance from
the first mass by another rigid rod, all confined to a vertical plane.
The configuration is specified if the orientation of the two rods is
given. This requires at least two parameters; the planar double pendulum
has two degrees of freedom. One way to specify the orientation of each
rod is to specify the angle it makes with the vertical. These two angles
are generalized coordinates for the planar double pendulum.

The number of coordinates need not be the same as the dimension of the
configuration space, though there must be at least that many. We may
choose to work with more parameters than necessary, but then the
parameters will be subject to constraints that restrict the system to
possible configurations, that is, to elements of the configuration
space.

For the planar double pendulum described above, the two angle
coordinates are enough to specify the configuration. We could also take
as generalized coordinates the rectangular coordinates of each of the
masses in the plane, relative to some chosen coordinate axes. These are
also fine coordinates, but we would have to explicitly keep in mind the
constraints that limit the possible configurations to the actual
geometry of the system. Sets of coordinates with the same dimension as
the configuration space are easier to work with because we do not have
to deal with explicit constraints among the coordinates. So for the time
being we will consider only formulations where the number of
configuration coordinates is equal to the number of degrees of freedom;
later we will learn how to handle systems with redundant coordinates and
explicit constraints.

In general, the configurations form a space *M* of some dimension *n*.
The *n*-dimensional configuration space can be parameterized by choosing
a coordinate function ![](chap1-Z-G-D-8.gif) that maps elements of the
configuration space to *n*-tuples of real numbers. If there is more than
one dimension, the function ![](chap1-Z-G-D-8.gif) is a tuple of *n*
independent coordinate functions[^19^](#footnote_Temp_30)
![](chap1-Z-G-D-8.gif)^*i*^, *i* = 0,`...`, *n* `-` 1, where each
![](chap1-Z-G-D-8.gif)^*i*^ is a real-valued function defined on some
region of the configuration space.[^20^](#footnote_Temp_31) For a given
configuration *m* in the configuration space *M* the values
![](chap1-Z-G-D-8.gif)^*i*^(*m*) of the coordinate functions are the
generalized coordinates of the configuration. These generalized
coordinates permit us to identify points of the *n*-dimensional
configuration space with *n*-tuples of real
numbers.[^21^](#footnote_Temp_32) For any given configuration space,
there are a great variety of ways to choose generalized coordinates.
Even for a single point moving without constraints, we can choose
rectangular coordinates, polar coordinates, or any other coordinate
system that strikes our fancy.

The motion of the system can be described by a configuration path
![](chap1-Z-G-D-1.gif) mapping time to configuration-space points.
Corresponding to the configuration path is a *coordinate path* *q* =
![](chap1-Z-G-D-8.gif) o ![](chap1-Z-G-D-1.gif) mapping time to tuples
of generalized coordinates. If there is more than one degree of freedom
the coordinate path is a structured object: *q* is a tuple of component
coordinate path functions *q*^*i*^ = ![](chap1-Z-G-D-8.gif)^*i*^ o
![](chap1-Z-G-D-1.gif). At each instant of time *t*, the values *q*(*t*)
= ( *q*^0^(*t*), `...`, *q*^*n*`-`1^(*t*) ) are the generalized
coordinates of a configuration.

The derivative *Dq* of the coordinate path *q* is a
function[^22^](#footnote_Temp_33) that gives the rate of change of the
configuration coordinates at a given time: *Dq*(*t*) = ( *Dq*^0^(*t*),
`...`, *Dq*^*n*`-`1^(*t*) ). The rate of change of a generalized
coordinate is called a *generalized velocity*.

We can make coordinate representations for higher derivatives of the
path as well. We introduce the function ![](chap1-Z-G-5.gif) (pronounced
\`\`chart'') that extends a coordinate representation to the local
tuple:[^23^](#footnote_Temp_34)

<div align="left">

![](chap1-Z-G-9.gif)

</div>

where *q* = ![](chap1-Z-G-D-8.gif) o ![](chap1-Z-G-D-1.gif). The
function ![](chap1-Z-G-10.gif)~![](chap1-Z-G-D-8.gif)~ takes the
coordinate-free local tuple ( *t*, ![](chap1-Z-G-D-1.gif)(*t*),
![](chap1-Z-G-D-7.gif)![](chap1-Z-G-D-1.gif)(*t*), `...` ) and gives a
coordinate representation as a tuple of the time, the value of the
coordinate path function at that time, and the values of as many
derivatives of the coordinate path function as are needed.

Given a coordinate path *q* = ![](chap1-Z-G-D-8.gif) o
![](chap1-Z-G-D-1.gif), the rest of the local tuple can be computed from
it. We introduce a function ![](chap1-Z-G-D-9.gif) that does this:

<div align="left">

![](chap1-Z-G-11.gif)

</div>

The function ![](chap1-Z-G-D-9.gif)[*q*] depends only on the coordinate
path *q* and its derivatives; the function ![](chap1-Z-G-D-9.gif)[*q*]
does not depend on ![](chap1-Z-G-D-8.gif) or the fact that *q* is made
by composing ![](chap1-Z-G-D-8.gif) with ![](chap1-Z-G-D-1.gif). From
relations ([1.5](#EQUATION_1.5)) and ([1.6](#EQUATION_1.6)) we find

<div align="left">

![](chap1-Z-G-12.gif)

</div>

**Exercise 1.3.**  **Generalized coordinates**\
 For each of the systems in exercise [1.2](book-Z-H-9.html#%_thm_1.2),
specify a system of generalized coordinates that can be used to describe
the behavior of the system.

#### [Lagrangians in generalized coordinates](book-Z-H-4.html#%_toc_%_sec_Temp_36)

The action is a property of a configuration path segment for a
particular Lagrangian ![](chap1-Z-G-D-5.gif). The action does not depend
on the coordinate system that is used to label the configurations. We
can use this property to find a coordinate representation
*L*~![](chap1-Z-G-D-8.gif)~ for the Lagrangian ![](chap1-Z-G-D-5.gif).

The action is

<div align="left">

![](chap1-Z-G-13.gif)

</div>

The Lagrangian ![](chap1-Z-G-D-5.gif) is a function of the local tuple
![](chap1-Z-G-D-6.gif)[![](chap1-Z-G-D-1.gif)](*t*) = ( *t*,
![](chap1-Z-G-D-1.gif)(*t*),
![](chap1-Z-G-D-7.gif)![](chap1-Z-G-D-1.gif)(*t*), `...` ). The local
tuple has the coordinate representation ![](chap1-Z-G-D-9.gif)[*q*] =
![](chap1-Z-G-14.gif)~![](chap1-Z-G-D-8.gif)~ o
![](chap1-Z-G-D-6.gif)[![](chap1-Z-G-D-1.gif)] , where *q* =
![](chap1-Z-G-D-8.gif) o ![](chap1-Z-G-D-1.gif). So if we
choose[^24^](#footnote_Temp_37)

<div align="left">

![](chap1-Z-G-16.gif)

</div>

then[^25^](#footnote_Temp_38)

<div align="left">

![](chap1-Z-G-19.gif)

</div>

On the left we have the composition of functions that use the
intermediary of a coordinate representation; on the right we have the
composition of two functions that do not involve coordinates. We define
the coordinate representation of the action to be

<div align="left">

![](chap1-Z-G-20.gif)

</div>

The function *S*~![](chap1-Z-G-D-8.gif)~ takes a coordinate path; the
function ![](chap1-Z-G-D-4.gif) takes a configuration path. Since the
integrands are the same by equation ([1.10](#EQUATION_1.10)), the
integrals have the same value:

<div align="left">

![](chap1-Z-G-21.gif)

</div>

So we have a way of constructing coordinate representations of a
Lagrangian that gives the same action for a path in any coordinate
system.

For Lagrangians that depend only on positions and velocities the action
can also be written

<div align="left">

![](chap1-Z-G-22.gif)

</div>

The coordinate system used in the definition of a Lagrangian or an
action is usually unambiguous, so the subscript ![](chap1-Z-G-D-8.gif)
will usually be dropped.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^19^](#call_footnote_Temp_30) A tuple of functions that all have the
same domain is itself a function on that domain: Given a point in the
domain, the value of the tuple of functions is a tuple of the values of
the component functions at that point.

[^20^](#call_footnote_Temp_31) The use of superscripts to index the
coordinate components is traditional, even though there is potential
confusion, say, with exponents. We use zero-based indexing.

[^21^](#call_footnote_Temp_32) More precisely, the generalized
coordinates identify open subsets of the configuration space with open
subsets of **R**^*n*^. It may require more than one set of generalized
coordinates to cover the entire configuration space. For example, if the
configuration space is a two-dimensional sphere, we could have one set
of coordinates that maps (a little more than) the northern hemisphere to
a disk, and another set that maps (a little more than) the southern
hemisphere to a disk, with a strip near the equator common to both
coordinate systems. A space that can be locally parameterized by smooth
coordinate functions is called a *differentiable manifold*. The theory
of differentiable manifolds can be used to formulate a coordinate-free
treatment of variational mechanics. An introduction to mechanics from
this perspective can be found
in [[2](book-Z-H-80.html#cite{Abraham-Marsden})] or
[[5](book-Z-H-80.html#cite{Arnold80})].

[^22^](#call_footnote_Temp_33) The derivative of a function *f* is a
function, denoted *Df*. Our notational convention is that *D* is a
high-precedence operator. Thus *D* operates on the adjacent function
before any other application occurs: *Df*(*x*) is the same as
(*Df*)(*x*).

[^23^](#call_footnote_Temp_34) The formal definition of
![](chap1-Z-G-6.gif) is unimportant to the discussion, but if you really
want to know here is one way to do it: First, we define the derivative
![](chap1-Z-G-D-7.gif) ![](chap1-Z-G-D-1.gif) of a configuration path
![](chap1-Z-G-D-1.gif) in terms of ordinary derivatives by specifying
how it acts on sufficiently smooth real-valued functions *f* of
configurations: (![](chap1-Z-G-D-7.gif)^*n*^
![](chap1-Z-G-D-1.gif))(*t*)(*f*) = *D*^*n*^ (*f* o
![](chap1-Z-G-D-1.gif))(*t*) . Then we define
![](chap1-Z-G-7.gif)~![](chap1-Z-G-D-8.gif)~(*a*, *b*, *c*, *d*, `...`)
= ( *a*, ![](chap1-Z-G-D-8.gif)(*b*), *c*(![](chap1-Z-G-D-8.gif)),
*d*(![](chap1-Z-G-D-8.gif)), `...` ). With this definition:

<div align="left">

![](chap1-Z-G-8.gif)

</div>

[^24^](#call_footnote_Temp_37) The coordinate function
![](chap1-Z-G-D-8.gif) is locally invertible, and so is
![](chap1-Z-G-15.gif)~![](chap1-Z-G-D-8.gif)~.

[^25^](#call_footnote_Temp_38) ![](chap1-Z-G-D-5.gif) o
![](chap1-Z-G-D-6.gif)[![](chap1-Z-G-D-1.gif)] = ![](chap1-Z-G-D-5.gif)
o ![](chap1-Z-G-17.gif)~![](chap1-Z-G-D-8.gif)~^`-`1^ o
![](chap1-Z-G-18.gif)~![](chap1-Z-G-D-8.gif)~ o
![](chap1-Z-G-D-6.gif)[![](chap1-Z-G-D-1.gif)] =
*L*~![](chap1-Z-G-D-8.gif)~ o
![](chap1-Z-G-D-9.gif)[![](chap1-Z-G-D-8.gif) o ![](chap1-Z-G-D-1.gif)]
= *L*~![](chap1-Z-G-D-8.gif)~ o ![](chap1-Z-G-D-9.gif)[*q*] .

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-9.html)</span><span>,
[next](book-Z-H-11.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


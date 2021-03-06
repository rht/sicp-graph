<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-64.html)</span><span>,
[next](book-Z-H-66.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[5.8  Hamilton-Jacobi Equation](book-Z-H-4.html#%_toc_%_sec_5.8)
----------------------------------------------------------------

If we could find a canonical transformation so that the transformed
Hamiltonian was identically zero, then by Hamilton's equations the new
coordinates and momenta would be constants. All of the time variation of
the solution would be captured in the canonical transformation, and
there would be nothing more to the solution. The mixed-variable
generating function that does this job satisfies a partial differential
equation called the Hamilton-Jacobi equation. In most cases, the
Hamilton-Jacobi equation cannot be solved explicitly. When it can be
solved, however, the Hamilton-Jacobi equation provides a means of
reducing a problem to a useful simple form.

Recall the relations satisfied by an *F*~2~-type generating function:

<div align="left">

![](chap5-Z-G-325.gif)

</div>

If we require the new Hamiltonian to be zero, then *F*~2~ must satisfy
the equation

<div align="left">

![](chap5-Z-G-326.gif)

</div>

So the solution of the problem is \`\`reduced'' to the problem of
solving an *n*-dimensional partial differential equation for *F*~2~ with
unspecified new (constant) momenta *p*'. This is the Hamilton-Jacobi
equation, and in some cases we can solve it.

We can also attempt a somewhat less drastic method of solution. Rather
than try to find an *F*~2~ that makes the new Hamiltonian identically
zero, we can seek an *F*~2~-shaped function *W* that gives a new
Hamiltonian that is solely a function of the new momenta. A system
described by this form of Hamiltonian is also easy to solve. So if we
set

<div align="left">

![](chap5-Z-G-327.gif)

</div>

and are able to solve for *W*, then the problem is essentially solved.
In this case, the primed momenta are all constant and the primed
positions are linear in time. This is an alternate form of the
Hamilton-Jacobi equation.

These forms are related. Suppose that we have a *W* that satisfies the
second form of the Hamilton-Jacobi equation ([5.361](#EQUATION_5.361)).
Then the *F*~2~ constructed from *W*

<div align="left">

![](chap5-Z-G-328.gif)

</div>

satisfies the first form of the Hamilton-Jacobi
equation ([5.360](#EQUATION_5.360)). Furthermore,

<div align="left">

![](chap5-Z-G-329.gif)

</div>

so the primed momenta are the same in the two formulations. But

<div align="left">

![](chap5-Z-G-330.gif)

</div>

so we see that the primed coordinates differ by a term that is linear in
time -- both *p*'(*t*) = *p*'~0~ and *q*'(*t*) = *q*'~0~ are constant.
Thus we can use either *W* or *F*~2~ as the generating function,
depending on the form of the new Hamiltonian we want.

Note that if *H* is time independent then we can often find a
time-independent *W* that does the job. For time-independent *W* the
Hamilton-Jacobi equation simplifies to

<div align="left">

![](chap5-Z-G-331.gif)

</div>

The corresponding *F*~2~ is then linear in time. Notice that an implicit
requirement is that the energy can be written as a function of the new
momenta alone. This excludes the possibility that the transformed
phase-space coordinates *q*' and *p*' are simply initial conditions for
*q* and *p*.

It turns out that there is flexibility in the choice of the function
*E*. With an appropriate choice the phase-space coordinates obtained
through the transformation generated by *W* are action-angle
coordinates.

**Exercise 5.23.**  **Hamilton-Jacobi with *F*~1~**\

We have used an *F*~2~-type generating function to carry out the
Hamilton-Jacobi transformations. Carry out the equivalent
transformations with an *F*~1~-type generating function. Find the
equations corresponding to equations ([5.360](#EQUATION_5.360)),
([5.361](#EQUATION_5.361)), and ([5.365](#EQUATION_5.365)).

### [5.8.1  Harmonic Oscillator](book-Z-H-4.html#%_toc_%_sec_5.8.1)

Consider the familiar time-independent Hamiltonian

<div align="left">

![](chap5-Z-G-332.gif)

</div>

We form the Hamilton-Jacobi equation for this problem:

<div align="left">

![](chap5-Z-G-333.gif)

</div>

Using *F*~2~(*t*, *x*, *p*') = *W*(*t*, *x*, *p*') `-` *E*(*p*') *t*, we
find

<div align="left">

![](chap5-Z-G-334.gif)

</div>

Writing this out explicitly yields

<div align="left">

![](chap5-Z-G-335.gif)

</div>

and solving for ![](front-Z-G-D-2.gif)~1~ *W* gives

<div align="left">

![](chap5-Z-G-336.gif)

</div>

Integrating gives the desired *W*:

<div align="left">

![](chap5-Z-G-337.gif)

</div>

We can use either *W* or the corresponding *F*~2~ as the generating
function. First, take *W* to be the generating function. We obtain the
coordinate transformation by differentiating:

<div align="left">

![](chap5-Z-G-338.gif)

</div>

and then integrating to get

<div align="left">

![](chap5-Z-G-339.gif)

</div>

with some integration constant *C*(*p*'). Inverting this, we get the
unprimed coordinate in terms of the primed coordinate and momentum:

<div align="left">

![](chap5-Z-G-340.gif)

</div>

The new Hamiltonian *H*' depends only on the momentum:

<div align="left">

![](chap5-Z-G-341.gif)

</div>

The equations of motion are just

<div align="left">

![](chap5-Z-G-342.gif)

</div>

with solution

<div align="left">

![](chap5-Z-G-343.gif)

</div>

for initial conditions *x*'~0~ and *p*'~0~. If we plug these expressions
for *x*'(*t*) and *p*'(*t*) into equation ([5.374](#EQUATION_5.374)) we
find

<div align="left">

![](chap5-Z-G-344.gif)

</div>

where the angular frequency is ![](chap1-Z-G-D-23.gif) = (*k*/*m*)^1/2^,
the amplitude is *A* = (2*E*(*p*')/*k*)^1/2^, and the phase is
![](chap1-Z-G-D-16.gif) = `-` ![](chap1-Z-G-D-23.gif) *t*~0~ =
![](chap1-Z-G-D-23.gif) (*x*'~0~ `-` *C*(*p*'))/*DE*(*p*').

We can also use *F*~2~ = *W* `-` *E* *t* as the generating function. The
new Hamiltonian is zero, so both *x*' and *p*' are constant, but the
relationship between the old and new variables is

<div align="left">

![](chap5-Z-G-345.gif)

</div>

Plugging in the solution *x*' = *x*'~0~ and *p*' = *p*'~0~ and solving
for *x*, we find equation ([5.378](#EQUATION_5.378)). So once again we
see that the two approaches are equivalent.

It is interesting to note that the solution depends upon the constants
*E*(*p*') and *DE*(*p*'), but otherwise the motion is not dependent in
any essential way on what the function *E* actually is. The momentum
*p*' is constant and the values of the constants are set by the initial
conditions. Given a particular function *E*, the initial conditions
determine *p*', but the solution can be obtained without further
specifying the *E* function.

If we choose particular functions *E* we can get particular canonical
transformations. For example, a convenient choice is simply

<div align="left">

![](chap5-Z-G-346.gif)

</div>

for some constant ![](chap1-Z-G-D-21.gif) that will be chosen later. We
find

<div align="left">

![](chap5-Z-G-347.gif)

</div>

So we see that a convenient choice is ![](chap1-Z-G-D-21.gif) =
![](chap1-Z-G-D-23.gif) = (*k*/*m*)^1/2^, so

<div align="left">

![](chap5-Z-G-348.gif)

</div>

with *ß* = (*km*)^1/2^. The new Hamiltonian is

<div align="left">

![](chap5-Z-G-349.gif)

</div>

The solution are just *x*' = ![](chap1-Z-G-D-23.gif) *t* + *x*'~0~ and
*p*' = *p*'~0~. Substituting the expression for *x* in terms of *x*' and
*p*' into *H*(*t*, *x*, *p*) = *H*'(*t*, *x*', *p*'), we derive

<div align="left">

![](chap5-Z-G-350.gif)

</div>

The two transformation equations ([5.382](#EQUATION_5.382)) and
([5.383](#EQUATION_5.383)) are what we have called the polar-canonical
transformation (equation [5.34](book-Z-H-59.html#EQUATION_5.34)). We
have already shown that this transformation is canonical and that it
solves the harmonic oscillator, but it was not derived. Here we have
derived this transformation as a particular case of the solution of the
Hamilton-Jacobi equation.

We can also explore other choices for the *E* function. For example, we
could choose

<div align="left">

![](chap5-Z-G-351.gif)

</div>

Following the same steps as before, we find

<div align="left">

![](chap5-Z-G-352.gif)

</div>

So a convenient choice is again ![](chap1-Z-G-D-21.gif) =
![](chap1-Z-G-D-23.gif), leaving

<div align="left">

![](chap5-Z-G-353.gif)

</div>

with *ß* = (*km*)^1/4^. By construction, this transformation is also
canonical and also brings the harmonic oscillator problem into an easily
solvable form:

<div align="left">

![](chap5-Z-G-354.gif)

</div>

The harmonic oscillator Hamiltonian has been transformed to what looks a
lot like the Hamiltonian for a free particle. This is very interesting.
Notice that whereas Hamiltonian ([5.383](#EQUATION_5.383)) does not have
a well defined Legendre transform to an equivalent Lagrangian, the
\`\`free particle'' harmonic oscillator has a well defined Legendre
transform:

<div align="left">

![](chap5-Z-G-355.gif)

</div>

Of course, there may be additional properties that make one choice more
useful than others for particular applications.

**Exercise 5.24.**  **Pendulum**\

Solve the Hamilton-Jacobi equation for the pendulum; investigate both
the circulating and oscillating regions of phase space. (Note: This is a
long story and requires some knowledge of elliptic functions.)

### [5.8.2  Kepler Problem](book-Z-H-4.html#%_toc_%_sec_5.8.2)

We can use the Hamilton-Jacobi equation to find canonical coordinates
that solve the Kepler problem. This is an essential first step in doing
perturbation theory for orbital problems.

In rectangular coordinates (*x*, *y*, *z*), the Kepler Hamiltonian is

<div align="left">

![](chap5-Z-G-356.gif)

</div>

where *r*^2^ = *x*^2^ + *y*^2^ + *z*^2^ and *p*^2^ = *p*~*x*~^2^ +
*p*~*y*~^2^ + *p*~*z*~^2^. The Kepler problem describes the relative
motion of two bodies; it is also encountered in the formulation of other
problems involving orbital motion, such as the *n*-body problem.

We try a generating function of the form *W*(*t*; *x*, *y*, *z*;
*p*'~*x*~, *p*'~*y*~, *p*'~*z*~). The Hamilton-Jacobi equation is
then[^30^](#footnote_Temp_403)

<div align="left">

![](chap5-Z-G-357.gif)

</div>

This is a partial differential equation in the three partial derivatives
of *W*. We stare at it a while and give up.

Next we try converting to spherical coordinates. This is motivated by
the fact that the potential energy depends only on *r*. The Hamiltonian
in spherical coordinates (*r*, ![](chap1-Z-G-D-19.gif),
![](chap1-Z-G-D-16.gif)), where ![](chap1-Z-G-D-19.gif) is the
colatitude and ![](chap1-Z-G-D-16.gif) is the longitude, is

<div align="left">

![](chap5-Z-G-358.gif)

</div>

The Hamilton-Jacobi equation is

<div align="left">

![](chap5-Z-G-359.gif)

</div>

We can solve the Hamilton-Jacobi equation by successively isolating the
dependence on the various variables. Looking first at the
![](chap1-Z-G-D-16.gif) dependence, we see that, outside of *W*,
![](chap1-Z-G-D-16.gif) appears only in one partial derivative. If we
write

<div align="left">

![](chap5-Z-G-360.gif)

</div>

then ![](front-Z-G-D-2.gif)~1,2~*W*(*t*; *r*, ![](chap1-Z-G-D-19.gif),
![](chap1-Z-G-D-16.gif); *p*'~0~, *p*'~1~, *p*'~2~) = *p*'~2~, and then
![](chap1-Z-G-D-16.gif) does not appear in the remaining equation for
*f*:

<div align="left">

![](chap5-Z-G-361.gif)

</div>

Any function of the *p*'~*i*~ could have been used as the coefficient of
![](chap1-Z-G-D-16.gif) in the generating function. This particular
choice has the nice feature that *p*'~2~ is the *z* component of the
angular momentum.

We can eliminate the ![](chap1-Z-G-D-19.gif) dependence if we choose

<div align="left">

![](chap5-Z-G-362.gif)

</div>

and require that ![](chap5-Z-G-D-15.gif) be a solution to

<div align="left">

![](chap5-Z-G-363.gif)

</div>

We are free to choose the right-hand side to be any function of the new
momenta. This choice reflects the fact that the left-hand side is
non-negative. It turns out that *p*'~1~ is the total angular momentum.
This equation for ![](chap5-Z-G-D-15.gif) can be solved by quadrature.

The remaining equation that determines *R* is

<div align="left">

![](chap5-Z-G-364.gif)

</div>

which also can be solved by quadrature.

Altogether the solution of the Hamilton-Jacobi equation reads

<div align="left">

![](chap5-Z-G-365.gif)

</div>

It is interesting that our solution to the Hamilton-Jacobi partial
differential equation is of the form

<div align="left">

![](chap5-Z-G-366.gif)

</div>

Thus we have a separation-of-variables technique that involves writing
the solution as a sum of functions of the individual variables. This
might be contrasted with the separation-of-variables technique
encountered in elementary quantum mechanics and classical
electrodynamics, which uses products of functions of individual
variables. However, integrable problems in classical mechanics are rare,
so it would be incorrect to think of this method as a general solution
method.

The coordinates *q*' = (*q*^/\\ 0^, *q*^/\\ 1^, *q*^/\\ 2^) conjugate to
the momenta *p*' = [*p*'~0~, *p*'~1~, *p*'~2~] are

<div align="left">

![](chap5-Z-G-367.gif)

</div>

We are still free to choose the functional form of *E*. A convenient
(and conventional) choice is

<div align="left">

![](chap5-Z-G-368.gif)

</div>

With this choice the momentum *p*'~0~ has dimensions of angular
momentum, and the conjugate coordinate is an angle.

The Hamiltonian for the Kepler problem is reduced to

<div align="left">

![](chap5-Z-G-369.gif)

</div>

Thus

<div align="left">

![](chap5-Z-G-370.gif)

</div>

where *n* = *m* µ^2^ / (*p*'~0~)^3^ and where *ß*^0^, *ß*^1^, and *ß*^2^
are the initial values of the components of *q*'. Only one of the new
variables changes with time.[^31^](#footnote_Temp_404)

### [5.8.3  *F*~2~ and the Lagrangian](book-Z-H-4.html#%_toc_%_sec_5.8.3)

The solution to the Hamilton-Jacobi equation, the mixed-variable
generating function that generates time evolution, is related to the
action used in the variational principle. In particular, the time
derivative of the generating function along realizable paths has the
same value as the Lagrangian.

Let ![](chap1-Z-G-D-47.gif)~2~ (*t*) = *F*~2~(*t*, *q*(*t*), *p*'(*t*))
be the value of *F*~2~ along the paths *q* and *p*' at time *t*. The
derivative of ![](chap1-Z-G-D-47.gif)~2~ is

<div align="left">

![](chap5-Z-G-371.gif)

</div>

where we have used the relation for *p* in terms of *F*~2~ in the first
term. Using the Hamilton-Jacobi equation ([5.360](#EQUATION_5.360)),
this becomes

<div align="left">

![](chap5-Z-G-372.gif)

</div>

On realizable paths we have *Dp*'(*t*) = 0, so along realizable paths
the time derivative of *F*~2~ is the same as the Lagrangian along the
path. The time integral of the Lagrangian along any path is the action
along that path. This means that, up to an additive term that is
constant on realizable paths but may be a function of the transformed
phase-space coordinates *q*' and *p*', the *F*~2~ that solves the
Hamilton-Jacobi equation has the same value as the Lagrangian action for
realizable paths.

The same conclusion follows for the Hamilton-Jacobi equation formulated
in terms of *F*~1~. Up to an additive term that is constant on
realizable paths but may be a function of the transformed phase-space
coordinates *q*' and *p*', the *F*~1~ that solves the corresponding
Hamilton-Jacobi equation has the same value as the Lagrangian action for
realizable paths.

Recall that a transformation given by an *F*~2~-type generating function
is also given by an *F*~1~-type generating function related to it by a
Legendre transform (see equation
[5.195](book-Z-H-63.html#EQUATION_5.195)):

<div align="left">

![](chap5-Z-G-373.gif)

</div>

provided the transformations are nonsingular. In this case, both *q*'
and *p*' are constant on realizable paths, so the additive constants
that make *F*~1~ and *F*~2~ equal to the Lagrangian action differ by
*q*' *p*'.

**Exercise 5.25.**  **Harmonic oscillator**\

Let's check this for the harmonic oscillator (of course).

**a**.  Finish the integral ([5.371](#EQUATION_5.371)):

<div align="left">

![](chap5-Z-G-374.gif)

</div>

Write the result in terms of the amplitude *A* = (2*E*(*p*')/*k*)^1/2^.

**b**.  Check that this generating function gives the transformation

<div align="left">

![](chap5-Z-G-375.gif)

</div>

which is the same as equation ([5.373](#EQUATION_5.373)) for a
particular choice of the integration constant. The other part of the
transformation is

<div align="left">

![](chap5-Z-G-376.gif)

</div>

with the same definition of *A* as before.

**c**.  Compute the time derivative of the associated *F*~2~ along
realizable paths (*Dp*'(*t*) = 0), and compare to the Lagrangian along
realizable paths.

### [5.8.4  The Action Generates Time Evolution](book-Z-H-4.html#%_toc_%_sec_5.8.4)

We define the function ![](chap5-Z-G-D-16.gif)(*t*~1~, *q*~1~, *t*~2~,
*q*~2~) to be the value of the action for a realizable path *q* such
that *q*(*t*~1~) = *q*~1~ and *q*(*t*~2~) = *q*~2~. So
![](chap5-Z-G-D-16.gif) satisfies

<div align="left">

![](chap5-Z-G-377.gif)

</div>

For variations ![](chap1-Z-G-D-13.gif) that are not necessarily zero at
the end times and for realizable paths *q*, the variation of the action
is

<div align="left">

![](chap5-Z-G-378.gif)

</div>

Alternatively, the variation of *S*[*q*] in
equation ([5.409](#EQUATION_5.409)) gives

<div align="left">

![](chap5-Z-G-379.gif)

</div>

Comparing equations ([5.410](#EQUATION_5.410)) and
([5.411](#EQUATION_5.411)) and using the fact that the variation
![](chap1-Z-G-D-13.gif) is arbitrary, we find

<div align="left">

![](chap5-Z-G-380.gif)

</div>

The partial derivatives of ![](chap5-Z-G-D-16.gif) with respect to the
coordinate arguments give the momenta. Abstracting off paths, we have

<div align="left">

![](chap5-Z-G-381.gif)

</div>

This looks a bit like the *F*~1~-type generating function relations, but
here there are two times.

Given a realizable path *q* such that *q*(*t*~1~) = *q*~1~ and
*q*(*t*~2~) = *q*~2~, we get the partial derivatives with respect to the
time slots:

<div align="left">

![](chap5-Z-G-382.gif)

</div>

Therefore

<div align="left">

![](chap5-Z-G-383.gif)

</div>

and similarly

<div align="left">

![](chap5-Z-G-384.gif)

</div>

These are a pair of the Hamilton-Jacobi equations, computed at the
endpoints of the path. Solving equations ([5.413](#EQUATION_5.413)) for
*q*~2~ and *p*~2~ as functions of *t*~2~ and the initial state *t*~1~,
*q*~1~, *p*~1~, we get the time evolution of the system in terms of
![](chap5-Z-G-D-16.gif). The function ![](chap5-Z-G-D-16.gif) generates
time evolution.

The function ![](chap5-Z-G-D-16.gif) can be written in terms of the
*F*~2~ or *F*~1~ that solves the Hamilton-Jacobi equation. We can
compute time evolution by using the *F*~2~ solution of the
Hamilton-Jacobi equation to express the state (*t*~1~, *q*~1~, *p*~1~)
in terms of the constants *q*' and *p*' at a given time *t*~1~. We can
then perform a subsequent transformation back from *q*' *p*' to the
original state variables at a different time *t*~2~, giving the state
(*t*~2~, *q*~2~, *p*~2~). The composition of canonical transformations
is canonical. The generating function for the composition is the
difference of the generating functions for each step:

<div align="left">

![](chap5-Z-G-385.gif)

</div>

with the condition

<div align="left">

![](chap5-Z-G-386.gif)

</div>

which allows us to eliminate *p*'.

**Exercise 5.26.**  **Uniform acceleration**\

\
**a**.  Compute the Lagrangian action, as a function of the endpoints
and times, for a uniformly accelerated particle. Use this to construct
the canonical transformation for time evolution from a given initial
state.

**b**.  Solve the Hamilton-Jacobi equation for the uniformly accelerated
particle, obtaining the *F*~2~ that makes the transformed Hamiltonian
zero. Show that the Lagrangian action can be expressed as a difference
of two applications of this *F*~2~.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^30^](#call_footnote_Temp_403) Remember that
![](front-Z-G-D-2.gif)~1,0~ means the derivative with respect to the
first coordinate position.

[^31^](#call_footnote_Temp_404) The canonical phase-space coordinates
can be written in terms of the parameters that specify an orbit. We
merely summarize the results; for further explanation see
[[36](book-Z-H-80.html#cite{Plummer})] or
[[38](book-Z-H-80.html#cite{Almanac})].

Assume we have a bound orbit with semimajor axis *a*, eccentricity *e*,
inclination *i*, longitude of ascending node ![](chap1-Z-G-D-57.gif),
argument of pericenter ![](chap1-Z-G-D-23.gif), and mean anomaly *M*.
The three canonical momenta are *p*'~0~ = (*m* µ *a*)^1/2^, *p*'~1~ =
(*m* µ *a* (1 `-` *e*^2^))^1/2^, and *p*'~2~ = (*m* µ *a* (1 `-`
*e*^2^))^1/2^ cos *i*. The first momentum is related to the energy, the
second momentum is the total angular momentum, and the third momentum is
the component of the angular momentum in the ![](chap2-Z-G-D-7.gif)
direction. The conjugate canonical coordinates are (*q*')^0^ = *M*,
(*q*')^1^ = ![](chap1-Z-G-D-23.gif), and (*q*')^2^ =
![](chap1-Z-G-D-57.gif).

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-64.html)</span><span>,
[next](book-Z-H-66.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


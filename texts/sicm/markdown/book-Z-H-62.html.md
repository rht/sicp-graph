<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-61.html)</span><span>,
[next](book-Z-H-63.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[5.5  Reduced Phase Space](book-Z-H-4.html#%_toc_%_sec_5.5)
-----------------------------------------------------------

Suppose we have a system with *n* + 1 degrees of freedom described by a
time-independent Hamiltonian in a (2*n* + 2)-dimensional phase space.
Here we can play the converse game: we can choose any generalized
coordinate to play the role of \`\`time'' and the negation of its
conjugate momentum to play the role of a new *n*-degree-of-freedom
time-dependent Hamiltonian in a *reduced phase space* of 2*n*
dimensions.

More precisely, let

<div align="left">

![](chap5-Z-G-119.gif)

</div>

and suppose we have a system described by a time-independent Hamiltonian

<div align="left">

![](chap5-Z-G-120.gif)

</div>

For each solution path there is a conserved quantity *E*. Let's choose a
coordinate *q*^*n*^ to be the time in a reduced phase space. We define
the dynamical variables for the *n*-degree-of-freedom reduced phase
space:

<div align="left">

![](chap5-Z-G-121.gif)

</div>

In the original phase space a coordinate such as *q*^*n*^ maps time to a
coordinate. In the formulation of the reduced phase space we will have
to use the inverse function ![](chap2-Z-G-D-22.gif) = (*q*^*n*^)^`-`1^
to map the coordinate to the time, giving the new coordinates in terms
of the new time

<div align="left">

![](chap5-Z-G-122.gif)

</div>

and thus

<div align="left">

![](chap5-Z-G-123.gif)

</div>

We propose that a Hamiltonian in the reduced phase space is the negative
of the inverse of *f*(*q*^0^, ..., *q*^*n*^; *p*~0~, ..., *p*~*n*~) =
*E* with respect to the *p*~*n*~ argument:

<div align="left">

![](chap5-Z-G-124.gif)

</div>

Note that in the reduced phase space we will have indices for the
structured variables in the range 0 `...` *n* `-` 1, whereas in the
original phase space the indices are in the range 0 `...` *n*. We will
show that *H*~*r*~ is an appropriate Hamiltonian for the given dynamical
system in the reduced phase space. To compute Hamilton's equations we
must expand the implicit definition of *H*~*r*~. We define an auxiliary
function

<div align="left">

![](chap5-Z-G-125.gif)

</div>

Note that *by construction* this function is identically a constant *g*
= *E*. Thus all of its partial derivatives are zero:

<div align="left">

![](chap5-Z-G-126.gif)

</div>

where we have suppressed the arguments. Solving for partials of
*H*~*r*~, we get

<div align="left">

![](chap5-Z-G-127.gif)

</div>

Using these relations, we can deduce the Hamilton's equations in the
reduced phase space from the Hamilton's equations in the original phase
space:

<div align="left">

![](chap5-Z-G-128.gif)

</div>

#### [Orbits in a central field](book-Z-H-4.html#%_toc_%_sec_Temp_365)

Consider planar motion in a central field. We have already seen this
expressed in polar coordinates in
equation ([3.99](book-Z-H-40.html#EQUATION_3.99)):

<div align="left">

![](chap5-Z-G-129.gif)

</div>

There are two degrees of freedom and the Hamiltonian is time
independent. Thus the energy, the value of the Hamiltonian, is conserved
on realizable paths. Let's forget about time and reparameterize this
system in terms of the orbital radius *r*.[^16^](#footnote_Temp_366) To
do this we solve

<div align="left">

![](chap5-Z-G-130.gif)

</div>

for *p*~*r*~, obtaining

<div align="left">

![](chap5-Z-G-131.gif)

</div>

which is the Hamiltonian in the reduced phase space.

Hamilton's equations are now quite simple:

<div align="left">

![](chap5-Z-G-132.gif)

</div>

We see that *p*~![](chap1-Z-G-D-16.gif)~ is independent of *r* (as it
was with *t*), so for any particular orbit we may define a constant
angular momentum *L*. Thus our problem ends up as a simple quadrature:

<div align="left">

![](chap5-Z-G-133.gif)

</div>

To see the utility of this procedure, we continue our example with a
definite potential energy -- a gravitating mass point:

<div align="left">

![](chap5-Z-G-134.gif)

</div>

When we substitute this into equation ([5.139](#EQUATION_5.139)) we
obtain a mess that can be simplified to

<div align="left">

![](chap5-Z-G-135.gif)

</div>

Integrating this, we obtain another mess, which can be simplified and
rearranged to obtain the following:

<div align="left">

![](chap5-Z-G-136.gif)

</div>

This can be recognized as the polar-coordinate form of the equation of a
conic section with eccentricity *e* and parameter *p*:

<div align="left">

![](chap5-Z-G-137.gif)

</div>

where

<div align="left">

![](chap5-Z-G-138.gif)

</div>

In fact, if the orbit is an ellipse with semimajor axis *a*, we have

<div align="left">

![](chap5-Z-G-139.gif)

</div>

and so we can identify the role of energy and angular momentum in
shaping the ellipse:

<div align="left">

![](chap5-Z-G-140.gif)

</div>

What we get from analysis in the reduced phase space is the geometry of
the trajectory, but we lose the time-domain behavior. The reduction is
often worth the price.

Although we have treated time in a special way so far, we have found
that time is not special. It can be included in the coordinates to make
a driven system autonomous. And it can be eliminated from any autonomous
system in favor of any other coordinate. This leads to numerous
strategies for simplifying problems, by removing time variation and then
performing canonical transforms on the resulting conservative autonomous
system to make a nice coordinate that we can then dump back into the
role of time.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^16^](#call_footnote_Temp_366) We could have chosen to reparameterize
in terms of ![](chap1-Z-G-D-16.gif), but then both *p*~*r*~ and *r*
would occur in the resulting time-independent Hamiltonian. The path we
have chosen takes advantage of the fact that ![](chap1-Z-G-D-16.gif)
does not appear in our Hamiltonian, so *p*~![](chap1-Z-G-D-16.gif)~ is a
constant of the motion. This structure suggests that to solve this kind
of problem we need to look ahead, as in playing chess.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-61.html)</span><span>,
[next](book-Z-H-63.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


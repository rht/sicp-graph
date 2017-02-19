<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-71.html)</span><span>,
[next](book-Z-H-73.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[6.1  Perturbation Theory with Lie Series](book-Z-H-4.html#%_toc_%_sec_6.1)
---------------------------------------------------------------------------

Given a system, we look for a decomposition of the Hamiltonian in the
form

<div align="left">

![](chap6-Z-G-2.gif)

</div>

where *H*~0~ is solvable. We assume that the Hamiltonian has no explicit
time dependence; this can be ensured by going to the extended phase
space if necessary. We also assume that a canonical transformation has
been made so that *H*~0~ depends solely on the momenta:

<div align="left">

![](chap6-Z-G-3.gif)

</div>

We carry out a Lie transformation and find the conditions that the Lie
generator *W* must satisfy to eliminate the
order-![](chap1-Z-G-D-12.gif) terms from the Hamiltonian.

The Lie transform and associated Lie series specify a canonical
transformation:

<div align="left">

![](chap6-Z-G-4.gif)

</div>

where *Q* = *I*~1~ and *P* = *I*~2~ are the coordinate and momentum
selectors and *I* is the identity function. Recall the definitions

<div align="left">

![](chap6-Z-G-5.gif)

</div>

with *L*~*W*~ *F* = { *F*, *W* }.

Applying the Lie transformation to *H* gives us

<div align="left">

![](chap6-Z-G-6.gif)

</div>

The first-order term in ![](chap1-Z-G-D-12.gif) is zero if *W* satisfies
the condition

<div align="left">

![](chap6-Z-G-7.gif)

</div>

which is a linear partial differential equation for *W*. The transformed
Hamiltonian is

<div align="left">

![](chap6-Z-G-8.gif)

</div>

where we have used condition ([6.7](#EQUATION_6.7)) to simplify the
![](chap1-Z-G-D-12.gif)^2^ contribution.

This basic step of perturbation theory has eliminated terms of a certain
order (order ![](chap1-Z-G-D-12.gif)) from the Hamiltonian, but in doing
so has generated new terms of higher order (here
![](chap1-Z-G-D-12.gif)^2^ and higher).

At this point we can find an approximate solution by truncating
Hamiltonian ([6.8](#EQUATION_6.8)) to *H*~0~, which is solvable. The
approximate solution for given initial conditions (*t*~0~, *q*~0~,
*p*~0~) is obtained by finding the corresponding (*t*~0~, *q*'~0~,
*p*'~0~) using the inverse of transformation ([6.4](#EQUATION_6.4)).
Then the system is evolved to time *t* using the solutions of the
truncated Hamiltonian *H*~0~, giving the state (*t*, *q*', *p*'). The
phase-space coordinates of the evolved point are transformed back to the
original variables using the transformation ([6.4](#EQUATION_6.4)) to
state (*t*, *q*, *p*). The approximate solution is

<div align="left">

![](chap6-Z-G-9.gif)

</div>

If the Lie transform *E*'~![](chap1-Z-G-D-12.gif),\\ *W*~ =
*e*^![](chap1-Z-G-D-12.gif)\\ *L*~*W*~^ must be evaluated by summing the
series, then we must specify the order to which the sum extends.

Assuming everything goes okay, we can imagine repeating this process to
eliminate the order-![](chap1-Z-G-D-12.gif)^2^ terms and so on, bringing
the transformed Hamiltonian as close as we like to *H*~0~.
Unfortunately, there are complications. We can understand some of these
complications and how to deal with them by considering some specific
applications.

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-71.html)</span><span>,
[next](book-Z-H-73.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


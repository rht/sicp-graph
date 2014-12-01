<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-73.html)</span><span>,
[next](book-Z-H-75.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[6.3  Many Degrees of Freedom](book-Z-H-4.html#%_toc_%_sec_6.3)
---------------------------------------------------------------

Other problems are encountered in applying perturbation theory to
systems with more than a single degree of freedom. Consider a
Hamiltonian of the form

<div align="left">

![](chap6-Z-G-46.gif)

</div>

where *H*~0~ depends only on the momenta and so is solvable. We assume
that the Hamiltonian has no explicit time dependence. We further assume
that the coordinates are all angles and that *H*~1~ is a multiply
periodic function of the coordinates.

Carrying out a Lie transformation with generator *W* produces the
Hamiltonian

<div align="left">

![](chap6-Z-G-47.gif)

</div>

as before. The condition that the order-![](chap1-Z-G-D-12.gif) terms
are eliminated is

<div align="left">

![](chap6-Z-G-48.gif)

</div>

a linear partial differential equation. By assumption, the Hamiltonian
*H*~0~ depends only on the momenta. We define

<div align="left">

![](chap6-Z-G-49.gif)

</div>

the tuple of frequencies of the unperturbed system. The condition on *W*
is

<div align="left">

![](chap6-Z-G-50.gif)

</div>

As *H*~1~ is a multiply-periodic function of the coordinates, we can
write it as a Poisson series:[^1^](#footnote_Temp_426)

<div align="left">

![](chap6-Z-G-51.gif)

</div>

Similarly, we assume *W* can be written as a Poisson series:

<div align="left">

![](chap6-Z-G-52.gif)

</div>

Substituting these into the condition that order-![](chap1-Z-G-D-12.gif)
terms are eliminated, we find

<div align="left">

![](chap6-Z-G-53.gif)

</div>

The cosines are orthogonal so each term must be individually zero. We
deduce

<div align="left">

![](chap6-Z-G-54.gif)

</div>

and that the required Lie generator is

<div align="left">

![](chap6-Z-G-55.gif)

</div>

There are a couple of problems. First, if *A*~0~ is nonzero then the
expression for *B*~0~ involves a division by zero. So the expression for
*B*~0~ is not correct. The problem is that the corresponding term in
*H*~1~ does not involve ![](chap1-Z-G-D-19.gif). So the integration for
*B*~0~ should introduce linear terms in ![](chap1-Z-G-D-19.gif). But
this is the same situation that led to the secular terms in the
perturbation approximation to the pendulum. Having learned our lesson
there, we avoid the secular terms by adjoining this term to the solvable
Hamiltonian and excluding *k* = 0 from the sum for *W*. We have

<div align="left">

![](chap6-Z-G-56.gif)

</div>

and

<div align="left">

![](chap6-Z-G-57.gif)

</div>

Another problem is that there are many opportunities for small
denominators that would make the perturbation large and therefore not a
perturbation. As we saw in the perturbation approximation for the
pendulum in terms of the rotor, we must exclude certain regions from the
domain of applicability of the perturbation approximation. These
excluded regions are associated with commensurabilities among the
frequencies ![](chap1-Z-G-D-23.gif)~0~(*p*). Consider the phase-space
transformation of the coordinates

<div align="left">

![](chap6-Z-G-58.gif)

</div>

So we must exclude from the domain of applicability all regions for
which the coefficients are large. If the second term dominates, the
excluded regions satisfy

<div align="left">

![](chap6-Z-G-59.gif)

</div>

Considering the fact that for any tuple of frequencies
![](chap1-Z-G-D-23.gif)~0~(*p*') we can find a tuple of integers *k*
such that *k* · ![](chap1-Z-G-D-23.gif)(*p*') is arbitrarily small, this
problem of *small divisors* looks very serious.

However, the problem, though serious, is not as bad as it may appear,
for a couple of reasons. First, it may be that *A*~*k*~ ne 0 only for
certain *k*. In this case, only the regions for these terms are excluded
from the domain of applicability. Second, for analytic functions the
magnitude of *A*~*k*~ decreases strongly with the size of *k* (see
[[4](book-Z-H-80.html#cite{Arnold63})]):

<div align="left">

![](chap6-Z-G-60.gif)

</div>

for some positive *ß* and *C*, and where | *k* |~+~ = | *k*~0~ | + |
*k*~1~ | + `···` . At any stage of a perturbation approximation we can
limit consideration to just those terms that are larger than a specified
magnitude. The size of the excluded region corresponding to a term is of
order square root of |*A*~*k*~(*p*')| and the
inequality ([6.51](#EQUATION_6.51)) shows that |*A*~*k*~(*p*')|
decreases exponentially with the order of the term.

### [6.3.1  Driven Pendulum as a Perturbed Rotor](book-Z-H-4.html#%_toc_%_sec_6.3.1)

More concretely, consider the periodically driven pendulum. We will
develop approximate solutions for the driven pendulum as a perturbed
rotor.

We use the Hamiltonian

<div align="left">

![](chap6-Z-G-61.gif)

</div>

We can remove the explicit time dependence by going to the extended
phase space. The Hamiltonian is

<div align="left">

![](chap6-Z-G-62.gif)

</div>

with the constants ![](chap1-Z-G-D-21.gif) = *ml*^2^, *ß* = *mlg*, and
![](chap1-Z-G-D-1.gif) = (1/2) *m* *l* *A* ![](chap1-Z-G-D-23.gif)^2^ .

With the intent to approximate the driven pendulum as a perturbed rotor,
we choose

<div align="left">

![](chap6-Z-G-63.gif)

</div>

Notice that the perturbation *H*~1~ has only three terms in its Poisson
series, so in the first perturbation step only three regions will be
excluded from the domain of applicability. The perturbation *H*~1~ is
particularly simple: it has only three terms, and the coefficients are
constants.

The Lie series generator that eliminates the terms in *H*~1~ to first
order in ![](chap1-Z-G-D-12.gif), satisfying

<div align="left">

![](chap6-Z-G-64.gif)

</div>

is

<div align="left">

![](chap6-Z-G-65.gif)

</div>

where ![](chap1-Z-G-D-23.gif)~*r*~(*p*) = ![](front-Z-G-D-2.gif)~2,0~
*H*~0~(![](chap2-Z-G-D-22.gif); ![](chap1-Z-G-D-19.gif), *t*; *p*,
*p*~*t*~) = *p*/![](chap1-Z-G-D-21.gif) is the unperturbed rotor
frequency.

The resulting approximate solution has three regions in which there are
small denominators, and so three regions that are excluded from
applicability of the perturbative solution. Regions of phase space for
which ![](chap1-Z-G-D-23.gif)~*r*~(*p*) is near 0,
![](chap1-Z-G-D-23.gif), and `-` ![](chap1-Z-G-D-23.gif) are excluded.
Away from these regions the perturbative solution works well, just as in
the rotor approximation for the pendulum. Unfortunately, some of the
more interesting regions of the phase space of the driven pendulum are
excluded: the region in which we find the remnant of the undriven
pendulum is excluded, as are the two resonance regions in which the
rotation of the pendulum is synchronous with the drive. We need to
develop methods for approximating these regions.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^1^](#call_footnote_Temp_426) In general, we need to include sine terms
as well, but the cosine expansion is enough for this illustration.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-73.html)</span><span>,
[next](book-Z-H-75.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


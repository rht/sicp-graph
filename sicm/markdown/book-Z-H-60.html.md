<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-59.html)</span><span>,
[next](book-Z-H-61.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[5.3  Invariants of Canonical Transformations](book-Z-H-4.html#%_toc_%_sec_5.3)
-------------------------------------------------------------------------------

Canonical transformations allow us to change the phase-space coordinate
system that we use to express a problem, preserving the form of
Hamilton's equations. If we solve Hamilton's equations in one
phase-space coordinate system we can use the transformation to carry the
solution to the other coordinate system. What other properties are
preserved by a canonical transformation?

#### [Noninvariance of *p* *v*](book-Z-H-4.html#%_toc_%_sec_Temp_349)

We noted in equation ([5.10](book-Z-H-58.html#EQUATION_5.10)) that
canonical extensions of point transformations preserve the value of *p*
*v*. This does not hold for more general canonical transformations. We
can illustrate this with the transformation just considered. Along
corresponding paths *x*, *p*~*x*~ and ![](chap1-Z-G-D-19.gif), *I*

<div align="left">

![](chap5-Z-G-63.gif)

</div>

and so *Dx* is

<div align="left">

![](chap5-Z-G-64.gif)

</div>

The difference of *p* *v* and the transformed *p*' *v*' is

<div align="left">

![](chap5-Z-G-65.gif)

</div>

In general this is not zero. The product *pv* is not necessarily
invariant under general canonical transformations.

#### [Invariance of Poisson brackets](book-Z-H-4.html#%_toc_%_sec_Temp_350)

Here is a remarkable fact: the composition of the Poisson bracket of two
phase-space state functions with a canonical transformation is the same
as the Poisson bracket of each of the two functions composed with the
transformation separately. Loosely speaking, the Poisson bracket is
invariant under canonical phase-space transformations.

Let *f* and *g* be two phase-space state functions. Using the
![](chap5-Z-G-D-1.gif) representation of the Poisson bracket (see
section [5.2.4](book-Z-H-59.html#%_sec_5.2.4)), we deduce

<div align="left">

![](chap5-Z-G-66.gif)

</div>

where the fact that *C* is symplectic and satisfies
equation ([5.52](book-Z-H-59.html#EQUATION_5.52)) was used in the
middle. Abstracted to functions of phase-space states, this is

<div align="left">

![](chap5-Z-G-67.gif)

</div>

#### [Volume preservation](book-Z-H-4.html#%_toc_%_sec_Temp_351)

Consider a canonical transformation *C*. Let ![](chap5-Z-G-D-4.gif)~*t*~
be a function with parameter *t* such that (*q*, *p*) =
![](chap5-Z-G-D-4.gif)~*t*~(*q*', *p*') if (*t*, *q*, *p*) = *C*(*t*,
*q*', *p*'). The function ![](chap5-Z-G-D-4.gif)~*t*~ maps phase-space
coordinates to alternate phase-space coordinates at a given time.
Consider regions *R* in (*q*, *p*) and *R*' in (*q*', *p*') such that
*R* = ![](chap5-Z-G-D-4.gif)~*t*~(*R*'). The volume of region *R*' is

<div align="left">

![](chap5-Z-G-68.gif)

</div>

where ![](chap3-Z-G-D-8.gif) is the function whose value is one for
every input. Now if *C* is symplectic then the determinant of *D*
![](chap5-Z-G-D-4.gif)~*t*~ is one (see
section [4.2](book-Z-H-50.html#%_sec_4.2)), so

<div align="left">

![](chap5-Z-G-69.gif)

</div>

Thus, phase-space volume is preserved by symplectic transformations.

Liouville's theorem shows that time evolution preserves phase-space
volume. Here we see that canonical transformations also preserve phase
volumes. Later, we will find that time evolution actually generates a
canonical transformation.

#### [A bilinear form preserved by symplectic transformations](book-Z-H-4.html#%_toc_%_sec_Temp_352)

The invariance of Poisson brackets under canonical transformations can
be used to prove the invariance of another closely related antisymmetric
bilinear form under canonical transformations.
Define[^11^](#footnote_Temp_353)

<div align="left">

![](chap5-Z-G-71.gif)

</div>

where *Q* = *I*~1~ and *P* = *I*~2~ are the coordinate and momentum
selectors, respectively. The arguments ![](chap2-Z-G-D-10.gif)~1~ and
![](chap2-Z-G-D-10.gif)~2~ are incremental phase-space states. Under a
canonical transformation *s* = *C*(*s*'), incremental states transform
with the derivative

<div align="left">

![](chap5-Z-G-72.gif)

</div>

We will show that

<div align="left">

![](chap5-Z-G-73.gif)

</div>

provided the ![](chap2-Z-G-D-10.gif)~*i*~' have zero time component.

Condition ([5.27](book-Z-H-59.html#EQUATION_5.27)) that a
time-independent *C* with compositional Hamiltonian *H* is canonical is
equivalent to the symplectic
condition ([5.31](book-Z-H-59.html#EQUATION_5.31)), which does not
mention the Hamiltonian *H*. So for time-independent symplectic *C*,
condition ([5.27](book-Z-H-59.html#EQUATION_5.27)) is also satisfied
with the Hamiltonian replaced by any function *f* on the phase-state
space:

<div align="left">

![](chap5-Z-G-74.gif)

</div>

We will use this in the following.

In terms of ![](chap1-Z-G-D-23.gif), the Poisson bracket is

<div align="left">

![](chap5-Z-G-75.gif)

</div>

as can be seen by writing out the components. We use the fact that
Poisson brackets are invariant under canonical transformations:

<div align="left">

![](chap5-Z-G-76.gif)

</div>

The left-hand side of equation ([5.76](#EQUATION_5.76)) is

<div align="left">

![](chap5-Z-G-77.gif)

</div>

where we have used the relation ([5.74](#EQUATION_5.74)). The right-hand
side of equation ([5.76](#EQUATION_5.76)) is

<div align="left">

![](chap5-Z-G-78.gif)

</div>

Now the left-hand side must equal the right-hand side for any *f* and
*g*, so the equation must also be true for arbitrary
![](chap2-Z-G-D-10.gif)~*i*~' of the form

<div align="left">

![](chap5-Z-G-79.gif)

</div>

The ![](chap2-Z-G-D-10.gif)'~*i*~ are arbitrary incremental states with
zero time components.

So we have proven that

<div align="left">

![](chap5-Z-G-80.gif)

</div>

for canonical *C* and incremental states ![](chap2-Z-G-D-10.gif)'~*i*~
with zero time components. Using equation ([5.72](#EQUATION_5.72)), we
have

<div align="left">

![](chap5-Z-G-81.gif)

</div>

Thus the bilinear antisymmetric function ![](chap1-Z-G-D-23.gif) is
invariant under canonical transformations.

As a program, ![](chap1-Z-G-D-23.gif) is

`(define (omega zeta1 zeta2)   (- (* (momentum zeta2) (coordinate zeta1))      (* (momentum zeta1) (coordinate zeta2)))) `

We can check that it is invariant under the polar to rectangular
canonical transformation by computing the residuals. We use the
arbitrary state

`(define a-polar-state   (up 't       (up 'r 'phi)       (down 'pr 'pphi))) `

and the typical state increments

`(define zeta1    (up 0        (up 'dr1 'dphi1)       (down 'dpr1 'dpphi1)))  (define zeta2    (up 0        (up 'dr2 'dphi2)       (down 'dpr2 'dpphi2))) `

Note that the time components of `zeta1` and `zeta2` are zero. We
evaluate the residual:

`(print-expression   (let ((DCs ((D (F->CT p->r)) a-polar-state)))     (- (omega zeta1 zeta2)        (omega (* DCs zeta1) (* DCs zeta2))))) 0 `

The residual is zero so ![](chap1-Z-G-D-23.gif) is invariant under this
canonical transformation.

#### [Poincaré integral invariants](book-Z-H-4.html#%_toc_%_sec_Temp_354)

Consider the oriented area of a region *R*' in phase space (see
figure [5.2](book-Z-H-1000.html#FIGURE_5.2)). Suppose we make a
canonical transformation from coordinates (*q*', *p*') to (*q*, *p*)
taking region *R*' to region *R*. The boundary of the region in the
transformed coordinates is just the image under the canonical
transformation of the original boundary. Let *R*~*q*^*i*^,\\ *p*~*i*~~
be the projection of the region *R* onto the *q*^*i*^, *p*~*i*~ plane of
coordinate *q*^*i*^ and conjugate momentum *p*~*i*~, and let *A*~*i*~ be
its area. We call the *q*^*i*^, *p*~*i*~ plane the *i*th *canonical
plane* in these phase-space variables. Similarly, let
*R*'~*q*'^*i*^,\\ *p*'~*i*~~ be the projection of *R*' onto the
*q*'^*i*^, *p*'~*i*~ plane, and let *A*'~*i*~ be its area. Then it turns
out that the sums of the areas of the projections of *R* and of *R*' are
the same:

<div align="left">

![](chap5-Z-G-82.gif)

</div>

That is, the sum of the projected areas on the canonical planes is
preserved by canonical transformations. Another way to say this is

<div align="left">

![](chap5-Z-G-83.gif)

</div>

<div align="left">

![](chap5-Z-G-84.gif)

</div>

To see why this is true, we first consider how the area of an
incremental parallelogram in phase space transforms under canonical
transformation. Let (![](chap1-Z-G-D-43.gif) *q*,
![](chap1-Z-G-D-43.gif) *p*) and (![](chap1-Z-G-D-17.gif) *q*,
![](chap1-Z-G-D-17.gif) *p*) be small increments in phase space,
originating at (*q*, *p*). Consider the incremental parallelogram with
vertex at (*q*, *p*) with these two phase-space increments as edges. The
sum of the areas of the canonical projections of this incremental
parallelogram can be written

<div align="left">

![](chap5-Z-G-85.gif)

</div>

The right-hand side is the sum of the areas on the canonical planes; for
each *i* the area of a parallelogram is computed from the components of
the vectors defining its adjacent sides. Let ![](chap2-Z-G-D-10.gif)~1~
= (0 , ![](chap1-Z-G-D-43.gif) *q*, ![](chap1-Z-G-D-43.gif) *p*) and
![](chap2-Z-G-D-10.gif)~2~ = (0 , ![](chap1-Z-G-D-17.gif) *q*,
![](chap1-Z-G-D-17.gif) *p*); then the sum of the areas of the
incremental parallelograms is just

<div align="left">

![](chap5-Z-G-86.gif)

</div>

where ![](chap1-Z-G-D-23.gif) is the bilinear antisymmetric function
introduced in equation ([5.71](#EQUATION_5.71)). The function
![](chap1-Z-G-D-23.gif) is invariant under canonical transformations, so
the sum of the areas of the incremental parallelograms is invariant
under canonical transformations.

The area of an arbitrary region is just the limit of the sum of the
areas of incremental parallelograms that cover the region, so the sum of
oriented areas is preserved by canonical transformations:

<div align="left">

![](chap5-Z-G-87.gif)

</div>

We define an *action-like region* to be one for which canonical
coordinates can be chosen so that the region is entirely in the subspace
spanned by a particular canonical pair *q*^*i*^, *p*~*i*~. For this
coordinate system the projection on that plane has all of the area. The
projections on the other canonical planes have no area. So the sum of
the areas of the canonical projections is just the area of the region
itself. The sum of the areas of the projections onto canonical planes is
preserved under canonical transformation, so the area of an action-like
region is the sum of the areas of the canonical projections for any
canonical coordinate system.

There are also regions that have no action-like projection. For example,
a region in the plane *q*^*i*^, *q*^*j*^ has no action-like projection.
Therefore the sum of the areas of the canonical projections is zero, and
this is the case for any canonical coordinate system, though in other
canonical coordinates some of the projections may have nonzero area to
be balanced by negative area of others.

The equality-of-areas relation ([5.83](#EQUATION_5.83)) can also be
written as an equality of line integrals using Stokes's theorem, for
simply-connected regions *R*~*q*^*i*^,\\ *p*~*i*~~ and
*R*'~*q*'^*i*^,\\ *p*'~*i*~~:

<div align="left">

![](chap5-Z-G-88.gif)

</div>

The canonical planes are disjoint except at the origin, so the projected
areas intersect in at most one point. Thus we may independently
accumulate the line integrals around the boundaries of the individual
projections of the region onto the canonical planes into a line integral
around the unprojected region:

<div align="left">

![](chap5-Z-G-89.gif)

</div>

**Exercise 5.9.**  **Watch out**\

Consider the canonical transformation *C*:

<div align="left">

![](chap5-Z-G-90.gif)

</div>

**a**.  Show that the transformation is symplectic for any *a*.

**b**.  Show that equation ([5.88](#EQUATION_5.88)) is not generally
satisfied for the region enclosed by a curve of constant *J*.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^11^](#call_footnote_Temp_353) The ![](chap1-Z-G-D-23.gif) form can
also be written as a sum over degrees of freedom:

<div align="left">

![](chap5-Z-G-70.gif)

</div>

Notice that the contributions for each *i* do not mix components from
different degrees of freedom.

This bilinear form is closely related to the symplectic 2-form of
differential geometry. It differs in that the symplectic 2-form is
formally a function of the phase-space point as well as the incremental
vectors.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-59.html)</span><span>,
[next](book-Z-H-61.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


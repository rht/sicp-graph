<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-37.html)</span><span>,
[next](book-Z-H-39.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[3.2  Poisson Brackets](book-Z-H-4.html#%_toc_%_sec_3.2)
--------------------------------------------------------

Here we introduce the *Poisson bracket*, in terms of which Hamilton's
equations have an elegant and symmetric expression. Consider a function
*F* of time, coordinates, and momenta. The value of *F* along the path
![](chap3-Z-G-D-5.gif)(*t*) = ( *t*, *q*(*t*), *p*(*t*) ) is (*F* o
![](chap3-Z-G-D-5.gif))(*t*) = *F*(*t*, *q*(*t*), *p*(*t*)). The time
derivative of *F* o ![](chap3-Z-G-D-5.gif) is

<div align="left">

![](chap3-Z-G-85.gif)

</div>

If the phase-space path is a realizable path for a system with
Hamiltonian *H*, then *Dq* and *Dp* can be reexpressed using Hamilton's
equations:

<div align="left">

![](chap3-Z-G-86.gif)

</div>

where the Poisson bracket { *F* , *H* } of *F* and *H* is defined
by[^17^](#footnote_Temp_253)

<div align="left">

![](chap3-Z-G-88.gif)

</div>

Note that the Poisson bracket of two functions on the phase-state space
is also a function on the phase-state space.

The coordinate selector *Q* = *I*~1~ is an example of a function on
phase-state space: *Q*(*t*, *q*, *p*) = *q*. According to
equation ([3.79](#EQUATION_3.79)),

<div align="left">

![](chap3-Z-G-89.gif)

</div>

but this is the same as Hamilton's equation

<div align="left">

![](chap3-Z-G-90.gif)

</div>

Similarly, the momentum selector *P* = *I*~2~ is a function on
phase-state space: *P*(*t*, *q*, *p*) = *p*. We have

<div align="left">

![](chap3-Z-G-91.gif)

</div>

which is the same as Hamilton's other equation

<div align="left">

![](chap3-Z-G-92.gif)

</div>

So the Poisson bracket provides a uniform way of writing Hamilton's
equations:

<div align="left">

![](chap3-Z-G-93.gif)

</div>

The Poisson bracket of any function with itself is zero, so we recover
the conservation of energy for a system that has no explicit time
dependence:

<div align="left">

![](chap3-Z-G-94.gif)

</div>

#### [Properties of the Poisson bracket](book-Z-H-4.html#%_toc_%_sec_Temp_254)

Let *F*, *G*, and *H* be functions of time, position, and momentum, and
let *c* be independent of position and momentum.

The Poisson bracket is antisymmetric:

<div align="left">

![](chap3-Z-G-95.gif)

</div>

It is bilinear (linear in each argument):

<div align="left">

![](chap3-Z-G-96.gif)

</div>

The Poisson bracket satisfies Jacobi's identity:

<div align="left">

![](chap3-Z-G-97.gif)

</div>

All but the last of ([3.87](#EQUATION_3.87)-[3.92](#EQUATION_3.92)) can
immediately be verified from the definition. Jacobi's identity requires
a little more effort to verify. We can use the computer to avoid some
work. Define some literal phase-space functions of Hamiltonian type:

`(define F   (literal-function 'F     (-> (UP Real (UP Real Real) (DOWN Real Real)) Real)))  (define G   (literal-function 'G      (-> (UP Real (UP Real Real) (DOWN Real Real)) Real)))  (define H    (literal-function 'H      (-> (UP Real (UP Real Real) (DOWN Real Real)) Real))) `

Then we check the Jacobi identity:

`(print-expression  ((+ (Poisson-bracket F (Poisson-bracket G H))      (Poisson-bracket G (Poisson-bracket H F))      (Poisson-bracket H (Poisson-bracket F G)))   (up 't (up 'x 'y) (down 'px 'py)))) 0 `

The residual is zero, so the Jacobi identity is satisfied for any three
phase-space state functions with two degrees of freedom.

#### [Poisson brackets of conserved quantities](book-Z-H-4.html#%_toc_%_sec_Temp_255)

The Poisson bracket of conserved quantities is conserved. Let *F* and
*G* be time-independent phase-space state functions:
![](front-Z-G-D-2.gif)~0~ *F* = ![](front-Z-G-D-2.gif)~0~ *G* = 0. If
*F* and *G* are conserved by the evolution under *H* then

<div align="left">

![](chap3-Z-G-98.gif)

</div>

So the Poisson brackets of *F* and *G* with *H* are zero: { *F*, *H*} =
{ *G*, *H*} = 0. The Jacobi identity then implies

<div align="left">

![](chap3-Z-G-99.gif)

</div>

and thus

<div align="left">

![](chap3-Z-G-100.gif)

</div>

so { *F*, *G* } is a conserved quantity. The Poisson bracket of two
conserved quantities is also a conserved quantity.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^17^](#call_footnote_Temp_253) In traditional notation the Poisson
bracket is written

<div align="left">

![](chap3-Z-G-87.gif)

</div>

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-37.html)</span><span>,
[next](book-Z-H-39.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


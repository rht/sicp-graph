<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-15.html)</span><span>,
[next](book-Z-H-17.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[1.9  Abstraction of Path Functions](book-Z-H-4.html#%_toc_%_sec_1.9)
---------------------------------------------------------------------

An essential step in the derivation of the local-tuple transformation
function *C* from the coordinate transformation *F* was the deduction of
the relationship between the velocities in the two coordinate systems.
We did this by inserting coordinate paths into the coordinate
transformation function *F*, differentiating, and then generalizing the
results on the path to arbitrary velocities at a moment. The last step
is an example of a more general problem of abstracting a local-tuple
function from a path function. Given a function *f* of a local tuple, a
corresponding path-dependent function ![](chap1-Z-G-D-51.gif)[*q*] is
![](chap1-Z-G-D-51.gif)[*q*] = *f* o ![](chap1-Z-G-D-9.gif)[*q*]. Given
![](chap1-Z-G-D-51.gif), how can we reconstitute *f*? The local-tuple
function *f* depends on only a finite number of components of the local
tuple, and ![](chap1-Z-G-D-51.gif) depends only on the corresponding
local components of the path. So ![](chap1-Z-G-D-51.gif) has the same
value for all paths that have that number of components of the local
tuple in common. Given ![](chap1-Z-G-D-51.gif) we can reconstitute *f*
by taking the argument of *f*, which is a finite initial segment of a
local tuple, constructing a path that has this local description, and
finding the value of ![](chap1-Z-G-D-51.gif) for this path.

Two paths that have the same local description up to the *n*th
derivative are said to *osculate with order-*n* contact*. For example, a
path and the truncated power series representation of the path up to
order *n* have order-*n* contact; if fewer than *n* derivatives are
needed by a local-tuple function, the path and the truncated power
series representation are equivalent. Let *O* be a function that
generates an osculating path with the given local-tuple components. So
*O*(*t*, *q*, *v*, `...`)(*t*) = *q*, *D*(*O*(*t*, *q*, *v*,
`...`))(*t*) = *v*, and in general

<div align="left">

![](chap1-Z-G-210.gif)

</div>

The number of components of the local tuple that are required is finite,
but unspecified. One way of constructing *O* is through the truncated
power series

<div align="left">

![](chap1-Z-G-211.gif)

</div>

where the number of terms is the same as the number of components of the
local tuple that are specified.

Given the path function ![](chap1-Z-G-D-51.gif) we reconstitute the *f*
function as follows. We take the argument of *f* and construct an
osculating path with this local description. Then the value of *f* is
the value of ![](chap1-Z-G-D-51.gif) for this osculating path:

<div align="left">

![](chap1-Z-G-212.gif)

</div>

Let ![](chap1-Z-G-D-52.gif) be the function that takes a path function
and returns the corresponding local-tuple function:

<div align="left">

![](chap1-Z-G-213.gif)

</div>

From equation ([1.165](#EQUATION_1.165)) we see that

<div align="left">

![](chap1-Z-G-214.gif)

</div>

The procedure `Gamma-bar` implements the function
![](chap1-Z-G-D-52.gif) that reconstitutes a path-dependent function
into a local-tuple function:

`(define ((Gamma-bar f-bar) local)   ((f-bar (osculating-path local)) (time local))) `

The procedure `osculating-path` takes a number of local components and
returns a path with these components; it is implemented as a power
series.

We can use `Gamma-bar` to construct the procedure `F->C` that takes a
coordinate transformation `F` and generates the procedure that
transforms local tuples. The procedure `F->C` constructs a
path-dependent procedure `f-bar` that takes a coordinate path in the
primed system and returns the local tuple of the corresponding path in
the unprimed coordinate system. It then uses `Gamma-bar` to abstract
`f-bar` to arbitrary local tuples in the primed coordinate system.

`(define (F->C F)   (define (f-bar q-prime)     (define q       (compose F (Gamma q-prime)))     (Gamma q))   (Gamma-bar f-bar)) (show-expression    ((F->C p->r)    (->local 't (up 'r 'theta) (up 'rdot 'thetadot)))) `

------------------------------------------------------------------------

<div align="left">

![](chap1-Z-G-215.gif)

</div>

------------------------------------------------------------------------

Notice that in this definition of `F->C` we do not explicitly calculate
any derivatives. The calculation that led up to the state
transformation ([1.74](book-Z-H-13.html#EQUATION_1.74)) is not needed.

We can also use ![](chap1-Z-G-D-52.gif) to make an elegant formula for
computing the total time derivative *D*~*t*~ *F* of the function *F*:

<div align="left">

![](chap1-Z-G-216.gif)

</div>

The total time derivative can be expressed as a program:

`(define (Dt F)   (define (G-bar q)     (D (compose F (Gamma q))))   (Gamma-bar G-bar)) `

Given a procedure `F` implementing a local-tuple function and a path
`q`, we construct a new procedure `(compose F (Gamma q))`. The procedure
`G-bar` implements the derivative of this function of time. We then
abstract this off the path with `Gamma-bar` to give the total time
derivative.

**Exercise 1.31.**  **Velocity transformation**\
 Use the procedure `Gamma-bar` to construct a procedure that transforms
velocities given a coordinate transformation. Apply this procedure to
the procedure `p->r` to deduce (again)
equation ([1.65](book-Z-H-13.html#EQUATION_1.65)).

**Exercise 1.32.**  **Path functions and state functions**\
 The local-tuple function *f* is the same as the local-tuple function
![](chap1-Z-G-D-52.gif)(![](chap1-Z-G-D-51.gif)) where
![](chap1-Z-G-D-51.gif)[*q*] = *f* o ![](chap1-Z-G-D-9.gif)[*q*]. On the
other hand, the path function ![](chap1-Z-G-D-51.gif)[*q*] and the path
function ![](chap1-Z-G-D-52.gif)(![](chap1-Z-G-D-51.gif)) o
![](chap1-Z-G-D-9.gif)[*q*] are not necessarily the same. Explain. Give
examples where they are the same and where they are not the same. Write
programs to illustrate the behavior.

#### [Lagrange equations at a moment](book-Z-H-4.html#%_toc_%_sec_Temp_152)

Given a Lagrangian, the Lagrange equations test paths to determine
whether they are realizable paths of the system. The Lagrange equations
relate the path and its derivatives. The fact that the Lagrange
equations must be satisfied at each moment suggests that we can abstract
the Lagrange equations off the path and write them as relations among
the local-tuple components of realizable paths.

Let ![](chap1-Z-G-D-53.gif)[*L*] be the path-dependent function that
produces the residuals of the Lagrange
equations ([1.18](book-Z-H-12.html#EQUATION_1.18)) for the
Lagrangian *L*:

<div align="left">

![](chap1-Z-G-217.gif)

</div>

Realizable paths *q* satisfy the Lagrange equations

<div align="left">

![](chap1-Z-G-218.gif)

</div>

The path-dependent Lagrange equations can be converted to local Lagrange
equations using ![](chap1-Z-G-D-52.gif):

<div align="left">

![](chap1-Z-G-219.gif)

</div>

The operator *E* is called the *Euler-Lagrange operator*. In terms of
this operator the Lagrange equations are

<div align="left">

![](chap1-Z-G-220.gif)

</div>

Applying the definition ([1.167](#EQUATION_1.167)) of
![](chap1-Z-G-D-52.gif) yields

<div align="left">

![](chap1-Z-G-221.gif)

</div>

So the Euler-Lagrange operator is explicitly

<div align="left">

![](chap1-Z-G-222.gif)

</div>

The procedure `Euler-Lagrange-operator` implements *E*:

`(define (Euler-Lagrange-operator L)   (- (Dt ((partial 2) L)) ((partial 1) L))) . `

For example, applied to the Lagrangian for the harmonic oscillator, we
have

`(print-expression  ((Euler-Lagrange-operator     (L-harmonic 'm 'k))   (->local 't 'x 'v 'a))) (+ (* a m) (* k x)) `

Notice that the components of the local tuple are individually
specified. Using equation ([1.172](#EQUATION_1.172)), the Lagrange
equations for the harmonic oscillator are[^87^](#footnote_Temp_153)

`(print-expression  ((compose     (Euler-Lagrange-operator (L-harmonic 'm 'k))    (Gamma (literal-function 'x) 4))   't)) (+ (* k (x t)) (* m (((expt D 2) x) t))) `

**Exercise 1.33.**  **Properties of *E***\
 Let *F* and *G* be two Lagrangian-like functions of a local tuple, *C*
be a local-tuple transformation function, and *c* a constant.
Demonstrate the following properties:

**a**.   *E*[*F* + *G*] = *E*[*F*] + *E*[*G*]

**b**.   *E*[*c* *F*] = *c* *E*[*F*]

**c**.   *E*[*F* *G*] = *E*[*F*] *G* + *F* *E*[*G*] + (*D*~*t*~ *F*)
![](front-Z-G-D-2.gif)~2~ *G* + ![](front-Z-G-D-2.gif)~2~ *F* (*D*~*t*~
*G*)

**d**.   *E*[*F* o *C*] = *D*~*t*~ (*DF* o *C*)
![](front-Z-G-D-2.gif)~2~ *C* + *DF* o *C* *E*[*C*]

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^87^](#call_footnote_Temp_153) Notice that `Gamma` has one more
argument than it usually has. This argument gives the length of the
initial segment of the local tuple needed. The default length is 3,
giving components of the local tuple up to and including the velocities.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-15.html)</span><span>,
[next](book-Z-H-17.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


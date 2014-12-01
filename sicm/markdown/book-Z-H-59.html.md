<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-58.html)</span><span>,
[next](book-Z-H-60.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[5.2  General Canonical Transformations](book-Z-H-4.html#%_toc_%_sec_5.2)
-------------------------------------------------------------------------

Although we have shown how to extend any point transformation of the
configuration space to a canonical transformation, there are other ways
to construct canonical transformations. How do we know if we have a
canonical transformation? To test if a transformation is canonical we
may use the fact that if the transformation is canonical, then
Hamilton's equations of motion for the transformed system and the
original system will be equivalent.

Consider a Hamiltonian *H* and a phase-space transformation *C*. The
transformation *C* transforms the phase-space path
![](chap3-Z-G-D-5.gif)'(*t*) = (*t*, *q*'(*t*), *p*'(*t*)) into
![](chap3-Z-G-D-5.gif)(*t*) = (*t*, *q*(*t*), *p*(*t*)):

<div align="left">

![](chap5-Z-G-13.gif)

</div>

The rates of change of the phase-space coordinates are transformed by
the derivative of the transformation

<div align="left">

![](chap5-Z-G-14.gif)

</div>

Let *D*~*s*~ be the phase-space derivative operator

<div align="left">

![](chap5-Z-G-15.gif)

</div>

Hamilton's equations are

<div align="left">

![](chap5-Z-G-16.gif)

</div>

for any realizable phase-space path ![](chap3-Z-G-D-5.gif).

The transformation is canonical if the equations of motion obtained from
the new Hamiltonian are the same as those that could be obtained by
transforming the equations of motion derived from the original
Hamiltonian to the new coordinates:

<div align="left">

![](chap5-Z-G-17.gif)

</div>

Comparing equation ([5.15](#EQUATION_5.15)) with this, we see

<div align="left">

![](chap5-Z-G-18.gif)

</div>

Using ![](chap3-Z-G-D-5.gif) = *C* o ![](chap3-Z-G-D-5.gif)', we find

<div align="left">

![](chap5-Z-G-19.gif)

</div>

This condition must hold for any realizable phase-space path
![](chap3-Z-G-D-5.gif)'. Certainly this is true if the following
condition holds for every phase-space point:

<div align="left">

![](chap5-Z-G-20.gif)

</div>

Any transformation that satisfies equation ([5.19](#EQUATION_5.19)) is a
canonical transformation among phase-space representations of a
dynamical system. In one phase-space representation the system's
dynamics is characterized by the Hamiltonian *H*' and in the other by
*H*. The idea behind this equation is illustrated in
figure [5.1](book-Z-H-1000.html#FIGURE_5.1).

<div align="left">

![](chap5-Z-G-21.gif)

</div>

We can formalize this test as a program:

`(define (canonical? C H Hprime)   (- (compose (phase-space-derivative H) C)      (* (D C) (phase-space-derivative Hprime)))) `

where `phase-space-derivative`, which was introduced in
chapter [3](book-Z-H-36.html#%_chap_3), implements *D*~*s*~. The
transformation is canonical if these residuals are zero.

If a suitable Hamiltonian for the transformed system is obtained by
composing *H* with the phase-space transformation, we obtain a more
specific formula:

<div align="left">

![](chap5-Z-G-22.gif)

</div>

and a more specific test:

`(define (compositional-canonical? C H)   (canonical? C H (compose H C))) `

Using this test, we can verify that the polar-to-rectangular
transformation satisfies the test for a canonical transformation on a
general central field:

`(print-expression  ((compositional-canonical?     (F->CT p->r)    (H-central 'm (literal-function 'V)))   (up 't       (up 'r 'phi)       (down 'p_r 'p_phi)))) (up 0 (up 0 0) (down 0 0)) `

The residuals are zero so the transformation is canonical.

**Exercise 5.2.**  **Group properties**\
 If we say that *C* is canonical with respect to Hamiltonians *H* and
*H*' if and only if *D*~*s*~ *H* o *C* = *DC* · *D*~*s*~ *H*', then:

**a**.  Show that the composition of canonical transformations is
canonical. **b**.  Show that composition of canonical transformations is
associative. **c**.  Show that the identity transformation is canonical.
**d**.  Show that there is an inverse for a canonical transformation and
the inverse is canonical.

### [5.2.1  Time-Independent Canonical Transformations](book-Z-H-4.html#%_toc_%_sec_5.2.1)

We have defined a canonical transformation as a transformation of
phase-space coordinates for which Hamilton's equations transform
appropriately. The conditions that a canonical transformation must
satisfy (equations [5.19](#EQUATION_5.19) or [5.20](#EQUATION_5.20))
involve the Hamiltonians. If the Hamiltonians transform by composition
and the transformation is time independent, then we can tell if the
phase-space transformation is canonical without further reference to the
Hamiltonian.

First, we rewrite Hamilton's equations in a slightly different form.
Hamilton's equations are constructed from the derivative of the
Hamiltonian by rearranging the components and then negating some of
them. We introduce a shuffle function that does this rearrangement:

<div align="left">

![](chap5-Z-G-23.gif)

</div>

The argument to ![](chap5-Z-G-D-1.gif) is a down tuple of components of
the derivative of a Hamiltonian-like function. The shuffle function is
linear. We also introduce a constant function:

<div align="left">

![](chap5-Z-G-24.gif)

</div>

With these, Hamilton's equations can be expressed as

<div align="left">

![](chap5-Z-G-25.gif)

</div>

With ![](chap5-Z-G-D-1.gif) and ![](chap1-Z-G-D-35.gif) the canonical
condition ([5.20](#EQUATION_5.20)) can be rewritten

<div align="left">

![](chap5-Z-G-26.gif)

</div>

The value of ![](chap1-Z-G-D-35.gif) does not depend on its arguments,
and for time-independent transformations ![](chap1-Z-G-D-35.gif) = *DC*
· ![](chap1-Z-G-D-35.gif), so the canonical condition becomes

<div align="left">

![](chap5-Z-G-27.gif)

</div>

Applied to a particular phase-space state *s* this is

<div align="left">

![](chap5-Z-G-28.gif)

</div>

Let ![](chap5-Z-G-D-2.gif) be a function that takes a multiplier and
produces a linear transformation that multiplies the multiplier by the
argument to the linear transformation:

<div align="left">

![](chap5-Z-G-29.gif)

</div>

Similarly, let ![](chap5-Z-G-D-2.gif)^\*^ be a function that takes a
multiplier and produces a linear transformation that multiplies the
argument to the linear transformation by the multiplier:

<div align="left">

![](chap5-Z-G-30.gif)

</div>

Using ![](chap5-Z-G-D-2.gif) and ![](chap5-Z-G-D-2.gif)^\*^, we can
rewrite condition ([5.27](#EQUATION_5.27)) as

<div align="left">

![](chap5-Z-G-31.gif)

</div>

This condition is satisfied if

<div align="left">

![](chap5-Z-G-32.gif)

</div>

A time-independent transformation *C* is canonical, for Hamiltonians
that transform by composition, if this condition on its derivative *DC*
is satisfied.

Note that the condition ([5.31](#EQUATION_5.31)) does not refer to the
Hamiltonian. This is a remarkable result. Though we have assumed the
Hamiltonians transform by composition with the transformation, we can
decide whether a time-independent phase-space transformation preserves
the dynamics of Hamilton's equation without further reference to the
details of the dynamical system.

The test is implemented thus:

`(define ((time-independent-canonical? C) s)   ((- J-func       (compose (Phi ((D C) s))                 J-func                (Phi* ((D C) s))))    (compatible-shape s))) (define (J-func DH)   (up 0 (ref DH 2) (- (ref DH 1)))) (define ((Phi A) v) (* A v))  (define ((Phi* A) w) (* w A)) `

This procedure tests whether a composition of functions is the same
function as ![](chap5-Z-G-D-1.gif) by computing their difference when
applied to a general typical argument.[^4^](#footnote_Temp_334) Here
they are applied to a structure with the shape of *DH*(*s*), for an
arbitrary phase-space state *s*.[^5^](#footnote_Temp_335)

For example, consider the following polar-canonical transformation:

<div align="left">

![](chap5-Z-G-33.gif)

</div>

where

<div align="left">

![](chap5-Z-G-34.gif)

</div>

Here ![](chap1-Z-G-D-21.gif) is an arbitrary parameter. We define:

`(define ((polar-canonical alpha) H-state)   (let ((t (time H-state))         (theta (coordinate H-state))         (I (momentum H-state)))     (let ((x (* (sqrt (/ (* 2 I) alpha)) (sin theta)))           (p_x (* (sqrt (* 2 alpha I)) (cos theta))))       (up t x p_x)))) `

And now we just run our test:

`(print-expression  ((time-independent-canonical? (polar-canonical 'alpha))   (up 't 'theta 'I))) (up 0 0 0) `

So the transformation is canonical.[^6^](#footnote_Temp_336)

Of course, not every transformation we might try is canonical. For
example, we might try *x* = *p* sin ![](chap1-Z-G-D-19.gif) with
*p*~*x*~ = *p* cos ![](chap1-Z-G-D-19.gif). The implementation
is[^7^](#footnote_Temp_337)

`(define (a-non-canonical-transform H-state)   (let ((t (time H-state))         (theta (coordinate H-state))         (p (momentum H-state)))     (let ((x (* p (sin theta)))           (p_x (* p (cos theta))))       (up t x p_x)))) `

`(print-expression  ((time-independent-canonical? a-non-canonical-transform)   (up 't 'theta 'p)))  (up 0 (+ (* -1 p x8102) x8102) (+ (* p x8101) (* -1 x8101))) `

So this transformation is not canonical.

#### [Harmonic oscillator](book-Z-H-4.html#%_toc_%_sec_Temp_338)

The analysis of the harmonic oscillator illustrates the use of a general
canonical transformation in the solution of a problem. The harmonic
oscillator is a mathematical model of a simple spring-mass system. The
Hamiltonian for a spring-mass system with mass *m* and spring constant
*k* is

<div align="left">

![](chap5-Z-G-35.gif)

</div>

Hamilton's equations of motion are

<div align="left">

![](chap5-Z-G-36.gif)

</div>

giving the second-order system

<div align="left">

![](chap5-Z-G-37.gif)

</div>

The solution is

<div align="left">

![](chap5-Z-G-38.gif)

</div>

where

<div align="left">

![](chap5-Z-G-39.gif)

</div>

and where *A* and ![](chap1-Z-G-D-16.gif) are determined by initial
conditions.

Let's try our polar-canonical transformation
*C*~![](chap1-Z-G-D-21.gif)~ on the harmonic oscillator. We substitute
expressions ([5.33](#EQUATION_5.33)) and ([5.34](#EQUATION_5.34)) for
*x* and *p*~*x*~ in the Hamiltonian, getting our new Hamiltonian:

<div align="left">

![](chap5-Z-G-40.gif)

</div>

If we choose ![](chap1-Z-G-D-21.gif) = (*km*)^1/2^ then we obtain

<div align="left">

![](chap5-Z-G-41.gif)

</div>

and the new Hamiltonian no longer depends on the coordinate. Hamilton's
equation for *I* is

<div align="left">

![](chap5-Z-G-42.gif)

</div>

so *I* is constant. The equation for ![](chap1-Z-G-D-19.gif) is

<div align="left">

![](chap5-Z-G-43.gif)

</div>

so

<div align="left">

![](chap5-Z-G-44.gif)

</div>

In the original variables,

<div align="left">

![](chap5-Z-G-45.gif)

</div>

with the constant *A* = ( 2 *I*(*t*)/ ![](chap1-Z-G-D-21.gif))^1/2^. So
we have found the solution to the problem by making a canonical
transformation to new phase-space variables for which the solution is
easy and then transforming the solutions back to the original variables.

**Exercise 5.3.**  **Trouble in Lagrangian world**\

Is there a Lagrangian *L*' that corresponds to the harmonic oscillator
Hamiltonian *H*'(*t*, ![](chap1-Z-G-D-19.gif), *I*) =
![](chap1-Z-G-D-23.gif) *I*? What could this possibly mean?

**Exercise 5.4.**  **Polar-canonical transformations**\

Let *x*, *p* and ![](chap1-Z-G-D-19.gif), *I* be two sets of canonically
conjugate variables. Consider transformations of the form *x* = *ß*
*I*^![](chap1-Z-G-D-21.gif)^ sin ![](chap1-Z-G-D-19.gif) and *p* = *ß*
*I*^![](chap1-Z-G-D-21.gif)^ cos ![](chap1-Z-G-D-19.gif). Determine all
![](chap1-Z-G-D-21.gif) and *ß* for which this transformation is
compositional canonical.

**Exercise 5.5.**  **Standard map**\

Is the standard map a canonical transformation? Recall that the standard
map is: *I*' = *I* + *K* sin ![](chap1-Z-G-D-19.gif), with
![](chap1-Z-G-D-19.gif)' = ![](chap1-Z-G-D-19.gif) + *I*', both modulo
2![](chap1-Z-G-D-15.gif).

### [5.2.2  Symplectic Transformations](book-Z-H-4.html#%_toc_%_sec_5.2.2)

Condition ([5.31](#EQUATION_5.31)) involves the composition of
functions, all of which are linear transformations. Linear
transformations can be represented in terms of matrices. A matrix
representation is defined with respect to a basis. For incremental
Hamiltonian states we organize the state components as a column matrix
of time, the components of the coordinates, and the corresponding
components of the momenta.

Let ![](chap5-Z-G-D-3.gif) and ***DC*** be matrix representations of
![](chap5-Z-G-D-1.gif) and ![](chap5-Z-G-D-2.gif)(*DC*(*s*)),
respectively, where *s* is the arbitrary phase-space state at which the
canonical condition is being tested. The matrix representation of
![](chap5-Z-G-D-2.gif)^\*^(*DC*(*s*)) is the transpose of ***DC***. In
terms of these matrix representations, the test for canonical becomes

<div align="left">

![](chap5-Z-G-46.gif)

</div>

We say that a transformation is *symplectic* if the matrix
representation of its derivative satisfies this identity.

The matrix representation of the multiplier for the linear
transformation ![](chap5-Z-G-D-1.gif) is ![](chap5-Z-G-D-3.gif). We can
find the multiplier for a linear transformation by taking the derivative
of the linear transformation and evaluating it at an arbitrary
point:[^8^](#footnote_Temp_342) *D*![](chap5-Z-G-D-1.gif)( [ *a*, *b*,
*c* ] ). We can obtain a matrix representation with the utility `s->m`
that takes a structure that represents a multiplier of a linear
transformation and returns a matrix representation of the
multiplier.[^9^](#footnote_Temp_343) The matrix ![](chap5-Z-G-D-3.gif)
depends only on the number of degrees of freedom of the system. For
example, the ![](chap5-Z-G-D-3.gif) for a system with two degrees of
freedom is

`(print-expression  (let* ((s (up 't (up 'x 'y) (down 'px 'py)))         (s* (compatible-shape s)))    (s->m s* ((D J-func) s*) s*)))        (matrix-by-rows (list 0 0 0 0 0)                 (list 0 0 0 1 0)                 (list 0 0 0 0 1)                 (list 0 -1 0 0 0)                 (list 0 0 -1 0 0)) `

In terms of matrix representations, the test that a transformation is
symplectic is

`(define ((symplectic? C) s)   (let ((s* (compatible-shape s)))     (let ((J (s->m s* ((D J-func) s*) s*))           (DCs (s->m s* ((D C) s) s)))       (- J (* DCs J (m:transpose DCs)))))) `

For example, we can verify that the point transformation derived from
the coordinate transformation `p->r` is symplectic:

`(print-expression  ((symplectic? (F->CT p->r))   (up 't       (up 'r 'varphi)       (down 'p_r 'p_varphi)))) (matrix-by-rows (list 0 0 0 0 0)                 (list 0 0 0 0 0)                 (list 0 0 0 0 0)                 (list 0 0 0 0 0)                 (list 0 0 0 0 0)) `

There is a further simplification available. The elements of the first
row and the first column of the matrix representation of
![](chap5-Z-G-D-1.gif) are all zeros. Thus we need to consider only the
submatrix associated with the coordinates and the momenta.

The *qp* submatrix[^10^](#footnote_Temp_344) of dimension 2*n*× 2*n* of
the matrix ![](chap5-Z-G-D-3.gif) is called the *symplectic unit* for
*n* degrees of freedom:

<div align="left">

![](chap5-Z-G-47.gif)

</div>

The matrix ***J***~*n*~ satisfies the following identities:

<div align="left">

![](chap5-Z-G-48.gif)

</div>

A 2*n*× 2*n* matrix ***A*** that satisfies the relation

<div align="left">

![](chap5-Z-G-49.gif)

</div>

is called a *symplectic matrix*.

Here is an alternate test for whether a transformation is symplectic:

`(define ((symplectic-transform? C) s)   (symplectic-matrix?    (qp-submatrix     (s->m (compatible-shape s)           ((D C) s)           s)))) `

`(define (symplectic-matrix? M)   (let ((2n (m:dimension M)))     (let ((J (symplectic-unit (quotient 2n 2))))       (- J (* M J (m:transpose M)))))) `

The procedure `symplectic-transform?` returns a zero matrix if and only
if the transformation being tested passes the symplectic matrix test. An
appropriate symplectic unit matrix of a given size is produced by the
procedure `symplectic-unit`.

The point transformations are symplectic. For example,

`(print-expression  ((symplectic-transform? (F->CT p->r))   (up 't       (up 'r 'theta)       (down 'p_r 'p_theta)))) (matrix-by-rows (list 0 0 0 0)                 (list 0 0 0 0)                 (list 0 0 0 0)                 (list 0 0 0 0)) `

**Exercise 5.6.**  **Symplectic matrices**\
 Let ***A*** be a symplectic matrix: ***J***~*n*~ = ***A*** ***J***~*n*~
***A***^`T`^ . Show that ***A***^`T`^ and ***A***^`-`1^ are symplectic.

**Exercise 5.7.**  **Whittaker transform**\
 Shew that the transformation *q* = log ( (1/*q*') sin *p*' ) with *p* =
*q*' cot *p*' is symplectic.

### [5.2.3  Time-Dependent Transformations](book-Z-H-4.html#%_toc_%_sec_5.2.3)

We have found that a time-independent transformation (involving the
coordinates and conjugate momenta, but not the time) is canonical if the
derivative of the transformation is symplectic. Let's return to the
calculation of the symplectic condition, but now allow explicit time
dependence in the transformation equations.

If the transformation is time dependent, then it turns out that *H* o
*C* does not make a suitable *H*'. Instead, we assume

<div align="left">

![](chap5-Z-G-50.gif)

</div>

and look for conditions on *K* and *C* that guarantee the transformation
is canonical. Equation ([5.25](#EQUATION_5.24)), the condition that a
transformation is canonical, becomes

<div align="left">

![](chap5-Z-G-51.gif)

</div>

This condition is satisfied if the following two conditions are
satisfied:

<div align="left">

![](chap5-Z-G-52.gif)

</div>

and

<div align="left">

![](chap5-Z-G-53.gif)

</div>

Condition ([5.52](#EQUATION_5.52)) is the condition that *C* is a
symplectic transformation. Condition ([5.53](#EQUATION_5.53)) is an
auxiliary condition on *K*. This condition does not actually depend on
the Hamiltonian *H* because the constant value of
![](chap1-Z-G-D-35.gif) does not depend on the argument. The time
component is always satisfied; only the coordinate and momentum
components of this condition constrain *K*. Evaluated at a particular
state *s* (with compatible shape *s*^\*^), the condition on *K* is

<div align="left">

![](chap5-Z-G-54.gif)

</div>

explicitly showing that the Hamiltonian *H* does not enter.

Thus we can conclude that a time-dependent transformation is canonical
if its position-momentum part is symplectic and if we form the new
Hamiltonian by adding an appropriate piece. Note that we have not proven
that the position-momentum part must be symplectic. Rather, we have
shown that if this part is symplectic then the Hamiltonian must be
modified in an appropriate way.

As a program, the test for *K* is

`(define ((canonical-K? C K) s)   (let ((s* (compatible-shape s)))     (- (T-func s*)        (+ (* ((D C) s) (J-func ((D K) s)))           (((partial 0) C) s))))) `

#### [Rotating coordinates](book-Z-H-4.html#%_toc_%_sec_Temp_347)

Consider a time-dependent transformation to uniformly rotating
coordinates:

<div align="left">

![](chap5-Z-G-55.gif)

</div>

with components

<div align="left">

![](chap5-Z-G-56.gif)

</div>

As a program this is

`(define ((rotating n) state)   (let ((t (time state))         (q (coordinate state)))     (let ((x (ref q 0))           (y (ref q 1))           (z (ref q 2)))       (up (+ (* (cos (* n t)) x) (* (sin (* n t)) y))           (- (* (cos (* n t)) y) (* (sin (* n t)) x))           z)))) `

The extension of this transformation to a phase-space transformation is

`(define (C-rotating Omega) (F->CT (rotating Omega))) `

We first verify that the position-momentum part of this time-dependent
transformation is symplectic:

`(print-expression  ((symplectic-transform? (C-rotating 'Omega))   (up 't        (up 'x 'y 'z)       (down 'px 'py 'pz)))) (matrix-by-rows (list 0 0 0 0 0 0)                 (list 0 0 0 0 0 0)                 (list 0 0 0 0 0 0)                 (list 0 0 0 0 0 0)                 (list 0 0 0 0 0 0)                 (list 0 0 0 0 0 0)) `

For this transformation the appropriate correction to the Hamiltonian is

<div align="left">

![](chap5-Z-G-57.gif)

</div>

which is the rate of rotation of the coordinate system multiplied by the
angular momentum. The justification for this will be given in
section [5.6](book-Z-H-63.html#%_sec_5.6). The implementation is

`(define ((K Omega) s)   (let ((q (coordinate s)) (p (momentum s)))     (let ((x (ref q 0)) (y (ref q 1))           (px (ref p 0)) (py (ref p 1)))       (* -1 Omega (- (* x py) (* y px)))))) `

Applying the test, we find:

`(print-expression   ((canonical-K? (C-rotating 'Omega) (K 'Omega))    (up 't         (up 'x 'y 'z)        (down 'p_x 'p_y 'p_z)))) (up 0 (up 0 0 0) (down 0 0 0)) `

The residuals are zero so this *K* completes the canonical
transformation.

### [5.2.4  The Symplectic Condition](book-Z-H-4.html#%_toc_%_sec_5.2.4)

A transformation is symplectic if the *qp* part of the transformation
has a symplectic derivative. This condition can be written simply in
terms of Poisson brackets.

The Poisson bracket can be written in terms of ![](chap5-Z-G-D-1.gif):

<div align="left">

![](chap5-Z-G-58.gif)

</div>

as can be seen by writing out the components.

We break the transformation *C* into position and momentum parts:

<div align="left">

![](chap5-Z-G-59.gif)

</div>

In terms of the individual component functions, the symplectic
condition ([5.46](#EQUATION_5.46)) is

<div align="left">

![](chap5-Z-G-60.gif)

</div>

where ![](chap1-Z-G-D-17.gif)^*i*^~*j*~ is one if *i* = *j* and zero
otherwise. These are called the *fundamental Poisson brackets*. If a
transformation satisfies these Poisson bracket relations then it is
symplectic.

We have found that a time-dependent transformation is canonical if its
position-momentum part is symplectic and we modify the Hamiltonian by
the addition of a suitable *K*. We can rewrite these conditions in terms
of Poisson brackets. If the Hamiltonian is

<div align="left">

![](chap5-Z-G-61.gif)

</div>

the transformation will be canonical if the coordinate-momentum
transformation satisfies the fundamental Poisson brackets, and *K*
satisfies:

<div align="left">

![](chap5-Z-G-62.gif)

</div>

**Exercise 5.8.**  ****\

Fill in the details to show that the symplectic
condition ([5.31](#EQUATION_5.31)) is equivalent to the fundamental
Poisson brackets ([5.61](#EQUATION_5.61)) and that the condition on
*K* ([5.53](#EQUATION_5.53)) is equivalent to the Poisson bracket
condition on *K* ([5.63](#EQUATION_5.63)).

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^4^](#call_footnote_Temp_334) It is in principle impossible to
determine in general if two functions are the same, but in this case,
since ![](chap5-Z-G-D-2.gif)(*DC*(*s*)) is linear, this test is valid.

[^5^](#call_footnote_Temp_335) The shape of *DH*(*s*) is a *compatible
shape* to the shape of *s*: if they are multiplied the result is a real
number. The procedure `compatible-shape` takes any structure and
produces another structure that is guaranteed to multiply with the given
structure to produce a real number. The structure produced is filled
with unique real literals, so if the residual is zero then the functions
are the same.

[^6^](#call_footnote_Temp_336) Actually, for *I* = 0 the transform is
not well defined and so it is not compositional canonical for that
value. This transformation is \`\`locally compositional canonical'' in
that it is compositional canonical for nonzero values of *I*. We will
ignore this essentially topological problem.

[^7^](#call_footnote_Temp_337) The mysterious symbols such as `x8102`
are unique real literals introduced to test functional equalities. That
they appear in a residual demonstrates that the equality is invalid.

[^8^](#call_footnote_Temp_342) The derivative of a linear transformation
is a constant function, independent of the argument.

[^9^](#call_footnote_Temp_343) The procedure `s->m` takes three
arguments: `(s->m s* A s)`. The `s*` and `s` specify the shapes of
objects that multiply `A` on the left and right to give a numerical
value; these specify the basis.

[^10^](#call_footnote_Temp_344) The *qp* submatrix of a 2*n* +
1-dimensional square matrix is the 2*n*-dimensional matrix obtained by
deleting the first row and the first column of the given matrix. This
can be computed by:

`(define (qp-submatrix m)   (m:submatrix m 1 (m:num-rows m) 1 (m:num-cols m))) `

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-58.html)</span><span>,
[next](book-Z-H-60.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


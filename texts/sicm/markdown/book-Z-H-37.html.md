<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-36.html)</span><span>,
[next](book-Z-H-38.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[3.1  Hamilton's Equations](book-Z-H-4.html#%_toc_%_sec_3.1)
------------------------------------------------------------

The momenta are given by momentum state functions of the time, the
coordinates, and the velocities.[^1^](#footnote_Temp_223) Locally, we
can find inverse functions that give the velocities in terms of the
time, the coordinates, and the momenta. We can use this inverse function
to represent the state in terms of the coordinates and momenta rather
than the coordinates and velocities. The equations of motion when recast
in terms of coordinates and momenta are called *Hamilton's canonical
equations*.

We present three derivations of Hamilton's equations. The first
derivation is guided by the strategy outlined above and uses nothing
more complicated than implicit functions and the chain rule. The second
derivation first abstracts a key part of the first derivation and then
applies the more abstract machinery to derive Hamilton's equations. The
third uses the action principle.

Lagrange's equations give us the time derivative of the momentum *p* on
a path *q*:

<div align="left">

![](chap3-Z-G-1.gif)

</div>

where

<div align="left">

![](chap3-Z-G-2.gif)

</div>

To eliminate *Dq* we need to solve equation ([3.2](#EQUATION_3.2)) for
*Dq* in terms of *p*.

Let ![](chap1-Z-G-D-27.gif) be the function that gives the velocities in
terms of the time, coordinates, and momenta. Defining
![](chap1-Z-G-D-27.gif) is a problem of functional inverses. To prevent
confusion we use names for the variables that have no mnemonic
significance. Let

<div align="left">

![](chap3-Z-G-3.gif)

</div>

then ![](chap1-Z-G-D-27.gif) satisfies

<div align="left">

![](chap3-Z-G-4.gif)

</div>

So ![](chap1-Z-G-D-27.gif) and ![](front-Z-G-D-2.gif)~2~ *L* are
inverses on the third argument position:

<div align="left">

![](chap3-Z-G-5.gif)

</div>

The Lagrange equation ([3.1](#EQUATION_3.1)) can be rewritten in terms
of *p* using ![](chap1-Z-G-D-27.gif):

<div align="left">

![](chap3-Z-G-6.gif)

</div>

We can also use ![](chap1-Z-G-D-27.gif) to rewrite
equation ([3.2](#EQUATION_3.2)) as an equation for *Dq* in terms of *t*,
*q* and *p*:

<div align="left">

![](chap3-Z-G-7.gif)

</div>

Equations ([3.7](#EQUATION_3.7)) and ([3.8](#EQUATION_3.8)) give the
rate of change of *q* and *p* along realizable paths as functions of
*t*, *q*, and *p* along the paths.

Though these equations fulfill our goal of expressing the equations of
motion entirely in terms of coordinates and momenta, we can find a more
convenient representation. Define the function

<div align="left">

![](chap3-Z-G-8.gif)

</div>

which is the Lagrangian reexpressed as a function of time, coordinates,
and momenta.[^2^](#footnote_Temp_224) For the equations of motion we
need ![](front-Z-G-D-2.gif)~1~ *L* evaluated with the appropriate
arguments. Consider

<div align="left">

![](chap3-Z-G-9.gif)

</div>

where we used the chain rule in the first step and the inverse
property ([3.5](#EQUATION_3.5)) of ![](chap1-Z-G-D-27.gif) in the second
step. Introducing the momentum selector[^3^](#footnote_Temp_225)
*P*(*t*, *q*, *p*) = *p*, and using the property
![](front-Z-G-D-2.gif)~1~ *P* = 0, we have

<div align="left">

![](chap3-Z-G-10.gif)

</div>

where the *Hamiltonian* *H* is defined by[^4^](#footnote_Temp_226)

<div align="left">

![](chap3-Z-G-11.gif)

</div>

Using the algebraic result ([3.11](#EQUATION_3.11)), the Lagrange
equation ([3.7](#EQUATION_3.7)) for *Dp* becomes

<div align="left">

![](chap3-Z-G-12.gif)

</div>

The equation for *Dq* can also be written in terms of *H*. Consider

<div align="left">

![](chap3-Z-G-13.gif)

</div>

To carry out the derivative of ![](chap1-Z-G-D-49.gif) we write it out
in terms of *L*:

<div align="left">

![](chap3-Z-G-14.gif)

</div>

again using the inverse property ([3.5](#EQUATION_3.5)) of
![](chap1-Z-G-D-27.gif). So, putting equations ([3.14](#EQUATION_3.14))
and ([3.15](#EQUATION_3.15)) together, we obtain

<div align="left">

![](chap3-Z-G-15.gif)

</div>

Using the algebraic result ([3.16](#EQUATION_3.16)),
equation ([3.8](#EQUATION_3.8)) for *Dq* becomes

<div align="left">

![](chap3-Z-G-16.gif)

</div>

Equations ([3.13](#EQUATION_3.13)) and ([3.17](#EQUATION_3.17)) give the
derivatives of the coordinate and momentum path functions at each time
in terms of the time, and the coordinates, and momenta at that time.
These equations are known as
*Hamilton's equations*:[^5^](#footnote_Temp_227)

<div align="left">

![](chap3-Z-G-19.gif)

</div>

The first equation is just a restatement of the relationship of the
momenta to the velocities in terms of the Hamiltonian and holds for any
path, whether or not it is a realizable path. The second equation holds
only for realizable paths.

Hamilton's equations have an especially simple and symmetrical form.
Just as Lagrange's equations are constructed from a real-valued
function, the Lagrangian, Hamilton's equations are constructed from a
real-valued function, the Hamiltonian. The Hamiltonian function
is[^6^](#footnote_Temp_228)

<div align="left">

![](chap3-Z-G-21.gif)

</div>

The Hamiltonian has the same value as the energy function
![](chap1-Z-G-D-45.gif) (see
equation [1.140](book-Z-H-15.html#EQUATION_1.140)), except that the
velocities are expressed in terms of time, coordinates, and momenta by
![](chap1-Z-G-D-27.gif):

<div align="left">

![](chap3-Z-G-22.gif)

</div>

#### [Illustration](book-Z-H-4.html#%_toc_%_sec_Temp_229)

Let's try something simple: the motion of a particle of mass *m* with
potential energy *V*(*x*, *y*). A Lagrangian is

<div align="left">

![](chap3-Z-G-23.gif)

</div>

To form the Hamiltonian we find the momenta *p* =
![](front-Z-G-D-2.gif)~2~ *L*(*t*, *q*, *v*): *p*~*x*~ = *m* *v*~*x*~
and *p*~*y*~ = *m* *v*~*y*~. Solving for the velocities in terms of the
momenta is easy here: *v*~*x*~ = *p*~*x*~/*m* and *v*~*y*~ =
*p*~*y*~/*m*. The Hamiltonian is *H*(*t*, *q*, *p*) = *pv* `-` *L*(*t*,
*q*, *v*), with *v* reexpressed in terms of (*t*, *q*, *p*):

<div align="left">

![](chap3-Z-G-24.gif)

</div>

The kinetic energy is a homogeneous quadratic form in the velocities, so
the energy is *T* + *V* and the Hamiltonian is the energy expressed in
terms of momenta rather than velocities. Hamilton's equations for *Dq*
are

<div align="left">

![](chap3-Z-G-25.gif)

</div>

Note that these equations merely restate the relation between the
momenta and the velocities. Hamilton's equations for *Dp* are

<div align="left">

![](chap3-Z-G-26.gif)

</div>

The rate of change of the linear momentum is minus the gradient of the
potential energy.

**Exercise 3.1.**  **Deriving Hamilton's equations**\
 For each of the following Lagrangians derive the Hamiltonian and
Hamilton's equations. These problems are simple enough to do by hand.

**a**.  A Lagrangian for a planar pendulum: *L*(*t*,
![](chap1-Z-G-D-19.gif), ![](chap1-Z-G-D-20.gif)) = (1/2) *m* *l*^2^
![](chap1-Z-G-D-20.gif)^2^ + *m* *g* *l* cos ![](chap1-Z-G-D-19.gif).

**b**.  A Lagrangian for a particle of mass *m* with a two-dimensional
potential energy: *V*(*x*, *y*) = (*x*^2^ + *y*^2^)/2 + *x*^2^ *y* `-`
*y*^3^/3 is *L*(*t*; *x*, *y*; ![](chap1-Z-G-D-37.gif),
![](chap3-Z-G-D-1.gif)) = (1/2) *m* (![](chap1-Z-G-D-37.gif)^2^ +
![](chap3-Z-G-D-1.gif)^2^) `-` *V*(*x*, *y*).

**c**.  A Lagrangian for a particle of mass *m* constrained to move on a
sphere of radius *R*: *L*(*t*; ![](chap1-Z-G-D-19.gif),
![](chap1-Z-G-D-16.gif); ![](chap1-Z-G-D-20.gif),
![](chap1-Z-G-D-34.gif)) = (1/2) *m* *R*^2^
(![](chap1-Z-G-D-20.gif)^2^ + (![](chap1-Z-G-D-34.gif) sin
![](chap1-Z-G-D-19.gif))^2^), where ![](chap1-Z-G-D-19.gif) is the
colatitude and ![](chap1-Z-G-D-16.gif) is the longitude on the sphere.

**Exercise 3.2.**  **Sliding pendulum**\
 For the pendulum with a sliding support (see
exercise [1.20](book-Z-H-13.html#%_thm_1.20)), derive a Hamiltonian and
Hamilton's equations.

#### [Hamiltonian state](book-Z-H-4.html#%_toc_%_sec_Temp_232)

Given a coordinate path *q* and a Lagrangian *L*, the corresponding
momentum path *p* is given by equation ([3.2](#EQUATION_3.2)). Equation
([3.17](#EQUATION_3.17)) expresses the same relationship in terms of the
corresponding Hamiltonian *H*. That these relations are valid for any
path, whether or not it is a realizable path, allows us to abstract to
arbitrary velocity and momentum at a moment. At a moment, the momentum
*p* for the state tuple ( *t*, *q*, *v* ) is *p* =
![](front-Z-G-D-2.gif)~2~ *L*(*t*, *q*, *v*). We also have *v* =
![](front-Z-G-D-2.gif)~2~ *H*(*t*, *q*, *p*). In the Lagrangian
formulation the state of the system at a moment can be specified by the
local state tuple ( *t*, *q*, *v* ) of time, generalized coordinates,
and generalized velocities. Lagrange's equations determine a unique path
emanating from this state. In the Hamiltonian formulation the state can
be specified by the tuple ( *t*, *q*, *p* ) of time, generalized
coordinates, and generalized momenta. Hamilton's equations determine a
unique path emanating from this state. The Lagrangian state tuple ( *t*,
*q*, *v* ) encodes exactly the same information as the Hamiltonian state
tuple ( *t*, *q*, *p* ); we need a Lagrangian or a Hamiltonian to relate
them. The two formulations are equivalent in that the same coordinate
path emanates from them for equivalent initial states.

The Lagrangian state derivative is constructed from the Lagrange
equations by solving for the highest-order derivative and abstracting to
arbitrary positions and velocities at a moment.[^7^](#footnote_Temp_233)
The Lagrangian state path is generated by integration of the Lagrangian
state derivative given an initial Lagrangian state ( *t*, *q*, *v* ).
Similarly, the Hamiltonian state derivative can be constructed from
Hamilton's equations by abstracting to arbitrary positions and momenta
at a moment. Hamilton's equations are a set of first-order differential
equations in explicit form. The Hamiltonian state derivative can be
directly written in terms of them. The Hamiltonian state path is
generated by integration of the Hamiltonian state derivative given an
initial Hamiltonian state ( *t*, *q*, *p* ). If these state paths are
obtained by integrating the state derivatives with equivalent initial
states, then the coordinate path components of these state paths are the
same and satisfy the Lagrange equations. The coordinate path and the
momentum path components of the Hamiltonian state path satisfy
Hamilton's equations. The Hamiltonian formulation and the Lagrangian
formulation are equivalent.

Given a path *q*, the Lagrangian state path and the Hamiltonian state
paths can be deduced from it. The Lagrangian state path
![](chap1-Z-G-D-9.gif)[*q*] can be constructed from a path *q* simply by
taking derivatives. The Lagrangian state path satisfies:

<div align="left">

![](chap3-Z-G-27.gif)

</div>

The Lagrangian state path is uniquely determined by the path *q*. The
Hamiltonian state path ![](chap3-Z-G-D-2.gif)~*L*~[*q*] can also be
constructed from the path *q* but the construction requires a
Lagrangian. The Hamiltonian state path satisfies

<div align="left">

![](chap3-Z-G-28.gif)

</div>

The Hamiltonian state tuple is not uniquely determined by the path *q*
because it depends upon our choice of Lagrangian, which is not unique.

The 2*n*-dimensional space whose elements are labeled by the *n*
generalized coordinates *q*^*i*^ and the *n* generalized momenta
*p*~*i*~ is called the *phase space*. The components of the generalized
coordinates and momenta are collectively called the *phase-space
components*.[^8^](#footnote_Temp_234) The dynamical state of the system
is completely specified by the phase-space state tuple ( *t*, *q*, *p*
), given a Lagrangian or Hamiltonian to provide the map between
velocities and momenta.

#### [Computing Hamilton's equations](book-Z-H-4.html#%_toc_%_sec_Temp_235)

Hamilton's equations are a system of first-order ordinary differential
equations. A procedural formulation of Lagrange's equations as a
first-order system was presented in
section [1.7](book-Z-H-14.html#%_sec_1.7). The following formulation of
Hamilton's equations is analogous:

`(define ((Hamilton-equations Hamiltonian) q p)   (let ((H-state-path (qp->H-state-path q p)))     (- (D H-state-path)        (compose (phase-space-derivative Hamiltonian)                 H-state-path)))) `

The Hamiltonian state derivative is computed as follows:

`(define ((phase-space-derivative Hamiltonian) H-state)   (up 1       (((partial 2)Hamiltonian) H-state)       (- (((partial 1)Hamiltonian) H-state)))) `

The state in the Hamiltonian formulation is composed of the time, the
coordinates, and the momenta. We call this an `H-state`, to distinguish
it from the state in the Lagrangian formulation. We can select the
components of the Hamiltonian state with the selectors `time`,
`coordinate`, `momentum`. We construct Hamiltonian states from their
components with `up`. The first component of the state is time, so the
first component of the state derivative is one, the time rate of change
of time. Given procedures `q` and `p` implementing coordinate and
momentum path functions, the Hamiltonian state path can be constructed
with the following procedure:

`(define ((qp->H-state-path q p) t)   (up t (q t) (p t))) `

The `Hamilton-equations` procedure returns the residuals of Hamilton's
equations for the given paths.

For example, a procedure implementing the Hamiltonian for a point mass
with potential energy *V*(*x*, *y*) is

`(define ((H-rectangular m V) H-state)   (let ((q (coordinate H-state))         (p (momentum H-state)))     (+ (/ (square p) (* 2 m))        (V (ref q 0) (ref q 1))))) `

Hamilton's equations are[^9^](#footnote_Temp_236)

`(show-expression   (((Hamilton-equations       (H-rectangular            'm           (literal-function 'V (-> (X Real Real) Real))))      (up (literal-function 'x) (literal-function 'y))      (down (literal-function 'p_x) (literal-function 'p_y)))     't)) `

------------------------------------------------------------------------

<div align="left">

![](chap3-Z-G-29.gif)

</div>

------------------------------------------------------------------------

The zero in the first element of the structure of Hamilton's equation
residuals is just the tautology that time advances uniformly: the time
function is just the identity, so its derivative is one and the residual
is zero. The equations in the second element of the structure relate the
coordinate paths and the momentum paths. The equations in the third
element give the rate of change of the momenta in terms of the applied
forces.

**Exercise 3.3.**  **Computing Hamilton's equations**\
 Check your answers to exercise [3.1](#%_thm_3.1) with the
`Hamilton-equations` procedure.

### [3.1.1  The Legendre Transformation](book-Z-H-4.html#%_toc_%_sec_3.1.1)

The Legendre transformation abstracts a key part of the process of
transforming from the Lagrangian to the Hamiltonian formulation of
mechanics -- the replacement of functional dependence on generalized
velocities with functional dependence on generalized momenta. The
momentum state function is defined as a partial derivative of the
Lagrangian, a real-valued function of time, coordinates, and velocities.
The Legendre transformation provides an inverse that gives the
velocities in terms of the momenta: we are able to write the velocities
as a partial derivative of a different real-valued function of time,
coordinates, and momenta.[^10^](#footnote_Temp_238)

Given a real-valued function *F*, if we can find a real-valued function
*G* such that *DF* = (*DG*)^`-`1^, then we say that *F* and *G* are
related by a Legendre transform.

Locally, we can define the inverse function[^11^](#footnote_Temp_239)
![](chap1-Z-G-D-27.gif) of *DF* so that *DF* o ![](chap1-Z-G-D-27.gif) =
*I*, where *I* is the identity function *I*(*w*) = *w*. Consider the
composite function ![](chap1-Z-G-D-47.gif) = *F* o
![](chap1-Z-G-D-27.gif). The derivative of ![](chap1-Z-G-D-47.gif) is

<div align="left">

![](chap3-Z-G-30.gif)

</div>

Using the product rule and *DI* = 1, we have

<div align="left">

![](chap3-Z-G-31.gif)

</div>

or

<div align="left">

![](chap3-Z-G-32.gif)

</div>

The integral is determined up to a constant of integration. If we define

<div align="left">

![](chap3-Z-G-33.gif)

</div>

then we have

<div align="left">

![](chap3-Z-G-34.gif)

</div>

The function *G* has the desired property that *DG* is the inverse
function ![](chap1-Z-G-D-27.gif) of *DF*. The derivation just given
applies equally well if the arguments of *F* and *G* have multiple
components.

Given a relation *w* = *DF*(*v*) for some given function *F*, then *v* =
*DG*(*w*) for *G* = *I*![](chap1-Z-G-D-27.gif) `-` *F* o
![](chap1-Z-G-D-27.gif), where ![](chap1-Z-G-D-27.gif) is the inverse
function of *DF* provided it exists.

<div align="left">

![](chap3-Z-G-35.gif)

</div>

A picture may help (see figure [3.1](#FIGURE_3.1)). The curve is the
graph of the function *DF*. Turned sideways, it is also the graph of the
function *DG*, because *DG* is the inverse function of *DF*. The
integral of *DF* from *v*~0~ to *v* is *F*(*v*) `-` *F*(*v*~0~); this is
the area below the curve from *v*~0~ to *v*. Likewise, the integral of
*DG* from *w*~0~ to *w* is *G*(*w*) `-` *G*(*w*~0~); this is the area to
the left of the curve from *w*~0~ to *w*. The union of these two regions
has area *w* *v* `-` *w*~0~ *v*~0~. So

<div align="left">

![](chap3-Z-G-36.gif)

</div>

which is the same as

<div align="left">

![](chap3-Z-G-37.gif)

</div>

The left-hand side depends only on the point labeled by *w* and *v* and
the right-hand side depends only on the point labeled by *w*~0~ and
*v*~0~, so these must be constant, independent of the variable
endpoints. So as the point is changed the combination *G*(*w*) +
*F*(*v*) `-` *wv* is invariant. Thus

<div align="left">

![](chap3-Z-G-38.gif)

</div>

with constant *C*. The requirement for *G* depends only on *DG* so we
can choose to define *G* with *C* = 0.

#### [Legendre transformations with passive arguments](book-Z-H-4.html#%_toc_%_sec_Temp_240)

Let *F* be a real-valued function of two arguments and

<div align="left">

![](chap3-Z-G-39.gif)

</div>

If we can find a real-valued function *G* such that

<div align="left">

![](chap3-Z-G-40.gif)

</div>

we say that *F* and *G* are related by a Legendre transformation, that
the second argument in each function is *active*, and that the first
argument is *passive* in the transformation.

If the function ![](front-Z-G-D-2.gif)~1~ *F* can be locally inverted
with respect to the second argument we can define

<div align="left">

![](chap3-Z-G-41.gif)

</div>

giving

<div align="left">

![](chap3-Z-G-42.gif)

</div>

where *W* = *I*~1~ is the selector function for the second argument.

For the active arguments the derivation goes through as before. The
first argument to *F* and *G* is just along for the ride -- it is a
passive argument. Let

<div align="left">

![](chap3-Z-G-43.gif)

</div>

then define

<div align="left">

![](chap3-Z-G-44.gif)

</div>

We can check that *G* has the property ![](chap1-Z-G-D-27.gif) =
![](front-Z-G-D-2.gif)~1~ *G* by carrying out the derivative:

<div align="left">

![](chap3-Z-G-45.gif)

</div>

but

<div align="left">

![](chap3-Z-G-46.gif)

</div>

or

<div align="left">

![](chap3-Z-G-47.gif)

</div>

So

<div align="left">

![](chap3-Z-G-48.gif)

</div>

as required. The active argument may have many components.

The partial derivatives with respect to the passive arguments are
related in a remarkably simple way. Let's calculate the derivative
![](front-Z-G-D-2.gif)~0~ *G* in pieces. First,

<div align="left">

![](chap3-Z-G-49.gif)

</div>

because ![](front-Z-G-D-2.gif)~0~ *W* = 0. To calculate
![](front-Z-G-D-2.gif)~0~ ![](chap1-Z-G-D-47.gif) we must supply
arguments:

<div align="left">

![](chap3-Z-G-50.gif)

</div>

Putting these together, we find

<div align="left">

![](chap3-Z-G-51.gif)

</div>

The calculation is unchanged if the passive argument has many
components.

We can write the Legendre transformation more symmetrically:

<div align="left">

![](chap3-Z-G-52.gif)

</div>

The last relation is not as trivial as it looks, because *x* enters the
equations connecting *w* and *v*. With this symmetrical form, we see
that the Legendre transform is its own inverse.

**Exercise 3.4.**  **Simple Legendre transforms**\
 For each of the following functions, find the function that is related
to the given function by the Legendre transform on the indicated active
argument. Show that the Legendre transform relations hold for your
solution, including the relations among passive arguments, if any.

**a**.  *F*(*x*) = *a* *x* + *b* *x*^2^, with no passive arguments.

**b**.  *F*(*x*, *y*) = *a* sin *x* cos *y*, with *x* active.

**c**.  *F*(*x*, *y*, ![](chap1-Z-G-D-37.gif), ![](chap3-Z-G-D-1.gif)) =
*x* ![](chap1-Z-G-D-37.gif)^2^ + 3 ![](chap1-Z-G-D-37.gif)
![](chap3-Z-G-D-1.gif) + *y* ![](chap3-Z-G-D-1.gif)^2^, with
![](chap1-Z-G-D-37.gif) and ![](chap3-Z-G-D-1.gif) active.

#### [Hamilton's equations from the Legendre transformation](book-Z-H-4.html#%_toc_%_sec_Temp_242)

We can use the Legendre transformation with the Lagrangian playing the
role of *F* and with the generalized velocity slot playing the role of
the active argument. The Hamiltonian plays the role of *G* with the
momentum slot active. The coordinate and time slots are passive
arguments.

The Lagrangian *L* and the Hamiltonian *H* are related by a Legendre
transformation:

<div align="left">

![](chap3-Z-G-53.gif)

</div>

<div align="left">

![](chap3-Z-G-54.gif)

</div>

and

<div align="left">

![](chap3-Z-G-55.gif)

</div>

with passive equations

<div align="left">

![](chap3-Z-G-56.gif)

</div>

Presuming it exists, we can define the inverse of
![](front-Z-G-D-2.gif)~2~ *L* with respect to the last argument:

<div align="left">

![](chap3-Z-G-57.gif)

</div>

and write the Hamiltonian

<div align="left">

![](chap3-Z-G-58.gif)

</div>

These relations are purely algebraic in nature.

On a path *q* we have the momentum *p*:

<div align="left">

![](chap3-Z-G-59.gif)

</div>

and from the definition of ![](chap1-Z-G-D-27.gif) we find

<div align="left">

![](chap3-Z-G-60.gif)

</div>

The Legendre transform gives

<div align="left">

![](chap3-Z-G-61.gif)

</div>

This relation is purely algebraic and is valid for any path. The passive
equation ([3.53](#EQUATION_3.53)) gives

<div align="left">

![](chap3-Z-G-62.gif)

</div>

but the left-hand side can be rewritten using the Lagrange equations, so

<div align="left">

![](chap3-Z-G-63.gif)

</div>

This equation is valid only for realizable paths, because we used the
Lagrange equations to derive it. Equations ([3.58](#EQUATION_3.58)) and
([3.60](#EQUATION_3.60)) are Hamilton's equations.

The remaining passive equation is

<div align="left">

![](chap3-Z-G-64.gif)

</div>

This passive equation says that the Lagrangian has no explicit time
dependence (![](front-Z-G-D-2.gif)~0~ *L* = 0) if and only if the
Hamiltonian has no explicit time dependence (![](front-Z-G-D-2.gif)~0~
*H* = 0). We have found that if the Lagrangian has no explicit time
dependence, then energy is conserved. So if the Hamiltonian has no
explicit time dependence then it is a conserved quantity.

**Exercise 3.5.**  ****\
 Using Hamilton's equations, show directly that the Hamiltonian is a
conserved quantity if it has no explicit time dependence.

#### [Legendre transforms of quadratic functions](book-Z-H-4.html#%_toc_%_sec_Temp_244)

We cannot implement the Legendre transform in general because it
involves finding the functional inverse of an arbitrary function.
However, many physical systems can be described by Lagrangians that are
quadratic forms in the generalized velocities. For such functions the
generalized momenta are linear functions of the generalized velocities,
and thus explicitly invertible.

More generally, we can compute a Legendre transformation for polynomial
functions where the leading term is a quadratic form:

<div align="left">

![](chap3-Z-G-65.gif)

</div>

We can assume *M* is symmetric,[^12^](#footnote_Temp_245) because it
defines a quadratic form. We can find linear expressions for *w* as

<div align="left">

![](chap3-Z-G-66.gif)

</div>

So if *M* is invertible we can solve for *v* in terms of *w*. Thus we
may define a function ![](chap1-Z-G-D-27.gif) such that

<div align="left">

![](chap3-Z-G-67.gif)

</div>

and we can use this to compute the value of the function *G*:

<div align="left">

![](chap3-Z-G-68.gif)

</div>

#### [Computing Hamiltonians](book-Z-H-4.html#%_toc_%_sec_Temp_246)

We implement the Legendre transform for quadratic functions by the
procedure[^13^](#footnote_Temp_247)

`(define (Legendre-transform F)   (let ((w-of-v (D F)))     (define (G w)       (let ((z (dual-zero w)))         (let ((M ((D w-of-v) z))               (b (w-of-v z)))           (let ((v (/ (- w b) M)))             (- (* w v) (F v))))))     G)) `

The procedure `Legendre-transform` takes a procedure of one argument and
returns the procedure that is associated with it by the Legendre
transform. If *w* = *DF*(*v*), *wv* = *F*(*v*) + *G*(*w*), and *v* =
*DG*(*w*) specifies a one-argument Legendre transformation, then *G* is
the function associated with *F* by the Legendre transform: *G* = *I*
![](chap1-Z-G-D-27.gif) `-` *F* o ![](chap1-Z-G-D-27.gif), where
![](chap1-Z-G-D-27.gif) is the functional inverse of *DF*.

We can use the `Legendre-transform` procedure to compute a Hamiltonian
from a Lagrangian:

`(define ((Lagrangian->Hamiltonian Lagrangian) H-state)   (let ((t (time H-state))         (q (coordinate H-state))         (p (momentum H-state)))     (define (L qdot)       (Lagrangian (up t q qdot)))     ((Legendre-transform L) p))) `

Notice that the one-argument `Legendre-transform` procedure is
sufficient. The passive variables are given no special attention, they
are just passed around.

The Lagrangian may be obtained from the Hamiltonian by the procedure:

`(define ((Hamiltonian->Lagrangian Hamiltonian) L-state)   (let ((t (time L-state))         (q (coordinate L-state))         (qdot (velocity L-state)))     (define (H p)       (Hamiltonian (up t q p)))     ((Legendre-transform H) qdot))) `

Notice that the two procedures `Hamiltonian->Lagrangian` and
`Lagrangian->Hamiltonian` are identical, except for the names.

For example, the Hamiltonian for the motion of the point mass with the
potential energy *V*(*x*, *y*) may be computed from the Lagrangian:

`(define ((L-rectangular m V) local)   (let ((q (coordinate local))         (qdot (velocity local)))     (- (* 1/2 m (square qdot))        (V (ref q 0) (ref q 1))))) `

And the Hamiltonian is

`(show-expression   ((Lagrangian->Hamiltonian    (L-rectangular        'm       (literal-function 'V (-> (X Real Real) Real))))   (up 't (up 'x 'y) (down 'p_x 'p_y)))) `

------------------------------------------------------------------------

<div align="left">

![](chap3-Z-G-69.gif)

</div>

------------------------------------------------------------------------

**Exercise 3.6.**  **On a helical track**\
 A uniform cylinder of mass *M*, radius *R*, and height *h* is mounted
so as to rotate freely on a vertical axis. A mass point of mass *m* is
constrained to move on a uniform frictionless helical track of pitch *ß*
(measured in radians per meter of drop along the cylinder) mounted on
the surface of the cylinder (see figure [3.2](#FIGURE_3.2)). The mass is
acted upon by standard gravity (*g* = 9.8 ms^`-`2^).

<div align="left">

![](chap3-Z-G-70.gif)

</div>

**a**.  What are the degrees of freedom of this system? Pick and
describe a convenient set of generalized coordinates for this problem.
Write a Lagrangian to describe the dynamical behavior. It may help to
know that the moment of inertia of a cylinder around its axis is
(1/2)*MR*^2^. You may find it easier to do the algebra if various
constants are combined and represented as single symbols.

**b**.  Make a Hamiltonian for the system. Write Hamilton's equations
for the system. Are there any conserved quantities?

**c**.  If we release the mass point at time *t* = 0 at the top of the
track with zero initial speed and let it slide down, what is the motion
of the system?

**Exercise 3.7.**  **An ellipsoidal bowl**\
 Consider a point particle of mass *m* constrained to move in a bowl and
acted upon by a uniform gravitational acceleration *g*. The bowl is
ellipsoidal, with height *z* = *a* *x*^2^ + *b* *y*^2^. Make a
Hamiltonian for this system. Can you make any immediate deductions about
this system?

### [3.1.2  Hamilton's Equations from the Action Principle](book-Z-H-4.html#%_toc_%_sec_3.1.2)

The previous two derivations of Hamilton's equations have made use of
the Lagrange equations. Hamilton's equations can also be derived
directly from the action principle.

The action is the integral of the Lagrangian along a path:

<div align="left">

![](chap3-Z-G-71.gif)

</div>

The action is stationary with respect to variations of the path that
preserve the configuration at the endpoints (for Lagrangians that are
functions of time, coordinates, and velocities).

We can rewrite the integrand in terms of the Hamiltonian

<div align="left">

![](chap3-Z-G-72.gif)

</div>

with *p*(*t*) = ![](front-Z-G-D-2.gif)~2~ *L*(*t*, *q*(*t*), *Dq*(*t*)).
The Legendre transformation construction gives

<div align="left">

![](chap3-Z-G-73.gif)

</div>

which is one of Hamilton's equations, the one that does not depend on
the path being a realizable path.

In order to vary the action we need to make the dependences on the path
explicit. We introduce

<div align="left">

![](chap3-Z-G-74.gif)

</div>

so *p*(*t*) = ![](chap3-Z-G-D-3.gif)[*q*](*t*)
and[^14^](#footnote_Temp_250)

<div align="left">

![](chap3-Z-G-75.gif)

</div>

The integrand of the action integral is then

<div align="left">

![](chap3-Z-G-76.gif)

</div>

The variation of the action is

<div align="left">

![](chap3-Z-G-77.gif)

</div>

where ![](chap1-Z-G-D-17.gif) ![](chap3-Z-G-D-3.gif)[*q*] is the
variation in the momentum.[^15^](#footnote_Temp_251) Integrating the
second term by parts, using *D*(![](chap3-Z-G-D-3.gif)[*q*]
![](chap1-Z-G-D-17.gif) *q*) = *D*(![](chap3-Z-G-D-3.gif)[*q*])
![](chap1-Z-G-D-17.gif) *q* + ![](chap3-Z-G-D-3.gif)[*q*] *D*
![](chap1-Z-G-D-17.gif) *q*, we get

<div align="left">

![](chap3-Z-G-79.gif)

</div>

The variations are constrained so that ![](chap1-Z-G-D-17.gif)
*q*(*t*~1~) = ![](chap1-Z-G-D-17.gif) *q*(*t*~2~) = 0, so the integrated
part vanishes. The variation of the action is

<div align="left">

![](chap3-Z-G-80.gif)

</div>

As a consequence of equation ([3.68](#EQUATION_3.68)), the factor
multiplying ![](chap1-Z-G-D-17.gif) ![](chap3-Z-G-D-3.gif)[*q*] is zero.
We are left with

<div align="left">

![](chap3-Z-G-81.gif)

</div>

For the variation of the action to be zero for arbitrary variations,
except for the endpoint conditions, we must have

<div align="left">

![](chap3-Z-G-82.gif)

</div>

Using using *p*(*t*) = ![](chap3-Z-G-D-3.gif)[*q*](*t*), this is

<div align="left">

![](chap3-Z-G-83.gif)

</div>

which is the \`\`dynamical'' Hamilton
equation.[^16^](#footnote_Temp_252)

### [3.1.3  A Wiring Diagram](book-Z-H-4.html#%_toc_%_sec_3.1.3)

Figure [3.3](#FIGURE_3.3) shows a summary of the functional relationship
between the Lagrangian and the Hamiltonian descriptions of a dynamical
system. The diagram shows a \`\`circuit'' interconnecting some
\`\`devices'' with \`\`wires.'' The devices represent the mathematical
functions that relate the quantities on their terminals. The wires
represent identifications of the quantities on the terminals that they
connect. For example, there is a box that represents the Lagrangian
function. Given values *t*, *q*, and ![](front-Z-G-D-1.gif), the value
of the Lagrangian *L*(*t*, *q*, ![](front-Z-G-D-1.gif)) is on the
terminal labeled *L*, which is wired to an addend terminal of an adder.
Other terminals of the Lagrangian carry the values of the partial
derivatives of the Lagrangian function.

<div align="left">

![](chap3-Z-G-84.gif)

</div>

The upper part of the diagram summarizes the relationship of the
Hamiltonian to the Lagrangian. For example, the sum of the values on the
terminals *L* of the Lagrangian and *H* of the Hamiltonian is the
product of the value on the ![](front-Z-G-D-1.gif) terminal of the
Lagrangian and the value on the *p* terminal of the Hamiltonian. This is
the active part of the Legendre transform. The passive variables are
related by the corresponding partial derivatives being negations of each
other. In the lower part of the diagram the equations of motion are
indicated by the presence of the integrators, relating the dynamical
quantities to their time derivatives.

One can use this diagram to help understand the underlying unity of the
Lagrangian and Hamiltonian formulations of mechanics. Lagrange's
equations are just the connection of the ![](chap3-Z-G-D-4.gif) wire to
the ![](front-Z-G-D-2.gif)~1~ *L* terminal of the Lagrangian device. One
of Hamilton's equations is just the connection of the
![](chap3-Z-G-D-4.gif) wire (through the negation device) to the
![](front-Z-G-D-2.gif)~1~ *H* terminal of the Hamiltonian device. The
other is just the connection of the ![](front-Z-G-D-1.gif) wire to the
![](front-Z-G-D-2.gif)~2~ *H* terminal of the Hamiltonian device. We see
that the two formulations are consistent. One does not have to abandon
any part of the Lagrangian formulation to use the Hamiltonian
formulation: there are deductions that can be made using both
simultaneously.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^1^](#call_footnote_Temp_223) Here we restrict our attention to
Lagrangians that depend only on the time, the coordinates, and the
velocities.

[^2^](#call_footnote_Temp_224) Here we are using mnemonic names *t*,
*q*, *p* for formal parameters of the function being defined. We could
have used names like *a*, *b*, *c* as above, but this would have made
the argument harder to read.

[^3^](#call_footnote_Temp_225) *P* = *I*~2~.

[^4^](#call_footnote_Temp_226) The overall minus sign in the definition
of the Hamiltonian is traditional.

[^5^](#call_footnote_Temp_227) In traditional notation, Hamilton's
equations are written:

<div align="left">

![](chap3-Z-G-17.gif)

</div>

or as separate equations for each component:

<div align="left">

![](chap3-Z-G-18.gif)

</div>

[^6^](#call_footnote_Temp_228) Traditionally, the Hamiltonian is written

<div align="left">

![](chap3-Z-G-20.gif)

</div>

This way of writing the Hamiltonian confuses the values of functions
with the functions that generate them: both ![](front-Z-G-D-1.gif) and
*L* must be reexpressed as functions of the time, coordinates, and
momenta.

[^7^](#call_footnote_Temp_233) In the construction of the Lagrangian
state derivative from the Lagrange equations we must solve for the
highest-order derivative. The solution process requires the inversion of
![](front-Z-G-D-2.gif)~2~ ![](front-Z-G-D-2.gif)~2~ *L*. In the
construction of Hamilton's equations, the construction of
![](chap1-Z-G-D-27.gif) from the momentum state function
![](front-Z-G-D-2.gif)~2~ *L* requires the inverse of the same
structure. If the Lagrangian formulation has singularities, they cannot
be avoided by going to the Hamiltonian formulation.

[^8^](#call_footnote_Temp_234) The term *phase space* was introduced by
Josiah Willard Gibbs in his formulation of statistical mechanics. The
Hamiltonian plays a fundamental role in the Boltzmann-Gibbs formulation
of statistical mechanics and in both the Heisenberg and Schrödinger
approaches to quantum mechanics.

The momentum *p* can be viewed as the coordinate representation of a
linear form on the tangent space. Thus *p*![](front-Z-G-D-1.gif) is a
scalar quantity that is invariant under time-independent coordinate
transformations of the configuration space. The set of momentum forms
comprise an *n*-dimensional vector space at each point of the
configuration space called the *cotangent space*. The collection of all
cotangent spaces of a configuration space forms a space called the
*cotangent bundle* of the configuration manifold.

[^9^](#call_footnote_Temp_236) By default, literal functions map reals
to reals; the default type for a literal function is `(-> Real Real)`.
Here, the potential energy `V` takes two real arguments and returns a
real.

[^10^](#call_footnote_Temp_238) The Legendre transformation is more
general than its use in mechanics in that it captures the relationship
between conjugate variables in systems as diverse as thermodynamics,
circuits, and field theory.

[^11^](#call_footnote_Temp_239) This can be done so long as the
derivative is not zero.

[^12^](#call_footnote_Temp_245) If ***M*** is the matrix representation
of *M*, then ***M*** = ***M***^`T`^.

[^13^](#call_footnote_Temp_247) The division operation, denoted by `/`
in the `  Legendre-transform` procedure, is generic over mathematical
objects. We interpret the division in the matrix representation as
follows: a vector ***y*** divided by a matrix ***M*** is interpreted as
a request to solve the linear system ***M*** ***x*** = ***y***, where
***x*** is the unknown vector.

[^14^](#call_footnote_Temp_250) The function ![](chap3-Z-G-D-2.gif)[*q*]
is the same as ![](chap3-Z-G-D-2.gif)~*L*~[*q*] introduced previously.
Indeed, the Lagrangian is needed to define momentum in every case, but
we are suppressing the dependency here because it does not matter in
this argument.

[^15^](#call_footnote_Temp_251) The variation of the momentum
![](chap1-Z-G-D-17.gif) ![](chap3-Z-G-D-3.gif)[*q*] need not be further
expanded in this argument because it turns out that the factor
multiplying it is zero.  However, it is handy to see how it is related
to the variations in the coordinate path ![](chap1-Z-G-D-17.gif) *q*:

<div align="left">

![](chap3-Z-G-78.gif)

</div>

[^16^](#call_footnote_Temp_252) It is sometimes asserted that the
momenta have a different status in the Lagrangian and Hamiltonian
formulations: that in the Hamiltonian framework the momenta are
\`\`independent'' of the coordinates. From this it is argued that the
variations ![](chap1-Z-G-D-17.gif) *q* and ![](chap1-Z-G-D-17.gif) *p*
are arbitrary and independent, therefore implying that the factor
multiplying each of them in the action integral ([3.74](#EQUATION_3.74))
must independently be zero, apparently deriving both of Hamilton's
equations. The argument is fallacious: we can write
![](chap1-Z-G-D-17.gif) *p* in terms of ![](chap1-Z-G-D-17.gif) *q* (see
footnote [15](#footnote_Temp_251)).

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-36.html)</span><span>,
[next](book-Z-H-38.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-27.html)</span><span>,
[next](book-Z-H-29.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[2.8  Vector Angular Momentum](book-Z-H-4.html#%_toc_%_sec_2.8)
---------------------------------------------------------------

The vector angular momentum of a particle is the cross product of the
position and the linear momentum. For a rigid body the vector angular
momentum is the sum of the vector angular momentum of each of the
constituents. Here we find an expression for the vector angular momentum
of a rigid body in terms of the inertia tensor and the angular velocity
vector.

The vector angular momentum of a rigid body is

<div align="left">

![](chap2-Z-G-49.gif)

</div>

where ![](chap1-Z-G-D-26.gif)~![](chap1-Z-G-D-21.gif)~,
![](chap2-Z-G-D-1.gif)~![](chap1-Z-G-D-21.gif)~, and
*m*~![](chap1-Z-G-D-21.gif)~ are the positions, velocities, and masses
of the constituent particles. It turns out that the vector angular
momentum decomposes into the sum of the angular momentum of the center
of mass and the rotational angular momentum about the center of mass,
just as the kinetic energy separates into the kinetic energy of the
center of mass and the kinetic energy of rotation. As in the kinetic
energy demonstration, decompose the position into the vector to the
center of mass ![](chap2-Z-G-D-2.gif) and the vectors from the center of
mass to the constituent mass elements
![](chap2-Z-G-D-3.gif)~![](chap1-Z-G-D-21.gif)~:

<div align="left">

![](chap2-Z-G-50.gif)

</div>

with velocities

<div align="left">

![](chap2-Z-G-51.gif)

</div>

Substituting, the angular momentum is

<div align="left">

![](chap2-Z-G-52.gif)

</div>

Multiplying out the product, and using the fact that
![](chap2-Z-G-D-2.gif) is the center of mass and *M* =
sum~![](chap1-Z-G-D-21.gif)~ *m*~![](chap1-Z-G-D-21.gif)~ is the total
mass of the body, the angular momentum is

<div align="left">

![](chap2-Z-G-53.gif)

</div>

The angular momentum of the center of mass is

<div align="left">

![](chap2-Z-G-54.gif)

</div>

and the rotational angular momentum is

<div align="left">

![](chap2-Z-G-55.gif)

</div>

We can also reexpress the rotational angular momentum in terms of the
angular velocity vector and the inertia tensor, as we did for the
kinetic energy. Using ![](chap2-Z-G-D-5.gif)~![](chap1-Z-G-D-21.gif)~ =
![](chap2-Z-G-D-8.gif) ×
![](chap2-Z-G-D-3.gif)~![](chap1-Z-G-D-21.gif)~, we get the rotational
angular momentum

<div align="left">

![](chap2-Z-G-56.gif)

</div>

In terms of components with respect to the basis
{![](chap2-Z-G-D-9.gif)~0~, ![](chap2-Z-G-D-9.gif)~1~,
![](chap2-Z-G-D-9.gif)~2~}, this is

<div align="left">

![](chap2-Z-G-57.gif)

</div>

where *I*~*jk*~ are the components of the inertia
tensor ([2.14](book-Z-H-23.html#EQUATION_2.14)). The angular momentum
and the kinetic energy are expressed in terms of the same inertia
tensor.

With respect to the principal-axis basis, the angular momentum
components have a particularly simple form:

<div align="left">

![](chap2-Z-G-58.gif)

</div>

**Exercise 2.9.**  ****\
 Verify that expression ([2.52](#EQUATION_2.52)) for the components of
the rotational angular momentum ([2.51](#EQUATION_2.51)) in terms of the
inertia tensor is correct.

We can define procedures to calculate the components of the angular
momentum on the principal axes:

`(define ((Euler-state->L-body A B C) local)   (let ((omega-body (Euler-state->omega-body local)))     (column-matrix (* A (ref omega-body 0))                    (* B (ref omega-body 1))                    (* C (ref omega-body 2))))) `

We then transform the components of the angular momentum on the
principal axes to the components on the fixed basis
![](chap2-Z-G-D-9.gif)~*i*~:

`(define ((Euler-state->L-space A B C) local)   (let ((angles (coordinate local)))     (* (Euler->M angles)        ((Euler-state->L-body A B C) local)))) `

These procedures are local state functions, like Lagrangians.

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-27.html)</span><span>,
[next](book-Z-H-29.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


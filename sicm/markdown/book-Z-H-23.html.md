<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-22.html)</span><span>,
[next](book-Z-H-24.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[2.3  Moments of Inertia](book-Z-H-4.html#%_toc_%_sec_2.3)
----------------------------------------------------------

The rotational kinetic energy is the sum of the kinetic energy of each
of the constituents of the rigid body. We can rewrite the rotational
kinetic energy in terms of the angular velocity vector and certain
aggregate quantities determined by the distribution of mass in the rigid
body.

Substituting our representation of the relative velocity vectors into
the rotational kinetic energy, we obtain

<div align="left">

![](chap2-Z-G-12.gif)

</div>

We introduce an arbitrary rectangular coordinate system with origin at
the center of rotation and with basis vectors ![](chap2-Z-G-D-9.gif)~0~,
![](chap2-Z-G-D-9.gif)~1~, and ![](chap2-Z-G-D-9.gif)~2~, with the
property that ![](chap2-Z-G-D-9.gif)~0~ × ![](chap2-Z-G-D-9.gif)~1~ =
![](chap2-Z-G-D-9.gif)~2~. The components of ![](chap2-Z-G-D-8.gif) on
this coordinate system are ![](chap1-Z-G-D-23.gif)^0^,
![](chap1-Z-G-D-23.gif)^1^, and ![](chap1-Z-G-D-23.gif)^2^. Rewriting
![](chap2-Z-G-D-8.gif) in terms of its components, the rotational
kinetic energy becomes

<div align="left">

![](chap2-Z-G-13.gif)

</div>

with

<div align="left">

![](chap2-Z-G-14.gif)

</div>

The quantities *I*~*ij*~ are the components of the *inertia tensor* with
respect to the chosen coordinate system.

Note what a remarkable form the kinetic energy has taken. All we have
done is interchange the order of summations, but now the kinetic energy
is written as a sum of products of components of the angular velocity
vector, which completely specify how the orientation of the body is
changing, and the quantity *I*~*ij*~, which depends solely on the
distribution of mass in the body relative to the chosen coordinate
system.

We will deduce a number of properties of the inertia tensor. First, we
find a somewhat simpler expression for it. The components of the vector
![](chap2-Z-G-D-3.gif)~![](chap1-Z-G-D-21.gif)~ are (
![](chap1-Z-G-D-18.gif)~![](chap1-Z-G-D-21.gif)~,
![](chap1-Z-G-D-13.gif)~![](chap1-Z-G-D-21.gif)~,
![](chap2-Z-G-D-10.gif)~![](chap1-Z-G-D-21.gif)~
).[^3^](#footnote_Temp_177) If we rewrite
![](chap2-Z-G-D-3.gif)~![](chap1-Z-G-D-21.gif)~ as a sum over its
components and simplify the elementary vector products of basis vectors,
we can obtain the components of the inertia tensor. We can arrange the
components of the inertia tensor to form the *inertia matrix* ***I***,
which looks like:

<div align="left">

![](chap2-Z-G-15.gif)

</div>

The inertia tensor has real components and is symmetric: *I*~*jk*~ =
*I*~*kj*~.

We define the *moment of inertia* *I* about a line by

<div align="left">

![](chap2-Z-G-16.gif)

</div>

where ![](chap1-Z-G-D-18.gif)~![](chap1-Z-G-D-21.gif)~^|^ is the
perpendicular distance from the line to the constituent with index
![](chap1-Z-G-D-21.gif). The diagonal components of the inertia tensor
*I*~*ii*~ are recognized as the moments of inertia about the lines
coinciding with the coordinate axes ![](chap2-Z-G-D-9.gif)~*i*~. The
off-diagonal components of the inertia tensor are called *products of
inertia*.

The rotational kinetic energy of a body depends on the distribution of
mass of the body solely through the inertia tensor. Remarkably, the
inertia tensor involves only second-order moments of the mass
distribution with respect to the center of mass. We might have expected
the kinetic energy to depend in a complicated way on all the moments of
the mass distribution, interwoven in some complicated way with the
components of the angular velocity vector, but this is not the case.
This fact has a remarkable consequence: for the motion of a free rigid
body the detailed shape of the body does not matter. If a book and a
banana have the same inertia tensor, that is, the same second-order mass
moments, then if they are thrown in the same way the subsequent motion
will be the same, however complicated that motion is. The fact that the
book has corners and the banana has a stem do not affect the motion
except for their contributions to the inertia tensor. In general, the
potential energy of an extended body is not so simple and does indeed
depend on all moments of the mass distribution, but for the kinetic
energy the second moments are all that matter!

**Exercise 2.1.**  **Rotational kinetic energy**\
 Show that the rotational kinetic energy can also be written

<div align="left">

![](chap2-Z-G-17.gif)

</div>

where *I* is the moment of inertia about the line through the center of
mass with direction ![](chap2-Z-G-D-11.gif), and ![](chap1-Z-G-D-23.gif)
is the instantaneous rate of rotation.

**Exercise 2.2.**  **Steiner's theorem**\
 Let *I* be the moment of inertia of a body with respect to some given
line through the center of mass. Show that the moment of inertia *I*'
with respect to a second line parallel to the first is

<div align="left">

![](chap2-Z-G-18.gif)

</div>

where *M* is the total mass of the body and *R* is the distance between
the lines.

**Exercise 2.3.**  **Some useful moments of inertia**\
 Show that the moments of inertia of the following objects are as given:

**a**.  The moment of inertia of a sphere of uniform density with mass
*M* and radius *R* about any line through the center is (2/5) *MR*^2^.

**b**.  The moment of inertia of a spherical shell with mass *M* and
radius *R* about any line through the center is (2/3)*MR*^2^.

**c**.  The moment of inertia of a cylinder of uniform density with mass
*M* and radius *R* about the axis of the cylinder is (1/2) *MR*^2^.

**c**.  The moment of inertia of a thin rod of uniform density per unit
length with mass *M* and length *L* about an axis perpendicular to the
rod through the center of mass is (1/12) *ML*^2^.

**Exercise 2.4.**  **Jupiter**\
\
**a**.  The density of a planet increases toward the center. Provide an
argument that the moment of inertia of a planet is less than that of a
sphere of uniform density of the same mass and radius.

**b**.  The density as a function of radius inside Jupiter is well
approximated by

<div align="left">

![](chap2-Z-G-19.gif)

</div>

where *M* is the mass and *R* is the radius of Jupiter. Find the moment
of inertia of Jupiter in terms of *M* and *R*.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^3^](#call_footnote_Temp_177) Here we avoid the more consistent
notation (![](chap1-Z-G-D-18.gif)~![](chap1-Z-G-D-21.gif)~^0^,
![](chap1-Z-G-D-18.gif)~![](chap1-Z-G-D-21.gif)~^1^,
![](chap1-Z-G-D-18.gif)~![](chap1-Z-G-D-21.gif)~^2^) for the components
of ![](chap2-Z-G-D-3.gif)~![](chap1-Z-G-D-21.gif)~ because expressions
involving powers of the components are awkward in this form.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-22.html)</span><span>,
[next](book-Z-H-24.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


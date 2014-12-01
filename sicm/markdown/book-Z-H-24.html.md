<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-23.html)</span><span>,
[next](book-Z-H-25.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[2.4  Inertia Tensor](book-Z-H-4.html#%_toc_%_sec_2.4)
------------------------------------------------------

The representation of the rotational kinetic energy in terms of the
inertia tensor was derived with the help of a rectangular coordinate
system with basis vectors ![](chap2-Z-G-D-9.gif)~*i*~. There was nothing
special about this particular rectangular basis. So, the kinetic energy
must have the same form in any rectangular coordinate system. We can use
this fact to derive how the inertia tensor changes if the body or the
coordinate system is rotated.

Let's talk a bit about *active* and *passive* rotations. The rotation of
the vector ![](chap1-Z-G-D-26.gif) by the rotation *R* produces a new
vector ![](chap1-Z-G-D-26.gif)' = *R* ![](chap1-Z-G-D-26.gif). We may
write ![](chap1-Z-G-D-26.gif) in terms of its components with respect to
some arbitrary rectangular coordinate system with orthonormal basis
vectors ![](chap2-Z-G-D-9.gif)~*i*~: ![](chap1-Z-G-D-26.gif) = *x*^0^
![](chap2-Z-G-D-9.gif)~0~ + *x*^1^ ![](chap2-Z-G-D-9.gif)~1~ + *x*^2^
![](chap2-Z-G-D-9.gif)~2~. Let ***x*** indicate the column matrix of
components *x*^0^, *x*^1^, and *x*^2^ of ![](chap1-Z-G-D-26.gif), and
***R*** be the matrix representation of *R* with respect to the same
basis. In these terms the rotation can be written ***x***' = ***R***
***x***. The rotation matrix ***R*** is a real orthogonal
matrix.[^4^](#footnote_Temp_182) A rotation that carries vectors to new
vectors is called an *active* rotation.

Alternately, we can rotate the coordinate system by rotating the basis
vectors, but leave other vectors that might be represented in terms of
them unchanged. If a vector is unchanged but the basis vectors are
rotated, then the components of the vector on the rotated basis vectors
are not the same as the components on the original basis vectors. Denote
the rotated basis vectors by ![](chap2-Z-G-D-9.gif)~*i*~' = *R*
![](chap2-Z-G-D-9.gif)~*i*~. The component of a vector along a basis
vector is the dot product of the vector with the basis vector. So the
components of the vector ![](chap1-Z-G-D-26.gif) along the rotated basis
![](chap2-Z-G-D-9.gif)~*i*~' are (*x*')^*i*^ = ![](chap1-Z-G-D-26.gif) ·
![](chap2-Z-G-D-9.gif)~*i*~' = ![](chap1-Z-G-D-26.gif) · (*R*
![](chap2-Z-G-D-9.gif)~*i*~) = (*R*^`-`1^ ![](chap1-Z-G-D-26.gif)) ·
![](chap2-Z-G-D-9.gif)~*i*~.[^5^](#footnote_Temp_183) Thus the
components with respect to the rotated basis elements are the same as
the components of the rotated vector *R*^`-`1^ ![](chap1-Z-G-D-26.gif)
with respect to the original basis. In terms of components, if the
vector ![](chap1-Z-G-D-26.gif) has components ***x*** with respect to
the original basis vectors ![](chap2-Z-G-D-9.gif)~*i*~, then the
components ***x***' of the same vector with respect to the rotated basis
vectors ![](chap2-Z-G-D-9.gif)~*i*~' are ***x***' = ***R***^`-`1^
***x***, or equivalently ***x*** = ***R*** ***x***'. A rotation that
actively rotates the basis vectors, leaving other vectors unchanged, is
called a *passive* rotation. For a passive rotation the components of a
fixed vector change as if the vector was actively rotated by the inverse
rotation.

With respect to the rectangular basis ![](chap2-Z-G-D-9.gif)~*i*~ the
rotational kinetic energy is written

<div align="left">

![](chap2-Z-G-20.gif)

</div>

In terms of matrix representations, the kinetic energy is

<div align="left">

![](chap2-Z-G-21.gif)

</div>

where ![](chap1-Z-G-D-23.gif) is the column of components representing
![](chap2-Z-G-D-8.gif).[^6^](#footnote_Temp_184) If we rotate the
coordinate system by the passive rotation *R* about the center of
rotation, the new basis vectors are ![](chap2-Z-G-D-9.gif)~*i*~' = *R*
![](chap2-Z-G-D-9.gif)~*i*~. The components ![](chap1-Z-G-D-23.gif)' of
the vector ![](chap2-Z-G-D-8.gif) with respect to the rotated coordinate
system satisfy

<div align="left">

![](chap2-Z-G-22.gif)

</div>

where ***R*** is the matrix representation of *R*. The kinetic energy is

<div align="left">

![](chap2-Z-G-23.gif)

</div>

However, if we had started with the basis ![](chap2-Z-G-D-9.gif)~*i*~',
we would have written the kinetic energy directly as

<div align="left">

![](chap2-Z-G-24.gif)

</div>

where the components are taken with respect to the
![](chap2-Z-G-D-9.gif)~*i*~' basis. Comparing the two expressions, we
see that

<div align="left">

![](chap2-Z-G-25.gif)

</div>

Thus the inertia matrix transforms by a similarity
transformation.[^7^](#footnote_Temp_185)

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^4^](#call_footnote_Temp_182) An orthogonal matrix ***R*** satisfies
***R***^`T`^ = ***R***^`-`1^ and det ***R*** = 1.

[^5^](#call_footnote_Temp_183) The last equality follows from the fact
that the rotation of two vectors preserves the dot product:
![](chap1-Z-G-D-26.gif) · ![](chap2-Z-G-D-12.gif) =
(*R*![](chap1-Z-G-D-26.gif)) · (*R*![](chap2-Z-G-D-12.gif)), or
(*R*^`-`1^ ![](chap1-Z-G-D-26.gif)) · ![](chap2-Z-G-D-12.gif) =
![](chap1-Z-G-D-26.gif) · (*R* ![](chap2-Z-G-D-12.gif)).

[^6^](#call_footnote_Temp_184) We take a 1-by-1 matrix as a number.

[^7^](#call_footnote_Temp_185) That the inertia tensor transforms in
this manner could have been deduced from its
definition ([2.14](book-Z-H-23.html#EQUATION_2.14)). However, it seems
that the argument based on the coordinate-system independence of the
kinetic energy provides insight.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-23.html)</span><span>,
[next](book-Z-H-25.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


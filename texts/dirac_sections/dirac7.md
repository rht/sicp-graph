#7. Linear operators

IN the preceding section we considered a number which is a linear function of a ket vector, and this led to the concept of a bra vector. We shall now consider a ket vector which is a linear function of a ket vector, and this will lead to the concept of a linear operator.

Suppose we have a ket $\ket{F}$ which is a function of a ket $\ket{A}$, i.e. to each ket $\ket{A}$ there corresponds one ket $\ket{F}$, and suppose further that the function is a linear one, which means that the $\ket{F}$ corresponding to $\ket{A}+\ket{A'}$ is the sum of the $\ket{F}$’s corresponding to $\ket{A}$ and to $\ket{A’}$, and the $\ket{F}$ corresponding to $c\ket{A}$ is c times the $\ket{F}$ corresponding to $\ket{A}$, c being any numerical factor. Under these conditions, we may look upon the passage from $\ket{A}$ to $\ket{F}$ as the application of a linear operator to $\ket{A}$. Introducing the symbol a: for the linear operator, we may write

$$\ket{F} = \alpha\ket{A},$$
in which the result of on operating on $\ket{A}$ is written like a product of a with $\ket{A}$. We make the rule that in such products the ket vector
must always be put on the right of the linear operator. The above conditions of linearity may now be expressed by the equations
\begin{align}
\alpha\\{\ket{A}+\ket{A'}\\} &= \alpha\ket{A} + \alpha\ket{A'},\\
\alpha\\{c\ket{A}\\} = c\alpha\ket{A}.
\end{align}

A linear operator is considered to be completely defined when the result of its application to every ket vector is given. Thus a linear operator is to be considered zero if the result of its application to every ket vanishes, and two linear operators are to be considered equal if they produce the same result when applied to every ket.

Linear operators can he added together, the sum of two linear operators being defined to be that linear operator which, operating on any ket, produces the sum of what the two linear operators separately would produce. Thus $\alpha+\beta$ is defined by
\begin{equation}
    \\{\alpha + \beta \\} \ket{A} = \alpha\ket{A} + \beta\ket{A}
\end{equation}
for any $\ket{A}$. Equation (2) and the first of equations (1) show that products of linear operators with ket vectors satisfy the distributive axiom of multiplication.

Linear operators can also be multiplied together, the product of two linear operators being defined as that linear operator, the application of which to any ket produces the same result as the application of the two linear operators successively.. Thus the product $\alpha\beta$ is defined as the linear operator which, operating on any ket $\ket{A}$, changes it into that ket which one would get by operating first on $\ket{A}$ with B, and then on the result of the first operation with $\alpha$. In symbols
$$\\{\alpha\beta\\}\ket{A} = \alpha\\{\beta\ket{A}\\}$$

This definition appears as the associative axiom of multiplication for the triple product of $\alpha$, $\beta$, and $\ket{A}$, and allows us to write this triple product as $\alpha\beta\ket{A}$ without brackets. However, this triple product is in general not the same as what we should get if we operated on $\ket{A}$ first with $\alpha$ and then with $\beta$, i.e. in general $\alpha\beta\ket{A}$ differs from $\beta\alpha\ket{A}$, so that in general $\alpha\beta$ must differ from $\beta\alpha$. The commutative axiom of multiplication does not hold for linear operators. It may happen as a special case that two linear operators if $\xi$ and $\eta$ are such that $\xi\eta$ and $\eta\xi$ are equal. In this case we say that $\xi$ commutes with $\eta$, or that $\xi$ and $\eta$ commute.

By repeated applications of the above processes of adding and multiplying linear operators, one can form sums and products of more than two of them, and one can proceed to build up an algebra with them. In this algebra the commutative axiom of multiplication does not hold, and also the product of two linear operators may vanish without either factor vanishing. But all the other axioms of ordinary algebra, including the associative and distributive axioms of multiplication, are valid, as may easily be verified.

If we take a number k and multiply it into ket vectors, it appears as a linear operator operating on ket vectors, the conditions (1) being fulﬁlled with k substituted for $\alpha$. A number is, thus a special case of a linear operator. It has the property that it commutes with all linear operators and this property distinguishes it from a general linear operator.

So far we have considered linear operators operating only on ket
vectors. We can give a meaning to their operating also on bra vectors,
in the following way. Take the scalar product of any bra $\bra{B}$ with
the ket $\alpha\ket{A}$. This scalar product is a number which depends
linearly on $\ket{A}$ and therefore, from the definition of bras, it may be
considered as the scalar product of $\ket{A}$ with some bra. The bra thus defined depends linearly on $\bra{B}$, so we may look upon it as the result of some linear operator applied to $\bra{B}$. This linear operator is uniquely
determined by the original linear operator a and may reasonably be called the same linear operator operating on a bra. In this way our linear operators are made capable of operating on bra vectors.

A suitable notation to use for the resulting bra when a operates on the bra $\bra{B}$ is $\bra{B}\alpha$, as in this notation the equation which defines $\bra{B}\alpha$ is
\begin{equation}
\\{\bra{B}\alpha\\}\ket{A} = \bra{B}\\{\alpha\ket{A}\\}
\end{equation}

for any $\ket{A}$, which simply expresses the associative axiom of multi-
plication for the triple product of $\bra{B}$, \alpha, and $\ket{A}$. We therefore make the general rule that in a product of a bra and a linear operator, the bra must always be put on the left. We can now write the triple product of $\bra{B}$, $\alpha$, and $\ket{A}$ simply as $\bra{B}\alpha\ket{A}$ without brackets. It may easily be verified that the distributive axiom of multiplication holds for products of bras and linear operators just as well as for products of linear operators and kets.

There is one further kind of product which has a meaning in our scheme, namely the product of a ket vector and a bra vector with the ket on the left, such as $\ket{A}\bra{B}$. To examine this product, let us multiply it into an arbitrary ket $\ket{P}$, putting the ket on the right, and assume the associative axiom of multiplication. The product is then $\ket{A}\braket{B}{P}$, which is another ket, namely $\ket{A}$ multiplied by the
number $\braket{B}{P}$, and this ket depends linearly on the ket $\ket{P}$. Thus $\ket{A}\bra{B}$ appears as a linear operator that can operate on kets. It can also operate on bras, its product with a bra $\bra{Q}$ on the left being
$\braket{Q}{A}\bra{B}$, which is the number $\braket{Q}{A}$ times the bra $\bra{B}$. The product $\ket{A}\bra{B}$ is to be sharply distinguished from the product $\braket{B}{A}$ of the same factors in the reverse order, the latter product being, of course, a number.

We now have a complete algebraic scheme involving three kinds of quantities, bra vectors, ket vectors, and linear operators. They can be multiplied together in the various ways discussed above, and the associative and distributive axioms of multiplication always hold, but the commutative axiom of multiplication does not hold. In this general scheme we still have the rules of notation of the preceding section, that any complete bracket expression, containing $\langle$ on the left and $\rangle$ on the right, denotes a number, while any incomplete bracket expression, containing only $\langle$ or $\rangle$, denotes a vector.

With regard to the physical significance of the scheme, We have already assumed that the bra vectors and ket vectors, or rather the directions of these vectors, correspond to the states of a dynamical system at a particular time. We now make the further assumption that the linear operators correspond to theklynamical variables at that time. By dynamical variables are meant quantities such as the coordinates and the components of velocity, momentum and angular momentum of particles, and functions of these quantities--in fact the variables in terms of which classical mechanics is built up. The new assumption requires that these quantities shall occur also in quantum mechanics, but with the striking difference that they are now subject to an algebra in which the commutative axionz of multiplication does not hold.

This different algebra for the dynamical variables is one of the most important ways in which quantum mechanics differs from classical mechanics. We shall see later on that, in spite of this fundamental difference, the dynamical variables of quantum mechanics still. have many properties in common with their classical counterparts and it will be possible to build up a theory of them closely analogous to the classical theory and forming a beautiful generalization of it.

It is convenient to use the same letter to denote a dynamical variable and the corresponding linear operator. In fact, We may consider a dynamical variable and the corresponding linear operator to be both the same thing, Without getting into confusion.

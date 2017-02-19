#6. Bra and ket vectors

Whenever we have a set of vectors in any mathematical theory, we can always set up a second set of vectors, which mathematicians call the dual vectors. The procedure will be described for the case when the original vectors are our ket vectors.

Suppose we have a number $\varphi$ which is a function of a ket vector $|A\rangle$, i.e. to each ket vector $|A\rangle$ there corresponds one number and suppose further that the function is a linear one, which means that the number corresponding to $\ket{A} + \ket{A'}$ is the sum of the numbers corresponding to $\ket{A}$ and to $\ket{A'}$, and the number corresponding to c$\ket{A}$ is c times the number corresponding to $\ket{A}$, c being any numerical factor. Then the number $\varphi$ corresponding to any $\ket{A}$ may be looked upon as the scalar product of that $\ket{A}$ with some new vector, there being one of these new vectors for each linear function of the ket vectors $\ket{A}$. The justification for this way of looking at $\varphi$ is that, as will be seen later (see equations (5) and (6)), the new vectors may be added together and may be multiplied by numbers to give other vectors of the same kind. The new vectors are, of course, defined only to the extent that their scalar products with the original ket vectors are given numbers, but this is sufficient for one to be able to build up a mathematical theory about them.

We shall call the new vectors bra vectors, or simply bras, and denote a general one of them by the symbol $\bra{A}$, the mirror image of the symbol for a ket vector. If we want to specify a particular one of them by a label, B say, we write it in the middle, thus $\bra{B}$. The scalar product of a bra vector $\bra{B}$ and a ket vector $\ket{A}$ will be written $\braket{B}{A}$, i.e. as a juxtaposition of the symbols for the bra and ket vectors, that for the bra vector being on the left, and the two vertical lines being contracted to one for brevity.

One may look upon the symbols $\langle$ and $\rangle$ as a distinctive kind of brackets. A scalar product $\braket{B}{A}$ now appears as a complete bracket expression and a bra vector $\bra{B}$ or a ket vector $\ket{A}$ as an incomplete bracket expression. We have the rules that any complete bracket expression denotes a number and any incomplete bracket expression denotes a vector, of the bra or ket kind according to whether it contains the first or second part of the brackets. The condition that the scalar product of $\bra{B}$ and $\ket{A}$ is a linear function of $\ket{A}$ may be expressed symbolically by

\begin{equation}\bra{B} \\{ \ket{A} + \ket{A}\\} = \braket{B}{A} + \braket{B}{A'},
\end{equation}

\begin{equation}
\bra{B} \\{ cA \rangle \\} = c\braket{B}{A},
\end{equation}

c being any number.

A bra vector is considered to be completely defined when its scalar product with every ket vector is given, so that if a bra vector has its scalar product with every ket vector vanishing, the bra vector itself must be considered as vanishing. In symbols, if

\begin{align}
\braket{P}{A} = 0, \mathrm{all} \ket{A},\\
\mathrm{then }	\bra{P} = 0.
\end{align}

The sum of two bra vectors $\bra{B}$ and $\bra{B'}$ is defined by the condition that its scalar product with any ket vector $\ket{A}$ is the sum of the scalar products of $\bra{B}$ and $\bra{B'}$ with $\ket{A}$,

\begin{equation}{ \bra{B} + \bra{B'} } \ket{A} = \braket{B}{A} + \braket{B'}{A},        \end{equation}

and the product of a bra vector $\bra{B}$ and a number c is defined by the condition that its scalar product with any ket vector $|A\rangle$ is c times the scalar product of $\bra{B}$ with $\ket{A}$,

\begin{equation}\\{c \bra{B} \\} \ket{A} = c \braket{B}{A}.        \end{equation}

Equations (2) and (5) show that products of bra and ket vectors satisfy the distributive axiom of multiplication, and equations (3) and (6) show that multiplication by numerical factors satisfies the usual algebraic axioms.

The bra vectors, as they have been here introduced, are quite a different kind of vector from the kets, and so far there is no connexion between them except for the existence of a scalar product of a bra and a ket. We now make the assumption that there is a one-one correspondence between the bras and the kets, such that the bra corresponding to $\ket{A} + \ket{A'}$ is the sum of the bras corresponding to $\ket{A}$ and to $\ket{A'}$, and the bra corresponding to $c\ket{A}$ is c times the bra corresponding to $\ket{A}$, c being the conjugate complex number to c. We shall use the same label to specify a ket and the corresponding bra. Thus the bra corresponding to $\ket{A}$ will be written $\bra{A}$.

The relationship between a ket vector and the corresponding bra makes it reasonable to call one of them the conjugate imaginary of the other. Our bra and ket vectors are complex quantities, since they can be multiplied by complex numbers and are then of the same nature as before, but they are complex quantities of a special kind which cannot be split up into real and pure imaginary parts. The usual method of getting the real part of a complex quantity, by taking half the sum of the quantity itself and its conjugate, cannot be applied since a bra and a ket vector are of different natures and cannot be added together. To call attention to this distinction, we shall use the words 'conjugate complex' to refer to numbers and other complex quantities which can be split up into real and pure imaginary parts, and the words 'conjugate imaginary' for bra and ket vectors, which cannot. With the former kind of quantity, we shall use the notation of putting a bar over one of them to get the conjugate complex one.

On account of the one-one correspondence between bra vectors and ket vectors, any state of our dynamical system at a particular time may be specified by the direction of a bra vector just as well as by the direction of a ket vector. In fact the whole theory will be symmetrical in its essentials between bras and kets.

Given any two ket vectors $\ket{A}$ and $\ket{B}$, we can construct from them a number $\braket{A}{B}$ by taking the scalar product of the first with the conjugate imaginary of the second. This number depends linearly on $\ket{A}$ and antilinearly on $\ket{B}$, the antilinear dependence meaning that the number formed from $\ket{B} + \ket{B'}$ is the sum of the numbers formed from $\ket{B}$ and from $\ket{B'}$, and the number formed from $c\ket{B}$ is c-bar times the number formed from $\ket{B}$. There is a second way in which we can construct a number which depends linearly on $\ket{A}$ and antilinearly on $\ket{B}$, namely by forming the scalar product of $\ket{B}$ with the conjugate imaginary of $\ket{A}$ and taking the conjugate complex of this scalar product. We assume that these two numbers are always equal, i.e.

\begin{equation}\braket{B}{A} = \overline{\braket{A}{B}}.        \end{equation}
Putting $\ket{B} = \ket{A}$ here, we find that the number < A | } $|A\rangle$ must be real. We make the further assumption

\begin{equation}\braket{A}{A} > 0,        \end{equation}
except when $\ket{A} = 0$.

In ordinary space, from any two vectors one can constrict a number — their scalar product — which is a real number and is symmetrical between them. In the space of bra vectors or the space of ket vectors, from any two vectors one can again construct a number — the scalar product of one with the conjugate imaginary of the other — but this number is complex and goes over into the conjugate complex number when the two vectors are interchanged. There is thus a kind of perpendicularity in these spaces, which is a generalization of the perpendicularity in ordinary space. We shall call a bra and a ket vector orthogonal if their scalar product is zero, and two bras or two kets will be called orthogonal if the scalar product of one with the conjugate imaginary of the other is zero. Further, we shall say that two states of our dynamical system are orthogonal if the vectors corresponding to these states are orthogonal.

The length of a bra vector $\bra{A}$ or of the conjugate imaginary ket vector $\ket{A}$ is defined as the square root of the positive number $\braket{A}{A}$. When we are given a state and wish to set up a bra or ket vector to correspond to it, only the direction of the vector is given and the vector itself is undetermined to the extent of an arbitrary numerical factor. It is often convenient to choose this numerical factor so that the vector is of length unity. This procedure is called normalization and the vector so chosen is said to be normalized. The vector is not completely determined even then, since one can still multiply it by any number of modulus unity, i.e. any number $e^{i\gamma}$ where $\gamma$ is real, without changing its length. We shall call such a number a phase factor.

The foregoing assumptions give the complete scheme of relations between the states of a dynamical system at a particular time. The relations appear in mathematical form, but they imply physical conditions, which will lead to results expressible in terms of observations when the theory is developed further. For instance, if two states are orthogonal, it means at present simply a certain equation in our formalism, but this equation implies a definite physical relationship between the states, which further developments of the theory will enable us to interpret in terms of observational results (see the bottom of p. 35).

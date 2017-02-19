#17. The representation of linear operators

In § 14 me saw how to represent ket and bra vectors by sets of
numbers. We now have to do the same for linear operators, in order
to have a complete scheme for representing all our abstract quantities
by sets of numbers. The same basic vectors that we had in§ 14 can
be used again for this purpose.

Let us suppose the basic vectors are simultaneous eigenvectors of
a complete set of commuting observables §1,§2,...,§,,. If or. is any
linear operator, we take a general basic bra (§;...§;,| and a general
basic ket Iffnﬁﬂ) and form the numbers

<€1---€ltl@¢l§i'---€{i>- (39)
These numbers are sufficient to determine a completely, since in the
first place they determine the ket altfiiuﬁﬂ) (as they provide the
representative of this ket), and the value of this ket for all the basic
kets l§1'...§.§;) determines a. The numbers (39) are called the repre-
sentative of the linear operator a or of the dynamical variable a. They
are more complicated than the representative of a ket or bra vector
in that they involve the parameters that label two basic vectors
instead of one.

Let us examine the form of these numbers in simple cases. Take
ﬁrst the case when there is only one f, forming a complete commuting
set by itself, and suppose that it has discrete eigenvalues §'. The
representative of a is then the discrete set of numbers <§'|a]§">. If
one had to write out these numbers explicitly, the natural way of
arranging them would be as a two-dimensional array, thus:

l<€1l¢==I€1> <§1|¢>¢IE2> <€1IQ¢IE3>
$210451) <§2|<1|§2> <E2IO¢I§3> - .
<§3l<>¢l§1> <€3I<>==IEZ> <§3l<>=l€3> . . (49)

6s REPRESENTATIONS §1'?

Where §1,§2,§3,.. are all the eigenvalues of £1. Such an array is called
a matrix and the numbers are called the elements of the matrix. We
make the convention that the elements must always be arranged s0
that those in the same row refer t0 the same basic bra vector and
those in the same column refer to the same basic ket vector.

An element (flail?) referring to two basic vectors With the same
label is called a diagonal element of the matrix, as all such elements
lie on a diagonal. If We put a: equal to unity, We have from (16) all
the diagonal elements equal to unity and all the other elements equal
to zero. The matrix is then called the ttnit matrix.

If a: is real, We have

<€'|@=l€”> = <€"|¢r|§'>- (41)

The effect of these conditions on the matrix (40) is to make the

diagonal elements ‘all real and each of the other elements equal the

conjugate complex of its mirror reﬂectionin the diagonal. The matrix
is then called a Hermitian matrix.

If We put a: equal to E, We get for a general element of the matrix

(FEW) = 5’<€’l€"> == 5755p (42)
Thus all the elements not on the diagonal are zero. The matrix is
then called a diagonal matrix. Its diagonal elements are just equal
to the eigenvalues of 5. More generally, if me put a: equal to f(§), a
function of 5, We get
<§'|f(§)|E”> = f(§') 335-» (43)
and the matrix is again a diagonal matrix.
Let us determine the representative of a product oaﬁ of two linear

operators a: and i5’ in terms of the representatives of the factors.
From equation (22) With 5"” substituted for i’ We obtain

<§'|<1B|€"> = (He; |€'”><E”’|J5|§”>
1g <grioﬁlgm><ézrrlﬁlén>, 

Which gives us the required result. Equation (44) shows that the
matrix formed by the elements (§'|aB|§") equals the product of the
matrices formed by the elements (E104?) and (FIBIF) respectively,
according to the usual mathematical rule for multiplying matrices.
This rule gives for the element in the rth row and sth column of the
product matrix the sum of the product of each element in the rth
row of the first factor matrix urith the corresponding element in the sth

§l7 THE REPRESENTATION OF LINEAR OI'EH.ATORS B9

column 0f the second factor matrix. The multiplication of matrices
is non-commutative, like the multiplication of linear operators.

We can summarize our results for the case when there is only one
5 and it has discrete eigenvalues as follows:

(i) A n y linear operator is represented by a matrix.
(ii) The unit operator is represented by the unit matrix.

(iii) A real linear operator is represented by a Hermitian matrix.

(iv) 1f and functions of E are represented by diagonal matrices.

(v) The matrix representing the product of two linear operators is the
product of the matrices representing the two factors.

Let us now consider the case when there is only one 5 and it has
continuous eigenvalues. The representative of o: is now (51048), a
function of two variables f’ and i" which can vary continuously. It
is convenient to call such a function a ‘matrix’, using this word in
a generalized sense, in order that we may be able to use the same
terminology for the discrete and continuous cases. One of these
generalized matrices cannot, of course, be written out as a two-
dimensional array like an ordinary matrix, since the number of its
rows and columns is an infinity equal to the number of points on a
line, and the number of its elements is an infinity equal to the
number of points in an area.

We arrange our definitions concerning these generalized matrices
so that the rules (i)-(v) which we had above for the discrete case
hold also for the continuous ‘case. The unit operator is represented
by 8(§'—-§") and the generalized matrix formed by these elements
we define to be the unit matrix. We still have equation (41) as the
condition for a to be real and we define the generalized matrix formed
by the elements (§’[a|f"> to be Hermitian when it satisfies this
condition. f is represented by

<e|§ic> = 4' 8<§'~s") <45)
$115176 b)’ <§'|f(€)|§”> = f(E’)3(§’~—€")= (45)
and the generalized matrices formed by these elements we define to be
diagonal matrices. From (11), we could equally well have ﬁ” and f(§")
as the coefﬁcients of 3(E’—§”) on the right-hand sides of (45)and (46)
respectively. Corresponding to equation (44) we now have, from (24)

when?» = f <s'|a|c'> dz" <§’”IBI€">, w)

with an integral instead of a sum, and we define the generalized

matrix formed by the elements on the right-hand side here to be the
—_i3~5_95,57 F

70 REPRESENTATIONS § 17

product of the matrices formed by <§'|a]§"> and (§'|,B[§”>. With
these deﬁnitions we secure complete parallelism between the discrete
and continuous cases and we have the rules (i)-(v) holding for both.

The question arises how a general diagonal matrix is to be deﬁned
in the continuous case, as so far we have only deﬁned the right-hand
sides of (45) and (46) to be examples of diagonal matrices. One
mightftae inclined to deﬁne as diagonal any matrix whose (§',§”)
elements all vanish except when 5' differs inﬁnitely little from i",
but this would not be satisfactory, because an important property
of diagonal matrices in the discrete case is that they always commute
with one another and we want this property to hold also in the
continuous case. In order that the matrix formed by the elements
(§’|w]2§"> in the continuous case may commute with that formed by
the elements on the right-hand side of (45)we must have, using the
multiplication rule (4:7),

J‘ <€r|w|grrr> d5!!! §rr!8(§rrr__§rr) z J‘ 5" 8(§'___€nr) dgm <§rlr|w]§:r>.
With the help of formula (4), this reduces to

<£’|wl€”>E” = §'<s'|w|§"> <48)
or (€’--§”)<§’|w|§"> = 0-
This gives, according to the rule by which (l3) follows from (12),
<§'|wl€”> = ¢'5(§'—§")

where c’ is a number that may depend on .5’. Thus <5’ [w I5”) is of the
form of the right-hand side of (46). For this reason we deﬁne only
matrices whose demerits are 0f the form 0f the right-hand side 0f (46) t0
be diagonal matrices. It is easily veriﬁed that these matrices all
commute with one another. One can form other matrices whose
(f, E”) elements all vanish when f’ differs appreciably from E" and
have a different form of singularity when 5’ equals if” [we shall later
introduce the derivative 81x) of the 6 function and 8’(§’--§") will
then be an example, see § 22 equation (19)], but these other matrices
are not diagonal according to the deﬁnition.

Let us now pass on to the case when there is only one f and it has
both discrete and continuous eigenvalues. Using 5’, £8 to denote

discrete eigenvalues and 5’, f” to denote continuous eigenvalues, we
now have the representative of on consisting of four kinds of quanti-

ties, (8104.58), <§"|@i|§’>, (§’|a|§">, (('la l5”). These quantities can all

§l7 THE REPRESENTATION OF LINEAR OPERATORS 71

be put together and considered to form a more general kind of matrix
having some discrete rows and columns and also a continuous range
of rows and columns. We deﬁne unit matrix, Hermitian matrix,
diagonal matrix, and the product of two matrices also for this more
general kind of matrix so as to make the rules (i)-(v) still hold. The
details are a straightforward generalization of what has gone before
and need not be given explicitly.

Let us now go back to the general case of several §’s,§1,§2,...,.§,,.
The representative of oz, expression (39), may still be looked upon as
forming a matrix, with rows corresponding to different values of
§1,...,E.1,, and columns corresponding to different values of §1',...,§{1.
Unless all the §’s have discrete eigenvalues, this matrix will be of the
generalized kind wvith continuous ranges of rows and columns. We
again arrange our definitions so that the rules (i)-(v) hold, with rule
(iv) generalized to:

(iv') Each 5m (m= 1,2,...,u) and any function of them is repre-
sented by a diagonal matrix.

A diagonal matrix is now defined as one whose general element

<§1...§;,\wlﬂ...§,’f,> is of the form
<€1-~-§§ilwl§i-~-§l1> = c’3&1§I--3§;§;3(€L+1~€Z+1)--5(€li"—E{l) (49)

in the case when $1,“, 5,, have discrete eigenvalues and 5,, 4,1,", 5,, have
continuous eigenvalues, c’ being any function of the 5%. This defini-
tion is the generalization of what we had with one 5 and makes
diagonal matrices always commute with one another. The other
definitions are straightforward and need not be given explicitly.

We now have a linear operator always represented by a matrix.
The sum of two linear operators is represented by the sum of the
matrices representing the operators and this, together with rule (v),
means that the matrices are subject t0 the same algebraic relations as
the linear operators. If any algebraic equation holds between certain
linear operators, the same equation must hold between the matrices
representing those operators.

The scheme of matrices can be extended to bring in the repre-
sentatives of ket and bra vectors. The matrices representing linear
operators areiall square matrices with the same number of rows and
columns, and with, in fact, a one-one correspondence between their
rows and columns. We may look upon the representative of a ket
{P} as a matrix with a single column by setting all the numbers

72 REPRESENTATIONS § 17

<§Q...§.:,|P) which form this representative one below the other. The
number of rows in this matrix tvill be the same as the number of
rows or columns in the square matrices representing linear operators.
Such a single-column matrix can be multiplied on the left by a square
matrix <§;j--~<f-;JCB|§;...§;> representing a linear operator, by a rule
similar tojahat for the multiplication of two square matrices. The
product is another single-column matrix with elements given by

,2, H <s;-.-s;.|@|§;ms;;> ds;..1_»ds;; <£i'---£ILIP>-
grin

From (35) this is just equal to (<§i...§;,]a|P), the.representative of
O¢|P>. Similarly we may look upon the representative of a bra <Q[
as a natrix with a Single row by setting all the numbers <Q|§i...§;>
side by side. Such a single-row matrix may be multiplied on the
right by a square matrix (§;...§;,_|oc |§{...§.ﬂ>, the product being another
single-row matrix, which is just the representative of <Q|0c. The
single-row matrix representing (QI may be multiplied on the right
by the single-column matrix representing |P), the product being a
matrix with just a single element, which is equal to (QIP). Finally,
the single-row matrix representing (Ql may be multiplied on the left
by the single-column matrix representing |P), the product being a
square matrix, which is just the representative of ]P><Q|. In.this
way all our abstract symbols, Linear operators, bra vectors, and ket
vectors, can be represented by matrices, which are subject to the
same algebraic relations as the abstract symbols themselves.

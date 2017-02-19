#33. The Gibbs ensemble

In our work up to the present we have been assuming all along that
our dynamical system at each instant of time is in a definite state,
that is to say, its motion is specified as completely and accurately as
is possible without conﬂictingwith the generalprinciples of the theory

This means that

   

§33 THE GIBBS ENSEMBLE 131

In the classical theory this would mean, of course, that all the coordi-
nates and momenta. have speciﬁed values. Now we may be interested
in a motion which is speciﬁed to a lesser extent than this maximum
possible. The present section will be devoted to the methods to be

used in such a .case.
The procedure in classical mechanics is to introduce what is called

a Gibbs ensemble, the idea of which is as follows. We consider all the
dynamical coordinates and momenta as Cartesian coordinates in a
certain space, the phase space, whose number of dimensions is twice
the number of degrees of freedom of the system. Any state of the
system can then be represented by a point in this space. This point
will move according to the classical equations of motion (14). Sup-
pose, now, that we are not given that the system is in a deﬁnite state
at any tintte, but only that it is in one or other of a number of possible
states according to a deﬁnite probability law. We should then be
able to represent it by a ﬂuid in the phase space, the mass of ﬂuid in
any volume of the phase space being the total probability of the
system being in any state whose representative point lies in that
volume. Each particle of the ﬂuid will be moving according to the
equations of motion (14). If we introduce the density p of the ﬂuid
at any point, equal to the probability per unit volume of phase space
of the system being in the neighbourhood of the corresponding state,
we shall have the equation of conservation

3P____ 5 d9,- 3 JP,-
e“ " Zlelpeltelp dill

= - 2163.035) "~@Z.(P3§)l

= ——[p, (65)
This may be considered as the equation of motion for the ﬂuid, since
it determines the density p for all time if p is given initially as a
function of the q's and p's. It is, apart from the minus sign, of the
same form as the ordinary equation of motion (15) for a dynamical

variable.
The requirement that the total probability of the system being in

any state shall be unity gives us a normalizing condition for p
ff P Jed? = l, (66)

the integration being over the whole of phase space and the single

132 THE EQUATIONS OF MOTION §33

differential dq or dp being written to denote the product of all the
dgfs or dgfs. If B denotes any function of the dynamical variables,
the average value of B will be

ff a» dqdp- (w)

It makes only a trivial alteration in the theory, but often facilitates
discussion, if we work with a density p differing from the above one
by a positive constant factor, k say, so that we have instead of (66)

jfpdqdimk-

With this density we can picture the ﬂuid as representing a. "number
k of similar dynamical systems, all following through their motions
independently in the same place, without any mutual disturbance or
interaction. The density at any point ‘would then be the probable or
average number of systems in the neighbourhood of any state per unit
volume of phase space, and expression (67) would give the average
total value of B for all the systems. Such a set of dynamical systems,
which is the ensemble introduced by Gibbs, is usually not realizable
in practice, except as a rough approximation, but it forms all the
same a useful theoretical abstraction.

We shall now see that there exists a corresponding density p
in quantum mechanics, having properties analogous to the above.
It was ﬁrst introduced by von Neumann. Its existence is rather
surprising in view of the fact that phase space has no meaning in
quantum mechanics, there being no possibility of assigning numerical
values simultaneously to the q's and p's.

We consider a dynamical system which is at a certain time in one
or other of a number of possible states according to some given
probability law. These states may be either a discrete set or a con-
tinuous range, or both together. We shall here take for definiteness
the case of a discrete set and suppose them labelled by a parameter m.
Let the normalized ket vectors corresponding to them be Im) and let
the probability of the system being in the mth state be Pm. We then
define the quantum density p by

P = 2 lm>13n<ml- (68)

m
Let p’ be any eigenvalue of p and 1p’) an eigenket belonging to this
eigenvalue. Then

g lm>Pm<mlP'> = P|P'> = P’IP’>

§33 THE GIBBS ENSEMBLE 133
S0 that Z <P’lm>Pm<mlP'> == p’<p'lp’.l>
In
01‘ Z Pml<mlp’>lg = P'<P'|P'>-
m

Now PW, being a probability, can never he negative. It follows that
p’ cannot be negative. Thus p has no negative eigenvalues, in analogy
With the fact that the classical density p is never negative.

Let us now obtain the equation of motion for our quantum p. In
Schrodinger-k picture the kets and bras in (68)Will vary With the time
in accordance With Schr6dinger’s equation (5) and the conjugate
imaginary of this equation, While the Pm’s Will remain constant, since
the system, so long as it is left undisturbed, cannot change over from
a state corresponding to one ket satisfying Schrodinger's equation to
a state corresponding to another. We thus have

d<m|
dt

. 65p n  dlm)
‘dig’;  ‘it 

7R»

= Z {H |m>Pm<ml -" lm>Pm<m l5}

z Hp-pff. (69)

This is the quantum analogue of the classical equation of motion
(65). Our quantum p, like the classical one, is determined for all time
if it is given initially.

From the assumption of § 12, the average value of any observable
[3 When the system is in the state m is (vnlmm). Hence if the system
is distributed over the various states m according to the probability
laW Pm, the average value of B Will be  Pmcmiﬁlm). If We introduce

a representation with a discrete set of basic ket vectors 1-5’) say, this
equals
ZPm<ml€’><€'h3|m> m Z <5’ I13 Im>Pm<'"1|§’>
‘m ' fm
=g<é1ﬁpi€> -—- £g<s'|p,8|s'>. <70)

the last step being easily Kferiﬁeal with the law of matrix multiplica~
tion, equation (44) of § 17. The expressions ('7 0) are the analogue of
the expression (67) of the classical theory. Whereas in tlie classical
theory We have to multiply B by p arid take the integral of the
product over all phase space, in the quzmntum theory we have to

multiply ,8 by p, With the factors in either order, and take the
3595,57 K

134 THE EQUATIONS OF MOTION §33

diagonal sum of the product in a representation. If the representa-
tion involves a continuous range of basic vectors E’), we get instead

°f (70) f <é’IBPI€’> as - f swpﬁsv dsx m)

so that we must carry through a process of ‘integrating along the
diagonal‘ instead of summing the diagonal elements. Weshall deﬁne
(7l)to be the diagonal sum of 5p in the continuous case. It can easily
be veriﬁed, from the properties of transformation functions (56) of
§ l8, that the diagonal sum is the same for all representations.

From the condition that the |m>’s are normalized we get, with
discrete "s

since the total probability of the system being in any state is unity.
This is the analogue of equation (66). The probability of the system
being in the state E’, or the probability of the observables g which
are diagonal in the representation having the values 5’, is, according
to the rule for interpreting representatives of kets (51) of § l8,

Z l<€|m>|2Pm = <€’IPI§'>, (73)

7??-

which gives us a meaning for each term in t-he sum on the left-hand
side of (72). For continuous §”s, the right-hand side of (73) gives the
probability of the Es having values in the neighbourhood of 5’ per
unit range of variation of the values 5’.

As in the classical theory, we may take a density equal to k times
the above p and consider it as representing a Gibbs ensemble of k
similar dynamical systems, between which there is no mutual dis-
turbance or interaction. We shall then have k on the right-hand side
of (72), and (70) or (71) will give the total average B for all the
members of the ensemble, while (73) will give the total probability
of a member of the ensemble having values for its Ks equal to 2f’
or in the neighbourhood of 5' per unit range of variation of the
values 5'.

An important application of the Gibbs ensemble is to a dynamical
system in thermodynamic equilibrium with its surroundings at a
given temperature T. Gibbs showed that such a system is repre-
sented in classical mechanics by the density

§33 THE GIBBS ENSEMBLE 135

H being the Hamiltonisn, which is now independent of the time, k
being Boltzmanrfs constant, and c being a number chosen to make
the normalizing condition (66)hold. This formula may be taken over
unchanged into the quantum theory. At high temperatures, (74)
becomes p = c, which gives, on being substituted into the right-hand
side of (73), c<f'[§'> = c in the case of discrete E”s. This shows that
at high temperatures all discrete states are equally probable.


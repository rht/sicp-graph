#44. The perturbation considered as causing transitions

We shall now consider the second of the two perturbation methods
mentioned in § 42. We suppose again that we have an unperturbed
system governed by a Hamiltonian E which does not involve the
time explicitly, and a perturbing energy V which can now be an
arbitrary function of the time. The Hamiltonian for the perturbed
system is again H := E-I-V. For the present method it does not
make any essential difference whether the energy-levels of the
unperturbed system, i.e. the eigenvalues of E, form a discrete or
continuous set. We shall, however, take the discrete case, for
definiteness. We shall again work with a Heisenberg representation
for the unperturbed system, but as there will now be no advantage in
taking E itself as one of the observables whose eigenvalues label the
representatives, we shall suppose we have a general set of afs to label
the representatives.

Let us suppose that at the initial time to the system is in a state for
which the a's certainly have the values a'. The ket corresponding to
this state is the basic ket lal). If there were no perturbation, i.e. if the
Hamiltonian were E, this state» "would be stationary. The perturba-
tion causes the state to change. At time t the ket corresponding to the
state in Schrodinger's picture will be The’), according to equation (l)
of $27 . The probability of the 08s then having the values a" is

Pﬁafoc") = |(a“ [T|oc'>|2. (11)

For a" 7i a', Pﬁifa") is the probability of a transition taking place
from state a’ to state a" during the time interval to —> t, while PMQ’

1 z.£. Physik, 35 (1925), 565.

§44= PERTURBATION CAUSING TRANSITIONS 173

is the probability of no transition taking place at all. The sum of
P(a’a”) for all a” is, of course, unity.

Let us now suppose that initially the system, instead of being
certainly in the state a’, is in one or other of various states a’ with
the probability Pa» for each. The Gibbs densitycorresponding to this
distribution is, according to (68) of § 33

p == g l@'>P..-<@'r- (12)

At time t, each ket hi’) will have changed to Tla’) and each bra <a’|
to (a517, so p will have changed to

p, = Z T|a*>P,.<a'|T. (13)
The probability of the a's then having the values a” will be, from
(73) of§ 33, ___
<anlptlmrr> Z g <anlTloér>pa’<arlTlan>
= §P,,P(a’@” (14)

with the help of (ll). This result expresses that the probability of
the system being in the state a” at time t is the sum of the probabilities
of the system being initially in any state a’ 7’: a”, and making a transi-
tion from state a’ to state a" and the probability of its being initially
in the state 0c” and making n0 transition. Thus the various transition
probabilities act independently of one another, according to the
ordinary laws of probability.

The whole problem of calculating transitions thus reduces to the
determination of the probability amplitudes <@¢”|T la’). These can be
Worked out from the differential equation for T, equation (6)of $27 ,or

iﬁdT/dt = HT z (E—{—V)T. (15)

The calculation can be simpliﬁed by working with
T* = e‘E<‘""<=?lﬁT. (16)

We have 11ft dT*/dt = e"3E('"‘@)""(~—E T +11% dT/dt)
Z emrwoyny/T I, Vaqw, (17)
where 7* = eiEu-eoyaVe-azmz-aoyn, (18)

i.e. V* is the result of applying a certain unitary transformation to V.
Equation (17) is of a more convenient form than (15), because (17)
makes the change in T * depend entirely on the perturbation V, and

174 PERTURBATION THEORY §44=

for V = O it would make T * equal its initial value, namely unity.
We have from (1 6)

<@"1T*|@v> = @*E"<*4~>'ﬂ<@~"|r1w@'>.

S0 that P0130?) = I<O1”IT*I¢¥’>IZ, (19)
showing that T * and T are equally good for determining transition
probabilities.

Our Work up to the present has been exact. We noW assume V is
a small quantity of the first order and express T* in the form

T* = l-l-Tf-l-Tj-i-m, (20)

“there T? is of the first order, T3‘ is of the second, and so on. Substi-
tuting (20)into (17) and equating terms of equal order, We get

ifaldTffdt = V*,
ifzldTj/dt = V*T;“, (21)

From the first of these equations We obtain
z
f = “ta-l f V*(¢’) dz, (22)
in "
from the second We obtain

t t’
T; z Hit-Z f V*(t’) at’ f 11m") at’; (2a)
in to

and so on. For many practical problems it is sufficiently accurate to
retain only the term T1“, which gives for the transition probability
P(oa'oz") With cx" # a’

2

P(o¢’o¢") = ﬁ/“Z

   

:
<05’; J V*(t’) dt’ {of}
z to
I <oc"]V*(i')|o¢'> dﬁ’
n,
We obtain in this xvay the transition probability to the second order

of accuracy. The result depends only on the matrix element

<cx"|V*(t’)|cx'> of V*(t’) referring to the tWo states concerned, with t’
going from to to t. Since V* is real, like V,

(a"lV*(t’)ﬂ = (a'lV*(t’)la'Q
and hence PMQ”) = P(a”@¢' (25)

to the second order of accuracy.

, <24)

z h"'2

   

§44= PERTURBATION CAUSING TRANSITIONS 175

Sometimes one is interested in a transition a’ ~+ a” such that the
matrix element <Q¢”IV* la’) vanishes, 0r is small compared with other
matrix elements of V*. It is then necessary to work to a higher
accuracy. If we retain only the terms Elf and Tg‘, we get, for m” 2;‘: a’,

Pﬂxlcx") = 5'2

t
f <@"1V*<r>|@r> db
in

r r z
—iﬁ"1  b I <u”]V*(t’)[a”’> dt’ J (a”’{V*(t")la9 alt” . (26)
oam¢a .0: to to

The terms a" = a’ and a" = a" are omitted from the sum since they
are small compared with other terms of the sum, on account of the
smallness of <a"|V* lot’). To interpret the result (26), we may suppose

that the term t

l <@”lV*(¢')I@¢’> at’ <27)
in
gives rise to a transition directly from state a’ to state a", while the
term r r
_-m.-1f <a*'|v*(t')|a~"> at’ <a"'|v*(z*’)[a’> dz" (28)
t0 o

gives rise to a transition from state a’ to state of”, followed by a
transition from state of” to state ca”. The state d” is called an inter-
mediate state in this interpretation. We must add the term (2 7 )to the
various terms (28) corresponding to different intermediate states
and then take the square of the modulus of the sum, which means
that there is interference between the different transition processes-
the direct one and those involving intermediate states —and one can-
not give a meaning to the probability for one of these processes by
itself. For each of these processes, however, there is a probability
amplitude. If one carries out the perturbation method to a higher
degree of accuracy, one obtains a result which can be interpreted
similarly, with the help of more complicated transition processes
involving a succession of intermediate states.

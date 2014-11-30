#12. The general physical interpretation

The assumptions that me made at the beginning of § 10 to get a physical interpretation of the mathematical theory are of a rather special kind, since they can be used only in connexion with eigenstates. We need some more general assumption which will enable us to extract physical information from the mathematics even when me are not dealing with eigenstates.

In classical mechanics an observable always, as we say, 'has a value' for any particular state of the system. What is there in quantum mechanics corresponding to this? If we take any observable $\xi$ and any two states $x$ and $y$, corresponding to the vectors $\bra{x}\xi\ket{y}$, then we can form the number $\bra{x}\xi\ket{y}$. This number is not very closely analogous to the value which an observable can 'have' in the classical theory, for three reasons, namely, (i) it refers to two states of the system, while the classical value always refers to one, (ii) it is in general not a real number, and (iii) it is not uniquely determined by the observable and the states, since the vectors $\bra{x}$ and $\ket{y}$ contain arbitrary numerical factors. Even if we impose on $\bra{x}$ and $\ket{y}$ the condition that they shall be normalized, there will still be an undetermined factor of modulus unity in $\bra{x}\xi\ket{y}$. These three reasons cease to apply, however, if we take the two states to be identical and $\ket{y}$to be the conjugate imaginary vector to $\bra{x}$. The number that we then get, namely $\bra{x}\xi\ket{x}$, is necessarily real, and also it is uniquely determined when $\bra{x}$ is normalized, since if we multiply $\bra{x}$ by the numerical factor $e^{ic}$, $c$ being some real number, we must multiply $\ket{x}$ by $e^{-ic}$ and $\bra{x}\xi\ket{x}$ will be unaltered.

One might thus be inclined to make the tentative assumption that the observable $\xi'$ has the value $\bra{x}\xi\ket{x}$ for the state $x$, in a sense analogous to the classical sense. This would not be satisfactory, though, for the following reason. Let us take a second observable $\eta$, which would have by the above assumption the value $\bra{x}\eta\ket{x}$ for this same state. We should then expect, from classical analogy, that for this state the sum of the two observables would have a value equal to the sum of the values of the two observables separately and the product of the two observables would have a value equal to the product of the values of the two observables separately. Actually, the tentative assumption would give for the sum of the two observables the value $\bra{x}\xi + \eta \ket{x}$, which is, in fact, equal to the sum of $\bra{x}\xi\ket{x}$ and $\bra{x}\eta\ket{x}$, but for the product it would give the value $\bra{x}\xi\eta\ket{x}$ or $\bra{x}\eta\xi\ket{x}$, neither of which is connected in any simple way with $\bra{x}\xi\ket{x}$ and $\bra{x}\eta\ket{x}$.

However, since things go wrong only with the product and not with the sum, it would be reasonable to call $\bra{x}\xi\ket{x}$ the *average* value of the observable $\xi$ for the state $x$. This is because the average of the sum of two quantities must equal the sum of their averages, but the average of their product need not equal the product of their averages. We therefore make the general assumption that *if the measurement of the observable $\xi$ for the system in the state corresponding to $\ket{x}$ is made a large number of times, the average of all the results obtained will be $\bra{x}\xi\ket{x}$, provided $\ket{x}$ is normalized*. If $\ket{x}$ is not normalized, as is necessarily the case if the state $x$ is an eigenstate of some observable belonging to an eigenvalue in a range, the assumption becomes that the average result of a measurement of $\xi$ is proportional to $\bra{x}\xi\ket{x}$. This general assumption provides a basis for a general physical interpretation of the theory.

The expression that an observable 'has a particular value' for a particular state is permissible in quantum mechanics in the special case when a measurement of the observable is certain to lead to the particular value, so that the state is an eigenstate of the observable.

It may easily be verified from the algebra that, with this restricted meaning for an observable 'having a value', if two observables have values for a particular state, then for this state the sum of the two observables (if this sum is an observable?) has a value equal to the sum of the values of the two observables separately and the product of the two bbservables (if this product is an observable) has a value equal to the product of the values of the two observables separately.

In the general case we cannot speak of an observable having a value for a particular state, but we can speak of its having an average value for the state.\*We can go further and speak of the probability of its having any speciﬁed value for the state, meaning the probability of this speciﬁed value being obtained when one makes a measurement of the observable. This probability can be obtained from the general assumption in the following way.

Let the observable be $\xi$ and let the state correspond to the normalized ket $\ket{x}$. Then the general assumption tells us, not only that the average value of $\xi$ is $\bra{x}\xi\ket{x}$, but also that the average value of any function of $\xi$, $f(\xi)$ say, is $\bra{x}f(\xi)\ket{x}$. Take $f(\xi)$ to be that function of $\xi$ which is equal to unity when $\xi = a$, $a$ being some real number, and zero otherwise. This function of $\xi$ has a meaning according to our general theory of functions of an observable, and it may be denoted by $\delta\_{\xi a}$ in conformity with the general notation of the symbol $\xi$ with two suﬁxes given on p. 62 (equation (17)). The average value of this function of $\xi$ is just the probability, $P_a$ say, of $\xi$ having the value $a$. Thus
\begin{equation}
P_a = \bra{x} \delta\_{\xi a} \ket{x}.
\end{equation}

If $a$ is not an eigenvalue of $\xi$, $\delta\_{\xi a}$ multiplied into any eigenket of $\xi$ is zero, and hence $\delta\_{\xi a} = 0$ and $P_a = 0$. This agrees with a conclusion of § 10, that any result of a measurement of an observable must be one of its eigenvalues.

If the possible results of a measurement of $\xi$ form a range of numbers, the probability of $\xi$ having exactly a particular value will be zero in most physical problems. The quantity of physical importance is then the probability of $\xi$ having a value within a small range, say from $a$ to $a+da$. This probability, which we may call $P(a) da$, is

$\dagger$ This is not obviously so, since the sum may not have sufficient eigenstates to form a complete set, in which case the sum, considered as a single quantity, would not be measurable.
$\ddagger$ Here the reality condition may fail, as well as the condition for the eigenstates to form a complete set.

equal to the average value of that function of $\xi$ which is equal to
unity for $\xi$ lying within the range $a$ to $a+da$ and zero otherwise.
This function of $\xi$ has a meaning according to our general theory of
functions of an observable. Denoting it by $\chi(\xi)$, we have
\begin{equation}
P(a)da = \bra{x}\chi(\xi)\ket{x}
\end{equation}

If the range $a$ to $a+da$ does not include any eigenvalues of $\xi$, we have as above $\chi(\xi) = 0$ and $P(a) = 0$. If $\ket{x}$ is not normalized, the right-hand sides of (45) and (46) will still be proportional to the probability of $\xi$ having the value $a$ and lying within the range $a$ to $a+da$ respectively.

The assumption of § 10, that a measurement of $\xi$ is certain to give
the result $\xi'$ if the system is in an eigenstate of $\xi$ belonging to the
eigenvalue $\xi'$, is consistent with the general assumption for physical
interpretation and can in fact be deduced from it. Working from the
general assumption we see that, if $\ket{\xi'}$ is an eigenket of $\xi$ belonging to the eigenvalue $\xi'$, then, in the case of discrete eigenvalues of $\xi$,
$$\delta\_{\xi a} \ket{\xi'} = 0 \,\, \mathrm{unless} \,\, a = \xi', $$
and in the case of a range of eigenvalues of $\xi$
$$\chi(\xi)\ket{\xi'} = 0 \,\, unless\,the\,range\,a\,to\,a+da\,includes\,\xi'.$$
In either case, for the state corresponding to $\ket{F}$, the probability of $\xi$ having any value other than $\xi'$ is zero.

An eigenstate of $\xi$ belonging to an eigenvalue $\xi'$ lying in a range is a state which cannot strictly be realized in practice, since it would need an inﬁnite amount of precision to get $\xi$ to equal exactly $\xi'$. The most that could be attained in practice would be to get $\xi$ to lie within a narrow range about the value $\xi'$. The systam would then be in a state approximating to an eigenstate of $\xi$. Thus an eigenstate belonging to an eigenvalue in a range is a mathematical idealization of what can be attained in practice. All the same such eigenstates play a very useful role in the theory and one could not very well do without them. Science contains many examples of theoretical concepts which are limits of things met with in practice and are useful for the precise formulation of laws of nature, although they are not realizable experimentally, and this is just one more of them. It may be that the infinite length of the ket vectors corresponding to these eigenstates is connected with their unrealizability, and that all realizable states correspond to ket vectors that can be normalized and that form a Hilbert space.

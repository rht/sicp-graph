<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-74.html)</span><span>,
[next](book-Z-H-76.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

[6.4  Nonlinear Resonance](book-Z-H-4.html#%_toc_%_sec_6.4)
-----------------------------------------------------------

We can develop an approximation for an isolated resonance region as
follows. We again consider Hamiltonians of the form

<div align="left">

![](chap6-Z-G-66.gif)

</div>

where *H*~0~(*t*, *q*, *p*) = ![](chap6-Z-G-D-1.gif)~0~(*p*) depends
only on the momenta and so is solvable. We assume that the Hamiltonian
has no explicit time dependence. We further assume that the coordinates
are all angles, and that *H*~1~ is a multiply periodic function of the
coordinates that can be written

<div align="left">

![](chap6-Z-G-67.gif)

</div>

Suppose we are interested in a region of phase space for which *n* ·
![](chap1-Z-G-D-23.gif)~0~(*p*) is near zero, where *n* is a tuple of
integers, one for each degree of freedom. If we develop the perturbation
theory as before with the generator *W* that eliminates all terms of
order ![](chap1-Z-G-D-12.gif), then the transformed Hamiltonian is
*H*~0~, which is analytically solvable, but there would be terms with
*n* · ![](chap1-Z-G-D-23.gif)~0~(*p*) in the denominator. The resulting
solution is not applicable near this resonance.

Just as the problem of secular terms was solved by grouping more terms
with the solvable part of the Hamiltonian, we can develop approximations
that are valid in the resonance region by eliminating fewer terms and
grouping more terms in the solvable part.

To develop a perturbative approximation in the resonance region for
which *n* · ![](chap1-Z-G-D-23.gif)~0~(*p*) is near zero, we take the
generator *W* to be

<div align="left">

![](chap6-Z-G-68.gif)

</div>

excluding terms in *W* that lead to small denominators in this region.
The transformed Hamiltonian is

<div align="left">

![](chap6-Z-G-69.gif)

</div>

where the additional terms are higher-order in ![](chap1-Z-G-D-12.gif).
By excluding the term *k* = *n* from the sum in the generating function,
that term is left after the transformation.

The transformed Hamiltonian depends only on a single combination of
angles, so a change of variables can be made so that the new transformed
Hamiltonian is cyclic in all but one coordinate, which is this
combination of angles. This transformed Hamiltonian is solvable
(reducible to quadratures).

For example, suppose there are two degrees of freedom
![](chap1-Z-G-D-19.gif) = (![](chap1-Z-G-D-19.gif)~1~,
![](chap1-Z-G-D-19.gif)~2~) and we are interested in a region of phase
space in which *n* · ![](chap1-Z-G-D-23.gif)~0~ is near zero, with *n* =
(*n*~1~, *n*~2~). The combination of angles *n* ·
![](chap1-Z-G-D-19.gif) is slowly varying in the resonance region. The
transformed Hamiltonian ([6.60](#EQUATION_6.60)) is of the form

<div align="left">

![](chap6-Z-G-70.gif)

</div>

We can transform variables to ![](chap3-Z-G-D-5.gif) = *n*~1~
![](chap1-Z-G-D-19.gif)~1~ + *n*~2~ ![](chap1-Z-G-D-19.gif)~2~, with
second coordinate, say, ![](chap1-Z-G-D-19.gif)' =
![](chap1-Z-G-D-19.gif)~2~.[^2^](#footnote_Temp_427) Using the
*F*~2~-type generating function

<div align="left">

![](chap6-Z-G-71.gif)

</div>

we find that the transformation is

<div align="left">

![](chap6-Z-G-72.gif)

</div>

In these variables the transformed resonance Hamiltonian *H*'~*n*~
becomes

<div align="left">

![](chap6-Z-G-73.gif)

</div>

This Hamiltonian is cyclic in ![](chap1-Z-G-D-19.gif)', so
![](chap5-Z-G-D-15.gif)' is constant. With this constant momentum, the
Hamiltonian for the conjugate pair (![](chap3-Z-G-D-5.gif),
![](chap5-Z-G-D-5.gif)) has one degree of freedom. The solutions are
level curves of the Hamiltonian. These solutions, reexpressed in terms
of the original phase-space coordinates, give the evolution of
*H*'~*n*~. An approximate solution in the resonance region is therefore

<div align="left">

![](chap6-Z-G-74.gif)

</div>

If the resonance regions are sufficiently separated, then a global
solution can be constructed by splicing together such solutions for each
resonance region.

### [6.4.1  Pendulum Approximation](book-Z-H-4.html#%_toc_%_sec_6.4.1)

The resonance Hamiltonian ([6.64](#EQUATION_6.64)) has a single degree
of freedom and is therefore solvable (reducible to quadratures). We can
develop an approximate analytic solution in the vicinity of the
resonance by making use of the fact that the solution is valid there.
The resonance Hamiltonian can be approximated by a generalized pendulum
Hamiltonian.

Let

<div align="left">

![](chap6-Z-G-75.gif)

</div>

and

<div align="left">

![](chap6-Z-G-76.gif)

</div>

then the resonance Hamiltonian is

<div align="left">

![](chap6-Z-G-77.gif)

</div>

Define the resonance center ![](chap5-Z-G-D-5.gif)~*n*~ by the
requirement that the resonance frequency be zero there:

<div align="left">

![](chap6-Z-G-78.gif)

</div>

Now expand both parts of the resonance Hamiltonian about the resonance
center:

<div align="left">

![](chap6-Z-G-79.gif)

</div>

and

<div align="left">

![](chap6-Z-G-80.gif)

</div>

The first term in the expansion of *H*''~*n*,0~ is a constant and can be
ignored. The coefficient of the second term is zero, from the definition
of ![](chap5-Z-G-D-5.gif)~*n*~. The third term is the first significant
term. We presume here that the first term of *H*''~*n*,1~ is a nonzero
constant. Now the scale of the separatrix in ![](chap5-Z-G-D-5.gif) at
resonance is typically proportional to (![](chap1-Z-G-D-12.gif))^1/2^.
So the third term of *H*''~*n*,0~ and the first term of *H*''~*n*,1~ are
both proportional to ![](chap1-Z-G-D-12.gif). Subsequent terms are
higher-order in ![](chap1-Z-G-D-12.gif). Keeping only the
order-![](chap1-Z-G-D-12.gif) terms, the approximate resonance
Hamiltonian is of the form

<div align="left">

![](chap6-Z-G-81.gif)

</div>

which is the Hamiltonian for a pendulum with a shifted center in
momentum. This is analytically solvable.

#### [Driven pendulum resonances](book-Z-H-4.html#%_toc_%_sec_Temp_428)

Consider the behavior of the periodically driven pendulum in the
vicinity of the resonance ![](chap1-Z-G-D-23.gif)~*r*~(*p*) =
![](chap1-Z-G-D-23.gif).

The Hamiltonian ([6.54](#EQUATION_6.54)) for the driven pendulum has
three resonance terms in *H*~1~. The full
generator ([6.56](#EQUATION_6.56)) has three terms that are designed to
eliminate the corresponding resonance terms in the Hamiltonian. The
resulting approximate solution has small denominators close to each of
the three resonances, ![](chap1-Z-G-D-23.gif)~*r*~(*p*) = 0,
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = ![](chap1-Z-G-D-23.gif), and
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = `-` ![](chap1-Z-G-D-23.gif).

To develop a resonance approximation near
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = ![](chap1-Z-G-D-23.gif), we do not
include the corresponding term in the generator, so that the
corresponding term is left in the Hamiltonian. It is helpful to give
names to the various terms in the full
generator ([6.56](#EQUATION_6.56)):

<div align="left">

![](chap6-Z-G-82.gif)

</div>

The full generator is *W*^0^ + *W*^`-`^ + *W*^+^.

To investigate the motion in the phase space near the resonance
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = ![](chap1-Z-G-D-23.gif) (the "+"
resonance), we use the generator that excludes the corresponding term

<div align="left">

![](chap6-Z-G-83.gif)

</div>

With this generator the transformed Hamiltonian is

<div align="left">

![](chap6-Z-G-84.gif)

</div>

After we exclude the higher-order terms, this Hamiltonian has only a
single combination of coordinates, and so can be transformed into a
Hamiltonian that is cyclic in all but one degree of freedom. Define the
transformation through the mixed-variable generating function

<div align="left">

![](chap6-Z-G-85.gif)

</div>

giving the transformation

<div align="left">

![](chap6-Z-G-86.gif)

</div>

Expressed in these new coordinates, the resonance Hamiltonian is

<div align="left">

![](chap6-Z-G-87.gif)

</div>

This Hamiltonian is cyclic in *t*', so the solutions are level curves of
*H*~+~' in (![](chap3-Z-G-D-5.gif), ![](chap5-Z-G-D-5.gif)). Actually,
more can be said here because *H*~+~' is already of the form of a
pendulum shifted in the ![](chap5-Z-G-D-5.gif) direction by
![](chap1-Z-G-D-21.gif) ![](chap1-Z-G-D-23.gif) and shifted by
![](chap1-Z-G-D-15.gif) in phase. The shift by ![](chap1-Z-G-D-15.gif)
comes about because the sign of the cosine term is positive, rather than
negative as in the usual pendulum. A sketch of the level curves is given
in figure [6.8](#FIGURE_6.8).

<div align="left">

![](chap6-Z-G-88.gif)

</div>

**Exercise 6.2.**  **Resonance width**\
 Verify that the half-width of the resonance region is 2
(![](chap1-Z-G-D-21.gif) ![](chap1-Z-G-D-1.gif)
![](chap1-Z-G-D-12.gif))^1/2^.

**Exercise 6.3.**  **With the computer**\
 Verify, with the computer, that with the generator *W*~+~ the
transformed Hamiltonian is given by equation ([6.75](#EQUATION_6.75)).

An approximate solution of the driven pendulum near the
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = ![](chap1-Z-G-D-23.gif) resonance is

<div align="left">

![](chap6-Z-G-89.gif)

</div>

To find out to what extent the approximate solution models the actual
driven pendulum, we make a surface of section using this approximate
solution and compare it to a surface of section for the actual driven
pendulum. The surface of section for the approximate solution in the
resonance region is shown in figure [6.9](#FIGURE_6.9). A surface of
section for the actual driven pendulum is shown in the lower part of
figure [6.10](#FIGURE_6.10). The correspondence is surprisingly good.
Note how the resonance island is not symmetrical about a line of
constant momentum. The resonance Hamiltonian is symmetrical about
![](chap5-Z-G-D-5.gif) = ![](chap1-Z-G-D-21.gif)
![](chap1-Z-G-D-23.gif), and by itself would give a symmetric resonance
island (see figure [6.8](#FIGURE_6.8)). The necessary distortion is
introduced by the *W*^+^ transformation that eliminates the other
resonances. Indeed, in the full section the distortion appears to be
generated by the nearby ![](chap1-Z-G-D-23.gif)~*r*~(*p*) = 0 resonance
\`\`pushing away'' nearby features so that it has room to fit. However,
some features of the actual section are not represented; for instance,
there is a small chaotic zone near the actual separatrix.

<div align="left">

![](chap6-Z-G-90.gif)

</div>

<div align="left">

![](chap6-Z-G-91.gif)

</div>

The perturbation solution near the ![](chap1-Z-G-D-23.gif)~*r*~(*p*) = 0
resonance merges smoothly with the perturbation solutions for the
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = ![](chap1-Z-G-D-23.gif) and
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = `-` ![](chap1-Z-G-D-23.gif)
resonances. We can make a composite perturbative solution by using the
appropriate resonance solution for each region of phase space. A surface
of section for the composite perturbative solution is shown in the upper
part of figure [6.10](#FIGURE_6.10), as is the corresponding surface of
section for the actual driven pendulum. The perturbative solution
captures many features seen on the actual section. However, the
first-order perturbative solution does not capture the resonant islands
between the two primary resonances or the secondary island chains
contained within a primary resonance region. Also, the first-order
perturbative solution does not show the chaotic zone near the separatrix
apparent in the surface of section for the actual driven pendulum.

We see, from the comparisons of the sections of the first-order
perturbative solutions for the various resonance regions, that the
section for the actual driven pendulum can be approximately constructed
by combining the approximations developed for each resonance. The shapes
of the resonance regions are distorted by the transformations that
eliminate the nearby resonances, so the resulting pieces fit together
consistently. The predicted width of each resonance region agrees with
the actual width: it is not substantially changed by the distortion of
the region introduced by the elimination of the other resonance terms.
Not all the features of the actual section are reproduced in this
composite of first-order approximations: there are chaotic zones and
islands that do not appear in this collage of first-order
approximations.

For larger drives, the approximations derived by first-order
perturbations are worse. In the lower part of
figure [6.11](#FIGURE_6.11), with drive larger by a factor of five we
lose the invariant curves that separate the resonance regions. The main
resonance islands persist, but the chaotic zones near the separatrices
have merged into one large chaotic sea.

<div align="left">

![](chap6-Z-G-92.gif)

</div>

The composite first-order perturbative solution for the more strongly
driven pendulum in the upper part of figure [6.11](#FIGURE_6.11) still
approximates the centers of the main resonance islands reasonably well,
but it fails as we move out and encounter the secondary islands that are
visible in the resonance region for ![](chap1-Z-G-D-23.gif)~*r*~(*p*) =
![](chap1-Z-G-D-23.gif). Here the approximations for the two regions do
not fit together so well. The chaotic sea is found in the region where
the perturbative solutions do not match.

### [6.4.2  Reading the Hamiltonian](book-Z-H-4.html#%_toc_%_sec_6.4.2)

The locations and widths of the primary resonance islands can often be
read straight off the Hamiltonian when expressed as a Poisson series.
For each term in the series for the perturbation there is a
corresponding resonance island. The width of the island can often be
simply computed from the coefficients in the Hamiltonian. So just by
looking at the Hamiltonian we can get a good idea of what sort of
behavior we will see on the surface of section. For instance, in the
driven pendulum, the Hamiltonian ([6.53](#EQUATION_6.53)) has three
terms. We could anticipate, just from looking at the Hamiltonian, that
three main resonance islands are to be found on the surface of section.
We know that these islands will be located where the resonant
combination of angles is slow. So for the periodically driven pendulum
the resonances occur near ![](chap1-Z-G-D-23.gif)~*r*~(*p*) =
![](chap1-Z-G-D-23.gif), ![](chap1-Z-G-D-23.gif)~*r*~(*p*) = 0, and
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = `-` ![](chap1-Z-G-D-23.gif). The
approximate widths of the resonance islands can be computed with a
simple calculation.

### [6.4.3  Resonance-Overlap Criterion](book-Z-H-4.html#%_toc_%_sec_6.4.3)

As the size of the drive increases, the chaotic zones near the
separatrices get larger and then merge into a large chaotic sea. The
resonance-overlap criterion gives an analytic estimate of when this
occurs. The basic idea is to compare the sum of the widths of
neighboring resonances with their separation. If the sum of the
half-widths is greater than the separation, then the resonance-overlap
criterion predicts there will be large-scale chaotic behavior near the
overlapping resonances. In the case of the periodically driven pendulum,
the half-width of the ![](chap1-Z-G-D-23.gif)~*r*~(*p*) = 0 resonance is
2 (![](chap1-Z-G-D-21.gif) *ß*)^1/2^ and the half-width of the
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = ![](chap1-Z-G-D-23.gif) resonance is
2 (![](chap1-Z-G-D-21.gif) ![](chap1-Z-G-D-1.gif))^1/2^ (see
figure [6.12](#FIGURE_6.12)). The separation of the resonances is
![](chap1-Z-G-D-21.gif) ![](chap1-Z-G-D-23.gif). So resonance overlap
occurs if

<div align="left">

![](chap6-Z-G-93.gif)

</div>

The amplitude of the drive enters through ![](chap1-Z-G-D-1.gif).
Solving, we find the value of ![](chap1-Z-G-D-1.gif) above which
resonance overlap occurs. For the parameters ![](chap1-Z-G-D-21.gif) =
*ß* = 1, ![](chap1-Z-G-D-23.gif) = 5 used in
figures [6.9](#FIGURE_6.9)-[6.11](#FIGURE_6.11), the resonance overlap
value of ![](chap1-Z-G-D-1.gif) is 9/4. We see that, in fact, the
chaotic zones have already merged for ![](chap1-Z-G-D-1.gif) = 5/4. So
in this case the resonance-overlap criterion overestimates the strength
of the resonances required to get large-scale chaotic behavior. This is
typical of the resonance-overlap criterion.

A way of thinking about why the resonance-overlap criterion usually
overestimates the strength required to get large-scale chaos is that
other effects must be taken into account. For instance, as the drive is
increased second-order resonances appear between the primary resonances;
these resonances take up space and so resonance overlap occurs for
smaller drive than would be expected by considering the primary
resonances alone. Also, the chaotic zones at each separatrix have area
that must be accounted for.

<div align="left">

![](chap6-Z-G-94.gif)

</div>

### [6.4.4  Higher-Order Perturbation Theory](book-Z-H-4.html#%_toc_%_sec_6.4.4)

As the drive is increased, a variety of new islands emerge, which are
not evident in the original Hamiltonian. To find approximations for
motion in these regions we can use higher-order perturbation theory. The
basic plan is the same as before. At any stage the Hamiltonian (which is
perhaps a result of earlier stages of perturbation theory) is expressed
as a Poisson series (a multiple-angle Fourier series). The terms that
are not resonant in a region of interest are eliminated by a Lie
transformation. The remaining resonance terms involve only a single
combination of angle and are thus solvable by making a canonical
transformation to resonance coordinates. We complete the solution and
transform back to the original coordinates.

Let's find a perturbative approximation for the second-order islands
visible in figure [6.10](#FIGURE_6.10) between the
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = 0 resonance and the
![](chap1-Z-G-D-23.gif)~*r*~(*p*) = `-` ![](chap1-Z-G-D-23.gif)
resonance. The details are messy, so we will just give a few
intermediate results.

This resonance is not near the three primary resonances, so we can use
the full generator ([6.56](#EQUATION_6.56)) to eliminate those three
primary resonance terms from the Hamiltonian. After this perturbation
step the Hamiltonian is too hairy to look at.

We expand the transformed Hamiltonian in Poisson form and divide the
terms into those that are resonant and those that are not. The terms
that are not resonant can be eliminated by a Lie transform. This Lie
transform leaves the resonant terms in the Hamiltonian and introduces an
additional distortion to the curves on the surface of section. In this
case this latter distortion is small, but very messy to compute, so we
will just not include this effect. The resonance Hamiltonian is then
(after considerable algebra)

<div align="left">

![](chap6-Z-G-95.gif)

</div>

This is solvable because there is only a single combination of
coordinates.

We can get an analytic solution by making the pendulum approximation.
The Hamiltonian is already quadratic in the momentum *p*, so all we need
to do is evaluate the coefficient of the potential terms at the
resonance center *p*~2:1~ = ![](chap1-Z-G-D-21.gif)
![](chap1-Z-G-D-23.gif) / 2. The resonance Hamiltonian, in the pendulum
approximation, is

<div align="left">

![](chap6-Z-G-96.gif)

</div>

Carrying out the transformation to the resonance variable
![](chap3-Z-G-D-5.gif) = 2 ![](chap1-Z-G-D-19.gif) `-`
![](chap1-Z-G-D-23.gif) *t* reduces this to a pendulum Hamiltonian with
a single degree of freedom. Combining the analytic solution of this
pendulum Hamiltonian with the transformations generated by the full *W*,
we get an approximate perturbative solution

<div align="left">

![](chap6-Z-G-97.gif)

</div>

A surface of section in the appropriate resonance region using this
solution is shown in figure [6.13](#FIGURE_6.13). Comparing this to the
actual surface of section (figure [6.10](#FIGURE_6.10)), we see that the
approximate solution provides a good representation of this resonance
motion.

<div align="left">

![](chap6-Z-G-98.gif)

</div>

### [6.4.5  Stability of the Inverted Vertical Equilibrium](book-Z-H-4.html#%_toc_%_sec_6.4.5)

As a second application, we use second-order perturbation theory to
investigate the inverted vertical equilibrium of the periodically driven
pendulum.

Here, the procedure parallels that just followed, but we focus on a
different set of resonance terms. The terms that are slowly varying for
the vertical equilibrium are those that involve ![](chap1-Z-G-D-19.gif)
but do not involve *t*, such as cos (![](chap1-Z-G-D-19.gif)) and cos (2
![](chap1-Z-G-D-19.gif)). So we want to use the generator *W*^+^ +
*W*^`-`^ that eliminates the nonresonant terms involving combinations of
![](chap1-Z-G-D-19.gif) and ![](chap1-Z-G-D-23.gif) *t*, while leaving
the central resonance. After the Lie transform of the Hamiltonian with
this generator, we write the transformed Hamiltonian as a Poisson series
and collect the resonant terms. The transformed resonance Hamiltonian is

<div align="left">

![](chap6-Z-G-99.gif)

</div>

Figure [6.14](#FIGURE_6.14) shows contours of this resonance Hamiltonian
*H*'~*V*~ and a surface of section for the actual driven pendulum for
the same parameters. The behavior of the resonance Hamiltonian is
indistinguishable from that of the actual driven pendulum. The theory
does especially well here; there are no nearby resonances because the
drive frequency is high.

<div align="left">

![](chap6-Z-G-100.gif)

</div>

We can get an analytic estimate for the stability of the inverted
vertical equilibrium by carrying out a linear stability analysis of the
resonance Hamiltonian of the fixed point ![](chap1-Z-G-D-19.gif) =
![](chap1-Z-G-D-15.gif), *p* = 0. The algebra is somewhat simpler if we
first make the pendulum approximation about the resonance center. The
resonance Hamiltonian is then approximately

<div align="left">

![](chap6-Z-G-101.gif)

</div>

Linear stability analysis of the inverted vertical equilibrium indicates
stability for

<div align="left">

![](chap6-Z-G-102.gif)

</div>

In terms of the original physical parameters, the vertical equilibrium
is linearly stable if

<div align="left">

![](chap6-Z-G-103.gif)

</div>

where ![](chap1-Z-G-D-23.gif)~*s*~ = (*g*/*l*)^1/2^, the small-amplitude
oscillation frequency. For the vertical equilibrium to be stable, the
scaled product of the amplitude of the drive and the drive frequency
must be sufficiently large.

<div align="left">

![](chap6-Z-G-104.gif)

</div>

This analytic estimate is compared with the behavior of the driven
pendulum in figure [6.15](#FIGURE_6.15). For any given assignment of the
parameters, the driven pendulum can be tested for the linear stability
of the inverted vertical equilibrium by the methods of
chapter [4](book-Z-H-48.html#%_chap_4); this involves determining the
roots of the characteristic polynomial for a reference orbit at the
resonance center. In the figure the stability of the inverted vertical
equilibrium was assessed at each point of a grid of assignments of the
parameters. A dot is shown for combinations of parameters that are
linearly stable. The diagonal line is the analytic boundary of the
region of stability of the inverted equilibrium:
(![](chap1-Z-G-D-23.gif)/![](chap1-Z-G-D-23.gif)~*s*~)(*A*/*l*) =
(2)^1/2^. We see that the boundary of the region of stability is well
approximated by the analytic estimate derived from perturbation theory.
Note that for very high drive amplitudes there is another region of
instability, which is not captured by this perturbation analysis.

<div class="smallprint">

------------------------------------------------------------------------

</div>

<div class="footnote">

[^2^](#call_footnote_Temp_427) Any linearly independent combination will
be acceptable here.

</div>

<div class="navigation">

[Go to <span>[first](book.html),
[previous](book-Z-H-74.html)</span><span>,
[next](book-Z-H-76.html)</span> page<span>;
  </span><span>[contents](book-Z-H-4.html#%_toc_start)</span><span><span>;
  </span>[index](book-Z-H-82.html#%_index_start)</span>]

</div>

activate javascript


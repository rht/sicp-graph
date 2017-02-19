"""
# The Principle of Superposition
#1. The need for a quantum theory
"""

"""
CLASSICAL mechanics has been developed continuously from the time of Newton and applied to an ever-widening range of dynamical systems, including the electromagnetic field in interaction with matter. The underlying ideas and the laws governing their application form a simple and elegant scheme, which one would be inclined to think could not be seriously modified without having all its attractive features spoilt. Nevertheless it has been found possible to set up a new scheme, called quantum mechanics, which is more suitable for the description of phenomena on the atomic scale and which is in some respects more elegant and satisfying than the classical scheme. This possibility is due to the changes which the new scheme involves being of a very profound character and not clashing with the features of the classical theory that make it so attractive, as a result of which all these features can be incorporated in the new scheme.
"""
#Summary: (okay) Consistency between the classical scheme and the new scheme.
#'not clashing' can possibly have two meanings:
#1. that the new scheme agrees with the classical scheme via Bohr correspondence
#   principle in the classical limit.
#2. the expectation value of the new scheme agrees with the classical scheme
#   (Ehrenfest theorem).
#We have witnessed a huge progress in this 'not clashing' requirement of the
#first paragraph of Dirac thanks to Zurek's quantum Darwinism (on the origin of
#the classical trajectory).
"""
The necessity for a departure from classical mechanics is clearly shown by experimental results. In the first place the forces known in classical electrodynamics are inadequate for the explanation of the remarkable stability of atoms and molecules, which is necessary in order that materials may have any definite physical and chemical properties at all. The introduction of new hypothetical forces will not save the situation, since there exist general principles of classical mechanics, holding for all kinds of forces, leading to results in direct disagreement with observation. For example, if an atomic system has its equilibrium disturbed in any way and is then left alone, it will be set in oscillation and the oscillations will get impressed on the surrounding electromagnetic field, so that their frequencies may be observed with a spectroscope. Now whatever the laws of force governing the equilibrium, one would expect to be able to include the various frequencies in a scheme comprising certain fundamental frequencies and their harmonics. This is not observed to be the case. Instead, there is observed a new and unexpected connexion between the frequencies, called Ritz's Combination Law of Spectroscopy, according to which all the frequencies can be expressed as differences between certain terms, the number of terms being much less than the number of frequencies. This law is quite unintelligible from the classical standpoint.

One might try to get over the difficulty without departing from classical mechanics by assuming each of the spectroscopically observed frequencies to be a fundamental frequency with its own degree of freedom, the laws of force being such that the harmonic vibrations do not occur. Such a theory will not do, however, even apart from the fact that it would give no explanation of the Combination Law, since it would immediately bring one into conflict with the experimental evidence on specific heats. Classical statistical mechanics enables one to establish a general connexion between the total number of degrees of freedom of an assembly of vibrating systems and its specific heat. If one assumes all the spectroscopic frequencies of an atom to correspond to different degrees of freedom, one would get a specific heat for any kind of matter very much greater than the observed value. In fact the observed specific heats at ordinary temperatures are given fairly well by a theory that takes into account merely the motion of each atom as a whole and assigns no internal motion to it at all.

This leads us to a new clash between classical mechanics and the results of experiment. There must certainly be some internal motion in an atom to account for its spectrum, but the internal degrees of freedom, for some classically inexplicable reason, do not contribute to the specific heat. A similar clash is found in connexion with the energy of oscillation of the electromagnetic field in a vacuum. Classical mechanics requires the specific heat corresponding to this energy to be infinite, but it is observed to be quite finite. A general conclusion from experimental results is that oscillations of high frequency do not contribute their classical quota to the specific heat.
"""
Summary: (possibly outdated) Three experimental evidences of the need of quantum
mechanics.
#1. The stability of atoms. This is forbidden in classical electrodynamics by
#   Earnshaw theorem. The stability of atoms is explained through Heisenberg
#   uncertainty, while the stability of many body systems is explained by Fermion
#   repulsion. However, we know that the existence of stability is no longer
#   exclusive to quantum mechanics, as we have seen it in 'optical trapping'.
#   Yet stability is not a direct result of superposition principle (excluding the
#   fact that we implement indistinguishability by using superposition), and
#   hence is not a good first illustration of the principle.
#2. The Ritz combination principle suggests additional internal degrees of freedom.
#3. The specific heat of a vibrating system suggests that the
#   additional degrees of freedom is frozen. This experimental method is
#   particularly adept at detecting number of active degrees of freedom.
#   Why does a discrete degree of freedom leads to its freezing/activation at
#   specific temperature range? 'Because' a discrete dof implies the existence
#   of characteristic energy scale. A quantized degree of freedom is less tightly
#   coupled compared to its classical counterpart.
"""
As another illustration of the failure of classical mechanics we may consider the behaviour of light. We have, on the one hand, the phenomena of interference and diffraction, which can be explained only on the basis of a wave theory; on the other, phenomena such as photo-electric emission and scattering by free electrons, which show that light is composed of small particles. These particles, which are called photons, have each a definite energy and momentum, depending on the frequency of the light, and appear to have just as real an existence as electrons, or any other particles known in physics. A fraction of a photon is never observed.

Experiments have shown that this anomalous behaviour is not peculiar to light, but is quite general. All material particles have wave properties, which can be exhibited under suitable conditions. We have here a very striking and general example of the breakdown of classical mechanics — not merely an inaccuracy in its laws of motion, but an inadequacy of its concepts to supply us with a description of atomic events.
"""
#Summary: (Outdated) Three more experimental evidences.
#1. Photo-electric effect shows that electrons are quantum object, and only
#   indirectly that light can have quantum property, through the reasoning that
#   anything which interact directly with a quantum object must be quantum, too.
#2. 'scattering by free electrons'? Does this refer to compton scattering?
#   If yes, then there are several missing logical steps here that leads to
#   "ergo, light is a quantum object". We need to first state de-Broglie principle
#3. The statement 'A fraction of a photon is never observed' can have multiple
#   interpretation. One modern QED confirmation (this takes into account pair
#   production loop diagrams) is via Furry's theorem, which forbids odd photon
#   vertices but still allows scattering like 2 -> 4 photons.
#   Also, there might be counterexamples from nonlinear media.
"""
The necessity to depart from classical ideas when one wishes to account for the ultimate structure of matter may be seen, not only from experimentally established facts, but also from general philosophical grounds. In a classical explanation of the constitution of matter, one would assume it to be made up of a large number of small constituent parts and one would postulate laws for the behaviour of these parts, from which the laws of the matter in bulk could be deduced. This would not complete the explanation, however, since the question of the structure and stability of the constituent parts is left untouched. To go into this question, it becomes necessary to postulate that each constituent part is itself made up of smaller parts, in terms of which its behaviour is to be explained. There is clearly no end to this procedure, so that one can never arrive at the ultimate structure of matter on these lines. So long as big and small are merely relative concepts, it is no help to explain the big in terms of the small. It is therefore necessary to modify classical ideas in such a way as to give an absolute meaning to size.
"""
#Pending, lots of thoughts.
"""
At this stage it becomes important to remember that science is concerned only with observable things and that we can observe an object only by letting it interact with some outside influence. An act of observation is thus necessarily accompanied by some disturbance of the object observed. We may define an object to be big when the disturbance accompanying our observation of it may be neglected, and small when the disturbance cannot be neglected. This definition is in close agreement with the common meanings of big and small.

It is usually assumed that, by being careful, we may cut down the disturbance accompanying our observation to any desired extent. The concepts of big and small are then purely relative and refer to the gentleness of our means of observation as well as to the object being described. In order to give an absolute meaning to size, such as is required for any theory of the ultimate structure of matter, we have to assume that there is a limit to the fineness of our powers of observation and the smallness of the accompanying disturbance a limit which is inherent in the nature of things and can never be surpassed by improved technique or increased skill on the part of the observer. If the object under observation is such that the unavoidable limiting disturbance is negligible, then the object is big in the absolute sense and we may apply classical mechanics to it. If, on the other hand, the limiting disturbance is not negligible, then the object is small in the absolute sense and we require a new theory for dealing with it.
"""
#Summary: The observer effect.
#This is 'observer effect' and has nothing to do with Heisenberg uncertainty principle.
#However, it is interesting that Dirac connects the idea of 'observer effect' and
#absolute scale. The statement is however, too handwavy to be sharpened.
#I used to use this 'observer effect' as a signature to distinguish quantum
#phenomena from classical phenomena.
#
#Quantum zeno effect is another interesting consequence of the observer effect,
#since a measurement always reduce the entropy of a state into a pure state.
"""
A consequence of the preceding discussion is that we must revise our ideas of causality. Causality applies only to a system which is left undisturbed. If a system is small, we cannot observe it without producing a serious disturbance and hence we cannot expect to find any causal connexion between the results of our observations. Causality will still be assumed to apply to undisturbed systems and the equations which will be set up to describe an undisturbed system will be differential equations expressing a causal connexion between conditions at one time and conditions at a later time. These equations will be in close correspondence with the equations of classical mechanics, but they will be connected only indirectly with the results of observations. There is an unavoidable indeterminacy in the calculation of observational results, the theory enabling us to calculate in general only the probability of our obtaining a particular result when we make an observation.
"""
#(interesting) Dirac is connecting the idea of 'observer effect' and causality.
"""
#2. The polarization of photons
"""

"""
The discussion in the preceding section about the limit to the gentleness with which observations can be made and the consequent indeterminacy in the results of those observations does not provide any quantitative basis for the building up of quantum mechanics. For this purpose a new set of accurate laws of nature is required. One of the most fundamental and most drastic of these is the Principle of Superposition of States. We shall lead up to a general formulation of this principle through a consideration of some special cases, taking first the example provided by the polarization of light.
"""
#Summary: (1 -> 2)
#The photon polarization (the double-slit experiment in other books) is used to
#motivate the first Dirac axiom of quantum mechanics: the superposition principle.
#Its connection with the observer effect will be elaborated soon.
"""
It is known experimentally that when plane-polarized light is used for ejecting photo-electrons, there is a preferential direction for the electron emission. Thus the polarization properties of light are closely connected with its corpuscular properties and one must ascribe a polarization to the photons. One must consider, for instance, a beam of light plane-polarized in a certain direction as consisting of photons each of which is plane-polarized in that direction and a beam of circularly polarized light as consisting of photons each circularly polarized. Every photon is in a certain state of polarization, as we shall say. The problem we must now consider is how to fit in these ideas with the known facts about the resolution of light into polarized components and the recombination of these components.
"""
#Summary: (false outdated) Experimental suggestion of the particle nature of light.
#On the contrary, classical electrodynamics can still fully explain the
#preferred polarization direction of the light (radiated by the electron).
"""
Let us take a definite case. Suppose we have a beam of light passing through a crystal of tourmaline, which has the property of letting through only light plane-polarized perpendicular to its optic axis. Classical electrodynamics tells us what will happen for any given polarization of the incident beam. If this beam is polarized perpendicular to the optic axis, it will all go through the crystal; if parallel to the axis, none of it will go through; while if polarized at an angle $\alpha$ to the axis, a fraction $\sin 2\alpha$ will go through. How are we to understand these results on a photon basis?

A beam that is plane-polarized in a certain direction is to be pictured as made up of photons each plane-polarized in that direction. This picture leads to no difficulty in the cases when our incident beam is polarized perpendicular or parallel to the optic axis. We merely have to suppose that each photon polarized perpendicular to the axis passes unhindered and unchanged through the crystal, while each photon polarized parallel to the axis is stopped and absorbed. A difficulty arises, however, in the case of the obliquely polarized incident beam. Each of the incident photons is then obliquely polarized and it is not clear what will happen to such a photon when it reaches the tourmaline.

A question about what will happen to a particular photon under certain conditions is not really very precise. To make it precise one must imagine some experiment performed having a bearing on the question and inquire what will be the result of the experiment. Only questions about the results of experiments have a real significance and it is only such questions that theoretical physics has to consider.
"""
#Summary: Quantum description of the projection of light polarization.
#Indeed, classical optics with Maxwell equations already has superposition
#feature built-in. Furthermore, we can even observe a Hilbert space structure
#in classical electrodynamics (thus, enabling Bell-like nonlocal entanglement).
#
#This is about to become a misleading classical statistical mechanics picture of
#a photon passing through a polarizer. Fortunately, Dirac stood a few steps back
#from this, staying within the explicit 'positivism' approach of physics (i.e.
#the only meaningful scientific questions are the ones that can be measured).
"""
In our present example the obvious experiment is to use an incident beam consisting of only a single photon and to observe what appears on the back side of the crystal. According to quantum mechanics the result of this experiment will be that sometimes one will find a whole photon, of energy equal to the energy of the incident photon, on the back side and other times one will find nothing. When one finds a whole photon, it will be polarized perpendicular to the optic axis. One will never find only a part of a photon on the back side. If one repeats the experiment a large number of times, one will find the photon on the back side in a fraction $\sin 2\alpha$ of the total number of times. Thus we may say that the photon has a probability sin2α of passing through the tourmaline and appearing on the back side polarized perpendicular to the axis and a probability cos2α of being absorbed. These values for the probabilities lead to the correct classical results for an incident beam containing a large number of photons.

In this way we preserve the individuality of the photon in all cases. We are able to do this, however, only because we abandon the determinacy of the classical theory. The result of an experiment is not determined, as it would be according to classical ideas, by the conditions under the control of the experimenter. The most that can be predicted is a set of possible results, with a probability of occurrence for each.

The foregoing discussion about the result of an experiment with a single obliquely polarized photon incident on a crystal of tourmaline answers all that can legitimately be asked about what happens to an obliquely polarized photon when it reaches the tourmaline. Questions about what decides whether the photon is to go through or not and how it changes its direction of polarization when it does go through cannot be investigated by experiment and should be regarded as outside the domain of science. Nevertheless some further description is necessary in order to correlate the results of this experiment with the results of other experiments that might be performed with photons and to fit them all into a general scheme. Such further description should be regarded, not as an attempt to answer questions outside the domain of science, but as an aid to the formulation of rules for expressing concisely the results of large numbers of experiments.
"""
#Summary: A more refined and relevant description of a quantum of polarized light.
#A fair move, for if we don't how things work, better describe it statistically
#(a kind of coarse-graining is implied?).
"""
The further description provided by quantum mechanics runs as follows. It is supposed that a photon polarized obliquely to the optic axis may be regarded as being partly in the state of polarization parallel to the axis and partly in the state of polarization perpendicular to the axis. The state of oblique polarization may be considered as the result of some kind of superposition process applied to the two states of parallel and perpendicular polarization. This implies a certain special kind of relationship between the various states of polarization, a relationship similar to that between polarized beams in classical optics, but which is now to be applied, not to beams, but to the states of polarization of one particular photon. This relationship allows any state of polarization to be resolved into, or expressed as a superposition of, any two mutually perpendicular states of polarization.

When we make the photon meet a tourmaline crystal, we are subjecting it to an observation. We are observing whether it is polarized parallel or perpendicular to the optic axis. The effect of making this observation is to force the photon entirely into the state of parallel or entirely into the state of perpendicular polarization. It has to make a sudden jump from being partly in each of these two states to being entirely in one or other of them. Which of the two states it will jump into cannot be predicted, but is governed only by probability laws. If it jumps into the parallel state it gets absorbed and if it jumps into the perpendicular state it passes through the crystal and appears on the other side preserving this state of polarization.

#3. Interference of photons
"""
"""
In this section we shall deal with another example of superposition. We shall again take photons. but shall be concerned with their position in space and their momentum instead of their polarization. If we are given a beam of roughly monochromatic light, then we know something about the location and momentum of the associated photons. We know that each of them is located somewhere in the region of space through which the beam is passing and has a momentum in the direction of the beam of magnitude given in terms of the frequency of the beam by Einstein's photo-electric law — momentum equals frequency multiplied by a universal constant, When we have such information about the location and momentum of a photon we shall say that it is in a definite translational state.
"""
#Summary: The actual double-slit experiment.
#The difference with the previous polarization experiment is that now we require
#de-Broglie relation which connects momentum and wavenumber, since we now need
#to represent the quantum state into the space-time basis.
"""
We shall discuss the description which quantum mechanics provides of the interference of photons. Let us take a definite experiment demonstrating interference. Suppose we have a beam of light which is passed through some kind of interferometer, so that it gets split up into two components and the two components are subsequently made to interfere. We may, as in the preceding section, take an incident beam consisting of only a single photon and inquire what will happen to it as it goes through the apparatus. This will present to us the difficulty of the conflict between the wave and corpuscular theories of light in an acute form.

Corresponding to the description that we had in the case of the polarization, we must now describe photon as going partly into each of the two components into which the incident beam is split. The photon is then, as we may say, in a translational state given by the superposition of the two translational states associated with the two components. We are thus led to a generalization of the term 'translational state' applied to a photon. For a photon to be in a definite translational state it need not be associated with one single beam of light, but may be associated with two or more beams of light which are the components into which one original beam has been split. † In the accurate mathematical theory each translational state is associated with one of the wave functions of ordinary wave optics, which wave function may describe either a single beam or two or more beams into which one original beam has been split. Translational states are thus superposable in a similar way to wave functions.

† The circumstance that the superposition idea requires us to generalize our original meaning of translational states, but that no corresponding generalization was needed for the states of polarization of the preceding section, is an accidental one with no underlying theoretical significance.
Let us consider now what happens when we determine the energy in one of the components. The result of such a determination must be either the whole photon or nothing at all. Thus the photon must change suddenly from being partly in one beam and partly in the other to being entirely in one of the beams. This sudden change is due to the disturbance in the translational state of the photon which the observation necessarily makes. It is impossible to predict in which of the two beams the photon will be found. Only the probability of either result can be calculated from the previous distribution of the photon over the two beams.

One could carry out the energy measurement without destroying the component beam by, for example, reflecting the beam from a movable mirror and observing the recoil. Our description of the photon allows us to infer that, after such an energy measurement, it would not be possible to bring about any interference effects between the two components. So long as the photon is partly in one beam and partly in the other, interference can occur when the two beams are superposed, but this possibility disappears when the photon is forced entirely into one of the beams by an observation. The other beam then no longer enters into the description of the photon, so that it counts as being entirely in the one beam in the ordinary way for any experiment that may subsequently be performed on it.

On these lines quantum mechanics is able to effect a reconciliation of the wave and corpuscular properties of light. The essential point is the association of each of the translational states of a photon with one of the wave functions of ordinary wave optics. The nature of this association cannot be pictured on a basis of classical mechanics, but is something entirely new. It would be quite wrong to picture the photon and its associated wave as interacting in the way in which particles and waves can interact in classical mechanics. The association can be interpreted only statistically, the wave function giving us information about the probability of our finding the photon in any particular place when we make an observation of where it is.
"""
#Distinguishing between 1-norm probability and 2-norm probability.
#Todo: fine-grain the summary more.
"""
Some time before the discovery of quantum mechanics people realized that the connexion between light waves and photons must be of a statistical character. What they did not clearly realize, however, was that the wave function gives information about the probability of one photon being in a particular place and not the probable number of photons in that place. The importance of the distinction can be made clear in the following way. Suppose we have a beam of light consisting of a large number of photons split up into two components of equal intensity. On the assumption that the intensity of a beam is connected with the probable number of photons in it, we should have half the total number of photons going into each component. If the two components are now made to interfere, we should require a photon in one component to be able to interfere with one in the other. Sometimes these two photons would have to annihilate one another and other times they would have to produce four photons. This would contradict the conservation of energy. The new theory, which connects the wave function with probabilities for one photon, gets over the difficulty by making each photon go partly into each of the two components. Each photon then interferes only with itself. Interference between two different photons never occurs.
"""
#'Interference between two different photons never occurs' may be related to the
#previous statement 'A fraction of a photon is never observed'. Again, this is no
#longer true in QED.
"""
The association of particles with waves discussed above is not restricted to the case of light, but is, according to modern theory, of universal applicability. All kinds of particles are associated with waves in this way and conversely all wave motion is associated with particles. Thus all particles can be made to exhibit interference effects and all wave motion has its energy in the form of quanta. The reason why these general phenomena are not more obvious is on account of a law of proportionality between the mass or energy of the particles and the frequency of the waves, the coefficient being such that for waves of familiar frequencies the associated quanta are extremely small, while for particles even as light as electrons the associated wave frequency is so high that it is not easy to demonstrate interference.
"""
#Finally, an explicit statement of de-Broglie relation between wave and particle,
#but the question is, why do we need to use a special name for the representation
#of degrees of freedom associated with space and time?
"""
#4. Superposition and Indeterminacy
"""

"""
The reader may possibly feel dissatisfied with the attempt in the two preceding sections to fit in the existence of photons with the classical theory of light. He may argue that a very strange idea has been introduced — the possibility of a photon being partly in each of two states of polarization, or partly in each of two separate beams — but even with the help of this strange idea no satisfying picture of the fundamental single-photon processes has been given. He may say further that this strange idea did not provide any information about experimental results for the experiments discussed, beyond what could have been obtained from an elementary consideration of photons being guided in some vague way by waves. What, then, is the use of the strange idea?
"""
#Summary: connects 3 -> 4.
#Spot on.
#The two criticisms on the previous section are:
#1. "no satisfying picture of the fundamental single-photon processes has been
#    given".
#2. (the wording of the second criticism is still unclear)
"""
In answer to the first criticism it may be remarked that the main object of physical science is not the provision of pictures, but is the formulation of laws governing phenomena and the application of these laws to the discovery of new phenomena. If a picture exists, so much the better; but whether a picture exists or not is a matter of only secondary importance. In the case of atomic phenomena no picture can be expected to exist in the usual sense of the word 'picture', by which is meant a model functioning essentially on classical lines. One may, however, extend the meaning of the word 'picture' to include any way of looking at the fundamental laws which makes their self-consistency obvious. With this extension, one may gradually acquire a picture of atomic phenomena by becoming familiar with the laws of the quantum theory.
"""
#Summary: what a 'picture' ought to mean in physics.
#So far Dirac has only used tautology, that the photon is in a superposition state
#By 'laws of the quantum theory', he only refers to the unitary quantum dynamics,
#but doesn't include the measurement/collapse process.
"""
With regard to the second criticism, it may be remarked that for many simple experiments with light, an elementary theory of waves and photons connected in a vague statistical way would be adequate to account for the results. In the case of such experiments quantum mechanics has no further information to give. In the great majority of experiments, however, the conditions are too complex for an elementary theory of this kind to be applicable and some more elaborate scheme, such as is provided by quantum mechanics, is then needed. The method of description that quantum mechanics gives in the more complex cases is applicable also to the simple cases and although it is then not really necessary for accounting for the experimental results, its study in these simple cases is perhaps a suitable introduction to its study in the general case.
"""
#todo: connect this to the observer effect again.
"""
There remains an overall criticism that one may make to the whole scheme, namely, that in departing from the determinacy of the classical theory a great complication is introduced into the description of Nature, which is a highly undesirable feature. This complication is undeniable, but it is offset by a great simplification, provided by the general principle of superposition of states, which we shall now go on to consider. But first it is necessary to make precise the important concept of a 'state' of a general atomic system.

Let us take any atomic system, composed of particles or bodies with specified properties (mass, moment of inertia, etc.) interacting according to specified laws of force. There will be various possible motions of the particles or bodies consistent with the laws of force. Each such motion is called a state of the system. According to classical ideas one could specify a state by giving numerical values to all the coordinates and velocities of the various component parts of the system at some instant of time, the whole motion being then completely determined. Now the argument of pp. 3 and 4 shows that we cannot observe a small system with that amount of detail which classical theory supposes. The limitation in the power of observation puts a limitation on the number of data that can be assigned to a state. Thus a state of an atomic system must be specified by fewer or more indefinite data than a complete set of numerical values for all the coordinates and velocities at some instant of time. In the case when the system is just a single photon, a state would be completely specified by a given translational state in the sense of § 3 together with a given state of polarization in the sense of § 2.

A state of a system may be defined as an undisturbed motion that is restricted by as many conditions or data as are theoretically possible without mutual interference or contradiction. In practice the conditions could be imposed by a suitable preparation of the system, consisting perhaps in passing it through various kinds of sorting apparatus, such as slits and polarimeters, the system being left undisturbed after the preparation. The word 'state' may be used to mean either the state at one particular time (after the preparation), or the state throughout the whole of time after the preparation. To distinguish these two meanings, the latter will be called a 'state of motion' when there is liable to be ambiguity.
"""
#Summary: technical definition of the word 'state'
"""
The general principle of superposition of quantum mechanics applies to the states, with either of the above meanings, of any one dynamical system. It requires us to assume that between these states there exist peculiar relationships such that whenever the system is definitely in one state we can consider it as being partly in each of two or more other states. The original state must be regarded as the result of a kind of superposition of the two or more new states, in a way that cannot be conceived on classical ideas. Any state may be considered as the result of a superposition of two or more other states, and indeed in an infinite number of ways. Conversely any two or more states may be superposed to give a new state. The procedure of expressing a state as the result of superposition of a number of other states is a mathematical procedure that is always permissible, independent of any reference to physical conditions, like the procedure of resolving a wave into Fourier components. Whether it is useful in any particular case, though, depends on the special physical conditions of the problem under consideration.

In the two preceding sections examples were given of the superposition principle applied to a system consisting of a single photon. § 2 dealt with states differing only with regard to the polarization and § 3 with states differing only with regard to the motion of the photon as a whole.

The nature of the relationships which the superposition principle requires to exist between the states of any system is of a kind that cannot be explained in terms of familiar physical concepts. One cannot in the classical sense picture a system being partly in each of two states and see the equivalence of this to the system being completely in some other state. There is an entirely new idea involved, to which one must get accustomed and in terms of which one must proceed to build up an exact mathematical theory, without having any detailed classical picture.

When a state is formed by the superposition of two other states, it will have properties that are in some vague way intermediate between those of the two original states and that approach more or less closely to those of either of them according to the greater or less 'weight' attached to this state in the superposition process. The new state is completely defined by the two original states when their relative weights in the superposition process are known, together with a certain phase difference, the exact meaning of weights and phases being provided in the general case by the mathematical theory. In the case of the polarization of a photon their meaning is that provided by classical optics, so that, for example, When two perpendicularly plane polarized states are superposed with equal weights, the new state may be circularly polarized in either direction, or linearly polarized at an angle $\pi/4$, or else elliptically polarized, according to the phase difference.

The non-classical nature of the superposition process is brought out clearly if we consider the superposition of two states, A and B, such that there exists an observation which, when made on the system in state A, is certain to lead to one particular result, a say, and when made on the system in state B is certain to lead to some different result, b say. What will be the result of the observation when made on the system in the superposed state? The answer is that the result will be sometimes a and sometimes b, according to a probability law depending on the relative weights of A and B in the superposition process. It will never be different from both a and b. The intermediate character of the state formed by superposition thus expresses itself through the probability of a particular result for an observation being intermediate between the corresponding probabilities for the original states,† not through the result itself being intermediate between the corresponding results for the original states.

† The probability of a particular result for the state formed by superposition is not always intermediate between those for the original states in the general case when those for the original states are not zero or unity, so there are restrictions on the 'intermediateness' of a state formed by superposition.
In this way we see that such a drastic departure from ordinary ideas as the assumption of superposition relationships between the states is possible only on account of the recognition of the importance of the disturbance accompanying an observation and of the consequent indeterminacy in the result of the observation. When an observation is made on any atomic system that is in a given state, in general the result will not be determinate, i.e., if the experiment is repeated several times under identical conditions several different results may be obtained. It is a law of nature, though, that if the experiment is repeated a large number of times, each particular result will be obtained in a definite fraction of the total number of times, so that there is a definite probability of its being obtained. This probability is what the theory sets out to calculate. Only in special cases when the probability for some result is unity is the result of the experiment determinate.

The assumption of superposition relationships between the states leads to a mathematical theory in which the equations that define a state are linear in the unknowns. In consequence of this, people have tried to establish analogies with systems in classical mechanics, such as vibrating strings or membranes, which are governed by linear equations and for which, therefore, a superposition principle holds. Such analogies have led to the name 'Wave Mechanics' being sometimes given to quantum mechanics. It is important to remember, however, that the superposition that occurs in quantum mechanics is of an essentially different nature from any occurring in the classical theory, as is shown by the fact that the quantum superposition principle demands indeterminacy in the results of observations in order to be capable of a sensible physical interpretation. The analogies are thus liable to be misleading.
"""

"""
#5. Mathematical formulation of the principle
"""

"""
A profound change has taken place during the present century in the opinions physicists have held on the mathematical foundations of their subject. Previously they supposed that the principles of Newtonian mechanics would provide the basis for the description of the whole of physical phenomena and that all the theoretical physicist had to do was suitably to develop and apply these principles. With the recognition that there is no logical reason why Newtonian and other classical principles should be valid outside the domains in which they have been experimentally verified has come the realization that departures from these principles are indeed necessary. Such departures find their expression through the introduction of new mathematical formalisms, new schemes of axioms and rules of manipulation, into the methods of theoretical physics.
"""
#Summary: this section is essentially the mathematical formulation of the
#         non-classical superposition state introduced earlier.
"""
Quantum mechanics provides a good example of the new ideas. It requires the states of a dynamical system and the dynamical variables to be interconnected in quite strange ways that are unintelligible from the classical standpoint. The states and dynamical variables have to be represented by mathematical quantities of different natures from those ordinarily used in physics. The new scheme becomes a precise physical theory when all the axioms and rules of manipulation governing the mathematical quantities are specified and when in addition certain laws are laid down connecting physical facts with the mathematical formalism, so that from any given physical conditions equations between the mathematical quantities may be inferred and vice versa. In an application of the theory one would be given certain physical information, which one would proceed to express by equations between the mathematical quantities. One would then deduce new equations with the help of the axioms and rules of manipulation and would conclude by interpreting these new equations as physical conditions. The justification for the whole scheme depends, apart from internal consistency, on the agreement of the final results with experiment.
"""
#(interesting) "The Justification for the whole scheme depends, apart from
#internal consistency, on the agreement of the final results with experiment"
"""
We shall begin to set up the scheme by dealing with the mathematical relations between the states of a dynamical system at one instant of time, which relations will come from the mathematical formulation of the principle of superposition. The superposition process is a kind of additive process and implies that states can in some way be added to give new states. The states must therefore be connected with mathematical quantities of a kind which can be added together to give other quantities of the same kind. The most obvious of such quantities are vectors. Ordinary vectors, existing in a space of a finite number of dimensions, are not sufficiently general for most of the dynamical systems in quantum mechanics. We have to make a generalization to vectors in a space of an infinite number of dimensions, and the mathematical treatment becomes complicated by questions of convergence. For the present, however, we shall deal merely with some general properties of the vectors, properties which can be deduced on the basis of a simple scheme of axioms, and questions of convergence and related topics will not be gone into until the need arises.

It is desirable to have a special name for describing the vectors which are connected with the states of a system in quantum mechanics, whether they are in a space of a finite or an infinite number of dimensions. We shall call them ket vectors, or simply kets, and denote a general one of them by a special symbol $\ket{}$. If we want to specify a particular one of them by a label, A say, we insert it in the middle, thus $\ket{A}$. The suitability of this notation will become clear as the scheme is developed.

Ket vectors may be multiplied by complex numbers and may be added together to give other ket vectors, from two ket vectors $\ket{A}$ and $\ket{B}$ we can form
"""

"""
\begin{equation}c_1| A \rangle + c_2 | B \rangle = | R \rangle,\end{equation}
"""
#(interesting) The first equation of the book! Page 16.
"""
say, where $c_1$ and $c_2$ are any two complex numbers. We may also perform more general linear processes with them, such as adding an infinite sequence of them, and if we have a ket vector $\ket{x}$, depending on and labelled by a parameter x which can take on all values in a certain range, we may integrate it with respect to x, to get another ket vector
$$\int \ket{x} \operatorname{d}x = \ket{Q}$$
say. A ket vector which is expressible linearly in terms of certain others is said to be dependent on them. A set of ket vectors are called independent if no one of them is expressible linearly in terms of the others.

We now assume that each state of a dynamical system at a particular time corresponds to a ket vector, the correspondence being such that if a state results from the superposition of certain other states, its corresponding ket vector is expressible linearly in terms of the corresponding ket vectors of the other states, and conversely. Thus the state $\ket{R}$ results from a superposition of the states $\ket{A}$ and $\ket{B}$ when the corresponding ket vectors are connected by (1).

The above assumption leads to certain properties of the superposition process, properties which are in fact necessary for the word 'superposition' to be appropriate. When two or more states are superposed, the order in which they occur in the superposition process is unimportant, so the superposition process is symmetrical between the states that are superposed. Again, we see from equation (1) that (excluding the case when the coefficient $c_1$ or $c_2$ is zero) if the state $\ket{R}$ can be formed by superposition of the states $\ket{A}$ and $\ket{B}$, then the state $\ket{A}$ can be formed by superposition of $\ket{B}$ and $\ket{R}$, and $\ket{B}$ can be formed by superposition of $\ket{A}$ and $\ket{R}$. The superposition relationship is symmetrical between all three states $\ket{A}$, $\ket{B}$, and $\ket{R}$.

A state which results from the superposition of certain other states will be said to be dependent on those states. More generally, a state will be said to be dependent on any set of states, finite or infinite in number, if its corresponding ket vector is dependent on the corresponding ket vectors of the set of states. A set of states will be called independent if no one of them is dependent on the others.

To proceed with the mathematical formulation of the superposition principle we must introduce a further assumption, namely the assumption that by superposing a state with itself we cannot form any new state, but only the original state over again. If the original state corresponds to the ket vector $\ket{A}$, when it is superposed with itself the resulting state will correspond to

\begin{equation} \nonumber c_1\ket{A} + c_2\ket{A} = (c_1 + c_2) \ket{A},\end{equation}
where c1 and c2 are numbers. Now we may have $c_1 + c_2 = 0$, in which case the result of the superposition process would be nothing at all, the two components having cancelled each other by an interference effect. Our new assumption requires that, apart from this special case, the resulting state must be the same as the original one, so that $(c_1 + c_2) \ket{A}$ must correspond to the same state that $\ket{A}$ does. Now $c_1 + c_2$ is an arbitrary complex number and hence we can conclude that if the ket vector corresponding to a state is multiplied by any complex number, not zero, the resulting ket vector will correspond to the same state. Thus a state is specified by the direction of a ket vector and any length one may assign to the ket vector is irrelevant. All the states of the dynamical system are in one - one correspondence with all the possible directions for a ket vector, no distinction being made between the directions of the ket vectors $\ket{A}$ and $-\ket{A}$.
"""

"""
The assumption just made shows up very clearly the fundamental difference between the superposition of the quantum theory and any kind of classical superposition. In the case of a classical system for which a superposition principle holds, for instance a vibrating membrane, when one superposes a state with itself the result is a different state, with a different magnitude of the oscillations. There is no physical characteristic of a quantum state corresponding to the magnitude of the classical oscillations, as distinct from their quality, described by the ratios of the amplitudes at different points of the membrane. Again, while there exists a classical state with zero amplitude of oscillation everywhere, namely the state of rest, there does not exist any corresponding state for a quantum system, the zero ket vector corresponding to no state at all.
"""
#The statement is 'true', but for a different reason.
#We need superposition because we genuinely cannot distinguish between
#alternative paths.
"""
Given two states corresponding to the ket vectors $\ket{A}$ and $\ket{B}$, the general state formed by superposing them corresponds to a ket vector $\ket{R}$ which is determined by two complex numbers, namely the coefficients $c_1$ and $c_2$ of equation (1). If these two coefficients are multiplied by the same factor (itself a complex number), the ket vector $\ket{R}$ will get multiplied by this factor and the corresponding state will be unaltered. Thus only the ratio of the two coefficients is effective in determining the state R. Hence this state is determined by one complex number, or by two real parameters. Thus from two given states, a twofold infinity of states may be obtained by superposition.

This result is confirmed by the examples discussed in § 2 and § 3. In the example of § 2 there are just two independent states of polarization for a photon, which may be taken to be the states of plane polarization parallel and perpendicular to some fixed direction, and from the superposition of these two a twofold infinity of states of polarization can be obtained, namely all the states of elliptic polarization, the general one of which requires two parameters to describe it. Again, in the example of § 3, from the superposition of two given translational states for a photon a twofold infinity of translational states may be obtained, the general one of which is described by two parameters, which may be taken to be the ratio of the amplitudes of the two wave functions that are added together and their phase relationship. This confirmation shows the need for allowing complex coefficients in equation (1). If these coefficients were restricted to be real, then, since only their ratio is of importance for determining the direction of the resultant ket vector $\ket{R}$ when $\ket{A}$ and $\ket{B}$ are given, there would be only a simple infinity of states obtainable from the superposition.

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
"""
todo:fix equation 4
"""

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
"""

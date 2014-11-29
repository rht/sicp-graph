Dependencies:
pandoc

Create a d3 visualization of the interconnectedness between the sections in SICP.

#sicp http://rht.github.io/diracgraph/force.html?type=sicp
1. create tokens from each sections found in http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_start (after the content has been sanitized, of course).
2. remove common english words from the token
3. make corpora and dictionary of the book, with gensim
4. compute tfidf for each section
5. compute cosine similarity
The result is harder to interpret, but I can narrate for you the next one. If I remove links with weak weight, maybe the structure can be clearer.

#dirac http://rht.github.io/diracgraph/force.html
same as above, but since I do the partition based on chapters instead of section, it is easier to interpret.
Reference chapters:
1. The Principle of Superposition 
2. Dynamical Variables and Observables 
3. Representations 
4. The Quantum Conditions 
5. The Equations of Motion 
6. Elementary Applications 
7. Perturbation Theory 
8. Collision Problems 
9. Systems Containing Several Similar Particles 
10. Theory of Radiation 
11. Relativistic Theory of the Electron 
12. Quantum Electrodynamics 

* Introductory chapters (1,2,3) are disjoint from the rest because they mainly introduce elaborate basic terms which are then used as one or two words in the latter chapters.
* Chapter 6 has the most connections, followed by chapter 5. They form the center of mass of the book, mostly related to other chapters.
* Of course, I wouldn't expect the "bag of words" approach to be similar to my intended goal, to infer the EXACT logical structure of the ideas. Those two books are very suitable for this purpose because they are well written.

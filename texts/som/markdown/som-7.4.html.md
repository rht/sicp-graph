<div class="chapnav">

<span class="prev">Previous: [the puzzle
principle](./som-7.3.html)</span><span class="next">Next: [learning and
memory](./som-7.5.html)</span><span
class="contents">[Contents](index.html)</span>
<div class="titlebar">

Society of Mind
===============

</div>

</div>

*7.4* problem solving
---------------------

In principle, we can use the *generate and test* method — that is, trial
and error — to solve any problem whose solution we can recognize. But in
practice, it can take too long for even the most powerful computer to
test enough possible solutions. Merely assembling a simple house from a
dozen wooden blocks would require searching through more possibilities
than a child could try in a lifetime. Here is one way to improve upon
blind trial-and-error search.

The Progress Principle: Any process of exhaustive search can be greatly
reduced if we possess some way to detect when *progress* has been made.
Then we can trace a path toward a solution, just as a person can climb
an unfamiliar hill in the dark — by feeling around, at every step, to
find the direction of steepest ascent.

Many easy problems can be solved this way, but for a hard problem, it
may be almost as difficult to recognize *progress* as to solve the
problem itself. Without a larger overview, that *hill climber* may get
stuck forever on some minor peak and never find the mountaintop. There
is no foolproof way to avoid this.

Goals and Subgoal: The most powerful way we know for discovering how to
solve a hard problem is to find a method that splits it into several
simpler ones, each of which can be solved separately.

Much research in the field called Artificial Intelligence has been
concerned with finding methods machines can use for splitting a problem
into smaller subproblems and then, if necessary, dividing these into yet
smaller ones. In the next few sections we'll see how this can be done by
formulating our problems in terms of *goals.*

Using Knowledge: The most efficient way to solve a problem is to already
know how to solve it. Then one can avoid search entirely.

Accordingly, another branch of Artificial Intelligence research has
sought to find ways to embody knowledge in machines. But this problem
itself has several parts: we must discover how to acquire the knowledge
we need, we must learn how to represent it, and, finally, we must
develop processes that can exploit our knowledge effectively. To
accomplish all that, our memories must represent, in preference to vast
amounts of small details, only those relationships that may help us
reach our goals. This research has led to many practical
*knowledge-based* problem-solving systems. Some of these are often
called *expert systems* because they're based on imitating the methods
of particular human practitioners.

A curious phenomenon emerged from this research. It often turned out
easier to program machines to solve specialized problems that educated
people considered hard — such as playing chess or proving theorems about
logic or geometry — than to make machines do things that most people
considered easy — such as building toy houses with children's blocks.
This is why I've emphasized so many *easy* problems in this book.

<div class="footer">

[![Creative Commons
License](http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US)\
\
[![](./images/som_book.jpeg){#book}
![](./images/a_logo_17.gif)](http://www.amazon.com/gp/product/0671657135?ie=UTF8&camp=1789&creativeASIN=0671657135&linkCode=xm2&tag=marvinminsky)

</div>

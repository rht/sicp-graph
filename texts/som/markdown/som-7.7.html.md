<div class="chapnav">

<span class="prev">Previous: [reinforcement and
reward](./som-7.6.html)</span><span class="next">Next:
[difference-engines](./som-7.8.html)</span><span
class="contents">[Contents](index.html)</span>
<div class="titlebar">

Society of Mind
===============

</div>

</div>

*7.7* local responsibility
--------------------------

Suppose that Alice, who owns a wholesale store, asks the manager, Bill,
to increase sales. Bill instructs the salesman, Charles, to sell more
radios. Charles secures a large order, on profitable terms. But then the
firm can't actually deliver those radios, because they are in short
supply. Who is to blame? Alice would be justified in punishing Bill,
whose job it was to verify the inventory. The question is, should
Charles be rewarded? From Alice's viewpoint, Charles's actions have only
disgraced the firm. But from Bill's viewpoint, Charles succeeded in his
mission to get sales, and it wasn't his fault that this failed to
accomplish his supervisor's goal. Consider this example from two
perspectives — call them *local reward* and *global reward.*

The Local scheme rewards each agent that helps accomplish its
supervisor's goal. So Bill rewards Charles, even though Charles's action
served no higher-level goal.

The Global scheme rewards only agents that help accomplish top-level
goals. So Charles gets no reward at all.

It is easy to invent machinery to embody local learning policies, since
each assignment of credit depends only on the relation between an agent
and its supervisor. It is harder to implement a global learning scheme
because this requires machinery to find out which agents are connected
all the way to the original goal by unbroken chains of accomplished
subgoals. The local scheme is relatively generous to Charles by
rewarding him whenever he accomplishes what is asked of him. The global
scheme is much more parsimonious. It dispenses no credit whatever to
Charles, even though he does as his supervisor requests, unless his
action also contributes to the top-level enterprise. In such a scheme,
agents will often learn nothing at all from their experiences.
Accordingly, global policies lead to learning more slowly.

Both schemes have various advantages. The cautiousness of the global
policy is appropriate when mistakes are very dangerous or when the
system has plenty of time. This can lead to more *responsible* behavior
— since it could make Charles learn, in time, to check the inventory for
himself instead of slavishly obeying Bill. The global policy does not
permit one to justify a bad action with *I was only obeying the orders
of my superior.* On the other side, the local policy can lead to
learning many more different things at once, since each agent can
constantly improve its ability to achieve its local goals, regardless of
how they relate to those of other portions of the mind. Surely our
agencies have several such options. Which ones they use may depend, from
moment to moment, upon the states of other agencies whose job it is to
learn, themselves, which learning strategies to use, depending on the
circumstances.

The global scheme requires some way to distinguish not only which
agents' activities have helped to solve a problem, but also which agents
helped with which subproblems. For example, in the course of building a
tower, you might find it useful to push a certain block aside to make
room for another one. Then you'd want to remember that pushing can help
in building a tower — but if you were to conclude that pushing is a
generally useful thing to do, you'd never get another tower built. When
we solve a hard problem, it usually is not enough to say that what a
certain agent did was *good* or *bad* for the entire enterprise; one
must make such judgments depend, to some extent, on the local
circumstances — that is, on how the work of each agent helped or
hindered the work of related agents. The effect of rewarding an agent
must be to make that agent react in ways that help to accomplish some
specific goal — without too much interference with other, more important
goals. All this is simple common sense, but in order to pursue it
further, we'll have to clarify our language. We have all experienced the
pursuit of goals, but experience is not the same as understanding. What
is a goal, and how can a machine have one?

<div class="footer">

[![Creative Commons
License](http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US)\
\
[![](./images/som_book.jpeg){#book}
![](./images/a_logo_17.gif)](http://www.amazon.com/gp/product/0671657135?ie=UTF8&camp=1789&creativeASIN=0671657135&linkCode=xm2&tag=marvinminsky)

</div>

<div class="chapnav">

<span class="prev">Previous: [learning and
memory](./som-7.5.html)</span><span class="next">Next: [local
responsibility](./som-7.7.html)</span><span
class="contents">[Contents](index.html)</span>
<div class="titlebar">

Society of Mind
===============

</div>

</div>

*7.6* reinforcement and reward
------------------------------

One thing is sure: we always find it easier to do things we've done
before. What happens in our minds to make that possible? Here's one
idea: In the course of solving some problem, certain agents must have
aroused certain other agents. So let's take *reward* to mean that if
agent A has been involved in arousing agent B, the effect of reward is,
somehow, to make it easier for A to arouse B in the future and also,
perhaps, to make it harder for A to arouse other agents. At one time, I
was so taken with this idea that I designed a machine called the Snarc,
which learned according to this principle; it was composed of forty
agents, each connected to several others, more or less at random,
through a *reward* system that, when activated after each success, made
each agent more likely to rearouse the same recipients at later times.

We presented this machine with problems like learning to find a path
through a maze while avoiding a hostile predator. It quickly learned to
solve easy problems but never could learn to solve hard problems like
building towers or playing chess. It became clear that, in order to
solve complicated problems, any machine of limited size must be able to
reuse its agents in different ways in different contexts — as See must
do when involved in two concurrent tasks. But when the Snarc tried to
learn its way through a complicated maze, a typical agent might suggest
a good direction to move in at one moment, then suggest a bad direction
at another moment. Later, when we rewarded it for doing something we
liked, both those decisions became more likely — and all those *goods*
and *bads* tended to cancel one another out!

This poses a dilemma in designing machines that learn by *reinforcing*
the connections between agents. In the course of solving a hard problem,
one will usually try several bad moves before finding a good one — for
this is virtually what we mean by calling a problem *hard.* To avoid
learning those bad moves, we could design a machine to reinforce only
what happened in the last few moments before success. But such a machine
would be able to learn only to solve problems whose solutions require
just a few steps. Alternatively, we could design the reward to work over
longer spans of time; however, that would not only reward the bad
decisions along with the good but would also erase other things that it
had previously learned to do. We cannot learn to solve hard problems by
indiscriminately reinforcing agents or their connections. Why is it that
among all the animals, only the great-brained relatives of man can learn
to solve problems that require many steps or involve using the same
agencies for different purposes? We'll seek the answer in the policies
our agencies use for accomplishing goals.

You might argue that a beaver goes through many steps to build a dam, as
does a colony of termites when it builds its complex castle nest.
However, these wonderful animals do not learn such accomplishments as
individuals but use the procedures that have become encoded in their
species' genes over millions of years of evolution. You cannot train a
beaver to build a termite nest or teach termites to build beaver dams.

<div class="footer">

[![Creative Commons
License](http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US)\
\
[![](./images/som_book.jpeg){#book}
![](./images/a_logo_17.gif)](http://www.amazon.com/gp/product/0671657135?ie=UTF8&camp=1789&creativeASIN=0671657135&linkCode=xm2&tag=marvinminsky)

</div>

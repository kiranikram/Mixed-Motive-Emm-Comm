"""
DESCRIPTION OF EFG
set of players:
P U {c} , where c is a chance player that selects actions according to fixed known probability distributions, representing exogenous stochasticity.

game tree:
H: set of nodes of the tree
a node:
h ∈ H is identified by the ordered sequence of actions from the root to the node
Z ⊆ H is the set of terminal nodes
P(h) ∈ P ∪ {c}: unique player who acts at h
A(h): set of actions she has available
u_i : Z → R: Player i's payoff function
i ∈ P: player i’s infoset I groups nodes belonging to player i that are indistinguishable for her
I_i: set of all player i’s infosets
A(I): set of actions available at infoset I ∈ Ii
I ≼ J: infoset I ∈ I_i precedes J ∈ I_i
C⋆(I) : set of player i’s infosets that follow infoset I (this included)
C(I,a) ⊆ I_i: set of player i’s infosets that immediately follow I by playing action a
"""


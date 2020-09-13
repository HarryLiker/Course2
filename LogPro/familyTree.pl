parent(nikolay2,olga1).
parent(nikolay2,maria1).
parent(nikolay2,alexey).
parent(nikolay2,tatyana).
parent(nikolay2,anastasia).

parent(alf1,olga1).
parent(alf1,maria1).
parent(alf1,alexey).
parent(alf1,tatyana).
parent(alf1,anastasia).

parent(alex3,alex).
parent(alex3,xenia).
parent(alex3,nikolay2).

parent(marf1,alex).
parent(marf1,xenia).
parent(marf1,nikolay2).


ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).
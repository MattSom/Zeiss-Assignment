#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from app.models import Box, Stack


a = Box("A")
b = Box("B")
c = Box("C")
d = Box("D")
e = Box("E")
f = Box("F")
g = Box("G")
h = Box("H")
i = Box("I")
j = Box("J")
k = Box("K")
l = Box("L")
m = Box("M")
n = Box("N")
o = Box("O")
p = Box("P")
q = Box("Q")
r = Box("R")
s = Box("S")
t = Box("T")
u = Box("U")
v = Box("V")
w = Box("W")
x = Box("X")
y = Box("Y")
z = Box("Z")

boxes = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

stack1 = Stack(number=1)
stack1.add_box(a)
stack1.add_box(c)

stack2 = Stack(number=2)
stack2.add_box(b)
stack2.add_box(d)
stack2.add_box(k)
stack2.add_box(j)

stack3 = Stack(number=3)
stack3.add_box(e)
stack3.add_box(f)

stacks = [stack1, stack2, stack3]

print(stacks)

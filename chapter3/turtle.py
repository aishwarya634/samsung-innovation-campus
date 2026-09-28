import turtle as t

t.setup(width=500, height=500)
for j in range(50):

    for i in range(40):
        t.forward(i)
        t.left(i)
        t.right(30)
        t.color("blue")
    for i in range(40):
        t.forward(i)
        t.right(i)
        t.left(30)
for i in range(60):
    t.forward(i)
    t.right(i)
    t.left(20)
t.done()
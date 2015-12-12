import turtle 
import random

def tree(branch_len, t):
    if branch_len > 5:
        if branch_len < 8:
            t.color('red')
        if branch_len >= 8:
            t.color('green')
        t.forward(branch_len)
        t.right(20)
        len = random.randrange(5, 16)
        tree(branch_len - len, t)
        t.left(40)
        len = random.randrange(5, 16)
        tree(branch_len - len, t)
        t.right(20)        
        t.backward(branch_len)
        
def main():
    t = turtle.Turtle()
    t.speed(10)
    my_scr = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75, t)
    my_scr.exitonclick()
    
main()    
        
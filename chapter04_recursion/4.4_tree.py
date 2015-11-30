import turtle
import ipdb

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        # 与当前方向右边成 20°
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)
        
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    # 上浮，不会画出痕迹，重新落点
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()
    
main()    
    
    
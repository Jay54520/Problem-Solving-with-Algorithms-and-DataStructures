import turtle
import ipdb


def tree(branch_len, t):    
    # base case
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        
        # 上一个 tree() 到达 base case
        # 递归另一边，如果符合 base case 的话
        t.left(40)
        tree(branch_len - 15, t)
        # 不满足 base case
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
    
    
def move_tower(height, from_pole, with_pole, to_pole):
    if height >= 1:
        move_tower(height-1, from_pole, to_pole, with_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, from_pole, to_pole)
    # 不需要知道它实际怎么移动的，只要告诉它目标是什么
    
def move_disk(from_pole, to_pole):
    print("moving disk from", from_pole, "to", to_pole)
    
move_tower(3, "A", "B", "C")    
import random
import ipdb

# Generate n length string
def generate(n):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    string = ""    
    for i in range(n):
        # Get a random letter from 27 length letters
        string = string+letters[random.randrange(27)]
    return string

# Score by comparing 
def score(string, goal_string):
    score = 0
    for i in range(28):
        if string[i] == goal_string[i]:
            score+=1
    return score
    
# Repeatedly call generate and score
def call():
    goal_string = 'methinks it is like a weasel'
    new_string = generate(28)
    new_score = score(new_string, goal_string)
    best_score = 0
    best_string = ""
    loop_count = 0
    while new_score != 28:        
            if new_score > best_score:
                best_score = new_score
                best_string = new_string
            new_string = generate(28)
            new_score = score(new_string, goal_string)
            loop_count += 1
            
            if loop_count % 1000 == 0:
                print(best_string, best_score, loop_count)
    # When the loop_while break
    print("You have type the %s in the %d times" % (new_string, loop_count))
    return 
    
if __name__ == "__main__":
    call()
            
        
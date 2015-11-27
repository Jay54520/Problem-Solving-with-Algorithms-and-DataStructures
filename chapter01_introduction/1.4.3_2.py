word_list = ['cat','dog','rabbit']
# Use list comprehensions
print([ch for ch in "".join(wordlist)])

# Use list comprehensions and remove the duplicates
# I can not solve it in one line
letter_list = [word[i] for word in word_list for i in range(len(word)) if word[i]]

spam = 0.1
free_spam = 0.9
ham = 0.9
free_ham = 0.05

spams = spam * free_spam
hams = ham * free_ham
free = (spams) + (hams)
print(f'P(free) : {free}')

spam_free = (free_spam * spam) / free
print(f'email with the word "Free", probability it is actually Spam : {spam_free:.2f}')


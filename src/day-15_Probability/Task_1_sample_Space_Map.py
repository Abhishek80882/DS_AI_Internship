import random

actions = ['Click','Scroll','Exit']

sample_space = []
for i in actions:
    for j in actions:
        sample_space.append((i,j))

clicks = []
for x in sample_space:
    if 'Click' in x:
        clicks.append(x)

probability = len(clicks) / len(sample_space)
print(f'probability of the event "Clicks" where the customer clicks at least once : {probability:.2f}')


# rolling two dice 1,000 times and calculate the experimental probability of the sum being 7
count = 0
rolling_trails = 1000

for i in range(rolling_trails):
    sample1 = random.randint(1,6)
    sample2 = random.randint(1,6)
    if sample1 + sample2 == 7:
        count += 1
print(f'Probability of the sum being 7 : {count/rolling_trails}')

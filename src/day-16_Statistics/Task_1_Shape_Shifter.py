import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

height = pd.read_csv('heights.csv')
income = pd.read_csv('income.csv')
scores = pd.read_csv('test_scores.csv')

#Height Dataset
height_means = height['heights'].mean()
height_median = height['heights'].median()
print(f'Mean of Height : {height_means}, Median of Height : {height_median}')
sns.histplot(height['heights'],kde = True)
plt.xlabel('Height')
plt.ylabel('frequecy')
plt.show()
if height_means > height_median:
    print('the height dataset has Right Scewed\n')
elif height_means == height_median:
    print('Both mean and median are same\n')
else:
    print('the height dataset has Left Scewed\n')


#Income Dataset
income_means = income['incomes'].mean()
income_median = income['incomes'].median()
print(f'Mean of income : {income_means}, Median of income : {income_median}')
sns.histplot(income['incomes'],kde = True)
plt.xlabel('Income')
plt.ylabel('frequecy')
plt.show()
if income_means > income_median:
    print('the income dataset has Right Scewed\n')
elif income_means == income_median:
    print('Both mean and median are same\n')
else:
    print('the income dataset has Left Scewed\n')


#Scores Dataset
scores_means  = scores['scores'].mean()
scores_median = scores['scores'].median()
print(f'Mean of scores : {scores_means}, Median of scores : {scores_median}')
sns.histplot(scores['scores'],kde = True)
plt.xlabel('Scores')
plt.ylabel('frequecy')
plt.show()
if scores_means > scores_median:
    print('the Scores dataset has Right Scewed\n')
elif scores_means == scores_median:
    print('Both mean and median are same\n')
else:
    print('the Scores dataset has Left Scewed\n')


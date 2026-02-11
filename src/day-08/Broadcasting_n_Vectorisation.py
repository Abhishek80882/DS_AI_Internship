#TASK 01
import numpy as np
scores = np.array(np.random.randint(50,100, size=(5,3)))
#mean for each subject (Each Subject)
column_subject_mean = np.mean(scores,axis=0)
#Broadcasting
centered_score = scores - column_subject_mean
print(f'Original Scores : \n{scores}\n \nmean score : {column_subject_mean}\n \nCentered scores : \n{centered_score}')


#TASK 02
readings = np.arange(24)
array = readings.reshape(4,2,3)
transposed = array.transpose()
shapes = np.shape(array)
print(f'Shape : {shapes}\n\nTransposed Array : \n {transposed}')

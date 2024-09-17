import numpy as np 
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt

#a) Display all data
filepath = r"/Users/nadiarao/Library/Mobile Documents/com~apple~CloudDocs/Development/COD/AdvancePython/Week 2/Assignment 2/Student_Grades.csv"
data = np.genfromtxt(filepath, delimiter=',', skip_header= 1)

print ("Loaded dataset:")
print(data)

#b) Numer of students
num_students = len(data)
print("Number of Students:", num_students)

#c) Numbers of rows and coloumns
num_rows, num_coloums = data.shape
print("Number of rows:", num_rows)
print("Number of comuns:", num_coloums)

#d) Array data type
print("Data types:", data.dtype)

#min score
min_score = np.min(data[:, -1])

#max score
max_score = np.max(data[:, -1])

#mean value
mean = np.mean(data[:, -1])

#median value
median = np.median(data[:, -1])

#mode
mode = np.argmax(np.bincount(data[:,-1].astype(int)))

#standard deviatiion
std_deviation = np.std(data[:, -1])

#25% percentile
percentile_25 = np.percentile(data[:, -1], 25)

#75% percentile
percentile_75 = np.percentile(data[:, -1], 75)

print(" Descriptive Statistics:")
print(" Min score:", min_score)
print(" Max score:", max_score)
print("Mean score:", mean)
print("Median score:", median)
print("Mode score:", mode)
print("Standard score:", std_deviation)
print("25% Percentile:", percentile_25)
print("75% Percentile:", percentile_75)


grade_counts = [0, 20, 50, 60, 70, 100]
grade_labels = ['F', 'D', 'C', 'B', 'A']


# Calculate the number of students in each grade category
grade_counts = np.histogram(data[:, -1], bins=grade_counts)[0]

# Print the number of students in each grade category
for grade, count in zip(grade_labels, grade_counts):
    print(f"Number of students with {grade} grade:", count)

grade_dict = dict(zip(grade_labels, grade_counts))

#pie chart visualization
plt.pie(grade_dict.values(), labels=grade_dict.keys(), autopct='%1.1f%%', startangle=140)
plt.axis("equal")
plt.title("Grade Achievements")
plt.show()




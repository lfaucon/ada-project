print("--------------------------")
print("--- Scala MOOC project ---")
print("--------------------------")

print("-------------------")
print("--- Version 0.0 ---")
print("-------------------")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math

print("----------------------------")
print("--- Set up configuration ---")
print("----------------------------")

courseName = "progfun-002"

showPlots = True

print("-----------------------")
print("--- Import datasets ---")
print("-----------------------")

df_User_Grades = pd.read_csv('data/' + courseName + '_User_Grades.csv', index_col='SessionUserID')
df_User_Grades = df_User_Grades[['Grade','AchievementLevel']]
print(df_User_Grades.head())

df_Problem_Event = pd.read_csv('data/' + courseName + '_Problem_Events_with_Info.csv', index_col='SessionUserID')
df_Problem_Event = df_Problem_Event[['MaximumSubmissions','SubmissionNumber','Grade','TimeStamp','ProblemID','SoftCloseTime','ProblemType','HardCloseTime','OpenTime','Title','UniqueProblemID']]
print(df_Problem_Event.head(20))

print("---------------------")
print("--- Counts grades ---")
print("---------------------")

successCounts = df_User_Grades.AchievementLevel.value_counts()
print(successCounts.head())

print("--------------------------------")
print("--- RMSE for mean prediction ---")
print("--------------------------------")

df_User_Grades['NormalisedGrade'] = df_User_Grades.Grade / 100
df_User_Grades['Prediction'] = df_User_Grades.NormalisedGrade.mean()
df_User_Grades['SE'] = (df_User_Grades.NormalisedGrade - df_User_Grades.Prediction)**2
print("MEAN = " + str(df_User_Grades.NormalisedGrade.mean()))
print("RMSE = " + str(df_User_Grades.SE.mean()**0.5))

print("------------------------------")
print("--- Plotting course grades ---")
print("------------------------------")

plt.figure('Course grades')
plt.hist(df_User_Grades.Grade,bins=25)

print("------------------------------")
print("--- Explore Problem Events ---")
print("------------------------------")

print("SESSIONUSERID")
print(df_Problem_Event.index.value_counts().head())
print("PROBLEMTYPE")
print(df_Problem_Event.ProblemType.value_counts())

df_assignments = df_Problem_Event[df_Problem_Event.ProblemType == "Assignment"]
print("GRADE")
print(df_assignments.Grade.value_counts().head())
print("UNIQUEPROBLEMID")
print(df_assignments.UniqueProblemID.value_counts())

print("-----------------------------------")
print("--- Plotting assignments grades ---")
print("-----------------------------------")

grades = pd.to_numeric(df_assignments.Grade, errors='coerce').dropna()
print(grades.isnull().value_counts())

plt.figure('Assignment grades')
plt.hist(grades, bins=25)

print("-------------")
print("--- Plots ---")
print("-------------")

if showPlots: plt.show()
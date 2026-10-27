# Project Report: Student Academic Performance Analysis

## 1. Introduction
This project analyzes a small synthetic dataset of 30 students to practice basic educational data analysis with Python, Pandas, and Matplotlib.

## 2. Objectives
- Summarize subject marks and attendance.
- Calculate each student's total and average marks.
- Calculate Pass/Fail status and identify the topper.
- Explore relationships between attendance, study hours, and average marks.

## 3. Methodology
The CSV dataset was loaded with Pandas. Missing numeric values are filled using the median. Total marks, average marks, and result labels are calculated. Bar and scatter plots are generated using Matplotlib, and a correlation matrix is calculated.

## 4. Sample results
- Number of students: 30
- Average attendance: 76.5%
- Average study time: 2.3 hours/day
- Pass percentage (33 marks in every subject): 80.0%
- Topper in this sample: Student_25 (237 total marks out of 300)

### Correlation matrix
                     Attendance_Percent  Study_Hours_Per_Day  Average_Marks
Attendance_Percent                 1.00                -0.26           0.19
Study_Hours_Per_Day               -0.26                 1.00           0.73
Average_Marks                      0.19                 0.73           1.00

## 5. Visualizations
- `charts/subject_performance.png`: average marks by subject.
- `charts/attendance_vs_marks.png`: attendance compared with average marks.
- `charts/study_hours_vs_marks.png`: study time compared with average marks.

## 6. Conclusion and limitations
The project demonstrates how to summarize and visualize student data. Correlations can indicate that two variables move together, but **correlation does not prove causation**. The dataset is synthetic and small, so these results must not be treated as evidence about real students. Real-world use would require permission, privacy safeguards, and a larger reliable dataset.

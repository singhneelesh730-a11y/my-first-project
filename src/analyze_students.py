"""
Student Academic Performance Analysis
Beginner-friendly Python project using Pandas and Matplotlib.
Dataset is synthetic sample data, not real student records.
Run: python src/analyze_students.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "dataset" / "students.csv"
CHARTS_DIR = ROOT / "charts"
CHARTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)
subjects = ["Maths", "Science", "English"]
pass_mark = 33  # Example pass mark; change if your institution uses a different rule.

# 1. Basic inspection
print("FIRST FIVE STUDENTS")
print(df.head())
print("\nDATASET INFO")
print(df.info())
print("\nMISSING VALUES")
print(df.isnull().sum())

# 2. Handle missing values in numeric columns, if any
numeric_columns = ["Attendance_Percent", "Study_Hours_Per_Day"] + subjects
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# 3. Calculate total, average, pass/fail, and topper
df["Total_Marks"] = df[subjects].sum(axis=1)
df["Average_Marks"] = df[subjects].mean(axis=1).round(2)
df["Result"] = df[subjects].ge(pass_mark).all(axis=1).map({True: "Pass", False: "Fail"})

topper = df.loc[df["Total_Marks"].idxmax()]
print("\nSTUDENT RESULTS")
print(df[["Student", "Total_Marks", "Average_Marks", "Result"]].to_string(index=False))
print(f"\nTopper: {topper['Student']} with {topper['Total_Marks']} total marks")

# 4. Descriptive statistics and pass percentage
print("\nSUBJECT-WISE SUMMARY")
print(df[subjects].describe().round(2))
pass_percentage = (df["Result"].eq("Pass").mean() * 100)
print(f"\nPass percentage: {pass_percentage:.1f}%")
print(f"Average attendance: {df['Attendance_Percent'].mean():.1f}%")
print(f"Average study time: {df['Study_Hours_Per_Day'].mean():.1f} hours/day")

# 5. Subject average bar chart
subject_means = df[subjects].mean()
plt.figure(figsize=(7, 5))
subject_means.plot(kind="bar")
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks (out of 100)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(CHARTS_DIR / "subject_performance.png", dpi=150)
plt.close()

# 6. Attendance vs average marks scatter plot
plt.figure(figsize=(7, 5))
plt.scatter(df["Attendance_Percent"], df["Average_Marks"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "attendance_vs_marks.png", dpi=150)
plt.close()

# 7. Study time vs average marks scatter plot
plt.figure(figsize=(7, 5))
plt.scatter(df["Study_Hours_Per_Day"], df["Average_Marks"])
plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours per Day")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "study_hours_vs_marks.png", dpi=150)
plt.close()

# 8. Correlations (association does not prove causation)
correlation = df[["Attendance_Percent", "Study_Hours_Per_Day", "Average_Marks"]].corr()
print("\nCORRELATION MATRIX")
print(correlation.round(2))

# Save a results file for easy viewing in Excel
df.to_csv(ROOT / "student_results.csv", index=False)
print(f"\nDone! Charts saved in: {CHARTS_DIR}")
print(f"Detailed results saved in: {ROOT / 'student_results.csv'}")

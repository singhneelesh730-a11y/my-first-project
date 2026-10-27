# Student Academic Performance Analysis

## Project overview
This beginner-friendly Python data analysis project explores how students' marks relate to attendance and daily study time.

**Important:** `dataset/students.csv` contains synthetic sample data created for practice. It does not contain real student records.

## Objectives
- Calculate total and average marks for each student.
- Classify students as Pass or Fail.
- Find the topper.
- Summarize marks subject-wise and calculate pass percentage.
- Visualize subject performance, attendance vs marks, and study hours vs marks.
- Calculate correlations without claiming that correlation proves causation.

## Tools
- Python
- Pandas
- Matplotlib
- CSV

## Project structure
```text
Student_Academic_Performance_Analysis/
├── dataset/
│   └── students.csv
├── src/
│   └── analyze_students.py
├── charts/
│   ├── subject_performance.png
│   ├── attendance_vs_marks.png
│   └── study_hours_vs_marks.png
├── student_results.csv
├── report.md
└── README.md
```

## How to run in VS Code
1. Install Python if it is not installed.
2. Open this project folder in VS Code.
3. Open Terminal → New Terminal.
4. Install libraries:
   ```bash
   python -m pip install pandas matplotlib
   ```
5. Run:
   ```bash
   python src/analyze_students.py
   ```

If `python` does not work on Windows, try `py` instead.

## Dataset columns
- `Student`: anonymous sample ID
- `Attendance_Percent`: attendance percentage
- `Study_Hours_Per_Day`: estimated daily study hours
- `Maths`, `Science`, `English`: marks out of 100

## Pass rule
The script uses 33 marks as an example pass mark in every subject. Change `pass_mark = 33` in `src/analyze_students.py` if your college/school uses a different rule.

## Findings
Run the script to print the actual summaries and correlations from the included sample dataset. Since the data is synthetic, use the findings only to demonstrate your analysis workflow—not to make claims about real students.

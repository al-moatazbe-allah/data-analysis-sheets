#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

class StudentScoreSheet:
    def __init__(self):
        """Initialize the student score sheet with sample data."""
        self.students = [f"Student {i}" for i in range(1, 11)]
        self.subjects = ["Math", "Physics", "Chemistry", "Biology", "English", "History", "Geography", "Computer Science"]
        self.scores = np.random.randint(50, 101, size=(10, 8))
        self.df = pd.DataFrame(self.scores, index=self.students, columns=self.subjects)

    def add_student(self, name, scores):
        """Add a new student with scores."""
        if name in self.df.index:
            return f"Student {name} already exists."
        self.df.loc[name] = scores
        return f"Student {name} added successfully!"

    def delete_student(self, name):
        """Remove a student from the table."""
        if name in self.df.index:
            self.df.drop(name, inplace=True)
            return f"Student {name} deleted."
        return f"Student {name} not found."

    def update_excel(self, filename):
        """Save the DataFrame to an Excel file."""
        self.df.to_excel(filename, index=True)
        return f"Excel file '{filename}' updated successfully."

    def get_subject_scores(self, subject):
        """Retrieve scores for a specific subject."""
        return self.df[subject] if subject in self.df.columns else f"Subject {subject} not found."

    def set_subject_score(self, student, subject, score):
        """Update a specific student's score for a subject."""
        if student in self.df.index and subject in self.df.columns:
            self.df.at[student, subject] = score
            return f"Updated {student}'s {subject} score to {score}."
        return "Invalid student or subject."

# Create instance
score_sheet = StudentScoreSheet()

# Save initial Excel file
score_sheet.update_excel("Student_Scores.xlsx")

# Plot grade distribution
def plot_grade_distribution(df):
    plt.figure(figsize=(12, 6))
    df.plot(kind='hist', bins=10, alpha=0.7, figsize=(12, 6))
    plt.title("Grade Distribution for All Subjects")
    plt.xlabel("Scores")
    plt.ylabel("Frequency")
    plt.legend(df.columns, loc="upper right")
    plt.grid(True)
    plt.savefig("Grade_Distribution.png")
    plt.show()

plot_grade_distribution(score_sheet.df)

# Add two new students
new_students = pd.DataFrame({
    "Math": [85, 78], "Physics": [80, 75], "Chemistry": [88, 82], "Biology": [90, 85],
    "English": [76, 80], "History": [82, 79], "Geography": [91, 87], "Computer Science": [89, 84]
}, index=["Student 11", "Student 12"])

score_sheet.df = pd.concat([score_sheet.df, new_students])
score_sheet.update_excel("Merged_Student_Scores.xlsx")

# Save and reload data
score_sheet.df.to_csv("Student_Scores.csv", index=True)

# Load DataFrame from the CSV file
loaded_df = pd.read_csv("Student_Scores.csv", index_col=0)

print(loaded_df)

# Save statistics to a text file
stats = score_sheet.df.describe()
stats.to_csv("Student_Statistics.txt", sep='\t')
# Save and load feedback
feedback = "This course was very informative and practical. The use of Python for data science tasks is highly effective."
with open("Course_Feedback.txt", "w") as f:
    f.write(feedback)

with open("Course_Feedback.txt", "r") as f:
    loaded_feedback = f.read()
    print(loaded_feedback)

print("All tasks completed successfully!")


# In[ ]:





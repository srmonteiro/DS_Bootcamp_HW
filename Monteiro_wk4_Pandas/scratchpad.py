# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

# school_data_complete.head()                                                        # Test Run to see what the data frame looks like
# school_data_complete['school_name'].unique()                                       # Test Run to see the unique names are, just to make sure I have the right count
# school_data_complete['school_name'].value_counts()                                 # Test Run to see total number of students by school
total_schools = school_data_complete['school_name'].nunique()                        # This function produces *TOTAL NUMBER OF SCHOOLS*
total_students = school_data_complete['Student ID'].nunique()                        # This function produces *TOTAL NUMBER OF STUDENTS*
# school_data_complete['budget'].unique()                                            # Test Run This function pulls the budget total for each school
# df_school_budgets = school_data_complete['budget'].unique()                          # Stores all individual school budgets as array
total_budget = df_school_budgets.sum()                                               # Sums individual school budgets // still need to format as $$
avg_math_score_dist = school_data_complete['math_score'].mean()                    #
avg_read_score_dist = school_data_complete['reading_score'].mean()                 #
math_pass = school_data_complete.loc[school_data_complete['math_score'] > 69]
read_pass = school_data_complete.loc[school_data_complete['reading_score'] > 69]
percent_pass_math = len(math_pass) / total_students
percent_pass_read = len(read_pass) / total_students
overall_passing_Rate = (percent_pass_math + percent_pass_read)/2

print(total_schools)
print(total_students)
print(total_budget)
print(avg_math_score_dist)
print(avg_read_score_dist)
print(percent_pass_math)
print(percent_pass_read)
print(overall_passing_Rate)


district_data = pd.DataFrame({'Total Schools': [total_schools],
                      'Total Students': [total_students],
                      'Total Budget': {:,.2f}format.([total_budget]),
                      'Average Math Score': [avg_math_score_dist],
                      'Average Reading Score': [avg_read_score_dist],
                      '% Passing Math': [percent_pass_math],
                      '% Passing Reading': [percent_pass_read],
                      '% Overall Passing Rate': [overall_passing_Rate],
                     })

district_data


# ____________________

# bins = [0, 69, 100]
# pass_fail = ["Fail", "Pass"]
# school_data_complete['Reading Score'] = pd.cut(school_data_complete['reading_score'], bins, labels=pass_fail)
# school_data_complete['Math Score'] = pd.cut(school_data_complete['math_score'], bins, labels=pass_fail)
# reading_score_df = school_data_complete['Reading Score'].value_counts() 
# math_score_df = school_data_complete['Math Score'].value_counts() 
# reading_raw = school_data_complete['Reading Score'].value_counts('Pass')



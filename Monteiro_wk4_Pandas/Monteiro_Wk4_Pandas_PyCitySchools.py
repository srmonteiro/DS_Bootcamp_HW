
# coding: utf-8

# # PyCity Schools Analysis
# 
# * As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (<\$585 per student).
# 
# * As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).
# 
# * As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school. 
# ---

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[177]:


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


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[178]:


total_schools = school_data_complete['school_name'].nunique()                        # Produces *TOTAL NUMBER OF SCHOOLS*
total_students = school_data_complete['Student ID'].nunique()                        # Produces *TOTAL NUMBER OF STUDENTS*
df_school_budgets = school_data_complete['budget'].unique()                          # Stores all individual school budgets as array
total_budget = df_school_budgets.sum()                                  # Sums individual school budgets // still need to format as $$
avg_math_score_dist = school_data_complete['math_score'].mean()                      #
avg_read_score_dist = school_data_complete['reading_score'].mean()                   #
math_pass = school_data_complete.loc[school_data_complete['math_score'] > 69]
read_pass = school_data_complete.loc[school_data_complete['reading_score'] > 69]
percent_pass_math = (len(math_pass) / total_students) * 100
percent_pass_read = (len(read_pass) / total_students) * 100
overall_passing_Rate = (avg_math_score_dist + avg_read_score_dist)/2

#print(total_schools)
#print(total_students)
#print(total_budget)
#print(avg_math_score_dist)
#print(avg_read_score_dist)
#print(percent_pass_math)
#print(percent_pass_read)
#print(overall_passing_Rate)

#school_data_complete.head()                                                          # Test Run to see what the data frame looks like


# In[179]:


district_data = pd.DataFrame({'Total Schools': [total_schools],
                      'Total Students': [total_students],
                      'Total Budget': [total_budget],
                      'Average Math Score': [avg_math_score_dist],
                      'Average Reading Score': [avg_read_score_dist],
                      '% Passing Math': [percent_pass_math],
                      '% Passing Reading': [percent_pass_read],
                      '% Overall Passing Rate': [overall_passing_Rate],
                     })

district_data['Total Budget'] = district_data['Total Budget'].map("${:,.2f}".format)
district_data['Total Students'] = district_data['Total Students'].apply('{:,}'.format)

district_data


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[180]:


school_group = school_data_complete.groupby('school_name')
print(school_group)


# In[181]:


school_type = school_data_complete[['school_name', 'type']]
school_type = school_type.drop_duplicates()
school_type = school_type.reset_index()
school_type = school_type.drop(columns=['index'])
school_type


# In[182]:


student_total = pd.DataFrame(school_group['Student ID'].count())
student_total = student_total.reset_index()
student_total 


# In[183]:


school_budget = school_data_complete[['school_name', 'budget']]
school_budget = school_budget.drop_duplicates()
school_budget = school_budget.reset_index()
school_budget = school_budget.drop(columns=['index'])

school_budget


# In[184]:


by_school_data_math = school_data_complete.groupby(['school_name'])
avg_math_score_school = by_school_data_math['math_score'].mean() 
avg_math_score_school = pd.DataFrame([avg_math_score_school])
avg_math_score_school = avg_math_score_school.transpose()
avg_math_score_school = avg_math_score_school.rename(columns = {'math_score':'Average Math Score'})
avg_math_score_school = avg_math_score_school.reset_index()
avg_math_score_school 


# In[185]:


by_school_data_read = school_data_complete.groupby(['school_name'])
avg_read_score_school = by_school_data_read['reading_score'].mean() 
avg_read_score_school = pd.DataFrame([avg_read_score_school])
avg_read_score_school = avg_read_score_school.transpose()
avg_read_score_school = avg_read_score_school.rename(columns = {'reading_score':'Average Reading Score'})
avg_read_score_school = avg_read_score_school.reset_index()
avg_read_score_school 


# In[186]:


math_pass = school_data_complete.loc[school_data_complete['math_score'] > 69]
math_pass_byschool = math_pass['school_name'].value_counts()
math_pass_byschool = pd.DataFrame(math_pass_byschool)
math_pass_byschool = math_pass_byschool.rename(columns = {'school_name':'Pass Math'})
math_pass_byschool = math_pass_byschool.reset_index()
math_pass_byschool = math_pass_byschool.rename(columns = {'index':'school_name'})
math_pass_byschool 


# In[187]:


read_pass = school_data_complete.loc[school_data_complete['reading_score'] > 69]
read_pass
read_pass_byschool = read_pass['school_name'].value_counts()
read_pass_byschool = pd.DataFrame(read_pass_byschool)
read_pass_byschool = read_pass_byschool.rename(columns = {'school_name':'Pass Reading'})
read_pass_byschool = read_pass_byschool.reset_index()
read_pass_byschool = read_pass_byschool.rename(columns = {'index':'school_name'})
read_pass_byschool 


# In[188]:


school_data_mergeseries = pd.merge(school_type, student_total, on=["school_name"])
school_data_mergeseries = pd.merge(school_data_mergeseries, school_budget, on=["school_name"])
school_data_mergeseries = pd.merge(school_data_mergeseries, avg_math_score_school, on=["school_name"])
school_data_mergeseries = pd.merge(school_data_mergeseries, avg_read_score_school, on=["school_name"])
school_data_mergeseries = pd.merge(school_data_mergeseries, math_pass_byschool, on=["school_name"])
school_data_summaryfile = pd.merge(school_data_mergeseries, read_pass_byschool, on=["school_name"])
school_data_summaryfile


# In[189]:


school_data_summaryfile['Per Student Budget'] = (school_data_summaryfile['budget'] / school_data_summaryfile['Student ID'])
school_data_summaryfile['% Passing Math'] = (school_data_summaryfile['Pass Math'] / school_data_summaryfile['Student ID']) * 100 
school_data_summaryfile['% Passing Reading'] = (school_data_summaryfile['Pass Reading'] / school_data_summaryfile['Student ID']) * 100 
school_data_semi_clean = school_data_summaryfile.drop(columns=['Pass Math', 'Pass Reading'])
school_data_semi_clean['% Overall Passing Rate'] = (school_data_semi_clean['% Passing Reading'] + school_data_semi_clean['% Passing Math']) / 2
school_data_semi_clean


# In[190]:


school_data_col_rename = school_data_semi_clean.rename(columns = {'type':'School Type', 'Student ID':'Total Students', 'budget':'Total School Budget'})
school_data_col_rename 


# In[191]:


school_data_semi_arranged = school_data_col_rename[['school_name','School Type','Total Students','Total School Budget', 'Per Student Budget', 'Average Math Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall Passing Rate']] 

school_data_semi_final = school_data_semi_arranged.set_index(['school_name'])
school_data_semi_final


# In[192]:


school_data_finalreport = school_data_semi_final.sort_values('% Overall Passing Rate',ascending=False)
school_data_finalreport.head()


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[193]:


school_data_finalreport = school_data_finalreport.sort_values('% Overall Passing Rate',ascending=True)
school_data_finalreport.head()


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[194]:


school_data_complete.head()


# In[195]:


ninth_grade = school_data_complete.loc[school_data_complete['grade'] == '9th']
ninth_grade = ninth_grade[['school_name','grade','math_score']]
ninth_grade_math_avg = ninth_grade.groupby(['school_name']).mean()


# In[196]:


tenth_grade = school_data_complete.loc[school_data_complete['grade'] == '10th']
tenth_grade = tenth_grade[['school_name','grade','math_score']]
tenth_grade_math_avg = tenth_grade.groupby(['school_name']).mean()


# In[197]:


eleventh_grade = school_data_complete.loc[school_data_complete['grade'] == '11th']
eleventh_grade = eleventh_grade[['school_name','grade','math_score']]
eleventh_grade_math_avg = eleventh_grade.groupby(['school_name']).mean()


# In[198]:


twelveth_grade = school_data_complete.loc[school_data_complete['grade'] == '12th']
twelveth_grade = twelveth_grade[['school_name','grade','math_score']]
twelveth_grade_math_avg = twelveth_grade.groupby(['school_name']).mean()


# In[199]:


school_math_by_grade = pd.merge(ninth_grade_math_avg, tenth_grade_math_avg, on=["school_name"])
school_math_by_grade = school_math_by_grade.rename(columns={'math_score_x':'9th','math_score_y':'10th'} )
school_math_by_grade = pd.merge(school_math_by_grade, eleventh_grade_math_avg, on=["school_name"])
school_math_by_grade = pd.merge(school_math_by_grade, twelveth_grade_math_avg, on=["school_name"])
school_math_by_grade = school_math_by_grade.rename(columns={'math_score_x':'11th','math_score_y':'12th'} )
school_math_by_grade


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[200]:


ninth_grade = school_data_complete.loc[school_data_complete['grade'] == '9th']
ninth_grade = ninth_grade[['school_name','grade','reading_score']]
ninth_grade_read_avg = ninth_grade.groupby(['school_name']).mean()


# In[201]:


tenth_grade = school_data_complete.loc[school_data_complete['grade'] == '10th']
tenth_grade = tenth_grade[['school_name','grade','reading_score']]
tenth_grade_read_avg = tenth_grade.groupby(['school_name']).mean()


# In[202]:


eleventh_grade = school_data_complete.loc[school_data_complete['grade'] == '11th']
eleventh_grade = eleventh_grade[['school_name','grade','reading_score']]
eleventh_grade_read_avg = eleventh_grade.groupby(['school_name']).mean()


# In[203]:


twelveth_grade = school_data_complete.loc[school_data_complete['grade'] == '12th']
twelveth_grade = twelveth_grade[['school_name','grade','reading_score']]
twelveth_grade_read_avg = twelveth_grade.groupby(['school_name']).mean()


# In[214]:



school_reading_by_grade = pd.merge(ninth_grade_read_avg, tenth_grade_read_avg, on=["school_name"])
school_reading_by_grade = school_reading_by_grade.rename(columns={'reading_score_x':'9th','reading_score_y':'10th'} )
school_reading_by_grade = pd.merge(school_reading_by_grade, eleventh_grade_read_avg, on=["school_name"])
school_reading_by_grade = pd.merge(school_reading_by_grade, twelveth_grade_read_avg, on=["school_name"])
school_reading_by_grade = school_reading_by_grade.rename(columns={'reading_score_x':'11th','reading_score_y':'12th'} )
school_reading_by_grade


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[218]:


# Sample bins. Feel free to create your own bins.
bins = [0, 585, 620, 650, 675]
group_names = ["<$585", "$585-620", "$620-650", "$645-660"]


# In[219]:


school_data_finalreport.head()


# In[220]:



school_data_finalreport['Spending Ranges (Per Student)'] = pd.cut(school_data_finalreport["Per Student Budget"], bins, labels=group_names)
school_data_studentcostbin = school_data_finalreport.drop(columns=['Total Students','Total School Budget','Per Student Budget'])
school_data_studentcostbin.groupby(['Spending Ranges (Per Student)']).mean()


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[234]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 3000, 5000]
group_names = ["Tall <1000", "Grande 1000-3000", "Venti 3000-5000"]


# In[235]:



school_data_finalreport['School Size'] = pd.cut(school_data_finalreport['Total Students'], size_bins, labels=group_names)
school_data_studentsizebin = school_data_finalreport.drop(columns=['Total Students','Total School Budget','Per Student Budget'])
school_data_studentsizebin.groupby(['School Size']).mean()


# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[236]:



school_data_typereport = school_data_finalreport.drop(columns=['Total Students','Total School Budget','Per Student Budget'])
school_data_typereport.groupby(['School Type']).mean()


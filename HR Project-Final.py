#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


# Read the employee data from the CSV file
employee = pd.read_csv(r"H:\DEPI\Datasets\Datasets\HR\Employee.csv")
pd.set_option('display.max_columns', None)
employee


# In[4]:


# Replace abbreviations with the full state name 
employee['State']= employee['State'].replace('IL', 'Illinois', inplace=False)
employee['State']= employee['State'].replace('CA', 'California', inplace=False)
employee['State']= employee['State'].replace('NY', 'New York', inplace=False)
employee


# In[5]:


#checking if there are duplicates
employee.dropna(how='all', inplace=True)
employee


# In[6]:


# Read the EducationLevel data from the CSV file
Educationlevel = pd.read_csv(r"H:\DEPI\Datasets\Datasets\HR\EducationLevel.csv")
Educationlevel


# In[7]:


# Map numerical education codes to descriptive education levels
for index, row in employee.iterrows():
     # Check the value in the 'EducationLevelID' column
    if row['Education'] == 1:
        employee.at[index, 'EducationLevel'] = 'No Formal Qualifications'
    elif row['Education'] == 2:
        employee.at[index, 'EducationLevel'] = 'Highschool'
    elif row['Education'] == 3:
        employee.at[index, 'EducationLevel'] = 'Bachelors'
    elif row['Education'] == 4:
        employee.at[index, 'EducationLevel'] = 'Masters'
    elif row['Education'] == 5:
        employee.at[index, 'EducationLevel'] = 'Doctorate'

employee


# In[8]:


# Read the PerformanceRating data from the CSV file
PerformanceRating = pd.read_csv(r"H:\DEPI\Datasets\Datasets\HR\PerformanceRating.csv")
PerformanceRating


# In[9]:


#checking if there are duplicates
PerformanceRating.dropna(how='all', inplace=True)
PerformanceRating


# In[10]:


# Read the RatingLevel data from the CSV file
RatingLevel = pd.read_csv(r"H:\DEPI\Datasets\Datasets\HR\RatingLevel.csv")
RatingLevel


# In[11]:


# Map numerical Self-Rating codes to descriptive education levels
for index, row in PerformanceRating.iterrows():
    if row['SelfRating'] == 1:
        PerformanceRating.at[index, 'SelfRatingLevel'] = 'Unacceptable'
    elif row['SelfRating'] == 2:
        PerformanceRating.at[index, 'SelfRatingLevel'] = 'Needs Improvement'
    elif row['SelfRating'] == 3:
        PerformanceRating.at[index, 'SelfRatingLevel'] = 'Meets Expectation'
    elif row['SelfRating'] == 4:
        PerformanceRating.at[index, 'SelfRatingLevel'] = 'Exceeds Expectation'
    elif row['SelfRating'] == 5:
        PerformanceRating.at[index, 'SelfRatingLevel'] = 'Above and Beyond'

PerformanceRating


# In[12]:


# Map numerical Manager-Rating codes to descriptive education levels
for index, row in PerformanceRating.iterrows():
    if row['ManagerRating'] == 1:
        PerformanceRating.at[index, 'ManagerRatingLevel'] = 'Unacceptable'
    elif row['ManagerRating'] == 2:
        PerformanceRating.at[index, 'ManagerRatingLevel'] = 'Needs Improvement'
    elif row['ManagerRating'] == 3:
        PerformanceRating.at[index, 'ManagerRatingLevel'] = 'Meets Expectation'
    elif row['ManagerRating'] == 4:
        PerformanceRating.at[index, 'ManagerRatingLevel'] = 'Exceeds Expectation'
    elif row['ManagerRating'] == 5:
        PerformanceRating.at[index, 'ManagerRatingLevel'] = 'Above and Beyond'

PerformanceRating


# In[13]:


# Read the Satisfied-Level data from the CSV file
SatisfiedLevel = pd.read_csv(r"H:\DEPI\Datasets\Datasets\HR\SatisfiedLevel.csv")
SatisfiedLevel


# In[14]:


# Map numerical Environment-Satisfaction codes to descriptive education levels
for index, row in PerformanceRating.iterrows():
    if row['EnvironmentSatisfaction'] == 1:
        PerformanceRating.at[index, 'EnvironmentSatisfactionLevel'] = 'Very Dissatisfied'
    elif row['EnvironmentSatisfaction'] == 2:
        PerformanceRating.at[index, 'EnvironmentSatisfactionLevel'] = 'Dissatisfied'
    elif row['EnvironmentSatisfaction'] == 3:
        PerformanceRating.at[index, 'EnvironmentSatisfactionLevel'] = 'Neutral'
    elif row['EnvironmentSatisfaction'] == 4:
        PerformanceRating.at[index, 'EnvironmentSatisfactionLevel'] = 'Satisfied'
    elif row['EnvironmentSatisfaction'] == 5:
        PerformanceRating.at[index, 'EnvironmentSatisfactionLevel'] = 'Very Satisfied'

PerformanceRating


# In[15]:


# Map numerical Job-Satisfaction codes to descriptive education levels
for index, row in PerformanceRating.iterrows():
    if row['JobSatisfaction'] == 1:
        PerformanceRating.at[index, 'JobSatisfactionLevel'] = 'Very Dissatisfied'
    elif row['JobSatisfaction'] == 2:
        PerformanceRating.at[index, 'JobSatisfactionLevel'] = 'Dissatisfied'
    elif row['JobSatisfaction'] == 3:
        PerformanceRating.at[index, 'JobSatisfactionLevel'] = 'Neutral'
    elif row['JobSatisfaction'] == 4:
        PerformanceRating.at[index, 'JobSatisfactionLevel'] = 'Satisfied'
    elif row['JobSatisfaction'] == 5:
        PerformanceRating.at[index, 'JobSatisfactionLevel'] = 'Very Satisfied'

PerformanceRating


# In[16]:


# Map numerical Relationship-Satisfaction codes to descriptive education levels
for index, row in PerformanceRating.iterrows():
    if row['RelationshipSatisfaction'] == 1:
        PerformanceRating.at[index, 'RelationshipSatisfactionLevel'] = 'Very Dissatisfied'
    elif row['RelationshipSatisfaction'] == 2:
        PerformanceRating.at[index, 'RelationshipSatisfactionLevel'] = 'Dissatisfied'
    elif row['RelationshipSatisfaction'] == 3:
        PerformanceRating.at[index, 'RelationshipSatisfactionLevel'] = 'Neutral'
    elif row['RelationshipSatisfaction'] == 4:
        PerformanceRating.at[index, 'RelationshipSatisfactionLevel'] = 'Satisfied'
    elif row['RelationshipSatisfaction'] == 5:
        PerformanceRating.at[index, 'RelationshipSatisfactionLevel'] = 'Very Satisfied'

PerformanceRating


# In[17]:


#Merging both employee and PerformanceRating tables
Employee_Performance_Merged = pd.merge(employee, PerformanceRating, on='EmployeeID')
pd.set_option('display.max_columns', None)
Employee_Performance_Merged


# In[18]:


Employee_Performance_Merged.to_csv(r"C:\Users\ELZAHBIA\Downloads\pro\HR.csv")


# In[19]:


# Print information about the Employee_Performance_Merged DataFrame
Employee_Performance_Merged.info()


# In[20]:


# Calculate and print summary statistics for the Employee_Performance_Merged DataFrame
Employee_Performance_Merged.describe()


# In[21]:


#Identifying outliers

sns.boxplot(x='Salary', data=employee)
plt.title('Salary Distribution')
plt.show()


# # Salary

# In[22]:


#Configuring the departments with the highest average salary
highest_salary_department = employee.groupby('Department')['Salary'].mean().nlargest().reset_index()
plt.figure(figsize=(7, 3))
sns.barplot(x='Salary', y='Department', data=highest_salary_department, palette='viridis', width=0.6)
for index, value in enumerate(highest_salary_department['Salary']):
    plt.text(value, index, f'{value:.2f}', ha='center', va='center')
    
plt.title('Top-Paying Departments')
plt.xlabel('Average Salary')
plt.ylabel('Department')
plt.show()


# In[23]:


# The salary distribution across different education levels
education_salary_stats = employee.groupby('EducationLevel')['Salary'].mean().nlargest().reset_index()
plt.figure(figsize=(8, 4))
plt.pie(education_salary_stats['Salary'], labels=education_salary_stats['EducationLevel'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('coolwarm', len(education_salary_stats)))
plt.title('Salary distribution across different education levels')
plt.show()


# In[24]:


## The salary distribution across different fields of study
education_field_salary_stats = employee.groupby('EducationField')['Salary'].mean().nlargest().reset_index()
unique_education_field = employee.drop_duplicates(subset=['EducationField'])

education_field_salary_stats = unique_education_field.groupby('EducationField')['Salary'].mean().nlargest(5).reset_index()
plt.figure(figsize=(8, 3))
sns.barplot(x='Salary', y='EducationField', data=education_field_salary_stats, palette='Blues', width=0.6)
plt.title('Income Disparity Among Educational Backgrounds')
plt.xlabel('Average Salary')
plt.ylabel('Education Field')
for i, (index, row) in enumerate(education_field_salary_stats.iterrows()):
    plt.text(row['Salary'] + 0.1, i, f"{row['Salary']:.2f}", ha='center', va='bottom', fontsize=10)
plt.show()


# In[25]:


##Arranging the salaries in descending order according to their associated positions 

average_salary_by_JobRole = employee.groupby('JobRole')['Salary'].mean().sort_values(ascending=False).reset_index()
plt.figure(figsize=(8, 4))
sns.barplot(x='Salary', y='JobRole', data=average_salary_by_JobRole, palette='magma', width=0.6)

for index, value in enumerate(average_salary_by_JobRole['Salary']):
    plt.text(value, index, f'{value:.2f}', va='center')

plt.title('Salary Differences Across Occupations')
plt.xlabel('Average Salary')
plt.ylabel('Job Role')
plt.show()


# In[26]:


##The job roles with the highest percentage of employees working overtime
total_employees = employee.shape[0]

JobRole_Overtime = employee[employee['OverTime'] == 'Yes'].groupby('JobRole')['OverTime'].count()
JobRole_Total = employee.groupby('JobRole').size()

JobRole_Overtime_rate = (JobRole_Overtime / total_employees) * 100
JobRole_Overtime_rate = JobRole_Overtime_rate.fillna(0)  
JobRole_Overtime_rate = JobRole_Overtime_rate.nlargest().reset_index().rename(columns={'index': 'JobRole', 0: 'OvertTime Rate'})

plt.figure(figsize=(7, 4))
plt.pie(JobRole_Overtime_rate[JobRole_Overtime_rate.columns[1]], labels=JobRole_Overtime_rate['JobRole'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2', len(JobRole_Overtime_rate)))
plt.title('Occupations with High Overtime Demand')
plt.show()


# In[27]:


# The differences in salaries between genders

average_salary_by_Gender = employee.groupby('Gender')['Salary'].mean().nlargest().reset_index()
plt.figure(figsize=(7, 3))
sns.barplot(x='Gender', y='Salary', data=average_salary_by_Gender, palette='cool', width=0.5)

for index, value in enumerate(average_salary_by_Gender['Salary']):
    plt.text(index, value, f'{value:.2f}', ha='center')

plt.title('Salary Differences Between Genders')
plt.xlabel('Gender')
plt.ylabel('Average Salary')
plt.show()


# In[28]:


#Salary Disparities between ethnic groups
average_salary_by_Ethnicity = employee.groupby('Ethnicity')['Salary'].mean().nlargest().reset_index()
plt.figure(figsize=(8, 4))
sns.stripplot(x='Salary', y='Ethnicity', data=employee, jitter=True, hue='Ethnicity')

plt.title('Salary Disparities Across Ethnicities')
plt.xlabel('Salary')
plt.ylabel('Ethnicity')
plt.legend().remove() 

plt.show()


# # Turnover

# In[45]:


# Employee attrition by state
state_turnover = employee[employee['Attrition'] == 'Yes'].groupby('State')['Attrition'].count()
state_total_employees = employee.groupby('State').size()
state_turnover_rate = (state_turnover / state_total_employees) * 100
state_turnover_rate = state_turnover_rate.nlargest(n=10).reset_index().rename(columns={'index': 'State', 0: 'Turnover Rate'})
plt.figure(figsize=(7, 3))
sns.barplot(x=state_turnover_rate['Turnover Rate'], y=state_turnover_rate['State'], palette='coolwarm', width=0.6)

for index, value in enumerate(state_turnover_rate['Turnover Rate']):
    plt.text(value, index, f'{value:.2f}%', va='center')

plt.title('Employee Attrition in Each State')
plt.xlabel('Turnover Rate (%)')
plt.ylabel('State')
plt.show()


# In[30]:


#The department with the highest rate of employee turnover
department_turnover = employee[employee['Attrition'] == 'Yes'].groupby('Department')['Attrition'].count()
department_total_employees = employee.groupby('Department').size()

department_turnover_rate = (department_turnover / department_total_employees) * 100
department_turnover_rate = department_turnover_rate.nlargest().reset_index().rename(columns={'index': 'Department', 0: 'Turnover Rate'})

plt.figure(figsize=(7, 3))
sns.barplot(x=department_turnover_rate['Turnover Rate'], y=department_turnover_rate['Department'], palette='coolwarm', width=0.6)

for index, value in enumerate(department_turnover_rate['Turnover Rate']):
    plt.text(value, index, f'{value:.2f}%', va='center')

plt.title('Employee Attrition in each Department')
plt.xlabel('Turnover Rate (%)')
plt.ylabel('Department')
plt.show()


# In[31]:


#The position with the highest employee turnover
JobRole_turnover = employee[employee['Attrition'] == 'Yes'].groupby('JobRole')['Attrition'].count()
total_employees = employee.groupby('JobRole').size()

JobRole_turnover_rate = (JobRole_turnover / total_employees) * 100
JobRole_turnover_rate = JobRole_turnover_rate.nlargest().reset_index().rename(columns={'index': 'JobRole', 0: 'Turnover Rate'})

plt.figure(figsize=(7, 4))
plt.pie(JobRole_turnover_rate['Turnover Rate'], labels=JobRole_turnover_rate['JobRole'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2', len(JobRole_turnover_rate)))
plt.title('Employee Attrition Across Different Positions')
plt.show()


# In[32]:


#Turnover rate by ethnic groups
Ethnicity_turnover = employee[employee['Attrition'] == 'Yes'].groupby('Ethnicity')['Attrition'].count()
total_employees = employee.groupby('Ethnicity').size()

Ethnicity_turnover_rate = (Ethnicity_turnover / total_employees) * 100
Ethnicity_turnover_rate = Ethnicity_turnover_rate.nlargest().reset_index().rename(columns={'index': 'Ethnicity', 0: 'Turnover Rate'})

plt.figure(figsize=(7, 3))
sns.stripplot(x=Ethnicity_turnover_rate['Turnover Rate'], y=Ethnicity_turnover_rate['Ethnicity'], jitter=True)  # Remove palette argument

plt.title('Ethnic Turnover Rates')
plt.xlabel('Turnover Rate (%)')
plt.ylabel('Ethnicity')
plt.show()


# In[33]:


#Attrition among different age groups
employee = pd.DataFrame(employee )

bins = [20, 30, 40, 50, 60] 
labels = ['20-29', '30-39', '40-49', '50-59']  
employee['AgeGroup'] = pd.cut(employee['Age'], bins=bins, labels=labels, right=False)

Turnover_by_age = employee.groupby(['AgeGroup', 'Attrition']).size().unstack().fillna(0)

plt.figure(figsize=(7,3))
sns.heatmap(Turnover_by_age, annot=True, cmap='Blues', fmt='g')

plt.title('Departure Rates by Age Cohort')
plt.xlabel('Attrition')
plt.ylabel('Age Group')
plt.show()


# In[34]:


#gender and turnover rate
Gender_turnover = employee[employee['Attrition'] == 'Yes'].groupby('Gender')['Attrition'].count()
total_employees = employee.groupby('Gender').size()

Gender_turnover_rate = (Gender_turnover / total_employees) * 100
Gender_turnover_rate = Gender_turnover_rate.nlargest().reset_index().rename(columns={'index': 'Gender', 0: 'Turnover Rate'})
plt.figure(figsize=(6, 3))
sns.violinplot(x='Gender', y='Turnover Rate', showmeans=True, data=Gender_turnover_rate, palette='coolwarm')

plt.title('Gender-Based Turnover')
plt.xlabel('Gender')
plt.ylabel('Turnover Rate (%)')
plt.show()


# In[35]:


#The Relationship Between Overtime and Employee Departure
OverTime_turnover = employee[employee['Attrition'] == 'Yes'].groupby('OverTime')['Attrition'].count()
total_employees = employee.groupby('OverTime').size()
OverTime_turnover_rate = (OverTime_turnover / total_employees) * 100
OverTime_turnover_rate = OverTime_turnover_rate.nlargest().reset_index().rename(columns={'index': 'OverTime', 0: 'Turnover Rate'})
plt.figure(figsize=(7,5))
plt.pie(OverTime_turnover_rate['Turnover Rate'], labels=OverTime_turnover_rate['OverTime'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3', len(OverTime_turnover_rate)))

plt.title('The Relationship Between Overtime and Employee Departure')
plt.show()


# # Employees satisfaction

# In[36]:


#The relationship between salary levels and Relationship-satisfaction
salary_RelationshipSatisfaction = Employee_Performance_Merged.groupby('RelationshipSatisfactionLevel')['Salary'].mean().nlargest().reset_index()
plt.figure(figsize=(6,3))
sns.barplot(x='Salary', y='RelationshipSatisfactionLevel', data=salary_RelationshipSatisfaction, palette='coolwarm',width=0.5)

for index, value in enumerate(salary_RelationshipSatisfaction['Salary']):
    plt.text(value, index, f'{value:.2f}', va='center')

plt.title('Salary Differences Based on Relationship Evaluation')
plt.xlabel('Average Salary')
plt.ylabel('Relationship Satisfaction Level')
plt.show()


# In[37]:


# The overall levels of EnvironmentSatisfaction, JobSatisfaction, and RelationshipSatisfaction between employees who turned over and those who stayed
attrition_satisfaction = Employee_Performance_Merged.groupby('Attrition')[['EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction']].mean()
attrition_satisfaction.plot(kind='bar', figsize=(5, 3), color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Satisfaction Among Stayers vs. Leavers')
plt.ylabel('Satisfaction Level')
plt.xticks(rotation=0)
plt.legend(title='Satisfaction Types', bbox_to_anchor=None)  
plt.show()


# In[38]:


# Employees satisfation with their job
JobRole_Satisfaction = Employee_Performance_Merged.groupby('JobRole')['JobSatisfaction'].mean()
plt.figure(figsize=(7, 3))
sns.violinplot(x='JobSatisfaction', y='JobRole', data=Employee_Performance_Merged, palette='magma')

plt.title('The Impact of Job Position on Satisfaction')
plt.xlabel('Job Satisfaction')
plt.ylabel('Job Role')
plt.show()


# In[39]:


#The impact of the training on the employees
training_satisfaction = Employee_Performance_Merged.groupby('TrainingOpportunitiesTaken')['JobSatisfaction'].mean()
plt.figure(figsize=(6, 3))
sns.lineplot(x='TrainingOpportunitiesTaken', y='JobSatisfaction', data=training_satisfaction.reset_index(), marker='o', color='purple')

plt.title('The Impact of Training on Employee Morale')
plt.xlabel('Training Opportunities Taken')
plt.ylabel('Job Satisfaction')
plt.show()


# # Ratings

# In[40]:


#The relationship between self-rating and salary
average_salary_by_SelfRatingLevel = Employee_Performance_Merged.groupby('SelfRatingLevel')['Salary'].mean().nlargest().reset_index()
plt.figure(figsize=(7, 3))
sns.scatterplot(x='SelfRatingLevel', y='Salary', size='Salary', data=average_salary_by_SelfRatingLevel, legend=False, sizes=(100, 500))

plt.title('Salary Differences Based on Self-Evaluation')
plt.xlabel('Self-Rating Level')
plt.ylabel('Average Salary')
plt.show()


# In[41]:


#The relationship between Manager Rating Level and salary
average_salary_by_ManagerRatingLevel = Employee_Performance_Merged.groupby('ManagerRatingLevel')['Salary'].mean().nlargest().reset_index()
plt.figure(figsize=(6, 3))
sns.barplot(x='Salary', y='ManagerRatingLevel', data=average_salary_by_ManagerRatingLevel, palette='RdYlGn', width=0.6)

for index, value in enumerate(average_salary_by_ManagerRatingLevel['Salary']):
    plt.text(value, index, f'{value:.2f}', ha='center', va='center')

plt.title('Salary Differences Based on Manger-Evaluation')
plt.xlabel('Average Salary')
plt.ylabel('Manager Rating Level')
plt.show()


# In[42]:


#Alignment of self and manager assessments
ratings_comparison = Employee_Performance_Merged[['SelfRating', 'ManagerRating']].mean()
plt.figure(figsize=(6, 4))
sns.heatmap(ratings_comparison.to_frame().T, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.title('Self Rating vs Manager Rating ')
plt.show()


# # Work-life Balance

# In[43]:


#The impact of overtime on work-life balance
overtime_worklife = Employee_Performance_Merged.groupby('OverTime')['WorkLifeBalance'].mean()
plt.figure(figsize=(7, 4))
plt.pie(overtime_worklife, labels=overtime_worklife.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2', len(overtime_worklife)))

plt.title('Work-Life Equilibrium and Extra Hours')
plt.show()


# In[44]:


# The work-life balance within each department
Department_worklife = Employee_Performance_Merged.groupby('Department')['WorkLifeBalance'].mean()
Employee_Performance_Merged['dummy_hue'] = 'same_color'
plt.figure(figsize=(8, 4))
sns.violinplot(x='Department', y='WorkLifeBalance', showmeans=True, data=Employee_Performance_Merged)

plt.title('Work-Life Balance Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Work-Life Balance')
plt.show()


# In[ ]:





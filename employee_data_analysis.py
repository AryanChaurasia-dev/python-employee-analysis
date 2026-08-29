# import pandas as pd
# import numpy as np

# # STEP 1: DATA LOAD

# df = pd.read_excel(r"C:\Users\ARYAN\OneDrive\Desktop\python\project\employee_data.xlsx")
# # print(df)

# import pandas as pd
# import numpy as np






# #  STEP 2: DATA OVERVIEW

# # Show me first 10 rows
# print("FIRST 10 ROWS:")
# print(df.head(10))

# # Size of the Dataset
# print("\nDATASET SIZE (Rows x Columns):")
# print(df.shape)

# # Column names
# print("\nCOLUMNS:")
# print(df.columns.tolist())

# # Data types and info
# print("\nDATASET INFO:")
# print(df.info())

# # NULL values check
# print("\nMISSING VALUES:")
# print(df.isnull().sum())

# # Duplicate rows check
# print("\nDUPLICATE ROWS:", df.duplicated().sum())


# # STEP 3: BASIC STATISTICS 

# print("\nSALARY STATISTICS:")
# print("Average Salary : ", round(np.mean(df["Salary"]), 2))
# print("Maximum Salary : ", np.max(df["Salary"]))
# print("Minimum Salary : ", np.min(df["Salary"]))
# print("Std Deviation  : ", round(np.std(df["Salary"]), 2))


# # STEP 4: FILTERING 

# # High salary employees (> 100,000)
# print("\nHIGH SALARY EMPLOYEES (> 1,00,000):")
# high_salary = df[df["Salary"] > 100000]
# print(high_salary[["Employee_Name", "Department", "City", "Salary"]])

# # Excellent performers
# print("\nEXCELLENT PERFORMERS:")
# excellent = df[df["Performance_Category"] == "Excellent"]
# print(excellent[["Employee_Name", "Department", "Performance_Score"]])

# # Delhi + Salary > 80000
# print("\nDELHI EMPLOYEES WITH SALARY > 80,000:")
# delhi_high = df[(df["City"] == "Delhi") & (df["Salary"] > 80000)]
# print(delhi_high[["Employee_Name", "Department", "Salary"]])


# #  STEP 5: GROUP BY ANALYSIS 

# # Department wise average salary
# print("\nDEPARTMENT WISE AVERAGE SALARY:")
# print(df.groupby("Department")["Salary"].mean().round(0))

# # Department wise employee count
# print("\nDEPARTMENT WISE EMPLOYEE COUNT:")
# print(df["Department"].value_counts())

# # City wise average performance score
# print("\nCITY WISE AVERAGE PERFORMANCE SCORE:")
# print(df.groupby("City")["Performance_Score"].mean().round(2))

# # Performance category wise count
# print("\nPERFORMANCE CATEGORY WISE COUNT:")
# print(df.groupby("Performance_Category")["Employee_ID"].count())


# #  STEP 6: TOP PERFORMERS 

# # Top 10 highest salary
# print("\nTOP 10 HIGHEST SALARY EMPLOYEES:")
# top_salary = df.nlargest(10, "Salary")
# print(top_salary[["Employee_Name", "Department", "Salary"]])

# # Top 10 best performers
# print("\nTOP 10 BEST PERFORMERS:")
# top_performers = df.nlargest(10, "Performance_Score")
# print(top_performers[["Employee_Name", "Department", "Performance_Score"]])


# # STEP 7: NEW COLUMNS 

# # Add the Annual Salary column 
# df["Annual_Salary"] = np.multiply(df["Salary"], 12)

# # Classify the Salary Range 
# df["Salary_Range"] = df["Salary"].apply(
#     lambda x: "High" if x > 100000
#     else ("Medium" if x > 60000
#     else "Low")
# )

# # Experience Level by Age
# df["Experience_Level"] = df["Age"].apply(
#     lambda x: "Senior" if x > 40
#     else ("Mid" if x > 30
#     else "Junior")
# )

# print("\nEMPLOYEES WITH NEW COLUMNS:")
# print(df[["Employee_Name", "Salary", "Annual_Salary",
#           "Salary_Range", "Experience_Level"]].head(10))


# # STEP 8: BUSINESS INSIGHTS

# print("\nBUSINESS INSIGHTS:")
# print("Highest Paying Department :",
#       df.groupby("Department")["Salary"].mean().idxmax())

# print("Most Employees in City    :",
#       df["City"].value_counts().idxmax())

# print("Age-Salary Correlation    :",
#       round(df["Age"].corr(df["Salary"]), 2))

# needs_imp = df[df["Performance_Category"] == "Needs Improvement"]
# print("Needs Improvement %       :",
#       round(len(needs_imp) / len(df) * 100, 1), "%")


# # STEP 9: EXPORT 

# # Export the complete analysis in Excel
# df.to_excel("employee_analysis.xlsx", index=False)
# print("\nFull analysis exported: employee_analysis.xlsx")

# # Export only excellent Performers
# excellent.to_excel("excellent_employees.xlsx", index=False)
# print("Excellent employees exported: excellent_employees.xlsx")



# # STEP 10: SORTING 

# # Sort salary by descending order
# print("\nEMPLOYEES SORTED BY SALARY:")
# print(df.sort_values("Salary", ascending=False)[
#     ["Employee_Name", "Department", "Salary"]
# ].head(10))

# # Multiple columns sort
# print("\nSORTED BY DEPARTMENT THEN SALARY:")
# print(df.sort_values(
#     ["Department", "Salary"],
#     ascending=[True, False]
# )[["Employee_Name", "Department", "Salary"]])


# #  STEP 11: STRING OPERATIONS 

# # Names uppercase
# print("\nEMPLOYEE NAMES UPPERCASE:")
# print(df["Employee_Name"].str.upper().head(5))

# # City lowercase
# print("\nCITIES LOWERCASE:")
# print(df["City"].str.lower().unique())

# # Does the name contain the word 'Employee' or not
# print("\nNAMES CONTAINING 'Employee':")
# print(df[df["Employee_Name"].str.contains("Employee")]["Employee_Name"].head(5))


# # STEP 12: PIVOT TABLE 

# # Department + City wise average salary 
# print("\nPIVOT TABLE — DEPT x CITY AVERAGE SALARY:")
# pivot = df.pivot_table(
#     values="Salary",
#     index="Department",
#     columns="City",
#     aggfunc="mean"
# ).round(0)
# print(pivot)


# # STEP 13: PERCENTAGE ANALYSIS

# # Percentage of every performing category
# print("\nPERFORMANCE CATEGORY PERCENTAGE:")
# perf_pct = df["Performance_Category"].value_counts(normalize=True) * 100
# print(perf_pct.round(1))

# # Department wise excellent percentage
# print("\nEXCELLENT PERFORMERS % PER DEPARTMENT:")
# dept_excellent = df.groupby("Department").apply(
#     lambda x: (x["Performance_Category"] == "Excellent").sum() / len(x) * 100
# ).round(1)
# print(dept_excellent)


# # STEP 14: CONDITIONAL ANALYSIS 

# # Age group wise average salary
# df["Age_Group"] = df["Age"].apply(
#     lambda x: "20-25" if x <= 25
#     else ("26-35" if x <= 35
#     else ("36-45" if x <= 45
#     else "46+"))
# )

# print("\nAGE GROUP WISE AVERAGE SALARY:")
# print(df.groupby("Age_Group")["Salary"].mean().round(0))


# # STEP 15: FINAL SUMMARY REPORT 

# print("\n" + "="*50)
# print("FINAL EMPLOYEE ANALYSIS SUMMARY REPORT")
# print("="*50)
# print(f"Total Employees       : {len(df)}")
# print(f"Total Departments     : {df['Department'].nunique()}")
# print(f"Total Cities          : {df['City'].nunique()}")
# print(f"Average Salary        : ₹{df['Salary'].mean():,.0f}")
# print(f"Highest Salary        : ₹{df['Salary'].max():,.0f}")
# print(f"Lowest Salary         : ₹{df['Salary'].min():,.0f}")
# print(f"Excellent Performers  : {(df['Performance_Category']=='Excellent').sum()}")
# print(f"Needs Improvement     : {(df['Performance_Category']=='Needs Improvement').sum()}")
# print("="*50)



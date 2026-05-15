
# STUDENT RESULT ANALYZER
# Beginner-Friendly Python Project


# Import pandas library
import pandas as pd


try:
    # Read student CSV file
    df = pd.read_csv("students.csv")


    print("      STUDENT RESULT ANALYZER")
  

    # Display student data
    print("📋 Student Data:\n")
    print(df)

    
    # CALCULATE TOTAL MARKS
   

    df["Total"] = df["Math"] + df["Science"] + df["English"]

    # CALCULATE AVERAGE
    

    df["Average"] = df["Total"] / 3

    
    # ASSIGN GRADE
    

    grades = []

    for avg in df["Average"]:

        if avg >= 90:
            grades.append("A")

        elif avg >= 75:
            grades.append("B")

        elif avg >= 50:
            grades.append("C")

        else:

          grades.append("Fail")

    # Add grades column
    df["Grade"] = grades

    # FIND TOPPER


    topper = df.loc[df["Average"].idxmax()]
    # DISPLAY RESULTS
   

   
    print(" FINAL RESULTS")


    print(df)

    print("\n🏆 TOPPER DETAILS")

    print("Name :", topper["Name"])
    print("Average :", topper["Average"])
    print("Grade :", topper["Grade"])

    # SAVE RESULT TO NEW CSV


    df.to_csv("final_results.csv", index=False)

    print("\n Result saved as 'final_results.csv'")

except FileNotFoundError:
    print("\nError: students.csv file not found.")

except Exception as e:
    print("\n Error:", e)

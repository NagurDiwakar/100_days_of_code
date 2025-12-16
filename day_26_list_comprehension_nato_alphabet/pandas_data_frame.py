# example for creating a pandas DataFrame from a dictionary using iterrows() 
# iterrows() allows you to iterate over DataFrame rows as (index, Series) pairs.
# alike for loops in lists, iterrows() is specifically designed for DataFrames.



import pandas as pd
data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
}   

df = pd.DataFrame(data)
for (index, row) in df.iterrows():
    print(row)  


# student score example
student_scores = {
    "student": ["Alice", "Bob", "Charlie"],
    "score": [85, 92, 78]
}

student_df = pd.DataFrame(student_scores)
for (index, row) in student_df.iterrows():
    if row.score >= 90:
        print(row.student)
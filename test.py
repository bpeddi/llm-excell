import pandas as pd

# Specify the path to your CSV file
csv_file_path = 'Exams_list.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Print the first few rows of the DataFrame to verify it was read correctly
average_value = df['Exam points'].mean()

# Print the average value
print(f"The average of the column Exam Points is: {average_value}")

import pandas as pd

# Read the CSV files
daigt = pd.read_csv('./data/own/daigt.csv')
persuade = pd.read_csv('./data/ellipse/ELLIPSE_Final_github.csv')

# Merge the DataFrames based on 'id' in daigt and 'text_id_kaggle' in persuade
merged_df = pd.merge(daigt, persuade, left_on='id', right_on='text_id_kaggle', suffixes=('_daigt', '_persuade'))

# Remove rows that don't have a value in 'essay_result'
filtered_df = merged_df.dropna(subset=['essay_result'])

# Filter rows where grade is between 9 and 12
filtered_df = filtered_df[(filtered_df['grade'] >= 9) & (filtered_df['grade'] <= 12)]

# Create a new DataFrame with the required structure
expanded_rows = []

for _, row in filtered_df.iterrows():
    expanded_rows.append({
        'text': row['source_text'],
        'label': 0,
        'prompt': row['prompt'],
        'grade': row['grade'],
        'task': row['task']
    })
    expanded_rows.append({
        'text': row['essay_result'],
        'label': 1,
        'prompt': row['prompt'],
        'grade': "gpt-4",
        'task': row['task']
    })

# Convert the list of dictionaries to a DataFrame
expanded_df = pd.DataFrame(expanded_rows)

# Save the new DataFrame to a CSV file
expanded_df.to_csv('Data.csv', index=False)

print(f"The expanded DataFrame has been saved as 'expanded_merged_output.csv'. It contains {expanded_df.shape[0]} rows.")

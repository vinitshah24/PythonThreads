"""
test_case_id, metrics_name, metric_value_test
12344,metric1,val1
12344,metric2,val2
12344,metric3,val3
22344,metric1,val1
22344,metric2,val2
22344,metric3,val3
22344,metric4,val4

id,metric1,metric2,metric3,metric4
12344,val1,val2,val3,
22344,val1,val2,val3,val4
"""

import csv

input_file = 'original.csv'
output_file = 'transformed.csv'
metrics_by_test_case = {}

with open(input_file, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        test_case_id = row['test_case_id']
        metrics_name = row['metrics_name']
        metric_value = row['metric_value_test']

        if test_case_id not in metrics_by_test_case:
            metrics_by_test_case[test_case_id] = {'id': test_case_id}

        metrics_by_test_case[test_case_id][metrics_name] = metric_value

# Get all unique metric names from the CSV
unique_metrics = set()
for data in metrics_by_test_case.values():
    unique_metrics.update(data.keys())

# Write the data to the new CSV file in the desired format
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['id'] + sorted(unique_metrics - {'id'})
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for test_case_data in metrics_by_test_case.values():
        # Fill in empty values for missing metrics
        for metric in fieldnames[1:]:
            test_case_data.setdefault(metric, '')

        writer.writerow(test_case_data)


# ----------------------------

import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('file1.csv')

# Read the second CSV file
df2 = pd.read_csv('file2.csv')

# Merge the two dataframes based on 'test_case_id'
merged_df = pd.merge(df1, df2, on='test_case_id', how='outer')

# Write the merged dataframe to a new CSV file
merged_df.to_csv('merged.csv', index=False)

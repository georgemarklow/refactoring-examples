from workflow_reader import *
 
"""
Runs workflow 1.

@return: output criticality string
"""
def run_workflow1():
    data1 = extract_csv_rows('data1.csv')
    data2 = extract_csv_rows('data2.csv')
    weights = extract_weights_csv_rows('weights.csv')
    results = calculate_weighted_data(data1, data2, weights)

    critical = 0
    for i in results:
        if i > 5:
            critical += 1
    if critical == 1:
        return "criticality: 1 result above 5"
    else:
        return f"criticality: {critical}, results above 5"



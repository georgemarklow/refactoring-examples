import numpy as np
from workflow_reader import *
 
"""
Runs workflow 2.

@return: output d-index string
"""
def run_workflow2():
    data1 = extract_csv_rows('samples1.csv')
    data2 = extract_csv_rows('samples2.csv')
    weights = extract_weights_csv_rows('weights.csv')
    results = calculate_weighted_data(data1, data2, weights)
    mean = np.mean(results)

    return f"d-index: {mean}"

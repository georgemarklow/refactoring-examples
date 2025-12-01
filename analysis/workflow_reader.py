
"""
Extract rows from CSV files.

@param file_name: name of CSV file
@return: data from extracted CSV rows
"""
def extract_csv_rows(file_name):
    with open(file_name) as file1:
        lines = file1.readlines()
        data = []
        for line in lines:
            row = []
            for n in line.split(','):
                row.append(float(n.strip()))
            data.append(row)
    return data

"""
Extract row weights from CSV files.

@param file_name: name of weights CSV file
@return: data from extracted CSV weights rows
"""
def extract_weights_csv_rows(file_name):
    with open(file_name) as filew:
        linew = filew.read()
        w = []
        for n in linew.split(','):
            w.append(float(n.strip()))
    return w

"""
Computes weighed sum of two data sources.

@param data1: first data set
@param data2: second data set
@param weights: weights data set
@return: weighted data
"""
def calculate_weighted_data(data1, data2, weights):
    results = []
    for i in range(len(data1)):
        s = 0
        for j in range(len(weights)):
            d = data1[i][j] - data2[i][j]
            s += weights[j] * abs(d)
        results.append(s)
    return results
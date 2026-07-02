# finds_without_lib.py

import time
import sys

def load_csv(filename):
    data = []
    try:
        with open(filename, 'r') as f:
            headers = f.readline().strip().split(',')
            for line in f:
                data.append(line.strip().split(','))
        return headers, data
    except FileNotFoundError:
        print("❌ ERROR: File not found")
        sys.exit(1)

def find_s(data):
    hypothesis = None
    comparisons = 0  # count attribute comparisons

    for row in data:
        if row[-1].lower() == 'yes':
            if hypothesis is None:
                hypothesis = row[:-1]
            else:
                for i in range(len(hypothesis)):
                    comparisons += 1
                    if hypothesis[i] != row[i]:
                        hypothesis[i] = '?'

    return hypothesis, comparisons

# ---- MAIN ----
start_time = time.time()

headers, dataset = load_csv("training_data_10.csv")

n = len(dataset)                 # number of examples
m = len(dataset[0]) - 1          # number of attributes (excluding target)

final_hypothesis, comparisons = find_s(dataset)

end_time = time.time()

print("Final Hypothesis:", final_hypothesis)
print(f"n (examples) = {n}")
print(f"m (attributes) = {m}")
print(f"Total Attribute Comparisons = {comparisons}")
print(f"Time Complexity = O(n × m) = O({n} × {m}) = O({n*m})")
print("Execution Time:", end_time - start_time, "seconds")
print("Space Complexity: O(m)")

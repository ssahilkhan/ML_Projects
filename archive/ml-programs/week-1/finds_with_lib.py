import pandas as pd
import time

df = pd.read_csv("training_data_300.csv")

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

n = X.shape[0]
m = X.shape[1]

comparisons = 0
hypothesis = None

start_time = time.time()

for i in range(len(y)):
    if y[i].lower() == 'yes':
        if hypothesis is None:
            hypothesis = X[i].copy()
        else:
            for j in range(m):
                comparisons += 1
                if hypothesis[j] != X[i][j]:
                    hypothesis[j] = '?'

end_time = time.time()

print("Final Hypothesis:", hypothesis)
print(f"Time Complexity = O(n × m) = O({n} × {m}) = O({n*m})")
print("Actual Comparisons:", comparisons)
print("Execution Time:", end_time - start_time)
print("Space Complexity: O(n × m)")

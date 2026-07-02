# finds_model_performance_pipeline.py

import pandas as pd
import time
import matplotlib.pyplot as plt


datasets = [
    "training_data_10.csv",
    "training_data_100.csv",
    "training_data_300.csv"
]

results = []

def train_find_s(df):
    hypothesis = None
    attributes = df.columns[:-1]

    for _, row in df.iterrows():
        if row['EnjoySport'].lower() == 'yes':
            if hypothesis is None:
                hypothesis = list(row[attributes])
            else:
                for i in range(len(hypothesis)):
                    if hypothesis[i] != row[attributes[i]]:
                        hypothesis[i] = '?'
    return hypothesis, attributes

def predict(row, hypothesis, attributes):
    for i, attr in enumerate(attributes):
        if hypothesis[i] != '?' and row[attr] != hypothesis[i]:
            return 'No'
    return 'Yes'

for file in datasets:
    print(f"\nProcessing {file}")
    df = pd.read_csv(file)

    start_time = time.time()

    # ---- TRAIN ----
    hypothesis, attributes = train_find_s(df)

    TP = FP = TN = FN = 0

    # ---- TEST ----
    for _, row in df.iterrows():
        actual = row['EnjoySport']
        predicted = predict(row, hypothesis, attributes)

        if actual == 'Yes' and predicted == 'Yes':
            TP += 1
        elif actual == 'No' and predicted == 'Yes':
            FP += 1
        elif actual == 'No' and predicted == 'No':
            TN += 1
        elif actual == 'Yes' and predicted == 'No':
            FN += 1

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    precision = TP / (TP + FP) if (TP + FP) else 0
    recall = TP / (TP + FN) if (TP + FN) else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

    end_time = time.time()

    results.append([
        file,
        hypothesis,
        round(accuracy, 3),
        round(precision, 3),
        round(recall, 3),
        round(f1, 3),
        f"O(n × m)",
        round(end_time - start_time, 5)
    ])

# ---- RESULT TABLE ----
result_df = pd.DataFrame(
    results,
    columns=[
        "Dataset",
        "Final Hypothesis",
        "Accuracy",
        "Precision",
        "Recall",
        "F1-Score",
        "Time Complexity",
        "Execution Time (s)"
    ]
)

print("\nFINAL MODEL PERFORMANCE TABLE\n")
print(result_df.to_string(index=False))


metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
values = [accuracy, precision, recall, f1]

plt.figure()
plt.plot(metrics, values, marker='o')
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Model Performance Curve")
plt.grid(True)

plt.show()

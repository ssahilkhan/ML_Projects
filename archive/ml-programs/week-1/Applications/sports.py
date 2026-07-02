import pandas as pd

df = pd.read_csv("sports_weather.csv")
attrs = df.columns[:-1]

# ---- TRAIN FIND-S ----
hyp = None
for _, r in df.iterrows():
    if r['EnjoySport'] == 'Yes':
        hyp = list(r[attrs]) if hyp is None else [
            hyp[i] if hyp[i] == r[attrs[i]] else '?' for i in range(len(hyp))
        ]

# ---- PREDICT + EVALUATE ----
TP = FP = TN = FN = 0
for _, r in df.iterrows():
    pred = "Yes"
    for i,a in enumerate(attrs):
        if hyp[i] != '?' and r[a] != hyp[i]:
            pred = "No"
            break
    actual = r['EnjoySport']
    if actual=="Yes" and pred=="Yes": TP+=1
    elif actual=="No" and pred=="Yes": FP+=1
    elif actual=="No" and pred=="No": TN+=1
    elif actual=="Yes" and pred=="No": FN+=1

def evaluate_metrics(TP, FP, TN, FN):
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    precision = TP / (TP + FP) if (TP + FP) else 0
    recall = TP / (TP + FN) if (TP + FN) else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0
    return accuracy, precision, recall, f1


from sklearn.metrics import precision_recall_curve, average_precision_score, precision_score, recall_score, f1_score

# Load and preprocess data
# ... (Assuming 'X_train', 'X_test', 'y_train', 'y_test' are available)

# Train a model (e.g., Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# Get predicted probabilities for positive class
probs = model.predict_proba(X_test)[:, 1]

# Compute precision, recall, and F1-score
precision, recall, thresholds = precision_recall_curve(y_test, probs)
avg_precision = average_precision_score(y_test, probs)
f1 = f1_score(y_test, model.predict(X_test))

# Plot Precision-Recall curve
plt.figure(figsize=(8, 8))
plt.plot(recall, precision, color='darkorange', lw=2, label=f'Precision-Recall curve (AP = {avg_precision:.2f})')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='upper right')
plt.show()

# Save Precision-Recall curve and scores if needed
# ...

# Print precision, recall, and F1-score
print(f"Precision: {precision_score(y_test, model.predict(X_test))}")
print(f"Recall: {recall_score(y_test, model.predict(X_test))}")
print(f"F1-Score: {f1}")

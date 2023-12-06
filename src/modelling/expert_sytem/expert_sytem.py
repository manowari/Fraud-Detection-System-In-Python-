# Define rules for fraud detection (sample rules, you should customize based on your domain knowledge)
def detect_fraud(transaction_data):
    if "unauthorized" in transaction_data.lower():
        return "Fraud Detected: Unauthorized Access"
    elif "high amount" in transaction_data.lower():
        return "Fraud Detected: High Amount Transaction"
    else:
        return "No Fraud Detected"

# Example usage
transaction_data = "Unauthorized access attempt in account #123456."
result = detect_fraud(transaction_data)
print(result)

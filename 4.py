import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load the integrated dataset (assumed to be pre-processed)
# Example columns: 'Age', 'PSA', 'Free_PSA', 'F_T_Ratio', 'PSAD', 'PIRADS', 'Gleason_Score'
data = pd.read_csv('integrated_data.csv')

# Define features and target
X = data[['Age', 'PSA', 'Free_PSA', 'F_T_Ratio', 'PSAD', 'PIRADS']]
y = data['Gleason_Score']

# Split the data into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the XGBoost classifier
model = xgb.XGBClassifier(
    objective='multi:softmax',  # Multi-class classification
    num_class=5,  # Assuming Gleason Score classes 7 (1-7, 2-7), 8, 9, 10
    eval_metric='mlogloss',  # Log loss for multi-class classification
    learning_rate=0.01,
    max_depth=6,
    n_estimators=500,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')
print(classification_report(y_test, y_pred, target_names=['1-7', '2-7', '8', '9', '10']))

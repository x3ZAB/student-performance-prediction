import joblib

model = joblib.load("../models/random_forest_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

# new_student = ...

# prediction = model.predict(new_student)

# print(prediction)
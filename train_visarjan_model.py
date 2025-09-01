import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("maharashtra_water_quality.csv")

df = df.dropna()

X = df[["pH", "DO", "BOD", "Turbidity", "TDS"]]
y = df[["SafeForVisarjan"]]

X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train,y_train)
 
with open("visarjan_model.pkl" , "wb") as f:
    pickle.dump(model,f)

print("Model Trained succesfully")
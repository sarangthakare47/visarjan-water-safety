**🌊 Visarjan Water Safety Prediction**
Project Overview

Every year during festivals, idols are immersed (Visarjan) in rivers, lakes, and ponds across India. However, many of these waterbodies are polluted, making them unsafe for immersion and harmful to aquatic life.
This project uses Machine Learning (Random Forest Classifier) to predict whether a waterbody is SAFE or NOT SAFE for Visarjan based on water quality parameters like:

pH,
Dissolved Oxygen (DO),
Biological Oxygen Demand (BOD),
Turbidity,
Total Dissolved Solids (TDS)

The system provides a Streamlit web app where users can:
✅ Select a City and Waterbody
✅ Enter water quality parameters manually (if available)
✅ Get an instant prediction on whether the waterbody is safe for Visarjan

⚙️ Tech Stack

Python 🐍

Pandas & NumPy → Data handling

Scikit-learn → Machine Learning (Random Forest Classifier)

Pickle → Save & load trained ML model

Streamlit → Web app interface

🚀 How to Run

-Clone this repo

git clone https://github.com/yourusername/visarjan-water-safety.git
cd visarjan-water-safety

Install dependencies

pip install -r requirements.txt
Train the model (optional if model already provided)
python train_visarjan_model.py
Run the Streamlit app
streamlit run app.py

👩‍💻 Developed by - Sarang A Thakare

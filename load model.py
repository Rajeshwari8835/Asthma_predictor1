import pickle

# Load Air Quality Model
with open("air.pkl", "rb") as file:
    air_model = pickle.load(file)

print("Air model loaded!")

# Load Weather Model
with open("weather.pkl", "rb") as file:
    weather_model = pickle.load(file)

print("Weather model loaded!")

# Load Patient Model
with open("patient.pkl", "rb") as file:
    patient_model = pickle.load(file)

print("Patient model loaded!")

# Load Final Model (if any)
with open("ML project.pkl", "rb") as file:
    final_model = pickle.load(file)

print("Final model loaded!")
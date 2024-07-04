import numpy as np

# Known pH values
pH_values = np.array([4.0, 7.0, 10.0])

# Connect the A0 pin of NodeMCU ESP8266 to P0 pin of pH Sensor. 
# Get the analog value for 7.0 pH by setting voltage at 4v
# Corresponding analog values from sensor readings
analog_values = np.array([467, 818, 1012])

# Convert analog values to voltages
voltages = analog_values * 5.0 / 1023.0

# Perform linear regression to find the slope and intercept
slope, intercept = np.polyfit(voltages, pH_values, 1)

print("Slope:", slope)
print("Intercept:", intercept)

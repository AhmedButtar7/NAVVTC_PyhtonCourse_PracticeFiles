import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # Create Some Random Data For Your Vehicles
# Weight = np.random.uniform(low=100, high=500, size=1000)
# Colour = np.array(['red', 'blue', 'green', 'yellow', 'black', 'white', 'grey', 'purple', 'radish', 'pink'] * 100)
#
# # Write Data to a Csv File
# df = pd.DataFrame({'Weight': Weight, 'Colour': Colour})
# df.to_csv('random_data_Vehicles.csv', index=False)
# print(df.head())
# print(len(df))
#
# df = pd.read_csv('random_data_Vehicles.csv')
#
#
# # Refer Wheels to the Vehicles according to their Weight
# def wheels(row):  # Maximum Weight is 500, Lowest is 100
#     if row['Weight'] < 220:
#         return 2
#     elif row['Weight'] <= 300:
#         return 3
#     else:
#         return 4
#
#
# df['Wheels'] = df.apply(wheels, axis=1)
# df.to_csv('random_data_Vehicles.csv', index=False)
# print(df.head(), df.tail())
# x = pd.read_csv('random_data_Vehicles.csv')
# print(x)
#
# #Assign Height to the Vehicles
# def height(row):
#     if row['Wheels'] == 2:
#         return np.random.randint(50, 100, size=1)
#     elif row['Wheels'] == 3:
#         return np.random.randint(50, 70, size=1)
#     else:
#         return np.random.randint(1, 50, size=1)
#
#
# df['Height'] = df.apply(height, axis=1)
# df.to_csv('random_data_Vehicles.csv')
# print(df)
# df = pd.read_csv('random_data_Vehicles.csv')
#
#
# #
# #
# # Now Classify The Vehicles according to their weight and wheels
# #
# def classify_vehicle(row):
#     if row['Wheels'] <= 3:
#         if row['Weight'] < 200:
#             return 'Bike'
#         elif row['Weight'] < 300:
#             return 'Bike'
#         else:
#             return 'Unknown'
#     elif row['Wheels'] == 4:
#         if row['Weight'] < 300:
#             return 'Bike'
#         else:
#             return 'Car'
#     else:
#         return 'Unknown'
#
# #
# # Apply the classification function to each row
# df['Classification'] = df.apply(classify_vehicle, axis=1)
# df.to_csv('VehicleClassification.csv')
# print(df.head())
# #
# df = pd.read_csv('VehicleClassification.csv')
#
#
# # Get User Input and Give it's Classification, Get user inputs
# wheels = int(input("Enter the number of wheels: "))
# weight = float(input("Enter the weight (in pounds): "))
# color = input("Enter the color: ")
# height = int(input("Enter the height "))
#
# # Create a new row with user inputs
# new_row = {'Wheels': wheels, 'Weight': weight, 'Colour': color, 'Height': height}
#
# # Append the new row to the DataFrame
# df = df._append(new_row, ignore_index=True)
#
# # Apply the classify_vehicle function
# df['Classification'] = df.apply(classify_vehicle, axis=1)
#
# # Save the updated DataFrame back to the CSV file
# df.to_csv('VehicleClassification', index=False)
#
# print("Data appended and classification complete!")
# print(df.tail())

# Draw Some Graphs of the data
# Load the existing CSV file
existing_csv_path = 'VehicleClassification.csv'
data = pd.read_csv(existing_csv_path)

# Select rows 500 to 999 (excluding row 1000) and plot the 'value' column
data.iloc[99:220].plot(y='Weight', x='Colour')

# Customize the plot (add labels, title, etc.) as needed
plt.xlabel('Colours')
plt.ylabel('Weight ')
plt.title('Plot of Weight of Different Colors Vehicles')

# Show the plot
plt.show()
df = pd.read_csv('VehicleClassification.csv')
plt.xlabel('Classification as Bike & Car')
plt.ylabel('Verify Number of Wheels for Bike & Car')
plt.title('Vehicle Classification Check')
plt.bar(df['Classification'], df['Wheels'])
plt.show()


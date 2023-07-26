import pandas as pd

# Load the races.csv file into a DataFrame
df_races = pd.read_csv('races.csv')

# Filter the data to include records from 2006 to the present
df_filtered = df_races[df_races['year'] >= 2006]

# # Optional: You can print the first few rows of the filtered DataFrame to verify the data
# print(df_filtered.head())

# Load the remaining data files with the filtered data
df_circuits = pd.read_csv('circuits.csv')
df_constructor_results = pd.read_csv('constructor_results.csv')
df_constructor_standings = pd.read_csv('constructor_standings.csv')
df_constructors = pd.read_csv('constructors.csv')
df_driver_standings = pd.read_csv('driver_standings.csv')
df_drivers = pd.read_csv('drivers.csv')
df_lap_times = pd.read_csv('lap_times.csv')
df_pit_stops = pd.read_csv('pit_stops.csv')
df_qualifying = pd.read_csv('qualifying.csv')
df_results = pd.read_csv('results.csv')
# df_seasons = pd.read_csv('seasons.csv')
df_sprint_results = pd.read_csv('sprint_results.csv')
df_status = pd.read_csv('status.csv')

# Replace '\N' with NaN for all DataFrames
dataframes = [df_circuits, df_constructor_results, df_constructor_standings, df_constructors, df_driver_standings, df_drivers, df_lap_times, df_pit_stops, df_qualifying, df_results, df_sprint_results, df_status]

for df in dataframes:
    df.replace('\\N', pd.NA, inplace=True)


# Dropping columns
df_circuits.drop(columns=['circuitRef', 'lat', 'lng', 'alt', 'url'], inplace=True)

# # Display the DataFrame after dropping the columns
# print(df_circuits.head())

# Assuming you have already loaded df_constructor_results DataFrame
df_constructor_results.drop(columns=['status'], inplace=True)

# # Display the DataFrame after dropping the column
# print(df_constructor_results.head())

# Assuming you have already loaded df_constructor_standings DataFrame
df_constructor_standings.drop(columns=['positionText'], inplace=True)

# # Display the DataFrame after dropping the column
# print(df_constructor_standings.head())

# Assuming you have already loaded df_constructors DataFrame
df_constructors.drop(columns=['constructorRef', 'url'], inplace=True)

# Display the DataFrame after dropping the columns
# print(df_constructors.head())

# Assuming you have already loaded df_driver_standings DataFrame
df_driver_standings.drop(columns=['positionText'], inplace=True)

# Display the DataFrame after dropping the column
# print(df_driver_standings.head())

# Assuming you have already loaded df_drivers DataFrame
df_drivers.drop(columns=['code', 'url'], inplace=True)

# Display the DataFrame after dropping the columns
# print(df_drivers.head())

# Assuming you have already loaded df_lap_times DataFrame
df_lap_times.drop(columns=['milliseconds'], inplace=True)

# Display the DataFrame after dropping the column
# print(df_lap_times.head())

# Assuming you have already loaded df_pit_stops DataFrame
df_pit_stops.drop(columns=['time', 'duration', 'milliseconds'], inplace=True)

# Display the DataFrame after dropping the columns
# print(df_pit_stops.head())

# Assuming you have already loaded df_results DataFrame
df_results.drop(columns=['number', 'positionText', 'milliseconds'], inplace=True)

# Display the DataFrame after dropping the columns
# print(df_results.head())

# Assuming you have already loaded df_sprint_results DataFrame
df_sprint_results.drop(columns=['number', 'positionText', 'milliseconds'], inplace=True)

# Display the DataFrame after dropping the columns
# print(df_sprint_results.head())


# Filter out rows for races that occurred after 2006
race_years_after_2006 = df_races[df_races['year'] >= 2006]['raceId'].tolist()

# Create a new DataFrame with only race IDs after 2006
df_results_after_2006 = df_results[df_results['raceId'].isin(race_years_after_2006)]

# Filter the data to include only records related to races after 2006 in other DataFrames
df_constructors = df_constructors[df_constructors['constructorId'].isin(df_results_after_2006['constructorId'])]
df_driver_standings = df_driver_standings[df_driver_standings['raceId'].isin(race_years_after_2006)]
# and so on for other DataFrames

# Also, filter drivers who have raced after 2006 in the df_drivers DataFrame
df_drivers = df_drivers[df_drivers['driverId'].isin(df_results_after_2006['driverId'])]

# Filter the data to include only lap times related to races after 2006
df_lap_times = df_lap_times[df_lap_times['raceId'].isin(race_years_after_2006)]

# Filter the data to include only pit stops related to races after 2006
df_pit_stops = df_pit_stops[df_pit_stops['raceId'].isin(race_years_after_2006)]

# Filter the data to include only qualifying records related to races after 2006
df_qualifying = df_qualifying[df_qualifying['raceId'].isin(race_years_after_2006)]

# Filter the data to include only sprint race results related to races after 2006
df_sprint_results = df_sprint_results[df_sprint_results['raceId'].isin(race_years_after_2006)]

# Filter the data to include only status records related to races after 2006
df_status = df_status[df_status['statusId'].isin(df_results_after_2006['statusId'])]


# Display the DataFrame after applying the filter
# print(df_drivers.head())


# Replace 'cleaned_data_filename.csv' with the desired file name for each DataFrame
df_circuits.to_csv('cleaned_data_circuits.csv', index=False)
df_constructor_results.to_csv('cleaned_data_constructor_results.csv', index=False)
df_constructor_standings.to_csv('cleaned_data_constructor_standings.csv', index=False)
df_constructors.to_csv('cleaned_data_constructors.csv', index=False)
df_driver_standings.to_csv('cleaned_data_driver_standings.csv', index=False)
df_drivers.to_csv('cleaned_data_drivers.csv', index=False)
df_lap_times.to_csv('cleaned_data_lap_times.csv', index=False)
df_pit_stops.to_csv('cleaned_data_pit_stops.csv', index=False)
df_qualifying.to_csv('cleaned_data_qualifying.csv', index=False)
df_results.to_csv('cleaned_data_results.csv', index=False)
df_filtered.to_csv('cleaned_data_races.csv', index=False)
# df_seasons.to_csv('cleaned_data_seasons.csv', index=False)
df_sprint_results.to_csv('cleaned_data_sprint_results.csv', index=False)
df_status.to_csv('cleaned_data_status.csv', index=False)

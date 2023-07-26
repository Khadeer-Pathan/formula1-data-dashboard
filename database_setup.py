from sqlalchemy import create_engine
import pandas as pd


username = 'postgres'
password = 'PostgreSQL'
database_name = 'formula1_dashboard_db'

# Create a connection URL
connection_url = f'postgresql://{username}:{password}@localhost:5432/{database_name}'
# Create the engine
engine = create_engine(connection_url)


# Load the cleaned CSV data into DataFrames
df_circuits = pd.read_csv('cleaned_data_circuits.csv')
df_constructor_results = pd.read_csv('cleaned_data_constructor_results.csv')
df_constructor_standings = pd.read_csv('cleaned_data_constructor_standings.csv')
df_constructors = pd.read_csv('cleaned_data_constructors.csv')
df_driver_standings = pd.read_csv('cleaned_data_driver_standings.csv')
df_drivers = pd.read_csv('cleaned_data_drivers.csv')
df_lap_times = pd.read_csv('cleaned_data_lap_times.csv')
df_pit_stops = pd.read_csv('cleaned_data_pit_stops.csv')
df_qualifying = pd.read_csv('cleaned_data_qualifying.csv')
df_results = pd.read_csv('cleaned_data_results.csv')
df_races = pd.read_csv('cleaned_data_races.csv')
df_sprint_results = pd.read_csv('cleaned_data_sprint_results.csv')
df_status = pd.read_csv('cleaned_data_status.csv')

# Create tables in the database using the DataFrames
df_circuits.to_sql('circuits', engine, index=False, if_exists='replace')
df_constructor_results.to_sql('constructor_results', engine, index=False, if_exists='replace')
df_constructor_standings.to_sql('constructor_standings', engine, index=False, if_exists='replace')
df_constructors.to_sql('constructors', engine, index=False, if_exists='replace')
df_driver_standings.to_sql('driver_standings', engine, index=False, if_exists='replace')
df_drivers.to_sql('drivers', engine, index=False, if_exists='replace')
df_lap_times.to_sql('lap_times', engine, index=False, if_exists='replace')
df_pit_stops.to_sql('pit_stops', engine, index=False, if_exists='replace')
df_qualifying.to_sql('qualifying', engine, index=False, if_exists='replace')
df_results.to_sql('results', engine, index=False, if_exists='replace')
df_races.to_sql('races', engine, index=False, if_exists='replace')
df_sprint_results.to_sql('sprint_results', engine, index=False, if_exists='replace')
df_status.to_sql('status', engine, index=False, if_exists='replace')

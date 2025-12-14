import inspect
import utils.preprocess as pp

print("IMPORT PATH:", inspect.getfile(pp))

from utils.preprocess import load_crime_data, clean_crime_data

# Use default path (DO NOT override)
df = load_crime_data()

print("Raw Data:")
print(df.head())

df_clean = clean_crime_data(df)
print("\nClean Data:")
print(df_clean.head())

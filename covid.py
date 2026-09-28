# ============================================================
# GLOBAL CORONA PANDEMIC ANALYSIS MINI PROJECT
# UNIT 44
# ============================================================

# Import NumPy
import numpy as np

# Import Pandas
import pandas as pd

# Import datetime
import datetime

# Import Matplotlib
import matplotlib.pyplot as plt

# Import specific date/time classes
from datetime import date, datetime, time, timezone


# ============================================================
# STEP 1: PREPARE THE DATA
# ============================================================

# Read the COVID vaccination CSV file
df = pd.read_csv(
    "covid-vaccination-doses-per-capita.csv"
)


# Check the technical summary of the data
df.info()


# Convert Day column into datetime
df["Date"] = pd.to_datetime(df["date"])


# Change the index to the Date column
df.set_index("Date", inplace=True)


# Delete the unnecessary Day column
df.drop(
    "Day",
    axis=1,
    inplace=True
)


# Check the first five rows
print(df.head())


# ============================================================
# STEP 1: CHECK NUMBER OF COUNTRIES
# ============================================================

# Find the number of unique countries
print(
    len(df["Entity"].unique())
)


# ============================================================
# STEP 2: GROUP DATA BY COUNTRY
# ============================================================

# Group the data according to Entity (country)
covid_c = df.groupby(
    ["Entity"]
)



# STEP 2: DISPLAY INFORMATION FOR EACH GROUP


# Go through every country group
for key, group in covid_c:

    # Print the country name
    print("key:", key)

    # Print number of rows for that country
    print("number:", len(group))

    # Print first five rows
    print(group.head())

    # Print blank line
    print("\n")



# STEP 2: CALCULATE CUMULATIVE VALUE


# Calculate the sum of vaccinations per 100 people
# for each country
total_df = covid_c[
    ["total_vaccinations_per_hundred"]
].sum()


# Display the result
print(total_df.head())


# STEP 3: FOLIUM MAP


# Import Folium
import folium



# STEP 3: CREATE A BASIC MAP


# Create a map centered at the given coordinates
m = folium.Map(
    location=[
        37.2549,
        127.0549
    ],

    zoom_start=13,

    tiles="Esri.WorldStreetMap"
)


# Display the map
m



# STEP 3: EXAMPLE MARKER


# Add a marker to the map
folium.Marker(
    location=[
        45.3788,
        -122.6735
    ],

    popup="Example Location",

    icon=folium.Icon(
        color="blue"
    )
).add_to(m)


# Display the map
m


# ============================================================
# STEP 3: CIRCLE EXAMPLE
# ============================================================

# Add a circle to the map
folium.Circle(
    location=[
        45.3800,
        -122.6600
    ],

    radius=100,

    popup="Example Circle",

    color="blue",

    fill=True,

    fill_color="blue"
).add_to(m)


# Display the map
# Save the map as an HTML file
m.save("covid_map.html")

print("Map created successfully!")



# STEP 4: WORLD COVID VACCINATION MAP


# Import JSON
import json


# Center coordinates for world map
center = [
    35.76288735145795,
    84.08313219585636
]


# Create world map
m = folium.Map(

    location=center,

    zoom_start=2,

    max_bounds=True,

    min_zoom=1,

    min_lat=-84,

    max_lat=84,

    min_lon=-175,

    max_lon=187
)


# ============================================================
# LOAD WORLD GEOJSON DATA
# ============================================================

# Location of GeoJSON file\
geo_path = "./data/world_geojson/world_Countries_Generalized.geojson"
    

# Open the GeoJSON file
with open(
    geo_path,
    encoding="utf-8"
) as f:

    json_data = json.load(f)


# ============================================================
# CREATE CHOROPLETH MAP
# ============================================================

folium.Choropleth(

    # Country boundary information
    geo_data=json_data,

    # Our country vaccination data
    data=total_df,

    # DataFrame index and value column
    columns=[
        total_df.index,
        "total_vaccinations_per_hundred"
    ],

    # Match country names
    key_on="properties.COUNTRY",

    # Map color
    fill_color="RdYlGn",

    # Transparency of country color
    fill_opacity=0.7,

    # Transparency of country borders
    line_opacity=0.5

).add_to(m)


# ============================================================
# ADD LAYER CONTROL
# ============================================================

folium.LayerControl().add_to(m)


# ============================================================
# DISPLAY FINAL MAP
# ============================================================

m
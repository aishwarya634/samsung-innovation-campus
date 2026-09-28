import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


population_2024 = {
    "Tokyo": 37115000,
    "Delhi": 33807400,
    "Shanghai": 29867900,
    "Dhaka": 23990000,
    "Cairo": 22623000,
    "Sao Paulo": 22099000,
    "Mexico City": 22585000,
    "Beijing": 21890000,
    "Mumbai": 21673000,
    "Osaka": 18976500,
    "Chongqing": 17739800,
    "Karachi": 17686000,
    "Kinshasa": 17332000,
    "Lagos": 16636000,
    "Istanbul": 16074000,
    "Kolkata": 15576000,
    "Buenos Aires": 15162000,
    "Manila": 14924000,
    "Guangzhou": 14519000,
    "Tianjin": 14079000
}


population_2025 = {
    "Tokyo": 37126000,
    "Delhi": 34665200,
    "Shanghai": 30842100,
    "Dhaka": 24705200,
    "Cairo": 23074200,
    "Sao Paulo": 22999000,
    "Mexico City": 22752400,
    "Beijing": 22655400,
    "Mumbai": 22088000,
    "Osaka": 19251000,
    "Chongqing": 18171200,
    "Karachi": 16907600,
    "Kinshasa": 17775000,
    "Lagos": 17150600,
    "Istanbul": 16337600,
    "Kolkata": 15858000,
    "Buenos Aires": 15732600,
    "Manila": 15236000,
    "Guangzhou": 14877800,
    "Tianjin": 14704100
}


city_area = {
    "Tokyo": 2194,
    "Delhi": 1484,
    "Shanghai": 6341,
    "Dhaka": 306,
    "Cairo": 366,
    "Sao Paulo": 1521,
    "Mexico City": 1495,
    "Beijing": 1641,
    "Mumbai": 603,
    "Osaka": 225,
    "Chongqing": 82403,
    "Karachi": 3780,
    "Kinshasa": 9965,
    "Lagos": 1171,
    "Istanbul": 5343,
    "Kolkata": 286,
    "Buenos Aires": 203,
    "Manila": 43,
    "Guangzhou": 4343,
    "Tianjin": 11966
}


# Convert dictionaries into Series
s_2024 = pd.Series(population_2024)
s_2025 = pd.Series(population_2025)
s_area = pd.Series(city_area)

print(s_2024)
print(s_2025)
print(s_area)
growth = s_2024 - s_2025
print(growth)
population_density = s_2024 / s_area

print(population_density)
x = growth.index
y = growth.values
plt.figure(figsize=(13, 6))

plt.xticks(rotation='vertical', size=10)

plt.barh(x, y)

plt.show()
x = population_density.index
y = population_density.values

plt.figure(figsize=(13, 6))

plt.xticks(rotation=45, size=10)

plt.barh(x, y, color='red')

plt.title('population density', size=15)
plt.ylabel('city', size=15)
plt.xlabel('population', size=15)

plt.show()
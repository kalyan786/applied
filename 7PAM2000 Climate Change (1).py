#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt1
import pandas as pd1
import seaborn as sea   
# Importing the required modules 


# In[2]:


def fun_read(dataset):
    """
    Reads a CSV file and returns two dataframes.

    Parameters:
    -----------
    dataset : str
        The path to the CSV file.

    Returns:
    --------
    dt_name : pandas.DataFrame
        A dataframe with the country names as index and the columns as years.
    dt_data_country : pandas.DataFrame
        A dataframe with the country codes as index and the columns as years.
    """
    dt = pd1.read_csv(dataset, skiprows=4)
   
    dt_data_country = dt.drop(columns=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','Country Code', 'Indicator Code','Unnamed: 66'], inplace=True)
    dt_data_country = dt.set_index('Country Name').T
    dt_name = dt.set_index('Country Name').reset_index()
    return  dt_name, dt_data_country


# In[3]:


# Reading the CSV file
dt_name , dt_data_country = fun_read("who_climate_change.csv")

# Displaying the first five rows of the dt_name dataframe
dt_name.head()


# In[4]:


dt_data_country
# Printing data


# In[5]:


def choose_attribute(indicators, dt):
    """
    Returns a dataframe with the specified indicator.

    Parameters:
    -----------
    indicators : str
        The name of the indicator to select.
    dt : pandas.DataFrame
        The dataframe to select from.

    Returns:
    --------
    dt : pandas.DataFrame
        A dataframe with the specified indicator.
    """
    dt = dt[dt['Indicator Name'].isin([indicators])]
    return dt


# In[6]:


def country_name(country, dt):
    """
    Returns a dataframe with the specified country.

    Parameters:
    -----------
    country : str
        The name of the country to select.
    dt : pandas.DataFrame
        The dataframe to select from.

    Returns:
    --------
    dt : pandas.DataFrame
        A dataframe with the specified country.
    """
    dt = dt[dt['Country Name'].isin([country])]
    dt=dt.set_index("Indicator Name")
    dt=dt.drop("Country Name",axis=1)
    dt=dt.T
    return dt


# In[7]:


# Selecting data for Argentina
Arable_land = country_name('Argentina',dt_name)

# Selecting a subset of columns
total_perc = Arable_land[["Agricultural land (sq. km)", "Population, total", "Arable land (% of land area)",
                          "Agricultural land (sq. km)"]]

# Calculating the correlation matrix
ed = total_perc.corr()


# In[8]:


ax = sea.heatmap(ed, annot=True)
# Generating Heatmap for showing Correlation


# In[9]:


# Selecting data for CO2 emissions from solid fuel consumption (% of total)
co2_solid=choose_attribute("CO2 emissions from solid fuel consumption (% of total)",dt_name)

# Creating a list of countries
countries = ['Afghanistan', 'Bangladesh', 'Aruba', 'Africa Western and Central']

# Selecting data for these countries
co2_solid = co2_solid[co2_solid['Country Name'].isin(countries)]

# Creating a step plot
plt1.step(co2_solid['Country Name'], co2_solid['2015'])

# Rotating x-axis labels
plt1.xticks(rotation=90)

# Setting y-axis label
plt1.ylabel('Population < 1 million')

# Setting title
plt1.title('CO2 emissions from solid fuel consumption (% of total) by Country')

# Displaying plot
plt1.show()


# In[10]:


# Creating a list of countries
countries = ['Pakistan', 'Bangladesh', 'Hungary', 'Africa Western and Central']

# Selecting data for these countries
urban_pop_elevation = dt_name[dt_name['Country Name'].isin(countries)]

# Creating a bar plot
plt1.bar(urban_pop_elevation['Country Name'], urban_pop_elevation['2015'])

# Rotating x-axis labels
plt1.xticks(rotation=90)

# Setting y-axis label
plt1.ylabel('Urban population')

# Setting title
plt1.title('Urban population (% of total population)')

# Displaying plot
plt1.show()


# In[11]:


# Load data
rural_pop_elevation = choose_attribute("Rural population living in areas where elevation is below 5 meters (% of total population)",dt_name)

# Filter data for specific countries
countries = ['Australia', 'United States', 'United Kingdom', 'World']
rural_pop_elevation = rural_pop_elevation[rural_pop_elevation['Country Name'].isin(countries)]

# Create stem plot
plt1.stem(rural_pop_elevation['Country Name'], rural_pop_elevation['2015'])
plt1.xticks(rotation=90)
plt1.ylabel('Rural population (% of total population')
plt1.title('Rural population living in areas where elevation is below 5 meters by Country')
plt1.show()


# In[12]:


# Define countries and indicators
countries = ['Pakistan', 'Bangladesh', 'Hungary', 'Africa Western and Central']
indicators = ['GDP (current US$)', 'Renewable energy consumption (% of total final energy consumption)']

# Filter data based on countries and indicators
df = dt_name[dt_name['Country Name'].isin(countries) & dt_name['Indicator Name'].isin(indicators)]

# Group data by indicator name and calculate mean
df_mean = df.groupby('Indicator Name').mean().reset_index()

# Print mean values
df_mean


# In[13]:


# Defining Countries & Indicators for plotting
countries = ['Pakistan', 'Bangladesh', 'Hungary', 'Africa Western and Central']
indicators = ['GDP (current US$)', 'Renewable energy consumption (% of total final energy consumption)']
df = dt_name[dt_name['Country Name'].isin(countries) & dt_name['Indicator Name'].isin(indicators)]

# Define Mean
df_mean = df.groupby('Indicator Name').mean().reset_index()

# Figure size for plotting
plt1.figure(figsize=(10, 6))

# Calling Mean
gdp_data = df_mean[df_mean['Indicator Name'] == 'GDP (current US$)']
plt1.plot(df['Country Name'], marker='o', label='GDP')

# Giving Labels for the plotted graph
plt1.ylabel('Country')
plt1.xlabel('Value')
plt1.title('GDP and Renewable Energy Consumption by Country')

plt1.legend()

# Calling the Plotting
plt1.show()


# In[ ]:





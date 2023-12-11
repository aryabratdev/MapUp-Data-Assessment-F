#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("dataset-1.csv")
df.head()


# ## Question 1: Car Matrix Generation
# ### Under the function named generate_car_matrix write a logic that takes the dataset-1.csv as a DataFrame. Return a new DataFrame that follows the following rules:
# 
# #### values from id_2 as columns
# #### values from id_1 as index
# #### dataframe should have values from car column
# #### diagonal values should be 0.

# In[8]:


def generate_car_matrix(data):
    # Create a pivot table with id_1 as index, id_2 as columns, and car as values
    matrix = data.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set the diagonal values to 0
    for i in range(min(matrix.shape[0], matrix.shape[1])):
        matrix.iloc[i, i] = 0

    # Reorder columns and index to match the desired output
    matrix = matrix[matrix.columns.sort_values()].sort_index()

    return matrix

# Assuming df is your DataFrame loaded from dataset-1.csv
result = generate_car_matrix(df)

# Print the result
result.head(10)


# ## Question 2: Car Type Count Calculation
# ### Create a Python function named get_type_count that takes the dataset-1.csv as a DataFrame. Add a new categorical column car_type based on values of the column car:
# 
# ### low for values less than or equal to 15,
# ### medium for values greater than 15 and less than or equal to 25,
# ### high for values greater than 25.
# ### Calculate the count of occurrences for each car_type category and return the result as a dictionary. Sort the dictionary alphabetically based on keys.

# In[9]:


def get_car_type(value):
    if value <= 15:
        return 'low'
    elif 15 < value <= 25:
        return 'medium'
    else:
        return 'high'

def get_type_count(data):
    # Add a new column 'car_type' based on the values in the 'car' column
    data['car_type'] = data['car'].apply(get_car_type)

    # Calculate the count of occurrences for each car_type category
    type_count = data['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    type_count = dict(sorted(type_count.items()))

    return type_count

df = pd.read_csv('dataset-1.csv')
result = get_type_count(df)

print(result)


# # Question 3: Bus Count Index Retrieval
# ### Create a Python function named get_bus_indexes that takes the dataset-1.csv as a DataFrame. The function should identify and return the indices as a list (sorted in ascending order) where the bus values are greater than twice the mean value of the bus column in the DataFrame.

# In[10]:


def get_bus_indexes(df) -> list:
    """
    Identifies indices where 'bus' values are greater than twice the mean value.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: A list of indices where 'bus' values are greater than twice the mean.
    """
    # Calculate the mean value of the 'bus' column
    mean_bus = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

result = get_bus_indexes(df)
print(result)


# ## Question 4: Route Filtering
# ### Create a python function filter_routes that takes the dataset-1.csv as a DataFrame. The function should return the sorted list of values of column route for which the average of values of truck column is greater than 7.

# In[11]:


def filter_routes(data):
    # Calculate the average of values in the 'truck' column for each route
    route_avg_truck = data.groupby('route')['truck'].mean()

    # Filter routes where the average of 'truck' column is greater than 7
    filtered_routes = route_avg_truck[route_avg_truck > 7]

    # Get the sorted list of values of the filtered routes
    sorted_filtered_routes = filtered_routes.index.sort_values().tolist()

    return sorted_filtered_routes

result = filter_routes(df)

print(result)


# ## Question 5: Matrix Value Modification
# ### Create a Python function named multiply_matrix that takes the resulting DataFrame from Question 1, as input and modifies each value according to the following logic:
# 
# ### If a value in the DataFrame is greater than 20, multiply those values by 0.75,
# ### If a value is 20 or less, multiply those values by 1.25.
# ### The function should return the modified DataFrame which has values rounded to 1 decimal place.

# In[24]:


def multiply_matrix(input_dataframe):
    # Create a copy of the input DataFrame to avoid modifying the original DataFrame
    modified_dataframe = input_dataframe.copy()
   
    
    modified_dataframe['truck'] = modified_dataframe['truck'].apply(lambda x: round(x * 0.75, 1) if x > 20 else round(x * 1.25))


    # Round the values to 1 decimal place
    modified_dataframe = modified_dataframe.round(1)

    return modified_dataframe

resulting_dataframe = multiply_matrix(df)

resulting_dataframe


# # Question 6: Time Check
# ### You are given a dataset, dataset-2.csv, containing columns id, id_2, and timestamp (startDay, startTime, endDay, endTime). The goal is to verify the completeness of the time data by checking whether the timestamps for each unique (id, id_2) pair cover a full 24-hour period (from 12:00:00 AM to 11:59:59 PM) and span all 7 days of the week (from Monday to Sunday).
# 
# ### Create a function that accepts dataset-2.csv as a DataFrame and returns a boolean series that indicates if each (id, id_2) pair has incorrect timestamps. The boolean series must have multi-index (id, id_2).

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





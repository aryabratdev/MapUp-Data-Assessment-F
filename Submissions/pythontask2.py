#!/usr/bin/env python
# coding: utf-8

# # Python Task 2
# ### Question 1: Distance Matrix Calculation¶
# ### Create a function named calculate_distance_matrix that takes the dataset-3.csv as input and generates a DataFrame representing distances between IDs.
# ### The resulting DataFrame should have cumulative distances along known routes, with diagonal values set to 0. If distances between toll locations A to B and B to C are known, then the distance from A to C should be the sum of these distances. Ensure the matrix is symmetric, accounting for bidirectional distances between toll locations (i.e. A to B is equal to B to A).

# In[1]:


import pandas as pd


# In[3]:


df =pd.read_csv("dataset-3.csv")
df.head()


# In[ ]:





# # Question 2: Unroll Distance Matrix
# ### Create a function unroll_distance_matrix that takes the DataFrame created in Question 1. The resulting DataFrame should have three columns: columns id_start, id_end, and distance.
# 
# ### All the combinations except for same id_start to id_end must be present in the rows with their distance values from the input DataFrame.

# In[4]:


def unroll_distance_matrix(df):
    distance_matrix_reset = df.reset_index()

    # Melt the DataFrame to get 'id_end' and 'distance' columns
    unrolled_df = pd.melt(distance_matrix_reset, id_vars='id_start', var_name='id_end', value_name='distance')

    # Exclude rows where 'id_start' is equal to 'id_end'
    unrolled_df = unrolled_df[unrolled_df['id_start'] != unrolled_df['id_end']]

    # Reset the index of the resulting DataFrame
    unrolled_df.reset_index(drop=True, inplace=True)

    return unrolled_df

result_df = unroll_distance_matrix(df)

result_df.head()


# # Question 3: Finding IDs within Percentage Threshold
# ### Create a function find_ids_within_ten_percentage_threshold that takes the DataFrame created in Question 2 and a reference value from the id_start column as an integer.
# 
# ### Calculate average distance for the reference value given as an input and return a sorted list of values from id_start column which lie within 10% (including ceiling and floor) of the reference value's average.

# In[8]:


def find_ids_within_ten_percentage_threshold(df, reference_value):
    reference_rows = df[df['id_start'] == reference_value]

    # Calculate the average distance for the reference value
    average_distance = reference_rows['distance'].mean()

    # Calculate the threshold values
    lower_threshold = average_distance - (average_distance * 0.10)
    upper_threshold = average_distance + (average_distance * 0.10)

    # Filter rows within the 10% threshold
    within_threshold = df[(df['distance'] >= lower_threshold) & (df['distance'] <= upper_threshold)]

    # Get unique values from the 'id_start' column and sort them
    result_ids = sorted(within_threshold['id_start'].unique())

    return result_ids

reference_value = 1001400  
result_ids = find_ids_within_ten_percentage_threshold(df, reference_value)
print(result_ids)


# # Question 4: Calculate Toll Rate
# ## Create a function calculate_toll_rate that takes the DataFrame created in Question 2 as input and calculates toll rates based on vehicle types.
# 
# ### The resulting DataFrame should add 5 columns to the input DataFrame: moto, car, rv, bus, and truck with their respective rate coefficients. The toll rates should be calculated by multiplying the distance with the given rate coefficients for each vehicle type:
# 
# ### 0.8 for moto
# ### 1.2 for car
# ### 1.5 for rv
# ### 2.2 for bus
# ### 3.6 for truck

# In[7]:


def calculate_toll_rate(df):
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    # Calculate toll rates for each vehicle type
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        column_name = f'{vehicle_type}_rate'
        df[column_name] = df['distance'] * rate_coefficient

    return df
result_df_with_rates = calculate_toll_rate(df)

result_df_with_rates.head(5)


# # Question 5: Calculate Time-Based Toll Rates
# ## Create a function named calculate_time_based_toll_rates that takes the DataFrame created in Question 3 as input and calculates toll rates for different time intervals within a day.
# 
# ### The resulting DataFrame should have these five columns added to the input: start_day, start_time, end_day, and end_time.
# 
# ### start_day, end_day must be strings with day values (from Monday to Sunday in proper case)
# ### start_time and end_time must be of type datetime.time() with the values from time range given below.
# ### Modify the values of vehicle columns according to the following time ranges:
# 
# ### Weekdays (Monday - Friday):
# 
# ### From 00:00:00 to 10:00:00: Apply a discount factor of 0.8
# ### From 10:00:00 to 18:00:00: Apply a discount factor of 1.2
# ### From 18:00:00 to 23:59:59: Apply a discount factor of 0.8
# ### Weekends (Saturday and Sunday):
# 
# ### Apply a constant discount factor of 0.7 for all times.
# ### For each unique (id_start, id_end) pair, cover a full 24-hour period (from 12:00:00 AM to 11:59:59 PM) and span all 7 days of the week (from Monday to Sunday).

# In[12]:


from datetime import time
def calculate_discount_factor(row):
    # Define time ranges and corresponding discount factors
    time_ranges = [
        (time(0, 0, 0), time(10, 0, 0), 0.8),
        (time(10, 0, 0), time(18, 0, 0), 1.2),
        (time(18, 0, 0), time(23, 59, 59), 0.8)
    ]

    # Check if the time falls within any of the defined ranges
    for start, end, factor in time_ranges:
        
        if start <= row['start_time'] <= end and start <= row['end_time'] <= end:
            return factor


# In[ ]:





# In[ ]:





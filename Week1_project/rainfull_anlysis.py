import numpy as np

rainfall_array=np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
# Print the total rainfall for the week.
def print_total_rainfall():
    result=rainfall_array.sum()
    print(f"The total rainfall for the week is {result:.2f} mm")

# Print the average rainfall for the week.
def print_average_rainfall():
    result=np.mean(rainfall_array)
    print(f"The average rainfall for the week is {result:.2f} mm")

# Count how many days had no rain (0 mm).
def count_noraindays():
    result=np.where(rainfall_array==0)[0]
    count=len(result)
    print(f"The count of rainfall for the week is {count}")
    
# Print the days (by index) where the rainfall was more than 5 mm.
def count_rainday_index():
    result=np.where(rainfall_array>5)[0]
    print(f"The index of rainfall days more than 5 is {result}")

# Calculate the 75th percentile of the rainfall data and identify values above it. (help : use numpy.percentile())
def calculate_percentile():
    pecentile_num =np.percentile(rainfall_array,75)
    above_value= np.where(rainfall_array>pecentile_num)[0]
    print(f"The above values are {rainfall_array[above_value]}")

if __name__=="__main__":

    # pint rainfall array
    print_result=np.array2string(rainfall_array,precision=1, separator=", ")
    print(f"the rainfull array is:{print_result}")

    # Print the total rainfall for the week.
    print_total_rainfall()

    # Print the average rainfall for the week.
    print_average_rainfall()

    # Count how many days had no rain (0 mm).
    count_noraindays()

    # Print the days (by index) where the rainfall was more than 5 mm.
    count_rainday_index()

    # Calculate the 75th percentile of the rainfall data and identify values above it.
    calculate_percentile()
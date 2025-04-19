"""
Task 2.2
    This program provides a function to analyze a list of temperatures and compute
    statistical measures such as mean, median, standard deviation, and variance.
    Functions:
        analyze_temperatures(temps):
            Analyzes a list of temperatures and returns a dictionary containing
            statistical measures. Prints an error message if the input list is empty.
            Args:
                temps (list of float): A list of temperature values.
            Returns:
                dict: A dictionary containing the following keys:
                    - 'mean': The mean (average) of the temperatures.
                    - 'median': The median of the temperatures.
                    - 'standard deviation': The standard deviation of the temperatures.
                    - 'variance': The variance of the temperatures.
                Returns None if the input list is empty.
            Raises:
                None.
            Notes:
                - If the input list contains only one temperature, the standard deviation
                and variance are set to 0.
"""
import statistics

def analyze_temperatures(temps):
    if(len(temps) == 0):
        print("Temperature list cannot be empty")
        return None
    statistics = {}
    statistics['mean']=statistics.mean(temps)
    statistics['median']=statistics.median(temps)
    if(len(temps)==1):
        statistics['standard deviation']=0
        statistics['variance'] = 0
    else:
        statistics['standard deviation']=statistics.stdev(temps)
        statistics['variance'] = statistics.variance(temps)
    return statistics

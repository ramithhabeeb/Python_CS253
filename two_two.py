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


"""

Task: 3

This program generates a dataset using mathematical functions and visualizes it using various plots.
Modules:
    - numpy: For numerical operations and random number generation.
    - matplotlib.pyplot: For creating visualizations.
Functions:
    - function_apply(x, function): Applies a specified mathematical function to the input x.
    - generate_dataset(N, x_min, x_max): Generates a dataset of size N with x values in the range [x_min, x_max] 
      and computes corresponding y values using random mathematical functions.
    - plot_scatter(X, Y): Creates a scatter plot of the dataset.
    - plot_histogram(X): Creates a histogram of the x values.
    - plot_box(Y): Creates a box plot of the y values.
    - plot_line(X, Y): Creates a line plot of the dataset with sorted x values.
    - set_random_seed(seed): Sets the random seed for reproducibility.
Usage:
    - The script prompts the user to input the number of samples (N), the minimum value for x (x_min), 
      and the maximum value for x (x_max).
    - It validates the inputs and generates a dataset.
    - The dataset is visualized using scatter, histogram, box, and line plots.
Notes:
    - The script ensures that the random seed is set for reproducibility.
    - If x_min > 0, the logarithmic function is included in the possible functions for generating y values.
    - The script exits with an error message if invalid inputs are provided.
Example:
    Run the script and provide the following inputs:
        Enter the number of samples: 100
        Enter the minimum value for x: 0
        Enter the maximum value for x: 10
    The script will generate a dataset and display the corresponding plots.
"""

import numpy as np
import matplotlib.pyplot as plt

def function_apply(x,function):
    if(function=='sin'):
        return np.sin(x)
    elif(function=='cos'):
        return np.cos(x)
    elif(function=='tan'):  
        return np.tan(x)
    elif(function=='square'):
        return np.square(x)
    elif(function=='cube'):
        return np.power(x, 3)
    elif(function=='log'):
        return np.log(x)

def generate_dataset(N, x_min, x_max):
    x = np.random.uniform(x_min, x_max, N)
    coeff = np.random.rand(6)
    all_functions=['sin', 'cos', 'tan','square', 'cube']
    if(x_min>0):
        all_functions.append('log')
    functions = np.random.choice(all_functions, 3, replace=False)
    y=0
    for i in range(3):
        y+=coeff[2*i]*function_apply(coeff[2*i+1]*x, functions[i])
    return (x,y)

def plot_scatter(X, Y):
    plt.scatter(X, Y, color='blue', label='Data Points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot of Generated Data')
    plt.legend()
    plt.show()
def plot_histogram(X):
    plt.hist(X, bins=30, color='green', alpha=0.7, label='Histogram of X')
    plt.xlabel('X-axis')
    plt.ylabel('Frequency')
    plt.title('Histogram X')
    plt.legend()
    plt.show()

def plot_box(Y):
    plt.boxplot(Y, vert=False)
    plt.xlabel('Y-axis')
    plt.title('Box Plot of Y')
    plt.show()
def plot_line(X,Y):
    sorted_X=np.sort(X)
    plt.plot(sorted_X, Y, color='red', label='Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Plot of Generated Data with sorted X')
    plt.legend()
    plt.show()

def set_random_seed(seed):
    np.random.seed(seed)
    print(f"Random seed set to: {seed}")



if __name__ == "__main__":
    set_random_seed(0)
    N = int(input("Enter the number of samples: "))
    if N <= 0:
        print("Invalid number of samples. Exiting.")
        exit(1)
    x_min = float(input("Enter the minimum value for x: "))
    x_max = float(input("Enter the maximum value for x: "))
    if x_min >= x_max:
        print("Invalid range for x. Exiting.")
        exit(1)
    X, Y = generate_dataset(N, x_min, x_max)
    
    plot_scatter(X, Y)
    plot_histogram(X)
    plot_box(Y)
    plot_line(X,Y)


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


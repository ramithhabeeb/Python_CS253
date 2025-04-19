# Python_CS253


# Task 1.1 - `one_one.py`

## Smart Text-Processing Tool

This program processes a registration number and a content string based on specific rules.  
It is designed to assist writers, poets, and journalists in formatting their content efficiently.  
The tool dynamically processes the input based on the registration number and content string.

---

## Features

1. **Even Registration Number**  
   - Reverses the content string to reflect a "mirror perspective."

2. **Odd Registration Number**  
   - Converts vowels to uppercase and consonants to lowercase for poetic emphasis.

3. **Word Pattern Extraction**  
   - Determines substring length `k` based on the number of 1s in the binary representation of the registration number.  
   - Extracts all substrings of length `k` from the content string.

4. **Lexicographical Ordering for Clarity**  
   - Sorts substrings lexicographically if the bitwise AND between the registration number and the string length is zero.  
   - Otherwise, lists substrings in reverse order for artistic effect.

---

## Functions

### `validate_input(n, s)`

Validates the input values for the registration number and content string.

- **Args**:
  - `n (int)`: Registration number (must be a positive integer).
  - `s (str)`: Content string (must be alphabetic and non-empty).
- **Returns**:
  - `int`: 1 if inputs are valid, 0 otherwise.

---

### `process_string(n, s)`

Processes the content string based on the parity of the registration number.

- **Args**:
  - `n (int)`: Registration number.
  - `s (str)`: Content string.
- **Returns**:
  - `str`: Processed string. Reversed if `n` is even, or vowels uppercased and consonants lowercased if `n` is odd.

---

### `count_set_bits(n)`

Counts the number of set bits (1s) in the binary representation of the registration number.

- **Args**:
  - `n (int)`: Registration number.
- **Returns**:
  - `int`: Count of set bits.

---

### `extract_substrings(s, k)`

Extracts all substrings of length `k` from the given string.

- **Args**:
  - `s (str)`: Content string.
  - `k (int)`: Length of substrings to extract.
- **Returns**:
  - `list`: List of substrings of length `k`.

---

### `sort_or_reverse(n, s, substrings)`

Sorts or reverses the list of substrings based on a bitwise condition.

- **Args**:
  - `n (int)`: Registration number.
  - `s (str)`: Processed content string.
  - `substrings (list)`: List of substrings.
- **Returns**:
  - `list`: Sorted or reversed list of substrings.

---

### `main()`

Main function to handle user input, process the data, and display results.  
Continuously prompts the user for input until they choose to exit.


# Task 1.2 - one_two.py

This program simulates a **Rock-Paper-Scissors** game between a human player and the computer.

---

## Rules of the Game

- Rock beats Scissors.  
- Scissors beats Paper.  
- Paper beats Rock.

---

## Features

The program allows the user to:

1. Input their choice (**Rock**, **Paper**, or **Scissors**).
2. Play multiple rounds until they decide to quit by typing `'Quit'`.
3. View the choices of both the user and the computer for each round.
4. See the total score (**wins**, **losses**, and **ties**) after each round.

---

## Program Ensures

- **Case-insensitive input** handling.
- Handling of **invalid inputs** with appropriate prompts.
- **Random choice generation** for the computer using the `random` module.


# Task 2.1 - two_two.py

This program contains a function to calculate the sum of the first `n` prime numbers.

## Functions

### `sum_of_primes(n)`

Calculates the sum of the first `n` prime numbers.

#### Args

- `n` (`int`): The number of prime numbers to sum.

#### Returns

- `int`: The sum of the first `n` prime numbers.

#### Algorithm

1. Use the Sieve of Eratosthenes to generate a list of prime numbers.
2. Overestimate the range of numbers to ensure at least `n` primes are found.
3. Sum the first `n` primes from the generated list.

#### Notes

- The range for the sieve is overestimated as `15 * n` to ensure enough primes are generated.
- The algorithm assumes `n` is a positive integer.
- The function may not be efficient for very large values of `n` due to the overestimation and memory usage.



# Task 2.2 - two_two.py

This program provides a function to analyze a list of temperatures and compute statistical measures such as mean, median, standard deviation, and variance.

## Functions

### `analyze_temperatures(temps)`

Analyzes a list of temperatures and returns a dictionary containing statistical measures. Prints an error message if the input list is empty.

#### Args

- `temps` (list of float): A list of temperature values.

#### Returns

- `dict`: A dictionary containing the following keys:
    - `'mean'`: The mean (average) of the temperatures.
    - `'median'`: The median of the temperatures.
    - `'standard deviation'`: The standard deviation of the temperatures.
    - `'variance'`: The variance of the temperatures.
- Returns `None` if the input list is empty.

#### Raises

- None.

#### Notes

- If the input list contains only one temperature, the standard deviation and variance are set to 0.


# Task 2.3 - two_three.py

This program provides a function to solve a system of linear equations using NumPy.

## Functions

### `solve_linear_system(A, B)`

Solves the linear system Ax = B, where A is the coefficient matrix and B is the constant matrix/vector. Handles cases where the matrix is singular or not square.

#### Parameters

- `A` (`numpy.ndarray`): A 2D array representing the coefficient matrix.
- `B` (`numpy.ndarray`): A 1D or 2D array representing the constant matrix/vector.

#### Returns

- `numpy.ndarray` or `None`: The solution vector/matrix if the system is solvable, or `None` if the matrix is singular or not square.

#### Raises

- `np.linalg.LinAlgError`: If the matrix A is singular or not square.


# Task 3 - three.py

This program generates a dataset using mathematical functions and visualizes it using various plots.

## Modules

- `numpy`: For numerical operations and random number generation.
- `matplotlib.pyplot`: For creating visualizations.

## Functions

- `function_apply(x, function)`: Applies a specified mathematical function to the input `x`.
- `generate_dataset(N, x_min, x_max)`: Generates a dataset of size `N` with `x` values in the range [`x_min`, `x_max`] and computes corresponding `y` values using random mathematical functions.
- `plot_scatter(X, Y)`: Creates a scatter plot of the dataset.
- `plot_histogram(X)`: Creates a histogram of the `x` values.
- `plot_box(Y)`: Creates a box plot of the `y` values.
- `plot_line(X, Y)`: Creates a line plot of the dataset with sorted `x` values.
- `set_random_seed(seed)`: Sets the random seed for reproducibility.

## Usage

- The script prompts the user to input the number of samples (`N`), the minimum value for `x` (`x_min`), and the maximum value for `x` (`x_max`).
- It validates the inputs and generates a dataset.
- The dataset is visualized using scatter, histogram, box, and line plots.

## Notes

- The script ensures that the random seed is set for reproducibility.
- If `x_min > 0`, the logarithmic function is included in the possible functions for generating `y` values.
- The script exits with an error message if invalid inputs are provided.

## Example

Run the script and provide the following inputs:
```
Enter the number of samples: 100
Enter the minimum value for x: 0
Enter the maximum value for x: 10
```


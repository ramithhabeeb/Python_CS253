"""
Task 1.1
    Smart Text-Processing Tool
    This program processes a registration number and a content string based on specific rules.
    It is designed to assist writers, poets, and journalists in formatting their content efficiently.
    The tool dynamically processes the input based on the registration number and content string.

    Features:
        1. Even Registration Number:
            - Reverses the content string to reflect a "mirror perspective."
        2. Odd Registration Number:
            - Converts vowels to uppercase and consonants to lowercase for poetic emphasis.
        3. Word Pattern Extraction:
            - Determines substring length `k` based on the number of 1s in the binary representation of the registration number.
            - Extracts all substrings of length `k` from the content string.
        4. Lexicographical Ordering for Clarity:
            - Sorts substrings lexicographically if the bitwise AND between the registration number and the string length is zero.
            - Otherwise, lists substrings in reverse order for artistic effect.

    Functions:
        validate_input(n, s):
            Validates the input values for the registration number and content string.
            Args:
                n (int): Registration number (must be a positive integer).
                s (str): Content string (must be alphabetic and non-empty).
            Returns:
                int: 1 if inputs are valid, 0 otherwise.

        process_string(n, s):
            Processes the content string based on the parity of the registration number.
            Args:
                n (int): Registration number.
                s (str): Content string.
            Returns:
                str: Processed string. Reversed if `n` is even, or vowels uppercased and consonants lowercased if `n` is odd.

        count_set_bits(n):
            Counts the number of set bits (1s) in the binary representation of the registration number.
            Args:
                n (int): Registration number.
            Returns:
                int: Count of set bits.

        extract_substrings(s, k):
            Extracts all substrings of length `k` from the given string.
            Args:
                s (str): Content string.
                k (int): Length of substrings to extract.
            Returns:
                list: List of substrings of length `k`.

        sort_or_reverse(n, s, substrings):
            Sorts or reverses the list of substrings based on a bitwise condition.
            Args:
                n (int): Registration number.
                s (str): Processed content string.
                substrings (list): List of substrings.
            Returns:
                list: Sorted or reversed list of substrings.

        main():
            Main function to handle user input, process the data, and display results.
            Continuously prompts the user for input until they choose to exit.
"""
def validate_input(n, s):
    if not isinstance(n, int) or n <= 0:
        return 0
    if not isinstance(s, str) or not s.isalpha() or len(s) == 0:
        return 0
    return 1

def process_string(n, s):
    if n%2==0:
        s = s[::-1]
    else:
        s = ''.join([s[i].upper() if s[i] in ['a', 'e', 'i', 'o', 'u'] else s[i].lower() for i in range(len(s))])
    return s

def count_set_bits(n):
    count =0
    while n:
        if(n%2==1):
            count+=1
        n=n//2
    return count

def extract_substrings(s, k):
    substrings = []
    for i in range(len(s) - k + 1):
        substrings.append(s[i:i+k])
    return substrings

def sort_or_reverse(n, s, substrings):
    if n&len(s)==0:
        substrings.sort()
    else:
        substrings.reverse()
    return substrings

def main():
    while 1:
        n = int(input("Enter registration number: "))
        s = input("Enter content string (letters only): ")
        if validate_input(n, s) == 0:
            print("Invalid input. Please try again.")
            continue
        s= process_string(n, s)
        k= count_set_bits(n)
        substrings = extract_substrings(s, k)
        substrings = sort_or_reverse(n, s, substrings)
        print("Substrings:", substrings)
        cont = input("Process another? (y/n): ").lower()
        if cont != 'y':
            break

main()



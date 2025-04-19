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



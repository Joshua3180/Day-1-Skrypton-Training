def is_palindrome(s):
    return s == s[::-1]

    s= ''.join(e.lower() for e in s 
                     if e. isalnum())
                      
        # Removs non-alphanumeric characters and converting to lowercase and apudu checks if the string is equal to its reverse or not
        # Konni Examples: racecar, level, madam, refer, pop, bob, rotor, noon, tenet, radar, .....

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")

"""
Problem Statement
Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:

a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.
"""

def b_rule_check(string,  index):
    if len(string) == index or string[index] != 'b':
        return False

    index += 1

    if len(string) == index:
        return True
    elif string[index] == 'a':
        return a_rule_check(string, index + 1)        
    
    return False

def a_rule_check(string, index):
    if len(string) == index:
        return True
    elif string[index] == 'a':
        return a_rule_check(string, index+1)
    elif string[index] == 'b':
        return b_rule_check(string, index+1)
    
    return False

def string_check(string: str, i = 0) -> bool:
    if string[0] != 'a':
        return 'false'
    
    if a_rule_check(string, i+1):
        return 'true'
    
    return 'false'

string = input("Enter string: ")
print(string_check(string))

# Output the integer number indicating the total number of occurrences of the substring in the original string.

def count_substring(string, sub_string):
    c = 0
    while len(string) != len(sub_string) - 1:
        if sub_string == string[:len(sub_string)]:
            c += 1
        string = string[1:]

    return c

count_substring("ABCDCDC", "CDC"):

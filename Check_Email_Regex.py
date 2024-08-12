# a-z
# 0-9
# . _ time 1
# @ time 1
# . 2,3

# ^ asserts the start of the string
# [a-z]+ matches one or more lowercase letters
# [\._]? allows for an optional dot (.) or underscore (_)
# [a-z 0-9]+ matches one or more lowercase letters or digits
# [@] matches the literal @ symbol.
# \w+ matches one or more word characters (letters, digits, or underscores).
# [.] matches the literal dot (.).
# \w{2,3} matches exactly 2 or 3 word characters (for the domain extension).


import re

# email_condition = "^[a-z]+[\\._]?[a-z 0-9]+[@]\\w+[.]\\w{2,3}$"
email_condition = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input('Enter your Email: ')

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")

    # """The issue with your regular expression is that the backslash \ is being treated as 
    # an escape character within the string, which leads to the invalid escape sequence warning.
    # To fix this, you can either escape the backslash itself by using a double backslash (\\) 
    # or use a raw string by prefixing the string with an r. Here’s the corrected versio"""
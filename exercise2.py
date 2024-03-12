import re
# Develop a regular expression to validate a username. The username should start with a letter,
# followed by any combination of letters, numbers, underscores, and dots. It should be between 3 and 16 characters long
# Ex. 1
# username = "CodingTemple123"
# Expected Output: True


def check_username(username):
    regex = r'^[a-zA-Z][a-zA-Z0-9._]{3,16}$'
    r = re.compile(regex)

    if re.search(r, username):
        print("Valid")
    else:
        print("Not Valid")


username1 = 'Us3r_name.123'

check_username(username1)

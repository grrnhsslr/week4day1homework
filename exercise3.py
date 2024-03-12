# Using the Python open() function, read in the example.txt file (attached in Google Classroom, make sure it is in
# the same folder as this notebook). Create a pattern that will find all the dates in the text.
# Dates are in the format of YYYY-MM-DD. The pattern should have groups for year, month, and day.
# Using the .finditer() method, iterate over the dates and print in format of month/day/year
import re
from datetime import datetime

file_path = 'example.txt'

# Regular expression to match dates in yyyy-mm-dd format
date_pattern = re.compile(r'\b(\d{4})-(\d{2})-(\d{2})\b')

# Open and read the file
with open(file_path, 'r') as file:
    file_content = file.read()

    # Use finditer to find all matches in the file content
    for match in date_pattern.finditer(file_content):
        year, month, day = match.groups()

        # Convert the numerical month to a month name
        month_name = datetime.strptime(month, "%m").strftime("%B")

        # Print the date in "month day, year" format
        print(f"{month_name} {int(day)}, {year}")

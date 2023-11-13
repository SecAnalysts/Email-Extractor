import re
import sys

# Define a more accurate regular expression pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'

if len(sys.argv) != 2:
    print("Usage: python mail.py input_file")
else:
    input_file_name = sys.argv[1]

    try:
        # Open the input file for reading
        with open(input_file_name, 'r') as input_file:
            text = input_file.read()

        # Use regular expressions to find all email addresses in the text
        email_addresses = re.findall(email_pattern, text)

        with open('result.txt', 'a') as result_file:
            result_file.write("Coded by Sec Analysts\n")
            result_file.write("Extracted {} email addresses from '{}' and appended to 'result.txt'.\n".format(len(email_addresses), input_file_name))

        # Append the email addresses to 'result.txt'
        with open('result.txt', 'a') as result_file:
            for email in email_addresses:
                result_file.write(email + '\n')

        print("Extracted {} email addresses from '{}' and appended to 'result.txt'.".format(len(email_addresses), input_file_name))
    except FileNotFoundError:
        print("Input file '{}' not found. Please make sure the file exists.".format(input_file_name))
    except Exception as e:
        print("An error occurred: " + str(e))

import pyperclip
import re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))            # area code
    (\s|-|\.)                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    phone_num = groups[0]
    matches.append(phone_num)


for groups in email_regex.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print("No phone numbers or emails found.")

#
# phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
#
#
# def is_phone_number(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True
#
#
# print("415-555-4242 is a phone number: ")
# print(is_phone_number('415-555-4242'))
# print('Moshi moshi is a phone number: ')
# print(is_phone_number('Moshi moshi'))
#
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if phone_num_regex.search(chunk):
#         print(f"Phone number found: {chunk}")
# print('done')
#
# mo = phone_num_regex.findall(message)
#
# print(mo)


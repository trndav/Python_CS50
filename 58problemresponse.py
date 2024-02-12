# pip install validator-collection
from validator_collection import validators, checkers, errors

email = input("What's your email address?")

is_email_address = checkers.is_email(email)
if is_email_address is True:
    print("Valid")
else:
    print("Invalid")

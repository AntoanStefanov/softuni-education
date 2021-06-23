from custom_exceptions import NameTooShortError, MustContainAtSymbolError, InvalidDomainError
from helpers import VALID_DOMAINS


def is_email_valid(email):
    try:
        name, domain = email.split('@')
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    try:
        name, extension = domain.split('.')
    except ValueError:
        raise InvalidDomainError(
            "Domain must be one of the following: .com, .bg, .org, .net")

    if extension not in VALID_DOMAINS:
        raise InvalidDomainError(
            "Domain must be one of the following: .com, .bg, .org, .net")

    return True


while True:
    data = input()
    if data == 'End':
        break

    if is_email_valid(data):
        print("Email is valid")

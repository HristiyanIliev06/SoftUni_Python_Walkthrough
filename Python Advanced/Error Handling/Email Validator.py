class NameTooShortError(Exception):
    "Name must be more than 4 characters"
    
class MustContainAtSymbolError(Exception):
    "Email must contain @"
    
class InvalidDomainError(Exception):
    "Domain must be one of the following: .com, .bg, .org, .net"

while True:
    email = input()
    if email=="End": break
    
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    
    parts = email.split('@')
    name = parts[0]
    if len(name)<=4:
        raise NameTooShortError("Name must be more than 4 characters")
    
    more_parts = parts[1].split('.')
    domain = more_parts[1]
    if domain!='com' and domain!='bg' and domain!='net' and domain!='org':
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    
    print("Email is valid")
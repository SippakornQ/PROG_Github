from auth import login
from logic import get_secret, set_secret

password = input("password: ")
if not login(password):
    print("wrong password")
    
else:
    option = input("option (get/set): ")
    key = int(input("key (0-9): "))
if option==set:
    value=int(input())
    set_secret(key, value)
    # TODO: if option is "set", ask for a value and call set_secret
else:
    value=get_secret(key)
    print(value)

    # TODO: otherwise call get_secret and print the value

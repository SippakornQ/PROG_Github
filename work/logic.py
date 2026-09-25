secret = [""] * 10
def set_secret(key, value):
    if key <= 0 or key >= 9:
     secret[key] = value
     pass

def get_secret(key):
   return secret[key]

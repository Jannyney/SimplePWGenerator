import random
import string
characters = string.ascii_letters + string.punctuation  + string.digits
a = int(input("How long is the password do you want?"))
pw = random.sample(characters, a)
print("".join(pw))
import random 
import string 
length=12 
characters = string.ascii_letters + string.digits + string.punctuation 
password = ''.join(random.choice(characters) for 
_ in range(length)) 
print("Randam password:", password)
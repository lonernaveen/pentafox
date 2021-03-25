import random
import string
s=input("Enter name: ")
s=s[::-1].lower()
i=''.join(random.choices(string.ascii_uppercase))
print(i+s)

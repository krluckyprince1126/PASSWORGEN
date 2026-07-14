import string
import random
PASSWORD=string.ascii_letters+string.digits+string.punctuation
digit=7
PASS="".join([random.choice(PASSWORD) for i in range(digit)])
print("YOUR PASSWORD IS  ",PASS)
print()
print("method 2")
gen=""
for i in range (digit):
    gen+=random.choice(PASSWORD)
print("PASSWORD IS  ", gen)
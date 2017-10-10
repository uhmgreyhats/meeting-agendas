import hashlib

with open("rockyou.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

passwords = ['68a96446a5afb4ab69a2d15091771e39', 'ec5f0b1826389df8622133014e88afde', 'e99d20c80a71b463fb44562da0f8817f', '65b5e7ca67533adacc91e48cc7267496', 'db6eb87ac39bc42562fcc1abc506dc34']

for password in content:
    hash = hashlib.md5(password).hexdigest()
    if hash in passwords:
        print password
        print passwords.index(hash)

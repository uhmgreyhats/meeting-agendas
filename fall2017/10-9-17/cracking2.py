import hashlib
import itertools

passwords = ['7bd11faff07d0609adbd87a996b50900', 'd3173a11a624b1a983bfdc532665054c', '7ba290ef53b83d6b60c8ab8897eb269a', 'b26a030a021762c0ddb718c5650b0417', 'e81c0dd1c86b14af1c77ef2d1f09c24c']

words = []

for combination in itertools.product(xrange(10), repeat=4):
    words.append('FLAG-HQNT-' + ''.join(map(str, combination)))

for word in words:
    hash = hashlib.md5(word).hexdigest()
    if hash in passwords:
        print word
        print passwords.index(hash)

# import random
from itertools import chain

#Special characters
spec_chr = [chr(i) for i in chain(range(33,48), range(58, 65), range(91, 97), range(123, 127))]
print(spec_chr)

#Uppercase characters
upp_chr = [chr(i) for i in range(65, 91)]
print(upp_chr)

#Lowercase characters
low_chr = [chr(i) for i in range(97, 123)]
print(low_chr)

#Numbers
num_chr = [chr(i) for i in range(48, 58)]
print(num_chr)
 

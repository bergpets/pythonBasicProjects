import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
symbs = "[]{}()*_-.,/'"
all = lower + upper + nums + symbs
lenght = 16
print("Select mode:")
print("Press 'g' to generate a password")
print("Press 'q' to quit")
while True:
    button = input()
    if button == 'g':
        pswd = "".join(random.sample (all, lenght))
        print(pswd)
    if button == 'q':
        break


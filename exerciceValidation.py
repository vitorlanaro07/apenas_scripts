num = int(-1)
word = str("")
count = int(-1)

while num < 0 or num > 10:
    num = int(input())

while count < 0 or count > 15:
    word = str(input())
    for x in word:
        count += 1

num1 = num*2
print(num1)
print(word)

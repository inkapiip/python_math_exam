from random import randint
number_1 = randint(0, 10)
number_2 = randint(0, 10)
sum = number_1 + number_2
print(str(number_1) + " + " + str(number_2))
answer = input()
if sum == int(answer):
  print("correct!")
else:
  print("wrong!")

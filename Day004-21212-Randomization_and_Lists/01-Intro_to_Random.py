import random

for i in range(10):
  random_integer = random.randint(10,100)
  print("Random Integer:",random_integer)

  random_float = random.random()
  print("Random Float:",random_float)

  random_5 = 5.0*random_float
  print("Random Float b/w 0 and 5:",random_5)

  random_score = random.randint(1,100)
  print(f"Your Score is {random_score}")

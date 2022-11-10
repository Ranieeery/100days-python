import os, time

boolean = True
i = 0

while boolean:
  print("HIGH SCORE TABLE")
  print()
  name = input("INITIALS > ").upper()
  score = input("SCORE > ")
  print()

  f = open("high.score", "a+")
  f.write(f"| {name} | {score} |\n")

  print("ADDED")
  time.sleep(1)
  os.system("clear")
  i += 1
  f.close()

  if i == 3:
    f = open("high.score", "r")
    print(f.read())
    f.close()
    print("END")
    boolean = False
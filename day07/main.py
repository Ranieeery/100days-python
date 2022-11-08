print ("""Are you a fan of 'FMA' or a fake fan?
Answer these questions to find out.
""")

Glasses = input("Does someone wear a plate armor? ")
if Glasses == "yes":
  print("Correct!")
  WhoGlasses = input("And who wears? ")
  if WhoGlasses == "Alphonse":
    print("You got it")
  else:
    print("Try again!")
else:
  print("Wrong!")

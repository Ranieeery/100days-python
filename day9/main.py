birthYear = int(input("What year were you born?"))
if birthYear <= 1946:
  print("Traditionalist")
elif birthYear >= 1947 and birthYear <= 1964:
  print("Baby Boomer")
elif birthYear >= 1965 and birthYear <= 1981:
  print("Gen X")
elif birthYear >= 1982 and birthYear <= 1995:
  print("Millenials")
elif birthYear >= 1996:
  print("Gen Z")
else: 
  print("Invalid year")
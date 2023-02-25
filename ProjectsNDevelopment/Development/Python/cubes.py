single_digits = []
single_digits = range(0,10)
print(single_digits)
squares = []
for item in single_digits:
  print(item)
  squares.append(single_digits[item]**2)

print(squares)
cubes = [item**3 for item in single_digits]
print(cubes)
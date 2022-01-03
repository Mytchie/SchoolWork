input_str = input("Completions Per Attempt")
input_int = int(number_str)

C = ((input_int * 100) - 30) / 20
print(f"C = {C}")

input_str = input("Yards Per Attempt")
input_int = int(number_str)

Y = (input_int * 3) / 4
print(f"Y = {Y}")

input_str = input("Touchdowns Per Attempt")
input_int = int(number_str)

T = (number_int * 20)
print(f"T = {T}")

input_str = input("Completions Per Attempt")
input_int = int(number_str)

I = 2.375 - (input_int * 35)
print(f"I = {I}")



SUM= ((C + Y + T + I) / 6) * 100
print(f"SUM = {SUM}")

# The Goal is to manipulate my data in the given order
# and compare between the imparative and declaritive approaches

# Task 1 Goals
# -------------
# 1 - add one to each value
# 2 - square the result of step 1
# 3 - substract ten from the result of step 2
#
# Task 2 Goals
# ------------
# 4 - in step 3 the input should be only the values less than 20 from step 2 output
#
# Task 3 Goals
# ------------
# 5 - in step 3 the input to substract_ten should be only the
#     smallest 2 values from the step 2 output where the
#     step 2 output is less than 70
# ---------------------------------------------

def add_one(x: float) -> float:
    return x + 1


def square(x: float) -> float:
    return x ** 2


def substract_ten(x: float) -> float:
    return x - 10


my_data = (7, 4, 5, 6, 3, 8, 10)


print('Imparative Method')
# -------------------------
# Task 1 Pythonic Way using List Comprehensions (imparative code)
y = [add_one(val) for val in my_data]
z = [square(val) for val in y]
output = [substract_ten(val) for val in z]
print('Task 1:', output)

# Task 2 Pythonic Was (imparative)
y = [add_one(val) for val in my_data]
z = [square(val) for val in y]
output = [substract_ten(val) for val in z if val <= 20]
print('Task 2:', output)

# Task 2 Pythonic Was (imparative)
y = [add_one(val) for val in my_data]
z = [square(val) for val in y]
temp = [substract_ten(val) for val in z if val <= 70]
output = sorted(temp)[:2]
print('Task 3:', output)
# ---------------------------------------------------


print('Declaritive Method')
# -------------------------
# Task 1 Declaritive Way (Functional Programming)
output = tuple(
    map(substract_ten, (map(square, (map(add_one, my_data))))))
print('Task 1:', output)

# Task 2 Declaritive Way (Functional Programming)
output = tuple(map(substract_ten, filter(
    lambda x: x <= 20, map(square, map(add_one, my_data)))))
print('Task 2:', output)


# Task 2 Declaritive Way (Functional Programming)
output = tuple(sorted(map(substract_ten, filter(
    lambda x: x < 70, map(square, map(add_one, my_data)))))[:2])
print('Task 3:', output)

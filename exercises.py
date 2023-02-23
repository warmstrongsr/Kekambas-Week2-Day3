# Exercise 1 understanding both ways

def negnums(nums):
    negatives = []
    for num in nums:
        if num < 0:
            negatives.append(num)
    return negatives
print(negnums([-100, 534, 32, -15, 77, 222, -788, 345, -75645, 22]))

""""""

def negnums(nums):
    negatives = [num for num in nums if num < 0]
    return negatives
print(negnums([-100, 534, 32, -15, 77, 222, -788, 345, -75645, 22]))

"""================================================================================"""

# Exercise 2
def is_digit(intflt):
    digistr = []
    for i in intflt:
        if i.isdigit():
            digistr.append(i)
    return digistr

print(is_digit("123 Real Street, Apt. 2, Springfield, OR 43498"))


def is_digit(intflt):
    digistr = [int(i) for i in intflt if i.isdigit()]
    return digistr

print(is_digit("123 Real Street, Apt. 2, Springfield, OR 43498"))
print(is_digit("My phone number is (555) 555-4321"))

# Exercise 3

def digits(s):
    n = int(s)
    n += 1
    return str(n)

print(digits('123'))
print(digits('99'))



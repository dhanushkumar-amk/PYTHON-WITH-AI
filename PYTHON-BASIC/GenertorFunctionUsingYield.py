
#  A generator function in Python is a special type of function
#  that returns an iterator object called a generator.
#  Instead of returning all values at once, it yields values one at a time
#  , allowing you to iterate through them lazily (on-demand).


def normal_numbers():
    result = []
    for i in range(5):
        result.append(i)
    return result

# Usage
numbers = normal_numbers()
print(numbers)  # Output: [0, 1, 2, 3, 4]
print(type(numbers))  # Output: <class 'list'>

def generator_numbers():
    for i in range(5):
        yield i

# Usage
numbers = generator_numbers()
print(numbers)  # Output: <generator object generator_numbers at 0x...>
print(type(numbers))  # Output: <class 'generator'>
print(list(numbers))  # Output: [0, 1, 2, 3, 4]
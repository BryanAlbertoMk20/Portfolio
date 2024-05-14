

# def fizzBuzz(n):
#
#     answer = []
#
#     for i in range(n):
#         if i % 3 and i % 5 == 0:
#             answer.append("FizzBuzz")
#         elif i % 3 == 0:
#             answer.append("Fizz")
#         elif i % 5 == 0:
#             answer.append("Buzz")
#         else:
#             answer.append(str(i))
#
#     return answer

def fizzBuzz(n):

    answer = []

    for i in range(1,n+1):


        divisible_by_three = i % 3 == 0
        divisible_by_five = i % 5 == 0

        string = ""

        if divisible_by_three and divisible_by_five:
            answer.append("FizzBuzz")
        elif divisible_by_three:
            answer.append("Fizz")
        elif divisible_by_five:
            answer.append("Buzz")
        else:
            answer.append(str(i))

    return answer

print(fizzBuzz(3))

print(fizzBuzz(5))

print(fizzBuzz(15))


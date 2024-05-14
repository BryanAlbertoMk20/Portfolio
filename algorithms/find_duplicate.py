#O(n^2)
def find_duplicate(numbers):
    duplicate_numbers = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicate_numbers.append(numbers[i])
                print(f"{numbers[i]} is a duplicate")
                break

    print("")
    print(f"These are the duplicated numbers in the list: {duplicate_numbers}")

    return duplicate_numbers

def main():

    numbers = [3,6,2,4,3,6,8,9]

    find_duplicate(numbers)


main()

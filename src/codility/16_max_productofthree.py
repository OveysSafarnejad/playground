from collections import OrderedDict


# O(N)
def solution(numbers: list) -> int:
    counter = OrderedDict()

    # Populate the OrderedDict with counts and negative counts
    for item in numbers:
        abs_item = abs(item)
        if abs_item in counter:
            counter[abs_item][0] += 1
            if item < 0:
                counter[abs_item][1] += 1
        else:
            counter[abs_item] = [1, 1 if item < 0 else 0]

    # Initialize lists to store the largest and smallest values
    largest = []
    smallest = []

    # Extract the three largest absolute values
    for key in sorted(counter.keys(), reverse=True):
        count, neg_count = counter[key]
        for _ in range(count):
            largest.append(key if neg_count == 0 else -key)
            neg_count -= 1
        if len(largest) >= 3:
            break

    # Extract the two smallest absolute values
    for key in sorted(counter.keys()):
        count, neg_count = counter[key]
        for _ in range(count):
            smallest.append(key if neg_count == 0 else -key)
            neg_count -= 1
        if len(smallest) >= 2:
            break

    # Compute the potential maximal products
    max_product_1 = largest[0] * largest[1] * largest[2]
    max_product_2 = smallest[0] * smallest[1] * largest[0]

    return max(max_product_1, max_product_2)


# O(n)

# The product of the three largest elements. OR
# The product of the two smallest elements and the largest element.

# def solution(A):
#     # Initialize variables to track the three largest and two smallest numbers
#     max1 = max2 = max3 = float('-inf')
#     min1 = min2 = float('inf')
#
#     # Iterate through the array to find the top 3 largest and top 2 smallest numbers
#     for number in A:
#         # Update the three largest numbers
#         if number > max1:
#             max3, max2, max1 = max2, max1, number
#         elif number > max2:
#             max3, max2 = max2, number
#         elif number > max3:
#             max3 = number
#
#         # Update the two smallest numbers
#         if number < min1:
#             min2, min1 = min1, number
#         elif number < min2:
#             min2 = number
#
#     # Calculate the maximum product of the triplets
#     max_product_1 = max1 * max2 * max3
#     max_product_2 = min1 * min2 * max1
#
#     # Return the maximum of the two products
#     return max(max_product_1, max_product_2)

# O(NlogN)
# def solution(A):
#     # Sort the array
#     A.sort()
#
#     # The maximum product can either be:
#     # 1. The product of the three largest numbers
#     # 2. The product of the two smallest numbers and the largest number
#     max_product_1 = A[-1] * A[-2] * A[-3]
#     max_product_2 = A[0] * A[1] * A[-1]
#
#     # Return the maximum of the two
#     return max(max_product_1, max_product_2)
if __name__ == '__main__':
    print(solution(numbers=[-5, 5, -5, 4]))

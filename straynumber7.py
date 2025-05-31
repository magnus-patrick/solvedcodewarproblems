"""You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3

DIFFICULTY: 7 kyu

"""


def stray(arr):
    arr.sort()
    if arr[len(arr) - 1] > arr[len(arr) - 2]:
        return arr[len(arr) - 1]
    elif arr[0] < arr[1]:
        return arr[0]

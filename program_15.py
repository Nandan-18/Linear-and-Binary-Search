"""
Write a menu-driven program
to search element either by using Linear or Binary search"""


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def binary_search(arr, low, high, x):
    if high >= 1:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(arr)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


arr = [11, 13, 12, 5, 6]
print(arr)
print('''
    --------------------
    |  SEARCH OPTIONS  |
    --------------------
    | 1. Linear Search |
    | 2. Binary Search |
    --------------------
    ''')
ans = 'y'
while ans == 'y' or ans == 'Y':
    ch = int(input("Enter your choice(1/2): "))

    if ch == 1:
        x = int(input("Enter your search element: "))
        pos = linear_search(arr, x)
        if pos == -1:
            print("The search element not found!")
        else:
            print("The element was found at the position: ", pos + 1)
    elif ch == 2:
        x = int(input("Enter your search element: "))
        print("Sort the elements:-")
        print("1. Insertion sort")
        print("2. Bubble sort")
        ans = 'y'
        while ans == 'y' or ans == 'Y':
            ch = int(input("Enter your choice(1/2): "))
            if ch == 1:
                insertion_sort(arr)
            elif ch == 2:
                bubble_sort(arr)
            else:
                print("Wrong choice!!!")
            break
        pos = binary_search(arr, 0, len(arr) - 1, x)
        if pos != -1:
            print("Element is present at position:", pos + 1, "of sorted array")
        else:
            print("Element is not present in array !")
    else:
        print("Wrong choice!!!")
    ans = str(input("Do you want to continue?(y/n): "))

################################################################################

# OUTPUT#
'''[11, 13, 12, 5, 6]

    --------------------
    |  SEARCH OPTIONS  |
    --------------------
    | 1. Linear Search |
    | 2. Binary Search |
    --------------------
    
Enter your choice(1/2): 1
Enter your search element: 5
The element was found at the position:  4
Do you want to continue?(y/n): y
Enter your choice(1/2): 2
Enter your search element: 12
Sort the elements:-
1. Insertion sort
2. Bubble sort
Enter your choice(1/2): 1
[5, 6, 11, 12, 13]
Element is present at position: 4 of sorted array
Do you want to continue?(y/n): y
Enter your choice(1/2): 2
Enter your search element: 6
Sort the elements:-
1. Insertion sort
2. Bubble sort
Enter your choice(1/2): 2
[5, 6, 11, 12, 13]
Element is present at position: 2 of sorted array
Do you want to continue?(y/n): n
>>> '''

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    new_arr = sorted(arr)
    for idx in range(0, len(new_arr), 2):
        if new_arr[idx] != new_arr[idx + 1] :
            return new_arr[idx]

        

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
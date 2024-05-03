import random

import numpy as np


def load_arrays(file_path):
    try:
        arrays = np.load(file_path, allow_pickle=True)
        return arrays
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def select_random_arrays():
    
    arrays_file1 = load_arrays('arrays_file1.npy')
    arrays_file2 = load_arrays('arrays_file2.npy')

    if arrays_file1.size == 0 or arrays_file2.size == 0:
        print("Error: Unable to load arrays.")
        return None, None

    random_array1 = random.choice(arrays_file1)
    random_array2 = random.choice(arrays_file2)

    return random_array1, random_array2

name = input("Enter your name: ")
score = 0
total_score = 5


for array in range(0,total_score):
    array1, array2 = select_random_arrays()
    if array1 is not None and array2 is not None:
        print("Randomly selected array from arrays_file1.npy:")
        print(array1)
        print("Randomly selected array from arrays_file2.npy:")
        print(array2)
        arr3 = np.dot(array1, array2)
        arr3 = arr3.ravel()
        
        # print(arr3)
        
        user_answer = input("Enter dot product of the matrix seprate by space (answer row wise): ")
        user_answer = np.array(list(map(int, user_answer.split())))
        
        if np.array_equal(arr3, user_answer):
            score += 1

print(f"Player {name} score total of {score}")
with open('player_data.txt', 'a') as file:
    file.write(f"Player Name: {name}\n")
    file.write(f"Score: {score}\n")
    file.write("\n")

import sys

# Function to read all input at once using sys.stdin.read()
def fast_input():
    """
    Reads all input at once and strips trailing whitespace.
    """
    return sys.stdin.read().strip()

# # Reading raw input data
# raw_data = fast_input()

# # Example 1: Handling a single string input
# # -----------------------------------------
# # Suppose the input is: "hello_world"
# single_string = raw_data
# print(f"Single string: {single_string}")
# # Output: Single string: hello_world


# # Example 2: Handling multiple integers (space-separated)
# # --------------------------------------------------------
# # Suppose the input is: "10 20 30 40 50"
# numbers = list(map(int, raw_data.split()))
# print(f"List of integers: {numbers}")
# # Output: List of integers: [10, 20, 30, 40, 50]


# # Example 3: Handling multiple floats (space-separated)
# # ------------------------------------------------------
# # Suppose the input is: "3.14 2.718 1.618 0.577"
# floats = list(map(float, raw_data.split()))
# print(f"List of floats: {floats}")
# # Output: List of floats: [3.14, 2.718, 1.618, 0.577]


# # Example 4: Handling a group of strings (space-separated)
# # ---------------------------------------------------------
# # Suppose the input is: "apple banana cherry mango"
# strings = raw_data.split()
# print(f"List of strings: {strings}")
# # Output: List of strings: ['apple', 'banana', 'cherry', 'mango']


# # Example 5: Handling a dictionary input (key:value pairs space-separated)
# # ------------------------------------------------------------------------
# # Suppose the input is: "name:john age:25 city:paris"
# pairs = dict(item.split(":") for item in raw_data.split())
# print(f"Dictionary: {pairs}")
# # Output: Dictionary: {'name': 'john', 'age': '25', 'city': 'paris'}


# # Example 6: Handling ASCII characters or raw character input
# # -----------------------------------------------------------
# # Suppose the input is: "hello @world! #2024"
# mixed_input = list(raw_data)  # Breaks the string into individual characters
# print(f"List of characters: {mixed_input}")
# # Output: List of characters: ['h', 'e', 'l', 'l', 'o', ' ', '@', 'w', 'o', 'r', 'l', 'd', '!', ' ', '#', '2', '0', '2', '4']



# # Example 7: Handling every character input at once
# # -----------------------------------------------------------
# # Suppose the input is: "hello @world! #2024"
# Single string: hello @world! #2024
# List of integers: []
# List of floats: []
# List of strings: ['hello', '@world!', '#2024']
# Dictionary: {}
# List of characters: ['h', 'e', 'l', 'l', 'o', ' ', '@', 'w', 'o', 'r', 'l', 'd', '!', ' ', '#', '2', '0', '2', '4']

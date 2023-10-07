import ctypes

# Load the shared library
lib = ctypes.CDLL('./libPyList.so')

# Define the argument types for the print_python_list_info function
lib.print_python_list_info.argtypes = [ctypes.py_object]

def print_and_modify_list(l):
    # Print information about the list
    lib.print_python_list_info(l)
    
    # Perform some operations on the list
    l.append("New Element")
    l.pop()
    lib.print_python_list_info(l)

def main():
    # Create and modify a list
    my_list = ['hello', 'World']
    print_and_modify_list(my_list)
    
    # Create and modify another list
    another_list = [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
    print_and_modify_list(another_list)
    
    # Create and modify an empty list
    empty_list = []
    print_and_modify_list(empty_list)

if __name__ == "__main__":
    main()

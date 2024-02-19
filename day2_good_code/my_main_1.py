# `my_main_1.py
# 
import sys

def say_hello_to(name):
    print(f"Hello {name}!")

def main():
    name = sys.argv[1]
    say_hello_to(name)
    print("Program ended.")  
    
if __name__ == "__main__":
    main()
    




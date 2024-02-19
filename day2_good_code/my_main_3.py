# `my_main_3.py
# 
import sys

def say_hello_to(name):
    print(f"Hello {name}!")

def main():
    try:
        name = sys.argv[1]
        say_hello_to(name)
        
        print("Done.")
    except:
        print("Error: No argument")
      
    print("Program ended.")  

if __name__ == "__main__":
    main()
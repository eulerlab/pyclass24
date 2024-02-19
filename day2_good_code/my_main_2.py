# `my_main_2.py
# 
import sys

def say_hello_to(name):
    print(f"Hello {name}!")

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
        say_hello_to(name)
        
        print("Done.")  
    else:
        print("Error: No argument")
    
    print("Program ended.")          

if __name__ == "__main__":
    main()




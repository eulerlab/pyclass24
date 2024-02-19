# `my_main_4.py
# 
import sys

def say_hello_to(name):
    print(f"Hello {name}!")

def main():
    try:
        name = sys.argv[1]
        say_hello_to(name)
        
        val1 = float(sys.argv[2])
        val2 = float(sys.argv[3])
        res = val1 /val2
        print(f"val1/val2={res:.3f}")
        
        print("Done.")
    except IndexError:
        print("Error: No argument")
      
    print("Program ended.")  

if __name__ == "__main__":
    main()
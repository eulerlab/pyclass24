# `my_main_4.py
# 
import sys, os
MyIssue = BaseException("Somehow I expected the file to be there ... ???")

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
        
        f_name = 'nowhere.txt'
        try:
            f = open(f_name)
            print(f.readline())
        except OSError:
            raise MyIssue
        else:   
            f.close
        
        print("Done.")
    except IndexError:
        print("Error: Too few arguments")
    except ZeroDivisionError:
        print("Error: Third argument cannot be zero")
      
    print("Program ended.")  

if __name__ == "__main__":
    main()
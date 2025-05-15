import sys 
from interpreter import BrainfuckInterpreter

def main():
    if len(sys.argv) != 2:
        print ("Expected a Filename: ")
        return

    with open(sys.argv[1]) as f:
        code = f.read()
    
    interpreter = BrainfuckInterpreter(code)
    interpreter.run()



if __name__ == "__main__":
    main()

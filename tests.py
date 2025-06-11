from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

    
    result = run_python_file("calculator", "main.py")
    print(result) 

    result = run_python_file("calculator", "tests.py")
    print(result) 

    result = run_python_file("calculator", "../main.py")
    print(result) 

    result = run_python_file("calculator", "nonexistent.py")
    print(result) 

if __name__ == "__main__":
    test()

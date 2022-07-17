"""
The purpose of this exercise is to introduce the splat operator (*). Specifically when used as a paarameter when invoking a function. 
It allows any number of parameters to be passed.
"""
def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number

    print(output)    
    return output

if __name__ == "__main__":
    mysum(10, 20, 30, 40)
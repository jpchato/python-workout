"""
"""

def hex_output():

    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

if __name__ == '__main__':
    hex_output()
    # returns decimal equivalent and hex_number
"""
The purpose of this exercise is to introduce the splat operator (*). Specifically when used as a paarameter when invoking a function. 
It allows any number of parameters to be passed.
"""
def mysum(*numbers, starting_point=0):
    output = 0
    for number in numbers[starting_point:]:
        output += number
    print(output)    
    return output

def average(numbers: list):
    output = 0
    for number in numbers:
        output += number
    average = output/len(numbers)
    print(average)
    return average

def words(word_list: list):  

    shortest_word, longest_word = len(word_list[0]), len(word_list[0])
    total_chars = 0
    total_chars = 0

    for word in word_list:
        word_length = len(word)
        if word_length > longest_word:
            longest_word = word_length
        if word_length < shortest_word:
            shortest_word = word_length
        total_chars += word_length

    avg_word_length = total_chars/len(word_list)

    word_tuple = (shortest_word, longest_word, avg_word_length)

    print(word_tuple)
    return word_tuple



if __name__ == "__main__":
    mysum(10, 20, 30, 40, starting_point=2)
    average([10, 20, 30, 40])
    words(['a', 'ab', 'abc', 'adcd', 'abcde'])
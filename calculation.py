def calculation(text):
    number1 = ''
    for i in text: 
      if i == ' ': 
        number2 = number1
        number1 = ''
      elif i != ',': 
        number1 = number1 + i
    answer = int(number2) + int(number1)
    return answer

text_1 = input('Please, enter the numbers 1: ')
text_2 = input('Please, enter the numbers 2: ')

answer_1 = calculation(text_1)
answer_2 = calculation(text_2)

print(answer_1)
print(answer_2)

# Example:

# Input:
# 1,234 2,345,678
# -234,567,890 123,456,780

# Output:
# 2346912
# -111111110

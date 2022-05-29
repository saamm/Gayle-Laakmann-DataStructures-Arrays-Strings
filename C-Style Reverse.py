original= "abc\0"
final = "cba\0"

answer = original[:-1]
answer = answer[::-1]
answer = answer + '\0'

print(answer == final)
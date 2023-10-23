# continue statement kinda does the same thing to break but opposite
# The continue statement is typically used in situations where you want to skip some specific iterations but continue with the remaining iterations of the loop.

for number in range(10):
    if number%3 == 0:
        print(number,end="\t")
        print("divisible by 3")
        continue
    print(number," not divisible by 3")
        

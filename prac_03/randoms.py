import random
dir(random)

"""
What did you see on line 1?
14
What was the smallest number you could have seen, what was the largest?
5 16

What did you see on line 2?
3
What was the smallest number you could have seen, what was the largest?
3 9
Could line 2 have produced a 4?
No

What did you see on line 3?
2.812064421148539
What was the smallest number you could have seen, what was the largest?
2.812064421148539 4.241581775352891
"""

random_number = random.randint(1, 100)
print(random_number)
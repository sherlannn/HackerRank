def is_even(num):
    return num % 2 == 0

def score_words(words):
    score = 0
    vowels = 'aeiouy'
    for word in words:
        vowel_count = sum(1 for letter in word if letter in vowels)
        if is_even(vowel_count):
            score += 2
        else:
            score += 1
    return score

# Reading input
n = int(input())
words = input().split()

# Calling the corrected function and printing the result
result = score_words(words)
print(result)

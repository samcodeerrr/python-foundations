# Day 1 basics practice

def is_even(n):
    return n % 2 == 0

print("is_even(10):", is_even(10))

s = "sanskriti"
print("reverse:", s[::-1])

# count vowels
vowels = "aeiou"
count = 0
for ch in s.lower():
    if ch in vowels:
        count += 1
print("vowel count:", count)

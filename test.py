from attandance_pattern import graduation_probability

N = int(input(f"Enter nomber of days to check the graduation probability\n"))
ans = graduation_probability(N)
print(f"prabability of graduation missing is = {ans}")

# print(graduation_probability(5))  # Expected: "14/29"
# print(graduation_probability(10)) # Expected: "372/773"
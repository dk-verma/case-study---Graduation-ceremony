def graduation_probability(N):
    if N < 1:
        return "0/1"
    
    # Initialize arrays for state counts
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    C = [0] * (N + 1)
    D = [0] * (N + 1)
    
    # Initial conditions
    A[0] = 1
    B[0] = 0
    C[0] = 0
    D[0] = 0
    
    for i in range(1, N + 1):
        A[i] = A[i-1] + B[i-1] + C[i-1] + D[i-1]
        B[i] = A[i-1]
        C[i] = B[i-1]
        D[i] = C[i-1]
    
    total_valid = A[N] + B[N] + C[N] + D[N]
    miss_graduation = B[N-1] + C[N-1] + D[N-1]
    
    return f"{miss_graduation}/{total_valid}"

# Test cases
# N = int(input("Enter college days \n"))
# print(graduation_probability(N))  # Expected: "14/29"
# print(graduation_probability(10)) # Expected: "372/773"

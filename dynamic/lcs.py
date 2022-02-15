def LCS(A, B, i, j, stack, m):
    if i == len(A) or j == len(B):
        return 0
    elif A[i] == B[j]:
        stack.append(A[i])

        if f"{i+1}{j+1}" in m:
            return m[f"{i+1}{j+1}"]
        else:
            m[f"{i+1}{j+1}"] = 1 + LCS(A, B, i + 1, j + 1, stack, m)
            return m[f"{i+1}{j+1}"]
    else:
        if f"{i+1}{j}" not in m:
            m[f"{i+1}{j}"] = LCS(A, B, i + 1, j, stack, m)

        if f"{i}{j+1}" not in m:
            m[f"{i}{j+1}"] = LCS(A, B, i, j + 1, stack, m)

        return max(m[f"{i+1}{j}"], m[f"{i}{j+1}"])


stack = []

A = "abcdefghij"
B = "cdgi"

print(LCS(A, B, 0, 0, stack, {}))

print("".join(stack))

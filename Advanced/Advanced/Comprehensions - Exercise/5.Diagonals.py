n = int(input())


matrix = [[int(num) for num in input().split(', ')] for inpt in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - 1 - i]
                      for i in range(n)]
# n - 1 - i втори индекс за втори диагонал

print(
    f"First diagonal: {', '.join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}")

print(
    f"Second diagonal: {', '.join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

def matrix_chain_order(dims):
    """
    Matrix Chain Multiplication using DP
    dims: list of dimensions, matrix i has dims[i-1] x dims[i]
    Time: O(n^3), Space: O(n^2)
    """

    n = len(dims) - 1

    # m[i][j] = minimum multiplications for matrices i..j
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # l is the chain length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + dims[i - 1] * dims[k] * dims[j]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        return f'A{i}'

    k = s[i][j]

    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)

    return f'({left} x {right})'


def print_dp_table(m, n):
    print('\nDP Cost Table m[i][j]:')

    print(f'{"":>6}', end='')

    for j in range(1, n + 1):
        print(f'A{j:>8}', end='')

    print()

    for i in range(1, n + 1):
        print(f'A{i:<5}', end='')

        for j in range(1, n + 1):
            if j < i:
                print(f'{"---":>9}', end='')
            else:
                print(f'{m[i][j]:>9}', end='')

        print()


# Matrix dimensions:
# A1(10x30), A2(30x5), A3(5x60), A4(60x10)

dims = [10, 30, 5, 60, 10]

n = len(dims) - 1

print('Matrix Dimensions:')

for i in range(n):
    print(f' A{i + 1}: {dims[i]} x {dims[i + 1]}')

m, s = matrix_chain_order(dims)

print(f'\nMinimum scalar multiplications: {m[1][n]}')

print(
    f'Optimal parenthesization: '
    f'{print_optimal_parens(s, 1, n)}'
)

print_dp_table(m, n)
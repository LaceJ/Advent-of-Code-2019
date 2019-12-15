def computer(n):
    steps = 0
    while n[0+steps] != 99:
        if n[0+steps] == 1:
            n[n[3+steps]] = n[n[1+steps]] + n[n[2+steps]]
            steps += 4
        elif n[0+steps] == 2:
            n[n[3+steps]] = n[n[1+steps]] * n[n[2+steps]]
            steps += 4
    return n[0]


def solution(n, start, end):
    arr = list(range(start, end))
    for i in range(len(arr)):
        for j in range(len(arr)):
            temp = n[:]
            temp[1] = arr[i]
            temp[2] = arr[j]
            x = computer(temp)
            if x == 19690720:
                res = 100 * arr[i] + arr[j]
                return res


input = [1, 12, 2, 3,
         1, 1, 2, 3,
         1, 3, 4, 3,
         1, 5, 0, 3,
         2, 13, 1, 19,
         1, 19, 10, 23,
         2, 10, 23, 27,
         1, 27, 6, 31,
         1, 13, 31, 35,
         1, 13, 35, 39,
         1, 39, 10, 43,
         2, 43, 13, 47,
         1, 47, 9, 51,
         2, 51, 13, 55,
         1, 5, 55, 59,
         2, 59, 9, 63,
         1, 13, 63, 67,
         2, 13, 67, 71,
         1, 71, 5, 75,
         2, 75, 13, 79,
         1, 79, 6, 83,
         1, 83, 5, 87,
         2, 87, 6, 91,
         1, 5, 91, 95,
         1, 95, 13, 99,
         2, 99, 6, 103,
         1, 5, 103, 107,
         1, 107, 9, 111,
         2, 6, 111, 115,
         1, 5, 115, 119,
         1, 119, 2, 123,
         1, 6, 123, 0,
         99, 2, 14, 0, 0]


x = solution1(input, 1, 101)
print(x)

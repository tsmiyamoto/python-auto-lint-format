def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    a, b = 0, 1
    series = [a, b]
    for _ in range(n - 2):
        a, b = b, a + b
        series.append(b)
    return series

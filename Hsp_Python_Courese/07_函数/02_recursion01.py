def test(n):
    if n > 2:
        test(n - 1)
    print("n=", n)

test(4)

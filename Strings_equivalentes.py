def equiv(a, b):
    if a == b:
        return True
    if len(a) % 2:
        return False
    n = len(a)
    a1 = a[:n//2]
    a2 = a[n//2:]
    b1 = b[:n//2]
    b2 = b[n//2:]
    return (equiv(a1, b2) and equiv(a2, b1)) or (equiv(a1, b1) and equiv(a2, b2))

a = input()
b = input()

print("YES" if equiv(a, b) else "NO")


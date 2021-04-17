for t in range(1, int(input()) + 1):
    n = int(input())
    blocks = [int(x) for x in input().split()]
    res = ['A']
    for i in range(n):
        is_even = (i + 1) % 2 == 0
        if is_even:
            res.extend([chr(c) for c in range(64 + blocks[i], 64, -1)])
        else:
            if i + 1 < n:
                res.extend([chr(c) for c in range(66, 65 + blocks[i])])
                if blocks[i+1] > blocks[i]:
                    res.append(chr(blocks[i+1] - blocks[i] + ord(res[-1]) + 1))
                else:
                    res.append(chr(65 + blocks[i]))
            else:
                res.extend([chr(c) for c in range(66, 66 + blocks[i])])

    print(f"Case #{t}: {''.join(res)}")
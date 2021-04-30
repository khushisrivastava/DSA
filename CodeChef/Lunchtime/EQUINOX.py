# cook your dish here
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    anuradha_point = 0
    sarthak_point = 0

    for i in range(n):
        s = input()
        if s[0] in "EQUINOX": sarthak_point += a
        else: anuradha_point += b
    
    if sarthak_point > anuradha_point:
        print("SARTHAK")
    elif sarthak_point < anuradha_point:
        print("ANURADHA")
    else:
        print("DRAW")
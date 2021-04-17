from collections import Counter

for t in range(1,int(input())+1):
    t = input()
    b = list(t)
    i = 0
    o = 0
    score = 1
    
    if b[0] != "I" and b[-1] != "I":
        score += len(b)
        print(f"Case #{t}: O {score}")
        continue
    if b[0] == "I" and b[-1] == "I" and (b[1] == "I" or b[-2] == "I"):
        score += len(b) - 1
        print(f"Case #{t}: I {score}")
        continue
    
    b = Counter(b)

    if b["I"] == b["O"]:
        print(f"Case #{t}: O {score}")
    if b["I"] - b["O"] == 1 or b["I"] - b["O"] == -1:
        if "OO" in t:
            score += len(t[t.find("O"):t.find("OO")]) +1
            print(f"Case #{t}: O {score}")
            continue
        print(f"Case #{t}: I {score}")
        
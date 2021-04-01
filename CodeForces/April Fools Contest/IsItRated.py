while(True):
    try:
        s = input()
        print("NO", flush=True)
    except EOFError as e:
        quit()
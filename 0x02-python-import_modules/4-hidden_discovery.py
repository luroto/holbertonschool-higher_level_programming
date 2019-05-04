#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    varia = dir(hidden_4)
    totaria = len(varia)
    for i in range(0, totaria):
        if varia[i][1] != "_":
            print("{}".format(varia[i]))

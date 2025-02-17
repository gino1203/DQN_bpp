# -*- coding: utf-8 -*-
"""datagenerate.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17_aUocWFe2_g86FgxIwgqkge4FO79QH3
"""

import random

def random_item_generate(w, h, a, b):
    f=open('data.txt','w')
    cutW = [0] * a
    cutH = [[0] * b for _ in range(a)]

    section = w // a
    for i in range(a-1):
        randn = random.randint(0, section-1)
        cutW[i] = i * section + randn
    cutW[a-1] = w - 1
    print(a*b,file=f)
    section = h // b
    for i in range(a):
        for j in range(b-1):
            randn = random.randint(0, section-1)
            cutH[i][j] = j * section + randn
        cutH[i][b-1] = h - 1

    item = [[[0 for _ in range(w)] for _ in range(h)] for _ in range(a*b)]
    for i in range(a*b):
        nW = i // b
        nH = i % b
        width = cutW[nW] + 1 if nW == 0 else cutW[nW] - cutW[nW-1]
        height = cutH[nW][nH] + 1 if nH == 0 else cutH[nW][nH] - cutH[nW][nH-1]
        for j in range(height):
            for k in range(width):
                item[i][j][k] = 1

    # Check part
    print("Item placement:")
    bin = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(a*b):
        nW = i // b
        nH = i % b
        for j in range(cutH[nW][nH-1]+1 if nH else 0, cutH[nW][nH]+1):
            for k in range(cutW[nW-1]+1 if nW else 0, cutW[nW]+1):
                bin[j][k] = i
    for i in range(h):
        print(" ".join(map(str, bin[i])))

    # Generate size
    size = [[0, 0] for _ in range(a*b)]
    for i in range(a*b):
        nW = i // b
        nH = i % b
        size[i][0] = cutH[nW][nH] - (cutH[nW][nH-1] if nH else -1)
        size[i][1] = cutW[nW] - (cutW[nW-1] if nW else -1)

    # Check sizes
    print("\nSizes:")

    for s in size:
        print(f"{s[0]} {s[1]}",file=f)
        print(f"{s[0]} {s[1]}")
    return item, size

def print_item(item, w, h, a, b):
    for i in range(a*b):
        print(f"Item {i}:")
        for j in range(h):
            print(" ".join(map(str, item[i][j])))
        print()

if __name__ == "__main__":
    w, h, a, b = map(int, input("w, h, a, b: ").split())
    item, size = random_item_generate(w, h, a, b)
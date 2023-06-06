#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i  == 0:
            print(f"{i}{j}", end=", ")
        elif i < j:
            if i * 10 + j < 89:
                print(f"{i}{j}", end=", ")
            else:
                print(f"{i}{j}")

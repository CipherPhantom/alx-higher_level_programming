#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    attributes = dir(hidden_4)

    for index in range(len(attributes)):
        att = attributes[index]
        if "__" not in att:
            print(att)

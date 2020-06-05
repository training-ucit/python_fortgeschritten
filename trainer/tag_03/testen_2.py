def multiply(a, b):
    return a * b

if __name__ == "__main__":
    if not multiply(2, 3) == 6:
        print("Failure")
    if not multiply("a", 3) == "aaa":
        print("Failure 2")
    if multiply("a", 3) != "aaa":
        print("Seltsames Ergebnis")
if __name__=="__main__":
    formatter = "{} {} {} {}"

    print(formatter.format(1, 2, 3, 4))
    print(formatter.format("One", "Two", "Three", "Four"))
    print(formatter.format(True, False, True, False))
    print(formatter.format(formatter, formatter, formatter, formatter))
    print(formatter.format("Sourabh Deshmukh", "Aditya Patni", "Sarthak Patel", "Dhruv Desai"))


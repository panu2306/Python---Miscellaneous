if __name__=="__main__":
    print("This program demonstrates ways to print in Python!")
    
    print("First Way:")
    var = "Sounds good!"
    print("This is one way where comma is used as a separate to separate string and variable", var)

    print("Second Way:")
    print("This is second way where .format is used to mention variables inside the curly braces. {}".format(var))
    
    print("Third Way:")
    print(f"This is third way where fstring is used to mention variables inside curly braces. {var}")

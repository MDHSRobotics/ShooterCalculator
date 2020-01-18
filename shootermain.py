
def main():
    print("Welcome to the Shooter Calculator")

    xvalue = input("Enter an x value: ")
    
    yvalue = input("Enter a y value: ")
    print("x="+ xvalue)
    print("y=" + yvalue)

    zvalue = int(xvalue) + int(yvalue)
    print("z=" + str(zvalue))

if __name__ == '__main__':
    main()
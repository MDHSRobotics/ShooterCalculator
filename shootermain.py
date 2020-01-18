import math

def main():
    print("Welcome to the Shooter Calculator")

    x1= int( input("Enter an x1 value: "))
    y1= int( input("Enter a y1 value: "))

    x2= int( input("Enter an x2 value: "))
    y2= int( input("Enter a y2 value: "))

    print("A=(" ,x1,",",y1,"), B=(" ,x2,",", y2 ,")")
    slope = (y2 - y1)/ (x2 - x1)
    print("slope=" , slope)

    perp_slope = 1/slope * (-1)
    print("perpendicular slope=" , perp_slope)

    angle = math.atan(perp_slope)
    print("angle=" ,angle)

if __name__ == '__main__':
    main()
import math

def main():
    print("Welcome to the Shooter Calculator")

    x1= int( input("Enter an x1 value: "))
    y1= int( input("Enter a y1 value: "))

    x2= int( input("Enter an x2 value: "))
    y2= int( input("Enter a y2 value: "))
    
    h= (y1 + y2)/2
    g= 32.2

    velocity= float( input("Enter velocity:"))

    print("A=(" ,x1,",",y1,"), B=(" ,x2,",", y2 ,")")
    slope = (y2 - y1)/ (x2 - x1)
    print("slope=" , slope)

    perp_slope = 1/slope * (-1)
    print("perpendicular slope=" , perp_slope)

    angle_radians = math.atan(perp_slope)
    angle_degree = angle_radians * 180/math.pi

    hmax = h + velocity * velocity * math.sin(angle_radians) * math.sin(angle_radians) / (2 * g)
    
    print("angle in degrees=" ,angle_degree)

    print("velocity=",velocity)

    print("Initial Height=", h)

    print("Max Height=", hmax)

if __name__ == '__main__':
    main()
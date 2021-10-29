import math
# ex 7.3 book page 70
def estimate_pi():
    result = 0
    k = 0

    while result < 10**(-15):        
        result += (math.factorial(4*k)*(1103+(26390*k))) / ((math.factorial(k)**4)*(396**(4*k)))

    result *= (2*math.sqrt(2))/9801
    print("Srinivasa Ramanujan equation for 1/π = " + str(result))

print("\t\t\t\t 1/π = " + str(1/math.pi))
estimate_pi()
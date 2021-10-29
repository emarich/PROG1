# ex 7.1 book page 69
import math

def mysqrt(a):
    x = 1
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return y

def test_square_root():
    print("a\tmysqrt(a)\t\tmath.sqrt(a)\t\tdiff")
    print("_\t---------\t\t------------\t\t----")

    for i in range(1, 10):
        mySqrt = mysqrt(i)
        mathSqrt = math.sqrt(i)
        diff = 0
        if (mySqrt > mathSqrt):
            diff = mySqrt - mathSqrt
        else:
            diff = mathSqrt - mySqrt

        print(float(i), end="\t")
        print(mySqrt, end="\t" if len(str(mySqrt)) > 3 else "\t\t\t")
        print(mathSqrt, end="\t" if len(str(mathSqrt)) > 3 else "\t\t\t")
        print(diff)

test_square_root()
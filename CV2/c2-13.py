def geo_rad(a,r,n):
    r0 = r
    for i in range(n):
        print(a)
        a += r
        r *= r0

geo_rad(1, 2, 5)

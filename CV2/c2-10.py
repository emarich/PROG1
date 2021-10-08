from time import process_time_ns

g_a = 1
g_r = 2
g_n = 50000

def geo_postupnost8(a,r,n):
    for i in range(n):
        result = a*(r**i)

def geo_postupnost9(a,r,n):
    for i in range(n):
        a *= r

t1_start = process_time_ns() 
geo_postupnost8(g_a, g_r, g_n)
t1_stop = process_time_ns() 
print("Trvanie behu funkcie geo_postupnost8 v nanosekundach:\n", t1_stop-t1_start)  

t2_start = process_time_ns() 
geo_postupnost9(g_a, g_r, g_n)
t2_stop = process_time_ns()
print("Trvanie behu funkcie geo_postupnost9 v nanosekundach::\n", t2_stop-t2_start) 
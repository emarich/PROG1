from time import process_time_ns
from neefektivny_skript import geom_rad_neefektivne

g_a = 1
g_r = 2
g_n = 1000

def geo_rad11(a,r,n):
    for i in range(n):
        a += (r**(i+1))

def geo_rad13(a,r,n):
    r0 = r
    for i in range(n):
        a += r
        r *= r0

t1_start = process_time_ns() 
geo_rad11(g_a, g_r, g_n)
t1_stop = process_time_ns() 
print("Trvanie behu funkcie geo_rad11 v nanosekundach:\n", t1_stop-t1_start)

t2_start = process_time_ns() 
geo_rad13(g_a, g_r, g_n)
t2_stop = process_time_ns()
print("Trvanie behu funkcie geo_rad13 v nanosekundach::\n", t2_stop-t2_start)

t3_start = process_time_ns() 
geom_rad_neefektivne(g_a, g_r, g_n)
t3_stop = process_time_ns() 
print("Trvanie behu funkcie geom_rad_neefektivne v nanosekundach:\n", t3_stop-t3_start)
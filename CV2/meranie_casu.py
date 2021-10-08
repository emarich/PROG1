

from time import process_time_ns   #tu importujeme funkciu processs_time_ns z kniznice time. pomocou tejto funkcie budeme merat cas behu programu. 
                                   #o funkcii process_time_ns si mozete viac precitat tu: https://www.geeksforgeeks.org/time-process_time-function-in-python/  

####################################### definicie funkcii #######################################################

def arit(a0,d,N):         # prve riesenie ulohy 6 z cvicenia
    for i in range(N):
        b=a0+i*d
        #print(b)         # v rieseni ulohy 6 by mal byt tento riadok odkomentovany. ja som ho tu zakomentoval kvoli meraniu casu

def arit2(a0,d,N):         # druhe riesenie 6 a sucasne riesenie ulohy 7
    b=a0
    for i in range(N):
        #print(b)          # v rieseni ulohy 6 by mal byt tento riadok odkomentovany. ja som ho tu zakomentoval kvoli meraniu casu  
        b=b+d

####################################### meranie casu pre funkciu arit #######################################################

t1_start = process_time_ns() 
   
arit(1,7,10000000)
  
t1_stop = process_time_ns()
 
print("Trvanie behu funkcie arit v nanosekundach:\n", t1_stop-t1_start)  

####################################### meranie casu pre funkciu arit2 #######################################################

t2_start = process_time_ns() 
   
arit2(1,7,10000000)
  
t2_stop = process_time_ns()
 
print("Trvanie behu funkcie arit2 v nanosekundach::\n", t2_stop-t2_start) 

def geom_rad_neefektivne(a0,r,N):
     for i in range(N):
         s=a0
         for j in range(i):
             s=s+a0*(r**(j+1))
        #  print(s)

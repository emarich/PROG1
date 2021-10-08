def draw_column_line(n):
    for j in range(n):
        print("|     ", end="")
    print("|",)

def draw_grid(n):
    for i in range(n+1):
        for j in range(n):
            print("+", end="")
            print(" - - ", end="")            
        print("+")
        if (i != n):
            draw_column_line(n)

draw_grid(3)
def move(f, t):
    print("Move from {} to {}".format(f,t))

def hanoi(h,f,v,t):
    if h == 0:
        pass
    else:
        hanoi(h-1,f,t,v)
        move(f,t)
        hanoi(h-1,v,f,t)
        
if __name__ == "__main__":
    
    h = input("What is the height of the tower to solve?\n")       
    hanoi(int(h),'A','B','C')
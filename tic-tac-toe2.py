field = [['- ']*3 for _ in range(3)]

def show_field(f):
    print('  0  1  2 ')
    for i in range(len(field)):
        print(str(i),*field[i])

        
def ask(f):
    while True:
        coords = input("введите коррдинаты х у через пробел ").split()
        if len(coords)!= 2: 
            print("введите две коррдинаты через пробел")
            continue
        if not(coords[0].isdigit() and coords[1].isdigit()):
            print("введите именно числа через пробел")
            continue
        x,y=map(int, coords)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print("вышли из диапазона")
            continue
        if f[x][y] !='- ': 
            print("клетка занята") 
            continue
        break
    return x,y


def win(f, user):
        win_cord = (((0, 0),(0, 1),(0, 2)),((1, 0),(1, 1),(1, 2)),((2, 0),(2, 1),(2, 2)),  
                   ((2, 0),(1, 1),(0, 2)),((0, 0),(1, 1),(2, 2)),((0, 0),(1, 1),(2, 2)),
                   ((0, 1),(1, 1),(2, 1)),((0, 1),(1, 1),(2, 2)))
        for cord in win_cord:
            symbols = []
            for c in cord:
                symbols.append(f[c[0]][c[1]])
            if symbols == [user, user, user]:
                return True
        return False


counter=0    
while True:
    if counter%2==0:
        user='x'
    else:
        user=' o'
    show_field(field)
    x,y=ask(field)
    field[x][y]=user
    if counter==9:
        print('ничья')
    if win(field, user):
        print(f"выйграл {user}")
        show_field(field)
        break
    counter+=1

    



    
            

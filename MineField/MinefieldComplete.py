import random

def display_board():
    print("\n")
    for Row in range(0, length):
        for Column in range(0, length):
            print(" {} ".format(MineField[Row][Column][0]), end='  ')
        print("\n")


def game(k, l):

    if (MineField[k][l][1] == 1):
        MineField[k][l][0] = "X"

    else:
        bombCount = 0
        #  Köşeler için

        if (k == 0 and l == 0):  # Sol üst köşe

            bombCount += MineField[k + 1][l][1]  # Hücrenin Altı
            bombCount += MineField[k][l + 1][1]  # Hücrenin Sağı
            bombCount += MineField[k + 1][l + 1][1]  # Hücrenin Sağ Altı

            MineField[k][l][0] = bombCount
            bombCount = 0

        elif (k == length - 1 and l == 0):  # Sol alt köşe

            bombCount += MineField[k - 1][l][1]  # Hücrenin Üstü
            bombCount += MineField[k - 1][l + 1][1]  # Hücrenin Sağ Üstü
            bombCount += MineField[k][l + 1][1]  # Hücrenin Sağı

            MineField[k][l][0] = bombCount
            bombCount = 0

        elif (k == length - 1 and l == length - 1):  # Sağ alt köşe

            bombCount += MineField[k - 1][l - 1][1]  # Hücrenin Sol Üstü
            bombCount += MineField[k][l - 1][1]  # Hücrenin Solu
            bombCount += MineField[k - 1][l][1]  # Hücrenin Üstü

            MineField[k][l][0] = bombCount
            bombCount = 0

        elif (k == 0 and l == length - 1):  # Sağ üst köşe

            bombCount += MineField[k][l - 1][1]  # Hücrenin Solu
            bombCount += MineField[k + 1][l - 1][1]  # Hücrenin Sol Altı
            bombCount += MineField[k + 1][l][1]  # Hücrenin Altı

            MineField[k][l][0] = bombCount
            bombCount = 0

            #  Kenarlar için

        if ((k == 0) and (0 < l < length - 1)):  # Üst kenar

            bombCount += MineField[k][l - 1][1]  # Hücrenin Solu
            bombCount += MineField[k][l + 1][1]  # Hücrenin Sağı
            bombCount += MineField[k + 1][l + 1][1]  # Hücrenin Sağ Altı
            bombCount += MineField[k + 1][l - 1][1]  # Hücrenin Sol Altı
            bombCount += MineField[k + 1][l][1]  # Hücrenin Altı

            MineField[k][l][0] = bombCount
            bombCount = 0

        elif ((0 < k < length - 1) and (l == 0)):  # Sol kenar

            bombCount += MineField[k][l + 1][1]  # Hücrenin Sağı
            bombCount += MineField[k - 1][l + 1][1]  # Hücrenin Sağ Üstü
            bombCount += MineField[k + 1][l + 1][1]  # Hücrenin Sağ Altı
            bombCount += MineField[k - 1][l][1]  # Hücrenin Üstü
            bombCount += MineField[k + 1][l][1]  # Hücrenin Altı

            MineField[k][l][0] = bombCount
            bombCount = 0

        elif ((k == length - 1) and (0 < l < length - 1)):  # Alt kenar

            bombCount += MineField[k - 1][l][1]  # Hücrenin Üstü
            bombCount += MineField[k - 1][l + 1][1]  # Hücrenin Sağ Üstü
            bombCount += MineField[k][l + 1][1]  # Hücrenin Sağı
            bombCount += MineField[k - 1][l - 1][1]  # Hücrenin Sol Üstü
            bombCount += MineField[k][l - 1][1]  # Hücrenin Solu

            MineField[k][l][0] = bombCount
            bombCount = 0

        elif ((0 < k < length - 1) and (l == length - 1)):  # Sağ kenar

            bombCount += MineField[k - 1][l - 1][1]  # Hücrenin Sol Üstü
            bombCount += MineField[k][l - 1][1]  # Hücrenin Solu
            bombCount += MineField[k - 1][l][1]  # Hücrenin Üstü
            bombCount += MineField[k + 1][l][1]  # Hücrenin Altı
            bombCount += MineField[k + 1][l - 1][1]  # Hücrenin Sol Altı

            MineField[k][l][0] = bombCount
            bombCount = 0

            # Ortadaki Hücreler için

        if ((0 < k < length - 1) and (0 < l < length - 1)):
            bombCount += MineField[k - 1][l - 1][1]  # Hücrenin Sol Üstü
            bombCount += MineField[k - 1][l][1]  # Hücrenin Üstü
            bombCount += MineField[k - 1][l + 1][1]  # Hücrenin Sağ Üstü
            bombCount += MineField[k][l - 1][1]  # Hücrenin Solu
            bombCount += MineField[k][l + 1][1]  # Hücrenin Sağı
            bombCount += MineField[k + 1][l - 1][1]  # Hücrenin Sol Altı
            bombCount += MineField[k + 1][l][1]  # Hücrenin Altı
            bombCount += MineField[k + 1][l + 1][1]  # Hücrenin Sağ Altı

            MineField[k][l][0] = bombCount
            bombCount = 0

def reset_board():
    MineField.clear()
    print(MineField)

def generate_board():
    for i in range(0,length):
        MineField.append([])
        for j in range(0,length):
            y = random.randint(0,3)  # %30~ şans
            if (y == 1):
                MineField[i].append(["?",y])
            else:
                MineField[i].append(["?",0])

length = int(input("oyun alanı AxA, A="))

MineField = []

reset = 1
while(reset == 1):
    openPlay = int(input("Enter 1 for revealed board, 2 for regular game : "))

    reset_board()
    generate_board()

    if(openPlay == 1):
        k = 0
        l = 0

        for k in range(0,length):
            for l in range(0,length):
                game(k,l)
        display_board()

        reset = int(input("Enter 1 to play again, 2 to exit : "))

    if(openPlay == 2):
        state = "playing"
        while(state == "playing"):
            display_board()

            row = int(input("Give me Row (0 - " + (length - 1).__str__() + ") : "))
            col = int(input("Give me Column (0 - " + (length - 1).__str__() + ") : "))
            game(row,col)

            if(MineField[row][col][1] == 1):
                display_board()
                reset = int(input("Game over, stepped on a mine.\nEnter 1 to play again, 2 to exit : "))
                state = "dead"




def board(index=0, sign=" ", a=['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']):
    a[index] = sign
    print(" " * 41 + a[0] + "|" + a[1] + "|" + a[2])
    print(" " * 41 + "-----")
    print(" " * 40 + a[3] + "|" + a[4] + "|" + a[5])
    print(" " * 41 + "-----")
    print(" " * 40 + a[6] + "|" + a[7] + "|" + a[8])
    return a


def main_game():
    a = ["  ", '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    turn = 0
    index2 = []
    board()
    print("The first player is X and the second player will be O: alt turns wiil be there")
    player1 = input("enter player1 's name")
    player2 = input("enter player2 's name")
    while True:
        if "  " in a:
            if turn == 1:
                try:
                    index = int(input("enter the index"))
                    if index not in index2 and index > 0 and index < 10:
                        a = board(index - 1, "O", a)
                        index2.append(index)
                        turn = 0
                    elif index <= 0 or index >= 10:
                        print("invalid input")
                    else:
                        print("index used before  please enter new index")
                except:
                    print("error occured plaese try again ")
            elif turn == 0:
                try:
                    index = int(input("enter the index"))

                    if index not in index2 and index > 0 and index < 10:
                        a = board(index - 1, "X", a)
                        index2.append(index)
                        turn = 1
                    elif index <= 0 or index > 9:
                        print("invalid input")
                    else:
                        print("index used before  please enter new index")
                except:
                    print("error occured plaese try again")
            if a[0] == a[1] == a[2] == "X" or a[3] == a[4] == a[5] == "X" or a[6] == a[7] == a[8] == "X" or a[0] == a[
                3] == a[6] == "X" or a[1] == a[4] == a[7] == "X" or a[8] == a[5] == a[2] == "X" or a[0] == a[4] == a[
                8] == "X" or a[2] == a[4] == a[6] == "X":
                print(player1 + "(X) wins the game ")
                break
            elif a[0] == a[1] == a[2] == "O" or a[3] == a[4] == a[5] == "O" or a[6] == a[7] == a[8] == "O" or a[0] == a[
                3] == a[6] == "O" or a[1] == a[4] == a[7] == "O" or a[8] == a[5] == a[2] == "O" or a[0] == a[4] == a[
                8] == "O" or a[2] == a[4] == a[6] == "O":
                print(player2 + "(O) wins the game ")
                break
        else:
            print("game over no one wins")
            break


main_game()
while True:
    a = str(input("wanna play again Y/N:"))
    if a == "Y" or a == "y":
        main_game()
    elif a == "N" or a == "n":
        break
    else:
        print("invalid answer ")

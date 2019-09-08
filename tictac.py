#!/usr/bin/python3
import os

class tictac():
    def __init__(self):
     self.player = "Player 1"
     self.marker = ''
     self.status="Playing ......"
     self.detect = "Win not detected"
     self.game = [[0,0,0],
		   [0,0,0],
		   [0,0,0],]
    def play(self):
        player1 = 'X'
        player2 = 'Y'

        if self.player =="Player 1":

            self.marker=player1
            self.player="Player 2"
            return self.marker
        else:
            self.marker=player2
            self.player="Player 1"
            return self.marker

    def game_board(self):
     os.system('clear' or 'cls')
     print("     0   1   2")
     print("")
     count = 0
     for row in self.game:
      print (count ,"  ", '   '.join(str(now) for now in row))
      count+=1

     print(self.status)
     print("Player :" + self.player)

    def checkwin(self):

     if((self.game[0][0] == self.game[0][1] == self.game[0][2] == self.marker) or
        (self.game[0][0] == self.game[1][0] == self.game[2][0] == self.marker) or
        (self.game[0][0] == self.game[1][1] == self.game[2][2] == self.marker) or
        (self.game[0][1] == self.game[1][1] == self.game[2][1] == self.marker) or
        (self.game[1][0] == self.game[1][1] == self.game[1][2] == self.marker) or
        (self.game[2][0] == self.game[2][1] == self.game[2][2] == self.marker) or
        (self.game[0][2] == self.game[1][2] == self.game[2][2] == self.marker) or
        (self.game[0][2] == self.game[1][1] == self.game[2][0] == self.marker)) :

           self.detect="Win detected"
           if self.marker == 'X':
            print("Win detected Player 1 wins")
           elif self.marker == 'Y':
            print("Win detected Player 2 wins")


    def playing(self):
     os.system('clear' or 'cls')
     while self.detect=="Win not detected":
        self.game_board()
        self.checkwin()
        if self.detect=="Win detected":
         self.status="Stopped ......"
         self.player=""
         break
        try:
         row = int(input("Enter row where you want to input :"))

         column = int(input("Enter column where you want to input :"))
         a = int(row)
         b = int(column)
         os.system('clear' or 'cls')
         if (0<= a <= 2) and (0<= b <= 2):
            if self.game[a][b] ==0:
               self.game[a][b]=self.play()
            else:
                print("There is a mark existing at that position")
         else:
             print("Error :make sure digit entered is between zero and two")
             #continue
        except (ValueError):
            os.system('clear' or 'cls')
            print("Error :make sure you entered a digit")
     self.game_board()
     self.checkwin()

obj=tictac()
obj.playing()

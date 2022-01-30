import turtle
from helper import *

'''
Helper Functions for Draw Chess Board
--------------------------------------------------------
draw_white_square()
draw_black_square()
'''
if __name__ == "__main__":
  for i in range(size_of_board):
    pen.up()
    pen.setpos(-50, 30 * i)
    pen.down()
      ### END CODE HERE ###
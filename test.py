from board import *
from main import *

board = Board()
main = Main()

#print board.inside_board(1,5)
print "Programm zur Loesungsfindung zum Solitaerbrettspiel - Informatik Projekt von Erik Haarlaender und Max Kessler"
print " "
print " "
print "PROCESSING --- Please stand by!"
solution = []
main.recursion(board, solution)
main.print_solutions(solution)

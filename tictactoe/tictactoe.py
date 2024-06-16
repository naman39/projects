"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Number_of_X = 0
    Number_of_O = 0
    Number_of_EMPTY = 0

    for row in board:
        Number_of_X += row.count(X)
        Number_of_O += row.count(O)
        Number_of_EMPTY += row.count(EMPTY)
    
    if Number_of_X > Number_of_O:
        return O  
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    set_of_actions = set()
    a = 0
    b = 0

    '''The following loop will iterate through each row of the list and the board and will check for the 
       EMPTY places and will note down its places with a and b as counters cause we cannot use j as a counter
       because it is a none value and we cannot iterate it.
    '''
    for i in board:
        for j in i:
            if j == EMPTY:
                iterating_tuple = (a,b)
                set_of_actions.add(iterating_tuple)
            b += 1
        b = 0
        a+=1

    return set_of_actions 


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #Firstly making a deepcopy of the board for changing states without affecting the actual board
    #After that it is just checking if that place of the board is empty if so place the player mark whose turn it is
    # Otherwise just raise an exception

    new_board = copy.deepcopy(board)
    a = action[0]
    b = action[1]

    if new_board[a][b] == None:
        new_board[a][b] = player(board)
    else:
        raise Exception("Not a valid action")
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #ROW AND COLUMN CHECK
    for i in range(3):
        if board[i][0] == board[i][1] == board [i][2] and board[i][0] != EMPTY:
            return board[i][0]
        elif board[0][i] == board[1][i] == board [2][i] and board[0][i] != EMPTY:
            return board[0][i]
    
    #DIAGONAL CHECK
    if board[0][0] == board[1][1] == board [2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board [2][0] and board[0][2] != EMPTY:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def maxval(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -2
            for action in actions(board):
                minvalue = minval(result(board, action))[0]
                if minvalue > v:
                    v = minvalue
                    optimal_move = action
            return v, optimal_move

    def minval(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 2
            for action in actions(board):
                maxvalue = maxval(result(board, action))[0]
                if maxvalue < v:
                    v = maxvalue
                    optimal_move = action
            return v, optimal_move

    if terminal(board):
        return None

    if player(board) == X:
        return maxval(board)[1]

    else:
        return minval(board)[1]
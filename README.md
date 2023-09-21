# Chess
bare-bones Chess specifically for pi Pico

for all locations, they must be a string in the form of a common chess coordinate ("A1", "C4", "H8", etc...). The letter must always be capitalized, and can be any letter from A to H inclusive.
The number must be from 1 to 8 inclusive. All Pieces may assume the location is correct, the board must check any location provided.

all string representations of pieces shall be in the form of (color)(piece), where color is either piece.TOP_COLOR or piece.BOTTOM_COLOR ("w" or "b"), and piece is one of the following:
'p' = pawn
'n' = knight
'b' = bishop
'r' = rook
'q' = queen
'k' = king

as an example, the row A1 to A8 is: wr, wn, wb, wk, wq, wb, wn, wr

The board is laid out so that the top left corner square (A1) is white, the top row is row A, the bottom row is row H, the left column is column 1, the right column is column 8.

board Functions:
  bool board.move([present_loc],[new_loc])
      This function moves whichever piece is at present_loc to new_loc if the following are true:
        1) there is a piece at present_loc
        2) the piece at present_loc is owned by the person taking the turn (the piece is TOP_COLOR while it's TOP_COLOR's turn, the piece is BOTTOM_COLOR while it's BOTTOM_COLOR's turn)
        3) the move from present_loc to new_loc is legal for the type of piece making the move
        4) the person whose move it is doesn't end the turn in check
      If the piece was moved, this function returns True. otherwise, the function returns False

  piece board.king(color)
      This function returns a reference to the piece which is king and has the provided color.
      if color is neither piece.TOP_COLOR or piece.BOTTOM_COLOR, an TypeError is thrown (explaining that the color must be either piece.BOTTOM_COLOR or piece.TOP_COLOR)

  string board.get_cell(loc)
      This returns the string representation of the piece on the space "loc". If no piece is on the space, an empty string ("") is returned instead.

  bool board.capture(loc)
      This causes the piece.capture() routine to run on the piece located at loc.
      If no piece is at loc, return False.
      If the piece at loc is of the same color as the player whose turn it is, return False.

  piece board.promote(loc,promotion_type)
      This function can only be called on pawns (the piece at loc is a pawn), and only when:
        1) the player who owns the pawn at loc is the player whose turn it is
        2) loc is the starting location of the current move
        3) the row is "B" for piece.BOTTOM_COLOR or "G" for piece.TOP_COLOR (penultimate rank)
        4) promotion_type is one of ['n', 'b', 'r', 'q'] (knight, bishop, rook, queen)
          4a) if promotion_type is incorrect, raise TypeError (explaining what the correct types are)
      This function returns a piece of the selected type initialized with the pawn at loc as the input

  board.reset()
    This function resets the board to initial state. (Use piece.TOP_COLOR and piece.BOTTOM_COLOR instead of w and b when initializing)
      1) row A is:
        A1: wr
        A2: wn
        A3: wb
        A4: wk
        A5: wq
        A6: wb
        A7: wn
        A8: wr
      2) row B is all wp's
      3) rows C through F are empty ("")
      4) row G is all bp's
      5) row H is similar to row A except black, H4 is bq and H5 is bk
      
    I am unsure how well the embedded garbage collector works, so would prefer placing all pieces from the previous game back to their original locations, 
    but demoting pieces may get a bit trickier than relying on the garbage collector.

piece functions:
  bool piece.move(newLoc, board)
    must be overridden by all pieces - this function checks to see if moving the piece to the newLoc is legal based on
    the movement capabilities of the given piece (see below).  Some pieces must know the board state to determine if a 
    move is legal (pawns can only change columns if they are attacking something, for instance)
    If the move is legal, the piece should also update its internal known location (if having location information
    in multiple locations - board and piece - is cumbersome, we can add another input to this function so that it's 
    (self, loc, newLoc, board) instead). Return True if legal.
    if the move is not legal, return False.

  if location and/or capture state are held internally to each piece, the following functions are also required:

  captured()
    this function changes the internal state of the piece to recognize that it is no longer on the board

  bool get_captured()
    this function returns the state of capture (False if it is on the board still, True if it is no longer on the board)

  str get_pos()
    this function returns the internally held location for the piece
    

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

  list board.get_state()
    This function should return the current state of the board as a list, where list[0] corresponds to A1, list[1] corresponds to A2,
    list[8] corresponds to B1, and list[63] corresponds to H8 (with all intervening cells corresponding to the relative coordinate along the way)

    The contents of each cell of the list should be a string in the form described above (i.e., 'wp', 'bq', etc...). 
    Empty cells should be represented with an empty string ("")

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
    
legal piece movements:
all legal moves must be on the board (A1 through H8)

pawn -
  can move forward 1 or 2 spaces if it is on its starting location 
    the space in front of it, and the space it moves to (if those are different) must be empty
  can only move forward 1 space if it is not on its starting location and is moving forward
    space it moves to must be empty
  can move forward 1 space and sideways (either way) 1 space if it is attacking
    can attack anything owned by the opposing player on the space it moves diagonally to
    can attack a pawn owned by the opposing player on the space adjacent to it
      the move previous to this must be that same pawn moving forward 2 spaces
      known as en passant

knight -
  can move 2 spaces in one direction and 1 space orthogonally to the first direction
    space it moves to must either be empty or held by a piece owned by the opposing player

bishop -
  can move diagonally (same increment or decrement of columns as rows) as far as the player wants 
    the spaces between its starting and ending location must be empty
    the ending location must be empty or be held by a piece owned by the opposing player

rook -
  can move horizontally or vertically as far as the player wants
    the spaces between its starting and ending location must be empty
    the ending locaiton must be empty or be held by a piece owned by the opposing player
  can castle
    rook and king must not have moved during this game
    there are no pieces between the rook and king
    the king is not in check
    the square the king goes to and the intervening square cannot be under attack (cannot castle through check)
    moves with king
      king moves 2 spaces
      rook moves to opposite side of king (2 or 3 spaces, depending on which rook castles)

queen -
  can move horizontally, vertically, or diagonally as far as the player wants
    the spaces between its starting and ending locations must be empty
    the ending location must be empty or be held by a piece owned by the opposing player

king -
  can move one space horizontally, vertically or diagonally
    cannot move onto a space which contains a piece owned by the same player
    cannot move into a space which is threatened (something can move there next turn)
  can castle
    see rook explanation

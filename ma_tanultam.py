Ma Tanultam:

180207:
    "nagyitás projekt"
    # ahhoz, hogy ne stringnek printelje ki az alábbi tartalmat:
    board[0][0] = '\033[0;37;41m   |\033[0m'
    # joinolni kellett a cella elemeket és megfelelő [] tömbbé alakitani, 
    # (mert különben több elemnek nézi a join és azt nem fogadja el):
    board2="".join([board[0][0]*2, board[0][1]*2, board[1][0]*2, board[1][1]*2])

    "torpedó"
    board_ai_ships = [0, 0, 0, 0, 0, 0] #ez 5 pozició és 5 érték! nem 5 nulla!

180206:
    # az in-nek kell megnézni, hogy egy string/int benne van-e egy listában, nem az egyenlővel!
    if user_input in allowed_chars:

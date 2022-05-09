from cairosvg import svg2png
import chess
import chess.svg
import random

j = 0
i = 1
for i in range(1, 26):

    board_ = chess.Board('8/8/8/8/8/8/8/8 w - - 0 1')
    cases_liste = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "c1",
                   "c2", "c3", "c4", "c5", "c6", "c7", "c8", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "e1", "e2",
                   "e3","e4", "e5", "e6", "e7", "e8", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "g1", "g2", "g3",
                   "g4",
                   "g5", "g6", "g7", "g8", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
    piece_liste = ["K", "Q", "N", "P", "R", "B", "k", "q", "n", "p", "r", "b"]

    J = random.randint(15, 20)

    for j in range(J):
        c = random.choice(cases_liste)
        p = random.choice(piece_liste)
        board_.set_piece_at(square=chess.SQUARE_NAMES.index(c), piece=chess.Piece.from_symbol(p))
        cases_liste.remove(c)
        j = j + 1

    print(board_)
    board_svg = chess.svg.board(board_)
    svg2png(bytestring=board_svg, write_to=f'/Users/jeanne_spiteri/PycharmProjects/Chess/positions/img_{i}_0.png')


    i = i + 1

from cairosvg import svg2png
import chess
import chess.svg
import random
from PIL import Image


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


j = 0
i = 76
s = 0
for i in range(76, 101):
    interdit = []
    board_ = chess.Board('8/8/8/8/8/8/8/8 w - - 0 1')
    cases_liste = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "c1",
                   "c2", "c3", "c4", "c5", "c6", "c7", "c8", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "e1", "e2",
                   "e3", "e4", "e5", "e6", "e7", "e8", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "g1", "g2", "g3",
                   "g4", "g5", "g6", "g7", "g8", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
    piece_liste = ["K", "Q", "N", "P", "R", "B", "k", "q", "n", "p", "r", "b"]

    # construire l'image initiale.

    J = random.randint(15, 20)  # J est le nombre de pieces sur l'image initiale de l'échequier

    for j in range(J):
        c = random.choice(cases_liste)
        p = random.choice(piece_liste)
        board_.set_piece_at(square=chess.SQUARE_NAMES.index(c), piece=chess.Piece.from_symbol(p))
        cases_liste.remove(c)
        j = j + 1
    print(board_)
    board_svg = chess.svg.board(board_)
    svg2png(bytestring=board_svg, write_to=f'/Users/jeanne_spiteri/PycharmProjects/Chess/positions/chess#{i}-0.png')

    im1 = Image.open(f'/Users/jeanne_spiteri/PycharmProjects/Chess/positions/chess#{i}-0.png')
    get_concat_h(im1, im1).save(f'/Users/jeanne_spiteri/PycharmProjects/Chess/Chess_PNG/IMG_{i}_00.png')

    # construire les images avec les differences.
    S = random.randint(0, 7)  # on randomise combien il y aura de differences pour l'image i
    print(S)
    if S == 0:
        svg2png(bytestring=board_svg, write_to=f'/Users/jeanne_spiteri/PycharmProjects/Chess/positions/chess#{i}-00.png')
    else:
        for s in range(S):
            cases_liste = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "b1", "b2", "b3", "b4", "b5", "b6", "b7",
                           "b8", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "d1", "d2", "d3", "d4", "d5", "d6",
                           "d7", "d8", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "f1", "f2", "f3", "f4", "f5",
                           "f6", "f7", "f8", "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "h1", "h2", "h3", "h4",
                           "h5", "h6", "h7", "h8"]
            piece_liste = ["K", "Q", "N", "P", "R", "B", "k", "q", "n", "p", "r", "b"]

            c2 = random.choice(chess.SQUARE_NAMES)
            p2 = random.choice(piece_liste)

            while c2 in interdit:
                c2 = 0
                c2 = random.choice(chess.SQUARE_NAMES)

            print(c2)
            jeanne = board_.piece_type_at(square=chess.SQUARE_NAMES.index(c2))
            print("jeanne =")
            print(jeanne)

            if jeanne == None:  # si case vide, ajouter une piece
                board_.set_piece_at(square=chess.SQUARE_NAMES.index(c2),
                                    piece=chess.Piece.from_symbol(p2))  # rajouter une piece

            else:  # si case pleine, alors au hasard
                Q = random.randint(1, 2)
                if Q == 1:  # soit se contenter de retirer la piece
                    board_.remove_piece_at(square=chess.SQUARE_NAMES.index(c2))  # juste retirer la piece

                else:  # soit retirer la piece et la remplacer: Q = 2
                    if jeanne != p2:  # si ma proposition de nouvelle piece est bien differente de celle actuelle
                        board_.set_piece_at(square=chess.SQUARE_NAMES.index(c2),
                                            piece=chess.Piece.from_symbol(p2))  # remplacer la piece

                    else:  # jeanne == p2, la piece proposée et celle qui occupe deja la case sont les memes
                        piece_liste = piece_liste.remove(p2)
                        p2 = random.choice(piece_liste)
                        board_.set_piece_at(square=chess.SQUARE_NAMES.index(c2),
                                            piece=chess.Piece.from_symbol(p2))  # remplacer la piece

            interdit.append(c2)
            print(interdit)
            s = s + 1

            print(board_)
            board_svg = chess.svg.board(board_)
            svg2png(bytestring=board_svg, write_to=f'/Users/jeanne_spiteri/PycharmProjects/Chess/positions/chess#{i}-{s}.png')
            im1 = Image.open(f'/Users/jeanne_spiteri/PycharmProjects/Chess/positions/chess#{i}-0.png')
            im2 = Image.open(f'/Users/jeanne_spiteri/PycharmProjects/Chess/positions/chess#{i}-{s}.png')

            get_concat_h(im1, im2).save(f'/Users/jeanne_spiteri/PycharmProjects/Chess/Chess_PNG/IMG_{i}_{s}.png')




    i = i + 1

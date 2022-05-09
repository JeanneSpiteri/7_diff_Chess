from cairosvg import svg2png
import chess
import chess.svg
import random
from PIL import Image, ImageOps
import copy


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0), )
    dst.paste(im2, (im1.width, 0))
    return dst


for i in range(29, 40):
    interdit = []
    board_ = chess.Board('8/8/8/8/8/8/8/8 w - - 0 1')
    cases_liste = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "c1",
                   "c2", "c3", "c4", "c5", "c6", "c7", "c8", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "e1", "e2",
                   "e3", "e4", "e5", "e6", "e7", "e8", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "g1", "g2", "g3",
                   "g4", "g5", "g6", "g7", "g8", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
    piece_liste = ["K", "Q", "N", "P", "R", "B", "k", "q", "n", "p", "r", "b"]

    # build the initial image
    J = random.randint(15, 20)  # J est le nombre de pieces sur l'image initiale de l'échequier

    for j in range(J):
        c = random.choice(cases_liste)
        p = random.choice(piece_liste)
        board_.set_piece_at(square=chess.SQUARE_NAMES.index(c), piece=chess.Piece.from_symbol(p))
        cases_liste.remove(c)
        j = j + 1
    board_svg = chess.svg.board(board_, coordinates=False)
    svg2png(bytestring=board_svg,
            write_to=f'/Users/jeanne_spiteri/PycharmProjects/Chess14avril/positions/chess14avril#{i}-0.png')

    # border color and width
    color = "black"
    border = (20, 20, 20, 20)

    im1 = Image.open(f'/Users/jeanne_spiteri/PycharmProjects/Chess14avril/positions/chess14avril#{i}-0.png')
    im1 = ImageOps.expand(im1, border=border, fill=color)
    # get_concat_h(im1, im1).save(f'/Users/jeanne_spiteri/PycharmProjects/Chess14avril/Chess_PNG/img_{i}_0.png')

    # generate 5 different numbers of differences
    list_diff = list(range(0, 7))
    L = random.sample(list_diff, 5)
    print(L)

    for S in L:
        print(S)
        new_board = copy.copy(board_)
        if S == 0:
            svg2png(bytestring=board_svg,
                    write_to=f'/Users/jeanne_spiteri/PycharmProjects/Chess14avril/positions/chess14avril#{i}-00.png')
            get_concat_h(im1, im1).save(f'/Users/jeanne_spiteri/PycharmProjects/Chess14avril/Chess_PNG/img_{i}_0.png')
        else:  # build the images with the differences
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
                    c2 = random.choice(chess.SQUARE_NAMES)

                print(c2)
                jeanne = new_board.piece_type_at(square=chess.SQUARE_NAMES.index(c2))
                print("jeanne =", jeanne)

                if jeanne == None:  # if empty square, add piece
                    new_board.set_piece_at(square=chess.SQUARE_NAMES.index(c2),
                                           piece=chess.Piece.from_symbol(p2))  # rajouter une piece

                else:  # if full square, then two possibilities, randomly
                    Q = random.randint(1, 2)
                    if Q == 1:  # just remove the piece
                        new_board.remove_piece_at(square=chess.SQUARE_NAMES.index(c2))  # juste retirer la piece

                    else:  # replace the piece : Q = 2
                        if jeanne != p2:  # if the new piece proposition is really different than the current one
                            new_board.set_piece_at(square=chess.SQUARE_NAMES.index(c2),
                                                   piece=chess.Piece.from_symbol(p2))  # replace the piece

                        else:  # jeanne == p2, if the new piece proposition is the same as the current one
                            piece_liste.remove(p2)
                            p2 = random.choice(piece_liste)
                            new_board.set_piece_at(square=chess.SQUARE_NAMES.index(c2),
                                                   piece=chess.Piece.from_symbol(p2))  # replace the piece

                interdit.append(c2)
        print(new_board)
        new_board_svg = chess.svg.board(new_board, coordinates=False)
        svg2png(bytestring=new_board_svg,
                write_to=f'/Users/jeanne_spiteri/PycharmProjects/Chess14avril/positions/chess14avril#{i}-{S}.png')
        im1 = Image.open(f'/Users/jeanne_spiteri/PycharmProjects/Chess14avril/positions/chess14avril#{i}-0.png')
        im2 = Image.open(f'/Users/jeanne_spiteri/PycharmProjects/Chess14avril/positions/chess14avril#{i}-{S}.png')

        im1 = ImageOps.expand(im1, border=border, fill=color)
        im2 = ImageOps.expand(im2, border=border, fill=color)
        get_concat_h(im1, im2).save(f'/Users/jeanne_spiteri/PycharmProjects/Chess14avril/Chess_PNG/img_{i}_{S}.png')

    i = i + 1

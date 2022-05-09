7_diff_Chess
Create a 7 diff game between two chessboards

to import chess :

- use python 3.7 at least
- use conda/miniconda (then conda install chess) (with pip, it doesn't work) We only set the number of types of chessboards and theire names (or rather their rank, i): there are 25 images and they go from 76 to 101. So, i goes from 76 to 101. This script creates duets of two chessboards side by side with:
- the number of chess pieces (between 15 and 20) is random (J)
- type of chesspiece in the initial board is random (p)
- the location of the occupied squares in the initial board is random (c)
- the maximal number of differences (between 0 and 7) is random (S)
- the place where the differences are set is random (and changes each times) (c2)
- the type of the difference (add, replace or delete) is random (Q)
- the piece that replaces another piece is random (p2) The several random differences in a precise i chessboard always changes of square lolation since the list 'interdit" prevents the given square from being changed twice (otherwise we would have less than n differnces). The duet of images img_i_s is compposed by :
- the initial Chess#i-0 on the left hand side.
- the changed Chess#i-s, where s is the degree of differnce (s goes from 0 to 7), on the right hand side. The Chess#i-s is alwayes compared to the initial Chess#i-0, never with the previous construction Chess#i-(s-1). Between Chess#i-0 and Chess#i-s, there are s differences. The duet is called img_i_s. Between Chess#i-(s-1) and Chess#i-s, there is 1 difference. No constructed duet.
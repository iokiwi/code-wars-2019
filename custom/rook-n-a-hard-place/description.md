# Rook 'n' a Hard Place

You are within a few moves of becomming, the next Wellington Regional chess champion. In chess, it is customary to declare `Check` when your opponents king is in danger of being taken, but could move to safety and `Checkmate` when your opponents King is in danger and has nowhere to run.

You have them in a corner - maybe literally, but are they in `Check`, `Checkmate`, or do you have a bit more work to do?

If you are not already familiar with all of the chess pieces and the moves each of them can make, you may find them [here](https://www.dummies.com/games/chess/knowing-the-moves-that-chess-pieces-can-make/).


Positions on the chess board are described by XY coordinates where X coordinates
are letters A-Z and Y coordinates are numbers 1-8 as follows.

```
8
7
6
5
4
3
2
1
  A B C D E F G H I J K
```

## Input

The input consist of, on the first line, the coordinates of your opponents king on the chess board. Subequent lines contain pairs of  the name of your pieces (`king`, `queen`, `rook`, `knight`, `bishop` or `pawn`) and their position on the board, Eg. `A1`

## Output

* `Check` if the king is in danger of being taken
* `Checkmate` if the king is in danger of being taken and has no safe spaces to move to
* `Safe` otherwise

## Example

```
Input:      Output:
a8          Checkmate
2
rook  a1
queen b1
```

```
Input:      Output:
K8          Check
2
knight J6
bishop I5
```

```
Input:      Output:
K1          Safe
2
rook I2
bishop J3
```
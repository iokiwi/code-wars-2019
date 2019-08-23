# Fold the Paper Nicely

Danny has a daily calendar (365 pages) on his desk.  Every morning, he tears off one page and, as he is reading the notes on the next page, he folds (out of habit) the sheet in his hand.  Danny noticed that he always folds the sheet (a rectangular paper) along the longer side, e.g., if one side is 80 and the other side is 60, he would fold along 80; this will make the paper of size 40 and 60; if he folds it again, he would fold along 60 since that’s the longer side now.

### The Problem:

Given a rectangular piece of paper and how many times Danny folds it, you are to determine the final sizes.  When folding a side with an odd length, the fraction is ignored after folding, e.g., if a side is 7, it will become 3 after folding.

### The Input:

The  input  consists  of  one  line,  containing  three  positive  integers  (each  ≤  10000),  the  first  two providing the rectangle sides and the third providing the number of folds.

### The Output:

Print the final values for the rectangle (larger side of the final values first).  

```
Sample Input    Sample Output
60 51 4         15 12
```

```
Sample Input    Sample Output
3 2 50          0 0
```

```
Sample Input    Sample Output
3 2 1           2 1
```

```
Sample Input    Sample Output
5 800 2         200 5
```

**Explanation for the first Sample Input/Output:** the rectangle starts with sides {60, 51} and successively becomes {30, 51}, {30, 25}, {15, 25}, {15, 12}.

**Explanation for the last Sample Input/Output:** the rectangle starts with sides {5, 800} and successively becomes {5, 400}, {5, 200}.
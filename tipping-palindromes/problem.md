# Tipping Palindromes

Danny is a "Palindrome Tipper". A palindrome is a string that reads the same forward and backward, e.g., madam, abba, 3, 44, 525.

One cool thing about Danny is that he leaves at least 20% tip when he eats out, e.g., if the meal is  $30,  Danny  leaves  $6  (30*.20)  for  tip.    If  the  tip  (20%)  is  not  a  whole  dollar  amount,  he  rounds up the tip to make it a whole number.  For example, if the meal is  $12, a 20% tip would be $2.40 (12*0.20) but Danny would leave $3 for tip.

Another cool thing about Danny is that he is a palindrome guru.  If his total bill (meal plus tip) is  not  a  palindrome,  he  will  increase  the  total  (by  adding  to  the  tip)  to  make  the  total  a  palindrome.  He will, of course, add the minimum needed to make the total a palindrome.

### The Problem:

Given Danny’s meal cost, your program should determine the tip amount for him (according to his rules) and the total bill.

### The Input:

The first input line contains a positive integer, n, indicating the number of times Danny ate out.  The meal costs are on the following n input lines, one per line.  Each input will contain an integer between 5 and 10000 (inclusive).

### The Output:

At the beginning of each test case, output “Input cost: c”   where c is the input cost.  Then, on the next output line, print the tip amount and the total bill, separated by one space.  Leave a blank line after the output for each test case.

Sample Input:
```
2
12
84
```

Sample Output:
```
Input cost: 12
10 22

Input cost: 84
17 101
```
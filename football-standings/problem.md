# Football Standings

Being an enterprising sort, you’ve started up your own internet World Cup Football Channel for streaming matches online. Recently you came up  with  the  idea  of  filling  up  the  time  between  matches  by  having  a  couple  of  ‘experts’  offer  critical analysis of games.   For this purpose, you have devised a unique ranking system for football teams, which you must now implement.  

### The Problem: 

Given  a  list  of  teams  and  a  list  of  match  scores,  you  must  compute  several  quantities  for  each  team.   These are: the total number of goals scored over all their games, the total number of goals scored  against  them  (goals  allowed,  for  short),  the  number  of  wins,  draws  and  losses,  and  the  number  of  points  scored  so  far.    Points  are  to  be  computed  as  follows:  winning  a  match  nets  a  team 3 points, losing gets them nothing.  In the event of a tie, both teams get 1 point.

In addition to this, you must order the teams correctly according to your new system.  Teams are ordered according to points, from highest to lowest.   In the event of a tie in points, the team that has  a  higher  goal  difference  comes  first.    The  goal  difference  is  defined  as  the  total  number  of  goals scored by the team minus the total number of goals scored against them.

If there is still a tie (i.e., two or more teams have the same points and the same goal differences), the  team  with  higher  total  goals  scored  comes  first.     If  even  this  is  tied,  the  team  whose  name  comes first in alphabetical order goes first.

### The Input: 

The  first  input  line  contains  a  positive  integer, n,  indicating  the  number  of  data  sets  to  be  processed.  The first line of each data set consists of two positive integers T (T ≤ 30) and G    (G≤400)  – the  number  of  teams  in  this  group  and  the  total  number  of  games  played  by  them.    The next line contains T unique names separated by single spaces.  Each name is a single uppercase word with no more than 15 characters.

Each  of  the  next G  input lines  will  contain  the  results  of  a  match.    Each  line  is  of  the  form  <country_1>   <score_1>   <country_2>   <score_2>.   For   example,   `Greece 2 Nigeria 1`   indicates that Greece and Nigeria played a game with score 2-1.  All four terms will be separated by single spaces.

### The Output: 

At  the  beginning  of  output  for  each  data  set,  output  “Group g:”   where g is  the  data  set  number,  starting  from  1.    Next  you  should  print  a  single  line  for  each  team,  ordering  teams  as  mentioned  above.  For  each  team,  the  line  you  print  should  be  of  the  form  “<name>  <points>  <wins>  <losses>  <draws>  <goals  scored>  <goals  allowed>”.   These  items  should  be  separated by single spaces.  Leave a blank line after the output for each data set.

**Sample Input:**
```
2
2 1
KASNIA LATVERIA
KASNIA 0 LATVERIA 1
4 6
ENGLAND USA ALGERIA SLOVENIA 
ENGLAND 1 USA 1
ALGERIA 0 SLOVENIA 1
SLOVENIA 2 USA 2
ENGLAND 0 ALGERIA 0
SLOVENIA 0 ENGLAND 1
USA 1 ALGERIA 0
```

**Sample Output:**
```
Group 1:
LATVERIA 3 1 0 0 1 0
KASNIA 0 0 1 0 0 1

Group 2:
USA 5 1 0 2 4 3
ENGLAND 5 1 0 2 2 1
SLOVENIA 4 1 1 1 3 3
ALGERIA 1 0 2 1 0 2
```
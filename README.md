# python-temel-project-with-patika
## Reverse List

* Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak: input: [[1, 2], [3, 4], [5, 6, 7]] output: [[[7, 6, 5], [4, 3], [2, 1]]

## Flatten
* Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak: input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5] output: [1,'a','cat',2,3,'dog',4,5]

## occurences of substring

* the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# exec function
* Input Format

The first line contains an integer,n , denoting the number of commands.
Each line  i of the n subsequent lines contains one of the commands described above.

* Constraints

The elements added to the list must be integers.
* Output Format

For each command of type print, print the list on a new line.

* Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
* Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

## Closures and Decorators
Let's dive into decorators! You are given  mobile numbers. Sort them in ascending order then print them in the standard format.
The given mobile numbers may have +91, 91  or 0  written before the actual 10 digit number. Alternatively, there may not be any prefix at all.
* Sample Input
 3
07895462130
919875641230
9195969878

* Sample Output
 +91 78954 62130
+91 91959 69878
+91 98756 41230

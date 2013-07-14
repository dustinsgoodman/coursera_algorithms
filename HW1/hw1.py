'''
Homework 1
Download the text file here. (Right click and save link as)
This file contains all of the 100,000 integers between 1 and
100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file
given, where the ith row of the file indicates the ith entry 
of an array.

Because of the large size of this array, you should implement
the fast divide-and-conquer algorithm covered in the video 
lectures. The numeric answer for the given input file should 
be typed in the space below.

=> 2407905288
'''
def merge_and_count(b,c):
    res_arr, inv_count = [], 0
    while len(b) > 0 or len(c) > 0:
        if len(b) > 0 and len(c) > 0:
            if b[0] < c[0]:
                res_arr.append(b[0])
                b = b[1:]
            else:
                res_arr.append(c[0])
                c = c[1:]
                inv_count += len(b)
        elif len(b) > 0:
            res_arr.append(b[0])
            b = b[1:]
        elif len(c) > 0:
            res_arr.append(c[0])
            c = c[1:]

    return res_arr, inv_count

def sort_and_count(a):
    arr_len = len(a)
    if arr_len <= 1:
        return a, 0
    b,x = sort_and_count(a[:(arr_len/2)])
    c,y = sort_and_count(a[(arr_len/2):])
    d,z = merge_and_count(b,c)

    return d, x+y+z

#Test Cases
t1 = [1,3,5,2,4,6]
print "Testing using", t1
print "Expecting:", 3
print "Returned:", sort_and_count(t1)[1]

t2 = [1,5,3,2,4]
print "\nTesting using", t2
print "Expecting:", 4
print "Returned:", sort_and_count(t2)[1]

t3 = [5,4,3,2,1]
print "\nTesting using", t3
print "Expecting:", 10
print "Returned:", sort_and_count(t3)[1]

t4 = [1,6,3,2,4,5]
print "\nTesting using", t4
print "Expecting:", 5
print "Returned:", sort_and_count(t4)[1]

t5 = [1,2,3,4,5,6]
print "\nTesting using", t5
print "Expecting:", 0
print "Returned:", sort_and_count(t5)[1]

print "\n\nFinal run against IntergerArray.txt"
with open('IntegerArray.txt', 'r') as f:
    print sort_and_count([int(l) for l in f])[1]

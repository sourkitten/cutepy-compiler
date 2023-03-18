#$ this is a simple test $#

#declare a, b, c, c_a, d

a = 100;
b = a + 10;
d = 10;
e = [0, 1, 2];

while ( b >= a ): #$ this is a random-ass comment that should be discarded $#
#{
    print(b);
    b = b -  1;
    c = a *  10;
    c = c // 9;
#}

if ( a == b ):
    c_a = 10;

d#$$#=5


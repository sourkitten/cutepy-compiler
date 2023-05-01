def main_factorial():
#{
	#$ declarations #$
	#declare x
	#declare i,fact
	#$ body of main_factorial #$
	x = int(input());
	fact = 1;
	i = 1;
	while (i<=x):
	#{
		fact = fact * i;
		i = i + 1;
	#}
	print(fact);
#}

def main_fibonacci():
#{
	#declare x
	def fibonacci(x):
	#{
		if (x<=1):
			return(x);
		else:
			return (fibonacci(x-1)+fibonacci(x-2));
	#}
	x = int(input());
	print(fibonacci(x));
#}

def main_countdigits():
#{
	#declare x, count
	x = int(input());
	count = 0;
	while (x>0):
	#{
		x = x // 10;
		count = count + 1;
	#}
	print(count);
#}

def main_primes():
#{
	#declare i
	def isPrime(x):
	#{
		#declare ibasic
		def divides(x,y):
		#{
			if (y == (y//x) * x):
				return (1);
			else:
				return (0);
		#}
		i = 2;
		while (i<x):
		#{
			if (divides(i,x)==1):
				return (0);
			i = i + 1;
		#}
		return (1);
	#}
	#$ body of main_primes #$
	i = 2;
	while (i<=30):
	#{
		if (isPrime(i)==1):
			print(i);
		i = i + 1;
	#}
#}

def main_test():
#{
	#declare x
	def max(a, b):
	#{
		if (a > b):
			return (a);
		else:
			return (b);
	#}
	x = max (max( 5, 7), max(8, 9));
	print(x);
#}

def main_ifWhile():
#{
	#declare c,a,b,t
	a=1;
	b=0;
	t=0;
	while ([a+b<1 and b<5]):
	#{
		if (t==1):
			c=2;
		else:
			if (t==2):
				c=4;
			else:
				c=0;
		while (a<1):
		#{
			if (a==2):
				while(b==1):
				#{
					c=2;
				#}
		#}
	#}
#}

def main_small():
#{
    #declare b,g,f
	def P1(X,Y):
	#{ 
		#declare e,f
		def P11(X):
		#{ 
			#declare e
			e=1;
			X=Y;
			f=b;
			return(e);
		#}
		#$ code for P1 #$
		b=X;
		e=P11(X);
		e=P1(X, Y);
		X=b;
		return(e);
	#}
	#$ code for main #$
	b=0;
	f=0;
	g=0;
	if ([b>1 and f<2 or g+1<f+b]):
		f=P1(g);
	else:
		f=1;
#}

if __name__ == "__main__":
	#$ call of main functions #$
	main_factorial();
	main_fibonacci();
	main_countdigits();
	main_primes();
	main_test();
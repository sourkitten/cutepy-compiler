def main_test():
#{
	#$ declarations #$
	#declare x,y,i
	x = 10;
	y = 1;
	i = 1;
	while (i<=x):
	#{
		while (y<=x):
		#{
			i = i + 1;
			y = y + 1;
		#}
	#}
	print(i);
	print(y);
#}

if __name__ == "__main__":
	#$ call of main functions #$
	main_test();
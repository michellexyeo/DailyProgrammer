# Makefile for DailyProgrammer puzzle
# Author: Michelle Yeo

tetris : solution.o
		 clang++ -stdlib=libc++ -std=c++11 -o pom solution.o -Wc++11-extensions 

solution.o : solution.cpp
		 cc -c solution.cpp

clean : 
	rm pom *.o

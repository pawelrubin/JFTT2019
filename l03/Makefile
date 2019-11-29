all: calc.tab lexer.l.c
	g++ -o calc calc.tab.cpp lexer.l.c -lm

lexer.l.c: lexer.l
	flex -o lexer.l.c lexer.l

calc.tab: calc.ypp
	bison -d calc.ypp

clean:
	rm calc.tab.* lexer.l.*

cleanall:
	rm calc

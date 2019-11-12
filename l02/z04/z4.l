%{
#include <iostream>
#include <stack>
#include <cmath>
#include <string>

std::stack<int> calc_stack;
std::string error = "";

void handle_error(std::string error_message)
{
  error = error_message;
  calc_stack = std::stack<int>();
}

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }
int mod(int a, int b) { return a % b; }
int power(int a, int b) { return pow(a, b); }
int divide(int a, int b) 
{
  if (b != 0) { return a / b; }
  else {
    handle_error("Pamiętaj cholero nie dziel przez zero xD!!!");
  }
}

void calc(int (*operation)(int, int))
{
  if (calc_stack.size() > 1) {
    int a = calc_stack.top();
    calc_stack.pop();
    int b = calc_stack.top();
    calc_stack.pop();
    calc_stack.push(operation(b, a));
  } else {
    handle_error("Za mała liczba argumentów!!!");
  }
}

void result()
{
  if (calc_stack.size() > 1) {
    handle_error("Za mała liczba operatorów!!!");
  }
  if (calc_stack.size() == 1 && error == "") {
    std::cout << "= " << calc_stack.top() << std::endl;
    calc_stack.pop();
  } else {
    std::cout << error << std::endl;
    error = "";
  }
}

%}

%x ERROR

%%

\-?[0-9]+   {calc_stack.push(std::stoi(yytext));}
\+          calc(&add);
\-          calc(&sub);
\*          calc(&mul);
\/          calc(&divide);
\%          calc(&mod);
\^          calc(&power);
\n          result();
" "         ;
.           { handle_error(std::string("Zły symbol!!! - ") + yytext); BEGIN(ERROR); }
<ERROR>{
  .|\n      BEGIN(0);
}
%%

int yywrap() {}

int main() {
  return yylex();
}

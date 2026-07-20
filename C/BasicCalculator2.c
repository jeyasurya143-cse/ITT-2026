#include <ctype.h>

int calculate(char* s) {
    long long current_num = 0;
    int last_term = 0;
    int total_sum = 0;
    char op = '+';

    for (int i = 0; s[i] != '\0'; i++) {
        if (isdigit(s[i])) {
            current_num = current_num * 10 + (s[i] - '0');
        }

        if ((!isdigit(s[i]) && s[i] != ' ') || s[i + 1] == '\0') {
            if (op == '+') {
                total_sum += last_term;
                last_term = current_num;
            } else if (op == '-') {
                total_sum += last_term;
                last_term = -current_num;
            } else if (op == '*') {
                last_term = last_term * current_num;
            } else if (op == '/') {
                last_term = last_term / current_num;
            }

            op = s[i];
            current_num = 0;
        }
    }

    return total_sum + last_term;
}

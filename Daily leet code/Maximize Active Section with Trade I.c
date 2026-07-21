#include <stdio.h>
#include <string.h>

int maxActiveSectionsAfterTrade(const char* s) {
    int n = strlen(s);
    int total_ones = 0;
    int max_any_zero = 0;
    
    int current_zero_run = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') {
            total_ones++;
            if (current_zero_run > max_any_zero) {
                max_any_zero = current_zero_run;
            }
            current_zero_run = 0;
        } else {
            current_zero_run++;
        }
    }
    if (current_zero_run > max_any_zero) {
        max_any_zero = current_zero_run;
    }
    
    int max_gain = 0;
    int i = 0;
    while (i < n) {
        if (s[i] == '1') {
            int start_one = i;
            while (i < n && s[i] == '1') {
                i++;
            }
            int end_one = i;
            
            if (start_one > 0 && end_one < n) {
                int ones_len = end_one - start_one;
                
                int left_zero_len = 0;
                int idx = start_one - 1;
                while (idx >= 0 && s[idx] == '0') {
                    left_zero_len++;
                    idx--;
                }
                
                int right_zero_len = 0;
                idx = end_one;
                while (idx < n && s[idx] == '0') {
                    right_zero_len++;
                    idx++;
                }
                
                int merged_zero_len = left_zero_len + ones_len + right_zero_len;
                int chosen_zero_len = (merged_zero_len > max_any_zero) ? merged_zero_len : max_any_zero;
                
                int current_gain = chosen_zero_len - ones_len;
                if (current_gain > max_gain) {
                    max_gain = current_gain;
                }
            }
        } else {
            i++;
        }
    }
    
    return total_ones + max_gain;
}

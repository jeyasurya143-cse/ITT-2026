#include <string.h>
#include <stdlib.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) return "";

    char* prefix = strs[0];

    for (int i = 1; i < strsSize; i++) {
        while (strstr(strs[i], prefix) != strs[i]) {
            int current_len = strlen(prefix);
            if (current_len == 0) return "";
            prefix[current_len - 1] = '\0';
        }
    }

    return prefix;
}

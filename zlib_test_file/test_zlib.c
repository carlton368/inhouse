#include <stdio.h>
#include <zlib.h>

int main() {
    const char *version = zlibVersion();
    printf("Zlib version: %s\n", version);
    return 0;
}

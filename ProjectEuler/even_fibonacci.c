int evenFibo(){
    int a = 1, b = 2;
    int c = a + b;
    int sum = b;
    do {
        if (c % 2 == 0)
            sum += c;
        a = b;
        b = c;
        c = a + b;
    } while (c <= 4000000);
    return sum;
}

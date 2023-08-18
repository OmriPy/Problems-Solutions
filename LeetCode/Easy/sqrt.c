int mySqrt(int x){
    if (x == 0 || x == 1){
        return x;
    }
    unsigned int a = 1;
    unsigned int b = 2;
    while (1){
        if (a*a == x) return a;
        if (b*b == x) return b;
        if (a*a < x && b*b > x){
            return a;
        }
	    a++;
	    b++;
    }
}

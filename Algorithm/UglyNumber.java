class Solution {
    public boolean isUgly(int num) {
        // if (num == 0) { //可以放在下面while循环中判断 
        //     return false;
        // }
        int[] factors = {2, 3, 5};
        for (int factor : factors) {
            while (num != 0 && num % factor == 0) {
                num /= factor;
            }
        }
        return num == 1;
    }
}

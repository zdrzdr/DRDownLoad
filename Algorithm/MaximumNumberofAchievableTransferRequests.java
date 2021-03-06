// Solution: Combination
// Try all combinations: O(2^n * (r + n))
// Space complexity: O(n)
class Solution {
    public int maximumRequests(int n, int[][] requests) {
        final int r = requests.length;
        int[] nets = new int[n];
        int ans = 0;
        for (int s = 0; s < (1 << r); ++s) {
            Arrays.fill(nets, 0);
            for (int j = 0; j < r; ++j) 
                if ((s & (1 << j)) != 0) {
                    --nets[requests[j][0]];
                    ++nets[requests[j][1]];
                }
            if (check(nets))
                ans = Math.max(ans, Integer.bitCount(s)); // 记住Java对应的C++的__builtin_popcount为Integer.bitCount！！！
        }
        return ans;
    }
    private boolean check(int[] nets) {
        for (int e : nets) // 当nets数组为空时，不会进入循环，所以不用担心nets数组为空的情况。
            if(e != 0) return false;
        return true;
    }
}

class Solution {
    public int numberOfSteps(int num) {
        return reducer(num,0);
    }
    static int reducer(int num,int count){
        if (num == 0)return count;

        if (num % 2 == 0) return reducer(num/2,++count);
        else return reducer(--num,++count);
    }
}
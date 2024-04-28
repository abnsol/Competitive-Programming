class CustomStack {
    int[] stack;
    int maxSize;
    int top = -1;

    public CustomStack(int maxSize) {
        stack = new int[maxSize];
        this.maxSize = maxSize;
    }
    
    public void push(int x) {
        top++;
        if (top >= maxSize) {
            top--;
            return;
            }
        stack[top] = x;
    }
    
    public int pop() {
        if (top == -1)return -1;
        return stack[top--];
    }
    
    public void increment(int k, int val) {
        int idx = 0;
        while (idx <= top && idx < k){
            stack[idx++] += val;
        } 
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */
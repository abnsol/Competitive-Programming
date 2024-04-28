class MyStack {
    ArrayDeque<Integer> first;
    ArrayDeque<Integer> second;
    public MyStack() {
        first = new ArrayDeque();
        second = new ArrayDeque();
    }
    public void push(int x) {
        this.first.add(x);
    }
    
    public int pop() {
        int n = this.first.size();
        for (int i = 0; i < n - 1;i++){
            this.second.add(this.first.poll());
        }
        int popped = this.first.poll();
        while (!this.second.isEmpty()){
            this.first.add(this.second.poll());
        }
        return popped;        
    }
    
    public int top() {
        int n = this.first.size();
        for (int j = 0; j < n - 1; j++){
            this.second.add(this.first.poll());
        }

        int peeked = this.first.poll();
        while (!this.second.isEmpty()){
            this.first.add(this.second.poll());
        }
        this.first.add(peeked);
        return peeked;
    }
    
    public boolean empty() {
        return this.first.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
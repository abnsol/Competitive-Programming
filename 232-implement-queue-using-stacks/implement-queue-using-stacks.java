class MyQueue {
    Stack<Integer> first;
    Stack<Integer> second;

    public MyQueue() {
        first = new Stack();
        second = new Stack();
    }
    
    public void push(int x) {
        this.first.push(x);
    }
    
    public int pop() {
        while (!this.first.empty()){
            this.second.push(this.first.pop());
        }
        int popped = this.second.pop();

        while (!this.second.empty()){
            this.first.push(this.second.pop());
        }
        return popped;
    }
    
    public int peek() {
        while (!this.first.empty()){
            this.second.push(this.first.pop());
        }
        int peeked = this.second.peek();

        while (!this.second.empty()){
            this.first.push(this.second.pop());
        }
        return peeked;
    }
    
    public boolean empty() {
        return this.first.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
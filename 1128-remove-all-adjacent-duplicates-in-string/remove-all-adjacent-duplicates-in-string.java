class Solution {
    public String removeDuplicates(String s) {
        List<Character> stack = new ArrayList<Character>();
        char[] charArray = s.toCharArray();

        for (char c: charArray){
            if(!stack.isEmpty() && stack.get(stack.size() - 1) == c){
                stack.remove(stack.size() - 1);
            }
            else{
                stack.add(c);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (char c:stack){
            sb.append(c);
        }
        return sb.toString();
    }
}
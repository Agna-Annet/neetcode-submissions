class Solution {
    public String minRemoveToMakeValid(String str) {
        ArrayList<Integer> stack = new ArrayList<>();
        ArrayList<Integer> remove = new ArrayList<>();
        char[] s = str.toCharArray();
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<s.length;i++)
        {
            if(s[i]=='(')
                stack.add(i);
            else if (s[i]==')')
                if (stack.isEmpty())
                    remove.add(i);
                else
                    stack.remove(stack.size()-1);
        }
        for(int j=0;j<stack.size();j++)
        {
            remove.add(stack.get(j));
        }
        for(int i=0;i<s.length;i++)
        {
            if(!remove.contains(i))
                sb.append(s[i]);
        }
        String st= sb.toString();
        return st;    
    }
}
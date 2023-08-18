public class Solution {

    static string brackets = "()[]{}" ;
    
    public bool Start(char c){
        return c == brackets[0] || c == brackets[2] || c == brackets[4];
    }
    public bool End(char c){
        return c == brackets[1] || c == brackets[3] || c == brackets[5];
    }

    public bool IsValid(string s) {
        Stack<char> stk = new Stack<char>();
        foreach (char c in s){
            if (Start(c)){
                stk.Push(c);
            }
            else if (End(c)){
                if (stk.Count == 0 || stk.Peek() != brackets[brackets.IndexOf(c) - 1])
                    return false;
                else
                    stk.Pop();
            }
        }
        return stk.Count == 0;
    }
}

public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] == val)
            {
                nums[i] = -1;
            }
            else k++;
        }
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] == -1)
            {
                for (int j = i + 1; j < nums.Length; j++)
                {
                    if (nums[j] != -1)
                    {
                        nums[i] = nums[j];
                        nums[j] = -1;
                        break;
                    }
                }
            }
        }
        return k;
    }
}

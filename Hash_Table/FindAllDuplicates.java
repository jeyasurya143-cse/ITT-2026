import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        int n = nums.length;
        List<Integer> result = new ArrayList<>();
        
        Arrays.sort(nums);
        
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                result.add(nums[i]);
            }
        }
        
        return result;
    }
}

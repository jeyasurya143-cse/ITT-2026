class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        int[] result = new int[n1];
        int p = 0;   
        for (int i = 0; i < n1; i++) {
            for (int j = 0; j < n2; j++) {
                if (nums1[i] == nums2[j]) {
                    boolean isDuplicate = false;
                    for (int k = 0; k < p; k++) {
                        if (nums1[i] == result[k]) {
                            isDuplicate = true;
                            break;
                        }
                    }    
                    if (!isDuplicate) {
                        result[p] = nums1[i];
                        p++;
                    }
                }
            }
        }
        int[] finalResult = new int[p];
        for (int i = 0; i < p; i++) {
            finalResult[i] = result[i];
        }
        return finalResult;
    }
}


import java.util.ArrayList;
import java.util.List;

public class sortByParity {
    public static int[] sortArrayByParity(int[] nums) {
        List<Integer> even = new ArrayList();
        List<Integer> odd = new ArrayList();
        
        for (int i: nums) {
            if (i%2 == 0) {
                even.add(i);
            } else {
                odd.add(i);
            }
        }
        
        List<Integer> result = new ArrayList<>();
        result.addAll(even);
        result.addAll(odd);
        
        int[] finalResult = new int[nums.length];
        
        for (int i = 0; i < result.size(); i++) {
            finalResult[i] = result.get(i);
        }
        
        return finalResult;
    }
    public static void main(String[] args) {
        sortByParity check = new sortByParity();
        int[] nums = {3, 1, 2, 4};
        int[] ans = check.sortArrayByParity(nums);
        System.out.println("run");
    }
}

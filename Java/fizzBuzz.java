public class Solution {
    public static List<String> fizzBuzz(int n) {
        // Initialize the list with type String
        List<String> answer = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                answer.add("FizzBuzz");
            } else if (i % 3 == 0) {
                answer.add("Fizz");
            } else if (i % 5 == 0) {
                answer.add("Buzz");
            } else {
                // Convert integer to string and add it to the list
                answer.add(Integer.toString(i));
            }
        }
        return answer;
    }
    
    }
}

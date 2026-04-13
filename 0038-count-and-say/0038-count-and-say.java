class Solution {
    public String countAndSay(int n) {
        if (n <= 0) return "";
        String result = "1";
        
        for (int i = 1; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            int count = 1;
            
            for (int j = 0; j < result.length(); j++) {
                // If the next character is the same, increase the count
                if (j + 1 < result.length() && result.charAt(j) == result.charAt(j + 1)) {
                    count++;
                } else {
                    // Otherwise, append count followed by the digit
                    sb.append(count).append(result.charAt(j));
                    count = 1; // Reset count for the next unique digit
                }
            }
            result = sb.toString();
        }
        
        return result;
    }
}

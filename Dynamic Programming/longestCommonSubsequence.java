class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        
        int[][] cache = new int[text2.length() + 1][text1.length()+1];
        
        for(int text2Row = 0; text2Row <= text2.length(); text2Row++){
            for(int text1Col = 0; text1Col <= text1.length(); text1Col++){
                if (text2Row == 0 || text1Col == 0){
                    cache[text2Row][text1Col] = 0;
                } else if (text2.charAt(text2Row - 1) == text1.charAt(text1Col - 1)) { //if letters are the same
                    cache[text2Row][text1Col] = cache[text2Row-1][text1Col-1] + 1;
                }
                //if letters are not the same
                else {
                    cache[text2Row][text1Col] = Math.max(cache[text2Row-1][text1Col], cache[text2Row][text1Col-1]);
                }
            }
        }
        
        return cache[text2.length()][text1.length()];
    }
}
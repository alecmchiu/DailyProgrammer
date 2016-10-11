/*
 * Challenge I3
 * https://www.reddit.com/r/dailyprogrammer/comments/pkwb1/2112012_challenge_3_intermediate/
 */

import java.util.ArrayList;

public class Main {


    public static String encode(String text) {
        char[] characters = text.toCharArray();
        char[] char_new = new char[characters.length];
        for (int i = 0; i < characters.length; ++i) {
            int num = (int) (characters[i]) - 32 + i;
            if (num > 94) {
                num = (num % 94);
            }
            char_new[i] = (char) (num+32);
        }
            String encrypted = new String(char_new);
            return encrypted;
    }

    public static String decode(String text){
        char[] characters = text.toCharArray();
        char[] decoded = new char[characters.length];
        for (int i = 0; i < characters.length; ++i){
            int num = (int) (characters[i]) - 32 - i;
            if (num < 0){
                int shift_from_end = Math.abs(num)%94;
                num = 94 - shift_from_end;
            }
            decoded[i] = (char)(num+32);
        }
        return new String(decoded);
    }

    public static void main(String[] args) {
        String t = "I am not a half-baked potato! I'm a couch potato!";
        System.out.println(t);
        String e = encode(t);
        System.out.println(e);
        System.out.println(decode(e));
    }
}

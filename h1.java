import java.util.Scanner;

/**
 * Created by Alec on 9/1/16.
 */
public class h1 {
    public static void main(String[] args){
        int guess = 50;
        int upperbound = 100;
        int lowerbound = 1;
        boolean found = false;
        Scanner input = new Scanner(System.in);
        while (found != true){
            System.out.println("Is your number " + guess + "?(Y/N)");
            if (input.next().equalsIgnoreCase("Y")){
                found = true;
            }
            else {
                System.out.println("Higher or lower?");
                if(input.next().equalsIgnoreCase("Higher")){
                    lowerbound = guess;
                    guess += (upperbound - lowerbound)/2;
                }
                else {
                    upperbound = guess;
                    guess -= (upperbound - lowerbound)/2;
                }
            }
        }
        System.out.println("Your number is " + guess + "!");
    }
}

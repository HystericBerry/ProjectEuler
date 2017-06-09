import java.math.BigInteger;
/**
 * Problem 1
 * Title:    Multiples of 3 or 5
 * Author:   Paul Kim
 * Date:     6/9/2017
 *
 * Description
 * If we list all the natural numbers below 10 that are multiples of 3 OR 5, we
 * get 3, 5, 6, and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */
public class Problem1
{
  public static void main(String[] args)
  {
    String format = "sum of all 3 or 5 multiples below %d is: %s.\n";

    int upperBound = 1000;
    BigInteger sum = threeFiveSum(upperBound);

    // sum of all 3 or 5 multiples below 1000 is: 233168.
    System.out.printf(format, upperBound, sum.toString());
  }

  private static BigInteger threeFiveSum( int upperBound )
  {
    BigInteger sum = BigInteger.ZERO;
    int i, isThree = 0, isFive = 0;
    boolean isEither;
    for(i = 1; i < upperBound; ++i )
    {
      isEither = false;
      if( ++isThree == 3 )
      {
        isEither = true;
        isThree = 0;
      }
      if( ++isFive == 5 )
      {
        isEither = true;
        isFive = 0;
      }

      if( isEither )
        sum = sum.add(BigInteger.valueOf(i));
    }

    return sum;
  }
}

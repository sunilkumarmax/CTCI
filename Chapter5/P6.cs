namespace Chapter5
{
    public class P6
    {
        /// <summary>
        /// Conversion
        /// </summary>
        /// <param name="a"></param>
        /// <param name="b"></param>
        /// <returns></returns>
        public int ConvertNumbers(int a, int b)
        {
            int x = a ^ b;
            int count = 0;
            while (x > 0)
            {
                if ((x & 1) > 0)
                {
                    count++;
                }
                x >>= 1;
            }
            return count;
        }
    }
}
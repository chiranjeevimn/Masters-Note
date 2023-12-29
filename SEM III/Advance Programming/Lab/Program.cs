using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Program_3_B
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] n = new int[6] { 66, 33, 56, 23, 81 ,1};
            int i = 0;
            int sum = 0;
            try
            {
                for (i = 0; i < 6; i++)
                {
                    sum += n[i];
                }
                Console.WriteLine("Sum is : " + sum);
                Console.ReadKey();
            }
            catch (IndexOutOfRangeException e)
            {
                Console.WriteLine(e.Message);
            }
            Console.ReadKey();
        }
    }
}

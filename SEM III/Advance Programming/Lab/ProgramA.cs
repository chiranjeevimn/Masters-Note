using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Program_3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Numerator");
            int p = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter the numerator");
            int q = int.Parse(Console.ReadLine());
            try
            {
                int r = p / q;
                Console.WriteLine("The value of quotient is {0} ", r);
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
            }
            Console.ReadKey();
        }
    }
}

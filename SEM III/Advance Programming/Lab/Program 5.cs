using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Program_5
{
    public delegate int deli(int a, int b);
    public class prg9
    {
        public int sum(int a, int b)
        {
            return a + b;
        }
        public int diff(int a, int b)
        {
            return a - b;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            prg9 p = new prg9();
            deli d = p.sum;
            int r = 20;
            int q = 30;
            int i = d(r,q);
            prg9 p2 = new prg9();
            deli f = p2.diff;
            int m = 40;
            int n = 20;
            int j = f(m,n);
            Console.WriteLine("The sum is " + i + "\nThe Difference is " + j);
            Console.ReadKey();
        }
    }
}

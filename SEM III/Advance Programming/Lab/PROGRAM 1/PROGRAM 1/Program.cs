using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PROGRAM_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("The number of arguments are: {0}", args.Length);
            for (int i = 0; i < args.Length; i++)
                Console.WriteLine("argument {0} is {1} ", i + 1, args[i]);
            Console.ReadLine();
        }
    }
}

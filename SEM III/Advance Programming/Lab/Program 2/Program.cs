using System;

namespace Program_2
{
    class Program
    {
        static void Main(string[] args)
        {
            int[][] jag;
            int i, j, var, sum = 0;
            Console.WriteLine("Enter the number of rows ");
            int row = int.Parse(Console.ReadLine());
            jag = new int[row][];

            for (i = 0; i < row; i++)
            {
                Console.WriteLine("Enter the number of elements in row {0}: ", i + 1);
                var = int.Parse(Console.ReadLine());
                jag[i] = new int[var];

                Console.WriteLine("Enter the {0} values", var);
                for (j = 0; j < var; j++)
                    jag[i][j] = int.Parse(Console.ReadLine());

                Console.WriteLine();
            }

            Console.WriteLine("jag[{0}][]:", row);

            for (i = 0; i < row; i++)
            {
                for (j = 0; j < jag[i].Length; j++)
                {
                    Console.Write(" " + jag[i][j]);
                    sum = sum + jag[i][j];
                }
                Console.WriteLine();
            }

            Console.WriteLine("Sum of the Jagged Array : "+sum);
            Console.ReadLine();
        }
    }
}

using System;

class QuadraticRoots
{
    static void Main()
    {
        Console.WriteLine("Quadratic Equation Solver");
        Console.WriteLine("Enter the coefficients of the quadratic equation (ax^2 + bx + c = 0):");

        Console.Write("Enter a: ");
        double a = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter b: ");
        double b = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter c: ");
        double c = Convert.ToDouble(Console.ReadLine());

        // Calculate the discriminant
        double discriminant = b * b - 4 * a * c;

        if (discriminant > 0)
        {
            // Two real and distinct roots
            Console.WriteLine("\n THE ROOTS ARE REAL AND DISTINCT ROOTS \n");  
            double root1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
            double root2 = (-b - Math.Sqrt(discriminant)) / (2 * a);

            Console.WriteLine("Root 1: " + root1);
            Console.WriteLine("Root 2: " + root2);
        }
        else if (discriminant == 0)
        {
            // One real root (double root)
            Console.WriteLine("\n THE ROOTS ARE REPEATED ROOTS \n"); 
            double root = -b / (2 * a);
            Console.WriteLine("Double Root:  " + root);
        }
        else
        {
            // Complex roots
            Console.WriteLine("\n THE ROOTS ARE IMAGINARY ROOTS\n"); 
            double realPart = -b / (2 * a);
            double imaginaryPart = Math.Sqrt(-discriminant) / (2 * a);

            Console.WriteLine("Root 1: " + realPart + " + " + imaginaryPart + "i");
            Console.WriteLine("Root 2: " + realPart + " - " + imaginaryPart + "i");
        }

        Console.ReadLine();
    }
}

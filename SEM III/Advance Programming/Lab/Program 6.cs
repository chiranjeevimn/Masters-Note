using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Program_6
{
    public abstract class Shape
    {
        public abstract void draw();
    }
    public class Rectangle : Shape
    {
        public override void draw()
        {
            Console.WriteLine("Drawing rectangle...");
        }
    }
    public class Circle : Shape
    {
        public override void draw()
        {
            Console.WriteLine("Drawing circle...");
        }
    }
    public class TestAbstract
    {
        public static void Main()
        {
            Shape s;
            s = new Rectangle();
            s.draw();
            s = new Circle();
            s.draw();
            Console.ReadKey();
        }
    }
}

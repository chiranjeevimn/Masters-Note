using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Program_4
{
    class baseclass
    {
        public virtual string city()
        {
            return "BMSCE";
        }
    }
    class Derivedclass:baseclass
    {
        public override string city()
        {
            return "BMSIT";
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Derivedclass o = new Derivedclass();
            string str = o.city();
            Console.WriteLine("College name is {0}", str);
            Console.ReadKey();
        }
    }
}

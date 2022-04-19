using System;
using Deep;

namespace ExampleProgram
{
    class ExapmleProgram
    {
        static void Main(string[] args)
        {
            var net = new Net(new int[] { 2, 4, 3 });
            foreach (float x in net.FireAll(new float[] { 4, 3 }))
            {
                Console.WriteLine(x);
            }
        }
    }
}

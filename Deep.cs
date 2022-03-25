using System;
using System.Linq;


namespace Deep
{
    /// <summary>
    /// A neural network capable of deep learning.
    /// </summary>
    public class Net
    {
        /// <summary>
        /// Represents a node in a neural network.
        /// </summary>
        private class Node
        {
            /// <summary>
            /// The activation of the node.
            /// </summary>
            public double a;
            /// <summary>
            /// The bias of the node.
            /// </summary>
            public double b;
            /// <summary>
            /// The weights of the node.
            /// </summary>
            public double[] w;
            /// <summary>
            /// Creates a new node with an undefiened list of weights and a bias;
            /// </summary>
            /// <param name="b">The bias of the created node.</param>
            public Node(double b = 0) => this.b = b;
            /// <summary>
            /// The sigmoid activation function.
            /// </summary>
            /// <param name="x">The number to be activated.</param>
            /// <returns>One divided by one plus <see cref="Math.E"/> raised to the power of negative <paramref name="x"/>.</returns>
            public static double Sigmoid(double x) => 1 / (1 + Math.Exp(-x));
        }
        /// <summary>
        /// A 2d representation of the <see cref="Node"/>s in the network.
        /// </summary>
        private Node[][] web;
        /// <summary>
        /// Creates a new <see cref="Net"/> with a specified amount of <see cref="Node"/>s in each layer.
        /// </summary>
        /// <param name="layer_depth">Represents the amount of layers and the amount of <see cref="Node"/>s in each.
        /// <para>Ex: <paramref name="layer_depth"/> = [3, 5, 2] (3 <see cref="Node"/>s in the first layer, 5 <see cref="Node"/>s in the second and 2 in the third)</para>
        /// </param>
        public Net(int[] layer_depth)
        {
            web = new Node[layer_depth.Length][];
            foreach (int x in Enumerable.Range(0, layer_depth.Length))
            {
                web[x] = new Node[layer_depth[x]];
                foreach (int y in Enumerable.Range(0, layer_depth[x]))
                {
                    web[x][y] = new Node(); // bias
                    if (x == 0) continue;
                    web[x][y].w = new double[web[x - 1].Length];
                    foreach (int _y in Enumerable.Range(0, web[x - 1].Length))
                        web[x][y].w[_y] = 1; // weights
                }
            }
        }
        /// <summary>
        /// Fires all <see cref="Node"/>s in order of layer.
        /// </summary>
        /// <param name="inputs">What to set the <see cref="Node.a"/> of each input <see cref="Node"/>. Does not include bias.</param>
        /// <returns>The activations of the output layer. Includes bias.</returns>
        public double[] FireAll(float[] inputs)
        {
            foreach (int y in Enumerable.Range(0, web[0].Length))
                web[0][y].a = Node.Sigmoid(inputs[y] + web[0][y].b);

            foreach (int x in Enumerable.Range(0, web.Length))
            {
                if (x == 0) continue;
                foreach (int y in Enumerable.Range(0, web[x].Length))
                {
                    web[x][y].a = web[x][y].b;
                    foreach (int _y in Enumerable.Range(0, web[x - 1].Length))
                        web[x][y].a += web[x - 1][_y].a * web[x][y].w[_y];
                    web[x][y].a = Node.Sigmoid(web[x][y].a);
                }
            }
            double[] o = new double[web[web.Length - 1].Length];

            foreach (int y in Enumerable.Range(0, web[web.Length - 1].Length))
                o[y] = web[web.Length - 1][y].a;

            return o;
        }

        public void SetBias(int layer, int index, double bias) => web[layer][index].b = bias;
    }

    /// <summary>
    /// A collection of static matrix manipulation methods.
    /// </summary>
    public static class Matrix
    {
        public static double DotProduct(double[][] x, double[][] y)
        {
            return 0;
        }
    }
}
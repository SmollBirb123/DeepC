import numpy, matplotlib.pyplot
import net, net2

trainingFile = ""
testingFile = ""

input_nodes = 1
hidden_nodes = 2
output_nodes = 1

learning_rate = 0.3

# Setting up the neural network
n = net2.neuralNetwork(input_nodes, hidden_nodes, output_nodes,learning_rate)
print(n.query([7.0]))

# Setting up the MNIST Dataset

# TRAINING FILES
# train_data_file = open(trainingFile, 'r')
# train_data_list = train_data_file.readlines
# train_data_file.close()

# all_values = train_data_list[0].split(',')

# first rescale the input color values from 0 - 255 to 0 - 1
# we don't have to worry about the inputs being 1.0 but we should avoid the impossible 1.0 output
# scaled_input = numpy.asfarray(all_values[1:] / 255.0 * 0.99) + 0.01
# print(scaled_input)

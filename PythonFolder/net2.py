import numpy, scipy.special
class neuralNetwork:
    
    #initialisation setup input hidden and output nodes/layers
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #set number of nodes for each layers
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # linking weight matries, wih - weight_inputhidden and who - weight_hiddenoutput
        # weights inside the arrays are w_i_j
        # linking node i to node j in the next layer
        # w11 w21
        # w12 w22
        self.wih = (numpy.random.rand(self.hnodes, self.inodes) - 0.5) #subtracting 0.5 here allows weights to be negative
        self.who = (numpy.random.rand(self.onodes, self.hnodes)- 0.5)

        # optional normal distribution weights for more sophistication
        # https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
        # self.wih = (numpy.random.normal(0.0, pow(self.inodes- 0.5), (self.hnodes, self.inodes))
        # self.wih = (numpy.random.normal(0.0, pow(self.hnodes- 0.5), (self.onodes, self.hnodes))

        # learning rate
        # -learning rate helps us moderate the strength of change for our training
        # denoted by alpha in MYONN Tariq Rashid
        self.lr = learningrate

        #X being the weight(?) times input in hidden layer
        #activation function is the sigmoid function
        #basically lambda is a quick way to create short functions
        #scipy calls sigmoid as expit
        #translated to def sigmoidFunc(x): sigmoid * x
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    #training/refining weights
    def train():
        pass

    #answers from output nodes
    def query(self, inputs_list):

        #convert inputs list to 2d array (2x2 array)
        #Why a 2by2?
        #Double check numpy documentation for array().T function
        inputs = numpy.array(inputs_list, ndmin=2).T

        # dot product between layers to find X_hidden = Weight_input-hidden * Inputs
        # signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)

        # signals from hidden layer
        # O_hidden = sigmoid(X_hidden function)
        hidden_outputs = self.activation_function(hidden_inputs)

        # signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)

        # signals from output layer with sigmoid function'
        final_outputs = self.activation_function(final_inputs)

        return final_outputs




import numpy as np

class DetectNumber():
    
    def __init__(self):
        np.random.seed(1)
        
        self.synaptic_weights=2 * np.random.random((7,1))-1
        
    def sigmoid(self, x):
        return 1/(1+np.exp(-x))
        
    def sigmoid_derivative(self, x):
        return x* (1-x)
        
    def train(self,training_inputs, training_outputs, training_iterations):
        
        
        for iteration in range(training_iterations):
        
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments
            
    def think(self, inputs):
    
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        
        return output
        
        
if __name__ == "__main__":
    
    detect_number = DetectNumber()
    
    print("Random Jin(weights):")
    print(detect_number.synaptic_weights)
    
    
    training_inputs = np.array([[1,1,1,1,1,0,1],
                                [1,1,1,1,1,1,1],
                                [0,1,1,1,0,0,0],
                                [1,1,0,1,1,1,1],
                                [1,1,0,1,1,0,1],
                                [1,0,1,1,0,0,1],
                                [0,1,1,1,1,0,1],
                                [0,1,1,0,1,1,1],
                                [0,0,1,1,0,0,0],
                                [0,0,0,0,0,0,0],
                                [1,1,1,1,1,0,0],
                                [0,0,1,1,1,1,1],
                                [0,0,1,1,1,0,0],
                                [0,0,1,1,1,1,0],
                                [0,1,1,1,1,1,0],
                                [1,1,1,1,0,0,0],
                                [0,1,1,1,1,1,1],
                                [1,1,1,1,0,1,0],
                                [1,1,1,1,1,0,0],
                                [1,1,1,0,1,0,0],
                                [1,1,1,0,0,0,0],
                                [1,0,0,0,0,0,0],
                                [0,1,0,0,0,0,0],
                                [0,0,1,0,0,0,0],
                                [0,0,0,1,0,0,0],
                                [0,0,0,0,1,0,0],
                                [0,0,0,0,0,1,0],
                                [0,0,0,0,0,0,1],
                                [1,1,0,0,0,0,0],
                                [0,1,1,1,1,1,1],
                                [0,1,0,0,1,1,1],
                                [0,0,0,0,1,1,1],
                                [0,0,0,1,1,1,1],
                                [1,1,1,1,1,1,0]])
    
    training_outputs = np.array([[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]).T
    
    
    
    detect_number.train(training_inputs,training_outputs,200000)
    i=1
    while i>0:
        
        print("Surgalt hiisnii daraagaar jin(weights) : ")
        print(detect_number.synaptic_weights)
        
        A = str(input("Input 1:"))
        B = str(input("Input 2:"))
        C = str(input("Input 3:"))
        D = str(input("Input 4:"))
        E = str(input("Input 5:"))
        F = str(input("Input 6:"))
        G = str(input("Input 7:"))

                
        print("Shine shalgah ogogdol = ",A,B,C,D,E,F,G)
        print("ur dun:")
        result = detect_number.think(np.array([A,B,C,D,E,F,G]))
        print(result)
        
        if result >= 0.9 and  result <= 0.99999999:
            print("10-n system-n too mon")
        else:
            print ("10-n system-n too bish")
                    
                   
        print("Dahin test hiih bol 1. Duusgah bol 0  = ") 
        i=int(input())
        
        
   
    
        
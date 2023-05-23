import random
import json
import torch
from brain import neuralNetwork
from brain2 import Bag_Of_Words,token_size

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)


FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = neuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# From here we start to write the code for my personal assistant......


Name = "David"

from listen import Listen
from Speak import Say
def Main():
    sentence = Listen()
    if sentence == "bye":
        exit()

    sentence = token_size(sentence)
    X = Bag_Of_Words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _ , predicted = torch.max(output,dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                reply = random.choice(intent["response"])
                Say(reply)

while True:
    Main()

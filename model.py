import cv2

import IPython.display
from IPython.display import clear_output

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.models import resnet18, mobilenet_v3_small
from torch.optim import Adam
from tqdm import tqdm

from easyfsl.data_tools import TaskSampler
from easyfsl.utils import plot_images, sliding_average
from easyfsl.data_tools import EasySet, TaskSampler
from easyfsl.methods import PrototypicalNetworks
# from easyfsl.methods import AbstractMetaLearner


import os
from os import listdir

from PIL import Image
import json

path = './dataset/train/'

for _dir in listdir(path):
    class_dir = os.path.join(path,_dir)
    if '.DS_Store' in class_dir:
      os.remove(class_dir)
    else:
      print(_dir)
      for _dir2 in listdir(class_dir):
          # print(str(_dir+_dir2))
          _dir3 = os.path.join(class_dir,_dir2)
          if '.DS_Store' in _dir3:
              print(_dir3)
              os.remove(_dir3)

class Model():

    def __init__(self):
        
        convolutional_network = mobilenet_v3_small(pretrained=False)
        convolutional_network.fc = nn.Flatten()


        self.model = PrototypicalNetworks(convolutional_network)
        self.model.load_state_dict(torch.load('./weights/cv-proj-mobilenet_v3_small.pth', map_location=torch.device('cpu')))
        self.model.eval()

        NORMALIZE_DEFAULT = dict(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

        self.pred_trans = transforms.Compose(
                        [
                            transforms.Resize([224, 224]),
                            transforms.CenterCrop(224),
                            transforms.ToTensor(),
                            transforms.Normalize(**NORMALIZE_DEFAULT),
                        ]
                    )

        self.example_query_images ,self.example_query_labels = self.list_query()

        with open('./train.json') as f:
            train_json = json.load(f)
        self.label_list = train_json['class_names']


        

    def predict(self, img):
        x_pred = img
        x_pred = self.pred_trans(x_pred)
        x_pred = torch.unsqueeze(x_pred,0)
        y_pred = self.model(
            self.example_query_images,
            self.example_query_labels,
            x_pred)

        # print(y_pred)
        max_idx = int(torch.argmax(y_pred))
        output = self.label_list[max_idx]
        # if y_pred[0][max_idx]>-3: output = self.label_list[max_idx]
        # else:output = 'Unknown'
        return output


    def list_query(self):
        test_set = EasySet(specs_file="train.json", training=False)

        example_query_images = []
        example_query_labels = []
        class_count = dict()
        for idx, data in enumerate(test_set):
            if data[1] not in class_count:
                class_count[data[1]]=0
                
            if class_count[data[1]] == 2:continue
            else:
                class_count[data[1]]+=1
                if idx==0:
                    example_query_images = data[0]
                    example_query_images = torch.unsqueeze(example_query_images,0)

                else:
                    nxt = torch.unsqueeze(data[0],0)
                    example_query_images = torch.cat((example_query_images, nxt),0)

                label = data[1]
                example_query_labels.append(label)
            
        example_query_labels = torch.FloatTensor(example_query_labels)

        return example_query_images, example_query_labels

    # def add_item(self, )
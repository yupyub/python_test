# CIFAR10에 적용하기 위한 임의의 NN
import torch
import torch.nn as nn
import torch.nn.functional as F
##############################################################################################################################
# Conv2d Node 계산법
# Conv2d(inChannelSize(RGBdepth=3), outVolumeSize(NumberOfFilter), kernelSize(Filter'sSize), Padding:default=0, Stride:default=0)
# Output Size = (W - F + 2P) / S + 1
# W: input_volume_size
# F: kernel_size
# P: padding_size
# S: strides
##############################################################################################################################
# Maxpooling을 하면 그 값으로 나눈 값이 Output Size
# ex) maxpooling 을 2로 하게 되면 input_filter_size의 값을 2로 나눈 값이 output_filter_size
##############################################################################################################################
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__() 
        # OutSize = (32 - 5 + 0)/1 + 1 = 28 
        # Output = 28*28 size img with 6-Filters
        self.conv1 = nn.Conv2d(3, 6, 5) 
        # Output = 14*14 size img with 6-Filters
        self.pool = nn.MaxPool2d(2, 2)
        # OutSize = (14 - 5 + 0)/1 + 1 = 10
        # Output = 10*10 size img with 16-Filters
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net()

# 전체 모델 저장하기
torch.save(net, "./DATA/NN_Model_1.pt")

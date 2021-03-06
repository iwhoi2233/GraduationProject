import torch
import torch.nn as nn


class example(nn.Module):
    def __init__(self):
        super(example, self).__init__()
        self.fc1 = nn.Linear(3, 3)
        self.bn = nn.BatchNorm1d(num_features=3)

    def forward(self, x):
        print(x)  # 输入
        x = self.fc1(x)
        x = self.bn(x)
        return x


data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
data = data.cuda()
net = example().cuda()
out = net(data)
print(out)

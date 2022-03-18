import torch.nn as nn


class SELayer(nn.Module):
    def __init__(self, channel, reduction=16):
        super(SELayer, self).__init__()

        # 全局平均池化，输入B*C*H*W -> 输出 B*C*1*1
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channel // reduction, channel, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size()

        # B*C*1*1转成B*C，再送入FC层
        y = self.avg_pool(x).view(b, c)

        # 全连接层+池化
        y = self.fc(y).view(b, c, 1, 1)

        # 和原特征图相乘
        return x * y.expand_as(x)
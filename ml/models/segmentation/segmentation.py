import segmentation_models_pytorch as smp
import torch.nn as nn


class UNet(nn.Module):
    def __init__(self, classes, in_channels, encoder_name='resnet34', encoder_weights='imagenet'):
        super().__init__()

        self.model = smp.Unet(
            encoder_name=encoder_name,   
            encoder_weights=encoder_weights,
            in_channels=in_channels,
            classes=classes,
        )

    def forward(self, x):
        return self.model(x)

    def to(self, device):
        return self.model.to(device)
    

class PSPNet(nn.Module):
    def __init__(self, classes, in_channels, encoder_name='resnet34', encoder_weights='imagenet'):
        super().__init__()

        self.model = smp.PSPNet(
            encoder_name=encoder_name,   
            encoder_weights=encoder_weights,
            in_channels=in_channels,
            classes=classes,
        )

    def forward(self, x):
        return self.model(x)

    def to(self, device):
        return self.model.to(device)
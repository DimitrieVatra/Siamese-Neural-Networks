import torch

torch.zeros(1).cuda()
print(torch.cuda.device_count())
print(torch._C._cuda_getDeviceCount())
import models.dataset.vlog_train as vlog
import torch
import argparse

params = {}
params = {}
params['filelist'] = '/Users/zhuocheng/Documents/GitHub/TimeCycle/dataset/test.txt'
params['imgSize'] = 256
params['imgSize2'] = 306
params['cropSize'] = 240
params['cropSize2'] = 80
params['offset'] = 0
params['batchSize'] = 2
params['videoLen'] = 4
params['predDistance'] = 2

parser = argparse.ArgumentParser(description='PyTorch ImageNet Training')

parser.add_argument('--T', default=512**-.5, type=float,
                    help='temperature')
parser.add_argument('--gridSize', default=9, type=int,
                    help='temperature')
parser.add_argument('--classNum', default=49, type=int,
                    help='temperature')

args = parser.parse_args()
state = {k: v for k, v in args._get_kwargs()}

print('temperature: ' + str(state['T']))

params['gridSize'] = 9

params['classNum'] = 1


train_loader = torch.utils.data.DataLoader(
        vlog.VlogSet(params, is_train=True, frame_gap=2),
        batch_size=2, shuffle=True,
        num_workers=1, pin_memory=True)

for batch_idx, (imgs, img, patch2, theta, meta) in enumerate(train_loader):
    # print(imgs)
    print(img)
    # print(patch2)
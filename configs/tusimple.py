# DATA
dataset='Tusimple'
data_root = '/home/martin/datasets/TuSimple'

# TRAIN
epoch = 100
batch_size = 30
optimizer = 'Adam'    #['SGD','Adam']
# learning_rate = 0.1
learning_rate = 4e-4
weight_decay = 1e-4
momentum = 0.9

scheduler = 'cos'     #['multi', 'cos']
# steps = [50,75]
gamma  = 0.1
warmup = 'linear'
warmup_iters = 100

# NETWORK
backbone = '18'
griding_num = 100
use_aux = True
num_classes = 8

# LOSS
sim_loss_w = 1.0
shp_loss_w = 0.0
cls_loss_w = 0.1

# EXP
note = ''

log_path = '/home/martin/datasets/TuSimple/logs'

# FINETUNE or RESUME MODEL PATH
finetune = None
resume = None

# TEST
test_model = None
test_work_dir = None

num_lanes = 4
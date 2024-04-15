# train a miniature character-level model

out_dir = 'out-theoffice'

always_save_checkpoint = False # we expect to overfit on this small dataset, so only save when val improves

dataset = 'the-office'
batch_size = 64
block_size = 256 # context of up to 256 previous characters

# baby GPT model
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

max_iters = 500 #5000
lr_decay_iters = 500 # make equal to max_iters usually

device = 'cpu'  # run on cpu only
compile = False # do not torch compile the model

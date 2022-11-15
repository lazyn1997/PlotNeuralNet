import sys

sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    # input
    to_input('../examples/fcn8s/cats.jpg', to="(0,0,0)", width=12, height=6.75),
    to_Conv("conv1", s_filer=(48, 27), n_filer=32, offset="(4.5,0,0)", to="(0,0,0)", height=27, depth=48, width=2, caption="conv1"),
    to_Conv("conv2", s_filer=(48, 27), n_filer=64, offset="(4,0,0)", to="(conv1-east)", height=27, depth=48, width=4, caption="conv2"),
    to_connection("conv1", "conv2"),
    to_Pool("pool1", s_filer=(24, 14), n_filer=64, offset="(3.5,0,0)", to="(conv2-east)", height=14, depth=24, width=4, opacity=0.5, caption='pool1'),
    to_connection("conv2", "pool1"),
    to_SoftMax("fc1", 200, "(3,0,0)", "(pool1-east)", width=1, height=1, depth=60, caption="fc"),
    to_connection("pool1", "fc1"),
    to_SoftMax("soft1", 139, "(2,0,0)", "(fc1-east)", width=1, height=1, depth=42, caption="softmax"),
    to_connection("fc1", "soft1"),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()

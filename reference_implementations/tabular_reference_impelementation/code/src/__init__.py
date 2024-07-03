import torch
from icecream import install

torch.set_num_threads(1)
install()

from . import env  # noqa
from .data import *  # noqa
from .metrics import *  # noqa
from .util import *  # noqa

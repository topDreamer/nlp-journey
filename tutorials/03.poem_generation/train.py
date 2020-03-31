# coding=utf-8
# created by msgi on 2020/3/31 12:31 上午

from model import PoemModel
from tokenizer import Tokenizer
from preprocess import preprocess
from dataset import PoetryDataSet
from utils import save_config, load_config

# 数据路径
DATA_PATH = './data/poetry.txt'

# 单行诗最大长度
MAX_LEN = 64

# 批次
BATCH_SIZE = 128

# 禁用的字符，拥有以下符号的诗将被忽略
REMOVED_WORDS = ['（', '）', '(', ')', '__', '《', '》', '【', '】', '[', ']']

# 最小词频
MIN_WORD_FREQUENCY = 8

# 补上特殊词标记：填充字符标记、未知词标记、开始标记、结束标记
INIT_TOKENS = ["[PAD]", "[NONE]", "[START]", "[END]"]

poetry, tokens, idx_word, word_idx = preprocess(DATA_PATH, MAX_LEN, MIN_WORD_FREQUENCY, REMOVED_WORDS, INIT_TOKENS)

save_config([tokens, idx_word, word_idx], 'config/config.pkl')

# 初始化tokenizer
tokenizer = Tokenizer(tokens)

# 构建数据集
dataset = PoetryDataSet(poetry, tokenizer, BATCH_SIZE)

# 训练（有模型的时候直接家在）
model = PoemModel(tokenizer, 'model', dataset)

# NLP积累

## Technique

### NLP中的Max Pooling

对于word embedding矩阵，可以设置维度为k*d的卷积核来抽取特征，其中k是卷积核指定的窗口大小，d是word embedding的维度。n个卷积核得到了n个特征向量。

max pooling over time。对于某一个卷积核抽取出来的特征项里，只保留得分最大的那个值作为pooling层保留值，其他特征值全部抛弃，值最大代表只保留这些特征中最强的，而抛弃其它弱的此类特征。

#### 讨论

- max pooling抛弃了位置信息，因为只保留一个，且没有它出现的位置。这对于文本并不一定好。
- 减少了后面层的参数。
- 可以把变长的输入整理成固定的输出，这个对于文本数据非常重要的好处。

#### Chunk-Max Pooling

对特征向量进行分段，取每段的最大值拼在一起。

## BERT相关

### RoBERTa

RoBERTa相比BERT有以下优势

- 动态masking
- 去掉NSP任务
- 更大的batch size
- byte级别的BPE
- 更多的预训练数据

### 预训练

MLM预训练任务中，只mask掉15%的单词。但是为了缩小pretraing和finetuning之间的gap，实际的做法是：随机选取15%的token的位置，之后

- 80%的概率替换为[MASK]
- 10%的概率替换为随机的另一个token
- 10%的概率保持不变

### 与BiLSTM

Bert相对于LSTM的优势

- 可以建模任意两个token之间的attention关系
- 可并行计算，比lstm快很多
- benefit from large quantity of text data

LSTM相对于Bert的优势

- 更适用于有很强的时序性的数据
- 参数较少，易于收敛

### 与ELMO

ELMO使用2个单向多层的LSTM获得表示，最终的表示是2L+1个表示的线性组合。

![elmo](..\img\elmo.png)

BERT相比ELMO的优势1. 直接学习双向的表示，而非拼接成的2. 利用attention

### 模型细节

#### Position Embedding

一般是随机初始化的。BERT的三个embedding可以直接相加，因为和拼接类似，相加也是对元素的线性组合（同Transformer）

## Transformer

### 模型细节

#### Position Encoding

每个词的位置编码仅仅与模型维度$d_{model}$和当前词的位置pos有关
$$
PE(pos,2i)=\sin(\frac{pos}{10000^{2i/d_{model}}})\\
PE(pos,2i+1)=\cos(\frac{pos}{10000^{2i/d_{model}}})
$$
PE和word embedding相加而不是拼接，因为这两种都相当于对元素的线性组合，拼接反而会增加参数量

#### Attention为什么要scaled

- 当x数量级过大时，y=softmax(x)中会给最大值赋予特别大的概率，其他位置几乎为0。这导致$\part y/\part x$很多位置都是0，导致梯度消失
- 假设q和k是相互独立的随机变量，服从标准正态分布，则qk=$\sum^d_{i=1} q_ik_i$~N(0, d)，所以为了将其标准化，除以$\sqrt d$可使方差变为1

## WordEmbedding

### W2V

基本的训练方法：

- CBOW：给周围词预测中心词
- Skip-gram：给中心词预测周围词

加速方法：

- 负采样：只采用一部分负样例，将loss转变为对数几率的加和
  $$
  \log Q_\theta(D=1|w_t,c)+kE_{\tilde w-P_{noise}}[\log Q_\theta(D=0|\tilde w,c)]
  $$


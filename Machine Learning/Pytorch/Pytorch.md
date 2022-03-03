### 一些函数

#### pack_padded_sequence

在使用深度学习特别是LSTM进行文本分析时，经常会遇到文本长度不一样的情况，此时就需要对同一个batch中的不同文本使用padding的方式进行文本长度对齐，方便将训练数据输入到LSTM模型进行训练，同时为了保证模型训练的精度，应该同时告诉LSTM相关padding的情况

```
x_packed = nn.utils.rnn.pack_padded_sequence(input=x, lengths=lengths, batch_first=True)
```

- 输入：**lengths**需要从大到小排序，**x**为已根据长度大小排好序，**batch_first**如果设置为true，则**x**的第一维为**batch_size**，第二维为**seq_length**
- 输出：前两维合并后的数据（单词序列）

#### permute(dims)

将tensor的维度换位

```
a=np.array([[[1,2,3],[4,5,6]]])
unpermuted=torch.tensor(a)
print(unpermuted.size())  #  ——>  torch.Size([1, 2, 3])
permuted=unpermuted.permute(2,0,1)
print(permuted.size())     #  ——>  torch.Size([3, 1, 2])
```

#### multinomial(prob, num_samples=1)

```
torch.multinomial(prob, num_samples=1, replacement=True)
```

对prob每一行采样num_samples次，返回每一行被采样到的数的下标，采样概率是prob这一行的数，数越大，概率越大，如果有数是0，那么在非0元素被采样完之前是不会被选取到的

replacement=True表示有放回

### 经验

#### F.crossentropy

- F.crossentropy函数自动包含softmax过程，所以送入其中的tensor不需要提前做softmax
- F.crossentropy函数的target必须是long类型
- F.crossentropy函数的直接输入维度必须是[n, m]和[n]
- 参数weight必须是float类型，且设备要一致

#### optimizer

- 一定要先进行model.to(device)，再定义优化器/加载优化器参数

#### zero_grad()

根据pytorch中的backward()函数的计算，当网络参量进行反馈时，梯度是被积累的而不是被替换掉；但是在每一个batch时毫无疑问并不需要将两个batch的梯度混合起来累积，因此这里就需要每个batch设置一遍zero_grad 了。

其实这里还可以补充的一点是，如果不是每一个batch就清除掉原有的梯度，而是比如说两个batch再清除掉梯度，这是一种变相提高batch_size的方法，对于计算机硬件不行，但是batch_size可能需要设高的领域比较适合，比如目标检测模型的训练。

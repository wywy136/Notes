# 实习/ML/RL

总结一些RL复习中的收获，希望能够通过面试

## 基本知识

### 马尔可夫决策过程

- 马尔可夫过程：状态满足马尔科夫性的随机过程

  - 随机过程

- 马尔可夫决策过程：带有决策和回报的马尔可夫过程

  - 随机变量s', r的分布由环境定义：$P(s',r|s,a)$
  - 状态转移概率：对r在汇报空间R求和
  - 回报的期望：$r(s,a)=E[R_t|S_{t-1}=s,A_{t-1}=a]=\sum_rr\sum_{s'}p(s',r|s,a)$

- 贝尔曼方程

  - $$
    V_\pi(s)=\sum_a\pi(a|s)Q_\pi(s,a)=\sum_a\pi(a|s)[r+\gamma\sum_{s'}P(s'|s,a)V_\pi(s')]
    $$

  - $$
    Q_\pi(s,a)=r+\gamma \sum_{s'}P(s'|s,a)\sum_{a'}\pi(a'|s')Q(s',a')
    $$

### 动态规划

- 贝尔曼方程的推到

  - $$
    v_\pi(s)=E_\pi[G_t|S_t=s]\\
    =E_\pi[R_{t+1}+\gamma G_{t+1}|S_t=s]\\
    =E_\pi[R_{t+1}+\gamma v_\pi(S_{t+1})|S_t=s]\\
    =\sum_a\pi(a|s)\sum_{s',r}p(s',r|s,a)[r+\gamma v_\pi(s')]
    $$

  - $$
    q_\pi(s,a)=E_\pi[R_{t+1}+\gamma v_\pi(S_{t+1})|s,a]\\
    =\sum_{s',r}p(s',r|s,a)[r+\gamma v(s')]\\
    =\sum_{s',r}p(s',r|s,a)[r+\gamma \sum_{a'}\pi(a'|s')q(s',a')]
    $$

### MC & TD

- Sarsa与Qlearning的区别
  - Sarsa：采样策略和目标策略都是soft策略
  - Qlearning：采样策略是soft，目标策略是贪婪策略，学到的Q直接逼近最优行为值函数
- Qlearning容易导致最大化偏差
  - solution: Double Qlearning: 贪婪策略选动作时按Q1去选，但是计算TD误差时用Q2的输出值
  - Q1Q2交替更新

### 策略梯度

- 策略梯度的推导 - 展开轨迹似然率和轨迹回报
  - 增加基线
  - 当前的动作只与未来的回报有关
  - 当前的回报只与过去的动作有关

### TRPO

- 对替代回报函数一阶近似的证明，还不是很熟悉

### Double DQN

$$
\theta=\theta+\alpha[r+Q'(s',\arg\max_{a'}Q(s',a'))-Q(s,a)]
$$

## 面试问题

- POMDP：部分可观测马尔可夫过程
- 重要性采样：增加准确度，减小方差
  - G的期望建立在$\pi$上，但无法直接从$\pi$上进行采样
- TRPO单调不减的证明
  - 重量级不等式 - ppt
  - 目标是最大化$M(\hat \pi)$
- A3C：避免经验回放相关性过强的问题，引入异步训练框架
  - 每个线程（agent）独立地和环境交互得到经验数据
  - 不同的线程会独立地使用累积的梯度分别更新公共部分的神经网络模型的参数
  - 每隔一段时间，线程将自己的神经网络的参数更新为公共神经网络的参数
  - 优化网络结构，一个网络同时作为策略网络和值网络
  - critic不再是$A=r+\gamma V(s')-V(s)$，而是n步采样的A
- DQN: off policy; A3C: on policy; DDPG: off policy(经验回放)
- AC的优点
  - 策略搜索，不局限于动作空间
  - 相比于策略梯度，AC进行策略的单步更新；且不再使用采样整条轨迹得到的真实回报

## AlphaGo

- 浅层策略网络$P_\pi$
- 深层SL策略网络$P_\sigma$ - CNN
- RL策略网络$P_\rho$ - CNN
- 值网络$V_\theta$ - CNN

#### SL网络

3000万张局面图

输入SL策略网络：48张局面图，19*19

- 3张stone color
- 8张turns since：8位2进制数表示棋子顺序
- ...

一系列卷积，输出一张棋盘概率，以人类下棋的结果作为监督信息，来预测人类下到哪的概率最高

#### 快速策略网络

下棋速度非常快

#### RL策略网络

初始化就是$P_\sigma$

让$P_\sigma$与$P_\rho$对局

位值网络提供学习样本

#### 值网络

输出一个值，代表胜率，用回归的方法


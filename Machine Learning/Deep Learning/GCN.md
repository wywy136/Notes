# GCN

## Why

- CNN无法处理非结构化数据
- 希望在非结构化数据上提取特征来进行机器学习
- GCN也可以应用在无拓扑结构的网络上

## How

（1）vertex domain，找到每个顶点相邻的neighbors

- 按照什么条件去找？- 如何确定receptive field
- 按照什么方式处理包含不同数目neighbors的特征

（2）spectral domain

- Spectral graph theory：借助图的拉普拉斯矩阵的特征值和特征向量来研究图的性质

## 拉普拉斯矩阵与GCN

拉普拉斯矩阵：L = D - A，D是顶点的度矩阵（对角矩阵），对角线上元素依次为各个顶点的度， A是图的邻接矩阵

另外两种计算方式

- $L^{sys}=D^{-1/2}LD^{-1/2}$: Symmetric normalized Laplacian
- $L^{rw}=D^{-1}A$: Random walk normalized Laplacian

为什么GCN要用拉普拉斯矩阵

- L阵是对称矩阵，可进行特征分解，和GCN spectral domain对应
- L阵只在中心顶点和一阶相连的顶点上有非0元素，其余之处均为0
- 通过拉普拉斯算子与拉普拉斯矩阵进行类比

## 拉普拉斯矩阵的特征分解

拉阵是半正定对称矩阵

- 对称矩阵一定有n个线性无关的特征向量，因此可以进行特征分解
- 半正定矩阵的特征值一定非负
- 对称矩阵的特征向量相互正交，即特征向量构成的矩阵为正交阵

$L=U\lambda U^{-1},U=(u_1,u_2,...,u_n)$，U是列向量为单位特征向量的矩阵，因此有$L=U\lambda U^T$

## 从传统的傅里叶变换、卷积类比到Graph上的傅里叶变换及卷积

传统傅里叶变换：$F(\omega)=\int {f(t)e^{-i\omega t}dt}$

$LV=\lambda V$

$F(\lambda_t)=\hat f(\lambda_l)=\sum_{i=1}^N f(i)u^*_l(i)$

- $f(i)$与是Graph顶点embedding
- $u_l(i)$是第l个特征向量的第i个分量
- 含义：特征值$\lambda_l$下，f的Graph傅里叶变换与$\lambda_l$对应的特征向量$u_l$进行内积运算

矩阵形式：$\hat f=U^Tf$

Graph的傅里叶逆变换：$f=U\hat f$

根据卷积定理
$$
f*h=U[\hat h(\lambda_n)]U^Tf
$$

- f的graph傅里叶变换：$U^Tf$

 - 在每个特征值下，h的graph傅里叶变换与特征值对应的特征向量之间进行内积运算，写成对角矩阵的形式
   	- 等价于$U^Th$，都是h在Graph上的傅里叶变换

## GCN

第一代GCN：把diag(h)变成diag(θ)：$y=\sigma(Udiag(\theta)U^Tx)$

第二代GCN：把$\hat h(\lambda_l)$变成了$\sum^K_{j=0}\alpha_j\lambda^j_l$

- $\sum^K_{j=0}\alpha_j\lambda^j_l=\sum^K_{j=0}\alpha_j\Lambda^j$

- $U\sum^K_{j=0}\alpha_j\Lambda^jU^T=\sum^K_{j=0}\alpha_jL^j$ - ！！！
- $y=\sigma(\sum^K_{j=0}\alpha_jL^jx)$
  - 仅需要K个参数（K一般<n）
  - 不需要特征分解，直接用拉阵L
  - K就是卷积核的感受野，每次卷积会将中心顶点k-top neighbor上的feature加权求和，系数就是$\alpha_k$


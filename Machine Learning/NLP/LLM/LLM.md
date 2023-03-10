# LLM

## Paper Readings

### A Comprehensive Survey on Pretrained Foundation Models: A History from BERT to ChatGPT

#### Semi-supervised Learning Mechanisms

Given an unlabelled dataset $Z=\{z_i\}^m_{i=1}$, the learning process could be formalized as
$$
\arg\min_\theta \frac{1}{n}\sum^n_{i=1}L(f(x_i;\theta),y_i)+\frac{1}{m}\sum^m_{i=1}L'(f'(z_i;\theta'),R(z_i,X))+\lambda\Omega(\theta)
$$

- $L,\Omega$: loss function and regularization term
- $f'$: encoder to learn a new representation for the original data in the dataset $Z$
- $R$: is a relation function defining the targets for unlabelled data, and then these pseudo-labels are integrated into the end-to-end training process.

#### Weakly-Supervised Learning

Suppose there are inaccurate K labels for each sample in the dataset, denoted by $y_i=[y^1_i,y^2_i,...,y^K_i]$
$$
\arg\min_\theta \frac{1}{nK}\sum^n_{i=1}\sum^K_{k=1}L(f(x_i;\theta),y_i^k)+λΩ(θ)
$$
$L$ could be a loss function suitable for binomial classification problem. For any entry in $y_i$, computing the loss function of the one-versus-all binomial classification is needed.

#### Self-supervised Learning

- Generative SSL: Variational autoencoder (VAE) and generative adversarial network (GAN)
- Discriminative SSL: Contrastive learning. The main idea of contrastive learning is to learn the prior knowledge distribution of the data itself with the aid of various methods such as data augmentation. In this way, contrastive learning can learn a model that makes similar instances closer in the projected space, and dissimilar instances farther apart in the projected space. A simple version of contrastive loss:

$$
L_c(x_i,x_j,θ)=m||f_θ(x_i)−f_θ(x_j)||_2^2 +(1−m)\max(0,\epsilon−||f_θ(x_i)−f_θ(x_j)||_2)^2
$$

where m is 1 if two samples have the same label, otherwise 0, and $\epsilon$ is the upper bound distance.

#### NLP Pretraining Tasks

- Mask Language Modeling (MLM): BERT, SpanBERT
- Denoising AutoEncoder (DAE): add noise to the original corpus and reconstruct the original input using the corpus containing noise: BART
- Replaced Token Detection (RTD): a discriminant task that determines whether the LM has replaced the current token: ELECTRA
- Next Sentence Prediction (NSP): BERT
- Sentence Order Prediction (SOP): uses two contiguous fragments from a document as positive samples and the exchange order of the two fragments as negative samples: ALBERT

RTD, NSP, and SOP are contrastive learning methods, which assume that the observed samples are more **semantically similar** than the random samples.

#### Word Representation Methods for PFMs

- **Autoregressive LM**. 
  $$
  p(w_1,w_2,...,w_N)=\Pi^N_{i=1}p(w_i|w_1,w_2,...,w_{i-1})
  $$

  - GPT adopts a two-stage method of self-supervised pretraining and supervised fine-tuning and uses stacked Transformer [36] as its decoder. 
  - GPT-2 increases the number of stacked Transformer layers to 48 layers (1.5 billion parameters) + multi-task learning. It also uses autoregressive LM. The main performance improvement of GPT-2 comes from the combined effect of multi-task pretraining, super-large datasets, and super-large models.
  - GPT-3 grows the model size to 175 billion parameters and trains with 45 Terabytes of data.

- **Contextual Language Model**. The contextual LM predictions are based on contextual words. It uses a Transformer encoder, and the upper and lower layers of the model are all directly connected to each other due to the self-attention mechanism.
  $$
  p(w_1,w_2,...,w_N)=\Pi^N_{i=1}p(w_i|w_1,w_2,...,w_N)
  $$
  

  - BERT.
  - RoBERTa uses a larger batch size and unlabeled data, trains the model for a longer time, removes the NSP task, and adds long sequence training, and adopts Byte Pair Encoding for word segmentation.

- **Permuted Language Model**. Contextual LM are poor in NLG task. Permuted LM aims to combine the advantages of the autoregressive LM and the Contextual LM. It improves the defects of the two models to a great extent and can be used as a basic idea for the construction of future pretraining target tasks. Given input sequence $T=[w_1,w_2,...,w_N]$, the target function of permuted LM is
  $$
  \max_\theta E_{z\sim Z_N}[\sum^N_{t=1}\log p_\theta(x_{z_{T=t}}|x_{z_{T<t}})]
  $$
  $\theta$ is the shared parameter in all permutations, $Z_N$ represents the set of all possible permutations of input sequence T, and and $z_{T=t}$ and $z_{T<t}$ represents the t-th element and the $[1,2,...,t − 1]$ elements of a permutation $z\in Z_N$ .

  Permuted LM is based on the autoregressive LM, which avoids the influence of inconsistent data for MLM. Unlike traditional autoregressive models, permuted LM no longer models sequences in order. It gives all possible permutations of sequences to maximize the expected logarithmic likelihood of the sequence.

  - XLNET is the first permuted LM-based PFM, plus relative positional encoding and the ==segment recurrence mechanism==.
  - MPNet combines MLM models with permuted LM models to predict dependencies between tokens through permuted LM.

#### Model Architecture Designing Methods for PFM

- ELMO: multi-layer bi-directional LSTM
- BERT: the document is encoded bidirectionally, reducing the generation ability.
- GPT: uses an autoregressive decoder as a feature extractor to predict the next word based on the first few words and solve downstream tasks using fine-tuning, but GPT only uses the former words for prediction.

- BART

  ![Screenshot 2023-03-09 at 6.42.10 PM](../../../img/papers/BART.png)Pretraining mainly includes using noise to destroy text and using the seq2seq model to rebuild the original text. Five nosing methods:

  - single word mask
  - word deletion
  - span mask
  - sentence rearrangement
  - document rearrangement

#### Masking Designing Methods for PFMs

SpanBERT adopts the idea of dynamic masking and single segment pretraining. 

![SpanBERT](../../../img/papers/SpanBERT.png)

The training stage uses the [dynamic mask](https://github.com/huggingface/transformers/issues/5979) strategy proposed in the RoBERTa, instead of the mask during the data preprocessing. Unlike BERT, SpanBERT randomly covers up a continuous text and adds the ==Span Boundary Objective (SBO)== training target. It predicts the span using the token closest to the span boundary and eliminates the NSP pretraining task.


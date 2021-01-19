## APNE - Personal Comments  

- the algorithm is not inductive --> Requires node features which are transformed into feature embeddings and finally multiplied with node embeddings. The node embedding and feature embedding matrices have fixed dimensions!

- The algorithm relies solely on matrix factorization, however from an abstract point of view it resembles very much the workings of GCN alggorithms. I wouldn't invest too much time in making this work. 

- The code is written in C and is very hard to read. There is no python version available of the explicit matrix factorization algorithm used as part of the APNE algorithm. Hence, it might be difficult to apply to our use case!

## APNE
This project contains code related to the paper "Enhancing Network Embedding with Auxiliary Information: An Explicit Matrix Factorization Perspective".
APNE (Auxiliary information Preserved Netork Embedding) is a graph/network embedding method that can incorporate the structure information,
content information and label information simultaneously in an unsupervised manner, i.e.,
without leveraging downstream classifiers.
APNE outperforms unsupervised baselines from 10.1% to 34.4% on the node classification task.
Details can be accessed [here](https://arxiv.org/abs/1711.04094).

### Requirements

* Matlab (>R2014a)
* gcc (>4.4.5)
* networkx

### Run the demo

Run the main script in matlab as:
```
run_emf
```

### Data

We test our model in four datasets in the paper, here in `./data/` folder we provide
files of `cora` dataset.
We use dataset splits provided by [Planetoid](https://github.com/kimiyoung/planetoid),
where data files are formatted as `ind.<dataset>.<suffix>`,
as well as several files processed from the origin files:
* {dataset}.embeddings.walks.0: random walk sequences obtained by directly running [DeepWalk](https://github.com/phanein/deepwalk)
* {dataset}_features.mat: features saved `.mat` file
* {dataset}_train_data.npy: training nodes and corresponding labels in `.npy` file

You can specify a dataset by editing `run_emf.m`, where details about other hyper-parameters
can also be found.

### Output

We save and test checkpoints at every `verbose`, and you
can change its value to fit your storage.

The final output as well as checkpoints are `.mat` files which
contain matrix **W** and matrix **S** described in our paper.
Matrix **W** is the embedding matrix of the input graph with size
`(num_nodes * emb_dim)`, and you can refer to `test.py`
to evalute its performance.

### Acknowledgements

The original version of this code base was forked from [emf](https://github.com/etali/emf),
and we also referred to [GCN](https://github.com/tkipf/gcn)
while preprocessing datasets. Many thanks to the authors for making their code available.

### Citing

Please cite our paper if you find APNE useful in your research:
```
@inproceedings{guo2018enhancing,
  title={Enhancing Network Embedding with Auxiliary Information: An Explicit Matrix Factorization Perspective},
  author={Guo, Junliang and Xu, Linli and Huang, Xunpeng and Chen, Enhong},
  booktitle={International Conference on Database Systems for Advanced Applications},
  pages={3--19},
  year={2018},
  organization={Springer}
}
```

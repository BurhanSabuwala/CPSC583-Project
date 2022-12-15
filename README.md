# Utilizing the Graph Neural Networks for annotation of Spatial Single-cell Datasets

This project is a part of CPSC 583: Deep Learning for Graph Structured Data Course

PyTorch implementation of STELLAR and other methods.


### Installation


**1. Python environment (Optional):**
We recommend using Conda package manager. The steps to install the required packages are given below.

```bash
module load miniconda
conda create --name pytorch_env python=3.8 pytorch torchvision torchaudio torch-geometric cudatoolkit=11.3 -c pytorch
conda activate pytorch_env
pip install pyg-lib torch-scatter torch-sparse -f https://data.pyg.org/whl/torch-1.13.0+cpu.html
pip install torch-geometric
pip install -r requirements.txt
```

### Datasets

CODEX multiplexed imaging datasets is available at [dryad](https://datadryad.org/stash/share/1OQtxew0Unh3iAdP-ELew-ctwuPTBz6Oy8uuyxqliZk). 

### Running the complete code
This step may consume a lot of memory (32GB RAM) and time (30 * 10 minutes). 
```bash
sh run_script.sh
```

### Running individual hubmap models

```
python3 run_stellar.py --dataset Hubmap --num-heads 22 --model GAT --randseed 2 --sample-rate 1.0
```

`GAT` can be changed to any of the following models
 - `FullyConnected`
 - `GCN`
 - `GraphSAGE`
 - `Transformers`

### Running individual TonsilBE models
```
python3 run_stellar.py --dataset TonsilBE --num-heads 13 --sample-rate 0.35 --model GraphSAGE
```

### Pre-recorded results
Results of the trials that I had run are given in `Hubmap_results.csv` and `TonsilBE_results.csv`. The first three rows are the accuracy results for three different runs on the different dataset split using different random seeds. The last three rows are balanced accuracy results for each of the three different runs. The columns are representative of different models tested - (Fully Connected (FC), Graph Convolutional Network (GCN), Graph Attention Network (GAT), GraphSAGE and Graph Transformer). 

import argparse
from utils import prepare_save_dir
from STELLAR import STELLAR
import numpy as np
import os
from sklearn.metrics import accuracy_score, balanced_accuracy_score
import torch
import pandas as pd
from datasets import GraphDataset, load_tonsilbe_data, load_hubmap_data_transductive

parser = argparse.ArgumentParser(description='STELLAR')
parser.add_argument('--dataset', default='Hubmap', help='dataset setting')
parser.add_argument('--seed', type=int, default=1, metavar='S', help='random seed (default: 1)')
parser.add_argument('--name', type=str, default='STELLAR')
parser.add_argument('--epochs', type=int, default=30)
parser.add_argument('--lr', type=float, default=1e-3)
parser.add_argument('--wd', type=float, default=5e-2)
parser.add_argument('--num-heads', type=int, default=22)
parser.add_argument('--num-seed-class', type=int, default=0)
parser.add_argument('--sample-rate', type=float, default=0.5)
parser.add_argument('--model', type=str, default='GraphSAGE')
parser.add_argument('-b', '--batch-size', default=1, type=int,
                metavar='N',
                help='mini-batch size')
parser.add_argument('--distance_thres', default=50, type=int)
parser.add_argument('--savedir', type=str, default='./')
parser.add_argument('--randseed', type=int, default=1)
args = parser.parse_args()
args.cuda = torch.cuda.is_available()
args.device = torch.device("cuda" if args.cuda else "cpu")

# Seed the run and create saving directory
args.name = '_'.join([args.dataset, args.name])
args = prepare_save_dir(args, __file__)

print("Retrive dataset and construct Graph")
if args.dataset == 'Hubmap':
    #labeled_X, labeled_y, unlabeled_X, labeled_edges, unlabeled_edges, inverse_dict = load_hubmap_data('B004_training_dryad.csv', 'B0056_unnanotated_dryad.csv', args.distance_thres, args.sample_rate)
    labeled_X, labeled_y, unlabeled_X, unlabeled_y, labeled_edges, unlabeled_edges, inverse_dict = load_hubmap_data_transductive('B004_training_dryad.csv', args.distance_thres, args.sample_rate, randseed = args.randseed)
    dataset = GraphDataset(labeled_X, labeled_y, unlabeled_X, labeled_edges, unlabeled_edges)
elif args.dataset == 'TonsilBE':
    #labeled_X, labeled_y, unlabeled_X, labeled_edges, unlabeled_edges, inverse_dict = load_tonsilbe_data('BE_Tonsil_l3_dryad.csv', args.distance_thres, args.sample_rate)
    labeled_X, labeled_y, unlabeled_X, unlabeled_y, labeled_edges, unlabeled_edges, inverse_dict = load_tonsilbe_data('BE_Tonsil_l3_dryad.csv', args.distance_thres, args.sample_rate, randseed = args.randseed)
    dataset = GraphDataset(labeled_X, labeled_y, unlabeled_X, labeled_edges, unlabeled_edges)
print("Initiate STELLAR")
stellar = STELLAR(args, dataset)
print("Start Training")
stellar.train()
_, results = stellar.pred()
print("Save Predictions")
np.save(os.path.join(args.savedir, args.dataset +'_'+ args.model + '_results.npy'), results)
print("Accuracy: ", accuracy_score(unlabeled_y, results))
print("Balanced Accuracy: ", balanced_accuracy_score(unlabeled_y, results))
    
## Saving results
results_df = pd.read_csv( args.dataset +"_results.csv", index_col = 0)
results_df[args.model][args.randseed-1] = accuracy_score(unlabeled_y, results)
results_df[args.model][args.randseed+2] = balanced_accuracy_score(unlabeled_y, results)
results_df.to_csv(args.dataset + "_results.csv")

import sys
sys.exit()
# This is the script to run Stellar multiple times to generate the data required for the performance plot

# Generate CSV template file
python3 generate_csv_files.py

# For Hubmap dataset

python3 run_stellar.py --dataset Hubmap --num-heads 22 --model FullyConnected --randseed 1 --sample-rate 1.0
python3 run_stellar.py --dataset Hubmap --sample-rate 1.0 --num-heads 22 --model FullyConnected --randseed 2
python3 run_stellar.py --dataset Hubmap --num-heads 22 --model FullyConnected --randseed 3 --sample-rate 1.0

python3 run_stellar.py --dataset Hubmap --num-heads 22 --model GCN --randseed 1 --sample-rate 1.0
python3 run_stellar.py --dataset Hubmap --num-heads 22 --model GCN --randseed 2 --sample-rate 1.0
python3 run_stellar.py --dataset Hubmap --num-heads 22 --model GCN --randseed 3 --sample-rate 1.0

python3 run_stellar.py --dataset Hubmap --num-heads 22 --model GAT --randseed 1 --sample-rate 1.0
python3 run_stellar.py --dataset Hubmap --num-heads 22 --model GAT --randseed 2 --sample-rate 1.0
python3 run_stellar.py --dataset Hubmap --num-heads 22 --model GAT --randseed 3 --sample-rate 1.0

python3 run_stellar.py --dataset Hubmap --num-heads 22 --model GraphSAGE --randseed 1 --sample-rate 1.0
python3 run_stellar.py --dataset Hubmap --num-heads 22 --model GraphSAGE --randseed 2 --sample-rate 1.0
python3 run_stellar.py --dataset Hubmap --num-heads 22 --model GraphSAGE --randseed 3 --sample-rate 1.0

python3 run_stellar.py --dataset Hubmap --num-heads 22 --model Transformers --randseed 1 --sample-rate 1.0
python3 run_stellar.py --dataset Hubmap --num-heads 22 --model Transformers --randseed 2 --sample-rate 1.0
python3 run_stellar.py --dataset Hubmap --num-heads 22 --model Transformers --randseed 3 --sample-rate 1.0


# For TonsilBE data

python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model FullyConnected --randseed 1
python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model FullyConnected --randseed 2
python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model FullyConnected --randseed 3

python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model GCN --randseed 1
python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model GCN --randseed 2
python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model GCN --randseed 3

python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model GAT --randseed 1
python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model GAT --randseed 2
python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model GAT --randseed 3

python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model GraphSAGE --randseed 1
python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model GraphSAGE --randseed 2
python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model GraphSAGE --randseed 3

python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model Transformers --randseed 1
python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model Transformers --randseed 2
python3 run_stellar.py --dataset TonsilBE --sample-rate 0.35 --num-heads 13 --model Transformers --randseed 3


# Script to plot the results
python3 plot_results.py 


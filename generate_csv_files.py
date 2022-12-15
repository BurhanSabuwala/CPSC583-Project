# file to create Hubmap_results.csv and TonsilBE_results.csv files
import csv

with open('Hubmap_results.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['', 'FullyConnected', 'GCN', 'GAT','GraphSAGE', 'Transformers'])
    spamwriter.writerow([1, 0, 0, 0, 0, 0])
    spamwriter.writerow([2, 0, 0, 0, 0, 0])
    spamwriter.writerow([3, 0, 0, 0, 0, 0])
    spamwriter.writerow([4, 0, 0, 0, 0, 0])
    spamwriter.writerow([5, 0, 0, 0, 0, 0])
    spamwriter.writerow([6, 0, 0, 0, 0, 0])
    
    
with open('TonsilBE_results.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['', 'FullyConnected', 'GCN', 'GAT','GraphSAGE', 'Transformers'])
    spamwriter.writerow([1, 0, 0, 0, 0, 0])
    spamwriter.writerow([2, 0, 0, 0, 0, 0])
    spamwriter.writerow([3, 0, 0, 0, 0, 0])
    spamwriter.writerow([4, 0, 0, 0, 0, 0])
    spamwriter.writerow([5, 0, 0, 0, 0, 0])
    spamwriter.writerow([6, 0, 0, 0, 0, 0])
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_hubmap = pd.read_csv("Hubmap_results.csv", index_col = 0)

plt.figure(figsize = (4,3))
plt.bar(np.arange(len(df_hubmap.columns)), [np.mean(df_hubmap[i][:3]) for i in df_hubmap.columns], color = "tab:blue")
plt.errorbar(np.arange(len(df_hubmap.columns)), [np.mean(df_hubmap[i][:3]) for i in df_hubmap.columns], yerr = [np.std(df_hubmap[i][:3]) for i in df_hubmap.columns], capsize = 10.0, c = "black")
plt.ylim(-0.05,1.05)
plt.xticks(np.arange(len(df_hubmap.columns)), df_hubmap.columns, rotation= 30)
plt.title("Accuracy (HuBMAP dataset)")
plt.tight_layout()
plt.savefig("Accuracy_Hubmap.png")
plt.close()

plt.figure(figsize = (4,3))
plt.bar(np.arange(len(df_hubmap.columns)), [np.mean(df_hubmap[i][3:]) for i in df_hubmap.columns], color = "tab:blue")
plt.errorbar(np.arange(len(df_hubmap.columns)), [np.mean(df_hubmap[i][3:]) for i in df_hubmap.columns], yerr = [np.std(df_hubmap[i][3:]) for i in df_hubmap.columns], capsize = 10.0, c = "black")
plt.xticks(np.arange(len(df_hubmap.columns)), df_hubmap.columns,rotation = 30)
plt.title("Balanced Accuracy (HuBMAP dataset)")
plt.ylim(-0.05,1.05)
plt.tight_layout()
plt.savefig("Balanced_Accuracy_Hubmap.png")
plt.close()

df_tbe = pd.read_csv("TonsilBE_results.csv", index_col = 0)

plt.figure(figsize = (4,3))
plt.bar(np.arange(len(df_tbe.columns)), [np.mean(df_tbe[i][:3]) for i in df_tbe.columns], color = "tab:blue")
plt.errorbar(np.arange(len(df_tbe.columns)), [np.mean(df_tbe[i][:3]) for i in df_tbe.columns], yerr = [np.std(df_tbe[i][:3]) for i in df_tbe.columns], capsize = 10.0, c = "black")
plt.xticks(np.arange(len(df_tbe.columns)), df_tbe.columns,rotation =30)
plt.title("Accuracy (TonsilBE dataset)")
plt.ylim(-0.05,1.05)
plt.tight_layout()
plt.savefig("Accuracy_TonsilBE.png")
plt.close()

plt.figure(figsize = (4,3))
plt.bar(np.arange(len(df_tbe.columns)), [np.mean(df_tbe[i][3:]) for i in df_tbe.columns], color = "tab:blue")
plt.errorbar(np.arange(len(df_tbe.columns)), [np.mean(df_tbe[i][3:]) for i in df_tbe.columns], yerr = [np.std(df_tbe[i][3:]) for i in df_tbe.columns], capsize = 10.0, c = "black")
plt.xticks(np.arange(len(df_tbe.columns)), df_tbe.columns, rotation = 30)
plt.title("Balanced Accuracy (TonsilBE dataset)")
plt.ylim(-0.05,1.05)
plt.tight_layout()
plt.savefig("Balanced_Accuracy_TonsilBE.png")
plt.close()

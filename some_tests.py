from scipy.io import loadmat

df = loadmat('./data/cora_features.mat')
print(df['features'])
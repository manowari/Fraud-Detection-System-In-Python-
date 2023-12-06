# pca_analysis.py

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def apply_pca(data):
    # Assuming data is preprocessed and features are selected
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(data)

    # Visualize the principal components
    plt.scatter(principal_components[:, 0], principal_components[:, 1])
    plt.title('PCA Analysis')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()

# Assuming data is preprocessed and features are selected
# Load the dataset
url = "https://raw.githubusercontent.com/curiousily/Credit-Card-Fraud-Detection-using-Autoencoders-in-Keras/master/creditcard.csv"
data = pd.read_csv(url)

# Apply PCA
apply_pca(data)

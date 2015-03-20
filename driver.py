import pandas as pd
import numpy as np
from perceptron import Perceptron


def perceptron_model():
    """ Perceptron classifier on Iris flower dataset
    """

    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

    # setosa and versicolor
    y = df.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)

    # sepal length and petal length
    X = df.iloc[0:100, [0, 2]].values
    ppn = Perceptron(epochs=10, eta=0.1)
    ppn.fit(X, y)
    print('Weights: %s' % ppn.w_)


def main():
    """ Driver script for running the models in the repo.
        * Perceptron
        * Adaline
        * Logistic regression
    """

    import argparse
    parser = argparse.ArgumentParser(
        description="Classify the data set",
        formatter_class=argparse.RawDescriptionHelpFormatter,)
    parser.add_argument('--model', help="Choose model", choices=['perceptron'])
    args = parser.parse_args()
    if args.model == "perceptron":
        perceptron_model()


if __name__ == '__main__':
    main()

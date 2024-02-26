import random
import numpy as np
from xgboost import XGBClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def get_splits(n, k, seed):
    splits = []
    # Implement your code to construct the splits here

    # Step 1: generate random number with seed
    random.seed(seed)

    # Step 2: create index list
    index = []
    for i in range(n):
        index.append(i)

    # Step 3: shuffle
    random.shuffle(index)

    # Step 4: partition
    for i in range(k):
        splits.append([])
    i = 0
    while i < n:
        splits[i % k].append(index[i])
        i += 1

    return splits

def my_cross_val(method, X, y, splits):
    errors = []
    # Implement your code to calculate the errors here

    # Step 1: define method model
    if method == "LinearSVC":
        clf = LinearSVC(max_iter=2000, random_state=412)
    elif method == "SVC":
        clf = SVC(gamma="scale", C=10, random_state=412)
    elif method == "LogisticRegression":
        clf = LogisticRegression(penalty="l2", solver="lbfgs", random_state=412, multi_class="multinomial")
    elif method == "RandomForestClassifier":
        clf = RandomForestClassifier(max_depth=20, n_estimators=500, random_state=412)
    elif method == "XGBClassifier":
        clf = XGBClassifier(max_depth=5, random_state=412)

    for k in range(len(splits)):
        idx_train = []                  # selected idxs for training
        idx_test = []
        x_train = []
        y_train = []
        x_test = []
        y_test = []

        # Step 2: fit the model with k-1 folds
        for group in range(len(splits)):
            if group == k:
                for idx in splits[group]:
                    idx_test.append(idx)
            else:
                for idx in splits[group]:
                    idx_train.append(idx)
        idx_train.sort()
        idx_test.sort()
        for idx in idx_test:
            x_test.append(X[idx])
            y_test.append(y[idx])
        for idx in idx_train:
            x_train.append(X[idx])
            y_train.append(y[idx])
        clf.fit(x_train, y_train)

        # Step 3: test model using k-th group
        y_hat = clf.predict(x_test)

        # Step 4: calculate error rate
        wrong_pred = 0
        for sample in range(len(x_test)):
            if y_hat[sample] != y_test[sample]:
                wrong_pred += 1
        errors.append(wrong_pred / len(x_test))

    return np.array(errors)

# from sklearn . datasets import load_digits
# digits = load_digits()
# X, y = digits.data, digits.target
# print(my_cross_val("RandomForestClassifier", X, y, get_splits(len(X), 10, 5)))
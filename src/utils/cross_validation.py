import numbers

import numpy as np
from sklearn.model_selection import BaseCrossValidator
from sklearn.utils.validation import indexable, check_array, _num_samples


class TimeSeriesGroupSplit(BaseCrossValidator):
    """Time Series cross-validator with group separation.

    Provides train/test indices to split time series data samples
    that are observed at fixed time intervals, in train/test sets.
    In each split, test group value must be higher than before.
    In comparison to TimeSeriesSplit one group goes to train or test
    at the same time. Group here is a time and we want for many time series
    to be splitted by this group.

    :param n_splits: int, default=5
    """
    def __init__(self, n_splits=5):
        if not isinstance(n_splits, numbers.Integral):
            raise ValueError('The number of folds must be of Integral type. '
                             '%s of type %s was passed.'
                             % (n_splits, type(n_splits)))
        n_splits = int(n_splits)

        if n_splits <= 1:
            raise ValueError(
                "k-fold cross-validation requires at least one"
                " train/test split by setting n_splits=2 or more,"
                " got n_splits={0}.".format(n_splits))
        self.n_splits = n_splits

    def split(self, X, y=None, groups=None):
        """Generate indices to split data into training and test set.

        :param X: array-like of shape (n_samples, n_features)
            Training data, where n_samples is the number of samples
            and n_features is the number of features.
        :param y: array-like of shape (n_samples,)
            Always ignored, exists for compatibility.
        :param groups: array-like of shape (n_samples,)
            Always ignored, exists for compatibility.

        :returns:
            train : ndarray
                The training set indices for that split.
            test : ndarray
                The testing set indices for that split.
        """
        if groups is None:
            raise ValueError("The 'groups' parameter should not be None.")
        X, y, groups = indexable(X, y, groups)
        groups = check_array(groups, ensure_2d=False, dtype=None)

        unique_groups, groups = np.unique(groups, return_inverse=True)
        n_groups = len(unique_groups)
        n_samples = _num_samples(X)
        n_splits = self.n_splits
        n_folds = n_splits + 1

        if self.n_splits > n_groups:
            raise ValueError("Cannot have number of splits n_splits=%d greater"
                             " than the number of groups: %d."
                             % (self.n_splits, n_groups))

        indices = np.arange(n_samples)
        test_size = (n_groups // n_folds)
        test_starts = range(test_size + n_groups % n_folds,
                            n_groups, test_size)
        for test_start in test_starts:
            # here we already have groups after inverse operation
            # and don't need to use unique_group
            yield (
                np.where(indices[groups < test_start]),
                np.where(indices[(groups >= test_start)
                                 & (groups < test_start + test_size)])
            )

    def get_n_splits(self):
        """Returns the number of splitting iterations in the cross-validator.

        :returns: the number of splitting iterations in the cross-validator.
        """
        return self.n_splits

import numpy as np

def calculate(list):

    target = np.array(list).reshape(3,3)

    result = {
        'mean': [np.mean(target, axis=0).tolist(), np.mean(target, axis=1).tolist(), np.mean(target)],
        'variance': [np.var(target, axis=0).tolist(), np.var(target, axis=1).tolist(), np.var(target)],
        'standard deviation': [np.std(target, axis=0).tolist(), np.std(target, axis=1).tolist(), np.std(target)],
        'max': [np.max(target, axis=0).tolist(), np.max(target, axis=1).tolist(), np.max(target)],
        'min': [np.min(target, axis=0).tolist(), np.min(target, axis=1).tolist(), np.min(target)],
        'sum': [np.sum(target, axis=0).tolist(), np.sum(target, axis=1).tolist(), np.sum(target)]
    }

    return result
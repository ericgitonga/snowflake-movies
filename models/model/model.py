"""
Trying out BigQuery
"""
from typing import Any
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score
import xgboost as xgb
from layer import Featureset, Train


def train_model(train: Train, tf: Featureset("features")) -> Any:
    train_df = tf.to_pandas()
    X = train_df.drop(["movie_id", "is_success"], axis=1)
    Y = train_df["is_success"]

    random_state = 13
    test_size = 0.2
    train.log_parameter("random_state", random_state)
    train.log_parameter("test_size", test_size)
    trainX, testX, trainY, testY = train_test_split(X, Y, test_size=test_size,
                                                    random_state=random_state)
    train.register_input(trainX)
    train.register_output(trainY)

    max_depth = 3
    objective = 'binary:logistic'
    train.log_parameter("max_depth", max_depth)
    train.log_parameter("objective", objective)

    param = {'max_depth': max_depth, 'objective': objective}
    dtrain = xgb.DMatrix(trainX, label=trainY)
    model_xg = xgb.train(param, dtrain)

    dtest = xgb.DMatrix(testX)
    preds = model_xg.predict(dtest)

    auprc = average_precision_score(testY, preds)
    train.log_metric("auprc", auprc)

    return model_xg

import numpy as np
from numpy.typing import ArrayLike
import pandas as pd
import sklearn.metrics as mt


class Metrics:

    def __init__(self):
        self.accuracy_score = []
        self.precision_score = []
        self.recall_score = []
        self.f1_score = []
        self.classifier = []

    def evaluate(self, y_test: ArrayLike, y_score: ArrayLike, classifier: str) -> None:
        try:
            y_test = np.array(y_test)
            y_score = np.array(y_score)
        except Exception as e:
            raise TypeError(f"입력 데이터를 변환할 수 없습니다: {e}")

        if not isinstance(classifier, str):
            raise TypeError(
                f"classifier는 str 타입이어야 합니다. 현재 타입: {type(classifier)}"
            )

        self.accuracy_score.append(mt.accuracy_score(y_test, y_score))
        self.precision_score.append(
            mt.precision_score(y_test, y_score, average="macro")
        )
        self.recall_score.append(mt.recall_score(y_test, y_score, average="macro"))
        self.f1_score.append(mt.f1_score(y_test, y_score, average="macro"))
        self.classifier.append(classifier)

    def to_dict(self) -> dict:
        return {
            "accuracy_score": self.accuracy_score,
            "precision_score": self.precision_score,
            "recall_score": self.recall_score,
            "f1_score": self.f1_score,
            "classifier": self.classifier,
        }

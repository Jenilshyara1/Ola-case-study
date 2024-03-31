import logging
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, roc_curve, auc
import numpy as np

logger = logging.getLogger()
STAGE_NAME = "Model evaluation"


class Model_evaluation:
    def __init__(
        self,
        model,
        X_test,
        y_test,
        classification_report_path,
        confusion_matrix_path,
        precision_recall_curve_path,
        ROC_AUC_path,
    ) -> None:
        self.model = model
        self.X_test = X_test
        self.y_test = y_test
        self.y_pred = self.model.predict(self.X_test)
        self.classification_report_path = classification_report_path
        self.confusion_matrix_path = confusion_matrix_path
        self.precision_recall_curve_path = precision_recall_curve_path
        self.ROC_AUC_path = ROC_AUC_path

    def save_confusion(self):
        cm = confusion_matrix(self.y_test, self.y_pred)
        plt.figure(figsize=(10, 7))
        sns.heatmap(cm, annot=True, fmt="d")
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Truth")
        plt.savefig(self.confusion_matrix_path)
        plt.cla()
        plt.clf()

    def save_classification_report(self):
        report = classification_report(self.y_test, self.y_pred)
        # Save classification report
        with open(self.classification_report_path, "w") as f:
            f.write(report)

    def save_precision_recall_curve(self):
        precisions, recalls, thresholds = precision_recall_curve(
            self.y_test, self.model.predict_proba(self.X_test)[:,1]
        )
        threshold_boundary = thresholds.shape[0]
        # plot precision
        plt.plot(
            thresholds,
            precisions[0:threshold_boundary],
            linestyle="--",
            label="precision",
        )
        # plot recall
        plt.plot(thresholds, recalls[0:threshold_boundary], label="recalls")
        start, end = plt.xlim()
        plt.xticks(np.round(np.arange(start, end, 0.1), 2))
        plt.xlabel("Threshold Value")
        plt.ylabel("Precision and Recall Value")
        plt.legend(); plt.grid()
        plt.savefig(self.precision_recall_curve_path)

    def save_roc_auc_curve(self):
        fpr, tpr, _ = roc_curve(self.y_test, self.y_pred)
        roc_auc = auc(fpr, tpr)

        # Plot
        plt.figure()
        lw = 2
        plt.plot(
            fpr,
            tpr,
            color="darkorange",
            lw=lw,
            label="ROC curve (area = %0.2f)" % roc_auc,
        )
        plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("Receiver Operating Characteristic")
        plt.legend(loc="lower right")
        plt.savefig(self.ROC_AUC_path)

    def evaluate(self):
        self.save_confusion()
        self.save_classification_report()
        self.save_precision_recall_curve()
        self.save_roc_auc_curve()

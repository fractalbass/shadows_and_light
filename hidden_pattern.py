import random
from numpy import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

class HiddenPattern:

    def run(self):
        data = list()

        fig = plt.figure()
        fig2 = plt.figure()
        ax3 = fig.add_subplot(111, projection='3d')
        ax2 = fig2.add_subplot(111)


        for i in range(0,500):
            x = -1 + (2 * random.random())
            y = -1 + (2 * random.random())
            z = random.normal(-3, 2) / 10
            ax2.scatter(x, y, c="r", s=6)
            ax3.scatter(x, y, z, c="r", s=6)
            data.append((x,y,z,"b"))

        for i in range(0, 500):
            x = -1 + (2 * random.random())
            y = -1 + (2 * random.random())
            z = random.normal(3, 2) / 10
            ax2.scatter(x, y, c="b", s=6)
            ax3.scatter(x, y, z, c="b", s=6)
            data.append((x,y,z,"r"))

        plt.show()
        return(data)

    def forest(self, points):
        train_x = list()
        train_y = list()

        for p in points[0:800]:
            train_x.append([p[0], p[1], p[2]])
            target = 0
            if p[3] == "b":
                target = 1
            train_y.append(target)

        model = RandomForestClassifier(n_estimators=1000)
        model.fit(train_x, train_y)

        test_y = list()
        test_x = list()
        for x in range(800, 1000):
            test_x.append([points[x][0], points[x][1], points[x][2]])
            target = 0
            if points[x][3] == 'b':
                target=1
            test_y.append(target)

        prediction = model.predict(test_x)
        accuracy = metrics.accuracy_score(prediction, test_y)
        print("Calculation complete.  Random Forest Accuracy: {0}".format(accuracy))

    def regression(self, points):
        print("do regression")


if __name__ == "__main__":
    hp = HiddenPattern()
    data2d = hp.run()
    hp.forest(data2d)
    #hp.regression(data2d)
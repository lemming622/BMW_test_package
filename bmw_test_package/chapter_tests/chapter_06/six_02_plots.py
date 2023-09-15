import numpy
import pandas as pd
import matplotlib.pyplot as plt

from six_ballisticMissileTrajectories import six_02_general_ballistic_missile_problem

#def maxRangePlot():
"""
This is a proof of the max range plot (figure 6.2-6 Range vs. \u03F4 :sub: `bo` )
"""
print("This is a reproduction of the Figure 6.2-6 - 1st ed")

dot3 = []
dot4 = []
dot5 = []
dot6 = []
dot7 = []
dot75 = []
dot8 = []
dot85 = []
dot9 = []
dot95 = []
onedot0 = []

for fpa in numpy.arange(0, 90, 0.5):
    print(fpa)

    dot3.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.3, fpa))
    dot4.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.4, fpa))
    dot5.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.5, fpa))
    dot6.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.6, fpa))
    dot7.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.7, fpa))
    dot75.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.75, fpa))
    dot8.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.8, fpa))
    dot85.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.85, fpa))
    dot9.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.9, fpa))
    dot95.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.95, fpa))
    onedot0.append(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(1.0, fpa))

datacolumns = {"Q_bo = 0.3": dot3,
               "Q_bo = 0.4": dot4,
               "Q_bo = 0.5": dot5,
               "Q_bo = 0.6": dot6,
               "Q_bo = 0.7": dot7,
               "Q_bo = 0.75": dot75,
               "Q_bo = 0.8": dot8,
               "Q_bo = 0.85": dot85,
               "Q_bo = 0.9": dot9,
               "Q_bo = 0.95": dot95,
               "Q_bo = 1.0": onedot0}

# Create empty data frame with predone column names
df = pd.DataFrame(datacolumns)

df.plot()

plt.show()

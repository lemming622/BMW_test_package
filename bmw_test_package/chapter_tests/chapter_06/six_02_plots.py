import numpy
import pandas as pd
import matplotlib.pyplot as plt

from six_ballisticMissileTrajectories import six_02_general_ballistic_missile_problem

#def maxRangePlot():
"""
This is a proof of the max range plot (figure 6.2-6 Range vs. \u03F4 :sub: `bo` )
"""
print("This is a reproduction of the Figure 6.2-6 - 1st ed")

datacolumns = {"Q_bo = 0.3": [],
               "Q_bo = 0.4": [],
               "Q_bo = 0.5": [],
               "Q_bo = 0.6": [],
               "Q_bo = 0.7": [],
               "Q_bo = 0.75": [],
               "Q_bo = 0.8": [],
               "Q_bo = 0.85": [],
               "Q_bo = 0.9": [],
               "Q_bo = 0.95": [],
               "Q_bo = 1.0": []}

# Create empty data frame with predone column names
df = pd.DataFrame(datacolumns)

for fpa in numpy.arange(0, 90, 0.5):
    df['Q_bo = 0.3'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.3, fpa))
    df['Q_bo = 0.4'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.4, fpa))
    df['Q_bo = 0.5'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.5, fpa))
    df['Q_bo = 0.6'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.6, fpa))
    df['Q_bo = 0.7'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.7, fpa))
    df['Q_bo = 0.75'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.75, fpa))
    df['Q_bo = 0.8'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.8, fpa))
    df['Q_bo = 0.85'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.85, fpa))
    df['Q_bo = 0.9'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.9, fpa))
    df['Q_bo = 0.95'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(0.95, fpa))
    df['Q_bo = 1.0'].add(six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(1.0, fpa))

df.plot()

plt.show()

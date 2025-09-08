from typing import Dict

import numpy as np

import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('Qt5Agg')


def main():

    print("---------------------------------")
    print("| codedrome.com                 |")
    print("| Tickertape Gravity Simulation |")
    print("---------------------------------\n")

    gravities = {"Moon": 1.622,
                 "Mercury": 3.7,
                 "Venus": 8.87,
                 "Earth": 9.80665,
                 "Mars": 3.72076,
                 "Jupiter": 24.79,
                 "Saturn": 10.44,
                 "Uranus": 8.69,
                 "Neptune": 11.15}

    data = calc_data(gravities["Earth"], 1, 16)

    print_data(data)

    g = calculate_gravity(data)
    print(f"\ng = {g}m/s²\n")

    display_tickertape(data)


def calc_data(acceleration: float, interval: float, iterations: int) -> Dict:

    """
    Create a dictionary of NumPy arrays containing:
        t - times in seconds
        v - speeds in metres/second
        s - displacements in metres
    of a falling mass across a period of time.
    Assumes initial speed is 0.
    """

    a = acceleration
    u = 0

    t = np.arange(0,17,1)

    v = u + (a * t)

    s = (u * t) + ( 0.5 * a * (t ** 2) )

    data = {"times": t, "speeds": v, "displacements": s}

    return data


def print_data(data: Dict) -> None:

    """
    Prints the time/speed/displacement data as a table.
    """

    heading = "time(s)      speed(m/s)   displacement(m)"

    print("-" * len(heading))
    print(heading)
    print("-" * len(heading))

    for (t, v, s) in zip(data["times"], data["speeds"], data["displacements"]):

        print(f"{t:>7}   {v:>13.5f}   {s:>15.5f}")

    print("-" * len(heading))


def display_tickertape(data: Dict) -> None:

    """"
    Creates a representation of an actual 
    tickertape showing times and displacements.
    """

    y = np.zeros(17)

    fig, ax = plt.subplots(figsize=(16,2))

    ax.set_box_aspect(1/32)

    plt.xlabel("Displacements (metres)")
    plt.title("Tickertape Gravity Simulation\n(each dot is 1 second)")
    plt.yticks([])
    plt.grid(True)

    plt.scatter(data["displacements"], y, color='#FF8000', s=4)
  
    plt.show()


def calculate_gravity(data: Dict) -> float:

    """
    implements a = (v-u)/t assuming u = 0
    v = final_speed
    t = final_seconds
    a = g
    """

    u = 0
    v = data["speeds"][-1]
    t = data["times"][-1]

    g = (v - u) / t

    return g


if __name__ == "__main__":

    main()

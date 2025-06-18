from turtle import *
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

def hilbert(level, angle, step, pause_time, depth, color_levels, indent=0):
    if level == 0:
        return

    prefix = "  " * indent
    print(f"{prefix}Enter level {level}: right({angle})")
    #pencolor(color_levels[depth - level])
    right(angle)
    time.sleep(pause_time)

    hilbert(level - 1, -angle, step, pause_time, depth, color_levels, indent + 1)

    print(f"{prefix}level {level}: forward({step})")
    pencolor("red")
    forward(step)
    time.sleep(pause_time)

    print(f"{prefix}level {level}: left({angle})")
    left(angle)
    time.sleep(pause_time)

    hilbert(level - 1, angle, step, pause_time, depth, color_levels, indent + 1)

    print(f"{prefix}level {level}: forward({step})")
    pencolor("green")
    forward(step)
    time.sleep(pause_time)

    hilbert(level - 1, angle, step, pause_time, depth, color_levels, indent + 1)

    print(f"{prefix}level {level}: left({angle})")
    left(angle)
    time.sleep(pause_time)

    print(f"{prefix}level {level}: forward({step})")
    pencolor("blue")
    forward(step)
    time.sleep(pause_time)

    hilbert(level - 1, -angle, step, pause_time, depth, color_levels, indent + 1)

    print(f"{prefix}level {level}: right({angle})")
    right(angle)
    time.sleep(pause_time)

    print(f"{prefix}Exit level {level}")

def main():
    try:
        level = int(input("Enter recursion level (e.g., 3): "))
        speed_input = input("Turtle speed (0–10, default 3): ").strip()
        pause_input = input("Pause between moves in seconds (e.g., 0.1, default 0): ").strip()

        speed_val = int(speed_input) if speed_input else 3
        pause_time = float(pause_input) if pause_input else 0

    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    speed(speed_val)
    size = 300
    penup()
    goto(-size / 2.0, size / 2.0)
    pendown()

    color_levels = [COLORS[i % len(COLORS)] for i in range(level)]

    hilbert(level, 90, size / (2**level - 1), pause_time, level, color_levels)

    done()

if __name__ == '__main__':
    main()


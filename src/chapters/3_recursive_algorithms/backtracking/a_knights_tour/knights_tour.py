## Fixed Knight's Tour Problem Solver using backtracking algorithm
## and visualization using matplotlib
#
#
# Example usage: 
# python knights_tour.py --board_size 6 --start_x 0 --start_y 0 --delay 0.3
# python knights_tour.py --board_size 8 --start_x 3 --start_y 3 --delay 0.1 --no_animatio\gn
#
#
   
import matplotlib.pyplot as plt
import numpy as np
import time
import random
import sys
import argparse
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib import colors
from matplotlib import cm
    
class KnightsTour:
    def __init__(self, board_size=8, start_pos=(0, 0), delay=0.1):
        self.board_size = board_size
        self.start_pos = start_pos
        self.delay = delay
        self.board = np.zeros((board_size, board_size), dtype=int)
        self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        self.solution_path = []
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.visited_squares = []

    def is_valid_move(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size and self.board[x][y] == 0

    def solve(self, x, y, move_count):
        # record the current position in solution path
        self.solution_path.append((x, y))
        
        if move_count == self.board_size * self.board_size:
            return True
            
        for dx, dy in self.moves:
            next_x, next_y = x + dx, y + dy
            if self.is_valid_move(next_x, next_y):
                self.board[next_x][next_y] = move_count + 1
                if self.solve(next_x, next_y, move_count + 1):
                    return True
                self.board[next_x][next_y] = 0
                
        # Backtrack: remove the current position from solution path
        self.solution_path.pop()
        return False

    def start_tour(self):
        x, y = self.start_pos
        self.board[x][y] = 1
        if not self.solve(x, y, 1):
            print("No solution found")
            return False
        else:
            print("Solution found")
            return True

    def init_board(self):
        self.ax.clear()
        
        # create board
        for i in range(self.board_size):
            for j in range(self.board_size):
                color = 'lightgray' if (i + j) % 2 == 0 else 'white'
                rect = Rectangle((j, i), 1, 1, facecolor=color, edgecolor='black', linewidth=1)
                self.ax.add_patch(rect)
        
        self.ax.set_xlim(0, self.board_size)
        self.ax.set_ylim(0, self.board_size)
        self.ax.set_aspect('equal')
        self.ax.set_title("Knight's Tour Visualization", fontsize=16)
        self.ax.set_xticks(range(self.board_size + 1))
        self.ax.set_yticks(range(self.board_size + 1))
        self.ax.grid(True, alpha=0.3)
        
        # Invert y-axis to match array indexing
        self.ax.invert_yaxis()

    def update_animation(self, frame):
        self.ax.clear()
        self.init_board()
        
        # Color the visited squares up to current frame
        cmap = cm.get_cmap('viridis')
        for i in range(min(frame + 1, len(self.solution_path))):
            x, y = self.solution_path[i]
            color = cmap(i / len(self.solution_path))
            rect = Rectangle((y, x), 1, 1, facecolor=color, edgecolor='black', linewidth=2)
            self.ax.add_patch(rect)
            
            # Add move number
            self.ax.text(y + 0.5, x + 0.5, str(i + 1), 
                        ha='center', va='center', fontsize=10, 
                        color='white' if i > len(self.solution_path) * 0.5 else 'black',
                        weight='bold')
        
        # Draw path lines
        if frame > 0:
            path_x = [pos[1] + 0.5 for pos in self.solution_path[:frame + 1]]
            path_y = [pos[0] + 0.5 for pos in self.solution_path[:frame + 1]]
            self.ax.plot(path_x, path_y, 'r-', linewidth=2, alpha=0.7)

    def animate(self):
        if not self.solution_path:
            print("No solution to animate")
            return
            
        self.init_board()
        
        # Create animation
        frames = len(self.solution_path)
        anim = FuncAnimation(self.fig, self.update_animation, frames=frames, 
                           interval=self.delay * 1000, repeat=True, blit=False)
        
        plt.tight_layout()
        plt.show()
        
        return anim

    def print_solution(self):
        if self.solution_path:
            print(f"\nSolution path ({len(self.solution_path)} moves):")
            for i, (x, y) in enumerate(self.solution_path):
                print(f"Move {i+1}: ({x}, {y})")
            
            print(f"\nFinal board state:")
            print(self.board)

def main():
    parser = argparse.ArgumentParser(description="Knight's Tour Problem Solver and Visualizer")
    parser.add_argument('--board_size', type=int, default=8, help='Size of the chessboard (default: 8)')
    parser.add_argument('--start_x', type=int, default=0, help='Starting x position of the knight (default: 0)')
    parser.add_argument('--start_y', type=int, default=0, help='Starting y position of the knight (default: 0)')
    parser.add_argument('--delay', type=float, default=0.5, help='Delay between moves in seconds (default: 0.5)')
    parser.add_argument('--no_animation', action='store_true', help='Skip animation, just solve and print')
    args = parser.parse_args()

    # Validation
    if args.board_size < 5:
        print("Board size must be at least 5")
        sys.exit(1)
    if not (0 <= args.start_x < args.board_size) or not (0 <= args.start_y < args.board_size):
        print("Starting position must be within the board")
        sys.exit(1)

    print(f"Solving Knight's Tour on {args.board_size}x{args.board_size} board")
    print(f"Starting position: ({args.start_x}, {args.start_y})")
    
    kt = KnightsTour(board_size=args.board_size, start_pos=(args.start_x, args.start_y), delay=args.delay)
    
    start_time = time.time()
    success = kt.start_tour()
    end_time = time.time()
    
    if success:
        print(f"Solution found in {end_time - start_time:.2f} seconds")
        kt.print_solution()
        
        if not args.no_animation:
            print("Starting animation...")
            kt.animate()
    else:
        print("No solution exists for this configuration")

if __name__ == "__main__":
    main()


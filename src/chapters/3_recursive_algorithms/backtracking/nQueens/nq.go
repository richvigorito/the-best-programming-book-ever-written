// n queens problem in go
// unlike a many of implementations 
// where the board is a n x n array
// this board is represented as a single
// array of n length where the value is 1..n

package main

import (
	"fmt"
	"math"
)

const N = 8

type Board [N]int       // board[row] = column
type Solutions []Board  // slice of valid boards

func isSafe(board Board, row, col int) bool {
	for r := 0; r < row; r++ {
		c := board[r]
		if c == col || int(math.Abs(float64(c-col))) == row-r {
			return false
		}
	}
	return true
}

func solveNQueens(board Board, row int, solutions *Solutions) {
	if row == N {
		*solutions = append(*solutions, board)
		return
	}

	for col := 0; col < N; col++ {
		if isSafe(board, row, col) {
			board[row] = col
			solveNQueens(board, row+1, solutions)
			// implicitly backtrack by row -> row+1+1,,B -> row-1-2-3N row without needing to reset the board
		}
	}
}

func printBoard(board Board) {
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if board[i] == j {
				fmt.Print("Q ")
			} else {
				fmt.Print(". ")
			}
		}
		fmt.Println()
	}
}

func main() {
	var board Board
	var solutions Solutions

	solveNQueens(board, 0, &solutions)

	fmt.Printf("Total solutions for %d queens: %d\n\n", N, len(solutions))
	for i, solution := range solutions {
		fmt.Printf("Solution #%d:\n", i+1)
		printBoard(solution)
		fmt.Println()
	}
}


package main

import "fmt"

func bubbleSort(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
}

func main() {
	numbers := []int{5, 99, 101, 100, 2, 90, 9, 1, 2, 22, 5, 6}
	fmt.Println("Unsorted array:", numbers)
	bubbleSort(numbers)
	fmt.Println("Sorted array:", numbers)
}


package main

import (
	"fmt"
)

func QuickSort(arr []int) {
	if len(arr) < 2 {
		return
	}

	left, right := 0, len(arr)-1
	pivotIdx := len(arr) / 2

	arr[pivotIdx], arr[right] = arr[right], arr[pivotIdx]

	for i := range arr {
		if arr[i] < arr[right] {
			arr[i], arr[left] = arr[left], arr[i]
			left++
		}
	}

	arr[left], arr[right] = arr[right], arr[left]

	QuickSort(arr[:left])
	QuickSort(arr[left+1:])
}

func main() {
	arr := []int{34, 7, 23, 32, 5, 62, 32, 4, 1, 19}
	fmt.Println("Original:", arr)

	QuickSort(arr)
	fmt.Println("Sorted:  ", arr)
}


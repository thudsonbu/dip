package main

import (
	"math"
)

// Given an integer array nums sorted in non-decreasing order, return an array
// of the squares of each number sorted in non-decreasing order.

func sortedSquares(nums []int) []int {
	if len(nums) == 0 {
		return nums
	}
	result := make([]int, 0, len(nums))
	midpointIndex := -1
	for i := 0; i < len(nums); i++ {
		if nums[i] >= 0 {
			midpointIndex = i
			break
		}
	}
	if midpointIndex == -1 {
		midpointIndex = len(nums)
	}
	leftIndex, rightIndex := midpointIndex-1, midpointIndex
	for leftIndex >= 0 && rightIndex < len(nums) {
		if math.Abs(float64(nums[leftIndex])) < math.Abs(float64(nums[rightIndex])) {
			result = append(result, nums[leftIndex]*nums[leftIndex])
			leftIndex--
		} else {
			result = append(result, nums[rightIndex]*nums[rightIndex])
			rightIndex++
		}
	}
	for leftIndex >= 0 {
		result = append(result, nums[leftIndex]*nums[leftIndex])
		leftIndex--
	}
	for rightIndex < len(nums) {
		result = append(result, nums[rightIndex]*nums[rightIndex])
		rightIndex++
	}
	return result
}

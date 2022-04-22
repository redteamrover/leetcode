/**
 * LeetCode Problem 704 - Binary Search
 * 
 * Given an array of integers nums which is sorted in ascending order, and an
 * integer target, write a function to search target in nums. If target exists,
 * then return its index. Otherwise, return -1.
 * 
 * You must write an algorithm with O(log n) runtime complexity.
 * 
 * Constraints
 * ===========
 *  1. 1 <= numbers.length <= 10^4
 *  2. -104 < numbers[i], target < 10^4
 *  3. All the integers in the numbers array are unique.
 *  4. The numbers are sorted in ascending order.
 * 
 */
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * This function searches for the index within the numbers input array
 * containing the target value, returning the index if the target value can be
 * found in the array.
 * 
 * If the target value is not in the input array, the function returns -1.
 *
 */
int search(int* numbers, int n, int target) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
        int mid = (high + low) / 2;

        if (target == numbers[mid]) {
            return mid;
        } else if (target < numbers[mid]) {
            high = mid - 1;
        } else if (target > numbers[mid]) {
            low = mid + 1;
        }
    }

    return -1;
}

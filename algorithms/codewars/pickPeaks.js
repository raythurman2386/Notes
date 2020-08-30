/*
https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/javascript

***
In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. 
If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is 
after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only return the 
position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent 
in other languages)

*/

function pickPeaks(arr) {
	const result = {
		pos: [],
		peaks: [],
	};

	// Find index in array that is higher than n - 1 and n + 1
	// add that index to result.pos and the number to result.peaks
	for (let i = 0; i < arr.length; i++) {
		// console.log(arr[i])
		if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
			// if the current index is greater than the previous
			// and greater than the next index
			// add index and number to object
			result.pos.push(i);
			result.peaks.push(arr[i]);
		}
		// Passes all basic tests without this section
		// else if (arr[i] > arr[i - 1] && arr[i] == arr[i + 1]) {
		// 	result.pos.push(i);
		// 	result.peaks.push(arr[i]);
		// }
		else if (
			// else if there is a plateau
			// add the first index where plateau starts
			arr[i] > arr[i - 1] &&
			arr[i] === arr[i + 1] &&
			arr[i] > arr[arr.length - 1]
		) {
			result.pos.push(i);
			result.peaks.push(arr[i]);
		}
	}

	return result;
}

console.log(pickPeaks([0, 1, 2, 5, 1, 0]));
console.log(pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]));
console.log(pickPeaks([1, 2, 2, 2, 1]));
console.log(pickPeaks([1, 2, 2, 2, 3]));
// Passing with current implementation
console.log(
	pickPeaks([
		2,
		-2,
		10,
		13,
		13,
		-3,
		6,
		14,
		4,
		2,
		10,
		11,
		0,
		7,
		-3,
		-2,
		7,
		3,
		12,
		15,
		0,
		1,
		-4,
		13,
		2,
		-2,
		10,
		-3,
		3,
		0,
		-4,
		6,
	])
);

// Failing Test
// Needs to equal === { pos: [ 2, 4, 7, 9, 11, 13, 16, 18, 22, 24, 28 ],
// 											peaks: [11, 11, 11, 14, 14, 15, 15, 15, 12, 11, 9] }
console.log(
	pickPeaks([
		12,
		0,
		11,
		-1,
		11,
		11,
		-1,
		11,
		0,
		14,
		11,
		14,
		3,
		15,
		2,
		14,
		15,
		11,
		15,
		-3,
		1,
		6,
		12,
		6,
		11,
		7,
		7,
		-1,
		9,
		3,
		11,
	])
);

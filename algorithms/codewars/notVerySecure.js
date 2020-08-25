/*
In this example you have to validate if a user 
input string is alphanumeric. The given string is 
not nil/null/NULL/None, so you don't have to 
check that.

The string has the following conditions to be 
alphanumeric:

    At least one character ("" is not valid)
    Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
    No whitespaces / underscore
*/

function alphanumeric(string) {
	if (string.length === 0) {
		return false;
	}
	//your code here
	let nonLetters = 0;
	const allowed = 'abcdefghijklmnopqrstuvwxyz0123456789';
	// breaking method
	const lowerString = string.toLowerCase();
	const strArr = lowerString.split('');
	for (let i = 0; i < strArr.length; i++) {
		if (!allowed.includes(strArr[i])) {
			nonLetters++;
		}
	}

	if (nonLetters !== 0) {
		return false;
	}

	return true;
}

console.log(alphanumeric('Mazinkaiser'));
console.log(alphanumeric('hello world_'));
console.log(alphanumeric('PassW0rd'));
console.log(alphanumeric('     '));

// Regex Pattern
console.log(/^[0-9a-z]+$/i.test('Mazinkaiser'));
console.log(/^[0-9a-z]+$/i.test('hello world_'));
console.log(/^[0-9a-z]+$/i.test('PassW0rd'));
console.log(/^[0-9a-z]+$/i.test('     '));

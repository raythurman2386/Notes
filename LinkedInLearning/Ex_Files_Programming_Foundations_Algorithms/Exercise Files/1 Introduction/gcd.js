function gcd(a, b) {
	while (b != 0) {
		temp = a;
		a = b;
		b = temp % b;
	}

	return a;
}

console.log(gcd(60, 96));
console.log(gcd(20, 8));

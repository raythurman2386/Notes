// /*
//   TypeWriter will take in 3 args
//   - txtElement is the span the words will go in
//   - words will be the words from the data tab
//   - wait is the wait time from the data tab
// */
// const TypeWriter = function (txtElement, words, wait = 3000) {
// 	this.txtElement = txtElement;
// 	this.words = words;
// 	this.txt = '';
// 	this.wordIndex = 0;
// 	this.wait = parseInt(wait, 10);
// 	this.type();
// 	this.isDeleting = false;
// };

// // Type Method
// TypeWriter.prototype.type = function () {
// 	// Current Index of word
// 	const current = this.wordIndex % this.words.length;

// 	// Get the text of the current word
// 	const fulltxt = this.words[current];

// 	// Check if isDeleting
// 	if (this.isDeleting) {
// 		// Remove a char
// 		this.txt = fulltxt.substring(0, this.txt.length - 1);
// 	} else {
// 		// Add a char
// 		this.txt = fulltxt.substring(0, this.txt.length + 1);
// 	}

// 	// Insert txt into element
// 	this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

// 	// Type Speed
// 	let typeSpeed = 300;

// 	if (this.isDeleting) {
// 		typeSpeed /= 2;
// 	}

// 	// See if word is complete
// 	if (!this.isDeleting && this.txt === fulltxt) {
// 		typeSpeed = this.wait;
// 		this.isDeleting = true;
// 	} else if (this.isDeleting && this.txt === '') {
// 		this.isDeleting = false;
// 		// Move to the next word
// 		this.wordIndex++;
// 		// Pause before typing again
// 		typeSpeed = 500;
// 	}

// 	setTimeout(() => this.type(), typeSpeed);
// };

class TypeWriter {
	constructor(txtElement, words, wait = 3000) {
		this.txtElement = txtElement;
		this.words = words;
		this.txt = '';
		this.wordIndex = 0;
		this.wait = parseInt(wait, 10);
		this.type();
		this.isDeleting = false;
	}

	type() {
		// Current Index of word
		const current = this.wordIndex % this.words.length;

		// Get the text of the current word
		const fulltxt = this.words[current];

		// Check if isDeleting
		if (this.isDeleting) {
			// Remove a char
			this.txt = fulltxt.substring(0, this.txt.length - 1);
		} else {
			// Add a char
			this.txt = fulltxt.substring(0, this.txt.length + 1);
		}

		// Insert txt into element
		this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

		// Type Speed
		let typeSpeed = 300;

		if (this.isDeleting) {
			typeSpeed /= 2;
		}

		// See if word is complete
		if (!this.isDeleting && this.txt === fulltxt) {
			typeSpeed = this.wait;
			this.isDeleting = true;
		} else if (this.isDeleting && this.txt === '') {
			this.isDeleting = false;
			// Move to the next word
			this.wordIndex++;
			// Pause before typing again
			typeSpeed = 500;
		}

		setTimeout(() => this.type(), typeSpeed);
	}
}

// Init on DOM Load
document.addEventListener('DOMContentLoaded', init);

// Init App
function init() {
	const txtElement = document.querySelector('.txt-type');
	const words = JSON.parse(txtElement.getAttribute('data-words'));
	const wait = txtElement.getAttribute('data-wait');
	// Init typeWriter
	new TypeWriter(txtElement, words, wait);
}

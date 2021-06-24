// Hi, here's your problem today. This problem was recently asked by Amazon:

// Given an integer, reverse the digits. Do not convert the integer into a 
// string and reverse it.

function reverseInteger( int ) {
	let magnitude = 10;
	let numArr    = [];
	let out       = 0;

	while ( int > 0 ) {
		let num = int % magnitude;

		int -= num;

		numArr.push( num / ( magnitude / 10 ) );
		magnitude *= 10;
	}

	magnitude = magnitude / 10;
	numArr.forEach(num => {
		magnitude = magnitude / 10;
		out += ( num * magnitude );
	});

	return out;
}

console.assert( reverseInteger( 24 ), 42 );
console.assert( reverseInteger( 9 ), 9 );
console.assert( reverseInteger( 804 ), 408 );
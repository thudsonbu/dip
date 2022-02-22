// Hi, here's your problem today. This problem was recently asked by Amazon:

// Given an integer, reverse the digits. Do not convert the integer into a 
// string and reverse it.

function reverseInteger( int ) {
	let magnitude = 10;
	let out       = 0;
	let negative  = 1;

	if ( int < 0 ) {
		negative = -1;
		int *= -1;
	} 

	while ( int > 0 ) {
		out *= 10;

		let num = int % magnitude;
		int -= num;

		magnitude *= 10;
		out += num;
	}

	return negative * out;
}

console.assert( reverseInteger( 24 ), 42 );
console.assert( reverseInteger( 9 ), 9 );
console.assert( reverseInteger( 804 ), 408 );
console.assert( reverseInteger( -29 ), -92 );
console.assert( reverseInteger( 400 ), 4 );
// Hi, here's your problem today. This problem was recently asked by Uber:

// Given a string s and a character c, find the distance for all characters in 
// the string to the character c in the string s. You can assume that the 
// character c will appear at least once in the string.

function shortestDistanceToChar( string, char ) {
	let distanceArr = [];

	// left to right starting at first instance of char and addign distance
	let first = false;
	let distance = 0;
	for ( i = 0; i < string.length; i++ ) {
		if ( string[i] === char ) {
			first = true;
			distance = 0;
			distanceArr.push( 0 );
		} else if ( first ) {
			distance++;
			distanceArr.push( distance );
		} else {
			distanceArr.push( 0 );
		}
	}

	first = false;
	distance = 0;
	for ( i = string.length - 1; i >= 0; i -= 1 ) {
		if ( string[i] === char ) {
			first = true;
			distance = 0;
		} else if ( first ) {
			distance++;
			if ( distanceArr[i] > distance || distanceArr[i] === 0 ) {
				distanceArr[i] = distance;
			}
		}
	}

	return distanceArr;
}

console.log( shortestDistanceToChar( "hello", "l" ) );
console.log( shortestDistanceToChar( "hello world", "l") );
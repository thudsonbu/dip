// There are n bulbs that are initially off. You first turn on all the bulbs, 
// then you turn off every second bulb.

// On the third round, you toggle every third bulb (turning on if it's off or 
// turning off if it's on). For the ith round, you toggle every i bulb. For the 
// nth round, you only toggle the last bulb.

// Return the number of bulbs that are on after n rounds.

function bulbSwitch ( n ) {
	let squares = 0;
	let int = 1;

	while ( ( int**2 ) <= n ) {
		squares++;
		int++;
	}

	return squares;
}

console.log( bulbSwitch( 12 ) );
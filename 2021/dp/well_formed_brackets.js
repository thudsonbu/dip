// Hi, here's your problem today. This problem was recently asked by Apple:

// Given a number n, generate all possible combinations of n well-formed brackets.

function wellFormedBrackets( n ) {
	let combinations = ['()'];

	if ( n == 1 ) {
		return combinations;
	}

	for ( let i = 0; i < n - 1; i++ ) {
		let newCombinations = new Set([]);

		combinations.forEach( combination => {
			let combArr = ( '()' + combination ).split('');
			newCombinations.add( combArr.join('') )
			
			for ( let i = 1; i < combination.length + 1; i++ ) {
				let paren = combArr.splice( i, 1 );
				combArr.splice( i+1, 0, paren );

				newCombinations.add( combArr.join('') );
			}
		});

		combinations = newCombinations;
	}

	return combinations;
}

console.log( wellFormedBrackets( 10 ) );

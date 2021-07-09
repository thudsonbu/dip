// The DNA sequence is composed of a series of nucleotides abbreviated as 
// 'A', 'C', 'G', and 'T'.

// For example, "ACGAATTCCG" is a DNA sequence.
// When studying DNA, it is useful to identify repeated sequences within the DNA.

// Given a string s that represents a DNA sequence, return all the 
// 10-letter-long sequences (substrings) that occur more than once in a DNA 
// molecule. You may return the answer in any order.


/**
 * @param {String} s
 * @return {String[]}
 */
function findRepeatedDnaSequences( s ) {
	let sequenceMap = new Map();
	let foundSet    = new Set();
	let index       = 9;

	while ( index < s.length ) {
		let sequence = s.slice( index-10, index );

		if ( sequenceMap.has( sequence ) ) {
			foundSet.add( sequence );
		} else {
			sequenceMap.set( sequence, true );
		}

		index++;
	}

	return foundSet;
}

console.log( findRepeatedDnaSequences( "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" ) );

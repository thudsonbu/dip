//  Hi, here's your problem today. This problem was recently asked by Facebook:

//  Reshaping a matrix means to take the same elements in a matrix but change the
//  row and column length. This means that the new matrix needs to have the same
//  elements filled in the same row order as the old matrix. Given a matrix, a
//  new row size x and a new column size y, reshape the matrix. If it is not 
//  possible to reshape, return None.

function reshapeMatrix( matrix, x, y ) {
	let newMatrix = [[]];

	// check if problem can be completed
	if ( ( x * y ) !== ( matrix.length * matrix[0].length ) ) {
		return undefined;
	}


	let xIndex = 0;
	let yIndex = 0;
	matrix.forEach( row => {
		row.forEach( item => {
			newMatrix[ yIndex ][ xIndex ] = item;

			xIndex++;

			if ( xIndex === ( x - 1 ) ) {
				xIndex = 0;
				yIndex += 1;
				newMatrix.push( [] );
			}
		});
	});

	return newMatrix;
}

// should not accept matrix size that is not same as start matrix size
const test1 = [
	[ 0, 1 ],
	[ 2, 3 ]
]

console.assert( reshapeMatrix( test1, 2, 4 ) === undefined );

// should reshape a 2 x 2 to a 4 by 1
const res = [
	[ 0, 1, 2, 3 ]
]

console.log( reshapeMatrix( test1, 1, 4 ) );

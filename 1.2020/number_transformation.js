// You are given two positive integers n and m. You have to perform some basic mathematical operations
// on n to obtain m. These are the potential operations:

// (n - 1) / 2  if (n - 1) is divisible by 2
// n / 2 if n is divisible by 2
// n * 2

// m will always be a power of 2

function numberTransform( n, m ) {
  let operations = 0;

  while ( !checkMultipleOfTwo(n) ) {
    
    if ( n % 2 ) {
      n = ( n - 1 ) / 2;
      operations += 1;
    } else {
      n /= 2;
      operations += 1;
    }
  }
  while ( n > m ) {
    n /= 2;
    operations += 1;
  }

  while ( n < m ) {
    n *= 2;
    operations += 1;
  }

  return operations;
}

function checkMultipleOfTwo( n ) {

  if ( n === 0 ) {
    return false;
  }

  let multiple = 1;

  while ( multiple <= n ) {
    
    if ( multiple === n ) {
      return true;  
    }
    multiple *= 2;
  }
  return false;
}

console.log( numberTransform( 2, 2 ) );
console.log( numberTransform( 2, 4 ) );
console.log( numberTransform( 3, 16 ) );
console.log( numberTransform( 1, 4 ) );
console.log( numberTransform( 4, 1 ) );
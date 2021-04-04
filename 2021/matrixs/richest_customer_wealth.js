// You are given an m x n integer grid accounts where accounts[i][j] is the 
// amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that
// the richest customer has.

// A customer's wealth is the amount of money they have in all their bank 
// accounts. The richest customer is the customer that has the maximum wealth.

/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function (accounts) {
  let max = null;
  let cur = 0;

  accounts.forEach( customer => {

    customer.forEach( account => {
      cur += account;
    });

    if ( !max ) {
      max = cur;
    } else if ( cur > max ) {
      max = cur;
    }

    cur = 0;
  })

  return max;
};

let accounts = [
  [ 0, 1, 2 ],
  [ 0, 4, 0 ],
  [ 1, 2, 1 ]
];

console.log(maximumWealth(accounts));
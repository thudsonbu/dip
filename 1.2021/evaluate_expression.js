// Given a relationship between two numbers create a function that returns if the
// relationship is true

// examples:
// 101=101 => true
// 2>1 => false
// 1<2 => false
// 2<=4 => true


function isTrue( relation ) {
  return eval( relation );
}

function isTrueNoEval( relation ) {

  const equal = ( left_num, right_num ) => {
    return Number(left_num) === Number(right_num);
  }

  const greater = ( left_num, right_num ) => {
    return Number(left_num) > Number(right_num);
  }

  const less = ( left_num, right_num ) => {
    return Number(left_num) < Number(right_num);
  }

  const operation = {
    '=' : equal,
    '>' : greater,
    '<' : less,
  }

  const relation_regex = /\D/g;
  const relations = [ ...relation.matchAll(relation_regex) ];

  const nums_regex = /[0-9]*/g;
  const nums = [ ...relation.matchAll(nums_regex) ];

  let out = relations.every( ( element ) => {
    return operation[element]( nums[0], nums[1] );
  })

  return out;
}

console.log(isTrueNoEval( '1=1' )); 
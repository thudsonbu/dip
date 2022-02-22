// Given an adjacency matrix, determine if two nodes are adjacent

function isAdjacent(matrix, node1, node2) {
  let first_link = matrix[ node1 ][ node2 ] === 1;
  let second_link = matrix[ node2 ][ node1 ] === 1;

  return first_link && second_link;
} 
// There are three towers. The objective of the game is to move all the disks over to tower #3.
// You cannot move larger disks on top of smaller disks. Create a function that returns
// the minimum number of steps in order to complete the game.

function towerHanoi(discs) {
  let towers = discs % 2 === 0 ? [[], [1], []] : [[], [], [1]];

  let disc = 2;
  let recent_move = null;
  let moves = 1;

  while (disc <= discs) {
    // place in new disc
    if (towers[1].length) {
      towers[2].push(disc);
      recent_move = 2;
    } else {
      towers[1].push(disc);
      recent_move = 1;
    }

    moves += 1;
    disc += 1;

    while (true) {
      let best_move = findBestMove(towers, recent_move);

      towers = makeMove(towers, best_move);
      moves += 1;

      recent_move = best_move.to;

      if (checkStackComplete(towers)) break;
    }
  }

  return moves;
}

let result = towerHanoi(2);
console.log(result + " should be 3");

result = towerHanoi(3);
console.log(result + " should be 7");

function makeMove(towers, best_move) {
  let top = towers[best_move.from].pop();
  towers[best_move.to].push(top);

  return towers;
}

let towers = [[3], [2], [5, 4, 1]];
let best_move = { score: 2, to: 1, from: 2 };
console.log(makeMove(towers, best_move));
console.log("should be \n[ [ 3 ], [ 2, 1 ], [ 5, 4 ] ]");

function findBestMove(towers, stuck_stack) {
  let best_move = {
    score: -1,
    to: null,
    from: null,
  };

  for (let i = 0; i < 3; i++) {
    if (i === stuck_stack || !towers[i].length) continue;

    for (let j = 0; j < 3; j++) {
      if (j === i) continue;

      let top = towers[i].slice(-1);

      // if its a null place give it a 1
      let bottom;
      if (towers[j].length) {
        bottom = towers[j].slice(-1);
      } else {
        if (best_move.score < 1) {
          best_move.score = 1;
          best_move.to = j;
          best_move.from = i;
        }
        continue;
      }

      // if its one greater give it a two
      if (top == bottom - 1) {
        best_move.score = 2;
        best_move.to = j;
        best_move.from = i;
      }

      // garbage moves go here
    }
  }

  return best_move;
}

towers = [[3], [2], [5, 4, 1]];
console.log(findBestMove(towers, 1));
console.log(" should be \n{ score: 2, to: 1, from: 2 }");

towers = [[], [2, 1], [5, 4, 3]];
console.log(findBestMove(towers, 2));
console.log(" should be \n{ score: 1, to: 0, from: 1 }");

function getStuckStack(towers, recent_move) {
  let loc = 0;
  let out;

  towers.forEach((tower) => {
    if (tower.slice(-1)[0] === recent_move) out = loc;

    loc += 1;
  });

  return out;
}

towers = [[3], [2], [5, 4, 1]];
console.log(getStuckStack(towers, 2) + " should be 1");

towers = [[1], [4, 3, 2], [5]];
console.log(getStuckStack(towers, 1) + " should be 0");

function checkStackComplete(towers) {
  zeros = 0;

  towers.forEach((tower) => {
    if (!tower.length) zeros += 1;
  });

  return zeros === 2;
}

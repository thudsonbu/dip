// There are three towers. The objective of the ggame is to move all the disks over to tower #3.
// You cannot move larger disks on top of smaller disks. Create a function that returns
// the minimum number of steps in order to complete the game.

function towerHanoi( discs ) {
  let towers = dics % 2 === 0 ? [ [], [ 1 ], [] ] : [ [], [], [ 1 ] ];

  let disc = 2;
  let recent_move = null;
  let moves = 1;

  while ( disc <= discs ) {
    
    // place in new disc
    if ( towers[1].length ) {
      towers[2].push( disc );
    } else {
      towers[1].push( disc );
    }

    moves += 1;
    recent_move = disc;
    disc += 1;

    while ( true ) {

      let stuck_stack = getStuckStack( towers, recent_move );
      let swap = false;

      towers, swap, recent_move = tryOneGreaterSwap( towers, stuck_stack );

      if ( !swap ) {
        

      }

    }

  } 

}

function analyzeMoves( towers, stuck_stack ) {
  let best_move = [];

  for ( let i = 0; i < 3; i++ ) {
    if ( i === stuck_stack || !towers[i].length ) continue;

    for ( let j = 0; j < 3; j++ ) {
      if ( j === i ) continue;

      
    }
  }
  
  // for each tower other then stuck

  // compare with other tops

  // skip if tower height is zero

  // if one greater give rating of two

  // if null give rating of 1

  // if greater bottom or odd with odd or even with even give 0


}

function tryOtherSwap( towers, stuck_stack ) {
  let swap = false;
  let recent_move = null;

  for ( let i = 0; i < 3 && !swap; i++ ) {
        
    if ( i === stuck_stack ) continue;

    if ( !towers[i][0] ) continue;
    
    let top_swap = towers[i][0];

    for ( let j = 0; j < 3 && !swap; j++ ) {

      if ( j === i ) continue;

      if ( !towers[j][0] ) continue;

      let below = towers[j][0];

      if ( top_swap < below && top_swap % 2 !== below % 2 ) {
        towers[j].push( top_swap );
        towers[i].pop();
        recent_move = top_swap;
        swap = true;
      }
    }
  }
  
  return towers, swap, recent_move;
}

function tryOneGreaterSwap( towers, stuck_stack ) {
  let swap = false;
  let recent_move = null;

  for ( let i = 0; i < 3 && !swap; i++ ) {
        
    if ( i === stuck_stack ) continue;

    if ( !towers[i][0] ) continue;
    
    let top_swap = towers[i][0];

    for ( let j = 0; j < 3 && !swap; j++ ) {

      if ( j === i ) continue;

      let below = towers[j][0];

      if ( ( top_swap + 1 ) === below ) {
        towers[j].push( top_swap );
        towers[i].pop();
        recent_move = top_swap;
        swap = true;
      }
    }
  }

  return towers, swap, recent_move;
}

function getStuckStack( towers, recent_move ) {
  let loc = 0;

  towers.foreach( (tower) => {

    if ( tower.slice(-1)[0] === recent_move ) return loc;

    loc += 1;
  })
}

function checkStackComplete( towers ) {
  zeros = 0;

  towers.foreach( (tower) => {

    if ( !tower.length ) zeros += 1;
  });

  return zeros === 2;
}

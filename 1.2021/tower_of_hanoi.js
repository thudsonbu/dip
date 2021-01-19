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

      towers, swap = tryOneGreaterSwap( towers, stuck_stack );

      if ( !swap ) {

      }

    }

  } 

}

function tryOneGreaterSwap( towers, stuck_stack ) {
  let swap = false;

  for ( let i = 0; i < 3 && !swap; i++ ) {
        
    if ( i === stuck_stack ) continue;
    
    let top_swap = towers[i][0];

    for ( let j = 0; j < 3 && !swap; j++ ) {

      if ( j === i ) continue;

      let below = towers[j][0];

      if ( ( top_swap + 1 ) === below ) {
        towers[j].push( top_swap );
        towers[i].pop();
        swap = true;
      }
    }
  }

  return towers, swap;
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

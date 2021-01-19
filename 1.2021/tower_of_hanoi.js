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
      towers[1].push( disc );
    } else {
      towers[2].push( disc );
    }

    moves += 1;
    recent_move = disc;
    disc += 1;

    while ( true ) {

      stuck_stack = getStuckStack( towers, recent_move );

    }

  } 


}

function getStuckStack( towers, recent_move ) {
  let loc = 0;

  towers.foreach( (tower) => {

    if ( towers[ towers[loc].length - 1 ] === recent_move ) return loc;
    loc += 1;
  })
}

function checkStackComplete( towers ) {
  zeros = 0;

  towers.foreach( (tower) => {

    if ( tower.length === 0 ) zeros += 1;
  });

  return zeros === 2;
}

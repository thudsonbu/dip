// There are three towers. The objective of the ggame is to move all the disks over to tower #3.
// You cannot move larger disks on top of smaller disks. Create a function that returns
// the minimum number of steps in order to complete the game.

function towerHanoi( discs ) {
  let towers = createTowers( discs );

  // if odd first move is two right else one

  // take one off and place it

  // build stack

}

function createTowers( disks ) {
  let towers = [ [], [], [], ];

  for ( let i = 0; i < disks; i++ ) {
    towers[0].push( i );
  }

  return towers;
}

console.log( createTowers(3) + " should be [ [ 0, 1, 2 ], [], [] ]");
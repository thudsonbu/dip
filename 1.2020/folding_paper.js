// Create a function that returns the thickness (in meters) of a piece of paper
// after folding it n times. The paper begins with a thickness of 0.5mm

function numLayers(n) {
  let thickness_meters = .0005 * ( 2 ** n );  
  return thickness_meters + 'm';
}
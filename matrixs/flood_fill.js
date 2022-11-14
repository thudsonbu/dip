/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
function fillImage(image, sr, sc, color) {
  if (!image?.[sr] || !image?.[sr]?.[sc]) {
    return image;
  }

  if (image[sr][sc] !== color) {
    floodPixel(image, sr, sc, color, image[sr][sc]);
  }

  return image;
}

function floodPixel(image, startRow, startColumn, newColor, oldColor) {
  image[startRow][startColumn] = newColor;

  const isFirstColumn = startColumn === 0;

  if (!isFirstColumn && image[startRow][startColumn - 1] === oldColor) {
    floodPixel(image, startRow, startColumn - 1, newColor, oldColor);
  }

  const isLastColumn = startColumn >= image[startRow].length - 1;

  if (!isLastColumn && image[startRow][startColumn + 1] === oldColor) {
    floodPixel(image, startRow, startColumn + 1, newColor, oldColor);
  }

  const isFirstRow = startRow < 1;

  if (!isFirstRow && image[startRow - 1][startColumn] === oldColor) {
    floodPixel(image, startRow - 1, startColumn, newColor, oldColor);
  }

  const isLastRow = startRow >= image.length - 1;

  if (!isLastRow && image[startRow + 1][startColumn] === oldColor) {
    floodPixel(image, startRow + 1, startColumn, newColor, oldColor);
  }
}

const alphabet = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
];

/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function (sentence) {
  let letterMap = new Map();

  alphabet.forEach((letter) => {
    letterMap.set(letter, true);
  });

  for (let i = 0; i < sentence.length; i++) {
    if (letterMap.has(sentence[i])) {
      letterMap.delete(sentence[i]);
    }
  }

  return letterMap.size === 0;
};

console.log(checkIfPangram("sentence a"));

let goodSentence = alphabet.join("");
console.log(checkIfPangram(goodSentence));
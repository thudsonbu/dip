// given a string containing letters and other characters return the string with
// the order of letters reversed but the position of other characters unchanged.

var reverseOnlyLetters = function (S) {
  let re = /[A-Za-z]/g;
  let chars = S.split("");
  let start = 0;
  let end = S.length - 1;
  let tmp;

  while (true) {
    while ( end > 0 && chars[end].search(re) != 0 ) {
      end -= 1;
    }

    while (start < chars.length && chars[start].search(re) != 0) {
      start += 1;
    }
      
    if (end <= start) break;

    tmp = chars[start];
    chars[start] = chars[end];
    chars[end] = tmp;

    end -= 1;
    start += 1;
  }

  return chars.join("");
};
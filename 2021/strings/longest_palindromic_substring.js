const assert = require("assert");

/**
 * Returns the longest palindromic substring in s
 * @param {string}
 * @return {string}
 */

function longestPalindrome(s) {
  let start;
  let end;
  let longest = "";
  let chars = s.split("");

  for (let i = 2; i < chars.length; i++) {
    end = i;
    start = i - 2;

    while (chars[start] === chars[end]) {
      if (end - start > longest.length) {
        longest = s.substring(start, end + 1);
      }

      if (end === chars.length - 1 || start === 0) {
        break;
      }

      start -= 1;
      end++;
    }
  }

  return longest;
}

assert(longestPalindrome("aba"), "aba");
assert(longestPalindrome("abcdcrs"),"cdc");
assert(longestPalindrome("eicaaoecekeke"), "ekeke")

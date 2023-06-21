import _ from "lodash";

function insertToSortedArray<T>({
  array,
  element,
  getValue,
}: {
  array: T[];
  element: T;
  getValue: (element: T) => number;
}) {
  if (!array.length) {
    array.push(element);
    return;
  }
  const elementValue = getValue(element);
  let lowPointer = 0;
  let highPointer = array.length - 1;
  let midPointer = Math.floor((highPointer - lowPointer) / 2);
  while (lowPointer < highPointer - 1) {
    if (getValue(array[midPointer]) >= elementValue) {
      highPointer = midPointer;
    } else {
      lowPointer = midPointer;
    }
    midPointer = lowPointer + Math.floor((highPointer - lowPointer) / 2);
  }
  if (elementValue < getValue(array[lowPointer])) {
    array.splice(lowPointer, 0, element);
  } else if (elementValue < getValue(array[highPointer])) {
    array.splice(highPointer, 0, element);
  } else {
    array.splice(highPointer + 1, 0, element);
  }
}

const array = [];

const getValue = (el) => JSON.parse(el).value;

const lodashArray = [];
console.time("lodash");
for (let i = 0; i < 100000; i++) {
  const element = JSON.stringify({ value: Math.random() * 100 });
  lodashArray.splice(_.sortedIndexBy(lodashArray, getValue), 0, element);
}
console.timeEnd("lodash");

const myArray = [];
console.time("myArray");
for (let i = 0; i < 100000; i++) {
  const element = JSON.stringify({ value: Math.random() * 100 });
  insertToSortedArray({
    array: myArray,
    element,
    getValue
  });
}
console.timeEnd("myArray");

outer: for (let i = 0; i < 1000; i++) {
  insertToSortedArray({
    array,
    element: Math.random() * 100,
    getValue: (el) => el,
  });
  const arrayCopy = [...array];
  arrayCopy.sort((a, b) => a - b);
  for (let i = 0; i < array.length; i++) {
    if (array[i] !== arrayCopy[i]) {
      console.log(array, arrayCopy, array[i], arrayCopy[i]);
      break outer;
    }
  }
}

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

outer: for (let i = 0; i < 1000; i++) {
  insertToSortedArray({
    array,
    element: Math.random() * 100,
    getValue: (el) => el,
  });
  const arrayCopy = [...array];
  arrayCopy.sort((a, b) => a - b);
  inner: for (let i = 0; i < array.length; i++) {
    if (array[i] !== arrayCopy[i]) {
      console.log(array, arrayCopy, array[i], arrayCopy[i]);
      break outer;
    }
  }
}

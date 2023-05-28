// Design a class to find the kth largest element in a stream. Note that it is
// the kth largest element in the sorted order, not the kth distinct element.

class KthLargest {
  numbers: number[];
  k: number;

  constructor(k: number, numbers: number[]) {
    this.numbers = numbers.sort().slice(-k);
    this.k = k;
  }

  add(nextNumber: number): number {
    let highIndex = this.numbers.length - 1;
    let lowIndex = 0;

    let middleIndex = 0;
    while (highIndex > lowIndex + 1) {
      middleIndex = Math.floor((highIndex - lowIndex) / 2) + lowIndex;

      if (this.numbers[middleIndex] >= nextNumber) {
        highIndex = middleIndex;
      } else {
        lowIndex = middleIndex;
      }
    }

    let spliceIndex = lowIndex;
    if (
      this.numbers[lowIndex] < nextNumber &&
      this.numbers[highIndex] > nextNumber
    ) {
      spliceIndex = lowIndex + 1;
    } else if (this.numbers[highIndex] < nextNumber) {
      spliceIndex = highIndex + 1;
    }

    this.numbers.splice(spliceIndex, 0, nextNumber);

    if (this.numbers.length > this.k) {
      this.numbers.shift();
    }

    return this.numbers[0];
  }
}

const myKLargest = new KthLargest(2, [0]);

console.log(myKLargest.add(-1));
console.log(myKLargest.numbers);
console.log(myKLargest.add(9));
console.log(myKLargest.numbers);

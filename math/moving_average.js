/**
 * @param {number} size
 */
var MovingAverage = function (size) {
  this.size = size;
  this.sum = 0;
  this.q = [];
};

/**
 * @param {number} val
 * @return {number}
 */
MovingAverage.prototype.next = function (val) {
  if (this.q.length >= this.size) {
    const popped = this.q.pop();
    this.sum -= popped;
  }

  this.q.unshift(val);
  this.sum += val;

  return this.sum / this.q.length;
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */

const LOG_SEPARATOR = '#';

type LogEntry = string;

class SnapshotArray {
  private currentVersion: number;
  private changeLogMatrix: number[][][];

  constructor(length: number) {
    this.currentVersion = 0;
    this.changeLogMatrix = Array.from({ length }, () => [[0,0]]);
  }

  set(index: number, val: number): void {
    const indexLog = this.changeLogMatrix[index];
    const lastLog = indexLog[indexLog.length - 1];
    const logVersion = lastLog[0];
    if (+logVersion === this.currentVersion) {
      this.changeLogMatrix[index][indexLog.length-1] = [this.currentVersion, val];
    } else {
      this.changeLogMatrix[index].push([this.currentVersion, val]);
    }
  }

  snap(): number {
    this.currentVersion++;
    return this.currentVersion - 1;
  }

  get(index: number, snap_id: number): number {
    const indexLog = this.changeLogMatrix[index];
    for (let i = indexLog.length - 1; i >= 0; i--) {
      const [ logVersion, logValue ] = indexLog[i];
      if (+logVersion <= snap_id) return +logValue;
    }
  }
}

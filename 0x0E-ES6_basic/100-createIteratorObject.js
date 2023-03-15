export default function createIteratorObject(report) {
    report = report.allEmployees;
    const values = Object.values(report);
    const iterator = [];
    for (const value of values) {
        iterator.push(...value);
    }
    return iterator
}
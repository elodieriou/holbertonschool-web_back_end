export default function createIteratorObject(report) {
  const { allEmployees } = report;
  const values = Object.values(allEmployees);
  const iterator = [];
  for (const value of values) {
    iterator.push(...value);
  }
  return iterator;
}

export default function cleanSet(set, startString) {
  if (startString === '' || startString === undefined) {
    return '';
  }

  const startBy = [];
  set.forEach((element) => {
    if (element !== undefined && element.startsWith(startString)) {
      startBy.push(element.substring(startString.length));
    }
  });

  return startBy.join('-');
}

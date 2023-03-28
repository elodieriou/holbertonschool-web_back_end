export default function cleanSet(set, startString) {
  if (!startString) {
    return '';
  }

  const startBy = [];
  set.forEach((element) => {
    if (element !== undefined && element.startsWith(startString)) {
      startBy.push(element.slice(startString.length));
    }
  });

  return startBy.join('-');
}

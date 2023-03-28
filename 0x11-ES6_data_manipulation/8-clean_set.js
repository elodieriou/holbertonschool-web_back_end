export default function cleanSet(set, startString) {
  if (!startString && startString === '') {
    return '';
  }

  const startBy = [];
  set.forEach((element) => {
    if (element && element.startsWith(startString)) {
      startBy.push(element.slice(startString.length));
    }
  });

  return startBy.join('-');
}

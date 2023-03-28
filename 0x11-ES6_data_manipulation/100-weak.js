const weakMap = new WeakMap();
function queryAPI(endpoint) {
  const count = weakMap.get(endpoint) || 0;

  if (count + 1 >= 5) {
    throw new Error('Endpoint load is high');
  }

  weakMap.set(endpoint, count + 1);
}

export { weakMap, queryAPI };

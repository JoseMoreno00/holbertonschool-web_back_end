export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw Error('Cannot process');
  for (const data of map) if (data[1] === 1) map.set(data[0], 100);
  return map;
}

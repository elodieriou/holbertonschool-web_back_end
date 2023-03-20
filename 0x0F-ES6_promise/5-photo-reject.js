export default function uploadPhoto(filename) {
  return new Promise((resolve, reject) => {
    const error = new Error(`${filename} cannot be processed`);
    reject(error);
  });
}

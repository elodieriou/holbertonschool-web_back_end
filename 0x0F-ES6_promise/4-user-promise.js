export default function signUpUser(firstName, lastName) {
  return new Promise((resolve) => {
    const success = { firstName, lastName };
    resolve(success);
  });
}

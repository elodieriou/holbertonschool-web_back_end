import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstname, lastname, fileName) {
  const promise1 = signUpUser(firstname, lastname);
  const promise2 = uploadPhoto(fileName);

  return Promise
    .allSettled([promise1, promise2])
    .then((values) => values);
}

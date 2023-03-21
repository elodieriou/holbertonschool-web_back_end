import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = signUpUser(firstName, lastName);
  const promise2 = uploadPhoto(fileName);

  return Promise
    .allSettled([promise1, promise2])
    .then((values) => values
      .map((v) => ({ status: v.status, value: v.status === 'fulfilled' ? v.value : `${v.reason.name}: ${v.reason.message}` })));
}

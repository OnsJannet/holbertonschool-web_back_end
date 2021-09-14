import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const user = await signUpUser(firstName, lastName);
  let photo = null;
  try {
    photo = await uploadPhoto(fileName);
  } catch (error) {
    photo = `${error.name}: ${error.message}`;
  }
  const promise1 = { status: 'fulfilled', value: user };
  const promise2 = { status: 'rejected', value: photo };
  return [promise1, promise2];
}

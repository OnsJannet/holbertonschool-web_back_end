export default function signUpUser(firstName, lastName) {
  const body = { firstName, lastName };
  return Promise.resolve({
    body,
  });
}

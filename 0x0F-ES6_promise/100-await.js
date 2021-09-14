import { createUser, uploadPhoto } from './utils';

export default async function asyncUploadUser() {
  const user = await createUser();
  const photo = await uploadPhoto();
  try {
    return {
      user,
      photo,
    };
  } catch (error) {
    return {
      photo: null,
      user: null,
    };
  }
}

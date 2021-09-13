function getResponseFromAPI() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve();
    });
  });
}

export default getResponseFromAPI;

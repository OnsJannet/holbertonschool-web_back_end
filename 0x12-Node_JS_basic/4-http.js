const http = require('http');

const port = 1245;
const requestListener = function listener(req, res) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
};
const app = http.createServer(requestListener);
app.listen(port);

module.exports = app;

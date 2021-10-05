import redis from "redis";
const client = redis.createClient();

client.on("connect", function() {
  console.log("Redis client connected to the server");
});

client.on("error", function(error) {
  console.log(`Redis client not connected to the server: ${error.toString()}`);
});

client.subscribe("holberton school channel");

client.on("message", function(channel, message) {
  if (channel === "holberton school channel") {
    console.log(message);
    if (message === "KILL_SERVER") {
      client.unsubscribe();
      client.quit();
    }
  }
});

import redis from "redis";
const client = redis.createClient();

client.on("connect", function() {
  console.log("Redis client connected to the server");
});

client.on("error", function(error) {
  console.log(`Redis client not connected to the server: ${error.toString()}`);
});

const hash = "HolbertonSchools"
client.hset(hash, "Portland", 50, redis.print);
client.hset(hash, "Seattle", 80, redis.print);
client.hset(hash, "New York", 20, redis.print);
client.hset(hash, "Bogota", 20, redis.print);
client.hset(hash, "Cali", 40, redis.print);
client.hset(hash, "Paris", 2, redis.print);

client.hgetall(hash, function(err, response) {
  console.log(response)
});

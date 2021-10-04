import redis from "redis";
const client = redis.createClient();

client.on("connect", function() {
  console.log("Redis client connected to the server");
});

client.on("error", function(error) {
  console.log(`Redis client not connected to the server: ${error.toString()}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, function(err, response) {
    console.log(response);
  });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

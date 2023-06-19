// import { createClient } from 'redis';
import redis from 'redis';
import { promisify } from 'util';
// import promisify from 'utils';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

// const set = promisify(client.set).bind(client)
const get = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const reply = await get(schoolName);
  console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

/* const hashes = [
  'Portland', '50',
  'Seattle', '80',
  'New York', '20',
  'Bogota', '20',
  'Cali', '40',
  'Paris', '2'
]; */

const hashes = new Set([
  ['Portland', '50'],
  ['Seattle', '80'],
  ['New York', '20'],
  ['Bogota', '20'],
  ['Cali', '40'],
  ['Paris', '2'],
]);

for (const [field, value] of hashes) {
  client.hset('HolbertonSchools', field, value, print);
}
// client.hset('HolbertonSchools', ...fieldsAndValues, print)

client.hgetall('HolbertonSchools', (err, object) => {
  console.log(object);
});

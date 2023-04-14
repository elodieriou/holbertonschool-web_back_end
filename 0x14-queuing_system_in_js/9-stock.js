import express from 'express';
import redis from 'redis';
import util from 'util';

// Utils

const listProducts = [
  {
    id: 1, name: 'Suitcase 250', price: 50, stock: 4,
  },
  {
    id: 2, name: 'Suitcase 450', price: 100, stock: 10,
  },
  {
    id: 3, name: 'Suitcase 650', price: 350, stock: 2,
  },
  {
    id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
  },
];

function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

// Server redis

const client = redis.createClient();
const getAsync = util.promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});
function reserveStockById(itemId, stock) {
  client.set(itemId, stock, redis.print);
}

async function getCurrentReservedStockById(itemId) {
  const reply = await getAsync(itemId);
  return reply;
}

// API express

const port = 1245;
const app = express();
const itemNotFound = { status: 'Product not found' };

app.get('/list_products', (request, response) => {
  response.send(listProducts);
});

app.get('/list_products/:itemId', async (request, response) => {
  const itemId = Number(request.params.itemId);
  const item = getItemById(itemId);
  if (!item) response.send(itemNotFound);

  else {
    let currentStock = await getCurrentReservedStockById(itemId);
    currentStock = currentStock === null ? item.stock : currentStock;
    item.currentStock = currentStock;
    response.send(item);
  }
});

app.get('/reserve_product/:itemId', async (request, response) => {
  const itemId = Number(request.params.itemId);
  const item = getItemById(itemId);
  if (!item) response.send(itemNotFound);
  else {
    let currentStock = await getCurrentReservedStockById(itemId);
    if (currentStock === null) currentStock = item.stock;

    const itemNotEnough = { status: 'Not enough stock available', itemId };
    if (currentStock < 1) response.send(itemNotEnough);
    else {
      const reserveStock = { status: 'Reservation confirmed', itemId };
      reserveStockById(itemId, Number(currentStock) - 1);
      response.send(reserveStock);
    }
  }
});

app.listen(port, () => {
  // Initialize value for the exercice when Redis start (NOT doing this in real situation)
  listProducts.forEach((product) => {
    reserveStockById(product.id, product.stock);
  });
});
module.exports = app;

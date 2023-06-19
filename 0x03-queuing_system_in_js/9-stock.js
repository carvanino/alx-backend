//import redis from 'redis';
const redis = require('redis');
const express = require('express');

const app = express();
const port = 1245

const client = redis.createClient();

const listProducts = [
        {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
        {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
        {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
        {id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
]

function getItemById(id) {
	for (const product of listProducts) {
		if ('id' in product) {
			return product
		}
	}
}

app.get('/list_products', (req, res) => {
	res.send(listProducts)
});

app.get('/list_products/:itemId', (req, res) => {
	const itemId = req.params.itemId
	const product = listProducts.find((p) => parseInt(p.id) === parseInt(itemId));
	if (!product) {
		res.send({'status': 'Product not found'})
	} else {
		res.send(product)
	}
});
app.get('/reserve_product/:itemId', (req, res) => {
	const itemId = req.params.itemId;
	const product = listProducts.find((p) => parseInt(p.id) === parseInt(itemId));
	// const product = listProducts.find((p) => p.id === itemId);
	if (!product) {
		res.send({'status': 'Product not found'})
	}
	if (product.stock > 1) {
		reserveStockById(itemId, listProducts);
		res.send({'status' : 'Reservation confirmed', 'itemId': itemId});
		return;
	} else {
		res.send({'status': 'Not enough stick available', 'itemId': itemId})
	}
});

// console.log(getItemById(4));


app.listen(port, () => {
	console.log(`App listening on port ${port}`)
})


function reserveStockById(id, stock) {
	product = getItemById(id);
	client.set(id, product);
}

async function getCurrentReservedStockById(id) {
	return client.get(id);
}


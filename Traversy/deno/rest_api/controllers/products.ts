import { v4 } from 'https://deno.land/std/uuid/mod.ts';
import { Product } from '../types.ts';

let products: Product[] = [
	{
		id: '1',
		name: 'Product One',
		description: 'This is product one',
		price: 29.99,
	},
	{
		id: '2',
		name: 'Product Two',
		description: 'This is product two',
		price: 39.99,
	},
	{
		id: '3',
		name: 'Product Three',
		description: 'This is product three',
		price: 59.99,
	},
];

// @desc Get all Products
// @route GET /api/products
const getProducts = ({ response }: { response: any }) => {
	response.body = {
		success: true,
		data: products,
	};
};

// @desc Get product by id
// @route GET /api/products/:id
const getProduct = ({
	params,
	response,
}: {
	params: { id: string };
	response: any;
}) => {
	let product: Product | undefined = products.find(
		(product) => product.id === params.id
	);

	if (product) {
		response.status = 200;
		response.body = {
			success: true,
			data: product,
		};
	} else {
		response.status = 404;
		response.body = {
			success: false,
			msg: 'No product found',
		};
	}
};

// @desc Add a product
// @route POST /api/products
const addProduct = async ({
	request,
	response,
}: {
	request: any;
	response: any;
}) => {
	const body = await request.body();

	if (!request.body) {
		response.status = 400;
		response.body = {
			success: false,
			msg: 'Please supply some data',
		};
	} else {
		const product: Product = body.value;
		product.id = v4.generate();
		products.push(product);
		response.status = 201;
		response.body = {
			success: true,
			data: product,
		};
	}
};

// @desc update a product
// @route PUT /api/products/:id
const updateProduct = async ({
	params,
	request,
	response,
}: {
	params: { id: string };
	request: any;
	response: any;
}) => {
	const product = products.find((product) => product.id === params.id);

	if (!product) {
		response.status = 400;
		response.body = {
			success: false,
			msg: 'No product by that id exists',
		};
	} else {
		const body = await request.body();

		const updateData: { name?: string; description?: string; price?: number } =
			body.value;

		products = products.map((product) =>
			product.id === params.id ? { ...product, ...updateData } : product
		);
		response.status = 201;
		response.body = {
			success: true,
			data: products,
		};
	}
};

// @desc Delete a project
// @route /api/products/:id
const deleteProduct = ({
	params,
	response,
}: {
	params: { id: string };
	response: any;
}) => {
	const product: Product | undefined = products.find(
		(product) => product.id === params.id
	);

	if (!product) {
		response.status = 400;
		response.body = {
			success: false,
			msg: 'Product not found',
		};
	} else {
		const updatedProducts = products.filter(
			(product) => product.id !== params.id
		);
		products = updatedProducts;
		response.status = 200;
		response.body = {
			success: true,
			data: products,
		};
	}
};

export { getProducts, getProduct, addProduct, updateProduct, deleteProduct };

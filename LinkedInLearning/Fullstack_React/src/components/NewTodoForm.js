import React, { useState } from 'react';

const NewTodoForm = () => {
	const [value, setValue] = useState('');

	return (
		<div>
			<input
				type='text'
				value={value}
				placeholder='New Todo'
				onChange={(e) => setValue(e.target.value)}
			/>
			<button>Create Todo</button>
		</div>
	);
};

export default NewTodoForm;

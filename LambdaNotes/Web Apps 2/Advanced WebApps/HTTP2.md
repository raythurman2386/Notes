# HTTP/AJAX II
## PUT requests with axios

When data needs to be updated we use a PUT HTTP response to do so.

PUT is the U in CRUD and it stands for update

    axios
      .put(`webAddressGoesHere${updatingId}`, data)
      .then(// returned success message)
      .catch(// returned error message)

## DELETE Request
The DELETE HTTP request method is also the D in CRUD.
We use this to delete or destroy items

    axios
      .delete(`url will go here ${deletingItem}`)
      .then(// success)
      .catch(// error)

Delete does not need any data passed down to it

I will only require the id of what you are wanting deleted to be in the URL.
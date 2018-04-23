def func(self):
	data = {"message": "Hello people!"}
	self.datastore.write_dict(data)
	return "data written"
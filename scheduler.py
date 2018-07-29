def func(self):
	from core import responses
	import json
	data = {"message": "Hello people!"}
	self.datastore.write_dict(data)
	return responses.JSONResponse(json.dumps({"message": "Data written to datastore"}))

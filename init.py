def func(self):
	import json
	from core import responses
	return responses.JSONResponse(json.dumps({"message": "Running Init"}))
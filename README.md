# optim


Combine and minify js files.


## Quick start

Create a .json configuration file:

	{
	    "version": "1",
	    "base": "./",
	    "output": "./build",
	    "files": [
	        "/js/file1.js",
	        "/js/file2.js",
	        "/js/file3.js"
	    ]
	}

Include the optim lib with the .json file in its attribute "data-optim":

	<html>
	<head></head>
	<body>	
		<!-- app ui here -->
		<script data-optim="config.json" src="/static/lib/optim.min.js"></script>
	</body>
	</html>

Build the app:
		
	python optim.py myapp/config.json uglifyjs


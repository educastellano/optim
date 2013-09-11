# optim


Combine and minify js files.


## Quick start

Create a .json configuration file:

 	{
    	"version": "1",
	    "basepath": "../../",
    	"minified_file": "build/app.min.js",
	    "files": [
        	"/static/app/file1.js",
			"/static/app/file2.js",
	        "/static/app/file3.js"
    	]
	}

Include the .json file path in a global variable called "\__optim_file__", and the optim lib:

	<html>
	<head></head>
	<body>
		<!-- app ui here -->
		<script>
        	window.__optim_file__ = '/static/app/config.json';
		</script>
		<script src="/static/lib/optim.min.js"></script>
	</body>
	</html>

Build the app:
		
	python optim.py myapp/config.json uglifyjs


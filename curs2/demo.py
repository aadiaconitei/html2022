# to open/create a new html file in the write mode
f = open('demo.html', 'w')
  
# the html code which will go in the file 
html_template = """
<html>
<head>
<title>Demo</title>
</head>
<body>
<h2>Curs  HTML CSS </h2>
  
<p>Bine ati venit!.</p>
  
</body>
</html>
"""
  
# writing the code into the file
f.write(html_template)
  
# close the file
f.close()
import urllib
for i in range(1,83):
    urllib.urlretrieve("http://mitpress.mit.edu/sites/default/files/titles/content/sicm/book-Z-H-"+str(i)+".html","book-Z-H-"+str(i)+".html")

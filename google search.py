import googlesearch
search = googlesearch.search("what is python", stop = 10)
for i in search:
	print(i)

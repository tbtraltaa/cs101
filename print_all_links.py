import urllib

def get_page(url):
	try:
		return str(urlopen(url).read())
	except:
		return ""

def get_next_target(page):
	
	start= page.find('<a href=')
	if start ==-1:
		return None,0
	start_quote= find(page,'"',start)
	end_quote = page.find('"',start_quote+1)
	url= page[start_quote+1:end_quote]
	return url, end_quote

def print_all_links(page):
	while True:
		url,endpos=get_next_target(page)
		if url:
			print url
			page= page[endpos:]
		else:
			break

#print_all_links(get_page('http://xkvd.com/353'))
#print_all_links(get_page('http://xkvd.com/353'))
#print_all_links(get_page('http://xkvd.com/353'))
print get_page('http://xkvd.com/353')
print_all_links(get_page("http://www.mobinet.mn"))

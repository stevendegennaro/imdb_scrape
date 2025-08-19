#### When I rewrote the code for publication, I didn't want to have to 
#### redo every list from scratch, so I wrote some helper functions
#### to put each intermediate file in a format that matched the final
#### updated versions of the functions.



# Cleanup function to combine horror and thriller files to new format
# horror = pd.read_csv("data/horrorculledimdb_urls.csv",header=None)
# horror.columns = ['id','title','url','year','run_time','imdb_url']
# horror.set_index('id',inplace = True)
# horror['genre'] = 'Horror'
# thriller = pd.read_csv("data/thrillerculledimdb_urls.csv")
# thriller.columns = ['id','title','url','year','run_time','imdb_url']
# thriller.set_index('id',inplace = True)
# thriller['genre']='Thriller'

# with open('data/horrorimdbinfoformatted.json','r') as f:
#   horrorformatted = json.load(f)
# horror_stars = pd.DataFrame([[h['lb_id'],h['lb_stars']] for h in horrorformatted])
# horror_stars.columns = ['lb_id','lb_stars']
# horror_stars.set_index('lb_id',inplace=True)

# with open('data/thrillerimdbinfoformatted.json','r') as f:
#   thrillerformatted = json.load(f)
# thriller_stars = pd.DataFrame([[h['lb_id'],h['lb_stars']] for h in thrillerformatted])
# thriller_stars.columns = ['lb_id','lb_stars']
# thriller_stars.set_index('lb_id',inplace=True)

# pd.set_option('display.max_rows', None)
# horror = horror.join(horror_stars)
# horror.replace({float("NaN"): None},inplace=True)
# thriller = thriller.join(thriller_stars)
# thriller.replace({float("NaN"): None},inplace=True)

# pd.concat([horror,thriller]).to_csv("data/culledimdb_urls.csv")



###### Cleanup function to take 
###### horrorimdbinfoformatted.json and thrillerimdbinfoformatted.json
###### And combine and look for additional info
# def populate_list_details_cleanup():
# 	# Open the files that have most of the info we need
# 	with open('data/old-intermediates/thrillerimdbinfoformatted.json') as f:
# 		thriller_dicts = json.load(f)
# 	with open('data/old-intermediates/horrorimdbinfoformatted.json') as f:
# 		horror_dicts = json.load(f)

# 	for movie in horror_dicts:
# 		movie['genre'] = 'horror'

# 	for movie in thriller_dicts:
# 		movie['genre'] = 'thriller'

# 	dicts = horror_dicts + thriller_dicts

# 	with open('imdb_cookies.txt','r') as f:
# 		cookies = ast.literal_eval(f.readline())
# 		headers = ast.literal_eval(f.readline())

# 	with open('data/imdbinfoformatted.json','w') as outputfile:
# 		outputfile.write("[\n")

# 		for this_movie in dicts:
# 			try:
# 				print(this_movie['title'])
# 				# Change key for genres to imdb_genres
# 				this_movie['imdb_genres'] = this_movie['genres']
# 				del this_movie['genres']

# 				for company in this_movie['prodcos']:
# 					company['company_meter'] = int(company['company_meter'])
# 				for company in this_movie['distributors']:
# 					company['company_meter'] = int(company['company_meter'])
# 				for company in this_movie['sales']:
# 					company['company_meter'] = int(company['company_meter'])

# 				# Open imdbpro page for this movie
# 				pagename = f"https://pro.imdb.com/title/{this_movie['imdb_id']}/filmmakers"
# 				page = requests.get(pagename,cookies=cookies, headers=headers)
# 				tree = html.fromstring(page.content)

# 				directors = tree.xpath('//div[@id="title_filmmakers_director_sortable_table_wrapper"]//tr[@class="filmmaker"]//span[@class="a-size-base-plus"]//a/text()')
# 				directorcredits = tree.xpath('//div[@id="title_filmmakers_director_sortable_table_wrapper"]//tr[@class="filmmaker"]//span[@class="see_more_text_collapsed"]/text()')
# 				directorlinks = tree.xpath('//div[@id="title_filmmakers_director_sortable_table_wrapper"]//tr[@class="filmmaker"]//span[@class="a-size-base-plus"]//a/@href')
# 				this_movie['directors'] = [{'name': name.strip(), 'credit': re.sub(r'\s+', ' ', credit).strip(), 'link': link.strip()} 
# 											for name, credit, link in zip(directors, directorcredits,directorlinks)]

# 				writers = tree.xpath('//div[@id="title_filmmakers_writer_sortable_table_wrapper"]//tr[@class="filmmaker"]//span[@class="a-size-base-plus"]//a/text()')
# 				writercredits = tree.xpath('//div[@id="title_filmmakers_writer_sortable_table_wrapper"]//tr[@class="filmmaker"]//span[@class="see_more_text_collapsed"]/text()')
# 				writerlinks = tree.xpath('//div[@id="title_filmmakers_writer_sortable_table_wrapper"]//tr[@class="filmmaker"]//span[@class="a-size-base-plus"]//a/@href')
# 				this_movie['writers'] = [{'name': name.strip(), 'credit': re.sub(r'\s+', ' ', credit).strip(), 'link': link.strip()} 
# 											for name, credit, link in zip(writers, writercredits,writerlinks)]

# 				producers = tree.xpath('//div[@id="title_filmmakers_producer_sortable_table_wrapper"]//tr[@class="filmmaker"]//span[@class="a-size-base-plus"]//a/text()')
# 				producercredits = tree.xpath('//div[@id="title_filmmakers_producer_sortable_table_wrapper"]//tr[@class="filmmaker"]//span[@class="see_more_text_collapsed"]/text()')
# 				producerlinks = tree.xpath('//div[@id="title_filmmakers_producer_sortable_table_wrapper"]//tr[@class="filmmaker"]//span[@class="a-size-base-plus"]//a/@href')
# 				this_movie['producers'] = [{'name': name.strip(), 'credit': re.sub(r'\s+', ' ', credit).strip(), 'link': link.strip()} 
# 											for name, credit, link in zip(producers, producercredits,producerlinks)]

# 				# Cast (same info as directors etc but also get Star Meter)
# 				pagename = f"https://pro.imdb.com/title/{this_movie['imdb_id']}/cast"
# 				page = requests.get(pagename,cookies=cookies, headers=headers)
# 				tree = html.fromstring(page.content)
# 				nactors = len(tree.xpath('//table[@id="title_cast_sortable_table"]//a[@data-tab="cst"]/text()'))
# 				actors = tree.xpath('//table[@id="title_cast_sortable_table"]//a[@data-tab="cst"]/text()')
# 				actorlinks = tree.xpath('//table[@id="title_cast_sortable_table"]//tr/td[1]//a[@data-tab="cst"]/@href')
# 				actorcredits = tree.xpath('//table[@id="title_cast_sortable_table"]//tr//span[@class="see_more_text_collapsed"]/text()')
# 				starmeters = tree.xpath(f'//table[@id="title_cast_sortable_table"]//tr//td[@class="a-text-right"]//text()')
# 				this_movie['actors'] = [{'name': name.strip(), 
# 										 'credit': re.sub(r'\s+', ' ', credit).strip(), 
# 										 'link': link.strip(),
# 										 'starmeter': int(starmeter.strip().replace(",",""))} 
# 											for name, credit, link, starmeter in zip(actors, actorcredits, actorlinks, starmeters)]

# 				outputfile.write(json.dumps(this_movie,indent = 4))
# 				outputfile.write(",\n")
# 				outputfile.flush()

# 			except KeyboardInterrupt:
# 				exit()
# 			except Exception as e:
# 				print(repr(e))
# 				print(traceback.format_exc())
# 				print(this_movie['title'])
# 				continue

# 		outputfile.write("]")
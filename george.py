import tweepy, random



CONSUMER_KEY = 'ZQtHZ8ywyjXMQBQrEL7oxK5g7'
CONSUMER_SECRET = 'BwugsWrr2GK3SoF7Z05cHRQO5EW0096wNyyQsx5AwrDej6QbwX'
ACCESS_KEY = '995088381993537536-5U0e83pKpwC2aAoHobLsZGuF8vASiuy'
ACCESS_SECRET = 'cPhFmZBlwOMpaZV02MgMsuKwUfhajCQNSlJh9AMWwwYXw'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



departure = {
	'Departure1': ' Me and Lennie departed after Lennies Aunt died. We travelled up and down west until we found jobs, and Lenny would kill something, and we would be out of a job again.', 
	'Departure2': ' Our departure started when we arrived at our new job. I was suspicious of the lice killer sitting on the bedside. It felt like we were really entering the belly of the whale, because I saw few scenarios where me and Lenny would make it out.',
	'Departure3': ' Me and Lenny sort of formed our own call to adventure. We kept imagining owning our own farm, where Lenny could tend to the rabbits, and I got finally enjoy life without having to stress over keeping a job. Too bad we never had any money.'
} # departure quotes

initiation = {
	'Initiation1': ' Our initiation started when Lenny and I were dropped off four miles off of our actual destination. We had to walk a road of trials, and frankly trying to get Lenny from one place to another without him killing something is hard.',
	'Initiation2': ' For Lennie, that damned Curlys wife appeared as a temptress. Ive seen plenty of her type in my time, but Lennie doesnt remember much of anything of his, and that lady messed both of us right up when he snapped her mousy little neck.'
} #Initiation quotes

ret = {
	'Return1': ' You know, at first I had a refusal of the call of any of these other men to just work til death, Barely able to afford more than a shot, I thought I was different, I thought me and Lennie could make it to the ranch.',
	'Return2': ' The guilt sits in the back of my mind like a tick hanging by the edge its little insect legs to a dirty dog. I wish I didn’t kill Lennie, but I had to. I had to kill him so that I would have the freedom to live a normal life. A better life.'
} # Return quotes



class BotStreamer(tweepy.StreamListener):
    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name #Setting username to equal the @ of the original sender
        status_id = status.id

        # entities provide structured data from Tweets including resolved URLs, media, hashtags and mentions without having to parse the text to extract that information
	tweet_text = status.text

	print(status.user.screen_name + ' tweeted you ' + status.text)

	if 'separation' in tweet_text or 'departure' in tweet_text:
		api.update_status('@' + username + random.choice(departure.values()))
		print (username + ' sent ' + tweet_text + ' and we  responded with a departure quote')
	elif 'initiation' in status.text:
		api.update_status('@' + username + random.choice(initiation.values()))
		print (username + ' sent ' + tweet_text + ' responded with initiation quote')
	elif 'return' in status.text:
		api.update_status('@' + username + random.choice(ret.values()))
		print (username + ' sent ' + tweet_text + 'responded with return quote')
	elif 'whats up' in tweet_text:
		api.update_status('@' + username + ' not much wasuup w u?')


myStreamListener = BotStreamer()
# Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['GeorgioMilton']) #filter the stream for tweets with "nickiboi_c" in them

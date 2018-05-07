import tweepy, random

CONSUMER_KEY = 'lq6ryVXnIKRyQGmFi5uEqMLPJ'
CONSUMER_SECRET = 'EylINJoPTDL9ij808SaOkT5yGr4aLf44wpu2IjXziTYrv13DBc'
ACCESS_KEY = '993250657003024384-KF0WjjIz9DNPoc4FIORetZjVDvOCKR4'
ACCESS_SECRET = 'YFOZqXxdr9jxzP8nCwh5QdIv0nNuOnudqGSyPCvqqZK2t'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

separation = {'Separation1': ' Placeholder1', 'Separation2': ' Placeholder'}
departure = {'Departure1': 'Placeholder', 'Departure2': 'Placeholder'}
initiation = {'Initiation1': 'Placeholder', 'Initiation2': 'Placeholder'}
ret = {'Return1': 'Placeholder', 'Return2': 'Placeholder'}



class BotStreamer(tweepy.StreamListener):
    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id

        # entities provide structured data from Tweets including resolved URLs, media, hashtags and mentions without having to parse the text to extract that information
        print(status.user.screen_name + ' tweeted you ' + status.text)
	if 'separation' in status.text:
		api.update_status('@'+ username + random.choice(separation.values()))
	if 'departure' in status.text:
		api.update_status('@' + username + random.choice(departure.values()))
	if 'initiation' in status.text:
		api.update_status('@' + username + random.choice(initiation.values()))
	if 'return' in status.text:
		api.update_status('@' + username + random.choice(ret.values()))


myStreamListener = BotStreamer()
# Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@nickiboi_c'])

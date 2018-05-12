# -*- coding: utf-8 -*-

import tweepy, random



CONSUMER_KEY = 'lq6ryVXnIKRyQGmFi5uEqMLPJ'
CONSUMER_SECRET = 'EylINJoPTDL9ij808SaOkT5yGr4aLf44wpu2IjXziTYrv13DBc'
ACCESS_KEY = '993250657003024384-KF0WjjIz9DNPoc4FIORetZjVDvOCKR4'
ACCESS_SECRET = 'YFOZqXxdr9jxzP8nCwh5QdIv0nNuOnudqGSyPCvqqZK2t'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



departure = {
	'Departure1': ' My family were well-to-do people in this MidWest city for 3 genz. Im a WW1vet. My departure started when I came East supposedly permanently in the spring of 22, looking for cash in the bond business.', 
	'Departure2': ' My first call to separation was actually when my cousin Daisy asked me to join her and her husband for dinner. At first I was a little disgusted with the whole rich life of her and Tom, but I got used to it.',
	'Departure3': ' Tbh I got a lowkey supernatural aid when Gatsby sent me an invitation to one of his massive parties. Turns out that he doesnt send those to many people, not that it matters, but it still felt special to me.'
} # departure quotes

initiation = {
	'Initiation1': ' My initiation started when I started to fall for the lying temptress that is Ms. Jordan Baker. I couldnt trust her much at all, but she was the only one capable of helping me through the mess that Gatsby was.',
	'Initiation2': ' I had to help Gatsby atone to me his history of bootlegging and other nefarious activities he had done when he was slightly more oblivious. Turns out his bootlegging buddy also fixed the world series. Whoda thunk it?',
	'Initiation3': ' You know I sort of had an ultimate boon kind of situation, where I was forced to help make some final decisions between Gatsby, Tom, and poor ole Daisy. That was not a fun evening. Blisteringly hot too.'
} #Initiation quotes

ret = {
	'Return1': ' At first I didnt even think about going back to the midwest, but Gatsby’s death didnt leave me with much, and I dont mean economically. But considering the sort of money filled hellscape that New York was, I had to go.',
	'Return2': ' I returned to the midwest after New York taught me that money, of the new world, or the old, is something I know far too much about, and something I dont care to drown in for the rest of my days. '
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
stream.filter(track=['nickiboi_c']) #filter the stream for tweets with "nickiboi_c" in them

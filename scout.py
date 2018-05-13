# -*- coding: utf-8 -*-

import tweepy, random



CONSUMER_KEY = 'FhNwnaK7sXrs1lILjfUTmwWj5'
CONSUMER_SECRET = 'WMVfFAVbHcGhoZ0bKqW5YNUgVi8p3dJP6fl5PFjvGEHJ4ZBhhK'
ACCESS_KEY = '995525450263916545-vFJYsvt5z8jWJ8QWtU4N52JxADwdpJP'
ACCESS_SECRET = 'O4dD11JeqGal8mloIu6t94JxJFKGHs7qugJZRkKK224aE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



departure = {
	'Departure1': ' The call to adventure for Jem and I started when the judge asked Atticus to handle Tom Robinsons case. At the time me and Jem didnt understand what the big deal was, the call wasnt something youd refuse you know?', 
	'Departure2': ' Me and Jem didnt realize why the new case was such a big deal until we crossed the first threshold. At the time I still didnt quite understand why, but when Mrs Dubose was very ...voacl... with Atticuss choice to defend a black man, it made more sense.''
} # departure quotes

initiation = {
	'Initiation1': ' Our meeting with a goddess, well more of a temptress but details are a bother, was with who I think was of all people Boo Radley. He gave me and Jem trinkets of all types, and even a blanket when Maudies house was coming down!',
	'Initiation2': ' I had an atonement with Atticus after the whole mob fiasco took place. Atticus explained to us that I had accidentally made Cunningham see things through another pair of shoes. Something about it taking an eight-year-old child to bring em to their senses.'
} #Initiation quotes

ret = {
	'Return1': ' Whenever me and Jem tried to check up on Atticus, he would always send us back home. But just when that mob showed up to try and hurt Atticus, Jem and I refused the call. We were gonna stick with Atticus all the way through.',
	'Return2': ' Once the Tom Robinsons trial ended, I found my little self the master of two worlds. The first being my immature, childlike side, obsessed with my pants and Boo Radleys gifts, but also my mature side, and seeing people for who they truly are.'
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
stream.filter(track=['missjeanlouisef']) #filter the stream for tweets with "missjeanlouisef" in them

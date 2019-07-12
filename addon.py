from xbmcswift2 import Plugin, xbmcgui
from resources.lib import radiodiariespodcast

plugin = Plugin()

URL = "http://feed.radiodiaries.org/radio-diaries"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://f.prxu.org/radiodiaries/images/d6e12225-df87-487b-96c5-f41c2ef4a7a2/radio_diaries_300.png"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://f.prxu.org/radiodiaries/images/d6e12225-df87-487b-96c5-f41c2ef4a7a2/radio_diaries_300.png"},
   {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('where_to_start'),
            'thumbnail': "https://f.prxu.org/radiodiaries/images/d6e12225-df87-487b-96c5-f41c2ef4a7a2/radio_diaries_300.png"},

    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = radiodiariespodcast.get_soup(URL)
    
    playable_podcast = radiodiariespodcast.get_playable_podcast(soup)
    
    items = radiodiariespodcast.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = radiodiariespodcast.get_soup(URL)
    
    playable_podcast1 = radiodiariespodcast.get_playable_podcast1(soup)
    
    items = radiodiariespodcast.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/where_to_start/')
def where_to_start():
    """
    contains playable podcasts listed as just-in
    """
    
    items = [{
		    'label': 'Busmans Holiday',
        	    'thumbnail': 'https://f.prxu.org/radiodiaries/7e71e729-57cd-43b1-b980-a8696807ece8/images/3fa52313-14d9-4dde-9e43-2ba925f64faf/Cimillo-portrait-on-bus-230x300.jpg',
        	    'path': 'https://dts.podtrac.com/redirect.mp3/media.blubrry.com/radiodiaries/dovetail.prxu.org/radiodiaries/7e71e729-57cd-43b1-b980-a8696807ece8/23-Busmans-Holiday.mp3',
        	    'info': 'The story of William Cimillo, a New York City bus driver who snapped one day in 1947, left his regular route in the Bronx, and drove his municipal bus down to Florida',
        	    'is_playable': True},
           	    {'label': 'Majds Diary: Two Years in the Life of a Saudi Girl',
	            'thumbnail': 'https://f.prxu.org/radiodiaries/8dfca65c-87cb-4663-92a4-5568b44c4ffe/images/8e891bea-a899-4a53-9979-1e50bd58950a/Majd-Microphone-2_square.jpg',
        	    'path': 'https://dts.podtrac.com/redirect.mp3/media.blubrry.com/radiodiaries/dovetail.prxu.org/radiodiaries/8dfca65c-87cb-4663-92a4-5568b44c4ffe/Majd-Podcast_Casper.mp3',
        	    'info': 'Majd Abdulghani is a teenager living in Saudi Arabia, one of the most restrictive countries for women in the world. She wants to be a scientist. Her family wants to arrange her marriage. From the age of 19 to 21, Majd has been chronicling her life with a microphone, taking us inside a society where the voices of women are rarely heard. She records herself practicing karate, conducting experiments in a genetics lab, and fending off pressure to accept an arranged marriage. In her audio diary, Majd documents everything from arguments with her brother about how much she should cover herself in front of men, to late night thoughts about loneliness, arranged marriages, and the possibility of true love',
        	    'is_playable': True},
		    {'label': 'From Flint To Rio',
        	    'thumbnail': 'https://f.prxu.org/radiodiaries/8b0b76c0-3f34-488d-bb54-8e7bfab504b9/images/883ac54c-5c49-4969-adfd-11556e7152bf/Claressa_1_T.jpg',
        	    'path': 'https://dts.podtrac.com/redirect.mp3/media.blubrry.com/radiodiaries/dovetail.prxu.org/radiodiaries/8b0b76c0-3f34-488d-bb54-8e7bfab504b9/From-Flint-to-Rio.mp3',
        	    'info': 'Claressa Shields was a 17-year-old from Flint, Michigan, with a dream -- to become the first American woman to win Olympic gold in boxing. And she did just that',
        	    'is_playable': True},
]

    return items



if __name__ == '__main__':
    plugin.run()

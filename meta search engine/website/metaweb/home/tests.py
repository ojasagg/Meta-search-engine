from django.test import TestCase

# Create your tests here.

from bs4 import BeautifulSoup
from bing import Bing
from google import Google
import unittest

BING_SEARCH_RESULT = [
    {'link': 'http://en.wikipedia.org/wiki/Hello_world_program', 'link_text': '" Hello, world !" program - Wikipedia, the free encyclopedia', 'additional_links': {'Purpose': 'http://en.wikipedia.org/wiki/Hello_world_program#Purpose', 'History': 'http://en.wikipedia.org/wiki/Hello_world_program#History', 'Variations': 'http://en.wikipedia.org/wiki/Hello_world_program#Variations'}, 'link_info': 'A " Hello, world !" program is a computer program that outputs " Hello, World !" (or some variant thereof) on a display device. Because it is typically one of the ...'},
    {'link': 'https://www.hello-world.com/', 'link_text': 'Total immersion, Serious fun! with Hello-World !', 'additional_links': {}, 'link_info': 'Main index for hello-world : links to login and all of the languages'}, 
    {'link': 'http://www.helloworld.com/', 'link_text': 'HelloWorld Inc - Official Site', 'additional_links': {}, 'link_info': 'Wayman joins senior leadership team. Meet Chris, Chief Client Officer, and learn about this new role at HelloWorld .'}, 
    {'link': 'http://www.helloworldchennai.com/', 'link_text': 'Hello World', 'additional_links': {}, 'link_info': 'A leading chain of mobile stores in Chennai , Hello World , founded in 1999, caters to all cellular needs of todays informed buyer.'}, 
    {'link': 'http://en.wikipedia.org/wiki/List_of_Hello_world_program_examples', 'link_text': 'List of Hello world program examples - Wikipedia, the free ...', 'additional_links': {}, 'link_info': 'The Hello world program is a simple computer program that prints (or displays) the string " Hello, world !" or some variant thereof. It is typically one of ...'}, 
    {'link': 'http://www.youtube.com/watch?v=al2DFQEZl4M', 'link_text': 'Lady Antebellum - Hello World - YouTube', 'additional_links': {}, 'link_info': '05-11-2010 · Music video by Lady Antebellum performing Hello World on You Tube.'}, 
    {'link': 'http://www.gnu.org/fun/jokes/helloworld.html', 'link_text': 'Hello World ! - GNU Project - Free Software Foundation (FSF)', 'additional_links': {}, 'link_info': 'Hello World ! How the way people code “ Hello World ” varies depending on their age and job: High School/Jr. High 10 PRINT " HELLO WORLD " 20 END'}, 
    {'link': 'http://msdn.microsoft.com/en-us/library/ms765388(v=vs.85).aspx', 'link_text': 'Hello, World ! (XSLT)', 'additional_links': {}, 'link_info': 'The following example shows a simple but complete XML document transformed by an XSLT style sheet. The source XML document, hello .xml, contains a " Hello, World !"'}, 
    {'link': 'http://asp.net-tutorials.com/basics/hello-world/', 'link_text': 'Hello, world ! - The complete ASP.NET Tutorial', 'additional_links': {}, 'link_info': 'In almost every programming tutorial you will find the classic " Hello, world !" example, and who am I to break such a fine tradition? Let me show you how you can say ...'}, 
    {'link': 'http://www.helloworldchennai.com/branches.asp', 'link_text': 'Hello World', 'additional_links': {}, 'link_info': 'HELLO WORLD . Basement Shop #2, Gokul Arcade, #2, Sardar Patel Road, Adyar, Chennai - 20 Ph: 044 - 24425573 / 42115215'}
    ]

BING_NEWS_RESULT = [
    {'source': 'ABP NEWS', 'link': 'http://www.abplive.in/incoming/2014/12/18/article457398.ece/Stopzzzzz', 'time': '18-12-2014', 'additional_links': {}, 'link_info': 'Hello world I am a test page and I am being worked upon by an ace developer A.K.S Hello world I am a test page and I am being worked upon by an ace developer A.K.S Hello world I am a test page and I am being worked upon by an ace developer A.K.S …', 'link_text': 'This is the new article'}, 
    {'source': 'The Hindu', 'link': 'http://www.thehindu.com/todays-paper/tp-features/tp-youngworld/say-hello-to-chikkanna-and-thimmakka/article6746498.ece', 'time': '14 hours ago', 'additional_links': {}, 'link_info': 'Fifty years ago, Chikkanna and Thimmakka decided to plant trees. Today, we have a long tree-lined stretch of road. D o ask your parents to take you to the road between Kudur and Hulikal in Karnataka. Get down and …', 'link_text': 'Say HELLO to… Chikkanna and Thimmakka'}, 
    {'source': 'India Today', 'link': 'http://indiatoday.intoday.in/story/hello-airtel-charging-extra-for-internet-calls-is-silly-business/1/408983.html', 'time': '26-12-2014', 'additional_links': {}, 'link_info': 'Just like almost all other telecom companies in the world , Airtel sees the internet as a business opportunity but also loathes it for providing people choices in the communication business, choices that allow people to …', 'link_text': 'Hello Airtel, charging extra for internet calls is silly business'}, 
    {'source': 'Game Dynamo', 'link': 'http://www.gamedynamo.com/company/info/719/hello_games', 'time': '1 day ago', 'additional_links': {}, 'link_info': 'Hello Games was founded in 2009 by a band of four friends who ... They decided to set forth on a brave journey of discovery and adventure to bring some new, funky-colored pixels to the world . They have loved every minute of helping to create great games ...', 'link_text': 'Hello Games'}, 
    {'source': 'The Hindu', 'link': 'http://www.thehindu.com/features/magazine/travel-to-hawaii/article6730641.ece', 'time': '29-12-2014', 'additional_links': {}, 'link_info': 'During the ‘big wave’ season from November through March, huge glassy waves attract surfers from all over the world . The North Shore hosts the world ’s elite surfing competitions during this time. Kawaika tells me that I am welcome to hire a board and ...', 'link_text': 'Hello , Hawaii'}, 
    {'source': 'NDTV', 'link': 'http://www.ndtv.com/article/offbeat/look-who-just-turned-114-say-hello-to-the-world-s-oldest-crocodile-635841?ndtv_prevstory', 'time': '17-12-2014', 'additional_links': {}, 'link_info': 'Johannesburg: Henry, the world \'s oldest crocodile, turned 114 Tuesday and will be the star at a birthday bash with balloons and cake for all well-wishers. Henry\'s party is being held at "Crocworld" in the South African city of Scottsburgh where employees ...', 'link_text': "Look Who Just Turned 114! Say Hello to the World 's Oldest Crocodile"}, 
    {'source': 'Yahoo Finance India', 'link': 'https://in.finance.yahoo.com/news/10-most-important-things-world-084400042.html', 'time': '29-12-2014', 'additional_links': {}, 'link_info': "Hello ! Here's what you need to know for Monday ... More From Business Insider The 10 Most Important Things In The World Right Now The 10 Most Important Things In The World Right Now 10 NFL Games Have Playoff …", 'link_text': 'The 10 Most Important Things In The World Right Now'}, 
    {'source': 'Crazy Engineers', 'link': 'http://www.crazyengineers.com/threads/hello-ceans.77650/', 'time': '08-12-2014', 'additional_links': {}, 'link_info': 'dia-project-report-contest.77548/#post-332822 I really liked the ideas of this website and congratulate the initiators for such a mind-blowing effort to make engineers crazy enough to do things that matter to the world . Please go through my project from ...', 'link_text': 'HELLO CEans'}, 
    {'source': 'India Today', 'link': 'http://indiatoday.intoday.in/story/2014-redux-best-gadgets-phones-apps-and-more/1/410449.html', 'time': '29-12-2014', 'additional_links': {}, 'link_info': 'This is it, folks. The year 2014 is over and day after tomorrow we will be saying hello to 2015. So how was the year 2014 in the world of technology? Incremental is one word that summarizes the year. We got some …', 'link_text': '2014 redux: 10 best gadgets, top smartphones, apps, and more'}, 
    {'source': 'Andhra News', 'link': 'http://www.andhranews.net/Intl/Web/23-66.asp', 'time': '20-12-2014', 'additional_links': {}, 'link_info': 'The "Flyer App" is here to solve exactly this problem: Suitable information from all over the world , on a vast range of topics, precisely when you need it, all in one compact app. Quickly and easily search for something or browse in clearly arranged ...', 'link_text': 'New Search App: Goodbye Paper Flyers - hello Flyer App'}
    ]

GOOGLE_SEARCH_RESULT = [
    {'additional_links': {'99 Bottles of Beer': 'http://en.wikipedia.org/wiki/99_Bottles_of_Beer&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CBoQ0gIoATAA&usg=AFQjCNHZPaTfYq-2nk39QTs4tGzCysQDMQ', 'List of Hello world program': 'http://en.wikipedia.org/wiki/List_of_Hello_world_program_examples&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CBkQ0gIoADAA&usg=AFQjCNETvyLmNFYslrfVpeXNVqjsiQImuQ', 'Just another Perl hacker': 'http://en.wikipedia.org/wiki/Just_another_Perl_hacker&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CBsQ0gIoAjAA&usg=AFQjCNHFa8c-nbLhQiMWHylFRC8P0Cmngg'}, 'link': 'http://en.wikipedia.org/wiki/%2522Hello,_world!%2522_program&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CBQQFjAA&usg=AFQjCNEDKRIU3IRETmNGWNFItE2V5Cs4Wg', 'link_text': '" Hello , world !" program - Wikipedia, the free encyclopedia', 'link_info': 'A " Hello , World !" program is a computer program that outputs " Hello , World !" (or some variant thereof) on a display device. Because it is typically one of the ...'}, 
    {'additional_links': {'Travel deals': 'http://www.helloworld.com.au/deals/dealshome/&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CCQQ0gIoATAB&usg=AFQjCNGbvJ0CBxWE_xiGzTZZ15aC_Bs7Mw', 'Cruises': 'http://cruise.helloworld.com.au/&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CCUQ0gIoAjAB&usg=AFQjCNGnJy4PLaLbcsswUeUvz787zWmwhg', 'Agent Finder': 'http://agents.helloworld.com.au/&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CCYQ0gIoAzAB&usg=AFQjCNECITukSSykPh7gP1rMITD-9I_C9w', 'Cheap Flights': 'http://www.helloworld.com.au/flights/&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CCMQ0gIoADAB&usg=AFQjCNHNVkEQ_OLG17iczsNEo2GLFppVjw'}, 'link': 'http://www.helloworld.com.au/&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CB0QFjAB&usg=AFQjCNEG87ayXffDjmKhEEC9IKoMCWhTMw', 'link_text': 'helloworld – Deals on Accommodation, Flights, Cruises and More', 'link_info': "Discover the best deals on flights, hotels, cars, cruises in Australia at helloworld – we're always here for you – in stores, online and on the phone!"}, 
    {'additional_links': {}, 'link': 'http://www.helloworld.com/&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CCgQFjAC&usg=AFQjCNEM2X_hQjMDo_0BQNI0BUuWk5KTXg', 'link_text': 'Digital, Social, Mobile Marketing | HelloWorld', 'link_info': 'Rich engagement platform empowers marketers to motivate and measure consumer behavior through promotions, loyalty solutions and mobile messaging.'}, 
    {'additional_links': {}, 'link': 'http://www.hello-world.com/&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CC4QFjAD&usg=AFQjCNE0XtCiJWQvDxg4ZzeeeDhjvv4y4g', 'link_text': 'Total immersion, Serious fun! with Hello - World !', 'link_info': 'Main index for hello - world : links to login and all of the languages.'}, 
    {'additional_links': {}, 'link': 'http://www.roesler-ac.de/wolfram/hello.htm&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CDQQFjAE&usg=AFQjCNGAd8wnUN_j_8tryNqEzSZSwGJCHQ', 'link_text': 'The Hello World Collection - www.roesler-ac.de!', 'link_info': 'The Collection without Frames.'}, 
    {'additional_links': {}, 'link': 'https://guides.github.com/activities/hello-world/&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CDoQFjAF&usg=AFQjCNHbqJxhpcu0TNU3_rsPulqw1vP7qA', 'link_text': 'Hello World · GitHub Guides', 'link_info': "The Hello World project is a time-honored tradition in computer programming. It is a simple exercise that gets you started when learning something new. Let's get ..."}, 
    {'additional_links': {}, 'link': 'http://groups.engin.umd.umich.edu/CIS/course.des/cis400/c/hworld.html&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CD8QFjAG&usg=AFQjCNGm6mpXL-jiDK6ZQ5cT4yghl_Zozw', 'link_text': 'The C Programming Language: Hello world ! Example Program', 'link_info': 'The C Programming Language. Hello world ! Example Program. /* Hello World program */ #include<stdio.h> main() { printf(" Hello World ");. } [Back] [Home]'}, 
    {'additional_links': {}, 'link': 'https://www.gnu.org/fun/jokes/helloworld.html&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CEUQFjAH&usg=AFQjCNGjXwbD5f2V5uihJNtii70HC6mzSA', 'link_text': 'Hello World ! - GNU Project - Free Software Foundation (FSF)', 'link_info': "Hello World ! How the way people code “ Hello World ” varies depending on their age and job: ... program Hello(input, output) begin writeln(' Hello World ') end."}, 
    {'additional_links': {}, 'link': 'https://www.facebook.com/helloworldau&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CEoQFjAI&usg=AFQjCNEX2lPt3dLaq6jUfpU714QwE_BRpQ', 'link_text': 'helloworld - Travel Agency | Facebook', 'link_info': 'helloworld . 107003 likes · 8742 talking about this. Welcome to the official Facebook page for helloworld . Ask us a question or "Like" us for travel...'}, 
    {'additional_links': {}, 'link': 'http://www.helloworldlimited.com.au/&sa=U&ei=pA6kVIHiMtD28QWSr4DoBQ&ved=0CFAQFjAJ&usg=AFQjCNE9DMTnoxnwCh3FgcwqAPi1nPUyUg', 'link_text': 'Helloworld Limited > Home', 'link_info': 'Helloworld Limited. Home. About Us; Brands; Investor Centre; Opportunities; Contact us · Share Price. Copyright © 2013 Helloworld Limited. Login.'}
    ]

GOOGLE_NEWS_RESULT = [
    {'link': 'http://www.directlyrics.com/kid-ink-hello-world-music-video-news.html&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CBMQqQIoADAB&usg=AFQjCNHZCZBM9HbRDjZPMcDwSpHL08oaXA', 'link_text': "Kid Ink - ' Hello World ' [Music Video]", 'additional_links': {'Kid Ink \x96 \x93 Hello World \x94 (Video)': ('/url?q=http://allhiphop.com/2015/01/01/kid-ink-hello-world-video/&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CBYQ-AsoATAB&usg=AFQjCNHqprZiqId_X_J-NLyYRHorUYFv0Q', 'AllHipHop'), "Kid Ink Shares Globe-Spanning ' Hello World ' Music Video [WATCH]": ('/url?q=http://www.musictimes.com/articles/22570/20141231/kid-ink-globe-spanning-hello-world-music-video.htm&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CBUQ-AsoADAB&usg=AFQjCNEM1EcBBGYTmnm8SAmClTYZL0x70g', 'Music Times')}, 'link_info': "In his latest visual release ' Hello World ', the Los Angeles rapper recaps his adventures all throughout the year into a three minute clip directed ...", 'time': '1 day ago', 'source': 'Music and Lyrics'}, 
    {'link': 'http://www.staplesworld.com/news/2015-01-01/Life_Currents/Hello_World.html&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CBkQqQIoADAC&usg=AFQjCNHNGs71QQ9onauWedVdbgULEK_v9Q', 'link_text': 'Hello World', 'additional_links': {}, 'link_info': 'BIRTHS REPORTED AT LAKEWOOD HEALTH SYSTEM HOSPITAL INCLUDED: Born to Bryan and Kripa Reese of Staples, a baby girl, ...', 'time': '2 days ago', 'source': 'Staples World (subscription)'}, 
    {'link': 'https://medium.com/backchannel/hello-world-cf8dd6fcb7f7&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CBsQqQIoADAD&usg=AFQjCNEXjijyJV3AHgIEagz0wyyOF0TBvQ', 'link_text': 'Hello , World !', 'additional_links': {}, 'link_info': 'You may even be able to work out, more or less, what this little \x93Program\x94 does: it writes to the console of some system the line \x93 Hello , world !\x94 A geek hunched ...', 'time': '19 Dec 2014', 'source': 'Backchannel'}, 
    {'link': 'http://www.osnews.com/story/28131/The_infamous_Windows_Hello_World_program&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CB4QqQIoADAE&usg=AFQjCNFhKJJwlNS2dTP2soFiX1Gc0iatKw', 'link_text': 'The infamous Windows " Hello World " program', 'additional_links': {}, 'link_info': 'I learned Windows programming from documents included with the Windows 1.0 beta and release Software Development Kits. These included ...', 'time': '9 Dec 2014', 'source': 'OS News'}, 
    {'link': 'http://www.fool.com.au/2014/12/12/helloworld-ltd-surges-on-positive-new-should-you-bet-on-it-for-2015/&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CCAQqQIoADAF&usg=AFQjCNHu2J_8HgVDvsQTsG5QLaIZSCxX7Q', 'link_text': 'Helloworld Ltd surges on positive new: Should you bet on it for 2015?', 'additional_links': {}, 'link_info': 'Helloworld Ltd (ASX: HLO) shares have skyrocketed today after the company announced that one of its subsidiaries, QBT Limited, had been ...', 'time': '11 Dec 2014', 'source': 'Motley Fool Australia'}, 
    {'link': 'http://mumbrella.com.au/travel-firm-helloworld-appoints-marketer-jane-mckellar-new-board-member-268338&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CCQQqQIoADAG&usg=AFQjCNE7SvfNPq3rC_j3OSFydFJjYRkLJg', 'link_text': 'Travel firm Helloworld appoints marketer Jane McKellar as new ...', 'additional_links': {}, 'link_info': 'Helloworld Limited (ASX:HLO) is pleased to announce the appointment of Ms Jane McKellar as an independent Non-Executive Director ...', 'time': '16 Dec 2014', 'source': 'MuMbrella'}, 
    {'link': 'http://www.fool.com.au/2014/12/11/cover-more-group-ltd-and-helloworld-ltd-announce-positive-news-should-you-buy/&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CCgQqQIoADAH&usg=AFQjCNGSA-g_H9sPhTQA6yP_FCFvKVp1Cw', 'link_text': 'Cover-More Group Ltd and Helloworld Ltd announce positive news ...', 'additional_links': {'Cover-More beats competition for Helloworld preferred status': ('/url?q=http://www.travelweekly.com.au/news/cover-more-beats-competition-for-helloworld-prefer&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CCoQ-AsoADAH&usg=AFQjCNHu3l7KaLX-nsVbNn5zq_4HMJXksw', 'Travel Weekly')}, 'link_info': 'Cover-More Group Ltd (ASX: CVO) and Helloworld Ltd (ASX: HLO) have reached an agreement which will see Cover-More become the ...', 'time': '10 Dec 2014', 'source': 'Motley Fool Australia'}, 
    {'link': 'http://www.nbcnews.com/news/world/hello-2015-new-year-rung-around-world-n277466&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CC0QqQIoADAI&usg=AFQjCNF1_XGw55g3JMJKF4wPPeFxNbMpQw', 'link_text': 'Hello , 2015! A New Year Is Rung In Around the World', 'additional_links': {"New Year's Eve: Watch the world ring in 2015": ('/url?q=http://www.haaretz.com/news/world/1.634707&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CDAQ-AsoATAI&usg=AFQjCNHqeKXiTua-zmUVxl3GZ7I7eE7ugw', 'Haaretz'), 'World rings in New Year': ('/url?q=http://www.reuters.com/video/2014/12/31/world-rings-in-new-year%3FvideoId%3D357271665&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CC8Q-AsoADAI&usg=AFQjCNHAfLrPCH4PQFYLnDgeodfZ8V2MlA', 'Reuters'), 'Hello , 2015! See New Year Celebrations Around the World': ('/url?q=http://www.bayoubuzz.com/top-stories/item/808469-hello-2015-see-new-year-celebrations-around-the-world&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CDEQ-AsoAjAI&usg=AFQjCNEYiPZtAz0xKqrGruII02BXU59z4A', 'Bayoubuzz')}, 'link_info': 'MUNICH, Germany \x97 Neo-Nazis are keeping their black combat boots and bomber jackets in the closet as they try to force their way into mainstream German ...', 'time': '1 day ago', 'source': 'NBCNews.com'}, 
    {'link': 'http://www.dailymercury.com.au/news/helloworlds-alyce-best-in-australia/2486084/&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CDQQqQIoADAJ&usg=AFQjCNFDbOrVHdyoebQJInpYl2I_Z9djTQ', 'link_text': "Helloworld's Alyce best in Australia", 'additional_links': {}, 'link_info': 'Head of helloworld -branded network Julie Primmer, Team Spirit Award winner Alyce Tweddle and event host Stevie Jacobs from the Today ...', 'time': '15 Dec 2014', 'source': 'Mackay Daily Mercury'}, 
    {'link': 'http://www.mediapost.com/publications/article/240253/helloworld-mellow-mushroom-stella-artois-launch.html&sa=U&ei=3QGnVKerC9CouQTY1oC4Dg&ved=0CDcQqQIoADAK&usg=AFQjCNFYKt6wpBUqJjymlKdTIj2cOXXTCA', 'link_text': 'HelloWorld , Mellow Mushroom, Stella Artois Launch Holiday ...', 'additional_links': {}, 'link_info': 'Mellow Mushroom, digital agency HelloWorld and beer brand Stella Artois are sponsoring a sweepstakes where customers can follow Mellow ...', 'time': '16 Dec 2014', 'source': 'MediaPost Communications'}
    ]

class BingTest(unittest.TestCase):

    def test_bing_scrape_search_result(self):
        with open('ipbing') as fp:
            bing_search_result = Bing.scrape_search_result(BeautifulSoup(fp))
            self.assertEqual(BING_SEARCH_RESULT, bing_search_result)

    def test_bing_scrape_news_result(self):
        with open('ipbingnews') as fp:
            bing_news_result = Bing.scrape_news_result(BeautifulSoup(fp))
            self.assertEqual(BING_NEWS_RESULT, bing_news_result)

    def test_google_scrape_search_result(self):
        with open('ipgoogle') as fp:
            google_search_result = Google.scrape_search_result(BeautifulSoup(fp))
            self.assertEqual(GOOGLE_SEARCH_RESULT, google_search_result)

    def test_google_scrape_news_result(self):
        with open('ipgooglenews') as fp:
            google_news_result = Google.scrape_news_result(BeautifulSoup(fp))
            self.assertEqual(GOOGLE_NEWS_RESULT, google_news_result)

if __name__ == '__main__':
    unittest.main()
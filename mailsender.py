import sendgrid
import os
import grab_story 

SEND_GRID_API_KEY = os.environ.get('SEND_GRID_API_KEY', 'INPUT_SEND_GRID_API_KEY_HERE')
SEND_GRID_USER = os.environ.get('SEND_GRID_USER', 'INPUT_SEND_GRID_USER_HERE')

#Some categoryID's: 1007(science), 1002(home page stories), 1090(story of the day), 103537970(shots: Health News) 
#Other Regional ID's: 1126(Africa), 1125(Asia), 1127(Latin America), 1124(Europe) 

sender = ''
recipient = ''
categoryID = ''

#This class parses the json returned from NPR
news_json = grab_story.AssembleStory(categoryID).parse_npr_json()

#Assembles the news stories from Json into HTML for the e-mail
HTML_text = ""
for story in news_json:
	HTML_text+='<p><b>'+ story['title']+'</b><br>'+'Date: '+story['date']+'<br>'+ 'Teaser: '+story['description']+'<br>'+'Full Story: '+story['url']+'</p>'
HTML_text= '<html><body>'+HTML_text+'</body></html>'

#Uses SendGrid API to send the e-mail 
sg = sendgrid.SendGridClient(SEND_GRID_USER, SEND_GRID_API_KEY)
message = sendgrid.Mail()
message.add_to(recipient)
message.set_from(sender)
message.set_subject("News updates from: NPR")
message.set_html(HTML_text)

status = sg.send(message)
print status

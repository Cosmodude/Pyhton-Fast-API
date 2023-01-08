### Sending emails with the Postmark Python library
from dotenv import load_dotenv
load_dotenv()
import os
from postmarker.core import PostmarkClient


postmark = PostmarkClient(server_token= os.getenv('Posmarker_Server_Token'))
postmark.emails.send(
    From='contact@crypto-goose.com',
    To='contact@crypto-goose.com',
    Subject='Postmark test',
    HtmlBody='Hi man!'
)

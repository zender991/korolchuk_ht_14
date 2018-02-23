import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(new_stories_count, spent_time):
    # me == my email address
    # you == recipient's email address
    me = "zender991@gmail.com"
    you = "yanutaoleg@gmail.com"

    LOGIN = "zender991@gmail.com"
    PASSWORD = "Punkrock"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hometask - Korolchuk"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
    html = """\
    <html>
     <head></head>
     <body>
       <p>Hi Oleg!<br>
       <p>Homework 14 by Oleksandr Korolchuk</p>
       <p>Results</p>
       <table>
            <tr>
                <th>Category name</th>
                <th>Gathered stories</th>
            </tr>
            <tr>
                <td>Askstories</td>
                <td>""" + str(new_stories_count['askstories']) + """</td>
            </tr>
            <tr>
                <td>Jobstories</td>
                <td>""" + str(new_stories_count['jobstories']) + """</td>
            </tr>
            <tr>
                <td>Showstories</td>
                <td>""" + str(new_stories_count['showstories']) + """</td>
            </tr>
            <tr>
                <td>Newstories</td>
                <td>""" + str(new_stories_count['newstories']) + """</td>
            </tr>
       </table>
       
       <h4> Time spent - """ + str(spent_time) + """

     </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    # re-identify ourselves as an encrypted connection
    s.ehlo()
    s.login(LOGIN, PASSWORD)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()

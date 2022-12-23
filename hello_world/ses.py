from datetime import datetime
import calendar
import boto3
from pandas import *
"""
Function: Can do something. You can get some job done
"""
client = boto3.client('ses')

# How to write a python function

def add(a, b):

    c = a + b

    print(c)
    name = "John"
    school = 'Izaan School'
    print(school)

    # Fency way to print
    print("My Name: {}, {}".format(name, school))

    a = 3
    print(type(a))

    print("name varaible time: {}, school variable type: {}".format(type(name), type(school)))


def students_info():
    students = [ "Foysal" , "Shamim", "Mohiuddin", "Masud", 22]

    print(students)
    print(type(students))

    return students


def send_greetings():
    email_list = get_email_list()
    current_day = get_current_day()

    # if current day is Friday send student a greetings
    # current_day == 'Friday'  - True or False
    # Thursday == Friday --> False
    # Wed == Fri --> False Tue == Fri --> False Mon == Fri --> False

    if current_day == 'Thursday':
        send_email_by_ses()
    else:
        print("Sorry cant send email, today is " + current_day)


def get_email_list():
    """
    1. List of students - Email
    2. Send students good thoughts in every Friday at 5:30 PM

    :return:
    """
    students_email_list = [
        'mr2chowd@uwaterloo.ca','bahjatkhan2002@gmail.com',
        'Rahmanmdm16@gmail.com', 'taha20jibril@gmail.com',
        'adeelmahmood125@gmail.com', 'Leonsubhan@outlook.com',
        'sreza30th@gmail.com'
    ]
    return students_email_list

def get_current_day():
    # get current datetime
    dt = datetime.now()
    print('Datetime is:', dt)

    # # weekday (Monday =0 Sunday=6)
    # print('Weekday Number:', dt.weekday())
    #
    # # isoweekday(Monday =1 Sunday=6)
    # print('ISO Weekday Number:', dt.isoweekday())
    #
    # # get weekday name
    # print('Weekday Name:', dt.strftime('%A'))

    # get day name
    current_day = calendar.day_name[dt.weekday()]
    print('Weekday name is:', current_day)
    return current_day


def send_email_by_ses():
    # create a connection object to use aws services.
    #
    students_email_list = get_email_list()
    # List - Or a data structure
    # 1. How to create the data structure
    # 2. How to insert data into a list?
    # 3. How to update data in a list?
    # 4. How to get the data from a list?
    # 5. How to delete a data from a list?
    # Write original, good code to send folks email

    # for temp_contaianer in target/source
    #    #consumeer
    #    print(temp_contaianer)
    """
    to = info@izaan.io
    from = anyone
    
    """

    for temp_container in students_email_list:
        user_name = temp_container.split('@')[0] # [mr2chowd, uwaterloo.ca]
        message = 'Hi {}, Wishing you a very good day'.format(user_name)
        ses_send(temp_container, message)


def ses_send(email, message):
    response = client.send_email(
        Source='info@izaan.io',
        Destination={
            'ToAddresses': [
                email,
            ]
        },
        Message={
            'Subject': {
                'Data': 'Greetings from Izaan School!!!'
            },
            'Body': {
                'Text': {
                    'Data': message
                },
            }
        },
        ReplyToAddresses=[
            'info@izaan.io',
        ]
    )


def create_template():
    response = client.create_template(
        Template={
            'TemplateName': 'B2301-DevOpsMarketing-Template3',
            'SubjectPart': 'Hello!!! Come check it out!!!',
           # 'HtmlPart': """<!DOCTYPE html><html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"><head><title></title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]--><!--[if !mso]><!--><link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Shrikhand" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Droid+Serif" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Cormorant+Garamond" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css"><!--<![endif]--><style>* {box-sizing: border-box;}body {margin: 0;padding: 0;}a[x-apple-data-detectors] {color: inherit !important;text-decoration: inherit !important;}#MessageViewBody a {color: inherit;text-decoration: none;}p {line-height: inherit}.desktop_hide,.desktop_hide table {mso-hide: all;display: none;max-height: 0px;overflow: hidden;}@media (max-width:670px) {.desktop_hide table.icons-inner,.social_block.desktop_hide .social-table {display: inline-block !important;}.icons-inner {text-align: center;}.icons-inner td {margin: 0 auto;}.image_block img.big,.row-content {width: 100% !important;}.mobile_hide {display: none;}.stack .column {width: 100%;display: block;}.mobile_hide {min-height: 0;max-height: 0;max-width: 0;overflow: hidden;font-size: 0px;}.desktop_hide,.desktop_hide table {display: table !important;max-height: none !important;}.reverse {display: table;width: 100%;}.reverse .column.first {display: table-footer-group !important;}.reverse .column.last {display: table-header-group !important;}.row-13 td.column.first .border {padding-left: 20px;padding-right: 20px;border-top: 0;border-right: 0px;border-bottom: 0;border-left: 0;}.row-13 td.column.last .border {padding-left: 0;padding-right: 0;border-top: 0;border-right: 0px;border-bottom: 0;border-left: 0;}}</style></head><body style="margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none; background-color: #161635;"><table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #161635;"><tbody><tr><td><table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-repeat: repeat; background-position: center top; background-color: #161635; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/Fondo_Cabecera_larga.jpg');"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-right: 20px; padding-left: 20px; vertical-align: top; padding-top: 30px; padding-bottom: 30px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="width:100%;padding-right:20px;padding-left:20px;"><div class="alignment" align="center" style="line-height:10px"><a href="https://www.example.com" target="_blank" style="outline:none" tabindex="-1"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/YourLogo.png" style="display: block; height: auto; border: 0; width: 175px; max-width: 100%;" width="175" alt="Your Logo Here" title="Your Logo Here"></a></div></td></tr></table><table class="divider_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="padding-top:10px;padding-right:10px;padding-bottom:20px;padding-left:10px;"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #EFB810;"><span>&#8202;</span></td></tr></table></div></td></tr></table><table class="image_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="width:100%;padding-right:0px;padding-left:0px;padding-top:40px;"><div class="alignment" align="center" style="line-height:10px"><img class="big" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/Copa_Champagne_02.png" style="display: block; height: auto; border: 0; width: 480px; max-width: 100%;" width="480" alt="Image of Drink Party" title="Image of Drink Party"></div></td></tr></table><table class="heading_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="width:100%;text-align:center;padding-top:30px;"><h1 style="margin: 0; color: #ffffff; font-size: 52px; font-family: 'Abril Fatface', Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: normal; letter-spacing: 1px; margin-top: 0; margin-bottom: 0;"><strong>NEW YEAR PARTY</strong></h1></td></tr></table><table class="divider_block block-6" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="padding-top:25px;padding-right:10px;padding-bottom:5px;padding-left:10px;"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="20%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 5px solid #EFB810;"><span>&#8202;</span></td></tr></table></div></td></tr></table><table class="heading_block block-7" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="width:100%;text-align:center;"><h1 style="margin: 0; color: #efb810; font-size: 98px; font-family: 'Abril Fatface', Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: 400; letter-spacing: 10px; margin-top: 0; margin-bottom: 0;"><strong>2023</strong></h1></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; border-top: 5px solid #EFB810; padding-left: 20px; padding-right: 20px; vertical-align: top; padding-top: 20px; padding-bottom: 25px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="text_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-top:20px;padding-bottom:10px;"><div style="font-family: sans-serif"><div class style="font-size: 14px; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2;"><p style="margin: 0; font-size: 14px; text-align: center; font-family: inherit; mso-line-height-alt: 16.8px;"><span style="font-size:24px;">LOREM IPSUM DOLOR SIT AMET, CONSECTETUR</span></p></div></div></td></tr></table><table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-right:15px;padding-bottom:10px;padding-left:15px;"><div style="font-family: Tahoma, Verdana, sans-serif"><div class style="font-size: 14px; font-family: 'Roboto', Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 21px; color: #5e5e6f; line-height: 1.5;"><p style="margin: 0; font-size: 14px; text-align: center; font-family: Roboto, Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 24px;"><span style="font-size:16px;">Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Maecenas faucibus mollis interdum. Nullam quis risus eget urna.</span></p></div></div></td></tr></table><table class="button_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="text-align:center;padding-top:20px;padding-bottom:10px;"><div class="alignment" align="center"><!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.example.com" style="height:54px;width:198px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#efb810"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#161635; font-family:Arial, sans-serif; font-size:22px"><![endif]--><a href="https://www.example.com" target="_blank" style="text-decoration:none;display:inline-block;color:#161635;background-color:#efb810;border-radius:0px;width:auto;border-top:0px solid #FFFFFF;font-weight:undefined;border-right:0px solid #FFFFFF;border-bottom:0px solid #FFFFFF;border-left:0px solid #FFFFFF;padding-top:5px;padding-bottom:5px;font-family:Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;font-size:22px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:30px;padding-right:30px;font-size:22px;display:inline-block;letter-spacing:1px;"><span style="word-break: break-word;" dir="ltr"><span style="line-height: 44px;" data-mce-style dir="ltr">YES, I'M GOING!</span></span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-3" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><div class="spacer_block" style="height:40px;line-height:40px;font-size:1px;">&#8202;</div></td></tr></tbody></table></td></tr></tbody></table><table class="row row-4" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="width:100%;padding-right:0px;padding-left:0px;"><div class="alignment" align="center" style="line-height:10px"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/another_events_01.jpg" style="display: block; height: auto; border: 0; width: 325px; max-width: 100%;" width="325" alt="Image of events" title="Image of events"></div></td></tr></table></td><td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #efb810; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="heading_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="width:100%;text-align:center;padding-top:45px;"><h3 style="margin: 0; color: #161635; font-size: 30px; font-family: 'Abril Fatface', Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: normal; letter-spacing: 1px; margin-top: 0; margin-bottom: 0;"><strong>YOUR BEST</strong></h3></td></tr></table><table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad"><div style="font-family: sans-serif"><div class style="font-size: 14px; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2;"><p style="margin: 0; font-size: 14px; text-align: center; font-family: inherit; mso-line-height-alt: 16.8px;"><span style="font-size:22px;">NEW YEARS PARTYS</span></p></div></div></td></tr></table><table class="heading_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="width:100%;text-align:center;"><h3 style="margin: 0; color: #161635; font-size: 30px; font-family: 'Abril Fatface', Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: normal; letter-spacing: 1px; margin-top: 0; margin-bottom: 0;"><strong>EXPERIENCE</strong></h3></td></tr></table><table class="divider_block block-6" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="padding-top:20px;padding-right:10px;padding-bottom:20px;padding-left:10px;"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td></tr></table></div></td></tr></table><table class="text_block block-7" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-right:15px;padding-left:15px;"><div style="font-family: sans-serif"><div class style="font-size: 12px; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 18px; color: #161635; line-height: 1.5;"><p style="margin: 0; font-size: 12px; text-align: center; font-family: inherit; mso-line-height-alt: 27px;"><span style="font-size:18px;">Lorem Ipsum Street 5, Barcelona</span></p></div></div></td></tr></table><table class="divider_block block-8" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="padding-top:20px;padding-right:10px;padding-bottom:20px;padding-left:10px;"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td></tr></table></div></td></tr></table><table class="text_block block-9" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-right:15px;padding-left:15px;padding-bottom:40px;"><div style="font-family: sans-serif"><div class style="font-size: 12px; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 18px; color: #161635; line-height: 1.5;"><p style="margin: 0; font-size: 12px; text-align: center; mso-line-height-alt: 27px;"><span style="font-size:18px;">31-12-2022 at 21:00</span></p></div></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-5" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="width:100%;padding-right:0px;padding-left:0px;"><div class="alignment" align="center" style="line-height:10px"><img class="big" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/another_events_04.jpg" style="display: block; height: auto; border: 0; width: 650px; max-width: 100%;" width="650" alt="Image of events" title="Image of events"></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-6" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 25px; padding-bottom: 25px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="button_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="text-align:center;padding-top:10px;padding-bottom:10px;"><div class="alignment" align="center"><!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.example.com" style="height:54px;width:198px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#efb810"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#161635; font-family:Arial, sans-serif; font-size:22px"><![endif]--><a href="https://www.example.com" target="_blank" style="text-decoration:none;display:inline-block;color:#161635;background-color:#efb810;border-radius:0px;width:auto;border-top:0px solid #FFFFFF;font-weight:undefined;border-right:0px solid #FFFFFF;border-bottom:0px solid #FFFFFF;border-left:0px solid #FFFFFF;padding-top:5px;padding-bottom:5px;font-family:Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;font-size:22px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:30px;padding-right:30px;font-size:22px;display:inline-block;letter-spacing:1px;"><span style="word-break: break-word;" dir="ltr"><span style="line-height: 44px;" data-mce-style dir="ltr">YES, I'M GOING!</span></span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-7" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="divider_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="padding-top:60px;padding-right:10px;padding-bottom:20px;padding-left:10px;"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #EFB810;"><span>&#8202;</span></td></tr></table></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-8" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 20px; padding-right: 20px; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="width:100%;text-align:center;padding-bottom:20px;"><h3 style="margin: 0; color: #ffffff; font-size: 30px; font-family: 'Abril Fatface', Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: normal; letter-spacing: 1px; margin-top: 0; margin-bottom: 0;"><strong>THE BEST EXPERIENCES FOR YOU</strong></h3></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-9" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 20px; padding-right: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="icons_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="vertical-align: middle; color: #ffffff; text-align: center; font-family: inherit; font-size: 24px; padding-top: 10px; padding-bottom: 10px;"><table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="alignment" style="vertical-align: middle; text-align: center;"><!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]--><!--[if !vml]><!--><table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation"><!--<![endif]--><tr><td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 15px; padding-left: 5px; padding-right: 5px;"><img class="icon" alt="Karaoke Events" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/events_karaokes.png" height="128" width="128" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td></tr><tr><td style="font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 24px; color: #ffffff; vertical-align: middle; letter-spacing: undefined; text-align: center;">Karaoke Events</td></tr></table></td></tr></table></td></tr></table></td><td class="column column-2" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="icons_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="vertical-align: middle; color: #ffffff; text-align: center; font-family: inherit; font-size: 24px; padding-top: 10px; padding-bottom: 10px;"><table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="alignment" style="vertical-align: middle; text-align: center;"><!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]--><!--[if !vml]><!--><table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation"><!--<![endif]--><tr><td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 15px; padding-left: 5px; padding-right: 5px;"><img class="icon" alt="Birthday Events" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/events_years.png" height="128" width="128" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td></tr><tr><td style="font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 24px; color: #ffffff; vertical-align: middle; letter-spacing: undefined; text-align: center;">Birthday Events</td></tr></table></td></tr></table></td></tr></table></td><td class="column column-3" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="icons_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="vertical-align: middle; color: #ffffff; text-align: center; font-family: inherit; font-size: 24px; padding-top: 10px; padding-bottom: 10px;"><table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="alignment" style="vertical-align: middle; text-align: center;"><!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]--><!--[if !vml]><!--><table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation"><!--<![endif]--><tr><td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 15px; padding-left: 5px; padding-right: 5px;"><img class="icon" alt="Work Celebrations" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/events_work.png" height="128" width="128" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td></tr><tr><td style="font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 24px; color: #ffffff; vertical-align: middle; letter-spacing: undefined; text-align: center;">Work Celebrations</td></tr></table></td></tr></table></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-10" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 30px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="button_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="text-align:center;padding-top:25px;padding-bottom:10px;"><div class="alignment" align="center"><!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.example.com" style="height:44px;width:158px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#efb810"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#161635; font-family:Arial, sans-serif; font-size:22px"><![endif]--><a href="https://www.example.com" target="_blank" style="text-decoration:none;display:inline-block;color:#161635;background-color:#efb810;border-radius:0px;width:auto;border-top:0px solid #FFFFFF;font-weight:undefined;border-right:0px solid #FFFFFF;border-bottom:0px solid #FFFFFF;border-left:0px solid #FFFFFF;padding-top:0px;padding-bottom:0px;font-family:Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;font-size:22px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:30px;padding-right:30px;font-size:22px;display:inline-block;letter-spacing:1px;"><span style="word-break: break-word;" dir="ltr"><span style="line-height: 44px;" data-mce-style dir="ltr">MORE INFO</span></span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div></td></tr></table><table class="divider_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="padding-top:20px;padding-right:10px;padding-bottom:20px;padding-left:10px;"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #EFB810;"><span>&#8202;</span></td></tr></table></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-11" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; border-top: 5px solid #EFB810; padding-left: 20px; padding-right: 20px; vertical-align: top; padding-top: 20px; padding-bottom: 25px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="text_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-top:20px;padding-bottom:10px;"><div style="font-family: sans-serif"><div class style="font-size: 14px; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2;"><p style="margin: 0; font-size: 14px; text-align: center; font-family: inherit; mso-line-height-alt: 16.8px;"><span style="font-size:24px;">THINK ABOUT US</span></p></div></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-12" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #d9d9e3; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #d9d9e3; padding-left: 20px; padding-right: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-top:25px;padding-right:10px;padding-bottom:10px;padding-left:10px;"><div style="font-family: sans-serif"><div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;"><p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><em><span style="font-size:18px;">"Cras mattis consectetur purus sit amet fermentum. Donec ullamcorper nulla non metus auctor fringilla."</span></em></p></div></div></td></tr></table><table class="divider_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td></tr></table></div></td></tr></table><table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-top:5px;padding-right:10px;padding-bottom:25px;padding-left:10px;"><div style="font-family: sans-serif"><div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;"><p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:22px;">Morgan McDonalds</span></p></div></div></td></tr></table></td><td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #c5c5cd; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-top:25px;padding-right:10px;padding-bottom:10px;padding-left:10px;"><div style="font-family: sans-serif"><div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;"><p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><em><span style="font-size:18px;">"Cenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Maecenas faucibus mollis interdum."</span></em></p></div></div></td></tr></table><table class="divider_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td></tr></table></div></td></tr></table><table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-top:5px;padding-right:10px;padding-bottom:25px;padding-left:10px;"><div style="font-family: sans-serif"><div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;"><p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:22px;">Lourdes Garcia</span></p></div></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-13" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #d9d9e3; color: #000000; width: 650px;" width="650"><tbody><tr class="reverse"><td class="column column-1 first" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #c5c5cd; padding-left: 20px; padding-right: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><div class="border"><table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-top:25px;padding-right:10px;padding-bottom:10px;padding-left:10px;"><div style="font-family: sans-serif"><div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;"><p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><em><span style="font-size:18px;">"Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Praesent commodo cursus magna."</span></em></p></div></div></td></tr></table><table class="divider_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td></tr></table></div></td></tr></table><table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-top:5px;padding-right:10px;padding-bottom:25px;padding-left:10px;"><div style="font-family: sans-serif"><div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;"><p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:22px;">Alex Harrisson</span></p></div></div></td></tr></table></div></td><td class="column column-2 last" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #d9d9e3; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><div class="border"><table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-top:25px;padding-right:10px;padding-bottom:10px;padding-left:10px;"><div style="font-family: sans-serif"><div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;"><p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><em><span style="font-size:18px;">"CNulla vitae elit libero, a pharetra augue. Curabitur blandit tempus porttitor.ras mattis consectetur purus sit amet."</span></em></p></div></div></td></tr></table><table class="divider_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td></tr></table></div></td></tr></table><table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-top:5px;padding-right:10px;padding-bottom:25px;padding-left:10px;"><div style="font-family: sans-serif"><div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;"><p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:22px;">Marta Cuggan</span></p></div></div></td></tr></table></div></td></tr></tbody></table></td></tr></tbody></table><table class="row row-14" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 20px; padding-right: 20px; vertical-align: top; padding-top: 25px; padding-bottom: 25px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="button_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="text-align:center;padding-top:10px;padding-bottom:10px;"><div class="alignment" align="center"><!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.example.com" style="height:54px;width:198px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#efb810"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#161635; font-family:Arial, sans-serif; font-size:22px"><![endif]--><a href="https://www.example.com" target="_blank" style="text-decoration:none;display:inline-block;color:#161635;background-color:#efb810;border-radius:0px;width:auto;border-top:0px solid #FFFFFF;font-weight:undefined;border-right:0px solid #FFFFFF;border-bottom:0px solid #FFFFFF;border-left:0px solid #FFFFFF;padding-top:5px;padding-bottom:5px;font-family:Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;font-size:22px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:30px;padding-right:30px;font-size:22px;display:inline-block;letter-spacing:1px;"><span style="word-break: break-word;" dir="ltr"><span style="line-height: 44px;" data-mce-style dir="ltr">YES, I'M GOING!</span></span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-15" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #161635; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/Fondo_footer.jpg'); background-position: top center; background-repeat: repeat;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="social_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:80px;text-align:center;"><div class="alignment" align="center"><table class="social-table" width="208px" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;"><tr><td style="padding:0 10px 0 10px;"><a href="https://www.facebook.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-circle-white/facebook@2x.png" width="32" height="32" alt="Facebook" title="facebook" style="display: block; height: auto; border: 0;"></a></td><td style="padding:0 10px 0 10px;"><a href="https://www.twitter.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-circle-white/twitter@2x.png" width="32" height="32" alt="Twitter" title="twitter" style="display: block; height: auto; border: 0;"></a></td><td style="padding:0 10px 0 10px;"><a href="https://www.linkedin.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-circle-white/linkedin@2x.png" width="32" height="32" alt="Linkedin" title="linkedin" style="display: block; height: auto; border: 0;"></a></td><td style="padding:0 10px 0 10px;"><a href="https://www.instagram.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-circle-white/instagram@2x.png" width="32" height="32" alt="Instagram" title="instagram" style="display: block; height: auto; border: 0;"></a></td></tr></table></div></td></tr></table><table class="text_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;"><div style="font-family: sans-serif"><div class style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #ffffff; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;"><p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:14px;">Sed posuere consectetur est at lobortis. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Cras mattis consectetur purus sit amet fermentum. Vestibulum id ligula porta felis euismod semper. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</span></p></div></div></td></tr></table><table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tr><td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;"><div style="font-family: sans-serif"><div class style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #efb810; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;"><p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:14px;"><a href="http://www.example.com" target="_blank" style="text-decoration: underline; color: #efb810;" rel="noopener">VIEW ONLINE</a> | <a href="http://www.example.com" target="_blank" style="text-decoration: underline; color: #efb810;" rel="noopener">UNSUBSCRIBE</a></span></p></div></div></td></tr></table><table class="image_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="padding-bottom:30px;padding-left:20px;padding-right:20px;padding-top:10px;width:100%;"><div class="alignment" align="center" style="line-height:10px"><a href="https://www.example.com" target="_blank" style="outline:none" tabindex="-1"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/YourLogo.png" style="display: block; height: auto; border: 0; width: 130px; max-width: 100%;" width="130" alt="Your Logo" title="Your Logo"></a></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table><table class="row row-16" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="pad" style="vertical-align: middle; color: #9d9d9d; font-family: inherit; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;"><table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tr><td class="alignment" style="vertical-align: middle; text-align: center;"><!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]--><!--[if !vml]><!--><table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation"><!--<![endif]--><tr><td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 6px;"><a href="https://www.designedwithbee.com/" target="_blank" style="text-decoration: none;"><img class="icon" alt="Designed with BEE" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/53601_510656/Signature/bee.png" height="32" width="34" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></a></td><td style="font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 15px; color: #9d9d9d; vertical-align: middle; letter-spacing: undefined; text-align: center;"><a href="https://www.designedwithbee.com/" target="_blank" style="color: #9d9d9d; text-decoration: none;">Designed with BEE</a></td></tr></table></td></tr></table></td></tr></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table><!-- End --></body></html>"""
             'HtmlPart' :
                 """
                    <!DOCTYPE html>
<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

<head>
	<title></title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
	<!--[if !mso]><!-->
	<link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Shrikhand" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Droid+Serif" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Cormorant+Garamond" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css">
	<!--<![endif]-->
	<style>
		* {
			box-sizing: border-box;
		}

		body {
			margin: 0;
			padding: 0;
		}

		a[x-apple-data-detectors] {
			color: inherit !important;
			text-decoration: inherit !important;
		}

		#MessageViewBody a {
			color: inherit;
			text-decoration: none;
		}

		p {
			line-height: inherit
		}

		.desktop_hide,
		.desktop_hide table {
			mso-hide: all;
			display: none;
			max-height: 0px;
			overflow: hidden;
		}

		@media (max-width:670px) {

			.desktop_hide table.icons-inner,
			.social_block.desktop_hide .social-table {
				display: inline-block !important;
			}

			.icons-inner {
				text-align: center;
			}

			.icons-inner td {
				margin: 0 auto;
			}

			.image_block img.big,
			.row-content {
				width: 100% !important;
			}

			.mobile_hide {
				display: none;
			}

			.stack .column {
				width: 100%;
				display: block;
			}

			.mobile_hide {
				min-height: 0;
				max-height: 0;
				max-width: 0;
				overflow: hidden;
				font-size: 0px;
			}

			.desktop_hide,
			.desktop_hide table {
				display: table !important;
				max-height: none !important;
			}

			.reverse {
				display: table;
				width: 100%;
			}

			.reverse .column.first {
				display: table-footer-group !important;
			}

			.reverse .column.last {
				display: table-header-group !important;
			}

			.row-13 td.column.first .border {
				padding-left: 20px;
				padding-right: 20px;
				border-top: 0;
				border-right: 0px;
				border-bottom: 0;
				border-left: 0;
			}

			.row-13 td.column.last .border {
				padding-left: 0;
				padding-right: 0;
				border-top: 0;
				border-right: 0px;
				border-bottom: 0;
				border-left: 0;
			}
		}
	</style>
</head>

<body style="margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none; background-color: #161635;">
	<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #161635;">
		<tbody>
			<tr>
				<td>
					<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-repeat: repeat; background-position: center top; background-color: #161635; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/Fondo_Cabecera_larga.jpg');">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-right: 20px; padding-left: 20px; vertical-align: top; padding-top: 30px; padding-bottom: 30px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:20px;padding-left:20px;">
																<div class="alignment" align="center" style="line-height:10px"><a href="https://www.example.com" target="_blank" style="outline:none" tabindex="-1"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/YourLogo.png" style="display: block; height: auto; border: 0; width: 175px; max-width: 100%;" width="175" alt="Your Logo Here" title="Your Logo Here"></a></div>
															</td>
														</tr>
													</table>
													<table class="divider_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:10px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #EFB810;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="image_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;padding-top:40px;">
																<div class="alignment" align="center" style="line-height:10px"><img class="big" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/Copa_Champagne_02.png" style="display: block; height: auto; border: 0; width: 480px; max-width: 100%;" width="480" alt="Image of Drink Party" title="Image of Drink Party"></div>
															</td>
														</tr>
													</table>
													<table class="heading_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;text-align:center;padding-top:30px;">
																<h1 style="margin: 0; color: #ffffff; font-size: 52px; font-family: 'Abril Fatface', Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: normal; letter-spacing: 1px; margin-top: 0; margin-bottom: 0;"><strong>NEW YEAR PARTY</strong></h1>
															</td>
														</tr>
													</table>
													<table class="divider_block block-6" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:25px;padding-right:10px;padding-bottom:5px;padding-left:10px;">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="20%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 5px solid #EFB810;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="heading_block block-7" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;text-align:center;">
																<h1 style="margin: 0; color: #efb810; font-size: 98px; font-family: 'Abril Fatface', Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: 400; letter-spacing: 10px; margin-top: 0; margin-bottom: 0;"><strong>2023</strong></h1>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; border-top: 5px solid #EFB810; padding-left: 20px; padding-right: 20px; vertical-align: top; padding-top: 20px; padding-bottom: 25px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="text_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-top:20px;padding-bottom:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 14px; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; text-align: center; font-family: inherit; mso-line-height-alt: 16.8px;"><span style="font-size:24px;">LOREM IPSUM DOLOR SIT AMET, CONSECTETUR</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-right:15px;padding-bottom:10px;padding-left:15px;">
																<div style="font-family: Tahoma, Verdana, sans-serif">
																	<div class style="font-size: 14px; font-family: 'Roboto', Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 21px; color: #5e5e6f; line-height: 1.5;">
																		<p style="margin: 0; font-size: 14px; text-align: center; font-family: Roboto, Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 24px;"><span style="font-size:16px;">Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Maecenas faucibus mollis interdum. Nullam quis risus eget urna.</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="button_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="text-align:center;padding-top:20px;padding-bottom:10px;">
																<div class="alignment" align="center">
																	<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.example.com" style="height:54px;width:198px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#efb810"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#161635; font-family:Arial, sans-serif; font-size:22px"><![endif]--><a href="https://www.example.com" target="_blank" style="text-decoration:none;display:inline-block;color:#161635;background-color:#efb810;border-radius:0px;width:auto;border-top:0px solid #FFFFFF;font-weight:undefined;border-right:0px solid #FFFFFF;border-bottom:0px solid #FFFFFF;border-left:0px solid #FFFFFF;padding-top:5px;padding-bottom:5px;font-family:Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;font-size:22px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:30px;padding-right:30px;font-size:22px;display:inline-block;letter-spacing:1px;"><span style="word-break: break-word;" dir="ltr"><span style="line-height: 44px;" data-mce-style dir="ltr">YES, I'M GOING!</span></span></span></a>
																	<!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-3" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block" style="height:40px;line-height:40px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-4" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/another_events_01.jpg" style="display: block; height: auto; border: 0; width: 325px; max-width: 100%;" width="325" alt="Image of events" title="Image of events"></div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #efb810; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;text-align:center;padding-top:45px;">
																<h3 style="margin: 0; color: #161635; font-size: 30px; font-family: 'Abril Fatface', Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: normal; letter-spacing: 1px; margin-top: 0; margin-bottom: 0;"><strong>YOUR BEST</strong></h3>
															</td>
														</tr>
													</table>
													<table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 14px; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; text-align: center; font-family: inherit; mso-line-height-alt: 16.8px;"><span style="font-size:22px;">NEW YEARS PARTYS</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="heading_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;text-align:center;">
																<h3 style="margin: 0; color: #161635; font-size: 30px; font-family: 'Abril Fatface', Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: normal; letter-spacing: 1px; margin-top: 0; margin-bottom: 0;"><strong>EXPERIENCE</strong></h3>
															</td>
														</tr>
													</table>
													<table class="divider_block block-6" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:20px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-7" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-right:15px;padding-left:15px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 18px; color: #161635; line-height: 1.5;">
																		<p style="margin: 0; font-size: 12px; text-align: center; font-family: inherit; mso-line-height-alt: 27px;"><span style="font-size:18px;">Lorem Ipsum Street 5, Barcelona</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="divider_block block-8" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:20px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-9" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-right:15px;padding-left:15px;padding-bottom:40px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 18px; color: #161635; line-height: 1.5;">
																		<p style="margin: 0; font-size: 12px; text-align: center; mso-line-height-alt: 27px;"><span style="font-size:18px;">31-12-2022 at 21:00</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-5" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px"><img class="big" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/another_events_04.jpg" style="display: block; height: auto; border: 0; width: 650px; max-width: 100%;" width="650" alt="Image of events" title="Image of events"></div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-6" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 25px; padding-bottom: 25px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="button_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="text-align:center;padding-top:10px;padding-bottom:10px;">
																<div class="alignment" align="center">
																	<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.example.com" style="height:54px;width:198px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#efb810"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#161635; font-family:Arial, sans-serif; font-size:22px"><![endif]--><a href="https://www.example.com" target="_blank" style="text-decoration:none;display:inline-block;color:#161635;background-color:#efb810;border-radius:0px;width:auto;border-top:0px solid #FFFFFF;font-weight:undefined;border-right:0px solid #FFFFFF;border-bottom:0px solid #FFFFFF;border-left:0px solid #FFFFFF;padding-top:5px;padding-bottom:5px;font-family:Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;font-size:22px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:30px;padding-right:30px;font-size:22px;display:inline-block;letter-spacing:1px;"><span style="word-break: break-word;" dir="ltr"><span style="line-height: 44px;" data-mce-style dir="ltr">YES, I'M GOING!</span></span></span></a>
																	<!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-7" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="divider_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:60px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #EFB810;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-8" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 20px; padding-right: 20px; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;text-align:center;padding-bottom:20px;">
																<h3 style="margin: 0; color: #ffffff; font-size: 30px; font-family: 'Abril Fatface', Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: normal; letter-spacing: 1px; margin-top: 0; margin-bottom: 0;"><strong>THE BEST EXPERIENCES FOR YOU</strong></h3>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-9" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 20px; padding-right: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #ffffff; text-align: center; font-family: inherit; font-size: 24px; padding-top: 10px; padding-bottom: 10px;">
																<table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																	<tr>
																		<td class="alignment" style="vertical-align: middle; text-align: center;">
																			<!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
																			<!--[if !vml]><!-->
																			<table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation">
																				<!--<![endif]-->
																				<tr>
																					<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 15px; padding-left: 5px; padding-right: 5px;"><img class="icon" alt="Karaoke Events" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/events_karaokes.png" height="128" width="128" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td>
																				</tr>
																				<tr>
																					<td style="font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 24px; color: #ffffff; vertical-align: middle; letter-spacing: undefined; text-align: center;">Karaoke Events</td>
																				</tr>
																			</table>
																		</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #ffffff; text-align: center; font-family: inherit; font-size: 24px; padding-top: 10px; padding-bottom: 10px;">
																<table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																	<tr>
																		<td class="alignment" style="vertical-align: middle; text-align: center;">
																			<!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
																			<!--[if !vml]><!-->
																			<table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation">
																				<!--<![endif]-->
																				<tr>
																					<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 15px; padding-left: 5px; padding-right: 5px;"><img class="icon" alt="Birthday Events" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/events_years.png" height="128" width="128" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td>
																				</tr>
																				<tr>
																					<td style="font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 24px; color: #ffffff; vertical-align: middle; letter-spacing: undefined; text-align: center;">Birthday Events</td>
																				</tr>
																			</table>
																		</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-3" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #ffffff; text-align: center; font-family: inherit; font-size: 24px; padding-top: 10px; padding-bottom: 10px;">
																<table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																	<tr>
																		<td class="alignment" style="vertical-align: middle; text-align: center;">
																			<!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
																			<!--[if !vml]><!-->
																			<table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation">
																				<!--<![endif]-->
																				<tr>
																					<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 15px; padding-left: 5px; padding-right: 5px;"><img class="icon" alt="Work Celebrations" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/events_work.png" height="128" width="128" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td>
																				</tr>
																				<tr>
																					<td style="font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 24px; color: #ffffff; vertical-align: middle; letter-spacing: undefined; text-align: center;">Work Celebrations</td>
																				</tr>
																			</table>
																		</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-10" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 30px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="button_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="text-align:center;padding-top:25px;padding-bottom:10px;">
																<div class="alignment" align="center">
																	<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.example.com" style="height:44px;width:158px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#efb810"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#161635; font-family:Arial, sans-serif; font-size:22px"><![endif]--><a href="https://www.example.com" target="_blank" style="text-decoration:none;display:inline-block;color:#161635;background-color:#efb810;border-radius:0px;width:auto;border-top:0px solid #FFFFFF;font-weight:undefined;border-right:0px solid #FFFFFF;border-bottom:0px solid #FFFFFF;border-left:0px solid #FFFFFF;padding-top:0px;padding-bottom:0px;font-family:Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;font-size:22px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:30px;padding-right:30px;font-size:22px;display:inline-block;letter-spacing:1px;"><span style="word-break: break-word;" dir="ltr"><span style="line-height: 44px;" data-mce-style dir="ltr">MORE INFO</span></span></span></a>
																	<!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
																</div>
															</td>
														</tr>
													</table>
													<table class="divider_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:20px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #EFB810;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-11" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; border-top: 5px solid #EFB810; padding-left: 20px; padding-right: 20px; vertical-align: top; padding-top: 20px; padding-bottom: 25px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="text_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-top:20px;padding-bottom:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 14px; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; text-align: center; font-family: inherit; mso-line-height-alt: 16.8px;"><span style="font-size:24px;">THINK ABOUT US</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-12" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #d9d9e3; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #d9d9e3; padding-left: 20px; padding-right: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-top:25px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><em><span style="font-size:18px;">"Cras mattis consectetur purus sit amet fermentum. Donec ullamcorper nulla non metus auctor fringilla."</span></em></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="divider_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-top:5px;padding-right:10px;padding-bottom:25px;padding-left:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:22px;">Morgan McDonalds</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #c5c5cd; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-top:25px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><em><span style="font-size:18px;">"Cenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Maecenas faucibus mollis interdum."</span></em></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="divider_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-top:5px;padding-right:10px;padding-bottom:25px;padding-left:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:22px;">Lourdes Garcia</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-13" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #d9d9e3; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr class="reverse">
												<td class="column column-1 first" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #c5c5cd; padding-left: 20px; padding-right: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="border">
														<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad" style="padding-top:25px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
																	<div style="font-family: sans-serif">
																		<div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;">
																			<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><em><span style="font-size:18px;">"Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Praesent commodo cursus magna."</span></em></p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
														<table class="divider_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad">
																	<div class="alignment" align="center">
																		<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																			<tr>
																				<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td>
																			</tr>
																		</table>
																	</div>
																</td>
															</tr>
														</table>
														<table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad" style="padding-top:5px;padding-right:10px;padding-bottom:25px;padding-left:10px;">
																	<div style="font-family: sans-serif">
																		<div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;">
																			<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:22px;">Alex Harrisson</span></p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
													</div>
												</td>
												<td class="column column-2 last" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #d9d9e3; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="border">
														<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad" style="padding-top:25px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
																	<div style="font-family: sans-serif">
																		<div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;">
																			<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><em><span style="font-size:18px;">"CNulla vitae elit libero, a pharetra augue. Curabitur blandit tempus porttitor.ras mattis consectetur purus sit amet."</span></em></p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
														<table class="divider_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad">
																	<div class="alignment" align="center">
																		<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																			<tr>
																				<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #FFFFFF;"><span>&#8202;</span></td>
																			</tr>
																		</table>
																	</div>
																</td>
															</tr>
														</table>
														<table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad" style="padding-top:5px;padding-right:10px;padding-bottom:25px;padding-left:10px;">
																	<div style="font-family: sans-serif">
																		<div class style="font-size: 14px; mso-line-height-alt: 16.8px; color: #161635; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;">
																			<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:22px;">Marta Cuggan</span></p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
													</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-14" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 20px; padding-right: 20px; vertical-align: top; padding-top: 25px; padding-bottom: 25px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="button_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="text-align:center;padding-top:10px;padding-bottom:10px;">
																<div class="alignment" align="center">
																	<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.example.com" style="height:54px;width:198px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#efb810"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#161635; font-family:Arial, sans-serif; font-size:22px"><![endif]--><a href="https://www.example.com" target="_blank" style="text-decoration:none;display:inline-block;color:#161635;background-color:#efb810;border-radius:0px;width:auto;border-top:0px solid #FFFFFF;font-weight:undefined;border-right:0px solid #FFFFFF;border-bottom:0px solid #FFFFFF;border-left:0px solid #FFFFFF;padding-top:5px;padding-bottom:5px;font-family:Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;font-size:22px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:30px;padding-right:30px;font-size:22px;display:inline-block;letter-spacing:1px;"><span style="word-break: break-word;" dir="ltr"><span style="line-height: 44px;" data-mce-style dir="ltr">YES, I'M GOING!</span></span></span></a>
																	<!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-15" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #161635; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/Fondo_footer.jpg'); background-position: top center; background-repeat: repeat;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="social_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:80px;text-align:center;">
																<div class="alignment" align="center">
																	<table class="social-table" width="208px" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;">
																		<tr>
																			<td style="padding:0 10px 0 10px;"><a href="https://www.facebook.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-circle-white/facebook@2x.png" width="32" height="32" alt="Facebook" title="facebook" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 10px 0 10px;"><a href="https://www.twitter.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-circle-white/twitter@2x.png" width="32" height="32" alt="Twitter" title="twitter" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 10px 0 10px;"><a href="https://www.linkedin.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-circle-white/linkedin@2x.png" width="32" height="32" alt="Linkedin" title="linkedin" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 10px 0 10px;"><a href="https://www.instagram.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-circle-white/instagram@2x.png" width="32" height="32" alt="Instagram" title="instagram" style="display: block; height: auto; border: 0;"></a></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #ffffff; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:14px;">Sed posuere consectetur est at lobortis. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Cras mattis consectetur purus sit amet fermentum. Vestibulum id ligula porta felis euismod semper. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #efb810; line-height: 1.2; font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:14px;"><a href="http://www.example.com" target="_blank" style="text-decoration: underline; color: #efb810;" rel="noopener">VIEW ONLINE</a> | <a href="http://www.example.com" target="_blank" style="text-decoration: underline; color: #efb810;" rel="noopener">UNSUBSCRIBE</a></span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="image_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:30px;padding-left:20px;padding-right:20px;padding-top:10px;width:100%;">
																<div class="alignment" align="center" style="line-height:10px"><a href="https://www.example.com" target="_blank" style="outline:none" tabindex="-1"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/7701/YourLogo.png" style="display: block; height: auto; border: 0; width: 130px; max-width: 100%;" width="130" alt="Your Logo" title="Your Logo"></a></div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-16" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #9d9d9d; font-family: inherit; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;">
																<table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																	<tr>
																		<td class="alignment" style="vertical-align: middle; text-align: center;">
																			<!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
																			<!--[if !vml]><!-->
																			<table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation">
																				<!--<![endif]-->
																				<tr>
																					<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 6px;"><a href="https://www.designedwithbee.com/" target="_blank" style="text-decoration: none;"><img class="icon" alt="Designed with BEE" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/53601_510656/Signature/bee.png" height="32" width="34" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></a></td>
																					<td style="font-family: Oswald, Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 15px; color: #9d9d9d; vertical-align: middle; letter-spacing: undefined; text-align: center;"><a href="https://www.designedwithbee.com/" target="_blank" style="color: #9d9d9d; text-decoration: none;">Designed with BEE</a></td>
																				</tr>
																			</table>
																		</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
				</td>
			</tr>
		</tbody>
	</table><!-- End -->
</body>

</html>
                """
        }
    )
    print(response)


def send_email_using_template():
    response = client.send_templated_email(
        Source='izaanit.dev@gmail.com',
        Destination={
            'ToAddresses': [
                'testdata.islam@gmail.com',
            ]
        },
        ReplyToAddresses=[
            'testdata.islam@gmail.com',
        ],
        Template='B2301-DevOpsMarketing-Template3',
        TemplateData='{"name": "b2202"}'
    )

    print(response)


send_email_using_template()
#create_template()

from django.views.generic import *
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import SaisieForm, CheckRecForm

import csv
import datetime
import copy
import sys

from django import template
#from pcloud import PyCloud
#from fs import open_fs, opener

register = template.Library()

nbing = 0
rep_tab = []
plan_tab = []
myinglist = []

globvar = ['this', 'is', 'my', 'test']
mondic = {}

import imaplib, email
import parser

import string
import parser
from email import utils

import imaplib
user = "francis.bich@sfr.fr"
password = "Insistt100"
#imap_url = "imap.sfr.fr"
#imap_url = "imap.gmail.com"

datadir = 'https://eu.pythonanywhere.com/user/fbich/files/home/fbich/wwa/static/datafiles'
infile = datadir + '/WWA_TABLDC1.csv'

def home(request):
    return render(request,'index.html')

def page2(request):
    return render(request,'page2.html')

def page3(request):
    return render(request,'page3.html')

def grille(request):
    return render(request,'grille.html')

#-----------------------------------------------------------------------
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    con.select("INBOX")

    result, data = con.fetch(b"3","(RFC822)")
    raw = email.message_from_bytes(data[0][1])
    print(get_body(raw))

#-----------------------------------------------------------------------
'''
def lirefic():
    
    print('debut de lirefic')
    global rep_tab
    global plan_tab
    global myinglist
    MyFilename = 'D:/FBWebDev/waswetasse/templates/static/WWA_TABLDC1.csv'
    https://eu.pythonanywhere.com/user/fbich/files/home/fbich/wwa/static/datafiles

    with open(MyFilename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        rep_tab = []
        for row in csv_reader:
            if line_count == 1:
                myinglist = row
                # print(len(myinglist))  # 28
                del myinglist[0:7]     
                # print(len(myinglist))  # 21
                line_count += 1
            if line_count > 2:
                rep_tab.append(row)
                line_count += 1
            else:
                line_count += 1
    
    print(f'Processed {line_count} lines.')
    plan_tab = copy.deepcopy(rep_tab)
    for r in plan_tab:
        del r[5:]

    return rep_tab, plan_tab, myinglist
'''
#-----------------------------------------------------------------------
def successpage(request):

    if request.method == 'GET':
        print("successpage Method=GET")
        form = CheckRecForm()
        return render(request, "index.html", {'form': form})

    my_form = CheckRecForm()
    if request.method == "POST":
        print("successpage Method=POST")
        my_form = CheckRecForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            mondic = my_form.cleaned_data
        else:
            print('myform is not yet valid')
            mondic = {}
        context = {
            "form": my_form,
            "mondic": mondic,
        }
        return render(request, 'index.html', context)
    
#-----------------------------------------------------------------------
def index(request):

    import os
    DirExist = os.path.exists("D:\Kawashima1")
    print(' the file D:\Kawashima exists ? ', DirExist)

    #os.path.exists(test_file.txt)
    #os.path.exists(no_exist_file.txt)
    #os.path.exists(test_dir)
    #os.path.exists(no_exist_dir)

    '''
    rep_tab2 = lirefic()
    print('dans index :', rep_tab2, '<<<')
    '''
    template = loader.get_template('index.html')
    '''
    context = {
        'inglist' : myinglist,
        'replist' : rep_tab2,
        'planlist' : plan_tab,
        'nbing' : nbing,
    }
    '''
    context = {
        'dummy' : 'this is useless',
    }
        
    return HttpResponse(template.render(context, request))

#-----------------------------------------------------------------------
def get_mail_client(email_address):
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993
    
    password = "13Karabatic&"
    '''
    password = ""
    with open("password.txt", "r") as f:
        password = f.read().strip()
    '''

    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(email_address, password)
    return mail

#-----------------------------------------------------------------------
def saisie(request): # This is mandatory ; I don't know why !

    print("coucou")
    mymail = get_mail_client("francis.bich@gmail.com")
    print(mymail)
    '''
    import poplib
    import email.parser
    parser = email.parser.Parser()
    mailbox = poplib.POP3_SSL("pop.sfr.fr",995)

    import os
    DirExist = os.path.exists(infile)
    print(' the data file exists ? ', DirExist)
    
    try:
        mailbox.user(user)
        mailbox.pass_(password)
        response, listings, octet_count = mailbox.list()
        numMessages = len(mailbox.list()[1])

        for listing in listings:
            number, size = listing.decode('ascii').split()

            #print("Message %s has %s bytes" % (number, size))
            resp, lines, octets = mailbox.retr(number)
            #print('===')
            #print(lines)

            # lines stores each line of the original text of the message
            # so that you can get the original text of the entire message use the join function and lines variable. 
            try:
                msg_content = b'\r\n'.join(lines).decode('utf-8')
                
            except:
                print("Unexpected error", sys.exc_info()[0])
                print(lines[11:20] )
                break
                raise
            #finally:
                #print("Probleme de conversion")

            # now parse out the email object.
            msg = parser.parsestr(msg_content)

            # get email from, to, subject attribute value.
            email_from = msg.get('From')
            email_subject = msg.get('Subject')

            if email_subject == 'LDC':
                sent = msg['date']
                #print(f"Date header: {sent}")
                #received = msg['Received'][0]
                #received = received.split(";")[-1]
                #print(f"Received: {received}")
                #sent_ts = utils.parsedate(sent)
                #received_ts = utils.parsedate(received)
                print('From ' + email_from + sent + ' : ' + email_subject)
                email_body = get_body(msg)
                # print(email_body)
                email_body = msg.get('Body')
                if msg.is_multipart():
                    print("message is multipart")
                    for part in email_body.get_payload():
                        print(part.get_payload())
                else:
                    print("message isn't multipart")
                    print(msg.get_payload())
            
    except poplib.error_proto as exception:
        print("Login failed:", exception)

    finally:
        mailbox.quit() 

    print('---------------------------------------------------------------------------------------')
    
    #print(pc.listfolder(folderid=0))
    #print('---------------------------------------------------------------------------------------')
    #print(pc.listfolder(folderid=5759400854))
    #print('---------------------------------------------------------------------------------------')

    ##opener.open_fs('pcloud://email%40example.com:SecretPassword@/')
    ##<pCloudFS>

    ##opener.open_fs('pcloud://francis.bich@sfr.fr:8Narcisse&/')
    #opener.open('pcloud://francis.bich@sfr.fr:8Narcisse&/', writeable=True, create=False, cwd='.', default_protocol='osfs')
    ##<pCloudFS>
    #print("coucou")

    ## Upload files
    ##pc.uploadfile(files=['/full/path/to/image1.jpg', '/Users/tom/another/image.png'],
    ##pc.uploadfile(files=['/My Files/LDC_20201001.txt'], path='D:') 

    ##MyFilename = 'D:/FBWebDev/waswetasse/templates/static/WWA_TABLDC1.csv'

    #MyFilename = open_fs('/My Files/LDC_20201001.txt')

    #with open(MyFilename) as csv_file:
    #    csv_reader = csv.reader(csv_file, delimiter=';')
    #    for row in csv_reader:
    #      print(row)

'''
    return HttpResponse(request, "hello world")

#-----------------------------------------------------------------------
def _collect_headers(strings):
    headers, parser = {}, email.parser.Parser()

    for string in strings:
        headers.update(dict(parser.parsestr(string)))

    return headers

#-----------------------------------------------------------------------
def contact(request):

    posts = [
            { 'titre': 'premier','qty': '4', 'recok': 'False' },
            { 'titre': 'deuxieme','qty': '2','recok': 'False'},
            { 'titre': 'troisieme','qty': '3,5', 'recok': 'False' },
        ]

    # Au premier appel a un URL la request.method est GET (dirais-je...)
    if request.method == 'GET':
        print("Contact Method=GET")
        # Creation d'une instance de la Form "SaisieForm" avec les données de la requete.
        form = SaisieForm()
        # Demande d'affichage de la page "saisie.html" avec les données de la form.
        return render(request, "saisie.html", {'form': form})
    
    # if this is a POST request we need to process the form data 
    # En validant un bouton ou un texte "submit", la request.method est POST. 
    if request.method == 'POST':
        print("Contact Method=POST")
        form = SaisieForm(request.POST)
        # Verification si les données saisies sont valides...
        if form.is_valid(): # Si ok, on defini les variables a poster avec le render.
            print("SaisieForm data is valid")
            nom3 = request.POST.get('name2', '') #name2 est le nom de l'objet inputbox, dans form.
            myfirstname = request.POST.get('firstname2', '') 
            today = datetime.datetime.now().date()
            # redirect to a new URL is possible :
            return render(request, "contact.html", {'form': form, 'posts': posts, 'mydata': nom3, 'today': today, 'myfirstname' : myfirstname, 'globvar': globvar})
        
        else:
            print("SaisieForm data is NOT valid")
            mytext = 'donnée entrée de la grille'
            print(rep_tab[0])
            return render(request, "grille.html", {'mytext': mytext, 'globvar': globvar, 'replist': rep_tab})

    print("Probleme: la request.method n'est ni un POST, ni un GET, mais " + request.method)

    #return HttpResponse(request, "coucou")

#-----------------------------------------------------------------------
def http_response_form(request):

    if request.method == "POST":
        username = request.POST.get('username')
        if username:
            return HttpResponse(f'<h1>hello {username}</h1>')
        else:
            return HttpResponse('<h1>please, enter your username</h1>')

    return render(request, "HttpResponse.html")

#-----------------------------------------------------------------------
'''
D: & cd FBWebDev\waswetasse & myvenv37\Scripts\activate & python manage.py runserver 127.0.0.1:8000
python manage.py runserver 127.0.0.1:8000
'''

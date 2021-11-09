from feedgen.feed import FeedGenerator
import csv

siteURL = "https://security-guidance.service.justice.gov.uk/"

outFileDita = open('changelog.dita','w')
outFileDita.write('<?xml version="1.0" encoding="UTF-8"?>\n')
outFileDita.write('<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">\n')
outFileDita.write('<topic id="changelog">\n')
outFileDita.write('<title>Change log for <ph conref="conrefs.dita#conrefs/mojlong"/> Security Guidance</title>\n')
outFileDita.write('<body>\n')
outFileDita.write('<p>This document summarises what changes were made, and when, to <ph conref="conrefs.dita#conrefs/moj"/> Security policy and guidance. The most recent changes appear at the beginning of the list.</p>\n')
outFileDita.write('<dl>\n')

fg = FeedGenerator()
fg.id('https://security-guidance.service.justice.gov.uk/')
fg.title('MoJ Security Guidance')
fg.author( {'name':'Ministry of Justice','email':'itsecuritypolicy@digital.justice.gov.uk'} )
fg.link( href='https://security-guidance.service.justice.gov.uk/', rel='alternate' )
fg.logo('https://security-guidance.service.justice.gov.uk/images/moj-logotype-crest.png')
fg.subtitle('This site documents the Ministry of Justice (MoJ) security policies and guidance.')
fg.link( href='https://security-guidance.service.justice.gov.uk/', rel='self' )
fg.language('en')
fg.contributor( name='Ministry of Justice', email='itsecuritypolicy@digital.justice.gov.uk' )

with open('../changeLog.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    loopCounter = 0
    entryList = []
    ditaEntries = []
    for row in csvReader:
        entryList.append(fg.add_entry())
        entryList[loopCounter].id(""+siteURL+row[0]+"")
        entryList[loopCounter].title(""+row[1]+"")
        entryList[loopCounter].description(""+row[2]+"")
        entryList[loopCounter].link( href=""+siteURL+row[3]+"")
        entryList[loopCounter].pubDate(""+row[4]+"")
        ditaEntries.insert(0,"<dlentry><dt>"+row[4]+" <xref href='"+siteURL+row[3]+"' format='html' scope='external'>"+row[1]+"</xref></dt><dd>"+row[2]+"</dd></dlentry>")
        loopCounter = loopCounter + 1


atomfeed = fg.atom_str(pretty=True)
rssfeed  = fg.rss_str(pretty=True)
fg.atom_file('atom.xml')
fg.rss_file('rss.xml')

for row in ditaEntries:
    outFileDita.write(row+"\n")
outFileDita.write('</dl>\n')
outFileDita.write('</body>\n')
outFileDita.write('<topic id="contact-details" conref="conrefs.dita#contact-details" platform="html"><title/></topic>\n')
outFileDita.write('<topic id="feedback" platform="html" conref="conrefs.dita#feedback"><title/></topic>\n')
outFileDita.write('</topic>\n')

outFileDita.close

exit(0)

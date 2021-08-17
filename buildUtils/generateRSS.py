from feedgen.feed import FeedGenerator
import csv

outFileDita = open('../dita/changelog.dita','w')
outFileDita.write('<?xml version="1.0" encoding="UTF-8"?>\n')
outFileDita.write('<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">\n')
outFileDita.write('<topic id="changelog">\n')
outFileDita.write('<title>Changelog for <ph conref="conrefs.dita#conrefs/mojlong"/> Security Guidance</title>\n')
outFileDita.write('<body>\n')
outFileDita.write('<p>This document summarises what changes were made, and when, to <ph conref="conrefs.dita#conrefs/moj"/> Security policy and guidance. The most recent changes appear at the end of the list.</p>\n')

fg = FeedGenerator()
fg.id('https://security-guidance.service.justice.gov.uk')
fg.title('MoJ Security Guidance')
fg.author( {'name':'Ministry of Justice','email':'itsecuritypolicy@digital.justice.gov.uk'} )
fg.link( href='https://security-guidance.service.justice.gov.uk', rel='alternate' )
fg.logo('https://security-guidance.service.justice.gov.uk/favicon.ico')
fg.subtitle('This site documents the Ministry of Justice (MoJ) security policies and guidance.')
fg.link( href='https://security-guidance.service.justice.gov.uk', rel='self' )
fg.language('en')
fg.contributor( name='Ministry of Justice', email='itsecuritypolicy@digital.justice.gov.uk' )

with open('../changeLog.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    loopCounter = 0
    entryList = []
    for row in csvReader:
        entryList.append(fg.add_entry())
        entryList[loopCounter].id("'"+row[0]+"'")
        entryList[loopCounter].title("'"+row[1]+"'")
        entryList[loopCounter].description("'"+row[2]+"'")
        entryList[loopCounter].link( href="'"+row[3]+"'")
        entryList[loopCounter].pubDate("'"+row[4]+"'")
        loopCounter = loopCounter + 1

print('Finished looping.')

atomfeed = fg.atom_str(pretty=True)
rssfeed  = fg.rss_str(pretty=True)
fg.atom_file('atom.xml')
fg.rss_file('rss.xml')

outFileDita.close

exit(0)

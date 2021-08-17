from feedgen.feed import FeedGenerator
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

fe1 = fg.add_entry()
fe1.id('https://security-guidance.service.justice.gov.uk/202108161703')
fe1.title('Data Movement Form updated.')
fe1.description('Data Movement Form updated.')
fe1.link(href="https://security-guidance.service.justice.gov.uk/gs/data-movement-form.docx")
fe1.pubDate('2021-08-16T17:03:00Z')

fe2 = fg.add_entry()
fe2.id('https://security-guidance.service.justice.gov.uk/202108161704')
fe2.title('Clarification for accessing MoJ IT systems overseas.')
fe2.description('Additional information describing the process.')
fe2.link(href="https://security-guidance.service.justice.gov.uk/accessing-moj-it-systems-from-overseas/")
fe2.pubDate('2021-08-16T17:04:00Z')

fe3 = fg.add_entry()
fe3.id('https://security-guidance.service.justice.gov.uk/202108170926')
fe3.title('Provide offline version of Group Security content.')
fe3.description('Created PDF and eBook versions of the security policy and guidance subset for Group Security.')
fe3.link(href="https://security-guidance.service.justice.gov.uk/#offline-content")
fe3.pubDate('2021-08-17T09:26:00Z')

atomfeed = fg.atom_str(pretty=True) # Get the ATOM feed as string
rssfeed  = fg.rss_str(pretty=True) # Get the RSS feed as string
fg.atom_file('atom.xml') # Write the ATOM feed to a file
fg.rss_file('rss.xml') # Write the RSS feed to a file

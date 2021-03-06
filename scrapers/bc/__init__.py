# encoding: utf-8
import datetime

metadata = dict(
    name='British Columbia',
    capitol_timezone='America/Vancouver',
    abbreviation='bc',
    legislature_name=u'Legislative Assembly of British Columbia',
    chambers = {
        'lower': {'name': 'Assembly', 'title': 'MLA'}
    },
    terms=[
        dict(name='39', sessions=['39th1st', '39th2nd', '39th3rd', '39th4th'],
             start_year=2009, end_year=2012),
    ],
    session_details={
        '39th1st': {'type': 'primary',
                 'display_name': '1st Session, 39th Parliament',
                 '_scraped_name': u'1st Session, 39th Parliament (2009)',
                 'start_date': datetime.datetime(2009, 8, 25),
                 'end_date': datetime.datetime(2010, 2, 9)
                },
        '39th2nd': {'type': 'primary',
                 'display_name': '2nd Session, 39th Parliament',
                 '_scraped_name': u'2nd Session, 39th Parliament (2010)',
                 'start_date': datetime.datetime(2010, 2, 9),
                 'end_date': datetime.datetime(2011, 2, 14)
                },
        '39th3rd': {'type': 'primary',
                 'display_name': '3rd Session, 39th Parliament',
                 '_scraped_name': u'3rd Session, 39th Parliament (2011)',
                 'start_date': datetime.datetime(2011, 2, 14),
                 'end_date': datetime.datetime(2011, 10, 3)
                },
        '39th4th': {'type': 'primary',
                 'display_name': '4th Session, 39th Parliament',
                 'start_date': datetime.datetime(2011, 10, 3),
                 'end_date': datetime.datetime(2012, 5, 31)
                },
    },
    feature_flags=['events', 'speeches'],
    _ignored_scraped_sessions=[
        '5th Session, 38th Parliament (2009)',
        '4th Session, 38th Parliament (2008)',
        '3rd Session, 38th Parliament (2007)',
        '2nd Session, 38th Parliament (2006)',
        '1st Session, 38th Parliament (2005)',
        '6th Session, 37th Parliament (2005)',
        '5th Session, 37th Parliament (2004)',
        '4th Session, 37th Parliament (2003)',
        '3rd Session, 37th Parliament (2002)',
        '2nd Session, 37th Parliament (2001)',
        '1st Session, 37th Parliament (2001)',
        '5th Session, 36th Parliament (2001)',
        '4th Session, 36th Parliament (2000)',
        '3rd Session, 36th Parliament (1998/99)',
        '2nd Session, 36th Parliament (1997)',
        '1st Session, 36th Parliament (1996)',
        '5th Session, 35th Parliament (1996)',
        '4th Session, 35th Parliament (1995)',
        '3rd Session, 35th Parliament (1994)',
        '2nd Session, 35th Parliament (1993)',
        '1st Session, 35th Parliament (1992)'
    ]
)


def session_list():
    import re
    from billy.scrape.utils import url_xpath
    ret = [re.sub('\s+', ' ', x).strip() for x in url_xpath(
        'http://www.leg.bc.ca/documents/4-1-0.htm',
         '//table[3]//a[contains(@href, "index.htm")]/text()')]
    for key in ['', 'Home']:
        if key in ret:
            ret.remove(key)
    return ret

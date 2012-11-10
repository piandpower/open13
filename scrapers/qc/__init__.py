# encoding: utf-8

metadata = dict(
    name='Quebec',
    capitol_timezone='America/Quebec',
    abbreviation='qc',
    legislature_name=u'Assemblée nationale du Québec',
    # this should all go away once metadata v2 lands
    lower_chamber_name='',
    upper_chamber_name='',
    lower_chamber_title=u'député',
    upper_chamber_title='',
    upper_chamber_term='',
    lower_chamber_term='',
    terms=[
        dict(name='40', sessions=['40:1'], start_year=2012, end_year=2013),
    ],
    session_details={
        '40:1': {'type': 'primary',
                 'display_name': '40th Legislature, 1st Session',
                 '_scraped_name': u'Current session - 40th legislature, 1st session (October 30, 2012 - )',
                },
    },
    feature_flags=[],
    _ignored_scraped_sessions=[
        '39th legislature, 2nd session (February 23, 2011 - August 1, 2012)',
        '39th legislature, 1st session (January 13, 2009 - February 22, 2011)',
        '38th legislature, 1st session (May 8, 2007 - November 5, 2008)',
        '37th legislature, 2nd session (March 14, 2006 - February 21, 2007)',
        '37th legislature, 1st session (June 4, 2003 - March 10, 2006)',
        '36th legislature, 2nd session (March 22, 2001 - March 12, 2003)',
        '36th legislature, 1st session (March 2, 1999 - March 9, 2001)',
        '35th legislature, 2nd session (March 25, 1996 - October 21, 1998)',
        '35th legislature, 1st session (November 29, 1994 - March 13, 1996)',
        '34th legislature, 3rd session (March 17, 1994 - June 17, 1994)',
        '34th legislature, 2nd session (March 19, 1992 - March 10, 1994)',
        '34th legislature, 1st session (November 28, 1989 - March 18, 1992)',
        '33th legislature, 2nd session (March 8, 1988 - August 9, 1989)',
        '33th legislature, 1st session (December 16, 1985 - March 8, 1988)',
        '32th legislature, 5th session (October 16, 1984 - October 10, 1985)',
        '32th legislature, 4th session (March 23, 1983 - June 20, 1984)',
        '32th legislature, 3rd session (November 9, 1981 - March 10, 1983)',
        '32th legislature, 2nd session (September 30, 1981 - October 2, 1981)',
        '32th legislature, 1st session (May 19, 1981 - June 18, 1981)',
        '31th legislature, 6th session (November 5, 1980 - March 12, 1981)',
        '31th legislature, 5th session (October 24, 1980 - October 24, 1980)',
        '31th legislature, 4th session (March 6, 1979 - June 18, 1980)',
        '31th legislature, 3rd session (February 21, 1978 - February 20, 1979)',
        '31th legislature, 2nd session (March 8, 1977 - December 22, 1977)',
        '31th legislature, 1st session (December 14, 1976 - December 23, 1976)',
        '30th legislature, 4th session (March 16, 1976 - October 18, 1976)',
        '30th legislature, 3rd session (March 18, 1975 - December 19, 1975)',
        '30th legislature, 2nd session (March 14, 1974 - December 28, 1974)',
        '30th legislature, 1st session (November 22, 1973 - December 22, 1973)',
        '29th legislature, 4th session (March 15, 1973 - September 25, 1973)',
        '29th legislature, 3rd session (March 7, 1972 - March 14, 1973)',
        '29th legislature, 2nd session (February 23, 1971 - December 24, 1971)',
        '29th legislature, 1st session (June 9, 1970 - December 19, 1970)',
        '28th legislature, 5th session (February 24, 1970 - March 12, 1970)',
        '28th legislature, 4th session (February 25, 1969 - December 23, 1969)',
        '28th legislature, 3rd session (February 20, 1968 - December 18, 1968)',
        '28th legislature, 2nd session (October 20, 1967 - October 20, 1967)',
        '28th legislature, 1st session (December 1, 1966 - August 12, 1967)',
        '27th legislature, 6th session (January 25, 1966 - April 18, 1966)',
        '27th legislature, 5th session (October 22, 1965 - October 23, 1965)',
        '27th legislature, 4th session (January 21, 1965 - August 6, 1965)',
        '27th legislature, 3rd session (January 14, 1964 - July 31, 1964)',
        '27th legislature, 2nd session (August 21, 1963 - August 23, 1963)',
        '27th legislature, 1st session (January 15, 1963 - July 11, 1963)',
        '26th legislature, 3rd session (January 9, 1962 - September 19, 1962)',
        '26th legislature, 2nd session (November 10, 1960 - June 10, 1961)',
        '26th legislature, 1st session (September 20, 1960 - September 22, 1960)',
        '25th legislature, 4th session (November 18, 1959 - March 18, 1960)',
        '25th legislature, 3rd session (November 19, 1958 - March 5, 1959)',
        '25th legislature, 2nd session (November 13, 1957 - February 21, 1958)',
        '25th legislature, 1st session (November 14, 1956 - February 21, 1957)',
        '24th legislature, 4th session (November 16, 1955 - February 23, 1956)',
        '24th legislature, 3rd session (November 17, 1954 - February 22, 1955)',
        '24th legislature, 2nd session (November 18, 1953 - March 5, 1954)',
        '24th legislature, 1st session (November 12, 1952 - February 26, 1953)',
        '23th legislature, 4th session (November 7, 1951 - January 23, 1952)',
        '23th legislature, 3rd session (November 8, 1950 - March 14, 1951)',
        '23th legislature, 2nd session (February 15, 1950 - April 5, 1950)',
        '23th legislature, 1st session (January 19, 1949 - March 10, 1949)',
        '22th legislature, 4th session (January 14, 1948 - April 1, 1948)',
        '22th legislature, 3rd session (February 12, 1947 - May 10, 1947)',
        '22th legislature, 2nd session (February 13, 1946 - April 17, 1946)',
        '22th legislature, 1st session (February 7, 1945 - June 1, 1945)',
        '21th legislature, 5th session (January 18, 1944 - June 3, 1944)',
        '21th legislature, 4th session (February 23, 1943 - June 22, 1943)',
        '21th legislature, 3rd session (February 24, 1942 - May 29, 1942)',
        '21th legislature, 2nd session (January 7, 1941 - May 17, 1941)',
        '21th legislature, 1st session (February 20, 1940 - June 22, 1940)',
        '20th legislature, 4th session (January 18, 1939 - April 28, 1939)',
        '20th legislature, 3rd session (January 26, 1938 - April 12, 1938)',
        '20th legislature, 2nd session (February 24, 1937 - May 27, 1937)',
        '20th legislature, 1st session (October 7, 1936 - November 12, 1936)',
        '19th legislature, 1st session (March 24, 1936 - June 11, 1936)',
        '18th legislature, 4th session (January 8, 1935 - May 18, 1935)',
        '18th legislature, 3rd session (January 9, 1934 - April 20, 1934)',
        '18th legislature, 2nd session (January 10, 1933 - April 13, 1933)',
        '18th legislature, 1st session (November 3, 1931 - February 19, 1932)',
        '17th legislature, 4th session (December 2, 1930 - April 4, 1931)',
        '17th legislature, 3rd session (January 7, 1930 - April 4, 1930)',
        '17th legislature, 2nd session (January 8, 1929 - April 4, 1929)',
        '17th legislature, 1st session (January 10, 1928 - March 22, 1928)',
        '16th legislature, 4th session (January 11, 1927 - April 1, 1927)',
        '16th legislature, 3rd session (January 7, 1926 - March 24, 1926)',
        '16th legislature, 2nd session (January 7, 1925 - April 3, 1925)',
        '16th legislature, 1st session (January 17, 1923 - March 15, 1924)',
        '15th legislature, 4th session (October 24, 1922 - December 29, 1922)',
        '15th legislature, 3rd session (January 10, 1922 - March 21, 1922)',
        '15th legislature, 2nd session (January 11, 1921 - March 19, 1921)',
        '15th legislature, 1st session (December 10, 1919 - February 14, 1920)',
        '14th legislature, 3rd session (January 21, 1919 - March 17, 1919)',
        '14th legislature, 2nd session (December 4, 1917 - February 9, 1918)',
        '14th legislature, 1st session (November 7, 1916 - December 22, 1916)',
        '13th legislature, 4th session (January 11, 1916 - March 16, 1916)',
        '13th legislature, 3rd session (January 7, 1915 - March 5, 1915)',
        '13th legislature, 2nd session (November 11, 1913 - February 19, 1914)',
        '13th legislature, 1st session (November 5, 1912 - December 21, 1912)',
        '12th legislature, 4th session (January 9, 1912 - April 3, 1912)',
        '12th legislature, 3rd session (January 10, 1911 - March 24, 1911)',
        '12th legislature, 2nd session (March 15, 1910 - June 4, 1910)',
        '12th legislature, 1st session (March 2, 1909 - May 29, 1909)',
        '11th legislature, 4th session (March 3, 1908 - April 25, 1908)',
        '11th legislature, 3rd session (January 15, 1907 - March 14, 1907)',
        '11th legislature, 2nd session (January 18, 1906 - March 9, 1906)',
        '11th legislature, 1st session (March 2, 1905 - May 20, 1905)',
        '10th legislature, 4th session (March 22, 1904 - June 2, 1904)',
        '10th legislature, 3rd session (February 26, 1903 - April 25, 1903)',
        '10th legislature, 2nd session (February 13, 1902 - March 26, 1902)',
        '10th legislature, 1st session (February 14, 1901 - March 28, 1901)',
        '9th legislature, 3rd session (January 18, 1900 - March 23, 1900)',
        '9th legislature, 2nd session (January 12, 1899 - March 10, 1899)',
        '9th legislature, 1st session (November 23, 1897 - January 15, 1898)',
        '8th legislature, 6th session (November 17, 1896 - January 9, 1897)',
        '8th legislature, 5th session (October 30, 1895 - December 21, 1895)',
        '8th legislature, 4th session (November 20, 1894 - January 12, 1895)',
        '8th legislature, 3rd session (November 9, 1893 - January 8, 1894)',
        '8th legislature, 2nd session (January 12, 1893 - February 27, 1893)',
        '8th legislature, 1st session (April 26, 1892 - June 24, 1892)',
        '7th legislature, 1st session (November 4, 1890 - December 30, 1890)',
        '6th legislature, 4th session (January 7, 1890 - April 2, 1890)',
        '6th legislature, 3rd session (January 9, 1889 - March 21, 1889)',
        '6th legislature, 2nd session (May 15, 1888 - July 12, 1888)',
        '6th legislature, 1st session (January 27, 1887 - May 18, 1887)',
        '5th legislature, 5th session (April 8, 1886 - June 21, 1886)',
        '5th legislature, 4th session (March 5, 1885 - May 9, 1885)',
        '5th legislature, 3rd session (March 27, 1884 - June 10, 1884)',
        '5th legislature, 2nd session (January 18, 1883 - March 30, 1883)',
        '5th legislature, 1st session (March 8, 1882 - May 27, 1882)',
        '4th legislature, 4th session (April 28, 1881 - June 30, 1881)',
        '4th legislature, 3rd session (June 28, 1880 - July 24, 1880)',
        '4th legislature, 2nd session (June 19, 1879 - October 31, 1879)',
        '4th legislature, 1st session (June 4, 1878 - July 20, 1878)',
        '3rd legislature, 3rd session (December 19, 1877 - March 9, 1878)',
        '3rd legislature, 2nd session (November 10, 1876 - December 28, 1876)',
        '3rd legislature, 1st session (November 4, 1875 - December 24, 1875)',
        '2nd legislature, 4th session (December 3, 1874 - February 23, 1875)',
        '2nd legislature, 3rd session (December 4, 1873 - January 28, 1874)',
        '2nd legislature, 2nd session (November 7, 1872 - December 24, 1872)',
        '2nd legislature, 1st session (November 7, 1871 - December 23, 1871)',
        '1st legislature, 4th session (November 3, 1870 - December 24, 1870)',
        '1st legislature, 3rd session (November 23, 1869 - February 1, 1870)',
        '1st legislature, 2nd session (January 20, 1869 - April 5, 1869)',
        '1st legislature, 1st session (December 27, 1867 - February 24, 1868)']
)


def session_list():
    from billy.scrape.utils import url_xpath
    return url_xpath('http://www.assnat.qc.ca/en/travaux-parlementaires/projets-loi/projets-loi-40-1.html',
                     '//select[@name="ctl00$ColCentre$ContenuColonneGauche$ddlChoixSession"]/option/text()')

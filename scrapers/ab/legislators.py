import lxml.html

from billy.scrape.legislators import LegislatorScraper, Legislator


class ABLegislatorScraper(LegislatorScraper):
    jurisdiction = 'ab'

    def scrape(self, term, chambers):

        url = ('http://www.assembly.ab.ca/net/index.aspx?'
               'p=mla_report&memPhoto=True&alphaboth=True'
               '&alphaindex=True&build=y&caucus=All&conoffice=True'
               '&legoffice=True&mememail=True')
        doc = lxml.html.fromstring(self.urlopen(url))
        doc.make_links_absolute(url)

        parties = {
            '(PC)': 'Progressive Conservative',
            '(W)': 'Wildrose',
            '(AL)': 'Alberta Liberal',
            '(ND)': 'New Democrat'
            }

        row_xpath = '//table[@id="_ctl0_tblReport"]/descendant::tr'
        for row in doc.xpath(row_xpath)[1:]:
            data = {}
            td1, td2, td3 = row
            data['photo_url'] = td1.xpath('img/@src').pop()
            legislator_url = td1.xpath('a/@href')[0]
            data['url'] = legislator_url
            data['email'] = td3.xpath('a/@href')[0][7:]
            full_name = td1.xpath('a/b/text()').pop()
            data['party'] = parties[td1[2].tail.strip()]
            district = td1[3].tail.strip()
            leg = Legislator(term, 'lower', district, full_name, **data)

            type_dict = {
                'Legislature Office': 'capitol',
                'Constituency Office': 'district',
                }
            for office_type, column in zip(type_dict.items(), row[2:]):
                office = {}
                lines = reversed(list(column.itertext()))
                for line in lines:
                    for number_type in ['phone', 'fax']:
                        if number_type in line.lower():
                            _, number = line.split(':', 1)
                            office[number_type] = number
                    if 'Canada' in line:
                        break
                lines = list(lines)[::-1]
                office['address'] = '\n'.join(lines)
                if lines:
                    office_name = lines[0]
                    office_type = type_dict.get(office_name, 'district')
                    leg.add_office(office_type, office_name, **office)

            leg.add_source(legislator_url, page="legislator detail page")
            leg.add_source(url, page="legislator list page")
            # self.scrape_bio(leg, legislator_url)
            self.save_legislator(leg)

    def scrape_bio(self, legislator, url):
        doc = lxml.html.fromstring(self.urlopen(url))
        doc.make_links_absolute(url)

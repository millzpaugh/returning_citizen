from bs4 import BeautifulSoup
import re
import HTMLParser
import codecs
import glob
from os.path import join, dirname, realpath


def scraper(html_doc):
    # geolocator = Nominatim(country_bias="USA")
    soup = BeautifulSoup(html_doc)
    agency = soup.find(id="FacilityNameTextBox")['value']
    entry = {}
    final = {}
    classes = {}

    item = soup.find(id='FormView2')
    address = item.find(id='FormView2_AddressLabel').get_text()
    phone = item.find(id='FormView2_Resource_PhoneNoLabel').get_text()[9:23]
    fax = item.find(id='FormView2_Resource_PhoneNoLabel').get_text()[30:]
    website = item.find(id='FormView2_Resource_WebsiteLabel').get_text()
    hours = item.find(id='FormView2_Hours_Of_ServicesLabel').get_text()
    description = item.find(id='FormView2_Resource_DescriptionLabel').get_text()

    #split these on commas
    parser = HTMLParser.HTMLParser()
    html_doc = parser.unescape(html_doc)
    lines = re.findall('<span id="FormView2_HTML_CodeLabel">(.+?.)</span>',html_doc)
    if lines:
        things = re.split("<br \> ",lines[0])
        for thing in things:
            subfields = thing.split('<b>')[1:]
            for s in subfields:
                subfield = s.split('</b>')
                name = subfield[0][0:-3]
                things = subfield[1].rstrip('<br \>').split(',')
                things = map(unicode.strip, things)
                classes[name] = things
    else:
        classes = {'Category': '',
                   'Services': '',
                   'Program': '',
                   'Population': ''}

    # for field in item.find(id = 'FormView2_Special_Lng_ServiceLabel'):
    language = item.find(id='FormView2_Special_Lng_ServiceLabel').get_text()[26:].split(', ')
    eligibility = item.find(id='FormView2_Eligibility_CriteriaLabel').get_text()[22:]
    docs = item.find(id='FormView2_Documentation_NeededLabel').get_text()[22:]
    wheelchair = item.find(id='FormView2_Wheel_Chair_AccessibleLabel').get_text()[23:]

    entry = {'Documentation Needed':docs, 'Eligibility': eligibility, 'Language': language, 'Wheelchair Access': wheelchair, 'Address': address, 'Phone': phone, 'Fax': fax, 'Website': website, 'Hours': hours, 'Description' : description}
    final[agency] = dict(entry.items() + classes.items())
    return final


def org_from_filename(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        html_doc = f.read()
    return scraper(html_doc)


def reader_all():
    current_dir = dirname(realpath(__file__))
    filenames = glob.glob(current_dir + '/' + 'html/*')
    result = []
    for index, filename in enumerate(filenames):
        print index, filename
        result.append(org_from_filename(filename))
    return result

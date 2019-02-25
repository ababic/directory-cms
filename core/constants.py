from django.conf import settings

from directory_constants.constants import cms

APP_URLS = {
    cms.FIND_A_SUPPLIER: settings.APP_URL_FIND_A_SUPPLIER,
    cms.EXPORT_READINESS: settings.APP_URL_EXPORT_READINESS,
    cms.INVEST: settings.APP_URL_INVEST,
    cms.COMPONENTS: settings.APP_URL_COMPONENTS,
    cms.GREAT_INTERNATIONAL: settings.APP_URL_GREAT_INTERNATIONAL
}


COMPANY_SECTOR_CHOISES = (
    ('0', 'Advanced Manufacturing'),
    ('1', 'Aerospace'),
    ('2', 'Agri-Tech'),
    ('3', 'Aid Funded Business'),
    ('4', 'Airports'),
    ('5', 'Automotive'),
    ('6', 'Biotechnology and Pharmaceuticals'),
    ('7', 'Business (and Consumer) Services'),
    ('8', 'Capital Investment'),
    ('9', 'Clothing, Footwear and Fashion'),
    ('10', 'Communications'),
    ('12', 'Construction'),
    ('13', 'Creative and Media'),
    ('14', 'Defence (DSO)'),
    ('15', 'Education and Training'),
    ('16', 'Electronics and IT Hardware'),
    ('17', 'Energy'),
    ('18', 'Environment'),
    ('19', 'Financial Services (including Professional Services)'),
    ('20', 'Food and Drink'),
    ('21', 'Giftware, Jewellery and Tableware'),
    ('22', 'Global Sports'),
    ('23', 'Healthcare and Medical'),
    ('24', 'Household Goods, Furniture and Furnishings'),
    ('25', 'Infrastructure (Investment Only)'),
    ('26', 'Leisure and Tourism'),
    ('27', 'Life Sciences'),
    ('28', 'Marine'),
    ('29', 'Manufacturing'),
    ('30', 'Mass Transport'),
    ('31', 'Mining'),
    ('32', 'Nuclear'),
    ('33', 'Oil and Gas'),
    ('34', 'Ports and Logistics'),
    ('35', 'Power'),
    ('36', 'Railways'),
    ('37', 'Renewables'),
    ('38', 'Retail'),
    ('39', 'Security'),
    ('40', 'Software and Computer Services'),
    ('41', 'Space'),
    ('42', 'Technology'),
    ('43', 'Textiles, Interior Textiles and Carpets'),
    ('44', 'Other (please specify):'),
)

EMPLOYEES_NUMBER_CHOISES = (
    ('0', 'Less than 10'),
    ('1', '10-50'),
    ('2', '50+'),
)

HEARD_ABOUT_CHOISES = (
    ('0', 'In the press'),
    ('1', 'International Trade Advisor'),
    ('2', 'Anothercompany'),
    ('3', 'Tradeassociation'),
    ('4', 'On great.gov.uk'),
    ('5', 'Email from DIT'),
    ('6', 'At an event'),
    ('7', 'Other (please specify):'),
)

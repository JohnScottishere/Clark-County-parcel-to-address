import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_building_address(parcel_number):
    parcel_number = parcel_number.replace('-', '')
    url = f"https://maps.clarkcountynv.gov/assessor/assessorparceldetail/parceldetail.aspx?hdninstance=pcl7&hdnparcel={parcel_number}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        address_parts = []

        for span_id in ['lblAddr1', 'lblAddr2', 'lblAddr3']:
            span = soup.find('span', id=span_id)
            if span:
                address_parts.append(span.text.strip())

        return ', '.join(address_parts)
    else:
        return "Error fetching the webpage"
    
"""
- BeautifulSoup documentation: <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>
- To run...
    - cd into the xml_processing_code directory
    - $ python3 ./processor_01.py
- Shows:
    - how an xml file can be loaded
    - how to change the text of an element
    - how the changed output can be saved to a new file
"""

import os, pprint
from bs4 import BeautifulSoup


SOURCE_XML_DIR_PATH = os.environ['XML_PROCESSING__SOURCE_XML_DIR_PATH']
OUTPUT_DIR_PATH = os.environ['XML_PROCESSING__OUTPUT_DIR_PATH']

source_caes0163_path = f'{SOURCE_XML_DIR_PATH}/caes0163.xml'
output_caes0163_path = f'{OUTPUT_DIR_PATH}/caes0163_transformed_A.xml'


with open( source_caes0163_path ) as source_file_handler:
    soup_doc = BeautifulSoup( source_file_handler, features="html.parser" )

p_tags = soup_doc.find_all( 'p' )
first_p = p_tags[0]
print( f'first_p, ``{first_p}``' )

print( f'first_p.text starts as, ``{first_p.text}``' )
print( f'first_p.string starts as, ``{first_p.string}``' )

## first_p.text = 'foo'  # can't, yields something like a can't-edit-attribute error
first_p.string = 'foo'
print( f'first_p.text is now, ``{first_p.text}``' )

with open( output_caes0163_path, 'w' ) as output_file_handler:
    output_file_handler.write( str(soup_doc) )

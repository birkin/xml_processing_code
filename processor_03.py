"""
- Shows:
    - how a specific element be accessed
    - how the code can operate solely on that specific element
"""

import os, pprint
from bs4 import BeautifulSoup


SOURCE_XML_DIR_PATH = os.environ['XML_PROCESSING__SOURCE_XML_DIR_PATH']
OUTPUT_DIR_PATH = os.environ['XML_PROCESSING__OUTPUT_DIR_PATH']

source_caes0163_path = f'{SOURCE_XML_DIR_PATH}/caes0163.xml'
output_caes0163_path = f'{OUTPUT_DIR_PATH}/caes0163_transformed_C.xml'


with open( source_caes0163_path ) as source_file_handler:
    soup_doc = BeautifulSoup( source_file_handler, features="html.parser" )

# transcription_element = soup_doc.find_all( corresp="#caes0163.translation" )[0]
transcription_element = soup_doc.find_all( subtype="transcription" )[0]
print( f'transcription_element, ``{transcription_element}``' )

transcription_element_paragraph = transcription_element.p
print( f'transcription_element_paragraph, ``{transcription_element_paragraph}``' )

# with open( output_caes0163_path, 'w' ) as output_file_handler:
#     output_file_handler.write( str(soup_doc) )

"""
- Shows:
    - how an xml file can be loaded
    - how all elements of a certain type can be accessed
    - how the text of each element can be changed
    - how the changed output can be saved to a new file
- NOTE:
    - the new <w> tags are _not_ saved properly, instead, they're encoded
    - super hack I shouldn't even mention: do a whole-file string-replace before the save
        - downside -- it could replace any legitimate `&lt;` and `&gt;` strings that the file may contain.
    - better: <https://www.crummy.com/software/BeautifulSoup/bs4/doc/#insert> -- create the 'w'tags, populate them, and add each one to the p_tag.
    - another todo... perhaps check to see if the word begins with the character '<' -- and if so, do not enclose it in a <w> tag (but remember to add it as-is).
"""

import os, pprint
from bs4 import BeautifulSoup


SOURCE_XML_DIR_PATH = os.environ['XML_PROCESSING__SOURCE_XML_DIR_PATH']
OUTPUT_DIR_PATH = os.environ['XML_PROCESSING__OUTPUT_DIR_PATH']

source_caes0163_path = f'{SOURCE_XML_DIR_PATH}/caes0163.xml'
output_caes0163_path = f'{OUTPUT_DIR_PATH}/caes0163_transformed_B.xml'


with open( source_caes0163_path ) as source_file_handler:
    soup_doc = BeautifulSoup( source_file_handler, features="html.parser" )

p_tags = soup_doc.find_all( 'p' )

for p_tag in p_tags:
    p_text = p_tag.text
    assert type(p_text) == str
    print( f'p_text starts as, ``{p_text}``' )
    words = p_text.split()
    # print( f'words, ``{words}``' )
    # break
    new_words = []
    for word in words:
        new_word = f'<w>{word}</w>'
        new_words.append( new_word )
    new_string = ''.join( new_words )
    p_tag.string = new_string
    print( f'p_tag.text ends as, ``{p_tag.text}``' )

with open( output_caes0163_path, 'w' ) as output_file_handler:
    output_file_handler.write( str(soup_doc) )

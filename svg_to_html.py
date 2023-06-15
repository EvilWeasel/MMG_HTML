from lxml import etree as ET

def create_interactive_html(dot, node_mappings):
    # Get the SVG
    svg_bytes = dot.pipe(format='svg')
    svg = svg_bytes.decode('utf-8')
    
    # Remove the XML declaration
    lines = svg.split('\n')
    svg = '\n'.join([line for line in lines if not line.strip().startswith('<?xml')])
    
    # Parse the SVG
    parser = ET.XMLParser(recover=True)
    tree = ET.fromstring(svg, parser=parser)

    # Add links
    for node_id, url in node_mappings.items():
        for elem in tree.iter():
            if 'id' in elem.attrib and elem.attrib['id'] == node_id:
                for subelem in elem:
                    if subelem.tag == "{http://www.w3.org/2000/svg}text":
                        link = ET.Element('a', {'{http://www.w3.org/1999/xlink}href': url})
                        link.text = subelem.text  # set the text of the link to be the node_id
                        subelem.text = None
                        subelem.append(link)

    # Convert back to string
    svg = ET.tostring(tree, encoding='utf-8', method='xml').decode('utf-8')
    
    # Save to HTML file
    with open('interactive_graph.html', 'w', encoding='utf-8') as f:
        f.write('<html><body>' + svg + '</body></html>')

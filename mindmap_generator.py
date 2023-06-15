import graphviz
import os




def generate_mindmap(node_mappings):
    # Create a new directed graph
    dot = graphviz.Digraph('ScrumMasterCertification', comment='Mind Map for Scrum Master Certification', format='svg')

    # Add each node to the graph
    for title in node_mappings.keys():
        dot.node(title)

    # Add edges between every pair of nodes
    # This will create a fully connected graph
    titles = list(node_mappings.keys())
    for i in range(len(titles)):
        for j in range(i+1, len(titles)):
            dot.edge(titles[i], titles[j])
    
    return dot


def main():
    # Example data
    node_mappings = {
        r'Datentypen (für Nicht-Programmierer)': r'C:\Users\twehrle\source\personal_projects\Mind-Map-Generator\Learning-Paths\Datentypen\Datentypen (für Nicht-Programmierer) 4b8ea9da4f1544852b3f13e85d90094ee.html'
    }

    # Generate the mind map
    dot = generate_mindmap(node_mappings)

    # Render the graph to an SVG file
    # This will create a file named 'ScrumMasterCertification.gv.svg' in the current directory
    dot.render()

    
if __name__ == '__main__':
    main()
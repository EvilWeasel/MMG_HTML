from scraping_tool import generate_node_mappings
from svg_to_html import create_interactive_html
from mindmap_generator import generate_mindmap


def main():
    node_mappings = generate_node_mappings()

    # Ausgabe der Daten
    for title, filepath in node_mappings.items():
        print('Knotenname:', title)
        print('Pfad zur Datei:', filepath)
    
    dot = generate_mindmap(node_mappings)

    # render dot as html
    #dot.render('test-output/round-table.gv', view=True)

    create_interactive_html(dot, node_mappings)

if __name__ == "__main__":
    main()

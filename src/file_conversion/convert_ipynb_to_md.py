
from nbconvert import MarkdownExporter
from nbformat import reads


def notebook_to_markdown(notebook_path, output_path, exclude_outputs=False):
    """Convertit un notebook Jupyter en Markdown avec option pour exclure les sorties des cellules."""
    exporter = MarkdownExporter()

    # Ouvre et charge le fichier notebook
    with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = notebook_file.read()
        notebook_json = reads(notebook_content, as_version=4)  # Convertit en objet notebook

    # Supprimer les sorties des cellules
    if exclude_outputs:
        for cell in notebook_json['cells']:
            if cell.get('cell_type') == 'code':
                cell['outputs'] = []  # Vide les résultats
                cell['execution_count'] = None  # Réinitialise le compteur

    # Convertit en Markdown
    body, resources = exporter.from_notebook_node(notebook_json)

    # Sauvegarde le résultat
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(body)

    print(f"Le notebook a été converti en Markdown : {output_path}")


if __name__=='__main__':

    notebook_path = 'C://users/rapha/PycharmProjects/1_OC_IA/8_semantic-segmentation/src/notebooks/1_exploration/1_1_explore_data.ipynb'  # Remplacez par le chemin de votre notebook
    output_path = '../results/output.md'  # Chemin de sortie du fichier Markdown

    notebook_to_markdown(notebook_path, output_path, exclude_outputs=True)
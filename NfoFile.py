from lxml import etree as et


class NfoFile:

    def __init__(self, f, data):
        self.f = '{}.nfo'.format(f)
        self.data = data

    def gen_nfo(self):
        root = et.Element('movie')

        title = et.SubElement(root, 'title')
        title.text = self.data['title']

        year = et.SubElement(root, 'year')
        year.text = self.data['year']

        outline = et.SubElement(root, 'outline')
        outline.text = self.data['outline']

        plot = et.SubElement(root, 'plot')
        plot.text = self.data['plot']

        tagline = et.SubElement(root, 'tagline')
        tagline.text = self.data['tagline']

        runtime = et.SubElement(root, 'runtime')
        runtime.text = self.data['runtime']

        premiered = et.SubElement(root, 'premiered')
        premiered.text = self.data['premiered']

        genres = self.data['genre']
        for g in genres:
            genre = et.SubElement(root, 'genre')
            genre.text = g

        studio = et.SubElement(root, 'studio')
        studio.text = self.data['studio']

        set = et.SubElement(root, 'set')
        set.text = self.data['set']

        actors = self.data['actor']
        for a in actors:
            actor = et.SubElement(root, 'actor')
            name = et.SubElement(actor, 'name')
            name.text = a['name']

        tree = et.ElementTree(root)
        tree.write(self.f, pretty_print=True, xml_declaration=True)

    def generate(self):
        self.gen_nfo()

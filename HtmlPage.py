class HtmlPage:

    def __init__(self, f):
        self.f = open('{}.html'.format(f), 'w')

    def gen_html(self):
        self.f.write('<html>\n')
        self.f.write('<head>\n')
        self.f.write('{}{}{}'.format('<title>', 'Title', '</title>\n'))
        self.f.write('</head>\n')
        self.f.write('<body>\n')
        self.f.write('</body>\n')
        self.f.write('</html>\n')

    def generate(self):
        self.gen_html()

from weasyprint import HTML

if __name__ == '__main__':
    HTML('http://weasyprint.org/').write_pdf('weasyprint-website.pdf')

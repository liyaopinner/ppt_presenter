from pdf2image import convert_from_path, convert_from_bytes

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import tempfile

# with tempfile.TemporaryDirectory() as path:
images_from_path = convert_from_path('E:/test.pptx.pdf', 500)
for i, page in enumerate(images_from_path):
    page.save('{}.jpg'.format(i), 'JPEG')
a= 1
import pdfplumber


def read_pdf():
    data = ''
    with pdfplumber.open('pmfl.pdf') as pdf:
        for page in pdf.pages:
            old_data = page.extract_text()
            data = data + old_data

        # print('----分页分隔-----')
    # question=re.findall('[\.](.+?)[？]',data)

    with open('pmfl.docx', 'w') as a:
        a.write(data)
        a.close()

read_pdf()
import StringIO
output = StringIO.StringIO()
descr_tbl[descr_tbl['count']>0].to_html(output, float_format=lambda x: '%12.4f'%x)
##

with open(jp('www', 'desciption.html'), 'w') as out:
    out.write("""
    <html>
    <head>
    <style>
    table {border: 1px gray;}
    td {padding: 1em 0.3em; text-align: right;}
    </style>
    </head>
    <body>
    """)
    out.write(output.getvalue())
    out.write("""
    </body>
    </html>
    """)
output.close()



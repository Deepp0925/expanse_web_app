def plotMyTable(headerValues, cellValues, outputFile):
    import plotly.graph_objects as go

    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'

    fig = go.Figure(data=[go.Table(
        header=dict(values=headerValues,
#    values=['<b>EXPENSES</b>','<b>Q1</b>','<b>Q2</b>','<b>Q3</b>','<b>Q4</b>'],
        line_color='darkslategray',
        fill_color=headerColor,
        align=['left','center'],
        font=dict(color='white', size=14)
      ),
    cells=dict(values=cellValues,
    #values=[
#      ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
#      [1200000, 20000, 80000, 2000, 12120000],
#      [1300000, 20000, 70000, 2000, 130902000],
#      [1300000, 20000, 120000, 2000, 131222000],
#      [1400000, 20000, 90000, 2000, 14102000]],
        line_color='darkslategray',
        # 2-D list of colors for alternating rows
        fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
        align = ['left', 'center'],
        font = dict(color = 'darkslategray', size = 11)
    ))
])

#fig.show()
# To save the image in a file use the following
    #fig.write_image("./myTable00.png")
    #fig.write_image(outputFile)
# You need to install kaliedo with
# pip install -U kaleido
# Image formats include raster formats (PNG, JPEG, and WebP) and
# vector formats (pdf, svg, and eps)
# To save the table in an html file use
    #fig.write_html("./myTable00.html")
    if outputFile.lower().endswith(('.png', '.jpeg', '.webp', '.pdf', '.svg', '.eps')):
        fig.write_image(outputFile)
    elif outputFile.endswith('.html'):    
        fig.write_html(outputFile)
    else:
        print("Error in file name and/or format")


headerValues=['<b>EXPENSES</b>','<b>Q1</b>','<b>Q2</b>','<b>Q3</b>','<b>Q4</b>'    ]
cellValues=[
      ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
      [1200000, 20000, 80000, 2000, 12120000],
      [1300000, 20000, 70000, 2000, 130902000],
      [1300000, 20000, 120000, 2000, 131222000],
      [1400000, 20000, 90000, 2000, 14102000]]

plotMyTable(headerValues, cellValues, "jaja.html")

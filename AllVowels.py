import os


def figures_to_html(figs, filename="AllVowelTrajectory.html"):
    with open(filename, 'w', encoding="utf-8") as dashboard:
        dashboard.write("<html><head></head><body>" + "\n")
        for fig in figs:
            inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
            dashboard.write(inner_html)
        dashboard.write("</body></html>" + "\n")
def plotTrajectories(folderNames, vowels, language):  # Formant trajectory plot
    import os
    import requests
    import pandas as pd
    import urllib.request
    import parselmouth
    import tgt
    import plotly.subplots as sp
    import plotly.express as px
    import plotly.graph_objects as go
    import numpy as np
    originpath = os.getcwd()

    modelnum = len(folderNames)

    figs =[]
    for index, folder in enumerate(folderNames):
        data = []

        print(index)
        print(folder)
        path = os.getcwd() + "\\" + folder
        os.chdir(path)
        print(os.getcwd())
        namelist = os.listdir(path)
        fileNames = []
        for name in namelist:
            unique = name.split(".")[0]
            if unique not in fileNames:
                fileNames.append(unique)
        for fileName in fileNames:
            # Call WebMaus Basic Api to generate TextGrids.
            print("  " + "└── " + fileName)
            headers = {
                'content-type': 'multipart/form-data',
            }

            files = {
                'SIGNAL': (fileName + '.wav', open(fileName + '.wav', 'rb')),
                'LANGUAGE': (None, language),
                'OUTFORMAT': (None, 'TextGrid'),
                'TEXT': (fileName + '.txt', open(fileName + '.txt', 'rb')),
            }
            result = requests.post('https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/runMAUSBasic',
                                   files=files)
            decodeResponse = result.content.decode("utf-8")
            xmlSplit = decodeResponse.split("<downloadLink>")
            downURL = xmlSplit[1].split("</downloadLink>")
            downURL = downURL[0]
            urllib.request.urlretrieve(downURL, fileName + ".TextGrid")
            os.chdir(originpath)

    os.chdir(originpath)

    for index,folder in enumerate(folderNames):
        data = []

        print(index)
        print(folder)
        path = os.getcwd() +"\\"+ folder
        os.chdir(path)
        print(os.getcwd())
        namelist = os.listdir(path)
        fileNames =[]

        for name in namelist:
            unique = name.split(".")[0]
            if unique not in fileNames:
                fileNames.append(unique)


        for mode in range(0,3):
            vl = []
            f1l = []
            f2l = []

            for fileName in fileNames:

                # Use parselmouth + Textgrid tools to obtain formant information
                ps = parselmouth.Sound(fileName + ".wav")
                formants = ps.to_formant_burg()
                tg = tgt.io.read_textgrid(fileName + '.TextGrid')
                mau = tg.get_tier_by_name("MAU")
                mauObjs = mau.intervals
                for i in vowels:
                    for j in mauObjs:
                        if i in j.text:
                            start = j.start_time
                            end = j.end_time
                            t0 = (5*start + end) / 6
                            mid = (start + end) / 2
                            t2 = (start + 5*end) / 6

                            if mode is 0:
                                f1 = formants.get_value_at_time(1, t0, "HERTZ")
                                f2 = formants.get_value_at_time(2, t0, "HERTZ")
                            elif mode is 1:
                                f1 = formants.get_value_at_time(1, mid, "HERTZ")
                                f2 = formants.get_value_at_time(2, mid, "HERTZ")
                            elif mode is 2:
                                f1 = formants.get_value_at_time(1, t2, "HERTZ")
                                f2 = formants.get_value_at_time(2, t2, "HERTZ")
                            vl.append(j.text)
                            f1l.append(f1)
                            f2l.append(f2)

            # Store formant values in dataframe.
            d = {'vowel': vl, 'f1': f1l, 'f2': f2l}
            df = pd.DataFrame(d)
            f1Centroid = df.groupby('vowel')['f1'].apply(lambda x: np.mean(x.tolist(), axis=0))
            f2Centroid = df.groupby('vowel')['f2'].apply(lambda x: np.mean(x.tolist(), axis=0))
            d = {'f1': f1Centroid, 'f2': f2Centroid, 'steps': mode, 'point': mode}
            df2 = pd.DataFrame(d)
            data.append(df2)  # Append formant values for current training step
        os.chdir(originpath)
        full = pd.concat(data)  # Formant trajectory plot
        df = full
        fig = px.line(full, x="f2", y="f1", color=df.index, width=500, height=450, line_shape='spline', text='steps',
                      line_group=df.index, title=folder)

        fig.update_layout(
            font_family="Helvetica",
            font_color="black",
            font={"size": 20}
        )
        fig.update_xaxes(
            tickangle=90,
            title_text="F2 (Hz)",
            title_font={"size": 20},
            title_standoff=20
        )
        fig.update_yaxes(
            tickangle=90,
            title_text="F1 (Hz)",
            title_font={"size": 20},
            title_standoff=20
        )
        fig.update_layout({
            'plot_bgcolor': '#ffffff',
            'paper_bgcolor': '#ffffff',
            'yaxis_gridcolor': '#e5e5ea',
            'xaxis_gridcolor': '#e5e5ea'
        })
        fig.update_traces(textposition='top center')
        fig.update_yaxes(autorange="reversed")
        fig.update_xaxes(autorange="reversed")
        fig.update_xaxes(tickangle=0)
        fig.update_yaxes(tickangle=0)
        figs.append(fig)
    os.chdir(originpath)
    figures_to_html(figs)

    return df

def main():
    path = "Samples"
    os.chdir(path)
    plotTrajectories(['20k', '25k', "30k"], ["{", "}:", "3:", "6", "6:", "e", "I", "i:", "O", "o:", "U"], "eng-NZ")

if __name__ == "__main__":
    main()
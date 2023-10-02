import tools
import os


def main():
    path = "Samples"
    os.chdir(path)

    print(path)

    #df, fig = tools.plotFormants( ['download_1'],["{", "}:","3:","6","6:","e","I", "i:", "O", "o:", "U" ], "eng-NZ", True)

    #df, fig = tools.plotPath( ['20k', '25k', "30k"],["{", "}:","3:","6","6:","e","I", "i:", "O", "o:", "U" ], "eng-NZ")

    tools.plotTrajectories(['download_1'], ["{", "}:", "3:", "6", "6:", "e", "I", "i:", "O", "o:", "U"], "eng-NZ")

if __name__ == "__main__":
    main()
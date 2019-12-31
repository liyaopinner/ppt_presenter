import sys
import os

try:
    from comtypes import client
except:
    print("Install comtypes from http://sourceforge.net/projects/comtypes/")
    sys.exit(-1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python ppt2png.py [file]")
        sys.exit(-1)

    f = os.path.abspath(sys.argv[1])
    # f = "D:/ppt建站/ppt_presenter/test.pptx"
    if not os.path.exists(f):
        print("No such file!")
        sys.exit(-1)

    powerpoint = client.CreateObject('Powerpoint.Application')
    powerpoint.Presentations.Open(f)
    powerpoint.ActivePresentation.Export(f, 'PNG')
    powerpoint.ActivePresentation.Close()
    powerpoint.Quit()

    print("Converting successfully finished.")

def onBtnClicked(callBack):
    print("first Button clicked")
    callBack()


def showBtnClicked():
    print("second Button clicked ")


onBtnClicked(showBtnClicked)


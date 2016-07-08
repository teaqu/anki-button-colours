# Author: Calumks <calumks@live.com>
# Get reviewer class
from aqt.reviewer import Reviewer

# Replace _answerButtonList method
def answerButtonList(self):
    l = ((1, "<font color='red'>" + _("Again") + "</font>"),)
    cnt = self.mw.col.sched.answerButtons(self.card)
    if cnt == 2:
        return l + ((2, "<font color='green'>" + _("Good") + "</font>"),)
    elif cnt == 3:
        return l + ((2, "<font color='green'>" + _("Good") + "</font>"), (3, _("Easy")))
    else:
        return l + ((2, _("Hard")), (3, "<font color='green'>" + _("Good") + "</font>"), (4, _("Easy")))

Reviewer._answerButtonList = answerButtonList


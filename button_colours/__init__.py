# Author: C9HDN
# Get reviewer class
from aqt.reviewer import Reviewer
from aqt import mw

# Replace _answerButtonList method
def answerButtonList(self):
    config = mw.addonManager.getConfig(__name__)
    l = ((1, "<font color='"+config['Again']+"'>" + _("Again") + "</font>"),)
    cnt = self.mw.col.sched.answerButtons(self.card)
    if cnt == 2:
        return l + ((2, "<font color='"+config['Good (2 Answers)']+"'>" + _("Good") + "</font>"),)
    elif cnt == 3:
        return l + ((2, "<font color='"+config['Good (3 Answers)']+"'>" + _("Good") + "</font>"), (3, "<font color='"+config['Easy (3 Answers)']+"'>" + _("Easy") + "</font>"))
    else:
        return l + ((2, "<font color='"+config['Hard']+"'>" + _("Hard") + "</font>"), (3, "<font color='"+config['Good (4 Answers)']+"'>" + _("Good") + "</font>"), (4, "<font color='"+config['Easy (4 Answers)']+"'>" + _("Easy") + "</font>"))

Reviewer._answerButtonList = answerButtonList
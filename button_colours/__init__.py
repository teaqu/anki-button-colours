from aqt import mw
from aqt import gui_hooks

def buttonColours(buttons_tuple, reviewer, card):
    config = mw.addonManager.getConfig(__name__)
    button_count = mw.col.sched.answerButtons(card)
    colours = config['colours'].get(str(button_count) + ' answers')

    # if coulours found in config
    if colours:

        # Create new list of coloured buttons
        coloured_buttons = []
        for button in buttons_tuple:
            text = button[1]

            # See if colour exists else paint black
            try:
                colour = colours[button[0] - 1]
            except IndexError:
                colour = "black"

            # Add colour to button
            font = "<font color='{}'>{}</font>".format(colour, text)

            coloured_buttons.append((button[0], font))

        return tuple(coloured_buttons)
    else:
        return buttons_tuple

gui_hooks.reviewer_will_init_answer_buttons.append(buttonColours)
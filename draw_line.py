"""
File: draw_line.py
Name:Cheryl
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE=10  # constant
window=GWindow()
first_click_x = None
first_click_y=None
second_click_x=None
second_click_y=None
click_count=0


def main():
	"""
	Click your mouse at the locations where you want to
	start and end the line on the pop-up window.
	"""
	onmouseclicked(draw_line)

def draw_line(event):
	global first_click_x,first_click_y,click_count,second_click_x,second_click_y

	click_count+=1

	if click_count%2 == 1:
		# Store the first click position
		first_click_x = event.x
		first_click_y = event.y
	else:
		# Store the second click position
		second_click_x = event.x
		second_click_y = event.y

	mark = GOval(SIZE, SIZE, x=first_click_x - SIZE / 2, y=first_click_y - SIZE / 2)
	remove_mark = window.get_object_at(first_click_x,first_click_y)

	if click_count%2 == 1:  # odd click
		window.add(mark)
	else:
		# Draw a line between odd and even click
		pen_stroke = GLine(first_click_x, first_click_y, second_click_x, second_click_y)
		window.add(pen_stroke)
		window.remove(remove_mark)


if __name__ == "__main__":
	main()

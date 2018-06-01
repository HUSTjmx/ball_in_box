import math

import ball_in_box.ballinbox as bb
import ball_in_box.validate as val


def area_sum(circles):
	area = 0.0
	for circle in circles:
		area += circle[2] ** 2 * math.pi

	return area




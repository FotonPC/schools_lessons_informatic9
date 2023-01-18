"""My C++ Code
пересечение 2 прямых заданых точками
Vector2 intersection_2_lines(Vector2 v1, Vector2 v2, Vector2 v3, Vector2 v4) {
	double x1, y1, x2, y2, k1, b1, k2, b2, x, y;
	Vector2 res;
	//// Line 1 <<<
	x1 = v1.x + 0.00000001;
	x2 = v2.x - 0.00000001;
	y1 = v1.y + 0.00000001;
	y2 = v2.y - 0.00000001;
	if ((x2 - x1) == 0) {
		cout << "math error" << endl;
		res.x = 0;
		res.y = 0;
		return res;
	}
	k1 = (y2-y1) / (x2-x1);
	if ((x2 - x1) == 0) {
		cout << "math error" << endl;
		res.x = 0;
		res.y = 0;
		return res;
	}
	b1 = (y1 * (x2 - x1) - x1 * (y2 - y1)) / (x2 - x1);
	//// Line 1 >>>
	//// Line 2 <<<
	x1 = v3.x + 0.00000001;
	x2 = v4.x - 0.00000001;
	y1 = v3.y + 0.00000001;
	y2 = v4.y - 0.00000001;
	if ((x2 - x1) == 0) {
		cout << "math error" << endl;
		res.x = 0;
		res.y = 0;
		return res;
	}
	k2 = (y2 - y1) / (x2 - x1);
	if ((x2 - x1) == 0) {
		cout << "math error" << endl;
		res.x = 0;
		res.y = 0;
		return res;
	}
	b2 = (y1 * (x2 - x1) - x1 * (y2 - y1)) / (x2 - x1);
	//// Line 2 >>>
	if ((k1 - k2) == 0) {
		cout << "math error" << endl;
		res.x = 0;
		res.y = 0;
		return res;
	}
	x = (b2 - b1) / (k1 - k2);
	y = k2 * x + b2;
	res.x = x;
	res.y = y;
	return res;

}
# проверка на коллизию 2 отрезков
bool is_collision(double x3, double y3, double x4, double y4) {
		double dx0 = x2 - x1;
		double dx1 = x4 - x3;
		double dy0 = y2 - y1;
		double dy1 = y4 - y3;
		double p0 = dy1 * (x4 - x1) - dx1 * (y4 - y1);
		double p1 = dy1 * (x4 - x2) - dx1 * (y4 - y2);
		double p2 = dy0 * (x2 - x3) - dx0 * (y2 - y3);
		double p3 = dy0 * (x2 - x4) - dx0 * (y2 - y4);
		return (p0 * p1 <= 0) && (p2 * p3 <= 0);
	}
"""


import numpy as np
import numba as nb
import math
import random

@nb.njit(fastmath=True, cache=True)
def is_collision(x1: float, y1: float,
                 x2: float, y2: float,
                 x3: float, y3: float,
                 x4: float, y4: float) -> bool:
    dx0: float = x2 - x1;
    dx1: float = x4 - x3;
    dy0: float = y2 - y1;
    dy1: float = y4 - y3;
    p0: float = dy1 * (x4 - x1) - dx1 * (y4 - y1);
    p1: float = dy1 * (x4 - x2) - dx1 * (y4 - y2);
    p2: float = dy0 * (x2 - x3) - dx0 * (y2 - y3);
    p3: float = dy0 * (x2 - x4) - dx0 * (y2 - y4);
    return (p0 * p1 <= 0) and (p2 * p3 <= 0);





class Polygon:
    def __init__(self, vertexes=np.array([[0, 0], [0, 0], [0, 0]]), point_out=np.array([0, 0])):
        self.vertexes = vertexes
        self.point_out=point_out
    def is_point_in(self, point=np.array([0, 0])):
        i = len(self.vertexes)-1
        ints = 0
        while i > -2:
            if is_collision(point[0], point[1], self.point_out[0], self.point_out[1], self.vertexes[i][0], self.vertexes[i][1], self.vertexes[i-1][0], self.vertexes[i-1][1]):
                ints += 1
        return ints % 2 == 1

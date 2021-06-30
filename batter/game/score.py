#!/usr/bin/env python3
from game.point import Point
from game.actor import Actor

class Score(Actor):
	
	def __init__(self):
		super().__init__()
		
		self._points = 0
		self.set_text(f"Score: {self._points}")
		self.set_position(Point(3,0))
		
	def add_points(self, points):
		self._points += points
		self.set_text(f"Score: {self._points}")
class Point(object):
  def __init__(self, x, y):
    self.__x = x
    self.__y = y
  @property
  def x(self):
    return self.__x
  @property
  def y(self):
    return self.__y
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)
  def __iadd__(self, other):
    self.__x += other.x
    self.__y += other.y
    return self
  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)
  def __isub__(self, other):
    self.__x -= other.x
    self.__y -= other.y
    return self
  def __mul__(self, other):
    return Point(self.x * other, self.y * other)
  def __imul__(self, other):
    self.__x *= other
    self.__y *= other
    return self
  def __truediv__(self, other):
    return Point(self.x / other, self.y / other)
  def __itruediv__(self, other):
    self.__x /= other
    self.__y /= other
  def __floordiv__(self, other):
    return Point(self.x // other, self.y // other)
  def __ifloordiv__(self, other):
    self.__x // other.x
    self.__y // other.y
    return self

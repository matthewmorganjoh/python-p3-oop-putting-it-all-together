class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self._color = None  # Initialize color as None

    def get_size(self):
        try:
            return self._size
        except AttributeError:
            return
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    color = property(get_color, set_color)
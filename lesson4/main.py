from box import Box
from colorbox import ColorBox
box = Box(10,5)
print(f"Base box:{box.__str__()}")
cBox = ColorBox(box.Width, box.Height, "Greem")
print(f"Derived class:")
from src.eternity2_project.eternity2.Itinerary.itinerary import Itinerary
from src.eternity2_project.eternity2.Itinerary.path import Path

itinerary: Itinerary = Itinerary.create_with_first_5_pieces()
itinerary.print()

path: Path = itinerary.obtain_deepest_path()

# print(path)

path.generate_calculated_possibilities()

path: Path = itinerary.obtain_deepest_path()

# print(path)


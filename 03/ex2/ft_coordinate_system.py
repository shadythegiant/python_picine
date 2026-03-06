import sys
import math


def calc_distance(p1, p2) -> float:
    return math.sqrt(
        (p2[0] - p1[0])**2 +
        (p2[1] - p1[1])**2 +
        (p2[2] - p1[2])**2
    )


def main() -> None:
    if len(sys.argv) < 2:
        print(
            f"Error: <InvalidUsage> "
            f"Usage:{sys.argv[0].split('/')[-1]} <x,y,z>")
        return
    try:
        coord_parts = sys.argv[1].split(',')
        coords = []

        for part in coord_parts:
            coords.append(int(part))
        if len(coords) != 3:
            raise ValueError
        coords = tuple(coords)
    except ValueError as e:
        print("Error: <InvalidCoords> All Coordinates must be",
              "Numbers and in this format: <x,y,z>")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return

    current_position = (0, 0, 0)
    x1, y1, z1 = coords
    print(f"Parsing coordinates \"{x1},{y1},{z1}\"")
    print(f"Parsed Positions {coords}")
    print(f"Distance between {current_position} and {coords}:"
          f"{calc_distance(current_position, coords)}")
    player = "0rph3us"

    print("Unpacking demonstration:")
    print(f"{player} at x={x1}, y={y1}, z={z1}")
    print(f"Corrdinates : X={x1}, Y={y1}, Z={z1} ")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    main()

import json
import random
#changes
#assigning random values to random data in field_definition

class RealWorldInfo:
    def __init__(self, screen_width_p, screen_height_p):
        """
        Handles all details regarding converting real world details into renderables.
        """
        with open('field_definition.json') as field_json:
            field_data = json.load(field_json)

            for block in field_data:
                if block.get("x") == "random":
                    block["x"] = random() * field_data["Header"]["max_Width"]
                if block.get("y") == "random":
                    block["y"] = random() * field_data["Header"]["max_Height"]
                if block.get("twist") == "random":
                    block["twist"] = random.randrange(0,360)

        self.meters_to_pixels_vertical_scaling_factor = screen_height_p
        self.meters_to_pixels_horizontal_scaling_factor = screen_width_p
        self.json_val = field_data["ground"]

    def m_to_p_horizontal(self, value_m):
        return value_m * self.meters_to_pixels_horizontal_scaling_factor

    def m_to_p_vertical(self, value_m):
        return value_m * self.meters_to_pixels_vertical_scaling_factor

    def p_to_m_horizontal(self, value_p):
        return value_p / self.meters_to_pixels_horizontal_scaling_factor

    def p_to_m_vertical(self, value_p):
        return value_p / self.meters_to_pixels_vertical_scaling_factor
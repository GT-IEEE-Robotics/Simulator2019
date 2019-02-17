import json


class RealWorldInfo:
    def __init__(self, screen_width_p, screen_height_p):
        """
        Handles all details regarding converting real world details into renderables.
        """
        with open('field_definition.json') as field_json:
            field_data = json.load(field_json)

        self.meters_to_pixels_vertical_scaling_factor = screen_height_p / field_data["vertical"]
        self.meters_to_pixels_horizontal_scaling_factor = screen_width_p / field_data["horizontal"]

    def m_to_p_horizontal(self, value_m):
        return value_m * self.meters_to_pixels_horizontal_scaling_factor

    def m_to_p_vertical(self, value_m):
        return value_m * self.meters_to_pixels_vertical_scaling_factor

    def p_to_m_horizontal(self, value_p):
        return value_p / self.meters_to_pixels_horizontal_scaling_factor

    def p_to_m_vertical(self, value_p):
        return value_p / self.meters_to_pixels_vertical_scaling_factor
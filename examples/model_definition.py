import numpy as np
from pydantic import BaseModel, ConfigDict
from lume_model.base import LUMEBaseModel


class ExampleModel(LUMEBaseModel):
    def _evaluate(self, input_dict):
        output_dict = {}
        output_dict["y"] = np.max([input_dict["x1"], input_dict["x2"]])
        return output_dict

    
    def input_validation(self, input_dict: dict[str, np.ndarray]):
        """Bypass input validation because the example uses numpy arrays which
        are not yet implemented.

        Ideally this function would implement the check that all input array values
        are floats.
        """
        return input_dict

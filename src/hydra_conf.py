from omegaconf import OmegaConf
import hydra
from .experiment_definitions import ExperimentDefinitions


@hydra.main(version_base=None, config_name="config", config_path="../conf")
def dsp_main(cfg: ExperimentDefinitions | None = None) -> None:
    print(OmegaConf.to_yaml(cfg))

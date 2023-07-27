from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DS_PROJECTS",
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="DS_PROJECTS_MODE",
    # validator=Validator("MSG", "required", is_type_of=str),
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.

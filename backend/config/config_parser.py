import configparser


class ConfigurationHandler:

    def __init__(self):
        """

            - Configuration manager class, we define this as a singleton.
            - Fetch the database credentials from the config file.

        """

        self.config = configparser.ConfigParser()
        self.config.read('./backend/config/config.ini')

    def get_config_object(self):
        return self.config


configuration = ConfigurationHandler().get_config_object()

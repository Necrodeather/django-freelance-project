import configparser


class Config_Api:
    def __init__(self):
        self.path = 'data_storage/configs/config.ini'
        self.cfg = configparser.ConfigParser()
        self.cfg.read(self.path)

    async def time_zone(self):
        time_zone = self.cfg['settings']['time_zone']
        return(time_zone)
        
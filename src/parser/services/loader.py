#my imports
import parser.services.data_storage.database as database
#import data_storage.configs as configs
from core.settings import TIME_ZONE


#declaring instances of classes
db = database.DB()
cfg = TIME_ZONE
from waybackpy import WaybackMachineCDXServerAPI
from datetime import datetime , timedelta



class HistoricalSearch:
    
    def __init__(self, url, user_agent):
        
        self.url = url
        self.user_agent = user_agent
        
    def search_snapshot(self,years_ago=10, filename="snapshot.html"):
        
        """
        Busca y guarda una captura de una fecha especifica
        
        """
        
        #
        
        target_date =  datetime.now() - timedelta(days=365 * years_ago)
        year , month , day = target_date.year, target_date.month, target_date.day
        cdx_api = WaybackMachineCDXServerAPI(self.url, self.user_agent)
        snapshot = cdx_api.near(year=year, month=month, day=day)
        
        if snapshot:
            print(f'Fecha: { snapshot.timestamp}, URL: {snapshot.archive_url}')
            
        else:
            print("No se encontro captura")
            return
        
        
user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
url = "udemy.com"
hsearch = HistoricalSearch(url, user_agent)

hsearch.search_snapshot()

        





    
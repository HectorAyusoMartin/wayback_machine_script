from waybackpy import WaybackMachineCDXServerAPI
from datetime import datetime , timedelta
import requests

#TODO falta completar DocStrings. 

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
            self.downlaod_snapshot(snapshot.archive_url,filename)
        else:
            print("No se encontro captura para la fecha especificada")
            return False
                
    def downlaod_snapshot(self, archive_url , filename ):
        """
        Descarga y guarda el contenido de un snapshot en disco-
        """
        
        response = requests.get(archive_url)
        if response.status_code == 200:
            with open(filename, "w", encoding='utf8') as file:
                file.write(response.text)
            print(f'Documento guardado exitosamente en {filename}')
        
        else:
            print(f'Error al descargar el documento. Codigo de estado: {response.status_code}')

    def search_snapshots_by_extensions(self, years_ago=4, days_interval=15, extensions=None, math_type="domain"):
        """
        DocString
        """
        if extensions is None:
            extensions = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx','txt']
            
        #calcular la fecha para el periodo especificado
        today = datetime.now()
        start_period = (today - timedelta(days=365 * years_ago)).strftime("%Y%m%d")
        end_period = (today - timedelta(days=(365*years_ago) - days_interval)).strftime("%Y%m%d")
        
        cdx_api = WaybackMachineCDXServerAPI(url = self.url , user_agent=self.user_agent, start_timestamp=start_period, end_timestamp=end_period, match_type=math_type)
        
        #filtrando por extensiones con una expresion regular. Aplicamos un filtro mediante expresiones regulares
        #Para esta expresion concreta concidirian todas aquellas urls que tengan cualquier cosa y el final qde la url que sea .pdf --> (*.\\.pdf$)
        
        regex_filter = '(' +'|'.join([f".*\\.{ext}$" for ext in extensions]) + ')'
        cdx_api.filters = [f'urlkey:{regex_filter}']
        
        #Realizamos la busqueda
        
        snapshots = cdx_api.snapshots()
        for snapshot in snapshots:
            print(f'fecha: {snapshot.timestamp}, URL: {snapshot.archive_url}')
            
        
    
    
    
user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
url = "udemy.com"
hsearch = HistoricalSearch(url, user_agent)



hsearch.search_snapshot()
#hsearch.search_snapshots_by_extensions()


        





    
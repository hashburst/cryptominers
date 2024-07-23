# Esempio di implementazione di un protocollo personalizzato in Python

from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class CustomProtocolHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        # Logica per gestire la richiesta del tuo protocollo
        if parsed_url.scheme == 'tep':
            address = parsed_url.hostname
            port = parsed_url.port
            resource = query_params.get('resource', [''])[0]
            
            # Esegui l'azione desiderata in base all'URI personalizzato
            print(f"Ricevuta richiesta TEP: Address={address}, Port={port}, Resource={resource}")
            # Implementa la logica desiderata qui...

            # Invia la risposta al client
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Operazione completata con successo")

# Configura e avvia il server
port = 8080  # Sostituisci con la porta desiderata
server = HTTPServer(('localhost', port), CustomProtocolHandler)
print(f"Server in ascolto sulla porta {port}")
server.serve_forever()
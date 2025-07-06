# progetto-sicurezza
Progetto per l'esame di Sicurezza dell'informazione M
realizzato da Cavazzana Damiano (n° matricola 0001191354)

# Login passwordless

Questo progetto è stato realizzato per il corso di Sicurezza dell'Informazione M (LM), Unibo. L'obiettivo è implementare l'autenticazione passwordless, a questo scopo si usa il protocollo TLS per effettuare una mutua e sicura autenticazione tra Client e Server.

## Struttura del progetto

Tutti i componenti sono containerizzati tramite **Docker**.
```bash
progetto_sicurezza/
├── docker-compose.yml
├── client/
│   ├── Dockerfile
│   ├── ca.crt
│   ├── client.crt
│   ├── client.key
│   └── client.py
├── server/
│   ├── Dockerfile
│   ├── ca.crt
│   ├── server.crt
│   ├── server.key
│   └── server.py
```

## Esecuzione
Clonare il repository, spostarsi nella cartella e lanciare:
```bash
docker compose up --build
```

## Creazione CA e dei Certificati
I certificati x.509 sono generati tramite OpenSSL e copiati rispettivamente dentro Server e Client.
```bash
# CA key e cert
openssl genrsa -out ca.key 4096
openssl req -x509 -new -nodes -key ca.key -sha256 -days 3650 -out ca.crt -subj "/CN=MyCA"

# Server key e CSR
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -subj "/CN=server"

# Firma il certificato server con la CA
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365 -sha256

# Client key e CSR
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "/CN=client"

# Firma il certificato client con la CA
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365 -sha256
```

## Conclusione
Tramite comunicazione TLS è possibile implementare il login passwordless:
  - se c'è bisogno di credenziali
  - l'identità è stabilita tramite certificati digitali
  - si ha mutua autenticazione
  - si ha inoltre tutto il traffico cifrato

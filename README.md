# izity-rasp

Sistema de integração da Raspberry com a API central de processamento de voz. Inclui servidor para front-end da demo e um servidor que realiza a comunicação com a API em si.

## Building & Running

### Front-end da demo
```
go install
go run main.go
```

### Middleware para a API
```
pip install flask flask_cors pyaudio
python server.py
```

Agora navegue para `localhost:8080/static`, aperte o play e autentique a sua voz.

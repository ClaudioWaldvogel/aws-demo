# AWS Demo

Very simple web application to translate inputs.  
The app exposes 2 endpoints

* /ping
* /translate?text=string&src=lang&dest=lang


### Setup
Run in project root directory and add virtual env as python sdk to IntelliJ
```bash
source setupDev.rc
```

### Build and run Container
```bash
docker build -t translator:latest .
docker run -p 8081:8081 translator:latest
```
### Invoke methods

```bash
curl  curl http://localhost:8081/ping
curl  curl http://localhost:8081/translate?text=input&src=de&dest=en

```
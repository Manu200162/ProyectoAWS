# ProyectoAWS
## Integrantes:
Llubitza Linares, Benjamin Soto, Ian Terceros, Manuel Valenzuela, Rodrigo Viladegut
## Pasos para poder deployar
### Paso 1: cambiar el nombre del bucket del website en el template, y en el deployment.sh
```
 BucketName: fedex-bucket-website-1234
 aws s3 cp website s3://fedex-bucket-website-123/ --recursive
 ```
### Paso 2: cambiar el nombre del bucket donde se depositara el stack, esto en el deployment.sh
```
DEPLOYMENT_BUCKET="fedex-bucket-website-1234"
````
### Paso 3: deployar con los comandos:
```
chmod +x deployment.sh
./deployment.sh -b
./deployment.sh -p
./deployment.sh -d
./deployment.sh -w
```

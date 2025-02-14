BUILD 
    
     docker build -t demo .

RUN 

    docker run --rm -it --user root -p 8000:8000 demo

APIS
    
    - http://0.0.0.0:8000/crash-cpu

    - http://0.0.0.0:8000/dangerous-action

    - http://0.0.0.0:8000/health

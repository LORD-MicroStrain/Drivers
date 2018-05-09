import tarfile
from StringIO import StringIO

def main():
	installScript = open("install.sh.in").read()
	payloadStart = len(installScript.splitlines()) + 1
	#payloadStart = len(installScript) - 1 + len(str(len(installScript)))
	#if len(installScript) - 1 + len(str(payloadStart)) != payloadStart:
	#	payloadStart += 1
	
	print "payloadstart=%s" % payloadStart
	installScript = installScript.replace("payloadstart=0", "payloadstart=%s" % payloadStart)

	output = open("install.sh", 'wb')
	
	tarData = StringIO()
	tarFile = tarfile.open(fileobj=tarData, mode='w:bz2')
	tarFile.add("cp210x.c")
	tarFile.add("Makefile")
	tarFile.add("dkms.conf")
	tarFile.close()

	output.write(installScript)
	output.write(tarData.getvalue())
	output.close()
	
if __name__ == "__main__":
	main()

import psutil

DNF_NAME = "DNF.exe"
TARGET_NAME = []
TARGET_NAME.append("tguard.exe")
# TARGET_NAME.append('TGuardSvc.exe')

for proc in psutil.process_iter(attrs=['pid', 'name']):
    if proc.info['name'] in TARGET_NAME:
        try:
            p = psutil.Process(proc.info['pid'])
            p.kill()
            print('Kill process:', proc.info['name'])
        except Exception:
            print('Error when killing process', proc.info['name'])

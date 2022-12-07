import os
import psutil
import time
import re
    
#----------------------------------------------------------------------
def create_process_logs(log_dir):
    """
    Create a log of all the currently running processes
    """
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
 
    separator = "-" * 80
    col_format = "%7s %7s %30s %30s"
    data_format = "%7.4f %7.2f %30s %30s"
    while 1:
        procs = list(psutil.process_iter())
         
        log_path = os.path.join(log_dir, "log.txt")
        f = open(log_path, "a")
        f.write(separator + "\n")
        f.write(time.ctime() + "\n")
        f.write(col_format % ("%CPU", "%MEM", "NAME", "TIME"))
        f.write("\n")
         
        for proc in procs:
            if re.search('python', str(proc.name)):
                cpu_percent = proc.cpu_percent()
                mem_percent = proc.memory_percent()
                name = proc.name
                f.write(data_format % (cpu_percent, mem_percent, name, time.ctime()))
                f.write("\n\n")
        f.close()
        print ("Finished log update!")
        time.sleep(1)
        print ("writing new log data!")
                
if __name__ == "__main__":
    log_dir = "C:/Users/lucas/OneDrive/Documentos/GitHub/utfprds2022/Log"
    create_process_logs(log_dir)
from configobj import ConfigObj
import os
import socket

SERVICE_DIR = '/mymicroservice/'

def checkport(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return sock.connect_ex((host, port)) #response==0 if it successful, any other value if not successful

def launchsvc(svc,host,port):#todo, localhost,5001
    #Check if the service is running or not
    addr = "localhost:{}".format(port)#addr=localhost:5001
    resp = checkport(host, int(port))#localhost,5001 #resp!=0 ; resp=0
    if resp != 0:
        print("Service {} not running, starting service at port {} on host {}".format(svc, port, host))
        os.system('python3 '+ SERVICE_DIR + svc + '.py &')# python E:/todo/services/todo.py &;python E:/todo/services/users.py &
    else:
        print("Service {} running at port {} on host {}".format(svc, port, host))

def walkthrough(section,obj): #users,config
    if 'preload' in section: #users section contians a preload sub-section
        services = section['preload'].split(' ') #users[preload] it returns todo
        for service in services: #todo
            launchsvc(service, obj[service]['host'], obj[service]['port'])#launchsvc(todo,localhost, 5001) # todo is running
    launchsvc(section.name, section['host'], section['port']) #launchsvc(users, localhost,5000)

def loadDependencies():
    #Read the dependency file
    config = ConfigObj('dependencies.ini')
    #config.walk(walkthrough, obj=config)
    for section in config: #users, todo
        walkthrough(config[section], config)#iteration-1-->users,config

if __name__ == '__main__':
    loadDependencies()

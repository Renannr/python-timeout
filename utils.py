import signal
import time
from contextlib import contextmanager

class Utils(object):
	def __init__(self):
		print("Module Utils....")

	def raise_timeout(self, signum, frame):
		print("Msg error!!!")
		raise Exception("End of time")

	@contextmanager
	def time_out(self, time):
		signal.signal(signal.SIGALRM, self.raise_timeout)
		signal.alarm(time)

		try:
			yield
		except Exception:
			print("Time out")
		finally:
			signal.signal(signal.SIGALRM, signal.SIG_IGN)


def main():
	u = Utils()

	with u.time_out(10):
		while(True):
			time.sleep(1)
			print("Hello!")
	
if __name__ == '__main__':
	main()
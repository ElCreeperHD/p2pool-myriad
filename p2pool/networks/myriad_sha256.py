from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other
PARENT = networks.nets['myriad_sha256']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//15 # shares
REAL_CHAIN_LENGTH = 24*60*60//15 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 60 # blocks
IDENTIFIER = 'fc70135c700a00ee'.decode('hex')
PREFIX = '9472ef181e88efcb'.decode('hex')
P2P_PORT = 5588
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 5589
BOOTSTRAP_ADDRS = 'nz.nutty.one'.split(' ')
VERSION_CHECK = lambda v: None if 90216 <= v else 'Myriad version too old. Upgrade to 0.9.2.16 or newer!'
ALGORITHM = 'SHA256'

from copier import copyserver
import config

copyserver(token=config.token, new_server="created_server_name", prefix=config.prefix)
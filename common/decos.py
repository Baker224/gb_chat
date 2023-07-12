import sys
import gb_chat.log.server_log_config
import gb_chat.log.client_log_config
import logging
import socket

if sys.argv[0].find('client') == -1:
    logger = logging.getLogger('servers')
else:
    logger = logging.getLogger('client')


def log(func_to_log):

    def log_saver(*args, **kwargs):
        logger.debug(
            f'Была вызвана функция {func_to_log.__name__} c параметрами {args} , {kwargs}. Вызов из модуля {func_to_log.__module__}')
        ret = func_to_log(*args, **kwargs)
        return ret

    return log_saver


def login_required(func):

    def checker(*args, **kwargs):
        from gb_chat.server.core import MessageProcessor
        from gb_chat.common.variables import ACTION, PRESENCE
        if isinstance(args[0], MessageProcessor):
            found = False
            for arg in args:
                if isinstance(arg, socket.socket):
                    for client in args[0].names:
                        if args[0].names[client] == arg:
                            found = True
            for arg in args:
                if isinstance(arg, dict):
                    if ACTION in arg and arg[ACTION] == PRESENCE:
                        found = True
            if not found:
                raise TypeError
        return func(*args, **kwargs)

    return checker


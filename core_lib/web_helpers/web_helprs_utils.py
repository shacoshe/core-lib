import enum


class WebHelpersUtils(object):

    server_type = None

    class ServerType(enum.Enum):
        FLASK = 'flask'
        DJANGO = 'django'

    @staticmethod
    def init(server_type):
        WebHelpersUtils.server_type = WebHelpersUtils.ServerType[server_type]

    @staticmethod
    def get_server_type():
        if not WebHelpersUtils.server_type:
            raise ValueError('WebHelpersUtils never initialized')
        return WebHelpersUtils.server_type

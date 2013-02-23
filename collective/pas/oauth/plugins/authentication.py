from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin

class AuthenticationPlugin(BasePlugin):
    """ Map credentials to a user ID.
    """
    security = ClassSecurityInfo()

    security.declarePrivate('authenticateCredentials')
    def authenticateCredentials(self, credentials):

        """ credentials -> (userid, login)

        o 'credentials' will be a mapping, as returned by IExtractionPlugin.

        o Return a  tuple consisting of user ID (which may be different
          from the login name) and login

        o If the credentials cannot be authenticated, return None.
        """
        user_id = ''
        user_login = ''

        #add your code here
        if credentials.get('src', None) != self.getId():
            return
        if ('userid' in credentials and 'userlogin' in credentials):
            return (credentials['userlogin'] , credentials['useremail'],)
        else:
            return None

        raise Exception('Credentials:',credentials)
        return (user_id, user_login)
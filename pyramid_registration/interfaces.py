from zope.interface import Interface

class IRegistrationBackend(Interface):

    def __init__(self, config, settings):
        """ Must pass in configurator and settings objects

        ``config``
        An instance of :class:`pyramid.config.Configurator`

        ``settings``
        An instance of :class:`pyramid.settings.Settings`
        """

    def add_user(self, struct):
        """ Add a new user to the registration system. Adding a user creates an
        account entry in the storage backend and issues an access token for it,
        but does not activate the access token. Access token must be explicitly
        activated by activate() method. Return value is access token issued for this
        account.

        ``struct``
        User structure to store. It is up to the backend implementation to
        validate this structure. However, it is probably safe to assume it
        supports keys username, password and email.
        """

    def activate(self, token):
        """ Mark an already-issued token as activated.

        ``token``
        The token linked to the account to activate. Tokens are issed by the
        issue_access_token() method. """

    def verify_access_token(self, token):
        """ Verify whether access token is associated with a valid account and is not

        ``token``
        The token to verify.

        Returns the user id if valid, None otherwise. """

    def issue_access_token(self, user_id):
        """ Generate a new random access token
        and associate it with the user_id in the database. Returns the token
        issued.

        ``user_id``
        The user_id of the account to issue the token for.
        """

    def simple_login(self, username_or_email, password):
        """ Look up a user by either username or email, if it exists
        check the password against the hashed password in the database.

        If credentials are valid and user exists and is enabled, return a True
        value. Otherwise, return False.

        ``username_or_email``
        A string containing either a username or email for this account.

        ``password``
        A string containing the plaintext password for this account.
        """

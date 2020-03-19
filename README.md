[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# Django Bank Allauth REST
A simple CRUD REST app to manage borrowers, their bank account data (IBAN) and
invoices.

### Getting Started
A simple, out-of-the-box Django website with a "visitor" | `no login required` area
and a members | `login required` area. Supports local email/password as well as easy
configuration for authentication from providers like Google and Facebook.

Simple, old style HTML templates; no webpack or node. Focuses on getting a simple
visitors and members site up quickly.

Using `DRF` (Django Rest Framework) for REST CRUD operations.

### Prerequisites
* Python 3.x


### Pre-Install
If you want users to register and set passwords locally, i.e. never via a provider
like Facebook or Google, run `configure.py` and answer `'n'` to the questions.

If you want to use a provider like Facebook or Google, you'll need to do a little setup
on those sites to get settings you'll need in Django.

#### Configure Facebook Login
Follow these instructions if you want to use Facebook as an authentication provider.
Skip otherwise.

Sarah describes this nicely in [her article][2].

Aside from UI changes, the method she described worked well.

1. Go to [facebook-developer-settings].
2. Add app
3. Create a test app (under the above app)
4. Go to Settings > Advanced
5. Do *not* add any server to Server IP Whitelist ([facebook-whitelist-ip-error])
6. Add product "Facebook Login"
7. Enable if not automatically selected: Client OAuth Login, Web OAuth Login
8. Add OAuth redirect URL (in any order):
  `http://127.0.0.1:8000/`
  `http://127.0.0.1:8000/accounts/facebook/`
  `http://127.0.0.1:8000/accounts/facebook/login/callback/`

  Note: If you're loading your site with `localhost:8000` you should use "http://localhost:8000/..."
  above. Whichever you choose, do it consistently and you should be ok.

Note: The "app secret" and "client id" are a bit confusing with Facebook.
You want to record the "Facebook App Secret" and the "Facebook App ID". The latter
"Facebook App ID" becomes the "client ID" from a Django Allauth perspective.

#### Configure Google Login
Follow these instructions if you want to use Google as an authentication provider.
Skip this section otherwise.

To set up Google, follow the [Google oauth instructions][3] or [this help answer][4]
which is basically:

1. Go to https://console.developers.google.com/
2. Create a new app
3. Make sure that app is selected (next to the "Google APIs" Logo in the top-left)
4. In the left navigation rail under "APIs and Services", click "Credentials"
5. Create new oauth client ID
   You will need to specify some "consent screen details". You can skip most
   of the fields.
6. For Authorized Javascript Origins, add: http://127.0.0.1:8000
7. For Authorized Redirect URIs, add: http://127.0.0.1:8000/accounts/google/login/callback/
8. Click "Create"
9. Copy the "client ID" and "client secret" strings and keep each handy - you'll need them shortly.

Reminder: if you're loading your site at `localhost:8000` then you'll need to set the
URIs above to `http://localhost:8000/...` etc. I recommend not doing that. Instead, just
load your local site as http://127.0.0.1:8000/

#### Configure authentication with other providers
The django-allauth library covers [many others providers][allauth-providers].


### Installing
0. Clone the repo

    ```bash
    $ git clone https://github.com/serhatteker/django-bank-allauth-rest.git
    ```

1. Create a `virtualenv` and install `requirements`.

    ```bash
    $ virtualenv -p python3 .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    ```

2. Generate the initial settings:

      ```bash
      $ python configure.py
      ```

   Follow the prompts. This will generate the initial `config/settings.py`

3. Set up the initial migrations:

   A specific `makemigrations` is needed for the `auth_user` table:

    ```bash
    $ python manage.py makemigrations allauthdemo_auth
    ```

4. Build the database schema:

    ```bash
    $ python manage.py migrate
    ```

5. Create a superuser:

        $ python manage.py createsuperuser

   _Tip_: Do _NOT_ enter the same email address that you'll connect via Google/Facebook with.
   In development I use a made up address like "me@admin.test".

6. Add the social providers:

   Run this for each provider you want to include.

    ```bash
    $ python manage.py set_auth_provider google GOOGLE_CLIENT_ID GOOGLE_SECRET_ID
    saved: Google (...)
    ```

    ```bash
    $ python manage.py set_auth_provider facebook FACEBOOK_CLIENT_ID FACEBOOK_SECRET_ID
    saved: Facebook (...)
    ```

   This essentially runs SQL like:

    ```sql
    DELETE FROM socialaccount_socialapp WHERE provider='google';
    INSERT INTO socialaccount_socialapp (provider, name, secret, client_id, `key`)
    VALUES ("google", "Google", "SECRET", "CLIENT", '');
    INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (
      (SELECT id FROM socialaccount_socialapp WHERE provider='google'),1);
    ```

8. Check it's working:

    ```bash
    $ python manage.py runserver
    ```

   Load the site at http://127.0.0.1:8000. You should see a landing page. Click
   "Join" or "Login".


9. Log into admin and change the default site:

   Go to http://127.0.0.1:8000/admin/sites/site/ - you may need to log out, then log back in as the
   superuser you created above.

   You don't technically have to rename the site but the default "example.com" isn't very useful.
   In development I change the domain to `127.0.0.1` and the name to `<project name> (Dev)`.


## Authors
* [Serhat Teker](https://github.com/serhatteker)

## Code of Conduct
This repo uses same code as [Django Code of Conduct](https://www.djangoproject.com/conduct/) based on the [Open Code of Conduct](https://github.com/todogroup/opencodeofconduct).


## License
This work is licensed under a BSD 3-Clause "New" or "Revised" License. See the
[LICENSE](./LICENSE) for details.


### Credits
Thanks for:
* [aellerton/demo-allauth-bootstrap]
* [yaseralnajjar/debtor-administrator]


[aellerton/demo-allauth-bootstrap]: https://github.com/aellerton/demo-allauth-bootstrap
[yaseralnajjar/debtor-administrator]: https://github.com/yaseralnajjar/debtor-administrator
[django-allauth]: https://github.com/pennersr/django-allauth
[facebook-developer-settings]: https://developers.facebook.com/
[facebook-whitelist-ip-error]: http://stackoverflow.com/questions/21118089/uncaught-oauthexception-this-ip-cant-make-requests-for-that-application
[allauth-providers]: https://django-allauth.readthedocs.io/en/latest/providers.html
[2]: http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Create_and_configure_a_Facebook_app
[3]: https://developers.google.com/+/web/api/rest/oauth#login-scopes

# Kinde Python SDK

The Kinde Python SDK allows developers to integrate with Composable Commerce APIs using Python native interfaces, models and helpers instead of manually using the HTTP and JSON API.

## Register for Kinde

If you haven’t already got a Kinde account, [register for free here](http://app.kinde.com/register) (no credit card required).

You need a Kinde domain to get started, e.g. `yourapp.kinde.com`.



## Set callback URLs

1. In Kinde, go to **Settings** > **App keys**.
2. Add your callback URLs in the relevant fields. For example:

    - Allowed callback URLs - for example, `https://localhost:8000/callback`
    - Allowed logout redirect URLs - for example, `https://localhost:8000`

3. Select **Save**.

## Add environments

Kinde comes with a production environment, but you can set up other environments if you want to. Note that each environment needs to be set up independently, so you need to use the Environment subdomain in the code block above for those new environments.

## Configure your app

**Environment variables**

The following variables need to be replaced in the code snippets below.

-   `SITE_HOST` - e.g. `"localhost"`
-   `SITE_PORT` - e.g. `"8000"`
-   `SITE_URL` - e.g. `f"http://{SITE_HOST}:{SITE_PORT}"`
-   `KINDE_ISSUER_URL` - your Kinde domain - e.g. `"https://your_kinde_domain.kinde.com"`
-   `KINDE_CALLBACK_URL` - your callback url, make sure this URL is under your allowed callback redirect URLs. - e.g. http://localhost:8000/callback
-   `LOGOUT_REDIRECT_URL` - where you want users to be redirected to after logging out, make sure this URL is under your allowed logout redirect URLs. - e.g. `"/callback"`
-   `CLIENT_ID` - you can find this on the **App keys** page - e.g. `"your_kinde_client_id"`
-   `CLIENT_SECRET` - you can find this on the **App keys** page - e.g. `"your_kinde_client_secret"`
-   `GRANT_TYPE` - one of `GrantType: GrantType.CLIENT_CREDENTIALS`, `GrantType.AUTHORIZATION_CODE`, `GrantType.AUTHORIZATION_CODE_WITH_PKCE`
-   `CODE_VERIFIER` - required only if `GRANT_TYPE == GrantType.AUTHORIZATION_CODE_WITH_PKCE`;
     this code can be generated by e.g:
```python
     from authlib.common.security import generate_token
     CODE_VERIFIER = generate_token(48)
```


## Getting token
**Client Credentials flow**

```python
from kinde_sdk import Configuration
from kinde_sdk.kinde_api_client import GrantType, KindeApiClient

CLIENT_ID = "YOUR_KINDE_CLIENT_ID"
CLIENT_SECRET = "YOUR_KINDE_CLIENT_SECRET"
KINDE_ISSUER_URL = "https://[your_subdomain].kinde.com"
KINDE_CALLBACK_URL = "KINDE_CALLBACK_URL"
GRANT_TYPE = GrantType.CLIENT_CREDENTIALS

configuration = Configuration(host=KINDE_ISSUER_URL)
kinde_client = KindeApiClient(
    configuration=configuration,
    domain=KINDE_ISSUER_URL,
    callback_url=KINDE_CALLBACK_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    grant_type=GRANT_TYPE,
)

kinde_client.fetch_token()
```

**Authorisation Code flow**

```python
from kinde_sdk import Configuration
from kinde_sdk.kinde_api_client import GrantType, KindeApiClient

CLIENT_ID = "YOUR_KINDE_CLIENT_ID"
CLIENT_SECRET = "YOUR_KINDE_CLIENT_SECRET"
KINDE_ISSUER_URL = "https://[your_subdomain].kinde.com"
KINDE_CALLBACK_URL = "KINDE_CALLBACK_URL"
GRANT_TYPE = GrantType.AUTHORIZATION_CODE

configuration = Configuration(host=KINDE_ISSUER_URL)
kinde_client = KindeApiClient(
    configuration=configuration,
    domain=KINDE_ISSUER_URL,
    callback_url=KINDE_CALLBACK_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    grant_type=GRANT_TYPE,
)
```
*Login or register*<br />
The Kinde client provides methods for an easy to implement login/register flow.
These methods return the authorization URL to the authorization server.
You need to redirect the user to this URL to initiate the OAuth2 login/register flow.
```python
kinde_client.get_login_url()
kinde_client.get_register_url()
```
*Handle redirect and fetch token*<br />
The authorization server will redirect you back to your site (`authorization_response`). Use it as parameter to fetch token.
```python
kinde_client.fetch_token(authorization_response=authorization_response)
```
*Logout*<br />
This is implemented in much the same way as logging in or registering.<br />
The below method removes the token from the client and returns URL to the authorization server to log out.<br />
Parameter "redirect_to" - URL to your site where redirect from the authorization server after logging out.
```python
kinde_client.logout(redirect_to=redirect_to)
```

**Authorisation Code with PKCE flow**

This flow is similar to Authorisation Code, but you need CODE_VERIFIER. This code can be generated by e.g:
```python
from authlib.common.security import generate_token
CODE_VERIFIER = generate_token(48)
```

```python
from kinde_sdk import Configuration
from kinde_sdk.kinde_api_client import GrantType, KindeApiClient

CLIENT_ID = "YOUR_KINDE_CLIENT_ID"
CLIENT_SECRET = "YOUR_KINDE_CLIENT_SECRET"
KINDE_ISSUER_URL = "https://[your_subdomain].kinde.com"
KINDE_CALLBACK_URL = "KINDE_CALLBACK_URL"
GRANT_TYPE = GrantType.AUTHORIZATION_CODE_WITH_PKCE
CODE_VERIFIER = "CODE_VERIFIER"

configuration = Configuration(host=KINDE_ISSUER_URL)
kinde_client = KindeApiClient(
    configuration=configuration,
    domain=KINDE_ISSUER_URL,
    callback_url=KINDE_CALLBACK_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    grant_type=GRANT_TYPE,
    code_verifier=CODE_VERIFIER,
)
```
*Login or register*<br />
The Kinde client provides methods for an easy to implement login/register flow.
These methods return the authorization URL to the authorization server.
You need to redirect the user to this URL to initiate the OAuth2 login/register flow.
```python
kinde_client.get_login_url()
kinde_client.get_register_url()
```
*Handle redirect and fetch token*<br />
The authorization server will redirect you back to your site (`authorization_response`). Use it as parameter to fetch token.
```python
kinde_client.fetch_token(authorization_response=authorization_response)
```
*Logout*<br />
This is implemented in much the same way as logging in or registering.<br />
The below method removes the token from the client and returns URL to the authorization server to log out.<br />
Parameter "redirect_to" - URL to your site where redirect from the authorization server after logging out.
```python
kinde_client.logout(redirect_to=redirect_to)
```

## Getting user details

```python
kinde_client.get_user_details()
```
Result:
```python
{
  id: id_token.sub,
  given_name: id_token.given_name,
  family_name: id_token.family_name
  email: id_token.email
}
```

## Getting claims

We have provided a helper to grab any claim from your id or access tokens. The helper defaults to access tokens.
```python
kinde_client.get_claim("aud")
# ["api.stakesocial.com/v1"]

kinde_client.get_claim("given_name", "id_token")
# "David"
```

## Get user information from API
```python
from kinde_sdk import ApiException
from kinde_sdk.api import o_auth_api

api_instance = o_auth_api.OAuthApi(kinde_client)
try:
    # Returns the details of the currently logged in user
    api_response = api_instance.get_user()
    print(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->get_user: %s\n" % e)
```

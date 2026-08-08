{%- assign app = site.data.apps[include.app] -%}
*Effective date: {{ app.effective | date: "%B %-d, %Y" }} · Applies to **{{ app.name }}** (`{{ app.bundle_id }}`{% if app.platforms %}, {{ app.platforms | join: " and " }}{% endif %})*

繁體中文版本：[{{ app.name }} 隱私權政策]({{ include.zh_url }})

## The short version

{{ app.name }} has no accounts and asks for no personal information.{% if app.local_data %} Your bookmarks and reading history stay on your phone — I have no way to see them.{% endif %} The app sends anonymous usage and crash statistics to Google's Firebase so I can tell which articles get read and fix what breaks.{% if app.ads == false %} There are no ads{% if app.purchases == false %} and nothing to buy{% endif %}.{% endif %} I do not sell data, and I do not track you across other companies' apps or websites.

## Who is responsible

{{ app.name }} is developed and operated by **Marvin Lin**, an individual developer based in Taiwan. For anything in this policy, write to [{{ site.email }}](mailto:{{ site.email }}).

{% if app.local_data %}## What stays on your device

The following never leaves your phone. It is stored in the app's private storage, I cannot read it, and **uninstalling the app deletes all of it**:

{% for item in app.local_data.en %}- {{ item }}
{% endfor %}
{% endif %}
## What is sent off your device

{% for key in app.services %}{% assign svc = site.data.privacy_services[key] %}### {{ svc.en.name }}

{{ svc.en.data }}

*Why:* {{ svc.en.purpose }}
*Processed by:* {{ svc.provider }} — see their [privacy information]({{ svc.provider_policy }}).

{% endfor %}{% if app.ad_id %}On Android, the collection above can include the Google Advertising ID. I do not use it to show or target advertising; it arrives as part of the standard analytics package. You can reset or delete it at any time in **Settings → Privacy → Ads** on your device.

{% endif %}{% if app.content_api %}### Content downloaded from my own site

The app downloads articles, images, and video listings from `{{ app.content_api }}`. These are public files that need no sign-in. The request contains no information about you beyond what any web request necessarily includes (such as your IP address, which my hosting provider processes to deliver the file).

{% endif %}{% if app.embeds %}## Third-party content inside the app

{% for key in app.embeds %}{% assign svc = site.data.privacy_services[key] %}**{{ svc.en.name }}.** {{ svc.en.data }} {{ svc.provider }}'s own [privacy policy]({{ svc.provider_policy }}) governs that activity.

{% endfor %}{% endif %}## What the app does not do

- {% if app.account == false %}It has no sign-up, no login, and no user accounts.{% else %}Account details are described above.{% endif %}
- It never asks for your name, email address, phone number, or payment details.
- It does not request access to your location, contacts, photos, camera, microphone, or files.
- It does not sell or rent data to anyone, and it carries no third-party advertising SDKs.
- It does not track you across apps or websites owned by other companies.

## Children

{{ app.name }} is not directed at children under 13, and I do not knowingly collect information from them.

## How long data is kept, and how to get rid of it

- **On your device:** uninstall the app. Everything it stored locally goes with it.
- **Analytics and crash data at Google:** retained according to Firebase's retention settings, currently the default period, and held in anonymous form.
- **Want it removed sooner?** Email [{{ site.email }}](mailto:{{ site.email }}) and I will delete what can be identified. Because the analytics data is not tied to your name or account, please include the approximate dates and device model so it can be located.

Depending on where you live, you may have rights to access, correct, or erase personal data, or to object to its processing. The same email address is the way to exercise them.

## Changes to this policy

If the app starts collecting something new, this page is updated before that version ships, and the effective date at the top changes. Material changes will also be noted in the app's release notes.

## Contact

Marvin Lin — [{{ site.email }}](mailto:{{ site.email }})
{% if app.stores.play %}
[{{ app.name }} on Google Play]({{ app.stores.play }})
{%- endif %}

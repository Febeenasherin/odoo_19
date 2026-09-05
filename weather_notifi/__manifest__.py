{
    "name": "Weather notification",
    "version": "19.0.1.0.0",
    "summary": "Systray dropdown showing your last 20 opened records across all models & User history tab",
    "description": """
Track and quickly reopen your recently visited records in Odoo 19.

Key Features:
-------------
* Top Bar Systray History Dropdown showing the last 20 opened records.
* 1-Click Navigation back to any opened record form view across all models.
* User Profile History Tab on User form views positioned right after the Security tab.
* Server-side tracking per user, auto-upserted and pruned to 20 records.
* 1-Click Clear History option to reset viewing history anytime.
    """,
    "category": "Productivity",
    "author": "Micra Digital",
    "website": "https://www.micra.digital",
    "license": "OPL-1",
    "images": ["static/description/banner.png"],
    "depends": ["base", "web"],
    "data": [
        # "security/ir.model.access.csv",
        # "security/ir_recent_record_rule.xml",
        # "views/res_users_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # "micra_recently_viewed_basic/static/src/css/recently_viewed.css",
            "weather_notifi/static/src/xml/recently_viewed_systray.xml",
            "weather_notifi/static/src/js/recently_viewed_systray.js",
            # "micra_recently_viewed_basic/static/src/js/form_controller_patch.js",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
}

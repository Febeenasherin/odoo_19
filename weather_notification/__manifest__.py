
{
    'name': "Weather Notification",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Notification',
    'summary': 'weather notification',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base','sale_management','purchase','web'],
    # 'data':[
    #
    #         ],
    'assets': {
            'web.assets_backend': [

                # "weather_notification/statics/src/xml/systray_icon.xml",
                # "weather_notification/statics/src/js/systray_icon.js",
        ],
    },
}

from django.apps import apps


def app_nav_templates(request):

    nav_templates = []
    for app in apps.get_app_configs():
        if hasattr(app, 'nav_template'):
            nav_templates.append(app.nav_template)
    return {'nav_templates': sorted(nav_templates)}

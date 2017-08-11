import sys,os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","CrazyEye.settings")
    import django
    django.setup()#手动注册Django所有的APP
    from audit.backend import user_interactive
    obj = user_interactive.UserShell(sys.argv)
    obj.start()
def main():
    print("Starting wrapper...")
    import re
    import sys
    from api.assistant.__main__ import main
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
    return "Started api.assistant.__main__.main"
